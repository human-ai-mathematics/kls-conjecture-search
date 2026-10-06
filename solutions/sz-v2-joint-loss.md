---
title: "Song–Zhang v2: raw joint frames and delayed hierarchy losses"
ledger-node:
  - lem:sz-v2-raw-joint-frame
  - lem:sz-v2-propagated-joint-loss
numbering:
  enumerator: "146.%s"
---

**Overview.** This reconstructs the joint raw-orbit estimate and its normalized
hierarchy version from source Sections 8.3–8.4 of
[@SongZhang2026ConstantKLS]. The two claims are independent of any height
profile or block realization.

**Dependencies.** Use [](#def:sz-v2-common-radius),
[](#lem:sz-v2-joint-frame), [](#lem:sz-v2-operator-block-primitives),
[](#lem:sz-v2-normalized-hierarchy), and the Appell testing identity in
[](#prop:sz-v2-common-radius). All measures are centered regular covariance
contractions with positive lower curvature. All output indices are ordered
and retained in the Hilbert–Schmidt norms. Put $C_F=10^4$.
The operator notation and hierarchy sums are those of the two operator
lemmas. No BKL or KLS bound, or consequence of either, is used.

## Two joint-frame estimates

:::{prf:lemma} Raw moments and propagated normalization losses
:label: lem:sol-sz-v2-height-joint
Let $z>0$, $w_j=z^{-j/2}\mathcal T^jf$, $b_j=\|w_j\|^2$,
$l_j=\|Lw_j\|^2$, and $D_j=\|\nabla(B-zI)w_j\|^2$ for $j\ge1$.
If $\|\mathcal T^h\|\le E z^{h/2}$ for $h\ge0$, then for dyadic
$d\ge2$ and $j\ge2d-1$,
$$
 l_j\le C_Fd c_d^2z^{-(d-1)}b_{j-d+1}
 +108C_FE^2\sum_{k<d\ {\rm dyadic}}k^5c_k^2z^{-k}
       \sum_{h=1}^{3k-1}D_{j-k+1-h}.                 \tag{B1}
$$
If $0<z\le R$, without a global power bound the same formula holds with $E^2$ in
the $k$ summand replaced by $(R/z)^{3k-2}$.
If instead $\|\mathcal T^h\|\le E(h+1)^\alpha z^{h/2}$ for
$0\le\alpha\le1$, (B1) holds with $E^2$ replaced by
$E^2(3k)^{2\alpha}$ in its $k$ summand.

For an actual normalized hierarchy with a centered unit starting family,
suppose instead
$\|\mathcal T^h\|\le E(h+1)^\alpha z^{h/2}$, where $0\le\alpha\le1$.
Let $d_0\le d$ be dyadic and $J=2d_0-1$. On any prefix whose required
normalizers are at most $B_*$ put $t_* =\max\{1,B_*z\}$ and
$$
 \theta=5184C_FE^2\sum_{k<d\ {\rm dyadic}}
       k^8(B_*t_*^3)^k c_k^2,
$$
$$
 \Delta=P_J+2C_F\sum_{d_0\le k<d\ {\rm dyadic}}k^2B_*^kc_k^2,
 \qquad \tau=C_FdB_*^dc_d^2.
$$
Then, on each such justified prefix,
$$P_N\le\Delta+N\tau+(\theta/\lambda)X_{\max\{N-2,0\}}. \tag{B2}$$
For a prefix shorter than $J$, its retained actual losses suffice.
:::

:::{prf:proof}
Put $Q_kh=\mathbb E[\mathcal A_kh]$. Its norm is $k!c_k$.
The testing identity proved in [](#prop:sz-v2-common-radius) gives
$$
 \mathsf P_kQ_1w_j=
 \frac{Q_kw_{j-k+1}}{k!z^{(k-1)/2}}.              \tag{B3}
$$
The first $k$ slots are the coordinate slot and the $k-1$ newest
derivative slots. Each fresh adjacent swap in the remaining family has
norm at most $2\sqrt{D_i/z}$ by the operator primitive. After $h-1$
further steps its norm is multiplied by at most $E$ under the assumed
global bound. In the local version it is multiplied by
$(R/z)^{(h-1)/2}$. These componentwise operators commute with all
permutations of older slots.

Sorting a permutation of $N$ slots by adjacent swaps uses each adjacent
position at most $N$ times. To see this, insert the letters successively
into their required positions; a given boundary is crossed by at most
the number of letters. Telescoping the orthogonal products and averaging
therefore bounds the distance to the symmetric subspace by $N$ times
the sum of the adjacent errors. Apply this with $N=3k$ to the next
$3k$ slots after the first symmetric block. It yields
$$
 \|(I-\mathsf S_k)\mathsf P_kQ_1w_j\|
 \le6kE c_kz^{-k/2}
       \sum_{h=1}^{3k-1}\sqrt{D_{j-k+1-h}}.
$$
For $k<d$ and $j\ge2d-1$, the smallest index is
$j-4k+2\ge1$, so every fresh swap used is a genuine derivative swap.
The terminal projection in (B3) has norm at most
$c_dz^{-(d-1)/2}\sqrt{b_{j-d+1}}$.
Cauchy–Schwarz over fewer than $3k$ defects and
[](#lem:sz-v2-joint-frame) prove (B1). In the local version the longest
propagation has at most $3k-2$ steps and $R/z\ge1$; replacing its squared norm by
$(R/z)^{3k-2}$ gives the stated variant.
The polynomial-envelope variant charges at most
$E^2(3k)^{2\alpha}$ for that entire propagation, by the same argument.

For (B2), define $T_j=\sqrt{\beta_j}Q_1u^{j-1}$ for $j\ge1$;
its squared norm is $p_j$. Repeated testing gives
$$
 \mathsf P_kT_j=
 \frac{\prod_{i=0}^{k-1}\sqrt{\beta_{j-i}}}{k!}Q_ku^{j-k}.
$$
Since $\|u^{j-k}\|\le1$, the terminal squared norm is at most
$B_*^kc_k^2$. For completeness the inverse-normalization defect is
$$
 z^i=B^{1/2}F_{i+1}-\beta_{i+1}^{-1/2}u^i,
 \qquad \|\nabla z^i\|^2=\chi_i/\beta_{i+1}.
$$
This follows by expanding its Dirichlet square and using
$F_{i+1}=\sqrt{\beta_{i+1}}B^{1/2}u^i$.
Thus
$u^{i+1}=\beta_{i+1}^{-1/2}P_+\nabla u^i+P_+\nabla z^i$.
The first term has symmetric newest slots and the second contributes
a swap of norm at most $2\sqrt{\chi_i/\lambda}$.
Propagating an old swap uses the scalars of the original entire family,
not freshly chosen normalizers: the next $h-1$ maps have norm at most
$Eh^\alpha t_*^{(h-1)/2}$. The same sorting argument gives
$$
 \|(I-\mathsf S_k)\mathsf P_kT_j\|
 \le6kE B_*^{k/2}c_k\lambda^{-1/2}
 \sum_{h=1}^{3k-1}h^\alpha t_*^{(h-1)/2}
       \sqrt{\chi_{j-k-h}}.
$$
The sum's convolution kernel has total mass at most
$3k(3k+1)^\alpha t_*^{3k/2}$. Weighted Cauchy–Schwarz and summation
over $j$ bound its squared convolution by the square of that mass times
the sum of the source $\chi$'s. Multiplication by the joint-frame weight
$C_Fk^2$ and $(3k+1)^{2\alpha}\le16k^2$ gives the stated $\theta$.
Every source index is at most $N-3$ in a prefix $j<N$.
Keep $p_0,\ldots,p_{J-1}$ exactly. Subsequently use the largest
available dyadic degree, capped at $d$; degree $k$ is available when
$j\ge2k-1$. Each nonterminal degree is used at most $2k$ times.
Their coherent terms sum to the second part of $\Delta$, while the
terminal coherent terms sum to at most $N\tau$. This proves (B2).
:::


**Fences respected.** The estimates are conditional on their explicitly stated
power envelopes and normalizer bounds. Neither estimate constructs those
bounds or asserts a uniform coefficient radius. No `bounded_by` edge is
proposed.
