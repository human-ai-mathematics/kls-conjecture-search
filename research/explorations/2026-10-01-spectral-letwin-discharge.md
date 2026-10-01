---
---

# Fixed-eigenfunction consequences after the quadratic input was certified

## Question examined

Discharge the former Letwin antecedent in `lem:mm-stopped-window-source`
and `prop:mm-window-occupation`, the first item of
`TODO-letwin-follow-up.md`, on the existing fixed-eigenfunction route
`ap:s-occupation`. The starting lens is prove. The assignment concerns
the repository's agent-reviewed proof records, without changing a
companion formalization or asserting a formal certification.

## What we learned

*Established, subject to independent review of these revisions.* The
certified `thm:letwin-qcts` has exactly the all-law scope consumed by the
stopped-source proof: every isotropic log-concave law, in every dimension,
and every symmetric matrix, with quadratic variance constant eight.
The bounded-support restriction of the upstream moment-map construction
is absent from its quadratic conclusion. Every posterior of the regular
class has positive-definite covariance; centering and whitening therefore
put it in the certified theorem's class. No new restriction on the prior,
fixed test, restart, or time interval is needed.

*Established, subject to independent review of these revisions.* The
stopped-source proof retains its whitened duality, unwhitening before the
covariance exit, and posterior variance integration. The occupation proof
retains its stopping-time law identification, optional projection, tail
integral, small-gap fourth moment and fixed-dimensional bridge. Their
constants and the shrinking time window are unchanged. The revised
dossiers use the quadratic theorem as a proof dependency and contain no
unresolved Letwin antecedent.

*Observed from the record.* The original author recorded for both dossiers
is `claude-prover-w4p02, unknown, 2026-08-30`. The present revision author
is `researcher_followup, gpt-6-astra, 2026-10-01`. The old reviews pin the
previous conditional statements and dossier bytes; new joint independent
review is required. No Lean proof record or formalization dependency for
these two nodes appears in the inspected records.

## What resists

The occupation window still shrinks with dimension. These revisions neither
settle `conj:mm-spectral-occupation` nor extend the result beyond the
covariance window. The reproduced Poincare bound remains weaker than the
published bound already used by the small-gap argument. The route remains
active with its existing unresolved occupation target.

## Proposed next step

Review the two revised dossiers jointly, checking their applicability to
the certified all-law quadratic theorem, their unchanged constants, and
the removal of the antecedent from both canonical statements and ledger
edges. Retain the original authors in the new review along with the
revision author. Only the new independent review may replace the old
certification records.
