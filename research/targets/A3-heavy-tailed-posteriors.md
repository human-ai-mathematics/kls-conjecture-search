# A3 — Heavy-tailed posteriors beyond classical LSI

- **Ledger:** `conj:a3-dependent` (live replacement), `conj:a3` (refuted tombstone), `thm:a3-product`, `thm:a3-block-gibbs`, `prop:a3-horseshoe`, `prop:a3-hierarchical-prior` (+ `q:a3-*`) · **Manuscript:** `A3-heavy-tailed-posteriors.tex` (`sec:a3`)
- **Status:** the marginal-only target is refuted by a certified fixed-marginal obstruction; the sharp horseshoe and abstract block-Gibbs results also have standalone agent-reviewed solutions; the dependence-aware target and remaining analytic drafts stay open · **Evidence:** none · **Calibration anchor:** `thm:a3-student` (sharp, imported)
- **Audits:** [`2026-08-21-a3-weighted-pi-audit.md`](../explorations/2026-08-21-a3-weighted-pi-audit.md), [`2026-08-21-a3-independent-agent-audit.md`](../reviews/2026-08-21-a3-independent-agent-audit.md), [`2026-08-22-a3-marginals-independent-audit.md`](../reviews/2026-08-22-a3-marginals-independent-audit.md)
- **Resolved proof cycle:** [`2026-08-21-a3-horseshoe-gap-block-gibbs.md`](../explorations/2026-08-21-a3-horseshoe-gap-block-gibbs.md) · **Solutions:** [`prop:a3-horseshoe`](../../solutions/prop-a3-horseshoe.tex), [`thm:a3-block-gibbs`](../../solutions/thm-a3-block-gibbs.tex), [`obs:marginals-not-joint`](../../solutions/obs-marginals-not-joint.tex)

## Retired marginal-only target and surviving obstruction

The original `conj:a3` is a retained refuted tombstone. Polynomial coordinate tails and the one-dimensional Hardy constants of the coordinate
marginals do **not** control a non-product joint Poincaré constant. The certified proposition gives an
explicit three-dimensional copula that keeps all three standard-Cauchy marginals fixed while
creating an arbitrarily small bottleneck. Moreover, if `pi` denotes the
joint law of coefficients and scales, the displayed Dirichlet form differentiates only in the
coefficient coordinates and is zero on nonconstant functions of the scales.

The counterexample deliberately claims only a positive-a.e., piecewise-smooth density, not a
smooth one. In copula coordinates its two high-density octants touch at one point. A degree-zero
angular test is constant with opposite signs on those octants and has
`|grad phi(u)| = O(|u-u_0|^-1)`, which lies in `H^1` exactly from dimension three onward. Its
gradient is supported in the `epsilon`-density mixed octants. After the Cauchy CDF transform,
`(1+x^2)p(x)^2 <= pi^-2`, so the weighted energy is `O(epsilon)` while the variance stays bounded
below. Thus the joint constant is at least `c/epsilon`; no unproved smoothing step is used.

The safe split is:

1. **Product analytic proof draft (pending repository certification).** If
   `pi = tensor_j mu_j`, and `B_j = max(B_{j,+},B_{j,-})` is the larger of the two one-sided
   weighted Hardy quantities for `(mu_j,a_j)`, then
   `Var_pi(f) <= 4 max_j B_j int sum_j a_j |d_j f|^2 dpi`.
2. **Block-Gibbs theorem.** If `gamma_blk` is the block conditional-variance gap and
   the conditional block constants are at most `C_i`, then the joint constant is at most
   `max_i C_i/gamma_blk`. For two blocks, `gamma_blk=1-rho_max`, with `rho_max` the HGR maximal
   correlation.
3. **Dependent posterior theorem (open).** Add an explicit dependence hypothesis or prove a
   two-scale inequality in a fully specified joint metric. Marginal tails alone cannot do this.

## Exact model calibration and the correct tail-index statement

Write `alpha = 2 beta - d` for the radial tail index of
`mu_beta(dx) proportional (1+|x|^2)^(-beta) dx`. Huguet's sharp gap is:

- in `d=1`, `lambda = alpha^2/4` for `0<alpha<=2`, and
  `lambda = alpha-1` for `alpha>=2`;
- in `d>=2`, `lambda = alpha^2/4` for `0<alpha<=4`,
  `lambda = 2 alpha-4` for `4<=alpha<=d+2`, and
  `lambda = alpha+d-2` for `alpha>=d+2`.

Thus `C_w = 4/alpha^2` is exact only in the near-integrability branch. For lighter polynomial
tails the other spectral branches take over. More generally, if
`p(x) ~ c x^(-1-alpha)L(x)` and `a(x) ~ x^2`, Karamata's theorem gives only the tail limit
`tail(x) int^x dt/(a(t)p(t)) -> 1/alpha^2`. The full Hardy supremum can be much larger because
of a bulk bottleneck. The defensible asymptotic is `C_w = Theta(alpha^-2)` as `alpha -> 0`
only for a family with uniform bulk control.

For standard multivariate Student `t_nu`, `alpha=nu`. With radial normalized metric
`(1+x^T Sigma^{-1}x/nu) Sigma`, the sharp constant is `nu/lambda_{(nu+d)/2,d}`. Independent
Student coordinates instead use the tensorized one-dimensional constants.

Weighted LSI is a different, stronger-weight statement: Bobkov--Ledoux prove for generalized
Cauchy `nu_beta` that, when `beta >= (d+1)/2` and `beta>1`,
`Ent(g^2) <= (beta-1)^-1 int |grad g|^2(1+|x|^2)^2 dnu_beta`. It neither uses the quadratic
weighted-PI metric nor covers the one-dimensional Cauchy/horseshoe boundary.

**Citation corrected in the shared bibliography.** The sharp source is Baptiste Huguet,
*Poincaré inequalities and integrated curvature-dimension criterion for generalised Cauchy and
convex measures*, arXiv:2302.02684v2 (2024); the former arXiv:2403.07393 entry was unrelated.

## Horseshoe: corrected normalization and sharper subtarget

The standard hierarchy is
`theta | lambda,tau ~ N(0,tau^2 lambda^2)`, `lambda ~ C+(0,1)`. Its exact marginal is

`h_tau(x) = [pi sqrt(2pi) tau]^-1 exp(a) E1(a)`, `a=x^2/(2tau^2)`.

The logarithmic expression used by the historical `finum` run was a two-sided proxy, not this
density. For the correct one-sided Hardy quantity

`B_HS(tau) = sup_{r>0} P(theta>=r) int_0^r dt/((tau^2+t^2)h_tau(t))`,

scaling `x=tau y` proves exactly
`B_HS(tau)=B_HS(1)` and `C_HS(tau)=C_HS(1)`. Hence “sharp rate in tau” is not open. The
historical formula used `P(|theta|>=r)=2P(theta>=r)` with the one-sided bracket; the manuscript
and implementation now use the consistent one-sided convention.

The intrinsic change of variables `y=asinh(x/tau)` gives the independently agent-reviewed exact
answer `C_HS=4`; the standalone proof is [`solutions/prop-a3-horseshoe.tex`](../../solutions/prop-a3-horseshoe.tex). Put
`H(a)=exp(a)E1(a)=int_0^infinity exp(-t)/(a+t)dt`. With
`N=a^2+5a+2` and `Q=a(a^2+6a+6)`, the exact positive-remainder identity

`N-QH(a)=2 int_0^infinity exp(-t)t^3/(a+t)^3 dt > 0`

proves `H(a)<N/Q`. In intrinsic coordinates this yields
`W'(y)>=tanh(y/2)` for `W=-log q`. The odd half-line supersolution
`g(y)=sinh(y/2)` then gives spectral bottom at least `1/4`. The logarithmic pole has
`q(y)~log(1/y)`, so both `q` and `1/q` are locally integrable and the ground-state boundary term
vanishes like `y log(1/y)` on a smooth odd form core. Form closure then gives the odd inequality.
The same trace-zero estimate controls the even sector directly: for an even half-line function
with zero mean, `h=f-f(0)` has Dirichlet trace, unchanged energy, and no smaller squared norm.
Parity therefore gives the full lower gap without Sturm interlacing. Increasingly wide tail
cutoffs of `exp(y/2)`, corrected by their negligible mean, give the reverse bound.

Directional quadrature still gives `B_HS(1) approximately 1.012444`, so the generic Hardy upper
bound is about `4.04978`; it is not sharp here. Intrinsic-coordinate FEM increases toward `4` as
the domain grows. These diagnostics are not claim validation: the exact conclusion
rests on the analytic solution, not on finite-domain numerics. The remaining horseshoe frontier is
stability of the weighted constant under unbounded likelihood tilts.

## Weak Poincaré and dimension

Under regular variation plus the usual one-dimensional capacity regularity, the unweighted weak
Poincaré rate is `beta_WPI(s) = Theta(s^(-2/alpha))` as `s downarrow 0`. This rate is not
dimension-free under products: the elementary tensorization upper bound is
`beta_d(s) <= beta_1(s/d)`, hence of order `d^(2/alpha)s^(-2/alpha)`, and max-coordinate tail
tests give the same order for iid regularly varying factors. Only the **weighted** product metric
has a dimension-free constant.

## Hierarchical-prior analytic proof draft (natural pullback metric)

For the prior, non-centering gives concrete progress. Put
`theta_j = exp(u+v_j) z_j`, with independent standard Gaussians `z_j` and log-half-Cauchy
variables `u,v_j`. Each log-half-Cauchy law has classical Poincaré constant `4`, so product
tensorization and the chain rule yield the following analytic proof draft, pending repository
certification, of the joint inequality with constant `4` and energy

```
sum_j exp(2u+2v_j) |d_{theta_j}f|^2
+ sum_j |d_{v_j}f + theta_j d_{theta_j}f|^2
+ |d_u f + sum_j theta_j d_{theta_j}f|^2.
```

The cross terms are structural; a diagonal coefficient-only weight misses the hierarchical
geometry. If a likelihood ratio is bounded above and below, Holley--Stroock transfers this
inequality with its oscillation factor. General Bayesian likelihoods and coupled/multimodal
posteriors remain open.

The dependence loss now has a precise abstract placeholder. Define

`gamma_blk = inf_f sum_i E Var(f|X_-i) / Var(f)`.

Uniform conditional weighted Poincaré constants `C_i` imply the theorem

`C_joint <= max_i C_i / gamma_blk`.

For two blocks, conditional expectation is orthogonal projection in `L^2_0`; the two-projections
identity gives `gamma_blk=1-rho_max`, where `rho_max` is HGR maximal correlation. This exactly
detects the fixed-marginal counterexample: its dependence gap collapses even though its marginal
Hardy constants do not change. A standalone proof is
[`solutions/thm-a3-block-gibbs.tex`](../../solutions/thm-a3-block-gibbs.tex).

The posterior ladder should be climbed in this order:

1. If `0<m<=L<=M`, density comparison transfers the prior pullback inequality with
   `C_joint<=4M/m`.
2. For horseshoe normal means, integrate out `z_j`. With `w=u+v_j`, the scale likelihood is
   `m_j(w) proportional (sigma_j^2+exp(2w))^-1/2 exp[-y_j^2/(2(sigma_j^2+exp(2w)))]`, and the
   `(u,v)` posterior is `sech(u) product_j sech(v_j)m_j(u+v_j)`. Conditional on `u`, local blocks
   factorize. Prove conditional one-dimensional Hardy bounds and a positive `gamma_blk`, or an
   explicit two-scale score-covariance bound.
3. Only after that model should sparse/dense coupled likelihoods be attempted. Any dimension or
   data loss must remain visible in `gamma_blk` or the score factor.

Metric guardrail from A5: the finite constant above is Euclidean in log-noncentered coordinates
`(z,u,v)` and hence in the corresponding centered pullback metric. Raw-scale noncentering
`(z,tau,lambda)` can still have no classical Poincaré inequality. The map `tau <-> log tau` is
not bi-Lipschitz, so these statements are consistent but must never be conflated.

## Revised subtargets

| subtarget | status | deliverable |
|---|---|---|
| product Hardy theorem | analytic draft; certification pending | state exact assumptions and tensorized `4 max(B_{j,+},B_{j,-})` bound |
| sharp horseshoe | agent-reviewed analytic solution | extend `C_HS=4` to likelihood-tilted horseshoe marginals under assumptions weaker than bounded density ratio |
| regular-variation catalogue | open | separate tail floor `1/alpha^2` from a uniform bulk Hardy bound |
| `q:a3-weak` | open | prove 1D rate and record product `d^(2/alpha)` degradation |
| hierarchical prior | analytic draft; certification pending | formalize the non-centered pullback-metric inequality above |
| block-Gibbs tensorization | agent-reviewed analytic solution | prove positive, data-explicit `gamma_blk` bounds for a specified hierarchical posterior |
| bounded likelihood | analytic draft; certification pending | certify `C_joint<=4M/m` in the pullback metric |
| hierarchical posterior | frontier | verify conditional Hardy and dependence gaps first for horseshoe normal means; no marginal-only claim |

## Numerical contract

`experiments/finum/targets/a3.py` now uses the exact exponential-integral horseshoe density and
a standardized grid, checks scale covariance, and reports the parity-separated odd Barta residual
from the explicit positive certificate. Finite-domain FEM for Cauchy tails converges very slowly
and must not be read as a sharp constant; a stable sub-threshold eigenvalue would require
parity-separated boundary sweeps plus residual/two-sided control. The retired 2026-06-20 proxy
diagnostic is preserved only in the
[`2026-08-21 weighted-PI audit`](../explorations/2026-08-21-a3-weighted-pi-audit.md); it is not
live claim support. All listed computations are directional research diagnostics and possible
refutation aids; they do not validate or certify the analytic certificate or any proof. Rigorous
refutation still requires an analytic argument or exact lower bound.
