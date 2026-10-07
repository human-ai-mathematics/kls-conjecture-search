---
title: 'Song–Zhang v1: analytic foundations and Appell variance estimates'
ledger-node:
  - thm:sz-polynomial-variance
  - lem:sz-analytic-foundations
numbering:
  enumerator: '120.%s'
---

*Part of the first version of Song–Zhang, Chapter [](#sec:polynomial-curvature); the reading order is on the [full proofs](#sec:proofs-sz-v1) page.*

**Overview.** This reconstructs the polynomial estimate of Song–Zhang,
[@SongZhang2026IteratedLogKLS, Sections 3–4], with the quadratic estimate
[](#thm:letwin-qcts) as its nonclassical input. All tensor norms sum over ordered
indices. The proof constructs the localization globally, keeps the covariance–mean
cross variation, and closes a finite induction in the polynomial degree. It also
records the analytic foundations needed by the subsequent inverse-operator argument.
No eigenfunction or inverse operator is passed through an approximation limit.
The source version is [arXiv:2610.01447v1](https://arxiv.org/abs/2610.01447v1).

1. Appell expansion identifies the derivative means that polynomial testing controls.
2. Quadratic variance controls every whitened third-moment noise coefficient.
3. A coupled tensor hierarchy controls the mean and fluctuating derivative energies.
4. Matrix strong convexity at a short terminal time closes the degree induction.
5. Cutoff and moment approximation remove all auxiliary regularity assumptions.

## Statement and Appell coordinates

:::{prf:definition} Appell coefficients and ordered-index norms
:label: def:sol-sz-appell
For a probability measure $\mu$ with all polynomial moments define the symmetric
tensor polynomials $\mathcal A_k^\mu$ by the formal identity

$$
\frac{e^{z\cdot x}}{\mathbb E_\mu e^{z\cdot X}}
=\sum_{k\ge0}\frac{\langle\mathcal A_k^\mu(x),z^{\otimes k}\rangle}{k!}.
$$

The quotient means division of formal power series with denominator constant term
one. Set $P_k^\mu[T]=\langle T,\mathcal A_k^\mu\rangle$ and
$K_k(\mu)=\sup_{T\text{ symmetric},\ \|T\|_{\mathrm{HS}}=1}
\operatorname{Var}_\mu P_k^\mu[T]$. The Hilbert–Schmidt norm uses the full tensor
space, without dividing by a factorial. For a polynomial $q$, $D^kq$ is its full
symmetric derivative tensor.
:::

:::{prf:theorem} Polynomial variance and derivative means
:label: thm:sol-sz-polynomial
For every isotropic log-concave probability $\mu$ on $\mathbb R^n$, every integer
$d\ge1$ and every symmetric $d$-tensor $T$, the unique polynomial $P$ satisfying
$D^dP=d!T$ and $\mathbb E_\mu D^jP=0$ for $0\le j<d$ is $P_d^\mu[T]$, and

$$
\operatorname{Var}_\mu P_d^\mu[T]\le1024^d(d!)^4\|T\|_{\mathrm{HS}}^2.
$$

For every polynomial $q$ of degree at most $s$,

$$
\sqrt{\operatorname{Var}_\mu q}
\le\sum_{k=1}^s32^k k!\|\mathbb E_\mu D^kq\|_{\mathrm{HS}}.
$$

Both inequalities hold with the same constants for every centered log-concave
probability of covariance at most $I$, including singular covariance. These are the
assertions of [](#thm:sz-polynomial-variance).
:::

Formal differentiation followed by expectation gives
$\mathbb E D^jP_k[T]=0$ for $j<k$ and $D^kP_k[T]=k!T$.
These conditions characterize $P_k[T]$: the top derivative fixes its homogeneous
part, and descending through the degrees fixes each remaining homogeneous part.
Applying the same descending argument to an arbitrary polynomial gives the exact identity

$$
q-\mathbb E q=\sum_{k=1}^s\frac1{k!}P_k^\mu[\mathbb E D^kq].
$$

Consequently a bound $K_k(\mu)\le B_k$ implies the derivative-mean estimate with
coefficients $\sqrt{B_k}/k!$. This uses the triangle inequality in $L^2$, with no
orthogonality assertion. It applies to a polynomial valued in any finite-dimensional
Hilbert space as well: first sum the scalar bounds in an orthonormal output basis,
then apply the triangle inequality in the direct sum. Thus no output dimension is lost.

## The quadratic input and global localization

For an isotropic log-concave vector $\xi$ set
$S_i=\mathbb E[\xi_i\xi\xi^T]$ and $S_z=\sum_i z_iS_i$. For every symmetric $D$,
[](#thm:letwin-qcts) and Cauchy–Schwarz give

$$
|\langle D,S_z\rangle|
=|\mathbb E[(z\cdot\xi)(\xi^TD\xi-\operatorname{tr}D)]|
\le\sqrt8|z|\|D\|_{\mathrm{HS}}.
$$

Duality on symmetric matrices gives $\|S_z\|_{\mathrm{HS}}^2\le8|z|^2$.
Full symmetry of the third moment gives
$\sum_i|S_i z|^2=\|S_z\|_{\mathrm{HS}}^2$. Therefore

$$
\sum_i S_i^2\preceq8I,\qquad
\sum_i\operatorname{tr}(S_i^2)\le8n,\qquad
\sum_i(\operatorname{tr}S_i)^2\le8n^2.
$$

The last inequality follows from $(\operatorname{tr}S_i)^2\le
n\operatorname{tr}(S_i^2)$. No estimate on the full third-tensor norm independent
of dimension is used.

:::{prf:lemma} Global covariance-adapted localization
:label: lem:sol-sz-localization
For compactly supported isotropic log-concave $\mu_0$ there is a global process

$$
\mu_t(dx)=Z_t^{-1}e^{\theta_t\cdot x-x^T\Lambda_tx/2}\mu_0(dx),\qquad
 d\theta_t=A_t^{-1}m_t\,dt+A_t^{-1/2}\,d\beta_t,
 \qquad d\Lambda_t=A_t^{-1}\,dt,
$$

starting at $(\theta_0,\Lambda_0)=(0,0)$, where $m_t,A_t$ are its mean and
covariance. Its covariance stays positive definite at every finite time. For bounded
$q$, writing $\mathbb E_t$ for integration against $\mu_t$ and
$\xi_t=A_t^{-1/2}(x-m_t)$,

$$
 d\mathbb E_tq=\operatorname{Cov}_t(q,\xi_t)\cdot d\beta_t,
 \quad dm_t=A_t^{1/2}d\beta_t,
 \quad dA_t=\sum_iU_{i,t}d\beta_{i,t}-A_tdt,
 \quad U_i=A_t^{1/2}S_iA_t^{1/2}.
$$

The first process is a true martingale. For $t>0$, $\mu_t$ is strongly log-concave
with curvature matrix $\Lambda_t$ in the extended-valued convex-potential sense.
:::

:::{prf:proof}
Suppose the support lies in a ball of radius $\rho$. For finite $(\theta,\Lambda)$
the partition function and its derivatives are smooth, by differentiation under the
integral on compact parameter sets. The tilted measure has exactly the same null sets
as $\mu_0$, so its covariance is positive definite. The SDE coefficients are therefore
locally Lipschitz and admit a unique solution up to their explosion time $\zeta$.

Work first before leaving a compact parameter set. For
$r_t(x)=e^{\theta_t\cdot x-x^T\Lambda_tx/2}$, Itô's formula gives
$dr_t/r_t=x^TA_t^{-1}m_tdt+x^TA_t^{-1/2}d\beta_t$: its quadratic variation cancels
the derivative of the quadratic tilt. Integration gives the same identity for $Z_t$
with $x$ replaced by $m_t$. The quotient rule then gives

$$
d(r_t/Z_t)=(r_t/Z_t)(x-m_t)^TA_t^{-1/2}d\beta_t.
$$

Stochastic Fubini is valid on these stops because the support and all coefficients
are bounded. Taking $q=x$ gives the mean equation; taking $q=xx^T$ and subtracting
$d(m_tm_t^T)$ gives the covariance equation, including drift $-A_tdt$.
The positive semidefinite tilt preserves log-concavity, so the third-moment estimates
above hold for $\xi_t$ until $\zeta$.

Apply Itô's formula to the logarithmic determinant. Cyclicity of trace gives

$$
\log\det A_t=M_t-nt-\frac12\int_0^t\sum_i\operatorname{tr}(S_{i,s}^2)ds
\ge M_t-5nt,\qquad
M_t=\int_0^t\sum_i\operatorname{tr}(S_{i,s})d\beta_{i,s}.
$$

Its quadratic variation is at most $8n^2t$. Extend the predictable integrand by zero
after $\zeta$; the resulting integral is a continuous martingale on each deterministic
finite interval $[0,T]$. Its pathwise minimum on that interval is finite. Consequently
$\det A_t$ has a positive pathwise lower bound for $t<T\wedge\zeta$.
Since $A_t\preceq\rho^2I$, the smallest eigenvalue is at least
$\det A_t/(\rho^2)^{n-1}$. Thus $A_t^{-1}$ is pathwise bounded on that interval.
Also $|m_t|\le\rho$. The finite-variation parts of $\theta_t,\Lambda_t$ then have
finite limits at a purported finite $\zeta$, and the martingale part of $\theta_t$
has finite quadratic variation and a finite limit there. This last assertion follows
by stopping when the preceding bounds exceed an integer, then taking their union.
At the limiting finite parameters the coefficients are locally Lipschitz, allowing
continuation, a contradiction. Thus $\zeta=\infty$.

Every bounded posterior expectation is now a bounded local martingale, hence a true
martingale. Its conditional-expectation consistency at different times is exactly the
martingale property; no independent construction of an underlying signal is needed.
Finally if $\mu_0(dx)=e^{-V_0(x)}dx$ with $V_0$ convex and possibly infinite, its
posterior potential is $V_0-\theta_t\cdot x+\log Z_t+x^T\Lambda_tx/2$.
The integral defining $\Lambda_t$ is positive definite for $t>0$, proving the claim.
:::

## Tensor hierarchy with all cross terms

Fix a polynomial $f$ of degree $d$, and put

$$
h_j(t)=\mathbb E_tD^jf,\quad K_j(t)=A_t^{\otimes j},\quad
N_j(t)=\mathbb E_{\mathrm{loc}}\langle h_j,K_jh_j\rangle,
$$

$$
L_j(t)=\mathbb E_{\mathrm{loc}}\mathbb E_t
\langle D^jf-h_j,K_j(D^jf-h_j)\rangle.
$$

The tensor slots here concern input derivatives; any additional output slots are
contracted with their ordinary Euclidean metric.

:::{prf:lemma} Drift of covariance-weighted derivative means
:label: lem:sol-sz-hierarchy
The functions $N_j$ are locally absolutely continuous and satisfy, almost everywhere,
$N_j'\le4j^2N_j+9j^2L_j$ for $1\le j\le d$.
:::

:::{prf:proof}
On two tensor slots, for each symmetric $S_i$,

$$
2S_i\otimes S_i\preceq S_i^2\otimes I+I\otimes S_i^2
$$

because the difference is $(S_i\otimes I-I\otimes S_i)^2$.
Hence $\sum_iS_i\otimes S_i\preceq8I$, and congruence gives
$\sum_iU_i\otimes U_i\preceq8A_t\otimes A_t$.
The product rule for $K=K_j$ now bounds its drift by
$(-j+8\binom j2)K=(4j^2-5j)K$. Indeed each slot contributes $-K$ and each
unordered pair contributes once its product of noise coefficients. The normalized
noise on the $i$th Brownian coordinate is
$V_i=K^{-1/2}(dK/d\beta_i)K^{-1/2}=\sum_{r=1}^jS_i^{(r)}$.
For a vector $v$, $|\sum_rS_i^{(r)}v|^2\le j\sum_r|S_i^{(r)}v|^2$, so
$\sum_iV_i^2\preceq8j^2I$.

Write $dh_j=\sum_ic_i d\beta_i$, where
$c_i=\mathbb E_t[(D^jf-h_j)\xi_i]$. The functions $\xi_i$ are orthonormal in
$L^2(\mu_t)$. Bessel's inequality applied after the deterministic-at-time-$t$
linear map $K^{1/2}$ yields

$$
Q:=\sum_i\langle c_i,Kc_i\rangle
\le\mathbb E_t\langle D^jf-h_j,K(D^jf-h_j)\rangle.
$$

The entire drift of $\langle h_j,Kh_j\rangle$ is at most

$$
(4j^2-5j)\langle h_j,Kh_j\rangle+Q
+2\sum_i\langle K^{1/2}h_j,V_iK^{1/2}c_i\rangle.
$$

Cauchy–Schwarz over $i$, followed by $2ab\le a^2+b^2$, bounds the last term by
$\langle h_j,Kh_j\rangle+8j^2Q$. Consequently its expected drift is bounded by
$(4j^2-5j+1)N_j+(1+8j^2)L_j$, which implies the assertion.

All preceding identities initially hold with compact parameter stops. They pass to
expectations without a residual local-martingale term: on fixed spatial support the
derivatives of $f$, $h_j$ and $A_t$ are uniformly bounded; the Bessel bound controls
$K^{1/2}c_i$ in square sum, and the bound for $V_i$ controls all normalized metric
noise. These bounds also bound the actual scalar stochastic integrand in square sum,
since $K^{1/2}h_j$ is bounded. The drifts are absolutely bounded by the same
arguments (use absolute values for each pair term). Global existence and dominated
convergence remove the stops and give local absolute continuity of $N_j$.
:::

## Closing the polynomial induction

:::{prf:proof} Proof of the polynomial theorem
For degree one isotropy gives $\operatorname{Var}(T\cdot X)=|T|^2$.
Induct on $d\ge2$, first for compactly supported isotropic laws. Each whitened
posterior is again in that class. Applying the already established Appell inequality
through degree $d-j$ to the Hilbert-valued polynomial

$$
y\longmapsto(A_t^{1/2})^{\otimes j}D^jf(m_t+A_t^{1/2}y)
$$

and then using the triangle inequality in the localization probability space gives

$$
\sqrt{L_j(t)}\le\sum_{k=1}^{d-j}32^k k!\sqrt{N_{j+k}(t)}
\quad(1\le j<d).
$$

The new $k$ derivative slots supply the extra $A_t^{1/2}$ factors. This explains
exactly why the right metric is $A_t^{\otimes(j+k)}$ and why no output dimension
appears.

Take $f=P_d^{\mu_0}[T]$. The zero tensor case is trivial; otherwise set

$$
Q=(d!)^2\|T\|_{\mathrm{HS}}^2,\quad
w_j=1024^{d-j}((d-j)!)^2,\quad
M(t)=\max_{1\le j\le d}\frac{N_j(t)}{Qw_j}.
$$

Initially the lower derivative means vanish, while $N_d(0)=Q$, so $M(0)=1$.
Writing $s=d-j\ge1$, cancellation of the powers of $32$ gives

$$
\frac{\sqrt{L_j(t)}}{\sqrt{Qw_j}}
\le\sqrt{M(t)}\sum_{k=1}^s\binom sk^{-1}\le2\sqrt{M(t)}.
$$

For $s=1$ the sum is one; for $s\ge2$ its first $s-1$ terms are at most $1/s$
and its last is one. Also $L_d=0$. The hierarchy lemma therefore gives

$$
\frac{N_j(t)}{Qw_j}\le\frac{N_j(0)}{Qw_j}
+40d^2\int_0^tM(u)du.
$$

Taking the maximum and applying the scalar integral Gronwall inequality shows
$M(t)\le e^{40d^2t}$. In particular, for $r=\nabla f$,

$$
G_1(t):=\mathbb E_{\mathrm{loc}}\mathbb E_t[r^TA_tr]
=N_1(t)+L_1(t)
\le5(d!)^2\|T\|^2 1024^{d-1}((d-1)!)^2e^{40d^2t}.
$$

The martingale identities for $f$ and $f^2$ give
$V'(t)=-\mathbb E_{\mathrm{loc}}|\operatorname{Cov}_t(f,\xi_t)|^2\ge-V(t)$,
where $V(t)=\mathbb E_{\mathrm{loc}}\operatorname{Var}_t f$ and the inequality
is Bessel's. Hence $V(\tau)\ge e^{-\tau}\operatorname{Var}_{\mu_0}f$.

The matrix strong-convexity Poincaré inequality gives
$\operatorname{Var}_{\mu_\tau}f\le\mathbb E_\tau[r^T\Lambda_\tau^{-1}r]$.
Here we use the established Brascamp–Lieb inequality [@BrascampLieb1976]; its smooth
matrix form is also stated in [@BakryGentilLedoux2014, Theorem 4.9.1]. We use its
constant-curvature form: if the potential is $V+x^TBx/2$, $V$ extended-valued convex
and $B\succ0$, then $\operatorname{Var}q\le\mathbb E\nabla q^TB^{-1}\nabla q$.
Its applicability to nonsmooth convex supports can also be obtained by replacing $V$
by smooth convex approximations increasing to it (Moreau envelopes followed by
mollification), applying the smooth inequality, and passing compact smooth tests to
the limit; truncation and spatial cutoff extend it to finite-energy locally Lipschitz
tests. A supporting affine lower bound for $V$ supplies Gaussian domination under
the fixed positive quadratic term in this approximation.

For any $v$, expansion of the square yields the exact identity

$$
\int_0^\tau v^TA_sv\,ds-\tau^2v^T\Lambda_\tau^{-1}v
=\int_0^\tau|A_s^{1/2}v-\tau A_s^{-1/2}\Lambda_\tau^{-1}v|^2ds.
$$

Thus $\Lambda_\tau^{-1}\preceq\tau^{-2}\int_0^\tau A_sds$.
For fixed $s\le\tau$, the entries of $A_s$ are $\mathcal F_s$-measurable and
$\mathbb E_t(r_ir_j)$ is a true martingale, so

$$
\mathbb E_{\mathrm{loc}}\mathbb E_\tau[r^TA_sr]
=\mathbb E_{\mathrm{loc}}\mathbb E_s[r^TA_sr]=G_1(s).
$$

All tests are bounded on the fixed support; Fubini is legitimate. Combining these
facts proves

$$
\operatorname{Var}_{\mu_0}f\le\frac{e^\tau}{\tau^2}\int_0^\tau G_1(s)ds.
$$

Take $\tau=(40d^2)^{-1}$. Since $d\ge2$, $e^{1+\tau}<3$, and bounding the
integral by its interval length times its maximum gives

$$
\operatorname{Var}_{\mu_0}f
\le600d^2\cdot1024^{d-1}((d-1)!)^2(d!)^2\|T\|^2
\le1024^d(d!)^4\|T\|^2.
$$

This completes the induction for compact support. For arbitrary isotropic log-concave
$\mu$, condition on growing centered Euclidean balls, then center and whiten.
All polynomial moments of a finite-dimensional log-concave law are finite; hence all
conditional moments through order $2d$ converge. Conditional means tend to zero and
covariances to $I$, so the affine normalizations tend to the identity. The coefficients
of each Appell polynomial are polynomial expressions in moments up to degree $d$
(obtain the inverse generating series recursively). Their variances therefore converge
using moments up to degree $2d$. This passes the same coefficient bound to $\mu$.
The exact Appell expansion proves the stated derivative-mean inequality.

Finally let a centered law have covariance $0\preceq\Sigma\preceq I$. On its linear
support choose an isometric embedding $J:\mathbb R^m\to\mathbb R^n$ and positive
covariance $B\preceq I_m$, so $X=JB^{1/2}Y$ with $Y$ isotropic. The formal
identity gives
$P_k^\mu[T](JB^{1/2}y)=P_k^{\mathcal L(Y)}[((JB^{1/2})^T)^{\otimes k}T](y)$.
The tensor map has norm at most one, proving the coefficient bound. The exact
Appell expansion, valid for singular laws as a formal identity, proves the polynomial
bound too. Rank zero means a point mass and both variances vanish.
:::

## Analytic foundations for the curvature comparison

The following two lemmas record the precise analytic claims of
[](#lem:sz-analytic-foundations). They are included here so that applying polynomial
testing to inverse operators does not leave an implicit domain assumption.

:::{prf:lemma} Operator domain, Bochner identity and spectral gap
:label: lem:sol-sz-operator
Let $\mu(dx)=e^{-W(x)}dx$ be a probability with $W$ smooth and
$0<aI\preceq D^2W\preceq bI<\infty$. The nonnegative self-adjoint operator
$H=-\Delta+\nabla W\cdot\nabla$ associated with the closed Dirichlet form has
form domain $H^1(\mu)=\{g\in L^2(\mu):\nabla g\in L^2(\mu)\}$, constants as
kernel, and $C_c^\infty$ as graph core. For every $g\in\operatorname{Dom}H$,
$D^2g\in L^2(\mu)$, its mixed weak derivatives commute, and

$$
\|Hg\|_2^2=\mathbb E\|D^2g\|_{\mathrm{HS}}^2+
\mathbb E\langle\nabla g,D^2W\nabla g\rangle.
$$

In particular each $\partial_i g$ belongs to the form domain. Polynomials belong to
that domain, and $\langle\phi,Hg\rangle=\mathbb E\nabla\phi\cdot\nabla g$
for every form-domain $\phi$.
The resolvent is compact. The smallest positive eigenvalue is
$\lambda=C_P(\mu)^{-1}>0$, with a real normalized centered eigenfunction.
On the centered subspace $H^{-1/2}$ is bounded. If centered
$h\in\operatorname{Dom}H^{1/2}$ and $g=H^{-1/2}h$, then
$g\in\operatorname{Dom}H$, $\|Hg\|_2^2=\|H^{1/2}h\|_2^2$ and
$\|\nabla g\|_2^2=\|h\|_2^2$.
:::

:::{prf:proof}
Choose smooth cutoffs $\chi_R$ equal to one on the radius-$R$ ball, zero beyond
radius $2R$, with derivative bounds $C/R,C/R^2$. They approximate every weighted
Sobolev function in the form norm: the extra gradient term has norm at most
$C\|g\|_2/R$, and the other terms tend to zero by integrability. On compact sets
the positive smooth density is bounded above and below, so ordinary mollification
proves density and identifies the form domain. The same cutoff approximates the
constant one; a zero weak gradient on connected $\mathbb R^n$ gives a constant,
identifying the kernel.

For $g\in\operatorname{Dom}H$ the weak equation and interior elliptic regularity
give $g\in H^2_{\mathrm{loc}}$. The product rule reads

$$
H(\chi_Rg)=\chi_RHg-2\nabla\chi_R\cdot\nabla g+gH\chi_R.
$$

Since $|\nabla W(x)|\le|\nabla W(0)|+b|x|$, the functions $H\chi_R$ are
uniformly bounded for $R\ge1$ and supported in the cutoff annuli. Every displayed
term belongs to $L^2(\mu)$, so the weak operator characterization puts $\chi_Rg$
in its domain. The last two terms tend to zero in $L^2$, proving graph convergence.
Mollification on a fixed compact neighborhood of each support converges in $H^2$;
bounded coefficients there give graph convergence. This proves the graph-core claim.
Subtracting means gives the centered graph core as well.

For a compact smooth function differentiate
$\partial_iHg=H\partial_i g+\sum_jW_{ij}\partial_jg$ and integrate by parts to
obtain the Bochner identity. For differences $u$ of graph-core approximants,
$\|\nabla u\|_2^2=\langle u,Hu\rangle\le\|u\|_2\|Hu\|_2$.
The gradients are Cauchy, and Bochner with $D^2W\succeq0$ makes their Hessians
Cauchy. Their limits are distributional derivatives of $g$. Boundedness of $D^2W$
passes the curvature term to the limit. Mixed weak derivatives commute, and the
form-domain characterization applies to $\partial_i g$. The testing formula is the
definition of the associated operator. Strong convexity gives Gaussian tails, so
polynomials and their gradients lie in $L^2$.

The unitary map $g\mapsto e^{-W/2}g$ conjugates $H$ to the Friedrichs operator
$-\Delta+V$, where $V=|\nabla W|^2/4-\Delta W/2$, first on its graph core and
then by closure. If $x_*$ minimizes $W$, strong monotonicity gives
$|\nabla W(x)|\ge a|x-x_*|$, while $\Delta W\le nb$. Consequently
$V\ge a^2|x-x_*|^2/4-nb/2$. After adding $nb/2+1$, the form norm controls
$\|u\|_2$, $\|\nabla u\|_2$, and $\||x-x_*|u\|_2$. Rellich compactness on
balls and the uniform tail bound
$\int_{|x-x_*|>R}|u|^2\le R^{-2}\||x-x_*|u\|_2^2$ imply compact embedding
of the form domain in $L^2$. Thus the resolvent is compact.

The kernel is one dimensional, so its first positive eigenvalue $\lambda$ exists.
The Rayleigh inequality and the truncation argument in the next lemma identify its
reciprocal with the Poincaré constant for all locally Lipschitz finite-energy tests.
The reverse inequality follows by approximating a first eigenfunction in form norm
by compact smooth functions. Real coefficients allow a real eigenfunction.
On the centered spectral subspace the spectrum lies in $[\lambda,\infty)$.
Spectral calculus gives $Hg=H^{1/2}h$, $H^{1/2}g=h$, and all remaining claims.
:::

:::{prf:lemma} Regular approximation and scalar Poincaré stability
:label: lem:sol-sz-approximation
Every isotropic log-concave probability on $\mathbb R^n$ is a weak limit of isotropic
regular probabilities satisfying the hypotheses of the preceding lemma, with bounds
$a_j,b_j$ allowed to vary. If probabilities $\nu_j\Rightarrow\nu$ have a common
Poincaré bound $K<\infty$ on $C_c^\infty$ and $\nu$ is absolutely continuous,
then every locally Lipschitz $q$ of finite $\nu$-Dirichlet energy belongs to
$L^2(\nu)$ and $\operatorname{Var}_\nu q\le K\mathbb E_\nu|\nabla q|^2$.
:::

:::{prf:proof}
For the stability assertion first pass each compact smooth test by weak convergence,
since its square and squared gradient are bounded continuous. For locally Lipschitz
$q$ truncate its values to $q_M=\max(-M,\min(q,M))$. Then
$|\nabla q_M|\le|\nabla q|$ almost everywhere. Multiply by $\chi_R$ from the
preceding proof. For fixed $M,R$ the product is a compactly supported Lipschitz
function, so mollifications and their gradients converge Lebesgue almost everywhere,
are uniformly bounded, and live in a common compact set. Absolute continuity and
dominated convergence pass the inequality to $\chi_Rq_M$. As $R\to\infty$,
its value converges in $L^2$ to $q_M$ and its gradient to $\nabla q_M$, since the
cutoff error is bounded by $CM/R$. Thus
$\operatorname{Var}_\nu q_M\le K\mathbb E_\nu|\nabla q|^2$.
With independent $X,X'$ of law $\nu$, Fatou gives

$$
\frac12\mathbb E(q(X)-q(X'))^2\le K\mathbb E_\nu|\nabla q|^2.
$$

Fubini gives some $y$ with $\int(q(x)-q(y))^2\nu(dx)<\infty$; since $q(y)$ is
finite this implies $q\in L^2(\nu)$. The independent-copy expression is then its
variance, proving stability without assuming square integrability in advance.

For approximation let $Y_\delta=X+\sqrt\delta Z$ with $Z$ standard Gaussian
independent of the isotropic log-concave $X$. Its smooth positive log-concave density
$e^{-V_\delta}$ satisfies

$$
D^2V_\delta(y)=\delta^{-1}I-\delta^{-2}
\operatorname{Cov}(X\mid Y_\delta=y),\qquad
0\preceq D^2V_\delta\preceq\delta^{-1}I.
$$

Differentiate the Gaussian kernel twice; Gaussian damping justifies differentiation
locally uniformly in $y$. The lower bound follows from preserved log-concavity and
the upper bound from positivity of the conditional covariance.
Multiply this density by $e^{-\epsilon|y|^2/2}$ and normalize. Its Hessian lies
between $\epsilon I$ and $(\delta^{-1}+\epsilon)I$.
For fixed $\delta$, dominated convergence as $\epsilon\downarrow0$ gives total
variation convergence and convergence of its first and second moments to those of
$Y_\delta$. Choose $\delta_j\downarrow0$ and then $\epsilon_j\downarrow0$
so that these errors tend to zero. The resulting laws converge weakly to $\mu$,
with means $m_j\to0$ and covariances $A_j\to I$.
The laws of $A_j^{-1/2}(Y-m_j)$ are isotropic and still regular: their Hessians
are congruent by $A_j^{1/2}$ to those just constructed. The transformations tend to
the identity uniformly on compact sets, so tightness proves the asserted weak
convergence. No uniform lower curvature bound is asserted.
:::

**Source mapping.** The formal Appell identity is source Section 2.3. The global SDE,
its logarithmic determinant, and the tensor hierarchy reconstruct source Lemmas 4.2
and 4.3; the coefficient induction reconstructs Theorem 4.1. The two analytic lemmas
reconstruct Section 3, separating moment convergence for polynomials from weak scalar
Poincaré stability. Standard finite-dimensional SDE existence, Itô calculus, interior
elliptic regularity, Rellich compactness and spectral calculus are the classical tools
used here. The only nonclassical mathematical dependency is [](#thm:letwin-qcts).

**Fences respected.** The new nodes have no proposed `bounded_by` edges. The
projection-only ceiling [](#rem:projection-ceiling) is respected by using all tensor
slots. The two-tail boundary [](#rem:two-tail-slice-bounds) is untouched: the conclusion
is an intrinsic polynomial estimate, not a bound on an unwhitened cut source.
The occupation and bootstrap boundaries [](#rem:relative-ceiling),
[](#rem:crude-insufficient), and [](#rem:profile-circularity) are untouched; no
universal-time occupation or moving-competitor estimate is claimed. Growing
factorials prevent treating this polynomial theorem alone as a dimension-free
Poincaré inequality. No comparison between members of the trace-upgrade cluster is
asserted. There are no open antecedents or unclosed mathematical steps claimed in
this dossier; its independent examination is a separate task.
