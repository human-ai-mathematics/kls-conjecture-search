---
title: 'Solution: KLS and exponential Appell coefficient growth'
ledger-node: prop:sz-exponential-coefficients-equivalence
numbering:
  enumerator: '124.%s'
---

*Part of the first version of Song–Zhang, Chapter [](#sec:polynomial-curvature); the reading order is on the [full proofs](#sec:proofs-sz-v1) page.*

**Overview.** The polynomial–curvature comparison identifies an exact growth condition
on the full Appell hierarchy that is equivalent to KLS. A Poincaré bound gives the
condition by a derivative recursion. In the converse direction, the coefficient profile
is constant in degree, so the comparison permits arbitrarily large finite dyadic degrees
at one fixed regular measure. Only the resulting scalar Poincaré bound is then passed to
arbitrary isotropic log-concave measures. This is an equivalent-strength reformulation,
not a proof of either side without its stated premise.

The Appell convention and ordered-index tensor norms are those of
[](#thm:sz-polynomial-variance). The reverse implication uses
[](#thm:sz-curvature-comparison), reconstructed from
[@SongZhang2026IteratedLogKLS, Section 5].

:::{prf:theorem} Exponential growth criterion
:label: thm:sol-sz-exponential-equivalence
The following two assertions are equivalent.

1. There is a finite universal $C$ such that $C_P(\mu)\le C$ for every isotropic
   log-concave probability on every $\mathbb R^n$, $n\ge1$.
2. There is a finite universal $A$ such that, for every integer $k\ge1$ and every
   isotropic probability $\nu(dx)=e^{-W(x)}dx$ in every dimension, where $W$ is
   smooth and $0<a_\nu I\preceq D^2W\preceq b_\nu I<\infty$, one has
   $c_k(\nu)\le A^k$. Here
   $c_k(\nu)=\sqrt{K_k(\nu)}/k!$ and
   $K_k(\nu)=\sup_{T\text{ symmetric},\ \|T\|_{\mathrm{HS}}=1}
   \operatorname{Var}_\nu P_k^\nu[T]$.

Quantitatively, assertion 1 with constant $C$ implies
$c_k(\nu)\le C^{(k-1)/2}$, and assertion 2 with constant $A$ implies assertion 1
with constant $32\max\{4A,2^{40}\}^2$.
This is [](#prop:sz-exponential-coefficients-equivalence); assertion 1 is
[](#conj:kls).
:::

:::{prf:proof}
Assume assertion 1. Necessarily $C\ge1$, by testing any isotropic law on a unit
linear function. At a fixed regular isotropic measure, let $T$ be a symmetric
$k$-tensor and put $T_i=(T_{i i_2\ldots i_k})_{i_2,\ldots,i_k}$.
Formal differentiation of the Appell generating identity gives

$$
\partial_iP_k^\nu[T]=kP_{k-1}^\nu[T_i],\qquad
\sum_i\|T_i\|_{\mathrm{HS}}^2=\|T\|_{\mathrm{HS}}^2.
$$

For $k\ge2$ the Appell polynomials on the right have mean zero. Every polynomial
and its derivatives have finite moments, so applying the assumed Poincaré inequality
is legitimate. It gives

$$
\begin{aligned}
\operatorname{Var}_\nu P_k[T]
&\le C\sum_i\mathbb E_\nu|\partial_iP_k[T]|^2\\
&=Ck^2\sum_i\operatorname{Var}_\nu P_{k-1}[T_i]\\
&\le Ck^2K_{k-1}(\nu)\|T\|_{\mathrm{HS}}^2.
\end{aligned}
$$

For $k=1$, isotropy gives $K_1(\nu)=1$. Taking the supremum and inducting yields
$K_k(\nu)\le C^{k-1}(k!)^2$ and hence the claimed sharper coefficient bound.
In particular $c_k(\nu)\le(\sqrt C)^k$, giving assertion 2.

Conversely assume assertion 2. Since $c_1(\nu)=1$, one has $A\ge1$.
The elementary inequality $k+1\le2^k$ for integers $k\ge1$ follows by induction,
so $(k+1)^2\le4^k$. Set $R=\max\{4A,2^{40}\}$. Then every measure in
assertion 2 satisfies, simultaneously for every $k\ge1$,

$$
c_k(\nu)\le A^k\le\frac{R^k}{(k+1)^2}.
$$

Apply [](#thm:sz-curvature-comparison) with $\epsilon=1$ and $\ell(k)=1$.
Every hypothesis is explicit: the measure is centered regular with covariance $I$,
its curvature is bounded below by its own fixed positive $a_\nu$, and
$R\ge2^{40}\epsilon^{-2}$. Thus for every dyadic $d\ge2$,

$$
C_P(\nu)\le32R^2\max\{1,a_\nu^{-1/(d+1)}\}.
$$

For this one fixed $\nu$, let $d$ run through arbitrarily large finite powers of two.
The scalar factor on the right tends to one because $a_\nu>0$ is fixed. Taking
its infimum proves $C_P(\nu)\le32R^2$. Neither the measure nor its curvature
lower bound varies while this infimum is taken. The resulting bound is uniform over
all regular isotropic measures and all dimensions.

Now fix any dimension and any isotropic log-concave $\mu$. By
[](#lem:sz-analytic-foundations) take regular isotropic $\mu_j\Rightarrow\mu$.
They all satisfy the same scalar Poincaré bound $32R^2$. Isotropy implies full
dimensionality, and a full-dimensional log-concave probability has a density.
The scalar stability clause of that lemma therefore passes the bound to every
locally Lipschitz finite-energy test under $\mu$, including the assertion that the
test belongs to $L^2(\mu)$. This proves assertion 1 with the stated constant.
:::

**Hypotheses and scope.** The constant $A$ in assertion 2 is outside the quantifiers
for degree, measure, dimension and regularization parameters. Bounds at each fixed
degree with unrelated constants do not meet this condition. Neither does choosing
a different $A$ at each iteration depth. The source's coefficient bounds with
iterated logarithms growing in the degree leave this condition unproved.
In the reverse implication the limit over dyadic degree is taken before varying the
regular measure; no uniform lower curvature bound or convergence of inverse operators
is needed.

**Fences respected.** The node has no proposed `bounded_by` edges. The equivalent-
strength warning [](#rem:relative-ceiling) is respected explicitly: the new criterion
renames the full target and is not an independent sufficient-condition advance.
The projection ceiling [](#rem:projection-ceiling) is respected because the criterion
quantifies over all symmetric tensors, not one-dimensional projections. No
occupation or moving-competitor estimate is inferred, so
[](#rem:crude-insufficient) and [](#rem:profile-circularity) are untouched.
No CMH or sharp gate-zero assertion is obtained. The proof has no open antecedent:
it establishes an equivalence whose two assertions are premises only within the
respective directions, and establishes neither assertion unconditionally.
