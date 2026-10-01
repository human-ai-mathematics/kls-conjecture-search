---
numbering:
  enumerator: "27.%s"
---

(sec:open)=
# The fixed cut: the remaining problems

What remains of the fixed-cut approach is a small set of precise problems, together with the obstructions that shaped them. We state the problems in decreasing order of strength.

:::{prf:conjecture} Operator-to-trace upgrade; tight-prefix Carleson
:label: conj:trace-upgrade
[](#ass:tight-prefix-carleson) holds: the unconditional per-direction Carleson estimate ([](#cor:per-direction)) upgrades to the trace scale, uniformly over fixed initially balanced cuts and prefixes from time zero, with damping coefficient $\alpha<1$.
:::

By [](#cor:tight-window-consumption), this prefix form on the tight window is exactly what the argument consumes; the stronger every-interval estimate [](#ass:all-cut-carleson) is not required. The projection-test ceiling of Section [](#sec:qcts) ([](#rem:projection-ceiling)) bears on the obvious proof method, although Letwin's moment-map argument bypasses it for the intrinsic static quadratic chaos. A proof of the dynamic upgrade must therefore use cut-specific structure and covariance occupation. Its restriction to products is examined in [](#rem:product-stress-test); a family of product cuts violating the prefix form for every choice of constants would refute it.

:::{prf:lemma} Scale-weighted all-cut source budget
:label: lem:time-weighted-source
For every isotropic log-concave initial law, every fixed measurable cut $E$ with $0<\mu(E)<1$, and every $T>0$, the two-color localization quantities satisfy

```{math}
:label: eq:time-weighted-source
\E\int_0^T t^2\bigl(S_t+r_t^2\bigr)\dd t
\le T^2\E r_T\le T.
```

Consequently, the same upper bound holds after restricting the nonnegative integrand to any balanced stopped window. This statement does not remove the quadratic time weight at the initial endpoint.
:::

:::{prf:lemma} One-dimensional density–variance bound
:label: lem:one-dimensional-density-variance
By [@BobkovChistyakov2015Concentration, Prop. 2.1], if a one-dimensional log-concave probability density $f$ has variance $v>0$, then

$$
\frac1{12}\le v\norm{f}_\infty^2\le1.
$$

In particular, the boundary density of every quantile halfline is at most $v^{-1/2}$.
:::

:::{prf:proposition} Exponential-spectator obstruction to global weighted propagation
:label: prop:weighted-spectator-obstruction
For every proposed constants $C,T_0,\gamma>0$, every $\eta\in(0,1/2)$, and every $\delta>0$, there exist a dimension $d$, an isotropic product $\mu$ of $d$ centered one-sided exponentials, a finite-perimeter cylinder $E$ with $\mu(E)=1/2$,

$$
e_0(E)\le\delta,
\qquad
\frac{e_0(E)}{I_\mu(1/2)}\le\delta,
$$

and a time $0<T\le T_0$ such that

$$
\E\int_0^{T\wedge\tau_\eta}
e_t(E)\bigl(1+\norm{A_t}_\op\bigr)^{5/2}\dd t
>C\bigl(Te_0(E)+T^{1+\gamma}\bigr).
$$

This proves that the global operator-norm weight is unstable under independent spectators and that the literal rate in [](#conj:weighted-excess-rate) fails. All witness measures are products, which satisfy KLS by [](#prop:products).
:::

:::{prf:proposition} Spectator obstruction to a superlinear excess remainder
:label: prop:spectator-excess-rate-obstruction
For every proposed constants $C,T_0,\gamma>0$, every $\eta\in(0,1/2)$, and every $\delta>0$, there exist a dimension $d$, an isotropic product $\mu$ of $d$ centered one-sided exponentials, a finite-perimeter cylinder $E$ with $\mu(E)=1/2$,

$$
e_0(E)\le\delta,
\qquad
\frac{e_0(E)}{I_\mu(1/2)}\le\delta,
$$

and a time $0<T\le T_0$ such that

$$
\E\int_0^{T\wedge\tau_\eta}e_t(E)\dd t
>C\bigl(Te_0(E)+T^{1+\gamma}\bigr).
$$

Thus replacing the global operator-norm weight by a tensor-stable or cut-local weight is not by itself enough to repair the current propagation gate: a surviving uniform statement must also allow an $O(T)$ remainder, make the remainder vanish with a source deficit, or impose an explicit near-worst-measure premise. The product witnesses satisfy KLS by [](#prop:products).
:::

:::{prf:conjecture} Global-operator-norm weighted excess rate
:label: conj:weighted-excess-rate
There exist universal $C,T_0,\gamma>0$ and $\eta\in(0,1/4]$ such that, for every isotropic log-concave law and every balanced finite-perimeter cut with $e_0(E)\le1$,

$$
\E\int_0^{T\wedge\tau_\eta}e_t(E)\,\bigl(1+\norm{A_t}_\op\bigr)^{5/2}\dd t
\ \le\ C\bigl(Te_0(E)+T^{1+\gamma}\bigr),\qquad T\le T_0 .
$$

This is exactly the weighted-excess component [](#eq:intro-weighted-excess) of [](#ass:weighted-package).
:::

Against this rate, [](#prop:weighted-spectator-obstruction) gives, for every proposed choice of constants, a product-cylinder witness with arbitrarily small additive and relative initial excess. Among pure powers of $\lmax(A_t)$ multiplying absolute excess in this slice-wise package, $5/2$ is the weakest exponent statically consistent with the two-tail mode ([](#prop:two-tail)); the time exponent was a deliberately stronger demand, not fixed by that static example. The near-worst bootstrap of [](#thm:bootstrap) supplies a different, externally anchored unweighted interface. It is not a uniform superlinear-remainder statement of the form above. [](#prop:spectator-excess-rate-obstruction) proves that the superlinear remainder already fails after the global covariance weight is removed. Thus changing only the weight cannot repair the uniform package: the replacement must also change the remainder or impose an explicit near-worst-measure premise.

A possible replacement interface, screened by the source, charges the weighted excess only on the aligned set $\mathcal A_{\kappa,t}=\{Q_t\ge\kappa\,e_tW_{\rm cut}\}$, where $Q_t=\calS_{\mu_t}(E)/s_t=s_t\norm{K_t}_{\HS}^2$ and $W_{\rm cut}=(1+\lambda_{\rm cut}(A_t,K_t))^{5/2}$ with the cut-oriented scale of [](#lem:lyapunov-stein-duality). Its first positive result, [](#prop:split-screened-supply) below, concerns the regular split class; general split laws are covered only through their regular approximants, because the interchange of the screened indicator with the approximation limit is not carried out.

% Agent note: isolated in the 2026-08-30 screened-interface probe; the limit interchange is
% recorded as open in the dossier of prop:split-screened-supply.

:::{prf:proposition} Split-class screened supply, total-budget form
:label: prop:split-screened-supply
Let $\mu$ be a product of isotropic one-dimensional log-concave laws, each compactly supported with smooth density, and let $E=E_J\times\R^{J^c}$ for a fixed coordinate set $J$ with $\abs J=k$, where $E_J\subset\R^J$ has $C^2$ relative boundary with a tubular neighbourhood over the support, and $0<p_0<1$. Then for every $\eta\in(0,1/4]$, every $\kappa>0$, and every $T>0$,

$$
\E\int_0^{T\wedge\tau_\eta}
e_t\,\bigl(1+\lambda_{\rm cut}(A_t,K_t)\bigr)^{5/2}
\mathbf 1_{\{Q_t\ge\kappa e_tW_{\rm cut}\}}\dd t
\ \le\ \frac{2k+64\eta^2(1+k)}{\kappa},
$$

uniformly in the ambient dimension and in every spectator coordinate. The bound is a total budget, not of the form $C(k)\,T$, and asserts nothing about the trace-upgrade cluster.
:::

:::{prf:conjecture} Weighted stable Stein-trace ingredient extracted from the literal package
:label: conj:stein-weighted
There exist universal constants $T_0,C_0,C_1,C_2>0$, $0\le\beta<\tfrac12$, and $\eta\in(0,\tfrac14]$ satisfying $2\beta+64\eta^2<1$ such that, for every isotropic log-concave law, every initial finite-perimeter cut $E$ with $e_0(E)\le1$ and $\abs{p_0-\tfrac12}\le\eta/2$, and every $0<T\le T_0$,

$$
\begin{aligned}
\E\int_0^{T\wedge\tau_\eta}\frac{\calS_{\mu_t}(E)}{s_t}\dd t
&\le C_0T+C_1\E\int_0^{T\wedge\tau_\eta}r_t\dd t
+\beta\E\int_0^{T\wedge\tau_\eta}D_t\dd t \\
&\qquad
+C_2\E\int_0^{T\wedge\tau_\eta}
e_t(E)\bigl(1+\norm{A_t}_\op\bigr)^{5/2}\dd t .
\end{aligned}
$$

This is exactly the stable Stein-trace clause of [](#ass:weighted-package), considered as an independent analytic ingredient.
:::

Taken alone, this clause neither repairs that package nor implies KLS: it needs a companion propagation statement that survives the spectator products. The intrinsic quadratic-chaos input is [](#thm:letwin-qcts). The mechanism of Section [](#sec:jacobi) needs in addition a localization-uniform quantitative almost-stability trace theorem for the fixed cut, modulo tangential Jacobi zero modes and with all Reilly boundary terms controlled ([](#conj:almost-stability-gap)). [](#prop:two-tail) rules out a slice-wise shortcut. No implication between this statement, [](#conj:trace-upgrade), and [](#conj:product-alignment) is asserted.

:::{prf:remark} A shared dynamic occupation problem, and a missing geometric bridge
:label: rem:trace-upgrade-unification
[](#conj:trace-upgrade) and [](#conj:stein-weighted) (its high-rank, mean-zero part) and the adapted alignment problem [](#conj:product-alignment) all confront a high-rank occupation difficulty, but no equivalence between them is asserted. Analytically, the gap of the all-cut variant is exactly the trace of the occupation operator $M:=\E\int_0^\infty s_t G_t^2\dd t$: [](#cor:per-direction) is the statement $M\preceq R_0\preceq I$ (the diagonal/quadratic-form level), and the trace target is $\Tr(M)$, whose naive bound $\sum_i(R_0)_{ii}=\Tr R_0\le n$ is the obstruction. Geometrically, the proposed Reilly/Jacobi approach aims to control analogous high-rank boundary modes, but [](#conj:almost-stability-gap) records the missing trace bridge; its proposed constant-mode branch is [](#conj:splitting). Combinatorially, summing the per-coordinate budgets of [](#thm:budget) over a product cut is again $\Tr R_0\le n$; this motivates the incident-high residue in [](#conj:product-alignment) but does not identify it with the full trace problem. The product budget argument supplies only the naive trace bound of order $n$, while the dimension-dependent early-window estimate follows separately from covariance moments ([](#thm:V2-window), conditional on the cited preprint at the $c/\log n$ scale). This motivates — but does not prove — an *occupation-density* bound: the source-occupation measure on time$\,\times\,$direction should have bounded density on the early balanced window, so that only $O(1)$ directions are simultaneously active. This is the form in which [](#conj:product-alignment) should be integrated against time.
:::

:::{prf:conjecture} Extremality tames the covariance process
:label: conj:taming
For every $\kappa\in(0,1]$ there exist $\eps>0$ and $T_0\in(0,1/8)$ such that every isotropic log-concave $\mu$ on $\R^n$ with $h_\mu\le(1+\eps)\hstar_n$ satisfies $h_\mu\bigl(T_0^{4/3}+\Xi_{T_0}(\mu)\bigr)\le\kappa\,T_0$. By [](#thm:bootstrap) this gives the absolute-scale supply $T_0e_0+C\kappa T_0$ for near-worst measures. At a sufficiently small universal time, the stronger, unweighted condition $\Xi_{T_0}\le\kappa T_0$ for every measure is already KLS-sufficient by [](#prop:ceiling); it is not the statement conjectured here. Heuristically, covariance inflation under localization is driven by third-moment anisotropy, while the splitting philosophy of Section [](#sec:jacobi) predicts that near-worst measures are approximately split along their dangerous directions, where the variance processes are one-dimensional and tame ([](#prop:products)(ii)); making this rigorous would couple the splitting analysis to the covariance SDE.
:::

:::{prf:remark} The naive splitting–covariance coupling faces a type mismatch
:label: rem:taming-type-mismatch
The coupling suggested above runs into a structural obstruction: $\Xi_T$ is a *cut-free* functional of the covariance process, whereas the splitting structure is *cut-indexed*. Product/splitting alone does not suppress coordinatewise covariance excursions; in the one-sided-exponential product stress test, a split coordinate can also contribute to $\lmax(A_t)$. Thus the splitting philosophy controls the *source* of the cut-aware Stein estimate ([](#conj:stein-weighted), [](#conj:splitting)), not the cut-free $\Xi_T$. The residual non-circular content of [](#conj:taming) is therefore a *near-worst-specific* improvement of the Klartag–Lehec window precisely in the regime $\hstar_n\gg1/\log\log n$ that [](#cor:loglog) does not reach.
:::

:::{prf:conjecture} Quantitative splitting / boundary Obata
:label: conj:splitting
The conjectural principle of [](#rem:obata) holds, first as a rigidity theorem and then in quantitative form: for a near-worst measure and a near-minimal balanced cut, small constant-mode curvature $\mathfrak K_\Sigma$ forces quantitative proximity, along the normal direction, to the split structure of [](#prop:exact-splitting), with constants stable under the localization tilt ([](#prop:persistent-splitting)). [](#prop:exact-splitting) proves only a sufficient globally split model and its flat halfspace; it does not prove the zero-curvature-to-splitting direction.
:::

:::{prf:assumption} Absolute-scale geometric completion
:label: ass:absolute-geometric-completion
There exist universal $T_0\in(0,1/8)$ and $\kappa,c_g,\eps_g>0$ such that the following interface implication holds. For any isotropic log-concave measure satisfying $h_\mu\le(1+\eps_g)\hstar_n$ and any balanced near-Cheeger cut $E$, if

$$
\int_0^{T_0}\E\bigl[\bar e_t\one_{\{t<\tau_\eta\}}\bigr]\dd t
\le T_0e_0+\kappa T_0,
$$

then the remaining geometric trace and stochastic consumption steps yield $\mu^+(E)\ge c_g$. This is an explicit placeholder for an absolute-scale completion, weaker and logically distinct from [](#ass:weighted-package).
:::

:::{prf:corollary} Residual dichotomy of the near-worst bootstrap
:label: cor:dichotomy
Under [](#ass:absolute-geometric-completion), the published [](#cor:KI-discharged) discharges [](#ass:KI), so by [](#cor:loglog), this supply is available for near-worst measures in every dimension with $\hstar_n\le c\kappa T_0/(1+\log\log n)$, and the resulting contradiction confines any failure of KLS to dimensions with $\hstar_n\ge c'/\log\log n$. Such a completion would therefore already yield

$$
\hstar_n\ \ge\ \frac{c'(\kappa)}{\log\log n}
\qquad\text{for all large }n,
$$

an asymptotic improvement over the version-1 preprint bound $\hstar_n\ge c(\log n)^{-1/4}$ [@Letwin2026QuadraticKLS]. Full KLS would additionally follow if [](#conj:taming) supplied its estimate at the same universal time consumed by [](#ass:absolute-geometric-completion) (or if that completion were uniform over the time supplied); the two existential times are not automatically equal.
:::

:::{prf:proof}
Choose the numerical constant $c$ in the hypothesis small enough, depending only on the constants in [](#cor:loglog) and on the completed argument. If $\hstar_n\le c\kappa T_0/(1+\log\log n)$, choose $0<\eps\le\min\{\eps_g,T_0^{1/3}\}$ and an isotropic log-concave $\mu$ in dimension $n$ with $h_\mu\le(1+\eps)\hstar_n$ and a balanced near-minimizer $E$ satisfying $\mu^+(E)\le I_\mu(\tfrac12)+o(1)=\tfrac12h_\mu+o(1)$, where the $o(1)$ is along the near-minimizing sequence. [](#cor:loglog) gives the supply $\int_0^{T_0}\E[\bar e_t\one_{t<\tau_\eta}]\dd t\le T_0e_0+\kappa T_0$ after reducing $c$. Running the completed argument on this near-minimizing sequence yields a universal lower bound $\mu^+(E)\ge c''>0$. Letting the near-minimizer error tend to zero gives $h_\mu\ge2c''$, which contradicts $h_\mu\le(1+\eps_g)\hstar_n$ once $n$ is in the asserted small-$\hstar_n$ regime. Hence any failure of KLS must lie in the complementary regime $\hstar_n\gtrsim1/\log\log n$.
:::

## Where to start

| Step | Input | Output |
|---|---|---|
| [](#rem:product-stress-test) | One-dimensional log-concave analysis; explicit variance dynamics | Decides whether the every-interval estimate [](#ass:all-cut-carleson) can hold on products. A proof models the cut-aware argument that [](#conj:trace-upgrade) needs; a counterexample bears on [](#conj:trace-upgrade) only if it also violates the prefix form, and does not favour the near-Cheeger variant. |
| Replacement for [](#conj:weighted-excess-rate) | A cut-local or tensor-stable covariance scale, plus a near-worst or source-deficit remainder that survives spectator products | A statement replacing the global-operator-norm rate; not yet formulated. |
| [](#conj:stein-weighted) | Letwin quadratic chaos; a new almost-stability trace lemma; Reilly boundary terms and zero modes; constant mode via [](#conj:splitting) | An analytic ingredient taken from [](#ass:weighted-package); it yields nothing toward KLS until a matching tensor-stable propagation statement is formulated. |
| [](#conj:taming) | Coupling of splitting structure to the covariance SDE | Absolute-scale bootstrap supply for near-worst measures; with the separate geometric completion in [](#cor:dichotomy), a path to full KLS at the matched time. |

## Summary

No new bound on $\hstar_n$ comes out of this approach: the bound it uses is Letwin's version-1 bound, and every use of it is marked conditional on that preprint. What does not depend on the preprint: the exact stochastic layer (Sections [](#sec:mass-martingale)–[](#sec:carleson)); the two-color Stein dictionary and the operator-to-trace gap (Section [](#sec:stein-dictionary)); the quadratic-chaos dictionary, the projection-method no-go, and the quantified two-tail configuration (Section [](#sec:qcts)); the published covariance technology (Section [](#sec:covariance-tech)); the consumption audit, the perimeter-martingale and excess identities, and the circularity warning (Section [](#sec:excess)); the bootstrap comparison theorem with its interface evaluation and ceiling (Section [](#sec:bootstrap)); the explicit sufficient model statements for splitting (Section [](#sec:jacobi)); and the model geometries (Section [](#sec:models)). What depends on it: dimension-free quadratic chaos and the $c/\log n$ covariance-moment window.

The all-cut estimate ([](#ass:all-cut-carleson)) and the absolute-scale completion ([](#ass:absolute-geometric-completion)) are hypotheses, and are stated as such. The spectator products of [](#prop:weighted-spectator-obstruction) violate the literal weighted package ([](#ass:weighted-package)) and [](#conj:weighted-excess-rate); the unweighted spectator products of [](#prop:spectator-excess-rate-obstruction) separately rule out the package's uniform superlinear remainder. The conditional implication from that package to KLS ([](#thm:intro-weighted)) is kept so that a reader can see what the package would have given. The problems this approach turns on are [](#conj:trace-upgrade), the trace and bootstrap statements [](#conj:stein-weighted)–[](#conj:splitting), and the formulation of a tensor-stable replacement.

The picture rests on three structural points: unweighted excess propagation is true as consumed and therefore inert; static two-tail calibration alone does not produce a tensor-stable weight or a viable uniform remainder; and the available near-worst propagation mechanism is compressed into the single scalar interface $h_\mu\,\Xi_T$, evaluated to within a $\log\log n$ factor of what the approach requires.
