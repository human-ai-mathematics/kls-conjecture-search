---
title: 'Solution: the localization, Riccati, and tight-window core'
label: sec:sol-kls-localization-riccati-core
ledger-node:
- lem:matrix-riccati
- thm:scalar-riccati
- cor:per-direction
- cor:tight-window-consumption
- lem:pathwise-BL
- cor:away-from-zero
numbering:
  enumerator: D6.%s
---

**Overview.** This dossier proves [](#lem:matrix-riccati), [](#thm:scalar-riccati), [](#cor:per-direction), [](#cor:tight-window-consumption), [](#lem:pathwise-BL) and [](#cor:away-from-zero). Under Eldan localization of a two-color cut, it derives exact Itô equations for the between-color covariance $B_t$, the within-color covariance $R_t$ and the separation $r_t=\Tr B_t$. A tight-window Carleson bound on the source $S_t$ then keeps the cut balanced. The boundary conclusion uses the separate canonical bridge [](#lem:survival-implies-kls).

1. [](#lem:sol-matrix-riccati): Itô calculus on $v_t=s_t\delta_t$ and $s_t$ gives [](#eq:sol-dB), and subtraction from the covariance SDE gives [](#eq:sol-dR).
2. [](#thm:sol-scalar-riccati): the trace of [](#eq:sol-dB) gives drift $S_t-D_t$, with $D_t\ge r_t^2$.
3. [](#cor:sol-per-direction): the drift of [](#eq:sol-dR) is nonpositive, so stopping and Fatou bound the directional dissipation by $\theta^TR_0\theta\le1$.
4. [](#cor:sol-tight-window-consumption): Step 3 supplies a finite source budget before the Carleson hypothesis [](#eq:sol-tight-carleson) is applied. Step 2 and Gronwall then bound $\E r$ in [](#eq:sol-u-bound). The maximal inequality with [](#eq:sol-p-qv) gives survival, and [](#lem:survival-implies-kls) supplies the boundary conclusion.
5. [](#lem:sol-pathwise-BL): the identity [](#eq:sol-color-quadratic) and Brascamp–Lieb give $s_t\norm{K_t}_\HS^2\le4/t^2$.
6. [](#cor:sol-away-from-zero): Step 5 and $r^2\le D$ give $S_t\le8/t^2+\tfrac12D_t$ in a tight window.

**Scope and regularity.** This dossier proves the six results listed in the header on the exact original posterior, with the original measurable cut. A full-dimensional log-concave probability has an exponential moment in a neighborhood of the origin. Since $c_t\to0$ as $t\downarrow0$, its posterior polynomial moments are continuous near zero by an exponential majorant. On each compact positive-time interval, bounded $c_t$ and the Gaussian factor give a common majorant for every polynomial moment. The positive normalizing factor is continuous, as are the moments restricted to the fixed cut. Finite-time posterior equivalence preserves $p_t,q_t>0$ when $p_0\in(0,1)$.

Consequently, localizing the time, posterior moments, reciprocals of $p_t,q_t$, and martingale quadratic variations gives increasing stopping times tending almost surely to infinity. All Itô calculations below hold before these stops, where the stochastic integrals are true martingales. No spatial derivative of the cut indicator occurs: it is a bounded multiplier of polynomial tests, so no smoothing of a rough cut is needed. Removal of stops uses the specific nonnegative budgets proved below, not a general approximation assertion about perimeters. The Brascamp–Lieb form inequality is applied directly to the uniformly log-concave positive-time posterior and its polynomial tests.

## 1\. Setup and elementary decompositions

Let $\mu$ be isotropic and log-concave on $\R^n$. Eldan localization is the posterior process

$$
\dd\mu_t(x)=Z_t^{-1}\exp\!\left(c_t\cdot x-\frac t2\abs{x}^2\right)\dd\mu(x),
$$

adapted to an $n$-dimensional Brownian motion $W$. Write

$$
a_t=\E_{\mu_t}X,\qquad A_t=\Cov_{\mu_t}(X).
$$

For every integrable test function $\phi$, after localization when necessary,

```{math}
:label: eq:sol-loc-martingale
\dd\!\int\phi\,\dd\mu_t=\Cov_{\mu_t}(\phi,X)\cdot\dd W_t,
\qquad
\dd a_t=A_t\dd W_t,
\qquad
\dd A_t=\dd\mathcal T_t-A_t^2\dd t,
```

where $\mathcal T$ is a matrix local martingale. For $t>0$, the posterior is $t$-uniformly log-concave, hence Brascamp–Lieb gives

```{math}
:label: eq:sol-BL-cap
A_t\preceq t^{-1}I_n.
```

Fix a measurable cut $E$, put $F=E^c$, and, as long as $p_t,q_t>0$, define

$$
p_t=\mu_t(E),\quad q_t=1-p_t,\quad s_t=p_tq_t,
$$

$$
m_t^E=\E_{\mu_t}[X\mid E],\quad m_t^F=\E_{\mu_t}[X\mid F],\quad
\delta_t=m_t^E-m_t^F,
$$

$$
\Sigma_t^E=\Cov_{\mu_t}(X\mid E),\quad
\Sigma_t^F=\Cov_{\mu_t}(X\mid F),\quad G_t=\Sigma_t^E-\Sigma_t^F.
$$

Finite-time posteriors have a strictly positive likelihood relative to $\mu$, so an initial $p_0\in(0,1)$ keeps $p_t,q_t>0$ at every finite time. Covariance decomposition gives

```{math}
:label: eq:sol-cov-decomp
A_t=p_t\Sigma_t^E+q_t\Sigma_t^F+s_t\delta_t\delta_t^T.
```

Set

$$
B_t=s_t\delta_t\delta_t^T,
\quad R_t=A_t-B_t=p_t\Sigma_t^E+q_t\Sigma_t^F\succeq0,
\quad r_t=\Tr B_t=s_t\abs{\delta_t}^2,
$$

$$
K_t=G_t+(q_t-p_t)\delta_t\delta_t^T,
\quad S_t=s_t\norm{G_t}_{\HS}^2,
\quad D_t=2s_t\delta_t^TA_t\delta_t-r_t^2.
$$

In particular $0\preceq B_t\preceq A_t$, $B_t^2=r_tB_t$, and at time zero $R_0\preceq A_0=I_n$.

Finally let

$$
v_t=\int_E(x-a_t)\dd\mu_t(x)=s_t\delta_t.
$$

Then

```{math}
:label: eq:sol-p-qv
\dd p_t=v_t\cdot\dd W_t,
\qquad \dd[p]_t=\abs{v_t}^2\dd t=s_t^2\abs{\delta_t}^2\dd t.
```

## 2\. The separate survival bridge

The boundary and KLS implication used here is the canonical [](#lem:survival-implies-kls), proved in the active [standalone survival dossier](lem-survival-implies-kls.md). That proof treats the lower outer Minkowski content of actual measurable sets using neighborhood increments and conditional expectation. It does not identify general outer Minkowski content with a reduced-boundary integral. The former internal survival argument is superseded; survival is not one of this dossier's six claims.

In Section 4 we apply this bridge to the original posterior at the deterministic positive time $T_*$, with $b_0=1/3$ and $c_0=1/2$. The bridge assumes no Riccati or source-occupation estimate.

## 3\. The matrix and scalar Riccati identities

:::{prf:lemma} = [](#lem:matrix-riccati)
:label: lem:sol-matrix-riccati
There are matrix local martingales $N,\widetilde N$ such that

```{math}
:label: eq:sol-dB
\begin{aligned}
\dd B_t&=\dd N_t+
\bigl(s_tG_t^2-A_tB_t-B_tA_t+r_tB_t\bigr)\dd t,
\end{aligned}
```

```{math}
:label: eq:sol-dR
\begin{aligned}
\dd R_t&=\dd\widetilde N_t-
\bigl(R_t^2+s_tG_t^2\bigr)\dd t.
\end{aligned}
```
:::

:::{prf:proof}
Suppress the time subscript. Define the unnormalised conditional second moment

$$
C^E=\int_E(x-a)(x-a)^T\dd\mu_t(x).
$$

Applying [](#eq:sol-loc-martingale) to $\int_E x\dd\mu_t$ and using Itô's product rule for $pa$ gives

```{math}
:label: eq:sol-dv
\dd v=(C^E-pA)\dd W-Av\dd t.
```

Indeed, the quadratic covariation of $p$ and $a$ is $Av\dd t$. From [](#eq:sol-cov-decomp), $m^E-a=q\delta$, and $m^F-a=-p\delta$, one obtains

$$
C^E-pA=s\bigl(G+(q-p)\delta\delta^T\bigr)=sK.
$$

Thus $\dd v=sK\dd W-Av\dd t$. Since $s=p(1-p)$ and $\dd p=v\cdot\dd W$,

```{math}
:label: eq:sol-ds
\dd s=(q-p)v\cdot\dd W-\abs v^2\dd t.
```

For completeness, we retain every Itô correction in $B=vv^T/s$. Put $\alpha=q-p$. The drift of $vv^T$ is

$$
-Avv^T-vv^TA+s^2K^2,
$$

while

$$
\dd(s^{-1})=-\alpha s^{-2}v\cdot\dd W
+\left(\frac{\abs v^2}{s^2}+\frac{\alpha^2\abs v^2}{s^3}\right)\dd t.
$$

The cross-variation between the martingale parts of $vv^T$ and $s^{-1}$ contributes $-\alpha(KB+BK)\dd t$. Consequently the drift of $B$ is

```{math}
:label: eq:sol-dB-before-cancel
sK^2-(AB+BA)+rB+\alpha^2\frac r sB-\alpha(KB+BK).
```

Now $K=G+\alpha B/s$ and $B^2=rB$. In [](#eq:sol-dB-before-cancel), the terms linear in $\alpha$ cancel and the three quadratic terms have coefficients $1+1-2=0$. This leaves the drift in [](#eq:sol-dB).

Finally subtract [](#eq:sol-dB) from the covariance SDE in [](#eq:sol-loc-martingale). Since

$$
-A^2+AB+BA-rB=-(A-B)^2=-R^2,
$$

we obtain [](#eq:sol-dR). The calculation is first made before a bounded stopping time; letting the stopping levels increase proves the local semimartingale identities.
:::

:::{prf:theorem} = [](#thm:scalar-riccati)
:label: thm:sol-scalar-riccati
There is a scalar local martingale $M$ such that

$$
\dd r_t=\dd M_t+(S_t-D_t)\dd t.
$$

Moreover $D_t\ge r_t^2$, so $S_t$ is the only positive drift term.
:::

:::{prf:proof}
Take the trace in [](#eq:sol-dB). Since $\Tr(AB)=s\delta^TA\delta$, $\Tr(rB)=r^2$, and $\Tr(G^2)=\norm G_\HS^2$, its drift is

$$
s\norm G_\HS^2-2s\delta^TA\delta+r^2=S-D.
$$

For coercivity, $B\preceq A$ implies

$$
s\abs\delta^4=\delta^TB\delta\le\delta^TA\delta.
$$

Multiplying by $2s$ gives $2s\delta^TA\delta\ge2s^2\abs\delta^4=2r^2$, hence $D\ge r^2$.
:::

:::{prf:corollary} = [](#cor:per-direction)
:label: cor:sol-per-direction
For every $T>0$ and every unit vector $\theta$,

$$
\E\int_0^T\bigl(s_t\abs{G_t\theta}^2+\abs{R_t\theta}^2\bigr)\dd t
\le\theta^TR_0\theta\le1.
$$

Consequently

$$
\E\int_0^\infty s_tG_t^2\dd t\preceq R_0\preceq I_n.
$$
:::

:::{prf:proof}
Apply [](#eq:sol-dR) to $\theta^TR_t\theta$. Up to a scalar local martingale its drift is

$$
-\theta^TR_t^2\theta-s_t\theta^TG_t^2\theta
=-\abs{R_t\theta}^2-s_t\abs{G_t\theta}^2.
$$

Stop when the martingale and coefficients are bounded, take expectations, and use $R_{T\wedge\sigma}\succeq0$. Fatou's lemma as $\sigma\uparrow\infty$ yields the displayed finite-$T$ inequality. Monotone convergence first in $T$ and then testing every deterministic $\theta$ gives the Loewner inequality on $[0,\infty)$. Finally $R_0=A_0-B_0\preceq A_0=I_n$.
:::

## 4\. Tight-window consumption

For $0<\eta\le1/6$ define the continuous-exit time

$$
\tau_\eta=\inf\{t\ge0:\abs{p_t-1/2}>\eta\}.
$$

:::{prf:corollary} = [](#cor:tight-window-consumption)
:label: cor:sol-tight-window-consumption
Suppose $\abs{p_0-1/2}\le\eta/2$ and, for nonnegative constants $C_0,C_1$, a number $\alpha<1$, and every $T\le T_0$,

```{math}
:label: eq:sol-tight-carleson
\E\int_0^{T\wedge\tau_\eta}S_t\dd t
\le C_0T+C_1\E\int_0^{T\wedge\tau_\eta}r_t\dd t
+\alpha\E\int_0^{T\wedge\tau_\eta}D_t\dd t.
```

Then there is a time $T_*>0$, depending only on $T_0,C_0,C_1,\alpha,\eta$, for which

$$
\Prob\{\min(p_{T_*},q_{T_*})\ge1/3\}\ge1/2.
$$

Hence [](#lem:survival-implies-kls) gives a boundary lower bound whose constant has the same dependence. In particular, universal input constants give a universal bound.
:::

:::{prf:proof}
Let $u(T)=\E r_{T\wedge\tau_\eta}$. First sum [](#cor:per-direction) over a fixed orthonormal basis $(e_i)_{i=1}^n$. Since $\sum_i|G_te_i|^2=\norm{G_t}_\HS^2$, this gives, without using the Carleson premise,

$$
\E\int_0^T S_t\dd t\le\Tr R_0\le n.
$$

Choose increasing auxiliary localizing times $\sigma_k\uparrow\infty$ for the scalar identity. Its stopped expectation reads

$$
\E r_{T\wedge\tau_\eta\wedge\sigma_k}
+\E\int_0^{T\wedge\tau_\eta\wedge\sigma_k}D_t\dd t
=r_0+\E\int_0^{T\wedge\tau_\eta\wedge\sigma_k}S_t\dd t.
$$

The source on the right has the integrable bound just proved and converges by monotone convergence. Fatou for the nonnegative terminal and dissipation terms on the left yields

$$
u(T)+\E\int_0^{T\wedge\tau_\eta}D_t\dd t
\le r_0+\E\int_0^{T\wedge\tau_\eta}S_t\dd t\le1+n.
$$

Here $r_0\le1$ because $B_0$ has rank at most one and $B_0\preceq I_n$. In particular $u$ is finite and locally integrable, and Tonelli gives
$\E\int_0^{T\wedge\tau_\eta}r_t\dd t\le\int_0^Tu(t)\dd t<\infty$.
All terms are therefore finite before absorption. Only now apply [](#eq:sol-tight-carleson), on its original deterministic prefix, without an auxiliary stop. Subtracting $\alpha\E\int D_t\dd t$ and discarding the nonnegative remainder with coefficient $1-\alpha>0$ gives

$$
u(T)\le1+C_0T+C_1\E\int_0^{T\wedge\tau_\eta}r_t\dd t
\le1+C_0T+C_1\int_0^T u(t)\dd t.
$$

The last inequality uses $\one_{\{t<\tau_\eta\}}r_t\le r_{t\wedge\tau_\eta}$ pointwise. Gronwall therefore yields

```{math}
:label: eq:sol-u-bound
u(T)\le(1+C_0T)e^{C_1T}\le C_*\qquad(0\le T\le T_0),
```

where $C_*$ depends only on the displayed input constants. Before exit, $s_t\ge1/4-\eta^2\ge2/9$, and so

```{math}
:label: eq:sol-centroid-window
\E\int_0^{T\wedge\tau_\eta}\abs{\delta_t}^2\dd t
\le\frac92\int_0^T\E[\one_{\{t<\tau_\eta\}}r_t]\dd t
\le\frac92C_*T.
```

Continuity of $p$ and the nested initial window imply that on $\{\tau_\eta\le T\}$, $\sup_{t\le T\wedge\tau_\eta}\abs{p_t-p_0}\ge\eta/2$. Doob's $L^2$ inequality and [](#eq:sol-p-qv) give

$$
\Prob(\tau_\eta\le T)
\le\frac4{\eta^2}\E[p]_{T\wedge\tau_\eta}
=\frac4{\eta^2}\E\int_0^{T\wedge\tau_\eta}s_t^2\abs{\delta_t}^2\dd t
\le\frac{9C_*T}{8\eta^2},
$$

because $s_t\le1/4$. Choose $T_*\le T_0$ positive so that the last expression is at most $1/2$. On $\{\tau_\eta>T_*\}$, $\min(p_{T_*},q_{T_*})\ge1/2-\eta\ge1/3$, proving the claim.
:::

## 5\. Pathwise control away from zero

:::{prf:lemma} = [](#lem:pathwise-BL)
:label: lem:sol-pathwise-BL
For every $t>0$,

$$
s_t\norm{K_t}_\HS^2\le\frac{4\lmax(A_t)}t\le\frac4{t^2}.
$$
:::

:::{prf:proof}
For a symmetric matrix $M$ let

$$
f_M(x)=(x-a_t)^TM(x-a_t)-\Tr(MA_t),
\qquad g=\frac{\one_E-p_t}{\sqrt{s_t}}.
$$

The conditional covariance decomposition gives the exact identity

```{math}
:label: eq:sol-color-quadratic
\E_{\mu_t}[g f_M]=\sqrt{s_t}\,\inner{K_t}{M}.
```

Since $\E g=0$ and $\E g^2=1$, Cauchy–Schwarz and the Brascamp–Lieb inequality for the $t$-uniformly log-concave law $\mu_t$ give

$$
s_t\inner{K_t}{M}^2
\le\Var_{\mu_t}(f_M)
\le\frac1t\E_{\mu_t}\abs{\nabla f_M}^2
=\frac4t\Tr(MA_tM)
\le\frac{4\lmax(A_t)}t\norm M_\HS^2.
$$

The posterior's Gaussian factor gives all polynomial moments for $t>0$, so the quadratic $f_M$ belongs to the Brascamp–Lieb form domain; equivalently one may apply the inequality to smooth truncations and pass by form closure. If $K_t\ne0$, take $M=K_t/\norm{K_t}_\HS$; otherwise the assertion is immediate. The second inequality follows from [](#eq:sol-BL-cap).
:::

:::{prf:corollary} = [](#cor:away-from-zero)
:label: cor:sol-away-from-zero
There is a numerical $\eta_0>0$ such that, for $0<\eta\le\eta_0$ and on $\{t<\tau_\eta\}$,

$$
S_t\le\frac8{t^2}+\frac12D_t.
$$

Thus, for every interval $I\subset[t_0,T_0]$ with $t_0>0$,

$$
\E\int_{I\cap[0,\tau_\eta]}S_t\dd t
\le\frac8{t_0^2}\abs I+\frac12
\E\int_{I\cap[0,\tau_\eta]}D_t\dd t.
$$
:::

:::{prf:proof}
On the tight window, $\abs{q-p}\le2\eta$. For $\eta\le1/4$ we also have $s\ge3/16$. Since $G=K-(q-p)\delta\delta^T$,

$$
S=s\norm G_\HS^2
\le2s\norm K_\HS^2+2s(q-p)^2\abs\delta^4
=2s\norm K_\HS^2+\frac{2(q-p)^2}{s}r^2.
$$

The first term is at most $8/t^2$ by [](#lem:sol-pathwise-BL); the second is at most $(128/3)\eta^2D$ because $r^2\le D$. Taking, for example, $\eta_0=\min\{1/4,\sqrt3/16\}$ makes this coefficient at most $1/2$. Integration on an interval bounded away from zero gives the final display.
:::

**Endpoint audit.** Every expectation of a stochastic identity above is taken first at a bounded localizing stopping time. Finite-horizon estimates survive its removal by Fatou and the nonnegativity of $R,S,D$ in the places used. The only infinite-horizon assertion is obtained from the already proved finite-horizon occupation inequality by monotone convergence. For tight-window absorption, the per-direction source budget first gives finite terminal and integrated dissipation bounds. The boundary conclusion uses the separate canonical survival bridge, valid without compact support. Thus no claim depends on silently declaring a local martingale to be uniformly integrable at time $\infty$.
