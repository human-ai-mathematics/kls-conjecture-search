---
title: 'Song–Zhang v2: summable budgets and starting depths'
ledger-node:
  - lem:sz-v2-profile-threshold
  - prop:sz-v2-summable-budgets
numbering:
  enumerator: "141.%s"
---

*Part of the second version of Song–Zhang, Chapter [](#sec:sz-v2-blocks); the reading order is on the [full proofs](#sec:proofs-sz-v2) page.*

**Overview.** This develops the finite-chain argument for
[](#prop:sz-v2-summable-budgets), corresponding to Propositions 9.23–9.25
of [@SongZhang2026ConstantKLS]. The scalar threshold and degree-sum
arguments are combined with the independently reconstructed finite-chain
block theorem and the near-unit depth/outer-round lemmas from the small-loss
dossier to close the full profile induction.

**Dependencies.** Use [](#def:sz-v2-common-radius),
[](#prop:sz-v2-common-radius), and the functions and scalar lemmas in
[](#prop:sz-v2-small-loss). In particular $W_i=\bar t\circ\bar\chi^{\circ i}$
and $\mathcal L_r=\ell_r/\varrho$. All laws below are centered regular
log-concave measures with covariance at most $I$. No BKL result or KLS
conclusion is used.

## Uniform block construction

The disjoint-degree moment estimate and the full finite-chain block
realization are proved in [](#prop:sz-v2-finite-chain-blocks). Their
constants do not depend on the number of retained coefficient majorants.

## Paying the growing depth thresholds


Let
$$
 \alpha_i={2^{-i}\over16},\quad R_i=\lceil C_R\alpha_i^{-12}\rceil,
 \quad S_i=1+B\sum_{l<i}2^{-l},\quad
 A_i=A_0\exp\left(C_A\sum_{l<i}\alpha_l\right).
$$

:::{prf:lemma} Threshold absorption
:label: lem:sol-sz-v2-threshold-absorption
For fixed $C,p\geq1$ there is $b_{C,p}$ independent of $i$ with
$$
 W_i(C\alpha_i^{-p})\leq4+b_{C,p}2^{-i}.
$$
For fixed $C_R,C$ there is $b$ such that for all real $x\geq1$,
$$
 W_i(R_i+\lceil Ct(x)\rceil)\leq W_i(x)+b2^{-i}.
$$
:::

:::{prf:proof}
Since $\alpha_i^{-1}=16\cdot2^i$, the fixed-power inequality for $W_i$
first gives
$$
 W_i(C16^p(2^i)^p)\leq W_i(2^i)+b_{C16^p,p}4^{-i}.
$$
The Lipschitz bound at the fixed point four gives
$W_i(2^i)\leq4+4^{-i-1}(2^i-4)_+$, including $i=0$.
This proves the first assertion. Since $\alpha_i^{-12}\geq1$,
$R_i\leq(C_R+1)\alpha_i^{-12}$. Apply the sum estimate to
$R_i+\lceil Ct(x)\rceil$. Its first term is at most $4+b_12^{-i}$
by the first assertion. The second is at most
$W_i(x)+b_24^{-i}$, since $t(x)\leq C'(x+1)\leq2C'x$ and
$\lceil Ct(x)\rceil\leq C''x$. Because $W_i(x)\geq4$, taking
the maximum and paying the one sum error proves the claim.
The order of operations matters: applying Lipschitz directly to $R_i$
would multiply $4^{-i}$ by a quantity of order $2^{12i}$.
:::

:::{prf:theorem} Target bounded-amplitude profiles
:label: thm:sol-sz-v2-summable-target
The universal constants $A_0,C_A,C_R,B$ can be chosen so that every integer
$i\geq0$, every integer $r\geq R_i$, and every law in the stated regular
class with curvature at least $aI$, $a>0$, satisfy
$$
 \mathcal A\leq A_i[W_i(r)+S_i]^{1/3}\mathcal L_r(a^{-1})^2.
$$
Furthermore $A_i\leq A_0e^{C_A/8}$ and $S_i\leq1+2B$.
This is [](#prop:sz-v2-summable-budgets).
:::

## Retaining caps and closing the analytic induction

Suppose the profile has been established through stage $i$, and define
$$
 r_l(x)=\max\{R_l,\lceil C_rt(x)\rceil+\lceil D_r/\alpha_l\rceil\}
 \quad(0\leq l\leq i).
$$
The static transfer [](#prop:sz-v2-static-coefficient-transfer) gives the fixed valid coefficient
majorants
$$
 H_l(x)^2=\min\{G_*(x)^2,
 e^{3\alpha_l}A_l[W_l(r_l(x))+S_l]^{1/3}\}.
$$
Here $G_*$ is the universal original coefficient majorant; its validity
comes from the preceding height-reduction argument, not from KLS.
Indeed take $\Gamma^2=A_l[W_l(r_l(d))+S_l]^{1/3}/\varrho^2$ at the
fixed depth $r_l(d)$. It is at least one after a fixed choice of $A_0$.
The all-law profile gives the transfer hypothesis at that depth; burn-in
bounds $\mathcal L_{r_l(d)}(d)^2$ and $(1+r_l(d)^{-2})^2$ by
$e^{\alpha_l}$ each, leaving room in the displayed $e^{3\alpha_l}$.
No comparison with $C_P$ or continuity of the supremum defining
$\mathcal A$ is used. Once extracted, these majorants are retained unchanged.

For an additional $0<\epsilon\leq\alpha_i$, use
$K_l=\lceil L\alpha_l^{-2}\rceil$ through $l=i$,
$K_{i+1}=\lceil L\epsilon^{-2}\rceil$, and
$\Xi_l=\lceil4C_{\rm deg}\alpha_l^{-1}K_{l+1}\rceil$.
For $l<i$, geometric margins give
$\Xi_l\leq C\alpha_l^{-3}$ and
$r_l(\Xi_l)\leq C'\alpha_l^{-12}$. Therefore
$$
 W_l(r_l(\Xi_l))\leq4+b_{\rm old}2^{-l}.
$$
Taking $B\geq b_{\rm old}$ pays this error from the very next increment
of $S$, and $C_A\geq4$ gives, for $l<i$,
$$
 (1+\alpha_l)H_l(\Xi_l)^2\leq A_i(4+S_i)^{1/3}.
$$
Indeed $\log(1+\alpha_l)+3\alpha_l\leq4\alpha_l$ and
$A_i/A_l\geq e^{C_A\alpha_l}$. This is a maximum bound on each
retained floor, so the number of floors does not enter.

:::{prf:lemma} Realized outer round with all earlier caps
:label: lem:sol-sz-v2-chain-outer-round
For $0<\epsilon\le\alpha_i$, every $j\ge1$, odd $Q\ge Q_\epsilon$,
and $r\ge\max\{R_i,\lceil C_bt(Q)\rceil+\lceil C_b'/\epsilon\rceil\}$,
$$
 \mathcal A\le e^{16\alpha_i+24\epsilon j}A_i
 \max\{t_j(Q),D_i\}^{1/3}(r+1)^{1/Q}\mathcal L_r(a^{-1})^2,
 \qquad D_i=W_i(\epsilon^{-1})+S_i+b_{\rm pre}4^{-i}.
$$
:::

:::{prf:proof}
Apply [](#lem:sz-v2-profile-refinement) with $V=W_i$, $m=i$,
$\delta=\alpha_i$, $A=A_i$ and $S=S_i$. The newest cap is the
$H_i$ already extracted above. The earlier floors were bounded
individually above by $A_i(4+S_i)^{1/3}$, which is exactly the
retained-floor hypothesis of that lemma. The original-seed floor is
constant: $K_0=\lceil C_{\rm cut}\alpha_0^{-2}\rceil$ is fixed.
Increase $A_0$ once to bound $C_0G_*(16K_0)^2$ and $C_0$.
The finite-chain theorem is applied with $N=i+1\ge1$; its constants
are independent of $i$. Finally $S_i\le1+2B$, so one universal
$b_{\rm pre}$ serves every $i$. The outer-round proof supplies the
coefficient return, initialization, and full terminal-depth induction;
none of these is inferred from the block construction alone.
:::

:::{prf:proof} Closure of the outer induction
The stage-zero profile follows from the initialization proved in the
small-loss dossier with $W_0=\bar t$; its proof does not require the
constant branch of $\widehat W$. Increase $A_0,C_R$ once accordingly.
Use the realized outer-round estimate above at each subsequent stage. For a
prescribed $r\geq R_{i+1}$ let $j=\kappa(r)$,
$\epsilon=\alpha_i/(j+1)$, and take the least odd $Q$ at least
$\max\{Q_\epsilon,\alpha_i^{-1}\log(r+1)\}$.
The polynomial threshold calculation in the small-loss argument proves
$Q\leq r$ and that this $r$ is admissible, with a universal choice of $C_R$.
Consequently $t^{\circ j}(Q)\leq3<D_i$,
$(r+1)^{1/Q}\leq e^{\alpha_i}$, and $\epsilon j\leq\alpha_i$.

Use the product inequality and $j+1\leq\chi(r)$ to obtain
$$
 \begin{split}
 W_i(\epsilon^{-1})
 &\leq\max\{W_i(\chi(r)),W_i(\alpha_i^{-1})\}+b4^{-i}\\
 &\leq W_{i+1}(r)+b_{\rm ret}2^{-i}.
 \end{split}
$$
The last step uses threshold absorption, $W_{i+1}\geq4$, and
$W_i\circ\bar\chi=W_{i+1}$. Choose
$B\geq b_{\rm ret}+b_{\rm pre}$ in addition to its earlier requirement.
Then $D_i\leq W_{i+1}(r)+S_{i+1}$. The total multiplicative loss is
at most $e^{41\alpha_i}$, so $C_A\geq42$ covers it.
This proves the next profile. All choices are universal: the dependence
of $b_{\rm pre}$ and the threshold-absorption constants on $B$ is at
most $C\log(e+B)$, because $S_*=1+2B$ changes only the fixed
high-height cutoff, and that cutoff enters a fixed-power height bound.
Thus choose $B$ to satisfy $B\ge C\log(e+B)$ and all the finitely
many earlier lower bounds; then freeze it before the induction.

The realized recurrences satisfy
$$
 \sum_{l<i}\alpha_l\leq1/8,\qquad
 \sum_{l<i}2^{-l}\leq2,
$$
and therefore the stated bounds on $A_i,S_i$. Together with the preceding finite induction, these sums prove the
claimed bounded-amplitude profiles.
:::

**Fences respected.** Uniform admissibility is paid before choosing each
depth; no estimate for a growing starting depth is suppressed. No
uniform coefficient bound is inferred from the target or from BKL.
