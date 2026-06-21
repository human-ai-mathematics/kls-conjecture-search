# KLS route registry

Part III is **exploratory**: the KLS conjecture may yield to more than one attack, and an
agent should be free to open a *new* route rather than only fill in the existing one. This
file is the registry. Each route is a directory under [`routes/`](routes/) with its own brief
(and, once it earns one, its own ledger). The facts every route must respect — the target
statement, the universal lower bounds, the refuted counterexamples — live in
[`shared/`](shared/), not in any single route.

## The target (route-agnostic)

Dimension-free Cheeger / Poincaré lower bound for **every** isotropic log-concave measure:
$\inf_n h^\star_n > 0$. Statement, $h^\star$ definition, and the bridge to Part II are in
[`shared/target.md`](shared/target.md). Universal lower bounds and the refuted forms any proof
must respect are in [`shared/lower-bounds.md`](shared/lower-bounds.md).

## Numerics

How numerics gate the routes — each open node mapped to a computable quantity and a
REFUTES/SUPPORTS threshold — is in [`gating.md`](gating.md). The SDE-free bridge signals
(realized $K = C_P/\lambda_{\max}(\mathrm{Cov})$, rank-one non-refutation) are built in
`finum` (`finum run --target kls`); the localization quantities ($\Xi_T$, alignment, weighted
Stein) are built in `finum.localization` (`finum run --target kls-loc`).

## Routes

| slug | thesis (one line) | status | headline | what it'd take to win |
|---|---|---|---|---|
| [`eldan-localization`](routes/eldan-localization/) | Track a fixed cut under Eldan localization; a balanced cut can't be identified too fast | **live** | `thm:intro-all-cut`, `thm:intro-weighted` | discharge `q:upgrade` (Route A) **or** `q:weighted` + `q:stein-weighted` (Route B) |

Status vocabulary: **live** (actively worked, no fatal obstruction) · **stalled** (blocked on
a named input with no current idea) · **refuted** (a route-fatal obstruction was proven) ·
**merged** (folded into another route).

## How to open a new route

1. Create `routes/<slug>/README.md` with: the one-line thesis, why it might beat the existing
   route(s), which `shared/` facts it must respect, and its first concrete sub-goal.
2. Add a row to the table above (status `live`).
3. Keep it **prose-only** at first. Use `finum` to gate it: numerically test the
   route's central hypothesis *before* investing in a proof; if a `shared/lower-bounds.md`
   counterexample kills it, mark the route `refuted` and record why.
4. A route earns its own `ledger.yaml` only when it has enough discharged structure to track
   formally — see the limitation below.

## Limitation: one `kls` ledger for now (deferred)

`check_ledger.py` keys ledgers by `meta.program` in a dict, so a *second* `program: kls`
`ledger.yaml` would silently overwrite the first. Until the checker is extended to **merge**
multiple same-program ledgers (and union their obstruction sibling sets), only one route —
currently `eldan-localization` — carries a ledger; other routes stay prose-only. When a second
route needs formal tracking, do that checker change first.
