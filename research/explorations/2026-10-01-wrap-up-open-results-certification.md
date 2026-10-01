---
---

# Certification of the open implications and preprint imports

## Question examined

Complete the certification of the open fixed-cut implications and of the preprint
imports, on the dedicated branch `certify-open-results`,
using the repository's researcher → independent reviewer → orchestrator → writer
workflow. The scope is 18 formerly open nodes: four internal implications, seven
preprint imports, and seven local consequences. The preparatory count of nine
consequences double-counted two Chen–Klartag imports.

## What we learned

*Observed in the certification record.* The following eight dossiers have independent
`pass` reviews and are registered in `research/program/ledger.yaml`. These are
agent-reviewed proofs under `SPECIFICATION.md`, not claims of journal peer review
or Lean certification. All paths in the table are relative to the repository root.

| Nodes | Dossier under `solutions/` | Passing report under `research/reviews/` |
|---|---|---|
| `thm:centroid-implies-kls`, `thm:intro-all-cut` | `thm-centroid-implies-kls.md` | `2026-10-01-conditional-bridges-review.md` |
| `thm:carleson-implies-centroid` | `thm-carleson-implies-centroid.md` | `2026-10-01-carleson-centroid-review.md` |
| `thm:intro-weighted` | `thm-intro-weighted.md` | `2026-10-01-weighted-implication-review.md` |
| `thm:letwin-moment-map`, `thm:letwin-qcts` | `thm-letwin-imports.md` | `2026-10-01-letwin-imports-r2-review.md` |
| `thm:chen-klartag-moment-hessian`, `thm:chen-klartag-thin-shell`, `thm:chen-klartag-third-moment` | `thm-chen-klartag-imports.md` | `2026-10-01-chen-klartag-imports-review.md` |
| `thm:kl-stopped-rank-tail`, `thm:kl-integrated-rank-covariance` | `thm-kl-rank-imports.md` | `2026-10-01-kl-rank-imports-review.md` |
| `cor:qcts-source`, `thm:covariance-bound`, `cor:V2-implies` | `letwin-source-consequences.md` | `2026-10-01-letwin-source-consequences-review.md` |
| `prop:letwin-kappa`, `cor:letwin-window`, `cor:KI-letwin`, `thm:V2-window` | `letwin-covariance-windows.md` | `2026-10-01-letwin-covariance-windows-review.md` |

*Observed in the proof and review record.* The mathematical repairs and scope
clarifications are recorded in the individual checkpoints and dossiers:

- The Carleson implication uses the finite trace-source budget from
  `cor:per-direction`, localization and Fatou, then deterministic-prefix Carleson
  estimates and Gronwall. It never applies the hypothesis to an auxiliary random
  interval. The intermediate dimensional finiteness bound does not enter the final
  universal constants.
- Positive horizons and nonnegative constants are explicit in the relevant
  assumptions. The change to `ass:weighted-package` required a complete fresh review
  of `prop:weighted-spectator-obstruction`: the report
  `2026-10-01-weighted-refuter-horizon-review.md` supports both existing refutations,
  `ass:weighted-package` and `conj:weighted-excess-rate`. Earlier reports are preserved.
- The covariance-window statements now state their dimension and nonnegative-time
  domains explicitly. Conditional Letwin antecedents remain in `assumes`, including
  those already carried by `lem:mm-stopped-window-source` and
  `prop:mm-window-occupation`. No Lean antecedent was removed.
- Letwin's source is pinned to arXiv 2607.24164v1, Chen–Klartag to 2607.23307v1,
  and Klartag–Lehec to 2507.15495v2. The reviews check the source proof chains needed
  for these precise imports, as well as transfer to the manuscript's conventions.
- The initial Letwin review requested an accessible reference for the boundary
  Brascamp–Lieb step. The repaired dossier uses Kolesnikov–Milman, Theorem 1.2(1);
  the second independent review passes. The initial `revise` report remains intact.
- The Klartag–Lehec reconstruction uses an a.e. derivative formulation and an
  explicit cutoff with universal coefficient 64 instead of the source's 12.
  The imported statements assert universal constants, so their scope is unchanged.
- The bibliography distinguishes the published 2022 GAFA fixed-time estimate from
  the supremum-in-time estimate in `KLnotes`; the boundary Brascamp–Lieb reference
  has been added.

*Observed by repository checks.* The full checker passes with 131 nodes:
4 defined, 21 open, 104 proved and 2 refuted, compared with 39 open and 86 proved
before this work. There are no draft dossiers. All 131 statement fingerprints
match before and after the writer's prose pass; the explicit mathematical
clarifications above were made before that baseline and independently reviewed.
`git diff --check` passes. Historical checkpoints and reviews have not been edited.

*Observed in the final independent sync audit* (`reviewer, gpt-6-astra,
2026-10-01`, fresh context). All 18 target nodes and the renewed weighted refuter
agree mathematically with their dossiers, dependency edges and visible antecedents;
the brief's negation of `conj:kls` agrees with its canonical statement. The audit
requested seven prose-only deltas, not a change to any certification: remove the
pending-review language in `modules/08-spectral-approach.md`; distinguish the
non-sharp directional bound from the sharp full-tensor bound in the overview;
state the internal stopped-rank → integrated-rank dependency in the covariance
chapter; and replace two manually written status phrases by statement pointers.
The writer applied these deltas in modules 00, 06, 08 and 30. The audit did not
recertify the source proofs; those remain supported by the individual reports above.
Author-dossier remarks about the ledger read during their mission describe the
pre-transition snapshot; the final ledger and independent reviews record the
subsequently added dependencies.

## What resists

`conj:kls` remains open. Certification of a conditional implication does not
establish its antecedent; in particular the weighted package remains refuted and
`ap:e-weighted-excess` remains closed. The preprint imports do not certify Letwin's
general KLS theorem, gate zero, adaptive matrix estimates, eigenspace orientation,
or dimension-free stochastic windows. No route in the portfolio is advanced or
reopened by this administrative and mathematical certification work alone.

## Proposed next step

Use the registered dossiers and their exact hypotheses as inputs to future research.
The remaining task is to establish an actual structural antecedent or a new route,
not to repeat these certifications. For a changed source version, statement or
dossier, obtain a new independent review rather than refreshing old fingerprints.

Two follow-ups are now possible. Each needs its own review.

- `thm:letwin-qcts` is proved, so `lem:mm-stopped-window-source` and
  `prop:mm-window-occupation` could drop "conditional on" from their titles and move it
  from `assumes` to `depends_on`. This is a change of statement and needs a new review.
- Letwin's general bound ψₙ ≲ (log n)^{1/4} is cited in prose but is not a statement. A
  new node would need a dossier for the remaining link: extracting `C_P ≲ κ_n √log n`
  from Klartag's estimates, point (d) of the manuscript's audit.
