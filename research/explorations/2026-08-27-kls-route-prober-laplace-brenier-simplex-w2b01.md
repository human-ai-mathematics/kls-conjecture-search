---
---
# Laplace--Brenier route probe: the rotation-optimized simplex gate

Date: 2026-08-27

Role: kls-route-prober

Run id: w2b01

## Outcome

The regular-simplex gate remains **unresolved**: no simplex refutation is established, and no
positive dimension-free bound is established either.  The exact rotation-optimized problem is a
new global Monge--Ampere transmission estimate.  Three tests that could have killed the route do
not:

1. the Monge--Ampere determinant forces only a dimension-free lower bound on the Lipschitz
   constant, asymptotic to $e/\sqrt2$;
2. an explicit Helmert rotation places a signed product-Laplace coordinate axis strictly inside
   every vertex normal cone of the regular simplex, providing compatible, correctly oriented
   exponential-tail reservoirs for all $d+1$ vertex caps at the level of the normal-ray test;
3. the cap distances and the matching source-tail distances are both $\Theta(d)$ at mass
   $e^{-\Theta(d)}$, so the elementary cap-packing/concentration comparison does not force a
   growing Lipschitz constant.

The first unjustified step is now exact.  For the Brenier solution, one must control the full
source-coordinate Gram tensor
$$
 \sum_{j=1}^d \partial_{u_j}T(x)\otimes\partial_{u_j}T(x)
 =\bigl(D^2\Phi(x)\bigr)^2
$$
uniformly in $d$ after optimizing the orthonormal source frame $(u_j)$.  Existing
support--curvature maximum principles do not apply: the product-Laplace potential has positive
surface-delta curvature on every source coordinate wall.  Inside each orthant the differentiated
Monge--Ampere equation has a favorable square, but wall transmission, normal-fan behavior at
infinity, and assembly of fixed components into the top eigenvalue remain uncontrolled.  The
first method-level failure is a dimension-free wall-to-bulk Schur/transmission estimate.

The route should therefore **not yet be registered**.  Its pre-registration gate should remain the
exact simplex PDE displayed in Section 9 below.

## 1. Gate, quoted and normalized

This proposal is not yet a live entry of `research/kls/gating.md`.  The orchestrator supplied the
surviving route-scout handoff verbatim as follows:

> Route `laplace-brenier`: use an isotropic product Laplace source and a suitably rotated
> Brenier map to the isotropic log-concave target, with a universal Lipschitz/Hessian control
> sufficient to transfer the source's dimension-free functional inequality; 1D and products
> calibrate positively.  It was proposed as distinct from CMH.  First kill test is the regular
> simplex with rotation/source-coordinate optimization, not just a canonical map.

Here is the weakest precise pointwise tensor statement consumed by that handoff.  Let
$$
 d\lambda_d(z)=2^{-d/2}e^{-\sqrt2\|z\|_1}\,dz.
 \tag{1}
$$
Every coordinate has mean zero and variance one, and
$C_P(\lambda_d)=2$ by the exact one-dimensional Laplace gap and tensorization.  For
$U\in O(d)$, set $\eta_U=U_\#\lambda_d$, write $u_j=Ue_j$, and let
$$
 T_U=\nabla\Phi_U:\eta_U\longrightarrow\mu
 \tag{2}
$$
be the quadratic-cost Brenier map to a full-dimensional isotropic log-concave target $\mu$.
The proposed global gate is
$$
 \boxed{
 \sup_{d\ge1}\ \sup_{\mu}\ \inf_{U\in O(d)}
 \operatorname*{ess\,sup}_{x\in\mathbb R^d}
 \|D^2\Phi_U(x)\|_{\rm op}<\infty .}
 \tag{LB}
$$
The supremum is over full-dimensional isotropic log-concave targets; proper affine support is
handled intrinsically in its affine hull.  For the first kill test, the second supremum is
replaced by the single isotropic regular-simplex law in every dimension.

The route scout used the phrase “Lipschitz/Hessian control.”  For a convex Brenier potential the
two versions agree:
$$
 \operatorname{Lip}(T_U)
 =\operatorname*{ess\,sup}_x\|D^2\Phi_U(x)\|_{\rm op}.
 \tag{3}
$$

## 2. Term-by-term decomposition of the demanded object

### 2.1 Source term

The source is not merely “some exponential-tailed law.”  It is the fixed product (1), because its
two features are both load-bearing:

- $C_P(\lambda_d)=2$ has no dimension loss;
- its Euclidean tails have the exponential scale needed to reach the long vertices of an
  isotropic simplex at their exponentially small mass.

The rotation $U$ is also load-bearing.  Product Laplace measure is not rotationally invariant;
optimizing $U$ changes the location of its $d$ cusp hyperplanes and its $2d$ heaviest tail rays.

### 2.2 Transport and tensor term

For $H_U=D^2\Phi_U\succeq0$, tensorization of the source gap gives, for locally Lipschitz $f$,
$$
\begin{aligned}
 \operatorname{Var}_\mu f
 &=\operatorname{Var}_{\eta_U}(f\circ T_U)\\
 &\le2\int |H_U(x)\nabla f(T_U(x))|^2\,d\eta_U(x)\\
 &=2\int \left\langle\nabla f(T_U(x)),H_U(x)^2
                 \nabla f(T_U(x))\right\rangle d\eta_U(x).
 \tag{4}
\end{aligned}
$$
Thus the precise source-coordinate tensor is
$$
 \mathcal G_U(x)
 :=\sum_{j=1}^d\partial_{u_j}T_U(x)\otimes\partial_{u_j}T_U(x)
 =H_U(x)^2.
 \tag{5}
$$
A bound $\mathcal G_U\preceq B I$ gives $C_P(\mu)\le2B$.  Equivalently,
$\|H_U\|_{\rm op}\le L$ gives $C_P(\mu)\le2L^2$.

This is the weakest *pointwise local tensor norm* that the direct transfer consumes.  Bounding
each column separately is insufficient: $|\partial_{u_j}T|\le C$ only gives
$\mathcal G_U\preceq dC^2I$ in the worst case.  A trace or Hilbert--Schmidt average has the same
defect.  Since a full-dimensional Brenier map is invertible almost everywhere, replacing (5) by
the same multiplication-form inequality after conditioning on $T_U(x)=y$ does not create useful
averaging: the conditional matrix is just $H_U(T_U^{-1}y)^2$.

### 2.3 Target term

No target Poincare, Cheeger, localized-profile, or CMH estimate may be inserted into the proof of
(LB).  The target assumptions available to the PDE are only:

- log-concavity of its density;
- isotropy, for normalization;
- for the simplex gate, a constant density and the explicit second-boundary condition
  $\overline{\nabla\Phi(\mathbb R^d)}=K_d$.

Using the already known affine Poincare bound for Dirichlet/simplex laws would verify that the
simplex itself satisfies KLS, but it would say nothing about this particular Brenier Hessian.
The Laplace--Brenier condition is a sufficient route stronger than KLS, so the simplex may refute
the route without refuting `conj:kls`.

### 2.4 Damping and stochastic boundary terms

There is no stochastic source, Riccati damping, stopping time, or moving isoperimetric profile in
this route.  Its analogue of a boundary/error term is deterministic: the singular curvature of
the source potential on the $d$ coordinate walls, together with the target support condition at
spatial infinity.  Section 8 isolates those terms exactly.

## 3. The KLS implication and the positive calibrations

### 3.1 Sufficiency is exact

If (LB) holds with constant $L$, equation (4) gives
$$
 \operatorname{Var}_\mu f\le2L^2\int|\nabla f|^2\,d\mu.
 \tag{6}
$$
No Milman upgrade, quadratic-chaos input, moment-map comparison, or localization estimate is
needed.  This proves that (LB) is genuinely KLS-sufficient and also shows that it is stronger
than the desired conclusion.

### 3.2 One dimension

The positive one-dimensional calibration can be made quantitative using the imported published
node `lem:one-dimensional-density-variance`.

Let $f$ be a one-dimensional log-concave density of variance one, $F$ its CDF, and
$$
 I_f(p)=f(F^{-1}(p)),\qquad 0<p<1.
$$
The profile $I_f$ is concave and has nonnegative one-sided endpoint limits (they need not vanish
for a bounded support).  If $M=\|f\|_\infty=\sup I_f$, concavity on the two chords from an
approximate maximizer to the endpoints, followed by a limit, gives
$$
 I_f(p)\ge M\min\{p,1-p\}.
 \tag{7}
$$
The Bobkov--Chistyakov density--variance bound recorded in the ledger gives
$M\ge1/\sqrt{12}$.  For the isotropic Laplace density $\ell$ in (1),
$$
 \ell(x)=\sqrt2\min\{F_\ell(x),1-F_\ell(x)\}.
 \tag{8}
$$
Therefore the monotone Brenier transport $t=F^{-1}\circ F_\ell$ satisfies almost everywhere
$$
 t'(x)=\frac{\ell(x)}{I_f(F_\ell(x))}\le\sqrt{24}=2\sqrt6.
 \tag{9}
$$
This covers bounded intervals, half-lines, and the whole line by the same quantile argument.

### 3.3 Products and rotated products

For an isotropic product target $\mu=\bigotimes_{j=1}^d\mu_j$, quadratic cost and uniqueness make
the Brenier map coordinatewise:
$$
 T(z)=(t_1(z_1),\ldots,t_d(z_d)).
$$
Equation (9) gives $\|DT\|_{\rm op}\le2\sqrt6$.  If the target is a rotation
$R_\#\mu$, choose the source rotation $U=R$ and conjugate this map by $R$; the same bound holds.
Thus the route recognizes tensorization exactly, rather than charging $d$ independent factors
$d$ times.

These calibrations do not prove the simplex gate, but they verify the two positive tests in the
route-scout handoff with explicit constants.

## 4. The isotropic regular simplex and its exact Monge--Ampere equation

Put $m=d+1$ and
$$
 H_m=\left\{y\in\mathbb R^m:\sum_{i=1}^m y_i=0\right\}.
$$
Let $P$ be uniform on the probability simplex
$\Delta_{m-1}=\{p_i\ge0,\ \sum_i p_i=1\}$.  Since
$$
 \operatorname{Cov}\!\left(P-\frac1m\mathbf1\right)
 =\frac1{m(m+1)}I_{H_m},
$$
the isotropic regular simplex is
$$
 K_d=\operatorname{conv}\{a_1,\ldots,a_m\},
 \qquad
 a_i=\sqrt{m(m+1)}\left(e_i-\frac1m\mathbf1\right).
 \tag{10}
$$
Its basic scales are
$$
 |a_i|^2=d(d+2),\qquad
 |a_i-a_j|=\sqrt{2(d+1)(d+2)},
 \tag{11}
$$
and, with $d$-dimensional Euclidean volume on $H_m$,
$$
 |K_d|
 =\frac{\sqrt{d+1}\,((d+1)(d+2))^{d/2}}{d!}.
 \tag{12}
$$

Fix any orthonormal source frame $u_1,\ldots,u_d$ of $H_m$.  The Brenier potential for transport
from the corresponding rotated product Laplace law to the uniform law on $K_d$ solves, almost
everywhere,
$$
 \boxed{
 \det D^2\Phi(x)
 =|K_d|2^{-d/2}
   \exp\!\left(-\sqrt2\sum_{j=1}^d|\langle x,u_j\rangle|\right),
 \qquad
 \overline{\nabla\Phi(H_m)}=K_d.}
 \tag{13}
$$
The simplex kill question is exactly whether the infimum over orthonormal frames of
$\|D^2\Phi\|_{L^\infty({\rm op})}$ stays bounded or diverges.

## 5. First attempted kill: determinant balance does not diverge

If $\|D^2\Phi\|_{\rm op}\le L$ almost everywhere, (13) and
$\det D^2\Phi\le L^d$ give
$$
 L\ge \ell_d
 :=\left(|K_d|2^{-d/2}\right)^{1/d}
 =\frac{(d+1)^{1/(2d)}\sqrt{(d+1)(d+2)}}
        {\sqrt2\,(d!)^{1/d}}.
 \tag{14}
$$
This is independent of the rotation.  Stirling's formula yields
$$
 \ell_d\longrightarrow\frac e{\sqrt2}.
 \tag{15}
$$
In dimension one, $K_1=[-\sqrt3,\sqrt3]$ and $\ell_1=\sqrt6$, which is exactly the
central derivative of the monotone Laplace-to-uniform map.  In every dimension (14) remains
$O(1)$.  Hence neither the central density ratio nor the product of the Hessian eigenvalues
refutes the route.  Any refutation must force anisotropy of the Hessian, not merely a large
determinant.

There is a parallel scalar limitation.  If $X$ has the rotated product-Laplace law and
$Y=T(X)$ is isotropic, integration by parts in each source coordinate gives formally (and by
standard approximation rigorously)
$$
 \mathbb E\operatorname{Tr}D^2\Phi(X)
 =\sqrt2\,\mathbb E\left\langle
       Y,\sum_{j=1}^d\operatorname{sgn}(\langle X,u_j\rangle)u_j
                         \right\rangle
 \le\sqrt2\,d.
 \tag{16}
$$
Thus determinant and mean trace both live at a constant per-direction scale.  They do not control
the top eigenvalue or its essential supremum.

## 6. Rotation optimization: a frame that feeds every vertex

A canonical coordinate test can falsely suggest that one of the $d+1$ simplex vertices has no
matching product tail.  The optimization over rotations removes that objection exactly.

For $k=1,\ldots,d$, define the Helmert vectors
$$
 h_k=\frac{1}{\sqrt{k(k+1)}}
 \bigl(\underbrace{1,\ldots,1}_{k},-k,0,\ldots,0\bigr)\in H_m.
 \tag{17}
$$
They form an orthonormal basis of $H_m$.  The normal cone of $K_d$ at $a_i$ is
$$
 N_i=\{x\in H_m:x_i\ge x_j\ \text{for all }j\},
 \tag{18}
$$
because $\langle x,a_i\rangle=\sqrt{m(m+1)}x_i$.

Now assign the following $d+1$ signed source axes:
$$
 b_1=h_1,\qquad b_i=-h_{i-1}\quad(2\le i\le m).
 \tag{19}
$$
The first coordinate is the unique maximum of $h_1$.  For $i=k+1$, coordinate $i$ is the unique
maximum of $-h_k$.  Consequently
$$
 b_i\in\operatorname{int}N_i\qquad(1\le i\le m).
 \tag{20}
$$
The assigned axes are mutually at distance $\sqrt2$ on the unit sphere, except for
$b_1=-b_2$, whose distance is $2$.  This uses the permissible signed axes of one orthonormal
product frame; it is not an enlargement of the source family.

Convex duality gives the right asymptotic assignment.  A compact-range Brenier potential has
recession function $h_{K_d}$.  Along a ray in the interior of $N_i$, the exposed face is the
singleton $\{a_i\}$, hence
$$
 \nabla\Phi(tb_i)\longrightarrow a_i\qquad(t\to\infty)
 \tag{21}
$$
at differentiability points.  Full finite cyclic monotonicity is automatic because
$a_i\in\partial h_{K_d}(b_i)$, so all pairs $(b_i,a_i)$ lie in the subgradient graph of one
convex function.  In particular, if $b_i\in N_i$ and $b_j\in N_j$, then
$$
 \langle b_i-b_j,a_i-a_j\rangle\ge0.
 \tag{22}
$$

Therefore a claim that “$d$ product axes cannot address $d+1$ simplex vertices” is false.  The
Helmert frame is an explicit feasible solution achieving complete coverage in that yes/no
normal-fan test.  No optimization theorem for the actual Brenier Lipschitz constant is claimed.
The construction removes one proposed reason for a divergent bound; it does **not** prove an
upper Hessian estimate.

## 7. Second attempted kill: cap geometry and tail geometry match

For fixed $\alpha\in(1/2,1)$, define the vertex cap
$$
 C_i(\alpha)
 =\left\{\sqrt{m(m+1)}\left(p-\frac1m\mathbf1\right):
               p\in\Delta_{m-1},\ p_i\ge\alpha\right\}.
$$
Since $p_i\sim\operatorname{Beta}(1,d)$ under the uniform simplex law,
$$
 \mu_{K_d}(C_i(\alpha))=(1-\alpha)^d.
 \tag{23}
$$
For $i\ne j$, the inequalities $p_i\ge\alpha$ and $q_j\ge\alpha$ imply
$p_i-q_i\ge2\alpha-1$ and $q_j-p_j\ge2\alpha-1$.  Equality is attained by interchanging
the masses $\alpha$ and $1-\alpha$ on coordinates $i,j$, so
$$
 \operatorname{dist}(C_i(\alpha),C_j(\alpha))
 =\sqrt{2m(m+1)}(2\alpha-1)=\Theta(d).
 \tag{24}
$$

The Helmert-oriented source has sets of the same exponential mass at the same separation scale.
In source coordinates let $b_i$ be represented by its signed coordinate axis and, for $r\ge1$,
take the box
$$
 B_i(r)=\left\{z:
  |z_{k(i)}-\sigma_i r|\le1,\quad |z_j|\le1\ (j\ne k(i))\right\}.
$$
Writing $p_0=\mathbb P(|Z_1|\le1)=1-e^{-\sqrt2}$ and
$c_1=\sinh(\sqrt2)$, independence gives
$$
 \lambda_d(B_i(r))=c_1e^{-\sqrt2r}p_0^{d-1}.
 \tag{25}
$$
Choosing
$$
 r=\frac{d}{\sqrt2}\log\frac{p_0}{1-\alpha}+O(1)
 \tag{26}
$$
makes (25) comparable to (23).  The centers of the boxes are separated by at least
$\sqrt2r$, while their Euclidean radii are $\sqrt d$, so
$$
 \operatorname{dist}(B_i(r),B_j(r))=\Theta(d).
 \tag{27}
$$

Equations (23)--(27), together with the normal-fan assignment (20), show that the **raw
mass-packing and normal-ray surrogate** has the correct constant-order scaling.  They do not
assert that the Brenier map sends these boxes onto the caps, that the actual cap preimages resemble
them, or that no subtler concentration/cyclic-monotonicity obstruction exists.  The precise
conclusion is only that abstract mass, separation, and representative-ray orientation do not by
themselves yield a divergent lower bound.

## 8. Where the analytic proof actually stops: the Laplace walls

### 8.1 Existing support--curvature theorems stop before the cusp

The specialized literature search is recorded in
`research/explorations/2026-08-27-literature-scout-laplace-brenier-w2l01.md`.

Gwozdz, arXiv:2608.15906v1 (an unreviewed preprint), proves for a compact log-concave target $K$
and a source $e^{-V}$ satisfying $D^2V\preceq Q$ that
$$
 \partial_{vv}\Phi
 \le0.587\sqrt{\langle Qv,v\rangle}\,w_K(v),
 \qquad
 \operatorname{Lip}(\nabla\Phi)
 \le0.587\sqrt{\|Q\|_{\rm op}}\operatorname{diam}(K).
 \tag{28}
$$
The paper also supplies a fully analytic but larger numerical constant.  Its relevance here is
twofold:

- it handles nonsmooth simplex targets, so simplex corners alone are not the obstruction;
- it requires a source upper-curvature matrix, which exact product Laplace measure does not have.

Indeed, for
$V_U(x)=\sqrt2\sum_j|\langle x,u_j\rangle|$, at a point on $u_j^\perp$ away from the other walls,
$$
 V_U(x+tu_j)+V_U(x-tu_j)-2V_U(x)=2\sqrt2|t|.
 \tag{29}
$$
No finite quadratic form $\langle Qu_j,u_j\rangle t^2$ dominates (29) as $t\downarrow0$.
Distributionally,
$$
 D^2V_U
 =2\sqrt2\sum_{j=1}^d u_j\otimes u_j\,
   \mathcal H^{d-1}\!\restriction u_j^\perp.
 \tag{30}
$$
Smoothing $|s|$ to $\sqrt{s^2+\varepsilon^2}$ makes the required upper curvature at zero of
order $\varepsilon^{-1}$, so (28) diverges and does not pass to the cusp.

Kolesnikov's published 2010 support estimates have the same first failure: the relevant theorem
assumes a smooth source with $V_{hh}\le\Lambda$ (and its directional refinement also uses a
gradient bound).  The source approximations called Laplace-like in that paper are rounded at the
origin.  The exact exponential-product problem is left open; rotating the exact source cannot
remove (30).

Klartag--Kolesnikov's published multiplicative concentration for the eigenvalues of Brenier
Hessians controls fluctuations of $\log\lambda_i$ around an unspecified scale.  It supplies
neither the scale of $\lambda_{\max}$ nor an $L^\infty$ upgrade, so it also stops before (LB).

### 8.2 The exact differentiated equation

The cusp obstruction is not merely a failed hypothesis; it identifies the uncontrolled term.
Write $z_j=\langle x,u_j\rangle$ and $H=D^2\Phi$.  In any open source orthant, (13) gives
$$
 \log\det H
 =\log(|K_d|2^{-d/2})-\sqrt2\sum_j\sigma_j z_j,
 \qquad \sigma_j=\operatorname{sgn}z_j.
 \tag{31}
$$
Let $\mathcal L_Hg=\operatorname{Tr}(H^{-1}D^2g)$.  For a fixed source-coordinate direction
$u_j$, differentiation yields
$$
 \mathcal L_H(\Phi_{u_j})=-\sqrt2\sigma_j,
 \tag{32}
$$
and, inside the orthant,
$$
 \mathcal L_H(\Phi_{u_ju_j})
 =\operatorname{Tr}\!\left(
 H^{-1}D^2\Phi_{u_j}H^{-1}D^2\Phi_{u_j}
 \right)\ge0.
 \tag{33}
$$
For a general unit $v=\sum_ja_ju_j$, the same identity holds in the bulk, while the
distributional second derivative of the source contributes
$$
 -2\sqrt2\sum_{j=1}^d a_j^2
 \mathcal H^{d-1}\!\restriction u_j^\perp
 \tag{34}
$$
to the right-hand side of the global equation for $\Phi_{vv}$.

Equations (32)--(33) are classical wherever the solution is smooth inside an orthant.  Globally,
(34) should be read as the source term in smooth approximations, converging to the displayed wall
measure; multiplying the limiting Hessian distributions by $H^{-1}$ requires a weak transmission
formulation that is itself part of Residue B.  No unproved global distributional product is used
as a conclusion here.

Thus the bulk square in (33) is favorable: a positive maximum of a fixed Hessian component cannot
be created strictly inside a smooth orthant.  The possible maxima are carried by

1. the source walls $u_j^\perp$ and their high-codimension intersections;
2. spatial infinity near transitions in the target normal fan;
3. the change of maximizing eigenvector when passing from a fixed $\Phi_{vv}$ to
   $\lambda_{\max}(H)$.

If $H$ has a common invertible wall trace $H_0$ and the required one-sided third-derivative
traces, (31) also gives the scalar wall jump
$$
 \left[\partial_{u_j}\log\det H\right]_{0^-}^{0^+}=-2\sqrt2,
 \qquad
 \operatorname{Tr}\!\left(H_0^{-1}
       [\partial_{u_j}H]_{0^-}^{0^+}\right)=-2\sqrt2.
 \tag{35}
$$
Equation (35) controls only one normalized trace.  It does not control the traceless response,
the mixed blocks $H_{u_j,u_j^\perp}$, or the Schur complement
$$
 H_{u_ju_j}
 -H_{u_j,u_j^\perp}
  H_{u_j^\perp,u_j^\perp}^{-1}
  H_{u_j^\perp,u_j}.
 \tag{36}
$$
Those are exactly the terms needed to bound the Gram tensor (5).

Restricting the map to a wall does not close an induction.  The image of
$u_j^\perp$ under $T$ is a transport-generated hypersurface in $K_d$, not a fixed affine simplex
slice; the restricted map is not known to be the Brenier map between a product-Laplace law in
$d-1$ dimensions and a log-concave target.  Treating it as such would silently assume the missing
Schur/interface theorem.

### 8.3 Exact first unjustified step

The first missing statement is the following dimension-free transmission estimate:

> For the solution of (13), in at least one orthonormal frame (for the simplex, the Helmert frame
> is the natural first candidate), control the wall traces, mixed blocks, and Schur complements
> in (35)--(36) strongly enough that the favorable orthant identity (33) propagates
> $D^2\Phi\preceq CI$ from the walls and infinity into every orthant, with $C$ independent of $d$.

No source in the repository or the checked literature proves this.  It is **needs new idea**, not
a removable smoothness detail: every standard smoothing loses the constant precisely in (34).

## 9. Residue and route-promotion verdict

### Residue A — simplex Hessian transmission (`needs new idea`)

Decide
$$
 \sup_{d\ge1}\inf_{U\in O(d)}
 \|D^2\Phi_{d,U}\|_{L^\infty({\rm op})}<\infty,
 \tag{37}
$$
where $\Phi_{d,U}$ is the solution of (13), or prove that the left side diverges.  The Helmert
frame removes the normal-fan/tail mismatch but supplies no wall-to-bulk Hessian estimate.

### Residue B — cusp approximation (`technical gap` after a new estimate)

Any proposed wall estimate must first be proved for a regularized second-boundary problem with
constants independent of the source smoothing, target collar, and spatial truncation; only then
may one pass to the Alexandrov/Brenier limit.  Existing stability theorems pass a bound that is
already uniform and do not create one.

### Residue C — fixed components versus the top eigenvector (`needs new idea`)

Equation (33) treats one fixed $v$.  The maximizer of $\Phi_{vv}$ may rotate with $x$, and a
coordinatewise wall bound may lose $d$ when assembled.  A successful estimate must act directly
on $H^2$ or on $\lambda_{\max}(H)$ without replacing it by $\operatorname{Tr}H^2$.

### Residue D — extension beyond compact simplices (`technical gap`, later)

Even a positive solution of (37) proves only the first calibration.  The full route would still
need a target approximation theorem for arbitrary, possibly unbounded, isotropic log-concave
laws that preserves the optimized rotation and the Hessian bound.  This is downstream and was
not used to weaken the simplex gate.

### Verdict

- **Simplex refutation:** not established.  Determinant, cap separation, exponential tails, and
  normal-fan orientation all have the constant-order scaling required by the route.
- **Simplex verification:** not established.  The exact $L^\infty$ operator-Hessian estimate
  remains open at the Laplace walls.
- **Route promotion:** **do not promote or register yet**.  The first kill gate remains unresolved,
  but it is now a single explicit PDE/transmission problem rather than an informal transport
  hope.

Proposed one-line pre-registration gate for the orchestrator:

> For the uniform isotropic regular simplex $K_d$, prove
> $\sup_d\inf_{U\in O(d)}\|D^2\Phi_{d,U}\|_{L^\infty({\rm op})}<\infty$ for the exact
> product-Laplace Monge--Ampere problem (13), or prove that this infimum diverges; a valid proof
> must control the source-cusp wall tensor uniformly and may not infer the result from determinant,
> marginal, or smoothed-curvature bounds.

## 10. Fence-by-fence check

The proposed node is not in the ledger and therefore has no formal `bounded_by` list.  Every live
KLS fence was nevertheless checked.

### `rem:two-tail-slice-bounds`

The argument makes no slice-wise unweighted Stein-source estimate and no covariance-weight claim.
Its exponential reference is static, and the consumed object is the full transport Gram tensor
(5).  The two-tail absolute-scale counterexample is therefore not contradicted.

### `rem:projection-ceiling`

No collection of one-dimensional projection variances is used to infer (LB).  Equations
(14), (16), and (23) are explicitly classified as scalar calibrations that do **not** control the
top Hessian eigenvalue.  The missing estimate is tensor-valued, so the projection ceiling is
respected.

### `rem:crude-insufficient`

No crude covariance integral or localization bootstrap appears.  This fence is inapplicable.

### `rem:relative-ceiling`

(LB) is openly a KLS-sufficient global hypothesis, not advertised as a weaker bootstrap input.
Equation (6) displays the implication and its constant.  This is acceptable for a new sufficient
route but means that proving (LB) is not progress by assumption alone.

### `rem:profile-circularity`

No localized isoperimetric profile or moving family is inserted.  In particular, the known
simplex Poincare/CMH result is not used to control its Brenier map.

### `rem:single-coordinate-cuts`

The product calibration in Section 3 verifies tensorization of a static transport.  It makes no
claim about persistent single-coordinate cuts under stochastic localization, so it does not
collide with the rank-one obstruction.

### Gaussian pathwise-Lipschitz warning and covariance-spike constraint

The manuscript's warning against a universal Gaussian-to-log-concave Lipschitz map is evaded by
the exponential-tailed source: one-dimensional exponential targets already pass (9).  The
conditional-covariance spike obstruction is also not contradicted; the route never bounds a
localized covariance process.  Its tensor norm is nevertheless tensorization-aware, as the exact
product calibration shows.

## 11. Proposed ledger delta

None.  The transfer implication and the 1D/product calibrations have complete analytic sketches,
but the proposed route has not passed its first kill gate and has no registered route value.  A
candidate node now would create a second control plane before the route decision.  If (37) is
later proved or refuted through a dossier and independent review, the orchestrator can register
the route, its exact sufficiency bridge (4)--(6), and the simplex result together.

## Handoff

```yaml
outcome: blocked
artifacts:
  - research/explorations/2026-08-27-kls-route-prober-laplace-brenier-simplex-w2b01.md
proposed_deltas:
  - "Do not register laplace-brenier yet; replace its informal first kill test by the exact rotation-optimized simplex PDE gate in Section 9."
  - "No ledger delta: the determinant and Helmert normal-fan results calibrate the gate but neither prove nor refute its L-infinity Hessian statement."
next_role: orchestrator
next_prompt: |
  Keep laplace-brenier outside the live route registry. Record the exact pre-registration gate from Section 9: decide the dimension-free rotation-optimized operator-Hessian bound for the product-Laplace-to-isotropic-simplex Monge--Ampere problem, with a uniform source-wall transmission estimate. Do not cite determinant balance, cap-tail matching, or Gwozdz/Kolesnikov smoothing as a resolution. If another wave attacks this proposal, give one owner the wall Schur-complement/transmission estimate in the explicit Helmert frame; do not split it into CMH or trace-upgrade subproblems.
```
