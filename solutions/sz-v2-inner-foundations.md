---
title: "Song–Zhang v2: inner refinement with a polynomial depth cost"
ledger-node:
  - prop:sz-v2-static-coefficient-transfer
  - lem:sz-v2-joint-frame
  - lem:sz-v2-skew-credit
numbering:
  enumerator: "144.%s"
---

**Overview.** This reconstruction concerns Section 6 of
[@SongZhang2026ConstantKLS]. It separates a coefficient transfer that works
with any static coefficient cap from the operator blocks needed to construct
such a cap. The transfer uses an accumulated covariance metric, so that the
terminal polynomial expansion is controlled in every degree at once.
All constants and depths in the statements below are independent of the
ambient dimension.

**Dependencies.** We use [](#lem:sz-analytic-foundations), the localization
construction and moment hierarchy in [](#thm:sz-polynomial-variance), with the established nonsmooth Brascamp–Lieb inequality used in those
dossiers. The purely algebraic frame has no analytic dependency. BKL, the proved KLS endpoint, and every
coefficient estimate derived from that endpoint are excluded. The Appell
normalization is $c_d=\sqrt{K_d}/d!$ as in
[](#thm:sz-polynomial-variance).

## Transfer of a static polynomial cap

:::{prf:theorem} Static coefficient transfer
:label: thm:sol-sz-v2-static-coefficients
There is a universal integer $r_*\ge2$ with the following property. Fix a
dimension range consisting either of all positive integers or of
$1,\ldots,n$. Let $r\ge r_*$ and $\Gamma\ge1$. Suppose that every centered
regular law in this range, of covariance at most $I$ and lower potential
Hessian bound $aI$, satisfies, for every $a>0$ and integer $k\ge1$,
$$c_k\le[\Gamma\ell_r(a^{-1})]^{k-1},
 \qquad \ell_r(x)=(\log(e+\cdot))^{\circ r}(x).$$
Then every centered log-concave law in the same dimension range, of
covariance at most $I$, satisfies
$$c_d\le[(1+r^{-2})\Gamma\ell_r(d)]^{d-1}
 \qquad(d\ge1).$$
The threshold $r_*$ does not depend on $\Gamma$, the dimension range, or the
law. This is [](#prop:sz-v2-static-coefficient-transfer).
:::

:::{prf:proof}
We first establish a posterior inequality. Let $\Psi:(0,\infty)\to[1,\infty)$
be continuous, and assume the regular coefficient bounds
$c_k\le\Psi(a^{-1})^{(k-1)/2}$. Consider a strongly log-concave law with
covariance $A\succ0$ and density proportional to
$\exp(-x^T\Lambda x/2-V(x))$, $\Lambda\succ0$, $V$ extended-valued convex.
If $M\succeq A$ and $M\succeq\delta\Lambda^{-1}$, then the law of
$M^{-1/2}(X-\mathbb EX)$ has covariance at most $I$ and curvature at least
$\delta I$. The latter follows by inversion and congruence, without
commuting matrices. Its full Appell expansion gives, for a polynomial $f$
of degree $d$,
$$
 \sqrt{\operatorname{Var}f}\le
 \sum_{k=1}^d J^{k-1}\|\mathbb ED^kf\|_{M^{\otimes k}},
 \qquad J=\sqrt{\Psi(\delta^{-1})}. \tag{1}
$$
Here the factor $1/k!$ is incorporated in $c_k$. For a finite vector or
tensor output use the same inequality in the output Hilbert direct sum and
Minkowski's inequality.

For a nonsmooth normalized posterior, convolve with $N(0,tI)$ and divide
by $\sqrt{1+t}$. Its covariance is at most $I$ and its Hessian lies between
$\delta(1+t)/(1+\delta t)I$ and $(1+t)t^{-1}I$. The Hessian formula is
$t^{-1}I-t^{-2}\operatorname{Cov}(X\mid X+\sqrt tG=y)$ before the final
rescaling; Brascamp–Lieb bounds the conditional covariance by
$(\delta+t^{-1})^{-1}I$. These are the same regularization and nonsmooth
Brascamp–Lieb inputs used in the certified analytic and polynomial dossiers.
Fixed-order moments and Appell coefficients converge as $t\downarrow0$.
Continuity of $\Psi$ therefore proves (1) for the original posterior.

Start covariance-adapted localization from a compactly supported isotropic
law, using the construction in [](#thm:sz-polynomial-variance). Denote its
covariance by $A_t$, precision by $\Lambda_t=\int_0^tA_u^{-1}du$, covariance
noise coefficients by $U_{i,t}$, and whitened noise matrices by
$S_{i,t}=A_t^{-1/2}U_{i,t}A_t^{-1/2}$. Its identities give
$$dA_t=\sum_iU_{i,t}\,d\beta_{i,t}-A_tdt,
 \qquad \sum_iS_{i,t}^2\preceq8I.$$
Fix $\tau,s>0$, put $\rho=s/\tau$, and introduce
$$M_t=A_t+\rho\int_0^tA_u\,du\succeq A_t.$$
For $h_j=\mathbb E_tD^jf$ set
$$N_j=\mathbb E_{\rm loc}\|h_j\|_{M_t^{\otimes j}}^2,
 \qquad L_j=\mathbb E_{\rm loc}\mathbb E_t
 \|D^jf-h_j\|_{M_t^{\otimes j}}^2.$$
We claim
$$N_j'\le(4j^2+j\rho)N_j+9j^2L_j. \tag{2}$$
Indeed, the drift of $M_t$ is $(\rho-1)A_t\preceq\rho M_t$.
With $C=M_t^{-1/2}A_t^{1/2}$, both $CC^T$ and $C^TC$ are contractions.
Thus its whitened noise matrices $\widetilde S_i=CS_iC^T$ obey
$$\sum_i\widetilde S_i^2
 =C\Big(\sum_iS_iC^TCS_i\Big)C^T\preceq8I.$$
For $K=M_t^{\otimes j}$ the product rule bounds the drift by
$[j\rho+8\binom j2]K$. To see the bound for each pair of slots, their
commuting symmetric matrices satisfy
$2\widetilde S_i^{(h)}\widetilde S_i^{(l)}
 \preceq(\widetilde S_i^{(h)})^2+(\widetilde S_i^{(l)})^2$;
sum over $i$. After congruence the noise of $K$ is
$V_i=\sum_{h=1}^j\widetilde S_i^{(h)}$, whence
$\sum_iV_i^2\preceq8j^2I$.
The noise of $h_j$ is
$c_i=\mathbb E_t[(D^jf-h_j)\xi_i]$, where $\xi=A_t^{-1/2}(X-m_t)$.
Weighted Bessel gives
$Q_j:=\sum_i\|c_i\|_K^2\le\mathbb E_t\|D^jf-h_j\|_K^2$.
The cross variation is bounded by
$$2\sum_i\langle K^{1/2}h_j,V_iK^{1/2}c_i\rangle
 \le\|h_j\|_K^2+8j^2Q_j.$$
Adding the quadratic variation of $h_j$ proves (2), because
$8\binom j2+1\le4j^2$ and $1+8j^2\le9j^2$.
One may first stop the localization parameters on compact sets. Spatial
compactness bounds the covariance, polynomial tests and accumulated metric
on each deterministic time interval. The displayed Bessel and noise bounds
then remove these stops in the integrated inequalities.

Suppose inductively that all smaller degrees in the dimension range satisfy
$c_k\le A^{k-1}$, with $A\ge1$. Applying the Appell expansion to each
$D^jf$ in a whitened posterior, and increasing each newly introduced
covariance slot from $A_t$ to $M_t$, yields
$$\sqrt{L_j}\le\sum_{k=1}^{d-j}A^{k-1}\sqrt{N_{j+k}}. \tag{3}$$
All old output slots keep the weight $M_t$. Thus (3) uses no comparison
between metrics at different times.

Take $f=P_d[T]$, $T\ne0$, put $Q=(d!)^2\|T\|_{\rm HS}^2$,
$w_l=A^{2\max(l-1,0)}$ and
$E(t)=\max_{1\le j\le d}N_j(t)/(Qw_{d-j})$.
For $1\le k\le l$ one has
$A^{k-1}\sqrt{w_{l-k}}\le\sqrt{w_l}$. Hence
$L_j\le d^2Qw_{d-j}E$. Appell centering gives
$N_j(0)=0$ for $j<d$ and $N_d(0)=Q$. Integrating (2), applying the
maximum, and using Gronwall therefore gives
$$E(t)\le e^{(13d^4+d\rho)t}.$$
Keeping the zero initial conditions in variation of constants gives the
additional estimates
$$N_j(t)\le9d^4t e^{(13d^4+d\rho)t}Qw_{d-j}\quad(j<d),
 \qquad N_d(t)\le Qe^{(4d^2+d\rho)t}. \tag{4}$$

For $0<\varepsilon<1$ take
$$\tau=\varepsilon/d^6,\qquad s=\varepsilon/d,
 \qquad\delta=s\tau=\varepsilon^2/d^7.$$
For every vector $v$, expansion of a square gives
$$\int_0^\tau v^TA_tv\,dt-\tau^2v^T\Lambda_\tau^{-1}v
 =\int_0^\tau|A_t^{1/2}v-\tau A_t^{-1/2}\Lambda_\tau^{-1}v|^2dt\ge0.$$
Thus $M_\tau\succeq\delta\Lambda_\tau^{-1}$, and (1) applies at time
$\tau$ with $J=\sqrt{\Psi(d^7/\varepsilon^2)}$.
The exponents in (4) are bounded respectively by $14\varepsilon$ and
$5\varepsilon$. When $J\le A$, the top term in (1) contributes at most
$\sqrt Qe^{5\varepsilon/2}J^{d-1}$. Each of the at most $d-1$ lower
terms contributes at most
$\sqrt Q3d^2\sqrt\tau e^{7\varepsilon}A^{d-2}$, including $k=d-1$
since $w_1=1$. Minkowski over localization randomness proves
$$\sqrt{\mathbb E_{\rm loc}\operatorname{Var}_\tau f}
 \le\sqrt Q\big(e^{5\varepsilon/2}J^{d-1}
       +3d^3\sqrt\tau e^{7\varepsilon}A^{d-2}\big).$$
Bessel and the posterior martingale identity imply
$(\mathbb E_{\rm loc}\operatorname{Var}_t f)'
=-\mathbb E_{\rm loc}|\operatorname{Cov}_t(f,\xi_t)|^2
\ge-\mathbb E_{\rm loc}\operatorname{Var}_t f$.
Since $\tau\le\varepsilon$, the finite-degree bound is consequently
$$c_d\le e^{3\varepsilon}J^{d-1}
        +3\sqrt\varepsilon e^{8\varepsilon}A^{d-2}. \tag{5}$$

Apply this with $\Psi(x)=\Gamma^2\ell_r(x)^2$ and, simultaneously over all
laws, induct on $d$. Degree one is covariance normalization. For $d\ge2$
set $\alpha=r^{-2}$, $\varepsilon=2^{-20}\alpha^2$, and
$A=(1+\alpha)\Gamma\ell_r(d)$. Monotonicity makes the smaller-degree
induction sufficient for (3). The elementary inequalities
$$\frac{xg'(x)}{g(x)}\le\frac12,
 \qquad g(d^7/\varepsilon^2)\le[7+2\log(1/\varepsilon)]g(d)$$
imply
$$\log\frac{\ell_r(d^7/\varepsilon^2)}{\ell_r(d)}
 \le2^{-(r-1)}\log[7+2\log(1/\varepsilon)]\le\alpha/8 \tag{6}$$
above one universal $r_*$. For the first inequality, with $t=e+x$,
$t\log t-2t+2e\ge0$ follows from its nonnegative derivative on $[e,\infty)$;
integrate the logarithmic derivative and compose. The second follows from
$e+d^7/\varepsilon^2\le(e+d)^7/\varepsilon^2$.
The last inequality in (6) holds uniformly in $d$ because
$r^22^{-r}\log[7+2\log(2^{20}r^4)]\to0$.

As $\log(1+\alpha/4)\ge\alpha/8$ and
$\log(1+\alpha)-\log(1+\alpha/4)\ge3\alpha/8$, we have
$J/A\le e^{-3\alpha/8}$. Divide (5) by $A^{d-1}$.
Its first term is at most $e^{3\varepsilon-3\alpha/8}
\le e^{-\alpha/4}\le1-\alpha/8$.
Its second is at most $3\sqrt\varepsilon e^{8\varepsilon}/A
\le\alpha/128$; here $A\ge1$ and the stated choice of $\varepsilon$
suffices. Their sum is less than one. This closes the degree induction
starting at degree two, with no depth-dependent small-degree threshold.

Finally condition an arbitrary isotropic law on increasing centered balls,
then center and whiten. Log-concavity gives convergence of moments of every
fixed order; the recursively determined Appell coefficients converge as
well. At each fixed degree the proved inequality therefore passes to the
limit. For covariance at most $I$, whitening and contraction in every tensor
slot transfer the same bounds; a singular covariance is treated on its
supporting subspace. Those subspaces remain in the specified dimension
range. This completes the proof.
:::

## A joint frame on all dyadic scales

:::{prf:theorem} Partial symmetrizations with one uniform frame constant
:label: thm:sol-sz-v2-frame
Let $d$ be dyadic and let a finite-dimensional real Hilbert space carry an
orthogonal representation of the permutation group on $2d$ letters. Write
$P_k$ for the average of permutations of $1,\ldots,k$, and $S_k$ for the
average of permutations of $k+1,\ldots,4k$ when $k<d$ is dyadic. Then
$$\|T\|^2\le10^4\left[d\|P_dT\|^2+
 \sum_{k<d\text{ dyadic}}k^2\|(I-S_k)P_kT\|^2\right]. \tag{7}$$
Finite orthogonal direct sums are allowed. This is
[](#lem:sz-v2-joint-frame).
:::

:::{prf:proof}
We give the representation calculation, including the scalar induction that
keeps the constant independent of the number of scales. Let $V_s(N)$ be
the permutation module on $s$-subsets of $N$ letters, with inclusion operator
$U_s$ and adjoint $D_{s+1}$. Counting subsets gives
$D_{s+1}U_s-U_{s-1}D_s=(N-2s)I$. If $D_jv=0$, induction gives
$$DU^tv=t(N-2j-t+1)U^{t-1}v,
 \quad\|U^tv\|^2=t!\frac{(N-2j)!}{(N-2j-t)!}\|v\|^2.$$
It follows that $V_s(N)$, $s\le N/2$, is the orthogonal sum of the lifted
harmonic spaces $\mathcal U_j(N)$, $0\le j\le s$, of dimensions
$\binom Nj-\binom N{j-1}$. The equivariant endomorphisms of $V_s(N)$ have
dimension $s+1$: their matrix entries depend only on intersection size.
Since there are already $s+1$ nonzero mutually orthogonal invariant spaces,
each has scalar real commutant, is irreducible, and is inequivalent to the
others. An invariant vector under the subgroup fixing one $s$-subset is
equivalently an equivariant map from $V_s(N)$, by mapping the distinguished
subset basis vector to that vector. Consequently averaging
$\mathfrak S_s\times\mathfrak S_{N-s}$ has rank one on each
$\mathcal U_j(N)$, $j\le s$, and vanishes on every other irreducible.

Let $z_j$ be its unit invariant vector for a first block of size $a\le N/2$.
For $a\le b\le N$, the inclusion map between subset levels has squared
singular value
$\binom{b-j}{a-j}\binom{N-a-j}{b-a}$ on the $j$th harmonic, by the
up/down identities. Complement subsets for levels beyond $N/2$; a missing
harmonic has zero singular value. Project the indicator of a fixed
$a$-subset onto this harmonic. Its squared norm is
$\dim\mathcal U_j(N)/\binom Na$ by transitivity. Averaging that indicator
over the first $b$ letters is the normalized sum of their $a$-subsets.
Apply the adjoint inclusion map and the corresponding norm identity at
level $b$. Division gives
$$\|P_bz_j\|^2=
 \frac{\binom{b-j}{a-j}\binom{N-a-j}{b-a}}
 {\binom ba\binom{N-a}{b-a}}. \tag{8}$$

In $\mathcal U_j(4m)$, $j\le m$, the part invariant under the last $2m$
letters restricts on the first $2m$ to one copy of each
$\mathcal U_l(2m)$, $0\le l\le j$. Indeed the invariant part of
$V_j(4m)$ is $\bigoplus_{t=0}^jV_t(2m)$, classified by the number of
selected letters in the first half. Subtracting the corresponding
$V_{j-1}(4m)$ decomposition leaves exactly one copy of each local harmonic.
The rank-one range of $E_m=P_mS_m$ has a unit vector $q$ invariant under
the first $m$ and last $3m$ letters. In this restriction write
$q=\sum_{l=0}^j\sqrt{w_l}z_{m,l}$, where $z_{m,l}$ is the unit vector
invariant under the two local halves; choose signs to make the coefficients
nonnegative. Equation (8) at $b=2m$ gives
$$w_0=\frac{(m)_{\underline j}}{(3m)_{\underline j}}.$$
Only local harmonics zero and one survive averaging the first $2m-1$
letters. On the latter, (8) gives squared averaging norm $(2m-1)^{-1}$.
Applying (8) at that $b$, subtracting $w_0$, and cancelling factorials yields
$$\frac{w_1}{w_0}
 =\frac{j(2m-1)(4m-j+1)}{(2m-j)(2m-j+1)}. \tag{9}$$
For $j=1$ the weights are $1/3,2/3$. For $j\ge2$, writing
$h=\sum_{l\ge2}w_l$, we have $h\ge4w_0$ and $h\ge w_1$.
Here is a direct verification. At $j=2$,
$w_0=(m-1)/(3(3m-1))$ and $w_1=h=(4m-1)/(3(3m-1))$.
At $j\ge3$, $w_0\le3^{-j}$ and $w_1/w_0<6j$, so
$h/w_0\ge3^j-1-6j\ge8$. For $j\ge4$,
$w_0+2w_1\le3^{-j}(1+12j)<1$; the inequality holds at four and
its left side decreases thereafter. At $j=3$, direct substitution in (9)
gives
$$h-w_1=\frac{2m(m-1)(14m-13)}
 {3(2m-3)(3m-2)(3m-1)}>0.$$

Put $c=10^{-4}$,
$H_d=\sum_{k<d\text{ dyadic}}k^2P_k(I-S_k)$ and $M_d=H_d+dP_d$.
The averages in each summand commute. We prove $M_d-cI\succ0$ by dyadic
induction with boundary Schur complements. The operator $H_m$ commutes
with the last $m$ letters: its largest summand averages a block containing
those letters and its earlier summands are supported in the first $m$.
In $\mathcal U_j(2m)$ let
$$a_{m,j}=\inf_{P_mT=z_{m,j},\ T\text{ last-}m\text{ invariant}}
                 \langle T,(H_m-cI)T\rangle.$$
When $M_m-cI\succ0$ this infimum is finite and attained, since its form
on $\ker P_m$ equals that of $M_m-cI$. It is the scalar Schur complement.
We maintain
$$a_{m,0}=-c,\quad 0<b_m:=-a_{m,1}\le4cm-2c,
 \quad a_{m,j}\ge m/8\quad(j\ge2). \tag{10}$$
At $m=1$, $M_1=I$ and both boundary values are $-c$, satisfying (10).

In any representation on $4m$ letters,
$$M_{2m}=H_m+m^2P_m-m^2E_m+2mP_{2m}.$$
On irreducibles where $E_m=0$, positivity follows from
$H_m+m^2P_m-cI\succeq M_m-cI$. Otherwise $E_m=qq^*$ in
$\mathcal U_j(4m)$ for $j\le m$. Its complement to the last-$2m$
invariants has no component of $q$ and remains positive. Within the latter
space, the local components containing $q$ are invariant under the next
$m$ letters; the remaining local subspaces also remain positive. Eliminating
all variables off their $P_m$ boundaries leaves exactly
$$\operatorname{diag}(m^2+a_{m,l})_{l=0}^j
              -m^2bb^*+2me_0e_0^*,\qquad b_l=\sqrt{w_l}. \tag{11}$$
All eliminated blocks are positive by induction. The index zero is the
line invariant under the first $2m$ letters. Define
$$D_{m,j}=1-m^2\sum_{l=1}^j\frac{w_l}{m^2+a_{m,l}}.$$
When this is positive the remaining nonzero-index block is positive by
the rank-one criterion, and its scalar Schur complement is
$$a_{2m,j}=m^2-c-\frac{m^2w_0}{D_{m,j}}. \tag{12}$$
For $m<j\le2m$, $E_m=0$ and the boundary is in the trivial local
representation, so $a_{2m,j}=m^2-c$.

For $j=1$, equations (9),(12) reduce to
$$b_{2m}=c+\frac{2b_m}{1-3b_m/m^2}.$$
Since $3b_m/m^2\le12c$, the difference of the fraction and $2b_m$ is
at most $96c^2/(1-12c)\le c$. Thus
$0<b_{2m}\le8cm-2c$ and $2m-b_{2m}>0$; the nonzero-index block is
positive since $m^2-3b_m>0$.
For $2\le j\le m$, using (10) and $h\ge w_1$ gives
$$D_{m,j}\ge w_0+\frac{h}{8m+1}-\frac{4cw_1}{m-4c}
 \ge w_0+\frac{h}{9m}>0.$$
Indeed $m\ge2$, $(8m+1)^{-1}\ge2/(17m)$,
$4c/(m-4c)\le8c/m$, and $2/17-8c>1/9$.
Equations (12) and $h\ge4w_0$ then give
$$a_{2m,j}\ge\frac{m^2h}{9mw_0+h}-c
 \ge\frac{4m^2}{9m+4}-c\ge m/4.$$
The last inequality follows by subtracting $m/4$: the positive difference
before $c$ is $m(7m-4)/(4(9m+4))\ge5m/44$.
The case $j>m$ satisfies the same bound, including $m=1$.
The trivial boundary remains $-c$, so after adding $2m$ all boundaries
are positive. Every eliminated block and unaffected sector is positive as
well. This closes the induction and establishes (7).
:::

## Credit for a skew linear moment

:::{prf:theorem} Skew loss paid by inverse normalization
:label: thm:sol-sz-v2-skew-credit
Let $\mu$ be a centered regular law with covariance at most $I$, and let
$H$ be its nonnegative gradient-form operator on centered $L^2(\mu)$.
Let $U=(U_1,\ldots,U_n)$ be a centered vector family in its form domain,
with $\|U\|_2=1$ and symmetric matrix $\mathbb E\nabla U$. Put
$$e=\|H^{1/2}U\|_2^2,\qquad
 \beta=\|H^{-1/2}U\|_2^{-2},\qquad LU=\mathbb E[X\otimes U].$$
Then
$$\beta\|\operatorname{Skew}(LU)\|_{\rm HS}^2\le1-\beta/e.$$
The assertion holds also for a finite direct sum of such vector families,
normalized jointly to norm one and with jointly defined $e,\beta$.
This proves [](#lem:sz-v2-skew-credit).
:::

:::{prf:proof}
If $C$ is any skew matrix with Hilbert–Schmidt norm one, the coordinate
family $V=CX$ has $\|H^{1/2}V\|_2=1$: its Dirichlet energy is $\|C\|^2$.
By the symmetry hypothesis,
$\langle H^{1/2}V,H^{1/2}U\rangle=\mathbb E\langle C,\nabla U\rangle=0$.
Moreover $\langle H^{-1/2}U,H^{1/2}U\rangle=1$.
The part of $H^{-1/2}U$ orthogonal to $H^{1/2}U$ therefore has squared
norm $\beta^{-1}-e^{-1}$. Pairing with $H^{1/2}V$ and using
Cauchy–Schwarz yields
$$|\langle V,U\rangle|^2
 =|\langle H^{1/2}V,H^{-1/2}U\rangle|^2
 \le\beta^{-1}-e^{-1}.$$
Taking the supremum over skew matrices is exactly the squared
Hilbert–Schmidt norm of the skew part of $LU$ (a transpose or sign does
not change this norm). Multiply by $\beta$.
For multiple output columns choose a collection of skew matrices whose
sum of squared Hilbert–Schmidt norms is one and apply the identical
orthogonality argument in the full direct sum. All pairings are form
pairings; no assumption that $HU\in L^2$ has been used.
:::

**Fences respected.** These three statements have no `bounded_by` edges.
The frame is finite-dimensional algebra. The skew estimate uses the
regular form domain and covariance normalization only. The coefficient
transfer is an implication whose uniform regular coefficient premise is
retained explicitly; it establishes no such premise on its own. In
particular it does not use the BKL coefficient bound or discharge a CMH,
occupation, or adaptive trace assumption. The threshold in its conclusion
is universal and the induction starts at degree two.
