---
type: audit
date: "2026-08-27"
---

# A3 product and hierarchical-prior post-promotion audit

This audit follows the prior certifying review
`research/reviews/2026-08-27-a3-product-hierarchical-prior-proof-review.md` and examines the
current bytes of `solutions/a3-product-hierarchical-prior.tex`, SHA-256
`37f3357c77d648e48fa376891d991b5e555d4bc9a6e2943d4b5b6e74249945db`, after promotion and the
final ledger/manuscript synchronization.

## Findings

The rendered current dossier was compared with the PDF built for the previously reviewed SHA-256
`5b23fc098363d58fa3691717ad680c91e4c1ca88d9708983b72923c0a51fcea6`.  The only rendered change
is the certification-boundary prose: the former `checked_by: none` disclaimer was replaced by an
agent-certification statement.  The repaired conditional-variance identity, exact finite-product
tensorization, $4\max_iB_i$ consequence, log-half-Cauchy normalization, sharp
$\operatorname{arsinh}$ transfer, Gaussian factor, full pullback chain rule and cross terms, and
near-extremizer optimality argument are unchanged.  Rechecking those steps against the prior
review and the published dependencies exposes no new mathematical defect.

The final manuscript now explicitly restricts both statements to finite dimension, matching the
dossier and ledger.  The dependency closures remain discharged: `thm:hardy-1d` and
`thm:a3-student` are published imports in the ledger.  The proofs respect
`obs:heavy-tail-no-classical` by using weighted or pullback geometry and respect
`obs:marginals-not-joint` by using an independent product or one completely specified dependent
pushforward with every scale derivative and cross term retained.

The post-synchronization bytes nevertheless contain a provenance contradiction.  The ledger now
formally records both `obs:heavy-tail-no-classical` and `obs:marginals-not-joint` as
`bounded_by` edges for each reviewed node.  Dossier line 9 says that neither target has any such
edge, and lines 229--232 repeat that false claim in the rendered body.  Although the following
bullets correctly respect the two obstructions, the current artifact fails the complete,
semantically accurate solution-header contract and cannot receive a new proof-review in this
state.

`cd solutions && latexmk -g -pdf -outdir=../build a3-product-hierarchical-prior.tex` succeeds and
produces a three-page PDF.  Its only warnings are the expected standalone unresolved parent
references to the two nodes and the two imported dependency labels.

## Corrections

In `solutions/a3-product-hierarchical-prior.tex`:

1. Replace line 9 by
   `%   bounded_by  : obs:heavy-tail-no-classical; obs:marginals-not-joint (both nodes)`.
2. Replace the false assertion at lines 229--232 with the statement that both
   `thm:a3-product` and `prop:a3-hierarchical-prior` have those two formal `bounded_by` edges.
   Keep the existing bullets explaining exactly how the weighted/product and full-pullback
   statements respect them; retain `obs:flat-direction` only as neighboring scope context.
   Do not change either theorem or proof.
3. Recompile, hash the repaired bytes, and run a new independent review.  If it succeeds, the
   still-unused declared certification path
   `research/reviews/2026-08-27-a3-product-hierarchical-prior-post-promotion-proof-review.md` may
   be created as a proof review following up the prior certifying report and this audit.

## Exclusions

This audit creates no certification delta.  It does not certify arbitrary dependent products,
posterior likelihood tilts, or raw Euclidean gaps for half-Cauchy scales.
