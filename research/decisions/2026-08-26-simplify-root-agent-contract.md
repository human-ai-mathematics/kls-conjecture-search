# Simplify the root agent contract

- **Date:** 2026-08-26
- **Type:** harness documentation refactor
- **Scope:** `CLAUDE.md` / `AGENTS.md`
- **Mathematical effect:** none

## Problem

The root instructions called all other documents maps while delegating mandatory dossier rules
and role write surfaces to two of them. Proof completion therefore required a second lookup, and
the command list mixed required validation with optional navigation. Historical rationale and
editorial commentary also obscured otherwise stable constraints.

## Decision

1. `CLAUDE.md` is the root contract. The ledger schema, proof plane, numerical plane, and role
   definitions may impose narrower scoped requirements but never override it; remaining READMEs
   are navigation maps.
2. The ownership table separates claims, manuscript prose, proof certification, diagnostics,
   research memory, and harness decisions.
3. Completion is stated in three explicit paths: mathematical, proof, and harness/repository.
   The four proof requirements remain visible in the root contract.
4. Historical rationale and role-specific narration are removed from the hard constraints. The
   eight constraints retain their numbers and order because append-only records cite them.
5. Validation commands are keyed to the content changed. Optional `status`, `node`, and
   `finum run` navigation remains in the appropriate plane README.
6. Ledger conventions retain only the high-risk label and dependency rules plus the Markdown
   math convention; numerical provenance detail remains in the numerical contract.

## Validation

- `AGENTS.md` resolves to byte-identical `CLAUDE.md`; all eight constraint numbers remain.
- Root-contract relative-link audit: 0 missing links.
- `python3 research/check_ledger.py`: 2 ledgers, 170 nodes, 632 labels, 0 errors.
- `python3 -m unittest discover -s research/tests -p 'test_*.py'`: 38 tests pass.
- `git diff --check`: clean.
