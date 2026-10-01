---
---

# Letwin follow-up: discharged premises, general bound, and occupation scope

## Question examined

Complete the two mathematical items of `TODO-letwin-follow-up.md` on
`certify-open-results`, following the researcher, fresh independent reviewer,
orchestrator and writer division. This follows
`2026-10-01-wrap-up-open-results-certification.md`. The optional human acceptance
was not a prerequisite and has not been recorded.

## What we learned

*Established through the certification records below.* The all-law quadratic
input discharges the Letwin antecedent of the two fixed-eigenfunction nodes.
Their `assumes` edges became `depends_on`. The occupation proposition contained
the antecedent in its body as well as its title, contrary to the temporary
TODO's description; both occurrences were removed. The stopped-source
constant and the occupation constants were unchanged.

| Node | Dossier | Selected new independent review |
|---|---|---|
| `lem:mm-stopped-window-source` | `solutions/lem-mm-stopped-window-source.md` | `research/reviews/2026-10-01-spectral-window-letwin-discharge-review.md` |
| `prop:mm-window-occupation` | `solutions/prop-mm-window-occupation.md` | `research/reviews/2026-10-01-window-occupation-empty-branch-review.md` |
| `thm:letwin-kls` | `solutions/thm-letwin-kls.md` | `research/reviews/2026-10-01-letwin-kls-review.md` |

The first two nodes remain `proved` with renewed records. The third is a new
canonical statement in module 04, promoted from `open` only after its review
passed. All reviews were performed by fresh-context reviewer agents
(`gpt-6-astra`), distinct from the researcher contexts. No human acceptance or
Lean certification is implied.

*Established in the new general-bound dossier and independently reviewed.* The
missing spectral passage retains the factor involving the initial Poincare
constant in Gaussian-observation variance transfer. Choosing the minimum of
the covariance-window time and the inverse Poincare constant yields two
branches, one with the desired logarithmic bound and one bounded by a universal
constant. The proof identifies the published Klartag--Lehec covariance theorem,
Klartag's improved Lichnerowicz and regular approximation, Milman's
Lipschitz-variance comparison, and Bobkov's qualitative finiteness result.
It does not use `thm:klartag-logn` as an input. The direct quadratic dependency
discharges the antecedent of `prop:letwin-kappa`. Source versions and exact
normalizations are recorded in the dossier and its review.

*Established scope correction.* The first joint review found that the small-gap
class in `prop:mm-window-occupation` is empty: the published input gives
`C_P <= K_n`, whereas the branch requires an eigenvalue below `3/(8 K_n)`.
Consequently that implication supplies no admissible occupation example, and
its weaker frontier consequence is already supplied by the input. The
stopped-source lemma has no such spectral restriction. This corrects any
interpretation of the earlier window-chain records as nonempty occupation
progress; the historical records are preserved.

A fresh `sync` audit confirmed agreement of all three statements, their proof
records, logical edges and the brief's target negation. It requested exact
corrections to the occupation dossier's overview, scope bullet and regularity
remark, as well as an atlas table row and a status phrase in the synthesis.
The researcher and writer applied those corrections. Because dossier bytes
changed, a further fresh `certify` review renewed only the occupation record.
The joint report remains the selected stopped-source certification. No old
review or checkpoint was rewritten.

*Observed verification.* The full checker passes after the final record
replacement; there are no draft dossiers. It reports 132 nodes: 4 defined,
21 open, 105 proved and 2 refuted. Comparison with the session's initial
statement fingerprints shows exactly the two intended changed statements and
one added statement. Both writer passes preserve all 132 statement
fingerprints. The brief no longer lists the two discharged results as
implications with open antecedents, and lists the new dimension-dependent
theorem among conclusions that do not settle KLS.

The manuscript updates cover modules 00, 04, 06, 08, 26 and 30. They distinguish
publication provenance from agent verification, explain the minimum-time
argument, and disclose the empty occupation branch. The temporary TODO is
removed as requested by its header; this checkpoint preserves its disposition.

## What resists

`conj:kls` and `conj:mm-spectral-occupation` remain open. The new general bound
retains logarithmic dimension dependence. It supplies neither a universal-time
occupation estimate nor gate zero, CMH or adaptive-matrix control. Other
canonical implications retaining explicit antecedents were not silently
rewritten.

The main route `ap:s-occupation` remains active. The sub-route
`ap:s-window-chain` stays closed: its present small-gap formulation cannot
provide nonempty occupation progress, rather than having solved an initial
layer of the conjecture. A renewed attempt would require an admissible
hypothesis or a different mechanism, not reuse of this empty branch. No
portfolio state change is needed for that clarification.

## Proposed next step

No required item of the temporary follow-up remains. A named human may later
accept `thm:letwin-qcts` and `thm:letwin-kls` after their own examination; no
`accepted_by` record is created on an agent's behalf. Further mathematical
work resumes from the existing active targets and their actual unresolved
premises, not from an assertion of KLS completion.
