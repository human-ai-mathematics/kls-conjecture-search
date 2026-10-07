---
title: 'Song–Zhang v2: finite chains with retained bounds'
ledger-node: prop:sz-v2-finite-chain-blocks
numbering:
  enumerator: "148.%s"
---

*Part of the second version of Song–Zhang, Chapter [](#sec:sz-v2-blocks); the reading order is on the [full proofs](#sec:proofs-sz-v2) page.*

**Overview.** This reconstructs the analytic finite-chain construction
behind Proposition 9.23 of [@SongZhang2026ConstantKLS], including its
one-inherited-floor specialization. It proves
[](#prop:sz-v2-finite-chain-blocks) from the explicit raw-frame,
normalization, Green, restart, and finite-power inputs below.
No small-loss or summable profile is an input.

**Dependencies.** Use [](#def:sz-v2-common-radius),
[](#prop:sz-v2-common-radius), [](#thm:sz-polynomial-variance),
[](#lem:sz-v2-operator-block-primitives), [](#lem:sz-v2-normalized-hierarchy),
[](#lem:sz-v2-mesoscopic-powers), [](#lem:sz-v2-raw-joint-frame),
[](#lem:sz-v2-propagated-joint-loss), [](#lem:sz-v2-orbit-green-restart),
[](#lem:sz-v2-block-extension), and [](#lem:sz-v2-block-propagation).
Every argument is finite. No BKL result or KLS assertion is used.

## A degree sum uniform in the number of retained bounds

:::{prf:lemma} Disjoint degree ranges
:label: lem:sol-sz-v2-chain-moment
Fix $M,h\geq0$ integral and $c>0$. For a finite sequence
$0<\alpha_N\leq\cdots\leq\alpha_0\leq1/16$, set
$K_i=\lceil L\alpha_i^{-2}\rceil$. Let nondecreasing integers $\Xi_i$
satisfy $\Xi_i\geq K_{i+1}$ for $i<N$. Suppose $0\leq\rho_k\leq1$,
$\rho_k\leq C_0^{-1}$ for $k\leq16K_0$, and
$\rho_k\leq(1+\alpha_i)^{-1}$ for $k\leq\Xi_i$.
Then
$$
 \sum_{k\geq h+1}k^M\rho_k^{k-h}e^{-c\alpha_N(k-h)}\leq C_{M,h,c},
$$
uniformly in $N$, all margins and all such sequences. The bound can be
made arbitrarily small by fixed increases of $L,C_0$.
:::

:::{prf:proof}
Choose $L$ so $K_0\geq2h+2$. The range $k\leq K_0$ is bounded by
$\sum_{j\geq1}(j+h)^MC_0^{-j}$. Partition the remaining integers into
$(K_0,\Xi_0]$, $(\Xi_{i-1},\Xi_i]$ for $1\leq i<N$, and
$(\Xi_{N-1},\infty)$. Repeated endpoints give empty intervals and
contribute nothing. In the $i$th finite interval $k>K_i$ and hence
$\alpha_i k\geq\sqrt{Lk}$. Moreover
$$
 \rho_k^{k-h}\leq\exp[-\alpha_i(k-h)/2]
 \leq\exp[-\sqrt{Lk}/4].
$$
In the last interval the same conclusion, with constant $c/2$, follows
from $k>K_N$ and the explicit $\alpha_N$ exponential factor. Because
these intervals are disjoint, their total is bounded by the single series
$$
 \sum_{k>K_0}k^M\exp[-b\sqrt{Lk}],\qquad b=\min\{1/4,c/2\}>0.
$$
For integers $l\geq1$, the range $l^2\leq k<(l+1)^2$ contains at most
$2l+1$ terms, each bounded by $(l+1)^{2M}e^{-b\sqrt L\,l}$.
The resulting polynomial times geometric series converges. With $L\geq1$
its summands are dominated by the summable series at $L=1$ and decrease
to zero as $L\to\infty$. The finite initial range is made small by $C_0$.
There is no factor proportional to the number of intervals.
:::


## Actual block realization

Before the height bookkeeping, the degree sum can be used to retain a
finite chain of coefficient floors in an actual block construction.
The following formulation records separately the orbit and normalized
frame inputs, so the dependency is visible.

:::{prf:lemma} Finite chains of coefficient floors
:label: lem:sol-sz-v2-chain-blocks
Let $G_*$ be a fixed universal coefficient seed. Assume it is
nondecreasing, $G_*\geq1$,
$G_*(k)^2\leq C_*k$, and $G_*(R^R)^2\leq R/2$ for all sufficiently
large $R$, with fixed universal constants. Let $G,H_0,\ldots,H_{N-1}$
be nondecreasing valid coefficient majorants with
$1\leq G\leq H_l\leq G_*$ and $c_k\leq G(k)^{k-1}$.
Fix $0<\epsilon=\alpha_N\leq\alpha_{N-1}\leq\cdots\leq\alpha_0\leq1/16$.
Put
$$
 K_l=\lceil C_{\rm cut}\alpha_l^{-2}\rceil,\quad
 \Xi_l=\lceil4C_{\rm deg}\alpha_l^{-1}K_{l+1}\rceil,
 \quad X=C_XQ^2,
$$
$$
 F^2=\max\{G(X^X)^2,C_0G_*(16K_0)^2,C_0,
              (1+\alpha_l)H_l(\Xi_l)^2:0\leq l<N\},
 \quad H_Q=(1+2\epsilon)F^2.
$$
Here $Q\geq3$ is odd. Use the regular measure class and operators of
[](#def:sz-v2-common-radius). The joint-frame inputs are
[](#lem:sz-v2-raw-joint-frame) and [](#lem:sz-v2-propagated-joint-loss),
and the initial power estimate is [](#lem:sz-v2-mesoscopic-powers).
There is an assignment $Z_Q$ with
$$
 H_Q\leq Z_Q\leq\max\{H_Q,R\},\qquad \mathcal A\leq Z_Q,
$$
and constants $a_Q,s_Q\geq0$ obeying
$$
 a_Q+s_Q+1\leq C(F^2/4)^{Q-3}\leq F^{2Q}.
$$
If $Z_Q>H_Q$, write $z=Z_Q$, $u=z^{-1}$. One actual centered unit
starting family has energy and losses satisfying
$$
 \nu\leq{u\over1-a_Qu^Q},\qquad
 P_J\leq s_Qu^Q\quad(1\leq J\leq J_Q),\qquad
 aV_M+X_M\leq\nu-u+uP_{M+1}\quad(M\geq0),
$$
and
$$
 \|\mathcal T^h\|\leq4(h+1)z^{h/2}\quad(h\geq0),\qquad
 0\leq R-z\leq\min\{1,C/R\},\qquad a_Qu^Q\leq1/8.
$$
For each odd $p\leq Q$, choose $d_p,e_p$ to be the least dyadic
integers at least $4p,8p$ when $p\leq K_0$. When
$K_l<p\leq K_{l+1}$ choose both to be the least dyadic integer at
least $C_{\rm deg}p/\alpha_l$; when $p>K_N$ use $\epsilon$ instead.
Set $J_p=4e_p$. Constants are independent of $N$, the margins, majorants
and order. The assertion about an actual family is made only above the floor.
:::

:::{prf:proof}
Write $D=1+\epsilon$ and $\kappa_q=(F^2/4)^{q-1}$ for odd $q\geq1$.
The constants for the two joint frames are fixed before any cutoffs.
First fix $C_{\rm cut}$ and $C_{\rm deg}$, then the Green, restart and
extension constants, and finally increase $C_0,C_X$ to exceed their
finitely many universal thresholds. Enlarging $C_0,C_X$ only raises
the floor or available degree range.

For each tested degree put
$$
 \rho_k=\min\{1,G_*(k)^2/F^2,H_l(k)^2/F^2:0\leq l<N\}.
$$
The preceding disjoint-range lemma gives uniformly bounded, and when
needed uniformly small, moments with any of the finitely many powers
$k^M$ used below. If $G(d)\leq F$ and $z\geq DF^2$, then for $k\leq d$
$$
 G(k)^2/z\leq\rho_k e^{-\epsilon/2}.
$$
The raw frame under $\|\mathcal T^h\|\leq4(h+1)z^{h/2}$ has the form
$$
 l_j\leq C_Fe c_e^2z^{-(e-1)}b_{j-e+1}
 +C\sum_{k<e,\ k\ {\rm dyadic}}k^7c_k^2z^{-k}
       \sum_{s=k}^{4k-2}D_{j-s},\qquad j\geq2e-1. \tag{F1}
$$
Use at each $j$ the largest available dyadic $e\leq d$.
Together with the degree-two identity this gives a convolution kernel
whose zeroth and first moments are at most $C/z$: summing over the
$O(k)$ delays gives powers $k^8$ and $k^9$, respectively.
Before the orbit has been bounded, propagation gives
$b_j\leq16(j+1)^2$. A degree $k<d$ is used only for
$2k-1\leq j\leq4k-2$. Its contribution to the early weighted coherent
sum, after multiplication by $z$, is at most
$C k^6\rho_k^{k-2}e^{-\epsilon(k-2)/2}$, because
$G(k)^2\leq C_*k$. Degree two is bounded directly by the fixed
quadratic estimate. The moment lemma therefore gives weighted early
sum $C/z$. For later indices the coherent term is
$\gamma b_{j-d+1}$, with $\gamma=C_Fd c_d^2z^{-(d-1)}$.
These are exactly the hypotheses of the Green sequence lemma, with a
universal $K$ independent of $N$.

Consider extension at odd $q$ from an already initialized actual family.
Let $\omega_q=1$ in the first band and equal the margin of its band
otherwise; put $\beta=1+\omega_q/128$.
Before the exit level of [](#lem:sz-v2-block-extension), the normalizers
are at most $\beta u$ when its two smallness bounds are at most
$\omega_q/1024$. The normalized joint frame has kernel bounded by
$$
 Cu\sum_{k<e_q,\ k\ {\rm dyadic}}k^8
       (\beta^4G(k)^2/z)^{k-1}. \tag{F2}
$$
In the small band all degrees are below $16K_0$, so the geometric
floor absorbs $\beta^4$. In a later band the tested degrees lie below
that band's $\Xi_l$. Earlier margins are no smaller than $\omega_q$;
$4\log(1+\omega_q/128)\leq\omega_q/32$ consumes only a fixed
fraction of $\log(1+\alpha_l)\geq\alpha_l/2$.
The last range uses $z/F^2\geq1+\epsilon$. Thus (F2) is at most
$C_\theta u$, independently of the number of bands.

For $d=e_q$, $g=G(d)^2$, and $\rho=g/F^2$, the terminal term
$\tau=C_Fd(\beta u)^dc_d^2$ satisfies
$$
 {\tau\over\kappa_q\kappa_{q-2}u^{2q}}
 \leq C_Fd g^3 4^{2q-4}\rho^{d-4}\beta^dD^{2q-d}. \tag{F3}
$$
This follows by substituting $c_d^2\leq g^{d-1}$ and $z\geq DF^2$;
the identity $(F^2)^3\rho^{d-1}=g^3\rho^{d-4}$ removes the floor.
In the small band $8q\leq d<16q$, $\rho\leq C_0^{-1}$, and
(F3) is at most $Cq^4C_0^4(16\beta^{16}/C_0^8)^q$.
In another finite band $d\geq C_{\rm deg}q/\alpha_l$,
$\rho\leq(1+\alpha_l)^{-1}$ and $\beta=1+\alpha_l/128$.
The exponential damping dominates $4^{2q}$; since
$q>K_l$ gives $\alpha_l^{-1}<\sqrt q$, the residual polynomial is
at most $Cq^6e^{-cC_{\rm deg}q}$. In the final band use $D^{2q-d}$
instead of the $\rho$ factor and obtain the same bound.
Fixed choices of constants make (F3) at most $C_F$.
Thus the delayed normalized frame and the exact matched budget satisfy
all loss-estimate inputs of [](#lem:sz-v2-block-extension).

For initialization at order $p\geq5$, suppose $m$ is within a factor
four of $z^{p-2}/\kappa_{p-2}$. The two coherent smallness expressions
are bounded by
$$
 \gamma m^2/z\leq Cd g\rho^{d-2}4^{2p-6}D^{2p-d-4},\quad
 J_p\gamma zm\leq CJ_pd g^2\rho^{d-3}4^{p-3}D^{p-d},\quad d=d_p.
$$
In the small band these are at most
$Cp^2C_0^2(16/C_0^4)^p$ and $Cp^4C_0^3(4/C_0^4)^p$.
In each other band its own damping bounds them by
$Cp^3e^{-cC_{\rm deg}p}$ and $Cp^6e^{-cC_{\rm deg}p}$.
These estimates are uniform in the band index, without summing them.
Also $m\geq cF^2 4^{p-3}D^{p-2}$, whereas $J_p,d_p\leq Cp^{3/2}$,
so $m\geq2d_p$ and $J_p\leq m/4$. The Green and actual-restart
lemmas now give $a_p+s_p+1\leq C\kappa_{p-2}$ once propagation has
been verified. The extension smallness bounds follow from
$C\kappa_{q-2}z^{-q}\leq CF^{-6}4^{3-q}D^{-q}$;
dividing by any nonsmall-band margin costs at most $\sqrt q$.

It remains to construct the blocks in an order that supplies propagation
before invoking Green. Work first in the branch $\mathcal A>H_Q$.
Start with $m_3=\lfloor R\rfloor$ and
$z_3=\|\mathcal T^{m_3}\|^{2/m_3}$. The mesoscopic estimate gives
$R-z_3\leq C_*/R$. Greedy division by $m_3$ with the remainder
estimated by $R$ gives a base propagation factor
$\exp[m_3(R-z_3)/(2z_3)]\leq2$ for large $R$.
Here $d_3=16,e_3=32,J_3=128$; the fixed-degree original seed makes the
two coherent errors $O(z_3^{-14})$ and $O(J_3z_3^{-13})$.
The lower-radius argument below applies also at this base.

Given the constructed order $q$, set
$$
 m_{q+2}=\lfloor z_q^q/\kappa_q\rfloor,\quad
 z_{q+2}=\|\mathcal T^{m_{q+2}}\|^{2/m_{q+2}},\quad
 \Delta_q=C_b\kappa_{q-2}z_q^{1-q}.
$$
Extension gives $z_{q+2}\geq z_q-\Delta_q$.
Every proposed length is at most $R^Q$. If $R\leq X$, its lower
coefficients are bounded by $G(X^X)^2\leq F^2<\mathcal A$.
If $X<R<2\mathcal A$, use $Q<R$ and
$G_*(R^R)^2\leq R/2<\mathcal A$.
In either case the common-radius block maximum forces
$z_{q+2}\geq\mathcal A$. If $R\geq2\mathcal A$, use the mesoscopic
gap and the previously proved decrement ratios: their sum, including
the current bridge, is at most $2\Delta_3=O(R^{-2})$, so
$z_{q+2}\geq R-C_*/R-O(R^{-2})\geq\mathcal A$.
There is no use of the new ratio in proving this lower bound.

Now the new ratio can be estimated:
$$
 {\Delta_{q+2}\over\Delta_q}
 ={F^4\over16z_{q+2}^2}(z_q/z_{q+2})^{q-1}\leq1/8.
$$
For an upward radius step the last factor is at most one. For a downward
step use $q\Delta_q/z_q\leq CF^{-6}$ and enlarge $C_0$ so the last
factor is at most two. Thus all constructed radii satisfy
$R-z_q\leq C/R\leq1$.
The length ratio for $q\geq5$, before integer rounding, is
$16(z_q/F^2)^2(z_q/z_{q-2})^{q-2}$; the downward correction is
$e^{-O(F^{-6})}$. Rounding loses an arbitrarily small fixed fraction
because all real lengths exceed $F^24^{q-1}$. The first ratio is
$16(z_3/F^2)^2(z_3/R)$ up to the same rounding error.
Consequently successive lengths grow by at least four.

Apply [](#lem:sz-v2-block-propagation) to this constructed prefix.
Its remainder cost is $O(1/R)$ and
$m_{q+2}\Delta_q/z_q\leq C/F^4$.
With a fixed large floor this yields
$\|\mathcal T^h\|\leq4(h+1)z_q^{h/2}$ for every $h$.
Counting only the $O(q)$ constructed levels also gives a global factor
$E_q$ with $\log E_q\leq C/R+Cq/F^4$.
At the proposed next length this implies
$$
 q(\log(z_{q+2}/z_q))_+
 \leq Cq4^{-q}/(F^2R)+Cq^24^{-q}/F^6.
$$
Together with the downward bound it places $m_{q+2}$ within a factor
four of $z_{q+2}^q/\kappa_q$. At this point the new radius, envelope,
and length hypotheses are established. Apply Green and actual restart
to the norm-attaining orbit at this length. This completes the finite
order induction, without using its new Green estimate to establish
its own propagation hypothesis.

Take $Z_Q=z_Q$ in this branch; otherwise take $Z_Q=H_Q$ and make
no assertion about a starting family. The coefficient inequalities
follow from $\mathcal A\leq Z_Q$. All final amplitude estimates follow
from $a_Q+s_Q+1\leq C\kappa_{Q-2}$, and all choices of constants
preceded the finite chain length. The raw and normalized frame inputs (F1)–(F2), including the
delayed-prefix applicability, are exactly the two joint-frame dependencies
named in the statement. No profile conclusion is used.
:::


**Fences respected.** The block radius is bounded using the exact common-radius
maximum before the new decrement ratio is estimated. Propagation is established
before Green is applied, and the retained family supplies its own matched
budget. No small-degree or depth threshold is removed by assertion.
