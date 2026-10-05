---
---

# A fresh grouped audit of the August-25 core dossiers

## Question examined

The user requests a new independent grouped review of the three core dossiers
still relying on the August-25 cross-reviews. The motivation is the proof gap
found and repaired for `lem:survival-implies-kls` during Wave A, not evidence
that any other conclusion is false.

## What we learned

*Observed from the ledger.* Sixteen current nodes, rather than fifteen, still
directly use the two relevant August-25 reports. The three dossiers have
seventeen current node consumers in total: `thm:bootstrap` uses the bootstrap
dossier with a later review. The full-dossier mission includes it as well.

| Dossier | Current node consumers |
|---|---|
| `solutions/kls-localization-riccati-core.md` | `lem:matrix-riccati`, `thm:scalar-riccati`, `cor:per-direction`, `cor:tight-window-consumption`, `lem:pathwise-BL`, `cor:away-from-zero` |
| `solutions/kls-qcts-stein-boundary-core.md` | `prop:qcts-equivalence`, `prop:stein-rep`, `lem:stein-vs-source`, `lem:boundary-rep`, `prop:two-tail` |
| `solutions/kls-bootstrap-interface.md` | `lem:half`, `lem:whitening`, `thm:bootstrap`, `lem:crude`, `cor:loglog`, `prop:ceiling` |

The historical reviews are
`research/reviews/2026-08-25-kls-core-r2-audit.md` and
`research/reviews/2026-08-25-kls-excess-bootstrap-r2-audit.md`.
Their identities record reciprocal review by the core and bootstrap authors.
They are provenance for this mission, not conclusions the new reviewer retains.

`lem:survival-implies-kls` now has the separate certified proof
`solutions/lem-survival-implies-kls.md`; it is not another active claim of the
old core dossier. Its corrected interface may be used as a certified input,
while the mission checks how remaining arguments consume it.

*Observed (execution).* A `reviewer` agent, `aug25_grouped_fresh_review`, was
launched with `fork_turns: none`, repository paths and a full `certify` mission.
It has no authoring conversation and is not permitted to repair proofs. The
working tree was clean at launch, and the initial full checker passed.

## What resists

The previous survival review covered only that implication, not the other
arguments. Structural validation cannot settle their correctness. Neither a
shared dossier nor reciprocal authorship alone establishes a mathematical
defect, so no certification is withdrawn merely because this audit starts.

## Proposed next step

Read every proof in the three dossiers against its canonical statement,
quantifiers, dependencies, conditional premises and actual sources. Examine
stopping, integrability, approximation, boundary conventions and cross-dossier
circularity. Give an explicit conclusion for all seventeen nodes, identifying
the downstream impact of any defect; in particular audit the negative-method
interpretation of `prop:ceiling`.

Persist independent reports under `research/reviews/`, separating passing and
failing scopes if outcomes differ. Apply only the certified deltas; preserve
the original reports and any diagnosed gap. A proof failure calls for an exact
repair or a withdrawal of unsupported certification, not a claim of refutation.
