---
title: "Song–Zhang v2: the common coefficient radius and height reduction"
ledger-node: prop:sz-v2-common-radius
numbering:
  enumerator: "139.%s"
---

**Overview.** The coefficient radius is one scalar assigned to a fixed measure,
independent of polynomial degree, block length, and block order. Its finiteness
follows from the bounded inverse diffusion operator. Polynomial testing relates
it to every finite block, and the already certified curvature comparison bounds
the Poincaré constant by this radius. This proves
[](#prop:sz-v2-common-radius), with the normalization of
[](#def:sz-v2-common-radius). These are the interfaces of Lemmas 8.17–8.18
of [@SongZhang2026ConstantKLS], reconstructed below without a uniform KLS input.

**Dependencies.** The proof uses [](#lem:sz-analytic-foundations), the Appell
conventions in [](#thm:sz-polynomial-variance), and
[](#thm:sz-curvature-comparison). It does not use the improved iteration,
BKL, any consequence of BKL, or a uniform bound on the Poincaré constant.
The finiteness of the inverse operator is used for one regular measure at a
time, with no claim of uniformity in that measure.

## The common radius

Let $\mu=e^{-W}dx$ be centered, with $W\in C^\infty$,
$aI\preceq D^2W\preceq bI$ for $0<a\le b<\infty$, and
$\operatorname{Cov}(\mu)\preceq I$. Put
$\mathscr H=L^2_0(\mu)$, let $H$ be its nonnegative diffusion operator, and
write $B=H^{-1}$ on $\mathscr H$. Let $P_+$ subtract componentwise means,
and set
$$
 \mathcal T=P_+\nabla B,\qquad R=\|\mathcal T\|_{\mathrm{op}}^2.
$$
The codomain of $\mathcal T$ is $\mathscr H\otimes\mathbb R^n$.
Its iterates apply it componentwise and append an ordered output slot.
All tensor norms below sum over ordered indices. In particular, finite
orthogonal amplification preserves the operator norm of $\mathcal T$.
For the Appell coefficients $c_d=\sqrt{K_d}/d!$, define
$$
 \mathcal A(\mu)=\max\left\{1,\sup_{d\ge2}c_d^{2/(d-1)}\right\}.
$$

:::{prf:theorem} A finite radius shared by every degree and block
:label: thm:sol-sz-v2-common-radius
For every measure in the stated regular class,
$$
 C_P(\mu)-1\le R\le C_P(\mu),\qquad
 1\le\mathcal A(\mu)\le\max\{1,R\},\qquad
 c_d\le\mathcal A(\mu)^{(d-1)/2}\quad(d\ge1).
$$
If $G:\mathbb N_{\ge1}\to[1,\infty)$ is nondecreasing and
$c_k\le G(k)^{k-1}$ for every $k\ge1$, then, for every integer $m\ge1$,
$$
 \mathcal A(\mu)\le
 \max\{G(m)^2,\|\mathcal T^m\|_{\mathrm{op}}^{2/m}\}.
$$
Moreover,
$$
 C_P(\mu)\le2^{85}\mathcal A(\mu).
$$
Each assertion concerns the same fixed measure. The constant in the last
inequality is independent of its dimension and curvature bounds.
:::

:::{prf:proof}
**The restricted operator.** Spectral calculus from
[](#lem:sz-analytic-foundations) gives a bounded positive inverse $B$ on
$\mathscr H$, with $\|B\|=C_P(\mu)<\infty$.
For $f\in\mathscr H$, $Bf\in\operatorname{Dom}H$ and
$$
 \|\nabla Bf\|_2^2=\langle Bf,HBf\rangle=\langle f,Bf\rangle.
$$
The coordinate $x_i$ belongs to the form domain; testing the form against it
gives $\mathbb E\partial_i Bf=\mathbb E[X_i f]$.
Write $Lf=\mathbb E[Xf]$. By duality and covariance normalization,
$$
 |Lf|=\sup_{|v|=1}|\mathbb E[f\langle v,X\rangle]|
 \le\|f\|_2.
$$
Consequently
$$
 \mathcal T^*\mathcal T=B-L^*L,
 \qquad B-I\preceq\mathcal T^*\mathcal T\preceq B.
$$
Taking suprema of the quadratic forms over unit vectors proves the claimed
bounds on $R$, without any uniform estimate on $C_P$.

**The testing identity.** For $d\ge1$ let
$Q_df=\mathbb E[f\mathcal A_d^\mu]$. This bounded map from $\mathscr H$
to symmetric $d$-tensors is adjoint to $T\mapsto P_d^\mu[T]$;
therefore $\|Q_d\|=\sqrt{K_d}=d!c_d$.
All these polynomials and their derivatives are square integrable because
the positive lower Hessian bound gives Gaussian tails. They belong to the
form domain by cutoff approximation.

For $d\ge2$, integration by parts in the form sense gives
$$
 \mathbb E[fP_d[T]]
 =\mathbb E\langle\nabla Bf,\nabla P_d[T]\rangle.
$$
Differentiating the formal generating identity shows
$\partial_iP_d[T]=dP_{d-1}[T_i]$, where $T_i$ is the slice with one
index fixed at $i$. Since $\mathbb E P_{d-1}[T_i]=0$, replacing
$\nabla Bf$ by $P_+\nabla Bf$ leaves this integral unchanged.
It follows, as an identity of bounded maps, that
$$
 \frac{Q_d}{d!}
 =\mathsf S_d\left(\frac{Q_{d-1}}{(d-1)!}\otimes I\right)\mathcal T.
 \tag{H1}
$$
Here $\mathsf S_d$ averages all permutations of the $d$ tensor slots.
The displayed identity follows by pairing against every symmetric tensor;
its right side is symmetric and hence this determines it uniquely.
Symmetrization is an orthogonal projection. Thus
$c_d\le\sqrt R\,c_{d-1}$. The covariance bound gives $c_1\le1$,
and finite induction yields
$$
 c_d\le R^{(d-1)/2}\quad(d\ge2).
$$
This also covers $R<1$. If $R=0$, all $c_d$ with $d\ge2$ vanish
by the same identity. The definition of $\mathcal A$ now proves its
finiteness and its first stated bounds. In particular no supremum is taken
before obtaining one finite bound valid at every degree.

**Finite blocks.** Iterating (H1) exactly $m$ times, for $d\ge m+1$,
gives
$$
 \frac{Q_d}{d!}
 =\mathsf S_d\left(\frac{Q_{d-m}}{(d-m)!}\otimes I\right)\mathcal T^m.
 \tag{H2}
$$
To justify the intermediate symmetrizations, $\mathcal T$ acts on scalar
components and thus commutes with any permutation of existing output slots.
The final average absorbs every intermediate permutation average. This
proves (H2) by finite induction, with no commutation of a spatial derivative
and $B$. Taking norms gives
$c_d\le\|\mathcal T^m\|c_{d-m}$.
For each $d\ge1$ write $d=jm+r$, where $j\ge0$ and $1\le r\le m$.
Finite iteration, including the case $j=0$, gives
$$
 c_d\le \|\mathcal T^m\|^j c_r
 \le \|\mathcal T^m\|^jG(m)^{r-1}
 \le \max\{G(m)^2,\|\mathcal T^m\|^{2/m}\}^{(d-1)/2}.
$$
When the block norm is zero and $j\ge1$, the first inequality already
gives zero; no ambiguous zeroth power is needed. The maximum is at least
one, so taking the defining supremum for $\mathcal A$ proves the assertion.

**The conversion to Poincaré.** Set
$\mathcal R=2^{40}\sqrt{\mathcal A(\mu)}$, which meets the threshold of
[](#thm:sz-curvature-comparison) with $\epsilon=1$ and $\ell\equiv1$.
Since $(k+1)^2\le4^k$ for $k\ge1$ and $\mathcal A\ge1$,
$$
 c_k\le\mathcal A^{(k-1)/2}
 \le\frac{\mathcal R^k}{(k+1)^2}.
$$
For every finite dyadic integer $d\ge2$, that certified comparison gives
$$
 C_P(\mu)\le32\mathcal R^2\max\{1,a^{-1/(d+1)}\}
 =2^{85}\mathcal A(\mu)\max\{1,a^{-1/(d+1)}\}.
$$
The curvature parameter $a>0$ is fixed throughout these inequalities.
Letting $d$ increase along dyadic integers removes the last factor.
Only scalar inequalities are passed to the limit; no infinite family of
inverse-gradient iterates is constructed.
:::

**Fences respected.** The common radius is finite for each regular law, but
no dimension-free upper bound on this radius has been proved here. Thus the
coefficient/KLS equivalence is respected, and no conclusion about uniform
conditional initialization or summable block losses is inferred from
pointwise finiteness. No `bounded_by` node is proposed for this interface.

## Reconstruction boundary

:::{prf:remark} The radius comparison alone is not repeated height reduction
:label: rem:sol-sz-v2-height-boundary
The preceding theorem reconstructs source Lemmas 8.17–8.18. It does not yet
reconstruct the raw-orbit estimates and finite block construction in source
Sections 8.2–8.4 and 8.6, or the profile induction of Proposition 8.24.
In particular, the existence of a degree-independent finite radius does not
give an initial family with loss of order $z^{-Q}$, uniformly in the odd
block order $Q$. That initialization, its retained prefix, its propagation
envelope, and its matched energy budget must all be constructed before
Propositions 8.25 and 8.1 can be used as local proved results.
:::
