# Moment-map spectral occupation

**Thesis.** Follow a normalized first eigenfunction through stochastic localization while
preserving its orientation in the posterior covariance tensor.

## Active nodes

| node | role |
|---|---|
| `q:mm-spectral-occupation` | absorb the tensor source over universal time |
| `prop:spectral-sufficiency` | convert the occupation estimate into a dimension-free gap |

Detailed deliverables are in [`../gating.md`](../gating.md); exact statements and dependencies
are in [`../ledger.yaml`](../ledger.yaml).

## Main fence

The whitened tensor estimate must be unwhitened without losing alignment with the covariance
process. A global covariance-norm estimate alone does not close the route.
