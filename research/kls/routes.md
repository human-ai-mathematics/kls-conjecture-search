# KLS route registry

The route-neutral target is `conj:kls`: a universal Poincaré/Cheeger bound for every isotropic
log-concave measure. Its bridge to the A-series is `a-series/conj:a1-bis`.

| route | thesis | main fence |
|---|---|---|
| [`eldan-localization`](routes/eldan-localization.md) | A balanced cut cannot be identified too quickly under stochastic localization. | high-rank occupation and covariance/excess alignment |
| [`moment-map-spectral`](routes/moment-map-spectral.md) | Preserve eigenfunction tensor orientation through localization. | unwhitening without losing alignment |
| [`moment-map-cmh`](routes/moment-map-cmh.md) | Bound the canonical moment-Hessian quotient. | uniform CMH control on certified approximants, commutators, and the solenoidal channel |
| [`conditional-fiber-frame`](routes/conditional-fiber-frame.md) | A test-independent isotropic frame of inverse-variance-normalized conditional line resamplings has a universal $L^2$ gap. | construct one frame uniformly over all tests, or decide the all-frame simplex dual |

Choose a route here, then use [`gating.md`](gating.md) for current deliverables,
[`ledger.yaml`](ledger.yaml) for exact statements and logical state, and
[`obstructions.md`](obstructions.md) for proof-shape fences.

## Registered route probes

These are parked candidates, not live ledger routes and not members of the allowed `route:`
vocabulary.

- `cone-boundary-spectral`: a universal tangential Poincar\'e gap for normalized cone measure
  would feed the published Kolesnikov--Milman Hardy boundary bridge. The analytic right-cone
  falsification test survives uniformly, including smooth isotropic roundings; the first open
  wall is a dimension-free multi-facet/product seam-capacity estimate. See the
  [route scout](../explorations/2026-08-27-kls-route-scout-novel-w2n01.md) and
  [cone probe](../explorations/2026-08-27-kls-route-prober-cone-boundary-spectral-w3b01.md).
  No theorem, KLS implication beyond the published conditional bridge, or ledger status is
  asserted here.

## Shared ownership

`q:upgrade`, the high-rank part of `q:stein-weighted`, and `q:alignment` share one occupation
difficulty. The CMH gate-zero problem is related but not known equivalent. One owner compares
these problems; the ledger records only implications actually proved.
