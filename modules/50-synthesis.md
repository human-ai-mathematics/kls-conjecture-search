---
numbering:
  enumerator: "50.%s"
---

(sec:kls-synthesis)=
# Synthesis: what a proof of KLS now needs

The July 2026 preprints changed the shape of the problem, and it is worth stating the change precisely rather than as a mood. *The remaining difficulty is no longer quadratic forms or third moments.* Conditional on [@Letwin2026QuadraticKLS], $\kappa_n=O(1)$ and every quadratic witness is eliminated. What remains is the problem of promoting fixed-matrix or averaged information to uniform control of every nonlinear test function, without paying a logarithmic largest-eigenvalue cost.

This section states that residue in six versions — one per strategy family — and then names the four concrete next targets, each mapped to the labelled statement of this manuscript that carries it, where one exists.

(subsec:synthesis-table)=
## The residue, family by family

| Framework | What is now controlled | The missing estimate |
|---|---|---|
| Needles (§[](#sec:family-needles)) | One-dimensional conditional measures, sharply | A decomposition inheriting *operator* covariance, not one or two scalar constraints |
| Stochastic localization (§[](#sec:family-sl)) | Short-time covariance and, conditionally, sharp third moments | Avoid the $\log n$ cost of approximating the maximum eigenvalue |
| Heat flow, $H^{-1}$ (§[](#sec:family-bochner)) | Coordinate and quadratic spectral mass | Uniform estimates for derivatives of an arbitrary $f$ |
| Moment map (§[](#sec:family-moment-map)) | Fixed deterministic matrix energies $\E\Tr(BHBH)$; and, exactly, $\CMH$ on the line, on products, and on every log-concave Dirichlet law (§[](#sec:cmh-exact-cases)) | Control when the matrix or direction depends on $X$ or on $f$. Even the linear sector is missing: $\lmax(\E H^2)\le4$ does not follow from $\Tr(\E H^2)\le2n$, and [](#prop:letwin-not-gate-zero) shows no matrix-moment argument closes the gap |
| Parallel coupling (§[](#subsec:kls-solved-neighbours)) | Linear exponential tilts $e^{\inner\theta x}\mu$ | Couplings for arbitrary functional perturbations |
| Brownian transport (§[](#sec:family-transport)) | Polylogarithmic averaged derivative bounds | A dimension-free expected operator derivative |

Every row is the same sentence in a different dialect: something is controlled *on average*, or *for a fixed object*, and KLS needs it *uniformly*, for an object that is allowed to depend on the measure.

(subsec:synthesis-constraint)=
## The constraint any proposal must satisfy

[](#prop:covariance-spike) is not a technical nuisance; it is the sharpest available guide to what a correct argument can look like. Products of centered exponentials have a dimension-free Poincaré constant by tensorization, yet their conditional covariance spikes: $\E\norm{\Cov(X\mid X+\sqrt sG)}_\op\gtrsim s$ for $s\le\log n$.

Two consequences follow, and they cut in opposite directions.

(1) A straightforward “bound $\norm{A_t}_\op$ better” program cannot work: the statement it would need is false.

(2) Rare covariance spikes can be *harmless*. A successful potential should recognize this rather than charge the full largest eigenvalue whenever a spike occurs. Tensorization is the diagnostic: a potential that is not tensorization-aware will charge $n$ independent coordinates $n$ times for a phenomenon that costs $O(1)$.

(subsec:synthesis-targets)=
## The four concrete next targets

**Target 1 — function-adapted stochastic localization.** For a fixed test function set $M_t(f)=\E_{p_t}f$, so that

```{math}
:label: eq:function-adapted-sde
\dd M_t(f)=\Cov_{p_t}(X,f)\cdot\dd W_t .
```

Current proofs bound the integrand by the worst case,

```{math}
:label: eq:worst-case-step
\abs{\Cov_{p_t}(X,f)}^2\le\norm{A_t}_\op\Var_{p_t}f ,
```

which discards essentially all information about $f$. A direct estimate of

```{math}
:label: eq:function-adapted-occupation
\int\frac{\abs{\Cov_{p_t}(X,f)}^2}{\Var_{p_t}f}\dd t
```

for a near-extremizing eigenfunction would avoid the top-eigenvalue entropy cost of [](#eq:logtraceexp) and would respect tensorization, since [](#eq:function-adapted-occupation) factorizes over independent blocks in a way that $\norm{A_t}_\op$ does not.

*In this manuscript:* this is exactly [](#q:mm-spectral-occupation), the headline of Approach S; the fixed-cut analogue is [](#q:upgrade), the operator-to-trace upgrade of Section [](#sec:open).

**Target 2 — a nonlinear extension of the moment-map estimate.** Brascamp–Lieb in moment-map coordinates already gives [](#eq:mm-brascamp-lieb), so KLS would follow from

```{math}
:label: eq:nonlinear-moment-map
\E\inner{\tau_\mu\nabla f}{\nabla f}\lesssim\E\abs{\nabla f}^2 .
```

The identity $\E\tau_\mu=I$ is insufficient, because $\tau_\mu(X)$ may correlate with $\nabla f(X)$. Letwin controls a deterministic $B$; the missing theorem must handle an $X$-dependent direction or matrix field.

*In this manuscript:* the deterministic moment-map approach, Approach C (Section [](#sec:moment-map-cmh)). [](#def:cmh) fixes the regular-class operator data and [](#thm:cmh-implies-affine-poincare) compares $\CPaff$ with $\CMH$; the constant-preserving passage to arbitrary log-concave limits is [](#q:cmh-approximation), which assumes the separate premise [](#ass:uniform-cmh-approximants). The remaining questions of the approach split into a construction layer ([](#q:mm-invariant-lift), [](#q:mm-square-root-commutator)) and a falsification layer ([](#conj:gate-zero), its sharp form [](#conj:gate-zero-sharp), and [](#q:cmh-solenoidal-perturbation)).

% Agent note: Route C is tracked by the `ap:c-…` approaches of research/program/portfolio.yaml.

Two cautions belong here rather than in Section [](#sec:moment-map-cmh), because they change how this target should be read. First, $\mathrm{CMH}(4)$ is *not* a reformulation of [](#eq:nonlinear-moment-map) or of [](#conj:kls): by [](#prop:cmh-hodge) it additionally demands control of a solenoidal excess that vanishes identically in dimension one under the no-flux convention. This exhibits an additional channel, not a strict separation: whether the two are equivalent at constant $4$ is not decided by it ([](#rem:cmh-stronger-than-kls)). Second, its cheapest necessary consequence, gate zero ([](#conj:gate-zero)), is itself an instance of the row above: in isotropic position it asks $\lmax(\E H^2)\le4$ where [](#thm:chen-klartag-moment-hessian) supplies only the trace bound $\Tr(\E H^2)\le2n$. Target 2 therefore does not escape the average-versus-uniform pattern; it relocates it, and [](#prop:letwin-not-gate-zero) shows the relocation is not free. Two further facts calibrate how hard that relocation is. The trace bound is attained, so the natural operator statement is the sharp form $\E H^2\preceq2\Id$ ([](#conj:gate-zero-sharp)), and its equality set already contains a non-product family, the exponential cones at $\beta=n$ ([](#prop:cone-linear-sector)). And the linear sector is exactly a third-moment statement plus a named remainder ([](#lem:linear-sector-third-moment)), so by [](#cor:gate-zero-third-moment) the sharp form implies $\kappa_n\le2$, sharper than the $\kappa_n\le2\sqrt2$ of [](#prop:letwin-kappa): proving it is at least as hard as a sharp directional third-moment bound. Refuting it, on the other hand, decides nothing about $\mathrm{CMH}(4)$, which needs only the constant $4$.

**Target 3 — replace log-trace-exp by an effective-rank estimate.** By [](#rem:log-is-entropy), the remaining $\log n$ enters *solely* because the soft maximum [](#eq:logtraceexp) approximates $\lmax$ over $n$ directions. A potential depending only on the directions actually relevant to a near-extremizer — or on an effective rank rather than the ambient dimension — would convert $\kappa_n=O(1)$ directly into $\CP=O(1)$.

*In this manuscript:* the interface functional $\Xi_T(\mu)$ of [](#eq:interface-def) and its evaluation in Section [](#sec:bootstrap) are this manuscript's version of the question, and [](#q:taming) is the corresponding statement. Section [](#sec:bootstrap) explains why the crude evaluation cannot suffice ([](#rem:insufficiency), [](#obs:crude-insufficient)) and relates a relative bound at a sufficiently small universal time to KLS ([](#thm:bootstrap)).

**Target 4 — extend parallel coupling beyond linear tilts.** Present parallel coupling controls the finite-dimensional family $e^{\inner\theta x}\mu(\dd x)$. A coupling for perturbations $(1+\eps f)\mu$ with cost controlled by $\int\abs{\nabla f}^2\dd\mu$ would address arbitrary spectral directions directly, rather than one linear family.

*In this manuscript:* no labelled statement formulates it yet. This is a gap in the approaches developed here, not in the literature survey, and it is recorded as such.

% Agent note: target 4 has no ledger node and no portfolio approach.

(subsec:synthesis-assessment)=
## Assessment

Of the four, target 1 is the best aligned with the known obstruction: it is the only one that avoids asking for a uniform top-covariance statement, and by Section [](#subsec:synthesis-constraint) such a statement is false for tensorized exponentials. That is a structural argument for its priority, not merely a preference.

Target 2 is conceptually deeper and may ultimately be cleaner, since [](#eq:nonlinear-moment-map) is a single inequality with no stochastic apparatus at all. But it requires controlling correlations with nonlinear gradient fields, which is a considerably stronger theorem than Letwin's fixed-matrix estimate — and the work on Approach C (Section [](#sec:moment-map-cmh)) locates the difficulty in a commutator sum, [](#q:mm-square-root-commutator), for which no dimension-free control is known.

Target 3 is the most narrowly technical and the most clearly delimited: the quantity to be removed is identified exactly, in one displayed inequality. It is also the one on which this manuscript establishes the most, including the obstruction to the crude evaluation (Section [](#sec:bootstrap)).

A final caution. Three of the four targets take $\kappa_n=O(1)$ as their starting point, and that input is an unreviewed version-1 preprint (Section [](#subsec:mm-audit)). Should it not survive review, targets 1–3 do not become wrong, but their premise reverts to $\CP\lesssim\log n$ and the arithmetic of every “remaining gap” claim in this section changes. This is why the preprint's result enters only through statements that display their own status, such as [](#prop:letwin-kappa), and why no statement proved here rests on it.

% Agent note: the ledger records this dependency through `import_class: preprint-unreviewed`, which cannot underlie a `proved` node; that mechanism, not this prose, enforces the distinction.
