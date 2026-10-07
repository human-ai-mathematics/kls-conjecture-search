---
title: 'BKL: analytic foundations and tensor symmetrization'
ledger-node:
  - lem:bkl-analytic-foundations
  - lem:bkl-tensor-symmetrization
numbering:
  enumerator: '130.%s'
---

*Part of the Bizeul–Klartag–Lehec proof, Chapter [](#sec:bkl-proof); the reading order is on the [full proofs](#sec:proofs-bkl) page.*

**Overview.** This reconstructs the analytic interfaces of Section 2 of
[@BizeulKlartagLehec2026KLS], version
[arXiv:2610.05474v1](https://arxiv.org/html/2610.05474v1).
We establish closure of the polynomial-growth class under the inverse
Laplacian, justify the eigenfunction used by the criterion, and prove the
finite-dimensional tensor recovery inequality by an incidence calculation.
Regular approximation is arranged through compactly supported intermediate
measures; this makes the extra derivative-growth requirement explicit.

**Dependencies.** The normalization is [](#def:bkl-tilt-cumulants).
The spectral construction, graph core, Bochner identity and scalar
Poincaré stability for smooth potentials with two-sided positive Hessian
bounds are supplied by [](#lem:sz-analytic-foundations).
We prove below the additional polynomial-growth assertions needed here.
The tensor argument has no analytic or probabilistic input. In particular,
neither KLS nor the uniform Appell bound is used.

% Author identity: plan_import (researcher), unknown, 2026-10-06.
% This dossier is an uncertified reconstruction, not its own review.

## The analytic class and its operators

:::{prf:theorem} Analytic foundations in the BKL regular class
:label: thm:sol-bkl-analytic-foundations
Let $\mu(dx)=e^{-V(x)}dx$ be a probability on $\mathbb R^n$, where
$V\in C^\infty$, $aI\preceq D^2V\preceq bI$ for some $0<a\le b<\infty$,
and every derivative of $V$ has at most polynomial growth.
Let $\mathcal A$ consist of the smooth functions all of whose derivatives
have at most polynomial growth, and put
$\mathcal A_0=\{g\in\mathcal A:\int g\,d\mu=0\}$.
Set $L=\Delta-\nabla V\cdot\nabla$.

The operator $L$ preserves $\mathcal A$, and for $u,v\in\mathcal A$,

$$
\int (Lu)v\,d\mu=-\int\nabla u\cdot\nabla v\,d\mu,
\qquad
\|Lu\|_2^2=\|D^2u\|_2^2+
\int\langle D^2V\nabla u,\nabla u\rangle\,d\mu.
$$

Writing $\lambda=C_P(\mu)^{-1}$, one has $\lambda>0$ and a real
$f\in\mathcal A_0$ with $\|f\|_2=1$ and $-Lf=\lambda f$.
For every $g\in\mathcal A_0$ there is exactly one $u\in\mathcal A_0$
satisfying $-Lu=g$, and

$$
\|u\|_2\le\lambda^{-1}\|g\|_2,\qquad
\|\nabla u\|_2^2=\langle g,u\rangle
\le\lambda^{-1}\|g\|_2^2,\qquad
\|\nabla_0u\|_2\le\lambda^{-1/2}\|g\|_2,
\tag{A1}
$$

where $\nabla_0u=\nabla u-\int\nabla u\,d\mu$.
All identities and inequalities extend componentwise to tensors, using
the sum over ordered indices. Every isotropic log-concave probability is
a weak limit of isotropic probabilities in this regular class, with
convergence of every polynomial moment. A uniform scalar Poincaré
inequality on that class passes to the limit.
These are the assertions of [](#lem:bkl-analytic-foundations).
:::

:::{prf:proof}
Strong convexity gives
$V(x)\ge V(0)+\nabla V(0)\cdot x+a|x|^2/2$.
Thus polynomial-growth functions and their derivatives belong to every
finite $L^p(\mu)$. Products and derivatives preserve $\mathcal A$, as
does $L$. Cut off at radius $R$ with a smooth function $\chi_R$ whose
first two derivatives are bounded by $C/R$ and $C/R^2$. In integration
by parts the error is an integral of a polynomial-growth function times
a derivative of $\chi_R$, supported where $|x|\ge R$; Gaussian decay
makes it tend to zero. This proves the first identity.
In particular $u,Lu\in L^2(\mu)$ and $u$ is in the weak domain of
$-L$. The graph-core and Bochner assertions of
[](#lem:sz-analytic-foundations) apply and give the second identity.
They also give compact resolvent, constants as the kernel, and a
normalized first nonconstant eigenfunction in the operator domain,
with eigenvalue $\lambda=C_P^{-1}>0$.

We next show that this eigenfunction lies in $\mathcal A$; the argument
also specifies the growth issue behind this regularity statement.
Interior elliptic regularity first makes $f$ smooth. Choose an integer
$m$ with $2ma>\lambda+1$ and put $w(x)=(1+|x|^2)^m$.
The Hessian bounds imply

$$
\langle x,\nabla V(x)\rangle\ge a|x|^2-O(|x|),
\qquad
\frac{Lw}{w}\le-2ma+O(|x|^{-1})\quad (|x|\longrightarrow\infty).
\tag{A2}
$$

Indeed, $\nabla w/w=2mx/(1+|x|^2)$ and
$\Delta w/w=O(|x|^{-2})$; insert these in $Lw/w$.
Fix a radius outside which
$c=-Lw/w-\lambda\ge c_0>0$.
Let $v=f/w$ and let $d\rho=w^2\,d\mu$.
The equation for $f$ becomes, in weak form,

$$
-\operatorname{div}(w^2e^{-V}\nabla v)
+c\,w^2e^{-V}v=0.
\tag{A3}
$$

Here $v\in L^2(\rho)$ and $\nabla v\in L^2(\rho)$: the latter follows
from $\nabla f\in L^2(\mu)$ and boundedness of $\nabla\log w$.
The function $c$ is bounded, since $\nabla V$ has linear growth.
Choose $C>0$ so that $v<C$ on a slightly larger closed ball and set
$h=(v-C)_+$. Its support lies in the exterior where $c\ge c_0$.
Testing (A3) against $\chi_R^2h$ gives

$$
\int\chi_R^2|\nabla h|^2\,d\rho+
\int c\,v h\,\chi_R^2\,d\rho
=-2\int\chi_Rh\,\nabla h\cdot\nabla\chi_R\,d\rho.
$$

On $\{h>0\}$, $v=h+C$, so the second integral is nonnegative.
Young's inequality therefore bounds half the gradient integral and
the entire second integral by
$2\int h^2|\nabla\chi_R|^2\,d\rho\le CR^{-2}\|v\|_{L^2(\rho)}^2$.
Letting $R\to\infty$ gives $h=0$, since $c\,vh\ge c_0h^2$.
Apply the same argument to $-f$. Thus $|f|\le Cw$.
This weak barrier argument does not require pointwise decay of a
Schrödinger transform of $f$ at infinity.

For completeness, polynomial growth of all derivatives follows from
local elliptic estimates with a shrinking radius. At $x_0$ use
$r=(1+|x_0|)^{-1}$ and rescale $x=x_0+ry$ to a fixed unit ball.
The rescaled equation has Laplacian principal part and drift
$r\nabla V(x_0+ry)$ bounded uniformly on that ball. Its first
derivatives are bounded uniformly because $D^2V$ is bounded.
Interior gradient estimates bound $|\nabla f(x_0)|$ by a fixed power
of $1+|x_0|$ times the supremum of $|f|$ on the ball. For a multi-index
$\alpha$, differentiating $(L+\lambda)f=0$ yields

$$
(L+\lambda)\partial^\alpha f
=\sum_{0<\beta\le\alpha}\binom{\alpha}{\beta}
(\partial^\beta\nabla V)\cdot
\nabla\partial^{\alpha-\beta}f.
\tag{A4}
$$

If the derivatives of $f$ through order $|\alpha|$ have polynomial
growth, the right side does too. Apply the same interior gradient
estimate to $\partial^\alpha f$, now with this right side.
Rescaling contributes only powers of $r^{-1}$; the coefficient
derivatives are polynomially bounded by the hypotheses on $V$.
Induction gives polynomial growth at every order. Hence $f\in\mathcal A$.
The estimates invoked here are the classical interior estimates for
a uniformly elliptic equation with smooth coefficients on a fixed ball;
no estimate uniform in derivative order, dimension or $\mu$ is needed.

For $g\in\mathcal A_0$, spectral calculus on the centered subspace gives
a unique $u\in\operatorname{Dom}(-L)\cap L^2_0(\mu)$ with $-Lu=g$ and
$\|u\|_2\le\lambda^{-1}\|g\|_2$.
The form identity gives the middle statement of (A1).
Interior regularity again makes $u$ smooth.
Choose $m$ large enough that the same polynomial $w$ satisfies
$-Lw\ge|g|$ outside a ball; (A2) and polynomial growth of $g$ permit
this choice. Choose $C\ge1$ with $u<Cw$ on a slightly larger ball.
Now $h=(u-Cw)_+$ vanishes near that ball, lies in the form domain,
and satisfies $0\le h\le |u|$.
The weak equation for $u-Cw$ gives

$$
\int\chi_R^2|\nabla h|^2\,d\mu
+2\int\chi_Rh\,\nabla h\cdot\nabla\chi_R\,d\mu
=\int(g+CLw)\chi_R^2h\,d\mu\le0.
$$

Consequently
$\int\chi_R^2|\nabla h|^2\,d\mu
\le4\int h^2|\nabla\chi_R|^2\,d\mu
\le CR^{-2}\|u\|_2^2$.
Exhaustion makes $\nabla h=0$, and $h$ vanishes on a ball, so $h=0$.
Repeating with $-u$ gives $|u|\le Cw$.
Differentiate $Lu=-g$ and repeat the rescaled interior estimate:
the new right sides involve derivatives of $g,V$ and already
controlled derivatives of $u$. Thus $u\in\mathcal A_0$.
Uniqueness in this class follows from the form identity: a centered
solution of $Lv=0$ has zero gradient and is zero. Subtracting the mean
from $\nabla u$ is an orthogonal projection in $L^2$, proving the last
inequality of (A1). Summing the scalar arguments over tensor components
proves all componentwise claims.

Finally consider an arbitrary isotropic log-concave $\mu$.
Condition on growing balls, then center and whiten. The resulting
compactly supported isotropic laws converge weakly to $\mu$, and
their moments converge at each fixed order, by integrability of all
polynomials and convergence of the affine normalizations to the identity.
For a fixed one of these compactly supported laws, write it as the law
of $X$, and convolve with $N(0,\delta I)$. Apart from a constant its
density is

$$
p_\delta(y)=
e^{-|y|^2/(2\delta)}
\int e^{y\cdot x/\delta-|x|^2/(2\delta)}\,d\mu_X(x).
\tag{A5}
$$

The logarithmic derivatives of the last integral are cumulants of a
probability supported in the same fixed compact set. Every such
derivative, of each fixed order, is bounded uniformly in $y$: it is a
finite polynomial in moments of bounded coordinates. Thus derivatives
of $-\log p_\delta$ of order at least two are bounded, while its first
derivative has at most linear growth.
The Hessian formula and convolution log-concavity in
[](#lem:sz-analytic-foundations) give
$0\preceq D^2(-\log p_\delta)\preceq\delta^{-1}I$.
Multiplication of $p_\delta$ by $e^{-\epsilon|y|^2/2}$, followed by
normalization, gives a potential with
$\epsilon I\preceq D^2V\preceq(\epsilon+\delta^{-1})I$ and all
derivatives polynomially bounded.
Centering and whitening preserve this class.
For each compact intermediate law, letting $\delta\to0$ preserves
every fixed polynomial moment, by the binomial expansion of $X+\sqrt
\delta Z$ and finiteness of Gaussian moments. For fixed $\delta$,
letting $\epsilon\to0$ preserves those moments by dominated convergence.
For the $j$th intermediate law choose $\delta_j,\epsilon_j$ so that the
errors of all moments of degree at most $j$ are at most $1/j$.
Include convergence against a countable determining family of bounded
continuous functions in this diagonal choice.
Its means and covariances tend to $0,I$; centering and whitening
therefore preserve weak convergence and convergence of every
fixed polynomial moment.
The individual Hessian bounds need not be uniform.
The scalar stability assertion of [](#lem:sz-analytic-foundations)
passes any common Poincaré bound to $\mu$, including locally Lipschitz
tests of finite energy. This completes the analytic assertions.
:::

## Recovering a tensor from partial symmetrization

:::{prf:theorem} Two-block tensor recovery
:label: thm:sol-bkl-tensor-symmetrization
For integers $n,d\ge1$ let $T$ be a tensor over $\mathbb R^n$ with at
least $3d$ slots, invariant under permutations of its first $d$ slots
and, separately, its next $2d$ slots.
If $\mathcal S_q$ averages permutations of the first $q$ slots, then

$$
|T|\le\binom{2d}{d}|\mathcal S_{2d}T|
\le4^d|\mathcal S_{2d}T|.
\tag{A6}
$$

All norms are full Hilbert--Schmidt norms. This proves
[](#lem:bkl-tensor-symmetrization).
:::

:::{prf:proof}
Put $\Omega=\{1,\ldots,3d\}$. For each $d$-element subset $F$ of
$\Omega$, let $T_F$ be the copy of $T$ obtained by moving its first
block into the slots $F$ and the second block into $\Omega\setminus F$.
Leave all other slots fixed. The assumed symmetries make $T_F$
independent of the order chosen within either block.
Expand the following sums using the Hilbert-space scalar product:

$$
\sum_{\substack{E\subset\Omega\\|E|=2d}}
\left|\sum_{\substack{F\subset E\\|F|=d}}T_F\right|^2
=
\sum_{s=0}^d\binom ds
\sum_{\substack{S\subset\Omega\\|S|=s}}
\left|\sum_{\substack{F\supset S\\|F|=d}}T_F\right|^2.
\tag{A7}
$$

To verify equality, fix $F,F'$ and write $r=|F\cap F'|$.
The coefficient of $\langle T_F,T_{F'}\rangle$ on the left is the
number of $2d$-sets containing $F\cup F'$:
$\binom{d+r}{r}$.
On the right it is
$\sum_{s=0}^d\binom ds\binom rs=\binom{d+r}{d}$ by the
Vandermonde identity. The two coefficients agree, proving (A7)
term by term.

Every summand on the right is nonnegative. Keeping only $s=d$
bounds that side below by
$\sum_{|F|=d}|T_F|^2=\binom{3d}{d}|T|^2$.
For $E=\{1,\ldots,2d\}$, averaging permutations of $E$ sends the
first block of $T$ uniformly onto its $d$-subsets. Therefore the
inner sum on the left is
$\binom{2d}{d}\mathcal S_{2d}T$.
For any other $E$ it is a permutation of this same tensor, so it has
the same norm. The left side is consequently
$\binom{3d}{2d}\binom{2d}{d}^2|\mathcal S_{2d}T|^2$.
Since $\binom{3d}{2d}=\binom{3d}{d}$, cancellation proves the first
inequality of (A6). The second follows from
$\binom{2d}{d}\le\sum_{j=0}^{2d}\binom{2d}{j}=2^{2d}$.
:::

**Source concordance.** The operator assertions and the inverse on
$\mathcal A_0$ reconstruct BKL Section 2 and Lemma 2.1.
The incidence identity reconstructs Lemma 2.2.
The polynomial barrier for the eigenfunction above is a weak-form
justification of the growth assertion; the compact-support first
approximation supplies an explicit route to the stronger regular class.

**Fences respected.** No additional bounded-by edge is proposed.
[](#rem:projection-ceiling) is respected by recovering full tensors.
[](#rem:relative-ceiling), [](#rem:crude-insufficient), and
[](#rem:profile-circularity) concern stochastic occupation or profiles;
no such estimate is asserted here. The inverse operator is taken only
at one fixed regular measure; no inverse or eigenfunction is passed
through an approximation limit. None of these foundations establishes
the premise of the tilt criterion.
