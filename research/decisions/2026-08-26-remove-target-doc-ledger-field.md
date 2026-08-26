# Remove the target_doc ledger field

- **Date:** 2026-08-26
- **Type:** harness/control-plane schema simplification
- **Scope:** A-series ledger navigation and shared node fields
- **Mathematical effect:** none

## Problem

Five A-series headline nodes carried `target_doc` paths to mutable refinement briefs. The field had
no logical, provenance, certification, frontier, or orchestration semantics; the checker only
verified that each path existed. It coupled the canonical claim graph to workflow navigation that
already appeared in each brief's entry points.

## Decision

Remove `target_doc` from the shared node schema and from the five A-series headline nodes. Keep
`meta.scope` as the program boundary and `refines` as the genuine semantic-sharpening relation.

Move the forward A1--A5 navigation map to `research/a-series/targets/README.md`, where mutable
workflow navigation belongs. Retain `target_doc` only in the checker's obsolete-field diagnostics
so stale edits receive an actionable migration message rather than being silently accepted.

## Validation

- `python3 -B research/check_ledger.py`: 2 ledgers, 165 nodes, 632 manuscript labels,
  0 errors.
- `python3 -m unittest discover -s research/tests -p 'test_*.py'`: 38 tests passed.
- Relative links in the affected schema and A-series documentation resolve; intentional `(...)`
  target-page template placeholders were excluded.
- `git diff --check`: clean.
