---
numbering:
  enumerator: "0.%s"
---

(sec:overview)=
# The KLS theorem and its methods

+++ {"part": "abstract"}

The Kannan–Lovász–Simonovits (KLS) conjecture asked whether linear functions
detect, up to a universal constant, the slowest mode of every log-concave
measure. It is now a theorem, [](#conj:kls). This manuscript reconstructs,
checks and compares three source proofs: Bizeul–Klartag–Lehec (BKL), through
all-order cumulants and suspension; Song–Zhang, second version, through
refinement with summable losses; and Balasubramanian–Kasiviswanathan (BK),
through compatible integration and a direct Appell coefficient induction.
The last gives the explicit bound $C_P\le1+2\cdot10^{16}$
([](#thm:bk-explicit-poincare)). Their shared polynomial quantities connect
them to earlier work, while their closing estimates are different.

Besides these proofs, the manuscript develops three alternative mechanisms:
the canonical moment-Hessian inequality, occupation of a fixed eigenfunction,
and resampling along conditional lines. Their sufficient conditions are not
known here to follow from KLS, and none is established by the three proofs.
Localization of a fixed cut is retained as an archive. Every statement
shows its status and its reviewer-agent check, distinct from journal peer
review; see the [welcome page](#sec:overview-checking).

+++

This overview is meant to be read on its own. It states the question and works its smallest cases by hand (Sections [](#sec:kls-orientation) and [](#sec:kls-examples)), summarizes the literature (Section [](#sec:kls-known)), explains how KLS was proved — the two dimension-dependent conversions that came first, then the idea of each of the three proofs (Section [](#sec:kls-conversions)) — sets out the obstacles that alternative mechanisms meet (Section [](#sec:kls-remaining)), gives the main results with the idea of each proof (Section [](#sec:overview-results)), and ends with three problems for someone who might take them up (Section [](#sec:overview-open)). How the rest of the manuscript is organised, and how its results are checked, is on the [welcome page](#sec:reading-paths).

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

the implication “KLS $\Rightarrow$ thin shell” discussed in Section [](#subsec:kls-solved-neighbours). This radial estimate alone did not furnish a dimension-free proof of KLS in the arguments preceding the dimension-free proofs.

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

By the theorem, no family of log-concave measures has the ratio in [](#eq:kls-affine) growing with $n$, and none had been found before. The historical gap was entirely in the upper bound; the three proofs close it with a dimension-free bound.

(sec:kls-known)=
## What was known

This section records the quantitative history and the two neighbouring conjectures that have been settled, with why settling them did not settle KLS. How KLS was proved, from the dimension-dependent arguments that preceded the dimension-free proofs to the proofs themselves, is the subject of the next section.

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
| 6 October 2026 (version consulted), preprint (GitHub) | $O(1)$ | $O(1)$ | BK prove KLS through compatible integration and a direct Appell induction, with $C_P\le1+2\cdot10^{16}$; Chapter [](#sec:bk-proof) [@BalasubramanianKasiviswanathan2026KLS]. |

Through Buser–Ledoux, BK's Poincaré bound also gives an explicit Cheeger bound, $\Psi\le\sqrt{\pi(1+2\cdot10^{16})}$ ([](#cor:bk-cheeger)). The BK source has no arXiv number; the bibliography entry [@BalasubramanianKasiviswanathan2026KLS] pins the version read here by its Git commit and checksum.

The authors of all three proofs declare substantial use of AI tools in finding them; their statements are quoted on the [welcome page](#sec:reading-paths).

:::{prf:remark} Reading the table
:label: rem:history-table-caveats
Two entries deserve care. The 2016/2024 row is one result: the Lee–Vempala preprint of 2016 appeared in final form in the Annals in 2024, and the bibliography records both. The $O(n^{5/12})$ entry summarizes a sequence of thin-shell improvements rather than a single paper, and is quoted here only to mark the pre-localization ceiling. Separately, the bibliography contains [@vempala2016kls], a 2016 announcement of a proof of the full conjecture; it is not a milestone in this table, and it is listed in the bibliography for completeness of the record only. The BK row refers to a version distributed on GitHub and pinned by its Git commit, not to an arXiv deposit; its date is that of the version consulted.
:::

(subsec:kls-solved-neighbours)=
### Solved neighbours that are not KLS

The classical implication structure is

```{math}
:label: eq:kls-implication-chain
\mathrm{KLS}\ \Longrightarrow\ \text{thin shell}\ \Longrightarrow\ \text{slicing},
```

and the arguments resolving the two weaker conjectures did not supply a dimension-free proof of KLS. The three proofs add further mechanisms: estimates on cumulants of every order, losses made summable across refinements, or a common bound for compatible integration powers followed by a degree recurrence.

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

Stochastic localization and the quadratic estimate control linear and quadratic functions; the first eigenfunction of a general log-concave measure is neither. Every argument below is a way to reach *every* test function. Two dimension-dependent conversions came first, both starting from Letwin's quadratic estimate [](#thm:letwin-qcts): Letwin's own, through improved Lichnerowicz, which gives $\CP\lesssim\sqrt{\log n}$ (Section [](#subsec:kls-architecture)), and the first version of Song–Zhang, through polynomials of every degree, which gives $\CP\lesssim16^{\log^*(n+2)}$ (Section [](#subsec:song-zhang-mechanism)). The second also isolated a spectral criterion: a first eigenfunction followed through polynomial tests of every degree, which turns coefficient bounds into a Poincaré bound, and whose exponential form is equivalent to KLS. Three proofs followed. Two of them start from that criterion and close it differently: Bizeul, Klartag and Lehec prove the exponential coefficient bound directly, from cumulants of every order and a suspension construction (Section [](#subsec:kls-bkl-idea)); the second version of Song–Zhang keeps the iteration of the first and makes its losses summable (Section [](#subsec:kls-sz-v2-idea)). The third, by Balasubramanian and Kasiviswanathan, keeps the Appell normalization and Letwin's quadratic estimate but obtains its spectral conversion from its own integration calculus (Section [](#subsec:kls-bk-idea)).

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

The architecture of [](#thm:letwin-kls). Boxed in colour: the contribution of Letwin's preprint, an input to the localization–Lichnerowicz pipeline rather than a replacement for it.
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

**The spectral criterion.** For a measure of curvature $a$, bounds $c_k\le R^k\ell(k)^k/(k+1)^2$ give $\CP\lesssim R^2\ell(d)^2\max\{1,a^{-1/(d+1)}\}$, much better than the Bakry–Émery bound $1/a$ ([](#thm:sz-curvature-comparison)). The proof follows a first eigenfunction through repeated centered gradients and inverse square roots of the diffusion operator. Curvature consumes energy at each step, while centering removes mass that the polynomial tests measure; if the gap were too small, too much mass would survive for the energy available. With $\ell=1$ the comparison is exact at the end point: KLS is equivalent to one exponential bound $c_k\le A^k$, uniform in the degree, the dimension and the measure ([](#prop:sz-exponential-coefficients-equivalence)).

**The iteration.** Feeding the curvature profile back through localization improves the coefficient bounds, and the comparison can be run again. Each round replaces a logarithm by its logarithm: at depth $r$ the profile is $\CP\le\Gamma_r^2\ell_r(1/a)^2$, with $\ell_r$ the $r$-fold iterated logarithm and $\Gamma_r\le C4^r$ ([](#thm:sz-iterated-curvature)). Localizing an arbitrary isotropic log-concave measure to curvature $c/\log(en)$ transfers the profile to it ([](#thm:sz-curvature-transfer)), and $r\approx\log^*(n+2)$ gives [](#thm:song-zhang-kls).

**Where its loss lives.** The comparison is paid again at every round, at a fixed factor $4$ in $\Gamma_r$, with admissibility thresholds that grow with the depth, while the depth must grow, very slowly, with $n$ (Section [](#sec:sz-profile-iteration)). BKL proves the exponential end point through cumulants and suspension; SZ v2 makes the per-round costs summable. BK obtains the same end point through a direct recurrence with a common integration prefactor.

(subsec:kls-bkl-idea)=
### Bizeul–Klartag–Lehec: cumulants and suspension

**The calibration on the line.** The cumulants of a law are the Taylor coefficients of the logarithm of its Laplace transform. For the standard Gaussian that logarithm is $z^2/2$: the second cumulant is $1$ and every higher one vanishes. For the centred exponential $X=E-1$ it is $-z-\log(1-z)=\sum_{m\ge2}z^m/m$, so the $m$-th cumulant is $(m-1)!$. A bound on cumulants of every order, uniform over log-concave laws, must therefore allow factorial growth. In dimension $n$ the cumulant $\kappa_m^\mu$ is a tensor, and the quantity to bound is the full tensor with one slot fixed, $\abs{\kappa_m^\mu(u,\cdot,\dots,\cdot)}$, with every remaining entry summed and no factor of $n$.

**The criterion in terms of tilts.** For a test function $f$, let $F_f(z)$ be its average under $\mu$ reweighted by $e^{\inner zx}$, and $\mathcal T_df$ the $d$-th Taylor tensor of $F_f$ at $0$, normalized by $1/d!$ ([](#def:bkl-tilt-cumulants)). Since $e^{\inner zx-\Lambda_\mu(z)}$ is the generating function of the Appell polynomials, the operator norm of $\mathcal T_d$ on $L^2(\mu)$ is exactly the coefficient $c_d$ of the first version ([](#prop:bkl-tilt-appell-duality)). The tilt-average criterion [](#thm:bkl-tilt-criterion) — if $\abs{\mathcal T_df}\le R^d\norm f_2$ for every $d$ and $f$, then $\CP\le CR^2$ — is the spectral criterion above in its exponential form, proved by the same eigenfunction argument with a two-block tensor symmetrization ([](#lem:bkl-tensor-symmetrization)).

**Cumulants of every order, free of dimension.** [](#thm:bkl-cumulant-bound) gives $\abs{\kappa_m^\mu(u,\cdot,\dots,\cdot)}^2\le K^{m-1}((m-1)!)^2\abs u^2$ for every isotropic log-concave $\mu$, in every dimension: by the exponential, factorial growth is necessary, and up to a geometric factor it suffices. The proof runs a stochastic localization whose noise is rescaled by the inverse square root of the current covariance, so that the covariance decays on average like $e^{-t}I$ and every cumulant is measured in the inverse-covariance metric ([](#lem:bkl-cumulant-dynamics)). Along it, the $m$-th cumulant has the $(m+1)$-th as its noise and products of lower cumulants in its drift. The noise supplies positive energy at the next order, so a static bound at order $m$ and an integrated bound at order $m+1$ are proved together ([](#lem:bkl-cumulant-energy)), starting from the third-moment estimate. The binomial number of ways to split indices is cancelled by the factorials, and the remaining polynomial cost is absorbed into $K$. No KLS estimate enters.

**Suspension.** A cumulant bound concerns linear observables; the criterion needs every $f$. BKL put $f$ into a coordinate. Take $N$ independent copies $X_1,\dots,X_N$ of an isotropic regular law, a smooth $f$ orthogonal to affine functions, $F_N=N^{-1/2}\sum_if(X_i)$, and adjoin the coordinate $S=(F_N+\eta)/\sqrt{1+2/\beta^2}$ with an independent centred Laplace variable $\eta$ of rate $\beta$. The joint law on $\R^{nN+1}$ is isotropic and, for $N$ large, log-concave: each copy of $f$ enters with weight $N^{-1/2}$, so its Hessian is absorbed by the curvature of the original law. A cumulant of this enlarged law with one slot in $S$ and $d$ slots in one copy of $X$ is the tilt derivative of $f$ divided by $\sqrt{N(1+2/\beta^2)}$, and the $N$ disjoint blocks cancel the factor $N^{-1}$ in the squared norm ([](#prop:bkl-suspension)). The dimension has grown from $n$ to $nN+1$ with $N\to\infty$: a cumulant bound depending on the dimension would be useless here, and the uniform one applies unchanged. The factor $(d!)^2$ of the cumulant of order $d+1$ cancels the $1/d!$ in $\mathcal T_d$, which leaves [](#thm:bkl-tilt-bound), $\abs{\mathcal T_df}\le(2K)^{d/2}\norm f_2$ for every centred log-concave $\mu$ with $\Cov\mu\preceq I$. This is the exponential end point of [](#prop:sz-exponential-coefficients-equivalence); with the tilt-average criterion it gives [](#conj:kls), first for regular measures, then by approximation. The full argument is Chapter [](#sec:bkl-proof).

(subsec:kls-sz-v2-idea)=
### Song–Zhang, second version: summable losses

**The calibration in one line.** A fixed cost $C_*>1$ per repetition gives a factor $C_*^m$ after $m$ repetitions, however slowly $m$ grows with $n$; this is the loss of the first version. Costs $e^{C\alpha_i}$ with $\alpha_i=2^{-i}/16$ have product at most $e^{C/8}$, since $\sum_i\alpha_i=1/8$. The arithmetic proves nothing by itself: each repetition must remain admissible at its starting depth, and its estimates must concern the same functions. The second version of Song–Zhang supplies these estimates (Chapter [](#sec:sz-v2-proof)).

**One radius for all degrees.** Instead of the Poincaré constant, the proof iterates a single coefficient radius, $\mathcal A(\mu)=\max\{1,\sup_{d\ge2}c_d(\mu)^{2/(d-1)}\}$, so that $c_d\le\mathcal A^{(d-1)/2}$ in every degree; for the standard Gaussian $\mathcal A=1$ ([](#def:sz-v2-common-radius)). The spectral conversion is $\CP\le2^{85}\mathcal A$ ([](#prop:sz-v2-common-radius)). Because the radius, not $\CP$, is refined, this fixed factor is paid once, at the end, rather than at every round as in the first version.

**Four improvements.** First, polynomial cost in the logarithmic depth: [](#thm:sz-v2-iterated-curvature) replaces $16^r$ by $(r+1)^{1/3}$, because blocks of inverse-gradient iterates retain centering and symmetry information over many steps instead of charging a loss at each one (Chapter [](#sec:sz-v2-blocks)); via the transfer, $\CP\lesssim(1+\log^*(n+2))^{1/3}$ ([](#thm:sz-v2-dimension-bound)). Second, height reduction: repeating the improvement replaces $\log^*$ by $\log^*\circ\log^*$ and so on, at a fixed cost $C_*$ per repetition ([](#prop:sz-v2-height-reduction)), which still grows with the number of repetitions. Third, multipliers close to one: with a margin $\delta$, $m$ refinements cost $e^{C\delta m}$ ([](#prop:sz-v2-small-loss)), at the price of a degree cutoff of order $\delta^{-2}$ and a starting depth of order $\delta^{-12}$; earlier coefficient bounds are kept on the degree ranges where they are stronger. Fourth, summable costs: the margins $\alpha_i=2^{-i}/16$ give a multiplicative cost at most $e^{C_A/8}$ and, once the growing starting depths are absorbed into the improving height profile, an additive cost of order $2^{-i}$ ([](#prop:sz-v2-summable-budgets)).

**The end.** For a fixed regular measure of curvature $a$, finitely many refinements bring the height profile at $\max\{1,a^{-1}\}$ down to its floor, the profile gives a radius bound independent of the measure, and $\CP\le2^{85}\mathcal A$ converts it once; approximation then gives [](#thm:sz-v2-kls). The reconstruction uses neither the BKL estimates nor their consequences.

(subsec:kls-bk-idea)=
### Compatible integration: the BK proof

BK begins with the same Appell normalization and Letwin's quadratic
inequality, then controls inverse differentiation on compatible symmetric
tensor fields (Chapter [](#sec:bk-proof)) [@BalasubramanianKasiviswanathan2026KLS].
Weighted divergence can destroy compatibility; a Hodge projection retains
a curvature bound independent of tensor rank ([](#lem:bk-compatible-hodge)).
An operator estimate converts finitely many polynomial observations into
bounds for every integration power with one common prefactor
([](#lem:bk-uniform-power-bound)). Covariance-normalized localization then
transfers these integration bounds to the next polynomial coefficient
([](#prop:bk-reverse-transfer)).

This closes a direct induction giving $c_d\le10^{8d}/(d+1)^4$
([](#thm:bk-appell-bound)). For a fixed curved law, letting the number of
available observations tend to infinity gives
$C_P\le1+2\cdot10^{16}$; regular approximation extends this to every
log-concave law ([](#thm:bk-explicit-poincare)). No BKL or SZ v2 conclusion
initializes the induction. The spectral conversion comes from the
integration calculus itself, not from reusing either proof's final bound.

The three proofs are compared step by step, with their shared inputs and
reusable estimates, in Chapter [](#sec:kls-synthesis).

(sec:kls-remaining)=
## Obstacles for alternative arguments

KLS is proved, and the questions of this section concern other arguments: a proof by a different mechanism — deterministic, or with a sharp constant — or a proof of a property that implies KLS, such as the moment-Hessian inequality or the occupation estimate of Section [](#sec:overview-results). Three obstacles constrain any such attempt: a pattern that every classical family meets (Section [](#subsec:kls-adaptive-residue)), a counterexample to the most natural repair (Section [](#subsec:kls-spike-obstruction)), and a cheap test that any proposal should pass (Section [](#subsec:kls-tensorization-test)). The quadratic and third-moment bounds of [](#thm:letwin-qcts) and [](#prop:letwin-kappa) are common inputs, but they do not by themselves supply dimension-free estimates.

(subsec:kls-adaptive-residue)=
### Fixed and averaged, against adaptive and uniform

Needles control one-dimensional conditional laws; stochastic localization controls covariance and directional third moments; moment maps control fixed matrix energies; parallel coupling controls linear exponential tilts. Each estimate is fixed in advance or averaged, while a small spectral gap is carried by an object that the measure, or an extremal function, selects. The table of Section [](#subsec:kls-reading-map) records, family by family, what is controlled and what is missing. All three proofs get past this through polynomial tests of every degree. BKL pass beyond the third moment to all cumulants, then encode a general function in an extra coordinate, which uniformity in dimension makes possible. The second version of Song–Zhang controls the centering losses of an eigenfunction iteration degree by degree. BK controls arbitrary compatible integration chains from finitely many polynomial observations, then closes a degree recurrence through localization.

Two directions remain meaningful for a different proof:

- **Improve the polynomial comparison by another mechanism.** The exponential Appell criterion [](#prop:sz-exponential-coefficients-equivalence) identifies the end point. BKL prove it through [](#thm:bkl-tilt-bound); an independent derivation must supply different estimates, including control of centering losses.
- **Establish an adapted structural estimate.** The moment map uses a Hessian field; the fixed eigenfunction follows the function selected by a small spectral gap; conditional fibers select directions from the measure; the fixed cut, kept as an archive, retains a potential bottleneck. Their sufficient conditions are not known to follow from KLS.

(subsec:kls-reading-map)=
### The six families side by side

(sec:kls-strategy-map)=

Chapters [](#sec:family-needles)–[](#sec:family-coupling) survey six families of methods, from classical needles to the parallel coupling behind the thin-shell theorem. The table collects what each controls and the estimate it does not supply by itself.

| Family | What is controlled | The missing estimate | Section |
|---|---|---|---|
| Classical needles | One-dimensional conditional measures, sharply | A decomposition inheriting *operator* covariance: global isotropy is not inherited needle by needle | [](#sec:family-needles) |
| Stochastic localization | Short-time covariance and the directional third-moment estimate [](#prop:letwin-kappa) | Control of $\lmax(A_t)$ along the whole path without the $\log n$ cost of a soft maximum; see [](#prop:covariance-spike) | [](#sec:family-sl) |
| Bochner, $H^{-1}$, heat flow | Coordinate and quadratic spectral mass of the first eigenspace | Uniform estimates for the derivatives of an arbitrary $f$: trace, coordinate or averaged spectral information does not bound every slow mode | [](#sec:family-bochner) |
| Moment maps and Stein kernels | Fixed deterministic matrix energies $\E\Tr(BHBH)$; and, exactly, $\CMH$ on the line, on products and on every log-concave Dirichlet law ([](#sec:cmh-exact-cases)) | Control when the matrix or direction depends on $X$ or on $f$, that is, the correlation of the random Stein kernel with an arbitrary $\nabla f$. Even the linear sector is missing: $\lmax(\E H^2)\le4$ does not follow from $\Tr(\E H^2)\le2n$ ([](#prop:letwin-not-gate-zero)) | [](#sec:family-moment-map) |
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

This is due to Klartag and Lehec (Section 8.1 and Proposition 65 of [@KLnotes]). The mechanism fits in a line. A centred exponential coordinate has a flat tail: conditionally on a large observation, the prior barely varies on the scale of the noise, so the posterior of that coordinate is essentially the Gaussian noise itself, of variance $s$. One coordinate out of $n$ is that large with probability about $e^{-s}$, so as long as $s\lesssim\log n$ some coordinate is, and the top conditional eigenvalue is of order $s$ — while the product of exponentials has Poincaré constant $4$.

The consequence is structural: *uniform operator-norm control of the conditional covariance at every scale is false, even for a measure that satisfies KLS.* An argument whose only use of the localization path is a pathwise bound on $\norm{A_t}_\op$ is attempting to prove something stronger than KLS, and something that is not true. A successful potential must exploit eigenvalue profiles, averaging, tensorization, or the particular extremizing function — not better pointwise bounds. The consequence also cuts the other way: rare spikes can be *harmless*, and a potential that charges the full largest eigenvalue whenever a spike occurs is overcharging.

(subsec:kls-tensorization-test)=
### The tensorization test

That gives a cheap and discriminating test, which any proposal should pass before it is developed.

> *Evaluate the proposed potential on a product of $n$ independent copies of a one-dimensional measure. A quantity that is not tensorization-aware will charge $n$ independent coordinates $n$ times for a phenomenon that costs $O(1)$.*

A proposal that fails it is not merely inefficient; it is false at scale, and the failure is usually visible in a page. Chapter [](#sec:product-stress) applies it to the all-cut Carleson estimate of the fixed cut, where it shows that no fixed cut depending on a single coordinate can violate that estimate, even when that coordinate's variance inflates ([](#cor:single-coordinate-cuts)), and isolates what remains in the adapted alignment problem [](#conj:product-alignment) for cuts of unbounded coordinate complexity; [](#prop:weighted-spectator-obstruction) below is the same test applied to a weighted estimate.

(sec:overview-results)=
## The main results in short

The results fall into three groups: a deterministic inequality that implies KLS, and the families where it holds; two further alternative mechanisms for the Poincaré bound, each through an object of its own; and, from the fixed-cut archive, the limits of following a single cut, with the counterexamples that fix them. The idea of each proof is given here; the statements themselves are in the chapters that follow, where each one's status links to its full proof.

(subsec:overview-cmh)=
### A deterministic inequality, sharp on products and Dirichlet laws

The first results, those of the moment-map mechanism, use no stochastic localization. They start from the *moment map* of Cordero-Erausquin and Klartag [@CorderoErausquinKlartag2015MomentMeasures]: a centred log-concave $\mu$ is the image of $e^{-\varphi(y)}\dd y$ under $\nabla\varphi$ for an essentially unique convex $\varphi$. Transported to $\mu$, the Hessian $H=D^2\varphi\circ(\nabla\varphi)^{-1}$ is a *Stein kernel*: $\E_\mu\Tr(H\,D^2g)=\E_\mu\inner{x}{\nabla g}$ for every test function $g$, and $\E_\mu H=\Sigma=\Cov\mu$. It defines a generator $L_\mu g=\Tr(HD^2g)-\inner{x}{\nabla g}$, symmetric for $\mu$, which for the standard Gaussian ($H=\Id$) is the Ornstein–Uhlenbeck operator. The *canonical moment-Hessian constant* $\CMH(\mu)$ of [](#def:cmh) is the best constant in $\E_\mu\inner{H\nabla g}{\Sigma^{-1}H\nabla g}\le C\,\E_\mu(L_\mu g)^2$.

**The inequality implies the affine Poincaré inequality with no loss.** [](#thm:cmh-implies-affine-poincare) states $\CPaff(\mu)\le\CMH(\mu)$, where $\CPaff$ is the Poincaré constant measured against $\inner{\Sigma\nabla f}{\nabla f}$. A universal bound $\CMH\le4$ would therefore give KLS; what it would add to the three proofs is a deterministic argument, with no stochastic localization, and the constant $4$, which is attained. The mechanism is one Cauchy–Schwarz. Given a centred $f$, solve $-L_\mu g=f$ (up to a spectral truncation). Then

$$
\norm f_2^2=\E_\mu\inner{\nabla f}{H\nabla g}
\le\bigl(\E_\mu\inner{\Sigma\nabla f}{\nabla f}\bigr)^{1/2}
\bigl(\E_\mu\inner{H\nabla g}{\Sigma^{-1}H\nabla g}\bigr)^{1/2},
$$

and the last factor is at most $\CMH^{1/2}\norm{L_\mu g}_2=\CMH^{1/2}\norm f_2$. Only the symmetry, the positivity and the Stein identity of $H$ are used, which is why the constant passes intact. The statement is for a regular class of measures; [](#lem:affine-poincare-w2-liminf) and [](#prop:cmh-approximation-closure) carry the affine Poincaré inequality to every log-concave law along approximants, given the uniform control of [](#ass:uniform-cmh-approximants). The converse direction is less clear: a weighted Hodge decomposition ([](#prop:cmh-hodge), [](#cor:cmh-hodge-comparison)) splits the numerator of $\CMH$ into a gradient part, which is *exactly* the affine Poincaré quotient, and a divergence-free part that vanishes on the line but not beyond. So in dimension at least two the inequality asks for something besides KLS, and no measure separating the two is exhibited.

**Where it holds.** [](#thm:cmh-1d) computes $\CMH=\CP/\Var$ exactly on the line, so the exponential has constant exactly $4$; [](#thm:cmh-product) says the constant of a product is the largest constant of its factors; and [](#thm:cmh-dirichlet) gives $\CMH\le4$ for every log-concave Dirichlet law — the law of $(\gamma_1,\dots,\gamma_m)/\sum_j\gamma_j$ for independent $\gamma_i\sim\mathrm{Gamma}(\alpha_i)$ with all $\alpha_i\ge1$, which includes the uniform measure on a simplex. By [](#cor:cmh-dirichlet-poincare), every such law, and every product, linear image or convolution of independent ones, has $\CPaff\le4$. On the line the divergence-free part vanishes and the inequality becomes an identity. For products, the cross terms $\E[(L_ig)(L_jg)]$ between factors are nonnegative, so the denominator only gains. The Dirichlet family is the first non-product case, and its proof lifts the simplex to the independent Gamma variables: a function on the simplex is a function of the Gammas that is homogeneous of degree zero. The Bochner identity of the Gamma product, a completed square, and the Euler relation that homogeneity imposes reduce the claim to a scalar minimization in one variable per coordinate, which is where $\alpha_i\ge1$ — log-concavity — is spent. The moment-Hessian inequality with constant $4$ on these laws, and hence $\CPaff\le4$, is proved here; dimension-free Poincaré bounds for simplices had been obtained earlier, qualitatively, by Kolesnikov and Milman [@KolesnikovMilman2016OrliczKLS].

The product case is also a warning. A product of centred exponentials has $\CMH=4$ *exactly*, with no slack ([](#cor:cmh-product-saturation)): the inequality one needs in general is already tight on a product, so a log-concave perturbation of that product that raised the constant would refute it. [](#conj:cmh-second-variation) is the second-order form of that question, and conjectures that no admissible log-concave perturbation raises the constant to second order.

**The linear test is a third-moment problem.** Testing the inequality on linear functions gives its cheapest necessary condition, $\E_\mu H^2\preceq4\,\Id$ in isotropic position ([](#conj:gate-zero)). [](#lem:linear-sector-third-moment) identifies what that condition contains: for every unit $a$,

$$
\E_\mu\abs{Ha}^2=1+\tfrac14\norm{T_3(a)}_{\HS}^2+\E_\mu\abs{v_a}^2,
\qquad T_3(a)=\E_\mu\bigl[\inner Xa\,X\otimes X\bigr],
$$

with a remainder $v_a$ orthogonal to all affine functions. The mechanism is the Stein identity applied to quadratic test functions, which says that $\E_\mu[H_{ij}X_k]$ is half the third-moment tensor; projecting the column $Ha$ onto the span of $1,X_1,\dots,X_n$ leaves $a+\tfrac12T_3(a)X$, and Pythagoras gives the identity. By [](#cor:gate-zero-third-moment), an operator bound $\E H^2\preceq c\,\Id$ forces $\norm{T_3(a)}_{\HS}\le2\sqrt{c-1}$. On the *exponential cones* — density $\propto x_1^{\beta-n}e^{-x_1}$ on the cone over a centred convex body $K$ — the moment potential of the cone is built explicitly from that of the base, and the axis column of the kernel is the position vector itself, so the axis value of the linear test is an explicit Gamma moment, $1+n/\beta$ ([](#prop:cone-linear-sector)); over a cube base the whole matrix is in closed form ([](#cor:cube-cone-gate-zero)).

**Matrix inequalities over fixed matrices do not give the linear test.** The fixed-matrix estimate is [](#thm:letwin-moment-map). [](#prop:letwin-not-gate-zero) builds, for every $m\ge18$, a random positive semidefinite matrix with $\E H=\Id$ satisfying all these inequalities and yet $\lmax(\E H^2)>4$. The two quantities differ by one commutator, $\Tr(B^2H^2)=\Tr(BHBH)+\tfrac12\norm{[B,H]}_{\HS}^2$, and the countermodel — an arrowhead matrix built from a uniform point $z$ of $S^{m-1}$ — makes the commutator large in expectation while keeping every fixed-$B$ energy within budget. The countermodel is not a moment-map Hessian, so it says nothing about [](#conj:gate-zero) itself; it says that a proof must use more of the moment-map structure than matrix algebra over fixed $B$. It is the fixed-versus-adaptive pattern of Section [](#subsec:kls-adaptive-residue) once more.

(subsec:overview-reductions)=
### Two further mechanisms for the Poincaré bound

**Following one eigenfunction: the fixed eigenfunction.** Run stochastic localization on an isotropic log-concave $\mu$ and follow a first eigenfunction $f$: set $g_t=\Cov_{\mu_t}(f,X)$, $H_t=\E_{\mu_t}[(f-\E_{\mu_t}f)(X-a_t)^{\otimes2}]$ and $A_t=\Cov(\mu_t)$. [](#prop:spectral-sufficiency) says that the occupation estimate [](#conj:mm-spectral-occupation) — a bound of the time-integrated source $\E\int_0^t\norm{H_s}_{\HS}^2$ by a linear budget, a lower-order term, and the full damping $\E\int_0^t2g_s^TA_sg_s$ — implies KLS. What it would add beyond KLS is the object followed: one eigenfunction rather than the whole covariance. The mechanism: $g_t$ obeys an exact equation, $\dd g_t=H_t\,\dd W_t-A_tg_t\,\dd t$, so $\E\abs{g_t}^2$ grows by the source and decreases by the damping, with no inequality spent. The hypothesis lets the damping cancel the source; Grönwall's lemma then bounds how much of $f$ has been learned by a universal time $T_*$, so $\E\Var_{\mu_{T_*}}(f)\ge\tfrac12$; and the Brascamp–Lieb bound $\CP(\mu_t)\le1/t$ for the localized measure turns that into $\lambda\ge T_*/2$. The eigenfunction is the right object because, unlike the top covariance eigenvalue, it ignores spikes in directions it does not use. The stopped estimate [](#lem:mm-stopped-window-source) bounds the source before a covariance exit. The occupation proposition [](#prop:mm-window-occupation) supplies no nonempty small-gap case: its published input already forces $\lambda\ge1/K_n>3/(8K_n)$. Section [](#subsec:spectral-window-chain) explains why its $\CP\lesssim\log^2n$ consequence adds nothing to that input.

**Resampling along conditional lines: conditional fibers.** For a direction $\theta$, resample $X\sim\mu$ along the line through $X$ in direction $\theta$ from its conditional law, and divide the resulting variance of $f$ by the conditional variance of the line coordinate. Averaging over an isotropic frame $\rho$ of directions gives a Dirichlet form $\mathcal D_{\mu,\rho}$. [](#lem:conditional-fiber-form) shows that this form is well defined and closed, that $\mathcal D_{\mu,\rho}(f)\le4\int\abs{\nabla f}^2\dd\mu$ for log-concave $\mu$, and that linear functions have $\mathcal D_{\mu,\rho}(\inner ax)=\abs a^2$. Hence a frame with a dimension-free gap for $\mathcal D_{\mu,\rho}$ gives KLS with constant $4C$ ([](#conj:conditional-fiber-frame)), by a mechanism that uses only one-dimensional inequalities. The comparison with the gradient is the sharp one-dimensional inequality $\CP\le4\Var$ of Section [](#sec:kls-examples), applied on each line; the normalization by the conditional variance is chosen so that linear functions carry exactly their Euclidean energy, so the form cannot lose on the functions that define the covariance. What it may lose on is shown by the most natural frame on the simplex, the root directions $(e_i-e_j)/\sqrt2$: [](#prop:conditional-fiber-root-obstruction) shows its gap is $O(m^{-2})$ on the isotropic simplex of dimension $m-1$. The witness is the indicator of a corner $\{mP_1>m-\varepsilon\}$: only the $m-1$ root directions through that vertex can move it, and in the normalization of the form each carries weight of order $m^{-3}$ there. The simplex itself has a dimension-free Poincaré constant by [](#cor:cmh-dirichlet-poincare), so the frame, not the measure, is at fault. The failure does not show at any fixed polynomial degree: for degree at most $k$, every admissible frame has form at least $3/[k(k+1)^2(k+2)]$ times the variance ([](#lem:fiber-polynomial-floor)). The sharper degree-two value for the root frame is $(m+2)(m+3)/(5m^2)>1/5$ ([](#lem:fiber-root-degree-two)).

(subsec:overview-one-cut)=
### Following one cut: a ceiling and two counterexamples

The fixed cut, the oldest localization argument developed here and now kept as an archive, follows one cut $E$ of mass $\tfrac12$ and tracks the excess $e_t(E)$ of its boundary over the isoperimetric profile of the localized measure. Its results are limits and counterexamples, and they apply to any argument that follows a set.

**The near-worst bootstrap.** [](#thm:bootstrap) says that, for a measure whose Cheeger constant is within a factor $1+\varepsilon$ of the smallest in its dimension, the excess propagates along localization with one quantity as the only interface, $\Xi_T(\mu)=\int_0^T\E(\lmax(A_t)-1)_+\dd t$. Two deterministic comparisons do the work: the isoperimetric profile of a log-concave measure is concave and symmetric, so its Cheeger constant is read at mass $\tfrac12$; and whitening a localized measure of covariance $A_t$ loses at most $\lmax(A_t)^{1/2}$ against the worst isotropic measure of the same dimension. Near-worstness compares the localized Cheeger constant with that of $\mu$, and every loss is charged to $(\lmax(A_t)-1)_+$. The published covariance estimates give $\Xi_T\le C(1+\log\log n)$ ([](#cor:loglog)). [](#prop:ceiling) proves that an all-measure bound $\Xi_{T_0}(\mu)\le\kappa T_0$ at a sufficiently small universal time is itself sufficient for KLS. This measures how strong that one input would have to be; it says nothing against other propagation arguments.

**Independent spectators break global covariance weights.** The fixed-cut argument wanted a propagation estimate for the excess weighted by $(1+\norm{A_t}_\op)^{5/2}$, stated as [](#conj:weighted-excess-rate). [](#prop:weighted-spectator-obstruction) exhibits, for any proposed constants, a product of centred exponentials and a cylinder cut with arbitrarily small initial excess on which that estimate fails. The mechanism is the covariance spike of Section [](#subsec:kls-spike-obstruction): take a good cut in a few coordinates and add many independent exponential coordinates it does not depend on. Their spikes inflate the global weight and depress the isoperimetric profile of the localized measure, while the cut does not notice them — the estimate fails the tensorization test. Removing the weight does not help ([](#prop:spectator-excess-rate-obstruction)): a surviving estimate must also change its remainder, for instance to one linear in $T$, or assume the measure near-worst, as [](#thm:bootstrap) does. Every witness is a product, and so satisfies KLS.

(sec:overview-open)=
## Problems for someone who might take them up

Three problems are presented here for a reader who wants to start. Each is stated precisely in its chapter, and none of the three has an answer in the literature that we are aware of. None is decided by the proofs of KLS, and each asks for something they do not give: a sharp constant, an elementary one-dimensional mechanism, or a localization mechanism that ignores covariance spikes.

**The sharp linear test of the moment-Hessian inequality, [](#conj:gate-zero-sharp).** The linear test is the moment-Hessian inequality tested on linear functions only: the cheapest test it must pass, and so the first one that any proof of it, or any counterexample, goes through. The sharp form asks whether $\E H^2\preceq2\,\Id$ for the Stein kernel of the moment map of every isotropic log-concave measure. *Why it matters:* it asks for a sharp constant, $2$, attained by products of exponentials, which none of the three proofs gives. It is the operator form of the Chen–Klartag trace inequality $\Tr\E H^2\le2n$ ([](#thm:chen-klartag-moment-hessian)); by [](#cor:gate-zero-third-moment) it contains the sharp directional third-moment bound $\kappa_n\le2$, where the preprint literature reaches $2\sqrt2$ ([](#prop:letwin-kappa)); and it refines [](#conj:gate-zero), the linear shadow of the moment-Hessian inequality. A counterexample to it would leave KLS untouched. *What there is:* products of centred exponentials attain it in every direction, and every exponential cone with $\beta=n$ attains it in its axis direction, whatever the base ([](#prop:cone-linear-sector)); every product-simplex cone satisfies it, with transverse equality exactly when the base is a single simplex and $\beta=n$ ([](#prop:product-simplex-cone-gate)). An interval counts as a one-dimensional simplex. Any argument must be tight on these, and by [](#prop:letwin-not-gate-zero) no argument through fixed-matrix energies alone can succeed. *Where to start:* Section [](#subsec:gate-zero), and the spectral resolution of the linear sector in [](#lem:cmh-linear-spectral-resolution).

**A conditional-fiber frame, [](#conj:conditional-fiber-frame).** It asks whether every isotropic log-concave measure admits one frame of directions, chosen before the test function, for which the resampling form of [](#lem:conditional-fiber-form) has a dimension-free gap. *Why it matters:* it would give an elementary, purely one-dimensional mechanism for the Poincaré bound, with constant $4C$: it uses nothing beyond one-dimensional log-concave inequalities and a choice of directions. *What failed:* the root frame of the simplex ([](#prop:conditional-fiber-root-obstruction)). *Where to start:* the simplex itself is a self-contained test case, whose Poincaré constant is dimension-free, so the question there bears only on the frame idea. Either find an isotropic frame with a dimension-free gap on the simplex, or show that none exists; by [](#lem:fiber-polynomial-floor), polynomial certificates of the second alternative must have degrees growing with dimension: every fixed degree has a positive uniform floor, for every admissible frame. Section [](#subsec:fiber-root-failure) gives a short complete argument and is the place to begin.

**The occupation estimate for one eigenfunction, [](#conj:mm-spectral-occupation).** *Why it matters:* it would give a localization mechanism that ignores covariance spikes: it asks for control of an object — the tensor $H_t$ of one fixed eigenfunction — that does not see spikes in directions the eigenfunction does not use, so it is not ruled out by [](#prop:covariance-spike); by [](#prop:spectral-sufficiency) it implies KLS. *What there is:* the time-weighted budget [](#lem:mm-time-weighted-fixed-source) and the stopped source bound [](#lem:mm-stopped-window-source). The small-gap occupation implication in [](#prop:mm-window-occupation) has an empty admissible class. *Where to start:* Section [](#subsec:spectral-window-chain). What is missing is control of the source after covariance exits on a time interval of universal length; the time-weighted and stopped budgets do not supply that control.

From here, the [reading paths](#sec:reading-paths) of the welcome page lead on: to the map of the alternative mechanisms in Chapter [](#sec:frontier-atlas), to the entry chapter of one mechanism, or to how results are checked before one contributes.

% Agents: the brief's neighbourhood also lists conj:trace-upgrade (unlabelled here, Section sec:open) and
% ass:uniform-cmh-approximants; they are not presented as entry problems because conj:trace-upgrade has no
% labelled statement and uniform CMH(4) is at least as hard as KLS with no smaller entry point
% beyond conj:gate-zero-sharp.
% Order of the entry problems (owner's decision, 2026-10-06): conj:gate-zero-sharp first (sharp
% constant 2, given by neither proof), then conj:conditional-fiber-frame (elementary 1-D mechanism),
% then conj:mm-spectral-occupation (localization ignoring spikes). No bare "it implies KLS" motivation.
