---
title: The problem
numbering: false
relies-on:
  conj:kls: {status: open, fingerprint: b34221c5440f365f12cb6529324aed7a62b355236e5a037761de51f02adeab69}
  prop:products: {status: proved, fingerprint: 85b9ec9b7b81c783e52dce9f3edce41396f581da4f7a425bd3df9031860a6c8c}
  thm:cmh-1d: {status: proved, fingerprint: 20ca97481f8d3f33bab114618adc59596740cec2d34e37ad9c5c8ec1b9fa9904}
  thm:klartag-logn: {status: proved, fingerprint: 70dd5528111bc813bcfa6750d3afcfcdc31121dbf564fb0681db32265b576b60}
  thm:letwin-qcts: {status: open, fingerprint: 8e2ac0819f46db553fe83a6f3034436816565262316c2e6bde7d81baead1a082}
  prop:letwin-kappa: {status: open, fingerprint: 1b04c4bede249bc3a81062505abb913e3fc7dda6500c4c36b27cf1eb64c23bbd}
  thm:chen-klartag-thin-shell: {status: open, fingerprint: e5ca045da4693f7b43a52d66b6a7ee27bebfb7a4c945ab7f8dc5c8ed3f73449f}
  prop:covariance-spike: {status: proved, fingerprint: 161bf636e00b06d616360d86e08e775faacc85e3ebd8f62c91289807a22bfbb5}
checked: 2026-09-29
---

% stamp: written by check.py --stamp; do not edit
*Last checked against the research record: 2026-09-29.*
% end stamp

## The question

A probability measure $\mu$ on $\mathbb R^n$ is *log-concave* if it has a density $e^{-V}$
with $V$ convex; the uniform measure on a convex body and every Gaussian are examples. It is
*isotropic* if it is centred and its covariance matrix is the identity. The *Poincaré
constant* $C_{\mathrm P}(\mu)$ is the least constant with

$$
\operatorname{Var}_\mu(f)\;\le\;C_{\mathrm P}(\mu)\int_{\mathbb R^n}|\nabla f|^2\,\mathrm d\mu
\qquad\text{for every locally Lipschitz } f,
$$

that is, the inverse of the spectral gap of the natural diffusion attached to $\mu$.

The Kannan–Lovász–Simonovits conjecture [@KannanLovaszSimonovits1995] says that this
constant does not grow with the dimension:

:::{embed} #conj:kls
:::

**Why it is natural.** Testing the inequality on a linear function $f(x)=\langle x,v\rangle$
gives $\operatorname{Var}_\mu f=\langle\operatorname{Cov}(\mu)v,v\rangle$ and
$\int|\nabla f|^2\,\mathrm d\mu=|v|^2$, so always
$C_{\mathrm P}(\mu)\ge\|\operatorname{Cov}(\mu)\|_{\mathrm{op}}$. Written for measures in
any position, the conjecture is the reverse inequality up to a universal constant,

$$
C_{\mathrm P}(\mu)\;\le\;C\,\|\operatorname{Cov}(\mu)\|_{\mathrm{op}}
\qquad\text{for every log-concave } \mu \text{ on } \mathbb R^n,\ \text{every } n:
$$

*linear functions already detect the slowest mode of every log-concave measure.* The
geometric reading is the one Kannan, Lovász and Simonovits started from. Let
$h_\mu=\inf_A \mu^+(A)/\min\{\mu(A),1-\mu(A)\}$ be the Cheeger constant, where
$\mu^+(A)$ is the boundary measure of $A$. For log-concave measures
$\tfrac14\le 1/(h_\mu^2\,C_{\mathrm P}(\mu))\le\pi$ (Cheeger and Buser–Ledoux), so the
conjecture says that the cheapest way to cut a convex body into two large pieces is, up to a
universal factor, a hyperplane. A dumbbell — two balls joined by a thin tube — is cheap to
cut through its neck; convexity forbids necks, and the conjecture quantifies how completely.

The question came from the analysis of random walks used to compute the volume of a convex
body, whose mixing time is governed by $h_\mu$. It sits at the top of a chain of
implications,

$$
\text{KLS}\;\Longrightarrow\;\text{thin shell}\;\Longrightarrow\;\text{slicing},
$$

and no reverse implication is known in a dimension-free form.

## Examples by hand

**The Gaussian.** For the standard Gaussian, $C_{\mathrm P}=1=\|\operatorname{Cov}\|_{\mathrm{op}}$,
and linear functions are extremal: the model case, where the conjecture holds with constant one.

**An interval.** For the uniform measure on $[0,1]$, $\operatorname{Var}(x)=1/12$, and the
slowest mode is $f(x)=\cos\pi x$: $\operatorname{Var}f=1/2$ and $\int f'^2=\pi^2/2$, so
$C_{\mathrm P}=1/\pi^2$ (the Wirtinger inequality) and
$C_{\mathrm P}/\operatorname{Var}=12/\pi^2\approx1.22$. The slowest mode is not linear,
but a linear function is within a factor $1.22$ of it.

**The exponential.** Let $\mu$ have density $e^{-x}$ on $[0,\infty)$, so
$\operatorname{Var}(x)=1$. For $f(x)=e^{ax}$ with $0<a<\tfrac12$,

$$
\operatorname{Var}_\mu f=\frac1{1-2a}-\frac1{(1-a)^2},
\qquad
\int f'^2\,\mathrm d\mu=\frac{a^2}{1-2a},
\qquad\text{so}\qquad
\frac{\operatorname{Var}_\mu f}{\int f'^2\,\mathrm d\mu}=\frac1{(1-a)^2}\xrightarrow[a\to1/2]{}4 .
$$

Hence $C_{\mathrm P}(\mu)\ge4\operatorname{Var}(\mu)$, and in fact equality holds: in
dimension one, $C_{\mathrm P}\le4\operatorname{Var}$ for every log-concave law, and the
exponential is extremal (see [Theorem B](#site:thm-b), whose first case contains
exactly this statement). The extremal functions are not in $L^2$ at $a=\tfrac12$: the
slowest mode of the exponential escapes to infinity.

**Products.** The Poincaré constant of a product is the largest Poincaré constant of its
factors (tensorization), so a product of $n$ isotropic one-dimensional log-concave laws has
$C_{\mathrm P}\le4$ in every dimension; [](#prop:products) records the same fact for
the Cheeger constant.
The cube $[0,1]^n$ and the product of $n$ exponentials are therefore harmless. The
conjecture is about everything that is not a product: simplices, cones, balls of
non-Euclidean norms, and log-concave measures with no symmetry at all.

No family of log-concave measures is known for which the ratio
$C_{\mathrm P}(\mu)/\|\operatorname{Cov}(\mu)\|_{\mathrm{op}}$ grows with the dimension.
The whole gap is in the upper bound.

## What was known at the start

Write $C_{\mathrm P,n}$ for the supremum of $C_{\mathrm P}$ over isotropic log-concave
measures on $\mathbb R^n$. Part of the literature quotes $\psi_n\asymp C_{\mathrm P,n}^{1/2}$
(the inverse Cheeger constant) instead, which halves every exponent; both are given below.

| Year | $C_{\mathrm P,n}$ | $\psi_n$ | Main idea |
|---|---|---|---|
| 1995 | $O(n)$ | $O(n^{1/2})$ | The localization lemma [@KannanLovaszSimonovits1995] |
| 2013 | $O(n^{2/3}\log n)$ | $O(n^{1/3}\sqrt{\log n})$ | Stochastic localization [@Eldan2013ThinShell] |
| 2016/2024 | $O(n^{1/2})$ | $O(n^{1/4})$ | Covariance control along the localization [@LeeVempala2018; @LeeVempala2024] |
| 2021 | $e^{O(\sqrt{\log n\log\log n})}$ | same | Iterated matrix potentials [@Chen2021] |
| 2022 | $O(\log^{10}n)$ | $O(\log^5 n)$ | First polylogarithmic bound [@KlartagLehec2022Polylog] |
| 2023 | $O(\log n)$ | $O(\sqrt{\log n})$ | Improved Lichnerowicz inequality [@Klartag2023Logarithmic] |
| 2026, preprint | $O(\sqrt{\log n})$ | $O((\log n)^{1/4})$ | Sharp quadratic Poincaré inequality via moment maps [@Letwin2026QuadraticKLS] |

The best **published** bound is Klartag's $C_{\mathrm P,n}\lesssim\log n$
([](#thm:klartag-logn)). The last row is a first-version preprint of July 2026 that has not
been refereed. It rests on a sharp Poincaré inequality for quadratic polynomials,
$\operatorname{Var}(X^{\top}MX)\le 8\|M\|_{\mathrm{HS}}^2$ for isotropic log-concave $X$
([](#thm:letwin-qcts)), whose main consequence is a universal bound on third moments,
$\|\mathbb E[\langle X,\theta\rangle X\otimes X]\|_{\mathrm{HS}}\le2\sqrt2$
([](#prop:letwin-kappa)). Throughout this site both statements are treated as **open**,
however plausible: nothing marked proved here depends on them, and every result that uses
them says so.

The two weaker conjectures have moved. Slicing is solved: the isotropic constants are
bounded [@KlartagLehec2025Slicing]. For thin shell, $\operatorname{Var}|X|^2\le Cn$, a proof
was given in a 2025 preprint [@KlartagLehec2025ThinShell], and a July 2026 preprint
sharpens it to the optimal $\operatorname{Var}|X|^2\le8n$ ([](#thm:chen-klartag-thin-shell),
also treated as open here). Neither settles KLS. Eldan's reverse estimate bounds $\psi_n$
by a weighted average of thin-shell parameters [@Eldan2013ThinShell], and even optimal thin
shell leaves a harmonic sum worth $\log n$ in it. Thin shell controls one function,
$|x|^2$; KLS asks for every function.

**Where the last logarithm comes from.** The current bounds all run *stochastic
localization*. One observes $X\sim\mu$ through Gaussian noise of decreasing size,
$X+t^{-1/2}G$, and follows the conditional law $p_t$ of $X$. On average $p_t$ is $\mu$; at
time $t$ it is $t$-strongly log-concave, so its Poincaré constant is at most $1/t$; and a
cut of $\mu$ that stays balanced under $p_t$ inherits a boundary from it. The price is the
conditional covariance $A_t=\operatorname{Cov}(p_t)$, which moves randomly and must stay
bounded long enough. The published arguments control
$\|A_t\|_{\mathrm{op}}$ through the smooth maximum $\beta^{-1}\log\operatorname{Tr}e^{\beta A_t}$,
and approximating a maximum over $n$ directions to within a constant forces
$\beta\asymp\log n$. That entropy cost is where the remaining logarithm lives.

(site:obstacle)=
## The obstacle every method meets

The obvious repair is to bound $\|A_t\|_{\mathrm{op}}$ better. It cannot work, because the
statement it needs is false, and false for a measure that satisfies the conjecture:

:::{embed} #prop:covariance-spike
:::

This is due to Klartag and Lehec [@KLnotes]. The mechanism fits in a line. A centred
exponential coordinate has a flat tail: conditionally on a large observation, the prior
barely varies on the scale of the noise, so the posterior of that coordinate is essentially
the Gaussian noise itself, of variance $s$. One coordinate out of $n$ is that large with
probability about $e^{-s}$, so as long as $s\lesssim\log n$ some coordinate is, and the
top conditional eigenvalue is of order $s$ — while the product of exponentials has Poincaré
constant $4$.

Two lessons shape everything on the next page.

- **Pointwise covariance control is the wrong target.** An argument whose only use of the
  localization is a bound on $\|A_t\|_{\mathrm{op}}$ is trying to prove something false. It
  has to notice that a spike in a coordinate the extremal function ignores is harmless.
- **The tensorization test.** Evaluate any proposed estimate on a product of $n$
  independent copies of a one-dimensional law. A quantity that is not aware of the product
  structure charges $n$ coordinates $n$ times for a phenomenon that costs $O(1)$, and fails
  at scale. Several natural estimates fail exactly this way
  ([Counterexamples](#site:counterexamples)).

Behind both is one pattern. Every known method controls something *fixed* — one matrix, one
direction, one tilt — or *averaged* along a path; the conjecture needs the same control
*uniformly*, for an object allowed to depend on the measure or on the extremal function. The
gap is a quantifier in the wrong place, and each result on the next page is an attempt to
move it.
