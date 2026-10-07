---
title: "BK: uniform operator powers and integration seeds"
ledger-node:
  - lem:bk-uniform-power-bound
  - cor:bk-integration-powers
  - cor:bk-quadratic-seed
numbering:
  enumerator: "153.%s"
---

*Part of the Balasubramanian–Kasiviswanathan proof, Chapter [](#sec:bk-proof); the reading order is on the [full proofs](#sec:proofs-bk) page.*

**Overview.** The operator comparison first bounds the spectral radius. A recurrence
along each adjoint orbit then puts its largest normalized squared norm among the
first finitely many iterates. Summing second differences gives one prefactor for
all powers. Two applications give integration powers and the quadratic seed.
This reconstructs Lemma 5.1, Appendix C, and Corollaries 5.2–5.3 of
[@BalasubramanianKasiviswanathan2026KLS], pinned at commit
`4837c33649ba2271f43c9684e9350ecbdd725f95`.

**Dependencies.** The abstract lemma uses only bounded Hilbert-space operators and
spectral calculus. Its applications take [](#prop:bk-integration-calculus) as an
explicit input: bounded graded operators $J,L$, the comparison
$J^*J\preceq g(JJ^*+LL^*)$, observations $\|J^{j-1}L\|\le c_j(\nu)$,
the block identity for $J_0\cdots J_{q-1}$, and
$C_P(\nu)\le1+\|J\|^2$. They also use the normalizations in
[](#def:bk-compatible-calculus) and [](#def:bk-uniform-appell-coefficients).
The quadratic seed alone uses [](#thm:letwin-qcts).
No BKL theorem, SZ v2 theorem, or KLS conclusion is an input.

:::{prf:theorem} Finitely observed powers
:label: thm:sol-bk-uniform-power
Let $R:X\to X$ and $L:Y\to X$ be bounded operators on real or complex Hilbert
spaces and let $a>0$. Suppose
$$R^*R\preceq g(RR^*+LL^*),\qquad g(u)=u/(1+au).$$
Let $D\ge2$ be an integer, and let finite nonnegative numbers
$\gamma_2,\ldots,\gamma_D$ satisfy $\|R^{j-1}L\|\le\gamma_j$
for $2\le j\le D$. For every $B>0$ satisfying
$aB^{D+1}>\gamma_D^2$, and every integer $k\ge0$,
$$\|R^k\|^2\le B^k\left(1+\sum_{j=1}^{D-2}
\frac{j\gamma_{j+1}^2}{B^{j+1}}\right).$$
This is [](#lem:bk-uniform-power-bound).
:::

:::{prf:proof}
Complexification preserves the operator inequality and all norms, so work over
complex Hilbert spaces. For every bounded nonnegative operator $H$ and unit
vector $v$, its scalar spectral measure and concavity of $g$ give
$$\langle v,g(H)v\rangle\le g(\langle v,Hv\rangle).$$

We first show $r(R)^2\le(\gamma_D^2/a)^{1/(D+1)}$. If $r(R)=0$ there is
nothing to show. Otherwise take $\lambda\in\sigma(R^*)$ with
$|\lambda|=r(R)>0$. There exist unit vectors $v_h$ with
$(R^*-\lambda)v_h\to0$. Here is a direct verification: the points
$z_h=(1+h^{-1})\lambda$ lie in the resolvent set; the Neumann-series test at
$\lambda$ gives $\|(R^*-z_h)^{-1}\|\ge|z_h-\lambda|^{-1}$.
Choose unit vectors on which the resolvent norm is achieved within a factor
of two and normalize their resolvent images. The resulting vectors satisfy
$$\|(R^*-\lambda)v_h\|\le
2/\|(R^*-z_h)^{-1}\|+|z_h-\lambda|\longrightarrow0.$$
Put $s=|\lambda|^2$. Then $\|R^*v_h\|^2\to s$ and
$\liminf_h\|Rv_h\|^2\ge s$, the latter by
$\|Rv_h\|\ge|\langle R^*v_h,v_h\rangle|$.
Pass to a subsequence such that $\|L^*v_h\|^2\to p\ge0$, possible since
$L$ is bounded. The comparison and scalar Jensen inequality give
$$s\le g(s+p)<a^{-1},\qquad p\ge\frac{as^2}{1-as}.$$
Factoring the difference of powers shows
$((R^*)^{D-1}-\lambda^{D-1})v_h\to0$. Applying $L^*$ and the last
observation bound gives $s^{D-1}p\le\gamma_D^2$. Consequently
$$\frac{as^{D+1}}{1-as}\le\gamma_D^2,$$
which proves the asserted spectral-radius bound.

Fix a unit vector $f$ and define
$$x_m=\|(R^*)^mf\|^2,\quad b_m=\|L^*(R^*)^mf\|^2,
\quad y_m=x_m/B^m.$$
For $m\ge1$ with $x_{m-1},x_m>0$, Cauchy–Schwarz gives
$$x_m^2\le x_{m-1}\|R(R^*)^mf\|^2.$$
Applying the comparison and Jensen to $(R^*)^mf/\sqrt{x_m}$ yields
$$\frac{x_m}{x_{m-1}}\le
 g\left(\frac{x_{m+1}+b_m}{x_m}\right).$$
In particular $ax_m/x_{m-1}<1$. Since
$g^{-1}(v)=v/(1-av)\ge v+av^2$ on $[0,a^{-1})$, inversion gives
$$y_{m+1}\ge\frac{y_m^2}{y_{m-1}}+
 aB\frac{y_m^3}{y_{m-1}^2}-\frac{b_m}{B^{m+1}}.\tag{1}$$

The strict inequality for $B$ and the spectral-radius bound give
$r(R)<\sqrt B$. Choose $r(R)<\rho<\sqrt B$; the spectral-radius formula
implies $\|R^m\|\le\rho^m$ for all sufficiently large $m$.
Thus $y_m\to0$, and, since $y_0=1$, the sequence attains a positive global
maximum $Y$ at some finite index $h$.
If $h\ge D-1$, then
$$b_h\le\gamma_D^2x_{h-D+1}\le\gamma_D^2B^{h-D+1}Y.$$
Every iterate preceding the positive $x_h$ is positive. Using (1) at $h$
and $y_{h-1}\le y_h=Y$ gives
$$y_{h+1}\ge Y+(aB-\gamma_D^2/B^D)Y>Y,$$
a contradiction. Therefore $h\le D-2$.

If $h=0$, the conclusion is immediate. Otherwise put
$\Delta_j=y_j-y_{j-1}$. For $1\le j\le h$, we have
$b_j\le\gamma_{j+1}^2$ and all denominators in (1) are positive.
Dropping the nonnegative curvature term, and using
$v^2/u-2v+u=(v-u)^2/u\ge0$, gives
$$\Delta_{j+1}\ge\Delta_j-\gamma_{j+1}^2/B^{j+1}.$$
Since $\Delta_{h+1}\le0$, backwards summation and then summation over $j$
give
$$Y-1=\sum_{j=1}^h\Delta_j
\le\sum_{j=1}^h\sum_{i=j}^h\frac{\gamma_{i+1}^2}{B^{i+1}}
=\sum_{i=1}^h\frac{i\gamma_{i+1}^2}{B^{i+1}}\le Q_D(B)-1.$$
This argument allows $x_{h+1}=0$. Thus $y_k\le Q_D(B)$ for all $k$.
Taking the supremum over unit $f$ and using $\|(R^*)^k\|=\|R^k\|$
proves the claim. The zero Hilbert space causes no exception, since all its
operator norms are zero.
:::

:::{prf:theorem} The integration consequences
:label: thm:sol-bk-power-corollaries
Assume the integration-calculus input stated above. Let $\nu$ be centered,
regular and log-concave, with covariance at most $I$ and curvature at least
$aI$, $a>0$.
If $D\ge2$, $\rho\ge1$ and $c_j(\nu)\le\rho^j/(j+1)^4$ for
$2\le j\le D$, put $B=\rho^2\max\{1,a^{-1/(D+1)}\}$.
Then for every integer $q\ge1$,
$$\|J^q\|^2\le2B^q,\qquad\|J_0\cdots J_{q-1}\|^2\le2B^q,
\qquad C_P(\nu)\le1+2B.$$
Without any higher coefficient assumption,
$$\|J\|^2\le(2/a)^{1/3}.$$
These are [](#cor:bk-integration-powers) and [](#cor:bk-quadratic-seed).
:::

:::{prf:proof}
For the first assertion apply the preceding theorem with $R=J$, the
constant-field operator $L$, and $\gamma_j=\rho^j/(j+1)^4$.
Indeed $aB^{D+1}\ge\rho^{2D+2}>\gamma_D^2$, and
$$Q_D(B)-1\le\sum_{j=1}^\infty\frac{j}{(j+2)^8}
\le\sum_{j=1}^\infty(j+2)^{-7}
\le\int_2^\infty x^{-7}\,dx=\frac1{384}<1.$$
The block of $J^q$ from grade $q$ to grade zero is
$J_0\cdots J_{q-1}$, so its norm is no greater. The Poincaré conclusion
uses the stated calculus input.

For the seed, Letwin's inequality gives
$\operatorname{Var}(X^TTX)\le8\|T\|_{\mathrm{HS}}^2$ for isotropic
log-concave $X$. Since the normalized quadratic Appell polynomial is
$(X^TTX-\mathbb EX^TTX)/2$, its coefficient is at most $\sqrt2$.
If covariance is at most $I$, write the law as $AZ$ on its linear support,
where $Z$ is isotropic and $\|A\|\le1$. Replace $T$ by $A^TTA$;
its Hilbert–Schmidt norm is no larger, proving $c_2(\nu)\le\sqrt2$.
(The point mass case is zero.) Use $D=2$, $\gamma_2=\sqrt2$. The sum in
$Q_2$ is empty, so for every $B>(2/a)^{1/3}$ the theorem gives
$\|J\|^2\le B$. Taking the infimum over such $B$ proves the seed.
:::

**Fences respected.** No `bounded_by` fence is proposed for the abstract
operator statement. The integration assertions keep positive curvature and
regularity, and their coefficient hypotheses are restricted to the stated
finite degrees. They do not assert that separate one-step bounds retain a
uniform prefactor under multiplication. The quadratic estimate is precisely
Letwin's constant-eight variance normalization, not a sharper third-moment
or moment-map claim.

:::{prf:remark} Scope of the inputs
The abstract operator assertion is proved directly here. The two integration
consequences use the separately proved calculus input above; this document
does not replace that input's proof or independent review.
:::
