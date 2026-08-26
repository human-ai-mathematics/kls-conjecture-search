# Unified ledger kind vocabulary

- **Date:** 2026-08-26
- **Type:** harness/control-plane schema simplification
- **Scope:** shared ledger kinds, KLS node classifications, and matching manuscript environments
- **Mathematical effect:** none

## Problem

The shared `kind` enum mixed precise mathematical forms with duplicative or non-node roles.
`hypothesis` duplicated `assumption`; `program` belonged to ledger metadata; and `remark` mirrored
an expository LaTeX environment without supplying checker semantics. Four ledger-backed remarks
therefore carried open, conditional, or proved statuses despite having more precise mathematical
roles.

## Decision

1. Both ledgers use exactly ten kinds: `theorem`, `proposition`, `lemma`, `corollary`,
   `conjecture`, `assumption`, `question`, `definition`, `obstruction`, and `example`.
2. Replace the two KLS `hypothesis` nodes by `assumption`, preserving their stable `hyp:*` labels.
3. Keep `program` only as `meta.program`; it is not a node kind.
4. Remove `remark` as a node kind. Ordinary manuscript remarks remain available as prose, but a
   ledger-backed statement uses its precise mathematical form.
5. Reclassify the foundational almost-stability target as a question and the three CMH deductions
   as corollaries. Preserve their stable `rem:*` labels and update the matching manuscript
   environments and references.

No logical status, proof dependency, obstruction edge, or mathematical conclusion changes.

## Validation

Validated after the migration:

- `python3 -B research/check_ledger.py`: 2 ledgers, 165 nodes, 632 labels, 0 errors;
- `python3 -B -m unittest discover -s research/tests -p 'test_*.py'`: 38 tests pass;
- `latexmk -pdf -outdir=build main.tex`: the 149-page manuscript compiles;
- the four affected standalone dossiers compile with their expected unresolved external
  manuscript references; and
- `git diff --check` is clean.
