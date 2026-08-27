---
type: proof-review
date: "2026-08-27"
verdict: pass
authors:
  - /root/a4_logistic_prover
reviewer: /root/a3_prior_review
nodes:
  - prop:a4-logistic-global
solutions:
  - solutions/prop-a4-logistic-global.tex
follows_up: research/reviews/2026-08-27-a4-logistic-global-proof-review.md
---

# A4 global logistic rigidity — post-promotion proof review

This review certifies the current bytes of `solutions/prop-a4-logistic-global.tex`, SHA-256
`5e82a91b789e93ec04828c27462ed1cc4fa13ec3d1eb9669be523f2186c292f3`.  It follows the detailed
proof review named in the front matter and the intervening repair audit
`research/reviews/2026-08-27-a4-logistic-global-post-promotion-audit.md`.  The reviewer remains
distinct from the author.

## Findings

### Repair scope

The audit requested only synchronization of the two formal `bounded_by` edges in the header and
obstruction paragraph.  Mechanically reversing exactly those edits in the current file reproduces
the audited pre-repair SHA-256
`aa27b714d6b7106c9a7fcd4b9e4cb9eabc608994636c5f8619ad397af8adcd19`.  A rendered-text
comparison changes only the fence-classification sentence.  The theorem and proof are otherwise
byte-for-byte unchanged from the audited artifact.

### Statement, proof, and dependency closure

The finite Gaussian-prior binary-logistic target, Gaussian variational-family scope containing
all translations of one fixed $S\succ0$, normalization of all constants, and asserted value
$\lambda_{\max}(\Sigma_0)$ agree among the dossier, final ledger, and manuscript proposition at
`\label{prop:a4-logistic-global}`.  The final nearby A4 modified-cost import and residual
Student-logistic localization target have distinct scopes and do not enter this proposition.

Both dependencies remain proved and independently certified.  `prop:a2-logistic-global` supplies
the exact unrestricted $C_{T_2}=\lambda_{\max}(\Sigma_0)$, and `eq:a4-mean-dual` supplies the
extended-valued unrestricted mean identity.  There is no external or preprint dependency beyond
that discharged repository closure.

The unchanged proof was rechecked in full.  Each logistic summand is nonnegative and at most
$\log2+|x_i^T\theta|$, giving Gaussian quadratic-exponential tails.  For
$q_{t,v}=N(\mu_0+tv,S)$, entropy, normalizer, and trace terms are independent of $t$, while the
expected logistic loss is $O(1+t)$; hence
$$
2\operatorname{KL}(q_{t,v}\|\pi)
=t^2v^T\Sigma_0^{-1}v+O(1+t).
$$
The squared mean displacement is $t^2\|v\|^2+O(1+t)$ and is bounded above by $W_2^2$ under every
coupling.  Arbitrary $v$, Rayleigh optimization, and the unrestricted $T_2$ upper bound then give
both exact equality chains for the restricted mean, restricted transport, unrestricted mean, and
unrestricted transport constants.

### Fences and build

The header and body now agree exactly with the ledger's formal
`bounded_by: [obs:flat-direction, obs:gaussian-tail-rigidity]`.  Remote translations explicitly
realize the prior scale rather than claim a posterior/Fisher-scale global constant.  The remaining
A4-wide obstructions are correctly described only as neighboring scope boundaries.

`cd solutions && latexmk -g -pdf -outdir=../build prop-a4-logistic-global.tex` succeeds and
produces a two-page PDF.  The unresolved parent references are expected in standalone mode.  A
minor 3.1-point overfull box in the long obstruction identifier is typographical and has no
mathematical effect.

## Corrections

The provenance-only corrections required by the intervening audit are present.  No further
correction is required.

## Exclusions

This review does not certify localized A4 constants, the separate modified-transport import or
residual target, heavy-tailed targets, families lacking the translation witnesses, or a computable
variational KL certificate.
