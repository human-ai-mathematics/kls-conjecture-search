---
title: 'BK: compatible-tensor Hodge estimates and domains'
ledger-node: lem:bk-compatible-hodge
numbering:
  enumerator: "151.%s"
---

*Part of the Balasubramanian–Kasiviswanathan proof, Chapter [](#sec:bk-proof); the reading order is on the [full proofs](#sec:proofs-bk) page.*

**Overview.** We reconstruct Lemma 3.1 and Appendices A–B of
[@BalasubramanianKasiviswanathan2026KLS], at Git commit
`4837c33649ba2271f43c9684e9350ecbdd725f95`. The first part proves existence of
centered primitives and an adjoint graph core. The second bounds the loss from
projecting weighted divergence onto compatible tensors. Its finite-dimensional
Schur complement retains precisely the curvature lower bound at every rank.

**Dependencies.** We use [](#def:bk-compatible-calculus), the ordinary scalar
Bakry–Émery inequality $C_P(\mu)\le a^{-1}$
[@BakryGentilLedoux2014], distribution theory, elementary Fourier Sobolev
regularity, and closed-form operator representation. The finite-energy extension
of scalar Poincaré is proved below. Neither KLS, BKL, Song–Zhang v2, a uniform
Appell bound nor any assertion proved later in the BK argument is used.

:::{prf:theorem} Raw derivatives and the uniform Hodge estimate
:label: thm:sol-bk-compatible-hodge
Let $\mu(dx)=Z^{-1}e^{-V(x)}dx$ be centered on $\mathbb R^n$, with
$V\in C^\infty$ and $0<aI\preceq D^2V\preceq a_+I$. Use the spaces and
operators of [](#def:bk-compatible-calculus). For every integer $r\ge0$,
$D_r$ is closed, densely defined and bijective, with
$\|D_r^{-1}\|\le\sqrt{C_P(\mu)}$. The space
$\mathcal K_{r+1}=\{\nabla^{r+1}\psi:\psi\in C_c^\infty\}$ is a graph
core for $D_r^*$. For every $F\in\operatorname{Dom}(D_r^*)$,
$F\in W^{1,2}(\mu;E_{r+1})$ and
$$
 \|D_r^*F\|_2^2\ge\|\nabla F\|_2^2+a\|F\|_2^2.
$$
In particular, the constant is independent of both dimension and rank.
This includes [](#lem:bk-compatible-hodge).
:::

:::{prf:proof}
Write $p=C_P(\mu)<\infty$, $K=D^2V$, and $w=Z^{-1}e^{-V}$.
All tensor norms sum over ordered indices; exterior norms sum over increasing
indices. Distributional derivatives are meaningful because the weight is
positive and smooth and weighted $L^2$ convergence implies local distributional
convergence.

**Finite-energy primitives.** First, if $h\in W^{1,2}_{\rm loc}$ and
$\nabla h\in L^2(\mu)$, then $h\in L^2(\mu)$ and
$\operatorname{Var}_\mu h\le p\|\nabla h\|_2^2$. Here is the extension
argument, which avoids assuming the desired integrability. The scalar inequality
extends to compactly supported Sobolev functions by mollification on compact
sets. For bounded locally Sobolev $h$, multiply by a smooth cutoff $\chi_R$
with $|\nabla\chi_R|\le C/R$; both function and gradient converge in weighted
$L^2$. Thus the inequality holds for bounded finite-energy functions. Apply it
to $h_N=\max(-N,\min(h,N))$. Their variances are uniformly bounded by
$E=p\|\nabla h\|_2^2$. Choose $M$ such that
$A=\{|h|\le M\}$ has positive measure. For $N\ge M$ and
$m_N=\mathbb Eh_N$,
$$
 \mu(A)(|m_N|-M)_+^2\le\operatorname{Var}(h_N)\le E.
$$
The means and hence $\|h_N\|_2$ are bounded. Fatou gives $h\in L^2$;
then $h_N\to h$ in $L^2$ proves the asserted variance inequality.

A locally square-integrable curl-free vector field has a global locally
$W^{1,2}$ primitive on $\mathbb R^n$. Explicitly, mollify it, integrate the
resulting smooth field along the segment from zero to $x$, and subtract its
Lebesgue mean on the unit ball. On each larger ball the gradient converges in
$L^2$; the ordinary Poincaré inequality together with the fixed mean controls
the additive constant. These primitives converge locally in $W^{1,2}$.
For $F\in C_{r+1}$ do this for each vector $(F_{iI})_i$ and center the
primitive using the finite-energy result. Denote it by $U_I$. Permuting $I$
preserves its gradient, so uniqueness of a centered primitive makes $U$
symmetric. Moreover $\partial_iU_{jI}=F_{ijI}=\partial_jU_{iI}$, so $U$ is
compatible. Summing the scalar inequalities yields
$$
 \nabla U=F,\qquad \mathbb EU=0,\qquad \|U\|_2^2\le p\|F\|_2^2.
$$
Uniqueness follows from vanishing gradient and centering.

**Potential cores.** Repeated primitive construction writes every $F\in C_r$
as $F=\nabla^r\phi$ with $\phi\in W^{r,2}(\mu)$; if additionally
$F\in W^{1,2}$, then $\phi\in W^{r+1,2}$. Let $\chi_R$ be compactly
supported, equal to one on $B_R$, with
$|\nabla^j\chi_R|\le C_jR^{-j}$. The product rule gives
$\chi_R\phi\to\phi$ in every indicated weighted Sobolev norm: the terms
with cutoff derivatives are bounded by $C_jR^{-j}$ times lower derivative
norms and the term without cutoff derivatives converges by dominated
convergence. Mollification at fixed compact support is valid since $w,w^{-1}$
are bounded there. A diagonal sequence proves that $\mathcal K_r$ is dense
in $C_r$ and is a graph core for its maximal ordinary derivative. Subtracting
expectations proves the centered versions in $G_r$. These assertions also hold
at $r=0$ by the direct cutoff argument. Closedness of the distributional
derivative now proves that $D_r$ is closed and densely defined. The primitive
construction makes it bijective with the asserted bounded inverse.

**One missing weak derivative.** We need the following fact for the adjoint
core. Suppose $q\ge1$, $\phi\in W^{q-1,2}(\mu)$ and
$G\in L^2(\mu;(\mathbb R^n)^{\otimes q})$ satisfy
$$
 \int\langle\nabla^q\phi,\nabla^q\psi\rangle\,d\mu
 =\int\langle G,\nabla^q\psi\rangle\,d\mu
 \quad(\psi\in C_c^\infty),                                      \tag{1}
$$
where the left side is a distributional pairing. Then
$\phi\in W^{q,2}(\mu)$. Indeed the distributional equation is
$\sum_I\partial_I(w\partial_I\phi)=\sum_I\partial_I(wG_I)$.
After expanding derivatives of $w$, the leading part is $w\Delta^q\phi$;
the other terms have order at most $2q-1$ on $\phi$. Thus
$\Delta^q\phi\in H^{-q}_{\rm loc}$. For a compact smooth $\zeta$,
$\Delta^q(\zeta\phi)\in H^{-q}$ because the commutator has order
$2q-1$, and $\zeta\phi\in H^{q-1}$. In Fourier variables the high
frequencies satisfy
$$
 \frac{|\xi|^{4q}}{(1+|\xi|^2)^q}\asymp(1+|\xi|^2)^q
 \quad(|\xi|\ge1),
$$
while the $H^{q-1}$ norm controls the low frequencies. Hence
$\phi\in H^q_{\rm loc}$.

Choose $0\le\eta\le1$ compactly supported, equal to one near zero, and
$\eta_R(x)=\eta(x/R)$. Local regularity permits the Sobolev test
$\psi=\eta_R^{2q}\phi$ in (1). The product rule gives
$$
 \nabla^q(\eta_R^{2q}\phi)=\eta_R^{2q}\nabla^q\phi+R_R,
 \qquad |R_R|\le C_q\eta_R^q\sum_{j=1}^qR^{-j}|\nabla^{q-j}\phi|.
$$
For the power of $\eta_R$, regard $\eta_R^{2q}$ as a product of $2q$
factors: at least $q$ remain undifferentiated in every remainder term.
Set $A_R=\|\eta_R^q\nabla^q\phi\|_2$ and
$b_R=C_q\sum_{j=1}^qR^{-j}\|\nabla^{q-j}\phi\|_2$.
Both $\|R_R\|_2$ and $\|R_R/\eta_R^q\|_2$ are at most $b_R$,
with zero quotient where $\eta_R=0$. Equation (1) yields
$$
 A_R^2\le A_R(\|G\|_2+b_R)+\|G\|_2b_R,
 \qquad A_R\le\|G\|_2+2b_R.
$$
Since $b_R\to0$, Fatou supplies the missing global derivative.

**The adjoint graph core.** On $\mathcal K_{r+1}$ define
$S_rF=P_{G_r}\operatorname{div}_VF$, where
$(\operatorname{div}_VF)_I=\sum_j(-\partial_j+V_j)F_{Ij}$.
Integration by parts gives $S_r\subset D_r^*$, hence closability; its domain
is dense by the potential-core argument. We show $S_r^*=D_r$.
The forward inclusion $D_r\subset S_r^*$ is integration by parts. If
$u\in\operatorname{Dom}(S_r^*)$ with $g=S_r^*u$, write
$u=\nabla^r\phi$ with $\phi\in W^{r,2}$ (and $\phi=u$ if $r=0$).
The adjoint equation tested against $\nabla^{r+1}\psi$ is exactly (1)
with $q=r+1$ and $G=g$. Thus $\nabla u\in L^2$ and $u\in\operatorname{Dom}(D_r)$.
Density of $\mathcal K_{r+1}$ identifies $D_ru=g$. Taking adjoints proves
$\overline S_r=D_r^*$. This proves graph approximation of the adjoint,
not merely norm approximation of its domain.

**Weighted divergence and projection loss.** It remains to prove the estimate
on this core. Fix $m\ge0$ and $F=\nabla^{m+1}\psi$ with compact smooth
$\psi$, and put $Y=\operatorname{div}_VF$. Integration by parts gives
$\mathbb EY=0$ and
$D_m^*F=P_{G_m}Y=P_{C_m}Y$. Since $[\partial_i,\partial_j^*]=V_{ij}$
and $\nabla F$ is fully symmetric, two integrations by parts give
$$
 \|P_{C_m}Y\|_2^2=\|\nabla F\|_2^2+B_K(F)-\|(I-P_{C_m})Y\|_2^2,
 \quad B_K(F)=\mathbb E\sum_{I,i,j}V_{ij}F_{Ii}F_{Ij}.             \tag{2}
$$
If $m=0$, $C_0=L^2$ and there is no projection loss; $B_K(F)\ge a\|F\|_2^2$
finishes this case. Henceforth $m\ge1$. Differentiation and compatibility
cancel all derivatives of $F$ in the curl of $Y$:
$$
 \partial_kY_{lI}-\partial_lY_{kI}
 =\sum_j(V_{kj}F_{lIj}-V_{lj}F_{kIj}),\qquad |I|=m-1.           \tag{3}
$$

**A constrained complex with all domains specified.** On normalized symmetric
basis vectors $e_\alpha$ define
$a_ie_\alpha=\sqrt{\alpha_i}e_{\alpha-e_i}$ and
$a_i^*e_\alpha=\sqrt{\alpha_i+1}e_{\alpha+e_i}$.
Contraction in one slot of a rank-$q$ tensor is $a_i/\sqrt q$.
Let $\varepsilon_i$ be exterior multiplication and $\iota_i$ its adjoint.
They satisfy $[a_i,a_j^*]=\delta_{ij}$ and
$\iota_j\varepsilon_i+\varepsilon_i\iota_j=\delta_{ij}$.
Define $b=\sum_i a_i\varepsilon_i$ on the entire symmetric/exterior algebra.
It obeys $b^2=0$ and, at bidegree $(q,p)$,
$$bb^*+b^*b=(q+p)I.$$
Indeed the mixed terms cancel after commuting the two sorts of operators;
the terms remaining are the symmetric and exterior number operators.
Fix $q=m-1$, set $\mathscr E_p=\ker b\subset\operatorname{Sym}^{m-1}\otimes\Lambda^p$
for $p\ge1$, and let $P_p=bb^*/(m+p-1)$ be its orthogonal projection.
The map $I_mT=bT/\sqrt m$ is an isometry of $E_m$ onto $\mathscr E_1$:
$b^*b=mI$ on $E_m$, and $bb^*=mI$ on $\mathscr E_1$ proves surjectivity.

Let $d=\sum_i\varepsilon_i\partial_i$ and give
$d_p:L^2(\mu;\mathscr E_p)\to L^2(\mu;\mathscr E_{p+1})$ its maximal
 distributional domain. The identity $bd+db=0$ preserves the constraint;
$d_{p+1}d_p=0$ including its domain inclusion. These operators are closed
and densely defined. Their adjoints are the maximal expressions
$d_p^*=P_pd^*$, $d^*=\sum_i\iota_i(-\partial_i+V_i)$.
Here are the domain details. Cutoff commutators with these first-order
expressions are bounded pointwise by $C|\nabla\chi_R||\omega|$ and converge
to zero in $L^2$. On fixed compact supports convolution commutes with all
constant derivative coefficients and fiber projections. The only coefficient
commutator is
$$
 V_i(x)(\omega*\rho_\epsilon)(x)-(V_i\omega)*\rho_\epsilon(x)
 =\int\rho_\epsilon(y)[V_i(x)-V_i(x-y)]\omega(x-y)\,dy.
$$
Its local $L^2$ norm is at most $C\epsilon\|\omega\|_{L^2(dx)}$ by
local Lipschitz continuity and Young's inequality. Equivalence of weights on
compact sets proves convergence in weighted $L^2$. Consequently compact
smooth sections are simultaneous graph cores for each needed maximal
expression, in particular $d_2$ and $d_1^*$. Testing against compact sections
first characterizes the Hilbert adjoint distributionally; this graph
approximation extends integration by parts to the maximal domains and proves
the converse inclusion. Finally $I_mC_m=\ker d_1$, since these kernel
equations are precisely the compatibility equations.

**The Laplacian curvature estimate.** On $L^2(\mu;\mathscr E_2)$ let
$\mathcal L$ represent the closed densely defined form
$$\ell(\omega)=\|d_2\omega\|_2^2+\|d_1^*\omega\|_2^2,$$
with form domain $\operatorname{Dom}(d_2)\cap\operatorname{Dom}(d_1^*)$.
Initially take compact smooth $\omega$. Set
$$K_{\rm fer}=\sum_{i,j}V_{ij}\varepsilon_i\iota_j,
\quad K_{\rm bos}=\sum_{i,j}V_{ij}a_j^*a_i,
\quad c=\sum_i a_i\partial_i^*.$$
The ordinary weighted Weitzenböck identity, obtained by expanding $dd^*+d^*d$,
is
$\|d\omega\|_2^2+\|d^*\omega\|_2^2
=\|\nabla\omega\|_2^2+\mathbb E\langle\omega,K_{\rm fer}\omega\rangle$.
Since $I-P_1=b^*b/m$ and $bd^*+d^*b=c$, one obtains
$$\ell(\omega)=\|\nabla\omega\|_2^2+
\mathbb E\langle\omega,K_{\rm fer}\omega\rangle-m^{-1}\|c\omega\|_2^2.$$
Moreover $[c,c^*]=H-K_{\rm bos}$, where
$H=\sum_i\partial_i^*\partial_i$ acts componentwise. The row map
$(a_i^*)_i$ from copies of degree $m-1$ to degree $m$ has norm $\sqrt m$,
as its product with its adjoint is $\sum_i a_i^*a_i=mI$. Therefore
$$
 \|c\omega\|_2^2=\|c^*\omega\|_2^2-\|\nabla\omega\|_2^2
 +\mathbb E\langle\omega,K_{\rm bos}\omega\rangle
 \le(m-1)\|\nabla\omega\|_2^2+
 \mathbb E\langle\omega,K_{\rm bos}\omega\rangle.
$$
It follows that
$$
 \ell(\omega)\ge m^{-1}\|\nabla\omega\|_2^2+
 \mathbb E\langle\omega,Q_m(K)\omega\rangle,
 \qquad Q_m(K)=P_2(K_{\rm fer}-m^{-1}K_{\rm bos})P_2.             \tag{4}
$$

**Exact curvature blocks.** Diagonalize $K$ pointwise, with eigenvalues
$\kappa_i\ge a$. All calculations here are orthogonally invariant and use
no derivatives of this diagonalizing basis. Put $N=m+1$. The combined
multiplicity $\alpha$ of symmetric and exterior indices has $|\alpha|=N$.
In each block restrict coordinates to $S_\alpha=\{i:\alpha_i>0\}$,
write $r_i=\sqrt{\alpha_i}$ and $S=\sum_i\alpha_i\kappa_i$.
Then $|r|^2=N$, and $b$ is exterior multiplication by $r$. Thus the constrained
two-forms are exactly $\omega=r\wedge v$, $v\perp r$, with
$\|\omega\|^2=N|v|^2$. This also follows from
$\iota_r(r\wedge\omega)+r\wedge\iota_r\omega=N\omega$.
If the coordinate support has one element, the two-form space is zero;
all formulas below have their zero-space meanings.

On the exterior pair $ij$, $K_{\rm fer}-m^{-1}K_{\rm bos}$ has coefficient
$[N(\kappa_i+\kappa_j)-S]/m$. Expanding squares, and using $r\cdot v=0$,
gives
$$
 \sum_{i<j}(\kappa_i+\kappa_j)(r_iv_j-r_jv_i)^2
 =S|v|^2+N\langle v,Kv\rangle.
$$
Consequently
$$
 \langle r\wedge v,Q_m(K)(r\wedge v)\rangle
 =\frac{N^2}{m}\langle v,Kv\rangle.                           \tag{5}
$$
In particular $Q_m(K)\succeq(N/m)aI$. If $P$ projects onto $r^\perp$,
the isometry $Uv=(r/\sqrt N)\wedge v$ satisfies
$U^*Q_m(K)U=(N/m)(PKP)|_{r^\perp}$.
The Hessian upper bound makes $Q_m(K)$ a bounded multiplication operator
for each fixed rank. The joint graph core therefore extends (4) to the full
form domain: apply it to differences, use positivity from (5) to control
the ordinary gradients, and pass to the limit in the bounded curvature term.
In particular $\mathcal L\succeq Q_m(K)\succeq(N/m)aI$.

The curl $t=d_1I_mY$ in the block under consideration is, by (3),
$$
 t_{ij}=\frac{(\kappa_i-\kappa_j)\sqrt{\alpha_i\alpha_j}}{\sqrt{Nm}}F_\alpha,
 \qquad t=-\frac{F_\alpha}{\sqrt m}U(PKr).                    \tag{6}
$$
The denominator comes from two successive single-slot contractions,
$a_j/\sqrt N$ and $a_i/\sqrt m$; no tensor multiplicity is suppressed.
Equations (5)–(6) give
$$
 \langle t,Q_m(K)^{-1}t\rangle
 =\frac{|F_\alpha|^2}{N}
 \langle PKr,((PKP)|_{r^\perp})^{-1}PKr\rangle.                \tag{7}
$$
The contribution of this symmetric tensor component to $B_K$ is
$(S/N)|F_\alpha|^2$. Completing the square gives
$$
 S-\langle PKr,((PKP)|_{r^\perp})^{-1}PKr\rangle
 =\min_{w\perp r}\langle r+w,K(r+w)\rangle\ge aN.             \tag{8}
$$
Thus the inverse-curvature cost is at most $(S/N-a)|F_\alpha|^2$.
This exact cancellation, rather than an estimate on $\|K\|$, is the
rank-uniform part of the proof.

**Projection identity.** For clarity we justify the operator identity used to
convert (7) into a projection bound. Let $A:X_1\to X_2$, $B:X_2\to X_3$
be closed densely defined with $BA=0$ including domains. Suppose the closed
form $\|A^*z\|^2+\|Bz\|^2$ represents $\mathcal L\succeq cI$, $c>0$.
Then, for $u\in\operatorname{Dom}(A)$,
$$\|(I-P_{\ker A})u\|^2=\langle Au,\mathcal L^{-1}Au\rangle. \tag{9}$$
Indeed $X_2=\ker B\oplus(\ker B)^\perp$ splits the form: the second
summand lies in $\ker A^*$, and the first lies in $\operatorname{Dom}(B)$
with $B=0$. The corresponding projections preserve both domains. For
$z=\mathcal L^{-1}Au$, the weak equation tested against the perpendicular
component forces that component to vanish. Testing against all of
$\operatorname{Dom}(A^*)$ (projecting first onto $\ker B$) proves
$z\in\operatorname{Dom}(AA^*)$ and $AA^*z=Au$. Thus
$A^*z=(I-P_{\ker A})u$, proving (9). If also $\mathcal L\succeq Q\succeq cI$
with bounded $Q$, the form variational formula
$$
 \langle t,\mathcal L^{-1}t\rangle
 =\sup_z\{2\operatorname{Re}\langle t,z\rangle-\ell(z)\}
 \le\sup_z\{2\operatorname{Re}\langle t,z\rangle-\langle z,Qz\rangle\}
 =\langle t,Q^{-1}t\rangle                                  \tag{10}
$$
has its first supremum over the form domain and its second over $X_2$.

Apply (9)–(10) to $A=d_1$, $B=d_2$, $u=I_mY$, and $Q=Q_m(K)$.
The isometry $I_m$ identifies the kernel projection with $P_{C_m}$.
Sum (7)–(8) over blocks, integrate, and substitute in (2). This yields
$\|D_m^*F\|_2^2\ge\|\nabla F\|_2^2+a\|F\|_2^2$ on the potential core.
For general $F\in\operatorname{Dom}(D_m^*)$, the proved graph core gives
$F_k\to F$ and $D_m^*F_k\to D_m^*F$. Apply the core estimate to
$F_k-F_l$ to see $\nabla F_k$ is Cauchy. The closed distributional derivative
then gives $F\in W^{1,2}$ and $\nabla F_k\to\nabla F$. Passing to the
limit proves the theorem, including its domain assertion.
:::

**Hypotheses and limits.** Positive lower curvature supplies only the classical
scalar Poincaré inequality and positivity of the exact curvature blocks. Smooth
positive density supplies local distribution theory and mollification. Bounded
upper curvature makes the curvature multiplication operator bounded in the form
closure; its value never enters the final estimate. Dimension- and rank-dependent
cutoff constants occur only in errors sent to zero at each fixed rank. Centering
fixes constants; no covariance upper bound is needed for this theorem.

**Fences respected.** No `bounded_by` node is assigned to this statement. The
result concerns strictly positively curved regular laws. It proves no CMH,
occupation, trace-upgrade, or curvature-free Poincaré assertion, and uses none as
an input.
