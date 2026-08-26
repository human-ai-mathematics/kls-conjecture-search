# Route: moment-map spectral occupation

Status: live, secondary. The exposition of record is `modules/kls/30-spectral-route.tex`; sharpened
claims belong to the central [`../../ledger.yaml`](../../ledger.yaml) with
`route: moment-map-spectral`.

## Thesis

Follow a normalized first eigenfunction through stochastic localization. Let
$g_t=\operatorname{Cov}_{\mu_t}(f,X)$ and let $H_t$ be its posterior covariance tensor. The exact
SDE has source $\|H_t\|_{\mathrm{HS}}^2$ and damping $2g_t^TA_tg_t$. Conditional moment-map
quadratic control bounds the whitened tensor; the open problem is to unwhiten it over universal
time without losing its alignment with $A_t$.

## Active nodes

- `q:mm-spectral-occupation`: prove the absorptive source/damping occupation estimate uniformly
  on regular approximants.
- `prop:spectral-sufficiency`: turn that estimate into a dimension-free spectral gap, including
  terminal variance control and the approximation limit.

The two nodes are separate because the manuscript presently gives a mechanism sketch, not a
certified sufficiency proof.

## Fences

The old full $H^{-1}$ residual is quantitatively KLS-strength and is an endpoint diagnostic, not a
preliminary lemma. Direct unweighting is false on truncated-exponential first eigenfunctions.
Projection-only obstructions from the cut route do not refute this tensor-aware route, but another
global covariance-norm estimate will not close it.

Detailed failed attempts remain in the dated explorations
[`2026-08-20-kls-eigenfunction-localization.md`](../../../explorations/2026-08-20-kls-eigenfunction-localization.md)
and [`2026-08-20-kls-hminus1-models.md`](../../../explorations/2026-08-20-kls-hminus1-models.md).
