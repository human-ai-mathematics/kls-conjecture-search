---
type: proof-review
date: "2026-08-27"
verdict: pass
authors:
  - /root/a3_prior_prover
reviewer: /root/a3_prior_review
nodes:
  - thm:a3-product
  - prop:a3-hierarchical-prior
solutions:
  - solutions/a3-product-hierarchical-prior.tex
follows_up: research/reviews/2026-08-27-a3-product-hierarchical-prior-proof-review.md
---

# A3 product and hierarchical-prior results — post-promotion proof review

This review certifies the current bytes of `solutions/a3-product-hierarchical-prior.tex`, SHA-256
`2430c09febd78c23b8b3d2e48ead88de9edf0c842656b0f21e5877c3b9accd6d`.  It follows the detailed
proof review named in the front matter and the intervening repair audit
`research/reviews/2026-08-27-a3-product-hierarchical-prior-post-promotion-audit.md`.  The reviewer
remains distinct from the author.

## Findings

### Repair scope

The audit requested only synchronization of the two formal `bounded_by` edges in the header and
obstruction paragraph.  Mechanically reversing exactly those edits in the current file reproduces
the audited pre-repair SHA-256
`37f3357c77d648e48fa376891d991b5e555d4bc9a6e2943d4b5b6e74249945db`.  A rendered-text
comparison changes only the fence-classification paragraph.  The two statements and their proofs
are otherwise byte-for-byte unchanged from the audited artifact.

### Statements, proof, and dependency closure

The final finite-dimensional manuscript statements, ledger statements, and dossier statements
agree.  For the product node, conditional-variance tensorization gives the upper constant
$\max_iC_i$, one-coordinate tests give the matching lower bound even when only near-extremizers
exist, and the published one-dimensional Hardy--Muckenhoupt result gives
$C_i\le4B_i$, hence $4\max_iB_i$.  The repaired plus sign in the two-factor total-variance
identity remains present.

For the hierarchical-prior node, the standard half-Cauchy and Gaussian assumptions are explicit.
The logarithmic half-Cauchy density is correctly normalized as $(\pi\cosh u)^{-1}$.  The
$\operatorname{arsinh}$ change of variables transfers the sharp generalized-Cauchy constant $4$
without loss; the Gaussian factors contribute constant $1$; finite-product tensorization gives
base constant $4$; and the complete pullback chain rule produces every coefficient--local-scale,
coefficient--global-scale, and distinct-coefficient cross term.  Functions of the global scale
alone transfer the one-dimensional near-extremizers and prove optimality, without assuming an
attained extremizer.

Both dependency closures are discharged.  `thm:hardy-1d` and `thm:a3-student` remain published
imports, and their exact conventions and constants were checked against the sources in the prior
review.  No citation, numerical artifact, or mathematical use changed.

### Fences and build

The header and body now agree exactly with the ledger: both nodes are formally bounded by
`obs:heavy-tail-no-classical` and `obs:marginals-not-joint`.  The first is respected by weighted
or pullback rather than raw Euclidean geometry.  The second is respected because the first result
assumes independence and the second treats one fully specified dependent pushforward while
retaining every scale derivative and cross term.  `obs:flat-direction` remains correctly
identified only as neighboring context for a prior-only claim.

`cd solutions && latexmk -g -pdf -outdir=../build a3-product-hierarchical-prior.tex` succeeds and
produces a four-page PDF.  Its only warnings are the expected standalone unresolved references to
the two manuscript nodes and two imported dependency labels.

## Corrections

The provenance-only corrections required by the intervening audit are present.  No further
correction is required.

## Exclusions

This review does not certify arbitrary dependent products, posterior likelihood tilts,
marginal-only control of joint gaps, or raw Euclidean Poincaré inequalities for half-Cauchy
scales.
