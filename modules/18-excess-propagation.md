---
numbering:
  enumerator: "18.%s"
---

(sec:excess)=
# Excess propagation: audit and a circularity warning

This section proves [](#prop:intro-audit) — the consumption audit showing the unweighted excess term is inert — and explains why a direct propagation argument can merely restate a localized isoperimetric lower bound, motivating the bootstrap mechanism of Section [](#sec:bootstrap). This is a methodological warning, not a no-go theorem. The static obstruction that forces the covariance weight ([](#prop:two-tail)) is established in Section [](#sec:qcts).

## The consumption audit

:::{prf:proposition} Unconditional integrated excess bound
:label: prop:trivial-excess
Let $\mu$ be isotropic log-concave on $\R^n$, and let $E$ be Borel with $\mu(E)=\tfrac12$, finite initial lower outer Minkowski perimeter, and excess $e_0=e_0(E)$. Then for every $T>0$ and every stopping time $\tau$,

```{math}
:label: eq:trivial-excess
\E\int_0^{T\wedge\tau}e_t(E)\dd t\ \le\ (1+e_0)\,T .
```
:::

:::{prf:proof}
Since $I_{\mu_t}\ge0$, $e_t\le\mu_t^+(E)$ pathwise. By the perimeter supermartingale property [](#eq:perimeter-supermartingale) and Tonelli, $\E\int_0^{T\wedge\tau}e_t\le\int_0^T\E\mu_t^+(E)\dd t\le T\mu^+(E)=T(I_\mu(\tfrac12)+e_0)$. Finally $I_\mu(\tfrac12)\le1$. Indeed, let $f$ be the unit-variance first marginal density and $m$ one of its medians. The corresponding coordinate halfspace has mass $1/2$ and perimeter $f(m)$. Bobkov's one-dimensional identity and variance estimate [@Bobkov1999LogConcave, Proposition 4.1 and (4.2)] give $\operatorname{Is}(f)=2f(m)$ and $\operatorname{Is}(f)^2\le2$, so $f(m)\le1/\sqrt2<1$.
:::

:::{prf:proof} Proof of [](#prop:intro-audit)
(a) is [](#prop:trivial-excess). (b): run the proof of [](#thm:intro-weighted) in Section [](#subsec:consumption) with the weight replaced by $1$ and the weighted excess propagation input replaced by [](#eq:trivial-excess); every step goes through with the universal constant $C_0'=2C_0+2C_2(1+e_0)\le2C_0+4C_2$ for $e_0\le1$. Thus [](#cor:tight-window-consumption) gives a universal positive boundary lower bound for every balanced near-Cheeger cut to which the estimate applies. If KLS failed, [](#lem:half) would provide isotropic log-concave $\mu_k$ and balanced cuts $E_k$ with $\mu_k^+(E_k)\to0$ and $e_0(E_k)\le1$ for all large $k$, contradicting that lower bound. Hence KLS follows. (c) is [](#prop:two-tail) of Section [](#sec:qcts).
:::

:::{prf:remark} Interpretation of the audit
:label: rem:audit-interpretation
Item (b) is not good news about excess propagation; it is a diagnosis of the previously stated package. An additive excess term whose integral is a priori $O(T)$ is inert next to the $C_0T$ term: it can be deleted without changing the strength of the assumption, so the unweighted Stein-trace estimate silently carried the entire logical weight of the package. Item (c) shows this weight cannot be discharged slice-wise. The weighted restatement ([](#ass:weighted-package)) was a proposed repair: it made the excess term non-inert and passed the static two-tail calibration. [](#prop:weighted-spectator-obstruction) shows that its global-operator-norm propagation clause fails, because that weight responds to independent spectator coordinates. [](#prop:spectator-excess-rate-obstruction) further shows that a tensor-stable replacement weight alone is insufficient: the uniform superlinear remainder already fails with weight one. A viable replacement must also allow an $O(T)$ scale, use a genuinely source-tied remainder, or assume near-worstness. Other proof architectures need not use this decomposition.
:::

(subsec:circularity)=
## Why direct propagation risks circularity

:::{prf:lemma} Fixed-cut perimeter supermartingale and smooth martingale
:label: lem:perimeter-martingale
For every fixed Borel set $E$ of finite initial lower outer Minkowski perimeter, $t\mapsto\mu_t^+(E)$ is an integrable nonnegative supermartingale:

```{math}
:label: eq:perimeter-conditional-supermartingale
\E[\mu_t^+(E)\mid\mathcal F_s]\le\mu_s^+(E),\qquad 0\le s\le t.
```

If the initial density is smooth and compactly supported and $E$ has a $C^2$ boundary with a tubular neighborhood over that support, the same lower Minkowski perimeter is a true martingale, with

```{math}
:label: eq:perimeter-sde
\dd\,\mu_t^+(E)=\Bigl(\int_{\partial^*E}(x-a_t)\dd\sigma_t(x)\Bigr)\cdot\dd W_t ,
```

$\sigma_t$ being the weighted surface measure of $\mu_t$ on $\partial^*E$. The drift of the perimeter vanishes identically.
:::

:::{prf:proof}
Put $E_q=\{x:\operatorname{dist}(x,E)<q\}$ and, for rational $q>0$,

$$
X_{q,t}=\frac{\mu_t(E_q)-\mu_t(E)}q
=\frac{\mu_t(E_q\setminus E)}q.
$$

For fixed $q$, [](#eq:loc-martingale) makes $X_{q,t}$ a bounded nonnegative martingale. For $n\ge1$ set

$$
Y_{n,t}=\inf\{X_{q,t}:q\in\mathbb Q,\ 0<q<1/n\}.
$$

The family is fixed and countable, so conditional expectation followed by the infimum gives $\E[Y_{n,t}\mid\mathcal F_s]\le Y_{n,s}$. Continuity from below of $q\mapsto\mu_t(E_q\setminus E)$ shows that the rational and real infima agree, and hence $Y_{n,t}\uparrow\mu_t^+(E)$ pathwise. Conditional monotone convergence proves [](#eq:perimeter-conditional-supermartingale); taking $s=0$ first also proves integrability from the assumed finite initial perimeter.

In the stated smooth compact-support class, the one-sided tube formula gives

$$
\mu_t^+(E)=\int_{\partial^*E}F_t(x)\dd\sigma_0(x),
\qquad \dd\sigma_t=F_t\dd\sigma_0.
$$

Let $D$ be the diameter of the initial support. Since $|x-a_u|\le D$ on that support, localization of the pointwise density SDE, Itô's formula, and Gronwall give $\E F_u(x)^2\le e^{D^2u}$. Thus, for every finite $T$,

$$
\E\int_0^T\int_{\partial^*E}|F_u(x)(x-a_u)|^2
\dd\sigma_0(x)\dd u
\le D^2\sigma_0(\partial^*E)\int_0^T e^{D^2u}\dd u<\infty.
$$

This is a pre-interchange stochastic-Fubini bound, so [](#eq:density-sde) yields [](#eq:perimeter-sde). The same $L^2$ estimate makes each $F_t(x)$ a true martingale on bounded intervals; conditional Tonelli then upgrades [](#eq:perimeter-conditional-supermartingale) to equality in this smooth class.
:::

:::{prf:lemma} Exact excess identity
:label: lem:excess-identity
If the initial density is smooth and compactly supported and $E$ has a $C^2$ boundary with a tubular neighborhood over that support, then for every finite $t\ge0$,

```{math}
:label: eq:excess-identity
\E\,e_t(E)\ =\ e_0(E)+\Bigl[\,I_\mu(p_0)-\E\,I_{\mu_t}(p_t)\,\Bigr].
```
:::

:::{prf:proof}
Take expectations in $e_t=\mu_t^+(E)-I_{\mu_t}(p_t)$ and use $\E\mu_t^+(E)=\mu^+(E)=I_\mu(p_0)+e_0$ from [](#lem:perimeter-martingale).
:::

Within this smooth compact-support class, identity [](#eq:excess-identity) is conceptually decisive: excess propagation is not about the set $E$ at all, except through the random volume $p_t$. It is exactly the question of lower-bounding the expected isoperimetric profile of the random posterior at the current mass; the set enters only through the driftless perimeter martingale.

:::{prf:lemma} Infima over a fixed competitor family
:label: lem:inf-martingales
Let $\mathfrak S$ be a *fixed nonempty countable* family of Borel sets of finite initial lower outer Minkowski perimeter and define $J_t=\inf\{\mu_t^+(S):S\in\mathfrak S\}$. Then $J$ is a supermartingale. The same conclusion holds for a fixed family admitting a fixed countable determining subfamily whose pointwise infimum agrees almost surely at every time. Pointwise, on $\{t<\tau_\eta\}$,

$$
I_{\mu_t}(p_t)\ge J_t(\eta),
\qquad
J_t(\eta):=\inf\bigl\{\mu_t^+(S):
\mu_t(S)\in[\tfrac12-\eta,\tfrac12+\eta]\bigr\}.
$$

The competitor family defining $J_t(\eta)$ is random and time-dependent, so the first assertion does *not* imply that $J(\eta)$ or $I_{\mu_t}(p_t)$ is a supermartingale.
:::

:::{prf:proof}
Countability supplies measurability and one common null set for the fixed-cut inequalities. For each fixed $S$, [](#lem:perimeter-martingale) gives $\E[\mu_t^+(S)\mid\mathcal F_s]\le\mu_s^+(S)$ (with equality in its smooth compact-support class). Hence $\E[J_t\mid\mathcal F_s]\le\mu_s^+(S)$ for every $S$; take the infimum over $S$. Nonemptiness also gives an integrable upper bound for $J_t$. The second pointwise comparison holds because the constrained family at exact mass $p_t$ is contained in the windowed family when $p_t$ is in the window. No conditional-expectation comparison is available from this inclusion because the eligible family changes with $t$.
:::

:::{prf:remark} The circularity, formalized
:label: rem:circularity
Within the smooth compact-support class of [](#lem:excess-identity), excess propagation is equivalent to a lower bound on $\E I_{\mu_t}(p_t)$. Such a lower bound is itself a Cheeger-type statement for the random posterior, so an argument that simply inserts a lower bound for the localized profile risks assuming the phenomenon the argument is meant to prove. [](#lem:inf-martingales) supplies no monotonicity for that profile, because the mass-constrained competitor family changes with time. Thus “direct propagation is circular” should be read as a proof-design warning, not a formal impossibility result: additional structure could conceivably control the moving infimum. The external worst-case constant $\hstar_n$ of [](#eq:hstar-def) provides one demonstrably non-circular anchor in a contradiction argument; the next section develops that bootstrap without claiming it is the only possible anchor.
:::

(subsec:excess-barriers)=
## Methodological constraints from this section

:::{prf:remark} Localized profile insertion may assume the target
:label: rem:profile-circularity
Excess propagation requires a lower bound on the expected isoperimetric profile of the random posterior. The supermartingale statement available here, [](#lem:excess-identity) together with [](#lem:inf-martingales) and [](#rem:circularity), applies only to a *fixed* competitor family, whereas the balanced family changes with time. Directly inserting a lower bound for the time-dependent localized profile therefore risks assuming the Cheeger control that excess propagation is meant to prove; a proof must supply additional structure or an external non-circular anchor.
:::
