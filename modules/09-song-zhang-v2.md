---
title: "Song–Zhang, second version: repeated refinement with summable losses"
numbering:
  enumerator: "9.%s"
---

(sec:sz-v2-proof)=
# Song–Zhang, second version: repeated refinement with summable losses

**What to retain.** Instead of the Poincaré constant, the second version of Song–Zhang (SZ v2) iterates one number per measure, a common radius for the Appell coefficients of every degree, which controls the Poincaré constant up to a fixed factor paid once. Each refinement of that radius passes through curvature profiles and localization, as in the first version (SZ v1), but with margins $\alpha_i=2^{-i}/16$ whose costs have a bounded product, so infinitely many refinements leave a universal bound.

This chapter works through the second version of Song and Zhang's preprint, *An O(1) Bound for the KLS Constant* [@SongZhang2026ConstantKLS]; Chapter [](#sec:polynomial-curvature) concerns SZ v1 [@SongZhang2026IteratedLogKLS], and the preceding chapter the proof of Bizeul, Klartag and Lehec (BKL). Why bounded costs per repetition do not suffice, and summable ones may, is the calibration of Section [](#subsec:kls-sz-v2-idea).

## Versions and the two closing mechanisms

| Date | Preprint | Conclusion and role |
|---|---|---|
| 1 October 2026 | Song–Zhang, first version [@SongZhang2026IteratedLogKLS] | Iterated-logarithm bound, Chapter [](#sec:polynomial-curvature) |
| 4 October 2026 | BKL, first version [@BizeulKlartagLehec2026KLS] | Universal bound through cumulants and suspension, citing SZ v1; preceding chapter |
| 4 October 2026 | Song–Zhang, second version [@SongZhang2026ConstantKLS] | Universal bound through repeated refinement and summable losses; this chapter |

SZ v2 and BKL are two distinct closing mechanisms on a shared spectral foundation. SZ v2 improves the iteration producing the coefficients; BKL estimate the exponential coefficient end point directly (Chapter [](#sec:bkl-proof)). The argument of this chapter uses nothing from BKL; Chapter [](#sec:kls-synthesis) compares both with the proof of Balasubramanian and Kasiviswanathan (BK).

## The argument in outline

The quantity improved throughout the proof is a single radius for the whole coefficient hierarchy, and four improvements bring it to a universal bound.

1. **Polynomial cost in the logarithmic depth.** [](#thm:sz-v2-iterated-curvature) replaces the factor $16^r$ of SZ v1 by $(r+1)^{1/3}$, because blocks of inverse-gradient iterates retain centering and symmetry information over many steps instead of charging a loss at each one; via the transfer, $\CP\lesssim(1+\log^*(n+2))^{1/3}$ ([](#thm:sz-v2-dimension-bound)).
2. **Height reduction.** Repeating the improvement replaces $\log^*$ by $\log^*\circ\log^*$, and so on, at a fixed cost $C_*$ per repetition ([](#prop:sz-v2-height-reduction)), which still grows with the number of repetitions.
3. **Multipliers close to one.** With a margin $\delta$, $m$ refinements cost $e^{C\delta m}$ ([](#prop:sz-v2-small-loss)), at the price of a degree cutoff of order $\delta^{-2}$ and a starting depth of order $\delta^{-12}$; earlier coefficient bounds are kept on the degree ranges where they are stronger.
4. **Summable costs.** The margins $\alpha_i=2^{-i}/16$ give a multiplicative cost at most $e^{C_A/8}$ and, once the growing starting depths are absorbed into the improving height profile, an additive cost of order $2^{-i}$ ([](#prop:sz-v2-summable-budgets)).

The main estimates appear first, ending with the universal bound. The [technical part](#sec:sz-v2-blocks) then explains how one family of inverse-gradient iterates supplies the centering, symmetry and energy estimates needed throughout. Full proofs are linked beside the statements.

## One radius for all degrees

For the standard Gaussian, $c_d=1/\sqrt{d!}$, so the coefficient radius below equals one. For a general regular law it is finite for each fixed measure; this does not initially give a bound uniform over measures. Finiteness must precede any argument using the supremum over all degrees.

:::{prf:definition} The common coefficient radius and restricted inverse gradient
:label: def:sz-v2-common-radius
Let $\mu=e^{-W}dx$ be a centered probability measure on $\mathbb R^n$ with
$W\in C^\infty$, $\operatorname{Cov}(\mu)\preceq I$, and
$aI\preceq D^2W\preceq bI$ for some $0<a\le b<\infty$.
On $\mathscr H=L^2_0(\mu)$ let $H$ be the diffusion operator of
[](#lem:sz-analytic-foundations), and let $P_+$ subtract componentwise means.
Define $\mathcal T=P_+\nabla H^{-1}$, with its iterates acting componentwise
and appending ordered tensor slots, and $R=\|\mathcal T\|_{\mathrm{op}}^2$.
For the Appell coefficients of [](#thm:sz-polynomial-variance), put
$$
c_d(\mu)=\sqrt{K_d(\mu)}/d!,\qquad
\mathcal A(\mu)=\max\{1,\sup_{d\ge2}c_d(\mu)^{2/(d-1)}\}.
$$
All tensor norms sum over ordered indices.
:::

:::{prf:proposition} A finite radius shared by every degree and block
:label: prop:sz-v2-common-radius
For every measure in [](#def:sz-v2-common-radius),
$$
\CP(\mu)-1\le R\le \CP(\mu),\qquad
1\le\mathcal A(\mu)\le\max\{1,R\},\qquad
c_d(\mu)\le\mathcal A(\mu)^{(d-1)/2}\quad(d\ge1).
$$
If $G:\mathbb N_{\ge1}\to[1,\infty)$ is nondecreasing and
$c_k(\mu)\le G(k)^{k-1}$ for every $k\ge1$, then, for every integer $m\ge1$,
$$
\mathcal A(\mu)\le\max\{G(m)^2,\|\mathcal T^m\|_{\mathrm{op}}^{2/m}\}.
$$
Moreover $\CP(\mu)\le2^{85}\mathcal A(\mu)$, with a constant independent
of the dimension and curvature bounds.
:::

The operator $\mathcal T$ differentiates after solving the diffusion Poisson equation and removes the mean. The removed linear component has norm at most one, which explains the comparison of $R$ with $\CP$. Iterating the Appell derivative identity tests finite powers of $\mathcal T$ against every higher degree. Low degrees are covered by $G(m)$; the remaining degrees are covered by the same operator power. The final spectral comparison gives $\CP\le2^{85}\mathcal A$. That fixed factor is paid once, after refining $\mathcal A$, and does not accumulate with the number of refinements.

## Polynomial cost in the logarithmic depth

Section 6 of the preprint replaces the exponential depth cost of SZ v1 by a polynomial cost. Its inverse-gradient blocks retain centering and symmetry information over many steps instead of charging a fixed loss at each step.

:::{prf:theorem} Polynomial cost for logarithmic curvature refinement
:label: thm:sz-v2-iterated-curvature
Set $\ell_0(x)=x$ and $\ell_{r+1}(x)=\log(e+\ell_r(x))$ for $x\ge0$.
There is a universal constant $C<\infty$ such that, for every integer
$r\ge1$, every dimension $n\ge1$, and every centered probability measure
$\nu(dx)=e^{-W(x)}dx$ on $\mathbb R^n$ with $W\in C^\infty$,
$\operatorname{Cov}(\nu)\preceq I$ and
$aI\preceq D^2W\preceq bI$ for some $0<a\le b<\infty$,
$$
\CP(\nu)\le C(r+1)^{1/3}\ell_r(a^{-1})^2.
$$
:::

The power $(r+1)^{1/3}$ improves the factor $16^r$ in [](#thm:sz-iterated-curvature), but still grows with the depth. The proof estimates the accumulated errors in the inverse-gradient hierarchy before applying the spectral comparison. This yields a curvature profile valid uniformly in $r$. The existing transfer [](#thm:sz-curvature-transfer) evaluates that profile at a curvature inverse of order $\log(en)$, giving the following consequence.

:::{prf:theorem} The first improved log-star dimension bound
:label: thm:sz-v2-dimension-bound
With $\ell_r$ as in [](#thm:sz-v2-iterated-curvature), there is a universal
constant $C<\infty$ such that every isotropic log-concave probability measure
$\mu$ on $\mathbb R^n$, $n\ge1$, satisfies, for every integer $r\ge1$,
$$
\CP(\mu)\le C(r+1)^{1/3}\ell_r(\log(en))^2.
$$
In particular,
$$
\CP(\mu)\le C'(1+\log^*(n+2))^{1/3},
$$
where $C'$ is universal and $\log^*x$ is the least number of successive
natural logarithms needed to bring $x$ to at most $1$.
:::

Choose enough logarithms to bound $\ell_r(\log(en))$ universally. Only $(r+1)^{1/3}$ remains, with $r$ of order $1+\log^*(n+2)$. This bound also supplies an initial coefficient estimate for the next improvement; it is not yet the final dimension-free estimate.

## Reducing the height at a fixed cost

There are now two kinds of iteration. The index $r$ counts logarithms of the inverse curvature. The index $j$ below counts repetitions of the improvement of that profile. For example, $t_1(Q)=t(Q)$ grows like $\log^*Q$, whereas $t_2(Q)=t(t(Q))$ applies the same reduction to that already slow growth. The averaged functions $W_m$ will let the proof control changing starting depths quantitatively.

:::{prf:definition} Height profiles for the Song–Zhang v2 iteration
:label: def:sz-v2-height-profiles
For $x\geq1$ put $t(x)=1+\log^*(x+2)$, where $\log^*y$ is the least
number of natural logarithms required to bring $y$ to at most one.
Let $t_0(x)=x$, $t_{j+1}(x)=t(t_j(x))$,
$\kappa(x)=\min\{j\geq0:t_j(x)\leq3\}$ and
$\chi(x)=\max\{3,1+\kappa(x)\}$.
For $f=t,\chi$ set
$$
 \bar f(x)=\max\left\{4,\frac14\int_0^4f(x+s)\,ds\right\},
 \qquad W_m(x)=\bar t(\bar\chi^{\circ m}(x)).
$$
For $x\geq0$ put $\ell_0(x)=x$, $\ell_{r+1}(x)=\log(e+\ell_r(x))$,
and $\mathcal L_r(x)=\ell_r(x)/\varrho$, where
$\varrho=\log(e+\varrho)$ is the unique positive fixed point.
The index $\kappa(x)$ is finite for every $x\geq1$.
:::

:::{prf:proposition} Repeated height reduction at a fixed cost
:label: prop:sz-v2-height-reduction
There are universal constants $A_1,C_*,C_e,C_b\ge1$ and an integer
$r_*\ge1$ such that, with $A_j=A_1C_*^{j-1}$ and
$r_Q=\max\{r_*,\lceil C_b t(Q)\rceil\}$, every measure of
[](#def:sz-v2-common-radius) with lower curvature bound $a>0$ satisfies
$$
\CP(\mu)\le A_j t_j(Q)^{1/3}(r+1)^{1/Q}\ell_r(a^{-1})^2
$$
for every integer $j\ge1$, every odd integer $Q\ge3$, and every integer
$r\ge r_Q$. Moreover every centered log-concave probability measure of
covariance at most $I$ satisfies, for all integers $j,d\ge1$,
$$
c_d(\mu)\le[C_e\sqrt{A_j}\,t_{j+1}(d)^{1/6}]^{d-1}.
$$
The functions $t_j$ and $\ell_r$ are those of [](#def:sz-v2-height-profiles).
The admissible starting depths $r_Q$ do not depend on $j$.
:::

The proof keeps a static coefficient bound throughout all inner depths. Finite operator blocks improve that bound, and localization converts the improved curvature estimate into a new coefficient bound. Repetition replaces $t_j$ by $t_{j+1}$ without changing the admissible starting depth $r_Q$. The block estimates of Chapter [](#sec:sz-v2-blocks) explain how actual functions realize these bounds. The cost $A_j=A_1C_*^{j-1}$ still grows with the number of repetitions, so this estimate alone cannot give a universal constant by taking $j$ large.

## Refinements with a multiplier close to one

The final refinement of the preprint uses a degree cutoff of order $\delta^{-2}$ and a starting depth of order $\delta^{-12}$. The smaller multiplier is useful only if those growing thresholds remain admissible. Earlier coefficient estimates are retained on the degree ranges where they are stronger; the [finite-chain estimate](#prop:sz-v2-finite-chain-blocks) has constants independent of how many such estimates are kept. One outer round turns a radius bound into a new coefficient cap and then into an improved radius bound, with a cost $e^{16\delta}$ for forming the new cap and $e^{24\epsilon j}$ for repeating the inner improvement; this is [](#lem:sz-v2-profile-refinement), stated with the technical estimates in Chapter [](#sec:sz-v2-blocks). Its explicit dependence on both margins gives the following profile improvement.

:::{prf:proposition} Prescribed-depth profiles with a small multiplicative loss
:label: prop:sz-v2-small-loss
There are universal $A_0,C,C_R,D\geq1$ such that, for every
$0<\delta\leq1/16$, on setting
$$
 R_\delta=\lceil C_R\delta^{-12}\rceil,\qquad
 S_m=1+2D\sum_{l=0}^{m-1}4^{-l},\qquad
 \widehat W_{m,\delta}(x)=\max\{W_m(x),\bar t(\delta^{-1})\},
$$
every $m\geq0$ integer, every $r\geq R_\delta$ integer, and every
centered regular log-concave measure $\mu$ with covariance at most $I$
and curvature at least $aI$, $a>0$, satisfy
$$
 \mathcal A(\mu)\leq A_0e^{C\delta m}
 [\widehat W_{m,\delta}(r)+S_m]^{1/3}\mathcal L_r(a^{-1})^2.
$$
Here $\mathcal A$ is the common coefficient radius of
[](#def:sz-v2-common-radius), and the scalar functions are those of
[](#def:sz-v2-height-profiles).
:::

For a prescribed finite number $m$ of refinements, choose the margin $\delta$ before iterating. The multiplier is $e^{C\delta m}$, and $S_m$ stays bounded because its increments form a geometric series. The retained floor $\bar t(\delta^{-1})$ and the threshold $R_\delta$ keep the cost of that small margin visible. Taking $m$ large with $\delta$ fixed would still lose a uniform constant; the next estimate varies the margin from one repetition to the next.

## Summable costs and the universal bound

The choice $\alpha_i=2^{-i}/16$ has $\sum_{i\ge0}\alpha_i=1/8$. Thus the multipliers can have a bounded product. The additional task is to absorb $R_i$, which grows like $2^{12i}$, into the improving height profile $W_i$. The proof first uses how $W_i$ behaves under fixed powers of its argument, then its contraction near four. Applying only a Lipschitz estimate directly to $R_i$ would leave a growing error. With the two estimates combined, the additive cost is of order $2^{-i}$ and is summable too.

:::{prf:proposition} Profiles with summable multiplicative and additive costs
:label: prop:sz-v2-summable-budgets
There are universal $A_0,C_A,C_R,B\geq1$ such that, on setting
$$
 \alpha_i=2^{-i}/16,\quad R_i=\lceil C_R\alpha_i^{-12}\rceil,
 \quad A_i=A_0\exp\left(C_A\sum_{l=0}^{i-1}\alpha_l\right),
 \quad S_i=1+B\sum_{l=0}^{i-1}2^{-l},
$$
every $i\geq0$ integer, every $r\geq R_i$ integer, and every centered
regular log-concave measure $\mu$ with covariance at most $I$ and
curvature at least $aI$, $a>0$, satisfy
$$
 \mathcal A(\mu)\leq A_i[W_i(r)+S_i]^{1/3}\mathcal L_r(a^{-1})^2.
$$
The functions and radius are those of [](#def:sz-v2-height-profiles)
and [](#def:sz-v2-common-radius). In particular
$A_i\leq A_0e^{C_A/8}$ and $S_i\leq1+2B$ uniformly in $i$.
:::

The induction retains every earlier valid coefficient cap but uses each on a disjoint range of degrees. It therefore pays no factor equal to the number of retained caps. The finite-chain construction supplies one starting family with matched energy and centering losses; the outer profile estimate applies to that family. Threshold absorption accounts for the next starting depth through the increment of $S_i$, while the increment of $\log A_i$ pays the multiplicative cost.

:::{prf:theorem} The universal bound of Song–Zhang v2
:label: thm:sz-v2-kls
There is a universal constant $C<\infty$ such that, for every $n\ge1$ and
every isotropic log-concave probability measure $\mu$ on $\mathbb R^n$,
every real locally Lipschitz function $f$ with
$\int|\nabla f|^2d\mu<\infty$ belongs to $L^2(\mu)$ and satisfies
$$
\operatorname{Var}_\mu(f)\le C\int|\nabla f|^2d\mu.
$$
:::

Fix one regular measure and put $x=\max\{1,a^{-1}\}$. Choose a finite $i$ with $W_i(x)=4$, then choose $r=R_i+\lceil C_*t(x)\rceil$ with $C_*$ universal and sufficiently large. The normalized logarithm $\mathcal L_r(a^{-1})$ is bounded universally, and threshold absorption gives $W_i(r)\le4+b2^{-i}$. The bounded profiles therefore give a universal radius bound, and [](#prop:sz-v2-common-radius) converts it to a Poincaré bound once. Pass this scalar inequality to regular approximants using [](#lem:sz-analytic-foundations); no supremum over degrees passes through weak convergence. Clipping and truncation give both $L^2$ integrability and the finite-energy formulation above.
