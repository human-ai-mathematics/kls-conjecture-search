# KLS route registry

The route-neutral target is `conj:kls` in `modules/kls/00-orientation.tex`: a universal
Poincaré/Cheeger bound for every isotropic log-concave measure. Its ledger bridge to the A-series
is `ab/conj:a1-bis`. The manuscript owns the definition and normalization; the ledger owns its
status.

## Live routes

| route | thesis | active entry points | main fence |
|---|---|---|---|
| [`eldan-localization`](routes/eldan-localization/) | A fixed balanced cut cannot be identified too quickly under stochastic localization. | `q:upgrade`; or `q:weighted` + `q:stein-weighted`; model residue `q:alignment` | high-rank occupation and covariance/excess alignment |
| [`moment-map-spectral`](routes/moment-map-spectral/) | Localize a first eigenfunction and retain the orientation in its posterior covariance tensor. | `q:mm-spectral-occupation`, then `prop:spectral-sufficiency` | unwhitening over universal time |
| [`moment-map-cmh`](routes/moment-map-cmh/) | Bound the canonical moment-Hessian quotient using deterministic moment-map geometry. | `q:cmh-approximation`, `q:mm-invariant-lift`, `q:mm-square-root-commutator`, `conj:gate-zero`, `q:cmh-solenoidal-perturbation` | approximation, commutators, and the solenoidal channel |

`moment-map-cmh` is a sufficient-condition route, not a proved reformulation of KLS. A certified
counterexample to CMH(4) would close that constant/route without refuting `conj:kls`.

## Shared bottleneck

`q:upgrade`, the high-rank part of `q:stein-weighted`, and `q:alignment` all confront occupation
across many directions. `rem:trace-upgrade-unification` in the manuscript records this comparison,
but no equivalence is proved. One owner should compare them; the ledger records only dependencies
actually used in proofs.

The fixed-eigenfunction route also has an alignment problem, while the deterministic CMH route
meets a related operator-to-trace issue at `conj:gate-zero`. These similarities are roadmap facts,
not extra ledger edges.

## Opening a route

1. Add `routes/<slug>/README.md` with a thesis, why existing routes do not subsume it, the first
   precise target, and applicable obstructions.
2. Add the slug to `meta.route_policy.allowed` and a row above.
3. Once a statement is sharp, add it to the single [`ledger.yaml`](ledger.yaml) with explicit
   `route:` and logical `depends_on` edges.
4. Put numerical implementation and status in `experiments/`, not in the route brief.

Do not create a route-local ledger. Route status is prose; claim status is ledger state.
