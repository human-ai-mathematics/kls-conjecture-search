---
numbering:
  enumerator: "6.%s"
---

(sec:frontier-atlas)=
# The frontier at a glance

This section is the comparative map: what each family of methods controls and what it misses, what each of the four approaches tries, what it has established and what blocks it, which natural variants are already dead, and which approach currently looks best aligned with what is known. It is deliberately placed before any approach is developed. Everything in it is a pointer: the reasons are given where the overview explains the obstacle (Section [](#sec:kls-remaining)), the full development of each approach is in its entry chapter, and what a proof now needs is Section [](#sec:kls-synthesis).

(subsec:kls-reading-map)=
## The families of methods, side by side

(sec:kls-strategy-map)=

Sections [](#sec:family-needles)–[](#sec:family-transport) survey the five families in a common format: object followed, what it buys, sharpest result, precise missing estimate, why it stalls, and which of the four approaches it enters. Collected, together with the parallel coupling behind the thin-shell theorem:

| Family | What is now controlled | The missing estimate | Section |
|---|---|---|---|
| Classical needles | One-dimensional conditional measures, sharply | A decomposition inheriting *operator* covariance: global isotropy is not inherited needle by needle | [](#sec:family-needles) |
| Stochastic localization | Short-time covariance and, conditionally on the 2026 preprint, sharp third moments | Control of $\lmax(A_t)$ along the whole path without the $\log n$ cost of a soft maximum; see [](#prop:covariance-spike) | [](#sec:family-sl) |
| Bochner, $H^{-1}$, heat flow | Coordinate and quadratic spectral mass of the first eigenspace | Uniform estimates for the derivatives of an arbitrary $f$: trace, coordinate or averaged spectral information does not bound every slow mode | [](#sec:family-bochner) |
| Moment maps and Stein kernels | Fixed deterministic matrix energies $\E\Tr(BHBH)$; and, exactly, $\CMH$ on the line, on products and on every log-concave Dirichlet law ([](#sec:cmh-exact-cases)) | Control when the matrix or direction depends on $X$ or on $f$, that is, the correlation of the random Stein kernel with an arbitrary $\nabla f$. Even the linear sector is missing: $\lmax(\E H^2)\le4$ does not follow from $\Tr(\E H^2)\le2n$ ([](#prop:letwin-not-gate-zero)) | [](#sec:family-moment-map) |
| Parallel coupling | Linear exponential tilts $e^{\inner\theta x}\mu$ | Couplings for arbitrary functional perturbations | [](#subsec:kls-solved-neighbours) |
| Transport (Caffarelli, Föllmer, entropic barrier) | Polylogarithmic averaged derivative bounds | A dimension-free expected operator derivative | [](#sec:family-transport) |

Every row is the same sentence in a different dialect — something is controlled on average, or for a fixed object, where KLS needs it uniformly for an object that adapts — and Section [](#subsec:kls-adaptive-residue) explains why that is the obstacle.

(subsec:atlas-approaches)=
## The four approaches, side by side

The four approaches are this manuscript's own work. Each is named by the object it retains, with a letter for short — the fixed eigenfunction (S), the moment map (C), the fixed cut (E) and conditional fibers (F) — and they are listed in the order of the assessment below. Each responds to the obstacle of Section [](#sec:kls-remaining), and each is reduced to an exactly stated estimate that is not settled here.

% Agent note: each approach is tracked in research/program/portfolio.yaml by ids carrying its letter; the portfolio is search state and carries no truth value.

| Approach | Object retained | The idea in one line | Section |
|---|---|---|---|
| Fixed eigenfunction (S) | Covariance tensor of a first spectral mode | Follow a first eigenfunction through stochastic localization; one occupation estimate then gives KLS ([](#prop:spectral-sufficiency)) | [](#sec:spectral-approach) |
| Moment map (C) | Hessian metric of the moment map, Haar fields, Schur fibers | Prove one deterministic inequality for the moment-map Hessian, $\mathrm{CMH}(4)$, which bounds the affine Poincaré constant ([](#thm:cmh-implies-affine-poincare)) | [](#sec:moment-map-cmh) |
| Fixed cut (E) | Mass and two-colour covariance of one candidate bottleneck set | Follow one balanced set through stochastic localization; KLS follows if it cannot be identified before a universal time ([](#lem:survival-implies-kls)) | [](#sec:introduction) |
| Conditional fibers (F) | One isotropic frame of line resamplings, chosen from the measure before the test function | A dimension-free gap for the resampling form gives KLS with constant $4C$ ([](#lem:conditional-fiber-form)) | [](#sec:conditional-fiber-frame) |

(subsec:atlas-state)=
## What each approach gives, and what blocks it

The table above says what each approach *tries*; this one says where each has got to. The middle column is the approach's own contribution, the right column the statement whose absence stops it; the full account of both is the opening summary of each entry chapter, and each statement displays its status where it is stated.

| Approach | What it gives | What blocks it |
|---|---|---|
| Fixed eigenfunction (S) | The exact fixed-function equation, and the occupation estimate on the published polylogarithmic covariance window ([](#prop:mm-window-occupation)) | The same estimate for a *universal* time, [](#conj:mm-spectral-occupation) |
| Moment map (C) | The target inequality given precise operator data ([](#def:cmh)) and compared with the affine Poincaré constant ([](#thm:cmh-implies-affine-poincare)); exact values on the line, on products and on every log-concave Dirichlet law; the linear sector resolved into a directional third moment ([](#lem:linear-sector-third-moment)), with the exponential cones as its first non-product equality set | Constructing the proof: the invariant multiplier lift ([](#conj:mm-invariant-lift)) — how a multiplier defined on one block of a Schur split acts on the whole space — and the global square-root commutator ([](#conj:mm-square-root-commutator)). Testing it: gate zero ([](#conj:gate-zero), sharp form [](#conj:gate-zero-sharp)) and the second variation at the product ([](#conj:cmh-second-variation)) |
| Fixed cut (E) | The bootstrap comparison and its interface functional ([](#thm:bootstrap)), the insufficiency of the crude evaluation ([](#rem:crude-insufficient)) and the ceiling [](#prop:ceiling); the coordinate budgets of the product stress test (Section [](#sec:product-stress)) | On variant E–A, the operator-to-trace upgrade [](#conj:trace-upgrade); on variant E–B, a tensor-stable replacement for the weighted package that [](#prop:weighted-spectator-obstruction) rules out |
| Conditional fibers (F) | The resampling form, closed and compared with the gradient ([](#lem:conditional-fiber-form)); the natural simplex frame ruled out ([](#prop:conditional-fiber-root-obstruction)) | A universal form gap, [](#conj:conditional-fiber-frame), or a decision on the all-frame simplex dual, whose certificates must have degree at least three ([](#lem:fiber-root-degree-two)) |

(subsec:atlas-barriers)=
## What is already ruled out

Negative results are the most reusable part of a search, and four of them constrain everything above. Each is stated and explained in its own section; they are collected here so that a reader does not rediscover a dead variant.

- **No uniform operator-norm covariance bound.** [](#prop:covariance-spike): the statement a direct “bound $\norm{A_t}_\op$ better” program would need is false, for a measure that satisfies KLS (Section [](#subsec:kls-spike-obstruction)).

- **The global weighted package fails.** [](#prop:weighted-spectator-obstruction) rules out the global operator-norm covariance weight of variant E–B of the fixed cut; its status is displayed at [](#conj:weighted-excess-rate).

- **No matrix-moment argument supplies gate zero.** Gate zero is the moment-Hessian inequality tested on linear functions only, the cheapest test any proof of it must pass. [](#prop:letwin-not-gate-zero): the fixed-matrix estimate does not supply it, so the moment-map approach relocates the average-versus-uniform difficulty rather than escaping it.

- **The natural conditional-fiber root frame fails.** The most obvious implementation of the conditional-fiber approach is ruled out by [](#prop:conditional-fiber-root-obstruction), which is why the approach is stated as an all-frame question, [](#conj:conditional-fiber-frame).

Two further cautions are advisory rather than established: the two-tail obstruction ([](#rem:two-tail-slice-bounds)) and the circularity warning of Section [](#sec:excess). They are recorded as remarks for exactly that reason: they guide work, but no statement here is excluded on their strength.

(subsec:atlas-assessment)=
## Assessment of priorities

The fixed eigenfunction (S) is the approach best aligned with the known obstruction. Unlike the fixed cut, whose interface functional and weighted package charge $\lmax(A_t)$, it never asks for a uniform bound on the top covariance eigenvalue, and by Section [](#subsec:kls-spike-obstruction) such a bound is false for tensorized exponentials. The occupation quantity behind its target, [](#eq:function-adapted-occupation), factorizes over independent blocks where $\norm{A_t}_\op$ does not, so it respects the tensorization test of Section [](#subsec:kls-tensorization-test). That is a structural argument for its priority, not a preference.

The moment map (C) is conceptually deeper and may ultimately be cleaner, since its target is a single inequality with no stochastic apparatus at all. But it asks for control of correlations between the Stein kernel and nonlinear gradient fields, a considerably stronger theorem than the fixed-matrix estimate it starts from, and the work on it here concentrates the difficulty in a commutator sum, [](#conj:mm-square-root-commutator), for which no dimension-free control is known.

The fixed cut (E) is the most narrowly technical and the most clearly delimited: the quantity to remove is identified exactly, the soft-maximum cost [](#eq:logtraceexp) as it enters the interface functional [](#eq:interface-def). It is the approach on which this manuscript establishes the most, including the negative results. The conditional fibers (F) are the youngest; the natural implementation fails ([](#prop:conditional-fiber-root-obstruction)), and what remains is a single question, [](#conj:conditional-fiber-frame), rather than a program.

One caution belongs beside all four: several of these targets start from $\kappa_n=O(1)$, which comes from an unrefereed preprint; what changes if it does not survive review is said in Section [](#subsec:synthesis-caution).

(subsec:atlas-external-reading)=
## Suggested external reading order

For a reader coming to the subject rather than to this manuscript: [@KannanLovaszSimonovits1995] for the conjecture and deterministic localization; [@Eldan2013ThinShell] for stochastic localization and the third-moment parameter; [@LeeVempala2018; @LeeVempala2024] for the cleanest entry to the covariance SDE and the set-transfer argument; [@KLnotes] for the best conceptual exposition of localization, filtering, Bochner, and the operator-norm obstruction; [@KlartagLehec2022Polylog] for heat flow, spectral measures, and $H^{-1}$; [@Klartag2023Logarithmic] for improved Lichnerowicz and the published bound; [@Letwin2026QuadraticKLS] for the current preprint record; and [@KlartagLehec2025ThinShell; @ChenKlartag2026SharpThinShell] for the strongest related tools and the clearest illustration of the quadratic-to-all-functions gap.
