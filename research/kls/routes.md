# KLS route registry

Part III is **exploratory**: the KLS conjecture may yield to more than one attack, and an
agent should be free to open a *new* route rather than only fill in the existing one. This
file is the registry. Each route is a directory under [`routes/`](routes/) with its own brief.
All sharpened targets enter the single route-spanning [`ledger.yaml`](ledger.yaml) through the
orchestrator. The target statement and genuinely universal lower
bounds live in [`shared/`](shared/); mechanism-specific refutations remain explicitly scoped to
the route that proves them.

## The target (route-agnostic)

Dimension-free Cheeger / Poincaré lower bound for **every** isotropic log-concave measure:
$\inf_n h^\star_n > 0$. Statement, $h^\star$ definition, and the bridge to Part II are in
[`shared/target.md`](shared/target.md). Universal lower bounds and clearly labeled route-scoped
refuted forms are summarized in [`shared/lower-bounds.md`](shared/lower-bounds.md).

## Numerics

How numerics gate the routes — including which open-node observables are not yet implemented —
is in [`gating.md`](gating.md). The SDE-free finite-battery bridge signal and Gaussian rank-one
normalization sanity check are built in `finum` (`finum run --target kls`); they do not test the
cut-specific rank-one obstruction. `finum.localization` (`finum run --target kls-loc`) currently
provides calibration/source diagnostics only. The separate `finum run --target kls-align`
implements the full incident-high alignment margin for the designated Laplace-product tail union;
its held-out finite-dimensional run is non-refuting, but it does not decide the universal
`q:alignment` node. $\Xi_T$, weighted excess, and weighted Stein verdicts remain unbuilt.

## Routes

| slug | thesis (one line) | status | headline | what it'd take to win |
|---|---|---|---|---|
| [`eldan-localization`](routes/eldan-localization/) | Track a fixed cut under Eldan localization; a balanced cut can't be identified too fast | **live** | `thm:intro-all-cut`, `thm:intro-weighted` | discharge `q:upgrade` (Eldan-A) **or** `q:weighted` + `q:stein-weighted` (Eldan-B) |
| [`moment-map-spectral`](routes/moment-map-spectral/) | Localize a first eigenfunction and use moment-map quadratic control on its whitened posterior tensor | **live (secondary)** | `q:mm-spectral-occupation` | unwhiten for a universal time without losing tensor/covariance alignment |
| [`moment-map-cmh`](routes/moment-map-cmh/) | Extend constant moment-map multipliers to test-dependent Haar fields through Schur--Piola geometry | **live (primary deterministic)** | `q:cmh-normalization`, `q:mm-square-root-commutator` | freeze the endpoint/lift/domains, prove an all-split reduction, control the full commutator sum, and close CMH |

Status vocabulary: **live** (actively worked, no fatal obstruction) · **stalled** (blocked on
a named input with no current idea) · **refuted** (a route-fatal obstruction was proven) ·
**merged** (folded into another route).

## How to open a new route

1. Create `routes/<slug>/README.md` with: the one-line thesis, why it might beat the existing
   route(s), which `shared/` facts it must respect, and its first concrete sub-goal.
2. Add a row to the table above (status `live`).
3. It may begin as prose while its first statement is being made precise. Once it sharpens a
   target, add a `route:`-tagged node to the central [`ledger.yaml`](ledger.yaml) through the
   orchestrator. Use `finum` for sampled/FEM gating; exact analytic probes may be persisted
   directly. If a route-fatal counterexample is certified, mark the route `refuted` and record why.
4. Do not create a route-local ledger. The single route-spanning ledger is the merge barrier.

## One KLS ledger by design

`check_ledger.py` deliberately rejects a second `program: kls` ledger. All route nodes live in
[`ledger.yaml`](ledger.yaml). New cross-route nodes use `route:` metadata; untagged legacy nodes
default to the Eldan fixed-cut program as recorded in ledger metadata. The colocated obstruction
schema currently contains Eldan-specific mechanism fences; its prose states that scope
explicitly. This design keeps cross-route dependencies and the terminal `conj:kls` node visible
without introducing ambiguous same-program merge semantics.
