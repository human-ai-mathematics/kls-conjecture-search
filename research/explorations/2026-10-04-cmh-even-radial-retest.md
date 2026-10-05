---
artifacts:
  - research/runs/2026-10-04-cmh-even-radial-symbolic.jsonl
---

# Even radial CMH retest: admissible boundary family, negative low-degree variation

## Question examined

For `ap:c-solenoidal-perturbation`, construct the family

$$\rho_\beta(x,y)=\Gamma(\beta)^{-1}(x+y)^{\beta-2}e^{-x-y}\mathbf1_{x,y>0},
\qquad \beta=2+\varepsilon^2,$$

and calculate the optimized full polynomial CMH quotients of total degree at most
$d=1,2,3,4$. Starting lens: construct. After the admissibility gate, the mission
became boundary calibration: this family is not the source-linear family in
`conj:cmh-second-variation`, and no regular-kernel limit has been established.
This completes the explicit next test proposed in
[the earlier gate analysis](2026-10-04-wave-a-cmh-variation.md), without changing
any claim status.

The canonical statement, verbatim, is:

> Take the product moment potential $\psi_0(s,t)=\phi(s)+t^2/2$ with $\phi$ the one-sided exponential moment potential, and perturb it by $\psi_\eps=\psi_0+\eps\,a(s)b(t)$. Call the perturbation admissible if, for all sufficiently small $\abs\eps$, $\psi_\eps$ is smooth and strictly convex and its moment measure $\mu_\eps$ is log-concave and belongs to the regular moment-map class on which [](#def:cmh) is set. Then, for every admissible perturbation,
>
> $$\limsup_{\eps\to0}\frac{\CMH(\mu_\eps)+\CMH(\mu_{-\eps})-2\CMH(\mu_0)}{\eps^2}\le0,$$
>
> where $\CMH(\mu_0)=4$ by [](#cor:cmh-product-saturation).

Its negation requires existence of $a,b$ and $\varepsilon_0>0$ satisfying **all**
those admissibility hypotheses for every $|\varepsilon|<\varepsilon_0$, with the
displayed limsup strictly positive. The present path does not meet its specified
base or source-linear ansatz. It tests the boundary version of `def:cmh` only.

## What we learned

### Established analytically, uncertified: the family gate

Write $S=x+y$ and $T=(x-y)/(x+y)$. The Jacobian is $S/2$; hence
$S\sim\Gamma(\beta,1)$ and $T\sim\mathrm{Unif}[-1,1]$ independently.
This proves mass one and all polynomial moments for every $\beta>0$.
In original coordinates the mean is $(\beta/2,\beta/2)$, and

$$\Sigma_{xy}=\frac{\beta}{12}
\begin{pmatrix}\beta+4&2-\beta\\2-\beta&\beta+4\end{pmatrix}.$$

Its eigenvalues are $\beta/2$ and $\beta(\beta+1)/6$, both positive.
Centering by the displayed mean produces the centered law throughout this note.
The target potential satisfies

$$D^2V_\beta=\frac{\beta-2}{(x+y)^2}
\begin{pmatrix}1&1\\1&1\end{pmatrix}.$$

Thus log-concavity is equivalent to $\beta\ge2$, and the even path is admissible
as a full-dimensional log-concave **boundary law for both signs of epsilon**.
For nonzero epsilon its mixed log-density derivative is nonzero, so it is not a
product in these coordinates. Its unbounded support is outside the compact-target
hypothesis of `thm:regular-moment-map-compact-target`.

For $0<\delta<R$, restriction to $[\delta,R]^2$, normalization and centering
supply an explicit regular family for both signs. The density is positive and
smooth on a neighborhood of that body, where $x+y>0$. Extend its potential
smoothly to all space by a cutoff equal to one near the body, then exponentiate;
this gives the positive global smooth density extension required by
`thm:regular-moment-map-compact-target`. Log-concavity of the restricted measure
uses the convexity on the body, not convexity of the arbitrary extension.
Its covariance is strictly positive because it has positive density on an open
set. The theorem therefore supplies its canonical smooth strictly convex moment
potential, gradient diffeomorphism, Stein identity and weak zero flux.
At epsilon zero it is a product of truncated exponentials, not the exact endpoint.

Dominated convergence as $\delta\downarrow0$, $R\uparrow\infty$ gives all
moments of the boundary family, uniformly for beta in a fixed compact interval
in $[2,\infty)$. It does not identify the limiting canonical kernels or CMH.

### Established reduction: full matrices with moving covariance and kernel

Use the fixed linear coordinates $(s,v)=(x+y,x-y)$, and put $t=v/s$.
The centered coordinate is $(s-\beta,v)$, and the cone proposition
`prop:cone-moment-map`, with interval base $[-1,1]$, gives

$$\Sigma=\operatorname{diag}\left(\beta,\frac{\beta(\beta+1)}3\right),\qquad
H=\begin{pmatrix}s&v\\v&\frac{v^2}{s}+\frac\beta2\left(s-\frac{v^2}s\right)\end{pmatrix}.$$

Equivalently, in the original orthant coordinates,

$$H=\operatorname{diag}(x,y)+\frac{(\beta-2)xy}{2(x+y)}
\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.$$

This is the canonical kernel supplied by the certified cone construction, not
an alternative Stein kernel. Its normal flux vanishes on both orthant faces.
Polynomial tests have finite energy and square-integrable generator; the Stein
integration by parts extends to them by radial cutoff, with exponentially
vanishing tails. At the tip the density-volume factor is $s^{\beta-1}ds\,dt$,
$H=O(s)$, and each positive-degree polynomial is $O(s)$ or better; cutoff errors
there vanish for $\beta\ge2$. Constants may first be removed. The natural closed
Stein form therefore admits these polynomial tests in its operator domain.

Modulo constants, use the **entire** total-degree space with basis
$g_{kj}=s^kt^j=s^{k-j}v^j$, $1\le k\le d$, $0\le j\le k$.
No radial or parity restriction is imposed in the maximization. Centering and
whitening preserve this entire polynomial space. Consequently this fixed
ambient-coordinate representation does not freeze a moving affine test space.
For each basis element,

$$u_{kj}=H\nabla g_{kj}
=s^k\binom{kt^j}{kt^{j+1}+\frac{\beta j}{2}(1-t^2)t^{j-1}},$$

$$L g_{kj}=-ks^kt^j+s^{k-1}\left[k(k-1+\beta)t^j+
\frac{\beta j}{2}\big((j-1)t^{j-2}-(j+1)t^j\big)\right].$$

Terms with zero prefactor are zero, even if their formal exponent is negative.
The two exact Gram matrices are

$$N_{ab}=\mathbb E\left[\frac{u_{a,1}u_{b,1}}\beta+
\frac{3u_{a,2}u_{b,2}}{\beta(\beta+1)}\right],\qquad
D_{ab}=\mathbb E[(Lg_a)(Lg_b)],$$

using the identity

$$\mathbb E[S^mT^j]=(\beta)_m
\begin{cases}(j+1)^{-1},&j\text{ even},\\0,&j\text{ odd}.\end{cases}$$

All entries are rational functions of beta, analytic near two, and $D$ is
positive definite modulo constants. The full optimized quotient is
$Q_d(\beta)=\lambda_{\max}(N(\beta),D(\beta))$.

### Observed exact symbolic calculation, with reproducible identities

The seeded run uses these formulas to store **exact rational** $N(2),D(2)$ and
their beta derivatives, parity characteristic polynomials, exact radical null
vectors and derivative contractions. Floating eigenvalues are crosschecks only.
These algebraic results have not undergone independent proof review and request
no proved status. They are reproducible without numerical optimization.

The endpoint maximum has multiplicity two at each degree. The even and odd
branches under $x\leftrightarrow y$ have the following exact derivatives:

| $d$ | $Q_d(2)$ | even branch beta derivative | odd branch beta derivative |
|---|---|---|---|
| 1 | $2$ | $-1/2$ | $-1/2$ |
| 2 | $3$ | $-137/120$ | $-133/120$ |
| 3 | $2+\sqrt2$ | $-47/56-129\sqrt2/280$ | $-227/280-403\sqrt2/840$ |
| 4 | $(5+\sqrt5)/2$ | $-383/336-131\sqrt5/504$ | $-559/504-1373\sqrt5/5040$ |

For cold verification, the endpoint characteristic factors, with nonzero scalar
factors omitted, are:

| $d$ | even block | odd block |
|---|---|---|
| 1 | $q-2$ | $q-2$ |
| 2 | $(q-3)(q-1)^2$ | $(q-3)(q-1)$ |
| 3 | $(q-2)(q^2-4q+2)(9q^2-19q+8)$ | $(q-2)(9q-10)(q^2-4q+2)$ |
| 4 | $(q-1)(q^2-5q+5)(q^2-3q+1)(72q^3-242q^2+232q-57)$ | $(q^2-5q+5)(q^2-3q+1)(36q^2-85q+41)$ |

These factors verify maximality and simplicity inside each parity block. For
example, the extra quadratic at degree three has no root above two, and the
extra cubic at degree four has positive coefficients after $q=3+z$, so no root
at or above three. The other comparisons are immediate from quadratic roots.
Endpoint optimizer spaces are precisely
$\operatorname{span}\{f_d(x)+f_d(y),f_d(x)-f_d(y)\}$ modulo constants, where

$$\begin{aligned}
f_1(z)&=z,\\
f_2(z)&=z^2,\\
f_3(z)&=z^3+\left(-9+\frac{9\sqrt2}{2}\right)z^2+(36-18\sqrt2)z,\\
f_4(z)&=z^4+\left(-\frac{40}3+\frac{8\sqrt5}3\right)z^3+(60-12\sqrt5)z^2.
\end{aligned}$$

Substitution into the displayed exact matrices verifies both the eigenvector
identity and the derivative formula

$$q'_\pm(2)=\frac{a_\pm^T(N'(2)-Q_d(2)D'(2))a_\pm}
{a_\pm^TD(2)a_\pm}.$$

This includes denominator variation. The run additionally reports the separate
$N'$ and $D'$ contractions normalized by $D(2)$, so their cancellation is
inspectable. Optimizer derivatives cancel by stationarity; they are not omitted
by an assumption that the optimizing function stays fixed.

Since the top eigenspace is double, the right derivative is the larger branch
derivative, not an arbitrary vector's derivative. It is the odd branch for
$d=2,3,4$: odd minus even equals respectively $1/30$,
$(3-2\sqrt2)/105$, and $(155-63\sqrt5)/5040$, all positive.
For degree one both derivatives coincide. Every displayed derivative is strictly
negative. Thus

$$\left.\frac{d^2}{d\varepsilon^2}Q_d(2+\varepsilon^2)\right|_{\varepsilon=0}
=2Q'_{d,+}(2)<0\qquad(d=1,2,3,4).$$

The deficits $4-Q_d(2)$ are respectively $2$, $1$, $2-\sqrt2$, and
$(3-\sqrt5)/2$. Finite-dimensional analytic perturbation in each parity block
provides a local $O((\beta-2)^2)$ remainder. In particular each tested degree
moves down for sufficiently small positive $\beta-2$. No quantitative common
radius in degree, finite-parameter global bound, or full CMH derivative is asserted.

### Established reduction: both Hodge channels are accounted for

At beta two, $H=\operatorname{diag}(x,y)$ and $\Sigma=I$ in orthant coordinates.
For every endpoint optimizer $g=f_d(x)\pm f_d(y)$,

$$H\nabla g=\nabla\left(\int_0^x r f'_d(r)\,dr
\ \pm\int_0^y r f'_d(r)\,dr\right).$$

Hence its solenoidal field is zero: the entire endpoint numerator is in the
covariance-gradient channel. For an analytic optimizing branch $g_\beta$, the
explicit kernel, covariance and polynomial coefficients vary by $O(\beta-2)$
in the relevant weighted $L^2$ norm, with uniform polynomial moment bounds.
Fix the displayed endpoint potential $\psi_0$. Orthogonal projection onto the
closed covariance-gradient space gives

$$\|w_\beta\|_{L^2(\mu_\beta;\Sigma_\beta^{-1})}^2
\le\|H_\beta\nabla g_\beta-\Sigma_\beta\nabla\psi_0\|^2
=O((\beta-2)^2).$$

Polynomial gradients used here belong to that space by cutoff. This argument
needs no differentiability of a covariance Poisson inverse. Consequently the
solenoidal numerator has zero first beta derivative, and the affine numerator
has precisely the full $N'$ derivative in the fixed normalization; after
normalizing $D(\beta)=1$, their derivatives are respectively $0$ and $q'_\pm(2)$.
In epsilon coordinates the solenoidal energy is $O(\varepsilon^4)$.
No exact formula for the two separate channels away from the endpoint is claimed.

## What resists

This is a **boundary calibration with negative variation**, not a refutation,
not a proof of `conj:cmh-second-variation`, and not a bound on the full CMH
supremum. It uses no `cand:cmh-exponential-galerkin-rate` premise. It respects
product saturation, the full Hodge numerator, canonical kernel uniqueness,
and the distinction between the sharp linear gate and CMH(4). The target has
no explicit ledger `bounded_by` entries; none of those substantive fences is
bypassed. The degree-one result agrees with the certified cone axis gate.

Transfer to the regular restrictions remains unproved. A sufficient finite-test
interface would identify their kernels $H_{\delta,R}$ with the cone kernel in
weighted integrals strongly enough that, after centering, for every polynomial
in this finite-dimensional space,

$$\mathbb E\langle H_{\delta,R}\nabla g,
\Sigma_{\delta,R}^{-1}H_{\delta,R}\nabla g\rangle\longrightarrow N(g,g),
\qquad
\mathbb E(L_{\delta,R}g)^2\longrightarrow D(g,g).$$

Uniform versions in beta, with control of beta derivatives, are additionally
needed to transfer this variation. Weak moment convergence alone gives neither
estimate. `prop:cmh-approximation-closure` concerns scalar Poincare passage under
an independent CMH premise and does not supply them. Even a positive coefficient
would require a controlled remainder overcoming the finite-degree deficit and a
valid regular transfer before it could yield a CMH(4) counterexample.

## Proposed next step

Do not repeat this degree-one through degree-four boundary test. Proposed exact
portfolio edit: retain `ap:c-solenoidal-perturbation` as active and replace its
`next` by: “Resolve admissibility for a nontrivial source-linear perturbation in
`conj:cmh-second-variation`; the even radial boundary family has strictly negative
optimized degree-one through degree-four variation. A separate regular-kernel
convergence estimate is required before any cone calculation transfers to the
compact-target class.” No status, dependency or manuscript delta is requested.

Handoff: this checkpoint and the seeded symbolic script/output. The exact matrix
and branch identities are ready for independent examination if a future argument
needs them as premises. No dossier or new candidate is proposed, since this is
calibration rather than a target-settling claim. The family gate, quotient
reduction and Hodge-order argument are written analytical arguments but remain
uncertified; the table is labeled exact symbolic evidence.
