---
title: "Solution: Letwin's general KLS bound"
ledger-node: thm:letwin-kls
numbering:
  enumerator: "108.%s"
---

*Part of the results of the literature written out here, Chapter [](#sec:family-moment-map); the reading order is on the [full proofs](#sec:proofs-literature) page.*

**Overview.** The third-moment bound gives a fixed-time covariance window.
A Gaussian observation transfers the variance of each Lipschitz test to
its posterior. The improved Lichnerowicz inequality bounds the posterior
Poincaré constant. Choosing the observation time below both the covariance
window and the initial spectral gap closes the estimate without assuming
the desired bound on that gap. A published regular approximation then
removes the smoothness restriction.

**Sources and exact inputs.** The claim is Theorem 1.1 of
[@Letwin2026QuadraticKLS], pinned to
[arXiv:2607.24164v1](https://arxiv.org/html/2607.24164v1).
Its quadratic input is supplied here by [](#thm:letwin-qcts), whose proof
is in [the separate dossier](thm-letwin-imports.md); the present dossier
reconstructs the remaining passage to the general Poincaré constant.
The published sources used in this passage are:

- [@KlartagLehec2022Polylog, Corollary 5.4], checked in
  [arXiv:2203.15551v2, Section 5](https://arxiv.org/html/2203.15551v2#S5):
  universal constants $a,b>0$ give
  $\mathbb E\|A_t\|_{\mathrm{op}}\le b$ for
  $0<t\le a/(\kappa_n^2\log n)$. Only its moment exponent $p=1$ is used.
- [@Klartag2023Logarithmic], checked in the published-version PDF
  [arXiv:2303.14938v2](https://arxiv.org/pdf/2303.14938v2),
  DOI [10.15781/jsjy-0b06](https://doi.org/10.15781/jsjy-0b06):
  Theorem 1.3 is [](#thm:improved-lichnerowicz); Lemma 2.1 supplies
  regular approximation. The variance-transfer mechanism of Lemma 3.1
  and Corollary 3.2 is written out below, including its restriction on time.
- The published Lipschitz-variance comparison of
  [@Milman2009Isoperimetric], in the explicit normalization (3.10) of
  the preceding PDF, gives a universal $c_M>0$ such that
  $c_M\CP(\nu)\le\sup_{\operatorname{Lip}(f)\le1}\operatorname{Var}_\nu f$
  for log-concave $\nu$. This comparison is an imported theorem, not a
  consequence of the elementary Poincaré inequality in the other direction.

The constants $a,b,c_M$ do not depend on dimension, the initial law, its
regularization parameters, or the test function. They need not be optimal.
The published theorem [](#thm:klartag-logn) is not used as an input.

:::{prf:theorem} General bound from the quadratic input
:label: thm:sol-letwin-kls
There is a universal constant $C>0$ such that, for every integer $n\ge2$,

$$
C_{\mathrm P,n}\le C\sqrt{\log n},
\qquad
\PsiKLS_n\le C(\log n)^{1/4},
$$

where the suprema are over all isotropic log-concave probability measures
on $\mathbb R^n$, with the Poincaré and inverse-Cheeger normalizations of
Section [](#sec:kls-orientation). This is [](#thm:letwin-kls).
:::

:::{prf:proof}
**The third-moment parameter.** Use exactly the parameter of
[](#prop:letwin-kappa):

$$
\kappa_n=\sup_{\nu\text{ isotropic log-concave on }\mathbb R^n}
\sup_{|u|=1}
\left\|\mathbb E_\nu[\langle X,u\rangle X\otimes X]\right\|_{\mathrm{HS}}.
$$

The source's Schatten two-norm is the Hilbert--Schmidt norm; fixing the
direction to the first coordinate gives the same supremum by orthogonal
invariance. In particular the expectation is taken **before** the matrix
norm. The antecedent of [](#prop:letwin-kappa) is discharged by
[](#thm:letwin-qcts), giving $\kappa_n\le2\sqrt2$.
Also $\kappa_n\ge2$: take independent $X_i=E_i-1$, where each $E_i$ has
density $e^{-s}\mathbf1_{s>0}$. These variables have mean zero, variance
one and third moment two. Independence makes
$\mathbb E[X_1X\otimes X]=2e_1\otimes e_1$.

**The regular class and posterior.** Initially let $\mu$ be isotropic and
regular in the sense of Klartag's Section 2: its density $e^{-U}$ is smooth
and positive on $\mathbb R^n$, with
$\varepsilon I\preceq\nabla^2U\preceq\varepsilon^{-1}I$ for some
$\varepsilon>0$, and all derivatives of $U$ have at most polynomial growth.
Write $P=\CP(\mu)$. Then $1\le P<\infty$: coordinate tests give the lower
bound and strong convexity gives $P\le1/\varepsilon$.

Fix $t>0$ and let $Y=tX+\sqrt t G$, with $X\sim\mu$ and an independent
standard Gaussian $G$ in $\mathbb R^n$. Bayes' formula gives the conditional
law of $X$ given $Y=y$ as

$$
\mu_{t,y}(dx)=Z(t,y)^{-1}
e^{\langle y,x\rangle-t|x|^2/2}\mu(dx).
$$

The normalizer is positive and finite. Denote its mean by $m(t,y)$ and its
covariance by $A(t,y)$. The localization covariance $A_t$ has the same law
as $A(t,Y)$; this is the observation representation (3.1)--(3.5) of
Klartag's Section 3. No assertion about a supremum over times is needed.
The posterior Hessian is $\nabla^2U+tI\succeq tI$, so the ordinary and
improved Lichnerowicz inequalities give, for every $y$,

$$
A(t,y)\preceq t^{-1}I,
\qquad
\CP(\mu_{t,y})\le\sqrt{\|A(t,y)\|_{\mathrm{op}}/t}.
$$

The first inequality follows by applying $\CP(\mu_{t,y})\le1/t$ to
linear tests; the second is [](#thm:improved-lichnerowicz).
These applications are to full-space smooth positive densities and
introduce no boundary condition.

**Variance transfer, with its time factor.** For a globally 1-Lipschitz
$f$, put $F(y)=\int f\,d\mu_{t,y}$. All relevant moments are finite.
Differentiation under the integral is justified on compact sets of $y$
by the Gaussian factor in the likelihood and the at-most-linear growth
of $f$. It yields

$$
\nabla F(y)=\operatorname{Cov}_{\mu_{t,y}}(X,f),
\qquad
|\nabla F(y)|^2\le
\|A(t,y)\|_{\mathrm{op}}\operatorname{Var}_{\mu_{t,y}}f.
$$

The latter inequality is Cauchy--Schwarz after pairing the vector with
each unit direction. Tensorization and the chain rule give
$\CP(Y)\le t^2P+t$. Explicitly, conditional variance first in $G$ and
then in $X$ bounds the variance of $g(tX+\sqrt tG)$ by
$(t+t^2P)\mathbb E|\nabla g(Y)|^2$; Jensen bounds the derivative of
the conditional mean in the second term. Smooth approximation extends
this inequality to functions with finite Dirichlet energy.
It applies to $F$: conditional expectation is an $L^2$ contraction, and
the preceding gradient estimate and covariance cap give
$\mathbb E|\nabla F(Y)|^2\le t^{-1}\mathbb E
\operatorname{Var}_{\mu_{t,Y}}f<\infty$.
Consequently

$$
\operatorname{Var}(F(Y))
\le(t^2P+t)\mathbb E|\nabla F(Y)|^2
\le(1+tP)\mathbb E\operatorname{Var}_{\mu_{t,Y}}f.
$$

The conditional-variance identity now gives

$$
\operatorname{Var}_\mu f
=\mathbb E\operatorname{Var}_{\mu_{t,Y}}f+\operatorname{Var}(F(Y))
\le(2+tP)\mathbb E\operatorname{Var}_{\mu_{t,Y}}f.
$$

As $|\nabla f|\le1$ almost everywhere, the posterior Poincaré inequality
and then the improved bound imply

$$
\operatorname{Var}_\mu f
\le\frac{2+tP}{\sqrt t}\,
\mathbb E\sqrt{\|A_t\|_{\mathrm{op}}}.
$$

Taking the supremum over globally 1-Lipschitz tests and using the
published comparison with constant $c_M$ gives the precise bridge

$$
c_MP\le\frac{2+tP}{\sqrt t}
\mathbb E\sqrt{\|A_t\|_{\mathrm{op}}}.
$$

In particular, a uniform numerical bound on $2+tP$ is required. This is
the time restriction in the published Corollary 3.2, rather than an
unconditional estimate at every point of the covariance window.

**Closing the time restriction.** Set

$$
T=\frac{a}{\kappa_n^2\log n},
\qquad t=\min\{T,P^{-1}\},
\qquad K=\frac{3\sqrt b}{c_M}.
$$

These times are strictly positive because $n\ge2$ and
$2\le\kappa_n\le2\sqrt2$. The published covariance estimate applies at
$t\le T$. Jensen's inequality gives
$\mathbb E\sqrt{\|A_t\|_{\mathrm{op}}}\le\sqrt b$.
Since $tP\le1$, the bridge becomes $P\le K/\sqrt t$.
If $T\le P^{-1}$ this yields $P\le K/\sqrt T$.
If $P^{-1}\le T$ it yields $P\le K\sqrt P$, hence $P\le K^2$.
Equality of the two times causes no problem, so in all cases

$$
P\le\max\left\{K^2,\frac K{\sqrt a}\kappa_n\sqrt{\log n}\right\}
\le D\kappa_n\sqrt{\log n},
\qquad
D=\max\left\{\frac{K^2}{2\sqrt{\log2}},\frac K{\sqrt a}\right\}.
$$

The last step uses $\kappa_n\sqrt{\log n}\ge2\sqrt{\log2}$.
Thus $D$ is universal. This choice of time uses no a priori quantitative
bound for $P$ and no near-maximizer of $C_{\mathrm P,n}$ or $\PsiKLS_n$.

**Removal of regularity.** Let now $\mu$ be any isotropic log-concave
probability on $\mathbb R^n$. Its affine support is all of $\mathbb R^n$
because its covariance is $I$, so it is absolutely continuous. Its
Poincaré constant is finite in each fixed dimension by the qualitative
log-concave Poincaré theorem [@Bobkov1999LogConcave]; no estimate of that
constant is used. Apply the published Lemma 2.1 of
[@Klartag2023Logarithmic]: for every $0<\delta<1$ there is a regular
log-concave law $\nu_\delta$ with

$$
\CP(\nu_\delta)\ge\CP(\mu)-\delta,
\qquad \|\operatorname{Cov}(\nu_\delta)-I\|_{\mathrm{op}}<\delta.
$$

The lemma's additional assertion about preserving a positive curvature
lower bound is not needed here. Write $m_\delta$ and $S_\delta$ for the
mean and covariance of $\nu_\delta$. Since $S_\delta\succ0$, the affine
image under $x\mapsto S_\delta^{-1/2}(x-m_\delta)$ is isotropic and still
regular: the Hessian transforms by congruence, its two positive bounds
remain finite, and polynomial growth of derivatives is preserved by a
fixed invertible affine map. The regular-case estimate applies to this
image. Pulling its Poincaré inequality back by the chain rule gives

$$
\CP(\mu)-\delta\le\CP(\nu_\delta)
\le\|S_\delta\|_{\mathrm{op}}D\kappa_n\sqrt{\log n}
\le(1+\delta)D\kappa_n\sqrt{\log n}.
$$

Here the same $\kappa_n$ bounds every isotropic approximant; no
continuity of $\kappa_n$, eigenfunctions, or posterior paths is required.
Letting $\delta\downarrow0$ proves the bound for $\mu$, including uniform
laws on convex bodies and nonsmooth convex potentials. The Poincaré
constant throughout is the constant for all locally Lipschitz tests,
not just the globally Lipschitz tests used to estimate it.

Finally $\kappa_n\le2\sqrt2$ implies
$C_{\mathrm P,n}\le2\sqrt2D\sqrt{\log n}$.
The reverse-Cheeger direction of [](#eq:cheeger-two-sided), namely
$\PsiKLS_\mu^2\le\pi\CP(\mu)$, then gives the inverse-Cheeger bound.
The single constant
$C=\max\{2\sqrt2D,\sqrt{2\sqrt2\pi D}\}$ works in both inequalities.
All logarithms are natural.
:::

**Hypotheses and fences.** Isotropy identifies the initial covariance and
the dimensionwise parameter $\kappa_n$. Log-concavity is used in the
covariance theorem, the posterior curvature bound, the Lipschitz-variance
comparison and regular approximation. The restriction $n\ge2$ keeps the
window positive and permits absorption of the constant branch.
Regularity is an intermediate hypothesis removed in the proof.
The node has no registered `bounded_by` edge. Against the program's
general fences: this dimension-dependent bound does not settle
[](#conj:kls); the proof never upgrades a fixed-time moment to a
supremum-over-time event; it makes no trace-to-operator substitution;
and it uses no cut-relative source, moving competitor, gate-zero, or
CMH premise. The only preprint input is the separately reviewed
[](#thm:letwin-qcts), through [](#prop:letwin-kappa). No additional
conditional premise or numerical experiment is used.
