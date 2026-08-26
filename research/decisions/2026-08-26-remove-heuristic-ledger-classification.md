# Remove the heuristic ledger classification

- **Date:** 2026-08-26
- **Type:** harness/control-plane schema correction
- **Scope:** shared ledger kind vocabulary and active documentation
- **Mathematical effect:** none
- **Supersedes:** point 5 of `2026-08-26-unified-ledger-status-vocabulary.md`

## Problem

The unified-status migration removed `heuristic` from `status` but retained it in `kind`. That
left a second, non-logical ledger classification for material which belongs to research prose and
made the simplification incomplete.

## Decision

Remove `heuristic` from the ledger schema entirely. It is neither a status nor a kind. Speculative
reasoning remains available in manuscript prose and append-only explorations, while any precise
truth-valued claim is classified by its actual mathematical form and logical status.

The checker retains a regression asserting that the removed value is rejected in both fields.

## Validation

Validated after the migration:

- `python3 -B research/check_ledger.py`: 2 ledgers, 165 nodes, 632 labels, 0 errors;
- `python3 -B -m unittest discover -s research/tests -p 'test_*.py'`: 36 tests pass; and
- `git diff --check` is clean.
