---
numbering:
  enumerator: "6.%s"
---

(sec:frontier-atlas)=
# The frontier at a glance

This section is the shortest complete answer to the questions a reader is most likely to arrive with: what is being tried, what has actually been established, what blocks each attempt, which natural variants are already dead, and which attempt currently looks best aligned with what is known. It is deliberately placed before any approach is developed. Everything in it is a pointer; the statements themselves live in the sections that develop the four approaches, each with its status displayed next to its title, and the detailed synthesis that revisits them after the approaches have been read is Section [](#sec:kls-synthesis).

(subsec:kls-reading-map)=
## The five families, side by side

(sec:kls-strategy-map)=

Sections [](#sec:family-needles)–[](#sec:family-transport) above survey the five families in a common format: object followed, what it buys, sharpest result, precise missing estimate, why it stalls, and which of the four approaches it enters. Collected:

| Family | Object followed | Present obstruction | Section |
|---|---|---|---|
| Classical needles | One-dimensional restrictions | Global isotropy is not inherited needle by needle | [](#sec:family-needles) |
| Stochastic localization | Mass, centroid, and covariance along a filtration | Controlling $\lmax(A_t)$ along the whole path; see [](#prop:covariance-spike) | [](#sec:family-sl) |
| Bochner, $H^{-1}$, heat flow | First eigenspace and derivative energies | Trace, coordinate, or averaged spectral information does not bound every slow mode | [](#sec:family-bochner) |
| Moment maps and Stein kernels | Hessian metric of the moment map | Correlation of the random Stein kernel with an arbitrary $\nabla f$ | [](#sec:family-moment-map) |
| Transport (Caffarelli, Föllmer, entropic barrier) | Transport Jacobian or conditional covariance | Dimension-free operator control in expectation | [](#sec:family-transport) |

(subsec:atlas-approaches)=
## The four approaches, side by side

The four approaches are this manuscript's own work. Each, named by the object it retains with a letter for short (S, C, E or F), and listed here in the order of the assessment below, is a response to Section [](#sec:kls-remaining), and each is reduced to an exactly stated estimate that is not settled here.

% Agent note: each approach is tracked in research/program/portfolio.yaml by ids carrying its letter; the portfolio is search state and carries no truth value.

| Approach | Object retained | What it would take to win | Section |
|---|---|---|---|
| Fixed eigenfunction (S) | Covariance tensor of a first spectral mode | Unwhiten for a universal time without losing tensor/covariance alignment ([](#conj:mm-spectral-occupation)) | [](#sec:spectral-approach) |
| Moment map (C) | Hessian metric, Haar fields, Schur fibers, Stein residuals | Freeze the endpoint and lift, prove an all-split reduction, control the global square-root commutator | [](#sec:moment-map-cmh) |
| Fixed cut (E) | Mass and two-color covariance of one candidate bottleneck set | Discharge the tight-prefix operator-to-trace upgrade [](#conj:trace-upgrade) (E–A), or replace both the global weight ruled out by [](#prop:weighted-spectator-obstruction) and the uniform superlinear remainder ruled out by [](#prop:spectator-excess-rate-obstruction) by a tensor-stable near-Cheeger package, and re-check its Stein trace (E–B) | [](#sec:introduction) |
| Conditional fibers (F) | One measure-dependent, test-independent isotropic frame of inverse-variance line resamplings | Prove a universal form gap, or decide the all-frame simplex dual; the natural root frame fails by [](#prop:conditional-fiber-root-obstruction) | [](#sec:conditional-fiber-frame) |

(subsec:atlas-external-reading)=
## Suggested external reading order

For a reader coming to the subject rather than to this manuscript: [@KannanLovaszSimonovits1995] for the conjecture and deterministic localization; [@Eldan2013ThinShell] for stochastic localization and the third-moment parameter; [@LeeVempala2018; @LeeVempala2024] for the cleanest entry to the covariance SDE and the set-transfer argument; [@KLnotes] for the best conceptual exposition of localization, filtering, Bochner, and the operator-norm obstruction; [@KlartagLehec2022Polylog] for heat flow, spectral measures, and $H^{-1}$; [@Klartag2023Logarithmic] for improved Lichnerowicz and the published bound; [@Letwin2026QuadraticKLS] for the current preprint record; and [@KlartagLehec2025ThinShell; @ChenKlartag2026SharpThinShell] for the strongest related tools and the clearest illustration of the quadratic-to-all-functions gap.

(subsec:atlas-state)=
## What each approach gives, and what blocks it

The tables above say what each approach *tries*. This one says where each has got to. Read the middle column as the approach's own contribution and the right column as the precise statement whose absence stops it; each entry points at a labelled statement, whose status is displayed where it is stated.

| Approach | What it gives | What blocks it |
|---|---|---|
| Fixed eigenfunction (S) | The exact fixed-function SDE and the initial-layer window chain, which gives the occupation estimate on the published polylogarithmic covariance window, [](#prop:mm-window-occupation) (Section [](#sec:spectral-approach)) | [](#conj:mm-spectral-occupation): unwhiten for a *universal* time without losing tensor/covariance alignment |
| Moment map (C) | The endpoint given precise operator data ([](#def:cmh)), compared with the affine Poincaré constant by [](#thm:cmh-implies-affine-poincare), and computed exactly on the line, on products, on every log-concave Dirichlet law, and — in its linear sector only — on the exponential cones, which are its first non-product equality set (Section [](#sec:cmh-exact-cases)); that sector is resolved into a directional third moment plus a named remainder ([](#lem:linear-sector-third-moment)) | A construction layer ([](#conj:mm-invariant-lift), and [](#conj:mm-square-root-commutator): the global square-root commutator sum) and a falsification layer ([](#conj:gate-zero), its sharp form [](#conj:gate-zero-sharp), [](#conj:cmh-second-variation)) |
| Fixed cut (E) | The bootstrap comparison and the interface functional (Section [](#sec:bootstrap)), with the insufficiency of the crude evaluation ([](#rem:crude-insufficient)); the coordinate budgets and the covariance reduction of the product stress test (Section [](#sec:product-stress)) | The tight-prefix operator-to-trace upgrade [](#conj:trace-upgrade) (Section [](#sec:open)); on branch E–B, a tensor-stable replacement for the weighted package that [](#prop:weighted-spectator-obstruction) rules out |
| Conditional fibers (F) | The frame is constructed, and the natural simplex root frame is ruled out by [](#prop:conditional-fiber-root-obstruction) (Section [](#sec:conditional-fiber-frame)) | A universal form gap on the maximal closed form domain, or a decision on the all-frame simplex dual; the degree-two floors of [](#lem:fiber-root-degree-two) exclude every degree-two counterexample sequence, so a dual certificate must have degree at least three |

(subsec:atlas-barriers)=
## What is already ruled out

Negative results are the most reusable part of a search, and four of them constrain everything above. Each is stated in its own section; they are collected here so that a reader does not rediscover a dead variant.

- **No uniform operator-norm covariance bound.** [](#prop:covariance-spike): the statement a direct “bound $\norm{A_t}_\op$ better” programme would need is false, for a measure that satisfies KLS.

- **The global weighted package fails.** [](#prop:weighted-spectator-obstruction) kills the global operator-norm covariance weight of branch E–B; its status is displayed at [](#conj:weighted-excess-rate).

- **No matrix-moment argument supplies gate zero.** [](#prop:letwin-not-gate-zero): the fixed-matrix estimate does not close the linear sector of Approach C, so Target 2 relocates the average-versus-uniform difficulty rather than escaping it.

- **The natural conditional-fiber root frame fails.** Approach F's most obvious implementation is ruled out by [](#prop:conditional-fiber-root-obstruction), which is why the approach is stated in terms of an all-frame question, [](#conj:conditional-fiber-frame), instead.

Two further cautions are advisory rather than established: the two-tail obstruction ([](#rem:two-tail-slice-bounds)) and the circularity warning of Section [](#sec:excess). They are recorded as remarks for exactly that reason: they guide work, but no statement here is excluded on their strength.

(subsec:atlas-assessment)=
## Assessment of priorities

Of the four approaches, Approach S is the one best aligned with the known obstruction: it is the only one that avoids asking for a uniform top-covariance statement, and by Section [](#subsec:kls-spike-obstruction) such a statement is false for tensorized exponentials. That is a structural argument for its priority, not a preference.

Approach C is conceptually deeper and may ultimately be cleaner, since its endpoint is a single inequality with no stochastic apparatus at all — but the work on it here shows its difficulty concentrating in a commutator sum, [](#conj:mm-square-root-commutator), for which no dimension-free control is known. Approach E is the most narrowly technical and the most clearly delimited, and it is the one on which this manuscript establishes the most, including the negative results. Approach F is the youngest; its natural implementation fails ([](#prop:conditional-fiber-root-obstruction)), and what remains is a single question, [](#conj:conditional-fiber-frame), rather than a programme.

One caution belongs beside all four. Three of the four targets of Section [](#sec:kls-synthesis) take $\kappa_n=O(1)$ as their starting point, and that input is an unreviewed version-1 preprint. Should it not survive review, the targets do not become wrong, but their premise reverts to $\CP\lesssim\log n$ and the arithmetic of every “remaining gap” claim changes. This is why the preprint's result enters only through statements such as [](#prop:letwin-kappa) that display their own status, and why no statement proved here rests on it.
