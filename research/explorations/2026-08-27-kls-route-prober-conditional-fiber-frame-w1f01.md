---
type: exploration
date: "2026-08-27"
outcome: proposed
nodes:
  - lem:conditional-fiber-form
  - thm:cmh-1d
---
# KLS route probe: conditional fiber frames

Date: 2026-08-27

Role: `kls-route-prober`

Run id: `w1f01`

Candidate route: `conditional-fiber-frame`

Write scope: this append-only exploration only

No numerical evidence is used.  No ledger, manuscript, route-control, bibliography, dossier,
review, or knowledge-registry file is changed.

## Decisive outcome

**Still blocked.**  The proposal survives every named fence and is not a relabeling of any live
route, but its most natural simplex implementation does not survive.  The $A_{m-1}$ root frame
has gap $O(m^{-2})$, witnessed analytically by a vertex cap.  This kills the root-frame proposal,
not the existential route: no argument shows that every admissible tight frame degenerates, and
no argument constructs a different test-function-independent frame with a universal gap.

The measure-theoretic definition, closed reversible form, exact factor-$4$ KLS sufficiency
calculation, Gaussian/product calibrations, root-frame refuter, and uniform-simplex polynomial
and all-frame dual reductions are all analytic.  The unsupported step is now exactly the
optimization over all frames.

There is a prover-ready structural dossier below, but not a prover-ready proof of the universal
frame-gap target.  In particular, this report does not claim KLS, an equivalent reformulation of
KLS, or a counterexample.

## Provenance and the candidate gate, quoted verbatim

The proposal came from a read-only `kls-route-scout` handoff.  There is no persisted scout file.
The orchestrator supplied the following exact candidate:

> For every full-dimensional isotropic log-concave $\mu$, find an even
> test-function-independent probability $\rho_\mu$ on $S^{n-1}$ with
> $n\int\theta\theta^T\,d\rho=I$ such that
> $\operatorname{Var}_\mu(f)\le C\mathcal D_{\mu,\rho}(f)$, where $\mathcal D$ is the
> variance-normalized conditional-line variance form.  One-dimensional log-concave Poincar\'e
> gives $\mathcal D\le4\int|\nabla f|^2$, so this sufficient, not equivalent, target implies
> $C_P\le4C$.

The associated simplex falsification target in the same handoff was

> On the isotropic uniform simplex in affine dimension $d=m-1$, analyze the
> $A_{m-1}$ root frame and
> $$
> \Lambda_{m,k}=\sup_{\rho:\ d\int\theta\theta^T\,d\rho=I}
> \inf_{0\ne f\in\mathcal P_{\le k},\ \mathbb Ef=0}
> \frac{\mathcal D_{\mu,\rho}(f)}{\operatorname{Var}_\mu(f)}.
> $$
> An exact dual certificate with $\Lambda_{m,k}\to0$ at fixed $k$ kills the route.

During the probe, a parallel read-only literature-scout handoff (also with no persisted source
file) identified the root form with the negative-exponent simplex exchange model and supplied the
vertex-cap attack.  Equations (37)--(41) reproduce the complete analytic derivation rather than
treating the handoff as certification.

The order of quantifiers is load-bearing:

$$
 \forall\mu\quad\exists\rho_\mu\quad\forall f.
 \tag{G}
$$

Allowing $\rho$ to depend on $f$ would define a different and much weaker target.

## Term-by-term decomposition

Let the ambient dimension be $d$ in this report, reserving $m$ for the number of simplex
coordinates.

| demanded object | exact content | disposition |
|---|---|---|
| full-dimensional log-concave $\mu$ | a probability density $e^{-V}$ with $V$ proper convex and affine hull $\mathbb R^d$ | gives canonical Radon disintegrations and nondegenerate fibers almost everywhere |
| isotropy | $\mathbb EX=0$, $\operatorname{Cov}X=I_d$ | calibrates every linear test exactly |
| even $\rho$ | $\rho(B)=\rho(-B)$ | no loss because the $\theta$ and $-\theta$ forms coincide |
| probability and tight-frame identity | $d\int\theta\theta^T\,d\rho(\theta)=I_d$ | preserves the complete Euclidean gradient energy after the one-dimensional estimate |
| test-function independence | the same $\rho_\mu$ must work for the complete form domain | prevents optimizing a direction separately for each bad function |
| full conditional fibers | condition on the entire offset $P_{\theta^\perp}X=z$, not only on the marginal $\langle X,\theta\rangle$ | retains offset-dependent geometry and distinguishes the route from projection tests |
| variance normalization | divide the conditional variance of $f$ by the conditional variance of the line coordinate | removes the physical length/variance scale of each chord |
| global target | a dimension-free lower spectral bound for the averaged nonlocal form | the sole unresolved mathematical step |
| local-to-Euclidean bridge | the sharp one-dimensional bound $C_P(\nu)\le4\operatorname{Var}_\nu(T)$ | proves only $\mathcal D\le4$ times gradient energy; it does not prove the target lower bound |

There is no stochastic source, damping, stopping boundary, localized perimeter, or approximation
error term in this route.  The relevant analytic boundaries are instead null fibers, degenerate
fiber variances, the maximal form domain, and the possible unbounded jump rate near short fibers.

## 1. Canonical Radon disintegration along affine lines

Write

$$
 d\mu(x)=r(x)\,dx,\qquad r=e^{-V},
$$

using the standard pointwise Borel representative with $V$ lower-semicontinuous convex and
allowed to equal $+\infty$ off the convex support.  (Changing this representative on a
Lebesgue-null set changes the fiber formulas only on a null set for each direction, by Tonelli,
so the integrated form is representative-independent.)  Fix
$\theta\in S^{d-1}$ and let $\pi_\theta=P_{\theta^\perp}$.  For
$z\in\theta^\perp$, set

$$
 Z_\theta(z)=\int_{\mathbb R}r(z+t\theta)\,dt.
 \tag{1}
$$

Here and below $dz$ means $\mathcal H^{d-1}\!\restriction\theta^\perp$.  Fubini gives the
projected probability

$$
 d\bar\mu_\theta(z)=Z_\theta(z)\,dz
 \tag{2}
$$

Define the good-fiber set

$$
 \mathsf G_\theta
 =\left\{z:0<Z_\theta(z)<\infty,
 \ \int_{\mathbb R}t^2r(z+t\theta)\,dt<\infty\right\}.
$$

On $\mathsf G_\theta$, the canonical conditional law relative to the fixed density
representative is

$$
 d\mu_{\theta,z}(t)
 =\frac{r(z+t\theta)}{Z_\theta(z)}\,dt,
 \qquad
 \mu(dx)=\int_{\theta^\perp}(z+\cdot\,\theta)_\#\mu_{\theta,z}
 \,d\bar\mu_\theta(z).
 \tag{3}
$$

Each good conditional law is one-dimensional and log-concave.  Define there

$$
 m_\theta(z)=\int t\,d\mu_{\theta,z}(t),
 \qquad
 \sigma_\theta^2(z)=\int(t-m_\theta(z))^2\,d\mu_{\theta,z}(t).
 \tag{4}
$$

On the complement of $\mathsf G_\theta$ use the fixed Borel fallback $\delta_0$, set
$m_\theta=\sigma_\theta^2=0$, and set all normalized energies below to zero.  Fubini, isotropy,
and $\int Z_\theta dz=1$ show that the complement is $\bar\mu_\theta$-null.

### Null and degenerate fibers

- On a bad fiber the fixed fallback above removes any version choice, and every normalized
  quotient is zero.
- If $\sigma_\theta^2(z)=0$, the conditional law is a point mass and the conditional variance of
  every $f$ is also zero.  Define $0/0=0$ there.
- For a full-dimensional log-concave density, almost every projected point lies under a chord of
  positive length.  Consequently $0<\sigma_\theta^2(z)<\infty$ for
  $\bar\mu_\theta$-almost every $z$.

### Measurable versions

The incidence bundle

$$
 \mathcal I_d=\{(\theta,z):\theta\in S^{d-1},\ z\in\theta^\perp\}
$$

is Borel.  On local sphere charts choose a Borel orthonormal frame of $\theta^\perp$; pushing
Lebesgue measure through that frame defines a Borel kernel
$\theta\mapsto\mathcal H^{d-1}\!\restriction\theta^\perp$.  Tonelli applied to this kernel and
the Borel map $(\theta,z,t)\mapsto z+t\theta$ makes (1), the good-fiber indicator, and the
truncated moment numerators jointly Borel.  Division on the good set and the fixed fallback
then give jointly Borel versions of $m_\theta(z)$, $\sigma_\theta^2(z)$, and, for a fixed Borel
representative of $f$, $\int f(z+t\theta)d\mu_{\theta,z}(t)$.  Pulling these fields back by
$(\theta,x)\mapsto(\theta,P_{\theta^\perp}x)$ gives the line-constant versions used below.
Tonelli also shows that changing the Borel representative of $f$ does not change the integrated
energy.  This supplies the measurable field needed for the $\rho$-integral without choosing
unrelated regular conditional probabilities direction by direction.

## 2. The maximal conditional-fiber form

For real $f\in L^2(\mu)$ first define the extended nonnegative single-direction energy

$$
 \mathcal q_{\mu,\theta}[f]
 =\int_{\theta^\perp}
 \frac{\operatorname{Var}_{\mu_{\theta,z}}
   (f(z+T\theta))}
 {\sigma_\theta^2(z)}\,d\bar\mu_\theta(z),
 \tag{5}
$$

with values in $[0,+\infty]$ and with the conventions above.  For an even admissible frame
$\rho$, put

$$
 \boxed{
 \mathcal D_{\mu,\rho}[f]
 =d\int_{S^{d-1}}\mathcal q_{\mu,\theta}[f]\,d\rho(\theta).}
 \tag{6}
$$

Its maximal form domain is

$$
 \operatorname{Dom}(\mathcal D_{\mu,\rho})
 =\{f\in L^2(\mu):\mathcal D_{\mu,\rho}[f]<\infty\}.
 \tag{7}
$$

For $f,g$ in this domain, polarization defines the bilinear form
$\mathcal D_{\mu,\rho}(f,g)$.  Weighted Cauchy--Schwarz makes the integrated conditional
covariance absolutely integrable, and the pair-jump representation is

$$
 \begin{aligned}
 \mathcal D_{\mu,\rho}(f,g)
 =\frac d2\int_{S^{d-1}}\int_{\theta^\perp}
 &\frac{1}{\sigma_\theta^2(z)}
 \iint
 \bigl(f(z+s\theta)-f(z+t\theta)\bigr)\\
 &\times\bigl(g(z+s\theta)-g(z+t\theta)\bigr)
 \,d\mu_{\theta,z}(s)d\mu_{\theta,z}(t)
 \,d\bar\mu_\theta(z)d\rho(\theta).
 \end{aligned}
 \tag{8}
$$

This makes reversibility and the nonlocal nature of the route explicit.

### Closedness and density

Let $P_\theta$ be conditional expectation onto
$\sigma(P_{\theta^\perp}X)$ and let

$$
 w_\theta(x)=\sigma_\theta^{-2}(P_{\theta^\perp}x).
$$

Here and below $w_\theta=0$ on null or zero-variance fibers.

Multiplication by $w_\theta$ commutes with $P_\theta$.  Therefore

$$
 \mathcal q_{\mu,\theta}[f]
 =\|w_\theta^{1/2}(I-P_\theta)f\|_{L^2(\mu)}^2.
 \tag{9}
$$

The multiplication operator is closed and $I-P_\theta$ is bounded and commuting, so
$w_\theta^{1/2}(I-P_\theta)$ is closed.  The jointly measurable direct-integral operator

$$
 Tf(\theta,x)=\sqrt d\,w_\theta(x)^{1/2}(I-P_\theta)f(x)
$$

is closed from $L^2(\mu)$ into $L^2(\rho(d\theta);L^2(\mu))$.  Indeed, if
$f_j\to f$ in $L^2(\mu)$ and $Tf_j\to G$ in the direct-integral space, choose a subsequence
for which $(Tf_j)(\theta,\cdot)\to G(\theta,\cdot)$ in $L^2(\mu)$ for $\rho$-almost every
$\theta$.  Fiberwise closedness then gives
$G(\theta,\cdot)=\sqrt d\,w_\theta^{1/2}(I-P_\theta)f$ almost everywhere.  Hence
(6)--(7) is a closed nonnegative quadratic form.

It is densely defined.  Indeed the one-dimensional inequality proved in the next section gives,
for every locally Lipschitz $f\in L^2(\mu)$ (with weak directional derivative and an
extended-valued right side),

$$
 \mathcal q_{\mu,\theta}[f]
 \le4\int|\partial_\theta f|^2\,d\mu.
 \tag{10}
$$

Thus compactly supported smooth functions lie in the form domain, and they are dense in
$L^2(\mu)$.  Normal contractions decrease every conditional variance, so the form is Markovian.
The representation theorem supplies a nonnegative self-adjoint operator $A_{\mu,\rho}$ and a
reversible contraction semigroup.  It is conservative because $1$ belongs to the form domain
and $\mathcal D(1,g)=0$ for every form-domain $g$.

For a concrete sufficient operator domain, take $f\in\operatorname{Dom}(\mathcal D)$ such that
$w_\theta(I-P_\theta)f\in L^2(\mu)$ for $\rho$-almost every $\theta$ and

$$
 \int\|w_\theta(I-P_\theta)f\|_{L^2(\mu)}\,d\rho(\theta)<\infty.
$$

The resulting Bochner integral represents $g\mapsto\mathcal D(f,g)$ on the form domain, so
$f\in\operatorname{Dom}(A_{\mu,\rho})$ and the negative Markov generator is

$$
 \mathcal L_{\mu,\rho}f(x)
 =d\int_{S^{d-1}}w_\theta(x)
 \bigl(P_\theta f(x)-f(x)\bigr)\,d\rho(\theta),
 \qquad A_{\mu,\rho}=-\mathcal L_{\mu,\rho}.
 \tag{11}
$$

When the total pointwise jump rate is infinite, only the closed-form interpretation is asserted.
The operator has the structure of whole-conditional-line resampling with formal intensity
measure $d\,w_\theta(x)\rho(d\theta)$ at $x$; in particular, an atom $\theta$ has formal rate
$d\rho(\{\theta\})/\sigma_\theta^2$.  Thus it is a variance-normalized heat-bath-type form, not an
ordinary unit-rate hit-and-run kernel.  A literal jump-process realization would require a
separate quasi-regularity/process construction; the reversible Markov semigroup above does not
by itself supply that realization.

## 3. Exact one-dimensional sufficiency calculation

The certified repository theorem `thm:cmh-1d` includes the sharp one-dimensional log-concave
Poincar\'e estimate

$$
 C_P(\nu)\le4\operatorname{Var}_\nu(T).
 \tag{12}
$$

Apply (12) to every good conditional fiber and the function
$t\mapsto f(z+t\theta)$.  This proves (10).  Tonelli and the tight-frame identity now give

$$
 \begin{aligned}
 \mathcal D_{\mu,\rho}(f,f)
 &\le4d\int_{S^{d-1}}\int|\partial_\theta f(x)|^2
 \,d\mu(x)d\rho(\theta)\\
 &=4\int\nabla f(x)^T
 \left(d\int\theta\theta^T\,d\rho(\theta)\right)
 \nabla f(x)\,d\mu(x)\\
 &=4\int|\nabla f|^2\,d\mu.
 \end{aligned}
 \tag{13}
$$

Consequently the proposed frame inequality

$$
 \operatorname{Var}_\mu(f)\le C\mathcal D_{\mu,\rho_\mu}(f,f)
 \tag{14}
$$

implies

$$
 \boxed{C_P(\mu)\le4C.}
 \tag{15}
$$

The constant $4$ in this calculation is sharp: the centered one-sided exponential has variance
one and Poincar\'e constant $4$.  The frame constant must also satisfy $C\ge1$.  For every
linear $f_a(x)=a\cdot x$,

$$
 \mathcal q_{\mu,\theta}[f_a]=(a\cdot\theta)^2,
 \qquad
 \mathcal D_{\mu,\rho}(f_a,f_a)=|a|^2
 =\operatorname{Var}_\mu(f_a).
 \tag{16}
$$

Equation (13) has the wrong direction for a converse.  A KLS inequality controls variance by
Euclidean gradient energy, while (13) controls the conditional form from above by that energy.
No inequality derives (14) from KLS.  The proposal is therefore a sufficient-condition route,
not an equivalent reformulation.  Refuting its universal frame constant would not refute KLS.

## 4. Exact calibrations

### 4.1 Standard Gaussian: every admissible frame has gap one

Let $\mu=\gamma_d$.  Every conditional line law is $N(0,1)$ after fixing the orthogonal offset,
so $\sigma_\theta^2=1$.  Let $Q_\theta=I-\theta\theta^T$.  For $r\ge1$, in the usual
orthogonal Fock normalization of the $r$th Gaussian Wiener chaos, conditional expectation
$P_\theta$ is the second quantization of $Q_\theta$: it sends a symmetric tensor $h_r$ to
$Q_\theta^{\otimes r}h_r$.

The range of $Q_\theta^{\otimes r}$ is contained in the range of
$Q_\theta\otimes I^{\otimes(r-1)}$.  Hence

$$
 \|h_r\|^2-\|Q_\theta^{\otimes r}h_r\|^2
 \ge\|((\theta\theta^T)\otimes I^{\otimes(r-1)})h_r\|^2.
 \tag{17}
$$

Average (17) and use the frame identity on the first tensor leg:

$$
 d\int\|((\theta\theta^T)\otimes I^{\otimes(r-1)})h_r\|^2d\rho(\theta)
 =\|h_r\|^2.
 \tag{18}
$$

Orthogonality of chaoses and Tonelli yield the assertion first for every finite chaos sum.
Moreover $\mathcal D_{\gamma_d,\rho}[f]\le d\operatorname{Var}_{\gamma_d}(f)$, since each
$P_\theta$ is an orthogonal projection and $w_\theta=1$.  Thus passage to the $L^2$ limit yields

$$
 \boxed{\mathcal D_{\gamma_d,\rho}(f,f)\ge\operatorname{Var}_{\gamma_d}(f)}
 \tag{19}
$$

for every admissible $\rho$.  Linear functions give equality by (16), so the form gap is exactly
one, independently of the frame.

### 4.2 Centered one-sided-exponential products: the coordinate frame has gap one

Let $\lambda$ be the law of $Y-1$ for $Y\sim\operatorname{Exp}(1)$, and
$\mu=\lambda^{\otimes d}$.  Use

$$
 \rho_{\mathrm{coord}}
 =\frac1{2d}\sum_{i=1}^d(\delta_{e_i}+\delta_{-e_i}).
 \tag{20}
$$

Every coordinate fiber has conditional variance one and is independent of its offset.  Thus

$$
 \mathcal D_{\mu,\rho_{\mathrm{coord}}}(f,f)
 =\sum_{i=1}^d
 \mathbb E\operatorname{Var}
   (f(X)\mid X_1,\ldots,X_{i-1},X_{i+1},\ldots,X_d).
 \tag{21}
$$

The Efron--Stein inequality gives

$$
 \operatorname{Var}_\mu(f)\le\mathcal D_{\mu,\rho_{\mathrm{coord}}}(f,f).
 \tag{22}
$$

Again additive linear functions give equality in the heat-bath gap.  Combining (13) with (22)
gives $C_P(\lambda^{\otimes d})\le4$; functions depending only on one coordinate and the sharp
identity $C_P(\lambda)=4$ give the reverse inequality.  Hence
$C_P(\lambda^{\otimes d})=4$.  This calibration is important for the fence
audit: a frame may be rank-one at each update while its complete, test-independent aggregate is
not a single-coordinate argument.

Within the present density-based Radon setup, the same gap-one proof works for every product of
centered variance-one density factors, without log-concavity; log-concavity is used only in the
comparison with Euclidean gradient energy.  For arbitrary factors the identical statement can
instead be formulated using regular conditional probabilities.

## 5. Isotropic uniform simplex and the $A_{m-1}$ root frame

Let

$$
 \Delta_{m-1}=\{p\in\mathbb R_+^m:\textstyle\sum_i p_i=1\},
 \qquad P\sim\operatorname{Dir}(1,\ldots,1),
$$

and put $d=m-1$, $H_0=\mathbf1^\perp$, and

$$
 R_m=\sqrt{m(m+1)},
 \qquad X=R_m\left(P-\frac1m\mathbf1\right)\in H_0.
 \tag{23}
$$

Then $X$ is isotropic on $H_0$.  For $i\ne j$ define the unit roots

$$
 \theta_{ij}=\frac{e_i-e_j}{\sqrt2},
 \qquad
 \rho_{\mathrm{root}}
 =\frac1{m(m-1)}\sum_{i\ne j}\delta_{\theta_{ij}}.
 \tag{24}
$$

The identity

$$
 \sum_{i<j}(e_i-e_j)(e_i-e_j)^T=mI_{H_0}
$$

gives $d\int\theta\theta^T\,d\rho_{\mathrm{root}}=I_{H_0}$.

### Exact pair fiber

Fix $i<j$ and condition on all $p_\ell$, $\ell\ne i,j$, and on
$s=p_i+p_j$.  Dirichlet neutrality says

$$
 U=\frac{p_i}{s}\sim\operatorname{Unif}[0,1]
$$

independently of $(s,(p_\ell)_{\ell\ne i,j})$.  The isotropic line coordinate is uniform on

$$
 \left[-\frac{R_ms}{\sqrt2},\frac{R_ms}{\sqrt2}\right],
 \qquad
 \operatorname{Var}(T\mid s)=\frac{R_m^2s^2}{6}.
 \tag{25}
$$

Writing $\operatorname{Var}_{ij}$ for variance in $U$ at fixed outer variables, the root-frame
form is therefore

$$
 \boxed{
 \mathcal D_{\mathrm{root}}(f,f)
 =\frac{12}{m^2(m+1)}
 \sum_{i<j}\mathbb E
 \frac{\operatorname{Var}_{ij}(f)}{(p_i+p_j)^2}.}
 \tag{26}
$$

This is a complete-graph binary redistribution form with the singular rate
$(p_i+p_j)^{-2}$ and the isotropic prefactor in (26).

### Exact monomial matrices

Let $p^a=\prod_{\ell=1}^m p_\ell^{a_\ell}$ for a multi-index $a\in\mathbb N^m$, and define

$$
 \beta(r,s)=\int_0^1u^r(1-u)^sdu
 =\frac{r!s!}{(r+s+1)!}.
 \tag{27}
$$

For a pair $i<j$, put

$$
 r_a=a_i+a_j,
 \qquad
 c_{ij}(a,b)
 =\beta(a_i+b_i,a_j+b_j)
  -\beta(a_i,a_j)\beta(b_i,b_j).
 \tag{28}
$$

If the conditional covariance is nonzero, $r_a,r_b\ge1$, and Dirichlet moments give

$$
 \begin{aligned}
 B^{ij}_{a,b}
 &:=\mathbb E\frac{
 \operatorname{Cov}_{ij}(p^a,p^b)}{R_m^2(p_i+p_j)^2/6}\\
 &=\frac{6}{m(m+1)}c_{ij}(a,b)
 \frac{(m-1)!(r_a+r_b-1)!
 \prod_{\ell\ne i,j}(a_\ell+b_\ell)!}
 {(m+|a|+|b|-3)!}.
 \end{aligned}
 \tag{29}
$$

When the conditional covariance vanishes, set the entry to zero; this also covers the cases in
which the factorial expression in (29) is not invoked.  The variance Gram matrix is rational:

$$
 G_{a,b}
 =\frac{(m-1)!\prod_\ell(a_\ell+b_\ell)!}
 {(m+|a|+|b|-1)!}
 -\frac{(m-1)!\prod_\ell a_\ell!}{(m+|a|-1)!}
  \frac{(m-1)!\prod_\ell b_\ell!}{(m+|b|-1)!}.
 \tag{30}
$$

For $k\ge1$, modulo the relation $\sum p_i=1$ and constants, the root form matrix is

$$
 K_{m,k}^{\mathrm{root}}
 =\frac2m\sum_{i<j}B^{ij}
 \quad\text{on}\quad
 V_{m,k}=\mathbb R[p_1,\ldots,p_m]_{\le k}\Big/
 \left((\textstyle\sum_i p_i-1)\mathbb R[p]_{\le k-1}+\mathbb R1\right)
 \tag{31}
$$

After choosing any rational quotient basis, the matrices in (30)--(31) are well defined.
Consequently the exact degree-$k$ root-frame gap
is the finite rational generalized eigenvalue

$$
 \lambda^{\mathrm{root}}_{m,k}
 =\min_{0\ne c\in V_{m,k}}
 \frac{c^TK_{m,k}^{\mathrm{root}}c}{c^TG_{m,k}c}.
 \tag{32}
$$

No floating computation is required to define or certify (32).

### Symmetry sectors

Both matrices commute with the $S_m$ action.  For every partition $\lambda\vdash m$, the exact
central idempotent

$$
 \Pi_\lambda
 =\frac{\dim\lambda}{m!}\sum_{\sigma\in S_m}
 \chi_\lambda(\sigma)U_\sigma
 \tag{33}
$$

projects onto its isotypic component.  Only partitions with
$m-\lambda_1\le k$ can occur.  In rational Specht coordinates, Schur reduction writes the two
forms on the $\lambda$-isotypic component as

$$
 G=J_\lambda\otimes G_\lambda,
 \qquad K=J_\lambda\otimes K_\lambda,
$$

where $J_\lambda$ is a fixed rational Specht Gram form and $G_\lambda,K_\lambda$ are rational
forms on the finite multiplicity space.  (Replacing $J_\lambda$ by an identity may require an
irrational coordinate change.)  Thus
(32) is exactly the minimum of the generalized eigenvalues of those multiplicity-space pencils.
This is the requested symmetry-sector formulation; it also retains the possible multiple copies
of the standard representation, which a list of symmetric test polynomials alone would miss.

### Two exact sector checks

Linear functions lie in the standard sector and have quotient one by (16).  The first nontrivial
invariant sector has the centered radial quadratic

$$
 F(X)=|X|^2-d=R_m^2\left(\sum_iP_i^2-\frac2{m+1}\right).
 \tag{34}
$$

On a root fiber, $F$ varies only through $T^2$.  If $T$ is uniform on $[-h,h]$, then

$$
 \frac{\operatorname{Var}(T^2)}{\operatorname{Var}(T)}
 =\frac{4h^2}{15}.
$$

Here $h=R_ms/\sqrt2$ and
$\mathbb Es^2=6/[m(m+1)]$, so every root direction satisfies
$\mathcal q_{\mu,\theta_{ij}}[F]=4/5$ and

$$
 \mathcal D_{\mathrm{root}}(F,F)=\frac{4(m-1)}5.
 \tag{35}
$$

The Dirichlet moments

$$
 \operatorname{Var}\left(\sum_iP_i^2\right)
 =\frac{4(m-1)}{(m+1)^2(m+2)(m+3)}
$$

give

$$
 \operatorname{Var}(F)
 =\frac{4m^2(m-1)}{(m+2)(m+3)},
 \qquad
 \frac{\mathcal D_{\mathrm{root}}(F,F)}{\operatorname{Var}(F)}
 =\frac{(m+2)(m+3)}{5m^2}\longrightarrow\frac15.
 \tag{36}
$$

This low-degree check is nonfatal by itself.  It proves that a root-frame constant cannot be
smaller than asymptotically five, but it does not produce a decaying fixed-degree quotient and it
says nothing about the other symmetry sectors in (32).  The full $L^2$ root form is nevertheless
killed by the nonpolynomial cap below.

### Exact vertex-cap obstruction: the root-frame gap is $O(m^{-2})$

It is convenient to rescale to $\eta_i=mP_i$, so $\eta_i\ge0$ and
$\sum_i\eta_i=m$.  Formula (26) becomes

$$
 \mathcal D_{\mathrm{root}}(f,f)
 =\frac{12}{m+1}\sum_{i<j}
 \mathbb E\left[
 (\eta_i+\eta_j)^{-2}\operatorname{Var}_{ij}(f)
 \right].
 \tag{37}
$$

For $m\ge2$, fix $\varepsilon\in(0,1)$ and take the vertex cap

$$
 A_{m,\varepsilon}=\{\eta_1>m-\varepsilon\},
 \qquad
 p_{m,\varepsilon}:=\mu(A_{m,\varepsilon})
 =\left(\frac\varepsilon m\right)^{m-1}.
 \tag{38}
$$

Pair refreshes not involving coordinate $1$ leave its indicator fixed.  For a pair $(1,j)$,
write $q_{1j}$ for the conditional probability of $A_{m,\varepsilon}$.  Since
$q_{1j}(1-q_{1j})\le q_{1j}$ and every point of the cap satisfies
$\eta_1+\eta_j>m-\varepsilon$,

$$
 \begin{aligned}
 \mathbb E\left[(\eta_1+\eta_j)^{-2}
 \operatorname{Var}_{1j}(\mathbf1_A)\right]
 &\le
 \mathbb E\left[(\eta_1+\eta_j)^{-2}q_{1j}\right]\\
 &=\mathbb E\left[
 \frac{\mathbf1_A}{(\eta_1+\eta_j)^2}\right]
 \le\frac{p_{m,\varepsilon}}{(m-\varepsilon)^2}.
 \end{aligned}
 \tag{39}
$$

The middle equality is a weighted tower identity.  It is justified first with the
fiber-measurable weight $(\eta_1+\eta_j)^{-2}$ truncated at level $N$, and then by monotone
convergence as $N\to\infty$.

There are $m-1$ such pairs, so

$$
 \frac{\mathcal D_{\mathrm{root}}(\mathbf1_A,\mathbf1_A)}
 {\operatorname{Var}(\mathbf1_A)}
 \le
 \frac{12(m-1)}{(m+1)(m-\varepsilon)^2
 (1-p_{m,\varepsilon})}
 =O(m^{-2}).
 \tag{40}
$$

The centered indicator $\mathbf1_A-p_{m,\varepsilon}$ belongs to the maximal form domain: a pair
fiber has nonzero conditional variance
only when its conserved sum exceeds $m-\varepsilon$, where the inverse-square rate is bounded.
Moreover $p_{m,\varepsilon}<1/2$ and $m-\varepsilon>m/2$, so (40) gives the explicit uniform
bound

$$
 \operatorname{gap}(\mathcal D_{\mathrm{root}})
 <\frac{96}{m^2}=O(m^{-2}).
 \tag{41}
$$

This is a rigorous root-frame refutation, not numerical evidence.  It also explains why the
radial quadratic in (36) was misleading as a global calibration: fixed-degree bulk polynomials
do not see an exponentially small neighborhood of a vertex.  The cap does not refute (43) below,
because another frame can place long vertex-to-opposite-face directions where the root frame
places only pair exchanges.

## 6. The all-frame simplex min--max and an exact dual refuter

Fix $k\ge1$.  For a general direction $\theta\in S(H_0)$, let $B_{m,k}(\theta)$ be the matrix of the
single-direction normalized form (5) on $V_{m,k}$.  Put

$$
 \mathfrak F_d
 =\left\{\rho:\rho\text{ even probability on }S(H_0),\quad
 d\int\theta\theta^T\,d\rho=I_{H_0}\right\}
 \tag{42}
$$

and

$$
 \boxed{
 \Lambda_{m,k}
 =\sup_{\rho\in\mathfrak F_d}
 \lambda_{\min}\left(d\int B_{m,k}(\theta)d\rho(\theta),G_{m,k}\right).}
 \tag{43}
$$

The universal route implies $\inf_m\Lambda_{m,k}>0$ for every fixed $k\ge1$.  Conversely,
$\Lambda_{m,k}\to0$ for one fixed $k$ refutes the route, because the full $L^2$ gap is no larger
than its restriction to $V_{m,k}$.  Such a refuter necessarily has $k\ge2$, since $V_{m,1}$
consists of linear tests and (16) gives quotient one.

### Symmetrization is valid, but does not select the root orbit

Average any $\rho$ over $S_m$.  The frame constraints are preserved and

$$
 A_{\bar\rho}=\frac1{m!}\sum_{\sigma\in S_m}U_\sigma^*A_\rho U_\sigma.
$$

The minimum generalized eigenvalue is concave, so
$\lambda_{\min}(A_{\bar\rho},G)\ge\lambda_{\min}(A_\rho,G)$.  Therefore the supremum in (43)
may be restricted to permutation-invariant frames.  Such a frame can be a mixture of
continuously many $S_m$-orbits.  Symmetry does **not** prove that the $A_{m-1}$ root orbit is
optimal.

### Finite exact dual certificate

Let $N=\dim V_{m,k}$.  A certificate that $\Lambda_{m,k}\le\varepsilon$ consists of finite
matrices

$$
 Z\in\operatorname{Sym}_N,\qquad M\in\operatorname{Sym}(H_0)
 \tag{44}
$$

such that

$$
 Z\succeq0,\qquad \operatorname{Tr}(ZG_{m,k})=1,
 \tag{45}
$$

$$
 \operatorname{Tr}(ZB_{m,k}(\theta))
 \le\theta^TM\theta
 \quad\text{for every }\theta\in S(H_0),
 \tag{46}
$$

and

$$
 \operatorname{Tr}M\le\varepsilon.
 \tag{47}
$$

Indeed, for every admissible $\rho$,

$$
 \begin{aligned}
 \lambda_{\min}(A_\rho,G)
 &\le\operatorname{Tr}(ZA_\rho)
 =d\int\operatorname{Tr}(ZB(\theta))d\rho(\theta)\\
 &\le d\int\theta^TM\theta\,d\rho(\theta)
 =\operatorname{Tr}M.
 \end{aligned}
 \tag{48}
$$

After permutation symmetrization one may take $Z$ block diagonal in the exact isotypic
decomposition and $M=(\varepsilon/d)I_{H_0}$.  The certificate then reduces to

$$
 Z\succeq0,\qquad\operatorname{Tr}(ZG)=1,\qquad
 d\operatorname{Tr}(ZB(\theta))\le\varepsilon
 \quad\forall\theta\in S(H_0).
 \tag{49}
$$

Equivalently, factor
$Z=\sum_{r=1}^R w_rc_rc_r^T$ with exact nonnegative algebraic weights.  Equations (45) and (49)
say that a finite randomized ensemble of degree-$k$ test polynomials has total variance one and
average single-direction normalized energy at most $\varepsilon/d$ for every direction.  This
forces one member of the ensemble to be bad for each proposed frame by (48), without choosing a
test after seeing an individual sampled direction.

The regularity needed to make the continuum certificate exact is elementary for polynomial
tests.  For an interior simplex point $p$ and $\theta\in S(H_0)$, its chord in isotropic line
coordinates has endpoints

$$
 a(p,\theta)=\max_{\theta_i>0}\frac{-R_mp_i}{\theta_i},
 \qquad
 b(p,\theta)=\min_{\theta_i<0}\frac{-R_mp_i}{\theta_i}.
$$

For a polynomial $f$, the conditional covariance on $[a,b]$ is divisible by $(b-a)^2$; division
by $\operatorname{Var}(T)=(b-a)^2/12$ therefore has a continuous value when the chord
degenerates.  The resulting line-constant quotient is continuous in $(p,\theta)$ away from the
$\mu$-null boundary and is bounded uniformly by
$4\sup_{\Delta_{m-1}}|\partial_\theta f|^2$, by (12).  Writing (5) as the $\mu$-expectation of
this line-constant quotient and applying dominated convergence proves continuity of
$B_{m,k}(\theta)$.  On each of the finitely many sign, active-endpoint, and parametric-polytope
combinatorial chambers, the endpoint formulas and polynomial integration make every entry of
$B_{m,k}$ rational-semialgebraic in $\theta$.

For fixed $m,k$, (49) is finitely checkable in exact arithmetic.  Sort the coordinates of
$\theta$, split further by their signs and by the finitely many active-facet patterns of simplex
chords, integrate the polynomial conditional covariances on each resulting parametric polytope,
and clear the positive denominators.  What remains is a finite family of polynomial
nonnegativity statements on compact semialgebraic chambers.  A rational
sum-of-squares/Positivstellensatz identity, or exact real quantifier-elimination certificate, is
a finite proof of (49).  Ties and zero coordinates follow by the continuous boundary limits.

Thus a sequence of exact data $(Z_m,\varepsilon_m)$ satisfying (49) for one fixed $k$ and
$\varepsilon_m\to0$ is the requested decisive refuter of **every** admissible isotropic frame.
No such certificate is produced here.

For completeness, the primal is finite as well after an atomic reduction: the pair
$(B(\theta),\theta\theta^T)$ has compact image in a finite-dimensional vector space by the
continuity just proved.  Weak-* compactness gives an optimizer and Carath\'eodory gives one
supported on at most

$$
 1+\frac{N(N+1)}2+\frac{d(d+1)}2
$$

unoriented direction pairs.  This observation does not replace the upper-bound certificate
(44)--(47).

## 7. Primary-literature check

The nearby literature confirms that the object is recognizable but does not supply the proposed
dimension-free normalized gap.

1. **Ordinary hit-and-run.**  Hit-and-run resamples the conditional law on a randomly selected
   chord, so its unnormalized Dirichlet form averages
   $\mathbb E\operatorname{Var}(f\mid P_{\theta^\perp}X)$.  It does not insert the fiber rate
   $\sigma_\theta^{-2}$.  Chen--Eldan,
   [*Hit-and-run mixing via localization schemes*](https://arxiv.org/abs/2212.00297), bounds
   mixing in terms of the KLS constant; it does not prove the present sufficient condition.
2. **Recent spectral comparison.**  Kook--Vempala,
   [*Spectral Gaps of Hit-and-Run and Coordinate Hit-and-Run*](https://arxiv.org/abs/2608.16878)
   (17 August 2026 preprint), lower-bounds the ordinary hit-and-run gap in terms of the target's
   existing Poincar\'e constant and geometric scale.  That is the reverse logical direction and
   again concerns the unnormalized chain.
3. **Simplex heat baths.**  Caputo,
   [*On the spectral gap of the Kac walk and other binary collision
   processes*](https://alea.math.cnrs.fr/articles/v4/04-10.pdf), proves for the flat-simplex
   complete-graph pair-refresh generator $m^{-1}\sum_{i<j}(P_{ij}-I)$ the exact gap
   $(m+1)/(3m)$.  In the exchange normalization
   $$
   \mathcal E_{\gamma,m}
   =\frac{m}{\binom m2}\sum_{i<j}
   \mathbb E[(\eta_i+\eta_j)^\gamma\operatorname{Var}_{ij}(f)],
   $$
   formula (37) is exactly
   $$
   \mathcal D_{\mathrm{root}}
   =6\frac{m-1}{m+1}\mathcal E_{-2,m}.
   $$
   The published exact gap is the unweighted case $\gamma=0$, not $\gamma=-2$.
4. **Weighted exchange boundary.**  Carlen--Posta--T\'oth,
   [*Spectral Gap for the Stochastic Exchange
   Model*](https://doi.org/10.1016/j.spa.2025.104769), prove uniform exchange gaps for
   $\gamma\in[0,1]$.  Their theorem does not include the negative exponent $-2$, and the exact
   cap calculation (38)--(41) shows that such an extension would be false.
5. **Frame methods with invariance.**  Barthe--Cordero-Erausquin,
   [*Invariances in variance estimates*](https://doi.org/10.1112/plms/pds011), combine
   decompositions of the identity with conditional Poincar\'e estimates and include the regular
   simplex root system.  Their conclusion uses symmetry to produce a gradient variance bound;
   it is not inverse-conditional-variance approximate tensorization and does not overcome the
   cap obstruction.

The literature therefore supplies comparison mechanisms and exact neighboring models, not the
candidate theorem.  No bibliography delta is proposed from this probe; a literature scout should
audit publication metadata before any import.

## 8. Six-fence audit

### `obs:two-tail` — evaded

The route asserts no slice-wise source/excess inequality and follows no anisotropic stochastic
posterior.  Its normalization divides by the actual conditional line variance.  In particular,
an anisotropic Gaussian line variance cancels from the normalized linear quotient rather than
creating a $\Lambda^2$ source charged to an absolute excess.  The two-tail covariance weight is
neither hidden nor consumed.

### `obs:proj-ceiling` — evaded

Although each update uses a line direction, the datum is the full offset-dependent conditional
fluctuation $f-P_\theta f$, not a marginal or radial projection statistic.  The Gaussian proof
(17)--(19) acts on every tensor chaos and contracts a complete tensor leg; it does not reconstruct
a matrix estimate by integrating projection bounds.  There is no Lorentz $\ell_{2,1}$ summation
and no lost $\log d$.

### `obs:crude-insufficient` — inapplicable and not used

There is no stochastic localization time, covariance excess $\Xi_T$, or logarithmic bootstrap.
No crude covariance integral is presented as a closing estimate.

### `obs:relative-ceiling` — respected by classification

The headline frame inequality directly implies KLS by (13)--(15).  It is openly classified as a
new sufficient-condition target, not sold as a weaker bootstrap premise.  Therefore it does not
violate the fence; it accepts the full strength of what it asks.

### `obs:circularity` — evaded

No lower bound on a localized isoperimetric profile, moving competitor family, or perimeter
supermartingale appears.  The only slice input is the independently known sharp
one-dimensional Poincar\'e theorem.  The unresolved global form gap is stated as the target rather
than inserted inside its proof.

### `obs:rank-one-refuted` — evaded

No fixed cut or covariance-inflation witness is used.  A single directional heat bath has a large
kernel; the proposal relies on a complete test-independent tight frame.  The product calibration
uses all coordinate directions and Efron--Stein tensorization.  It makes no inference from one
coordinate alone.

No `bounded_by` edge is proposed: the six nodes currently constrain Eldan-route proof shapes,
and this report uses none of those shapes.  The explicit audit should be retained in any future
route brief.

## 9. Novelty against existing routes and classical needles

| comparison | different carrier | different bottleneck |
|---|---|---|
| classical KLS needles | one selected localization needle preserving one or two scalar constraints | this route simultaneously disintegrates all offsets for every frame direction and restores linear covariance through a tight-frame average |
| Eldan localization | fixed cuts, stochastic posterior paths, Riccati source/damping, covariance occupation | a static reversible nonlocal form on the original law; no cut, time, damping, or high-rank occupation |
| moment-map spectral | one first eigenfunction followed through stochastic localization, with $H_t$ unwhitening | every $L^2$ test in one fixed heat-bath form; no eigenfunction tensor or posterior orientation |
| moment-map/CMH | canonical moment Hessian, Stein generator, commutators, and solenoidal flux | conditional Radon fibers and a jump operator; no moment map or differential compatibility |
| standard hit-and-run | unit-rate or direction-rate conditional resampling | inverse conditional-variance acceleration and a measure-dependent but state/test-independent tight frame |

The novelty is therefore real at the level of mechanism.  The resemblance to needles and
hit-and-run is useful for literature, but neither known route contains the inverse-variance frame
gap or implies it.

## 10. Dead ends and exact residue

### Dead ends that should not be rerun

1. **The one-dimensional theorem does not prove the frame gap.**  It gives the upper comparison
   (13), while the target needs the lower comparison (14).
2. **Linear calibration is not a proof.**  Equation (16) only fixes the normalization and the
   necessary constant $C\ge1$; nonlinear sectors may be much worse.
3. **The root orbit is analytically dead but is not forced by symmetry.**  Equation (40) kills
   that frame.  Permutation symmetrization still leaves arbitrary mixtures of direction orbits,
   so this alone cannot refute the existential frame target.
4. **The radial quadratic misses the actual root obstruction.**  Its exact quotient tends to
   $1/5$; the vertex cap, not a fixed-degree bulk polynomial, produces the $m^{-2}$ gap.
5. **The published simplex exchange gap cannot be transplanted.**  Its update rate is constant;
   (26) has $(p_i+p_j)^{-2}$.
6. **Ordinary hit-and-run estimates run in the wrong logical direction.**  Bounds that consume
   $C_P(\mu)$ cannot prove a new frame inequality intended to imply $C_P(\mu)$.
7. **Choosing $\rho$ after choosing $f$ breaks the target.**  Any minimax argument must preserve
   $\exists\rho\,\forall f$.

### Residue

- **Needs new idea:** construct $\rho_\mu$ from log-concave geometry and prove a universal lower
  gap for (6), uniformly over all $f$ in the maximal form domain.
- **Needs new idea, decisive alternative:** for the isotropic uniform simplex, produce exact
  certificates (44)--(49) with $\varepsilon_m\to0$ at one fixed degree, or prove a uniform lower
  bound for (43).  The cap has already killed the root frame; it does not settle other invariant
  orbit mixtures.  The uniform spherical frame is the clean next analytic stress test.
- **Dossier packaging, no route-level gap:** formalize the Borel-kernel and direct-integral
  arguments above in a standalone proof, and retain the form-sense interpretation when
  pointwise total jump rates are infinite.  No pointwise process construction is needed for the
  spectral target.
- **Technical, not mathematical:** an algorithmic route would need a measurable rule
  $\mu\mapsto\rho_\mu$.  The existential KLS implication does not require such a selector.

No numerical diagnostic is dispatched.  A floating simplex sweep could neither certify the
continuum directional inequality in (46) nor refute every frame.  The next admissible
falsification object is the exact dual certificate itself.

## 11. Proposed route-control and claim text

The candidate survives, so the following is exact proposed text for the orchestrator.  It is not
an instruction to mark anything proved.

### Route registry row

| route | thesis | main fence |
|---|---|---|
| `conditional-fiber-frame` | A test-independent isotropic frame of inverse-variance-normalized conditional line resamplings has a universal $L^2$ gap. | construct one frame uniformly over all tests, or decide the all-frame simplex dual |

### Route gate

> For every full-dimensional isotropic log-concave $\mu$ on $\mathbb R^d$, construct one even
> probability $\rho_\mu$, independent of the test function, with
> $d\int\theta\theta^T\,d\rho_\mu=I_d$, and prove
> $\operatorname{Var}_\mu(f)\le C\mathcal D_{\mu,\rho_\mu}(f)$ on the maximal closed form domain
> with universal $C$.  Alternatively, refute the route by an exact fixed-degree uniform-simplex
> dual certificate satisfying (44)--(49) with objective tending to zero.  A root-frame-only or
> floating computation does not decide the gate.

### Manuscript question

> **Question (conditional-fiber frame).**  Let $\mu$ be a full-dimensional isotropic
> log-concave probability on $\mathbb R^d$.  Does there exist an even Borel probability
> $\rho_\mu$ on $S^{d-1}$, chosen independently of $f$, such that
> $d\int\theta\theta^T\,d\rho_\mu=I_d$ and, for a universal $C$,
> $$
> \operatorname{Var}_\mu(f)\le C d\int_{S^{d-1}}\int_{\theta^\perp}
> \frac{\operatorname{Var}_{\mu_{\theta,z}}(f(z+T\theta))}
> {\operatorname{Var}_{\mu_{\theta,z}}(T)}
> \,d\bar\mu_\theta(z)d\rho_\mu(\theta)
> $$
> for every $f$ in the maximal form domain, with null and zero-variance fibers assigned quotient
> zero?

### Proposed ledger candidate

Admission requires adding `conditional-fiber-frame` to `meta.route_policy.allowed` and a matching
manuscript file/label first.

```yaml
- id: q:conditional-fiber-frame
  kind: question
  status: open
  route: conditional-fiber-frame
  file: modules/kls/XX-conditional-fiber-frame.tex
  statement: "For every full-dimensional isotropic log-concave mu on R^d, there exists one even test-function-independent probability rho_mu on S^(d-1) with d int theta theta^T d rho_mu = I such that Var_mu(f) <= C D_(mu,rho_mu)(f) for all f in the maximal closed conditional-fiber form domain, with C universal."
```

The structural reduction can be proposed separately, still `open` until a prover and cold reviewer
certify it:

```yaml
- id: lem:conditional-fiber-form
  kind: lemma
  status: open
  route: conditional-fiber-frame
  file: modules/kls/XX-conditional-fiber-frame.tex
  statement: "The variance-normalized conditional-line form is a densely defined closed reversible Dirichlet form with its nonlocal generator understood in form sense, and pointwise on the stated sufficient Bochner domain; every admissible tight frame satisfies D_(mu,rho)(f) <= 4 int |grad f|^2 dmu, so a frame gap C implies CP(mu) <= 4C. Linear tests have quotient one; every admissible Gaussian frame and the coordinate frame on standardized products have form gap one."
  depends_on: [thm:cmh-1d]
```

No edge to a live route, no `bounded_by` edge, and no status transition is proposed.

The exact root-frame refuter is also a candidate node, not a certified delta:

```yaml
- id: prop:conditional-fiber-root-obstruction
  kind: proposition
  status: open
  route: conditional-fiber-frame
  file: modules/kls/XX-conditional-fiber-frame.tex
  statement: "For the isotropic uniform (m-1)-simplex and the even A_(m-1) root frame, a vertex-cap indicator has normalized conditional-fiber Rayleigh quotient at most 12(m-1)/[(m+1)(m-epsilon)^2(1-(epsilon/m)^(m-1))]; hence the root-frame gap is O(m^(-2))."
```

## Proposed one-line gate update

> Admit `conditional-fiber-frame` only as a new sufficient-condition route: certify its closed
> form and factor-$4$ bridge, then decide the test-independent universal frame gap; on the
> simplex, only an all-frame exact dual certificate or a uniform lower bound for (43) is
> decisive.

```yaml
outcome: blocked
artifacts:
  - research/explorations/2026-08-27-kls-route-prober-conditional-fiber-frame-w1f01.md
proposed_deltas:
  - "Optionally admit the new route and the three open candidate nodes using the exact text in Section 11; make no mathematical status change and add no cross-route edge."
  - "Record the analytic O(m^-2) root-frame refuter, but do not infer an all-frame simplex verdict: the unresolved quantity is the all-frame min--max Lambda_(m,k)."
next_role: prover
next_prompt: |
  Write a standalone structural dossier for `lem:conditional-fiber-form`, not for the universal
  question.  Starting from the canonical density disintegration along affine lines, state null
  fibers, zero conditional variance, jointly measurable versions, and the maximal form domain.
  Prove closedness through the commuting conditional projection and fiber-measurable weight,
  prove the symmetric pair-jump representation and Markov property, and identify the associated
  self-adjoint reversible nonlocal generator in form sense when pointwise rates are infinite.
  Apply the sharp one-dimensional log-concave Poincare bound to prove
  `D <= 4 int |grad f|^2`, hence the conditional implication `CP <= 4C`.  Prove the exact linear,
  Gaussian-chaos, and centered-product/Efron--Stein calibrations.  Include the uniform-simplex
  root formula (26), rational monomial matrices (29)--(32), radial quotient (36), and vertex-cap
  bound (38)--(41) as calibrated structural statements.  State exactly that the cap refutes the
  root frame but not the existential all-frame target; do not claim optimality of the root orbit,
  equivalence with KLS, or a simplex-wide refutation.  Compile the
  dossier and hand it to a distinct cold proof-checker.  Do not edit the ledger, manuscript,
  route-control files, bibliography, this exploration, or any numerical file.
```
