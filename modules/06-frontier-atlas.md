---
numbering:
  enumerator: "6.%s"
---

(sec:frontier-atlas)=
# The live frontier at a glance

This section is the shortest complete answer to the questions a reader is most likely to arrive with: what is being tried, what has actually been established, what blocks each attempt, which natural variants are already dead, and which attempt currently looks best aligned with what is known. It is deliberately placed before any route is developed. Everything in it is a pointer; the statements themselves live in Parts III and IV, and the detailed synthesis that revisits them after the routes have been read is Section [](#sec:kls-synthesis).

(subsec:kls-reading-map)=
## The five families, side by side

(sec:kls-strategy-map)=

Sections [](#sec:family-needles)–[](#sec:family-transport) above survey the five families in a common format: object followed, what it buys, sharpest result, precise missing estimate, why it stalls, and which live route it feeds. Collected:

| Family | Object followed | Present obstruction | Section |
|---|---|---|---|
| Classical needles | One-dimensional restrictions | Global isotropy is not inherited needle by needle | [](#sec:family-needles) |
| Stochastic localization | Mass, centroid, and covariance along a filtration | Controlling $\lmax(A_t)$ along the whole path; see [](#prop:covariance-spike) | [](#sec:family-sl) |
| Bochner, $H^{-1}$, heat flow | First eigenspace and derivative energies | Trace, coordinate, or averaged spectral information does not bound every slow mode | [](#sec:family-bochner) |
| Moment maps and Stein kernels | Hessian metric of the moment map | Correlation of the random Stein kernel with an arbitrary $\nabla f$ | [](#sec:family-moment-map) |
| Transport (Caffarelli, Föllmer, entropic barrier) | Transport Jacobian or conditional covariance | Dimension-free operator control in expectation | [](#sec:family-transport) |

(subsec:atlas-routes)=
## The four live routes, side by side

Parts III and IV are this repository's work. Each route is a response to Section [](#sec:kls-remaining), each has an exactly stated open estimate, and each is tracked by the approaches of `research/program/portfolio.yaml` whose ids carry its letter — which is search state and carries no truth value of its own.

| Route | Object retained | What it would take to win | Section |
|---|---|---|---|
| E — fixed cut | Mass and two-color covariance of one candidate bottleneck set | Discharge the tight-prefix operator-to-trace upgrade (E–A), or replace both the refuted global weight and the refuted uniform superlinear remainder by a tensor-stable near-Cheeger package and re-audit its Stein trace (E–B) | [](#sec:introduction) |
| S — fixed eigenfunction | Covariance tensor of a first spectral mode | Unwhiten for a universal time without losing tensor/covariance alignment ([](#q:mm-spectral-occupation)) | [](#sec:spectral-route) |
| C — deterministic moment map | Hessian metric, Haar fields, Schur fibers, Stein residuals | Freeze the endpoint and lift, prove an all-split reduction, control the global square-root commutator | [](#sec:moment-map-cmh) |
| F — conditional fibers | One measure-dependent, test-independent isotropic frame of inverse-variance line resamplings | Prove a universal form gap, or decide the all-frame simplex dual; the natural root frame already fails | [](#sec:conditional-fiber-frame) |

(subsec:atlas-external-reading)=
## Suggested external reading order

For a reader coming to the subject rather than to this repository: [@KannanLovaszSimonovits1995] for the conjecture and deterministic localization; [@Eldan2013ThinShell] for stochastic localization and the third-moment parameter; [@LeeVempala2018; @LeeVempala2024] for the cleanest entry to the covariance SDE and the set-transfer argument; [@KLnotes] for the best conceptual exposition of localization, filtering, Bochner, and the operator-norm obstruction; [@KlartagLehec2022Polylog] for heat flow, spectral measures, and $H^{-1}$; [@Klartag2023Logarithmic] for improved Lichnerowicz and the published bound; [@Letwin2026QuadraticKLS] for the current preprint record; and [@KlartagLehec2025ThinShell; @ChenKlartag2026SharpThinShell] for the strongest related tools and the clearest illustration of the quadratic-to-all-functions gap.

(subsec:atlas-state)=
## What each route has actually established, and what blocks it

The tables above say what each route *tries*. This one says where each has got to. Read the middle column as the route's own contribution and the right column as the precise statement whose absence stops it; both resolve to named nodes of `research/program/ledger.yaml`.

| Route | Main advance so far | Exact blocker |
|---|---|---|
| E — fixed cut | The bootstrap comparison and the interface functional (Section [](#sec:bootstrap)), with the crude evaluation proved insufficient; the coordinate budgets and the covariance reduction of the product stress test (Section [](#sec:product-stress)) | The tight-prefix operator-to-trace upgrade, `q:upgrade` (Section [](#sec:open)); on subroute E–B, a tensor-stable replacement for the refuted weighted package |
| S — fixed eigenfunction | The exact fixed-function SDE and the initial-layer window chain, which closes the occupation estimate on the published polylogarithmic covariance window (Section [](#sec:spectral-route)) | [](#q:mm-spectral-occupation): unwhiten for a *universal* time without losing tensor/covariance alignment |
| C — deterministic moment map | The endpoint given precise operator data ([](#def:cmh)), proved to dominate the affine Poincaré constant ([](#thm:cmh-implies-affine-poincare)), and computed exactly on the line, on products, on every log-concave Dirichlet law, and — in its linear sector only — on the exponential cones, which are its first non-product equality set (Section [](#sec:cmh-exact-cases)); that sector is resolved into a directional third moment plus a named remainder ([](#lem:linear-sector-third-moment)) | A construction layer (`q:mm-invariant-lift`, `q:mm-square-root-commutator`: the global square-root commutator sum) and a falsification layer ([](#conj:gate-zero), its sharp form [](#conj:gate-zero-sharp), `q:cmh-solenoidal-perturbation`) |
| F — conditional fibers | The frame is constructed and the natural simplex root frame is *rigorously refuted* (Section [](#sec:conditional-fiber-frame)) | A universal form gap on the maximal closed form domain, or a decision on the all-frame simplex dual; the certified degree-two floors of [](#lem:fiber-root-degree-two) rule out every degree-two refuter, so a dual certificate must have degree at least three |

(subsec:atlas-fences)=
## Fences: what is already ruled out

Negative results are the most reusable part of a search, and four of them constrain everything above. They are stated where they are proved and collected here so that a reader does not rediscover a dead variant.

- **No uniform operator-norm covariance bound.** [](#prop:covariance-spike): the statement a direct “bound $\norm{A_t}_\op$ better” programme would need is false, for a measure that satisfies KLS.

- **The global weighted package is refuted.** [](#prop:weighted-spectator-obstruction) kills the global operator-norm covariance weight of subroute E–B; `q:weighted` is a *refuted* node, not an open one.

- **No matrix-moment argument supplies gate zero.** [](#prop:letwin-not-gate-zero): the fixed-matrix estimate does not close the linear sector of Route C, so Target 2 relocates the average-versus-uniform difficulty rather than escaping it.

- **The natural conditional-fiber root frame fails.** Route F's most obvious implementation is refuted outright in Section [](#sec:conditional-fiber-frame), which is why the route is stated in terms of an all-frame question instead.

Two further cautions are advisory rather than proved, and the ledger records them as open `bounded_by` fences for exactly that reason: the two-tail obstruction ([](#obs:two-tail)) and the circularity warning of Section [](#sec:excess). They guide work; they do not fence a claim.

(subsec:atlas-assessment)=
## Assessment of priorities

Of the four routes, Route S is the one best aligned with the known obstruction: it is the only one that avoids asking for a uniform top-covariance statement, and by Section [](#subsec:kls-spike-obstruction) such a statement is false for tensorized exponentials. That is a structural argument for its priority, not a preference.

Route C is conceptually deeper and may ultimately be cleaner, since its endpoint is a single inequality with no stochastic apparatus at all — but the repository's own experience is that its difficulty concentrates in a commutator sum that has so far resisted dimension-free control. Route E is the most narrowly technical and the most clearly delimited, and it is the one on which this repository has proved the most, including the negative results. Route F is the youngest; its natural implementation is refuted and what remains is a genuine open question rather than a programme.

One caution belongs beside all four. Three of the four cross-route targets of Section [](#sec:kls-synthesis) take $\kappa_n=O(1)$ as their starting point, and that input is an unreviewed version-1 preprint. Should it not survive review, the targets do not become wrong, but their premise reverts to $\CP\lesssim\log n$ and the arithmetic of every “remaining gap” claim changes. The ledger enforces this: the preprint's result is `open`, and a node marked `proved` cannot depend on an open node.
