---
title: "BK compatible integration and the Appell operator calculus"
ledger-node: prop:bk-integration-calculus
numbering:
  enumerator: "152.%s"
---

*Part of the Balasubramanian–Kasiviswanathan proof, Chapter [](#sec:bk-proof); the reading order is on the [full proofs](#sec:proofs-bk) page.*

**Overview.** We reconstruct Section 4 of
[@BalasubramanianKasiviswanathan2026KLS], at Git commit
`4837c33649ba2271f43c9684e9350ecbdd725f95`. The bounded inverse of the raw
compatible derivative splits into centered and constant input blocks. The Hodge
estimate gives a form comparison whose inverse controls the centered integration
operators. Taking a Hilbert direct sum preserves the rank-uniform inequalities;
Appell differentiation identifies the constant-input products exactly.

**Dependencies.** The substantive analytic input is
[](#lem:bk-compatible-hodge). Notation and coefficient normalization are
[](#def:bk-compatible-calculus) and [](#def:bk-uniform-appell-coefficients).
We use only the formal Appell definition, not any uniform bound for its
coefficients. No KLS, BKL, Song–Zhang v2 or later BK theorem is an input.

:::{prf:theorem} Integration operators on all tensor ranks
:label: thm:sol-bk-integration-calculus
Let $\mu(dx)=Z^{-1}e^{-V(x)}dx$ be centered, $V\in C^\infty$, with
$0<aI\preceq D^2V\preceq a_+I$ and $\operatorname{Cov}(\mu)\preceq I$.
For the notation of [](#def:bk-compatible-calculus), all $\widetilde J_r$
exist, and $J,L$ are bounded on their indicated direct-sum spaces. They obey
$$
 \|J\|^2\le C_P(\mu)\le1+\|J\|^2,\qquad \|L\|\le1,
 \qquad H_r^{-1}=J_rJ_r^*+L_rL_r^* \quad(r\ge0).
$$
For $g_a(t)=t/(1+at)$, spectral calculus gives
$$J^*J\preceq g_a(JJ^*+LL^*).$$
For every $j\ge1$,
$$\|J^{j-1}L\|\le c_j(\mu).$$
More precisely, for every $r,k\ge0$ and $T\in E_{r+k+1}$,
$$
 J_r\cdots J_{r+k-1}L_{r+k}T
 =\frac{1}{(k+1)!}T\mathbin{\lrcorner}A_{k+1}^{\mu},
$$
where the contraction leaves $r$ free indices and the left side is $L_rT$
when $k=0$. This is [](#prop:bk-integration-calculus).
:::

:::{prf:proof}
Set $p=C_P(\mu)$. By [](#lem:bk-compatible-hodge), $D_r$ is closed,
densely defined and bijective, with bounded inverse
$\widetilde J_r:C_{r+1}\to G_r$, satisfying
$\nabla\widetilde J_rF=F$ and $\mathbb E\widetilde J_rF=0$.
Its operator norm is at most $\sqrt p$. Since
$C_{r+1}=E_{r+1}\oplus G_{r+1}$, the inverse is the row operator
$(L_r,J_r)$: on constants the centered primitive is
$L_rT=T\mathbin{\lrcorner}x$. This uses $\mathbb EX=0$.
For each ordered $r$-tuple $I$, the covariance bound gives
$$
 \|L_rT\|_2^2
 =\sum_I\mathbb E\Big(\sum_jT_{Ij}X_j\Big)^2
 \le\sum_{I,j}T_{Ij}^2=\|T\|^2.                              \tag{1}
$$
Thus $\|L_r\|\le1$ independently of $r$. Similarly, scalar Poincaré on
every centered component of $J_rF$ gives
$\|J_rF\|_2^2\le p\|F\|_2^2$; equivalently this follows from the inverse
bound in the Hodge lemma.

**Inverse identities, with domains.** A closed densely defined bijective
operator with everywhere bounded inverse has bijective adjoint and
$(D_r^*)^{-1}=(D_r^{-1})^*=\widetilde J_r^*$.
Indeed, the equations defining the Hilbert adjoint of the bounded inverse
are exactly those defining the inverse of the unbounded adjoint; injectivity
uses density of $\operatorname{Dom}(D_r)$ and surjectivity of $D_r$.
In particular $\widetilde J_r\widetilde J_r^*f$ lies in
$\operatorname{Dom}(D_r^*D_r)$: applying $D_r$ gives
$\widetilde J_r^*f\in\operatorname{Dom}(D_r^*)$, whose adjoint image is
$f$. Conversely applying the product inverse to $D_r^*D_ru$ recovers $u$.
Therefore
$$
 H_r^{-1}=\widetilde J_r\widetilde J_r^*
 =J_rJ_r^*+L_rL_r^*.                                          \tag{2}
$$
The same argument in the other order gives
$(D_rD_r^*)^{-1}=\widetilde J_r^*\widetilde J_r$.
The operators $D_r^*D_r$ and $D_rD_r^*$ are the positive self-adjoint
operators associated with their standard closed forms.

**Inverting the Hodge form inequality.** Let $\widetilde H_{r+1}$ be the
operator on $C_{r+1}$ associated with the full gradient form, whose domain
is $C_{r+1}\cap W^{1,2}$. The potential cores from the Hodge lemma's proof
ensure density. Splitting off constants shows
$\widetilde H_{r+1}=0\oplus H_{r+1}$ relative to
$C_{r+1}=E_{r+1}\oplus G_{r+1}$. The Hodge lemma gives both
$$
 \operatorname{Dom}(D_r^*)\subset
 \operatorname{Dom}(\widetilde H_{r+1}^{1/2}),\qquad
 \|D_r^*F\|_2^2\ge
 \|\widetilde H_{r+1}^{1/2}F\|_2^2+a\|F\|_2^2.
$$
This is the form order $D_rD_r^*\succeq\widetilde H_{r+1}+aI$.
The order includes a domain inclusion; it is not merely an identity on a
smooth core. For a positive self-adjoint $T$ with positive lower bound,
$$
 \langle f,T^{-1}f\rangle=
 \sup_{u\in\operatorname{Dom}(T^{1/2})}
 \{2\operatorname{Re}\langle f,u\rangle-\|T^{1/2}u\|^2\}.
$$
Thus inversion reverses this form order, and
$$
 \widetilde J_r^*\widetilde J_r
 \preceq(\widetilde H_{r+1}+aI)^{-1}.
$$
Compress to $G_{r+1}$ to obtain
$$
 J_r^*J_r\preceq(H_{r+1}+aI)^{-1}
 =g_a(H_{r+1}^{-1})
 =g_a(J_{r+1}J_{r+1}^*+L_{r+1}L_{r+1}^*).                    \tag{3}
$$
The middle equality follows on each spectral value $\lambda>0$ from
$(\lambda+a)^{-1}=g_a(\lambda^{-1})$; continuity of $g_a$ at zero
also covers spectral accumulation of $H_{r+1}^{-1}$ there. No operator
monotonicity of an arbitrary scalar concave function is asserted or needed.

**The simultaneous direct sum.** For square-summable $F=(F_r)$ and $T=(T_r)$,
(1) and the uniform bound $\|J_r\|\le\sqrt p$ imply
$$
 \sum_{r\ge0}\|J_rF_{r+1}\|_2^2\le p\sum_{r\ge0}\|F_r\|_2^2,
 \qquad \sum_{r\ge0}\|L_rT_r\|_2^2\le\sum_{r\ge0}\|T_r\|^2.
$$
So $J$ and $L$ extend to bounded operators with $\|J\|^2\le p$ and
$\|L\|\le1$. Their norms are the suprema of the block norms. At rank zero
$H_0$ is the scalar Poincaré form operator on mean-zero $L^2$, so its
variational definition gives $p=\|H_0^{-1}\|$. Equation (2) and (1) yield
$$p\le\|J_0\|^2+\|L_0\|^2\le\|J\|^2+1.$$

Both $JJ^*$ and $LL^*$ preserve each $G_r$ and have respective blocks
$J_rJ_r^*$ and $L_rL_r^*$. Functional calculus of their sum preserves the
same decomposition (first for polynomials, then by uniform approximation
on its bounded spectrum). On $G_r$ for $r\ge1$, $J^*J$ has block
$J_{r-1}^*J_{r-1}$, so (3) proves the desired comparison there. On $G_0$
its block is zero and the right side is positive. Summing the quadratic
forms proves $J^*J\preceq g_a(JJ^*+LL^*)$ on all of $\mathcal H$.

**Appell normalization and all constant-input products.** The lower curvature
bound gives $V(x)\ge V(0)+\langle\nabla V(0),x\rangle+a|x|^2/2$,
so all polynomial moments exist. The formal generating identity defining
$A_j^\mu$ gives $A_1^\mu(x)=x$, $\mathbb EA_j^\mu=0$ for $j\ge1$,
and
$$
 \nabla\left[\frac1{j!}T\mathbin{\lrcorner}A_j^\mu\right]
 =\frac1{(j-1)!}T\mathbin{\lrcorner}A_{j-1}^\mu,              \tag{4}
$$
where the right contraction has one additional free index. To derive these
facts, take expectations in the formal generating series, yielding the
constant series one, and differentiate it in $x$, which multiplies it by
the formal variable. Coefficient comparison proves (4). The polynomial
field on the left is compatible since its derivative is fully symmetric;
it is centered for $j\ge1$ and belongs to all required finite Sobolev
orders.

For $k=0$ the claimed identity is $L_rT=T\mathbin{\lrcorner}x$.
For $k\ge1$, the derivative of its proposed right side equals
$T\mathbin{\lrcorner}A_k^\mu/k!$, which by induction is
$J_{r+1}\cdots J_{r+k-1}L_{r+k}T$ and is centered. Uniqueness of the
centered primitive therefore proves the identity at rank $r$.

For an ordered free-index tuple $I$ of length $r$, let $T_I$ be the
symmetric rank-$k+1$ slice of $T$. The definition of $c_{k+1}(\mu)$ gives
$$
 \left\|\frac{\langle T_I,A_{k+1}^\mu\rangle}{(k+1)!}\right\|_2^2
 \le c_{k+1}(\mu)^2\|T_I\|^2.
$$
Summing over $I$ and using $\sum_I\|T_I\|^2=\|T\|^2$ proves
$$\|J_r\cdots J_{r+k-1}L_{r+k}\|\le c_{k+1}(\mu).$$
For fixed $j\ge1$, the nonzero blocks of $J^{j-1}L$ are precisely these
products with $k=j-1$. Their source summands $E_{r+j}$ and target summands
$G_r$ are mutually orthogonal as $r$ varies; the lower source summands
are annihilated by the shift. Taking the supremum of block norms proves
$\|J^{j-1}L\|\le c_j(\mu)$.
:::

**Hypotheses and limits.** Centering identifies $L_r$ with contraction against
$x$; the covariance bound supplies its norm at most one. Positive curvature
and regularity are used only through the Hodge/domain result and existence of
moments. The common bound $\sqrt{C_P(\mu)}$ justifies the infinite direct
sum. Every $c_j(\mu)$ here is for this fixed law; no dimension-uniform or
degree-uniform coefficient estimate has been inferred.

**Fences respected.** No `bounded_by` nodes are assigned. This calculus supplies
operator inputs for a later argument. It makes no CMH, occupation, trace-upgrade,
or curvature-free spectral conclusion and takes none as an input.
