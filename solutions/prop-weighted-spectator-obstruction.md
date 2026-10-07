---
title: 'The exponential-spectator obstruction'
label: sec:sol-weighted-spectator-obstruction
ledger-node: prop:weighted-spectator-obstruction
numbering:
  enumerator: D26.%s
---

*Part of the fixed-cut archive, Chapter [](#sec:open); the reading order is on the [full proofs](#sec:proofs-archive) page.*

**Overview.** This dossier proves [](#prop:weighted-spectator-obstruction) ([](#thm:sol-weighted-spectator-obstruction)). For all $C,T_0,\gamma,\eta,\delta$ there is a product of centered exponentials and a half-mass cylinder with arbitrarily small initial excess whose stopped excess, weighted by $(1+\norm{A_t}_\op)^{5/2}$, violates [](#eq:sol-spectator-violation). This refutes the literal global-operator-norm weighted gate of [](#conj:weighted-excess-rate) in both its additive and relative readings. It does not refute KLS, because every witness is a product ([](#prop:products)). The mechanism is a near-optimal base cylinder with a stable perimeter, plus many exponential spectators whose covariance spikes both collapse the profile and inflate the weight.

1. Regular exact-mass competitors and the exact density-change formula [](#eq:sol-spectator-density-change) for the exponential product ([](#lem:sol-spectator-regularization)).
2. [](#prop:products) and [](#lem:half) give a positive floor on the half-profiles ([](#eq:sol-spectator-profile-floor)). A base $E_0$ then gives a cylinder whose excess bounds hold uniformly in the spectator dimension $N$ ([](#eq:sol-spectator-additive), [](#eq:sol-spectator-relative)).
3. The posterior and $A_t$ factorize into base and spectator blocks ([](#eq:sol-spectator-factorization)). On a base event $G_b$ of probability at least $1/4$, the mass and the perimeter are stable up to $T_b$ ([](#eq:sol-spectator-base-stability)). This uses step 1.
4. At each fixed $t$, [](#prop:covariance-spike) with $s=1/t$ gives a spectator spike with positive probability ([](#eq:sol-spectator-fixed-time-positive)). Through [](#lem:one-dimensional-density-variance) the spike bounds the profile by $\sqrt{t/c_{\rm sp}}$ ([](#eq:sol-spectator-profile-competitor)) and the weight from below by $c_{\rm sp}^{5/2}t^{-5/2}$ ([](#eq:sol-spectator-weight-lower)).
5. Choose $T$, then $N$. Independence and Tonelli give the lower bound $\kappa_{\rm sp}P_0T^{-3/2}$ ([](#eq:sol-spectator-integrated-lower)), which exceeds $C(Te_0+T^{1+\gamma})$.

**Conventions.** Let $\lambda$ be the law of $Y-1$, where $Y$ is rate-one exponential. Thus $\lambda$ is centered, has variance one, and has density

$$
w_1(x)=e^{-(x+1)}\one_{\{x\ge-1\}}.
$$

All perimeters below use the outer Minkowski convention of the manuscript. For the regular sets selected below this agrees with relative weighted BV perimeter inside the convex support. For a localized measure $\mu_t$, a fixed cut $E$, and $p_t=\mu_t(E)$, write

$$
P_t(E)=\mu_t^+(E),\qquad
e_t(E)=P_t(E)-I_{\mu_t}(p_t),\qquad
\tau_\eta=\inf\{t:|p_t-\tfrac12|>\eta\}.
$$

:::{prf:theorem} Exponential-spectator obstruction; [](#prop:weighted-spectator-obstruction)
:label: thm:sol-weighted-spectator-obstruction
For every $C,T_0,\gamma>0$, every $\eta\in(0,1/2)$, and every $\delta>0$, there are an integer $d$, the isotropic log-concave product $\mu=\lambda^{\otimes d}$, a finite-perimeter cylinder $E\subset\R^d$ with $\mu(E)=1/2$ and

$$
e_0(E)\le\delta,
\qquad
\frac{e_0(E)}{I_\mu(1/2)}\le\delta,
$$

and a time $0<T\le T_0$ such that

```{math}
:label: eq:sol-spectator-violation
\E\int_0^{T\wedge\tau_\eta}
e_t(E)\bigl(1+\norm{A_t}_\op\bigr)^{5/2}\dd t
>C\bigl(Te_0(E)+T^{1+\gamma}\bigr).
```

The construction can additionally be made with $e_0(E)\le1$. Hence it refutes the current literal global-operator-norm weighted gate in [](#conj:weighted-excess-rate), including both the additive and relative approximate-minimizer readings. It does not refute KLS: every witness is a product measure and has a dimension-free KLS constant by [](#prop:products).
:::

We first isolate the regularization convention used to select the base cut. This also records why the later perimeter change-of-density formula is valid for the exact, noncompact one-sided-exponential law, rather than only for a compact surrogate.

:::{prf:lemma} Regular competitors and the Minkowski convention
:label: lem:sol-spectator-regularization
Let $\nu=\lambda^{\otimes m}$ and let $p\in(0,1)$. For every $\rho>0$ there is a relative weighted-BV set $S$ of mass $p$, regular in the interior of $K_m=[-1,\infty)^m$, such that

$$
\nu^+(S)\le I_\nu(p)+\rho.
$$

For this $S$, outer Minkowski perimeter equals relative weighted perimeter. For parameters $(u,t)$ such that $t\ge0$ and

$$
0<Z(u,t):=\int\exp(u\cdot x-t|x|^2/2)\dd\nu(x)<\infty,
$$

define

$$
\dd\nu_{u,t}=F_{u,t}\dd\nu,
\qquad
F_{u,t}(x)=\frac{\exp(u\cdot x-t|x|^2/2)}{Z(u,t)},
$$

Then

```{math}
:label: eq:sol-spectator-density-change
\nu_{u,t}^+(S)=\int F_{u,t}\,\dd\sigma_S,
```

where $\dd\sigma_S=e^{-\sum_{j=1}^m(x_j+1)} \dd\mathcal H^{m-1}|_{\partial^*S\cap\operatorname{int}K_m}$ is its relative weighted perimeter measure. No surface term on $\partial K_m$ occurs.
:::

:::{prf:proof}
Here are the approximation details needed later. On each compact subset of $\operatorname{int}K_m$, the density of $\nu$ is smooth and strictly positive. Start from a mass-$p$ competitor $S^{(0)}$ whose outer Minkowski content is within $\rho/4$ of $I_\nu(p)$. Finite outer Minkowski content implies finite relative BV perimeter, with BV perimeter no larger than that content. Restrict to $K_m\cap B_R$, mollify the indicator in interior and boundary charts, and use the coarea formula; then let $R\uparrow\infty$. The usual diagonal choice gives regular relative sets $S_k$ with

$$
\nu(S_k)\longrightarrow p,
\qquad
\operatorname{Per}_\nu(S_k)\longrightarrow
\operatorname{Per}_\nu(S^{(0)}).
$$

If necessary, a compactly supported smooth flow through a regular boundary patch in $\operatorname{int}K_m$ corrects the small mass error exactly. Its mass derivative is the strictly positive weighted area of that patch, while its perimeter varies continuously, so the correction costs $o(1)$ perimeter. This is the compact-smooth weighted-BV approximation layer; choose $k$ large and rename one exact-mass corrected regular approximant as $S$. It gives the displayed $\rho$ bound.

For a regular relative set, the one-sided tubular-neighborhood formula inside $K_m$ identifies outer Minkowski content with

$$
\int_{\partial^*S\cap\operatorname{int}K_m}
e^{-\sum_j(x_j+1)}\dd\mathcal H^{m-1}.
$$

Parts of the topological boundary lying on $\partial K_m$ are not interfaces inside the support and contribute neither to this formula nor to the ambient Minkowski derivative, since the measure vanishes outside $K_m$. Multiplying the volume density by the positive continuous factor $F_{u,t}$ leaves the relative reduced boundary unchanged and multiplies its weighted surface measure by $F_{u,t}$. Applying the same tubular-neighborhood formula proves [](#eq:sol-spectator-density-change). This direct weighted-BV identity is valid for the exact exponential product; no compact approximation of the probability law is taken in the argument below.
:::

:::{prf:proof} Proof of [](#thm:sol-weighted-spectator-obstruction)
*Step 1: choose a base before choosing either time or spectator dimension.* Set

$$
a_m:=I_{\lambda^{\otimes m}}(1/2),\qquad m\ge1.
$$

Cylinder extension makes this sequence nonincreasing. Indeed, if $S\subset\R^m$ has mass $1/2$, then

$$
\dist\bigl((x,z),S\times\R\bigr)=\dist(x,S),
\qquad
(S\times\R)_r=S_r\times\R,
$$

so $\lambda^{\otimes(m+1)}(S\times\R)=1/2$ and its outer Minkowski perimeter equals $\lambda^{\otimes m,+}(S)$. Taking the infimum gives $a_{m+1}\le a_m$.

On the other hand, [](#prop:products) gives a universal $h_*>0$ such that $h_{\lambda^{\otimes m}}\ge h_*$ for every $m$: every factor is isotropic and one-dimensional. [](#lem:half) therefore gives

```{math}
:label: eq:sol-spectator-profile-floor
a_m=\frac12h_{\lambda^{\otimes m}}\ge a_*:=\frac{h_*}{2}>0.
```

Consequently

$$
a_m\downarrow a_\infty\quad\hbox{with}\quad a_\infty\ge a_*>0.
$$

Choose $\varepsilon>0$ so small that

```{math}
:label: eq:sol-spectator-epsilon
2\varepsilon\le\min\{\delta,1,\delta a_*\}.
```

First choose $M$ with $a_M-a_\infty\le\varepsilon/2$. Then apply [](#lem:sol-spectator-regularization) with $p=1/2$ and $\rho=\varepsilon/2$ to choose a regular relative finite-perimeter set $E_0\subset\R^M$ satisfying

```{math}
:label: eq:sol-spectator-base
\lambda^{\otimes M}(E_0)=\frac12,
\qquad
P_0:=\lambda^{\otimes M,+}(E_0)\le a_M+\frac\varepsilon2.
```

By the definition of the profile and [](#eq:sol-spectator-profile-floor), $P_0\ge a_M\ge a_*>0$. For every integer $N\ge1$, put

$$
\mu^{M,N}=\lambda^{\otimes M}\otimes\lambda^{\otimes N},
\qquad
E^{M,N}=E_0\times\R^N.
$$

The distance identity above gives mass $1/2$ and perimeter $P_0$. Hence

```{math}
:label: eq:sol-spectator-additive
\begin{aligned}
0\le e_0(E^{M,N})
&=P_0-a_{M+N}
\le P_0-a_\infty\le\varepsilon,
\end{aligned}
```

```{math}
:label: eq:sol-spectator-relative
\begin{aligned}
\frac{e_0(E^{M,N})}{I_{\mu^{M,N}}(1/2)}
&\le\frac{\varepsilon}{a_*}.
\end{aligned}
```

In particular, [](#eq:sol-spectator-epsilon) makes both quantities at most $\delta$ and makes the additive excess at most $1$. Most importantly, these bounds are uniform in every spectator dimension $N$ chosen later.

*Step 2: product localization and the independent base event.* Use the planted Gaussian observation realization. Write

$$
X=(X^0,X^1,\ldots,X^N),
\qquad
c_t=tX+B_t,
$$

where $X^0\sim\lambda^{\otimes M}$, $X^i\sim\lambda$ for $i\ge1$, and all latent blocks and Brownian coordinate blocks are independent. Conditional on the observation path up to time $t$, its endpoint $c_t$ is sufficient and

$$
\dd\mu_t(x)=Z_t^{-1}
\exp\bigl(c_t\cdot x-t|x|^2/2\bigr)\dd\mu^{M,N}(x).
$$

Both the prior and the likelihood factorize, so, pathwise,

```{math}
:label: eq:sol-spectator-factorization
\mu_t=\nu_t^0\otimes\bigotimes_{i=1}^N\lambda_{i,t},
\qquad
A_t=\operatorname{diag}(A_t^0,v_{1,t},\ldots,v_{N,t}),
```

where $v_{i,t}=\Var(\lambda_{i,t})$. The entire base posterior process is independent of the spectator posterior processes. The cylinder and distance identities give, for every $t$,

```{math}
:label: eq:sol-spectator-cylinder-localized
p_t=\nu_t^0(E_0),
\qquad
P_t(E^{M,N})=(\nu_t^0)^+(E_0).
```

Thus $p_t$, $P_t(E^{M,N})$, and $\tau_\eta$ are base-block measurable.

We next construct a single base event on which mass and perimeter are stable for a short time. For deterministic $(u,t)$ let

$$
F_{u,t}(x)=
\frac{\exp(u\cdot x-t|x|^2/2)}
{\int\exp(u\cdot y-t|y|^2/2)\dd\lambda^{\otimes M}(y)}.
$$

The exponential product has a local exponential moment. Dominated convergence, applied uniformly as $(a,\bar T)\downarrow(0,0)$, therefore permits $a,\bar T>0$ such that

```{math}
:label: eq:sol-spectator-l1-stability
\int e^{a|x|}\dd\lambda^{\otimes M}(x)\le2,
\qquad
\sup_{|u|\le a,\ 0\le t\le\bar T}
\norm{F_{u,t}-1}_{L^1(\lambda^{\otimes M})}<\eta.
```

For completeness, the uniform domination is by $1+e^{a_0|x|}$ for a fixed sufficiently small local-moment radius $a_0$, while $\sup_{|u|\le a,\ 0\le t\le\bar T}|e^{u\cdot x-t|x|^2/2}-1|\to0$ pointwise.

Let $\sigma_0$ be the finite weighted perimeter measure of $E_0$. Choose $R<\infty$ so that

```{math}
:label: eq:sol-spectator-R
\sigma_0(B_R)\ge\frac{P_0}{2},
\qquad
aR+\frac{\bar T R^2}{2}\le\log2,
```

shrinking $a,\bar T$ again if required; the $L^1$ conclusion in [](#eq:sol-spectator-l1-stability) is preserved. Choose $L$ with $\Prob(|X^0|\le L)\ge1/2$, and take

```{math}
:label: eq:sol-spectator-Tb
T_b\le
\min\left\{\bar T,\frac{a}{2L},
\frac{a^2}{8M\log(8M)}\right\}.
```

Define the base-block event

```{math}
:label: eq:sol-spectator-Gb
G_b=\{|X^0|\le L\}\cap
\left\{
\max_{1\le j\le M}\sup_{0\le s\le T_b}|B_s^{0,j}|
\le\frac{a}{2\sqrt M}
\right\}.
```

The reflection principle and a union bound give

$$
\Prob\left(
\max_j\sup_{s\le T_b}|B_s^{0,j}|>\frac{a}{2\sqrt M}
\right)
\le4M\exp\left(-\frac{a^2}{8MT_b}\right)\le\frac12.
$$

Independence of $X^0$ and $B^0$ yields $\Prob(G_b)\ge1/4$. On $G_b$, $|c_s^0|=|sX^0+B_s^0|\le a$ for all $s\le T_b$. The second part of [](#eq:sol-spectator-l1-stability) then gives

$$
|\nu_s^0(E_0)-\tfrac12|<\eta.
$$

Moreover, for $x\in B_R$, the first part of [](#eq:sol-spectator-l1-stability) and [](#eq:sol-spectator-R) give

$$
F_{c_s^0,s}(x)
\ge
\frac{e^{-aR-T_bR^2/2}}
{\int e^{a|y|}\dd\lambda^{\otimes M}(y)}
\ge\frac14.
$$

The exact density-change formula [](#eq:sol-spectator-density-change) therefore yields, simultaneously for every $0\le s\le T_b$,

```{math}
:label: eq:sol-spectator-base-stability
\tau_\eta>T_b,
\qquad
P_s(E^{M,N})=(\nu_s^0)^+(E_0)
\ge\frac14\sigma_0(B_R)\ge\frac{P_0}{8}
\quad\hbox{on }G_b.
```

Neither $G_b$ nor $T_b$ depends on the later choice of $N$.

*Step 3: a fixed-time spectator spike and an exact-mass profile competitor.* The imported covariance-spike proposition, in its event form, says that for $N$ independent centered rate-one exponentials and Gaussian-channel noise variance $s$,

```{math}
:label: eq:sol-spectator-KL-channel
\Prob\left(
\norm{\Cov(X\mid X+\sqrt sG)}_\op\ge c_{\rm sp}s
\right)
\ge1-\left(1-\frac12e^{-s}\right)^N
```

for a universal $c_{\rm sp}>0$; this is the event computed in [@KLnotes, Prop. 65]. The localization observation satisfies

$$
\frac{c_t}{t}=X+\frac{B_t}{t}
\stackrel{d}=X+t^{-1/2}G.
$$

Thus the conversion is exactly $s=1/t$, and not $s=t$ or $s=t^{-1/2}$. In the spectator block, put

$$
H_t=\left\{\max_{1\le i\le N}v_{i,t}\ge\frac{c_{\rm sp}}t\right\}.
$$

Equation [](#eq:sol-spectator-KL-channel) gives, at each deterministic $t>0$,

```{math}
:label: eq:sol-spectator-fixed-time
\Prob(H_t)\ge1-\left(1-\frac12e^{-1/t}\right)^N.
```

If $\log N\ge2/T$, then, separately for every deterministic $t\in[T/2,T]$,

```{math}
:label: eq:sol-spectator-fixed-time-positive
\Prob(H_t)\ge h_{\rm sp}:=1-e^{-1/2}>0.
```

This is only a fixed-time assertion; no common spike event on the interval is claimed.

On $H_t$, take the least $i$ with $v_{i,t}\ge c_{\rm sp}/t$. Since the one-dimensional posterior $\lambda_{i,t}$ is log-concave and has a continuous positive density $f_{i,t}$ in the interior of its support, it has a quantile $q_{i,t}$ satisfying $\lambda_{i,t}(( -\infty,q_{i,t}])=p_t$. The product cylinder cut in this one spectator coordinate has $\mu_t$-mass exactly $p_t$ and outer Minkowski perimeter $f_{i,t}(q_{i,t})$. The imported sharp density–variance bound [@BobkovChistyakov2015Concentration, Prop. 2.1], in the ledger form of [](#lem:one-dimensional-density-variance), gives

```{math}
:label: eq:sol-spectator-profile-competitor
I_{\mu_t}(p_t)\le f_{i,t}(q_{i,t})
\le\norm{f_{i,t}}_\infty
\le v_{i,t}^{-1/2}
\le\sqrt{\frac{t}{c_{\rm sp}}}.
```

This is a pointwise upper bound on the profile at the actual random mass $p_t$. It inserts no lower bound on a localized profile.

*Step 4: choose $T$, then $N$, and integrate fixed-time events by Tonelli.* With the base, $P_0$, and $T_b$ already fixed, choose $T>0$ so small that

```{math}
:label: eq:sol-spectator-T-first
T\le\min\left\{T_0,T_b,\frac{c_{\rm sp}P_0^2}{256},1\right\}.
```

At this same choice, also require

```{math}
:label: eq:sol-spectator-final-T
T^{5/2}<\frac{\kappa_{\rm sp}}{2C},
\qquad
T^{\gamma+5/2}<\frac{\kappa_{\rm sp}P_0}{2C},
```

where

$$
\kappa_{\rm sp}
:=\frac{h_{\rm sp}c_{\rm sp}^{5/2}}{96}
(2^{3/2}-1)>0.
$$

Such a positive $T$ exists because every quantity on the right is already fixed. Only now choose a finite integer $N$ with $\log N\ge2/T$. For every deterministic $t\in[T/2,T]$, on $G_b\cap H_t$, equations [](#eq:sol-spectator-base-stability) and [](#eq:sol-spectator-profile-competitor) imply

```{math}
:label: eq:sol-spectator-excess-lower
t<\tau_\eta,
\qquad
e_t(E^{M,N})\ge\frac{P_0}{8}-\sqrt{\frac{t}{c_{\rm sp}}}
\ge\frac{P_0}{16}.
```

The block-diagonal covariance in [](#eq:sol-spectator-factorization) also gives

```{math}
:label: eq:sol-spectator-weight-lower
\bigl(1+\norm{A_t}_\op\bigr)^{5/2}
\ge c_{\rm sp}^{5/2}t^{-5/2}.
```

For each such deterministic $t$, $G_b$ is independent of $H_t$, because they depend on disjoint latent and Brownian blocks. Therefore

$$
\Prob(G_b\cap H_t)\ge\frac{h_{\rm sp}}4.
$$

The integrand is nonnegative, so Tonelli applied to these marginal-in-time events gives

```{math}
:label: eq:sol-spectator-integrated-lower
\begin{aligned}
&\E\int_0^{T\wedge\tau_\eta}
e_t(E^{M,N})\bigl(1+\norm{A_t}_\op\bigr)^{5/2}\dd t
\\
&\quad\ge
\frac{P_0h_{\rm sp}c_{\rm sp}^{5/2}}{64}
\int_{T/2}^Tt^{-5/2}\dd t
=\kappa_{\rm sp}P_0T^{-3/2},
\end{aligned}
```

No persistent spike and no interchange beyond nonnegative Tonelli is used.

Since $e_0(E^{M,N})\le P_0$, the conditions imposed before the single final choice of $N$ give

$$
C\bigl(Te_0(E^{M,N})+T^{1+\gamma}\bigr)
\le C\bigl(TP_0+T^{1+\gamma}\bigr)
<\kappa_{\rm sp}P_0T^{-3/2}.
$$

Together with [](#eq:sol-spectator-integrated-lower), this is [](#eq:sol-spectator-violation). The quantifier order was

$$
(C,T_0,\gamma,\eta,\delta)
\longrightarrow(\varepsilon,M,E_0,P_0,T_b)
\longrightarrow T
\longrightarrow N,
$$

and the near-minimality estimates [](#eq:sol-spectator-additive)– [](#eq:sol-spectator-relative) were uniform in that final $N$. This completes the proof.
:::

**Dependency and fence audit.** The proof uses exactly the four ledger dependencies in the header. [](#prop:products) and [](#lem:half) keep the monotone half-profile limit positive; [](#prop:covariance-spike) supplies only the fixed-time event [](#eq:sol-spectator-fixed-time); and [](#lem:one-dimensional-density-variance) supplies the explicit quantile-halfline competitor. The node has no `bounded_by` fence. The neighbouring fences are nevertheless respected: the proof retains the $5/2$ weight demanded by the two-tail calibration and evades the circularity warning by upper-bounding the random posterior profile with an explicit set. It asserts no implication about the trace-upgrade cluster.

**Hypotheses and closure.** All four dependencies are proved or published imports in the current ledger, so the result is unconditional relative to the repository's accepted analytic inputs. Besides them, the proof uses only standard deterministic weighted-BV approximation and density change, elementary local exponential integrability of a finite exponential product, the planted Gaussian posterior, the Brownian reflection principle, and Tonelli's theorem. There is no numerical input. There is no unclosed analytic step in this dossier; `checked_by: none` records that a distinct cold reviewer has not yet audited it.

**What is and is not refuted.** The construction refutes only the literal all-product, global-$\norm{A_t}_\op$ rate stated in [](#conj:weighted-excess-rate). A replacement with an explicit near-worst-measure condition, or a cut-local tensor-stable covariance weight, is a different statement. Since the witnesses themselves satisfy dimension-free KLS, no counterexample to the KLS conjecture is claimed.
