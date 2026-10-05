---
---

# Wave A: fixed-degree simplex fiber duals have a uniform analytic floor

## Question examined

Route `ap:f-simplex-dual`, under `ap:f-frame-construction`, requested the
exact all-frame degree-three min-max $\Lambda_{m,3}$ for $m=3,\ldots,8$,
with a certificate of global optimality. The starting lens was **construct**.
I changed to **prove** after finding a dimension-independent reverse
polynomial inequality on every uniform chord. It directly obstructs the
route's fixed-degree asymptotic objective, without determining the requested
finite-dimensional optima.

The exact object is, for $d=m-1$ and the isotropic uniform simplex $\mu_m$,

$$
\Lambda_{m,k}=\sup_{\substack{\rho\text{ even Borel probability}\\
d\int\theta\theta^T\,d\rho=I_{H_0}}}
\inf_{\substack{f\in\mathbb R[H_0],\ \deg f\le k\\
\operatorname{Var}_{\mu_m}(f)>0}}
\frac{\mathcal D_{\mu_m,\rho}(f)}{\operatorname{Var}_{\mu_m}(f)}.
$$

The frame is chosen before the polynomial. Constants are quotiented out,
and degree means degree at most $k$, not the homogeneous degree-$k$ sector.
The target served is [](#conj:conditional-fiber-frame), which requires one
frame to work for every function in its maximal closed form domain;
finite-degree tests cannot establish that conclusion.

**Preregistered criterion retained before any new run:** monotone decrease
across $m=3,\ldots,8$ by a total factor at least three, with the last value
below $0.1$, counts only as directional evidence. No such run was performed.
Absence of this finite-range trend does not force degree four; finite $m$
implies no asymptotic conclusion. The asymptotic conclusion below instead
comes from an analytic argument valid for all $m$.

## What we learned

**Established, not independently certified:** the draft
`solutions/lem-fiber-polynomial-floor.md` proves, with
$A_k=k(k+1)^2(k+2)$, for every $m\ge2$, every $k\ge1$, every admissible
frame, and every polynomial of degree at most $k$,

$$
\mathcal D_{\mu_m,\rho}(f)
\ge\frac{12}{A_k}\int|\nabla_{H_0}f|^2\,d\mu_m
\ge\frac{3}{A_k}\operatorname{Var}_{\mu_m}(f).
$$

The proof expands a centered polynomial on $[-1,1]$ in normalized Legendre
polynomials. The squared Hilbert–Schmidt norm of differentiation on the
nonconstant degree-$\le k$ subspace is $A_k/4$. Rescaling an interval of
length $L$ gives $\mathbb E|q'|^2\le A_k\operatorname{Var}(q)/L^2$.
Dividing by its coordinate variance $L^2/12$, then applying frame isotropy,
proves the first inequality. The second uses the certified
[](#cor:cmh-dirichlet-poincare), with ordinary isotropic Poincaré constant
at most four. Bounded gradients on the compact simplex prove membership in
the maximal form domain directly. No numerical evidence is used.

Thus the rigorous-bound proposal is $1/80\le\Lambda_{m,3}\le1$ for every
$m\ge2$, including the entire requested range. More strongly, every fixed
finite degree has a positive uniform floor. Subject to independent review,
this rules out all fixed-degree asymptotic simplex dual refuters, not merely
degree three. Degree growing with dimension and unrestricted tests remain
untouched. The root cap and negative-exchange obstructions
[](#prop:conditional-fiber-root-obstruction) and
[](#prop:sasada-negative-exchange) are therefore respected.

**Established, not independently certified: exact symmetry reduction.**
Choose a variance-orthonormal basis of the polynomial quotient
$V_{m,k}$ and let $B(\theta)$ be the matrix of the single-direction fiber
form, without the factor $d$. Coordinate permutations act orthogonally on
this basis, because they preserve $\mu_m$ and polynomial degree. If
$U_\sigma f(x)=f(\sigma^{-1}x)$, change of variables on chords gives
$B(\sigma\theta)=U_\sigma B(\theta)U_\sigma^T$.
Consequently pushing a frame forward by $\sigma$ conjugates its averaged
matrix and preserves its least eigenvalue. Averaging a frame over $S_m$
can only increase that eigenvalue: for any unit vector $v$,
$v^T(\sum A_\sigma/|S_m|)v\ge\sum\lambda_{\min}(A_\sigma)/|S_m|$.
Thus the all-frame supremum equals the supremum over permutation-invariant
even frames; this is not a restriction to root and vertex orbits.

In fact the even permutation orbit of **any** unit $\theta\in H_0$ is
already admissible. Its second moment matrix commutes with all coordinate
permutations, hence has one common diagonal entry and one common off-diagonal
entry. It is therefore scalar on $H_0$, annihilates $\mathbf1$, and has
trace one. Its restriction to $H_0$ is exactly $I_{H_0}/d$.
Define the orbit matrix

$$
\overline A(\theta)=\frac{d}{m!}\sum_{\sigma\in S_m}
U_\sigma B(\theta)U_\sigma^T.
$$

Evenness adds nothing to this matrix since $B(-\theta)=B(\theta)$.
Every probability mixture of these orbit frames is admissible. Conversely,
for a permutation-invariant frame $\rho$ its averaged matrix equals
$\int\overline A(\theta)\,d\rho(\theta)$. Hence an exact reduced formulation is

$$
\Lambda_{m,k}=\sup_{\nu\text{ probability on }S(H_0)}
\lambda_{\min}\left(\int\overline A(\theta)\,d\nu(\theta)\right).
$$

For an upper certificate it suffices to give a positive semidefinite matrix
$Z$ of trace one and a number $u$ such that
$\operatorname{Tr}(Z\overline A(\theta))\le u$ for **every** unit direction.
Indeed $\lambda_{\min}(A)\le\operatorname{Tr}(ZA)$ for any symmetric $A$,
and integration proves $\Lambda_{m,k}\le u$. One may average $Z$ under
$S_m$ without changing any of these inequalities, since the orbit matrices
commute with that group. A matching admissible mixture with matrix
$A\succeq uI$ would certify global optimality. No such matching pair is
constructed here. This argument does not assume a minimax interchange.

**Observed from source inspection:** the earlier frame code implements exact
root and vertex matrices, a one-parameter mixture search, and sampled
spherical matrices. Its matrix functions and degree quotient agree with the
normalization above. These are a library of primal lower bounds; none is an
all-direction dual inequality. The earlier run artifacts were inspected as
provenance/context only. No old numerical value is used to infer a new result
or route change, and no new run artifact is needed for the analytic argument.

## What resists

Exact values for $m=3,\ldots,8$ remain unresolved. The precise missing step
is a globally valid direction inequality
$\operatorname{Tr}(Z\overline A(\theta))\le u$ on the continuous sphere,
together with a matching primal frame mixture. Permutation symmetry reduces
frame admissibility but leaves a continuum of orbit types; neither root and
vertex eigenvalues nor a seeded optimizer remove this continuum.

There is no unclosed step claimed in the fixed-degree floor dossier, but its
status is a draft until independent review. The floor is too weak to decide
the preregistered finite-range threshold and tends to zero with $k$.
A variable-degree polynomial dual could therefore still work. A uniform
full-domain lower bound would need an additional argument that avoids this
degree loss, and is not supplied here.

## Proposed next step

Have an independent reviewer check `lem:fiber-polynomial-floor`, especially
the interval scaling by arc length, the Legendre sum, frame averaging, and
the use of the established Dirichlet Poincaré corollary without a universal
CMH premise. Proposed dependencies are `lem:conditional-fiber-form` and
`cor:cmh-dirichlet-poincare`; no `assumes` edge is needed.

Before review, keep `ap:f-simplex-dual` active with its next action set to
reviewing this proposed analytic obstruction. If certified, the route's
fixed-degree objective is exhausted: update it to pursue degrees $k(m)$
tending to infinity or nonpolynomial dual tests, or close that fixed-degree
sub-route. Reopening a closed fixed-degree objective would require a defect
in the certified floor or a change of measure class/normalization. The parent
frame-construction route and [](#conj:conditional-fiber-frame) remain open.
The next discriminating mathematical task after certification is to quantify
how rapidly polynomial degree must grow to approximate a cap with low fiber
energy simultaneously for all direction orbits. This differs from the
vertex-frame cap task, which tests one prescribed frame only.
