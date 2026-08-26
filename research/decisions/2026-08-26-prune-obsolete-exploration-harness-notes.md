# Prune obsolete harness notes from the exploration plane

- **Date:** 2026-08-26
- **Type:** repository-history cleanup
- **Scope:** `research/explorations/` and `research/decisions/`
- **Mathematical effect:** none
- **Contract exception:** explicitly authorized by the repository owner despite hard constraint 8

## Problem

Seven records created before or during the introduction of `research/decisions/` described only
ledger-schema, numerical-policy, review-schema, knowledge-plane, target-brief, or general harness
migrations. They contained no mathematical attempt, dead end, proof argument, or numerical
observation. Their operational content has since been replaced by the active scoped contracts and
the later decision records, while their presence in `research/explorations/` obscured the attempt
log's mathematical purpose.

## Decision

Delete the following tracked, recoverable historical files:

- `2026-08-25-ab-ledger-schema-cleanup.md`;
- `2026-08-25-directional-numerics-policy.md`;
- `2026-08-25-kls-harness-simplification.md`;
- `2026-08-25-knowledge-plane-harness-audit.md`;
- `2026-08-25-ledger-schema-simplification.md`;
- `2026-08-25-review-provenance-schema.md`; and
- `2026-08-25-target-brief-simplification.md`.

This is a one-time owner-authorized exception to the append-only rule, not a relaxation of that
rule for future contributions. The deleted contents remain recoverable from Git history.

## Preservation boundary

Retain every record containing mathematical analysis, including superseded frontier maps and dead
ends. In particular, retain the CMH construction/model archives, the KLS Part III restructure and
literature audit, the KLS certification/correction history, and the first-cycle A-series overview.

No file in `research/decisions/` was removed. Although some decisions supersede individual points
of earlier ones, each remaining record describes a distinct migration boundary or compatibility
choice.

## Validation

- An exact-name scan found no references to any deleted file outside this decision record.
- `python3 -B research/check_ledger.py`: 2 ledgers, 170 nodes, 632 labels, 0 errors.
- `python3 -B -m unittest discover -s research/tests -p 'test_*.py'`: 38 tests pass.
- `git diff --check`: tracked diff clean; a separate trailing-whitespace scan of this new record
  is also clean.
