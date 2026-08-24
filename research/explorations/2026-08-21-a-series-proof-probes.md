# A1–A5 proof probes — closed reductions and the next narrow frontiers

- **Date:** 2026-08-21
- **Scope:** second exploration cycle after the frontier audit
- **Evidence:** analytic proofs plus deterministic/focused regression guards; no clean run
  artifact and no `numerical-strong` promotion
- **Certification:** twenty-one results now have standalone solutions and independent-agent review;
  unaudited derivations retain their open/draft status

## Certification outcome

The project owner authorized independent-agent review as a proof gate. The persisted reports are
[`A1/A2`](../reviews/2026-08-21-a1-a2-independent-agent-audit.md),
[`A3`](../reviews/2026-08-21-a3-independent-agent-audit.md),
[`A4/A5`](../reviews/2026-08-21-a4-a5-independent-agent-audit.md), and the separate
[`A5 funnel second audit`](../reviews/2026-08-21-a5-funnel-second-agent-audit.md).
They promote exactly the nodes carrying `checked_by: agent` in `research/ledger.yaml`; each points
to a standalone TeX solution. This is recorded honestly as agent certification, not human or Lean
certification.

## Outcome map

| target | strongest certified result | genuinely open frontier |
|---|---|---|
| A1 | factor-one inverse-curvature bound for $mI\preceq\nabla^2U\preceq MI$; explicit mode-leverage geometry/tail certificate; exact fixed-$d$ coefficient when $\eta_n\to0$ | review the separate universal bulk--tail comparison; extend to unbounded Hessians/nonsmooth losses; replace the conservative rowwise certificate at high leverage |
| A2 | vanishing leverage proves the logistic $C_P$ limit; convex Gaussian-average-subquadratic perturbations have exact prior-scale global $C_{\rm LS}=C_{T_2}$ | random spectral stability outside bounded-Hessian logistic; growing dimension; tail/prior classes yielding genuinely Fisher-local global entropy constants |
| A3 | exact horseshoe weighted constant $C_{\rm HS}=4$; dependence loss isolated as $1/\gamma_{\rm blk}$, with $\gamma_{\rm blk}=1-\rho_{\max}$ for two blocks | likelihood-tilted horseshoe constants; conditional Hardy and positive block-gap bounds for a specified global--local posterior |
| A4 | exact localized mean-tilt dual; separate well-specified, misspecified, and optimizer-centred local laws; exact Gaussian calibration | a finite-radius posterior bulk/tail theorem over a coercive variational sublevel; modified transport for heavy tails |
| A5 | exact symmetry-block decomposition and stability; Gaussian crossover/optimal partial noncentring; prior-only partial-Neal no-go | certify the two-well Hardy bridge; prove a smooth statistical multiwell capacity theorem; develop likelihood-dependent partial noncentring in blocks/hierarchies |

## 1. A1 and A2 now meet at maximal leverage

Let $\widehat H=\nabla^2U(\hat\theta)$ and suppose each positive likelihood curvature has
log-Lipschitz constant $L_i$. Define

$$
 \alpha_i=L_i\sqrt{x_i^T\widehat H^{-1}x_i},
 \qquad \eta=\max_i\alpha_i,
 \qquad r=\|\widehat H^{1/2}(\theta-\hat\theta)\|.
$$

The segment Hessian comparison gives

$$
 e^{-\eta r}\widehat H\preceq\nabla^2U(\theta)\preceq e^{\eta r}\widehat H
$$

and the radial potential envelopes

$$
 g_-(r;\eta)=\frac{e^{-\eta r}+\eta r-1}{\eta^2},
 \qquad
 g_+(r;\eta)=\frac{e^{\eta r}-\eta r-1}{\eta^2}.
$$

They yield two complementary certificates.

1. For every log-Hessian-Lipschitz GLM, including Poisson, the ellipsoid $r\le R$ supplies
   explicit rowwise curvature floors and a posterior-tail upper bound given by a ratio of radial
   one-dimensional integrals.
2. If also $mI\preceq\nabla^2U\preceq MI$—in particular for finite logistic posteriors—the
   factor-one Bochner theorem gives

   $$
   C_P(\pi)\le K_d(\eta)\lambda_{\max}(\widehat H^{-1}),
   \qquad \eta<1,
   $$

   with $K_d(\eta)\to1$ as $\eta\downarrow0$.

The covariance lower test converges to the same coefficient under the radial envelope. Thus, in
fixed dimension,

$$
 \eta_n\to0,\quad \widehat H_n/n\to I(\theta_0)
 \quad\Longrightarrow\quad
 nC_P(\pi_n)\to\lambda_{\max}(I(\theta_0)^{-1}).
$$

This closes a concrete A1-to-A2 route without global oscillation comparison or a global PL
constant. It does not cover Poisson's unbounded Hessian, $d=d_n\to\infty$, or high-leverage
designs.

### The global entropy tradeoff is now sharper

For a Gaussian prior and finite convex perturbation $L$, completing the square samples
$Y_t\sim N(m+t\Sigma_0u,\Sigma_0)$. If, along one top covariance direction,
$\mathbb E L(Y_t)=o(t^2)$, then the centered log-MGF keeps quadratic coefficient
$\lambda_{\max}(\Sigma_0)/2$. Bakry--Émery and Otto--Villani give the matching upper bound:

$$
 C_{\rm LS}=C_{T_2}=\lambda_{\max}(\Sigma_0).
$$

Finite logistic loss is a corollary. Moreover, a Gaussian prior whose precision is $o(n)$ cannot
make these global constants $O(1/n)$; a prior that does make them $O(1/n)$ contributes order-$n$
local information. This removes “shrink the prior” as a way to preserve the ordinary Fisher target
and simultaneously repair the global logistic LSI.

## 2. A3 has one exact spectral model and one exact dependence parameter

For the horseshoe marginal, write $H(a)=e^aE_1(a)$. The key global remainder is

$$
 (a^2+5a+2)-a(a^2+6a+6)H(a)
 =2\int_0^\infty\frac{e^{-t}t^3}{(a+t)^3}\,dt>0.
$$

After $x=\sinh y$, this implies $W'(y)\ge\tanh(y/2)$. The positive odd-sector test
$g(y)=\sinh(y/2)$ gives a trace-zero half-line lower bound $1/4$. The logarithmic pole is handled
in the weighted form because $q,1/q\in L^1_{\rm loc}$. For a mean-zero even half-line function,
subtracting its trace preserves energy and increases its squared norm, so the same Dirichlet bound
controls the even sector directly. Mean-corrected tail cutoffs give the reverse inequality. The
independently reviewed proof therefore gives

$$
 C_{\rm HS}(\tau)=4
$$

for the weight $\tau^2+x^2$. This is now a solved, sharp one-dimensional calibration reusable
across robust-Bayes examples.

For dependence, define

$$
 \gamma_{\rm blk}
 =\inf_f\frac{\sum_i\mathbb E\operatorname{Var}(f\mid X_{-i})}
                 {\operatorname{Var}(f)}.
$$

Conditional weighted inequalities give $C_{\rm joint}\le\max_iC_i/\gamma_{\rm blk}$. For two
blocks the exact identity is

$$
 \gamma_{\rm blk}=1-\rho_{\max}(X,Y).
$$

The next A3 theorem should therefore name a concrete hierarchy and separately prove uniform
conditional Hardy constants and a nontrivial maximal-correlation/block-gap bound. Marginal tail
indices alone have been decisively removed from the theorem shape.

## 3. A4 local geometry depends on what is centred

Let $\delta_{\mathcal Q}=\inf_{q\in\mathcal Q}\mathrm{KL}(q\|\pi)$. Three ratios that were
previously conflated have different leading behavior.

- **Well specified:** if $q_0=\pi$, then the raw localized constant tends to the generalized
  eigenvalue $\lambda_{\max}(F^{-1/2}GF^{-1/2})$.
- **Misspecified raw:** if $q_*$ minimizes KL and $\delta_{\mathcal Q}>0$, then the raw constant
  starts at $W_2^2(q_*,\pi)/(2\delta_{\mathcal Q})$ and generically has a $\sqrt\rho$ correction.
- **Optimizer-centred excess:** subtracting both $q_*$ and $\delta_{\mathcal Q}$ restores the
  generalized eigenvalue, but measures optimization error rather than approximation error.

The fixed-covariance Gaussian location family solves all three formulas exactly. Separately, the
unrestricted localized mean constant is an exact one-dimensional tilt optimization in every
direction and approaches $\lambda_{\max}(\operatorname{Cov}\pi)$ as the entropy radius vanishes.

The next proof must be finite-radius and posterior-specific: prove compactness/uniform $P_2$
integrability of the variational sublevel, control transport through a posterior-curvature bulk,
and bound the complement. A tangent expansion alone cannot produce a VB error bar.

## 4. A5 is a transition network plus a metric choice

For equal-depth orbit wells with pair communication heights $H_{ij}$, the relevant raw-gap
exponent is

$$
 \Gamma_{\rm conn}
 =\max_{\varnothing\ne A\subsetneq\mathcal W}
   \min_{i\in A,j\notin A}H_{ij},
$$

the threshold at which the whole orbit graph connects. The easiest pairwise move is insufficient
unless its edges already connect the orbit. A two-Gaussian-well sequence has the analytic
calibration

$$
 \frac1n\log C_P(\text{raw})\to\frac{a^2}{2\sigma^2},
 \qquad nC_P(\text{quotient})\to\sigma^2.
$$

The certified block-stability theorem shows that invariant density-ratio perturbations preserve
each invariant/non-invariant gap within
$e^{\pm\varepsilon}$, so the raw exponent transfers under $o(n)$ oscillation and the quotient
leading coefficient under $o(1)$ oscillation. This bridge is intentionally much stronger than
TV-BvM.

For scalar Gaussian partial noncentring $z_\alpha=\theta-\alpha u$, fixed determinant reduces both
$C_P$ and the Gaussian condition number to trace minimization:

$$
 \alpha_*=\frac1{1+rB}.
$$

In contrast, the second-agent-certified prior-only Neal theorem shows that
$z_\alpha=e^{(1-\alpha)u}z$ for every $\alpha<1$ retains lognormal-type tails and infinite
Euclidean $C_P$; only full noncentring is finite. Hence local
Gaussian conditioning and global nonlinear tail regularity must be treated as separate design
criteria.

## Recommended next cycle

1. **Extend the certified cores:** A1 beyond bounded Hessians, A3 from the prior to a specified
   posterior, and A4 from tangent asymptotics to a finite-radius bulk--tail theorem.
2. **A1 high-leverage experiment:** optimize $R$ in the full bulk-tail certificate and compare
   rowwise with a spectral semidefinite floor on separable and wide designs.
3. **A3 concrete posterior:** two-block horseshoe normal means; prove conditional one-dimensional
   Hardy bounds and estimate/prove an HGR contraction.
4. **A4 finite-radius theorem:** begin with a fixed-covariance Gaussian family against a
   bounded-Hessian logistic posterior; state compactness and tail remainder explicitly.
5. **A5 smooth bridge:** replace the exact Gaussian-mixture sequence by a smooth finite-group
   statistical likelihood and prove two-sided capacity estimates at logarithmic scale.
6. **Partial noncentring:** lift $\alpha_*$ to commuting Gaussian blocks, then test which likelihood
   tail contracts turn the partial-Neal discontinuity into a finite interior phase.

## Numerical/provenance verdict

Focused regressions guard the new algebra and exact calibrations, but no clean provenance-stamped
JSONL was produced. The computations remain regression checks; proof promotion comes from the
standalone arguments and persisted independent-agent audits above.

## 2026-08-22 cleanup addendum

The positive-intermediate count remains twenty-one. A later cleanup review separately certified
three obstruction nodes: the Gaussian-tail and symmetry obstructions as direct consequences of
their already reviewed base propositions, and the fixed-Cauchy-marginal A3 counterexample through
a new standalone proof audit. See
[`2026-08-22-derived-obstructions-audit.md`](../reviews/2026-08-22-derived-obstructions-audit.md)
and
[`2026-08-22-a3-marginals-independent-audit.md`](../reviews/2026-08-22-a3-marginals-independent-audit.md).
The original A3 marginal-only target is therefore a certified refuted tombstone, while its
dependence-aware replacement remains open.

Terminology correction: the A1 bulk--tail split in the recommended next cycle is an unproved
candidate, not a certificate. Sampled covariance, MCMC, FEM, and finite-grid estimates are also
directional unless supplied with rigorous error bounds.
