---
numbering:
  enumerator: "21.%s"
---

(sec:kls-synthesis)=
# Synthesis: two proof mechanisms and structural questions

The polynomial method of Song and Zhang reached its first form in the first version of their preprint, an iterated-logarithm bound (Chapter [](#sec:polynomial-curvature)) [@SongZhang2026IteratedLogKLS]. Its second version proves KLS by repeated refinement with summable losses (Chapter [](#sec:sz-v2-proof)) [@SongZhang2026ConstantKLS]. Bizeul, Klartag and Lehec (BKL) prove it through dimension-free cumulant bounds and suspension, followed by the spectral criterion of the first version (Chapter [](#sec:bkl-proof)) [@BizeulKlartagLehec2026KLS]. Both proofs use the polynomial spectral foundation, but their closing estimates differ. Each reconstructed statement displays its status; how it was checked is explained on the [welcome page](#sec:overview-checking).

The question for the approaches below is what distinct mechanism or stronger property they can establish. Truth of KLS does not prove a sufficient condition for it. In particular the moment-Hessian, occupation and conditional-frame questions retain their own content. The five targets below describe that content and possible alternative proofs; the two proofs of KLS retain their separate provenance.

(subsec:synthesis-constraint)=
## The constraint any proposal must satisfy

The covariance spike ([](#prop:covariance-spike), explained in Section [](#subsec:kls-spike-obstruction)) cuts in two directions. A direct “bound $\norm{A_t}_\op$ better” program cannot work, since the statement it needs is false; and rare spikes can be harmless, so a successful potential must recognize them rather than charge the full top eigenvalue whenever one occurs. The working criterion is the tensorization test of Section [](#subsec:kls-tensorization-test), the first thing to check on each target below.

(subsec:synthesis-targets)=
## Five directions for further work

The targets are cross-cutting perspectives, not one per approach. Targets 1, 2 and 3 are the next steps of the fixed eigenfunction, the moment map and the fixed cut, and some of them bear on more than one approach; target 4 extends the coupling discussed in Chapter [](#sec:family-coupling), but has no precise extension statement here; target 5 works on the polynomial–curvature loop of Chapter [](#sec:polynomial-curvature), which is not one of this manuscript's approaches; and the conditional fibers, whose frame estimate is [](#conj:conditional-fiber-frame), have no target of their own.

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

*In this manuscript:* the moment-map approach (Section [](#sec:moment-map-cmh)), whose target inequality $\mathrm{CMH}(4)$ ([](#def:cmh)) bounds the affine Poincaré constant by [](#thm:cmh-implies-affine-poincare). Two facts, both developed in that chapter, change how this target should be read. $\mathrm{CMH}(4)$ is not known to be a reformulation of [](#eq:nonlinear-moment-map) or of [](#conj:kls): it also charges a solenoidal excess ([](#prop:cmh-hodge), [](#cor:cmh-hodge-comparison)). And its cheapest necessary consequence, the linear test — the inequality tested on linear functions only ([](#conj:gate-zero)) — is itself an average-versus-uniform statement, which [](#prop:letwin-not-gate-zero) shows no fixed-matrix argument supplies: Target 2 relocates the difficulty rather than escaping it. How hard even the linear test is, [](#cor:gate-zero-third-moment) calibrates: its sharp form implies $\kappa_n\le2$, so proving it is at least as hard as a sharp directional third-moment bound.

% Agent note: Route C is tracked by the `ap:c-…` approaches of research/program/portfolio.yaml.

**Target 3 — replace log-trace-exp by an effective-rank estimate.** In the localization–Lichnerowicz argument, [](#rem:log-is-entropy) attributes the $\log n$ cost to the fact that the soft maximum [](#eq:logtraceexp) approximates $\lmax$ over $n$ directions. A potential depending only on the directions actually relevant to a near-extremizer — or on an effective rank rather than the ambient dimension — would convert $\kappa_n=O(1)$ directly into $\CP=O(1)$.

*In this manuscript:* the interface functional $\Xi_T(\mu)$ of the fixed-cut approach, [](#eq:interface-def), and its evaluation in Section [](#sec:bootstrap) are this manuscript's version of the question, and [](#conj:taming) is the corresponding statement. Section [](#sec:bootstrap) explains why the crude evaluation cannot suffice ([](#rem:insufficiency), [](#rem:crude-insufficient)) and shows that a relative bound at a sufficiently small universal time would itself give KLS ([](#prop:ceiling)).

**Target 4 — extend parallel coupling beyond linear tilts.** Present parallel coupling controls the finite-dimensional family $e^{\inner\theta x}\mu(\dd x)$. A coupling for perturbations $(1+\eps f)\mu$ with cost controlled by $\int\abs{\nabla f}^2\dd\mu$ would address arbitrary spectral directions directly, rather than one linear family.

*In this manuscript:* the coupling and the reason it stops at linear tilts are described in Chapter [](#sec:family-coupling); no labelled statement formulates the extension, and none of the four approaches carries it.

% Agent note: target 4 has no ledger node and no portfolio approach.

**Target 5 — compare the repeated-refinement estimates with the earlier questions.**
The factor $16^r$ and growing admissibility thresholds of the first-version iteration
are limitations of those estimates, not unresolved requirements in the
literature after the second version. Chapter [](#sec:sz-v2-proof) explains the source's
replacement: polynomial depth cost, a common coefficient radius, repeated
height reduction, and finally a summable cost for the repetitions.

The finite-chain construction [](#prop:sz-v2-finite-chain-blocks) controls
centering losses, normalization and energy for one inverse-gradient
family, uniformly in the number of retained coefficient bounds. The
outer profiles, summable costs and final composition complete the
argument. BKL's coefficient theorem is not an input to it.

The older conditional-startup and near-unit-comparison questions retain
their exact normalization. The second version refines a common coefficient radius and
pays its fixed spectral conversion once, after all refinements. It does
not need a near-unit multiplier for the first-version comparison at each repetition.
Comparing the coefficient transfers must also account for their different
degree exponents and the older denominator $(d+1)^2$.

The earlier analysis correctly distinguished summable-loss arithmetic from
its missing estimates and identified the exponential coefficient end point
as KLS-strength in [](#prop:sz-exponential-coefficients-equivalence). It did
not supply either new proof mechanism. Section
[](#sec:sz-v2-methodological-comparison) records this comparison without a
claim of priority or a claim that the source satisfies every earlier
proposed interface literally.

(subsec:synthesis-assessment)=
## Which target first

With both proofs reconstructed, further work concerns comparison of their estimates, alternative proofs and structural inequalities. Section [](#subsec:atlas-assessment) distinguishes the exact polynomial comparison questions from structural tests: the sharp linear test of the moment-Hessian inequality, conditional frames on the simplex, occupation of a fixed eigenfunction and cut-dependent estimates. Neither proof discharges their sufficient conditions. Parallel coupling beyond linear tilts remains exploratory, without a precise statement here.

(subsec:synthesis-caution)=
## Scope of the inputs

The starting point for targets 1–3 is the quadratic estimate [](#thm:letwin-qcts) and its directional consequence [](#prop:letwin-kappa). Their source is the pinned version-1 preprint described in Section [](#subsec:mm-audit); the badges on the statements record internal verification separately from that publication history. The Chen–Klartag imports concern the moment Hessian, radial variance, and full third tensor, rather than a dimension-free directional bound or control of arbitrary nonlinear tests.

The covariance consequence [](#cor:letwin-window) concerns fixed-time moments only up to $c/\log n$. Neither it nor the fixed-matrix estimate supplies a universal-time occupation bound, orientation control, or an adaptive matrix estimate. The implications [](#thm:carleson-implies-centroid), [](#thm:centroid-implies-kls), and [](#thm:intro-all-cut) retain their Carleson or centroid premises. The source's general KLS theorem, Letwin Theorem 1.1, is [](#thm:letwin-kls). Its minimum-time argument is explained in Section [](#sec:family-moment-map). It gives a dimension-dependent bound for all tests, without extending the covariance window to universal time or supplying the linear test of the moment-Hessian inequality.

Song–Zhang use the quadratic input in a different conversion, the polynomial–curvature loop of target 5. Neither their general bound nor its inverse-operator construction supplies the canonical moment-Hessian inequality, its sharp linear test, or the universal-time occupation estimate [](#conj:mm-spectral-occupation). The Carleson, centroid and approximation premises remain necessary in the implications that use them.

% Agent note: source versions describe provenance; badges and proof links carry verification status. Preserve explicit antecedents and dimension-dependent windows when updating this synthesis. Theorem 1.1 has its own proof link; its time-restricted bridge is separate from the matrix, quadratic, and covariance imports.
