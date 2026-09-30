---
title: 'Solution: product coordinate budgets, quadratic chaos, and the published covariance window'
label: sec:sol-kls-product-covariance
ledger-node:
- lem:block
- thm:budget
- cor:single-coordinate-cuts
- lem:product-qcts
- cor:KI-discharged
numbering:
  enumerator: D7.%s
---

**Overview.** This dossier proves [](#lem:block), [](#thm:budget), [](#cor:single-coordinate-cuts), [](#lem:product-qcts) and [](#cor:KI-discharged). For product measures and cuts depending on $k$ coordinates, it bounds the total source budget by summing the per-direction estimate [](#cor:per-direction) over the $k$ supported columns. The scalar Riccati identity [](#thm:scalar-riccati) and balanced survival then give a boundary bound of order $(1+k)^{-1/2}$. Separately, it proves a quadratic-chaos variance bound on products and discharges [](#ass:KI) from the published Klartag–Lehec window.

1. [](#lem:sol-block): conditional independence confines $\delta$, $G$ and $K$ to the coordinates in $J$.
2. [](#thm:sol-budget) (i): product persistence [](#prop:products) and Step 1 reduce $S_t$ to $k$ columns, and [](#cor:per-direction) bounds each column by one.
3. [](#thm:sol-budget) (ii)–(iii): [](#thm:scalar-riccati) with Fatou gives $\E r_{t\wedge\tau}\le1+k$. Doob's inequality with $\tau$ from [](#eq:sol-product-tau) gives survival up to $T_k\sim(1+k)^{-1}$. Uniform log-concavity and the perimeter supermartingale then give $\mu^+(E)\gtrsim(1+k)^{-1/2}$.
4. [](#cor:sol-refutation): with $k=1$, Markov's inequality bounds the occupation time of high source levels. This refutes the single-coordinate two-tail spike only for fixed cuts and deterministic levels. It does not prove [](#ass:all-cut-carleson).
5. [](#lem:sol-product-qcts): orthogonality of the chaos terms and a one-dimensional fourth-moment bound give the variance estimate.
6. [](#cor:sol-KI-discharged): the sup-over-time window [](#thm:KL-window) and the cap [](#eq:BL-cap) give $\E\norm{A_t}_\op\le C_1$ for $t\lesssim(\log n)^{-2}$, which is [](#ass:KI) with $C_2=2$.

**Scope.** This dossier proves exactly the five statements listed in the header. The coordinate-budget argument uses the unconditional per-direction estimate [](#cor:per-direction), the scalar Riccati identity [](#thm:scalar-riccati), and product persistence from [](#prop:products). The final covariance-window corollary uses only the published sup-over-time Klartag–Lehec window and the Brascamp–Lieb cap; it does not use the conditional Letwin input. The current bytes are an unreviewed repair: the former review is historical and does not certify this version.

For an initial law $\mu$, let $\mu_t$ denote its Eldan localization posterior, and write $a_t$ and $A_t$ for the posterior mean and covariance. For a pair $(\nu,E)$, write $p=\nu(E)$, $q=1-p$, $s=pq$, $\delta=m^E-m^F$, $G=\Sigma^E-\Sigma^F$, and $K=G+(q-p)\delta\delta^T$. Along localization use the same symbols with subscript $t$, and set

$$
B_t=s_t\delta_t\delta_t^T,
\quad R_t=A_t-B_t,
\quad r_t=\Tr B_t=s_t\abs{\delta_t}^2,
\quad S_t=s_t\norm{G_t}_{\HS}^2,
\quad D_t=2s_t\delta_t^TA_t\delta_t-r_t^2.
$$

For the coordinate-budget theorem, the coarse balanced stopping time is

```{math}
:label: eq:sol-product-tau
\tau:=\inf\{t\ge0:p_t\notin[1/3,2/3]\},
\qquad \inf\varnothing:=\infty.
```

## 1\. Coordinate support

:::{prf:lemma} = [](#lem:block)
:label: lem:sol-block
Let $\nu=\bigotimes_{i=1}^n\nu_i$ be a product probability measure on $\R^n$ with finite second moment, and let $E$ be measurable with respect to the coordinates in $J\subset\{1,\dots,n\}$. Assume $0<\nu(E)<1$, so that both conditional means and conditional covariance matrices are defined. Then $\delta_i=0$ for $i\notin J$, and $G_{ij}=K_{ij}=0$ unless $i,j\in J$.
:::

:::{prf:proof}
Because $\one_E$ is measurable with respect to $(X_j)_{j\in J}$, the entire vector $(X_i)_{i\notin J}$ is independent of both $\one_E$ and $(X_j)_{j\in J}$. Hence, for $i\notin J$, $\E[X_i\mid E]=\E X_i=\E[X_i\mid E^c]$ and $\delta_i=0$. Conditional on either color, the coordinates outside $J$ retain their original joint product law and remain independent of the coordinates in $J$. Thus for $i\notin J$,

$$
\Cov(X_i,X_j\mid E)=\Cov(X_i,X_j\mid E^c)=\Cov(X_i,X_j)
$$

when $j\notin J$, while both conditional cross-covariances are zero when $j\in J$. Therefore $G$ is supported on $J\times J$. Since $\delta\delta^T$ has the same support, so does $K$. All displayed moments are finite by hypothesis. The proof uses only conditional independence.
:::

## 2\. The coordinate budget

:::{prf:theorem} = [](#thm:budget)
:label: thm:sol-budget
Let $\mu=\bigotimes_i\mu^{(i)}$ be a product of isotropic one-dimensional log-concave measures, and let $E$ be measurable with respect to a fixed set $J$ of $k$ coordinates, with $p_0:=\mu(E)\in[2/5,3/5]$ and $q_0:=1-p_0$. Let $\tau$ be the stopping time in [](#eq:sol-product-tau). Then:

(i) $\displaystyle\E\int_0^\infty S_t\,dt \le\sum_{i\in J}(R_0)_{ii}\le k$;

(ii) $\E r_{t\wedge\tau}\le1+k$ for every $t\ge0$;

(iii) for a universal $c>0$,

$$
\mu^+(E)\ge\frac{c}{\sqrt{1+k}}\min(p_0,q_0).
$$
:::

:::{prf:proof}
Product structure is preserved pathwise by localization. The fixed event $E$ remains $J$-measurable. At every finite time the posterior likelihood is strictly positive $\mu$-almost everywhere, so $0<p_t<1$; its second moment is finite. Thus [](#lem:sol-block) applied to $(\mu_t,E)$ gives

$$
S_t=s_t\norm{G_t}_{\HS}^2
=\sum_{i\in J}s_t\abs{G_te_i}^2.
$$

For each fixed coordinate, [](#cor:per-direction) gives

$$
\E\int_0^T s_t\abs{G_te_i}^2\,dt
\le e_i^TR_0e_i=(R_0)_{ii}.
$$

Here $R_0=A_0-B_0\preceq A_0=I$, so $(R_0)_{ii}\le1$. Summing over $J$ and using monotone convergence as $T\to\infty$ proves (i).

The scalar Riccati identity is

$$
dr_t=dM_t+(S_t-D_t)dt,
\qquad D_t\ge0.
$$

Let $(\sigma_m)$ be an increasing sequence of bounded stopping times, tending to infinity, such that $M^{\sigma_m}$ is a true martingale and all stopped coefficients are integrable. At $t\wedge\tau\wedge\sigma_m$, take expectations and discard the nonnegative $D$ term. Fatou's lemma on the left and monotone convergence for the nonnegative source on the right give

$$
\E r_{t\wedge\tau}
\le r_0+\E\int_0^{t\wedge\tau}S_u\,du
\le r_0+k.
$$

Covariance decomposition gives $B_0\preceq A_0=I$. Since $B_0$ has rank at most one, its trace $r_0$ is its only nonzero eigenvalue and is at most $1$. This proves (ii).

The stopped mass martingale has quadratic variation

$$
[p]_{T\wedge\tau}=\int_0^{T\wedge\tau}s_tr_t\,dt.
$$

Because $s_t\le1/4$ and $\one_{\{t<\tau\}}r_t\le r_{t\wedge\tau}$,

$$
\E[p]_{T\wedge\tau}
\le\frac14\int_0^T\E r_{t\wedge\tau}\,dt
\le\frac{(1+k)T}{4}.
$$

The initial interval $[2/5,3/5]$ lies at distance at least $1/15$ from the complement of the coarse window $[1/3,2/3]$. Continuity and Doob's $L^2$ inequality therefore give

$$
\Prob(\tau\le T)\le C_0(1+k)T
$$

with a universal $C_0$. Choose $T_k=[2C_0(1+k)]^{-1}$. Then $\Prob(\tau>T_k)\ge1/2$, and on this event $\min(p_{T_k},q_{T_k})\ge1/3$.

The posterior $\mu_{T_k}$ is $T_k$-uniformly log-concave, hence its boundary profile satisfies

$$
\mu_{T_k}^+(E)\ge c\sqrt{T_k}\min(p_{T_k},q_{T_k}).
$$

The perimeter supermartingale inequality and the survival event give

$$
\mu^+(E)
\ge\E\mu_{T_k}^+(E)
\ge c\sqrt{T_k}\cdot\frac13\cdot\frac12
\ge\frac{c'}{\sqrt{1+k}}.
$$

Since $\min(p_0,q_0)\le1$, this implies (iii), after renaming the universal constant.

All stochastic expectation steps above are first performed at the bounded stopping times just specified. Isotropy gives finite second moments at time zero, and the Gaussian localization factor gives every polynomial moment at positive times. The standard stochastic-localization construction for a general log-concave law is obtained by coordinatewise product-preserving truncation and smoothing; the nonnegative occupation bounds pass by Fatou. The perimeter step uses only the fixed-set supermartingale inequality $\E\mu_T^+(E)\le\mu^+(E)$, obtained directly from the likelihood martingale by applying Fatou to outer neighborhoods of $E$. If $\mu^+(E)=\infty$, the boundary assertion is immediate.
:::

:::{prf:corollary} = [](#cor:single-coordinate-cuts)
:label: cor:sol-refutation
Let $\mu$ be a product as in [](#thm:sol-budget), and let $E$ be a fixed balanced cut depending on a single coordinate, where here “balanced” means explicitly $p_0=\mu(E)\in[2/5,3/5]$. Then

$$
\E\int_0^\infty S_t\,dt\le1,
\qquad
\mu^+(E)\ge c\min(p_0,q_0).
$$

Moreover, for every deterministic $L>0$,

$$
\E\bigl|\{t\ge0:S_t\ge L^2/2\}\bigr|\le\frac2{L^2}.
$$

Thus a rank-one source spike of height comparable to $\Lambda^2$ has expected occupation time $O(\Lambda^{-2})$; the proposed single-coordinate dynamic two-tail counterexample is refuted.
:::

:::{prf:proof}
The first two conclusions are [](#thm:sol-budget) with $k=1$. Tonelli and the deterministic pointwise inequality $\one_{\{S_t\ge L^2/2\}}\le2S_t/L^2$ give

$$
\E\int_0^\infty\one_{\{S_t\ge L^2/2\}}dt
\le\frac2{L^2}\E\int_0^\infty S_tdt\le\frac2{L^2}.
$$

The assertion concerns a fixed cut and a deterministic level. It supplies the total source budget used by the Riccati consumption argument; it does not prove the literal interval-by- interval form of [](#ass:all-cut-carleson).
:::

## 3\. Quadratic chaos on a non-isotropic product

:::{prf:lemma} = [](#lem:product-qcts)
:label: lem:sol-product-qcts
Let $\nu=\bigotimes_i\nu^{(i)}$ be a product of centered one-dimensional log-concave measures, let $\Var(Y_i)=\sigma_i^2$, $A=\operatorname{diag}(\sigma_i^2)$, and $Y\sim\nu$. For every symmetric matrix $M$,

$$
\Var(Y^TMY)\le C_*\norm{A^{1/2}MA^{1/2}}_{\HS}^2
$$

with a universal $C_*$.
:::

:::{prf:proof}
Write

$$
Y^TMY=\sum_iM_{ii}Y_i^2+2\sum_{i<j}M_{ij}Y_iY_j.
$$

All cross-covariances between distinct displayed summands vanish. Diagonal terms with different indices are independent; a diagonal term and an off-diagonal term leave at least one centered singleton; two distinct off-diagonal pairs are either independent or again leave a centered singleton. Therefore

$$
\Var(Y^TMY)
=\sum_iM_{ii}^2\Var(Y_i^2)
+4\sum_{i<j}M_{ij}^2\sigma_i^2\sigma_j^2.
$$

The one-dimensional log-concave reverse Hölder estimate [@KLnotes, Cor. 5] gives a universal $C_4$ such that $\E Y_i^4\le C_4\sigma_i^4$, and hence $\Var(Y_i^2)\le(C_4-1)\sigma_i^4$. It follows that

$$
\begin{aligned}
\Var(Y^TMY)
&\le\max(C_4-1,2)
\sum_{i,j}M_{ij}^2\sigma_i^2\sigma_j^2\\
&=C_*\norm{A^{1/2}MA^{1/2}}_{\HS}^2.
\end{aligned}
$$

This proof is affine in each coordinate and therefore applies pathwise to every centered product posterior $Y=X-a_t$.
:::

## 4\. Published discharge of the early covariance window

:::{prf:corollary} = [](#cor:KI-discharged)
:label: cor:sol-KI-discharged
For every $n\ge3$, the published sup-over-time estimate of [](#thm:KL-window), together with the Brascamp–Lieb cap [](#eq:BL-cap), discharges [](#ass:KI) with exponent $C_2=2$.
:::

:::{prf:proof}
The imported Klartag–Lehec window [@KLnotes, Thm. 61] used here is exactly the following: for a universal $C$, an isotropic log-concave initial law, and $t\le(C\log^2n)^{-1}$,

$$
\Prob\left(\sup_{0\le s\le t}\norm{A_s}_\op\ge2\right)
\le e^{-1/(Ct)}.
$$

This is the sup-over-time statement in [](#thm:KL-window), not a fixed-time substitute. For $t>0$, $t$-uniform log-concavity gives the pathwise Brascamp–Lieb cap $\norm{A_t}_\op\le t^{-1}$. Splitting according to the preceding event therefore gives

$$
\E\norm{A_t}_\op
\le2+t^{-1}e^{-1/(Ct)}.
$$

The second term is uniformly bounded: with $u=(Ct)^{-1}$ it is $Cu e^{-u}\le C/e$. At $t=0$, $A_0=I$. Choosing a universal $c_0\le C^{-1}$ thus gives

$$
\E\norm{A_t}_\op\le C_1
\qquad\text{for }0\le t\le c_0(\log n)^{-2},
$$

which is [](#ass:KI) with $C_2=2$ (with harmless adjustment for bounded dimensions). No quadratic-chaos preprint input is used.
:::

**Dependency and regularity audit.** The dependency uses above match the ledger edges in the header. In particular, the coordinate budget consumes the per-direction estimate before summing only the $k$ supported columns; it does not replace that sum by an operator-norm estimate. The refutation is restricted to fixed single-coordinate cuts. [](#lem:sol-product-qcts) is an unconditional product argument. [](#cor:sol-KI-discharged) consumes the published $1/\log^2n$ sup-time window and the Brascamp–Lieb cap only; the conditional $1/\log n$ Letwin window is outside its scope.

The balance hypothesis $p_0\in[2/5,3/5]$ belongs to the packaged statement of [](#thm:sol-budget). Part (i) in fact uses only $0<p_0<1$, while the nested-window survival argument in part (iii) uses the displayed balance hypothesis. Every consequence claimed in this dossier retains that hypothesis: [](#cor:sol-refutation) spells it out, and the later product-alignment discussion concerns fixed balanced cuts. The phrase “product as in [](#thm:budget)” in the covariance-bound manuscript statement uses only the theorem's product-measure class; its proof instead uses [](#lem:sol-product-qcts) and is valid for an arbitrary nontrivial cut on the coarse window.

None of the five ledger nodes covered here has a `bounded_by` edge. The rank-one obstruction `rem:single-coordinate-cuts` is downstream of [](#cor:sol-refutation); this dossier proves only the fixed-cut, deterministic-level occupation statement and does not permit a coordinate or cut chosen after observing the localization path.
