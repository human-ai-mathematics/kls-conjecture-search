---
title: 'Solution: split-class screened weighted supply (total-budget form)'
label: sec:sol-split-screened-supply
ledger-node: prop:split-screened-supply
numbering:
  enumerator: D25.%s
---

**Overview.** This dossier proves [](#prop:split-screened-supply) in total-budget form, on the regular split class ([](#thm:sol-split-screened-supply)). For a product of isotropic one-dimensional log-concave laws and a cut depending on $k$ coordinates, the screened weighted excess over $[0,T\wedge\tau_\eta]$ is at most $(2k+64\eta^2(1+k))/\kappa$ ([](#eq:sol-split-screened-supply)), uniformly in $T$, $n$ and the spectators. It is not a $C(k)\,T$ estimate. On the screen the weighted excess is dominated by the Stein source $Q_t$, and $Q_t$ is then paid from the coordinate source and dissipation budgets. The passage to general split laws is left open ([](#rem:sol-general-class)).

1. On the screened set, $e_tW_{\rm cut}\le Q_t/\kappa$ pathwise ([](#eq:sol-screen-domination)). This uses only $e_t\ge0$ and gives [](#eq:sol-step1).
2. In the tight window, [](#lem:stein-vs-source) converts $Q_t$ into $2S_t+64\eta^2D_t$ ([](#eq:sol-step2)).
3. [](#lem:block) and [](#cor:per-direction) give the source budget $\E\int_0^\infty S_t\,\dd t\le k$ ([](#eq:sol-step3)).
4. [](#thm:scalar-riccati) with optional stopping and step 3 gives the dissipation budget $1+k$ ([](#eq:sol-step4)). Chaining steps 1–4 proves the theorem.
5. Separately, [](#lem:sol-constant-supply-consumption) extends [](#cor:tight-window-consumption) to a Carleson input with an additive constant. By Grönwall and Doob, the mass survives in the window up to a time $T_*$ with probability at least $1/2$, and [](#lem:survival-implies-kls) turns this into a perimeter bound. No screened trace companion and no KLS conclusion is claimed ([](#rem:sol-no-companion)).

**Scope.** This dossier proves the screened weighted-excess supply estimate for coordinate cuts on products of isotropic one-dimensional log-concave measures, in *total-budget* form: the bound is a constant depending only on the number $k$ of active coordinates, the window half-width $\eta$, and the screening ratio $\kappa$; it is uniform in the horizon $T$, in the ambient dimension $n$, and in every spectator coordinate. It is **not** an estimate of the form $C(k)\,T$, and no claim of that fixed-time or linear-in-$T$ shape is made here. The dossier asserts nothing about the trace-upgrade cluster ([](#conj:trace-upgrade), the high-rank part of [](#conj:stein-weighted), [](#conj:product-alignment)); in particular it neither proves nor compares any occupation estimate of that cluster, in compliance with repository constraint 6. A separate auxiliary lemma ([](#lem:sol-constant-supply-consumption) below) records the constant-supply extension of [](#cor:tight-window-consumption); it is logically independent of the main proposition and is clearly separated from it.

**Regularity and measurability conventions.** We adopt verbatim the conventions of Section 5 of the probe record

<research/explorations/2026-08-30-kls-route-prober-weighted-screened-interface-w4w01.md>:

(M1) We work on the usual $\Prob$-augmented right-continuous filtration of the driving $n$-dimensional Brownian motion of Eldan's stochastic localization.

(M2) *Regular split class.* The main theorem is stated and proved for initial data in the compact-smooth product-preserving regularity class of the certified Riccati-core and excess-audit dossiers (`kls-localization-riccati-core.md` and `kls-excess-audit.md`, both under `solutions/`): each factor $\mu^{(i)}$ is a compactly supported one-dimensional log-concave law with smooth density, normalized to mean zero and variance one, and the cut $E=E_J\times\R^{J^c}$ is measurable with respect to the coordinates in $J$ with $E_J\subset\R^{J}$ having $C^2$ relative boundary with a tubular neighborhood over the support, so that $P_0(E)<\infty$ and the one-sided tube formula identifies the lower outer Minkowski perimeter with weighted surface area. On every bounded time interval all stochastic integrals below are true martingales after the usual bounded stopping, with regularization-independent constants. Passage to general split laws and cuts is discussed, and its unresolved part explicitly flagged, in [](#rem:sol-general-class) below.

(M3) $P_t=P_t(E)=\mu_t^+(E)$ is the lower outer Minkowski perimeter, realized pathwise as the increasing limit of infima over the fixed countable rational boundary-layer family of bounded continuous mass martingales ([](#lem:perimeter-martingale), construction of `solutions/kls-excess-audit.md`); as a pathwise monotone limit of countable infima of continuous adapted processes it is progressively measurable. In the regular class the localized density field is jointly measurable and positive, and the moving profile value $I_{\mu_t}(p_t)$ is jointly measurable in $(t,\omega)$ via a fixed countable regular competitor family; hence the excess

$$
e_t \;=\; e_t(E)\;=\;P_t(E)-I_{\mu_t}(p_t)
$$

is progressively measurable. This is a *measurability* convention only: no supermartingale or martingale property of the moving profile infimum is asserted (the caveat of [](#lem:inf-martingales) is preserved), and no lower bound on $I_{\mu_t}(p_t)$ is used anywhere in this dossier.

(M4) On $\{0<p_t<1\}$ the processes $A_t$, $K_t$, $Q_t$ below are continuous and adapted in the regular class, and the map $(A,K)\mapsto\lambda_{\rm cut}(A,K)$ is Borel on supported pairs $\{(A,K):A\succeq0,\ K=P_{\operatorname{Ran}A}\,K\,P_{\operatorname{Ran}A}\}$ (fixed-rank strata together with the Borel Moore–Penrose formula [](#eq:sol-lyapunov-pseudoinverse) of `solutions/lem-lyapunov-stein-duality.md`, with the separate convention $\lambda_{\rm cut}(A,0)=0$). Hence the weight $W_{\rm cut}(A_t,K_t)$ and the screened indicator $\one_{\mathcal A_{\kappa,t}}=\one_{\{Q_t-\kappa e_tW_{\rm cut}(A_t,K_t)\ge0\}}$ are progressively measurable. Both appear *only* inside nonnegative Lebesgue-time integrals, handled by Tonelli; no Itô differential is ever taken of the weight, of the indicator, or of any function of $\lambda_{\rm cut}$.

**Notation.** Fix the manuscript localization notation: $p_t=\mu_t(E)$, $q_t=1-p_t$, $s_t=p_tq_t$, $\delta_t=m_t^E-m_t^F$, $G_t=\Sigma_t^E-\Sigma_t^F$, $K_t=G_t+(q_t-p_t)\delta_t\delta_t^T$, $B_t=s_t\delta_t\delta_t^T$, $R_t=A_t-B_t$, $r_t=\Tr B_t=s_t\abs{\delta_t}^2$, $S_t=s_t\norm{G_t}_\HS^2$, and $D_t=2s_t\delta_t^TA_t\delta_t-r_t^2\ge r_t^2\ge0$ ([](#thm:scalar-riccati)). Set

$$
Q_t\;=\;s_t\norm{K_t}_\HS^2\;=\;\frac{\calS_{\mu_t}(E)}{s_t},
$$

the second equality being the certified Stein-norm identity $\calS_\nu(E)=s^2\norm K_\HS^2$ of [](#prop:stein-rep). With the convention $\lambda_{\rm cut}(A,0)=0$ of [](#lem:lyapunov-stein-duality), put

$$
W_{\rm cut}(A,K)\;=\;\bigl(1+\lambda_{\rm cut}(A,K)\bigr)^{5/2},
\qquad
\mathcal A_{\kappa,t}\;=\;\bigl\{Q_t\ \ge\ \kappa\,e_t\,W_{\rm cut}(A_t,K_t)\bigr\}.
$$

Finally, for $\eta\in(0,1/4]$ let $\tau_\eta=\inf\{t\ge0:\abs{p_t-1/2}>\eta\}$ be the continuous-exit time of `solutions/kls-localization-riccati-core.md`; it is a stopping time for the augmented right-continuous filtration because $p$ has continuous paths.

**Refined statement.** The theorem below is the verbatim statement of the candidate ledger node `prop:split-screened-supply`, restricted per convention (M2) to the regular split class; [](#rem:sol-general-class) records the approximant convention for general split laws together with the explicit unresolved limit-interchange gap.

:::{prf:theorem} split-class screened weighted supply, total-budget form
:label: thm:sol-split-screened-supply
Let $\mu=\bigotimes_{i=1}^n\mu^{(i)}$ be a product of isotropic one-dimensional log-concave probability measures in the regular split class (M2), let $J\subset\{1,\dots,n\}$ with $\abs J=k$, and let $E$ be measurable with respect to the coordinates in $J$ with $0<p_0=\mu(E)<1$. Then, for every $\eta\in(0,1/4]$, every $\kappa>0$, and every $T>0$,

```{math}
:label: eq:sol-split-screened-supply
\E\int_0^{T\wedge\tau_\eta}
e_t\,\bigl(1+\lambda_{\rm cut}(A_t,K_t)\bigr)^{5/2}\,
\one_{\{Q_t\ \ge\ \kappa\,e_t\,W_{\rm cut}(A_t,K_t)\}}\,\dd t
\;\le\;\frac{2k+64\,\eta^2(1+k)}{\kappa}.
```

The right-hand side is independent of $T$, of the ambient dimension $n$, and of every spectator factor $\mu^{(i)}$, $i\notin J$.
:::

:::{prf:proof}
Throughout, product structure is preserved pathwise by stochastic localization and the posterior covariance $A_t$ is diagonal ([](#prop:products)); the fixed cut $E$ remains $J$-measurable; and, since $0<p_0<1$ and the finite-time posterior has a strictly positive likelihood relative to $\mu$, we have $0<p_t<1$ at every finite time, so all the displayed two-color quantities are defined along the whole path. If $\abs{p_0-1/2}>\eta$ then $\tau_\eta=0$ and [](#eq:sol-split-screened-supply) is the trivial statement $0\le(2k+64\eta^2(1+k))/\kappa$; assume therefore $\abs{p_0-1/2}\le\eta$ from now on. All integrands below are nonnegative and progressively measurable by conventions (M3)–(M4), so every interchange of $\E$ and $\dd t$ is Tonelli for nonnegative integrands and needs no a priori integrability.

*Step 1: pathwise domination on the aligned set.* We claim that, pathwise, for every $t$ with $0<p_t<1$,

```{math}
:label: eq:sol-screen-domination
e_t\,W_{\rm cut}(A_t,K_t)\,\one_{\mathcal A_{\kappa,t}}
\;\le\;\frac{Q_t}{\kappa}.
```

First, $e_t\ge0$: the set $E$ has $\mu_t$-mass $p_t$ and perimeter $P_t(E)$, hence is a competitor in the infimum defining the profile value $I_{\mu_t}(p_t)$, so $I_{\mu_t}(p_t)\le P_t(E)$. This uses only the definition of the profile as an infimum (the upper-bound direction); no profile lower bound enters. Now, on $\mathcal A_{\kappa,t}$ the defining inequality reads $\kappa\,e_tW_{\rm cut}\le Q_t$, and dividing by $\kappa>0$ gives $e_tW_{\rm cut}\le Q_t/\kappa$ there; off $\mathcal A_{\kappa,t}$ the left side of [](#eq:sol-screen-domination) vanishes while $Q_t=s_t\norm{K_t}_\HS^2\ge0$. This proves [](#eq:sol-screen-domination) with no case excluded.

For the record, the degenerate state $K_t=0$ is covered by the conventions of [](#lem:lyapunov-stein-duality) and charges nothing: there $Q_t=0$ and $\lambda_{\rm cut}(A_t,0)=0$, so $W_{\rm cut}=1$ and membership in $\mathcal A_{\kappa,t}$ reads $0\ge\kappa e_t$, which (as $e_t\ge0$) holds exactly when $e_t=0$; in either case both sides of [](#eq:sol-screen-domination) vanish.

Integrating [](#eq:sol-screen-domination) in time and taking expectations,

```{math}
:label: eq:sol-step1
\E\int_0^{T\wedge\tau_\eta}
e_t\,W_{\rm cut}(A_t,K_t)\,\one_{\mathcal A_{\kappa,t}}\,\dd t
\;\le\;\frac1\kappa\,\E\int_0^{T\wedge\tau_\eta}Q_t\,\dd t .
```

*Step 2: tight-window conversion to Riccati currencies.* On $\{t<\tau_\eta\}$ we have $\abs{p_t-1/2}\le\eta\le1/4$, hence $s_t\ge1/4-\eta^2\ge3/16>1/8$, and the second inequality of the certified conversion [](#lem:stein-vs-source) applies:

$$
Q_t=\frac{\calS_{\mu_t}(E)}{s_t}\;\le\;2S_t+64\,\eta^2D_t
\qquad\text{on }\{t<\tau_\eta\}.
$$

The single time $t=\tau_\eta$ has Lebesgue measure zero in the time integral, so

```{math}
:label: eq:sol-step2
\E\int_0^{T\wedge\tau_\eta}Q_t\,\dd t
\;\le\;2\,\E\int_0^{T\wedge\tau_\eta}S_t\,\dd t
+64\,\eta^2\,\E\int_0^{T\wedge\tau_\eta}D_t\,\dd t .
```

*Step 3: the coordinate source budget under $0<p_0<1$.* We prove

```{math}
:label: eq:sol-step3
\E\int_0^\infty S_t\,\dd t\;\le\;\sum_{i\in J}(R_0)_{ii}\;\le\;k .
```

This is part (i) of [](#thm:budget), whose certified dossier (`solutions/kls-product-covariance.md`) records in its dependency audit that this part uses only $0<p_0<1$ and not the packaged coarse balance window $p_0\in[2/5,3/5]$; for the reviewer's convenience we reproduce the three-line certified argument, which cites only unconditional inputs. At every finite time, $(\mu_t,E)$ is a finite-second-moment product pair with a $J$-measurable cut and $0<p_t<1$, so [](#lem:block) gives that $G_t$ is supported on $J\times J$; hence its columns $G_te_i$ vanish for $i\notin J$ and

$$
S_t=s_t\norm{G_t}_\HS^2=\sum_{i\in J}s_t\abs{G_te_i}^2 .
$$

For each fixed $i$, the unconditional per-direction estimate [](#cor:per-direction) gives $\E\int_0^Ts_t\abs{G_te_i}^2\,\dd t\le e_i^TR_0e_i=(R_0)_{ii}$ for every $T>0$. Since $R_0=A_0-B_0\preceq A_0=I_n$ by isotropy of the product, $(R_0)_{ii}\le1$. Summing over $i\in J$ and letting $T\to\infty$ by monotone convergence proves [](#eq:sol-step3). In particular, since $S\ge0$,

```{math}
:label: eq:sol-step3b
\E\int_0^{T\wedge\tau_\eta}S_t\,\dd t\;\le\;k .
```

*Step 4: the dissipation budget.* We prove

```{math}
:label: eq:sol-step4
\E\int_0^{T\wedge\tau_\eta}D_t\,\dd t\;\le\;1+k .
```

By [](#thm:scalar-riccati) there is a scalar local martingale $M$ with $\dd r_t=\dd M_t+(S_t-D_t)\,\dd t$. In the regular class (M2), let $(\sigma_m)_{m\ge1}$ be an increasing sequence of bounded stopping times tending to infinity such that each stopped $M^{\sigma_m}$ is a true martingale and all stopped coefficients are integrable — exactly the localizing times used in the certified dossiers `solutions/kls-localization-riccati-core.md` and `solutions/kls-product-covariance.md`. Optional stopping at the bounded stopping time $T\wedge\tau_\eta\wedge\sigma_m$ gives

$$
\E\, r_{T\wedge\tau_\eta\wedge\sigma_m}
\;=\;r_0+\E\int_0^{T\wedge\tau_\eta\wedge\sigma_m}(S_t-D_t)\,\dd t ,
$$

whence, discarding $\E\,r_{T\wedge\tau_\eta\wedge\sigma_m}\ge0$ and enlarging the $S$-integral to $[0,\infty)$ (both integrands are nonnegative),

$$
\E\int_0^{T\wedge\tau_\eta\wedge\sigma_m}D_t\,\dd t
\;\le\;r_0+\E\int_0^\infty S_t\,\dd t
\;\le\;r_0+k
$$

by [](#eq:sol-step3). Since $D\ge0$ and $T\wedge\tau_\eta\wedge\sigma_m\uparrow T\wedge\tau_\eta$, monotone convergence in $m$ gives $\E\int_0^{T\wedge\tau_\eta}D_t\,\dd t\le r_0+k$. Finally $r_0\le1$: the covariance decomposition gives $B_0\preceq A_0=I_n$, and $B_0=s_0\delta_0\delta_0^T$ has rank at most one, so its trace $r_0$ is its only nonzero eigenvalue and is at most $1$. This proves [](#eq:sol-step4).

*Step 5: combination.* Chaining [](#eq:sol-step1), [](#eq:sol-step2), [](#eq:sol-step3b), and [](#eq:sol-step4),

$$
\E\int_0^{T\wedge\tau_\eta}
e_t\,W_{\rm cut}(A_t,K_t)\,\one_{\mathcal A_{\kappa,t}}\,\dd t
\;\le\;\frac1\kappa\Bigl(2k+64\,\eta^2(1+k)\Bigr),
$$

which is [](#eq:sol-split-screened-supply). Every bound used — [](#eq:sol-screen-domination), the conversion constants $2$ and $64\eta^2$, the source budget $k$, and the dissipation budget $1+k$ — is independent of $T$, of $n$, and of the spectator factors, which never entered; the constant is therefore total-budget as claimed.
:::

:::{prf:remark} Shape of the bound; what is not claimed
:label: rem:sol-shape
The bound [](#eq:sol-split-screened-supply) is a *total budget*: a single constant $c_E(k,\eta,\kappa)=(2k+64\eta^2(1+k))/\kappa$ controlling the screened weighted excess over the entire window $[0,T\wedge\tau_\eta]$ for *every* $T>0$ simultaneously. It is not of the form $C(k)\,T$, and this dossier does not assert any fixed-time expected-source estimate $\sup_{t\le T_0}\E[Q_t\one_{\mathcal A_{\kappa,t}}\one_{\{t<\tau_\eta\}}]\le C(k)$ that would yield such a form; that upgrade is recorded as open in the probe record. Likewise nothing here bears on the trace-upgrade cluster ([](#conj:trace-upgrade), high-rank [](#conj:stein-weighted), [](#conj:product-alignment)) or on the general (non-product) screened supply: no occupation estimate, equivalence, or comparison across that cluster is proved or implied (constraint 6).
:::

:::{prf:remark} Interpretation: the weight is cut-local on the split class
:label: rem:sol-harmonic-mean
This remark is interpretive and is used nowhere in the proof of [](#thm:sol-split-screened-supply). Pathwise, $A_t$ is diagonal ([](#prop:products)) with positive diagonal entries $A_t^{(i)}$ in the regular class, and $K_t=P_JK_tP_J$ by [](#lem:block). By the certified eigenbasis identity [](#eq:sol-cut-harmonic-mean) of `solutions/lem-lyapunov-stein-duality.md` (Remark on the auxiliary harmonic-mean formula), $\lambda_{\rm cut}(A_t,K_t)$ is the $\abs{(K_t)_{ij}}^2$-weighted harmonic mean of $(A_t^{(i)}+A_t^{(j)})/2$ over $(i,j)\in J\times J$, hence

$$
\lambda_{\rm cut}(A_t,K_t)\;\le\;\max_{i\in J}A_t^{(i)} :
$$

on the split class the weight sees only the $J$-block covariance scale; spectator covariance spikes are invisible to both $Q_t$ and $W_{\rm cut}$, consistently with the uniformity in $n$ and in the spectators of the theorem.
:::

:::{prf:remark} General split laws: approximant convention and explicit gap
:label: rem:sol-general-class
For a general product $\mu=\bigotimes_i\mu^{(i)}$ of isotropic one-dimensional log-concave laws and a general $J$-measurable cut with $0<p_0<1$ and $P_0(E)<\infty$, statement [](#eq:sol-split-screened-supply) is *defined on approximants*, per convention (M2) and Section 5(5) of the probe record: apply [](#thm:sol-split-screened-supply) to the coordinatewise product-preserving truncated and smoothed approximants used in the certified scheme of `solutions/kls-product-covariance.md` (each factor truncated, smoothed, and renormalized to isotropic position — which preserves the class — and the cut regularized within the $J$-coordinates, preserving $J$-measurability); the constant $(2k+64\eta^2(1+k))/\kappa$ is uniform over the approximation. What is *not* proved here, and is flagged as an explicit open technical step, is the limit interchange for the screened integrand itself: the indicator $\one_{\mathcal A_{\kappa,t}}$ does not converge monotonically along the approximation, so the left side of [](#eq:sol-split-screened-supply) evaluated directly on the limiting rough data is not obtained from the approximant bound by Fatou. Any consumer of the general-class statement must either work with the approximants or close this interchange separately.
:::

## Auxiliary lemma: constant-supply extension of tight-window consumption

The following lemma is *not* part of [](#thm:sol-split-screened-supply) and is not needed by its proof. It extends the certified [](#cor:tight-window-consumption) by allowing a constant additive term in the absorptive Carleson input — exactly the shape a total-budget supply such as [](#eq:sol-split-screened-supply) would feed, as recorded in Section 1 of the probe. It is stated in the general (not split-specific) localization setting of the certified Riccati dossier, in the regular class of (M2) with its regularization-independent constants.

:::{prf:lemma} tight-window consumption with a constant supply term
:label: lem:sol-constant-supply-consumption
Let $\mu$ be isotropic and log-concave, $E$ a cut, and fix $0<\eta\le1/6$ with $\abs{p_0-1/2}\le\eta/2$. Suppose that for constants $c,C_0,C_1\ge0$, a number $\alpha<1$, a horizon $T_0>0$, and every $T\le T_0$,

```{math}
:label: eq:sol-constant-carleson
\E\int_0^{T\wedge\tau_\eta}S_t\,\dd t
\;\le\;c+C_0T
+C_1\,\E\int_0^{T\wedge\tau_\eta}r_t\,\dd t
+\alpha\,\E\int_0^{T\wedge\tau_\eta}D_t\,\dd t ,
```

and that

```{math}
:label: eq:sol-apriori-finite
\E\int_0^{T_0\wedge\tau_\eta}D_t\,\dd t<\infty
```

(automatic in the regular class (M2)). Set $C_*=(1+c+C_0T_0)\,e^{C_1T_0}$. Then for every positive $T_*\le\min\bigl(T_0,\ 4\eta^2/(9C_*)\bigr)$,

$$
\Prob\bigl\{\min(p_{T_*},q_{T_*})\ge1/3\bigr\}\;\ge\;\frac12 ,
$$

and hence [](#lem:survival-implies-kls) gives $\mu^+(E)\ge c'\sqrt{T_*}$ for a numerical $c'>0$, with $T_*$ depending only on $(T_0,c,C_0,C_1,\eta)$.
:::

:::{prf:proof}
This is the proof of the certified [](#cor:tight-window-consumption) (Section 4 of `solutions/kls-localization-riccati-core.md`) with one line changed in the Gronwall input; we run it in full. Let $u(T)=\E\,r_{T\wedge\tau_\eta}$ for $0\le T\le T_0$. In the regular class, $r_t=\Tr B_t\le\Tr A_t$ is bounded on bounded intervals by the squared support diameter, so $u$ is finite and bounded on $[0,T_0]$, and it is measurable ($r$ has continuous paths, so $u$ is a pointwise limit of continuous functions by dominated convergence); the constants produced below do not depend on the regularization.

Integrate [](#thm:scalar-riccati) at the bounded stopping times $T\wedge\tau_\eta\wedge\sigma_m$, with $(\sigma_m)$ the localizing sequence of (M2), and let $m\uparrow\infty$: Fatou on the left (as $r\ge0$ has continuous paths) and monotone convergence for the two nonnegative occupation terms give

$$
u(T)\;\le\;r_0+\E\int_0^{T\wedge\tau_\eta}S_t\,\dd t
-\E\int_0^{T\wedge\tau_\eta}D_t\,\dd t .
$$

Insert [](#eq:sol-constant-carleson) and use $r_0\le1$ (rank-one $B_0\preceq A_0=I$). The term $(\alpha-1)\E\int_0^{T\wedge\tau_\eta}D_t\,\dd t$ is nonpositive and finite by [](#eq:sol-apriori-finite) with $\alpha<1$, so it may be discarded — this is the one place the absorption margin and the a priori finiteness are used — leaving

$$
u(T)\;\le\;1+c+C_0T
+C_1\,\E\int_0^{T\wedge\tau_\eta}r_t\,\dd t
\;\le\;1+c+C_0T+C_1\int_0^Tu(t)\,\dd t ,
$$

the last inequality by the pathwise bound $\one_{\{t<\tau_\eta\}}r_t\le r_{t\wedge\tau_\eta}$ and Tonelli. Gronwall's inequality for the bounded measurable $u$ yields

$$
u(T)\;\le\;(1+c+C_0T)\,e^{C_1T}\;\le\;C_*
\qquad(0\le T\le T_0).
$$

Before exit, $\abs{p_t-1/2}\le\eta\le1/6$ gives $s_t\ge1/4-\eta^2\ge2/9$, hence $\abs{\delta_t}^2=r_t/s_t\le\tfrac92 r_t$ and

$$
\E\int_0^{T\wedge\tau_\eta}\abs{\delta_t}^2\,\dd t
\;\le\;\frac92\int_0^T\E\bigl[\one_{\{t<\tau_\eta\}}r_t\bigr]\,\dd t
\;\le\;\frac92\,C_*T .
$$

Since $\abs{p_0-1/2}\le\eta/2$, continuity of $p$ forces $\sup_{t\le T\wedge\tau_\eta}\abs{p_t-p_0}\ge\eta/2$ on $\{\tau_\eta\le T\}$. Doob's $L^2$ inequality applied to the stopped mass martingale, whose quadratic variation is $\dd[p]_t=s_t^2\abs{\delta_t}^2\,\dd t$ with $s_t\le1/4$, gives

$$
\Prob(\tau_\eta\le T)
\;\le\;\frac4{\eta^2}\,\E[p]_{T\wedge\tau_\eta}
\;\le\;\frac{4}{16\,\eta^2}\cdot\frac92\,C_*T
\;=\;\frac{9C_*T}{8\eta^2}.
$$

For $T_*\le\min(T_0,4\eta^2/(9C_*))$ this is at most $1/2$, and on $\{\tau_\eta>T_*\}$ we have $\min(p_{T_*},q_{T_*})\ge1/2-\eta\ge1/3$. The boundary consequence is [](#lem:survival-implies-kls) with $(T_0,c_0,b_0)=(T_*,1/2,1/3)$.
:::

:::{prf:remark} Role of the lemma; no companion claimed
:label: rem:sol-no-companion
[](#lem:sol-constant-supply-consumption) shows the consumption chain does not intrinsically require an $O(T)$ supply: a $T$-uniform constant such as the right-hand side of [](#eq:sol-split-screened-supply) is an admissible input shape, at the price of a shorter survival time $T_*\asymp\eta^2/C_*$. This dossier proves *only* the supply side on the split class. No screened trace companion (the estimate (C)/(22) of the probe record) is proved or assumed here, and no KLS-type conclusion is drawn from [](#thm:sol-split-screened-supply).
:::

**Obstructions respected.**

- `rem:two-tail-slice-bounds` ([](#prop:two-tail)): that fence kills slice-wise absolute-scale Stein estimates and calibrates the necessary covariance-weight power $5/2$. [](#thm:sol-split-screened-supply) is a time-integrated expectation bound, not a slice-wise estimate; it retains exactly the calibrated weight $(1+\lambda_{\rm cut})^{5/2}$, whose two-tail value is $\lambda_{\rm cut}(A_\Lambda,K_\Lambda)=\Lambda$ by the certified calibration [](#eq:sol-cut-two-tail), so no weaker power is smuggled in; and the two-tail initial laws $N(0,\diag(\Lambda,1,\dots,1))$, $\Lambda>1$, lie outside the hypothesis class (their first factor is not isotropic). States of two-tail type reached dynamically remain chargeable by the screen and are paid for through the budget $Q_t/\kappa$; the theorem never discards them.

- `rem:profile-circularity`: no lower bound on the moving profile $I_{\mu_t}(p_t)$ — and no profile information beyond its definition as an infimum, used once in Step 1 in the upper-bound direction $I_{\mu_t}(p_t)\le P_t(E)$ to record $e_t\ge0$ — enters any step. The excess-identity refinement fenced by this obstruction is not used; indeed $e_t$ is touched only through the pathwise screen inequality [](#eq:sol-screen-domination).
