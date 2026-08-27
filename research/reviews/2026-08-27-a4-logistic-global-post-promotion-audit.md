---
type: audit
date: "2026-08-27"
---

# A4 logistic-global post-promotion audit

This audit follows the prior certifying review
`research/reviews/2026-08-27-a4-logistic-global-proof-review.md` and examines the current bytes of
`solutions/prop-a4-logistic-global.tex`, SHA-256
`aa27b714d6b7106c9a7fcd4b9e4cb9eabc608994636c5f8619ad397af8adcd19`, after promotion and the
final ledger/manuscript synchronization.

## Findings

The rendered current dossier is identical to the PDF built for the previously reviewed SHA-256
`11715df143046b87387d677b7d4023e9676cafa02c3544ae09ca51c4bd3b1f69`; all byte changes are in
the non-rendered provenance header.  The fixed Gaussian entropy and trace terms, at-most-linear
logistic loss, exact quadratic reverse-KL coefficient, Wasserstein mean lower bound, arbitrary
direction, Rayleigh optimization, and both equality chains are unchanged.  Rechecking those
steps against the prior review exposes no new mathematical defect.

The Gaussian variational-family scope, finite binary-logistic target, and exact constant agree
among the dossier, ledger, and manuscript proposition at
`\label{prop:a4-logistic-global}`.  The dependencies `prop:a2-logistic-global` and
`eq:a4-mean-dual` remain proved and independently certified.  The final nearby A4 import and
residual-target synchronization is also consistent: the modified-transport import applies to its
stated convex cost class, while the residual Student-logistic target is family-localized and does
not alter or enter this Gaussian-prior global proposition.

The post-synchronization bytes nevertheless contain a provenance contradiction.  The ledger now
formally records
`bounded_by: [obs:flat-direction, obs:gaussian-tail-rigidity]`, but dossier line 10 says
`bounded_by: none`, and lines 163--165 repeat that false claim in the rendered body.  The next
bullet correctly explains how the remote translations realize rather than violate both fences,
but the current artifact still fails the complete, semantically accurate solution-header
contract and cannot receive a new proof-review in this state.

`cd solutions && latexmk -g -pdf -outdir=../build prop-a4-logistic-global.tex` succeeds and
produces a two-page PDF.  Its only warnings are the expected standalone unresolved parent
references to the proposition and its two certified dependencies.

## Corrections

In `solutions/prop-a4-logistic-global.tex`:

1. Replace line 10 by
   `%   bounded_by  : obs:flat-direction; obs:gaussian-tail-rigidity`.
2. At lines 163--165, state that these are the node's two formal `bounded_by` edges, then retain
   the existing explanation that remote translations realize the prior scale and make no global
   posterior/Fisher-scale claim.  The other A4-wide bullets may remain identified as neighboring
   scope context.  Do not change the theorem or proof.
3. Recompile, hash the repaired bytes, and run a new independent review.  If it succeeds, the
   still-unused declared certification path
   `research/reviews/2026-08-27-a4-logistic-global-post-promotion-proof-review.md` may be created
   as a proof review following up the prior certifying report and this audit.

## Exclusions

This audit creates no certification delta.  It does not certify the modified-transport import,
the residual Student-logistic localization target, localized A4 constants, heavy-tailed targets,
or families lacking the stated translation witnesses.
