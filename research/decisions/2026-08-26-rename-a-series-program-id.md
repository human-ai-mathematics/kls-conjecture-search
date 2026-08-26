# Rename the A-series program id

- **Date:** 2026-08-26
- **Type:** harness/control-plane identifier migration
- **Scope:** A-series ledger metadata, cross-program bridges, checker configuration, tests, and active documentation
- **Mathematical effect:** none
- **Supersedes:** the `ab` machine-id choice in `2026-08-25-program-directory-layout.md`

## Decision

Use `a-series` as the program id everywhere current program identity is represented:

- `meta.program: a-series` in `research/a-series/ledger.yaml`;
- `a-series/conj:a1-bis` for the A1-bis/KLS bridge;
- `a-series` in checker configuration, program-specific schema selection, diagnostics, and tests;
- `a-series` in active control-plane and orchestration documentation.

Persisted exploration, review, solution-provenance, and decision records are not renamed. In
particular, the filename `research/reviews/2026-08-25-ab-inline-r2-audit.md` remains a valid
immutable provenance path.

## Validation

- `python3 research/check_ledger.py`: 2 ledgers, 170 nodes, 632 labels, 0 errors.
- `python3 -m unittest discover -s research/tests -p 'test_*.py'`: 38 tests pass.
- Active program-id audit: no `ab` program identifiers remain; remaining `ab` strings are the
  immutable review filename or mathematical tensor indices.
- Active Markdown audit: 29 files checked, 0 missing relative links.
- Qualified lookup `python3 research/check_ledger.py node a-series/conj:a1-bis`: passes.
- `git diff --check`: clean.
