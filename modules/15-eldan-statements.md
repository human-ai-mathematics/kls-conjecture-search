---
numbering:
  enumerator: "15.%s"
---

(sec:introduction)=
# The fixed cut: the approach and its main conditional statements

## The approach at a glance

Each of the four approaches opens with the same short summary — the idea, how it would give KLS, what it uses, what it gives, what blocks it, what rules out its obvious variants, and what would settle it — so that the approaches can be compared without reading any of them in full. Section [](#sec:frontier-atlas) sets the four side by side.

**The idea.** Follow one *fixed* would-be bottleneck cut $E$ under Eldan's stochastic localization, and show that it cannot be identified too quickly.

**How it would give KLS.** Through a chain of two implications, conditional at exactly one place:

$$
\text{a balanced cut survives to a universal time}
\ \Longrightarrow\
\text{boundary lower bound}
\ \Longrightarrow\
\text{KLS}.
$$

The survival-to-boundary step is [](#lem:survival-implies-kls). To obtain survival, [](#thm:carleson-implies-centroid) converts the all-cut Carleson premise into stopped centroid control, and [](#thm:centroid-implies-kls) uses the mass martingale. The weaker deterministic-prefix premise [](#ass:tight-prefix-carleson) is the input consumed by [](#cor:tight-window-consumption); [](#thm:intro-all-cut) records the consequence of the stronger all-cut formulation. The separate weighted implication is formulated in [](#thm:intro-weighted), with the product witnesses of [](#prop:weighted-spectator-obstruction) testing its propagation premise. None of these implications supplies its own Carleson or centroid hypothesis, and a counterexample to such a hypothesis would not refute KLS.

**What it uses.** From the literature: the localization process and its covariance SDE, and the improved Lichnerowicz estimate ([](#thm:improved-lichnerowicz)). Developed in this manuscript: the two-colour Riccati identities ([](#thm:scalar-riccati), Section [](#sec:riccati)), the Stein dictionary (Section [](#sec:stein-dictionary)), and the covariance technology (Section [](#sec:covariance-tech)). Each statement below displays its own standing.

**What it gives.** Three results. The bootstrap comparison theorem and the interface functional $\Xi_T$ (Section [](#sec:bootstrap)), together with the fact that the crude evaluation of $\Xi_T$ *cannot* suffice ([](#rem:insufficiency)) — a negative result that says exactly which input the bootstrap needs. The scale-weighted all-cut source budget, [](#lem:time-weighted-source). And the coordinate budgets and covariance reduction of the product stress test (Section [](#sec:product-stress)), where the approach is tested against the measure that defeats naive covariance control.

**What blocks it.** For the all-cut variant, the operator-to-trace upgrade [](#conj:trace-upgrade): obtain [](#ass:tight-prefix-carleson) by lifting [](#cor:per-direction) from quadratic-form scale to trace scale, uniformly over fixed initial data (Section [](#sec:open)). For the near-Cheeger variant, the trace estimate [](#conj:stein-weighted) lacks a companion: a tensor-stable propagation statement to replace the literal package [](#ass:weighted-package), together with a localization-uniform almost-stability trace theorem.

**What rules out the obvious variants.** Two obstructions, which are the most reusable output of this approach. A global operator-norm covariance weight, as in [](#ass:weighted-package) and [](#conj:weighted-excess-rate), charges independent spectator coordinates that contribute nothing, and a balanced cylinder in a product of one-sided exponentials makes the overcharge unbounded ([](#prop:weighted-spectator-obstruction)). The same spectators rule out a uniform superlinear remainder even with weight one ([](#prop:spectator-excess-rate-obstruction)). Separately, a single inflated coordinate cannot carry a counterexample ([](#cor:single-coordinate-cuts), Section [](#sec:budgets)). Two further constraints are methodological warnings rather than theorems: the two-tail obstruction ([](#rem:two-tail-slice-bounds)) and the circularity warning of Section [](#sec:excess).

**What would settle it.** The all-cut variant is settled positively by [](#conj:trace-upgrade) with universal constants, and negatively by a family of balanced cuts on which the trace-scale statement fails. The near-Cheeger variant first needs a new formulation: a cut-local, tensor-stable covariance weight that ignores independent spectators while still dominating the aligned two-tail mode, or a replacement carrying an explicit near-worst-measure premise.

% Agent note: the approach ap:e-weighted-excess of research/program/portfolio.yaml is closed on
% the spectator obstruction; the checkpoints that name it record the reopening condition above.

**Where to read.** Conceptual prelude: Section [](#sec:localization-prelude). The static quadratic-chaos input and its limits: Section [](#sec:qcts). The approach proper: this section for the conditional statements, then Sections [](#sec:carleson)–[](#sec:open). Full apparatus: the shared technical foundations (Sections [](#sec:notation), [](#sec:riccati), [](#sec:qcts), [](#sec:covariance-tech) and [](#sec:models)), with the mass martingale (Section [](#sec:mass-martingale)), the Stein dictionary (Section [](#sec:stein-dictionary)) and the Jacobi splitting formulas (Section [](#sec:jacobi)) among this approach's chapters. Full proofs are linked from the status shown next to each statement.

**The idea, in one line.**

$$
\boxed{\text{follow the posterior evolution of a fixed would-be bottleneck cut }E.}
$$

The mass $p_t=\mu_t(E)$ is a martingale. KLS follows if a balanced near-bottleneck cut cannot be identified too rapidly by the early Gaussian observation generated by localization. Retaining one set, rather than the full spectrum of $A_t$, is this approach's response to [](#prop:covariance-spike).

Throughout, $\mu$ is isotropic log-concave on $\R^n$, so $\E_\mu X=0$ and $\Cov_\mu(X)=I_n$; the isoperimetric profile is

$$
I_\mu(p)=\inf\{\mu^+(E):\mu(E)=p\},\qquad 0<p<1,
$$

and $h_\mu$, $\PsiKLS_\mu=h_\mu^{-1}$, $\hstar_n$ are as fixed in Section [](#subsec:kls-conjecture) and [](#eq:hstar-def); recall in particular [](#rem:psi-convention) on the $\psi$ convention. The conjecture itself and the literature frontier are in Section [](#sec:kls-orientation); the sharp radial and homogeneous-quadratic results recorded there remove major static obstructions, but they do not by themselves control a fixed bottleneck set under localization.

The shared localization machinery — notation, the mass martingale, the two-color Riccati identities and Stein dictionary, the static obstruction, the covariance technology, and the model geometries — is deferred to the shared technical foundations and to the supporting chapters of this approach; the conceptual summary needed to follow this approach is the prelude, Section [](#sec:localization-prelude). The present section states the conditional results; Sections [](#sec:carleson)–[](#sec:open) carry out the arguments.

(subsec:two-variants)=
## The all-cut and near-Cheeger variants

Both variants run on the same stochastic localization; they differ in which cuts they must control, and are named accordingly.

**The all-cut variant.** Prove an absorptive two-color Carleson estimate for every balanced cut. This immediately yields KLS.

**The near-Cheeger variant.** Work only with near-minimizers of the isoperimetric profile. The conditional architecture below couples weighted excess propagation under localization to a weighted stable Stein-trace estimate. Its literal form fails on the product cylinders described under *What rules out the obvious variants* above. A workable replacement must use a cut-local or tensor-stable covariance scale and also permit an $O(T)$ supply, use a genuinely source-tied remainder, or impose an explicit near-worst-measure hypothesis.

The near-Cheeger variant is the natural home for the boundary/Jacobi ideas. It should not be advertised as an all-cut estimate: arbitrary balanced sets can have enormous two-color covariance contrast even when their perimeter is small in an anisotropic posterior.

## Main stochastic quantities

For orientation we recall the two-color quantities; they are defined in full in Section [](#sec:notation). Fix a measurable set $E$ and put $F=E^c$. Under localization define

$$
p_t=\mu_t(E),\qquad q_t=1-p_t,
\qquad s_t=p_tq_t,
$$

$$
\delta_t=m_t^E-m_t^F,
\qquad G_t=\Sigma_t^E-\Sigma_t^F,
\qquad r_t=s_t\abs{\delta_t}^2,
$$

where $m_t^E,m_t^F$ and $\Sigma_t^E,\Sigma_t^F$ are the two conditional means and covariances. The Riccati source and damping are

$$
S_t=s_t\norm{G_t}_{\HS}^2,
\qquad
D_t=2s_t\delta_t^TA_t\delta_t-r_t^2,
$$

where $A_t=\Cov(\mu_t)$. The isoperimetric excess process is

$$
e_t(E)=\mu_t^+(E)-I_{\mu_t}(p_t)\ge0,
$$

and the covariance-excess functionals, central to both variants, are

```{math}
:label: eq:interface-def
X_t=\bigl(\lmax(A_t)-1\bigr)_+,
\qquad
\Xi_T(\mu)=\int_0^T\E X_t\dd t .
```

Let $\tau$ be the coarse balanced exit time [](#eq:tau-coarse), the first time at which $p_t$ leaves $[1/3,2/3]$, and let $\tau_\eta$ be the tight window of [](#eq:tau-tight) below; balanced initial cuts are as in Section [](#sec:notation), $p_0\in[2/5,3/5]$ for the coarse window.

## Main conditional statements

:::{prf:assumption} All-cut absorptive two-color Carleson estimate
:label: ass:all-cut-carleson
There exist universal constants $T_0>0$, $C_0,C_1\ge0$ and $\alpha<1$ such that for every isotropic log-concave $\mu$, every balanced measurable set $E$, and every interval $I\subset[0,T_0]$,

```{math}
:label: eq:all-cut-carleson
\E\int_{I\cap[0,\tau]} S_t\dd t
\le
C_0\abs I+C_1\E\int_{I\cap[0,\tau]}r_t\dd t
+\alpha\E\int_{I\cap[0,\tau]}D_t\dd t .
```
:::

:::{prf:theorem} All-cut Carleson implies KLS
:label: thm:intro-all-cut
[](#ass:all-cut-carleson) implies the KLS conjecture.
:::

The argument is in Sections [](#sec:mass-martingale)–[](#sec:carleson). Taking $I=[0,T]$ and $\eta=1/6$, for which the tight window is the coarse one, the assumption gives the hypothesis of [](#cor:tight-window-consumption) for every cut of mass $1/2$; [](#lem:survival-implies-kls) then concludes. It uses only stochastic localization, the two-color Riccati identity, and the fact that a $T$-uniformly log-concave posterior has a dimension-free Cheeger lower bound at scale $\sqrt T$.

The consumption step [](#cor:tight-window-consumption) needs less than the all-interval formulation above. Its exact premise is the following.

:::{prf:assumption} Tight-prefix absorptive two-color Carleson estimate
:label: ass:tight-prefix-carleson
There exist universal constants $\eta\in(0,1/6]$, $T_0,C_0,C_1>0$, and $\alpha<1$ such that, for every isotropic log-concave $\mu$, every fixed measurable cut $E$ with $\abs{\mu(E)-1/2}\le\eta/2$, and every $0<T\le T_0$,

```{math}
:label: eq:tight-prefix-carleson
\E\int_0^{T\wedge\tau_\eta} S_t\dd t
\le C_0T+C_1\E\int_0^{T\wedge\tau_\eta}r_t\dd t
+\alpha\E\int_0^{T\wedge\tau_\eta}D_t\dd t .
```
:::

This prefix-only statement is implied by [](#ass:all-cut-carleson): take $I=[0,T]$ and $\eta=1/6$, for which [](#eq:tau-tight) is [](#eq:tau-coarse); no converse is known. [](#cor:tight-window-consumption) derives its boundary-lower-bound consequence for each cut; universal validity would therefore give KLS by the same balanced near-minimizer reduction. No argument is known that derives this assumption from the soft-projector calculations.

The literal package consumed by the conditional theorem [](#thm:intro-weighted) is recorded below, so that both the implication and the premise it needs can be checked.

:::{prf:assumption} Literal weighted near-Cheeger package
:label: ass:weighted-package
There are universal constants $T_0>0$, $C_0,C_1,C_2\ge0$, $0\le\beta<\tfrac12$, $\gamma>0$, and $\eta\in(0,\tfrac14]$ satisfying

```{math}
:label: eq:weighted-absorption-margin
2\beta+64\eta^2<1,
```

such that, for the corresponding fixed tight stopping window $\tau_\eta$, the following two estimates hold for every initial finite-perimeter set $E$ with $e_0(E)\le1$ and $p_0=1/2$ (or $\abs{p_0-1/2}\le\eta/2$).

(i-w) **Weighted excess propagation.**

```{math}
:label: eq:intro-weighted-excess
\E\int_0^{T\wedge\tau_\eta} e_t(E)\,\bigl(1+\norm{A_t}_\op\bigr)^{5/2}\dd t
\le C_2\bigl(T e_0(E)+T^{1+\gamma}\bigr),
\qquad 0<T\le T_0 .
```

(ii-w) **Weighted stable Stein-trace estimate.** With the Stein-trace norm $\calS_{\mu_t}(E)$ defined in Section [](#sec:stein),

```{math}
:label: eq:intro-weighted-stein
\begin{aligned}
\E\int_0^{T\wedge\tau_\eta}\frac{\calS_{\mu_t}(E)}{s_t}\dd t
&\le
C_0T+C_1\E\int_0^{T\wedge\tau_\eta}r_t\dd t
+\beta\E\int_0^{T\wedge\tau_\eta}D_t\dd t \\
&\qquad
+C_2\E\int_0^{T\wedge\tau_\eta}
e_t(E)\bigl(1+\norm{A_t}_\op\bigr)^{5/2}\dd t .
\end{aligned}
```
:::

[](#prop:weighted-spectator-obstruction) exhibits, for every choice of the constants, a product cylinder on which item (i-w) fails with these global quantifiers, even when the initial cut has arbitrarily small additive and relative excess. The package is kept because it is the explicit antecedent of the next theorem.

:::{prf:theorem} Weighted geometric package implies KLS
:label: thm:intro-weighted
[](#ass:weighted-package) implies the KLS conjecture.
:::

The argument for the implication is in Section [](#sec:stein), using the audit and propagation analysis of Section [](#sec:excess); it is a conditional argument, unaffected by whether its antecedent holds. The weight $(1+\norm{A_t}_\op)^{5/2}$ is calibrated on the anisotropic two-tail configuration ([](#prop:two-tail)): among pure powers of $\lmax(A_t)$ multiplying absolute excess in this slice-wise package, $5/2$ is the smallest statically consistent exponent. Static consistency is not enough: the same global norm also sees irrelevant independent spectators. The following audit explains the first constraint, and [](#prop:weighted-spectator-obstruction) supplies the second.

:::{prf:proposition} Consumption audit; deceptive strength of the unweighted estimate
:label: prop:intro-audit
(a) For every isotropic log-concave $\mu$, every Borel set $E$ with $\mu(E)=1/2$, finite initial lower outer Minkowski perimeter, and excess $e_0=e_0(E)$, every $T>0$ and every stopping time $\tau$,

$$
\E\int_0^{T\wedge\tau}e_t(E)\dd t\ \le\ (1+e_0)\,T .
$$

(b) Consequently, the *unweighted* stable Stein-trace estimate — estimate [](#eq:intro-weighted-stein) with the weight $(1+\norm{A_t}_\op)^{5/2}$ replaced by $1$ — implies the KLS conjecture by itself; the unweighted excess term is inert, and unweighted excess propagation is unconditionally true in the form consumed.

(c) Nevertheless, the unweighted estimate admits no slice-wise proof: there are log-concave pairs $(\nu,E)$ with $\nu(E)=1/2$, $r=D=0$, excess $e(E)\to0$, and $\calS_\nu(E)/s\to\infty$ ([](#prop:two-tail)).
:::

The argument is in Section [](#sec:excess). Item (b) is not good news about excess propagation; it is a warning that the unweighted geometric package concentrated its entire logical weight, invisibly, in the Stein-trace estimate. Item (c) shows that this weight cannot be discharged one time-slice at a time. The proposed weighted formulation made the excess term non-inert and passed the static two-tail calibration, but the spectator obstruction shows that its global-operator-norm version is not tensor-stable. The separate unweighted spectator obstruction also rules out every uniform superlinear source-vanishing remainder of the same form. The next formulation must meet the static, tensor-stability, and time-scale constraints rather than merely changing the covariance weight.

Finally, Section [](#sec:bootstrap) provides the available propagation mechanism: a bootstrap comparison theorem anchored at $\hstar_n$, valid for *every* balanced cut of a near-worst measure — the only regime a proof of KLS by contradiction requires — which compresses excess propagation into the scalar interface functional $h_\mu\,\Xi_T(\mu)$, together with a complete evaluation of that interface against the known covariance technology.

## The ingredients at a glance

| Ingredient | Role | Where |
|---|---|---|
| Mass martingale and stopped centroid reduction | Reduces KLS to survival of a balanced cut for universal time | [](#lem:survival-implies-kls), [](#thm:centroid-implies-kls) |
| Matrix and scalar two-color Riccati identities | Isolate the source $S_t$ and damping $D_t$ exactly | [](#thm:scalar-riccati), Section [](#sec:riccati) (formal, with standard approximation conventions) |
| Per-direction Carleson estimate | Shows that $s_tG_t^2$ has dimension-free occupation in every fixed direction | [](#cor:per-direction), from the matrix Riccati identity |
| Operator-to-trace upgrade | The true stochastic missing estimate | [](#conj:trace-upgrade) |
| Quadratic-chaos thin shell | Static time-zero form of two-color covariance control | [](#thm:letwin-qcts), imported with constant $8$ from a July 2026 version-1 preprint; whitening still leaves dynamic covariance alignment |
| Consumption audit of the excess term | Shows the unweighted excess term is inert and the unweighted Stein-trace estimate alone implies KLS | [](#prop:intro-audit), Section [](#sec:excess) |
| Two-tail calibration and spectator obstructions | The static aligned mode forces at least the $5/2$ pure-power scale, while independent spectators rule out both the resulting global-norm rate and every uniform superlinear remainder even at weight one | [](#prop:two-tail), [](#prop:weighted-spectator-obstruction), [](#prop:spectator-excess-rate-obstruction) |
| Perimeter martingale and exact excess identity | Reduces propagation to the localized profile floor; exposes a circularity risk without proving a no-go theorem | [](#lem:perimeter-martingale), [](#lem:excess-identity) |
| Bootstrap comparison theorem | Reduces near-worst excess propagation to the interface $h_\mu\,\Xi_T$ | [](#thm:bootstrap) |
| Interface evaluation | $\log\log n$ loss from known covariance technology; crude evaluation insufficient; a relative bound for all measures at a sufficiently small universal time is KLS-sufficient | [](#cor:loglog), [](#rem:insufficiency), [](#prop:ceiling), given the imported covariance input of [](#ass:KI) |
| Weighted excess propagation | A replacement must ignore irrelevant spectator covariance, retain the aligned two-tail mode, and change the uniform superlinear remainder or assume near-worstness | Literal form: [](#conj:weighted-excess-rate); the two spectator obstructions above; no replacement formulated yet (Section [](#sec:open)) |
| Extremality tames the covariance process | Residual target of the bootstrap | [](#conj:taming); proposed approach: couple the splitting analysis to the covariance SDE |
| Weighted stable Stein trace | Boundary approach to the two-color source estimate | [](#conj:stein-weighted); Reilly/Jacobi gives a proposed mechanism, but a uniform almost-stability trace lemma is missing |
| Jacobi constant-mode splitting | Proposed treatment of modes invisible to volume-preserving stability | Sufficient split model: [](#prop:exact-splitting); converse rigidity, coercivity modulo zero modes and quantitative stability: [](#conj:splitting) |
