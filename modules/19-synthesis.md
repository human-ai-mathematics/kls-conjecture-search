---
numbering:
  enumerator: "19.%s"
---

(sec:kls-synthesis)=
# Synthesis: what a proof of KLS now needs

Letwin's inputs [](#thm:letwin-moment-map), [](#thm:letwin-qcts), and [](#prop:letwin-kappa) isolate fixed-matrix, quadratic, and directional third-moment estimates. The general bound [](#thm:letwin-kls) combines these inputs with localization and retains a factor $\sqrt{\log n}$ in the Poincaré constant. Song and Zhang's preprint gives the sharper [](#thm:song-zhang-kls), through the polynomial–curvature loop of Chapter [](#sec:polynomial-curvature). Both conclusions cover general test functions; the remaining demand is a bound independent of dimension (Section [](#sec:kls-remaining)). Section [](#subsec:kls-reading-map) records, family by family, what is controlled and what is missing; this section turns that into five targets, each pointing to the labelled statement that carries it, where one exists.

(subsec:synthesis-constraint)=
## The constraint any proposal must satisfy

The covariance spike ([](#prop:covariance-spike), explained in Section [](#subsec:kls-spike-obstruction)) cuts in two directions. A direct “bound $\norm{A_t}_\op$ better” program cannot work, since the statement it needs is false; and rare spikes can be harmless, so a successful potential must recognize them rather than charge the full top eigenvalue whenever one occurs. The working criterion is the tensorization test of Section [](#subsec:kls-tensorization-test), the first thing to check on each target below.

(subsec:synthesis-targets)=
## The five concrete next targets

The targets are cross-cutting perspectives, not one per approach. Targets 1, 2 and 3 are the next steps of the fixed eigenfunction, the moment map and the fixed cut, and some of them bear on more than one approach; target 4, coupling, has no chapter here yet; target 5 works on the polynomial–curvature loop of Chapter [](#sec:polynomial-curvature), which is not one of this manuscript's approaches; and the conditional fibers, whose frame estimate is [](#conj:conditional-fiber-frame), have no target of their own.

**Target 1 — function-adapted stochastic localization.** For a fixed test function set $M_t(f)=\E_{p_t}f$, so that

```{math}
:label: eq:function-adapted-sde
\dd M_t(f)=\Cov_{p_t}(X,f)\cdot\dd W_t .
```

A covariance-based estimate bounds the integrand by the worst case,

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

*In this manuscript:* this is exactly [](#conj:mm-spectral-occupation), the central problem of the fixed-eigenfunction approach (Section [](#sec:spectral-approach)); the fixed-cut analogue is [](#conj:trace-upgrade), the operator-to-trace upgrade of Section [](#sec:open).

**Target 2 — a nonlinear extension of the moment-map estimate.** Brascamp–Lieb in moment-map coordinates already gives [](#eq:mm-brascamp-lieb), so KLS would follow from

```{math}
:label: eq:nonlinear-moment-map
\E\inner{\tau_\mu\nabla f}{\nabla f}\lesssim\E\abs{\nabla f}^2 .
```

The identity $\E\tau_\mu=I$ is insufficient, because $\tau_\mu(X)$ may correlate with $\nabla f(X)$. Letwin's fixed-matrix inequality controls a deterministic $B$; this proposed extension would need to handle an $X$-dependent direction or matrix field.

*In this manuscript:* the moment-map approach (Section [](#sec:moment-map-cmh)), whose target inequality $\mathrm{CMH}(4)$ ([](#def:cmh)) bounds the affine Poincaré constant by [](#thm:cmh-implies-affine-poincare). Two facts, both developed in that chapter, change how this target should be read. $\mathrm{CMH}(4)$ is not known to be a reformulation of [](#eq:nonlinear-moment-map) or of [](#conj:kls): it also charges a solenoidal excess ([](#prop:cmh-hodge), [](#cor:cmh-hodge-comparison)). And its cheapest necessary consequence, gate zero — the inequality tested on linear functions only ([](#conj:gate-zero)) — is itself an average-versus-uniform statement, which [](#prop:letwin-not-gate-zero) shows no fixed-matrix argument supplies: Target 2 relocates the difficulty rather than escaping it. How hard even the linear test is, [](#cor:gate-zero-third-moment) calibrates: the sharp form of gate zero implies $\kappa_n\le2$, so proving it is at least as hard as a sharp directional third-moment bound.

% Agent note: Route C is tracked by the `ap:c-…` approaches of research/program/portfolio.yaml.

**Target 3 — replace log-trace-exp by an effective-rank estimate.** In the localization–Lichnerowicz argument, [](#rem:log-is-entropy) attributes the $\log n$ cost to the fact that the soft maximum [](#eq:logtraceexp) approximates $\lmax$ over $n$ directions. A potential depending only on the directions actually relevant to a near-extremizer — or on an effective rank rather than the ambient dimension — would convert $\kappa_n=O(1)$ directly into $\CP=O(1)$.

*In this manuscript:* the interface functional $\Xi_T(\mu)$ of the fixed-cut approach, [](#eq:interface-def), and its evaluation in Section [](#sec:bootstrap) are this manuscript's version of the question, and [](#conj:taming) is the corresponding statement. Section [](#sec:bootstrap) explains why the crude evaluation cannot suffice ([](#rem:insufficiency), [](#rem:crude-insufficient)) and relates a relative bound at a sufficiently small universal time to KLS ([](#thm:bootstrap)).

**Target 4 — extend parallel coupling beyond linear tilts.** Present parallel coupling controls the finite-dimensional family $e^{\inner\theta x}\mu(\dd x)$. A coupling for perturbations $(1+\eps f)\mu$ with cost controlled by $\int\abs{\nabla f}^2\dd\mu$ would address arbitrary spectral directions directly, rather than one linear family.

*In this manuscript:* the coupling and the reason it stops at linear tilts are described in Chapter [](#sec:family-coupling); no labelled statement formulates the extension, and none of the four approaches carries it.

% Agent note: target 4 has no ledger node and no portfolio approach.

**Target 5 — reduce the losses of the polynomial–curvature loop.** In [](#thm:sz-iterated-curvature) each depth multiplies the profile constant by about $4$, which becomes $16^r$ in the Poincaré bound, and the depth must grow like $\log^*n$. The loss has three sources: tensor recovery (iterated derivative tensors are only approximately symmetric), which, through the centering losses it controls, sets the multiplier $4$; normalization, whose factors tend to one; and the initialization of low degrees, which imposes thresholds growing with the depth. The task is to tell which of these losses are necessary and which are artifacts of the comparison, and to reduce them while the admissibility thresholds stay uniform in the depth; reducing the multiplier alone while retaining those thresholds does not suffice (Section [](#sec:sz-profile-iteration)). The obstruction concerns the existing estimates: it does not exclude a different comparison with bounded cumulative multipliers. The missing ingredients are uniform conditional low-degree initialization and uniform control of the actual centering losses, including the start of the inverse-gradient sequence. Identifying those requirements supplies no new bound for KLS.

A first test is whether tensor recovery improves on the long sequences actually generated from a first eigenfunction, while their cumulative centering loss stays small. A loss necessary for arbitrary tensors need not be necessary on this class; conversely, a favourable one-step calculation does not control a long sequence. Products can be too symmetric to show the defect, so a calibration should couple coordinates and track both losses along the whole sequence.

The end point of this target has an exact form. By [](#prop:sz-exponential-coefficients-equivalence), KLS is equivalent to one exponential bound $c_k(\nu)\le A^k$ on the Appell coefficients of all regular isotropic log-concave measures. The order of quantifiers is the content: $A$ may depend neither on the degree, nor on the dimension, nor on the measure or its curvature bounds, so neither the factorial bound of [](#thm:sz-polynomial-variance) nor a base chosen afresh at each depth meets it. The Appell derivative identities and their tensor structure may give estimates that are less visible in the Poincaré inequality itself. Section [](#sec:sz-exponential-criterion) gives both directions with their constants.

*In this manuscript:* Chapter [](#sec:polynomial-curvature), whose final section shows where an improved curvature profile enters ([](#thm:sz-curvature-transfer)). No labelled statement formulates a reduced loss yet.

% Agent note: target 5 is tracked by ap:sz-recovery-probe in research/program/portfolio.yaml; it has no ledger node.

(subsec:synthesis-assessment)=
## Which target first

Section [](#subsec:atlas-assessment) sets the priorities and gives the reasons; in terms of the targets above they read as follows. Target 5 comes first: it works on the argument that reaches every test function with the slowest dimension dependence, and its losses are located, though its end point [](#prop:sz-exponential-coefficients-equivalence) is as hard as KLS. Then the decisive tests carried by target 2 (sharp gate zero) and by the conditional fibers. Then target 1, the best structurally motivated of the targets carried by this manuscript's approaches, whose first step is a comparison with the eigenfunction construction of target 5. Target 3 follows; target 4 remains exploratory, with no precise statement here.

(subsec:synthesis-caution)=
## Scope of the inputs

The starting point for targets 1–3 is the quadratic estimate [](#thm:letwin-qcts) and its directional consequence [](#prop:letwin-kappa). Their source is the pinned version-1 preprint described in Section [](#subsec:mm-audit); the badges on the statements record internal verification separately from that publication history. The Chen–Klartag imports concern the moment Hessian, radial variance, and full third tensor, rather than a dimension-free directional bound or control of arbitrary nonlinear tests.

The covariance consequence [](#cor:letwin-window) concerns fixed-time moments only up to $c/\log n$. Neither it nor the fixed-matrix estimate supplies a universal-time occupation bound, orientation control, or an adaptive matrix estimate. The implications [](#thm:carleson-implies-centroid), [](#thm:centroid-implies-kls), and [](#thm:intro-all-cut) retain their Carleson or centroid premises. The source's general KLS theorem, Letwin Theorem 1.1, is [](#thm:letwin-kls). Its minimum-time argument is explained in Section [](#sec:family-moment-map). It gives a dimension-dependent bound for all tests, without extending the covariance window to universal time or supplying gate zero.

Song–Zhang use the quadratic input in a different conversion, the polynomial–curvature loop of target 5. Neither their general bound nor its inverse-operator construction supplies the canonical moment-Hessian inequality, sharp gate zero, or the universal-time occupation estimate [](#conj:mm-spectral-occupation). The Carleson, centroid and approximation premises remain necessary in the implications that use them.

% Agent note: source versions describe provenance; badges and proof links carry verification status. Preserve explicit antecedents and dimension-dependent windows when updating this synthesis. Theorem 1.1 has its own proof link; its time-restricted bridge is separate from the matrix, quadratic, and covariance imports.
