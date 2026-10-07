---
title: "BK: uniform Appell coefficient induction"
ledger-node: thm:bk-appell-bound
numbering:
  enumerator: "156.%s"
---

*Part of the Balasubramanian–Kasiviswanathan proof, Chapter [](#sec:bk-proof); the reading order is on the [full proofs](#sec:proofs-bk) page.*

**Overview.** A convolution estimate controls the lowering drift. For bounded
initial degrees the quadratic integration seed and a small localization time
close the induction. In larger degrees, finitely many lower coefficients feed
the uniform power lemma at a rate strictly smaller than the target radius;
this gain absorbs the coordinate change and weight ratio. Every estimate below
is analytic. This reconstructs Theorem 8.1 and Appendix E of
[@BalasubramanianKasiviswanathan2026KLS], pinned at commit
`4837c33649ba2271f43c9684e9350ecbdd725f95`.

**Dependencies and explicit inputs.** We use the coefficients and operators of
[](#def:bk-uniform-appell-coefficients) and [](#def:bk-compatible-calculus).
The graded calculus [](#prop:bk-integration-calculus) is an explicit input:
for every centered regular law of covariance at most $I$ and curvature at
least $aI$, there are bounded operators $J,L$ with
$$J^*J\preceq g_a(JJ^*+LL^*),\quad g_a(u)=u/(1+au),\qquad
\|J^{j-1}L\|\le c_j(\nu),$$
and $J_0\cdots J_{q-1}$ is a block of $J^q$.
We use [](#lem:bk-uniform-power-bound) and [](#cor:bk-quadratic-seed).
The reverse-transfer input [](#prop:bk-reverse-transfer) is used in the
following exact form: for integers $d\ge2$, $1\le q<d$, $0<\eta\le1$,
$\delta=\eta^2/d^2$, and finite constants $C_k\ge c_k^*$ for $1\le k<d$,
if
$$\|J_0^\nu\cdots J_{q-1}^\nu\|\le M_q<\infty$$
for every centered regular law with covariance at most $I$ and curvature at
least $\delta I$, then
$$c_d^*\le e^{3\eta}\left((1+\eta)^{q/2}M_qC_{d-q}
 +\frac{\eta}{d^2}\Sigma_d\right),\qquad
\Sigma_d=\sum_{k=2}^{d-1}(d-k+1)C_kC_{d-k+1}.\tag{1}$$
In particular this input includes passage to all log-concave laws in $c_d^*$;
no limiting regularity claim is silently added here.
No BKL, SZ v2, KLS conclusion, or already uniform exponential Appell bound
is used.

:::{prf:theorem} Uniform coefficient induction
:label: thm:sol-bk-appell-growth
Under the explicit calculus and reverse-transfer inputs above, the quadratic
seed, and the uniform power lemma, let $c_d^*$ be the supremum of the
normalized degree-$d$ Appell coefficient over all dimensions and centered
log-concave laws of covariance at most the identity. Then with $R=10^8$,
$$c_d^*\le\beta_d:=R^d(d+1)^{-4}\qquad(d\ge1).$$
This gives [](#thm:bk-appell-bound) using the stated inputs.
:::

:::{prf:proof}
Put $w(j)=(j+1)^{-4}$ for $j\ge0$, $C_w=4$, and $D_0=10^7$.
We first verify the convolution estimate
$$\sum_{k=1}^s\frac{w(k)w(s-k)}{w(s)}\le C_w\qquad(s\ge1).\tag{2}$$
The endpoint $k=s$ contributes one. For $1\le k\le s/2$,
$(s+1)/(s-k+1)\le2$, so that term is at most $16/(k+1)^4$.
Pairing the interior terms about the midpoint (allowing double counting
there) bounds the left side by
$$1+32\sum_{j=2}^\infty j^{-4}
\le1+32\left(\frac1{16}+\frac1{81}+\int_3^\infty x^{-4}\,dx\right)
=\frac{307}{81}<4.$$
This also covers $s=1$, when there are no interior terms.

The first coefficient is the standard deviation of a linear functional,
so $c_1^*\le1<R/16=\beta_1$. Fix $d\ge2$ and suppose inductively
$c_k^*\le\beta_k$ for every $1\le k<d$. In (1) set $C_k=\beta_k$.
Every degree appearing in $\Sigma_d$ is less than $d$. Since
$d-k+1\le d$, (2) at $s=d+1$ gives
$$\Sigma_d\le dC_wR^{d+1}w(d+1).\tag{3}$$
For $d=2$ the sum is empty and this bound remains true.

**Initial degrees.** Suppose $2\le d\le D_0$. Set
$$q=1,\qquad\eta=\frac{d}{100R},\qquad
\delta=\frac{\eta^2}{d^2}=(100R)^{-2}.$$
Then $0<\eta\le1/1000<1/100$. For every law in the curvature class
required by (1), the quadratic seed supplies
$$\|J_0\|\le\|J\|\le M_1:=(2/\delta)^{1/6}
=[2(100R)^2]^{1/6}\le10\sqrt R.$$
The last inequality follows by sixth powers:
$20000R^2\le10^6R^3$. Also
$$\frac{\beta_{d-1}}{\beta_d}=
\frac1R\left(\frac{d+1}{d}\right)^4<\frac{16}{R}.$$
By (3) and monotonicity of $w$,
$$\frac{\eta\Sigma_d}{d^2\beta_d}
\le\frac{\eta C_wR}{d}=\frac1{25}.$$
Divide (1) by $\beta_d$. The elementary inequalities
$e^x\le(1-x)^{-1}$ for $0\le x<1$ and
$\sqrt{1+\eta}\le1+\eta$ imply
$e^{3\eta}<21/20$ and $\sqrt{1+\eta}<21/20$.
As $160/\sqrt R=2/125$, it follows that
$$\frac{c_d^*}{\beta_d}
\le e^{3\eta}\left(\sqrt{1+\eta}\frac{160}{\sqrt R}+\frac1{25}\right)
<\frac{21}{20}\left(\frac{21}{20}\frac2{125}+\frac1{25}\right)
=\frac{1491}{25000}<1.$$
This closes every initial degree, using only already bounded lower degrees.

**Degrees beyond the cutoff.** Suppose $d>D_0$. Choose
$$q=\lfloor d/2\rfloor,\quad D=\lfloor\sqrt d\rfloor,\quad
\eta=\frac{d^{-1/2}}{100C_wR},\quad
\delta=\frac{d^{-3}}{(100C_wR)^2},\quad
B=R^2e^{-1/(D+1)}.$$
These satisfy $1\le q<d$, $2\le D<d$, $0<\eta<1/100$ and
$\delta=\eta^2/d^2$. For every regular law in the curvature class of (1),
the calculus input and induction give the observation bounds
$$\|J^{j-1}L\|\le c_j(\nu)\le c_j^*\le
\gamma_j:=\frac{R^j}{(j+1)^4}\qquad(2\le j\le D).$$
The strict hypothesis of the power lemma is satisfied, because
$$\delta B^{D+1}
=\frac{R^{2D}}{e(100C_w)^2d^3}
>\frac{R^{2D}}{(D+1)^8}=\gamma_D^2.\tag{4}$$
Indeed $D+1>\sqrt d$ implies $(D+1)^8>d^4$, while
$e(100C_w)^2<3\cdot400^2=480000<D_0<d$.
The elementary bound $e<3$ follows, for example, from the factorial series
and $k!\ge2^{k-1}$ for $k\ge1$, with a strict inequality for $k\ge3$.

The same power lemma, keeping its common prefactor, gives
$$\begin{aligned}
Q_D(B)&=1+\sum_{j=1}^{D-2}\frac{je^{(j+1)/(D+1)}}{(j+2)^8}\\
&\le1+e\sum_{j=1}^\infty(j+2)^{-7}
\le1+\frac e{384}<2.
\end{aligned}$$
Consequently one uniform bound valid for the entire curvature class is
$$\|J_0\cdots J_{q-1}\|\le\|J^q\|
\le M_q:=\sqrt2R^q\exp\left(-\frac q{2(D+1)}\right).\tag{5}$$
Thus (1) applies without any dependence of $M_q$ on dimension or law.

The principal term in (1), divided by $\beta_d$, equals
$$\sqrt2\frac{w(d-q)}{w(d)}
\exp\left(3\eta+\frac q2\log(1+\eta)-\frac q{2(D+1)}\right).$$
Since $d-q\ge d/2$, the weight ratio is at most $16$.
Using $\log(1+\eta)\le\eta$ and $\sqrt2<2$, the term is at most
$$32\exp\left(3\eta+q\left[\frac\eta2-\frac1{2(D+1)}\right]\right).$$
Now $D+1\le2\sqrt d$ and hence
$\eta(D+1)\le2/(100C_wR)<1/2$; the bracket is at most
$-1/[4(D+1)]$. Since $q\ge d/3$,
$$\text{principal ratio}\le
32\exp\left(\frac3{100}-\frac{\sqrt d}{24}\right)<\frac14.$$
For the last strict estimate, $d>D_0>10^6$ gives $\sqrt d>1000$;
the exponent is less than $-7$, and the series for $e$ gives $e>2$,
so $32e^{-7}<1/4$.

Finally (3) bounds the drift ratio, including its exponential factor, by
$$\frac{e^{3\eta}\eta\Sigma_d}{d^2\beta_d}
\le\frac{e^{3\eta}\eta C_wR}{d}
=\frac{e^{3\eta}}{100d^{3/2}}<\frac1{50}.$$
Here $e^{3\eta}<(1-3/100)^{-1}<2$ and $d\ge1$.
The two ratios sum to less than one, proving $c_d^*<\beta_d$.
The induction holds for every integer $d$, with the single radius $R$ fixed
before choosing dimension, law, or degree.
:::

**Fences respected.** No separate `bounded_by` node is proposed. The
quantifiers enforce one radius for all degrees, dimensions and laws; the
argument never starts from merely degreewise finite constants. Curvature is
positive at each invocation of the power lemma, its strict last-observation
condition is checked in (4), and only degrees below $d$ feed the induction.
Degenerate-support laws are included solely through the explicit scope of
the reverse-transfer input and the elementary base case. The proof does not
use a KLS-equivalent conclusion as its initialization.

:::{prf:remark} Dependencies and scope
The scalar induction uses the separately proved integration calculus and
reverse-transfer estimates. Their analytic construction, regularity,
stopping, and approximation steps belong to those proofs. This dossier
supplies the degree induction from those inputs; it does not replace their
proofs or independent reviews.
:::
