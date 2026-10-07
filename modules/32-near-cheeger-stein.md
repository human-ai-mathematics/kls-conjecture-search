---
numbering:
  enumerator: "32.%s"
---

(sec:stein)=
# The fixed cut: the near-Cheeger variant

Part of the fixed-cut archive (Chapter [](#sec:introduction)); this chapter holds the near-Cheeger variant: the Stein dictionary that rewrites the two-color source as a covariance contrast and as a boundary flux (Section [](#sec:stein-dictionary)), the argument for [](#thm:intro-weighted) (Section [](#subsec:consumption)), and the excess bounds and circularity warning that shaped the variant (Section [](#sec:excess)).

The near-Cheeger variant trades the all-cut hypothesis for near-minimality. Its stochastic currency is the two-color covariance functional $\calS_\nu(E)=s^2\norm K_\HS^2$; the conversion between this functional and the Riccati source ([](#lem:stein-vs-source)) is lossless on the tight window.

(sec:stein-dictionary)=
## The Stein dictionary

Both variants of the fixed cut use the same covariance contrast of a cut, in two normalizations. This section records the exact algebraic dictionary relating that contrast to the Riccati source of Chapter [](#sec:riccati), and isolates the exact gap of the all-cut variant, which is also the covariance contrast the Reilly–Jacobi mechanism of Chapter [](#sec:jacobi) would have to control. No argument in this manuscript connects Jacobi/Reilly boundary modes to this trace ([](#conj:almost-stability-gap)).

(subsec:one-gap)=
### The operator-to-trace gap

The per-direction Carleson estimate ([](#cor:per-direction)) is the unconditional budget on the two-color source: with the occupation operator

$$
\calM:=\E\int_0^\infty s_tG_t^2\dd t,
$$

estimate [](#eq:loewner-carleson) reads $\calM\preceq R_0\preceq I_n$, a dimension-free bound at the level of quadratic forms. The KLS-strength statement of the all-cut variant is the *trace* $\Tr(\calM)$, whose only a priori bound is $\Tr R_0\le n$. The entire difficulty of the all-cut approach is this operator-to-trace upgrade. In the product model, [](#conj:product-alignment) isolates its incident-high residue; it is not an equivalent reformulation of the full trace target. The weighted Stein-trace estimate of the near-Cheeger variant ([](#conj:stein-weighted)) faces analogous high-rank boundary modes, but the claimed identification with this occupation operator awaits the almost-stability trace bridge of [](#conj:almost-stability-gap). The available product argument does not prove a static effective-rank bound: summing its coordinate budgets loses a factor $n$, whereas the dimension-dependent early-window estimate follows independently from covariance moments. This motivates an occupation-density bound forcing only $O(1)$ directions to be simultaneously active on the early balanced window; no such temporal sparsity is proved. This is the content of [](#rem:trace-upgrade-unification). The dictionary below is the change of variables tying the exact Riccati and Stein formulations together and supplying the common covariance currency for the Reilly–Jacobi mechanism.

### The two-color Stein representation

:::{prf:proposition} Two-color Stein representation
:label: prop:stein-rep
Let $\nu$ be a probability measure on $\R^n$ with finite fourth moment, mean $a$, covariance $A$, $E$ measurable, $p=\nu(E)\in(0,1)$, and let $\delta,G,K=G+(q-p)\delta\delta^T$ be the two-color quantities of Chapter [](#sec:notation). For a symmetric matrix $M$ set

$$
f_M(x)=(x-a)^TM(x-a)-\Tr(MA).
$$

Then

```{math}
:label: eq:stein-rep
\ell_{\nu,E}(M):=\int_E f_M\dd\nu
=\Cov_\nu\bigl(\one_E,\;(x-a)^TM(x-a)\bigr)
\;=\;s\bigl(\inner GM+(q-p)\,\delta^TM\delta\bigr)
\;=\;s\,\inner{K}{M}.
```

Consequently the *Stein-trace norm*

```{math}
:label: eq:stein-norm-def
\calS_\nu(E):=\sup_{\norm M_\HS\le1}\abs{\ell_{\nu,E}(M)}^2
\;=\;s^2\,\norm{K}_\HS^2 ,
```

and the functional used by the fixed-cut argument is $\calS_\nu(E)/s=s\norm K_\HS^2$. At balance $K=G$, so this equals the Riccati source $S=s\norm G_\HS^2$; off balance the two quantities are related, rather than identified, by [](#lem:stein-vs-source).
:::

:::{prf:proof}
Write $m^E,m^F,\Sigma^E,\Sigma^F$ for the conditional means and covariances, so that $p(m^E-a)+q(m^F-a)=0$ and, by the covariance decomposition [](#eq:cov-decomp), $A=p\Sigma^E+q\Sigma^F+s\,\delta\delta^T$. Then

$$
\int_E f_M\dd\nu
=p\,\inner{M}{\Sigma^E+(m^E-a)(m^E-a)^T-A} .
$$

Now $\Sigma^E-A=q(\Sigma^E-\Sigma^F)-s\delta\delta^T=qG-s\delta\delta^T$ and, since $m^E-a=q\delta$, $(m^E-a)(m^E-a)^T=q^2\delta\delta^T$. Hence

$$
\int_E f_M\dd\nu
=p\inner{M}{qG+(q^2-pq)\delta\delta^T}
=s\inner{M}{G+(q-p)\delta\delta^T}=s\inner KM ,
$$

where we used $pq^2-p^2q=pq(q-p)$. The supremum over $\norm M_\HS\le1$ of the linear functional $M\mapsto s\inner KM$ is $s\norm K_\HS$, giving [](#eq:stein-norm-def).
:::

:::{prf:remark}
The identity $\calS_\nu(E)=s^2\norm K_\HS^2$ is a small but clarifying consolidation. The “Stein” functional is the squared norm of the translation-invariant contrast $K$, whereas the Riccati source uses $G$. They coincide at balance; away from balance their difference is the explicit damping term $(q-p)\delta\delta^T$. Thus the all-cut and near-Cheeger variants exchange comparable, not identical, currency on the tight window, with the universal conversion constants below.
:::

:::{prf:lemma} Conversion between Stein norm and Riccati source on the tight window
:label: lem:stein-vs-source
For $0<\eta\le\tfrac14$, on the event $\{t<\tau_\eta\}$, with $S_t=s_t\norm{G_t}_\HS^2$ and $D_t\ge r_t^2$ as in [](#eq:D-ge-r2),

```{math}
:label: eq:conversion
S_t\;\le\;2\,\frac{\calS_{\mu_t}(E)}{s_t}+64\,\eta^2 D_t,
\qquad
\frac{\calS_{\mu_t}(E)}{s_t}\;\le\;2\,S_t+64\,\eta^2 D_t .
```
:::

:::{prf:proof}
On the tight window $\abs{p_t-\tfrac12}\le\eta$, so $\abs{q_t-p_t}\le2\eta$ and $s_t\ge\tfrac14-\eta^2\ge\tfrac3{16}$ for $\eta\le\tfrac14$; we only use $s_t\ge\tfrac14\cdot (1-4\eta^2)\ge\tfrac1{4}\cdot\tfrac34$, and in fact only $r_t^2/s_t\le 8r_t^2$, valid for $s_t\ge\tfrac18$. From $G=K-(q-p)\delta\delta^T$,

$$
s\norm G_\HS^2\le2s\norm K_\HS^2+2s(q-p)^2\abs\delta^4
\le2\,\frac{\calS}{s}+8\eta^2\,\frac{r^2}{s}
\le2\,\frac{\calS}{s}+64\eta^2r^2 ,
$$

and $r^2\le D$ by [](#eq:D-ge-r2). The reverse inequality is identical with the roles of $G$ and $K$ exchanged.
:::

## The boundary representation and the trace estimate

The name “Stein trace” refers to the second exact form of $\ell_{\nu,E}$, as a boundary flux.

:::{prf:lemma} Boundary representation
:label: lem:boundary-rep
Let $K$ be a smooth bounded convex domain and $\nu=Z^{-1}e^{-V}\one_Kdx$, with $V$ smooth and convex on $\overline K$. Let $E$ be smooth relative to $K$, put $\Sigma=\partial^*E\cap\operatorname{int}K$, and let $n$ be its inner unit normal. For smooth $f$ with $\nu$-mean $\bar f$, let $u_f$ be the mean-zero weak solution of the Neumann Poisson problem

$$
Lu_f=f-\bar f\quad\text{in }K,
\qquad \partial_{n_K}u_f=0\quad\text{on }\partial K,
\qquad L=\Delta-\nabla V\cdot\nabla .
$$

Then

```{math}
:label: eq:boundary-rep
\Cov_\nu(\one_E,f)
=\int_E(f-\bar f)\dd\nu
=-\int_\Sigma \partial_nu_f\dd\sigma_\nu ,
```

and in particular, by Cauchy–Schwarz on the weighted surface measure of total mass $\nu^+(E)$,

```{math}
:label: eq:trace-CS
\abs{\ell_{\nu,E}(M)}^2
\;\le\;\nu^+(E)\,\int_\Sigma\abs{\partial_nu_{M}}^2\dd\sigma_\nu ,
\qquad u_M:=u_{f_M} .
```

Here $f_M(x)=(x-a_\nu)^TM(x-a_\nu)-\Tr(MA_\nu)$ is the centered quadratic from [](#prop:stein-rep).
:::

:::{prf:proof}
$\int_E(f-\bar f)\dd\nu=Z^{-1}\int_E\operatorname{div}(e^{-V}\nabla u_f)dx$. The divergence theorem on $E\cap K$ gives the displayed flux on $\Sigma$ with the inner normal; the contribution on $\partial K\cap E$ vanishes by the Neumann condition. Existence and uniqueness up to constants are the standard centered Neumann problem on the smooth bounded weighted domain; the mean-zero normalization fixes the constant.
:::

:::{prf:remark} What the stable Stein-trace estimate is
:label: rem:what-stein-is
Estimate [](#eq:intro-weighted-stein) is, through [](#eq:stein-norm-def)–[](#eq:trace-CS), a *trace estimate for Poisson solutions with quadratic data*, integrated along the localization and tested against near-minimal cuts: the boundary energy $\int_\Sigma\abs{\partial_nu_M}^2\dd\sigma_\nu$ must, after absorption of the damped modes, be controlled at the Carleson scale. The natural tool for converting boundary traces into interior energies is the weighted Reilly identity, and the natural geometric input for near-minimal $\Sigma$ is the second-variation stability of Chapter [](#sec:jacobi). Two warnings constrain any such proof: by [](#prop:two-tail) it cannot proceed one time-slice at a time with an absolute-scale excess term, and by [](#prop:intro-audit)(b) an absolute-scale excess term would carry no logical weight anyway. The covariance-weighted trace estimate [](#eq:intro-weighted-stein) remains a meaningful geometric target, but it is not by itself part of a working package: [](#prop:weighted-spectator-obstruction) shows that its paired global-operator-norm propagation clause fails on spectator products, while [](#prop:spectator-excess-rate-obstruction) rules out the same uniform superlinear remainder even at weight one. Any replacement must first choose a cut-local or tensor-stable scale and a surviving remainder or near-worst hypothesis, and then check the trace estimate against both.
:::

(subsec:consumption)=
## From the weighted package to KLS

:::{prf:proof} Proof of [](#thm:intro-weighted)
Assume the weighted package ([](#ass:weighted-package)). Thus its fixed tight-window parameter satisfies $2\beta+64\eta^2<1$. Suppose, for contradiction, that KLS fails, and let $(\mu_k,E_k)$ be a sequence of isotropic log-concave measures and balanced near-Cheeger cuts with $\mu_k^+(E_k)\to0$ and $e_0(E_k)\le1$; this is the near-minimizer reduction in the remark following [](#thm:centroid-implies-kls). Choose once and for all $\alpha\in(2\beta+64\eta^2,1)$. In particular, the assumed value of $\eta$ is small enough for the tight-window conversion below; no stopping window is chosen after the two package estimates have been supplied.

By [](#lem:stein-vs-source) and the weighted Stein-trace estimate [](#eq:intro-weighted-stein),

$$
\begin{aligned}
\E\int_0^{T\wedge\tau_\eta}S_t\dd t
&\le2C_0T+2C_1\E\int_0^{T\wedge\tau_\eta}r_t\dd t \\
&\quad
+\bigl(2\beta+64\eta^2\bigr)\E\int_0^{T\wedge\tau_\eta}D_t\dd t \\
&\quad
+2C_2\,\E\int_0^{T\wedge\tau_\eta}
e_t\bigl(1+\norm{A_t}_\op\bigr)^{5/2}\dd t ,
\end{aligned}
$$

where the additional $64\eta^2D$ comes from the conversion. By weighted excess propagation [](#eq:intro-weighted-excess), the last term is at most $2C_2^2\bigl(Te_0+T^{1+\gamma}\bigr)\le2C_2^2(1+T^\gamma)\,T\le4C_2^2\,T$ for $T\le T_0\wedge1$. This is an absorptive two-color Carleson estimate on the tight window with universal constants $C_0'=2C_0+4C_2^2$, $C_1'=2C_1$ and damping coefficient $\alpha<1$, on the tight window from time zero. Since $\eta$ was fixed above (universally, with $\eta<\tfrac16$), this is exactly the hypothesis [](#eq:tight-carleson) of [](#cor:tight-window-consumption), applied to each $(\mu_k,E_k)$ (which has $p_0=\tfrac12$). It produces a universal constant $c'>0$ with $\mu_k^+(E_k)\ge c'$ for all $k$, contradicting $\mu_k^+(E_k)\to0$. Hence $\inf_n\hstar_n>0$.
:::

:::{prf:remark}
The proof shows that the only place the excess enters the argument is through the single scalar $\E\int e_t(1+\norm{A_t}_\op)^{5/2}\dd t$, and that any bound of size $O(T)$ for it, with universal constant, suffices. The stronger $T^{1+\gamma}$ remainder in [](#eq:intro-weighted-excess) is not needed for the argument, and the literal uniform hypothesis fails on spectator products ([](#prop:weighted-spectator-obstruction)). The unweighted spectator obstruction ([](#prop:spectator-excess-rate-obstruction)) shows that merely replacing the covariance weight does not rescue that remainder. A replacement may instead allow an $O(T)$ supply tied to a near-worst hypothesis, or use a remainder that vanishes with a genuinely cut-local source deficit; either choice requires checking again, as in [](#prop:intro-audit), which terms carry logical weight.
:::

(sec:excess)=
## Excess propagation

This section proves [](#prop:intro-audit), which shows that the unweighted excess term is inert, and explains why a direct propagation argument can merely restate a localized isoperimetric lower bound, motivating the bootstrap mechanism of Chapter [](#sec:bootstrap). This is a methodological warning, not a no-go theorem. The static obstruction that forces the covariance weight ([](#prop:two-tail)) is established in Chapter [](#sec:qcts).

### The unweighted excess term is inert

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
(a) is [](#prop:trivial-excess). (b): run the proof of [](#thm:intro-weighted) in Section [](#subsec:consumption) with the weight replaced by $1$ and the weighted excess propagation input replaced by [](#eq:trivial-excess); every step goes through with the universal constant $C_0'=2C_0+2C_2(1+e_0)\le2C_0+4C_2$ for $e_0\le1$. Thus [](#cor:tight-window-consumption) gives a universal positive boundary lower bound for every balanced near-Cheeger cut to which the estimate applies. If KLS failed, [](#lem:half) would provide isotropic log-concave $\mu_k$ and balanced cuts $E_k$ with $\mu_k^+(E_k)\to0$ and $e_0(E_k)\le1$ for all large $k$, contradicting that lower bound. Hence KLS follows. (c) is [](#prop:two-tail) of Chapter [](#sec:qcts).
:::

:::{prf:remark} Why the inert excess term matters
:label: rem:audit-interpretation
Item (b) is not good news about excess propagation; it is a diagnosis of the previously stated package. An additive excess term whose integral is a priori $O(T)$ is inert next to the $C_0T$ term: it can be deleted without changing the strength of the assumption, so the unweighted Stein-trace estimate silently carried the entire logical weight of the package. Item (c) shows this weight cannot be discharged slice-wise. The weighted restatement ([](#ass:weighted-package)) was a proposed repair: it made the excess term non-inert and passed the static two-tail calibration. [](#prop:weighted-spectator-obstruction) shows that its global-operator-norm propagation clause fails, because that weight responds to independent spectator coordinates. [](#prop:spectator-excess-rate-obstruction) further shows that a tensor-stable replacement weight alone is insufficient: the uniform superlinear remainder already fails with weight one. A viable replacement must also allow an $O(T)$ scale, use a genuinely source-tied remainder, or assume near-worstness. Other proof architectures need not use this decomposition.
:::

(subsec:circularity)=
### Why direct propagation risks circularity

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
Within the smooth compact-support class of [](#lem:excess-identity), excess propagation is equivalent to a lower bound on $\E I_{\mu_t}(p_t)$. Such a lower bound is itself a Cheeger-type statement for the random posterior, so an argument that simply inserts a lower bound for the localized profile risks assuming the phenomenon the argument is meant to prove. [](#lem:inf-martingales) supplies no monotonicity for that profile, because the mass-constrained competitor family changes with time. Thus “direct propagation is circular” should be read as a proof-design warning, not a formal impossibility result: additional structure could conceivably control the moving infimum. The external worst-case constant $\hstar_n$ of [](#eq:hstar-def) provides one demonstrably non-circular anchor in a contradiction argument; Chapter [](#sec:bootstrap) develops that bootstrap without claiming it is the only possible anchor.
:::

(subsec:excess-barriers)=
### Methodological constraints from this section

:::{prf:remark} Localized profile insertion may assume the target
:label: rem:profile-circularity
Excess propagation requires a lower bound on the expected isoperimetric profile of the random posterior. The supermartingale statement available here, [](#lem:excess-identity) together with [](#lem:inf-martingales) and [](#rem:circularity), applies only to a *fixed* competitor family, whereas the balanced family changes with time. Directly inserting a lower bound for the time-dependent localized profile therefore risks assuming the Cheeger control that excess propagation is meant to prove; a proof must supply additional structure or an external non-circular anchor.
:::
