---
title: 'The spectator obstruction to a superlinear excess remainder'
label: sec:sol-spectator-excess-rate-obstruction
ledger-node: prop:spectator-excess-rate-obstruction
numbering:
  enumerator: D23.%s
---

*Part of the fixed-cut archive, Chapter [](#sec:open); the reading order is on the [full proofs](#sec:proofs-archive) page.*

**Overview.** This dossier proves [](#prop:spectator-excess-rate-obstruction) ([](#thm:sol-spectator-excess-rate-obstruction)). For all $C,T_0,\gamma,\eta,\delta$ there is a product of centered exponentials $\mu=\lambda^{\otimes d}$ and a half-mass cylinder $E$ with arbitrarily small initial excess such that the stopped excess integral violates the superlinear rate [](#eq:sol-spectator-rate-violation). The idea is to fix a nearly optimal base cylinder first and then add many independent spectator coordinates. In each spectator the covariance spike collapses the localized profile, while the tracked perimeter of the base cylinder stays of order one. The witnesses are products, so they satisfy KLS by [](#prop:products), and KLS is not refuted.

1. Regular exact-mass competitors for the exponential product, with a density-change formula for the perimeter under tilts ([](#lem:sol-spectator-rate-regularization)).
2. Base selection: [](#prop:products) and [](#lem:half) give a positive floor on the half-profiles ([](#eq:sol-spectator-rate-profile-floor)). A near-optimal base $E_0$ then gives an excess below $\varepsilon$ that does not depend on the spectator dimension ([](#eq:sol-spectator-rate-additive)).
3. The posterior factorizes into base and spectator blocks ([](#eq:sol-spectator-rate-factorization)). On a base event $G_b$ of probability at least $1/4$, the mass stays in the window and the tracked perimeter stays at least $P_0/8$ up to time $T_b$ ([](#eq:sol-spectator-rate-base-stability)). This uses step 1.
4. At each fixed time, [](#prop:covariance-spike) gives a spectator spike with probability $h_{\rm sp}$. [](#lem:one-dimensional-density-variance) then turns it into a quantile halfline competitor that bounds the profile by $\sqrt{t/c_{\rm sp}}$ ([](#eq:sol-spectator-rate-profile-competitor)).
5. Choose $T$, then $N$. By independence of the base and spectator events and by Tonelli, the stopped integral is at least $\kappa_{\rm sp}P_0T$ ([](#eq:sol-spectator-rate-integrated-lower)), which beats $C(Te_0+T^{1+\gamma})$.

**Conventions.** Let $\lambda$ be the law of $Y-1$, where $Y$ has the rate-one exponential law. Thus $\lambda$ is centered, log-concave, and has variance one, with density

$$
w_1(x)=e^{-(x+1)}\one_{\{x\ge-1\}}.
$$

All perimeters use the lower outer Minkowski convention of the manuscript. For the regular sets selected below, this agrees with relative weighted BV perimeter inside the convex support. For a localized law $\mu_t$, a fixed cut $E$, and $p_t=\mu_t(E)$, write

$$
P_t(E)=\mu_t^+(E),\qquad
e_t(E)=P_t(E)-I_{\mu_t}(p_t),\qquad
\tau_\eta=\inf\{t:|p_t-\tfrac12|>\eta\}.
$$

:::{prf:theorem} Spectator obstruction to a superlinear excess remainder; [](#prop:spectator-excess-rate-obstruction)
:label: thm:sol-spectator-excess-rate-obstruction
For every $C,T_0,\gamma>0$, every $\eta\in(0,1/2)$, and every $\delta>0$, there are an integer $d$, the isotropic log-concave product $\mu=\lambda^{\otimes d}$, a finite-perimeter cylinder $E\subset\R^d$ with $\mu(E)=1/2$ and

$$
e_0(E)\le\delta,
\qquad
\frac{e_0(E)}{I_\mu(1/2)}\le\delta,
$$

and a time $0<T\le T_0$ such that

```{math}
:label: eq:sol-spectator-rate-violation
\E\int_0^{T\wedge\tau_\eta}e_t(E)\dd t
>C\bigl(Te_0(E)+T^{1+\gamma}\bigr).
```

The construction can additionally be made with $e_0(E)\le1$. Thus even the unweighted excess has no uniform remainder of the displayed source-vanishing superlinear form. In particular, within the usual normalized class of replacement weights $W_t\ge1$, changing only the global covariance weight cannot repair that rate. This does not refute KLS: every witness is a product measure and has a dimension-free KLS constant by [](#prop:products).
:::

We first record the regular selection and change-of-density statement needed for the exact noncompact one-sided-exponential product.

:::{prf:lemma} Regular competitors for the exponential product
:label: lem:sol-spectator-rate-regularization
Let $\nu=\lambda^{\otimes m}$ and let $p\in(0,1)$. For every $\rho>0$ there is a relative weighted-BV set $S$, regular in the interior of $K_m=[-1,\infty)^m$, such that

$$
\nu(S)=p,
\qquad
\nu^+(S)\le I_\nu(p)+\rho.
$$

For this $S$, lower outer Minkowski perimeter equals relative weighted perimeter. Whenever $t\ge0$ and

$$
0<Z(u,t):=\int\exp(u\cdot x-t|x|^2/2)\dd\nu(x)<\infty,
$$

define

$$
\dd\nu_{u,t}=F_{u,t}\dd\nu,
\qquad
F_{u,t}(x)=\frac{\exp(u\cdot x-t|x|^2/2)}{Z(u,t)}.
$$

Then

```{math}
:label: eq:sol-spectator-rate-density-change
\nu_{u,t}^+(S)=\int F_{u,t}\dd\sigma_S,
```

where

$$
\dd\sigma_S=e^{-\sum_{j=1}^m(x_j+1)}
\dd\mathcal H^{m-1}|_{\partial^*S\cap\operatorname{int}K_m}
$$

is the relative weighted perimeter measure. There is no surface term on $\partial K_m$.
:::

:::{prf:proof}
On compact subsets of $\operatorname{int}K_m$, the density of $\nu$ is smooth and strictly positive. Choose a mass-$p$ competitor $S^{(0)}$ whose lower outer Minkowski perimeter is within $\rho/4$ of $I_\nu(p)$. Finite lower outer Minkowski perimeter gives finite relative BV perimeter, no larger than that Minkowski content. Truncate in $K_m\cap B_R$, mollify the indicator in interior and boundary charts, use coarea, and let $R\uparrow\infty$. The usual diagonal choice gives regular relative sets $S_k$ for which

$$
\nu(S_k)\longrightarrow p,
\qquad
\operatorname{Per}_\nu(S_k)\longrightarrow
\operatorname{Per}_\nu(S^{(0)}).
$$

If necessary, a compactly supported smooth flow through a regular boundary patch in $\operatorname{int}K_m$ corrects the remaining mass error exactly. Its mass derivative is the strictly positive weighted area of the patch, while its perimeter changes continuously, so the correction costs $o(1)$ perimeter. Choose a sufficiently advanced exact-mass corrected approximant and rename it $S$. It has the asserted perimeter bound.

For a regular relative set, the one-sided tube formula inside $K_m$ identifies outer Minkowski content with

$$
\int_{\partial^*S\cap\operatorname{int}K_m}
e^{-\sum_j(x_j+1)}\dd\mathcal H^{m-1}.
$$

Topological-boundary pieces on $\partial K_m$ are support boundary, not interfaces in the support, and contribute neither to this relative formula nor to the ambient Minkowski derivative, since $\nu$ vanishes outside $K_m$. Multiplication by the positive continuous factor $F_{u,t}$ leaves the relative reduced boundary unchanged and multiplies its weighted surface measure by $F_{u,t}$. The same tube formula proves [](#eq:sol-spectator-rate-density-change). Thus no compact approximation of the probability law is used later.
:::

:::{prf:proof} Proof of [](#thm:sol-spectator-excess-rate-obstruction)
*Step 1: select one base cylinder before selecting time or spectator dimension.* For $m\ge1$, set

$$
a_m:=I_{\lambda^{\otimes m}}(1/2).
$$

If $S\subset\R^m$, then

$$
\dist\bigl((x,z),S\times\R\bigr)=\dist(x,S),
\qquad
(S\times\R)_r=S_r\times\R.
$$

Consequently cylinder extension preserves both mass and lower outer Minkowski perimeter, and $a_{m+1}\le a_m$.

[](#prop:products) gives a universal $h_*>0$ with $h_{\lambda^{\otimes m}}\ge h_*$ for every $m$. [](#lem:half) therefore gives

```{math}
:label: eq:sol-spectator-rate-profile-floor
a_m=\frac12h_{\lambda^{\otimes m}}\ge a_*:=\frac{h_*}{2}>0.
```

Thus $a_m\downarrow a_\infty$ for some $a_\infty\ge a_*>0$.

Put

$$
h_{\rm sp}:=1-e^{-1/2},
\qquad
\kappa_{\rm sp}:=\frac{h_{\rm sp}}{128}>0.
$$

Choose $\varepsilon>0$ strictly smaller than

```{math}
:label: eq:sol-spectator-rate-epsilon
\min\left\{\delta,\delta a_*,1,
\frac{\kappa_{\rm sp}a_*}{4C}\right\}.
```

Choose $M$ so that $a_M-a_\infty<\varepsilon/2$. Apply [](#lem:sol-spectator-rate-regularization) at $p=1/2$ with $\rho=\varepsilon/2$ to obtain a regular set $E_0\subset\R^M$ such that

```{math}
:label: eq:sol-spectator-rate-base
\lambda^{\otimes M}(E_0)=\frac12,
\qquad
P_0:=\lambda^{\otimes M,+}(E_0)\le a_M+\frac\varepsilon2.
```

By the definition of $a_M$, also $P_0\ge a_M\ge a_*>0$.

For every integer $N\ge1$, put

$$
\mu^{M,N}=\lambda^{\otimes M}\otimes\lambda^{\otimes N},
\qquad
E^{M,N}=E_0\times\R^N.
$$

The cylinder has mass $1/2$ and perimeter $P_0$, and hence

```{math}
:label: eq:sol-spectator-rate-additive
\begin{aligned}
0\le e_0(E^{M,N})
&=P_0-a_{M+N}<\varepsilon,
\end{aligned}
```

```{math}
:label: eq:sol-spectator-rate-relative
\begin{aligned}
\frac{e_0(E^{M,N})}{I_{\mu^{M,N}}(1/2)}
&<\frac{\varepsilon}{a_*}.
\end{aligned}
```

These estimates hold uniformly in every spectator dimension that will be chosen later. By [](#eq:sol-spectator-rate-epsilon), they imply both requested $\delta$ bounds and $e_0(E^{M,N})\le1$.

*Step 2: construct an independent positive-probability base-stability event.* Use the planted Gaussian observation realization of stochastic localization. Write

$$
X=(X^0,X^1,\ldots,X^N),
\qquad
c_t=tX+B_t,
$$

where $X^0\sim\lambda^{\otimes M}$, $X^i\sim\lambda$ for $i\ge1$, and all latent blocks and Brownian coordinate blocks are independent. Given the observation up to time $t$, its endpoint is sufficient and the posterior is

$$
\dd\mu_t(x)=Z_t^{-1}
\exp\bigl(c_t\cdot x-t|x|^2/2\bigr)\dd\mu^{M,N}(x).
$$

The prior and likelihood factorize, so pathwise

```{math}
:label: eq:sol-spectator-rate-factorization
\mu_t=\nu_t^0\otimes\bigotimes_{i=1}^N\lambda_{i,t},
\qquad
A_t=\operatorname{diag}(A_t^0,v_{1,t},\ldots,v_{N,t}),
```

where $v_{i,t}=\Var(\lambda_{i,t})$. The base posterior process is independent of the spectator posterior processes. The cylinder and distance identities give

```{math}
:label: eq:sol-spectator-rate-localized-cylinder
p_t=\nu_t^0(E_0),
\qquad
P_t(E^{M,N})=(\nu_t^0)^+(E_0),
```

so $p_t$, the tracked perimeter, and $\tau_\eta$ are all base-block measurable.

For deterministic $(u,t)$ in the base block, write

$$
F_{u,t}(x)=
\frac{\exp(u\cdot x-t|x|^2/2)}
{\int\exp(u\cdot y-t|y|^2/2)\dd\lambda^{\otimes M}(y)}.
$$

The finite exponential product has a local exponential moment. Uniform dominated convergence as $(a,\bar T)\downarrow(0,0)$ permits $a,\bar T>0$ such that

```{math}
:label: eq:sol-spectator-rate-l1-stability
\int e^{a|x|}\dd\lambda^{\otimes M}(x)\le2,
\qquad
\sup_{|u|\le a,\ 0\le t\le\bar T}
\norm{F_{u,t}-1}_{L^1(\lambda^{\otimes M})}<\eta.
```

Indeed, one may dominate uniformly by $1+e^{a_0|x|}$ at a fixed sufficiently small local moment radius $a_0$, while the unnormalized tilts converge pointwise to one.

Let $\sigma_0$ be the finite weighted perimeter measure of $E_0$. Choose $R<\infty$ with $\sigma_0(B_R)\ge P_0/2$, and shrink $a,\bar T$ if necessary so that

```{math}
:label: eq:sol-spectator-rate-R
aR+\frac{\bar T R^2}{2}\le\log2.
```

The conclusions in [](#eq:sol-spectator-rate-l1-stability) remain valid. Choose $L\ge1$ with $\Prob(|X^0|\le L)\ge1/2$, and choose

```{math}
:label: eq:sol-spectator-rate-Tb
0<T_b\le
\min\left\{\bar T,\frac{a}{2L},
\frac{a^2}{8M\log(8M)}\right\}.
```

Define the base event

```{math}
:label: eq:sol-spectator-rate-Gb
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

Independence of $X^0$ and $B^0$ yields $\Prob(G_b)\ge1/4$. On $G_b$, $|c_s^0|=|sX^0+B_s^0|\le a$ for every $s\le T_b$. Hence [](#eq:sol-spectator-rate-l1-stability) gives

$$
|\nu_s^0(E_0)-\tfrac12|<\eta.
$$

For $x\in B_R$, equations [](#eq:sol-spectator-rate-l1-stability) and [](#eq:sol-spectator-rate-R) also give

$$
F_{c_s^0,s}(x)
\ge
\frac{e^{-aR-T_bR^2/2}}
{\int e^{a|y|}\dd\lambda^{\otimes M}(y)}
\ge\frac14.
$$

The exact density-change formula [](#eq:sol-spectator-rate-density-change) therefore gives, simultaneously for every $0\le s\le T_b$,

```{math}
:label: eq:sol-spectator-rate-base-stability
\tau_\eta>T_b,
\qquad
P_s(E^{M,N})\ge\frac14\sigma_0(B_R)\ge\frac{P_0}{8}
\quad\hbox{on }G_b.
```

Neither $G_b$ nor $T_b$ depends on the later spectator dimension $N$.

*Step 3: at each fixed time, use a spectator spike to build an exact-mass profile competitor.* The published covariance-spike proposition gives, for $N$ independent centered rate-one exponentials and Gaussian-channel noise variance $s$,

```{math}
:label: eq:sol-spectator-rate-channel
\Prob\left(
\norm{\Cov(X\mid X+\sqrt sG)}_\op\ge c_{\rm sp}s
\right)
\ge1-\left(1-\frac12e^{-s}\right)^N
```

for a universal $c_{\rm sp}>0$; see [@KLnotes, Prop. 65]. Since

$$
\frac{c_t}{t}=X+\frac{B_t}{t}
\stackrel{d}=X+t^{-1/2}G,
$$

the exact conversion from localization time to channel noise variance is $s=1/t$. In the spectator block set

$$
H_t=\left\{\max_{1\le i\le N}v_{i,t}\ge\frac{c_{\rm sp}}t\right\}.
$$

The spectator covariance in [](#eq:sol-spectator-rate-factorization) is diagonal, so the channel event is exactly $H_t$. Thus, at every deterministic $t>0$,

```{math}
:label: eq:sol-spectator-rate-fixed-time
\Prob(H_t)\ge1-\left(1-\frac12e^{-1/t}\right)^N.
```

If $\log N\ge2/T$, then for each deterministic $t\in[T/2,T]$ separately,

```{math}
:label: eq:sol-spectator-rate-fixed-time-positive
\Prob(H_t)\ge h_{\rm sp}=1-e^{-1/2}.
```

Indeed, $Ne^{-1/t}\ge Ne^{-2/T}\ge1$ and $(1-x)^N\le e^{-Nx}$ for $x\in[0,1]$. This is only a fixed-time statement; the proof never asserts a common spike event on the whole interval.

On $H_t$, select the least $i$ with $v_{i,t}\ge c_{\rm sp}/t$. The posterior $\lambda_{i,t}$ is one-dimensional and log-concave, with a continuous positive density $f_{i,t}$ in the interior of its support. The base posterior is equivalent to its prior and $\lambda^{\otimes M}(E_0)=1/2$, so $0<p_t<1$. It therefore has a quantile $q_{i,t}$ with

$$
\lambda_{i,t}(( -\infty,q_{i,t}])=p_t.
$$

The corresponding full-product halfline cylinder has $\mu_t$-mass exactly $p_t$ and perimeter $f_{i,t}(q_{i,t})$. [](#lem:one-dimensional-density-variance), imported from [@BobkovChistyakov2015Concentration, Prop. 2.1], yields

```{math}
:label: eq:sol-spectator-rate-profile-competitor
I_{\mu_t}(p_t)\le f_{i,t}(q_{i,t})
\le\norm{f_{i,t}}_\infty
\le v_{i,t}^{-1/2}
\le\sqrt{\frac{t}{c_{\rm sp}}}.
```

This is a pointwise upper bound on the random profile using an explicit exact-mass competitor; no lower estimate for a moving localized profile is inserted.

*Step 4: choose time, then dimension, and integrate the fixed-time events.* With the base and $T_b$ already fixed, choose $T>0$ so that

```{math}
:label: eq:sol-spectator-rate-T
T\le\min\left\{T_0,T_b,\frac{c_{\rm sp}P_0^2}{256},1\right\},
\qquad
T^\gamma<\frac{\kappa_{\rm sp}P_0}{4C}.
```

Such a positive $T$ exists. Only now choose a finite integer $N$ satisfying $\log N\ge2/T$, and set $d=M+N$, $\mu=\mu^{M,N}$, and $E=E^{M,N}$.

For every deterministic $t\in[T/2,T]$, on $G_b\cap H_t$, equations [](#eq:sol-spectator-rate-base-stability) and [](#eq:sol-spectator-rate-profile-competitor) give

```{math}
:label: eq:sol-spectator-rate-excess-lower
t<\tau_\eta,
\qquad
e_t(E)\ge\frac{P_0}{8}-\sqrt{\frac{t}{c_{\rm sp}}}
\ge\frac{P_0}{16}.
```

For each such deterministic $t$, the base event $G_b$ and spectator event $H_t$ are independent, since they depend on disjoint latent and Brownian blocks. Hence

$$
\Prob(G_b\cap H_t)\ge\frac{h_{\rm sp}}4.
$$

Since excess is nonnegative, Tonelli applied to these marginal-in-time events gives

```{math}
:label: eq:sol-spectator-rate-integrated-lower
\begin{aligned}
\E\int_0^{T\wedge\tau_\eta}e_t(E)\dd t
&=\int_0^T\E\bigl[e_t(E)\one_{\{t<\tau_\eta\}}\bigr]\dd t
\\
&\ge\frac{P_0}{16}\frac{h_{\rm sp}}4\int_{T/2}^T\dd t
=\kappa_{\rm sp}P_0T.
\end{aligned}
```

No persistence of the spike event and no interchange beyond nonnegative Tonelli is used.

The base selection [](#eq:sol-spectator-rate-epsilon) and the time selection [](#eq:sol-spectator-rate-T) imply

$$
Ce_0(E)<\frac{\kappa_{\rm sp}P_0}{4},
\qquad
CT^\gamma<\frac{\kappa_{\rm sp}P_0}{4}.
$$

Consequently

$$
C\bigl(Te_0(E)+T^{1+\gamma}\bigr)
<\frac{\kappa_{\rm sp}P_0T}{2}
<\E\int_0^{T\wedge\tau_\eta}e_t(E)\dd t,
$$

which is [](#eq:sol-spectator-rate-violation). The complete quantifier order is

$$
(C,T_0,\gamma,\eta,\delta)
\longrightarrow(\varepsilon,M,E_0,P_0,T_b)
\longrightarrow T
\longrightarrow(N,d,\mu,E).
$$

In particular, both near-minimality estimates were fixed uniformly in $N$ before $T$ and the spectator dimension were selected.
:::

**Dependency and fence audit.** The proof uses exactly the four ledger dependencies in the header. [](#prop:products) and [](#lem:half) keep the monotone half-profile limit uniformly positive. [](#prop:covariance-spike) supplies only the separate fixed-time events [](#eq:sol-spectator-rate-fixed-time); [](#lem:one-dimensional-density-variance) supplies the exact-quantile profile competitor. The node has no `bounded_by` edge. The neighbouring circularity fence is respected because the proof upper-bounds the random profile by an explicit set instead of assuming a localized isoperimetric lower bound. The two-tail obstruction and the trace-upgrade cluster are not used, identified with this statement, or contradicted.

**Compatibility with the existing excess and KLS interfaces.** [](#prop:trivial-excess) gives the universal upper bound $\E\int_0^{T\wedge\tau}e_t\dd t\le(1+e_0)T$. There is no conflict: the lower bound [](#eq:sol-spectator-rate-integrated-lower) is itself only of order $T$. It shows that the coefficient of this $O(T)$ term cannot uniformly vanish with $e_0$ and $T^\gamma$. Indeed, $P_0=I_\mu(1/2)+e_0\le1+e_0$ by the same halfspace comparison used in [](#prop:trivial-excess).

The near-worst bootstrap in [](#thm:bootstrap) is also untouched. This construction supplies no near-worst-measure premise, and that theorem retains the external measure-scale term $h_\mu(T^{4/3}+\Xi_T)$ rather than asserting the uniform superlinear remainder refuted here. Finally, [](#prop:products) says precisely that all witness laws satisfy KLS. KLS controls their isoperimetry; it does not require the source-vanishing excess-propagation rate in [](#eq:sol-spectator-rate-violation).

**Hypotheses and closure.** All four dependencies are proved nodes or published imports in the current ledger, so the result is unconditional relative to the repository's accepted analytic inputs. The proof additionally uses standard deterministic weighted-BV approximation and tube formulas, local exponential integrability, the planted Gaussian posterior representation, the Brownian reflection principle, and Tonelli's theorem. No numerical evidence and no weighted-excess inequality enter. There is no step left analytically open in this dossier; `checked_by: none` records that a distinct cold reviewer has not yet audited it.
