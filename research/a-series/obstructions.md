# A-series obstructions — cross-target no-go knowledge

Cross-cutting barriers and known-false statement forms. Each obstruction constrains the
*shape* a valid theorem may take; a conjecture that violates one is wrong by construction.
The machine-readable nodes live in [`ledger.yaml`](ledger.yaml) (`kind: obstruction`); the prose, the
*why*, and the **diagnostic role** live here. Targets reference these via `bounded_by`.

Math is written in LaTeX (`$…$`); the canonical *formal* statement of each barrier is the
manuscript `\label` named under "Source" — this file links and explains, it does not restate
formally.

> When you discover a new barrier useful to more than one target, add it here AND as an `obs:`
> node in the ledger. Single-target subtleties stay in that target's `.md`.

---

## obs:flat-direction — no global likelihood-curvature floor for saturating links
**Used by:** A1 (bulk tail term), A3 (surviving saturating-likelihood directions). **Source:**
`prop:flat-prior-nonintegrable`.

For logistic and other saturating links, likelihood curvature
$\ell''(x_i^\top\theta)$ can vanish in remote predictor directions (logistic:
$\sigma(1-\sigma)\to0$), so the global Hessian floor can be set by the **prior alone**
($\Sigma_0^{-1}$). This is not a statement about every GLM: Gaussian-linear likelihoods have a
uniform data-curvature floor, and Poisson curvature is one-sided. The obstruction rules out a
universal posterior-scale estimate based only on a positive local/mode Hessian for the saturating
class; it does not rule out every tail-free data-informed statistic.

**Numerical diagnostic.** In separable / near-separable logistic examples, compare the sound lower
bound $\lambda_{\max}(\mathrm{Cov}_\pi)$ with each fully specified local-curvature proposal. A
proposal is falsified only when its claimed upper bound falls below that lower bound (with numerical
error controlled). The retired diagnostic and its retraction remain in the dated A1 exploration;
the analytic one-observation family below is the surviving obstruction.

The analytic one-observation family
$\pi_a(d\theta)\propto e^{-\theta^2/(2\sigma^2)}\operatorname{sigmoid}(a\theta)d\theta$
is decisive: it tends to a half Gaussian while its inverse mode Hessian tends to zero, so no
universal constant-times inverse-mode-Hessian bound can hold for this family.

---

## obs:gaussian-tail-rigidity — global logistic LSI/$T_2$ stay at the prior scale
**Used by:** A1, A2, A4. **Source:** `prop:a2-logistic-global`.

For every finite binary-logistic likelihood with Gaussian prior covariance $\Sigma_0$,
$$
C_{\mathrm{LS}}(\pi)=C_{\mathrm{TCI}}(\pi)=\lambda_{\max}(\Sigma_0).
$$
This identity and the broader theorem behind it have standalone independently agent-certified
proofs; the derived obstruction is included in the scope of
[`a2-subquadratic-tail-rigidity.tex`](../../solutions/a2-subquadratic-tail-rigidity.tex) and its
persisted A1/A2 review. It is enough that the convex likelihood
perturbation have Gaussian-average growth $o(t^2)$ along one top prior-covariance direction
(`prop:a2-subquadratic-global`). A pointwise estimate on the central ray alone is insufficient,
because the completed square samples a fixed-width Gaussian tube.
The loss grows only linearly in remote directions, so the centered log-MGF retains quadratic
coefficient $u^\top\Sigma_0u/2$. This lower-bounds any global $T_2$ constant; Bakry--Émery and
Otto--Villani give the matching upper bound. Thus only $C_P$, or explicitly
localized/restricted entropy and transport constants, can improve to Fisher scale with fixed prior.

---

## obs:heavy-tail-no-classical — no classical LSI/$T_2$ (and no classical Poincaré) for heavy tails
**Used by:** A3, A4, A5 (funnel tails). **Source:** `thm:heavy-tail-no-lsi`, Tier 4.

Polynomial/exponential tails admit no classical LSI and no $T_2$ (an LSI forces sub-Gaussian
concentration); for the heaviest tails even the classical Poincaré fails. The correct object is
a **weighted** (or weak) inequality with a tail-growing weight $a(x) \asymp 1+\|x\|^2$.

**Diagnostic role.** Generalized Cauchy $\mu_\beta \propto (1+\|x\|^2)^{-\beta}$: the
unweighted 1D Hardy functional $\asymp x^2 \to \infty$ (so $C_P=\infty$); reweighting the
Dirichlet form by $(1+x^2)$ brings it to $O(1)$. The Student-$t$ closed-form gaps
$\lambda_{\beta,d}$ (`thm:a3-student`) are the calibration anchor.

The same integrability test is decisive for reparameterization. In the prior-only Neal funnel,
$z_\alpha=e^{(1-\alpha)u}z$ has no exponential moment for every $\alpha<1$, so every incomplete
partial noncentring has infinite Euclidean $C_P$; only $\alpha=1$ is product Gaussian. A
likelihood can change this verdict only through an explicit model-specific tail argument.

---

## obs:marginals-not-joint — marginal Hardy constants do not control dependence
**Used by:** A3 (`conj:a3-dependent`, `q:a3-hierarchical`). **Source:**
`prop:a3-marginals-not-joint`.

A positive-a.e. piecewise-smooth copula with standard-Cauchy marginals can keep every
one-dimensional marginal fixed while placing two macroscopic regions
behind an $O(\varepsilon)$-density bottleneck, forcing the joint weighted Poincaré constant to be
$\Omega(\varepsilon^{-1})$. Therefore marginal tail indices/Hardy constants require product
structure or an explicit quantitative dependence contract. For a coefficient-scale joint law,
a coefficient-only Dirichlet form also vanishes on nonconstant functions of the scales; scale
derivatives and pullback cross terms are structural. This obstruction has a standalone analytic
proof and independent-agent audit.

---

## obs:tv-insufficient — TV-BvM does not control the constants
**Used by:** A2. **Source:** `warn:a2-tv-fails`.

Total-variation convergence to the BvM Gaussian says nothing about constants — they see tails
and remote mass that TV does not. A "BvM $\Rightarrow$ constants" claim is **false** as stated.

**Diagnostic role (the canonical A2 trap).**
$\mu_n = (1-\varepsilon_n)N(0,1) + \varepsilon_n N(a_n,1)$ with $\varepsilon_n \to 0$,
$\varepsilon_n a_n^2 \to \infty$: $\|\mu_n - N(0,1)\|_{\mathrm{TV}} \le \varepsilon_n \to 0$ yet
the linear test gives $C_P(\mu_n) \ge \mathrm{Var}_{\mu_n}(x) \to \infty$. The reward harness
must FALSIFY any "BvM $\Rightarrow$ $n\,C_P \to \lambda_{\max}(I^{-1})$" claim here.

---

## obs:symmetry-vs-physical — symmetry-induced vs physical multimodality
**Used by:** A2 (`q:a2-multimodal`), A4 (`q:a4-multimodal`), A5. **Source:** `prop:a5-ratio`.

Quotienting by a symmetry group $G$ strictly helps **iff**
$\lambda_{\mathrm{noninv}}<\lambda_{\mathrm{inv}}$. If the gaps coincide, a degenerate first
eigenspace may contain non-invariant vectors but the constant does not improve. If the invariant
gap is smaller (a physical alternative after relabeling), quotienting does nothing to the slow
mode. Estimating one arbitrary eigenfunction is therefore insufficient. This derived obstruction
is independently certified in the scope of
[`prop-a5-ratio.tex`](../../solutions/prop-a5-ratio.tex) and the persisted A4/A5 review.

**Diagnostic role.** Folded double well $\mu_a = \tfrac12 N(-a,\sigma^2)+\tfrac12 N(a,\sigma^2)$
(`ex:a5-folding`) has the normalized logarithmic raw-well law
$\log(C_P(\mu_a)/\sigma^2)=a^2/(2\sigma^2)+O(\log(a/\sigma))$ as $a/\sigma\to\infty$, while the
folding map gives $C_P(\bar\mu_a)\le\sigma^2$ and in fact
$C_P(\bar\mu_a)\to\sigma^2$.

For more than two symmetry wells, the raw exponential rate is not the easiest pairwise move. The
correct equal-depth orbit quantity is the worst-cut/connectivity height
$\Gamma_{\rm conn}=\max_{\varnothing\ne A\subsetneq\mathcal W}\min_{i\in A,j\notin A}H_{ij}$:
the threshold at which the full orbit transition graph becomes connected. A minimum pair height
is sufficient only when its edges already connect the whole orbit.

---

## obs:restricted-not-finite — family-restricted transport constants can be infinite
**Used by:** A4, A3. **Source:** `warn:a4-heavytail`.

$C_{\mathcal Q} \le C_{\mathrm{TCI}}$, and $C_{\mathcal Q}$ can be *much* smaller — but it is
**not automatically finite**, even for a Gaussian location family. A KL cutoff is also not enough
over arbitrary tail-reweighting families: fixed entropy balls can have unbounded second moments.
Finiteness needs family coercivity/boundedness on the sublevel, quadratic-exponential target tails,
or a modified cost.

**Diagnostic role.** $\pi \propto e^{-|x|^p}$, $1 \le p < 2$, and $q_m = N(m,\sigma^2)$:
$W_2^2(q_m,\pi) \asymp m^2$ while $\mathrm{KL}(q_m\|\pi) \asymp |m|^p$, so
$W_2^2/\mathrm{KL} \asymp |m|^{2-p} \to \infty$. Hence $C_{\mathcal Q}=\infty$ already at
mean-field Gaussian level for $p<2$. For the unrestricted entropy ball, mixing
$\varepsilon_R\asymp r/R^p$ of the target conditioned on $[R,R+1]$ keeps KL below $r$ while its
second moment grows like $rR^{2-p}$.
