---
numbering:
  enumerator: "0.%s"
---

(sec:overview)=
# The Kannan–Lovász–Simonovits frontier

+++ {"part": "abstract"}

The Kannan–Lovász–Simonovits conjecture asks whether linear functions detect, up to a universal constant, the slowest mode of every log-concave measure: $\CP(\mu)\le C\norm{\Cov\mu}_\op$ in every dimension. The best published bound replaces $C$ by $C\log n$; a July 2026 preprint, not yet refereed, claims $C\sqrt{\log n}$. This manuscript explains what stands between those bounds and the conjecture — every known method controls a fixed object, or an average, where the conjecture needs control of an object that adapts to the measure or to the extremal function — and develops four approaches that respond to it: following one cut, or one eigenfunction, along stochastic localization; a deterministic second-order inequality for the Hessian of the moment map; and a spectral gap for resampling along conditional lines. Its results are of three kinds: an inequality that implies the conjecture, with the first non-product families on which it holds; reductions of the conjecture to explicit estimates; and counterexamples to natural intermediate estimates, none of which is a counterexample to the conjecture. Each statement shows next to its title whether it is settled here.

+++

This overview is meant to be read on its own. It states the question and works its smallest cases by hand (Sections [](#sec:kls-orientation) and [](#sec:kls-examples)), summarizes the literature (Section [](#sec:kls-known)), isolates the obstacle every method meets (Section [](#sec:kls-remaining)), gives the main results with the idea of each proof (Section [](#sec:overview-results)), presents three problems for someone who might take them up (Section [](#sec:overview-open)), and ends with how the rest of the manuscript is organised and how its results are checked (Sections [](#sec:reading-paths) and [](#sec:overview-checking)).

(sec:kls-orientation)=
## The question

The conjecture is a statement about *expansion*. A log-concave measure cannot be cut in two without paying for the cut, and KLS asserts that in the right normalization the price does not decay as the dimension grows. Equivalently, in its analytic form, the measure has a spectral gap bounded below independently of $n$: no function of many variables can have large variance and small gradient energy at the same time. A dumbbell — two balls joined by a thin tube — is cheap to cut through its neck; convexity forbids necks, and the conjecture quantifies how completely.

The question came from the analysis of random walks that compute the volume of a convex body, whose mixing time is governed by the Cheeger constant [@KannanLovaszSimonovits1995].

(subsec:kls-conjecture)=
### The conjecture

Let $\mu$ be a log-concave probability measure on $\R^n$, that is, one with a density $e^{-V}$ for a convex $V$ (possibly on a lower-dimensional affine subspace); the uniform measure on a convex body and every Gaussian are examples. Write $\mu^+(A)$ for the Minkowski boundary measure of a Borel set $A$, and define the Cheeger constant and its reciprocal, the inverse Cheeger scale,

$$
h_\mu=\inf_{A}\frac{\mu^+(A)}{\min\{\mu(A),1-\mu(A)\}},
\qquad
\PsiKLS_\mu=h_\mu^{-1}.
$$

The Poincaré constant $\CP(\mu)$ is the least constant with

$$
\Var_\mu(f)\le\CP(\mu)\int_{\R^n}|\nabla f|^2\dd\mu
$$

for every locally Lipschitz $f$; it is the inverse of the spectral gap of the diffusion naturally attached to $\mu$.

:::{warning} The $\psi$ convention
:label: rem:psi-convention
Part of the literature calls $h_\mu$ “the KLS constant” and part calls $h_\mu^{-1}$ by the same name, both writing $\psi_\mu$. This document always writes $h$ for the expansion constant and $\PsiKLS=h^{-1}$ for the inverse scale, and never uses the bare symbol $\psi$ for either. Combined with $\CP\asymp\PsiKLS^2$ below, the convention accounts for most apparent contradictions between quoted exponents: a bound $\PsiKLS_n\lesssim(\log n)^{a}$ is the same statement as $\CP\lesssim(\log n)^{2a}$, so the same theorem is quoted with two different exponents depending on which constant the source names.
:::

For log-concave measures the Cheeger and reverse Cheeger (Buser–Ledoux) inequalities give the two-sided comparison

```{math}
:label: eq:cheeger-two-sided
\tfrac14\le\frac{\PsiKLS_\mu^2}{\CP(\mu)}\le\pi ,
```

so $\CP\asymp\PsiKLS^2$ with universal constants; the explicit constants are recorded in [@Klartag2023Logarithmic; @Milman2009Isoperimetric]. The lower bound is Cheeger's inequality in the normalization $\CP(\mu)\le4h_\mu^{-2}$ used throughout.

A measure is *isotropic* if it is centred and its covariance is the identity.

:::{prf:conjecture} KLS
:label: conj:kls
There is a universal constant $C<\infty$ such that, for every dimension, every isotropic log-concave $\mu$, and every locally Lipschitz $f$,

$$
\Var_\mu(f)\le C\int_{\R^n}|\nabla f|^2\dd\mu.
$$

Equivalently up to universal constants, the Cheeger constants of all such measures are bounded below uniformly in the dimension.
:::

Write

```{math}
:label: eq:hstar-def
\hstar_n=\inf\bigl\{h_\nu:\ \nu\ \text{isotropic log-concave on }\R^n\bigr\}.
```

Thus [](#conj:kls) is equivalently $\inf_n\hstar_n>0$, up to the comparison [](#eq:cheeger-two-sided).

Three formulations are used interchangeably below.

(a) **Isotropic form.** For isotropic $\mu$ (that is, $\E_\mu X=0$ and $\Cov_\mu(X)=I_n$),

$$
\CP(\mu)=O(1),\qquad \PsiKLS_\mu=O(1),\qquad h_\mu=\Omega(1).
$$

(b) **Affine form.** For every log-concave $\mu$,

```{math}
:label: eq:kls-affine
\CP(\mu)\le C\norm{\Cov\mu}_\op .
```

The reverse inequality $\CP(\mu)\ge\norm{\Cov\mu}_\op$ is automatic: testing the Poincaré inequality on the linear function $f(x)=\inner{x}{v}$ with $v$ a top eigenvector of $\Cov\mu$ gives $\Var_\mu f=\inner{\Cov\mu\,v}{v}$ and $\int|\nabla f|^2\dd\mu=|v|^2$. So [](#eq:kls-affine) says exactly this: *up to a universal constant, linear functions already detect the slowest mode of every log-concave measure.*

(c) **Geometric form.** The least-expanding arbitrary cut of a convex body is, up to a universal factor, no worse than the least-expanding hyperplane cut [@KannanLovaszSimonovits1995].

Applying Poincaré to $f(x)=|x|^2$ in isotropic position gives

```{math}
:label: eq:kls-implies-thin-shell
\Var(|X|^2)\le4n\,\CP(\mu),
```

the implication “KLS $\Rightarrow$ thin shell” discussed in Section [](#subsec:kls-solved-neighbours). No dimension-free converse from this one radial estimate to KLS is known, and none has been disproved within the log-concave class.

(sec:kls-examples)=
## Examples by hand

The ratio $\CP(\mu)/\norm{\Cov\mu}_\op$ is at least $1$ by the linear test above; the conjecture says it is bounded. Here it is in the smallest cases.

**The Gaussian.** For the standard Gaussian, $\CP=1=\norm{\Cov}_\op$ and linear functions are extremal: the ratio is exactly $1$ in every dimension.

**An interval.** For the uniform measure on $[0,1]$, $\Var(x)=1/12$. The slowest mode is $f(x)=\cos\pi x$, with $\Var f=\tfrac12$ and $\int f'^2=\pi^2/2$, so $\CP=1/\pi^2$ (Wirtinger's inequality) and $\CP/\Var=12/\pi^2\approx1.22$. The slowest mode is not linear, but a linear function is within a factor $1.22$ of it.

**The exponential.** Let $\mu$ have density $e^{-x}$ on $[0,\infty)$, so $\Var(x)=1$. For $f(x)=e^{ax}$ with $0<a<\tfrac12$,

$$
\Var_\mu f=\frac1{1-2a}-\frac1{(1-a)^2},
\qquad
\int f'^2\dd\mu=\frac{a^2}{1-2a},
\qquad\text{so}\qquad
\frac{\Var_\mu f}{\int f'^2\dd\mu}=\frac1{(1-a)^2}\xrightarrow[a\to1/2]{}4 .
$$

Hence $\CP(\mu)\ge4\Var(\mu)$. This is the worst case on the line: every one-dimensional log-concave law has $\CP\le4\Var$, the one-dimensional case of the Kannan–Lovász–Simonovits bound [@KannanLovaszSimonovits1995; @cattiaux2018poincare], which [](#thm:cmh-1d) contains. The near-extremal functions $e^{ax}$ leave $L^2$ at $a=\tfrac12$: the slowest mode of the exponential escapes to infinity.

**Products.** The Poincaré constant of a product is the largest Poincaré constant of its factors (tensorization), so a product of $n$ isotropic one-dimensional log-concave laws has $\CP\le4$ in every dimension; [](#prop:products) records the corresponding fact for the Cheeger constant. The cube $[0,1]^n$ and the product of $n$ exponentials are therefore harmless. The conjecture is about everything that is not a product: simplices, cones, balls of non-Euclidean norms, and log-concave measures with no symmetry at all.

No family of log-concave measures is known for which the ratio in [](#eq:kls-affine) grows with $n$. The whole gap is in the upper bound; it is not a gap between competing upper and lower power laws.

(sec:kls-known)=
## What was known

The quantitative frontier, the two neighbouring conjectures that have been settled and why settling them did not settle KLS, the architecture of the argument that produces the current best bound, and the place where the surviving logarithm enters.

(subsec:kls-status)=
### The quantitative history

Set

$$
\PsiKLS_n=\sup_\mu\PsiKLS_\mu,
\qquad
C_{\mathrm P,n}=\sup_\mu\CP(\mu),
$$

the suprema over isotropic log-concave measures on $\R^n$. The best published bound is Klartag's $\PsiKLS_n\lesssim\sqrt{\log n}$, that is $C_{\mathrm P,n}\lesssim\log n$ [@Klartag2023Logarithmic], stated here as [](#thm:klartag-logn). A first-version preprint of Letwin (arXiv, 27 July 2026) claims $\PsiKLS_n\lesssim(\log n)^{1/4}$, that is $C_{\mathrm P,n}\lesssim\sqrt{\log n}$ [@Letwin2026QuadraticKLS]; it has not been refereed, and Section [](#subsec:mm-audit) reads it closely. Every statement of this manuscript that uses it carries that dependence in its own text.

Exponents are given for $\PsiKLS_n$ and for $C_{\mathrm P,n}$ side by side, precisely because of [](#rem:psi-convention).

| Date | $\PsiKLS_n$ | $C_{\mathrm P,n}$ | Main development |
|---|---|---|---|
| 1995 | $O(n^{1/2})$ | $O(n)$ | The localization lemma [@KannanLovaszSimonovits1995]. |
| 1995–2011 | down to $O(n^{5/12})$ | — | Bobkov's radial inequality fed by successively better thin-shell bounds; the last notable pre-localization record [@GuedonMilman2011]. |
| 2012/13 | $O(n^{1/3}\sqrt{\log n})$ | $O(n^{2/3}\log n)$ | Stochastic localization [@Eldan2013ThinShell]. |
| 2016; 2024 | $O(n^{1/4})$ | $O(n^{1/2})$ | Fixed Gaussian tilt and the $\Tr(A_t^2)$ stopping argument [@LeeVempala2018; @LeeVempala2024]. |
| 2020/21 | $\exp O(\sqrt{\log n\log\log n})$ | same class | Iterated high-Schatten potentials and affine preconditioning [@Chen2021]. |
| 2022 | $O(\log^5 n)$ | $O(\log^{10}n)$ | First polylogarithmic bound; heat flow, spectral projections, $H^{-1}$ [@KlartagLehec2022Polylog]. |
| 2022 | $O(\log^{3.2226}n)$ | $O(\log^{6.4452}n)$ | Two localization representations and spiked-spectrum estimates [@JambulapatiLeeVempala2022KLS]. |
| 2023 | $O(\sqrt{\log n})$ | $O(\log n)$ | Improved Lichnerowicz plus short-time covariance control [@Klartag2023Logarithmic]. |
| July 2026, preprint | $O((\log n)^{1/4})$ | $O(\sqrt{\log n})$ | Sharp quadratic Poincaré inequality, giving $\kappa_n=O(1)$ [@Letwin2026QuadraticKLS]. |

:::{prf:remark} Reading the table
:label: rem:history-table-caveats
Two entries deserve care. The 2016/2024 row is one result: the Lee–Vempala preprint of 2016 appeared in final form in the Annals in 2024, and the bibliography records both. The $O(n^{5/12})$ entry summarizes a sequence of thin-shell improvements rather than a single paper, and is quoted here only to mark the pre-localization ceiling. Separately, the bibliography contains [@vempala2016kls], a 2016 announcement of a proof of the full conjecture; it is not a milestone in this table, and it is listed in the bibliography for completeness of the record only.
:::

(subsec:kls-solved-neighbours)=
### Solved neighbours that are not KLS

The classical implication structure is

```{math}
:label: eq:kls-implication-chain
\mathrm{KLS}\ \Longrightarrow\ \text{thin shell}\ \Longrightarrow\ \text{slicing},
```

and no reverse implication is known in a dimension-free form. Both of the weaker conjectures have now moved decisively. Neither resolution proves KLS, and it is worth being precise about why.

**Slicing.** Bourgain's slicing conjecture asks whether the isotropic constants $L_n$ are universally bounded. Guan proved $L_n\lesssim\log\log n$ and, in the process, obtained the stochastic-localization trace estimate that turned out to be decisive [@Guan2024]. Klartag and Lehec combined that estimate with $M$-ellipsoids and Shannon–Stam stability to prove $\sup_nL_n<\infty$, published in 2025 [@KlartagLehec2025Slicing]; Bizeul subsequently gave an alternative proof through small-ball estimates [@Bizeul2025SmallBallSlicing]. Slicing controls determinant and volume information, not the bottom of the full spectrum.

**Thin shell.** For isotropic log-concave $X$ the thin-shell conjecture asks for $\Var(|X|^2)\le Cn$, equivalently $\E(|X|-\sqrt n)^2\le C$. Klartag and Lehec gave a proof via parallel couplings of exponential tilts, nonlinear filtering, optimal transport, $H^{-1}$ estimates, and Guan-type covariance control [@KlartagLehec2025ThinShell]. A July 2026 first-version preprint of Chen and Klartag sharpens it to the optimal $\Var(|X|^2)\le8n$, with equality for products of centered exponentials, together with a sharp third-moment-tensor bound [@ChenKlartag2026SharpThinShell]; both statements are recorded as [](#thm:chen-klartag-thin-shell) and [](#thm:chen-klartag-third-moment).

**Why this does not close the gap.** Eldan's reverse estimate bounds the inverse Cheeger scale by a weighted average of thin-shell parameters $\sigma_k$ [@Eldan2013ThinShell],

```{math}
:label: eq:eldan-reverse
\PsiKLS_n\le C\sqrt{(\log n)\sum_{k=1}^n\frac{\sigma_k^2}{k}} .
```

Even with $\sigma_k=O(1)$ the harmonic sum contributes a $\log n$, and [](#eq:eldan-reverse) yields only $\PsiKLS_n\lesssim\log n$, not $O(1)$. Radial concentration constrains one observable, $|x|^2$; KLS quantifies over every function and every measurable cut. The same asymmetry recurs, in sharper form, for Letwin's preprint: it eliminates every *quadratic* witness, and the first eigenfunction of a general log-concave diffusion need not be quadratic.

(subsec:kls-architecture)=
### The present proof architecture

Modern progress on KLS is a hybrid argument with four ingredients, no one of which replaces another. Figure [](#fig:kls-architecture) is the shape of the current best bound.

- **Stochastic localization creates Gaussian curvature.** One observes $X\sim\mu$ through Gaussian noise of decreasing size and follows the conditional law $\mu_t$; the tilt $e^{-t|x|^2/2}$ makes $\mu_t$ $t$-strongly log-concave, and on average $\mu_t$ is $\mu$ (Section [](#sec:family-sl)).

- **Matrix martingale estimates control how much covariance survives.** The covariance process $A_t=\Cov(\mu_t)$ obeys an exact Riccati SDE whose noise is the third-moment tensor.

- **Bochner/Lichnerowicz converts curvature plus covariance into a spectral gap.** Klartag's improved comparison $\CP\le\sqrt{\norm{\Cov}_\op/t}$ ([](#thm:improved-lichnerowicz)) is what makes short-time curvature usable.

- **Letwin's preprint supplies a sharp third-moment estimate**, through moment maps, Monge–Ampère, Stein kernels, and $H^{-1}$ (Section [](#sec:family-moment-map)).

::::{figure}
:label: fig:kls-architecture

```{mermaid}
flowchart LR
  sl["Stochastic localization"] --> curv["Gaussian curvature t"]
  sl --> cov["Covariance process A_t"]
  cov --> pot["Third moments, matrix potentials"]
  mm["Moment map and Monge–Ampère"]:::new --> qp["Sharp quadratic Poincaré"]:::new
  qp --> kap["κ_n = O(1)"]:::new
  kap --> pot
  curv --> il["Improved Lichnerowicz"]
  pot --> il
  il --> cp["C_P ≲ √(log n)"]:::res
  cp --> psi["Ψ_KLS ≲ (log n)^(1/4)"]:::res
  classDef new fill:#eef2fb,stroke:#1f3a73,stroke-width:2px
  classDef res fill:#f2f2f2
```

The architecture of the current best bound. Boxed in colour: the July 2026 preprint contribution. It does not replace stochastic localization; it discharges a crucial input to the localization–Lichnerowicz pipeline.
::::

**The exact bridge, and where the logarithm lives.** Define the directional third-moment parameter

```{math}
:label: eq:kappa-def
\kappa_n=\sup_{\mu,\theta}\bigl\lVert\E_\mu[\inner{X}{\theta}X\otimes X]\bigr\rVert_{\HS},
```

the supremum over isotropic log-concave $\mu$ on $\R^n$ and $\theta\in S^{n-1}$. The localization–Lichnerowicz pipeline delivers

```{math}
:label: eq:kls-bridge
\boxed{\ C_{\mathrm P,n}\lesssim\kappa_n\sqrt{\log n}\ }
```

(Section [](#subsec:sl-where-the-log-lives)), and Letwin's $\kappa_n\le2\sqrt2$ ([](#prop:letwin-kappa)) is what turns [](#eq:kls-bridge) into the preprint's bound.

The surviving $\sqrt{\log n}$ is not hidden in the moment-map calculation. Klartag–Lehec smooth the maximum covariance eigenvalue by log-trace-exp,

$$
\Phi_t=\frac1\beta\log\Tr\bigl(e^{\beta A_t}\bigr),
\qquad
\norm{A_t}_\op\le\Phi_t\le\norm{A_t}_\op+\frac{\log n}\beta ,
$$

and approximating $\lmax$ to within a constant forces $\beta\asymp\log n$. The Itô drift is then of size $O(\kappa_n^2\log n)$, so covariance control survives only until $t_*\asymp1/(\kappa_n^2\log n)$, and improved Lichnerowicz converts that time into $\CP\lesssim t_*^{-1/2}\lesssim\kappa_n\sqrt{\log n}$. The logarithm is the *entropy cost of replacing a matrix maximum by a soft maximum over $n$ directions*. That diagnosis is what makes target 3 of Section [](#sec:kls-synthesis) concrete.

(sec:kls-remaining)=
## The obstacle every method meets

Conditional on [@Letwin2026QuadraticKLS], $\kappa_n=O(1)$ and every quadratic witness is eliminated: the remaining difficulty is no longer quadratic forms or third moments. What survives is a difficulty of a different type, and this section states it in the two forms every approach in this manuscript must answer.

(subsec:kls-adaptive-residue)=
### Fixed and averaged, against adaptive and uniform

Every method in the literature controls something. Needles control one-dimensional conditional measures sharply; stochastic localization controls short-time covariance and, conditionally, third moments; heat-flow and $H^{-1}$ arguments control coordinate and quadratic spectral mass; moment maps control fixed deterministic matrix energies $\E\Tr(BHBH)$; parallel coupling controls linear exponential tilts; Brownian transport controls averaged derivatives to within a polylogarithm. Section [](#subsec:synthesis-table) tabulates these one by one.

What none of them controls is the same object when it is allowed to *adapt*. In every row of that table the estimate holds for a fixed matrix, a fixed direction, a fixed tilt, or on average along a path, and KLS needs it uniformly, for an object that may depend on the measure or on the extremizing function. The gap is not a constant to be improved; it is a quantifier in the wrong place. Each of the four approaches of this manuscript is a different way around that quantifier.

(subsec:kls-spike-obstruction)=
### The covariance spike, and why the direct repair fails

The most natural repair is to bound $\norm{A_t}_\op$ better. It cannot work, because the statement it needs is false, and false for a measure that satisfies the conjecture.

:::{prf:proposition} Covariance spikes are compatible with KLS
:label: prop:covariance-spike
Let $\mu$ be the law of $n$ independent centered one-sided exponential coordinates and let $G$ be a standard Gaussian independent of $X\sim\mu$. Then $\CP(\mu)=O(1)$ by tensorization, yet

$$
\Prob\!\left(
\bigl\lVert\Cov(X\mid X+\sqrt sG)\bigr\rVert_\op\ge c_{\rm sp}s
\right)
\ge1-\left(1-\tfrac12e^{-s}\right)^n
$$

for a universal $c_{\rm sp}>0$. Consequently, for $s\le\log n$,

$$
\E\bigl\lVert\Cov(X\mid X+\sqrt sG)\bigr\rVert_\op\gtrsim s
\qquad\text{and}\qquad
\Prob\!\left(
\bigl\lVert\Cov(X\mid X+\sqrt sG)\bigr\rVert_\op\ge c_{\rm sp}s
\right)\ge1-e^{-1/2}.
$$
:::

This is due to Klartag and Lehec (Section 8.1 and Proposition 65 of [@KLnotes]). The mechanism fits in a line. A centred exponential coordinate has a flat tail: conditionally on a large observation, the prior barely varies on the scale of the noise, so the posterior of that coordinate is essentially the Gaussian noise itself, of variance $s$. One coordinate out of $n$ is that large with probability about $e^{-s}$, so as long as $s\lesssim\log n$ some coordinate is, and the top conditional eigenvalue is of order $s$ — while the product of exponentials has Poincaré constant $4$.

The consequence is structural: *uniform operator-norm control of the conditional covariance at every scale is false, even for a measure that satisfies KLS.* An argument whose only use of the localization path is a pathwise bound on $\norm{A_t}_\op$ is attempting to prove something stronger than KLS, and something that is not true. A successful potential must exploit eigenvalue profiles, averaging, tensorization, or the particular extremizing function — not better pointwise bounds. The consequence also cuts the other way: rare spikes can be *harmless*, and a potential that charges the full largest eigenvalue whenever a spike occurs is overcharging.

(subsec:kls-tensorization-test)=
### The tensorization test

That gives a cheap and discriminating test, which any proposal should pass before it is developed.

> *Evaluate the proposed potential on a product of $n$ independent copies of a one-dimensional measure. A quantity that is not tensorization-aware will charge $n$ independent coordinates $n$ times for a phenomenon that costs $O(1)$.*

A proposal that fails it is not merely inefficient; it is false at scale, and the failure is usually visible in a page. Section [](#sec:product-stress) applies it to the all-cut Carleson estimate of the fixed-cut approach, where it shows that no fixed cut depending on a single coordinate can violate that estimate, even when that coordinate's variance inflates ([](#cor:refutation)), and isolates what remains in the adapted alignment problem [](#q:alignment) for cuts of unbounded coordinate complexity; [](#prop:weighted-spectator-obstruction) below is the same test applied to a weighted estimate.

(sec:overview-results)=
## The main results in short

The results fall into three groups: an inequality that implies KLS and the families where it holds; two reductions of KLS to explicit estimates; and the limits of following a single cut, with the counterexamples that fix them. The idea of each proof is given here; the statements themselves are in the chapters that follow, where each one's status links to its full proof.

(subsec:overview-cmh)=
### A deterministic inequality that implies KLS

The first results use no stochastic localization. They start from the *moment map* of Cordero-Erausquin and Klartag [@CorderoErausquinKlartag2015MomentMeasures]: a centred log-concave $\mu$ is the image of $e^{-\varphi(y)}\dd y$ under $\nabla\varphi$ for an essentially unique convex $\varphi$. Transported to $\mu$, the Hessian $H=D^2\varphi\circ(\nabla\varphi)^{-1}$ is a *Stein kernel*: $\E_\mu\Tr(H\,D^2g)=\E_\mu\inner{x}{\nabla g}$ for every test function $g$, and $\E_\mu H=\Sigma=\Cov\mu$. It defines a generator $L_\mu g=\Tr(HD^2g)-\inner{x}{\nabla g}$, symmetric for $\mu$, which for the standard Gaussian ($H=\Id$) is the Ornstein–Uhlenbeck operator. The *canonical moment-Hessian constant* $\CMH(\mu)$ of [](#def:cmh) is the best constant in $\E_\mu\inner{H\nabla g}{\Sigma^{-1}H\nabla g}\le C\,\E_\mu(L_\mu g)^2$.

**The inequality implies the affine Poincaré inequality with no loss.** [](#thm:cmh-implies-affine-poincare) states $\CPaff(\mu)\le\CMH(\mu)$, where $\CPaff$ is the Poincaré constant measured against $\inner{\Sigma\nabla f}{\nabla f}$; a universal bound $\CMH\le4$ would give KLS with constant $4$. The mechanism is one Cauchy–Schwarz. Given a centred $f$, solve $-L_\mu g=f$ (up to a spectral truncation). Then

$$
\norm f_2^2=\E_\mu\inner{\nabla f}{H\nabla g}
\le\bigl(\E_\mu\inner{\Sigma\nabla f}{\nabla f}\bigr)^{1/2}
\bigl(\E_\mu\inner{H\nabla g}{\Sigma^{-1}H\nabla g}\bigr)^{1/2},
$$

and the last factor is at most $\CMH^{1/2}\norm{L_\mu g}_2=\CMH^{1/2}\norm f_2$. Only the symmetry, the positivity and the Stein identity of $H$ are used, which is why the constant passes intact. The statement is for a regular class of measures; [](#lem:affine-poincare-w2-liminf) and [](#q:cmh-approximation) carry the affine Poincaré inequality to every log-concave law along approximants, given the uniform control of [](#ass:uniform-cmh-approximants). The converse direction is less clear: a weighted Hodge decomposition ([](#prop:cmh-hodge), [](#rem:cmh-stronger-than-kls)) splits the numerator of $\CMH$ into a gradient part, which is *exactly* the affine Poincaré quotient, and a divergence-free part that vanishes on the line but not beyond. So in dimension at least two the inequality asks for something besides KLS, and no measure separating the two is exhibited.

**Where it holds.** [](#thm:cmh-1d) computes $\CMH=\CP/\Var$ exactly on the line, so the exponential has constant exactly $4$; [](#thm:cmh-product) says the constant of a product is the largest constant of its factors; and [](#thm:cmh-dirichlet) gives $\CMH\le4$ for every log-concave Dirichlet law — the law of $(\gamma_1,\dots,\gamma_m)/\sum_j\gamma_j$ for independent $\gamma_i\sim\mathrm{Gamma}(\alpha_i)$ with all $\alpha_i\ge1$, which includes the uniform measure on a simplex. By [](#cor:cmh-dirichlet-poincare), every such law, and every product, linear image or convolution of independent ones, has $\CPaff\le4$. On the line the divergence-free part vanishes and the inequality becomes an identity. For products, the cross terms $\E[(L_ig)(L_jg)]$ between factors are nonnegative, so the denominator only gains. The Dirichlet family is the first non-product case, and its proof lifts the simplex to the independent Gamma variables: a function on the simplex is a function of the Gammas that is homogeneous of degree zero. The Bochner identity of the Gamma product, a completed square, and the Euler relation that homogeneity imposes reduce the claim to a scalar minimization in one variable per coordinate, which is where $\alpha_i\ge1$ — log-concavity — is spent. Dimension-free Poincaré bounds for simplices were available qualitatively [@KolesnikovMilman2016OrliczKLS]; the constant $4$ and the stronger moment-Hessian inequality are what these statements add.

The product case is also a warning. A product of centred exponentials has $\CMH=4$ *exactly*, with no slack ([](#rem:cmh-saturation-risk)): the inequality one needs in general is already tight on a product, so a log-concave perturbation of that product that raised the constant would refute it. [](#q:cmh-solenoidal-perturbation) is the second-order form of that question, and conjectures that no admissible log-concave perturbation raises the constant to second order.

**The linear test is a third-moment problem.** Testing the inequality on linear functions gives its cheapest necessary condition, $\E_\mu H^2\preceq4\,\Id$ in isotropic position ([](#conj:gate-zero)). [](#lem:linear-sector-third-moment) identifies what that condition contains: for every unit $a$,

$$
\E_\mu\abs{Ha}^2=1+\tfrac14\norm{T_3(a)}_{\HS}^2+\E_\mu\abs{v_a}^2,
\qquad T_3(a)=\E_\mu\bigl[\inner Xa\,X\otimes X\bigr],
$$

with a remainder $v_a$ orthogonal to all affine functions. The mechanism is the Stein identity applied to quadratic test functions, which says that $\E_\mu[H_{ij}X_k]$ is half the third-moment tensor; projecting the column $Ha$ onto the span of $1,X_1,\dots,X_n$ leaves $a+\tfrac12T_3(a)X$, and Pythagoras gives the identity. By [](#cor:gate-zero-third-moment), an operator bound $\E H^2\preceq c\,\Id$ forces $\norm{T_3(a)}_{\HS}\le2\sqrt{c-1}$. On the *exponential cones* — density $\propto x_1^{\beta-n}e^{-x_1}$ on the cone over a centred convex body $K$ — the moment potential lifts from that of the base, and the axis column of the kernel is the position vector itself, so the axis value of the linear test is an explicit Gamma moment, $1+n/\beta$ ([](#prop:cone-linear-sector)); over a cube base the whole matrix is in closed form ([](#cor:cube-cone-gate-zero)).

**Matrix inequalities over fixed matrices do not give the linear test.** The moment-map preprint proves $\E\Tr(BHBH)\le2\Tr(B^2)$ for every fixed symmetric $B$ ([](#thm:letwin-moment-map)). [](#prop:letwin-not-gate-zero) builds, for every $m\ge18$, a random positive semidefinite matrix with $\E H=\Id$ satisfying all these inequalities and yet $\lmax(\E H^2)>4$. The two quantities differ by one commutator, $\Tr(B^2H^2)=\Tr(BHBH)+\tfrac12\norm{[B,H]}_{\HS}^2$, and the countermodel — an arrowhead matrix built from a uniform point $z$ of $S^{m-1}$ — makes the commutator large in expectation while keeping every fixed-$B$ energy within budget. The countermodel is not a moment-map Hessian, so it says nothing about [](#conj:gate-zero) itself; it says that a proof must use more of the moment-map structure than matrix algebra over fixed $B$. It is the fixed-versus-adaptive pattern of Section [](#subsec:kls-adaptive-residue) once more.

(subsec:overview-reductions)=
### Two reductions of KLS to explicit estimates

**Following one eigenfunction.** Run stochastic localization on an isotropic log-concave $\mu$ and follow a first eigenfunction $f$: set $g_t=\Cov_{\mu_t}(f,X)$, $H_t=\E_{\mu_t}[(f-\E_{\mu_t}f)(X-a_t)^{\otimes2}]$ and $A_t=\Cov(\mu_t)$. [](#prop:spectral-sufficiency) says that the occupation estimate [](#q:mm-spectral-occupation) — a bound of the time-integrated source $\E\int_0^t\norm{H_s}_{\HS}^2$ by a linear budget, a lower-order term, and the full damping $\E\int_0^t2g_s^TA_sg_s$ — implies KLS. The mechanism: $g_t$ obeys an exact equation, $\dd g_t=H_t\,\dd W_t-A_tg_t\,\dd t$, so $\E\abs{g_t}^2$ grows by the source and decreases by the damping, with no inequality spent. The hypothesis lets the damping cancel the source; Grönwall's lemma then bounds how much of $f$ has been learned by a universal time $T_*$, so $\E\Var_{\mu_{T_*}}(f)\ge\tfrac12$; and the Brascamp–Lieb bound $\CP(\mu_t)\le1/t$ for the localized measure turns that into $\lambda\ge T_*/2$. The eigenfunction is the right object because, unlike the top covariance eigenvalue, it ignores spikes in directions it does not use. As a calibration, [](#prop:mm-window-occupation) shows, conditionally on the quadratic Poincaré inequality of the preprint ([](#thm:letwin-qcts)), that the estimate holds with $C_0=34$, $C_1=0$ on a window of length $1/\log^2n$; that recovers only $\CP\lesssim\log^2n$, weaker than [](#thm:klartag-logn), and locates the whole difficulty in the length of the window.

**Resampling along conditional lines.** For a direction $\theta$, resample $X\sim\mu$ along the line through $X$ in direction $\theta$ from its conditional law, and divide the resulting variance of $f$ by the conditional variance of the line coordinate. Averaging over an isotropic frame $\rho$ of directions gives a Dirichlet form $\mathcal D_{\mu,\rho}$. [](#lem:conditional-fiber-form) shows that this form is well defined and closed, that $\mathcal D_{\mu,\rho}(f)\le4\int\abs{\nabla f}^2\dd\mu$ for log-concave $\mu$, and that linear functions have $\mathcal D_{\mu,\rho}(\inner ax)=\abs a^2$. Hence a frame with a dimension-free gap for $\mathcal D_{\mu,\rho}$ gives KLS with constant $4C$ ([](#q:conditional-fiber-frame)). The comparison with the gradient is the sharp one-dimensional inequality $\CP\le4\Var$ of Section [](#sec:kls-examples), applied on each line; the normalization by the conditional variance is chosen so that linear functions carry exactly their Euclidean energy, so the form cannot lose on the functions that define the covariance. What it may lose on is shown by the most natural frame on the simplex, the root directions $(e_i-e_j)/\sqrt2$: [](#prop:conditional-fiber-root-obstruction) shows its gap is $O(m^{-2})$ on the isotropic simplex of dimension $m-1$. The witness is the indicator of a corner $\{mP_1>m-\varepsilon\}$: only the $m-1$ root directions through that vertex can move it, and in the normalization of the form each carries weight of order $m^{-3}$ there. The simplex itself has a dimension-free Poincaré constant by [](#cor:cmh-dirichlet-poincare), so the frame, not the measure, is at fault. The failure does not show on polynomials: on functions of degree at most two, that frame's form is at least $(m+2)(m+3)/(5m^2)>1/5$ times the variance ([](#lem:fiber-root-degree-two)).

(subsec:overview-one-cut)=
### Following one cut: a ceiling and two counterexamples

The oldest approach through localization follows one cut $E$ of mass $\tfrac12$ and tracks the excess $e_t(E)$ of its boundary over the isoperimetric profile of the localized measure.

**The near-worst bootstrap.** [](#thm:bootstrap) says that, for a measure whose Cheeger constant is within a factor $1+\varepsilon$ of the smallest in its dimension, the excess propagates along localization with one quantity as the only interface, $\Xi_T(\mu)=\int_0^T\E(\lmax(A_t)-1)_+\dd t$. Two deterministic comparisons do the work: the isoperimetric profile of a log-concave measure is concave and symmetric, so its Cheeger constant is read at mass $\tfrac12$; and whitening a localized measure of covariance $A_t$ loses at most $\lmax(A_t)^{1/2}$ against the worst isotropic measure of the same dimension. Near-worstness compares the localized Cheeger constant with that of $\mu$, and every loss is charged to $(\lmax(A_t)-1)_+$. The published covariance estimates give $\Xi_T\le C(1+\log\log n)$ ([](#cor:loglog)). But [](#prop:ceiling) shows that the input which would make the bootstrap close — $\Xi_{T_0}\le\kappa T_0$ at a small universal time — already implies KLS by itself. The bootstrap is the natural way to feed the worst measure back into itself; the ceiling says that anything which improves it must bring something the bootstrap does not contain.

**Independent spectators break global covariance weights.** The fixed-cut approach wanted a propagation estimate for the excess weighted by $(1+\norm{A_t}_\op)^{5/2}$, stated as [](#q:weighted). [](#prop:weighted-spectator-obstruction) exhibits, for any proposed constants, a product of centred exponentials and a cylinder cut with arbitrarily small initial excess on which that estimate fails. The mechanism is the covariance spike of Section [](#subsec:kls-spike-obstruction): take a good cut in a few coordinates and add many independent exponential coordinates it does not depend on. Their spikes inflate the global weight and depress the isoperimetric profile of the localized measure, while the cut does not notice them — the estimate fails the tensorization test. Removing the weight does not help ([](#prop:spectator-excess-rate-obstruction)): a surviving estimate must also change its remainder, for instance to one linear in $T$, or assume the measure near-worst, as [](#thm:bootstrap) does. Every witness is a product, and so satisfies KLS.

(sec:overview-open)=
## Problems for someone who might take them up

Three problems are presented here for a reader who wants to start. Each is stated precisely in its chapter, and none of the three has an answer in the literature that we are aware of. The first and third imply KLS, so they are research problems at least as hard as the conjecture itself; the second does not imply KLS and is a research problem in its own right, with a concrete equality set to test against.

**The occupation estimate for one eigenfunction, [](#q:mm-spectral-occupation).** *Why it matters:* by [](#prop:spectral-sufficiency) it implies KLS, and it asks for control of an object — the tensor $H_t$ of one fixed eigenfunction — that ignores covariance spikes in directions the eigenfunction does not use, so it is not ruled out by [](#prop:covariance-spike). *What there is:* a time-weighted version with no hypothesis ([](#lem:mm-time-weighted-fixed-source)) and, conditionally on the quadratic Poincaré preprint, the estimate on a window of length $1/\log^2n$ ([](#prop:mm-window-occupation)). *Where to start:* Section [](#subsec:spectral-window-chain). What is missing is the charge of the source after the first covariance spike, on a window of universal length; the budgets established so far are exactly saturated by one explicit profile, so a new input is needed there.

**Sharp gate zero, [](#conj:gate-zero-sharp).** It asks whether $\E H^2\preceq2\,\Id$ for the Stein kernel of the moment map of every isotropic log-concave measure. *Why it matters:* it is the operator form of the Chen–Klartag trace inequality $\Tr\E H^2\le2n$ ([](#thm:chen-klartag-moment-hessian)); by [](#cor:gate-zero-third-moment) it contains the sharp directional third-moment bound $\kappa_n\le2$, where the preprint literature reaches $2\sqrt2$ ([](#prop:letwin-kappa)); and it refines [](#conj:gate-zero), the linear shadow of the moment-Hessian inequality. It does not imply KLS, and a counterexample to it would leave KLS untouched. *What there is:* products of centred exponentials attain it in every direction, and every exponential cone with $\beta=n$ attains it in its axis direction, whatever the base ([](#prop:cone-linear-sector)); the cube cone satisfies it with a closed-form matrix ([](#cor:cube-cone-gate-zero)). Any argument must be tight on these, and by [](#prop:letwin-not-gate-zero) no argument through fixed-matrix energies alone can succeed. *Where to start:* Section [](#subsec:gate-zero), and the spectral resolution of the linear sector in [](#lem:cmh-linear-spectral-resolution).

**A conditional-fiber frame, [](#q:conditional-fiber-frame).** It asks whether every isotropic log-concave measure admits one frame of directions, chosen before the test function, for which the resampling form of [](#lem:conditional-fiber-form) has a dimension-free gap. *Why it matters:* it implies KLS with constant $4C$, and it uses nothing beyond one-dimensional log-concave inequalities and a choice of directions. *What failed:* the root frame of the simplex ([](#prop:conditional-fiber-root-obstruction)). *Where to start:* the simplex itself is a self-contained test case, whose Poincaré constant is dimension-free, so the question there bears only on the frame idea. Either find an isotropic frame with a dimension-free gap on the simplex, or show that none exists; by [](#lem:fiber-root-degree-two), a polynomial certificate of the second alternative must have degree at least three. Section [](#subsec:fiber-root-failure) contains the shortest complete argument in the manuscript and is the place to begin.

% Agents: the brief's neighbourhood also lists q:upgrade (unlabelled here, Section sec:open) and
% ass:uniform-cmh-approximants; they are not presented as entry problems because q:upgrade has no
% labelled statement and uniform CMH(4) is at least as hard as KLS with no smaller entry point
% beyond conj:gate-zero-sharp.

(sec:reading-paths)=
## How the manuscript is organised

After this overview, the chapters fall into five groups, followed by the full proofs.

**The landscape of methods.** Five chapters, one per family of the literature, in a common format: classical needle localization (Section [](#sec:family-needles)), stochastic localization (Section [](#sec:family-sl)), Bochner, heat flow and the $H^{-1}$ calculus (Section [](#sec:family-bochner)), moment maps, Monge–Ampère and Stein kernels (Section [](#sec:family-moment-map)), and transport (Section [](#sec:family-transport)). Section [](#sec:frontier-atlas) then compares the four approaches of this manuscript side by side, with the main result and the exact bottleneck of each. The survey can be read on its own.

**Approaches through stochastic localization.** A prelude on what localization does and what it costs (Section [](#sec:localization-prelude)); the static quadratic-chaos input (Section [](#sec:qcts)); the fixed-cut approach, from its conditional statements (Section [](#sec:introduction)) through the Carleson target, the product stress test, the Stein traces, the excess propagation and the bootstrap, to its remaining targets (Section [](#sec:open)); and the fixed-eigenfunction approach (Section [](#sec:spectral-route)).

**Deterministic and conditional approaches.** The moment-map programme (Section [](#sec:moment-map-cmh)), the moment-Hessian inequality made precise with its Hodge content and gate zero (Section [](#sec:cmh-normalization)), the cases where it is computed exactly (Section [](#sec:cmh-exact-cases)), and conditional-fiber frames (Section [](#sec:conditional-fiber-frame)). None of these uses stochastic localization.

**Synthesis.** What a proof of KLS now needs, in four cross-cutting targets (Section [](#sec:kls-synthesis)), and a glossary (Section [](#sec:glossary)).

**Technical appendices.** Notation and the two-colour localization setup (Section [](#sec:notation)) through the model geometries (Section [](#sec:models)), the Jacobi splitting formulas (Section [](#sec:jacobi)), and the longer calculations of the fixed-cut and moment-map chapters (Sections [](#sec:appendix-route-e) and [](#sec:appendix-moment-map)). They are best read at the point they are first linked.

**Full proofs.** The complete written proofs, each linked from the status shown next to the statement it proves.

A reader with an afternoon can read this overview and the comparison of Section [](#sec:frontier-atlas); a reader interested in one approach can go straight to its chapter, which opens with its mechanism, its link to KLS, its main result and its exact bottleneck.

(sec:overview-checking)=
## How results are checked, and how to contribute

**Statements and their status.** Every labelled statement — theorem, lemma, proposition, corollary, conjecture, assumption, definition — is fixed text, and its status is shown next to its title from a record kept apart from the prose: *Not settled here*, *Proved* (linking to its full proof), or *Refuted by* the statement that refutes it. *Not settled here* says only that this manuscript does not settle the statement; it says nothing of the literature. A theorem imported from a preprint that has not been refereed shows *Not settled here* however plausible it is, and every statement that uses one names it in its own text. An implication whose hypothesis is not settled can be proved as an implication without being progress on the conjecture; its statement says so.

**What counts as proved.** A statement counts as proved only once a reviewer other than the author of its proof has checked the complete written proof against the statement, and the check is recorded. A proof still being written or checked is not published. If a statement is edited afterwards, its proof counts as unchecked until it is reviewed again. The prose around the statements is an exposition and may simplify; the statements are what count. Computations can suggest where to look, but they never count as proof, and where the text reports one it says so.

**How to contribute.** A contribution can be a proof, a counterexample, a partial result, a reference we missed, or a correction.

- **In discussion:** ask a question or think out loud in the project's [GitHub Discussions](https://github.com/numina-functional-inequalities/kls-conjecture-search/discussions).
- **On GitHub:** open an issue on the [project repository](https://github.com/numina-functional-inequalities/kls-conjecture-search/issues), choosing the form that fits — an idea on an open problem, a counterexample, or a correction — and name the statement by its label, for instance `conj:gate-zero-sharp`.
