---
title: "Song–Zhang, second version: repeated refinement with summable losses"
numbering:
  enumerator: "9.%s"
---

(sec:sz-v2-proof)=
# Song–Zhang, second version: repeated refinement with summable losses

**What to retain.** Instead of the Poincaré constant, the second version of Song–Zhang iterates one number per measure, a common radius for the Appell coefficients of every degree, which controls the Poincaré constant up to a fixed factor paid once. Each refinement of that radius passes through curvature profiles and localization, as in the first version, but with margins $\alpha_i=2^{-i}/16$ whose costs have a bounded product, so infinitely many refinements leave a universal bound.

Song and Zhang's second version, *An O(1) Bound for the KLS Constant* [@SongZhang2026ConstantKLS], develops a second proof of KLS from the polynomial–curvature iteration. It is a new version of the same preprint; Chapter [](#sec:polynomial-curvature) concerns the first version [@SongZhang2026IteratedLogKLS], and the preceding chapter the proof of Bizeul, Klartag and Lehec (BKL). The statements below record results of the second version; each displays its status, and how it was checked is explained on the [welcome page](#sec:overview-checking).

The simplest distinction is already scalar. A fixed cost $C_*>1$ per repetition gives a factor $C_*^m$ after $m$ repetitions, however slowly $m$ grows. Costs $e^{C\alpha_i}$ with $\alpha_i=2^{-i}/16$ instead have product at most $e^{C/8}$. This arithmetic does not prove a refinement estimate: every repetition must still be admissible at its chosen starting depth, and its operator estimates must concern the same functions.

## Versions and the two closing mechanisms

| Submitted (UTC) | Source | Conclusion and role |
|---|---|---|
| 1 October 2026, 10:43:04 | Song–Zhang, first version [@SongZhang2026IteratedLogKLS] | Iterated-logarithm bound, reconstructed in Chapter [](#sec:polynomial-curvature) |
| 4 October 2026, 19:30:34 | BKL, first version [@BizeulKlartagLehec2026KLS] | Universal bound through cumulants and suspension, citing the first version of Song–Zhang; preceding chapter |
| 4 October 2026, 21:21:03 | Song–Zhang, second version [@SongZhang2026ConstantKLS] | Universal bound through repeated refinement and summable losses; this chapter |

These are two distinct closing mechanisms with a shared spectral foundation. The second version improves the iteration producing the coefficients; BKL estimate the exponential coefficient end point directly ([](#sec:bkl-proof)). The reconstruction in this chapter uses nothing from BKL; Chapter [](#sec:kls-synthesis) compares these with the BK proof.

## The argument in outline

The quantity improved throughout the proof is a single radius for the whole coefficient hierarchy. The first improvement replaces exponential cost in the logarithmic depth by polynomial cost. Repeating this improvement reduces the number of logarithms itself, initially at a fixed cost per repetition. The last improvement makes these costs arbitrarily close to one, while retaining earlier coefficient bounds to control the larger degree ranges that appear.

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

Section 6 of the source replaces the exponential depth cost of the first version by a polynomial cost. Its inverse-gradient blocks retain centering and symmetry information over many steps instead of charging a fixed loss at each step.

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

The source's final refinement uses a degree cutoff of order $\delta^{-2}$ and a starting depth of order $\delta^{-12}$. The smaller multiplier is useful only if those growing thresholds remain admissible. Earlier coefficient estimates are retained on the degree ranges where they are stronger; the [finite-chain estimate](#prop:sz-v2-finite-chain-blocks) has constants independent of how many such estimates are kept. The following two statements express the resulting profile improvement.

:::{prf:lemma} Outer round with a retained profile
:label: lem:sz-v2-profile-refinement
Fix a universal valid coefficient seed $G_*$ satisfying the seed conditions
of [](#prop:sz-v2-finite-chain-blocks), with its fixed cutoff constants.
Use the functions in [](#def:sz-v2-height-profiles), and set
$\widehat W_{m,\delta}(x)=\max\{W_m(x),\bar t(\delta^{-1})\}$.
All radius bounds below are uniform over every dimension and every measure
in [](#def:sz-v2-common-radius), for every admissible lower curvature $a>0$.
There are universal $A_0,C_R,C_Q,C_b,C_b',C_r,D_r\ge1$ such that the following holds for every finite $S_*\ge1$ (the additional allowance $b_*$ may depend on $S_*$). For each integer $m\ge0$ and $0<\delta\le1/16$, suppose $V=W_m$ or $V=\widehat W_{m,\delta}$, $1\le S\le S_*$,
$A\ge A_0$, $R_\delta=\lceil C_R\delta^{-12}\rceil$, and
$$
 \mathcal A\le A[V(r)+S]^{1/3}\mathcal L_r(a^{-1})^2
 \qquad(r\ge R_\delta).                          
$$
Then the following function is a valid coefficient cap, meaning
$c_k\le H(k)^{k-1}$ for every centered log-concave covariance contraction:
$$
 H(x)^2=\min\{G_*(x)^2,e^{3\delta}A[V(r_\delta(x))+S]^{1/3}\},
 \quad r_\delta(x)=\max\{R_\delta,\lceil C_rt(x)\rceil+
                                      \lceil D_r/\delta\rceil\}.
$$
Optionally retain earlier caps, with margins $\delta=\alpha_{N-1}\le\cdots\le\alpha_0\le1/16$,
where $N\ge1$ is finite and the newest cap is $H_{N-1}=H$. For every
$0<\epsilon\le\delta$, put $\alpha_N=\epsilon$,
$K_l=\lceil C_{\rm cut}\alpha_l^{-2}\rceil$ and
$\Xi_l=\lceil4C_{\rm deg}\alpha_l^{-1}K_{l+1}\rceil$. Require
$(1+\alpha_l)H_l(\Xi_l)^2\le A(4+S)^{1/3}$ for $l<N-1$, and
$\max\{C_0G_*(16K_0)^2,C_0\}\le A(4+S)^{1/3}$.
All $H_l$ are nondecreasing valid coefficient majorants between $1$ and
$G_*$ for every centered log-concave covariance contraction. With a fixed sufficiently large
$b_*$ with $b_*\le C\log(e+S_*)$ for one universal $C$, put
$$
 D_*=V(\epsilon^{-1})+S+b_*4^{-m},\qquad0<\epsilon\le\delta.
$$
Then, for every $j\ge1$, odd $Q\ge \min\{q\ge C_Q\epsilon^{-4}:q\text{ odd}\}$, and
$r\ge r_0(Q):=\max\{R_\delta,\lceil C_bt(Q)\rceil+
\lceil C_b'/\epsilon\rceil\}$,
$$
 \mathcal A\le e^{16\delta+24\epsilon j}A
       \max\{t_j(Q),D_*\}^{1/3}(r+1)^{1/Q}\mathcal L_r(a^{-1})^2.
                                                               
$$
For the one-cap case, the original-seed floor can instead be bounded
by $e^{4\delta}A D_*^{1/3}$. The same conclusion holds.
:::

The radius bound first gives a coefficient cap through static transfer. One then divides degrees among retained caps and applies the finite-block construction with the corresponding margins. Terminal-degree distortion controls the logarithms introduced by localization. The factors $e^{16\delta}$ and $e^{24\epsilon j}$ record distinct costs: forming the new cap and repeating the inner improvement. Their explicit dependence on both margins is what permits a later summable choice.

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
