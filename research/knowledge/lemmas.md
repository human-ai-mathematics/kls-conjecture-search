# Shared mathematical tools

This file is a compact index of reusable facts. The cited manuscript or ledger label owns the
formal statement; proof dossiers own full arguments and certification. Entries here record only
the fact, its common use, and the main guardrail.

## `lem:linear-test-lower` — linear-test lower bound

**Fact.** For every nonzero $v$,
$$
C_P(\pi)\ge \frac{v^T\operatorname{Cov}_\pi(X)v}{\|v\|^2},
\qquad
C_P(\pi)\ge\lambda_{\max}(\operatorname{Cov}_\pi(X)).
$$

**Use.** Refute a proposed upper bound with an exact covariance witness.

**Guardrail.** An empirical covariance is directional unless its sampling and numerical errors
are controlled.

## `thm:hardy-1d` — weighted Hardy criterion

**Fact.** For a density $p$, median $m$, and weight $a$, let
$B_+=\sup_{x>m}\mu([x,\infty))\int_m^xdt/(a(t)p(t))$ and define $B_-$ analogously. Then
$$
\max(B_+,B_-)\le C_{\mathrm{opt}}\le4\max(B_+,B_-).
$$

**Use.** Decide existence and scale of one-dimensional weighted Poincaré constants.

**Guardrail.** Use one-sided tails; a two-sided tail changes the normalization.

## Holley--Stroock perturbation

**Source.** Holley--Stroock bounded perturbation principle.

**Fact.** If $d\pi=e^{-W}d\nu/Z$ and $\operatorname{osc}(W)\le A$, then
$C_P(\pi)\le e^A C_P(\nu)$, with the analogous log-Sobolev bound.

**Use.** Transfer constants through a uniform density-ratio comparison.

**Guardrail.** Total variation convergence alone does not provide this comparison.

## Tensorization

**Fact.** For $\mu=\bigotimes_i\mu_i$,
$C_P(\mu)=\max_i C_P(\mu_i)$. If coordinate $i$ has weighted constant $C_i$ with weight $a_i$,
then the product has constant $\max_i C_i$ for the form
$\int\sum_i a_i|\partial_i f|^2d\mu$.

**Use.** Lift one-dimensional estimates to product measures.

**Guardrail.** A hierarchical or otherwise dependent law is not a product.

## $T_2$ covariance constraint

**Fact.** Under the convention
$W_2^2(\nu,\pi)\le2C\,\mathrm{KL}(\nu\|\pi)$,
$$
\operatorname{Cov}_\pi(X)\preceq CI,
\qquad
C_{\mathrm{TCI}}(\pi)\ge\lambda_{\max}(\operatorname{Cov}_\pi(X)).
$$

**Use.** Supply a necessary lower constraint for transportation-cost constants.

**Guardrail.** This is not an upper bound or an estimator of the optimal constant.

## `lem:a5-lipschitz` — Lipschitz transport

**Fact.** If $T_\#\nu=\mu$ and $T$ is globally $L$-Lipschitz, then
$C_P(\mu)\le L^2C_P(\nu)$; the same implication holds for $C_{\mathrm{LS}}$ and
$C_{\mathrm{TCI}}$.

**Use.** Compare functional inequalities under a controlled reparameterization.

**Guardrail.** No global comparison follows when the map is not globally Lipschitz.

## `lem:a5-pi-exp-tail` — Poincaré forces exponential tails

**Fact.** If a Euclidean law has Poincaré constant $C<\infty$, then every real
$1$-Lipschitz $f\in L^2$ satisfies
$$
\mathbb E e^{c|f-\operatorname{med}f|}<\infty
\quad\text{for }0<c<\frac{\log2}{2\sqrt C}.
$$

**Use.** Rule out a finite Poincaré constant from a Lipschitz heavy-tail witness.

**Guardrail.** The witness must be globally Lipschitz in the metric of the claimed inequality.

## `prop:a1-euclidean-harmonic` — factor-one inverse-Hessian certificate

**Fact.** For smooth $U$ on $\mathbb R^d$ with
$mI\preceq\nabla^2U\preceq MI$ and $\pi\propto e^{-U}$,
$$
C_P(\pi)\le\mathbb E_\pi\lambda_{\max}((\nabla^2U)^{-1}).
$$

**Use.** Convert an average inverse-curvature estimate into a Poincaré bound.

**Guardrail.** The operative quantity is
$\mathbb E\lambda_{\max}(H^{-1})$, not $\lambda_{\max}((\mathbb EH)^{-1})$; check the source
statement before weakening its regularity assumptions.

## `prop:a1-mode-leverage` — mode-to-tail geometry

**Fact.** With mode Hessian $\widehat H$ and
$\eta=\max_iL_i\sqrt{x_i^T\widehat H^{-1}x_i}$, the source theorem gives radial curvature and
potential envelopes. When its hypotheses hold and $\eta<1$,
$$
C_P\le K_d(\eta)\lambda_{\max}(\widehat H^{-1}),
\qquad K_d(\eta)\to1\quad(\eta\to0).
$$

**Use.** Produce a data-computable certificate and recover the Fisher scale in low-leverage
sequences.

**Guardrail.** $\eta\ge1$ rejects this certificate, not the existence of a Poincaré inequality.

## Unrestricted posterior-mean transport dual

**Source.** `eq:a4-mean-dual` (manuscript label `thm:a4-mean-dual`).

**Fact.** For $X\sim\pi$,
$$
C_{\mathrm{mean},\mathrm{all}}(\pi)
=\sup_{\|u\|=1}\sup_{t\ne0}\frac{2}{t^2}
\log\mathbb E e^{tu^T(X-\mathbb EX)}.
$$

**Use.** Compute unrestricted posterior-mean transport through directional exponential moments.

**Guardrail.** For a restricted family $\mathcal Q$, only
$C_{\mathrm{mean},\mathcal Q}\le C_{\mathrm{mean},\mathrm{all}}$ is automatic.

## Symmetry averaging and block stability

**Source.** `lem:a4-symmetrization` and `prop:a5-block-stability`.

**Fact.** If a finite isometric group preserves $\pi$, then
$\bar q=|G|^{-1}\sum_g g_\#q$ preserves invariant observables and does not increase either
$\mathrm{KL}(q\|\pi)$ or $W_2^2(q,\pi)$. If invariant laws $\pi,\widetilde\pi$ satisfy
$\operatorname{osc}\log(d\widetilde\pi/d\pi)\le\varepsilon$, their invariant and non-invariant
restricted Poincaré gaps change by factors at most $e^{\pm\varepsilon}$.

**Use.** Separate quotient geometry from physical multimodality and test stability of a block
ordering.

**Guardrail.** The ratio $W_2^2/\mathrm{KL}$ need not decrease under averaging, and the
variational family must contain the average.

## `thm:a2-target` — sharp global-oscillation transfer

**Fact.** Fix $d$. If, after mode-Hessian whitening, a posterior has density
$e^{-r_n}/\int e^{-r_n}\,d\gamma$ relative to $\gamma=N(0,I_d)$ with
$\operatorname{osc}(r_n)=o_P(1)$, then
$$
 C_P(\pi_n),\ C_{\mathrm{LS}}(\pi_n),\ C_{\mathrm{TCI}}(\pi_n)
 =(1+o_P(1))\lambda_{\max}(H_n^{-1}).
$$
If $H_n/n\to I(\theta_0)\succ0$ in probability, all three $n$-scaled constants converge to
$\lambda_{\max}(I(\theta_0)^{-1})$.

**Use.** Turn a genuinely global Gaussian comparison into sharp functional-inequality
asymptotics, including the covariance lower bounds needed to match Holley--Stroock upper bounds.

**Guardrail.** The oscillation bound is global and the stated proof fixes $d$; total variation or
a local Laplace expansion is insufficient. Fixed-prior logistic posteriors need not satisfy this
hypothesis, and their global LSI/$T_2$ constants remain prior-scale.

## `prop:a3-hierarchical-prior` — tensorize, then pull back the metric

**Fact.** For independent $z_j\sim N(0,1)$ and independent log-half-Cauchy variables $u,v_j$,
the base product has optimal Poincaré constant $4$. Under
$\theta_j=e^{u+v_j}z_j$, the same optimal constant holds for the pullback energy
$$
 \sum_j e^{2u+2v_j}|\partial_{\theta_j}f|^2
 +\sum_j|\partial_{v_j}f+\theta_j\partial_{\theta_j}f|^2
 +\left|\partial_uf+\sum_j\theta_j\partial_{\theta_j}f\right|^2.
$$

**Use.** Derive a hierarchical weighted metric from independent base coordinates without losing
the product constant, and expose the coefficient--scale and inter-coefficient cross terms forced
by noncentering.

**Guardrail.** This is a prior statement in the exact pullback metric, not a raw Euclidean claim.
A likelihood tilt creates dependence that still needs conditional inequalities and a positive
block gap; coordinate marginal constants alone do not transfer it.

## `prop:a4-logistic-global` — translation-ray variational rigidity

**Fact.** For a finite binary-logistic posterior with Gaussian prior covariance $\Sigma_0$, if a
Gaussian variational family contains every translation of one fixed covariance, then
$$
 C_{\mathrm{mean},\mathcal Q}=C_{\mathcal Q}
 =C_{\mathrm{mean},\mathrm{all}}=C_{\mathrm{TCI}}
 =\lambda_{\max}(\Sigma_0).
$$
Remote translations give the matching lower bound; the likelihood contributes only lower-order
growth along the translation ray.

**Use.** Detect when a location-rich variational family necessarily sees the global prior-tail
scale even though the posterior bulk is much tighter.

**Guardrail.** The conclusion is global and uses the entire translation ray. It does not rule out
posterior-scale localized constants on compact optimizer-centered sublevels, nor does it apply to
a family without those translation witnesses.

## `thm:a4-modified-transport-1d` — real-line tail/cost matching

**Fact.** For a nonatomic full-support log-concave law on $\mathbb R$ and an admissible convex
cost $\alpha$ that is quadratic near zero, a scaled global inequality
$\mathcal T_{\alpha(a\,\cdot)}\le\mathrm{KL}$ holds for some $a>0$ exactly when
$\int e^{\alpha(bx)}\,d\mu(x)<\infty$ for some $b>0$. Thus
$e^{-|x|^p}$, $1\le p\le2$, admits a quadratic-to-$p$-power cost up to scaling, while a
polynomial-tail law admits no nonzero unbounded convex-cost global TCI.

**Use.** Match a one-dimensional log-concave tail to the strongest global convex transport cost
and identify when A4 must switch to a weighted, weak, restricted, or sublevel formulation.

**Guardrail.** The imported criterion is one-dimensional and its scale is existential. It gives
no dependent-posterior theorem, no optimal scale, and no finite localized $W_2^2/\mathrm{KL}$
coefficient for Student or horseshoe targets.

## `thm:a5-two-well-eyring-kramers` — fixed-landscape metastability anchor

**Fact.** For $\mu_\varepsilon\propto e^{-H/\varepsilon}$ under the imported fixed $C^3$ Morse
two-equal-well, unique-index-one-saddle hypotheses,
$$
 C_P(\mu_\varepsilon)
 =\left(1+O(\sqrt\varepsilon|\log\varepsilon|^{3/2})\right)
 \frac{2\pi\varepsilon}{\kappa_1+\kappa_2}
 \frac{\sqrt{|\det\nabla^2H(s)|}}{|\lambda_-(s)|}
 e^{(H(s)-H(m_2))/\varepsilon}.
$$
In particular, at $\varepsilon=1/n$, $n^{-1}\log C_P$ converges to the communication height.

**Use.** Calibrate the raw A5 barrier exponent and prefactor in the simplest certified
metastable landscape.

**Guardrail.** This is a fixed raw two-well theorem. It supplies no uniform random empirical
landscape control, repeated-orbit network capacities, collision-stratum estimates, or quotient
Bernstein--von Mises conclusion.
