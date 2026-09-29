---
title: 'Solution: the perimeter martingale and the excess-consumption audit'
label: sec:sol-kls-excess-audit
ledger-node:
- prop:intro-audit
- prop:trivial-excess
- lem:perimeter-martingale
- lem:excess-identity
- lem:inf-martingales
numbering:
  enumerator: D4.%s
---

**Overview.** This dossier proves [](#lem:perimeter-martingale), [](#prop:trivial-excess), [](#lem:excess-identity), [](#lem:inf-martingales) and [](#prop:intro-audit). Under stochastic localization, the lower Minkowski perimeter of a fixed cut is a supermartingale in general and a true martingale in the compact-support smooth class. The resulting excess bounds are then used to audit what an unweighted Stein-trace estimate would consume.

1. [](#lem:sol-perimeter-martingale): countable infima of bounded boundary-layer mass martingales increase to $P_t(E)$, which gives [](#eq:sol-perimeter-supermartingale). In the compact smooth class, the surface representation [](#eq:sol-perimeter-representation), the $L^2$ density bound [](#eq:sol-density-L2) and stochastic Fubini give the martingale SDE [](#eq:sol-perimeter-sde).
2. [](#prop:sol-trivial-excess): $e_t\le P_t$ and Step 1 give [](#eq:sol-trivial-excess). Here $I_\mu(1/2)<1$ follows from Bobkov's one-dimensional estimates.
3. [](#lem:sol-excess-identity): in the compact class only, the martingale property gives [](#eq:sol-excess-identity).
4. [](#lem:sol-inf-martingales): the infimum over a fixed countable family of cuts is a supermartingale. The comparison [](#eq:sol-window-infimum) is only pointwise, and no supermartingale property is claimed for the random windowed infimum.
5. [](#prop:sol-intro-audit): (i) is Step 2. (ii) Step 2 and [](#lem:stein-vs-source) turn the unweighted estimate [](#eq:sol-unweighted-stein) into the absorptive Carleson bound [](#eq:sol-absorptive-carleson). [](#cor:tight-window-consumption) and [](#lem:half) then give KLS. (iii) [](#prop:two-tail) rules out proving the unweighted estimate slice by slice.

**Scope and regularity.** Let $(\mu_t)_{t\geq0}$ be Eldan's stochastic-localization posterior started from a log-concave probability measure $\mu$ on $\mathbb R^n$. We use

$$
F_t(x)=\frac{\dd\mu_t}{\dd\mu}(x),\qquad
\dd F_t(x)=F_t(x)(x-a_t)\mathbin\cdot\dd W_t,
\qquad a_t=\int x\,\dd\mu_t(x).
$$

For a Borel set $E$ and $r>0$, put

$$
E_r=\{x\in\mathbb R^n:\operatorname{dist}(x,E)<r\},
$$

and use the lower outer Minkowski convention of the manuscript,

```{math}
:label: eq:sol-minkowski-perimeter
P_t(E)=\mu_t^+(E)
:=\liminf_{r\downarrow0}\frac{\mu_t(E_r)-\mu_t(E)}r.
```

We also write

$$
p_t=\mu_t(E),\qquad
e_t(E)=P_t(E)-I_{\mu_t}(p_t).
$$

The general fixed-cut result below assumes $P_0(E)<\infty$ and uses only bounded-test mass martingales. The stronger martingale identity is stated separately in the compact-support smooth regularity class: the initial density is smooth and compactly supported and $E$ has a $C^2$ boundary with a tubular neighborhood over the support of the density, so the one-sided tube formula identifies [](#eq:sol-minkowski-perimeter) with weighted surface area. No rough-set approximation or identification of inequivalent perimeter conventions is used.

## 1\. Perimeter under localization

:::{prf:lemma} Perimeter martingale; [](#lem:perimeter-martingale)
:label: lem:sol-perimeter-martingale
For every Borel set $E$ with $P_0(E)<\infty$, the lower Minkowski perimeter process is an integrable nonnegative supermartingale:

```{math}
:label: eq:sol-perimeter-supermartingale
\mathbb E[P_t(E)\mid\mathcal F_s]\leq P_s(E),\qquad 0\leq s\leq t.
```

In the compact-support smooth regularity class specified above, $P_t(E)$ is instead a true martingale and

```{math}
:label: eq:sol-perimeter-sde
\dd P_t(E)
=\left(\int_{\partial^*E}(x-a_t)\,\dd\sigma_t(x)\right)\mathbin\cdot\dd W_t,
```

where $\sigma_t$ is the weighted surface measure of $\mu_t$ on $\partial^*E$. Thus its drift vanishes identically and $\mathbb E P_t(E)=P_0(E)$.
:::

:::{prf:proof}
We first prove the general lower-Minkowski assertion directly. For $q\in\mathbb Q_{>0}$ define

$$
X_{q,t}=\frac{\mu_t(E_q)-\mu_t(E)}q
=\frac{\mu_t(E_q\setminus E)}q.
$$

For each fixed $q$, this is $q^{-1}$ times the mass of a fixed Borel set. The bounded-test localization identity [](#eq:loc-martingale) therefore makes $(X_{q,t})_{t\geq0}$ a bounded, nonnegative true martingale. For $n\geq1$ let

$$
Y_{n,t}=\inf\{X_{q,t}:q\in\mathbb Q,\ 0<q<1/n\}.
$$

The infimum is over a nonempty countable fixed family. For every admissible $q$ and $0\leq s\leq t$,

$$
\mathbb E[Y_{n,t}\mid\mathcal F_s]
\leq\mathbb E[X_{q,t}\mid\mathcal F_s]=X_{q,s}.
$$

Because there are only countably many $q$, the inequalities may be realized on one common full-probability set. Infimizing there gives

```{math}
:label: eq:sol-boundary-layer-supermartingale
\mathbb E[Y_{n,t}\mid\mathcal F_s]\leq Y_{n,s}.
```

Also $0\leq Y_{n,t}\leq X_{q_n,t}$ for any one admissible rational $q_n$, so $Y_{n,t}$ is integrable.

For any probability measure $\nu$, the map $r\mapsto\nu(E_r\setminus E)$ is continuous from below: if $q_k\uparrow r$, then $E_{q_k}\setminus E\uparrow E_r\setminus E$. Approximating every real $r>0$ from below by rationals consequently shows that the infimum over rational $q\in(0,1/n)$ equals the infimum over all real $r\in(0,1/n)$. Hence, pathwise,

```{math}
:label: eq:sol-boundary-layer-limit
Y_{n,t}\uparrow
\liminf_{r\downarrow0}\frac{\mu_t(E_r)-\mu_t(E)}r=P_t(E).
```

Ordinary monotone convergence and [](#eq:sol-boundary-layer-supermartingale) with $s=0$ give

$$
\mathbb E P_t(E)
=\lim_n\mathbb E Y_{n,t}
\leq\lim_nY_{n,0}=P_0(E)<\infty.
$$

Thus $P_t(E)$ is integrable. Conditional monotone convergence in [](#eq:sol-boundary-layer-supermartingale) now yields

$$
\mathbb E[P_t(E)\mid\mathcal F_s]
=\lim_n\mathbb E[Y_{n,t}\mid\mathcal F_s]
\leq\lim_nY_{n,s}=P_s(E),
$$

which proves [](#eq:sol-perimeter-supermartingale) for arbitrary support and without a rough-set approximation.

It remains to prove the stronger statement in the compact-support smooth class, using the same Minkowski convention. Let $w_0$ be the smooth compactly supported density of $\mu$ and put $\dd\sigma_0=w_0\,\dd\mathcal H^{n-1}|_{\partial^*E}$. The one-sided tubular-neighborhood formula for a smooth boundary and the continuous density $w_t=F_tw_0$ gives, for every fixed $t$ and sample path,

```{math}
:label: eq:sol-perimeter-representation
P_t(E)=\int_{\partial^*E}F_t(x)\,\dd\sigma_0(x),
\qquad
\dd\sigma_t(x)=F_t(x)\,\dd\sigma_0(x).
```

Indeed, in outward normal coordinates the Jacobian is $1+O(r)$ and $w_t(x+r\mathbf n_x)\to w_t(x)$, so division of the boundary-layer integral by its thickness and dominated convergence gives the displayed surface integral. Thus [](#eq:sol-perimeter-representation) is precisely the lower Minkowski perimeter [](#eq:sol-minkowski-perimeter), not a change of convention. Its initial surface measure is finite.

Let $K$ contain the support of $\mu$ and set $D=\operatorname{diam}K$. Both $x$ and $a_u$ belong to the convex hull of $K$ for $\sigma_0$-almost every $x$, so $|x-a_u|\leq D$. For fixed $x$, let $\rho_m\uparrow\infty$ localize the stochastic integral in the pointwise SDE and apply Itô's formula to $F_{u\wedge\rho_m}(x)^2$. Taking expectations gives

$$
\mathbb E F_{u\wedge\rho_m}(x)^2
\leq 1+D^2\int_0^u\mathbb E F_{v\wedge\rho_m}(x)^2\,\dd v.
$$

Gronwall and then Fatou as $m\uparrow\infty$ give

```{math}
:label: eq:sol-density-L2
\mathbb E F_u(x)^2\leq \exp(D^2u).
```

Consequently, for every finite $T$,

$$
\begin{aligned}
\mathbb E\int_0^T\int_{\partial^*E}
|F_u(x)(x-a_u)|^2\,\dd\sigma_0(x)\,\dd u
&\leq D^2\sigma_0(\partial^*E)\int_0^T e^{D^2u}\,\dd u<\infty.
\end{aligned}
$$

Since $\sigma_0$ is finite, Cauchy–Schwarz also gives

$$
\mathbb E\int_0^T
\left|\int_{\partial^*E}F_u(x)(x-a_u)\,\dd\sigma_0(x)\right|^2\dd u<\infty.
$$

These are pre-interchange stochastic-Fubini bounds. Stochastic Fubini applied to the pointwise density SDE therefore proves [](#eq:sol-perimeter-sde); $F_t\,\dd\sigma_0=\dd\sigma_t$ gives its displayed coefficient.

Finally, the same bound (or Novikov directly) makes every fixed-$x$ process $F_t(x)$ a true martingale on bounded intervals. Conditional Tonelli in [](#eq:sol-perimeter-representation) gives

$$
\mathbb E[P_t(E)\mid\mathcal F_s]
=\int_{\partial^*E}\mathbb E[F_t(x)\mid\mathcal F_s]\,\dd\sigma_0(x)
=P_s(E).
$$

Thus the smooth compact-support lower Minkowski perimeter is a true martingale with the stated SDE.
:::

## 2\. The unconditional excess bound and the exact identity

:::{prf:proposition} Unconditional integrated excess; [](#prop:trivial-excess)
:label: prop:sol-trivial-excess
Let $\mu$ be isotropic and log-concave, let $E$ be Borel with $\mu(E)=1/2$ and $P_0(E)<\infty$, and put $e_0=P_0(E)-I_\mu(1/2)$. For every $T>0$ and every stopping time $\tau$,

```{math}
:label: eq:sol-trivial-excess
\mathbb E\int_0^{T\wedge\tau}e_t(E)\,\dd t\leq(1+e_0)T.
```
:::

:::{prf:proof}
The profile is nonnegative, so $0\leq e_t(E)\leq P_t(E)$ pathwise. Consequently, Tonelli and [](#eq:sol-perimeter-supermartingale) give

$$
\mathbb E\int_0^{T\wedge\tau}e_t(E)\,\dd t
=\int_0^T\mathbb E[\mathbf 1_{\{t<\tau\}}e_t(E)]\,\dd t
\leq\int_0^T\mathbb E P_t(E)\,\dd t
\leq T P_0(E).
$$

This calculation uses neither optional stopping nor independence of $\tau$; only the deterministic-time supermartingale bound is used.

To bound $P_0(E)$, take a coordinate marginal of $\mu$. It is a one-dimensional log-concave law $\nu$ of variance one. If $f$ is its density and $m$ a median, the coordinate halfspace $H=\{x:x_1\leq m\}$ has $\mu(H)=1/2$ and $\mu^+(H)=f(m)$. Bobkov's one-dimensional isoperimetric identity and variance estimate [@Bobkov1999LogConcave, Proposition 4.1 and (4.2)] give $\operatorname{Is}(\nu)=2f(m)$ and $\operatorname{Is}(\nu)^2\leq2/\operatorname{Var}_\nu(X)$, hence $I_\mu(1/2)\leq f(m)\leq1/\sqrt2<1$. Therefore $P_0(E)=I_\mu(1/2)+e_0\leq1+e_0$, proving [](#eq:sol-trivial-excess).
:::

:::{prf:lemma} Exact excess identity; [](#lem:excess-identity)
:label: lem:sol-excess-identity
Under the compact-support smooth regularity hypotheses of [](#lem:sol-perimeter-martingale), for every finite $t\geq0$,

```{math}
:label: eq:sol-excess-identity
\mathbb E e_t(E)
=e_0(E)+I_\mu(p_0)-\mathbb E I_{\mu_t}(p_t).
```
:::

:::{prf:proof}
All quantities are nonnegative and integrable in the compact-support class. By definition,

$$
\mathbb E e_t(E)=\mathbb E P_t(E)-\mathbb E I_{\mu_t}(p_t).
$$

[](#lem:sol-perimeter-martingale) gives $\mathbb E P_t(E)=P_0(E)$, while $P_0(E)=I_\mu(p_0)+e_0(E)$. Substitution proves [](#eq:sol-excess-identity). Compact support is essential for the equality used here: the noncompact argument above supplies only $\mathbb E P_t(E)\leq P_0(E)$.
:::

## 3\. What a countable infimum of fixed-cut perimeter supermartingales implies

:::{prf:lemma} Fixed competitor families; [](#lem:inf-martingales)
:label: lem:sol-inf-martingales
Let $\mathfrak S$ be a fixed nonempty countable family of Borel sets of finite initial lower Minkowski perimeter and define $J_t=\inf_{S\in\mathfrak S}P_t(S)$. Then $J$ is a supermartingale. The same conclusion holds when a prescribed uncountable family has a fixed nonempty countable determining subfamily $\mathfrak S_0$ satisfying $\inf_{S\in\mathfrak S}P_t(S)=\inf_{S\in\mathfrak S_0}P_t(S)$ almost surely at every time under consideration; in that case $J$ means the latter countable infimum. On $\{t<\tau_\eta\}$ one has the pointwise comparison

```{math}
:label: eq:sol-window-infimum
I_{\mu_t}(p_t)\geq J_t(\eta),
\qquad
J_t(\eta)=\inf\{P_t(S):\mu_t(S)\in[1/2-\eta,1/2+\eta]\}.
```

The family in the last infimum depends on $(t,\omega)$; the first assertion therefore does not say that $J_t(\eta)$ or $I_{\mu_t}(p_t)$ is a supermartingale.
:::

:::{prf:proof}
Fix $0\leq s\leq t$. For every $S\in\mathfrak S$, $J_t\leq P_t(S)$, hence by monotonicity of conditional expectation and the noncompact part of [](#lem:sol-perimeter-martingale),

$$
\mathbb E[J_t\mid\mathcal F_s]
\leq\mathbb E[P_t(S)\mid\mathcal F_s]
\leq P_s(S).
$$

Taking the infimum in $S$ on the right gives $\mathbb E[J_t\mid\mathcal F_s]\leq J_s$. This argument needs only that each fixed-cut perimeter is a supermartingale; in the compact-support class the second inequality happens to be an equality. Moreover, choosing one $S_\star\in\mathfrak S$ gives $0\leq J_t\leq P_t(S_\star)$ and $\mathbb E P_t(S_\star)\leq P_0(S_\star)<\infty$, so $J_t$ is integrable. The determining-subfamily variant is exactly the same countable argument. No conclusion is claimed for a raw uncountable pointwise infimum merely assumed measurable.

On $\{t<\tau_\eta\}$, $p_t\in[1/2-\eta,1/2+\eta]$. Thus the exact-mass competitor class $\{S:\mu_t(S)=p_t\}$ is contained in the windowed class in [](#eq:sol-window-infimum). The infimum over the smaller class is at least the infimum over the larger one, proving the pointwise comparison. But eligibility for the windowed class is the random condition $\mu_t(S)\in[1/2-\eta,1/2+\eta]$; it is not a fixed family to which the conditional-expectation argument can be applied.
:::

## 4\. Consumption audit

:::{prf:proposition} Consumption audit; [](#prop:intro-audit)
:label: prop:sol-intro-audit
The following three assertions hold.

1. For every isotropic log-concave $\mu$, every Borel $E$ with $\mu(E)=1/2$ and $P_0(E)<\infty$, every $T>0$, and every stopping time $\tau$,

   $$
   \mathbb E\int_0^{T\wedge\tau}e_t(E)\,\dd t\leq(1+e_0)T.
   $$

2. Replace the covariance weight in the stable Stein-trace estimate by $1$, keeping its fixed tight window and absorption margin. Then this unweighted estimate, without any separate excess-propagation hypothesis, implies KLS.

3. There are log-concave pairs $(\nu,E)$ with $\nu(E)=1/2$, $r=D=0$, $e(E)\to0$, and $\mathcal S_\nu(E)/s\to\infty$. Hence the unweighted estimate cannot be proved by a universal one-time-slice inequality of the asserted form.
:::

:::{prf:proof}
The first assertion is [](#prop:sol-trivial-excess).

For the second, spell out exactly what is consumed. Fix a universal $\eta\in(0,1/6]$ and constants $C_0,C_1,C_2$, $\beta\geq0$ satisfying $2\beta+64\eta^2<1$. The unweighted stable Stein-trace estimate is

```{math}
:label: eq:sol-unweighted-stein
\begin{split}
\mathbb E\int_0^{T\wedge\tau_\eta}
\frac{\mathcal S_{\mu_t}(E)}{s_t}\,\dd t
\leq{}&C_0T+C_1\mathbb E\int_0^{T\wedge\tau_\eta}r_t\,\dd t
+\beta\mathbb E\int_0^{T\wedge\tau_\eta}D_t\,\dd t\\
&+C_2\mathbb E\int_0^{T\wedge\tau_\eta}e_t(E)\,\dd t .
\end{split}
```

The exact tight-window Stein/source conversion ([](#lem:stein-vs-source)) is

$$
\mathbb E\int_0^{T\wedge\tau_\eta}S_t\,\dd t
\leq2\mathbb E\int_0^{T\wedge\tau_\eta}
\frac{\mathcal S_{\mu_t}(E)}{s_t}\,\dd t
+64\eta^2\mathbb E\int_0^{T\wedge\tau_\eta}D_t\,\dd t.
$$

For the near-Cheeger cuts used in the contradiction argument, take $e_0\leq1$. Applying the first assertion to [](#eq:sol-unweighted-stein) gives

```{math}
:label: eq:sol-absorptive-carleson
\begin{split}
\mathbb E\int_0^{T\wedge\tau_\eta}S_t\,\dd t
\leq{}&(2C_0+4C_2)T
+2C_1\mathbb E\int_0^{T\wedge\tau_\eta}r_t\,\dd t\\
&+(2\beta+64\eta^2)
\mathbb E\int_0^{T\wedge\tau_\eta}D_t\,\dd t.
\end{split}
```

This is precisely an absorptive tight-window two-color Carleson estimate, with damping coefficient strictly below one. [](#cor:tight-window-consumption) then gives a positive universal boundary lower bound for every balanced near-Cheeger cut to which [](#eq:sol-unweighted-stein) applies.

For completeness, if KLS failed, there would be isotropic log-concave $\mu_k$ with $h_{\mu_k}\to0$. The balanced characterization from [](#lem:half), $h_\nu=2I_\nu(1/2)$, permits choices of sets $E_k$ of mass $1/2$ with $P_0(E_k)\leq I_{\mu_k}(1/2)+o(1)$. Thus $P_0(E_k)\to0$ and $e_0(E_k)\leq1$ for all large $k$, whereas [](#eq:sol-absorptive-carleson) and tight-window consumption give a uniform positive lower bound for the same perimeters, a contradiction. No weighted excess estimate was used.

The third assertion is exactly the certified anisotropic two-tail construction of [](#prop:two-tail): it has $r=D=0$, vanishing absolute excess, and divergent $\mathcal S/s$. A slice-wise version of [](#eq:sol-unweighted-stein) would have a uniformly bounded right-hand side on that family and a divergent left-hand side. This disproves that slice-wise route while making no claim against nonlocal-in-time proofs or the covariance-weighted formulation.
:::

**Obstructions respected.** No node in this dossier has a ledger `bounded_by` edge. Nevertheless, [](#lem:sol-excess-identity) and [](#lem:sol-inf-martingales) explicitly preserve the content of `obs:circularity`: the exact identity is restricted to compact support, and no supermartingale property is inferred for the random time-dependent balanced-profile infimum. [](#prop:sol-intro-audit) uses the separate two-tail obstruction only to refute a slice-wise unweighted estimate; it does not promote numerical or directional evidence to proof.
