# KLS route registry

The route-neutral target is `conj:kls`: a universal Poincaré/Cheeger bound for every isotropic
log-concave measure. Its bridge to the A-series is `a-series/conj:a1-bis`.

| route | thesis | main fence |
|---|---|---|
| [`eldan-localization`](routes/eldan-localization.md) | A balanced cut cannot be identified too quickly under stochastic localization. | high-rank occupation and covariance/excess alignment |
| [`moment-map-spectral`](routes/moment-map-spectral.md) | Preserve eigenfunction tensor orientation through localization. | unwhitening without losing alignment |
| [`moment-map-cmh`](routes/moment-map-cmh.md) | Bound the canonical moment-Hessian quotient. | approximation, commutators, and the solenoidal channel |

Choose a route here, then use [`gating.md`](gating.md) for current deliverables,
[`ledger.yaml`](ledger.yaml) for exact statements and logical state, and
[`obstructions.md`](obstructions.md) for proof-shape fences.

## Shared ownership

`q:upgrade`, the high-rank part of `q:stein-weighted`, and `q:alignment` share one occupation
difficulty. The CMH gate-zero problem is related but not known equivalent. One owner compares
these problems; the ledger records only implications actually proved.
