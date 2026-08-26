# Eldan localization

**Thesis.** A fixed balanced cut cannot be identified too quickly under stochastic localization.

## Active nodes

| node | role |
|---|---|
| `q:upgrade` | upgrade directional occupation control to trace scale for all balanced cuts |
| `q:weighted` | propagate perimeter excess with the required covariance weight |
| `q:stein-weighted` | obtain the stable weighted Stein trace input |
| `q:taming` | control covariance along near-worst measures |
| `q:splitting` | connect small boundary curvature to quantitative splitting |
| `q:alignment` | resolve the incident-high product-cut model |

Detailed deliverables are in [`../gating.md`](../gating.md); exact statements, dependencies, and
`bounded_by` edges are in [`../ledger.yaml`](../ledger.yaml).

## Main fence

The route must overcome high-rank occupation and covariance/excess alignment. Projection-only,
slice-wise absolute-scale, crude-bootstrap, and single-coordinate arguments are limited by the
applicable nodes in [`../obstructions.md`](../obstructions.md).
