---
type: proof-review
date: "2026-08-27"
verdict: pass
authors:
  - /root/a3_prior_prover
reviewer: /root/a3_prior_review
nodes:
  - thm:a2-target
solutions:
  - solutions/thm-a2-target.tex
follows_up: research/reviews/2026-08-27-a2-strong-laplace-proof-review.md
---

# A2 strong-Laplace transfer — post-promotion proof review

This review certifies the current bytes of `solutions/thm-a2-target.tex`, SHA-256
`b2718641f4ddb5ccabfea76f3c02ad79451c25e2eca4c7e929eee8be3190a209`.  It follows the detailed
proof review named in the front matter and the intervening repair audit
`research/reviews/2026-08-27-a2-strong-laplace-post-promotion-audit.md`.  The reviewer remains
distinct from the author.

## Findings

### Repair scope

The audit requested only two provenance corrections: add `obs:gaussian-tail-rigidity` to the
header's formal fence list, and call it the second formal fence rather than a neighboring one in
the obstruction paragraph.  Mechanically reversing exactly those two edits in the current file
reproduces the audited pre-repair SHA-256
`3470d774e7ebd8df788c06c8d39a7c342fe1c18ceec1b9a5a9a9cbfb6af1558d`.  A rendered-text
comparison likewise changes only that obstruction classification.  No theorem, hypothesis,
formula, or proof step changed.

### Statement, proof, and dependencies

The dossier theorem, the final ledger statement, and the expanded manuscript theorem at
`\label{thm:a2-target}` agree: in fixed dimension, the mode-Hessian limit and global whitened
Gaussian density-ratio representation with $\operatorname{osc}(r_n)=o_P(1)$ imply
$$
C_{\rm P},C_{\rm LS},C_{T_2}
=(1+o_P(1))\lambda_{\max}(H_n^{-1}),
$$
and multiplying by $n$ gives the Fisher-information limit.  The node has no unresolved
dependency.  The Holley--Stroock and Otto--Villani mechanisms used in the unchanged proof are
published and were source-checked in the preceding review; no citation, convention, or use has
changed.

The proof was rechecked at every load-bearing step: normalization gives
$e^{-\delta_n}\le q_n\le e^{\delta_n}$; the repository Holley--Stroock convention costs exactly
$e^{\delta_n}$; density comparison controls the centered covariance; congruence by
$H_n^{-1/2}$ retains the anisotropic Loewner bounds; linear tests and LSI linearization give the
$C_{\rm P}$ and $C_{\rm LS}$ lower bounds; entropy duality plus $W_1\le W_2$ gives the separate
$T_2$ covariance lower bound; the probabilistic exceptional-event convention is complete; and
$nH_n^{-1}=(H_n/n)^{-1}$ yields the claimed limit by continuity and Slutsky.  The hypotheses
actually used remain exactly those recorded in the dossier.

### Fences and build

The header and body now agree exactly with the ledger's formal
`bounded_by: [obs:tv-insufficient, obs:gaussian-tail-rigidity]`.  Global $L^\infty$ density-ratio
control excludes remote TV contamination, while global vanishing oscillation excludes the
ordinary fixed-Gaussian-prior logistic regime whose constants remain prior-scale.  Neither fence
is weakened or contradicted.

After clearing a stale auxiliary file produced by an earlier concurrent build, the required
sequential command
`cd solutions && latexmk -g -pdf -outdir=../build thm-a2-target.tex` succeeds and produces a
four-page PDF.  Its sole remaining warning is the expected standalone unresolved parent reference
to `thm:a2-target`.

## Corrections

The provenance-only corrections required by the intervening audit are present.  No further
correction is required.

## Exclusions

This review does not verify the global oscillation hypothesis in a concrete model, certify
total-variation BvM as sufficient, treat growing dimension, or certify the broader conjecture
`conj:a2`.
