---
type: audit
date: "2026-08-27"
---

# A2 strong-Laplace post-promotion audit

This audit follows the prior certifying review
`research/reviews/2026-08-27-a2-strong-laplace-proof-review.md` and examines the current bytes of
`solutions/thm-a2-target.tex`, SHA-256
`3470d774e7ebd8df788c06c8d39a7c342fe1c18ceec1b9a5a9a9cbfb6af1558d`, after promotion and the
final ledger/manuscript synchronization.

## Findings

The rendered current dossier was compared with the PDF built for the previously reviewed SHA-256
`d6deec5171f867218de151cd2a696c06f3b103ba60d9897664f60101e96bf3a7`.  The only rendered change
is the certification-boundary prose: the former `checked_by: none` disclaimer was replaced by an
agent-certification statement.  The normalized density-ratio bounds, exact Holley--Stroock
factor, covariance and $T_2$ lower bounds, anisotropic unwhitening, probabilistic quantifiers, and
$nH_n^{-1}$ limit are unchanged.  Rechecking those steps against the prior review exposes no new
mathematical defect.

The current ledger statement and the expanded manuscript theorem at `\label{thm:a2-target}` agree
with the dossier theorem.  The proof also continues to respect both relevant obstructions: its
global $L^\infty$ density-ratio hypothesis excludes `obs:tv-insufficient`, while its global
vanishing-oscillation hypothesis excludes the fixed-Gaussian-tail logistic regime covered by
`obs:gaussian-tail-rigidity`.

The post-synchronization bytes nevertheless contain a provenance contradiction.  The ledger now
formally records
`bounded_by: [obs:tv-insufficient, obs:gaussian-tail-rigidity]`, but dossier line 9 lists only
`obs:tv-insufficient`.  Lines 257--265 likewise call only `obs:tv-insufficient` formal and call
`obs:gaussian-tail-rigidity` merely neighboring.  This is false in the current claim graph and
fails the complete, semantically accurate solution-header contract.  The current artifact cannot
receive a new proof-review while that contradiction remains.

`cd solutions && latexmk -g -pdf -outdir=../build thm-a2-target.tex` succeeds and produces a
four-page PDF.  Its sole warning is the expected standalone unresolved parent reference to
`thm:a2-target`.

## Corrections

In `solutions/thm-a2-target.tex`:

1. Replace line 9 by
   `%   bounded_by  : obs:tv-insufficient; obs:gaussian-tail-rigidity`.
2. At lines 257--265, state that **both** `obs:tv-insufficient` and
   `obs:gaussian-tail-rigidity` are formal fences.  Retain the existing mathematical explanation:
   global $L^\infty$ comparison rules out remote TV contamination, and global
   vanishing-oscillation comparison rules out the ordinary fixed-Gaussian-prior logistic regime.
   Do not change the theorem or proof.
3. Recompile, hash the repaired bytes, and run a new independent review.  If it succeeds, the
   still-unused declared certification path
   `research/reviews/2026-08-27-a2-strong-laplace-post-promotion-proof-review.md` may be created as
   a proof review following up the prior certifying report and this audit.

## Exclusions

This audit creates no certification delta.  It does not reopen the unchanged mathematics, verify
the global oscillation hypothesis for a concrete model, or certify the broader conjecture
`conj:a2`.
