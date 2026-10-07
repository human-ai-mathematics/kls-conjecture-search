---
numbering:
  enumerator: "28.%s"
---

(sec:introduction)=
# The fixed cut: approach and lessons

This chapter opens the fixed-cut archive, formed by this chapter and the six that follow. The fixed cut was the first localization argument of this manuscript. KLS is now proved by other means (Chapter [](#sec:kls-synthesis)), and the fixed cut is kept for its results, which are obstructions, a ceiling and counterexamples, and which apply beyond it. The ceiling [](#prop:ceiling) measures how strong one covariance input would have to be for a bootstrap of the boundary excess to close. The spectator products of [](#prop:weighted-spectator-obstruction) refute a natural weighted propagation estimate, and with it any global covariance weight that charges coordinates a cut does not use. The product stress test of Chapter [](#sec:product-stress) is the tensorization test of Section [](#subsec:kls-tensorization-test) carried out on an all-cut estimate. Any argument that follows a set through localization meets all three. The open statements of the archive are precise problems, not steps towards KLS.

(subsec:two-variants)=
## The all-cut and near-Cheeger variants

Both variants follow a fixed cut under the same stochastic localization; they differ in which cuts they must control, and the two names used throughout the archive come from this difference.

**The all-cut variant** asks for an absorptive two-color Carleson estimate for *every* balanced cut ([](#ass:all-cut-carleson) below); this alone yields KLS ([](#thm:intro-all-cut)).

**The near-Cheeger variant** works only with near-minimizers of the isoperimetric profile, the cuts that a proof of KLS by contradiction has to handle. It couples weighted excess propagation under localization to a weighted stable Stein-trace estimate ([](#ass:weighted-package) below). Its literal form fails on the product cylinders described under *What rules out the obvious variants* below. A workable replacement must use a cut-local or tensor-stable covariance scale and also permit an $O(T)$ supply, use a genuinely source-tied remainder, or impose an explicit near-worst-measure hypothesis.

The near-Cheeger variant is the natural home for the boundary and Jacobi ideas of Chapter [](#sec:jacobi). It gives no all-cut estimate: arbitrary balanced sets can have enormous two-color covariance contrast even when their perimeter is small in an anisotropic posterior.

## The approach at a glance

The summary below has the format of those of the three alternative mechanisms, compared in Chapter [](#sec:frontier-atlas).

**The idea.** Follow one *fixed* would-be bottleneck cut $E$ under Eldan's stochastic localization, and show that it cannot be identified too quickly.

**What it would add.** The fixed cut is kept as the record of a method: its obstructions and its ceiling are its results, and they say what any argument that follows a single cut through localization has to overcome. Were its hypotheses established, it would give KLS through a chain of two implications, conditional at exactly one place, through a bottleneck set that cannot be identified too quickly:

$$
\text{a balanced cut survives to a universal time}
\ \Longrightarrow\
\text{boundary lower bound}
\ \Longrightarrow\
\text{KLS}.
$$

The survival-to-boundary step is [](#lem:survival-implies-kls). To obtain survival, [](#thm:carleson-implies-centroid) converts the all-cut Carleson hypothesis into stopped centroid control, and [](#thm:centroid-implies-kls) uses the mass martingale. The weaker hypothesis on deterministic prefixes, [](#ass:tight-prefix-carleson), is what [](#cor:tight-window-consumption) uses; [](#thm:intro-all-cut) records the consequence of the stronger all-cut formulation. The near-Cheeger implication is [](#thm:intro-weighted); the product witnesses of [](#prop:weighted-spectator-obstruction) refute its propagation hypothesis. None of these implications supplies its own Carleson or centroid hypothesis.

**What it uses.** From the literature: the localization process and its covariance SDE, and the improved Lichnerowicz estimate ([](#thm:improved-lichnerowicz)). Developed in this manuscript: the two-color Riccati identities ([](#thm:scalar-riccati), Chapter [](#sec:riccati)), the Stein dictionary (Section [](#sec:stein-dictionary)), and the small-time covariance control (Chapter [](#sec:covariance-tech)). Each statement below displays its own standing.

**What it gives.** Its implications towards KLS are conditional, and its results are its obstructions and its ceiling; this chapter states both, and Chapters [](#sec:carleson) to [](#sec:jacobi) hold the arguments.

- *A bootstrap, and the one quantity it needs.* [](#thm:bootstrap) says that for a measure whose Cheeger constant is within a factor $1+\varepsilon$ of the smallest in its dimension, the excess of every balanced cut propagates along localization with a single quantity, $\Xi_T(\mu)=\int_0^T\E(\lmax(A_t)-1)_+\dd t$. The idea: the isoperimetric profile of a log-concave measure is concave and symmetric, so its Cheeger constant is read at mass $\tfrac12$; whitening a localized measure of covariance $A_t$ loses at most $\lmax(A_t)^{1/2}$ against the worst isotropic measure of the same dimension; near-worstness compares the localized Cheeger constant with that of $\mu$, and every loss is charged to $(\lmax(A_t)-1)_+$.
- *How far it gets.* The crude evaluation $\Xi_T\lesssim\log n$ never suffices in high dimension ([](#rem:insufficiency), [](#rem:crude-insufficient)); the polylogarithmic covariance estimates improve it to $\Xi_T\le C(1+\log\log n)$ for $t_1(n)\le T\le1$ ([](#cor:loglog)), which still falls short of the $O(T)$ the bootstrap needs. A relative bound $\Xi_{T_0}(\mu)\le\kappa T_0$ for all measures at a sufficiently small universal time would itself give KLS ([](#prop:ceiling)): this measures the input the bootstrap needs, without excluding other propagation arguments.
- *Budgets.* The scale-weighted all-cut source budget [](#lem:time-weighted-source), and the coordinate budgets and covariance reduction of the product stress test (Chapter [](#sec:product-stress)), where the approach meets the measure that defeats naive covariance control: no fixed balanced cut of a product that depends on a single coordinate can witness a failure of the all-cut chain of implications, since its conclusion holds for such cuts unconditionally ([](#cor:single-coordinate-cuts)).
- *The excess term is inert.* Unweighted excess propagation holds unconditionally at scale $O(T)$, so the unweighted Stein-trace estimate alone would imply KLS, and that estimate admits no proof one time-slice at a time ([](#prop:intro-audit)). The whole weight of the near-Cheeger variant is carried by the trace estimate; a covariance weight is what makes the excess term matter.

**What blocks it.** For the all-cut variant, the operator-to-trace upgrade [](#conj:trace-upgrade): obtain [](#ass:tight-prefix-carleson) by lifting [](#cor:per-direction) from quadratic-form scale to trace scale, uniformly over fixed initial data (Chapter [](#sec:open)). For the near-Cheeger variant, the trace estimate [](#conj:stein-weighted) lacks a companion: a tensor-stable propagation statement to replace the refuted literal package [](#ass:weighted-package), together with a localization-uniform almost-stability trace theorem ([](#conj:almost-stability-gap)). For the bootstrap, the missing input is a near-worst bound on $h_\mu\,\Xi_T$ at a universal time ([](#conj:taming)); the constant-mode branch of the Reilly–Jacobi mechanism rests on quantitative splitting ([](#conj:splitting)).

**What rules out the obvious variants.** Two obstructions, which are the most reusable output of this approach. A global operator-norm covariance weight, as in [](#ass:weighted-package) and [](#conj:weighted-excess-rate), charges independent spectator coordinates that contribute nothing, and a balanced cylinder in a product of one-sided exponentials makes the overcharge unbounded ([](#prop:weighted-spectator-obstruction)). The same spectators rule out a uniform superlinear remainder even with weight one ([](#prop:spectator-excess-rate-obstruction)). Separately, a single inflated coordinate cannot carry a counterexample ([](#cor:single-coordinate-cuts), Section [](#sec:budgets)). Two further constraints are methodological warnings rather than theorems: the two-tail obstruction ([](#rem:two-tail-slice-bounds)) and the circularity warning of Section [](#subsec:circularity).

**What would settle it.** The all-cut variant is settled positively by [](#conj:trace-upgrade) with universal constants, and negatively by a family of balanced cuts on which the trace-scale statement fails. The near-Cheeger variant first needs a new formulation: a cut-local, tensor-stable covariance weight that ignores independent spectators while still dominating the aligned two-tail mode, or a replacement carrying an explicit near-worst-measure hypothesis.

% Agent note: the approach ap:e-weighted-excess of research/program/portfolio.yaml is closed on
% the spectator obstruction; the checkpoints that name it record the reopening condition above.

**Where to read.** Conceptual prelude: Chapter [](#sec:localization-prelude). The static quadratic-chaos input and its limits: Chapter [](#sec:qcts). The fixed cut itself: this chapter for the conditional statements and what they teach, Chapter [](#sec:open) for the remaining problems, and then the arguments — the mass martingale and the all-cut implication (Chapter [](#sec:carleson)), the product stress test with its calculations (Chapter [](#sec:product-stress)), the near-Cheeger variant with the Stein dictionary and excess propagation (Chapter [](#sec:stein)), the bootstrap (Chapter [](#sec:bootstrap)), and the Reilly, Jacobi and splitting formulas (Chapter [](#sec:jacobi)). Shared apparatus: Chapters [](#sec:notation), [](#sec:riccati), [](#sec:qcts), [](#sec:covariance-tech) and [](#sec:models). Full proofs are linked from the status shown next to each statement.

**The idea, in one line.**

$$
\boxed{\text{follow the posterior evolution of a fixed would-be bottleneck cut }E.}
$$

The mass $p_t=\mu_t(E)$ is a martingale. KLS follows if a balanced near-bottleneck cut cannot be identified too rapidly by the early Gaussian observation generated by localization. Retaining one set, rather than the full spectrum of $A_t$, is this approach's response to [](#prop:covariance-spike).

Throughout, $\mu$ is isotropic log-concave on $\R^n$, so $\E_\mu X=0$ and $\Cov_\mu(X)=I_n$; the isoperimetric profile is

$$
I_\mu(p)=\inf\{\mu^+(E):\mu(E)=p\},\qquad 0<p<1,
$$

and $h_\mu$, $\PsiKLS_\mu=h_\mu^{-1}$, $\hstar_n$ are as fixed in Section [](#subsec:kls-conjecture) and [](#eq:hstar-def); recall in particular [](#rem:psi-convention) on the $\psi$ convention. KLS and the state of the literature are in Sections [](#sec:kls-orientation) and [](#sec:kls-known); the sharp radial and homogeneous-quadratic results recorded there remove major static obstructions, but they do not by themselves control a fixed bottleneck set under localization.

## Main stochastic quantities

For orientation we recall the two-color quantities; they are defined in full in Chapter [](#sec:notation). Fix a measurable set $E$ and put $F=E^c$. Under localization define

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

Let $\tau$ be the coarse balanced exit time [](#eq:tau-coarse), the first time at which $p_t$ leaves $[1/3,2/3]$, and let $\tau_\eta$ be the tight window of [](#eq:tau-tight) below; balanced initial cuts are as in Chapter [](#sec:notation), $p_0\in[2/5,3/5]$ for the coarse window.

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
[](#ass:all-cut-carleson) implies KLS.
:::

The argument is in Chapter [](#sec:carleson). Taking $I=[0,T]$ and $\eta=1/6$, for which the tight window is the coarse one, the assumption gives the hypothesis of [](#cor:tight-window-consumption) for every cut of mass $1/2$; [](#lem:survival-implies-kls) then concludes. It uses only stochastic localization, the two-color Riccati identity, and the fact that a $T$-uniformly log-concave posterior has a dimension-free Cheeger lower bound at scale $\sqrt T$.

The step from a Carleson estimate to a boundary lower bound, [](#cor:tight-window-consumption), needs less than the all-interval formulation above. Its exact hypothesis is the following.

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

This prefix-only statement is implied by [](#ass:all-cut-carleson): take $I=[0,T]$ and $\eta=1/6$, for which [](#eq:tau-tight) is [](#eq:tau-coarse); no converse is known. [](#cor:tight-window-consumption) derives its boundary-lower-bound consequence for each cut; universal validity would therefore give KLS by the same balanced near-minimizer reduction.

The hypothesis of the conditional theorem [](#thm:intro-weighted) of the near-Cheeger variant is the following package.

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

(ii-w) **Weighted stable Stein-trace estimate.** With the Stein-trace norm $\calS_{\mu_t}(E)$ defined in Chapter [](#sec:stein),

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

[](#prop:weighted-spectator-obstruction) exhibits, for every choice of the constants, a product cylinder on which item (i-w) fails with these global quantifiers, even when the initial cut has arbitrarily small additive and relative excess. The package is therefore refuted; it is kept because it is the hypothesis of the next theorem, which records what it would have given.

:::{prf:theorem} Weighted geometric package implies KLS
:label: thm:intro-weighted
[](#ass:weighted-package) implies KLS.
:::

The argument is in Section [](#subsec:consumption), using the excess bounds of Section [](#sec:excess); it is a conditional argument, valid whether or not its hypothesis holds. The weight $(1+\norm{A_t}_\op)^{5/2}$ is calibrated on the anisotropic two-tail configuration ([](#prop:two-tail)): among pure powers of $\lmax(A_t)$ multiplying absolute excess in this slice-wise package, $5/2$ is the smallest statically consistent exponent. Static consistency is not enough: the same global norm also sees irrelevant independent spectators. The following proposition explains the first constraint, and [](#prop:weighted-spectator-obstruction) supplies the second.

:::{prf:proposition} Excess audit; deceptive strength of the unweighted estimate
:label: prop:intro-audit
(a) For every isotropic log-concave $\mu$, every Borel set $E$ with $\mu(E)=1/2$, finite initial lower outer Minkowski perimeter, and excess $e_0=e_0(E)$, every $T>0$ and every stopping time $\tau$,

$$
\E\int_0^{T\wedge\tau}e_t(E)\dd t\ \le\ (1+e_0)\,T .
$$

(b) Consequently, the *unweighted* stable Stein-trace estimate — estimate [](#eq:intro-weighted-stein) with the weight $(1+\norm{A_t}_\op)^{5/2}$ replaced by $1$ — implies KLS by itself; the unweighted excess term is inert, and unweighted excess propagation is unconditionally true in the form used.

(c) Nevertheless, the unweighted estimate admits no slice-wise proof: there are log-concave pairs $(\nu,E)$ with $\nu(E)=1/2$, $r=D=0$, excess $e(E)\to0$, and $\calS_\nu(E)/s\to\infty$ ([](#prop:two-tail)).
:::

The argument is in Section [](#sec:excess). Item (b) is not good news about excess propagation; it is a warning that the unweighted geometric package concentrated its entire logical weight, invisibly, in the Stein-trace estimate. Item (c) shows that this weight cannot be discharged one time-slice at a time. The proposed weighted formulation made the excess term non-inert and passed the static two-tail calibration, but the spectator obstruction shows that its global-operator-norm version is not tensor-stable. The separate unweighted spectator obstruction also rules out every uniform superlinear source-vanishing remainder of the same form. A replacement formulation would have to meet the static, tensor-stability and time-scale constraints together; changing the covariance weight alone does not suffice.

Finally, Chapter [](#sec:bootstrap) provides the available propagation mechanism: a bootstrap comparison theorem anchored at $\hstar_n$, valid for *every* balanced cut of a near-worst measure — the only regime a proof of KLS by contradiction requires — which compresses excess propagation into the scalar quantity $h_\mu\,\Xi_T(\mu)$, together with a complete evaluation of that quantity against the known covariance estimates.
