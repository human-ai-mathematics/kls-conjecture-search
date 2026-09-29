---
---

# Legacy R2 debt — schema and mathematical triage

This non-certifying, read-only proof-location and control-plane audit was orchestrated by
`/root`, with schema review by `/root/ledger_schema_simplify` and mathematical inventory review
by `/root/legacy_proof_triage`. Its debt inventory and classification passed; it provides no R2
proof certification.

## Scope

This report inventories every historical `proved` node without a certified standalone dossier in
the A-series and KLS ledgers. It supports the exact `meta.legacy_r2_debt.nodes_by_file` manifests;
it does not certify any listed proof. The August 24 KLS consolidation audit likewise stated that
the then-recorded 41 KLS exceptions had not been recertified.

## KLS triage

All 41 former KLS exceptions were located in the manuscript and classified:

- 34 theorem, lemma, proposition, or corollary nodes have identifiable inline proof arguments;
- `def:qcts` is a definition and has no proof obligation;
- `prop:second-variation` and `prop:reilly` rely on published inputs rather than local proofs. An
  independent source audit matched the former to Rosales (2014), Lemma 4.1(ii) and (4.1), and the
  latter to Ma--Du (2010), Theorem 1. The audit caught and repaired an inner/outer-normal sign
  mismatch in the manuscript's Reilly statement;
- `rem:almost-stability-gap` states a missing theorem and is open;
- `rem:kl-window-verified` records published-source attribution and is imported; and
- `rem:trace-upgrade-unification` and `rem:taming-type-mismatch` are diagnostic syntheses whose
  unproved extrapolations are heuristic.

The exact KLS R2 debt is therefore the 34 inline-proof nodes grouped under 13 manuscript files in
`research/kls/ledger.yaml`. A spot-check found no immediate contradiction in their elementary
algebra, but it was not a complete proof audit. In particular, the Riccati/stopping, perimeter and
stochastic-Fubini, bootstrap, QCTS regularization, and geometric sign/domain steps still require
standalone dossiers and independent review.

Two statement/provenance repairs were required during triage:

1. `lem:excess-identity` holds under compact support as stated in the manuscript; that hypothesis
   had been omitted from its ledger statement.
2. `prop:intro-audit` is labeled in `modules/kls/20-eldan-statements.tex`, while its proof is in
   `modules/kls/24-excess-propagation.tex`; the ledger now records the latter as `proof_file`.

## A-series inventory

Five elementary A-series results have inline manuscript arguments but no standalone certified
dossier: `obs:tv-insufficient`, `lem:linear-test-lower`, `thm:glm-fi`, `lem:a5-lipschitz`, and
`thm:a5-monotone`. Their former free-text `proof_provenance` fields did not constitute R2 and have
been replaced by the exact grouped debt manifest. They remain uncertified.

## Control-plane verdict

The checker must compute the set of non-definition `proved` nodes without `solution:` and require
exact equality with the flattened debt manifest. It must reject undeclared, duplicated, stale,
unknown, solution-bearing, status-mismatched, and file-mismatched entries. The manifest's audit path
must be a safe existing repository-relative file. Free-text `proof_provenance` may describe history
but cannot authorize `status: proved`.

Removing a node from the manifest is permitted only after either:

- a certified R2 dossier is attached; or
- the claim is honestly reclassified as a definition, import, open question, heuristic, or other
  non-proved state. Reclassification is bookkeeping, not proof certification.

## Final disposition

The inventory was transitional. Later on 2026-08-25, all 34 proof-bearing KLS entries passed
distinct-agent review in six standalone dossiers, and all five A-series entries passed in three
standalone dossiers. The definition and non-proof nodes were reclassified, the two published
geometry inputs were source-audited, and both ledgers removed the debt manifest. The checker now
admits no historical proof exception: every `proved` node requires R2.
