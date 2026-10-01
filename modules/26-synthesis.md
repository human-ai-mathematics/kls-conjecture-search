---
numbering:
  enumerator: "26.%s"
---

(sec:kls-synthesis)=
# Synthesis: what a proof of KLS now needs

The July 2026 inputs [](#thm:letwin-moment-map), [](#thm:letwin-qcts), and [](#prop:letwin-kappa) isolate fixed-matrix, quadratic, and directional third-moment estimates. The general bound [](#thm:letwin-kls) combines these inputs with localization and retains a factor $\sqrt{\log n}$ in the Poincaré constant. The difficulty addressed here is their promotion to uniform control of every nonlinear test function (Section [](#sec:kls-remaining)). Section [](#subsec:kls-reading-map) records, family by family, what is controlled and what is missing; this section says what a proof must therefore look like, and names four concrete next targets, each mapped to the labelled statement of this manuscript that carries it, where one exists.

(subsec:synthesis-constraint)=
## The constraint any proposal must satisfy

The covariance spike ([](#prop:covariance-spike), explained in Section [](#subsec:kls-spike-obstruction)) cuts in two directions. A direct “bound $\norm{A_t}_\op$ better” program cannot work, since the statement it needs is false; and rare spikes can be harmless, so a successful potential must recognize them rather than charge the full top eigenvalue whenever one occurs. The working criterion is the tensorization test of Section [](#subsec:kls-tensorization-test), the first thing to check on each target below.

(subsec:synthesis-targets)=
## The four concrete next targets

The targets are cross-cutting perspectives, not one per approach. Targets 1, 2 and 3 are the next steps of the fixed eigenfunction, the moment map and the fixed cut, and some of them bear on more than one approach; target 4, coupling, has no chapter here yet; and the conditional fibers, whose frame estimate is [](#conj:conditional-fiber-frame), have no target of their own.

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

*In this manuscript:* this is exactly [](#conj:mm-spectral-occupation), the central problem of the fixed-eigenfunction approach (Section [](#sec:spectral-approach)); the fixed-cut analogue is [](#conj:trace-upgrade), the operator-to-trace upgrade of Section [](#sec:open).

**Target 2 — a nonlinear extension of the moment-map estimate.** Brascamp–Lieb in moment-map coordinates already gives [](#eq:mm-brascamp-lieb), so KLS would follow from

```{math}
:label: eq:nonlinear-moment-map
\E\inner{\tau_\mu\nabla f}{\nabla f}\lesssim\E\abs{\nabla f}^2 .
```

The identity $\E\tau_\mu=I$ is insufficient, because $\tau_\mu(X)$ may correlate with $\nabla f(X)$. Letwin controls a deterministic $B$; the missing theorem must handle an $X$-dependent direction or matrix field.

*In this manuscript:* the moment-map approach (Section [](#sec:moment-map-cmh)), whose target inequality $\mathrm{CMH}(4)$ ([](#def:cmh)) bounds the affine Poincaré constant by [](#thm:cmh-implies-affine-poincare). Two facts, both developed in that chapter, change how this target should be read. $\mathrm{CMH}(4)$ is not known to be a reformulation of [](#eq:nonlinear-moment-map) or of [](#conj:kls): it also charges a solenoidal excess ([](#prop:cmh-hodge), [](#cor:cmh-hodge-comparison)). And its cheapest necessary consequence, gate zero — the inequality tested on linear functions only ([](#conj:gate-zero)) — is itself an average-versus-uniform statement, which [](#prop:letwin-not-gate-zero) shows no fixed-matrix argument supplies: Target 2 relocates the difficulty rather than escaping it. How hard even the linear test is, [](#cor:gate-zero-third-moment) calibrates: the sharp form of gate zero implies $\kappa_n\le2$, so proving it is at least as hard as a sharp directional third-moment bound.

% Agent note: Route C is tracked by the `ap:c-…` approaches of research/program/portfolio.yaml.

**Target 3 — replace log-trace-exp by an effective-rank estimate.** By [](#rem:log-is-entropy), the remaining $\log n$ enters *solely* because the soft maximum [](#eq:logtraceexp) approximates $\lmax$ over $n$ directions. A potential depending only on the directions actually relevant to a near-extremizer — or on an effective rank rather than the ambient dimension — would convert $\kappa_n=O(1)$ directly into $\CP=O(1)$.

*In this manuscript:* the interface functional $\Xi_T(\mu)$ of the fixed-cut approach, [](#eq:interface-def), and its evaluation in Section [](#sec:bootstrap) are this manuscript's version of the question, and [](#conj:taming) is the corresponding statement. Section [](#sec:bootstrap) explains why the crude evaluation cannot suffice ([](#rem:insufficiency), [](#rem:crude-insufficient)) and relates a relative bound at a sufficiently small universal time to KLS ([](#thm:bootstrap)).

**Target 4 — extend parallel coupling beyond linear tilts.** Present parallel coupling controls the finite-dimensional family $e^{\inner\theta x}\mu(\dd x)$. A coupling for perturbations $(1+\eps f)\mu$ with cost controlled by $\int\abs{\nabla f}^2\dd\mu$ would address arbitrary spectral directions directly, rather than one linear family.

*In this manuscript:* no labelled statement formulates it yet. This is a gap in the approaches developed here, not in the literature survey, and it is recorded as such.

% Agent note: target 4 has no ledger node and no portfolio approach.

(subsec:synthesis-assessment)=
## Which target first

The order of priority among targets 1, 2 and 3 is the order of the approaches argued in Section [](#subsec:atlas-assessment): target 1 first, because it is the only one that never asks for a uniform top-covariance bound. Target 4 has no approach behind it yet.

(subsec:synthesis-caution)=
## Scope of the inputs

The starting point for targets 1–3 is the quadratic estimate [](#thm:letwin-qcts) and its directional consequence [](#prop:letwin-kappa). Their source is the pinned version-1 preprint described in Section [](#subsec:mm-audit); the badges on the statements record internal verification separately from that publication history. The Chen–Klartag imports concern the moment Hessian, radial variance, and full third tensor, rather than a dimension-free directional bound or control of arbitrary nonlinear tests.

The covariance consequence [](#cor:letwin-window) concerns fixed-time moments only up to $c/\log n$. Neither it nor the fixed-matrix estimate supplies a universal-time occupation bound, orientation control, or an adaptive matrix estimate. The implications [](#thm:carleson-implies-centroid), [](#thm:centroid-implies-kls), and [](#thm:intro-all-cut) retain their Carleson or centroid premises. The source's general KLS theorem, Letwin Theorem 1.1, is [](#thm:letwin-kls). Its minimum-time argument is explained in Section [](#sec:family-moment-map). It gives a dimension-dependent bound for all tests, without extending the covariance window to universal time or supplying gate zero.

% Agent note: source versions describe provenance; badges and proof links carry verification status. Preserve explicit antecedents and dimension-dependent windows when updating this synthesis. Theorem 1.1 has its own proof link; its time-restricted bridge is separate from the matrix, quadratic, and covariance imports.
