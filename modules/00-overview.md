---
numbering:
  enumerator: "0.%s"
---

(sec:overview)=
# The KLS theorem and its methods

+++ {"part": "abstract"}

The Kannan–Lovász–Simonovits (KLS) conjecture asked whether linear functions detect, up to a universal constant, the slowest mode of every log-concave measure; it is now a theorem, [](#conj:kls), and this manuscript works through and compares its three proofs. Bizeul–Klartag–Lehec (BKL) bound cumulants of every order uniformly in the dimension and reach an arbitrary test function by suspension. The second version of Song–Zhang (SZ v2) refines one coefficient radius infinitely often, with losses whose product stays bounded. Balasubramanian–Kasiviswanathan (BK) bound all powers of an integration operator on compatible tensor fields at once and close an induction in the polynomial degree, with $\CP\le1+2\cdot10^{16}$ ([](#thm:bk-explicit-poincare)). The manuscript also develops three alternative mechanisms for the Poincaré bound — a deterministic moment-Hessian inequality, the occupation of a fixed eigenfunction, and resampling along conditional lines — each aiming at something the proofs do not give, and keeps the localization of a fixed cut as an archive.

+++

This overview is meant to be read on its own. It states the question and works its smallest cases by hand (Sections [](#sec:kls-orientation) and [](#sec:kls-examples)), summarizes the literature (Section [](#sec:kls-known)), explains how KLS was proved (Section [](#sec:kls-conversions)), sets out the obstacles that other arguments meet (Section [](#sec:kls-remaining)), gives the main results with the idea of each proof (Section [](#sec:overview-results)), and ends with three problems for someone who might take them up (Section [](#sec:overview-open)). How the manuscript is organized, and how its results are checked, is on the [welcome page](#sec:reading-paths).

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

A measure is *isotropic* if it is centered and its covariance is the identity.

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

the implication “KLS $\Rightarrow$ thin shell” discussed in Section [](#subsec:kls-solved-neighbours). Thin shell controls one observable, $|x|^2$, and on its own it did not lead to KLS.

(sec:kls-examples)=
## Examples by hand

The ratio $\CP(\mu)/\norm{\Cov\mu}_\op$ is at least $1$, by testing linear functions as above; the conjecture says it is bounded. Here it is in the smallest cases.

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

No family of log-concave measures had been found with the ratio in [](#eq:kls-affine) growing with $n$; the gap was entirely in the upper bound, which the three proofs make dimension-free.

(sec:kls-known)=
## What was known

This section records the quantitative history and the two neighboring conjectures settled before KLS, with why settling them did not settle KLS.

(subsec:kls-status)=
### The quantitative history

Set

$$
\PsiKLS_n=\sup_\mu\PsiKLS_\mu,
\qquad
C_{\mathrm P,n}=\sup_\mu\CP(\mu),
$$

the suprema over isotropic log-concave measures on $\R^n$. The published bound used here is Klartag's $\PsiKLS_n\lesssim\sqrt{\log n}$, or $C_{\mathrm P,n}\lesssim\log n$ [@Klartag2023Logarithmic], stated as [](#thm:klartag-logn). Letwin's first-version preprint (arXiv:2607.24164v1, 27 July 2026) gives $\PsiKLS_n\lesssim(\log n)^{1/4}$ and $C_{\mathrm P,n}\lesssim\sqrt{\log n}$ as [](#thm:letwin-kls). Song–Zhang's first-version preprint (arXiv:2610.01447v1, 1 October 2026) gives $C_{\mathrm P,n}\lesssim16^{\log^*(n+2)}$ as [](#thm:song-zhang-kls).

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
| July 2026, preprint | $O((\log n)^{1/4})$ | $O(\sqrt{\log n})$ | [](#thm:letwin-kls): quadratic Poincaré, $\kappa_n=O(1)$, and the time-restricted spectral bridge [@Letwin2026QuadraticKLS]. |
| 1 October 2026, preprint (v1) | $O(4^{\log^*(n+2)})$ | $O(16^{\log^*(n+2)})$ | [](#thm:song-zhang-kls): polynomial estimates fed into curvature estimates and back [@SongZhang2026IteratedLogKLS]. |
| 4 October 2026, preprint | $O(1)$ | $O(1)$ | BKL prove KLS through cumulants and suspension; Chapter [](#sec:bkl-proof) [@BizeulKlartagLehec2026KLS]. |
| 4 October 2026, preprint (v2) | $O(1)$ | $O(1)$ | The second version of Song–Zhang proves KLS by repeated refinement with summable losses; Chapter [](#sec:sz-v2-proof) [@SongZhang2026ConstantKLS]. |
| 6 October 2026, preprint | $O(1)$ | $O(1)$ | BK prove KLS through compatible integration and a direct Appell induction, with $\CP\le1+2\cdot10^{16}$; Chapter [](#sec:bk-proof) [@BalasubramanianKasiviswanathan2026KLS]. |

Through Buser–Ledoux, BK's Poincaré bound also gives an explicit Cheeger bound, $\Psi\le\sqrt{\pi(1+2\cdot10^{16})}$ ([](#cor:bk-cheeger)). The authors of all three proofs declare substantial use of AI tools in finding them; their statements are quoted on the [welcome page](#sec:ai-use).

:::{prf:remark} Reading the table
:label: rem:history-table-caveats
Two entries deserve care. The 2016/2024 row is one result: the Lee–Vempala preprint of 2016 appeared in final form in the Annals in 2024, and the bibliography records both. The $O(n^{5/12})$ entry summarizes a sequence of thin-shell improvements rather than a single paper, and is quoted here only to mark the pre-localization ceiling. Separately, the bibliography contains [@vempala2016kls], a 2016 announcement of a proof of the full conjecture; it is not a milestone in this table, and it is listed in the bibliography for completeness of the record only. The BK row refers to arXiv v1, deposited on 6 October 2026, whose text is identical to the version first distributed on GitHub.
:::

(subsec:kls-solved-neighbours)=
### Solved neighbors that are not KLS

The classical implication structure is

```{math}
:label: eq:kls-implication-chain
\mathrm{KLS}\ \Longrightarrow\ \text{thin shell}\ \Longrightarrow\ \text{slicing},
```

and the arguments resolving the two weaker conjectures did not supply a dimension-free proof of KLS.

**Slicing.** Bourgain's slicing conjecture asks whether the isotropic constants $L_n$ are universally bounded. Guan proved $L_n\lesssim\log\log n$ and, in the process, obtained the stochastic-localization trace estimate that turned out to be decisive [@Guan2024]. Klartag and Lehec combined that estimate with $M$-ellipsoids and Shannon–Stam stability to prove $\sup_nL_n<\infty$, published in 2025 [@KlartagLehec2025Slicing]; Bizeul subsequently gave an alternative proof through small-ball estimates [@Bizeul2025SmallBallSlicing]. Slicing controls determinant and volume information, not the bottom of the full spectrum.

**Thin shell.** For isotropic log-concave $X$ the thin-shell conjecture asks for $\Var(|X|^2)\le Cn$, equivalently $\E(|X|-\sqrt n)^2\le C$. Klartag and Lehec gave a proof via parallel couplings of exponential tilts, nonlinear filtering, optimal transport, $H^{-1}$ estimates, and Guan-type covariance control [@KlartagLehec2025ThinShell]; Chapter [](#sec:family-coupling) describes the coupling and what it does not reach. A July 2026 first-version preprint of Chen and Klartag sharpens it to the optimal $\Var(|X|^2)\le8n$, with equality for products of centered exponentials, together with a sharp third-moment-tensor bound [@ChenKlartag2026SharpThinShell]; both statements are recorded as [](#thm:chen-klartag-thin-shell) and [](#thm:chen-klartag-third-moment).

**Why the earlier comparison retained a loss.** Eldan's reverse estimate bounds the inverse Cheeger scale by a weighted average of thin-shell parameters $\sigma_k$ [@Eldan2013ThinShell],

```{math}
:label: eq:eldan-reverse
\PsiKLS_n\le C\sqrt{(\log n)\sum_{k=1}^n\frac{\sigma_k^2}{k}} .
```

Even with $\sigma_k=O(1)$ the harmonic sum contributes a $\log n$, and [](#eq:eldan-reverse) yields only $\PsiKLS_n\lesssim\log n$, not $O(1)$. Radial concentration constrains one observable, $|x|^2$; KLS quantifies over every function and every measurable cut. The same asymmetry recurs, in sharper form, for Letwin's preprint: it eliminates every *quadratic* witness, and the first eigenfunction of a general log-concave diffusion need not be quadratic.

(sec:kls-conversions)=
## How KLS was proved

Stochastic localization and the quadratic estimate control linear and quadratic functions; the first eigenfunction of a general log-concave measure is neither. Every argument below is a way to reach *every* test function. Two dimension-dependent conversions came first, both from Letwin's quadratic estimate [](#thm:letwin-qcts): Letwin's own, through improved Lichnerowicz (Section [](#subsec:kls-architecture)), and the first version of Song–Zhang (SZ v1), through polynomials of every degree (Section [](#subsec:song-zhang-mechanism)). SZ v1 also isolated a spectral criterion whose exponential form is equivalent to KLS. BKL and SZ v2 close that criterion in two different ways (Sections [](#subsec:kls-bkl-idea) and [](#subsec:kls-sz-v2-idea)); BK keep its polynomials but obtain the spectral gap from an integration calculus of their own (Section [](#subsec:kls-bk-idea)).

(subsec:kls-architecture)=
### Letwin: localization and improved Lichnerowicz

Letwin's [](#thm:letwin-kls) combines four ingredients (Figure [](#fig:kls-architecture)). Stochastic localization observes $X\sim\mu$ through Gaussian noise of decreasing size and follows the conditional law $\mu_t$, which is $t$-strongly log-concave and is $\mu$ on average (Chapter [](#sec:family-sl)). The covariance process $A_t=\Cov(\mu_t)$ obeys an exact Riccati SDE whose noise is the third-moment tensor. Klartag's improved Lichnerowicz inequality $\CP\le\sqrt{\norm{\Cov}_\op/t}$ ([](#thm:improved-lichnerowicz)) converts curvature $t$ into a spectral gap. The new input bounds directional third moments by the quadratic estimate ([](#prop:letwin-kappa)), through the moment-map and Stein-kernel mechanism of Chapter [](#sec:family-moment-map).

::::{figure}
:label: fig:kls-architecture
:class: col-page

```{mermaid}
flowchart TB
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

The architecture of [](#thm:letwin-kls). Boxed in color: the contribution of Letwin's preprint, an input to the localization–Lichnerowicz pipeline rather than a replacement for it.
::::

**The bridge.** Define the directional third-moment parameter

```{math}
:label: eq:kappa-def
\kappa_n=\sup_{\mu,\theta}\bigl\lVert\E_\mu[\inner{X}{\theta}X\otimes X]\bigr\rVert_{\HS},
```

the supremum over isotropic log-concave $\mu$ on $\R^n$ and $\theta\in S^{n-1}$. The localization–Lichnerowicz pipeline delivers

```{math}
:label: eq:kls-bridge
\boxed{\ C_{\mathrm P,n}\lesssim\kappa_n\sqrt{\log n}\ }
```

and Letwin's $\kappa_n\le2\sqrt2$ turns [](#eq:kls-bridge) into [](#thm:letwin-kls).

**Where its logarithm lives.** Not in the moment-map calculation. To keep $\norm{A_t}_\op$ bounded along the path, one follows a smooth surrogate of the top eigenvalue, $\frac1\beta\log\Tr e^{\beta A_t}$, which approximates it within a constant only if $\beta\asymp\log n$. Its Itô drift is then of order $\kappa_n^2\log n$, covariance control survives until $t_*\asymp1/(\kappa_n^2\log n)$, and improved Lichnerowicz turns that time into $\CP\lesssim t_*^{-1/2}\lesssim\kappa_n\sqrt{\log n}$. The logarithm is the *entropy cost of replacing a matrix maximum by a soft maximum over $n$ directions* ([](#rem:log-is-entropy); the computation is Section [](#subsec:sl-where-the-log-lives)). Section [](#subsec:kls-spike-obstruction) explains why a better pathwise bound on $\norm{A_t}_\op$ cannot remove it.

(subsec:song-zhang-mechanism)=
### Song–Zhang, first version: polynomial estimates and curvature

Song and Zhang keep the localization and the quadratic estimate, and replace improved Lichnerowicz by a conversion through polynomials of every degree (Chapter [](#sec:polynomial-curvature), Figure [](#fig:sz-loop)). The polynomials are the Appell polynomials of the measure, adapted to its moments in each degree, and their growth is measured by coefficients $c_k$; for the standard Gaussian they are the Hermite polynomials and $c_k=1/\sqrt{k!}$.

**The spectral criterion.** For a measure of curvature $a$, bounds $c_k\le R^k\ell(k)^k/(k+1)^2$ give $\CP\lesssim R^2\ell(d)^2\max\{1,a^{-1/(d+1)}\}$, much better than the Bakry–Émery bound $1/a$ ([](#thm:sz-curvature-comparison)). The proof follows a first eigenfunction through repeated centered gradients and inverse square roots of the diffusion operator. Curvature uses up energy at each step, while centering removes mass that the polynomial tests measure; if the gap were too small, too much mass would survive for the energy available. With $\ell=1$ the comparison is exact at the end point: KLS is equivalent to one exponential bound $c_k\le A^k$, uniform in the degree, the dimension and the measure ([](#prop:sz-exponential-coefficients-equivalence)).

**The iteration.** Feeding the curvature profile back through localization improves the coefficient bounds, and the comparison can be run again. Each round replaces a logarithm by its logarithm: at depth $r$ the profile is $\CP\le\Gamma_r^2\ell_r(1/a)^2$, with $\ell_r$ the $r$-fold iterated logarithm and $\Gamma_r\le C4^r$ ([](#thm:sz-iterated-curvature)). Localizing an arbitrary isotropic log-concave measure to curvature $c/\log(en)$ transfers the profile to it ([](#thm:sz-curvature-transfer)), and $r\approx\log^*(n+2)$ gives [](#thm:song-zhang-kls).

**Where its loss lives.** The comparison is paid again at every round, at a fixed factor $4$ in $\Gamma_r$, with admissibility thresholds that grow with the depth, while the depth must grow, very slowly, with $n$ (Section [](#sec:sz-profile-iteration)).

(subsec:kls-bkl-idea)=
### Bizeul–Klartag–Lehec: cumulants and suspension

**The calibration on the line.** The cumulants of a law are the Taylor coefficients of the logarithm of its Laplace transform. For the standard Gaussian that logarithm is $z^2/2$: every cumulant beyond the second vanishes. For the centered exponential $X=E-1$ it is $-z-\log(1-z)=\sum_{m\ge2}z^m/m$, so the $m$-th cumulant is $(m-1)!$. A bound on cumulants of every order, uniform over log-concave laws, must therefore allow factorial growth.

**The idea.** BKL prove that this growth is the worst possible: for every isotropic log-concave $\mu$, in every dimension, the cumulant tensor with one slot fixed satisfies $\abs{\kappa_m^\mu(u,\cdot,\dots,\cdot)}^2\le K^{m-1}((m-1)!)^2\abs u^2$, with every other entry summed and no factor of $n$ ([](#thm:bkl-cumulant-bound)). Along a stochastic localization whose noise is normalized by the current covariance, the $m$-th cumulant has the $(m+1)$-th as its noise; a static bound at order $m$ and an integrated bound at order $m+1$ are therefore proved together, starting from the third-moment estimate, with no KLS estimate. A cumulant bound concerns linear observables only, and *suspension* reaches an arbitrary $f$: average $f$ over $N$ independent copies of the law and adjoin the average, smoothed, as one extra coordinate. The enlarged law is log-concave in dimension $nN+1$, and its mixed cumulants are the derivatives of the average of $f$ under exponential tilts ([](#prop:bkl-suspension)). Because the cumulant bound does not see the dimension, it applies to this law and gives the exponential coefficient bound [](#thm:bkl-tilt-bound) for every test function; the tilt-average criterion [](#thm:bkl-tilt-criterion), the spectral criterion of SZ v1 in exponential form, turns it into KLS. The argument is Chapter [](#sec:bkl-proof).

(subsec:kls-sz-v2-idea)=
### Song–Zhang, second version: summable losses

**The calibration in one line.** A fixed cost $C_*>1$ per repetition gives a factor $C_*^m$ after $m$ repetitions, however slowly $m$ grows with $n$; this is the loss of SZ v1. Costs $e^{C\alpha_i}$ with $\alpha_i=2^{-i}/16$ have product at most $e^{C/8}$, since $\sum_i\alpha_i=1/8$. The arithmetic proves nothing by itself: each repetition must remain admissible at its starting depth, and its estimates must concern the same functions.

**The idea.** SZ v2 iterate not the Poincaré constant but one coefficient radius, $\mathcal A(\mu)=\max\{1,\sup_{d\ge2}c_d(\mu)^{2/(d-1)}\}$, equal to $1$ for the standard Gaussian ([](#def:sz-v2-common-radius)); the conversion $\CP\le2^{85}\mathcal A$ ([](#prop:sz-v2-common-radius)) is then paid once, at the end, instead of at every round. Each refinement of the radius still passes through curvature profiles and localization, as in SZ v1, but the inverse-gradient iterates are now controlled in blocks that keep centering and symmetry information over many steps, so that a refinement with margin $\delta$ costs a factor $e^{C\delta}$ rather than a fixed $C_*$. With the margins $\alpha_i$ above the multiplicative costs have a bounded product, and the starting depths, which grow as the margins shrink, are absorbed into an improving height profile at a summable additive cost ([](#prop:sz-v2-summable-budgets)). For a fixed regular measure finitely many refinements suffice, and approximation gives [](#thm:sz-v2-kls). The four successive improvements are Chapter [](#sec:sz-v2-proof); the block estimates are Chapter [](#sec:sz-v2-blocks).

(subsec:kls-bk-idea)=
### Balasubramanian–Kasiviswanathan: compatible integration

**The calibration on the line.** For the standard Gaussian the Appell polynomials are the Hermite polynomials $x$, $x^2-1$, $x^3-3x$, …, and centered integration — taking the primitive of mean zero — sends $A_d/d!$ to $A_{d+1}/(d+1)!$. The coefficients $c_d=1/\sqrt{d!}$ are therefore the norms of the successive powers of one integration operator applied to the constant $1$. BK make these powers the object of the proof.

**The idea.** For a general law, BK integrate *compatible* symmetric tensor fields, those that can be integrated again, and bound all powers of the integration operator at once: a Hodge estimate whose curvature constant does not depend on the tensor rank ([](#lem:bk-compatible-hodge)), an operator lemma that controls every power from finitely many polynomial observations with one common prefactor ([](#lem:bk-uniform-power-bound)), and a localization normalized by the covariance that transfers these bounds to the next Appell coefficient ([](#prop:bk-reverse-transfer)). Started from Letwin's quadratic estimate, this closes an induction giving $c_d\le10^{8d}/(d+1)^4$ ([](#thm:bk-appell-bound)). For a fixed curved law, letting the number of observations tend to infinity gives $\CP\le1+2\cdot10^{16}$, and approximation extends it to every log-concave law ([](#thm:bk-explicit-poincare)): the spectral gap comes from the integration calculus itself. The argument is Chapter [](#sec:bk-proof).

The three proofs are compared step by step, with their shared inputs and reusable estimates, in Chapter [](#sec:kls-synthesis).

(sec:kls-remaining)=
## Obstacles for alternative arguments

The questions of this section concern other arguments: a proof by a different mechanism — deterministic, or with a sharp constant — or a proof of a property that implies KLS, such as the moment-Hessian inequality or the occupation estimate of Section [](#sec:overview-results). Three obstacles constrain any such attempt: a pattern that every classical family meets (Section [](#subsec:kls-adaptive-residue)), a counterexample to the most natural repair (Section [](#subsec:kls-spike-obstruction)), and a cheap test that any proposal should pass (Section [](#subsec:kls-tensorization-test)).

(subsec:kls-adaptive-residue)=
### Fixed and averaged, against adaptive and uniform

Needles control one-dimensional conditional laws; stochastic localization controls covariance and directional third moments; moment maps control fixed matrix energies; parallel coupling controls linear exponential tilts. Each estimate is fixed in advance or averaged, while a small spectral gap is carried by an object that the measure, or an extremal function, selects. The table of Section [](#subsec:kls-reading-map) records, family by family, what is controlled and what is missing. The three proofs get past this through polynomial tests of every degree, which reach every function.

Two directions remain meaningful for a different proof:

- **Reach the exponential Appell criterion by another mechanism.** The criterion [](#prop:sz-exponential-coefficients-equivalence) is the common end point; a further derivation must supply its own estimates, including control of centering losses.
- **Establish an adapted structural estimate.** The moment map uses a Hessian field; the fixed eigenfunction follows the function selected by a small spectral gap; conditional fibers select directions from the measure; the fixed cut, kept as an archive, follows a potential bottleneck. What each would add is set out in Chapter [](#sec:frontier-atlas).

(subsec:kls-reading-map)=
### The six families side by side

(sec:kls-strategy-map)=

Chapters [](#sec:family-needles)–[](#sec:family-coupling) survey six families of methods, from classical needles to the parallel coupling behind the thin-shell theorem. The table collects what each controls and the estimate it does not supply by itself.

| Family | What is controlled | The missing estimate | Section |
|---|---|---|---|
| Classical needles | One-dimensional conditional measures, sharply | A decomposition inheriting *operator* covariance: global isotropy is not inherited needle by needle | [](#sec:family-needles) |
| Stochastic localization | Short-time covariance and the directional third-moment estimate [](#prop:letwin-kappa) | Control of $\lmax(A_t)$ along the whole path without the $\log n$ cost of a soft maximum; see [](#prop:covariance-spike) | [](#sec:family-sl) |
| Bochner, $H^{-1}$, heat flow | Coordinate and quadratic spectral mass of the first eigenspace | Uniform estimates for the derivatives of an arbitrary $f$: trace, coordinate or averaged spectral information does not bound every slow mode | [](#sec:family-bochner) |
| Moment maps and Stein kernels | Fixed deterministic matrix energies $\E\Tr(BHBH)$; and $\CMH$ exactly on the line and on products, with the bound $4$ on every log-concave Dirichlet law ([](#sec:cmh-exact-cases)) | Control when the matrix or direction depends on $X$ or on $f$, that is, the correlation of the random Stein kernel with an arbitrary $\nabla f$. Even the linear sector is missing: $\lmax(\E H^2)\le4$ does not follow from $\Tr(\E H^2)\le2n$ ([](#prop:letwin-not-gate-zero)) | [](#sec:family-moment-map) |
| Transport (Caffarelli, Föllmer, entropic barrier) | Polylogarithmic averaged derivative bounds | A dimension-free expected operator derivative | [](#sec:family-transport) |
| Parallel coupling | Linear exponential tilts $e^{\inner\theta x}\mu$ | Couplings for arbitrary functional perturbations | [](#sec:family-coupling) |

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

This is due to Klartag and Lehec (Section 8.1 and Proposition 65 of [@KLnotes]). The mechanism fits in a line. A centered exponential coordinate has a flat tail: conditionally on a large observation, the prior barely varies on the scale of the noise, so the posterior of that coordinate is essentially the Gaussian noise itself, of variance $s$. One coordinate out of $n$ is that large with probability about $e^{-s}$, so as long as $s\lesssim\log n$ some coordinate is, and the top conditional eigenvalue is of order $s$ — while the product of exponentials has Poincaré constant $4$.

The consequence is structural: *uniform operator-norm control of the conditional covariance at every scale is false, even for a measure that satisfies KLS.* An argument whose only use of the localization path is a pathwise bound on $\norm{A_t}_\op$ needs a statement that is false. A successful potential must exploit eigenvalue profiles, averaging, tensorization, or the particular extremizing function — not better pointwise bounds. The consequence also cuts the other way: rare spikes can be *harmless*, and a potential that charges the full largest eigenvalue whenever a spike occurs is overcharging.

(subsec:kls-tensorization-test)=
### The tensorization test

That gives a cheap and discriminating test, which any proposal should pass before it is developed.

> *Evaluate the proposed potential on a product of $n$ independent copies of a one-dimensional measure. A quantity that is not tensorization-aware will charge $n$ independent coordinates $n$ times for a phenomenon that costs $O(1)$.*

A proposal that fails it is false at scale, and the failure is usually visible in a page. Chapter [](#sec:product-stress) applies it to the all-cut Carleson estimate of the fixed cut ([](#cor:single-coordinate-cuts), [](#conj:product-alignment)); [](#prop:weighted-spectator-obstruction) below applies it to a weighted estimate.

(sec:overview-results)=
## The main results in short

The results fall into three groups: a deterministic inequality that implies KLS, and the families where it holds; two further mechanisms for the Poincaré bound, each through an object of its own; and, from the fixed-cut archive, the limits of following a single cut. Each paragraph gives the idea; the statements and their proofs are in the chapters cited.

(subsec:overview-cmh)=
### A deterministic inequality, sharp on products and Dirichlet laws

These results use no stochastic localization. They start from the *moment map* of Cordero-Erausquin and Klartag [@CorderoErausquinKlartag2015MomentMeasures]: a centered log-concave $\mu$ is the image of $e^{-\varphi(y)}\dd y$ under $\nabla\varphi$ for an essentially unique convex $\varphi$. Transported to $\mu$, the Hessian $H=D^2\varphi\circ(\nabla\varphi)^{-1}$ is a *Stein kernel*: $\E_\mu\Tr(H\,D^2g)=\E_\mu\inner{x}{\nabla g}$ for every test function $g$, and $\E_\mu H=\Sigma=\Cov\mu$. It defines a generator $L_\mu g=\Tr(HD^2g)-\inner{x}{\nabla g}$, symmetric for $\mu$, which for the standard Gaussian ($H=\Id$) is the Ornstein–Uhlenbeck operator. The *canonical moment-Hessian constant* $\CMH(\mu)$ of [](#def:cmh) is the best constant in $\E_\mu\inner{H\nabla g}{\Sigma^{-1}H\nabla g}\le C\,\E_\mu(L_\mu g)^2$.

**It implies the affine Poincaré inequality with no loss.** [](#thm:cmh-implies-affine-poincare) states $\CPaff(\mu)\le\CMH(\mu)$ for measures in the regular moment-map class, where $\CPaff$ is the Poincaré constant measured against $\inner{\Sigma\nabla f}{\nabla f}$. A universal bound $\CMH\le4$ would therefore prove KLS by a deterministic argument, with the constant $4$, which is attained. The mechanism is one Cauchy–Schwarz. Given a centered $f$, solve $-L_\mu g=f$; then

$$
\norm f_2^2=\E_\mu\inner{\nabla f}{H\nabla g}
\le\bigl(\E_\mu\inner{\Sigma\nabla f}{\nabla f}\bigr)^{1/2}
\bigl(\E_\mu\inner{H\nabla g}{\Sigma^{-1}H\nabla g}\bigr)^{1/2},
$$

and the last factor is at most $\CMH^{1/2}\norm{L_\mu g}_2=\CMH^{1/2}\norm f_2$. Only the symmetry, the positivity and the Stein identity of $H$ are used, which is why the constant passes intact. The converse is less clear: a weighted Hodge decomposition ([](#cor:cmh-hodge-comparison)) splits the numerator of $\CMH$ into a gradient part, which is exactly the affine Poincaré quotient, and a divergence-free part that vanishes on the line but not beyond. This decomposition concerns the moment-map Hessian. The Hodge estimate in BK's proof concerns the potential of the measure and a different energy; no implication between the two is established here (Section [](#subsec:proofs-compared-bk)).

**Where it holds.** On the line $\CMH=\CP/\Var$ exactly ([](#thm:cmh-1d)), so the exponential has constant exactly $4$; the constant of a product is the largest constant of its factors ([](#thm:cmh-product)). Beyond products, [](#thm:cmh-dirichlet) gives $\CMH\le4$ for every log-concave Dirichlet law — the law of $(\gamma_1,\dots,\gamma_m)/\sum_j\gamma_j$ for independent $\gamma_i\sim\mathrm{Gamma}(\alpha_i)$ with all $\alpha_i\ge1$, which includes the uniform measure on a simplex. Hence every such law, and every product, linear image or convolution of independent ones, has $\CPaff\le4$ ([](#cor:cmh-dirichlet-poincare)). The proof lifts the simplex to the independent Gamma variables, where the generator is that of a product, and ends in a scalar minimization where $\alpha_i\ge1$ is used (Chapter [](#sec:cmh-exact-cases)). Dimension-free Poincaré bounds for simplices had been obtained earlier, qualitatively, by Kolesnikov and Milman [@KolesnikovMilman2016OrliczKLS]. The product case is also a warning: a product of centered exponentials has $\CMH=4$ with no slack ([](#cor:cmh-product-saturation)), so a log-concave perturbation that raised the constant would refute the inequality. [](#conj:cmh-second-variation) conjectures that none does to second order.

**The linear test.** Testing the moment-Hessian inequality on linear functions only gives its cheapest necessary condition, $\E_\mu H^2\preceq4\,\Id$ in isotropic position ([](#conj:gate-zero)); this manuscript calls it the *linear test*, not to be confused with the bound $\CP\ge\norm{\Cov}_\op$ obtained from linear functions in Section [](#subsec:kls-conjecture). It is a third-moment problem: by [](#lem:linear-sector-third-moment), $\E_\mu\abs{Ha}^2$ is $1+\tfrac14\norm{T_3(a)}_{\HS}^2$, with $T_3(a)=\E_\mu[\inner Xa\,X\otimes X]$, plus a remainder orthogonal to affine functions. An operator bound on $\E H^2$ therefore bounds directional third moments ([](#cor:gate-zero-third-moment)), and the test is computed exactly on exponential cones ([](#prop:cone-linear-sector)). Matrix inequalities over fixed matrices do not give it. [](#prop:letwin-not-gate-zero) builds a random positive semidefinite matrix that satisfies every fixed-matrix energy bound of [](#thm:letwin-moment-map) and has $\lmax(\E H^2)>4$; the two quantities differ by a commutator. The countermodel is not a moment-map Hessian, so it does not refute [](#conj:gate-zero): it shows that a proof must use more of the moment-map structure, the fixed-versus-adaptive pattern of Section [](#subsec:kls-adaptive-residue) once more.

(subsec:overview-reductions)=
### Two further mechanisms for the Poincaré bound

**Following one eigenfunction: the fixed eigenfunction.** Run stochastic localization on an isotropic log-concave $\mu$ and follow a first eigenfunction $f$ through $g_t=\Cov_{\mu_t}(f,X)$ and the tensor $H_t=\E_{\mu_t}[(f-\E_{\mu_t}f)(X-a_t)^{\otimes2}]$. The vector $g_t$ obeys an exact equation in which $\norm{H_t}_{\HS}^2$ is a source and the covariance of the localized measure a damping, with no inequality spent. By [](#prop:spectral-sufficiency), an occupation estimate bounding the accumulated source by the full damping plus a linear budget ([](#conj:mm-spectral-occupation)) implies KLS. The damping then cancels the source, Grönwall's lemma shows that $f$ keeps half its variance up to a universal time, and the bound $\CP(\mu_t)\le1/t$ for the localized measure turns that into a spectral gap. The eigenfunction does not see covariance spikes in directions it does not use, which is why this approach is not ruled out by [](#prop:covariance-spike). One available implication, [](#prop:mm-window-occupation), assumes a small gap that no measure has: the published bound [](#thm:klartag-logn) already gives a larger one. What exists, and what is missing, is Section [](#subsec:spectral-window-chain).

**Resampling along conditional lines: conditional fibers.** For a direction $\theta$, resample $X\sim\mu$ along the line through $X$ in direction $\theta$ from its conditional law, and divide the resulting variance of $f$ by the conditional variance of the line coordinate; averaging over an isotropic frame $\rho$ of directions gives a Dirichlet form $\mathcal D_{\mu,\rho}$. By [](#lem:conditional-fiber-form), $\mathcal D_{\mu,\rho}(f)\le4\int\abs{\nabla f}^2\dd\mu$ — the one-dimensional bound $\CP\le4\Var$ applied on each line — and linear functions carry exactly their Euclidean energy. A frame with a dimension-free gap for this form would therefore give KLS with constant $4C$, using only one-dimensional inequalities ([](#conj:conditional-fiber-frame)). The natural frame on the simplex, the root directions $(e_i-e_j)/\sqrt2$, fails: its gap is $O(m^{-2})$, witnessed by the indicator of a small cap at a vertex, which few root directions can move ([](#prop:conditional-fiber-root-obstruction)). The simplex itself has a dimension-free Poincaré constant, so the frame, not the measure, is at fault. The failure is invisible at fixed polynomial degree, where every admissible frame has a positive floor ([](#lem:fiber-polynomial-floor)).

(subsec:overview-one-cut)=
### Following one cut: a ceiling and two counterexamples

The fixed cut, the oldest localization argument developed here and now kept as an archive, follows one cut $E$ of mass $\tfrac12$ and tracks the excess $e_t(E)$ of its boundary over the isoperimetric profile of the localized measure. Its results are limits and counterexamples, and they apply to any argument that follows a set.

**The near-worst bootstrap.** For a measure whose Cheeger constant is within a factor $1+\varepsilon$ of the smallest in its dimension, [](#thm:bootstrap) shows that the excess propagates along localization with one quantity as its only input, $\Xi_T(\mu)=\int_0^T\E(\lmax(A_t)-1)_+\dd t$. Whitening a localized measure loses at most $\lmax(A_t)^{1/2}$ against the worst isotropic measure of the same dimension, and near-worstness charges every loss to $(\lmax(A_t)-1)_+$. The published covariance estimates give $\Xi_T\le C(1+\log\log n)$ ([](#cor:loglog)). By [](#prop:ceiling), the bound $\Xi_{T_0}(\mu)\le\kappa T_0$ for all measures at a small universal time would by itself suffice for KLS: this measures how strong that one input would have to be.

**Independent spectators break global covariance weights.** The fixed-cut argument wanted a propagation estimate for the excess weighted by $(1+\norm{A_t}_\op)^{5/2}$ ([](#conj:weighted-excess-rate)). [](#prop:weighted-spectator-obstruction) refutes it on a product of centered exponentials with a cylinder cut: add many independent exponential coordinates that the cut ignores. Their covariance spikes (Section [](#subsec:kls-spike-obstruction)) inflate the global weight while the cut does not notice them, so the estimate fails the tensorization test. Removing the weight does not help ([](#prop:spectator-excess-rate-obstruction)): a surviving estimate must change its remainder, or assume the measure near-worst, as [](#thm:bootstrap) does.

(sec:overview-open)=
## Problems for someone who might take them up

Three problems are presented here for a reader who wants to start. Each is stated precisely in its chapter, and none of the three has an answer in the literature that we are aware of. Each asks for something the proofs of KLS do not give: a sharp constant, an elementary one-dimensional mechanism, or a localization mechanism that ignores covariance spikes.

**The sharp linear test of the moment-Hessian inequality, [](#conj:gate-zero-sharp).** It asks whether $\E H^2\preceq2\,\Id$ for the Stein kernel of the moment map of every isotropic log-concave measure: the linear test of Section [](#subsec:overview-cmh), with its sharp constant. *Why it matters:* the constant $2$ is attained by products of exponentials, and none of the three proofs gives a sharp constant. It is the operator form of the Chen–Klartag trace inequality $\Tr\E H^2\le2n$ ([](#thm:chen-klartag-moment-hessian)), and it contains the sharp directional third-moment bound $\kappa_n\le2$ ([](#cor:gate-zero-third-moment)), where the preprint literature reaches $2\sqrt2$ ([](#prop:letwin-kappa)). *What there is:* products of centered exponentials attain it in every direction, and every exponential cone with $\beta=n$ attains it in its axis direction, whatever the base ([](#prop:cone-linear-sector)). Every product-simplex cone satisfies it, with transverse equality exactly when the base is a single simplex and $\beta=n$ ([](#prop:product-simplex-cone-gate)); an interval counts as a one-dimensional simplex. Any argument must be tight on these, and by [](#prop:letwin-not-gate-zero) no argument through fixed-matrix energies alone can succeed. *Where to start:* Section [](#subsec:gate-zero), and the spectral resolution of the linear test in [](#lem:cmh-linear-spectral-resolution).

**A conditional-fiber frame, [](#conj:conditional-fiber-frame).** It asks whether every isotropic log-concave measure admits one frame of directions, chosen before the test function, for which the resampling form of [](#lem:conditional-fiber-form) has a dimension-free gap. *Why it matters:* it would give an elementary mechanism for the Poincaré bound, with constant $4C$, resting only on one-dimensional log-concave inequalities and a choice of directions. *What failed:* the root frame of the simplex ([](#prop:conditional-fiber-root-obstruction)). *Where to start:* the simplex is a self-contained test case whose Poincaré constant is dimension-free, so the question there bears only on the frame. Either find an isotropic frame with a dimension-free gap on the simplex, or show that none exists; by [](#lem:fiber-polynomial-floor), a proof of the second must use test functions whose degree grows with the dimension. Section [](#subsec:fiber-root-failure) gives a short complete argument and is the place to begin.

**The occupation estimate for one eigenfunction, [](#conj:mm-spectral-occupation).** *Why it matters:* it would give a localization mechanism that ignores covariance spikes, since the tensor $H_t$ of one eigenfunction does not see spikes in directions the eigenfunction does not use; by [](#prop:spectral-sufficiency) it implies KLS. *What there is:* the time-weighted budget [](#lem:mm-time-weighted-fixed-source) and the stopped source bound [](#lem:mm-stopped-window-source). *Where to start:* Section [](#subsec:spectral-window-chain). What is missing is control of the source after the covariance has left a bounded range, on a time interval of universal length; the two budgets above do not supply it.

From here, the [reading paths](#sec:reading-paths) of the welcome page lead on: to the map of the alternative mechanisms in Chapter [](#sec:frontier-atlas), to the entry chapter of one mechanism, or to how results are checked before one contributes.

% Agents: the brief's neighbourhood also lists conj:trace-upgrade (labelled in Chapter sec:open, part of
% the fixed-cut archive) and ass:uniform-cmh-approximants; they are not presented as entry problems because
% conj:trace-upgrade belongs to the archive and uniform CMH(4) is at least as hard as KLS with no smaller
% entry point beyond conj:gate-zero-sharp.
% Order of the entry problems (owner's decision, 2026-10-06): conj:gate-zero-sharp first (sharp
% constant 2, given by none of the proofs), then conj:conditional-fiber-frame (elementary 1-D mechanism),
% then conj:mm-spectral-occupation (localization ignoring spikes). No bare "it implies KLS" motivation.
