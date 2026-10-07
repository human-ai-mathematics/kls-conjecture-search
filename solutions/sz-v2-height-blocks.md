---
title: "Song–Zhang v2: finite blocks and repeated height reduction"
ledger-node:
  - prop:sz-v2-height-reduction
  - lem:sz-v2-terminal-distortion
numbering:
  enumerator: "143.%s"
---

*Part of the second version of Song–Zhang, Chapter [](#sec:sz-v2-proof); the reading order is on the [full proofs](#sec:proofs-sz-v2) page.*

**Overview.** This reconstructs the fixed-cost height reduction in Section 8
of [@SongZhang2026ConstantKLS]. Polynomial testing and a joint tensor frame
give delayed loss estimates. Actual norm-attaining orbits then produce
starting families at arbitrarily high odd orders. We use a fixed, enlarged
radius floor in this section; approaching the seed radius with loss tending
to zero is a separate issue in Section 9. A static radius is iterated
through all inner depths before its conversion to the Poincaré constant.

**Dependencies.** We use [](#lem:sz-v2-joint-frame),
[](#lem:sz-v2-operator-block-primitives),
[](#lem:sz-v2-normalized-hierarchy), [](#lem:sz-v2-mesoscopic-powers),
[](#prop:sz-v2-static-coefficient-transfer),
[](#thm:sz-v2-iterated-curvature), and
[](#prop:sz-v2-common-radius). Generic sequence and restart lemmas used
below have no height-reduction or small-loss profile as a premise.
There is no use of BKL, KLS, or a bound derived from either.

Throughout, the measure is centered and regular, with covariance at most
$I$ and $aI\preceq D^2W\preceq bI$ for $0<a\le b<\infty$.
Use the operators and hierarchy of
[](#lem:sz-v2-operator-block-primitives) and
[](#lem:sz-v2-normalized-hierarchy); put $R=\|\mathcal T\|^2$ and
$\lambda=C_P^{-1}$. Every tensor norm includes all ordered output indices.
Write $C_F=10^4$, $g(x)=\log(e+x)$, $\ell_r=g^{\circ r}$,
$t(x)=1+\log^*(x+2)$ and $t_j=t^{\circ j}$.
Constants denoted $C$ may increase only by universal factors, unless
their displayed arguments specify fixed seed-comparison constants.

## Joint-frame interfaces

We use the independently reconstructed [](#lem:sz-v2-raw-joint-frame)
and [](#lem:sz-v2-propagated-joint-loss). Their raw estimate is denoted (B1)
below and their delayed normalized loss estimate is denoted (B2).

## Seeds and elementary bounds uniform in the height stage

:::{prf:lemma} Capped height seeds
:label: lem:sol-sz-v2-height-seeds
There is a universal $C_6\ge1$ for which
$G_*(x)=C_6t(x)^{1/6}$ satisfies
$c_d\le G_*(d)^{d-1}$ for every centered log-concave covariance
contraction and every $d\ge1$.
For $j\ge1$, $A\ge1$, let
$G(x)=\min\{G_*(x),At_j(x)^{1/6}\}$ and $g_0=G^2$.
The same conclusions below hold for $G=G_*$, with constants independent
of $j,A$:
$$
 G(Cx^p)\le C_{C,p}G(x),\quad G(k)^6\le C_0k,       \tag{B4}
$$
$$
 g_0(R^Q)\le C g_0(8Q)+C G_*(R)^2\quad(R,Q\ge3),  \tag{B5}
$$
$$
 g_0(C(Qs)^2)\le C_Cg_0(Q)s^{1/Q}\quad(Q\ge3,s\ge1),\tag{B6}
$$
$$
 2C_F2^Q\sum_{k\ge Q}k^2g_0(k)^{Q-1}4^{-(k-Q)}
 \le[C_1g_0(Q)]^Q.                                \tag{B7}
$$
:::

:::{prf:proof}
The inner curvature theorem gives
$C_P\le C(r+1)^{1/3}\ell_r(a^{-1})^2$. Repeated Poincaré on Appell
derivatives, starting with $c_1\le1$, gives
$c_k\le C_P^{(k-1)/2}$ for each regular measure. Apply the static
coefficient transfer at a depth $r\ge r_*$ chosen so that
$r\le C't(d)$ and $\ell_r(d)\le5$.
Such a depth exists: while the ordinary logarithm iterate $y$ is at least
four, $g(y+1)\le\log y+1$, and $g$ preserves $[0,5]$.
Induction along the ordinary logarithms, followed by the fixed additional
$r_*$ steps, proves both requirements. The transfer now gives
$c_d\le[C''t(d)^{1/6}]^{d-1}$ uniformly over all log-concave covariance
contractions, as claimed.

The log-star thresholds $E_0=1$, $E_{k+1}=e^{E_k}$ imply
$t(x+b)\le t(x)+b$ for integers $b\ge0$; consecutive thresholds
on the domain $x\ge1$ have gaps greater than one. Induction preserves
this inequality for every $t_j$. Moreover $t(3)=3$, $t(n)\le n$ for
integers $n\ge3$, and hence $3\le t_j(x)\le t(x)\le4x$.
For $x,y\ge1$, $(x+2)(y+2)\le e^{\max(x+2,y+2)}$:
indeed $2\log u\le u$ for $u\ge3$. Since both $xy+2$ and $x+y+2$
are at most this product, it follows that
$t(xy),t(x+y)\le t(x)+t(y)$. Apply this inductively to obtain the
same inequalities for every $t_j$.

For fixed $C,p\ge1$, $Cx^p+2\le e^{x+2}$ beyond a fixed threshold;
the bounded remaining interval supplies an integer $b_{C,p}$ such that
$t(Cx^p)\le t(x)+b_{C,p}$ everywhere. Integer-shift stability propagates
this bound through any number of compositions. Likewise
$x^x+2\le\exp(\exp(x+2))$ gives
$t_j(x^x)\le t_j(x)+2$.
Since all heights are at least three, both branches of $G$ satisfy (B4).
The original cap gives $G(k)^6\le C_6^6t(k)\le4C_6^6k$.
For (B5) let $M=\max(R,Q)$. Then $R^Q\le M^M$, so
$G(R^Q)\le C G(M)$. If $M=Q$, use $G(M)\le G(8Q)$; otherwise
use $G(M)\le G_*(R)$.

To prove (B6), put $y=(\log s)/Q$ and $X=CQ^2e^{2Qy}$.
There is fixed $C'$ with $\log(X+2)\le C'Q(1+y)$.
The product and fixed-argument estimates therefore give
$$
 t_j(X)\le1+t_j(C'Q(1+y))
 \le1+t_j(Q)+b_{C',1}+4(1+y)
 \le C''t_j(Q)(1+y).
$$
Both branches of $g_0$ obey the resulting cube-root bound; their
minimum does too. Divide by $s^{1/Q}=e^y$ and use boundedness of
$(1+y)^{1/3}e^{-y}$.

Finally for $k\ge Q$, the product inequality gives
$t_j(k)\le t_j(Q)+4k/Q\le5(k/Q)t_j(Q)$, hence
$g_0(k)\le Cg_0(Q)(k/Q)$ for either branch and their minimum.
For $\beta=Q+1$,
$$
 \sum_{k\ge0}k^\beta4^{-k}
 \le \sup_{x\ge0}(x^\beta2^{-x})\sum_{k\ge0}2^{-k}
 =2[\beta/(e\log2)]^\beta.
$$
Substitute this estimate into (B7). All remaining factors are bounded
by a universal constant to the power $Q$: in particular $Q^{2/Q}$
is bounded for $Q\ge3$. This proves the lemma.
:::

:::{prf:lemma} Uniform moments under the original cap
:label: lem:sol-sz-v2-height-moments
Fix integers $M,h\ge0$ and constants $c,C_0>0$. For
$0<\epsilon\le1/16$, $\epsilon F^2\ge L$, and
$\rho_k=\min\{1,C_0k^{1/3}/F^2\}$, the sum
$$\sum_{k\ge h+1}k^M\rho_k^{k-h}e^{-c\epsilon k}$$
is uniformly bounded once $L$ is a sufficiently large fixed constant.
Its supremum tends to zero as $L\to\infty$.
:::

:::{prf:proof}
For $k\le F^3$, $\rho_k\le C_0/F\le F^{-1/2}$ after increasing
$L$, so this part is bounded by
$\sum_{k\ge h+1}k^MF^{-(k-h)/2}$, which tends to zero as
$F\ge4\sqrt L$ tends to infinity. For $k>F^3$ discard $\rho_k$,
remove $e^{-c\epsilon F^3/2}$, and bound the remaining exponential
moment by $C\epsilon^{-M-1}$ using an integral over unit intervals.
Since $\epsilon^{-1}\le F^2/L$ and $\epsilon F^3\ge LF$, the tail
is at most $CL^{-M-1}F^{2M+2}e^{-cLF/2}$.
The exponential dominates its polynomial uniformly on $F\ge4\sqrt L$,
proving both assertions.
:::

## Realizing an arbitrary odd block order

:::{prf:lemma} Local orbit and actual initialization
:label: lem:sol-sz-v2-height-local
Assume $G\le G_*$ is nondecreasing and bounds all coefficients.
There are universal $C,c>0$ with the following properties. Let $d\ge2$
be dyadic, $m\ge2d$, $z=\|\mathcal T^m\|^{2/m}$, and
$$
 0\le R-z\le2,\quad z\ge\max\{4G(d)^2,C\},\quad
 \gamma=C_Fd c_d^2z^{-(d-1)},\quad \gamma m^2/z\le c.
                                                               \tag{B8}
$$
A unit norm-attaining vector of $\mathcal T^m$ gives an orbit satisfying
$1/2\le b_j\le2$ for $0\le j\le m$ and $b_j\le2$ for all $j\ge0$.
It also satisfies
$$
 \sum_{j=2}^ml_j\le C/z+C\gamma m,\qquad
 \sum_{k=2}^{J+1}\sum_{j=k}^{m+k-1}l_j\le C/z+C\gamma Jm
 \quad(1\le J\le m/4).                            \tag{B9}
$$
Suppose $p\ge3$ is odd, $\kappa\ge1$, $d$ is the least dyadic
integer at least $4p$, and additionally
$$
 \frac{z^{p-2}}{4\kappa}\le m\le\frac{4z^{p-2}}\kappa,
 \quad J_0\le m/4,\quad J_0\gamma zm\le1,
 \quad C\kappa z^{-p}\le1/8.                       \tag{B10}
$$
There is one centered unit starting family with $u=z^{-1}$,
$$
 \nu\le\frac{u}{1-C\kappa u^p},\quad
 P_J\le C\kappa u^p\ (1\le J\le J_0),\quad
 aV_N+X_N\le\nu-u+uP_{N+1}\ (N\ge0).             \tag{B11}
$$
:::

:::{prf:proof}
Compactness in the operator primitive supplies the singular vector.
Submultiplicativity gives
$b_0=b_m=1$, $b_{j+m}\le b_j$, $b_{j+1}\le t b_j$ with
$t=R/z\le1+2/z$, and $b_j\le t^j$ before any orbit estimate.
Use the local form of (B1) at the largest available dyadic degree,
capped at $d$. At degree two and index two, the three-slot frame
$\|Y\|^2\le8(\|\mathsf P_2Y\|^2+
\|(I-\mathsf S_1)Y\|^2)$ gives
$$l_2\le(2K_2b_1+8D_1)/z.$$
That frame is immediate on the trivial and alternating representations;
on the two-dimensional standard representation its lower frame
eigenvalue is $1-\sqrt3/2>1/8$.
Consequently $l_j\le h_j+\sum_s\alpha_sD_{j-s}$ for $j\ge2$,
where $h_2=2K_2b_1/z$, the later $h_j$ is the coherent term at the
available degree, and the finite nonnegative kernel has $8/z$ at delay
one and, for each dyadic $k<d$, the weight
$108C_Fk^5c_k^2z^{-k}t^{3k-2}$ at each delay $k,\ldots,4k-2$.

Put $F^2=z/4$. For $k\le d$, $\rho_k=G(k)^2/F^2\le1$ and
$\rho_k\le C k^{1/3}/F^2$. At large universal $z$,
$t^3G(k)^2/z\le\rho_k/2$. Thus both kernel moments are at most
$C/z$: the factors $k^6$ and $k^7$ are summable against
$\rho_k^{k-1}2^{-(k-1)}$, by the preceding moment lemma with a fixed
$\epsilon$. The case $k=1$ is bounded separately by $C/z$.
The same estimates control the early coherent terms while only
$b_i\le t^i$ is available. Degree $k<d$ is used at indices
$2k-1,\ldots,4k-2$. After multiplication by $z$, their weighted
contribution $\sum jh_j$ is at most
$$
 Ck^3t^{3k-1}G(k)^{2k-2}z^{-(k-2)}
 =Ct^5k^3G(k)^2(t^3G(k)^2/z)^{k-2}
 \le Ck^4\rho_k^{k-2}2^{-(k-2)}
$$
for $k\ge4$. The degree-two terms are bounded using the fixed universal
$K_2$. Hence $\sum_{j=2}^{2d-2}jh_j\le C/z$.
At later indices $h_j=\gamma b_{j-d+1}$.

These are exactly the hypotheses of the two-block Green estimate
[](#lem:sz-v2-orbit-green-restart), using the raw defect inequality
from the operator primitive and $l_1\le b_1\le2$.
Its conclusion gives the orbit bounds and the second part of (B9).
The first-block telescope in its proof also gives
$\sum_{j=2}^ml_j\le C/z+C\gamma\sum_{j<m}b_j\le C/z+2C\gamma m$.

Quadratic testing gives
$\mathsf P_2Lw_1=Q_2f/(2\sqrt z)$, so
$\|\operatorname{Sym}(Lw_1)\|^2\le K_2/(4z)$.
Apply the actual-restart part of
[](#lem:sz-v2-orbit-green-restart), with (B9) and (B10).
It uses $Y=\bigoplus_{j=0}^{m-1}w_j$ and the unit restart at its
second normalized successor. Its matched budget follows from the exact
window monotonicity $S_{k+1}\le S_k$ for this same orbit, not by
replacing $R^{-1}$ in the generic hierarchy budget. This proves (B11).
:::

:::{prf:lemma} Extension at a fixed seed margin
:label: lem:sol-sz-v2-height-extension
Let $G\le G_*$ be a coefficient majorant, $q\ge3$ odd,
$F\ge1$, $d$ the least dyadic integer at least $8q$, and
$\kappa_q=F^{2q-2}$, $\kappa_{q-2}=F^{2q-6}$.
Assume $G(d)\le F$, $0\le R-z\le2$, $z\ge\max\{4F^2,C\}$,
and $\|\mathcal T^h\|\le4(h+1)z^{h/2}$ for all $h\ge0$.
Suppose one centered unit hierarchy has the matched budget (B11),
$\nu\le u/(1-a_qu^q)$ and $P_J\le s_qu^q$ through $J=32q$,
where $u=z^{-1}$ and $a_q+s_q+1\le C_0\kappa_{q-2}$.
If $F$ exceeds a sufficiently large constant depending only on $C_0$,
then
$$
 \|\mathcal T^m\|^{2/m}\ge z-C_b\kappa_{q-2}z^{1-q}
 \quad(1\le m\le\lfloor z^q/\kappa_q\rfloor),      \tag{B12}
$$
where $C_b$ is independent of $q,F,G$.
:::

:::{prf:proof}
Use (B2) with its retained degree $d_0=d$. Since $d<16q$,
its retained range $2d-1<32q$ is available and there are no intermediate
coherent terms in $\Delta$. Put
$K_q=4(s_q+C_F'\kappa_{q-2}+4C_\theta a_q+1)$,
$p_*=K_qu^q$, where $C_F'$ and $C_\theta$ are fixed below.
Before, and at, a first exit of $p_*$, required normalizers obey
$$
 B_*\le\frac{u}{(1-a_qu^q)(1-p_*)}\le(1+1/64)u.
$$
Indeed $a_qu^q,p_*\le C F^{-6}4^{-q}$; choose the fixed lower
bound on $F$ to make both at most $1/1024$.
Thus $t_*\le1+1/64$, and $B_*t_*^3G(k)^2\le G(k)^2/(2F^2)$
for $k\le d$. The same capped moment estimate bounds
$\theta\le C_\theta u$ uniformly. Also $C_P\le R+1\le z+3$
gives $\lambda\ge u/2$ at $z\ge3$.

For the terminal coefficient, write $\rho=G(d)^2/F^2\le1$.
Then
$$
 \frac{\tau}{\kappa_q\kappa_{q-2}u^{2q}}
 \le C_Fd F^6\rho^{d-1}(1+1/64)^d(z/F^2)^{2q-d}
 \le C d^2\rho^{d-4}(1+1/64)^d4^{2q-d}.
$$
We used $F^6\rho^{d-1}=G(d)^6\rho^{d-4}$ and
$G(d)^6\le Cd$. Since $d\ge8q$, the last expression is bounded
by a universal constant; polynomial growth in $d$ is dominated by its
geometric decay. Fix $C_F'$ to dominate it.
Now [](#lem:sz-v2-block-extension) applies with these $\theta,\tau$,
the retained losses and the actual matched budget. Its other thresholds
are $z\ge8C_\theta$ and the two already imposed smallness conditions.
It proves (B12), since $a_q+4K_q\le C_b\kappa_{q-2}$.
:::

:::{prf:lemma} Finite blocks at every odd order
:label: lem:sol-sz-v2-height-blocks
Let a nondecreasing $1\le G\le G_*$ bound the coefficients of all
regular covariance contractions and satisfy (B4),(B5) with fixed
comparison constants. For every odd $Q\ge3$ there is a static assignment
$Z_Q$ and constants $H_Q,a_Q,s_Q>0$ such that
$$
 H_Q\le K G(8Q)^2,\quad a_Q+s_Q+1\le[KG(8Q)^2]^Q,
                                                               \tag{B13}
$$
$$
 c_d\le Z_Q^{(d-1)/2},\quad
 H_Q\le Z_Q\le\max\{H_Q,C_P\},\quad C_P\le Z_Q+3.\tag{B14}
$$
Whenever $Z_Q>H_Q$, it is an actual finite block radius $z$, and one
centered unit family satisfies, with $u=z^{-1}$ and
$J_Q=\lceil128Q\log(e+G(8Q))\rceil$,
$$
 \nu\le u/(1-a_Qu^Q),\quad P_J\le s_Qu^Q\ (J\le J_Q),
 \quad aV_N+X_N\le\nu-u+uP_{N+1},                 \tag{B15}
$$
$$
 \|\mathcal T^h\|\le4(h+1)z^{h/2},\quad
 0\le R-z\le1,\quad a_Qu^Q\le1/8.               \tag{B16}
$$
All constants depend only on the fixed comparison constants and universal
analytic constants, not on $Q$, the measure, or the smaller seed $G$.
:::

:::{prf:proof}
Choose a universal multiplier $C_2$ sufficiently large in the order
specified below, and put $F=C_2G(8Q)$,
$R_0=16F^2$, $H_Q=R_0+1$, $\kappa_q=F^{2q-2}$ for odd $q\ge1$.
The fixed-argument comparison in (B4) permits increasing $C_2$ once
so that every initialization degree below $8Q$ and extension degree
below $16Q$ has seed at most $F/C_3$, where $C_3$ is any prescribed
large universal constant. Take
$\widetilde J_p=\lceil128p\log(e+F)\rceil$.

If $R<R_0$, set $Z_Q=H_Q$. The common-radius comparison gives
$c_d\le\max(1,R)^{(d-1)/2}\le H_Q^{(d-1)/2}$, and $C_P\le R+1$
gives (B14). Only the large-$R$ case requires a family.
Suppose therefore $R\ge R_0$.

**Base block.** Let $m_3=\lfloor R\rfloor$,
$z_3=\|\mathcal T^{m_3}\|^{2/m_3}$. The mesoscopic powers lemma gives
$R-C/R\le z_3\le R$, and dividing arbitrary powers into blocks of
length $m_3$ gives
$$
 \|\mathcal T^h\|\le(R/z_3)^{(m_3-1)/2}z_3^{h/2}
 \le2z_3^{h/2}
$$
at a universal large threshold. Also $m_3$ lies between $z_3/4$ and
$4z_3$, so its actual divisor is $\kappa_1=1$.
Its initialization degree is sixteen, with a fixed coefficient bound
from $G_*$. Thus $\gamma m_3^2/z_3\le Cz_3^{-14}$ and
$\widetilde J_3\gamma z_3m_3\le C\widetilde J_3z_3^{-13}$.
Since $\widetilde J_3=O(\log(e+F))$ and $z_3\ge15F^2$,
all conditions (B8),(B10), including
$\widetilde J_3\le m_3/4$, hold at a fixed large $C_2$.
The local initialization gives one family with
$a_3+s_3+1\le C\kappa_1$.

**Initialization conditions at any subsequent order.** Suppose $p\ge5$,
$z\ge15F^2$, $0\le R-z\le1$, and
$z^{p-2}/(4\kappa_{p-2})\le m\le4z^{p-2}/\kappa_{p-2}$.
Let $d$ be the least dyadic integer at least $4p$, $G_p=G(d)$,
and $\rho=G_p^2/F^2\le C_3^{-2}$.
The coefficient cap $G_p^6\le Cd$ and the preceding length bounds give
$$
 \gamma m^2/z
 \le CdG_p^2\rho^{d-2}15^{-(d-2p+4)}
 \le Cp^{4/3}C_3^{-8p+4}15^{-2p},                \tag{B17}
$$
$$
 \widetilde J_p\gamma zm
 \le C\widetilde J_p dG_p^6F^{-2}\rho^{d-4}15^{p-d}
 \le Cp^3\frac{\log(e+F)}{F^2}C_3^{-8p+8}15^{-3p}.
                                                               \tag{B18}
$$
The constants harmlessly cover $d<8p$ and the ceilings. The two
right sides are uniformly as small as required by choosing $C_3$,
then $C_2$, universally large. Also
$\widetilde J_p/m\le C p\log(e+F)/(F^2 15^{p-2})$ is uniformly
small, so $\widetilde J_p\le m/4$ and $m\ge2d$.
Finally $C\kappa_{p-2}z^{-p}\le CF^{-6}15^{-p}$ is small.
Thus local initialization gives
$a_p+s_p+1\le C\kappa_{p-2}$ through the entire longer prefix.
The same constant works for every order.

**Extension and radius control.** Given the block at odd order $q<Q$,
define
$$
 m_{q+2}=\lfloor z_q^q/\kappa_q\rfloor,\qquad
 z_{q+2}=\|\mathcal T^{m_{q+2}}\|^{2/m_{q+2}},\qquad
 \Delta_q=C_b\kappa_{q-2}z_q^{1-q}.               \tag{B19}
$$
The extension lemma uses only the already constructed family's losses
through $32q$, contained in $\widetilde J_q$, and its already proved
power envelope. It gives $z_{q+2}\ge z_q-\Delta_q$.
At $z_q\ge15F^2$,
$$
 \Delta_q/z_q\le C_bF^{-6}15^{-q},\qquad
 q\Delta_q/z_q\le CF^{-6}.                        \tag{B20}
$$
The decrement sequence decreases by at least a factor two: indeed,
once the new radius is above $15F^2$,
$$
 \frac{\Delta_{q+2}}{\Delta_q}
 =\frac{F^4}{z_{q+2}^2}(z_q/z_{q+2})^{q-1}
 \le15^{-2}\exp(CF^{-6})\le1/2.
$$
There is no circular assumption here. At the next step the decrements
already bounded give first
$R-z_{q+2}\le C/R+\sum_{p\le q}\Delta_p
\le C/R+2\Delta_3<1$ after increasing $C_2$.
Since $R\ge16F^2$, this establishes $z_{q+2}\ge15F^2$ before its
new decrement is compared. Increasing actual radii can only improve
these upper bounds. In particular every finite constructed prefix has
$0\le R-z_q<1$ and $(z_p-z_q)_+\le2\Delta_p$ for $p<q$.

**The power envelope before the next initialization.** The lower length
comparison already available at order $q$ gives
$m_q\le4z_q^{q-2}/\kappa_{q-2}$.
The new defining length is at least half its unfloored value, since
$z_q^q/\kappa_q\ge15^qF^2$. Therefore
$$m_{q+2}/m_q\ge z_q^2/(8F^4)\ge15^2/8>4.$$
Moreover
$m_{q+2}\Delta_q/z_q\le C_b/F^4$.
For any prefix ending at $p$, its base remainder satisfies
$$
 m_3(R-z_p)/z_p\le C/R+C/F^4.
$$
The greedy propagation lemma [](#lem:sz-v2-block-propagation) therefore
gives
$$
 \|\mathcal T^h\|\le z_p^{h/2}
 \exp\{C/R+C/F^4+(C/F^4)\log_4(h+1)\}
 \le4(h+1)z_p^{h/2}.                             \tag{B21}
$$
Fixing $C_2$ large makes both the prefactor and exponent no greater
than the displayed values. This uses only exact norms of constructed
blocks; it precedes initialization of the new block.

**New length compared with its own radius.** Apply the previous envelope
at $h=m_{q+2}$ to get
$$
 q\log(z_{q+2}/z_q)
 \le\frac q{m_{q+2}}[\log16+2\log(m_{q+2}+1)].
$$
The right side is uniformly small for all $q\ge3$ at large $F$:
$m_{q+2}\ge15^qF^2/2$, and $\log(x+1)/x$ is decreasing for $x>0$.
The resulting bound is
$Cq(q+\log(e+F))/(15^qF^2)$.
The negative part is bounded by (B20). With $C_2$ fixed large,
$z_{q+2}^q/z_q^q$ is between $1/2$ and two. The floor loses at most
a further factor two. Hence
$$
 \frac{z_{q+2}^q}{4\kappa_q}\le m_{q+2}
 \le\frac{4z_{q+2}^q}{\kappa_q}.
$$
All initialization conditions at order $q+2$ were verified in
(B17),(B18), so its new actual family exists with the required longer
prefix and matched budget. This completes a finite induction up to $Q$.

**All static degrees.** The constructed $m_Q$ satisfies $m_Q\le R^Q$.
By (B5),
$$
 G(m_Q)^2\le C G(8Q)^2+C G_*(R)^2\le R/2\le z_Q.
$$
The first term is at most $R/4$ because $F=C_2G(8Q)$ and
$R\ge16F^2$; the second is at most $R/4$ above a fixed universal
threshold since $G_*(R)^2=O(t(R)^{1/3})=o(R)$.
Increase $C_2$ to include that threshold. The common-radius finite-block
comparison now gives $c_d\le z_Q^{(d-1)/2}$ simultaneously for all
$d\ge1$. Put $Z_Q=\max\{H_Q,z_Q\}$.
We have $z_Q\le R\le C_P\le R+1\le z_Q+2$, which proves (B14).
Whenever $Z_Q>H_Q$, the constructed radius and family are the required
ones. The uniform initialization constants may be enlarged to fix
$a_Q,s_Q$ independently of the particular law; they satisfy
$a_Q+s_Q+1\le CF^{2Q-6}\le(KG(8Q)^2)^Q$.
The retained prefix contains $J_Q$, and (B16) follows from the preceding
induction. All choices of constants are made before any inner-depth or
outer-height iteration.
:::

## Logarithmic distortion and the full inner-depth profile

:::{prf:lemma} Uniform burn-in for terminal-degree distortion
:label: lem:sol-sz-v2-height-distortion
Let $\eta=(e+1)^{-1}$. For $M,x\ge1$ and integer $r\ge1$,
$$
 0\le\ell_r(Mx)-\ell_r(x)
 \le [v\mapsto\log(1+\eta v)]^{\circ(r-1)}(\log M).
                                                               \tag{B22}
$$
For $r\ge1+\log^*M$ the right side is at most
$2\eta^{r-1-\log^*M}$.
Consequently, for fixed $C_T\ge1$, sufficiently large universal $C_b$
and $r_*\ge2$, set $r_Q=\max\{r_*,\lceil C_bt(Q)\rceil\}$.
For $0<a\le1$, $r\ge r_Q$ and
$d<2C_TQ^2(r+1)^2\log(e+a^{-1})$,
$$
 \ell_r(d)\le\zeta_r\ell_{r+1}(a^{-1}),\qquad
 \zeta_r=1+2\eta^{r/2}.                           \tag{B23}
$$
The products $\prod_{r=r_Q}^R(1+r^{-2})^2\zeta_r^2$ have a universal
upper bound, independent of $Q$ and the finite terminal depth $R$.
:::

:::{prf:proof}
First $g(Mx)-g(x)\le\log M$. If $y\ge1$ and $v\ge0$,
$g(y+v)-g(y)\le\log(1+v/(e+1))$. Iteration proves (B22).
The map $F(v)=\log(1+\eta v)$ obeys $F(v)\le\eta v$ everywhere
and $F(v)\le\log v$ for $v\ge2$, because $1+\eta v\le v$ there.
Starting from $\log M$, its orbit reaches $[0,2]$ in at most
$\log^*M$ steps; once in that interval it contracts by $\eta$.
This gives the displayed bound, also directly if $1\le M\le e$.

For $M=2C_TQ^2(r+1)^2$, there is fixed $c_T$ such that
$1+\log^*M\le c_T+\max\{t(Q),\log^*(r+1)\}$.
Indeed with $N=\max\{16,2C_T,Q,r+1\}$, $M\le N^5\le e^N$;
the bounded small-argument range is absorbed in $c_T$.
For sufficiently large $r$, $\log^*(r+1)\le1+\log(r+1)\le r/4$.
Choose $C_b,r_*$ so $r\ge r_Q$ also implies
$r\ge4t(Q)$ and $r\ge4c_T$. Then $1+\log^*M\le r/2$.
Apply (B22) at $x=g(a^{-1})\ge1$; its unperturbed iterate equals
$\ell_{r+1}(a^{-1})\ge1$, proving (B23).
Finally the logarithm of the product is bounded by
$$2\sum_{r\ge r_Q}r^{-2}+4\sum_{r\ge r_Q}\eta^{r/2},$$
which is universally finite for $r_Q\ge2$.
:::

:::{prf:lemma} A full profile from a seed and one starting depth
:label: lem:sol-sz-v2-height-profile
Suppose $G$ satisfies the preceding coefficient-seed and block-realization
hypotheses, including (B6),(B7). For each odd $Q\ge3$, suppose
$M_Q\ge G(Q)^2$ and every regular covariance contraction satisfies
$$C_P\le M_Q\ell_{r_Q}(a^{-1})^2\quad(a>0).        \tag{B24}$$
Then uniformly for $r\ge r_Q$,
$$
 Z_Q\le C M_Q(r+1)^{1/Q}\ell_r(a^{-1})^2,\qquad
 C_P\le C M_Q(r+1)^{1/Q}\ell_r(a^{-1})^2.          \tag{B25}
$$
Here $r_Q$ is the preceding universal starting depth; the constant depends
only on the fixed seed-comparison constants, not on $M_Q,Q,r$ or the law.
:::

:::{prf:proof}
By (B4),(B13) and $M_Q\ge G(Q)^2$,
$H_Q\le CM_Q$ and $a_Q+s_Q+1\le(CM_Q)^Q$.
Set $A_Q=A M_Q$, where one sufficiently large universal $A$ will be
chosen. At an already established depth $r\ge r_Q$ suppose
$Z_Q\le\Gamma_r^2\ell_r(a^{-1})^2$, where
$\Gamma_r^2\ge A_Q(r+1)^{1/Q}$. The block radius's static coefficient
bound and the static coefficient transfer give simultaneously
$$
 c_k^2\le[\widehat\Gamma^2\ell_r(k)^2]^{k-1},
 \quad c_k^2\le g_0(k)^{k-1},\quad
 \widehat\Gamma=(1+r^{-2})\Gamma_r.                \tag{B26}
$$
The transfer's only premise is the previously established scalar profile;
no continuity of $Z_Q$ or of its finite defining block length is used.

Put $s=r+1$, $\delta=(64Qs)^{-1}$, $p=\delta/128$,
$b=(1-2p)^{-1}$, and
$k_0=\lceil100\delta^{-1}\log(M/\delta)\rceil$, where a universal
$M$ larger than all fixed frame constants is fixed once.
Let $d_0$ be the least dyadic integer at least $Q$, and for dyadic
$d\ge d_0$ suppose for a contradiction that
$$Z_Q>b^4e^\delta\widehat\Gamma^2\ell_r(d)^2.      \tag{B27}$$
Take $A$ so large that $A_Q>2H_Q$. Then (B27) excludes the floor:
$z=Z_Q$ is an actual radius with the single family of (B15).
For $u=z^{-1}$,
$$
 b^4u\widehat\Gamma^2\ell_r(d)^2<e^{-\delta},
 \quad u\le A_Q^{-1}s^{-1/Q},\quad
 u^Q\le A_Q^{-Q}s^{-1}.                           \tag{B28}
$$
Its retained range covers $2d_0-1<4Q$, and, provided $a_Qu^Q\le p$,
$$
 \nu\le u/(1-a_Qu^Q),\quad P_{2d_0-1}\le s_Qu^Q,
 \quad D_0:=\max(\nu-u,0)\le2a_Qu^{Q+1}.
$$
Before a first exit of mass $p$, required normalizers are at most
$B_*\le u/(1-p)^2\le bu$; hence $t_*\le b$ in (B2).
Its loss estimate is bounded by
$$
 \theta_d=C_\theta'\sum_{k<d\ {\rm dyadic}}k^8(b^4u)^kc_k^2,
 \quad \Delta_d=s_Qu^Q+2C_F\sum_{d_0\le k<d\ {\rm dyadic}}
                        k^2(bu)^kc_k^2,
 \quad\tau_d=C_Fd(bu)^dc_d^2,                     \tag{B29}
$$
where $C_\theta'=5184C_F\cdot16$ because the block envelope has $E=4$.

**Uniform kernel estimates.** Since $k_0\le C(Qs)^2$, (B6) implies
$g_0(k_0)\le Cg_0(Q)s^{1/Q}\le\Gamma_r^2/4$ after increasing $A$.
For $k\le k_0$, the seed and (B28) give
$$
 (b^4u)^kc_k^2\le b^4u\,4^{-(k-1)},
 \quad (bu)^kc_k^2\le b^Qu^Qg_0(k)^{Q-1}4^{-(k-Q)}\ (k\ge Q).
$$
Therefore the low-degree kernel is at most $Cu$, and its low-degree
coherent sum is at most $D_Qu^Q$, with
$D_Q^{1/Q}\le Cg_0(Q)$ by (B7); use $b\le2$.
For $k_0<k<d$, the first bound in (B26) gives
$$
 (b^4u)^kc_k^2\le b^4u e^{-\delta(k-1)},\qquad
 (bu)^kc_k^2\le e^{-\delta k}.
$$
For each fixed integer $h\ge0$,
$$
 \sum_{k>k_0}k^he^{-\delta k}
 \le C_h\delta^{-h-1}e^{-\delta k_0/2},\qquad
 e^{-\delta k_0/2}\le(\delta/M)^{50}.
$$
For the first inequality remove half of the exponential and integrate
$(x+1)^he^{-\delta x/2}$ over unit intervals; expansion into monomials
gives $C_h\delta^{-h-1}$. Choosing $M$ fixed large makes the two
tail contributions at most $u$ and $p/512$ respectively. Thus
$$
 \theta_d\le C_\theta u,\qquad
 \Delta_d\le(s_Q+D_Q)u^Q+p/512.                   \tag{B30}
$$

**The matched comparison.** Choose $A$ once so that
$$
 A_Q\ge\max\{2H_Q,16,16C_\theta,Cg_0(Q)\},
$$
$$
 A_Q^Q\ge2^{24}Q(a_Q+s_Q+D_Q+4C_\theta a_Q+1).    \tag{B31}
$$
These simultaneous inequalities are possible with one universal $A$:
every term's $Q$th root is bounded by a constant times $M_Q$, and
$Q^{1/Q}$ is uniformly bounded. The block comparison gives
$\lambda\ge1/(z+3)\ge u/2$. Equations (B28)–(B31) imply
$$
 \nu\le1/4,\quad D_0\le u,\quad a_Qu^Q\le p,
 \quad\theta_du/\lambda\le1/8,
 \quad\Delta_d+\theta_dD_0/\lambda\le p/64,
 \quad u+D_0/p\le2u.                             \tag{B32}
$$
For example $\theta_dD_0/\lambda\le4C_\theta a_Qu^{Q+1}$ and
$D_0/p\le16384Qa_QA_Q^{-Q}u\le u$; all remaining inequalities
follow by inserting $u^Q\le A_Q^{-Q}/s$ into (B31).

Here is the finite comparison with this matched scale, to make explicit
that no generic $R$-budget is substituted for it. If a delayed bound
$P_N\le\Delta+N\tau+(\theta/\lambda)X_{\max(N-2,0)}$
has $p_0+p_1\le\Delta$ and the conditions in (B32), then
$$a<12(u+D_0/p)\tau.                              \tag{B33}$$
Indeed the actual matched budget gives
$X_{N-2}\le D_0+uP_N$ and $a\le D_0+u(p_0+p_1)\le D_0+up$.
If the reverse of (B33) held, let
$m=\lceil(D_0+up)/a\rceil$, $M_1=m+1$; then
$M_1\tau\le p/4$.
Before or at a first exiting prefix $N\le M_1$ all required normalizers
use earlier masses at least $1-p$ and so are at most $\nu/(1-p)$;
the possible successor remains positive since $1-p-\nu>0$.
The delayed estimate yields
$P_N\le p/64+p/4+P_N/8$, hence $P_N\le cp$ with $c=17/56<1$.
No exit occurs. At time $m$ the budget and surviving masses imply
$$
 (1-cp)(D_0+up)\le aV_m\le D_0+cup.
$$
Their difference is at least $up(1-2c-cp)>0$, a contradiction.
This proves (B33). The retained prefix supplies its two initial losses.
Apply it to (B29) to get
$a<24u\tau_d\le24C_Fd(bu)^dc_d^2$.

For $0<a\le1$, select a dyadic integer
$$
 C_TQ^2s^2\log(e+a^{-1})\le d
 <2C_TQ^2s^2\log(e+a^{-1}).                       \tag{B34}
$$
A universal large $C_T$ ensures $d\ge d_0$ and
$\log(24C_Fd/a)\le\delta d$:
the former logarithm is at most
$\log(48C_FC_T)+2\log Q+2\log s+2\log(e+a^{-1})$,
whereas $\delta d\ge(C_T/64)Qs\log(e+a^{-1})$.
Writing $L=\widehat\Gamma^2\ell_r(d)^2\ge1$, (B26),(B28) would give
$$
 a<24C_FdL^{-1}(buL)^d\le24C_Fd e^{-\delta d}\le a.
$$
Thus (B27) is impossible. For $a\ge1$, Brascamp–Lieb gives
$C_P\le1$ and $Z_Q\le H_Q$, already covered by the same large amplitude.

**Closing all depths.** The distortion lemma now implies
$$
 Z_Q\le b^4e^\delta(1+r^{-2})^2\Gamma_r^2
                 \zeta_r^2\ell_{r+1}(a^{-1})^2.
$$
Since
$\log(b^4e^\delta)\le16p+\delta=9/(512Qs)
\le Q^{-1}\log(1+1/s)$, define
$$
 J_{r_Q}=1,\quad J_{r+1}=J_r(1+r^{-2})^2\zeta_r^2,
 \quad\Gamma_r^2=A_Q(r+1)^{1/Q}J_r.
$$
All $J_r$ are universally bounded. The initial bound follows from
$Z_Q\le\max(H_Q,C_P)$ and (B24) by increasing the same universal $A$.
Finite induction gives the first inequality in (B25), with its
coefficient transfer at each step justified by the previous profile.
Finally $C_P\le Z_Q+3$ and $M_Q,\ell_r\ge1$ absorb the additive
constant once, proving the second inequality.
:::

## Repeating the height reduction

:::{prf:theorem} Fixed-cost repeated height reduction
:label: thm:sol-sz-v2-height-reduction
There are universal $A_1,C_*,C_e,C_b\ge1$ and $r_*\ge2$ such that,
with $A_j=A_1C_*^{j-1}$ and
$r_Q=\max\{r_*,\lceil C_bt(Q)\rceil\}$, every regular covariance
contraction satisfies
$$
 C_P\le A_jt_j(Q)^{1/3}(r+1)^{1/Q}\ell_r(a^{-1})^2
 \quad(j\ge1,\ Q\ge3\text{ odd},\ r\ge r_Q).
$$
Every centered log-concave covariance contraction also satisfies
$$
 c_d\le[C_e\sqrt{A_j}\,t_{j+1}(d)^{1/6}]^{d-1}
 \quad(j,d\ge1).
$$
This is [](#prop:sz-v2-height-reduction).
:::

:::{prf:proof}
For $G=G_*$, the initial inner theorem at $r_Q\le Ct(Q)$ gives
$C_P\le Ct(Q)^{1/3}\ell_{r_Q}(a^{-1})^2$.
Its amplitude dominates $G_*(Q)^2$ after one enlargement. Apply (B25)
with $M_Q=Ct(Q)^{1/3}$ to obtain the asserted curvature profile at
$j=1$, choosing one universal $A_1\ge1$.

We next extract coefficients from any established stage $j$, without
changing its constant. Fix $d\ge2$, write $h=t(d)$ and choose
$r=\lceil C_rh\rceil$ for a fixed sufficiently large $C_r$.
The logarithm comparison used for the original seed gives
$\ell_r(d)\le5$. Let $k$ be the least odd integer at least
$\max\{3,\log(r+1)\}$. For all $h$ above a fixed threshold,
$$k\le h,\qquad r_k\le r,\qquad(r+1)^{1/k}\le e.$$
Indeed $k\le\log(C_rh+2)+3$ grows slower than $h$, and
$r_k\le C t(k)\le C'k$ grows slower than $r$; the finite remaining
range is handled below. The stage-$j$ profile at order $k$ yields,
uniformly in the regular law,
$$
 C_P\le e A_jt_j(k)^{1/3}\ell_r(a^{-1})^2
 \le e A_jt_{j+1}(d)^{1/3}\ell_r(a^{-1})^2.
$$
Repeated Poincaré on Appell derivatives then supplies the coefficient
premise of the static transfer with
$\Gamma^2=e A_jt_{j+1}(d)^{1/3}\ge1$. The transfer at this fixed
$r$ gives
$c_d\le[5(1+r^{-2})\sqrt{e A_j}\,t_{j+1}(d)^{1/6}]^{d-1}$.
If $h$ is below the fixed threshold, $G_*(d)$ is bounded by a universal
constant. Since $A_j\ge1$ and $t_{j+1}(d)\ge3$, increasing one
$C_e$ covers this entire exceptional range uniformly in $j$.
Degree one is the covariance bound. The transfer already covers
singular covariances and nonsmooth laws, so the coefficient conclusion
has exactly the stated class.

Suppose the curvature profile is established through stage $j-1$.
Its coefficient conclusion permits the capped seed
$$G_j(x)=\min\{G_*(x),C_e\sqrt{A_{j-1}}t_j(x)^{1/6}\}.$$
The seed lemma shows that every block and kernel constant required for
(B25) is uniform in $j$ and $A_{j-1}$. It remains to initialize at
the same $r_Q$, rather than introduce a stage-dependent depth.
Let $k$ be the least odd integer at least $\max\{3,\log(r_Q+1)\}$.
If $t(Q)$ exceeds a fixed threshold, then $k\le t(Q)$,
$r_k\le r_Q$, and $(r_Q+1)^{1/k}\le e$, by the same growth
comparisons as above. Applying the previous profile at order $k$
and depth $r_Q$ gives
$$
 C_P\le e A_{j-1}t_{j-1}(k)^{1/3}\ell_{r_Q}(a^{-1})^2
 \le e A_{j-1}t_j(Q)^{1/3}\ell_{r_Q}(a^{-1})^2.
$$
If $t(Q)$ is below that threshold, $r_Q$ is bounded by a fixed
constant. Use order three instead: $r_3\le r_Q$ by monotonicity,
$t_{j-1}(3)=3$, and $(r_Q+1)^{1/3}$ is uniformly bounded.
This gives the same initial estimate with a larger universal constant.
Therefore we may take
$M_Q=C_M A_{j-1}t_j(Q)^{1/3}$ in (B24), choosing $C_M$ also to
dominate $C_e^2$, so $M_Q\ge G_j(Q)^2$.
The full-profile lemma proves the next curvature stage with
$A_j=C_*A_{j-1}$ for a single universal $C_*$. The coefficient
extraction just proved gives its accompanying coefficient estimate.
Finite induction completes both statements, with the same depths
$r_Q$ at every stage.
:::

**Source mapping and fences.** The two independent joint-frame interfaces
reconstruct Lemmas 8.11 and 8.13. The local orbit and restart reconstruct
the mechanism of Lemmas 8.19–8.20. The fixed-margin extension and finite
odd-order induction give the interface of Proposition 8.22 with enlarged
universal constants; no near-unit floor is claimed. The final three
arguments reconstruct Lemma 8.23 and Propositions 8.24, 8.25 and 8.1.
Small degrees use the original cap at every repetition; block floors and
depth thresholds are fixed before their respective inductions. This
respects the uniform-admissibility warning in the brief. The cost
$C_*^{j-1}$ still grows, so this proof does not itself establish KLS or
uniform exponential coefficients. No additional `bounded_by` edge is
proposed, and no CMH, occupation, or trace premise is discharged.
