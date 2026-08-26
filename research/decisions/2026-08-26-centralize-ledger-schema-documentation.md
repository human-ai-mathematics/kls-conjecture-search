# Centralize ledger schema documentation

- **Date:** 2026-08-26
- **Type:** documentation/control-plane organization
- **Scope:** shared ledger schema and program documentation
- **Mathematical effect:** none

## Problem

After the A-series and KLS ledgers adopted common kind and status vocabularies, their schema was
still documented repeatedly in `CLAUDE.md`, `research/README.md`, the A-series README, the KLS
README, and both YAML headers. The A-series README also held most field documentation even though
the fields were now largely shared. These copies could drift.

## Decision

Create `research/ledger-schema.md` as the single field-level schema reference for both ledgers. It
owns the document shape, metadata, kinds, statuses, common graph fields, imported-result
provenance, proof-certification fields, excluded material, and both programs' extensions.

Other active documents retain only their own workflow or contribution rules and link to the
shared schema. Ledger headers likewise point to the schema rather than repeating enum values and
field semantics. `research/check_ledger.py` remains the executable structural validator, while
`CLAUDE.md` remains normative for how contributions enter the repository.

## Validation

Validated after consolidation:

- `python3 -B research/check_ledger.py`: 2 ledgers, 165 nodes, 632 labels, 0 errors;
- `python3 -B -m unittest discover -s research/tests -p 'test_*.py'`: 38 tests pass;
- all relative links in the five active schema/workflow documents resolve; and
- `git diff --check` is clean.
