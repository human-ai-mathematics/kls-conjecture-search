# Unified ledger status vocabulary

- **Date:** 2026-08-26
- **Type:** harness/control-plane schema simplification
- **Scope:** A-series and KLS ledger statuses, checker policy, and active documentation
- **Mathematical effect:** none

## Problem

The two program ledgers used different status enums even though they share one claim graph and
proof-certification contract. KLS also allowed `heuristic` as both a mathematical `kind` and a
logical `status`. Conversely, A-series could not represent a certified conditional implication or
a definition without overloading `open` or `proved`.

The inconsistency made identical logical situations program-dependent and blurred the intended
separation between mathematical form (`kind`) and repository standing (`status`).

## Decision

1. Both programs use exactly six statuses: `open`, `conditional`, `proved`, `imported`, `defined`,
   and `refuted`.
2. `conditional` means that an unresolved premise or unreviewed import remains in the dependency
   closure. The conditional implication may itself carry proof certification.
3. `proved` remains reserved for unconditional claims with a certified standalone dossier.
4. `defined` is the non-proof state of a definition node. The checker enforces both directions:
   `status: defined` requires `kind: definition`, and `kind: definition` requires
   `status: defined`.
5. `heuristic` remains a mathematical `kind` but is removed from the status enum. A labeled
   unresolved heuristic uses `status: open`; informal heuristic discussion may remain in prose.
6. `imported` and `refuted` retain their existing provenance requirements.

The CMH definition node is reclassified from `proved` to `defined`. Its shared dossier continues
to certify the neighboring propositions and theorems; the definition itself no longer carries
proof-certification metadata.

## Validation

Validated after the migration:

- `python3 -B research/check_ledger.py`: 2 ledgers, 165 nodes, 632 labels, 0 errors;
- `python3 -B -m unittest discover -s research/tests -p 'test_*.py'`: 36 tests pass; and
- `git diff --check` is clean.

This decision records a schema change only and creates no mathematical attempt or claim.
