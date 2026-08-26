# Remove the soundness-tier taxonomy

- **Date:** 2026-08-26
- **Type:** harness terminology simplification
- **Scope:** active repository rules, maps, ledger comments, and implementation comments
- **Mathematical effect:** none

## Problem

The `R0`/`R1`/`R2` taxonomy repeated contracts already expressed concretely by the structural
checker, provenance-stamped numerical runs, and certified proof dossiers. Although described as
three independent signals, the names suggested a maturity ladder and added terminology without
changing any workflow. `R0` and `R1` also occur as genuine mathematical quantities in the
numerical implementation.

## Decision

Remove the tier taxonomy from active repository language. State the two operational safeguards
directly where they apply:

- `check_ledger.py` validates repository structure, not mathematical correctness; and
- numerical runs may guide research but cannot certify a claim. Even an exact computational
  witness changes no ledger status until an independent critic checks it in a proof or
  refutation dossier.

Use `certified dossier`, `structural checker`, and `numerical artifact` instead of tier names.
Use `certification modes` rather than describing `checked_by` as a ladder.

## Compatibility

Historical explorations, reviews, and earlier decisions retain their original terminology.
Mathematical variables named `R0` or `R1` in `finum` also remain unchanged; they are unrelated to
the retired harness vocabulary.

## Validation

Validated on the current branch:

- active occurrences of the retired vocabulary are gone; remaining `R0`/`R1` occurrences are
  mathematical variables in `finum`;
- `python3 -B research/check_ledger.py`: 2 ledgers, 165 nodes, 632 labels, 0 errors;
- `python3 -B -m unittest discover -s research/tests -p 'test_*.py'`: 34 tests pass;
- all relative Markdown links resolve; and
- `git diff --check` is clean.
