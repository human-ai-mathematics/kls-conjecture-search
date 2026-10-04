---
numbering:
  enumerator: "7.%s"
---

(sec:frontier-atlas)=
# The frontier at a glance

This section is the comparative map: what each family of methods controls and what it misses, what each of the four approaches tries, what it has established and what blocks it, which natural variants are already dead, and where to start. It is deliberately placed before any approach is developed. Everything in it is a pointer: the reasons are given where the overview explains the obstacle (Section [](#sec:kls-remaining)), the full development of each approach is in its entry chapter, and what a proof now needs is Section [](#sec:kls-synthesis).

(subsec:kls-reading-map)=
## The families of methods, side by side

(sec:kls-strategy-map)=

Sections [](#sec:family-needles)–[](#sec:polynomial-curvature) survey six families of methods, from classical needles to the polynomial–curvature iteration. The table collects what each controls and the estimate still missing, together with the parallel coupling behind the thin-shell theorem:

| Family | What is now controlled | The missing estimate | Section |
|---|---|---|---|
| Classical needles | One-dimensional conditional measures, sharply | A decomposition inheriting *operator* covariance: global isotropy is not inherited needle by needle | [](#sec:family-needles) |
| Stochastic localization | Short-time covariance and the directional third-moment estimate [](#prop:letwin-kappa) | Control of $\lmax(A_t)$ along the whole path without the $\log n$ cost of a soft maximum; see [](#prop:covariance-spike) | [](#sec:family-sl) |
| Bochner, $H^{-1}$, heat flow | Coordinate and quadratic spectral mass of the first eigenspace | Uniform estimates for the derivatives of an arbitrary $f$: trace, coordinate or averaged spectral information does not bound every slow mode | [](#sec:family-bochner) |
| Moment maps and Stein kernels | Fixed deterministic matrix energies $\E\Tr(BHBH)$; and, exactly, $\CMH$ on the line, on products and on every log-concave Dirichlet law ([](#sec:cmh-exact-cases)) | Control when the matrix or direction depends on $X$ or on $f$, that is, the correlation of the random Stein kernel with an arbitrary $\nabla f$. Even the linear sector is missing: $\lmax(\E H^2)\le4$ does not follow from $\Tr(\E H^2)\le2n$ ([](#prop:letwin-not-gate-zero)) | [](#sec:family-moment-map) |
| Parallel coupling | Linear exponential tilts $e^{\inner\theta x}\mu$ | Couplings for arbitrary functional perturbations | [](#subsec:kls-solved-neighbours) |
| Transport (Caffarelli, Föllmer, entropic barrier) | Polylogarithmic averaged derivative bounds | A dimension-free expected operator derivative | [](#sec:family-transport) |
| Polynomial estimates and curvature | An iterated-logarithm bound for all test functions, through polynomial–curvature feedback | Uniform control of the depth-dependent losses; equivalently, a universal exponential bound on the Appell coefficients | [](#sec:polynomial-curvature) |

These families repeatedly meet the difference between fixed or averaged control and control of an object selected by the measure or an extremal function (Section [](#subsec:kls-adaptive-residue)). The last one gets around it: Song–Zhang's comparison [](#thm:sz-curvature-comparison) reaches every test function by controlling the centering and symmetry errors of an eigenfunction iteration, and its remaining cost is the growth with depth of the constants in [](#thm:sz-iterated-curvature).

(subsec:atlas-approaches)=
## The four approaches, side by side

The four approaches are this manuscript's own work. Each is named by the object it retains — the fixed eigenfunction, the moment map, the fixed cut and conditional fibers — with no claim that their order measures their prospects. Each responds to the obstacle of Section [](#sec:kls-remaining); the table in Section [](#subsec:atlas-state) points to the estimate each approach seeks.

% Agent note: each approach is tracked in research/program/portfolio.yaml by ids carrying its letter; the portfolio is search state and carries no truth value.

| Approach | Object retained | The idea in one line | Section |
|---|---|---|---|
| Fixed eigenfunction | Covariance tensor of a first spectral mode | Follow a first eigenfunction through stochastic localization; one occupation estimate then gives KLS ([](#prop:spectral-sufficiency)) | [](#sec:spectral-approach) |
| Moment map | Hessian metric of the moment map, Haar fields, Schur fibers | Prove one deterministic inequality for the moment-map Hessian, $\mathrm{CMH}(4)$, which bounds the affine Poincaré constant ([](#thm:cmh-implies-affine-poincare)) | [](#sec:moment-map-cmh) |
| Fixed cut | Mass and two-colour covariance of one candidate bottleneck set | Follow one balanced set through stochastic localization; KLS follows if it cannot be identified before a universal time ([](#lem:survival-implies-kls)) | [](#sec:introduction) |
| Conditional fibers | One isotropic frame of line resamplings, chosen from the measure before the test function | A dimension-free gap for the resampling form gives KLS with constant $4C$ ([](#lem:conditional-fiber-form)) | [](#sec:conditional-fiber-frame) |

(subsec:atlas-state)=
## What each approach gives, and what blocks it

The table above says what each approach *tries*; this one says where each has got to. The middle column is the approach's own contribution, the right column the statement whose absence stops it; the full account of both is the opening summary of each entry chapter, and each statement displays its status where it is stated.

| Approach | What it gives | What blocks it |
|---|---|---|
| Fixed eigenfunction | The exact fixed-function equation and the stopped source estimate [](#lem:mm-stopped-window-source); the small-gap implication [](#prop:mm-window-occupation) has an empty admissible class | Source occupation on a universal time interval, [](#conj:mm-spectral-occupation) |
| Moment map | The target inequality given precise operator data ([](#def:cmh)) and compared with the affine Poincaré constant ([](#thm:cmh-implies-affine-poincare)); exact values on the line, on products and on every log-concave Dirichlet law; the linear sector resolved into a directional third moment ([](#lem:linear-sector-third-moment)), with the exponential cones as its first non-product equality set | Constructing the proof: the invariant multiplier lift ([](#conj:mm-invariant-lift)) — how a multiplier defined on one block of a Schur split acts on the whole space — and the global square-root commutator ([](#conj:mm-square-root-commutator)). Testing it: gate zero ([](#conj:gate-zero), sharp form [](#conj:gate-zero-sharp)) and the second variation at the product ([](#conj:cmh-second-variation)) |
| Fixed cut | The bootstrap comparison and its interface functional ([](#thm:bootstrap)), the insufficiency of the crude evaluation ([](#rem:crude-insufficient)) and the ceiling [](#prop:ceiling); the coordinate budgets of the product stress test (Section [](#sec:product-stress)) | For the all-cut variant, the operator-to-trace upgrade [](#conj:trace-upgrade); for the near-Cheeger variant, a tensor-stable replacement for the weighted package that [](#prop:weighted-spectator-obstruction) rules out |
| Conditional fibers | The resampling form, closed and compared with the gradient ([](#lem:conditional-fiber-form)); the natural simplex frame ruled out ([](#prop:conditional-fiber-root-obstruction)) | A universal form gap, [](#conj:conditional-fiber-frame), or a decision on the all-frame simplex dual, whose certificates must have degree at least three ([](#lem:fiber-root-degree-two)) |

(subsec:atlas-barriers)=
## What is already ruled out

Negative results are the most reusable part of a search, and four of them constrain everything above. Each is stated and explained in its own section; they are collected here so that a reader does not rediscover a dead variant.

- **No uniform operator-norm covariance bound.** [](#prop:covariance-spike): the statement a direct “bound $\norm{A_t}_\op$ better” program would need is false, for a measure that satisfies KLS (Section [](#subsec:kls-spike-obstruction)).

- **Independent spectators and global covariance weights.** [](#prop:weighted-spectator-obstruction) supplies the product-cylinder witnesses relevant to [](#ass:weighted-package) and [](#conj:weighted-excess-rate).

- **No matrix-moment argument supplies gate zero.** Gate zero is the moment-Hessian inequality tested on linear functions only, the cheapest test any proof of it must pass. [](#prop:letwin-not-gate-zero): the fixed-matrix estimate does not supply it, so the moment-map approach relocates the average-versus-uniform difficulty rather than escaping it.

- **The natural conditional-fiber root frame fails.** The most obvious implementation of the conditional-fiber approach is ruled out by [](#prop:conditional-fiber-root-obstruction), which is why the approach is stated as an all-frame question, [](#conj:conditional-fiber-frame).

Two further cautions are advisory rather than established: the two-tail obstruction ([](#rem:two-tail-slice-bounds)) and the circularity warning of Section [](#sec:excess). They are recorded as remarks for exactly that reason: they guide work, but no statement here is excluded on their strength.

(subsec:atlas-assessment)=
## Assessment of priorities

**The most immediate question is the loss of the polynomial–curvature iteration.** It is the argument that reaches every test function with the slowest dimension dependence, $16^{\log^*(n+2)}$, and its loss is located: the factor $4$ per depth in [](#thm:sz-iterated-curvature) is the square root of the comparison constant $16$, set by tensor recovery (the recovery inequality that bounds the mass lost to centering costs a central binomial coefficient), while normalization contributes factors tending to one and the initialization of low degrees imposes admissibility thresholds that grow with the depth. Reducing these losses while keeping admissibility uniform in the depth is the task (why the multiplier alone does not suffice is Section [](#sec:sz-profile-iteration)), and its exact end point is the coefficient criterion [](#prop:sz-exponential-coefficients-equivalence). Target 5 of Section [](#subsec:synthesis-targets) describes how to start.

**Among the four approaches of this manuscript, the fixed eigenfunction is the best structurally motivated.** It retains the function responsible for a small spectral gap, and so passes the tensorization test of Section [](#subsec:kls-tensorization-test): a covariance spike in a direction the eigenfunction does not use costs it nothing, where a bound on the top covariance eigenvalue charges every spike. What it still needs is [](#conj:mm-spectral-occupation). This is a judgement of motivation, not of difficulty: the moment-map and conditional-fiber approaches also avoid a pathwise bound on the top eigenvalue, and nothing above excludes them.

The polynomial–curvature argument also changes what each approach is measured against:

| Approach | What the polynomial–curvature argument changes | What still needs its own estimate |
|---|---|---|
| Fixed eigenfunction | A second way to use an extremal eigenfunction: polynomial control of centering losses instead of a universal-time source occupation | [](#conj:mm-spectral-occupation); the spectral comparison does not estimate the stochastic source |
| Moment map | The quadratic input feeds a higher-degree argument that reaches all functions without the moment-Hessian inequality | Gate zero [](#conj:gate-zero) and the commutator [](#conj:mm-square-root-commutator), which the general bound does not imply |
| Fixed cut | A sharper general bound against which improved cut estimates are measured | [](#conj:trace-upgrade) and a spectator-inert replacement for the weighted package; [](#prop:weighted-spectator-obstruction) still applies |
| Conditional fibers | An all-function comparison through polynomial tensors, to set beside what a resampling form retains | [](#conj:conditional-fiber-frame); the polynomial comparison constructs no frame, and the root-frame obstruction still applies |

Several inputs above come from the preprints discussed in Section [](#subsec:synthesis-caution); the conditional implications of the four approaches keep their premises.

(subsec:atlas-external-reading)=
## Suggested external reading order

For a reader coming to the subject rather than to this manuscript: [@KannanLovaszSimonovits1995] for the conjecture and deterministic localization; [@Eldan2013ThinShell] for stochastic localization and the third-moment parameter; [@LeeVempala2018; @LeeVempala2024] for the cleanest entry to the covariance SDE and the set-transfer argument; [@KLnotes] for the best conceptual exposition of localization, filtering, Bochner, and the operator-norm obstruction; [@KlartagLehec2022Polylog] for heat flow, spectral measures, and $H^{-1}$; [@Klartag2023Logarithmic] for improved Lichnerowicz and the published bound; [@Letwin2026QuadraticKLS] for the quadratic input and its localization consequences; [@SongZhang2026IteratedLogKLS] for the October preprint's polynomial–curvature iteration, developed in Chapter [](#sec:polynomial-curvature); and [@KlartagLehec2025ThinShell; @ChenKlartag2026SharpThinShell] for the strongest related tools and the clearest illustration of the quadratic-to-all-functions gap.
