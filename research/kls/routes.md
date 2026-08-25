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
cut-specific rank-one obstruction. `finum run --target cmh-gate-zero` computes the Route C
gate-zero ratio and the Dirichlet surplus without Monte Carlo. Determinism alone is not rigor:
closed-form rational one-dimensional values and exact rational Dirichlet Rayleigh witnesses can
rigorously refute `conj:gate-zero`, while floating generalized eigenvalues, FEM, and the present
Galerkin surplus are directional only. Every instance currently carried lies inside an
already-proved class, so non-refutation there is calibration, not support.
`finum.localization` (`finum run --target kls-loc`) currently
provides calibration/source diagnostics only. The separate `finum run --target kls-align`
implements the full incident-high alignment margin for the designated Laplace-product tail union;
its held-out finite-dimensional run is non-refuting, but it does not decide the universal
`q:alignment` node. $\Xi_T$, weighted excess, and weighted Stein verdicts remain unbuilt.

## Routes

| slug | thesis (one line) | status | headline | what it'd take to win |
|---|---|---|---|---|
| [`eldan-localization`](routes/eldan-localization/) | Track a fixed cut under Eldan localization; a balanced cut can't be identified too fast | **live** | `thm:intro-all-cut`, `thm:intro-weighted` | discharge `q:upgrade` (Eldan-A) **or** `q:weighted` + `q:stein-weighted` (Eldan-B) |
| [`moment-map-spectral`](routes/moment-map-spectral/) | Localize a first eigenfunction and use moment-map quadratic control on its whitened posterior tensor | **live (secondary)** | `q:mm-spectral-occupation` (manuscript: `sec:spectral-route`, Group 4) | unwhiten for a universal time without losing tensor/covariance alignment |
| [`moment-map-cmh`](routes/moment-map-cmh/) | Extend constant moment-map multipliers to test-dependent Haar fields through Schur--Piola geometry | **live (primary deterministic)** | `q:cmh-approximation`; `q:mm-square-root-commutator` (construction); `conj:gate-zero`, `q:cmh-solenoidal-perturbation` (tests) | close approximation, prove the lift/all-split reduction and full commutator sum — or decide the headline first via gate zero/full perturbation |

Status vocabulary: **live** (actively worked, no fatal obstruction) · **stalled** (blocked on
a named input with no current idea) · **refuted** (a route-fatal obstruction was proven) ·
**merged** (folded into another route).

**`moment-map-cmh` has two layers (25 August 2026).** The *construction* layer is the Haar/
Schur--Piola/commutator programme; the *normalization* layer fixes the regular-class endpoint and
computes it exactly on the line, on products, and on every log-concave Dirichlet law.
`q:cmh-normalization` is discharged, while `q:cmh-approximation` records the open passage to
arbitrary limits. The headline $\mathrm{CMH}(4)$ is not a proved reformulation of `conj:kls`:
`prop:cmh-hodge` identifies a nonnegative solenoidal channel beyond the affine Poincar\'e channel,
but no separating log-concave measure or strict non-implication theorem is known. A certified CMH
refutation would close this sufficient-condition route without refuting KLS; gate zero and the
full perturbative quotient are therefore high-priority tests.

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
[`ledger.yaml`](ledger.yaml). New cross-route nodes use `route:` metadata; untagged nodes that
predate route metadata default to the Eldan fixed-cut program as recorded in ledger metadata. The colocated obstruction
schema currently contains Eldan-specific mechanism fences; its prose states that scope
explicitly. This design keeps cross-route dependencies and the terminal `conj:kls` node visible
without introducing ambiguous same-program merge semantics.
