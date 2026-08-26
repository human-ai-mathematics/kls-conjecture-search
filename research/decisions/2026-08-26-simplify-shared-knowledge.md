# Simplify the shared knowledge registry

- **Date:** 2026-08-26
- **Type:** repository-organization refactor
- **Scope:** `research/knowledge/`
- **Mathematical effect:** none

## Problem

The shared knowledge files mixed current reference material with proof progress, run history,
backend status, provenance policy, and manually maintained consumer lists. Several registered
calibration names also differed from the instance ids emitted by `finum`. This obscured which
information was canonical and allowed documentation to drift from the executable battery.

## Decision

1. `research/knowledge/README.md` defines a narrow ownership boundary: reusable facts and the
   shared instance registry only.
2. `instances.md` uses compact calibration and stress tables. Each implemented row names the
   exact `finum` target and emitted instance id; an em dash means no id-bearing backend exists.
3. Numerical-validity and provenance policy is linked once from `experiments/README.md` instead
   of repeated in each instance description.
4. `lemmas.md` uses a uniform fact/use/guardrail format. Proof summaries, certification state,
   implementation notes, and reverse consumer lists are removed; the ledger, manuscript, and
   dossiers remain authoritative for those concerns.
5. Earlier formulations, run commentary, and dated progress are not retained in the current
   knowledge reference. Their canonical homes remain the append-only exploration, run, review,
   and decision planes.

## Validation

- `python3 research/check_ledger.py`: 2 ledgers, 170 nodes, 632 labels, 0 errors.
- `python3 -m unittest discover -s research/tests -p 'test_*.py'`: 38 tests pass.
- `cd experiments && uv run python -m finum selftest`: all A1--A5 and KLS/CMH checks pass.
- Knowledge-document relative-link audit: 0 missing links.
- Registered `finum` id audit: all 29 explicitly implemented ids occur in `experiments/finum`.
- `git diff --check`: clean.
