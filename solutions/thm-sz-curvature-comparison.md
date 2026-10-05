---
title: "Polynomial coefficient profiles control the full spectral gap"
ledger-node: thm:sz-curvature-comparison
numbering:
  enumerator: "121.%s"
---

**Overview.** This reconstructs Section 5 of the version-pinned
[@SongZhang2026IteratedLogKLS]. The argument starts from a first eigenfunction,
iterates a normalized inverse square root followed by differentiation, and bounds
the mass removed by centering. A combinatorial recovery inequality converts
polynomial testing into a bound on this loss. A convolution estimate absorbs all
normalization defects, uniformly in the number of generations and the terminal
polynomial degree. The only quantitative input beyond the profile in the statement
is the universal coefficient estimate [](#thm:sz-polynomial-variance).

:::{prf:theorem} Coefficient profiles and curvature
:label: thm:sol-sz-curvature
Let $0<\varepsilon\le1$, let $\ell:\mathbb N\to[1,\infty)$ be nondecreasing,
and let $R\ge2^{40}\varepsilon^{-2}$. Let $\nu=e^{-W}dx$ be centered, with
$W$ smooth, $aI\preceq D^2W\preceq b_0I$ for finite $b_0\ge a>0$, and
$\operatorname{Cov}(\nu)\preceq I$. For the Appell polynomial determined by
$D^kP_k[T]=k!T$ and $\mathbb E D^jP_k[T]=0$ for $0\le j<k$, set
$K_k=\sup_{\|T\|_{\rm HS}=1}\mathbb E P_k[T]^2$ and $c_k=\sqrt{K_k}/k!$.
Suppose $c_k\le R^k\ell(k)^k/(k+1)^2$ for every $k\ge1$.
Then every dyadic integer $d\ge2$ satisfies
$$
 C_P(\nu)\le16(1+\varepsilon)R^2\ell(d)^2
 \max\{1,a^{-1/(d+1)}\}.
$$
This is the assertion [](#thm:sz-curvature-comparison).
:::

## Analytic setup and normalized families

The analytic preparation [](#lem:sz-analytic-foundations), proved in
[](#lem:sol-sz-operator), establishes the following facts for the present regular measure. The operator
$H=-\Delta+\nabla W\cdot\nabla$ is the self-adjoint operator associated with
the closed gradient form, its kernel is the constants, and its first positive
eigenvalue $\lambda=C_P(\nu)^{-1}$ is attained. Its form domain is the weighted
Sobolev space. On its operator domain,
$$
 \|Hg\|_2^2=\mathbb E\|D^2g\|_{\rm HS}^2+
 \mathbb E\langle D^2W\nabla g,\nabla g\rangle.
$$
In particular all second weak derivatives exist in $L^2$ and commute. Inverse
powers act on centered functions. For centered form-domain $h$,
$H^{-1/2}h\in\operatorname{Dom}(H)$,
$\|H H^{-1/2}h\|_2^2=\|H^{1/2}h\|_2^2$, and
$\|\nabla H^{-1/2}h\|_2^2=\|h\|_2^2$.
Polynomial tests belong to the form domain. These facts apply componentwise to
finite families, with summed squared norms.

Put $P_+h=h-\mathbb Eh$, $D=P_+\nabla H^{-1/2}$, and $Lh=\mathbb E[Xh]$.
Both $D$ and $L$ are contractions: for $L$ use
$\mathbb E(z\cdot X)^2\le|z|^2$ and duality. Testing the form against $x_i$
gives $\mathbb E\nabla H^{-1/2}h=LH^{1/2}h$.

For a nonzero centered form-domain family $u$, define
$$
 v=\|u\|_2^2,\quad b=\|H^{-1/2}u\|_2^2,\quad
 \beta=v/b,\quad h=\sqrt\beta H^{-1/2}u,\quad
 \chi=\|H^{1/2}u\|_2^2-\beta v.
$$
The scalar $\beta$ belongs to the entire family, not individual components.
Cauchy--Schwarz gives $v^2\le b\|H^{1/2}u\|_2^2$, whence
$\lambda\le\beta\le\|H^{1/2}u\|_2^2/v$ and $\chi\ge0$.
Furthermore
$$
 \|h\|_2^2=v,\qquad H^{1/2}h=\sqrt\beta u,
 \qquad
 z:=H^{-1/2}h-\beta^{-1/2}u
$$
satisfies the exact identity
$$
 \|\nabla z\|_2^2
 =\beta b-2v+\beta^{-1}\|H^{1/2}u\|_2^2=\chi/\beta.
$$
This uses spectral calculus and the form identity; it does not commute a
spatial derivative with an inverse spectral power.

Start with a centered unit first eigenfunction $F_0$. Set $u^j=DF_j$ and
normalize $u^j$ as above to obtain $F_{j+1}$, normalizer $\beta_{j+1}$,
and defect $\chi_j$. Write
$$
 v_j=\|F_j\|_2^2,\quad e_j=\|H^{1/2}F_j\|_2^2,\quad
 p_j=\|LH^{1/2}F_j\|^2,\quad E_j=e_j-\lambda v_j.
$$
The gradient before centering has norm squared $v_j$ and mean norm squared
$p_j$. Bochner applied to $H^{-1/2}F_j$ bounds its derivative energy by
$e_j-av_j$. Normalization removes exactly $\chi_j$. Thus
$$
 v_{j+1}=v_j-p_j,\qquad e_{j+1}\le e_j-av_j-\chi_j,
 \qquad 0\le E_{j+1}\le E_j+\lambda p_j-av_j-\chi_j. \tag{1}
$$
In particular $v_j\le1$, $e_j\le\lambda$, and $p_j\le\min(v_j,e_j)\le\lambda$.
At the first step, even if $u^0=0$,
$\lambda(1-p_0)\le\|H^{1/2}u^0\|_2^2\le\lambda-a$, so
$a\le\lambda p_0\le\lambda^2$. The same inequalities hold with zero
successors after a vanishing family, but normalizers will only be used on the
nonvanishing stopped prefix constructed below. Each $u^j$ is in the form domain
by Bochner; hence every operation on that prefix has the required domain.

## Recovering a partially symmetric tensor

:::{prf:lemma} Two-block recovery
:label: lem:sol-sz-block-recovery
Let $S\in\operatorname{Sym}^s(\mathbb R^n)\otimes
\operatorname{Sym}^l(\mathbb R^n)$, where $s\le q\le l$, and let $\mathsf P_q$
average permutations of the first $q$ slots. Then
$$
 \|\mathsf P_qS\|^2\ge
 \binom qs^{-1}\frac{(s+l-q)_{\underline s}}{l_{\underline s}}\|S\|^2.
$$
If $T$ is symmetric in its first $s$ slots, $S$ is its symmetrization in the
last $l$ slots, and $c$ is the reciprocal square root of the displayed
coefficient, then
$\|T\|\le c\|\mathsf P_qT\|+(c+1)\|T-S\|$.
Finite direct sums over other slots are permitted.
:::

:::{prf:proof}
Put $N=s+l$ and let $\mathcal M_k$ be the Euclidean space of functions on
$k$-subsets of $\{1,\ldots,N\}$. Let $U_k$ sum over contained $k$-subsets,
and $D_{k+1}=U_k^*$. Counting the diagonal and off-diagonal entries gives
$D_{k+1}U_k-U_{k-1}D_k=(N-2k)I$. If $D_jv=0$, induction gives
$$
 DU^rv=r(N-2j-r+1)U^{r-1}v,
 \qquad \|U^rv\|^2=r!\frac{(N-2j)!}{(N-2j-r)!}\|v\|^2.
$$
For $k<N/2$, the commutator makes $U_k$ injective and $D_{k+1}$ surjective.
Since $s\le N/2$, successive orthogonal decompositions into $\ker D_k$ and
$\operatorname{ran}U_{k-1}$ give
$\mathcal M_s=\bigoplus_{j=0}^s U^{s-j}\ker D_j$.
The summands are orthogonal by repeatedly moving a lowering operator to the
other factor. The incidence map $I_{q,s}=U^{q-s}/(q-s)!$ therefore has squared
singular values
$$
 \binom{q-j}{s-j}\binom{N-s-j}{q-s},\qquad 0\le j\le s.
$$
Their successive ratios are
$\frac{s-j}{q-j}\frac{N-q-j}{N-s-j}\le1$ (the trivial case $q=s$ gives
identity). Consequently
$I_{q,s}^*I_{q,s}\succeq\binom{N-2s}{q-s}I$.

For each $s$-subset $A$, move the first symmetric block of $S$ to $A$, giving
$S_A$ independently of internal orderings. For each $q$-subset $B$,
$\sum_{A\subset B}S_A$ is $\binom qs$ times an orthogonal permutation of
$\mathsf P_qS$. Apply the incidence bound to this tensor-valued list:
$$
 \binom Nq\binom qs^2\|\mathsf P_qS\|^2
 \ge\binom{N-2s}{q-s}\binom Ns\|S\|^2.
$$
Cancellation of factorials proves the claim. The robust version follows from
$\|T\|\le\|S\|+\|T-S\|$ and the contraction of $\mathsf P_q$.
:::

We will also use, for an $l$-slot array $Y$ and its adjacent transpositions $s_i$,
$$
 \|Y-\operatorname{Sym}_lY\|\le l\sum_{i=1}^{l-1}\|Y-s_iY\|. \tag{2}
$$
Indeed insertion sort writes each permutation with each generator at most $l$
times. For a product of isometries, telescope $I-U_1\cdots U_m$ as
$\sum_{i=1}^mU_1\cdots U_{i-1}(I-U_i)$; all differences are thereby applied to
the original array. Averaging the resulting bounds proves (2).

## Polynomial tests, adjacent swaps, and the dyadic loss

Let $\mathcal A_k$ be the tensor-valued Appell polynomial, so
$P_k[T]=\langle\mathcal A_k,T\rangle$, and put $Q_kh=\mathbb E[\mathcal A_kh]$.
Duality gives $\|Q_k\|\le\sqrt{K_k}$. If $\mathsf P_{k+1}$ symmetrizes the
$k$ polynomial indices and the newest derivative index, then for $j\ge1$
$$
 (k+1)\mathsf P_{k+1}Q_kDF_j
 =Q_{k+1}H^{1/2}F_j
 =\sqrt{\beta_j}Q_{k+1}u^{j-1}. \tag{3}
$$
To check this, pair against an arbitrary symmetric $(k+1)$-tensor, use
$\nabla P_{k+1}=(k+1)P_k$ with one free index, and test the form against
$H^{-1/2}F_j$. Centering contributes zero because $\mathbb E\mathcal A_k=0$.

Suppose the normalizers in question satisfy $\beta_j\le b\lambda$, $b\ge1$.
The normalization defect gives
$$
 u^{j+1}=\beta_{j+1}^{-1/2}P_+\nabla u^j+P_+\nabla z^j,
 \qquad \|\nabla z^j\|_2^2=\chi_j/\beta_{j+1}.
$$
The first term is symmetric in its newest two indices: $u^j$ is a centered
gradient and taking another weak derivative gives a Hessian. Thus the newest
swap has defect at most $2\sqrt{\chi_j/\lambda}$. Each subsequent map
$D\sqrt{\beta}H^{-1/2}$ has norm at most $\sqrt b$ and commutes with
permutations of old indices. Its scalar is kept fixed at the value for the
original entire family, even when the map is applied to a difference.
Numbering derivative slots newest first, the swap of slots $a,a+1$ in $u^J$
was created at $u^{J-a+1}$ and underwent exactly $a-1$ subsequent maps. Hence
$$
 \|u^J-s_au^J\|_2\le2b^{(a-1)/2}\sqrt{\chi_{J-a}/\lambda}. \tag{4}
$$
No old defect has been differentiated.

Fix an integer $L\ge3$ and put
$$
 B=2\sqrt{L/(L-2)},\qquad A=bB^2,\qquad J=B^4b^{L+1},\qquad
 m_d=(L+1)d/2-1.
$$
For $j\ge m_d$ and dyadic $d\ge2$, we claim
$$
 \sqrt{p_j}\le(A\lambda)^{d/2}c_d+
 \sum_{\substack{k<d\\k\text{ dyadic}}}t_k
       \sum_{a=1}^{Lk-1}\sqrt{\chi_{j-k-a}},
 \quad
 t_k=\frac{4Lk}{B}J^{k/2}c_k\lambda^{(k-1)/2}. \tag{5}
$$
Here and below dyadic indices start at one. To prove (5), set
$T_k=Q_ku^{j-k}$ at successive dyadic degrees. There are $k$ symmetric
polynomial slots and $j-k+1\ge Lk$ derivative slots for $k<d$.
Symmetrize the newest $Lk$ derivative slots to obtain $S_k$. The block lemma
with $(s,l,q)=(k,Lk,2k)$ has recovery constant
$$
 C_k^2=\binom{2k}k\frac{(Lk)_{\underline k}}{((L-1)k)_{\underline k}}
 \le4^k(L/(L-2))^k=B^{2k}.
$$
Every denominator factor exceeds $(L-2)k$, which proves this bound.
Repeated application of (3), whose inner projections are absorbed by the outer
symmetrization, yields
$$
 \|\mathsf P_{2k}T_k\|\le(b\lambda)^{k/2}\frac{k!}{(2k)!}\|T_{2k}\|.
$$
Equations (2), (4) and $\|Q_k\|\le\sqrt{K_k}$ give
$$
 E_k:=\|T_k-S_k\|
 \le2Lk b^{Lk/2}\sqrt{K_k/\lambda}
       \sum_{a=1}^{Lk-1}\sqrt{\chi_{j-k-a}}.
$$
Thus
$\|T_k\|\le B^k(b\lambda)^{k/2}k!/(2k)!\,\|T_{2k}\|+2B^kE_k$.
The initial factor is $\sqrt{p_j}=\sqrt{\beta_j}\|T_1\|$.
The preceding dyadic degrees sum to $k-1$, and the factorials telescope, so
the coefficient before stage $k$ is at most
$$
 (b\lambda)^{k/2}B^{k-1}/k!.
$$
At the terminal stage $\|T_d\|\le\sqrt{K_d}$ because $\|u^{j-d}\|_2\le1$.
Its contribution is $(A\lambda)^{d/2}c_d/B$. Multiplying the stage coefficient
by $2B^kE_k$ gives exactly $t_k$ above. Every defect index is nonnegative:
$j\ge(L+1)k-1$. This proves (5), including the boundary degree $d=2$.

## Uniform absorption and stopping

:::{prf:proof} Proof of the theorem
Set
$$
 C=16(1+\varepsilon),\quad L=\lceil64/\varepsilon\rceil+2,
 \quad p_*={\varepsilon\over64(L+1)},\quad b=(1-p_*)^{-1}.
$$
Then $L\le67/\varepsilon$, $p_*\ge\varepsilon^2/4352$,
$L\ge66$, and $p_*\le1/4096$. The definitions above imply
$$
 \log(J/16)=2\log(L/(L-2))+(L+1)\log(1/(1-p_*))
 \le\varepsilon/16+\varepsilon/32=3\varepsilon/32.
$$
For $0\le t\le1$, convexity gives $e^{3t/32}\le1+t/4$
(for example $e^{3/32}\le(1-3/32)^{-1}<5/4$).
Thus $q:=J/C\le1-3\varepsilon/8$, $\sqrt q\le1-3\varepsilon/16$,
and $A/C\le1/3$. The last estimate follows directly from
$b\le4096/4095$, $L/(L-2)\le66/64$, and $C\ge16$.

Fix dyadic $d\ge2$ and assume first $\lambda\le1/(CR^2\ell(d)^2)$.
Write
$$
 P_N=\sum_{j<N}p_j,\quad X_N=\sum_{j<N}\chi_j,\quad
 V_N=\sum_{j<N}v_j.
$$
Telescoping (1), with $E_0=0$, gives
$$
 v_N=1-P_N,\qquad aV_N+X_N\le\lambda P_N. \tag{6}
$$
For each $j\ge L=m_2$, use (5) at the largest dyadic $D_j\le d$ satisfying
$m_{D_j}\le j$. Degree $k<d$ is used for exactly $(L+1)k/2$ generations;
a shortened prefix uses it no more often. The first $L$ losses are at most
$\lambda$ each. Introduce the single nonnegative lag kernel
$$
 w_s=\sum_{\substack{k<d\\k\text{ dyadic}}}t_k
       \mathbf1_{\{k+1\le s\le(L+1)k-1\}},\qquad W_*=\sum_s w_s.
$$
With negative-index defects extended by zero,
$$
 \sum_{j<N}\Big(\sum_s w_s\sqrt{\chi_{j-s}}\Big)^2
 \le W_*\sum_s w_s\sum_{j<N}\chi_{j-s}\le W_*^2X_N.
$$
The first inequality is weighted Cauchy--Schwarz. Consequently, on any prefix
where the normalizer bound holds,
$$
 P_N\le\delta_d+NB_d\lambda^d+2W_*^2X_N, \tag{7}
$$
where
$$
 B_d=2A^dc_d^2,\qquad
 \delta_d=L\lambda+(L+1)\sum_{\substack{2\le k<d\\k\text{ dyadic}}}
                  k(A\lambda)^kc_k^2,
$$
and
$$
 \sqrt\lambda W_*\le C_0\sum_{\substack{k<d\\k\text{ dyadic}}}
                   k^2c_k(J\lambda)^{k/2},\qquad C_0=4L^2/B. \tag{8}
$$
This avoids any dependence on the number of overlapping lag intervals.

Here is the complete uniform bound on these quantities. The input
[](#thm:sz-polynomial-variance), transported by the contraction
$\operatorname{Cov}(\nu)^{1/2}$ from isotropic coordinates, gives
$c_k\le32^kk!$ for every $k$. Let
$k_0=\lceil2^{10}\varepsilon^{-1}\log(2/\varepsilon)\rceil$.
The inequalities $\log(2/t)\le2/t$ for $0<t\le1$ and the ceiling bound imply
$k_0\le2^{12}\varepsilon^{-2}$; also $C_0\le2^{14}\varepsilon^{-2}$ and
$R\ge64k_0$. Since $J\lambda\le R^{-2}$, for $k\le k_0$
$$
 C_0\sum_{k\le k_0}k^2c_k(J\lambda)^{k/2}
 \le{32C_0\over R}\sum_{k\ge1}k^3 2^{-k+1}
 ={1664C_0\over R}\le2^{-15}.
$$
Indeed $(32k/R)^k\le(32k/R)2^{-(k-1)}$ and
$\sum_{k\ge1}k^3x^k=x(1+4x+x^2)/(1-x)^4$.
For $k>k_0$ occurring in (8), monotonicity of $\ell$ gives
$k^2c_k(J\lambda)^{k/2}\le q^{k/2}$. Hence their contribution is at most
$$
 {16C_0\over3\varepsilon}e^{-3\varepsilon k_0/16}
 \le2^{17}\varepsilon^{-3}(\varepsilon/2)^{192}<1/8.
$$
Therefore $\theta:=2\lambda W_*^2\le1/8$.

For the small-degree startup sum, $A\lambda\le R^{-2}$ and
$(32k/R)^{2k}\le(32k/R)^4 4^{-k+2}$ give
$$
 \sum_{2\le k\le k_0}k(A\lambda)^kc_k^2
 \le(32/R)^4\sum_{k\ge2}k^5 4^{-k+2}\le2^{36}/R^4.
$$
For completeness the series bound here is exact: from
$\sum_{k\ge1}k^5x^k=x(1+26x+66x^2+26x^3+x^4)/(1-x)^6$,
at $x=1/4$ the numerator factor $1+26x+66x^2+26x^3+x^4$ is
less than $13$ and $(1-x)^6>1/8$. After multiplication by $16$, even
without subtracting the $k=1$ term, the bound is $416<2^{16}$.
Using $R\ge2^{40}\varepsilon^{-2}$ and $p_*\ge\varepsilon^2/4352$ gives
$$
 {L\over CR^2}+{(L+1)2^{36}\over R^4}\le p_*/32.
$$
For example the left side is bounded by
$67\,2^{-84}\varepsilon^3+68\,2^{-124}\varepsilon^7$;
comparison with $\varepsilon^2/(32\cdot4352)$ proves the assertion.
For the large-degree startup terms,
$$
 (L+1)\sum_{k>k_0}{k(A/C)^k\over(k+1)^4}
 \le(L+1)2^{-k_0}
 \le68\varepsilon^{-1}(\varepsilon/2)^{100}\le p_*/32.
$$
The first inequality follows by bounding the summands by $3^{-k}$ and summing;
the second uses $2^{10}\log2>100$ and $\varepsilon^{-1}\ge1$;
the last reduces to $68\cdot32\cdot4352<2^{100}$ and $\varepsilon^{97}\le1$.
Thus
$$
 \delta_d\le p_*/16,
 \qquad \lambda\le p_*/2,\qquad R^2\ge64/(p_*C). \tag{9}
$$
The last two inequalities follow from the same explicit parameter bounds.

Suppose, toward a contradiction, that $a\ge32B_d\lambda^{d+1}/p_*$,
and let $M=\lceil\lambda/a\rceil$. Stop at the first $N\le M$ with
$P_N>p_*/2$, if there is one. Through this possible exit,
$P_j\le p_*$, since each increment is at most $\lambda\le p_*/2$.
Consequently $v_j\ge1-p_*$ and
$\beta_j=e_j/v_j\le b\lambda$ for every normalizer required in (5).
The successor being normalized has squared norm $v_j-p_j\ge1-p_*-\lambda>0$.
Induction constructs all families on the stopped prefix; hence this argument
justifies the normalizer bound before using (7), with no assumption of its
validity on a later, unstopped family.

Combining (6)--(9) gives
$(1-\theta)P_N\le\delta_d+NB_d\lambda^d$.
For $N\le M$, the contradiction hypothesis and $a\le\lambda^2$ give
$$
 NB_d\lambda^d\le{p_*\over32}(1+a/\lambda)
 \le{p_*\over32}(1+\lambda)\le p_*/16.
$$
Thus $P_N\le p_*/7<p_*/6$, ruling out a first exit. This holds through $M$.
But (6) then implies both
$$
 aV_M\ge(1-p_*/6)aM\ge(1-p_*/6)\lambda,
 \qquad aV_M\le\lambda P_M<p_*\lambda/6,
$$
a contradiction. We obtain
$$
 a\lambda^{-(d+1)}<{64\over p_*}A^dc_d^2
 \le {64\over p_*}{A^dR^{2d}\ell(d)^{2d}\over(d+1)^4}
 \le(CR^2\ell(d)^2)^{d+1}.
$$
The last inequality uses $A<C$, $\ell(d)\ge1$ and (9). Taking the
$(d+1)$st root gives the asserted bound in the small-gap regime (indeed with
$a^{-1/(d+1)}$ before inserting the maximum). If
$\lambda>1/(CR^2\ell(d)^2)$ the asserted conclusion is immediate.
:::

**Fences respected.** The proposed node has no `bounded_by` edges. The argument
proves a curvature-dependent general-test estimate, not CMH, a sharp third-moment
constant, or a universal-time occupation estimate. In particular it does not
invert any sufficient-condition implication in the brief. Its constants require
$R\ge2^{40}\varepsilon^{-2}$ uniformly in the degree; retaining this threshold
is essential when the theorem is iterated with depth-dependent $\varepsilon$.
All polynomial assumptions are hypotheses of the displayed implication; the
universal small-degree estimate is an actual dependency, not an assumed open
antecedent. Independent review of this proof and that dependency is required.
