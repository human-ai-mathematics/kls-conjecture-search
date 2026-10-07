---
title: "Actual inverse-gradient blocks: Green estimates, restart, and extension"
ledger-node:
  - lem:sz-v2-orbit-green-restart
  - lem:sz-v2-block-extension
  - lem:sz-v2-block-propagation
numbering:
  enumerator: "145.%s"
---

*Part of the second version of Song–Zhang, Chapter [](#sec:sz-v2-blocks); the reading order is on the [full proofs](#sec:proofs-sz-v2) page.*

**Overview.** This proves the generic mechanisms of
[](#lem:sz-v2-orbit-green-restart), [](#lem:sz-v2-block-extension), and
[](#lem:sz-v2-block-propagation). The starting assumptions of each lemma
are explicit; no claim is made here that a particular degree majorant
satisfies the raw-frame hypotheses. These mechanisms underlie Sections 8–9
of [@SongZhang2026ConstantKLS].

**Dependencies.** Use [](#lem:sz-analytic-foundations),
[](#lem:sz-v2-operator-block-primitives), and
[](#lem:sz-v2-normalized-hierarchy). The skew compensation is derived below.
No height-reduction theorem, small-loss profile, summable profile, BKL
result, or KLS conclusion is used.

Write $H=-\Delta+\nabla W\cdot\nabla$ on centered $L^2(\mu)$,
$B=H^{-1}$, $Lf=\mathbb E[Xf]$, and $\mathcal T=P_+\nabla B$,
where $P_+$ centers every output component. All operators act componentwise
on finite direct sums with all ordered output indices retained. The law
is centered and regular, has covariance at most $I$, and curvature at least
$aI$, $a>0$. The generic sequence and norm lemmas also apply abstractly.

:::{prf:lemma} Two-block Green estimate
:label: lem:sol-sz-v2-green-sequences
Fix $K\geq1$. There are $z_0(K)$, $c_0(K)>0$ and $C(K)$ with the
following property. Let integers $m\geq2d\geq4$ and numbers $z\geq z_0$,
$\gamma\geq0$ satisfy $\gamma m^2/z\leq c_0$.
Suppose nonnegative sequences $b_j$ ($j\geq0$), $l_j,D_j$ ($j\geq1$)
obey
$$
 b_0=b_m=1,\quad b_{j+m}\leq b_j,\quad
 b_{j+1}\leq(1+2/z)b_j,\quad l_1\leq2,
$$
and
$$
 D_j\leq z(b_{j+1}-2b_j+b_{j-1})+l_j.
$$
Let $a_s\geq0$ have finite support and satisfy
$\sum_sa_s\leq K/z$, $\sum_ssa_s\leq K/z$.
Let $h_j\geq0$. With $D_j=0$ for $j\leq0$, assume, for $j\geq2$,
$$
 l_j\leq h_j+\sum_{s\geq1}a_sD_{j-s},\qquad
 \sum_{j=2}^{2d-2}j h_j\leq K/z,\qquad
 h_j=\gamma b_{j-d+1}\quad(j\geq2d-1).
$$
Then $1/2\leq b_j\leq2$ for $0\leq j\leq m$, $b_j\leq2$ for
every $j\geq0$, and for $1\leq J\leq m/4$,
$$
 \sum_{k=2}^{J+1}\sum_{j=k}^{m+k-1}l_j\leq C/z+C\gamma Jm.
$$
:::

:::{prf:proof}
All sums below are finite; $C$ depends only on $K$. Put
$S=\sum_{j=0}^{m-1}b_j$, $L_1=\sum_{j=1}^m l_j$ and
$D_1=\sum_{j=1}^mD_j$. The first telescope is
$$
 D_1\leq L_1+z(b_{m+1}-b_1)\leq L_1,
$$
since $b_{m+1}\leq b_1$. On this block the terminal coherent sum is
at most $\gamma S$, and all convolution source indices are less than $m$.
Thus
$$
 L_1\leq2+K/z+\gamma S+(K/z)D_1.
$$
Choose $z\geq2K$. Absorption gives
$D_1,L_1\leq C(1+\gamma S)$ and
$\sum_{j=2}^m l_j\leq C/z+C\gamma S$.
It also gives the boundary estimate
$z(b_1-b_{m+1})\leq L_1$.

For $\delta_j=b_j-b_{j-1}$, the defect inequality implies
$\delta_{j+1}\geq\delta_j-l_j/z$. Since
$\sum_{j=1}^m\delta_j=0$, some $\delta_j$ is nonnegative; propagating
from that index gives $\delta_{m+1}\geq-L_1/z$.
On the other hand, $b_{2m}\leq1$ and
$\delta_{2m+1}\leq2b_{2m}/z\leq2/z$.
Telescoping the defect inequality over the second block and adding the
first block yields
$$
 D_{\rm tot}:=\sum_{j=1}^{2m}D_j
 \leq\sum_{j=1}^{2m}l_j+2+L_1.
$$
The coherent sum through $2m$ is at most $K/z+2\gamma S$, because
$\sum_{j=0}^{2m-1}b_j\leq2S$. A second absorption proves
$$
 D_{\rm tot}\leq C+C\gamma S,\qquad
 \sum_{j=2}^{2m}l_j\leq C/z+C\gamma S. \tag{G1}
$$

Fix $1\leq q<m$, and extend
$g_q(j)=\min\{j,q\}(m-\max\{j,q\})/m$ by zero outside $1\leq j<m$.
It is nonnegative and globally one-Lipschitz. The discrete second
differences give exactly
$$
 \sum_jg_q(j)(b_{j+1}-2b_j+b_{j-1})=1-b_q.
$$
For $E=\sum_jg_q(j)l_j$ and $F=\sum_jg_q(j)D_j$ this gives
$F\leq E+z(1-b_q)\leq E+z$.
The term $j=1$ contributes at most two. The early coherent terms
contribute at most $K/z$, since $g_q(j)\leq j$; the later terms at
most $\gamma mS$. Reindex the convolution and use
$g_q(j+s)\leq g_q(j)+s$ to obtain
$$
 E\leq2+K/z+\gamma mS+(K/z)F+(K/z)D_1.
$$
By the preceding estimates, absorption gives $E\leq C+C\gamma mS$.
Since $F\geq0$, the Green identity implies
$b_q\leq1+C/z+C\gamma mS/z$. Setting
$M=\max_{0\leq q\leq m}b_q$ and using $S\leq mM$ yields
$M\leq1+C/z+Cc_0M$. Fix $z_0$ large and then $c_0$ small so
$M\leq2$. The shift inequality propagates this upper bound to all indices.

For the lower bound use the weight
$$
 n(j)=\#\{k\in\{2,\ldots,m+1\}:k\leq j\leq m+k-1\}.
$$
It is one-Lipschitz, supported in $[2,2m]$, and bounded by
$\min\{j-1,m\}$. With $E_n=\sum_jn(j)l_j$, $F_n=\sum_jn(j)D_j$,
telescoping each window gives
$$
 F_n\leq E_n+z(b_{2m+1}-2b_{m+1}+b_1)
 \leq E_n+L_1.
$$
The second inequality uses $b_{2m+1}\leq b_{m+1}$ and the first
boundary estimate. The coherent contribution is at most
$K/z+2\gamma mS$. Convolution reindexing, now using (G1), gives
$$
 E_n\leq K/z+2\gamma mS+(K/z)F_n+(K/z)D_{\rm tot}
 \leq C/z+C\gamma mS+(K/z)E_n.
$$
Therefore $E_n\leq C/z+C\gamma mS$.
Apply the Dirichlet Green identity on $[q,q+m]$ at $m$.
Both endpoint values are at most $b_q$, since $b_{q+m}\leq b_q$;
the lower bound $\Delta^2b_j\geq-l_j/z$ therefore implies
$$
 1=b_m\leq b_q+z^{-1}\sum_{j=q+1}^{q+m-1}G_{q,m}(j)l_j,
$$
where $G_{q,m}(j)=(\min\{m,j\}-q)(q+m-\max\{m,j\})/m$.
For $j\leq m$, this is at most $j-q\leq j-1=n(j)$; for $j>m$
it is at most $q+m-j\leq2m-j\leq n(j)$.
Thus $b_q\geq1-C/z^2-C\gamma mS/z\geq1/2$ by $S\leq2m$
and the same universal choices. Endpoints already equal one.

Finally replace the $m$ windows in $n$ by the $J$ windows starting
at $2,\ldots,J+1$. The new weight is still one-Lipschitz, at most
$\min\{j-1,J\}$, and supported inside $[2,2m]$. Its boundary telescope is
$z(b_{m+J+1}-b_{m+1}-b_{J+1}+b_1)\leq z(b_1-b_{m+1})\leq L_1$,
using $b_{m+J+1}\leq b_{J+1}$. Its coherent sum is at most
$K/z+2\gamma Jm$, now that $b_j\leq2$. The identical reindexing and
absorption give the asserted window estimate. This proves the lemma.
:::

:::{prf:lemma} A single restarted family with a matched budget
:label: lem:sol-sz-v2-actual-restart
Suppose $z=\|\mathcal T^m\|^{2/m}>0$ and a unit norm-attaining vector
$f$ gives $w_j=z^{-j/2}\mathcal T^jf$, $b_j=\|w_j\|_2^2$,
and $l_j=\|Lw_j\|^2$. Assume
$$
 b_{j+m}\leq b_j,\quad b_0=b_m=1,\quad
 1/2\leq b_j\leq2\ (0\leq j\leq m),\quad b_j\leq2\ (j\geq0),
$$
$$
 \sum_{j=2}^m l_j\leq K/z+K\gamma m,\qquad
 \sum_{k=2}^{J+1}\sum_{j=k}^{m+k-1}l_j\leq K/z+K\gamma Jm
 \quad(1\leq J\leq J_0),
$$
and $\|\operatorname{Sym}(Lw_1)\|^2\leq K/z$.
Here $1\leq J_0\leq m/4$ and $m\geq4$. Let $p\geq3$ be odd,
$\kappa\geq1$, and assume
$$
 {z^{p-2}\over4\kappa}\leq m\leq {4z^{p-2}\over\kappa},
 \qquad J_0\gamma zm\leq1.
$$
There is $C=C(K)$ such that, if $C\kappa z^{-p}\leq1/8$, one
centered unit starting family for the normalized inverse-gradient
hierarchy has energy $\nu$ and actual centering losses satisfying
$$
 \nu\leq{u\over1-C\kappa u^p},\qquad
 P_J\leq C\kappa u^p\quad(1\leq J\leq J_0),\qquad u=z^{-1},
$$
and the same family satisfies for every $N\geq0$
$$
 aV_N+X_N\leq\nu-u+uP_{N+1}.
$$
:::

:::{prf:proof}
Set $\mathcal W=\bigoplus_{j=0}^{m-1}w_j$,
$S_k=\sum_{j=k}^{m+k-1}b_j$ and $C_k=\sum_{j=k}^{m+k-1}l_j$.
Then $S_0=S_1\geq m/2$, and $S_{k+1}\leq S_k$ because
$S_{k+1}-S_k=b_{m+k}-b_k\leq0$. The family
$$
 U={\mathcal T\mathcal W\over\sqrt{zS_0}}
 $$
has norm one, since $\|\mathcal T\mathcal W\|^2=zS_1$.
Each component is the gradient of $B\mathcal W$ minus a constant
vector, hence its derivative is symmetric in its two newest slots.
Bochner gives
$\|H^{1/2}\mathcal T\mathcal W\|^2\leq\|\mathcal W\|^2=S_0$,
so its energy $e$ is at most $u$.
The direct-sum norm and the assumed loss bounds imply
$$
 s:=\|\operatorname{Sym}(LU)\|^2
 ={1\over S_0}\sum_{j=1}^m\|\operatorname{Sym}(Lw_j)\|^2
 \leq C/(zm)+C\gamma.
$$

Put $\beta=\|B^{1/2}U\|^{-2}$ and $F=\sqrt\beta B^{1/2}U$.
It is a centered unit family of energy $\beta\leq e$.
The normalized hierarchy first applies
$D=P_+\nabla H^{-1/2}$ and then applies $H^{-1/2}$ to the result,
rescaling to preserve that result's norm. Its removed mean at $F$
has squared norm $p_* =\beta\|LU\|^2$.

The skew contribution satisfies
$\beta\|\operatorname{Skew}(LU)\|^2\leq1-\beta/e$.
Indeed every unit skew tensor $C$ gives a vector family $CX$ of
Dirichlet norm one orthogonal in Dirichlet inner product to $U$.
Project $H^{-1/2}U$ orthogonally to $H^{1/2}U$; its squared norm is
$\beta^{-1}-e^{-1}$ because the inner product is $\|U\|^2=1$.
Duality over $C$ proves the claimed skew inequality, also for finite
direct sums. Consequently
$$
 1-p_*\geq\beta/e-\beta s=\beta(e^{-1}-s)>0.
$$
Bochner and Cauchy–Schwarz show that the mean energy of the normalized
successor, after making it a unit family, is at most
$$
 {\beta\over1-p_*}\leq {e\over1-es}
 \leq {u\over1-us}
 \leq {u\over1-C/(z^2m)-C\gamma/z}.
$$
Call this unit successor $G_0$. Its direction is exactly
$B^{1/2}\mathcal T^2\mathcal W$, so it is the actual two-step restart
of the orbit, rather than a separately selected low-energy family.

For any centered finite family $Y$ the identity
$\|B^{1/2}Y\|^2=\|\mathcal TY\|^2+\|LY\|^2$
follows by subtracting the mean from $\nabla BY$ and using the
Dirichlet identity. Thus the successive relative loss fractions of
$G_0$ are exactly
$$
 {C_k\over zS_{k+1}+C_k},\qquad k=2,3,\ldots.
$$
For $k\leq J_0+1$, the interval defining $S_{k+1}$ contains at least
$m-k\geq m-J_0-1\geq m/2$ indices in $[0,m]$, and hence
$S_{k+1}\geq m/4$. Successive unnormalized masses are at most one.
It follows that
$$
 P_J\leq {4\over zm}\sum_{k=2}^{J+1}C_k
 \leq C/(z^2m)+C\gamma J/z.
$$
All required successors are nonzero on this prefix by the same lower
window bounds. The length comparison gives $1/(z^2m)\leq4\kappa z^{-p}$,
and $J_0\gamma zm\leq1$ gives $\gamma J/z\leq1/(z^2m)$.
These observations prove the energy and prefix estimates with one $C$.

Finally every later nonzero hierarchy member has the form
$G_j=q_jB^{1/2}\mathcal T^{j+2}\mathcal W$ for a positive scalar $q_j$.
If $v_j,e_j$ denote its squared norm and energy, then
$$
 {v_{j+1}\over e_j}
 ={\|\mathcal T^{j+3}\mathcal W\|^2\over
   \|\mathcal T^{j+2}\mathcal W\|^2}
 =z{S_{j+3}\over S_{j+2}}\leq z.
$$
The hierarchy's Bochner/normalization recurrence gives
$aV_N+X_N\leq\nu-e_N$. Combining it with
$e_N\geq u v_{N+1}=u(1-P_{N+1})$ proves the matched budget.
If a later successor is zero, set all subsequent families to zero;
then $P_{N+1}=1$ and the same inequalities persist. All operations are
finite spectral-calculus and weak form operations covered by the analytic
foundations; no differentiability of $HU$ is asserted.
:::

:::{prf:lemma} Finite extension from a delayed loss estimate
:label: lem:sol-sz-v2-finite-extension
Let $q\geq3$ be odd, $C_F,C_\theta\geq1$, $u=z^{-1}$,
$\lambda\geq u/2$, and suppose an
actual centered unit hierarchy starts in direction $B^{1/2}Y$, with
energy $\nu\leq u/(1-a_qu^q)$ and matched budget
$X_M\leq\nu-u+uP_{M+1}$ for every $M$.
Fix $\kappa_q,\kappa_{q-2}\geq1$ and define
$$
 K_q=4(s_q+C_F\kappa_{q-2}+4C_\theta a_q+1),\quad
 p_*=K_qu^q,\quad T_*=\lfloor z^q/\kappa_q\rfloor.
$$
Assume $p_*\leq1/1024$, $a_qu^q\leq1/1024$, $z\geq8C_\theta$,
and the following delayed estimate is valid before, and at, a first
crossing of $p_*$, with its short prefixes justified by retained actual
losses:
$$
 P_N\leq s_qu^q+N\tau+{\theta\over\lambda}X_{\max\{N-2,0\}},
 \qquad \tau\leq C_F\kappa_q\kappa_{q-2}u^{2q},\quad
 \theta\leq C_\theta u.
$$
Then $P_N<p_*/2$ for every $N\leq T_*$, and
$$
 \|\mathcal T^m\|^{2/m}\geq z-(a_q+4K_q)z^{1-q}
 \qquad(1\leq m\leq T_*).
$$
:::

:::{prf:proof}
Let $D_0=\max\{\nu-u,0\}\leq2a_qu^{q+1}$.
For $N\geq3$ the matched budget bounds
$X_{N-2}\leq D_0+uP_{N-1}\leq D_0+uP_N$.
The assumed retained-prefix bound handles $N\leq2$.
At every justified $N\leq T_*$, including a putative first exit,
$$
 (1-2C_\theta u)P_N
 \leq s_qu^q+C_F\kappa_{q-2}u^q+4C_\theta a_qu^{q+1}
 \leq K_qu^q/4.
$$
The left coefficient is at least $3/4$, so $P_N\leq p_*/3$.
A first exit cannot occur. The lower bound $1-P_N>0$ and the retained
short prefixes ensure all families used in this argument exist. This
is a finite induction over $N$, not an estimate obtained by assuming
that normalizers remain bounded forever.

Write $Y_j=\mathcal T^jY$, $A_j=\|Y_j\|^2$, $B_j=\|LY_j\|^2$.
Each hierarchy member is a positive multiple of $B^{1/2}Y_j$.
Its mean energy $\eta_j=A_j/\langle Y_j,BY_j\rangle$ is at least
$\lambda$, and its relative loss is
$$
 {p_j\over v_j}={B_j\over\langle Y_j,BY_j\rangle}
 =\eta_j{B_j\over A_j}.
$$
Consequently $\sum_{j<m}B_j/A_j\leq P_m/[\lambda(1-p_*)]
\leq4K_qu^{q-1}$.
The identity $\mathcal T^*\mathcal T=B-L^*L$ gives
$A_1/A_0=\nu^{-1}-B_0/A_0$.
For $j\geq1$, Bochner gives
$\|H^{1/2}Y_j\|^2\leq A_{j-1}$, and Cauchy–Schwarz gives
$$
 A_j^2\leq\|H^{1/2}Y_j\|^2\langle Y_j,BY_j\rangle
 \leq A_{j-1}(A_{j+1}+B_j).
$$
Thus $A_{j+1}/A_j\geq A_j/A_{j-1}-B_j/A_j$.
Every ratio through $m$ is therefore at least
$\nu^{-1}-4K_qu^{q-1}\geq z-(a_q+4K_q)u^{q-1}$.
Multiplication bounds $\|\mathcal T^mY\|^2/\|Y\|^2$ below by
the $m$th power of this quantity. It is positive under the smallness
assumptions. Finite direct-sum amplification preserves the operator
norm, proving the assertion.
:::

:::{prf:lemma} Propagation from exact finite block norms
:label: lem:sol-sz-v2-block-propagation
Let $T$ be a bounded operator on a Hilbert space (or a compatible
graded family), $R=\|T\|^2$, and integers
$1<m_0<m_1<\cdots<m_s$ satisfy $m_{l+1}\geq4m_l$.
Put $z_l=\|T^{m_l}\|^{2/m_l}>0$. Suppose
$$
 z_l\leq R,\quad z_l\geq R/2,\quad
 z_{l+1}\geq z_l-\Delta_l,\quad
 \Delta_{l+1}\leq\Delta_l/2,
$$
and $m_{l+1}\Delta_l/z_l\leq\eta$ for every $l<s$.
If $m_0(R-z_s)/z_s\leq\eta_0$, then for all $h\geq0$,
$$
 \|T^h\|\leq z_s^{h/2}
 \exp\left({\eta_0\over2}+2\eta\min\{s,\log_4(h+1)+1\}\right).
$$
:::

:::{prf:proof}
Greedily divide $h$ by $m_s,m_{s-1},\ldots,m_0$ to write
$h=\sum_{l=0}^sn_lm_l+r$, $0\leq r<m_0$,
with $n_lm_l<m_{l+1}$ for $l<s$. Submultiplicativity and the exact
norm at each block give
$$
 {\|T^h\|\over z_s^{h/2}}
 \leq (R/z_s)^{r/2}\prod_{l<s}(z_l/z_s)^{n_lm_l/2}.
$$
The remainder contributes at most
$m_0(R-z_s)/(2z_s)\leq\eta_0/2$ to its logarithm.
The decrement hypotheses give
$(z_l-z_s)_+\leq\sum_{j=l}^{s-1}\Delta_j\leq2\Delta_l$.
Since $z_l/z_s\leq2$, each nonzero lower-level contribution is at
most $2m_{l+1}\Delta_l/z_l\leq2\eta$.
There are at most $s$ such levels. A level contributing a nonzero
digit has $m_l\leq h$, and $m_l\geq4^lm_0$; hence there are at most
$\log_4(h+1)+1$ of them. This proves the claim.
:::

**Fences respected.** The operator input uses the actual starting family
and its own matched budget. The scale $z$ is obtained from the exact orbit
window identity, not by replacing the global norm $R$ with $z$ in a generic
hierarchy estimate. No source-specific polynomial or height bound is claimed
without its hypotheses. No new `bounded_by` edges are proposed.
