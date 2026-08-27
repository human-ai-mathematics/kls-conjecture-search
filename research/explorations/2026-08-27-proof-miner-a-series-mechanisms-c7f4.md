# A-series proof mining: certified mechanisms, review-excluded drafts, and hidden consequences

**Date:** 2026-08-27
**Role:** `proof-miner`
**Scope:** A1--A5 dossiers, manuscript proofs, knowledge notes, reviews, and archived attempts
**Numerics:** none
**Status discipline:** every proposed strengthening below remains a candidate with `status: open`.
No ledger, manuscript, solution, review, or shared-knowledge file was edited.

## Outcome

The current A-series frontier contains two different kinds of open work that should not be mixed.

1. Five current open nodes already have essentially complete analytic arguments in the manuscript
   or append-only archive and were left open because they were explicitly outside an earlier
   independent review: `prop:a1-bulk-tail`, `thm:a2-target`, `thm:a3-product`,
   `prop:a3-hierarchical-prior`, and `prop:a4-logistic-global`. Their next step is a standalone
   dossier and cold review, not another exploratory derivation.
2. The genuinely open bottlenecks are model verification or new global control: useful A1
   selection at high leverage, weaker-than-global-oscillation A2 spectral stability, a positive
   posterior-specific A3 block gap, finite-radius A4 coercivity/tail control, and the raw A5 Hardy
   or capacity asymptotic.

There is also one source-of-truth defect: the shared-knowledge entry headed
`prop:a1-bulk-tail` states the factor-one bounded-Hessian theorem, which is actually the certified
node `prop:a1-euclidean-harmonic`. This can cause a consumer to treat an open universal Milman
comparison as certified or to attach the wrong hypotheses to the factor-one result.

### Classification map

| finding | classification | present logical status | next action |
|---|---|---|---|
| A1 universal Milman bulk--tail implication | plausible route, proof-ready draft | `prop:a1-bulk-tail` open | `prover`, then `proof-checker` |
| A1 factor-one theorem under an abstract operator-domain contract | plausible route | no node | refiner/prover only after a precise domain statement |
| A2 global-oscillation transfer | plausible route, proof-ready draft | `thm:a2-target` open | `prover`, then `proof-checker` |
| A2 exact unrestricted mean constant under subquadratic tail rigidity | proved reuse of two certified dossiers | no node | short corollary dossier |
| TV contamination also forces divergent LSI and $T_2$ constants | proved reuse plus the standard $T_2$ covariance lemma | only the $C_P$ obstruction is certified | separate strengthening dossier |
| A3 product Hardy theorem | proved reuse of certified block-Gibbs plus imported Hardy | `thm:a3-product` open | `prover`, then `proof-checker` |
| A3 log-noncentered hierarchical prior and bounded-likelihood rung | plausible route, proof-ready drafts | prior node open; corollary has no node | coupled dossier |
| A4 global logistic translation-family rigidity | plausible route, proof-ready draft | `prop:a4-logistic-global` open | `prover`, then `proof-checker` |
| A4 local ratio calculus transfers to any smooth numerator | proved reuse | no node needed | synthesize as a reusable lemma pattern |
| A5 folded quotient upper bound and quotient Fisher limit | proved reuse | bundled into open examples with an unproved raw half | split proof-ready quotient node(s) |
| A5 Gaussian partial noncentering is globally optimal over all $\alpha\in\mathbb R$ | proved reuse | certified only on $[0,1]$ | strengthen statement in a new proof cycle |
| A5 Neal partial phase is infinite for every $\alpha\ne1$ | plausible route with one sign-reflection step | certified only for $0\le\alpha<1$ | short strengthening dossier |
| A3 horseshoe sign quotient has no strict weighted-gap gain | plausible cross-target route | no node | parity-separated sharpness check |
| raw folded-well asymptotic | obstruction / incomplete archived route | `ex:a5-folding` open | finish the Hardy layer; do not cite the archive assertion as a proof |

## 1. A1: inverse curvature, mode leverage, and what the upper Hessian bound really does

### Mined proofs and mechanism

**Certified source:** `solutions/a1-harmonic-mode-leverage.tex`, especially
Theorem `thm:sol-a1-harmonic` and Theorem `thm:sol-a1-mode-leverage`.

The harmonic-mean proof takes a near-bottom spectral vector, applies the Bochner identity and the
weak Kato inequality to $g=|\nabla f|$, and then applies Poincaré once more to $g$. Weighted
Cauchy--Schwarz closes the loop with $\mathbb E\rho^{-1}$, where
$\rho=\lambda_{\min}(\nabla^2U)$. The mode-leverage proof compares every likelihood Hessian
along mode-Hessian rays and integrates twice to obtain radial potential envelopes; the direct
constant is then the harmonic-mean theorem applied to a radial inverse-curvature majorant.

**Review-excluded source:** `modules/open-targets/A1-data-informed-glm.tex`, lines 145--158, and
`research/explorations/2026-08-21-a1-bulk-tail-audit.md`, Result 1.

For every $1$-Lipschitz $f$, Brascamp--Lieb bounds its variance by
$\mathbb E\lambda_{\max}(H^{-1})$. Milman's log-concave spread-to-gap comparison upgrades this
to an ordinary Poincaré inequality with a universal constant $C_M$. The remaining bulk--tail split
is only Loewner inversion on $G_{\bar W}$ and the prior floor off that event.

### Hypothesis usage

| hypothesis | exact use | first failure on relaxation | mining conclusion |
|---|---|---|---|
| $U\in C^\infty$ | Bochner identity, ground-state transform, operator-core passage, Sobolev chain rule | for nonsmooth $U$, the Hessian term and graph-domain approximation are not defined by the written proof | essential to this dossier, but plausibly replaceable by a Mosco/approximation contract |
| $\nabla^2U\succeq mI$, $m>0$ | positive gap, $\rho^{-1}\le m^{-1}$, coercive gradient growth, and division by the curvature integral | weak convexity loses the starting gap and the estimate $\int g^2\le m^{-1}\int\rho g^2$ | genuinely essential to the factor-one mechanism as written |
| $\nabla^2U\preceq MI$ | used only in the noncompact domain step through $\Delta U\le dM$, making the Schrödinger potential bounded below and coercive | without it, the formal Bochner--Kato algebra remains, but the dossier no longer proves that $C_c^\infty$ is an operator core or that the identity closes | the true analytic hypothesis is a domain/core contract; the global upper Hessian bound is a sufficient, not algebraic, condition |
| each $\ell_i''>0$ and $\log\ell_i''$ is $L_i$-Lipschitz | defines $\log\ell_i''$ and gives the rowwise exponential comparison | zeros of curvature make the logarithm undefined and can destroy a two-sided rowwise comparison | essential to this particular mode-leverage certificate, not to Poincaré itself |
| $\eta<1$ | only makes the chosen numerator $e^{\eta r-g_-(r;\eta)}$ integrable | the exponent has nonnegative linear tail when $\eta\ge1$ | a gate on this radial majorant, not an obstruction to a finite $C_P$ |
| fixed $d$ in the asymptotic corollary | turns pointwise radial convergence plus one fixed integrable majorant into covariance convergence | the $r^{d-1}$ volume factor varies when $d=d_n$ | the bottleneck for growing dimension is uniform radial integrability, not the linear lower test |

### What is stronger than the current labels

- The factor-one algebra after the domain passage uses no upper Hessian bound. An abstract theorem
  can replace $\nabla^2U\preceq MI$ by: the diffusion generator is self-adjoint with a core on
  which Bochner holds; the identity closes on bounded spectral subspaces; and weak Kato holds
  there. This is **not yet a useful generalization** until those conditions are verified for an
  unbounded-Hessian class. In particular it does not already solve Poisson.
- The manuscript proof of `prop:a1-bulk-tail` is complete modulo exact citation/normalization of
  the imported Milman comparison. Its bottleneck is certification and the value/source of $C_M$,
  not a new GLM calculation.
- The one-observation logistic mode-Hessian no-go at
  `modules/open-targets/A1-data-informed-glm.tex`, lines 230--249, is an analytic counterexample
  draft for the still-open fence `obs:flat-direction`: the posterior tends to a half Gaussian while
  the inverse mode Hessian tends to zero. It is ready to be isolated in a dossier.

### True bottleneck

For the certified bounded-Hessian route, improving the conclusion means improving the global
radial majorant or replacing maximal row leverage by a spectral construction; more operator-domain
work does not improve the finite-$\eta$ constant. For unbounded Hessians, the first missing step is
the closed Bochner/Kato domain passage. For the universal bulk--tail route, the implication is
already present; selecting a useful $\bar W$ and proving a small integrated tail remain the
substantive A1 tasks.

## 2. A2: tail rigidity, strong Laplace transfer, and the TV underclaim

### Mined proofs and mechanism

**Certified tail source:** `solutions/a2-subquadratic-tail-rigidity.tex`, Theorem
`thm:sol-a2-subquadratic`.

Gaussian completion writes the directional log-MGF as the prior quadratic term plus
$\log\mathbb E e^{-L(Y_t)}$. An affine support gives an $O(t)$ upper correction and Jensen plus
the Gaussian-tube assumption gives an $o(t^2)$ lower correction. The resulting top-direction
quadratic rate forces the $T_2$ lower bound, while convexity gives matching Bakry--Émery and
Otto--Villani upper bounds.

**Review-excluded transfer source:** `modules/open-targets/A2-bernstein-von-mises.tex`, lines
230--259, and `research/explorations/2026-08-21-a2-strong-laplace-and-global-constants.md`, Result 1.

A globally vanishing log-density oscillation around the whitened Gaussian gives an
$e^{\pm\delta_n}$ density sandwich. Holley--Stroock gives all upper bounds, the same sandwich
gives covariance convergence, and covariance tests give all lower bounds. Whitening returns the
$\lambda_{\max}(H_n^{-1})$ scale.

**Certified obstruction source:** `solutions/obs-tv-insufficient.tex` plus
`solutions/glm-linear-baselines.tex` and the shared $T_2$ covariance fact.

The contamination has TV distance at most $\varepsilon_n$ and variance
$1+\varepsilon_n(1-\varepsilon_n)a_n^2$. Thus its Poincaré constant diverges. Since
$C_{LS}\ge C_P$ and $C_{T_2}\ge\operatorname{Var}(X)$ in the repository normalization, the very
same sequence also makes the optimal LSI and $T_2$ constants diverge; those two consequences were
conservatively excluded from the 2026-08-25 review rather than disproved.

### Hypothesis usage

| hypothesis | exact use | first failure on relaxation | mining conclusion |
|---|---|---|---|
| $L$ finite and convex | global affine support, posterior integrability, and Bakry--Émery upper bound | nonconvexity loses the matching prior-scale upper bound even if the MGF lower rate survives | essential for equality, not for the directional lower bound alone |
| $L\in C^2$ | only used to state the Hessian upper-bound route | nonsmoothness blocks the literal Hessian line | unused for the MGF lower bound; for finite convex GLM losses, `thm:glm-fi` already supplies the nonsmooth upper bound |
| $\mathbb E L(Y_t)=o(t^2)$ | makes the Jensen lower correction negligible | a positive quadratic limit changes the MGF coefficient | stronger than necessary: a subsequence with $\liminf t^{-2}\mathbb E L(Y_t)=0$ already forces the needed log-MGF limsup |
| $u$ a top eigenvector of $\Sigma$ | makes the lower MGF rate meet the global curvature upper bound | a non-top direction gives only a smaller lower bound | essential for equality with $\lambda_{\max}(\Sigma)$ |
| $\operatorname{osc}(r_n)=o_P(1)$ | global density sandwich, Holley--Stroock, moment convergence | local or TV comparison allows remote contamination or bottlenecks | the implication is complete; model verification or weaker spectral stability is the open payload |
| fixed $d$ in the density-sandwich covariance step | controls $\mathbb E|Z|^2$ uniformly | the elementary bound carries dimension dependence | growing dimension needs a quantitative relation between $d_n$ and $\delta_n$ |
| $\varepsilon_na_n^2\to\infty$ in the TV witness | makes covariance diverge | without it TV still vanishes but the linear witness may stay bounded | exact obstruction threshold for this witness |

### Hidden deductions

1. Combining `prop:a2-subquadratic-global` with `eq:a4-mean-dual` gives

   $$
   C_{\mathrm{mean},\mathrm{all}}(\pi)
   =C_{LS}(\pi)=C_{T_2}(\pi)=\lambda_{\max}(\Sigma).
   $$

   The top-direction log-MGF limit gives the lower bound in the A4 dual, and
   $C_{\mathrm{mean},\mathrm{all}}\le C_{T_2}$ gives the upper bound. The A2 statement does not
   record this A4 consequence.
2. The statistical regularity assumptions in `thm:a2-target` are not used in the transfer
   implication once $H_n/n\to I$ and the global density representation are assumed. The archive
   already contains the cleaner deterministic lemma for a positive matrix $H$ and a Gaussian
   perturbation. Separating that lemma would expose the true model-specific obligation.
3. In the Gaussian-prior GLM subclass, the $C^2$ assumption of the tail-rigidity theorem can be
   dropped by using the certified nonsmooth convex upper bound from `thm:glm-fi`; the MGF half
   never differentiated $L$.

### True bottleneck

For `thm:a2-target`, nothing remains in the abstract transfer proof beyond certification and an
exact $T_2$ covariance lemma in the dossier. The hard A2 question is replacing global oscillation
by a weaker condition that still controls the spectrum. For tail rigidity, weakening convexity is
the first point that breaks equality; weakening $o(t^2)$ to the precise one-sided liminf condition
is only a statement sharpening.

## 3. A3: product closure, pullback geometry, and dependence

### Mined proofs and mechanism

**Certified one-dimensional source:** `solutions/prop-a3-horseshoe.tex`.

The change $x=\sinh y$ converts the quadratic weighted form into an ordinary one-dimensional
form. An exact positive remainder for $e^aE_1(a)$ yields the drift inequality
$W'(y)\ge\tanh(y/2)$; the ground-state transform with $\sinh(y/2)$ gives a $1/4$ lower gap in
both parity sectors, and a translated tail sequence proves sharpness.

**Certified dependence source:** `solutions/thm-a3-block-gibbs.tex`.

The definition of $\gamma_{\mathrm{blk}}$ followed by conditional inequalities immediately gives
the joint energy bound. Product Efron--Stein makes $\gamma_{\mathrm{blk}}=1$. For two blocks,
conditional expectations are two orthogonal projections and the two-projection identity gives
$\gamma_{\mathrm{blk}}=1-\rho_{\max}$.

**Certified obstruction source:** `solutions/obs-marginals-not-joint.tex`.

A fixed-marginal copula places most mass in two opposite cubes and only $\varepsilon$ density in
the angular transition region. The variance stays order one while the diagonal weighted energy is
$O(\varepsilon)$; density comparison supplies the matching $O(\varepsilon^{-1})$ upper bound.

**Review-excluded drafts:** `modules/open-targets/A3-heavy-tailed-posteriors.tex`, lines 392--452
and 570--579.

The product theorem is already the product case of the certified block theorem combined with the
imported one-dimensional Hardy bound. The hierarchical prior is the product law of Gaussian
$z_j$ and log-half-Cauchy $u,v_j$, all with constants at most $4$, pulled through
$\theta_j=e^{u+v_j}z_j$; the chain rule gives exactly the displayed cross-term metric. A bounded
likelihood ratio then transfers the same form with factor $M/m$.

### Hypothesis usage

| hypothesis | exact use | first failure on relaxation | mining conclusion |
|---|---|---|---|
| exact horseshoe $e^aE_1(a)$ density | rational remainder and global drift inequality | a generic Cauchy tail fixes only the tail spectral floor, not the absence of a bulk eigenvalue | special-function input is essential for the exact constant $4$ |
| symmetry of the horseshoe law | parity split and trace-shift argument | without symmetry the proof does not decompose into the two half-line sectors | exact constant may survive, but this proof does not show it |
| deterministic uniform conditional constants $C_i$ | pulls $\max_iC_i$ outside the joint integral | varying unbounded conditional constants prevent that Euclidean/declared-metric bound | not needed if the varying constants are absorbed into the metric: set $A_i'=C_i(x_{-i})A_i$ and use deterministic constant $1$ |
| $\gamma_{\mathrm{blk}}>0$ | divides the conditional-variance estimate | a common factor or dependence bottleneck makes the joint gap zero | the true posterior bottleneck; marginal Hardy work cannot replace it |
| product structure in `thm:a3-product` | gives $\gamma_{\mathrm{blk}}=1$ | arbitrary dependence is exactly refuted by `obs:marginals-not-joint` | the open product node is already a direct certified reuse |
| nondegenerate scale coordinates and full pullback energy | permits tests in scale directions and records chain-rule cross terms | coefficient-only energy gives zero energy to nonconstant scale functions | essential fence imposed by `obs:marginals-not-joint` |
| $0<m\le L\le M$ for the likelihood tilt | two-sided density comparison | ordinary Gaussian/logistic likelihoods have infimum zero | the bounded-likelihood rung is complete but deliberately narrow |
| dimension $d\ge3$ in the copula witness | angular $|\nabla\varphi|\asymp r^{-1}$ is square-integrable near the common corner | in $d=2$ this particular angular witness has logarithmically divergent energy | the dossier does not already prove a two-dimensional version |

### Hidden deductions and transfers

- `thm:a3-product` needs no new idea: use `thm:a3-block-gibbs` with
  $\gamma_{\mathrm{blk}}=1$ and $C_i\le4B_i$. This was explicitly outside the prior A3 review.
- Conditional constants may vary with the complementary blocks if their variation is declared as
  part of the joint metric. This is already contained in the certified theorem because $A_i(x)$
  is allowed to be measurable and state-dependent. The requirement of uniform $C_i$ is a
  requirement only for retaining the original unrescaled metric.
- The horseshoe proof controls both parity sectors from below. Reflecting the one-sided sharpness
  sequence evenly and oddly should show that both restricted weighted gaps equal $1/4$; combined
  with `prop:a5-ratio`, the sign quotient would then have the same weighted constant $4$. The
  reflection/sharpness step is not written in the dossier, so this is a plausible route, not a
  certified consequence.

### True bottleneck

The product and prior-side hierarchy are certification tasks. For an actual hierarchical
posterior, the first conclusion-improving step is a quantitative lower bound on
$\gamma_{\mathrm{blk}}$ (or $1-\rho_{\max}$ for two blocks) in a named data regime. More precise
one-dimensional Hardy constants do nothing if that dependence factor collapses.

## 4. A4: duality, local ratio calculus, and remote translations

### Mined proofs and mechanism

**Certified global/local mean sources:** `solutions/eq-a4-mean-dual.tex` and
`solutions/prop-a4-mean-local.tex`.

The entropy inequality gives one direction of the linear log-MGF dual and the Gibbs variational
formula gives the converse. Under a Legendre cumulant contract, exponential tilts attain the
minimal entropy for each directional mean; restricting their entropy gives the exact localized
formula. Uniform third-cumulant control then yields the covariance limit.

**Certified local parametric sources:** `solutions/prop-a4-local-wellspecified.tex`,
`solutions/prop-a4-local-misspecified.tex`, and `solutions/prop-a4-local-excess.tex`.

Compact isolation shrinks a KL sublevel to an $O(\sqrt\rho)$ parameter ball. Dividing Taylor
expansions gives a generalized Rayleigh quotient in the well-specified or centered-excess case.
With misspecification, the numerator baseline and linear term survive, producing the raw baseline
and generic $\sqrt\rho$ correction.

**Review-excluded translation source:** `modules/open-targets/A4-variational-inference.tex`, lines
290--311, and `research/explorations/2026-08-21-a4-restricted-transport-audit.md`, Section 2.

For $q_{tv}=N(tv,S)$, the Gaussian prior contributes
$t^2v^T\Sigma_0^{-1}v$ to twice KL and a finite logistic loss contributes only $O(|t|)$. Both
$W_2^2$ and squared mean displacement are at least $t^2|v|^2+O(|t|)$. A top covariance direction
therefore matches the global $T_2$ upper bound and forces all four constants to the prior scale.

### Hypothesis usage

| hypothesis | exact use | first failure on relaxation | mining conclusion |
|---|---|---|---|
| $\pi\in\mathcal P_1$ in the global mean dual | defines centering and admissible competitor means | without a first moment the stated mean functional is undefined | minimal natural hypothesis |
| Legendre/endpoint contract in the localized dual | identifies every accessible projected-mean entropy infimum with an exponential tilt or limit | nondifferentiable cumulants or inaccessible boundary means can leave a duality gap | essential for the exact localized parameterization, not for the global dual |
| common exponential moment and $\operatorname{Cov}\succ0$ | uniform third cumulants and uniform conversion $r_u(t)\le r\Rightarrow |t|=O(\sqrt r)$ | null directions can have a different higher-order regime | used only for the $O(\sqrt r)$ covariance expansion |
| compact isolated KL sublevel | rules out remote competitors with asymptotically equal KL | a local Taylor expansion alone cannot control the supremum | the genuine coercivity hypothesis behind all three local theorems |
| $\delta>0$ in the raw misspecified theorem | makes the denominator nonzero at the optimizer | at $\delta=0$ the quadratic tangent regime replaces the baseline expansion | essential distinction, not a technicality |
| all translations of one fixed $S\succ0$ in `prop:a4-logistic-global` | supplies arbitrarily remote witnesses while keeping entropy and covariance terms fixed | a bounded or non-location-rich family can have a smaller global restricted constant | essential for equality of the restricted and unrestricted constants |
| at-most-linear logistic loss | makes its expectation under $N(tv,S)$ be $O(|t|)$ | quadratic likelihood tails can change the leading KL coefficient | the exact proof extends to any convex GLM loss that is Gaussian-average subquadratic under the witness family |

### Hidden deductions and transfers

- `prop:a4-logistic-global` is proof-ready as written. The exact A2 prior-scale theorem supplies
  the upper bound, and the manuscript already contains the matching family witness.
- The same argument proves a wider A2-to-A4 statement: for a Gaussian-prior convex GLM covered by
  `thm:glm-fi`, if the variational family contains $N(m_*+tu,S)$ in a top prior-covariance
  direction and $\mathbb E_{N(m_*+tu,S)}L=o(t^2)$, then

  $$
  C_{\mathrm{mean},\mathcal Q}=C_{\mathcal Q}
  =C_{\mathrm{mean},\mathrm{all}}=C_{T_2}=\lambda_{\max}(\Sigma_0).
  $$
- The three local proofs are instances of one abstract ratio lemma. Any nonnegative numerator
  with a uniform quadratic expansion produces the same generalized eigenvalue; a numerator with
  a nonzero baseline and linear term produces the same baseline plus support-function
  $\sqrt\rho$ correction. This is reusable for per-functional losses and A5 local
  reparameterization diagnostics without a new Wasserstein proof.

### True bottleneck

The global logistic proposition needs only dossier/review. The hard A4 target begins after global
translations are excluded: prove compactness and uniform $\mathcal P_2$ control of a finite-radius
family sublevel, then control the numerator away from the tangent chart. More local Taylor algebra
does not provide that finite-radius certificate.

## 5. A5: quotient blocks, perturbation stability, and parameterization tails

### Mined proofs and mechanism

**Certified quotient sources:** `solutions/a5-lipschitz-quotient.tex`,
`solutions/prop-a5-ratio.tex`, and `solutions/prop-a5-block-stability.tex`.

Pullback through a Lipschitz map preserves variance/entropy and contracts energy; the
fiber-constant density lift preserves KL and pushes couplings forward for $T_2$. Group averaging
orthogonally decomposes both variance and energy into invariant/non-invariant blocks. A bounded
invariant density ratio compares each fixed block's variance and energy and hence its restricted
gap.

**Certified Gaussian and funnel sources:** `solutions/prop-a5-partial-gaussian.tex`,
`solutions/ex-a5-neal.tex`, and `solutions/prop-a5-partial-funnel.tex`.

For the scalar Gaussian shear, the precision determinant is independent of $\alpha$, so both the
smallest eigenvalue and condition number are optimized by minimizing the trace. For Neal's funnel,
a Euclidean coordinate is Lipschitz and square-integrable but has no positive exponential moment;
the Poincaré-to-exponential-tail lemma rules out a finite constant unless noncentering is complete.

**Partially complete archived source:** `modules/open-targets/A5-quotient-and-reparameterization.tex`,
lines 212--264, and `research/explorations/2026-08-21-a5-quotient-reparameterization-audit.md`,
lines 130--208.

The folded law is exactly $|a+\sigma Z|$, a $\sigma$-Lipschitz Gaussian image, so all three
quotient constants are at most $\sigma^2$ and the quotient-coordinate variance proves
$C_P\to\sigma^2$. The raw double-well Hardy asymptotic is only asserted after “splitting off the
two Gaussian tails”; the needed two-sided integral estimates are not written. The quotient half is
proof-ready, while the raw half remains incomplete.

### Hypothesis usage

| hypothesis | exact use | first failure on relaxation | mining conclusion |
|---|---|---|---|
| global $L$-Lipschitz map | weak chain rule and coupling-cost contraction | a locally Lipschitz or high-probability map gives no global FI comparison | essential to the generic transport lemma |
| finite isometric group | finite averaging and the minimum formula for the orbit metric | a compact-group extension needs Haar integration and quotient measurability/domain checks | finiteness is sufficient; the written proof does not already certify the compact case |
| same pointwise carré du champ and invariant bounded density ratio | makes Sobolev domains and fixed representation blocks common to both laws | a changing metric or non-invariant tilt mixes blocks | essential to `prop:a5-block-stability` |
| only two blocks `inv/noninv` in the statement | not used in the density-comparison algebra | none: the proof compares Rayleigh quotients on any common fixed subspace | the same $e^{\pm\varepsilon}$ estimate holds for every real isotypic block |
| $0\le\alpha\le1$ in the Gaussian partial theorem | not used in trace minimization except to note the minimizer lies in the interval | no failure: the positive quadratic trace has the same unique global minimizer on $\mathbb R$ | immediate statement strengthening |
| $s>0$ in the funnel | creates a nondegenerate lognormal tail | at $s=0$ the counterexample collapses | essential and correctly added after review |
| $0\le\alpha<1$ in the partial funnel | makes $\beta=1-\alpha>0$ for the chosen $u\to+\infty$ event | for $\alpha>1$, the same proof must use $u\to-\infty$ | the actual singular phase is every $\alpha\ne1$, but the opposite-tail step is not written |
| raw folded-well Hardy assertion | needed only for the raw metastable rate | quotient Lipschitz and variance bounds do not imply a raw lower/upper barrier estimate | do not hold the quotient result hostage to this unfinished half |

### Hidden deductions and transfers

1. `prop:a5-partial-gaussian` already proves that
   $\alpha_*=1/(1+rB)$ is the unique minimizer over all $\alpha\in\mathbb R$, not only
   $[0,1]$: the trace is a positive quadratic with that global minimizer and every shear remains
   invertible and determinant one.
2. By Gaussian symmetry, the law of $e^{(1-\alpha)u}z$ depends on
   $|1-\alpha|$. The partial-funnel obstruction therefore extends from $\alpha<1$ to every
   $\alpha\ne1$ after reflecting the tail event.
3. The block-stability proof works verbatim on any common real isotypic subspace. This is the
   exact perturbation statement needed before the multi-block Ritz program in `q:a5-detect`; it
   does not give eigenvector or projector stability.
4. The ramp proof in `lem:a5-pi-exp-tail` has an unused optimization. With truncation height
   $a>\sqrt{2C}$ it gives tail contraction $2C/a^2$ per step. Optimizing
   $a^{-1}\log(a^2/(2C))$ yields exponential moments for every
   $c<\sqrt2/(e\sqrt C)$, stronger than the recorded
   $(\log2)/(2\sqrt C)$. No current funnel conclusion needs the sharper number.

### True bottleneck

For quotient calibrations, the quotient half of the Gaussian well is done; the raw Hardy
prefactor/exponent still needs a complete proof. For general metastability, capacity estimates and
global landscape control are the bottleneck, not the representation decomposition. For nonlinear
parameterization, the exponential-tail test is the first global gate; local conditioning cannot
repair a failed tail gate.

## 6. Candidate nodes and exact proof handoffs

Every item below is proposed with `status: open`. Existing IDs retain their current manuscript
anchor. New IDs require an orchestrator-approved manuscript statement before a ledger entry.

### Candidate A1-P: certify the existing universal bulk--tail node

```yaml
id: prop:a1-bulk-tail
kind: proposition
status: open
program: a-series
file: modules/open-targets/A1-data-informed-glm.tex
refines: prop:a1-bulk-tail
statement: >-
  For every smooth strictly log-concave Gaussian-prior convex GLM posterior and every
  deterministic diagonal Wbar >= 0, there is a universal C_M such that C_P is at most C_M
  times E lambda_max(H^{-1}); consequently it is at most C_M times each displayed
  bulk-plus-integrated-tail and bulk-plus-prior-scale-probability-tail expression.
depends_on: []
bounded_by: [obs:flat-direction]
```

**Proof source.** `modules/open-targets/A1-data-informed-glm.tex:145` and
`research/explorations/2026-08-21-a1-bulk-tail-audit.md`, Result 1.
**Fence check.** `obs:flat-direction` is respected because remote curvature loss remains in the
tail term. The statement concerns $C_P$, so `obs:gaussian-tail-rigidity` does not apply. It makes
no heavy-tail, dependence, TV-transfer, symmetry, or variational-family claim.
**What the prover must add.** State the precise imported Brascamp--Lieb and Milman theorem with
normalization and hypotheses; prove both Loewner splits; do not claim factor one outside the
bounded-Hessian theorem.

### Candidate A2-P: certify the existing strong-Laplace transfer

```yaml
id: thm:a2-target
kind: theorem
status: open
program: a-series
file: modules/open-targets/A2-bernstein-von-mises.tex
refines: conj:a2
statement: >-
  If the mode-whitened posterior has density exp(-r_n)/Z_n relative to N(0,I_d), with
  osc(r_n)=o_P(1), and H_n/n converges in probability to I(theta_0)>0, then C_P, C_LS,
  and C_TCI are all (1+o_P(1)) lambda_max(H_n^{-1}), hence their n-scaled limits equal
  lambda_max(I(theta_0)^{-1}).
depends_on: [lem:linear-test-lower]
bounded_by: [obs:tv-insufficient, obs:gaussian-tail-rigidity]
```

**Proof source.** `modules/open-targets/A2-bernstein-von-mises.tex:230` and the deterministic
sandwich in `research/explorations/2026-08-21-a2-strong-laplace-and-global-constants.md`.
**Fence check.** Global oscillation is strictly stronger than TV, so it defeats
`obs:tv-insufficient`. Fixed-prior logistic does not satisfy the hypothesis, so there is no
conflict with `obs:gaussian-tail-rigidity`. Other fences are irrelevant.
**What the prover must add.** Include the $T_2\Rightarrow\operatorname{Cov}\preceq CI$ proof or
an exact imported citation and make the covariance comparison after anisotropic unwhitening
explicit.

### Candidate A2-C: record the hidden unrestricted-mean equality

```yaml
id: cor:a2-subquadratic-mean-rigidity
kind: corollary
status: open
program: a-series
file: modules/open-targets/A2-bernstein-von-mises.tex
label: cor:a2-subquadratic-mean-rigidity
refines: prop:a2-subquadratic-global
statement: >-
  Under the hypotheses of prop:a2-subquadratic-global, the unrestricted posterior-mean
  entropy constant also equals lambda_max(Sigma); thus C_mean,all = C_LS = C_TCI =
  lambda_max(Sigma).
depends_on: [prop:a2-subquadratic-global, eq:a4-mean-dual]
bounded_by: [obs:gaussian-tail-rigidity]
```

**Fence check.** This strengthens, rather than evades, Gaussian-tail rigidity. TV, heavy-tail,
dependence, symmetry, and restricted-family fences do not enter.
**Proof.** The directional limit at `solutions/a2-subquadratic-tail-rigidity.tex:71` is a lower
witness in the exact dual `solutions/eq-a4-mean-dual.tex:20`; $T_2$ supplies the reverse bound.

### Candidate A2-O: strengthen the TV obstruction to all three constants

```yaml
id: obs:tv-insufficient-all-fi
kind: obstruction
status: open
program: a-series
file: modules/open-targets/A2-bernstein-von-mises.tex
label: warn:a2-tv-fails-all-fi
refines: warn:a2-tv-fails
statement: >-
  There are mu_n with ||mu_n-N(0,1)||_TV -> 0 for which the optimal Poincare,
  log-Sobolev, and T2 constants all diverge; the Gaussian contamination with
  epsilon_n -> 0 and epsilon_n a_n^2 -> infinity is one such sequence.
depends_on: [obs:tv-insufficient, lem:linear-test-lower]
bounded_by: []
```

**Fence check.** This is itself a fence.
**Proof obligation.** Reuse the certified variance calculation; invoke $C_{LS}\ge C_P$ and prove
the repository-normalized $T_2$ covariance constraint. The 2026-08-25 review explicitly excluded
these conclusions, so they require a new review rather than a metadata-only promotion.

### Candidate A3-P1: certify product Hardy tensorization

```yaml
id: thm:a3-product
kind: theorem
status: open
program: a-series
file: modules/open-targets/A3-heavy-tailed-posteriors.tex
refines: thm:a3-product
statement: >-
  If B_j is the maximum of the two one-sided weighted Hardy quantities for coordinate j,
  then the product law has weighted Poincare constant at most 4 max_j B_j in the diagonal
  product metric.
depends_on: [thm:hardy-1d, thm:a3-block-gibbs]
bounded_by: [obs:heavy-tail-no-classical, obs:marginals-not-joint]
```

**Proof source.** `modules/open-targets/A3-heavy-tailed-posteriors.tex:392`; alternatively apply
the certified `thm:a3-block-gibbs` with $\gamma_{\mathrm{blk}}=1$.
**Fence check.** The theorem is weighted, so it makes no forbidden classical heavy-tail claim.
It assumes a product and therefore does not infer a joint constant from marginals under arbitrary
dependence. Flat-direction, TV, symmetry, and variational fences do not apply.

### Candidate A3-P2: certify the hierarchical prior, coupled to A3-P1

```yaml
id: prop:a3-hierarchical-prior
kind: proposition
status: open
program: a-series
file: modules/open-targets/A3-heavy-tailed-posteriors.tex
refines: prop:a3-hierarchical-prior
statement: >-
  For independent standard Gaussian z_j and independent log-half-Cauchy u,v_j, with
  theta_j=exp(u+v_j)z_j, the hierarchical horseshoe prior has optimal weighted Poincare
  constant 4 in the full noncentered pullback metric, including all coefficient-scale cross
  terms displayed in the manuscript.
depends_on: [thm:a3-student, thm:a3-product]
bounded_by: [obs:heavy-tail-no-classical, obs:marginals-not-joint]
```

**Proof source.** `modules/open-targets/A3-heavy-tailed-posteriors.tex:432`.
**Fence check.** Log scales and the pullback metric avoid a false Euclidean heavy-tail claim; the
energy contains scale derivatives and cross terms, so it passes the joint-marginal fence. It is a
prior/product statement and makes no likelihood-flat claim.

### Candidate A3-C: isolate the bounded-likelihood posterior rung

```yaml
id: cor:a3-bounded-likelihood-pullback
kind: corollary
status: open
program: a-series
file: modules/open-targets/A3-heavy-tailed-posteriors.tex
label: cor:a3-bounded-likelihood-pullback
refines: conj:a3-dependent
statement: >-
  If pi_0 is the log-noncentered hierarchical horseshoe prior and
  d pi_L = L d pi_0 / Z with 0 < m <= L <= M < infinity, then pi_L has weighted
  Poincare constant at most 4 M/m in the same full pullback metric.
depends_on: [prop:a3-hierarchical-prior]
bounded_by: [obs:heavy-tail-no-classical, obs:marginals-not-joint, obs:flat-direction]
```

**Proof source.** `modules/open-targets/A3-heavy-tailed-posteriors.tex:570`.
**Fence check.** The full joint density-ratio comparison controls dependence and retains scale
derivatives. The lower bound $m>0$ explicitly excludes ordinary vanishing Gaussian/logistic
likelihoods, so it does not evade the flat-direction fence. The result stays weighted.

### Candidate A4-P: certify the existing global logistic variational rigidity

```yaml
id: prop:a4-logistic-global
kind: proposition
status: open
program: a-series
file: modules/open-targets/A4-variational-inference.tex
refines: prop:a4-logistic-global
statement: >-
  For a Gaussian-prior binary-logistic posterior and any Gaussian variational family
  containing all translations of one fixed positive-definite covariance,
  C_mean,Q = C_Q = C_mean,all = C_TCI = lambda_max(Sigma_0).
depends_on: [prop:a2-logistic-global, eq:a4-mean-dual]
bounded_by: [obs:flat-direction, obs:gaussian-tail-rigidity]
```

**Proof source.** `modules/open-targets/A4-variational-inference.tex:290` and
`research/explorations/2026-08-21-a4-restricted-transport-audit.md`, Section 2.
**Fence check.** The conclusion is prior-scale, exactly as Gaussian-tail rigidity demands. It
does not claim a posterior-mode scale, and the location-rich hypothesis is explicit. Heavy-tail,
dependence, TV, and symmetry fences do not enter.

### Candidate A5-P: split the completed quotient half from the incomplete raw half

```yaml
id: prop:a5-folded-gaussian-quotient
kind: proposition
status: open
program: a-series
file: modules/open-targets/A5-quotient-and-reparameterization.tex
label: prop:a5-folded-gaussian-quotient
refines: ex:a5-folding
statement: >-
  For mu_a = (N(-a,sigma^2)+N(a,sigma^2))/2 and its sign quotient bar_mu_a,
  C_P(bar_mu_a), C_LS(bar_mu_a), and C_TCI(bar_mu_a) are at most sigma^2 for every a,
  and C_P(bar_mu_a) tends to sigma^2 as a/sigma tends to infinity.
depends_on: [lem:a5-lipschitz, lem:linear-test-lower]
bounded_by: [obs:symmetry-vs-physical]
```

**Proof source.** `research/explorations/2026-08-21-a5-quotient-reparameterization-audit.md`,
lines 130--177.
**Fence check.** This computes the invariant/quotient block only and does not assert that every
physical slow mode disappears. The explicit model has no additional invariant metastability.
Other fences do not apply.
**Scope warning.** Do not include the raw asymptotic in this dossier unless the missing Hardy
integral estimates are supplied.

### Candidate A5-R: strengthen both scalar $\alpha$ domains

```yaml
id: cor:a5-partial-gaussian-all-alpha
kind: corollary
status: open
program: a-series
file: modules/open-targets/A5-quotient-and-reparameterization.tex
label: cor:a5-partial-gaussian-all-alpha
refines: prop:a5-partial-gaussian
statement: >-
  In the scalar Gaussian hierarchy, among z_alpha=theta-alpha u for every real alpha,
  both the Euclidean Gaussian Poincare constant and the precision condition number have the
  unique global minimizer alpha*=1/(1+rB).
depends_on: [prop:a5-partial-gaussian]
bounded_by: []
```

```yaml
id: cor:a5-partial-funnel-all-alpha
kind: corollary
status: open
program: a-series
file: modules/open-targets/A5-quotient-and-reparameterization.tex
label: cor:a5-partial-funnel-all-alpha
refines: prop:a5-partial-funnel
statement: >-
  For the prior-only Neal funnel with s>0, the Euclidean Poincare constant in coordinates
  (u,exp((1-alpha)u)z) is infinite for every real alpha != 1 and equals max(s^2,1) at alpha=1.
depends_on: [prop:a5-partial-funnel, lem:a5-pi-exp-tail]
bounded_by: [obs:heavy-tail-no-classical]
```

**Fence check.** The Gaussian result has no relevant obstruction. The funnel result explicitly
records the global heavy-tail failure and makes no likelihood-dependent claim.
**Proof source.** Global trace minimization is already at
`solutions/prop-a5-partial-gaussian.tex:40`; the funnel extension uses the same calculation as
`solutions/prop-a5-partial-funnel.tex:50` with the sign of $u$ reversed when $\alpha>1$.

## 7. Defects and semantic mismatches

### Defect D1: the A1 knowledge entry names the wrong node

**Affected artifact:** `research/knowledge/lemmas.md`, section
``prop:a1-bulk-tail — inverse-Hessian certificate``.
**Affected nodes:** `prop:a1-bulk-tail` and `prop:a1-euclidean-harmonic`.
**Severity:** source/provenance defect; no mathematical counterexample to the displayed fact.

The entry states the factor-one theorem under
$mI\preceq\nabla^2U\preceq MI$:

$$
C_P(\pi)\le\mathbb E\lambda_{\max}((\nabla^2U)^{-1}).
$$

That is the certified statement `prop:a1-euclidean-harmonic`, proved in
`solutions/a1-harmonic-mode-leverage.tex`. The node named in the heading,
`prop:a1-bulk-tail`, is still open and asserts a universal-$C_M$ Milman comparison plus the two
bulk--tail splits. Proposed synthesizer correction:

1. rename the heading/source to `prop:a1-euclidean-harmonic`;
2. retain the displayed factor-one fact and bounded-Hessian guardrail there;
3. if `prop:a1-bulk-tail` is indexed separately before certification, label it explicitly as an
   open analytic draft with universal $C_M$, not factor one.

### Defect D2: A5 reviewed-status prose is stale after the 2026-08-25 audit

**Affected artifact:** `modules/open-targets/A5-quotient-and-reparameterization.tex`, lines 31--38.
**Affected nodes:** `lem:a5-lipschitz`, `thm:a5-monotone`.
**Severity:** manuscript/ledger provenance mismatch, not a proof defect.

The prose says the quotient-monotonicity theorem and Lipschitz lemma are inline baselines not
counted in the reviewed set. Both now have `checked_by: agent`, the dossier
`solutions/a5-lipschitz-quotient.tex`, and the persisted review
`research/reviews/2026-08-25-ab-inline-r2-audit.md`. A latex-sync/orchestrator pass should update
the current-status paragraph without rewriting historical explorations.

### No substantive defect found in the certified dossier arguments

Within the hypotheses reviewed above, I found no mathematical error in the certified A1--A5
dossiers or their persisted reviews. The strongest concern is underclaim/provenance rather than
invalid proof: the TV dossier intentionally certifies only $C_P$ although existing standard
implications support a stronger new obstruction after a separate review. Review exclusions were
respected throughout this report.

## 8. Archived reruns and stop rules

- A new attempt to “prove” `prop:a1-bulk-tail` by factoring
  $\mathbb E[\lambda_{\max}(H^{-1})|\nabla f|^2]$ is a rerun of a rejected step. The valid archive
  route is Brascamp--Lieb only for Lipschitz spread, followed by Milman self-improvement.
- A tail-free inverse-mode-Hessian certificate for general logistic GLMs reruns the half-Gaussian
  counterfamily in `2026-08-21-a1-bulk-tail-audit.md`; it violates `obs:flat-direction`.
- A2 transfer from TV alone reruns the certified contamination obstruction. The global oscillation
  theorem is sufficient, not equivalent to a generic tail condition.
- A3 marginal Hardy constants without a dependence parameter rerun
  `solutions/obs-marginals-not-joint.tex`. A coefficient-only joint metric additionally fails on
  functions of the scales alone.
- A4 localization by a KL cutoff alone reruns `obs:restricted-not-finite`; compact family
  coercivity and uniform $\mathcal P_2$ control are separate hypotheses.
- The A5 raw folded-well estimate in the 2026-08-21 archive is not a completed proof: the phrase
  “after splitting off the two Gaussian tails” hides the two-sided Hardy estimates. The quotient
  half can be certified independently.
- Optimizing a partial Neal funnel locally before checking exponential tails reruns the certified
  singular phase. A likelihood-dependent interior optimum first needs a global tail-regularization
  theorem.

## 9. Parallel proof/consolidation plan

These tracks have distinct dossier keys and can run in parallel.

1. **A1 dossier:** `prop:a1-bulk-tail`, with exact Milman normalization and the two Loewner tail
   forms. Independently, isolate `obs:flat-direction` if the orchestrator wants the current fence
   certified.
2. **A2 dossier:** `thm:a2-target` plus, optionally, the short
   `cor:a2-subquadratic-mean-rigidity`. Keep the stronger TV obstruction in a distinct dossier so
   its reviewer is not asked to retroactively expand the 2026-08-25 review.
3. **A3 coupled dossier:** `thm:a3-product` and `prop:a3-hierarchical-prior`; once those pass, add
   the bounded-likelihood corollary. This is one logical chain and avoids a dangling dependency.
4. **A4 dossier:** `prop:a4-logistic-global`, then consider the wider Gaussian-average
   subquadratic translation statement as a separate refinement.
5. **A5 quotient dossier:** split the completed folded quotient claim from the unfinished raw
   Hardy asymptotic. A second small dossier can widen the two scalar $\alpha$ domains.
6. **Synthesis:** correct the A1 knowledge attribution and record the abstract local-ratio and
   isotypic-block stability mechanisms. The proof-miner does not edit shared knowledge.

## Shared handoff envelope

```yaml
outcome: complete
artifacts:
  - research/explorations/2026-08-27-proof-miner-a-series-mechanisms-c7f4.md
proposed_deltas:
  - "Synthesizer: reattribute the factor-one inverse-Hessian entry in research/knowledge/lemmas.md from prop:a1-bulk-tail to prop:a1-euclidean-harmonic; keep the open universal-C_M bulk-tail statement distinct."
  - "Orchestrator/latex-sync: update the A5 current reviewed-status paragraph to include the 2026-08-25 certification of lem:a5-lipschitz and thm:a5-monotone."
  - "Orchestrator: consider parallel prover lanes for prop:a1-bulk-tail, thm:a2-target, the coupled thm:a3-product + prop:a3-hierarchical-prior chain, prop:a4-logistic-global, and the split folded-quotient A5 candidate."
next_role: prover
next_prompt: |
  Own exactly solutions/thm-a2-target.tex and one collision-resistant
  research/explorations/2026-08-27-prover-thm-a2-target-<suffix>.md. Prove the existing open node
  thm:a2-target as stated in modules/open-targets/A2-bernstein-von-mises.tex. Audit the normalized
  density-ratio bounds from osc(r_n), the Holley--Stroock constants, covariance lower bounds for
  Poincare/LSI/T2, anisotropic whitening, and every o_P matrix/eigenvalue limit. Compile the
  standalone dossier and leave its header checked_by: none. Do not edit any ledger, manuscript,
  review, knowledge file, or bibliography. Record the attempt and hand the dossier to a distinct
  cold proof-checker.
```
