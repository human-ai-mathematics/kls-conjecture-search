---
title: "Small-loss refinement: scalar estimates and the analytic interface"
ledger-node:
  - lem:sz-v2-profile-calculus
  - lem:sz-v2-profile-refinement
  - prop:sz-v2-small-loss
numbering:
  enumerator: "140.%s"
---

**Overview.** The aim is [](#prop:sz-v2-small-loss), from Section 9 of
[@SongZhang2026ConstantKLS]. The proof combines scalar height estimates, the independently reconstructed
finite-chain block theorem, a near-unit terminal-depth induction, and exact
coefficient return. It does not rely on the claimed conclusion in the source.

**Dependencies.** The coefficient radius is [](#def:sz-v2-common-radius), with
comparison [](#prop:sz-v2-common-radius). The polynomial normalization and regular
measure class are those of [](#thm:sz-polynomial-variance) and
[](#lem:sz-analytic-foundations). No BKL bound, consequence of BKL, or assertion
of KLS is an input.

## Scalar functions and their exact properties

Write $E_0=1$, $E_{k+1}=\exp(E_k)$ and
$\log^*x=\min\{k\geq0:x\leq E_k\}$ for $x\geq1$.
For $x\geq1$ set
$$
 t(x)=1+\log^*(x+2),\quad
 \kappa(x)=\min\{j\geq0:t^{\circ j}(x)\leq3\},\quad
 \chi(x)=\max\{3,1+\kappa(x)\}.
$$
For $f=t,\chi$, define
$$
 \bar f(x)=\max\left\{4,{1\over4}\int_0^4f(x+s)\,ds\right\},
 \qquad W_m(x)=\bar t(\bar\chi^{\circ m}(x)).
$$
We use $g(x)=\log(e+x)$ for $x\geq0$, $\ell_r=g^{\circ r}$,
and $\mathcal L_r=\ell_r/\varrho$, where $g(\varrho)=\varrho$.

:::{prf:lemma} Discrete heights and contraction
:label: lem:sol-sz-v2-scalar-heights
The stopping index $\kappa(x)$ is finite. The maps $t,\chi$ are nondecreasing,
have jumps of size at most one separated by more than four on $[1,\infty)$,
and are at least three. Each averaged map is nondecreasing and $1/4$-Lipschitz,
$$
 \max\{4,f(x)\}\leq\bar f(x)\leq f(x)+1.
$$
Moreover $\bar t(4)=4$, $\bar\chi(x)=4$ for $1\leq x\leq6$,
$W_m(4)=4$, and $W_m$ is $4^{-m-1}$-Lipschitz. For every fixed $x$,
some finite $m$ satisfies $W_m(x)=4$.
:::

:::{prf:proof}
The first jump of $t$ on this domain is at $E_2-2=e^e-2>13$;
all successive jump locations are $E_k-2$ and their gaps increase.
In particular $t=3$ on $[1,13]$. On integer arguments $n\geq4$,
$t(n)\leq n-1$. Indeed this is direct below the first jump; above it,
$\log^*(n+2)\leq n-2$, since $E_{n-2}\geq n+2$ by induction starting
at $n=4$. On real arguments $3<x<4$, $t(x)=3<x$; for $x\geq4$,
monotonicity and the integer estimate give $t(x)\leq\lceil x\rceil-1\leq x$,
with strict inequality at integers as well. The first image is an integer,
and subsequent images decrease strictly until they reach three. This proves
finiteness and monotonicity of $\kappa$.

For integers $n\geq3$, induction gives
$0\leq\kappa(n+1)-\kappa(n)\leq1$. The initial pair $(3,4)$ has
values $(0,1)$. At later pairs use
$\kappa(n)=1+\kappa(t(n))$, the fact that $t(n+1)-t(n)$ is zero or one,
and that the arguments $t(n),t(n+1)$ precede the pair under consideration.
For $x>3$ the same recurrence shows that jumps of $\kappa$ can occur only
at jumps of $t$, with size at most one. The possible jump at three disappears
upon taking $\chi=\max\{3,1+\kappa\}$. Thus
$0\leq f(x+4)-f(x)\leq1$ for either function.

The forward average is locally absolutely continuous, with almost-everywhere
derivative $(f(x+4)-f(x))/4$. Its maximum with a constant has the same
Lipschitz bound. Monotonicity sandwiches the average between $f(x)$ and
$f(x)+1$; the additional floor obeys $4\leq f(x)+1$.
Since $t=3$ through eight and $\chi=3$ through ten, the asserted plateaus
follow. Composition multiplies Lipschitz constants. For $x\geq4$,
$$
 0\leq\bar\chi^{\circ m}(x)-4\leq4^{-m}(x-4).
$$
Choose finite $m$ so the right side is at most two; one additional iterate
then equals four. If $x<4$, the first iterate already equals four.
:::

The contraction and fixed point also give $\bar\chi(x)\le x$ for
$x\ge4$: $\bar\chi(x)\le4+(x-4)/4\le x$. Hence monotonicity
implies $W_m(x)\le\bar t(x)$ for $x\ge4$. On $1\le x\le4$ both
sides are four, so this holds throughout the domain.

:::{prf:lemma} Decreasing costs for polynomial arguments
:label: lem:sol-sz-v2-argument-cost
For fixed $C,p\geq1$ there is $b_{C,p}<\infty$, independent of $m$, such that
$$
 W_m(Cx^p)\leq W_m(x)+b_{C,p}4^{-m}\quad(x\geq1).
$$
There is a universal $b$ such that
$$
 \max\{W_m(xy),W_m(x+y)\}
 \leq\max\{W_m(x),W_m(y)\}+b4^{-m}.
$$
Both inequalities persist after taking the maximum of $W_m$ with any
constant at least four.
:::

:::{prf:proof}
For sufficiently large $x$, depending only on $C,p$,
$Cx^p+2\leq\exp(x+2)$; therefore $t(Cx^p)\leq t(x)+1$ there.
On the remaining compact interval $t(Cx^p)-t(x)$ is bounded above.
Consequently $t(Cx^p)\leq t(x)+b$ everywhere, for a fixed integer $b$.
The integer nonexpansiveness of $\kappa$ proved above gives, when $x>3$,
$$
 \kappa(Cx^p)=1+\kappa(t(Cx^p))
 \leq1+\kappa(t(x))+b=\kappa(x)+b.
$$
The bounded interval $x\leq3$ is handled by enlarging $b$. Taking the
maximum with three proves the fixed-power bound for $\chi$ too.

For either $f$, averaging and the bound $f(x)\leq\bar f(x)\leq f(x)+1$
now give $\bar f(Cx^p)\leq\bar f(x)+b+1$.
For $m\geq1$ apply this to the first $\bar\chi$ and use the
$4^{-m}$ Lipschitz constant of the remaining composition
$\bar t\circ\bar\chi^{\circ(m-1)}$. For $m=0$ use the bound for
$\bar t$. For sums and products put $z=\max\{x,y\}$ and use
$xy\leq z^2$, $x+y\leq2z$. Finally
$\max\{u+c,h\}\leq\max\{u,h\}+c$ for $c\geq0$ proves the last assertion.
:::

:::{prf:lemma} Uniform burn-in for the normalized logarithm
:label: lem:sol-sz-v2-burn-in
There are universal $C,D$ such that, for $x\geq1$,
$0<\eta\leq1/16$, and integers $r\geq Ct(x)+D/\eta$,
$$
 \mathcal L_r(x)^2\leq e^\eta,\qquad
 \mathcal L_r(0)^2\geq e^{-\eta},\qquad
 (1+r^{-2})^2\leq e^\eta.
$$
The weaker condition $r\geq Ct(x)$ gives a universal upper bound on
$\mathcal L_r(x)$.
:::

:::{prf:proof}
The function $g(x)-x$ is strictly decreasing, positive at one and negative
at two; hence $1<\varrho<2$ is unique. Since $0<g'(x)\leq e^{-1}$,
$$
 |\ell_s(y)-\varrho|\leq e^{-s}|y-\varrho|\quad(y\geq0).
$$
For $y\geq5$ one has $e+\log(e+y)\leq y$: it holds at five
($e<11/4$ and $\log(e+5)<9/4$ suffice), and the derivative of the
left side is less than one. Thus $g^{\circ2}(y)\leq\log y$.
Apply this comparison repeatedly while the current value is at least five.
After at most $2\log^*x$ iterations the current value is at most five;
otherwise ordinary logarithm iteration would reach at most one while the
current value remained at least five. The interval $[0,5]$ is invariant
under $g$. A further $s$ iterations give distance at most $5e^{-s}$
from $\varrho$. Taking $s\geq D/\eta$ with fixed sufficiently large $D$
makes this distance at most $\eta/8$; the elementary inequalities
$\log(1+u)\leq u$ and $\log(1-u)\geq-2u$ for $0\leq u\leq1/2$
give the two bounds for $\mathcal L_r$. The same contraction started
at zero proves the lower bound independently of $x$. Finally
$2\log(1+r^{-2})\leq2r^{-2}\leq\eta$ after increasing $D$.
:::

## Moment estimates below and above degree cutoffs

:::{prf:lemma} Uniform three-range sum
:label: lem:sol-sz-v2-three-range
Fix integers $M,h\geq0$ and $c>0$. Let
$0<\epsilon\leq\delta\leq1/16$,
$K_\alpha=\lceil L\alpha^{-2}\rceil$, and $\Xi\geq K_\epsilon$.
Suppose $0\leq\rho_k\leq1$, $\rho_k\leq C_0^{-1}$ for $k\leq16K_\delta$,
and $\rho_k\leq(1+\delta)^{-1}$ for $k\leq\Xi$.
For sufficiently large fixed $L,C_0$, the quantity
$$
 \sum_{k\geq h+1} k^M\rho_k^{k-h}e^{-c\epsilon(k-h)}
$$
is uniformly bounded in $\delta,\epsilon,\rho$. Its supremum tends to zero
as $L$ and $C_0$ tend to infinity.
:::

:::{prf:proof}
Choose $L$ so $K_\delta\geq2h+2$. Up to $K_\delta$, bound the sum by
$\sum_{j\geq1}(j+h)^MC_0^{-j}$, which tends to zero as $C_0\to\infty$.
For $K_\delta<k\leq\Xi$, use
$\log(1+\delta)\geq\delta/2$ and $k-h\geq k/2$ to bound each term
by $k^Me^{-\delta k/4}$. Beyond $\Xi$, use $k^Me^{-c\epsilon k/2}$.
For $0<s\leq1$, $K\geq1$ and fixed $b>0$,
$$
 \sum_{k>K}k^Me^{-bsk}
 \leq e^{-bsK/2}\sum_{k\geq1}k^Me^{-bsk/2}
 \leq C_{M,b}s^{-M-1}e^{-bsK/2}.
$$
The last estimate follows by integration on each unit interval, or from
$k^M\leq C_{M,b}s^{-M}e^{bsk/4}$ followed by a geometric sum.
The two tails are therefore at most
$C\delta^{-M-1}e^{-c_1L/\delta}$ and
$C\epsilon^{-M-1}e^{-c_2L/\epsilon}$. For $u\geq16$,
$u^{M+1}e^{-c_iLu}$ tends uniformly to zero as $L\to\infty$:
split the exponential into two equal factors, use one to dominate the
polynomial, and bound the other by $e^{-8c_iL}$. This proves both claims.
:::

## The claimed small-loss profile and its unresolved input

The two-block Green estimate and the actual restart are proved in
[](#lem:sz-v2-orbit-green-restart). They apply once the raw frame and
Bochner identities have supplied their explicit sequence hypotheses.



Set
$$
 \widehat W_{m,\delta}(x)=\max\{W_m(x),\bar t(\delta^{-1})\},\quad
 R_\delta=\lceil C_R\delta^{-12}\rceil,\quad
 S_m=1+2D\sum_{l=0}^{m-1}4^{-l}.
$$

## Analytic mechanisms available for the iteration

The actual restart, delayed finite extension, and exact-block propagation
are proved separately in [](#lem:sz-v2-orbit-green-restart),
[](#lem:sz-v2-block-extension), and [](#lem:sz-v2-block-propagation).
Their proofs do not depend on the profile targeted here.

For the source's block scales $m_{q+2}\simeq z_q^q/\kappa_q$,
$\kappa_q=(F^2/4)^{q-1}$ and
$\Delta_q=C_b\kappa_{q-2}z_q^{1-q}$, the per-level quantity is
at most $C/F^4$. The lemma explains how a polynomial propagation
bound can be established from already constructed exact block norms
before applying the Green lemma at the next block. It does not by
itself verify the lower radius, length comparability, or degree-frame
hypotheses needed to construct that next block.

:::{prf:lemma} Coherent sums with a near-unit root cost
:label: lem:sol-sz-v2-coherent-root
Fix $C_g,C_F\geq1$. There are fixed $D,C_Q$ such that for every
$0<\epsilon\leq1/16$, integer $Q\geq C_Q\epsilon^{-4}$, and
nondecreasing $g:[1,\infty)\to[1,\infty)$ satisfying
$g(k)\leq C_g k^{1/3}$ at integers,
$$
 \left(2C_F\sum_{k\geq Q} k^2g(k)^{Q-1}e^{-\epsilon(k-Q)}\right)^{1/Q}
 \leq e^\epsilon g(N),\qquad
 N=\lceil D\epsilon^{-2}Q^2\rceil.
$$
:::

:::{prf:proof}
For $Q\leq k\leq N$, monotonicity bounds $g(k)$ by $g(N)$.
Writing $k=Q+l$, and using $\sum_{l\geq0}l^je^{-\epsilon l}
\leq C_j\epsilon^{-j-1}$ for $j=0,1,2$, the corresponding sum is
at most $C\epsilon^{-3}(Q+1)^2g(N)^{Q-1}$.

For $k>N$, the logarithm of $2C_Fk^2g(k)^{Q-1}$ is at most
$C_1Q\log(e+k)$, for a constant depending only on $C_g,C_F$.
Choose $D$ so $C_1Q\log(e+k)\leq\epsilon k/4$ for $k\geq N$.
To justify a uniform choice, $\log(e+k)/k$ decreases on $[1,\infty)$,
so it suffices to check $N$. Up to universal factors the needed ratio
is at most
$$
 {C_1\epsilon\over DQ}
 [\log(D+2)+2\log(\epsilon^{-1})+2\log(Q+1)].
$$
The terms involving $\epsilon\log(\epsilon^{-1})$ are bounded,
and $\log(Q+1)/Q$ is bounded. Increasing $D$ dominates
$\log(D+2)$ and makes this ratio at most $1/4$.
The tail is therefore at most
$C\epsilon^{-1}\exp(\epsilon Q-3\epsilon N/4)\leq1$
after increasing $D$. Since $g(N)\geq1$, the whole sum is at most
$[C\epsilon^{-3}(Q+1)^2+1]g(N)^Q$.
For $Q\geq C_Q\epsilon^{-4}$,
$\log[C\epsilon^{-3}(Q+1)^2+1]\leq\epsilon Q$ with fixed sufficiently
large $C_Q$: the ratio of the left side to $Q$ decreases beyond a
fixed threshold, and at that threshold the remaining quantity is
bounded by a constant times $\epsilon^3\log(\epsilon^{-1})$ plus
$\epsilon^3\log(C_Q+2)$, divided by $C_Q$.
Taking $Q$th roots proves the assertion.
:::

:::{prf:lemma} Summable distortion at a chosen initial depth
:label: lem:sol-sz-v2-distortion
Put $\eta=(e+1)^{-1}$ and $\zeta_v=1+2\eta^{v/2}$.
There is a universal $C$ such that if $r_0\geq C/\epsilon$,
$0<\epsilon\leq1/16$, then for every finite $r\geq r_0$,
$$
 \prod_{v=r_0}^r(1+v^{-2})^2\zeta_v^2\leq e^\epsilon.
$$
:::

:::{prf:proof}
Taking logarithms and using $\log(1+t)\leq t$ bounds the left
logarithm by
$$
 2\sum_{v=r_0}^\infty v^{-2}
 +4\sum_{v=r_0}^\infty\eta^{v/2}
 \leq {2\over r_0-1}+{4\eta^{r_0/2}\over1-\sqrt\eta}.
$$
The first term is at most $\epsilon/2$ for a fixed large $C$.
The second is at most $\epsilon/2$ for another universal enlargement,
because $e^{-cC/\epsilon}/\epsilon$ is uniformly small on
$0<\epsilon\leq1/16$. This proves the bound at every finite endpoint.
:::

## The terminal-depth induction with an arbitrarily small cost

:::{prf:lemma} Near-unit depth step
:label: lem:sol-sz-v2-near-unit-depth
Fix $0<\epsilon\le1/16$ and odd $Q\ge C_Q\epsilon^{-4}$. Suppose
$G,H_l,\alpha_l$ are coefficient bounds and margins as in
[](#prop:sz-v2-finite-chain-blocks). Write $g_0=G^2$ and suppose, for
some $M\ge M_0^*$, where $M_0^*$ is a fixed universal constant,
$$
 F^2\le e^{6\epsilon}M,\quad
 \sup_{s\ge1}g_0(C_k(Qs)^2)s^{-1/Q}\le e^{5\epsilon}M,
 \quad g_0(X^X)\le e^{5\epsilon}M.                 \tag{D1}
$$
Assume also $g_0(k)\le Ck^{1/3}$ with a fixed universal constant.
Let $r_0\ge\max\{r_*,\lceil C_bt(Q)\rceil,\lceil C_b'/\epsilon\rceil\}$.
If the common radius satisfies the initial profile
$$
 \mathcal A\le e^{20\epsilon}M(r_0+1)^{1/Q}
                         \mathcal L_{r_0}(a^{-1})^2,       \tag{D2}
$$
uniformly over the regular law class, then for every $r\ge r_0$,
$$
 \mathcal A\le e^{21\epsilon}M(r+1)^{1/Q}
                         \mathcal L_r(a^{-1})^2.           \tag{D3}
$$
The constants are independent of the number of inherited bounds.
:::

:::{prf:proof}
Set $L=e^{20\epsilon}M$ and
$$
 J_{r_0}=1,\quad J_{r+1}=J_r(1+r^{-2})^2\zeta_r^2,
 \quad\Gamma_r^2={L\over\varrho^2}(r+1)^{1/Q}J_r,
 \quad\zeta_r=1+2(e+1)^{-r/2}.
$$
The product estimate proved above gives $J_r\le e^\epsilon$.
Induct on the statement $\mathcal A\le\Gamma_r^2\ell_r(a^{-1})^2$.
The static transfer at this fixed depth gives
$$
 c_k^2\le[\widehat\Gamma^2\ell_r(k)^2]^{k-1},
 \qquad\widehat\Gamma=(1+r^{-2})\Gamma_r.          \tag{D4}
$$
There is no assumption on continuity of the finite block assignment in
this use of static transfer. Its premise follows from the common-radius
bound, and $\Gamma_r\ge1$ follows by fixing the initial universal amplitude.

Put $s=r+1$, $\xi=(64Qs)^{-1}$, $p=\xi/128$, $b=(1-2p)^{-1}$,
and $k_0=\lceil100\xi^{-1}\log(M_0/\xi)\rceil$, with fixed large $M_0$.
Then $k_0\le C_k(Qs)^2$. For a dyadic $d\ge d_0$, where $d_0$ is the
least dyadic integer at least $Q$, suppose
$$
 \mathcal A>b^4e^\xi\widehat\Gamma^2\ell_r(d)^2.   \tag{D5}
$$
Because $\ell_r(d)\ge\varrho$ and $L\ge e^{20\epsilon}M$, this
exceeds the floor $H_Q=(1+2\epsilon)F^2\le e^{8\epsilon}M$.
Thus the finite-chain construction supplies an actual radius $z\ge\mathcal A$
with its actual family and matched budget. Write $u=z^{-1}$. Then
$$
 b^4u\widehat\Gamma^2\ell_r(d)^2<e^{-\xi},\quad
 u\le L^{-1}s^{-1/Q},\quad u^Q\le L^{-Q}/s.       \tag{D6}
$$
In the notation of that construction, its initial energy $\nu$ and loss
prefix satisfy $\nu\le u/(1-a_Qu^Q)$ and $P_{2d_0-1}\le s_Qu^Q$.
Until a first exit of mass $p$, all normalizers are at most $bu$, and
the power envelope has constant $4$ and polynomial exponent $1$.
The propagated joint-loss lemma therefore gives
$$
 \theta\le C_\theta'\sum_{k<d}k^8(b^4u)^kc_k^2,\quad
 \Delta\le s_Qu^Q+2C_F\sum_{Q\le k<d}k^2(bu)^kc_k^2,
 \quad\tau=C_Fd(bu)^dc_d^2,                       \tag{D7}
$$
where enlarging the sums from dyadic degrees to all integers only
increases these upper bounds.

Here the low-degree kernel has a uniform bound even when the number
of inherited bounds grows. For $k\le k_0$, (D1),(D6) give
$b^4ug_0(k)\le e^{-14\epsilon}b^4\le e^{-13\epsilon}$.
For the initial range $k\le16K_0$, the floor gives the stronger bound
$b^4ug_0(k)\le2/C_0$. In each subsequent inherited range it gives
$b^4ug_0(k)\le e^{-\alpha_l/2}$: the factor $b^4$ is absorbed since
$\log b^4\le16p\ll\epsilon\le\alpha_l$, and $z\ge H_Q$.
Here is the degree sum explicitly. Below $16K_0$ the ratio is
at most $2/C_0$, so its polynomially weighted powers have a uniformly
convergent geometric sum. Partition the remaining degrees into the
successive inherited intervals ending at $\Xi_l$, and the last interval
above $\Xi_{N-1}$. In the $l$th inherited interval $k>K_l$;
therefore $\alpha_l k\ge\sqrt{C_{\rm cut}k}$. In the last interval
$k>K_N$ and the same inequality holds with $\epsilon=\alpha_N$.
After removing the factor $b^4u$, every term is bounded by
$Ck^8\exp[-c\sqrt{C_{\rm cut}k}]$. The intervals are disjoint,
so their sum is bounded by this single convergent series, not by a
constant times the number of intervals. To check convergence, group
$k$ between $v^2$ and $(v+1)^2$ and bound the resulting sum by
$\sum_{v\ge1}(2v+1)(v+1)^{16}e^{-c\sqrt{C_{\rm cut}}v}$.
Thus the low kernel is at most $Cu$, uniformly in the cap chain.
For the low coherent sum use the coherent-root estimate above:
$$
 2C_F\sum_{Q\le k\le k_0}k^2(bu)^kc_k^2
 \le b^Q u^Q E_{Q,\epsilon}=D_Qu^Q,
 \qquad D_Q^{1/Q}\le e^{7\epsilon}M.              \tag{D8}
$$
Indeed $bu g_0(k)\le e^{-\epsilon}$ on this range, and
$E_{Q,\epsilon}^{1/Q}\le e^\epsilon g_0(N)$ with
$N=\lceil D\epsilon^{-2}Q^2\rceil\le X^X$; also $b\le e^\epsilon$.

For $k_0<k<d$, (D4),(D6) give respectively
$(b^4u)^kc_k^2\le b^4u e^{-\xi(k-1)}$ and
$(bu)^kc_k^2\le e^{-\xi k}$. For fixed integer $h\ge0$,
$$
 \sum_{k>k_0}k^he^{-\xi k}
 \le C_h\xi^{-h-1}e^{-\xi k_0/2}
 \le C_h\xi^{-h-1}(\xi/M_0)^{50}.
$$
This follows by integrating the remaining half-exponential over unit
intervals. Choose $M_0$ once to obtain
$$
 \theta\le C_\theta u,\qquad
 \Delta\le(s_Q+D_Q)u^Q+p/512.                    \tag{D9}
$$
The block theorem gives $(a_Q+s_Q+1)^{1/Q}\le C^{1/Q}F^2$.
For all $Q\ge C_Q\epsilon^{-4}$, increasing $C_Q$ once ensures
$\log(CQ)\le\epsilon Q$ for every fixed constant $C$ appearing here.
Consequently (D1),(D8) and the gap between $20\epsilon$ and
$7\epsilon$ ensure simultaneously
$$
 L\ge\max\{16,16C_\theta\},\qquad
 L^Q\ge2^{24}Q(a_Q+s_Q+D_Q+4C_\theta a_Q+1).       \tag{D10}
$$
The first assertion uses the fixed lower bound on the universal amplitude,
not a loss depending on $\epsilon$.

For clarity the finite curvature comparison is included here. Set
$D_0=\max\{\nu-u,0\}\le2a_Qu^{Q+1}$ and let $\lambda=C_P^{-1}$.
The actual-radius comparison gives $\lambda\ge u/2$. Equations
(D6),(D9),(D10) give
$$
 D_0\le u,\quad\nu\le1/4,\quad
 \theta u/\lambda\le1/8,\quad
 \Delta+\theta D_0/\lambda\le p/64,\quad D_0/p\le u.
$$
If $a\ge12(u+D_0/p)\tau$, put
$m=\lceil(D_0+up)/a\rceil$, $M_1=m+1$.
The matched budget at the initial time implies $a\le D_0+up$,
so $M_1\tau\le p/4$. Before or at the first exit $N\le M_1$, the
budget gives $X_{N-2}\le D_0+uP_N$ and the delayed loss bound gives
$P_N\le p/64+p/4+P_N/8$, hence $P_N\le cp$ with $c=17/56$.
The retained prefix supplies the first two losses. All subsequent
normalizers use earlier masses at least $1-p$; the next mass is
positive because $1-p-\nu>0$. No first exit can occur. At time $m$,
$$
 (1-cp)(D_0+up)\le aV_m\le D_0+cup,
$$
which is impossible since the left minus right is at least
$up(1-2c-cp)>0$. Thus $a<12(u+D_0/p)\tau\le24u\tau$.

For $0<a\le1$ take dyadic $d$ between
$C_TQ^2s^2\log(e+a^{-1})$ and twice this quantity. A fixed $C_T$
ensures $d\ge d_0$ and $\log(24C_Fd/a)\le\xi d$: the logarithm
is bounded by $C+2\log Q+2\log s+2\log(e+a^{-1})$, whereas
$\xi d\ge(C_T/64)Qs\log(e+a^{-1})$.
Writing $B=\widehat\Gamma^2\ell_r(d)^2\ge1$, (D4),(D6) contradict
$$
 a<24C_Fd(bu)^dc_d^2
 \le24C_Fd B^{-1}(buB)^d\le24C_Fd e^{-\xi d}\le a.
$$
Hence (D5) is false. For $a\ge1$, Brascamp--Lieb gives
$\mathcal A\le1$, already within the desired bound.

Apply [](#lem:sz-v2-terminal-distortion) to the chosen $d$. Since
$\log(b^4e^\xi)\le16p+\xi\le Q^{-1}\log(1+1/s)$, the resulting
upper bound on $\mathcal A$ is exactly
$\Gamma_{r+1}^2\ell_{r+1}(a^{-1})^2$.
This completes the finite induction on $r$. Using $J_r\le e^\epsilon$
gives (D3).
:::

## Returning coefficients to the next height

:::{prf:lemma} Outer round with a retained profile
:label: lem:sol-sz-v2-outer-round
Suppose $V=W_m$ or $V=\widehat W_{m,\delta}$, $1\le S\le S_*$,
$A\ge A_0$, $R_\delta=\lceil C_R\delta^{-12}\rceil$, and
$$
 \mathcal A\le A[V(r)+S]^{1/3}\mathcal L_r(a^{-1})^2
 \qquad(r\ge R_\delta).                          \tag{E1}
$$
Retain its valid coefficient cap
$$
 H(x)^2=\min\{G_*(x)^2,e^{3\delta}A[V(r_\delta(x))+S]^{1/3}\},
 \quad r_\delta(x)=\max\{R_\delta,\lceil C_rt(x)\rceil+
                                      \lceil D_r/\delta\rceil\}.
$$
Optionally retain earlier caps, provided their floors in the finite-chain
construction are at most $A(4+S)^{1/3}$; its fixed original-seed floor
must also be at most that quantity. With a fixed sufficiently large
$b_*$ with $b_*\le C\log(e+S_*)$ for one universal $C$, put
$$
 D_*=V(\epsilon^{-1})+S+b_*4^{-m},\qquad0<\epsilon\le\delta.
$$
Then, for every $j\ge1$, odd $Q\ge Q_\epsilon$, and
$r\ge r_0(Q):=\max\{R_\delta,\lceil C_bt(Q)\rceil+
\lceil C_b'/\epsilon\rceil\}$,
$$
 \mathcal A\le e^{16\delta+24\epsilon j}A
       \max\{t_j(Q),D_*\}^{1/3}(r+1)^{1/Q}\mathcal L_r(a^{-1})^2.
                                                               \tag{E2}
$$
For the one-cap case, the original-seed floor can instead be bounded
by $e^{4\delta}A D_*^{1/3}$. The same conclusion holds.
:::

:::{prf:proof}
The cap $H$ is valid by static transfer at the fixed depth $r_\delta(d)$:
the squared transfer and burn-in factors cost at most $e^{2\delta}$.
The third $\delta$ leaves room for integer rounding and increasing the
fixed burn-in constants. The coefficient bound is simultaneous on the
whole class, hence the cap may be retained at later stages.
Throughout the proof take minima also with the fixed bound
$C_2t_2(x)^{1/3}$ on squared coefficients supplied by the first
height-reduction stage. This ensures the growth hypothesis $g_0(x)\le Cx^{1/3}$.

Here are the elementary bounds needed for both initialization and
coefficient return. For fixed constants $C,p$,
$$
 V(C\epsilon^{-p})\le V(\epsilon^{-1})+b(C,p)4^{-m}.              \tag{E3}
$$
For the maximum defining $\widehat W$, this follows by taking the
maximum with its constant branch. Also $V$ is $4^{-m-1}$-Lipschitz.
For $Y=C_k(Qs)^2$, $h=t(Q)$ and $y=\log(s)/Q$, the tower definition
gives
$$
 t(X^X)\le h+B_h,\qquad t(Y)\le h+B_h+y.                       \tag{E4}
$$
Indeed $\log(Y+2)\le C Q(1+y)$; the product bound for the remaining
iterated logarithms gives $t(Y)\le t(Q)+C+t(1+y)-3$,
and $t(1+y)\le y+4$. The self-power bound follows by applying the
same argument to $\log(X^X)=X\log X$.
Choose $C_h=C(1+S_*)^2$ with a sufficiently large universal $C$,
and call a height high if
$h\ge C_hR_\delta\epsilon^{-5}$.
At low heights (E4) implies
$$
 r_\delta(Y)\le C(\epsilon^{-17}+y),\qquad
 r_\delta(X^X)\le C\epsilon^{-17}.                            \tag{E5}
$$
Combining (E3), Lipschitz continuity, and $D_*\ge5$ gives
$$
 e^{-y}[V(r_\delta(Y))+S]^{1/3}\le D_*^{1/3},                 \tag{E6}
$$
provided $b_*$ absorbs the fixed constants in (E3).
More explicitly, split (E5) into $C\epsilon^{-17}+C_r'y$,
use (E3) on the first term, and Lipschitz continuity on the second.
This gives $V(r_\delta(Y))+S\le D_*+C_r'4^{-m-1}y$.
Choose $b_*$ above the constant required by (E3), and also so that
$D_*\ge C_r'4^{-m}/12$ for every $m$. Then
$\log(1+C_r'4^{-m}y/(4D_*))/3-y\le0$.
The constant in (E5) is polynomial in $C_h$, while the fixed-power
allowance (E3) is at most $C\log(e+C_h)$: this follows by counting
the additional ordinary logarithms needed to remove a fixed factor
and applying the $4^{-m}$ contraction. Thus all these choices permit
$b_*\le C\log(e+S_*)$.
Thus (E6) has coefficient exactly one; no fixed multiplicative loss
is introduced. The analogous estimate at $X^X$ follows with $y=0$.

We first initialize $j=1$. Use the original cap $H$, and all earlier
caps if present, as the working coefficient majorant. At high heights,
$r_\delta(Y)\le C(h+\epsilon^{-1}+y)$ and
$V(r_\delta(Y))+S\le h+y$ after increasing $C_h$.
To justify this also for $\widehat W$, note its constant branch
$\bar t(\delta^{-1})$ is smaller than $h/4$ here. For the nonconstant
branch, $W_m\le\bar t\le t+1$ and
$t(C(h+\epsilon^{-1}+y))\le t(C'(h+\epsilon^{-1}))+t(1+y)+C$;
its first term plus the fixed $S_*$ and constants is at most $h/2$.
For $0\le y\le1$ use the same slack to get a bound by $h$;
for $y\ge1$ use $t(1+y)\le y+4$. Then
$e^{-y}(h+y)^{1/3}\le h^{1/3}$. The same argument applies to $X^X$.
At low heights use (E6). Consequently the two dynamic bounds (D1)
hold with $M=e^{16\delta}A\max\{t(Q),D_*\}^{1/3}$.
The starting depth $r_0(Q)$ is treated in exactly these two ranges:
high heights give $V(r_0)+S\le h$, and low heights give
$V(r_0)+S\le D_*$. Thus (E1) supplies (D2).

The newest floor is also covered: with
$\Xi=\lceil4C_{\rm deg}\delta^{-1}\lceil C_{\rm cut}\epsilon^{-2}\rceil\rceil$,
we have $r_\delta(\Xi)\le C\epsilon^{-12}$ and hence
$$
 (1+\delta)H(\Xi)^2\le e^{4\delta}A D_*^{1/3}.                \tag{E7}
$$
Older floors are covered by hypothesis. So is the original-seed floor.
The constant $C_0$ itself is covered by $A_0$. This proves the floor
part of (D1). The near-unit depth lemma gives (E2) for $j=1$.

Now suppose (E2) proved for a given $j$. Write
$A'=e^{16\delta+24\epsilon j}A$ and
$P_j(x)=\max\{t_j(x),D_*\}^{1/3}$. Define
$$
 r_\epsilon(x)=\max\{R_\delta,\lceil C_rt(x)\rceil+
                                        \lceil D_r/\epsilon\rceil\},
 \quad k_\epsilon(x)=\text{least odd integer at least }
       \max\{Q_\epsilon,\epsilon^{-1}\log(r_\epsilon(x)+1)\}.
$$
With universal large $D_r,C_r$, one has
$r_\epsilon(x)\ge r_0(k_\epsilon(x))$.
Indeed $R_\delta$ is included, the logarithmic part of $k_\epsilon$
has height at most $C\log(r_\epsilon+2)$, and the $Q_\epsilon$
part has height $O(\log(\epsilon^{-1}+2))$; both fit below
$r_\epsilon/2C_b$ after the fixed burn-in increase.
Apply the known profile at this order and depth and then static
transfer. The order factor, squared burn-in factor and squared
transfer factor cost at most $e^{3\epsilon}$ in total, and therefore
$$
 g_0(x):=\min\{G_*(x)^2,C_2t_2(x)^{1/3},H_l(x)^2,
                         e^{5\epsilon}A'P_j(k_\epsilon(x))\}
                                                               \tag{E8}
$$
is a valid nondecreasing squared coefficient majorant. The minimum
includes every retained $H_l$ and the newest $H$.

Set $M=A'P_{j+1}(Q)$. At high heights,
$k_\epsilon(X^X)\le h$, and for the cutoff
$k_\epsilon(Y)\le h$ when $y\le1$; when $y\ge1$,
$$
 k_\epsilon(Y)\le h/2+2+y/(\epsilon h)\le h+y\le h(1+y).
$$
These follow from $k_\epsilon(x)\le Q_\epsilon+3+
\epsilon^{-1}\log[C(R_\delta+t(x)+\epsilon^{-1})]$ and the
choice $h\ge C_hR_\delta\epsilon^{-5}$. The same logarithmic
bound at $y=0$ is at most $h/2$; its increment is at most
$y/(\epsilon h)$, with at most two for odd rounding.
The iterated-height product estimate used here follows directly
from the tower thresholds. For $x_1,x_2\ge1$ set
$n=\max\{t(x_1),t(x_2)\}\ge3$ and $E=E_{n-1}$.
Then $x_l\le E-2$, and both $x_1+x_2$ and $x_1x_2$ are at most
$e^E-2=E_n-2$; indeed $2(E-2)$ and $(E-2)^2$ are below that
quantity for $E\ge e^e$. Thus
$t(x_1+x_2),t(x_1x_2)\le n+1\le t(x_1)+t(x_2)$.
Apply the sum bound successively to the product bound to obtain
$t_j(x_1x_2)\le t_j(x_1)+t_j(x_2)$ for every $j\ge1$.
For $y\ge1$, the already proved $t(n)\le n$ on integers $n\ge3$
gives $t_j(1+y)\le t(1+y)\le y+4\le5y$.
Consequently $t_j(k_\epsilon(Y))\le t_j(h)+5y$, as required.
Since $\max\{t_j(h),D_*\}\ge5$, multiplication by $e^{-y}$
after taking cube roots removes this additive $5y$ exactly.
Thus (E8) proves both dynamic inequalities (D1) at high heights.
At low heights use the retained newest cap and (E6), whose cost
$e^{3\delta}A$ is smaller than $A'$. The floor proof (E7) is unchanged.

It remains to initialize the new depth induction; a coefficient bound
alone would not do this. At high heights apply the preceding stage
at order $k=k_\epsilon(x_0)$ with $x_0$ any argument of height $h$
and choose its logarithmic order using $r_0(Q)$ directly:
$k$ is the least odd integer at least
$\max\{Q_\epsilon,\epsilon^{-1}\log(r_0(Q)+1)\}$.
Then $k\le h$, $r_0(k)\le r_0(Q)$, and its order factor is at most
$e^\epsilon$. This supplies (D2) with the new $M$.
At low heights the original profile (E1) and (E3) supply it instead.
The near-unit depth lemma costs $e^{21\epsilon}$, covered by the
next $e^{24\epsilon}$. Finite induction on $j$ proves (E2).
:::

:::{prf:theorem} Target small-loss profile
:label: thm:sol-sz-v2-small-loss-target
There are universal $A_0,C,C_R,D\geq1$ such that for every
$0<\delta\leq1/16$, $m\geq0$, integer $r\geq R_\delta$, and centered
regular log-concave $\mu$ with covariance at most $I$ and curvature at least
$aI$, $a>0$,
$$
 \mathcal A(\mu)\leq A_0e^{C\delta m}
 [\widehat W_{m,\delta}(r)+S_m]^{1/3}\mathcal L_r(a^{-1})^2.
$$
This is the intended reconstruction of [](#prop:sz-v2-small-loss).
:::

:::{prf:proof} Initialization and analytic outer round
For $m=0$, the original inner profile together with the fixed-cost
height theorem gives $\mathcal A\le C[t(r)+1]^{1/3}\mathcal L_r^2$:
choose the least odd $Q\ge\log(r+1)$ in its $j=1$ profile.
Then $(r+1)^{1/Q}\le e$, $t(Q)\le t(r)$, and the starting depth
condition holds for all sufficiently large $r$. Increase $C_R,A_0$
once to cover the fixed initial threshold. This proves the initial
profile since $\widehat W_{0,\delta}\ge t$.

Assume the stage-$m$ profile. The outer-round lemma applies with
$V=\widehat W_{m,\delta}$ and $S=S_m$, which is uniformly bounded
by $1+8D/3$. Retain just its one cap $H$, so $N=1$ in the block
theorem. The original seed satisfies $G_*(x)^2=C_6^2t(x)^{1/3}$;
therefore its initial floor at $16K_\delta$ is at most
$C[t(\delta^{-1})+1]^{1/3}\le A_0D_*^{1/3}$ after fixing $A_0$.
The cap's newest floor is covered by (E7).
Choose $D$ to dominate the constant $b_*$ of the outer-round lemma.
There is no circular choice involving $S_*$: only the high-height
threshold $C_h$ depends on $S_*$; the additive allowances in (E3),(E5)
then grow at most logarithmically in $C_h$, so $D\ge C\log(e+D)$
suffices and has a universal solution. Alternatively fix the bound
$S_*\le1+8D/3$ and take this last scalar inequality as the explicit
final choice of $D$.
The result is, for all indicated $j,Q,r$,
$$
 \mathcal A\le e^{16\delta+24\epsilon j}A
 \max\{t_j(Q),\widehat W_{m,\delta}(\epsilon^{-1})+S_m+D4^{-m}\}^{1/3}
 (r+1)^{1/Q}\mathcal L_r(a^{-1})^2.
$$
Thus the outer-round estimate is supplied by the analytic proof, not
assumed as an additional premise.
:::

:::{prf:proof} Completion of the outer induction
Fix a permitted $r$ and let $j=\kappa(r)$, $\epsilon=\delta/(j+1)$.
Choose the least odd $Q$ at least
$\max\{Q_\epsilon,\delta^{-1}\log(r+1)\}$.
Since $\kappa(r)\leq t(r)$ and $t(r)\leq C r^{1/8}$,
$Q_\epsilon\leq C\delta^{-4}r^{1/2}$; hence $Q\leq r$ for
$r\geq C_R\delta^{-12}$ after a universal enlargement of $C_R$.
The elementary growth bound follows from $t(r)\leq C\log(r+2)$
and $\log(r+2)\leq C r^{1/8}$. The second term in $Q$ fits below $r/2$
by the same growth estimate. Furthermore
$C_bt(Q)+C_b'/\epsilon\leq C\delta^{-1}t(r)\leq r$.
Thus the analytic estimate just proved applies at this same $r$.

Monotonicity gives $t^{\circ j}(Q)\leq3<D_*$, while
$(r+1)^{1/Q}\leq e^\delta$ and $\epsilon j\leq\delta$.
Since $j+1\leq\chi(r)$, the product estimate above yields
$$
 \widehat W_{m,\delta}(\epsilon^{-1})
 \leq\widehat W_{m+1,\delta}(r)+D4^{-m},
$$
after fixing $D$ sufficiently large. Here $W_m\circ\bar\chi=W_{m+1}$,
$\bar\chi\geq\chi$, and $W_m(\delta^{-1})\leq\bar t(\delta^{-1})$.
The two additive allowances total $2D4^{-m}=S_{m+1}-S_m$.
Consequently the next amplitude is at most $e^{41\delta}A$, and
$C=42$ suffices. Together with the initialization and analytic outer round, finite induction
on $m$ proves the stated small-loss profile.
:::

**Fences respected.** No new `bounded_by` edges are proposed. The argument
does not discharge a CMH, occupation, or cut-relative premise. Uniform
admissibility is retained explicitly, and exponential coefficients are
not obtained by invoking the already proved target.
