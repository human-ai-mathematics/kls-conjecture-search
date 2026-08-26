# Organize `finum` targets by research program

- **Date:** 2026-08-26
- **Type:** numerical-harness organization
- **Scope:** `experiments/finum/targets/`, target imports, and active harness links
- **Mathematical effect:** none

## Problem

All target implementations lived directly under `finum.targets`, despite belonging to two
separate research programs. The flat directory mixed A1--A5 statement batteries with the KLS
bridge, localization engine, alignment diagnostic, and CMH gate. The public registry was clear,
but the implementation layout obscured ownership and made closely related KLS modules appear
independent.

## Decision

1. A1--A5 live under `finum.targets.a_series` as `a1.py` through `a5.py`.
2. KLS implementations live under `finum.targets.kls`: `bridge.py`, `loc_engine.py`,
   `alignment.py`, and the `cmh_gate_zero/` package.
3. `finum.targets.REGISTRY` remains the single public dispatch table. Public target ids stay
   `A1`, `A2`, `A3`, `A4`, `A5`, `kls`, `loc-engine`, `kls-align`, and `cmh-gate-zero`.
4. CLI commands, profiles, run configuration, record contents, artifact schema, and historical
   artifacts do not change.
5. Active tests and target briefs use the new implementation paths. Append-only explorations,
   prior decisions, reviews, and run artifacts retain their historical paths.

## Compatibility

The CLI and artifact interfaces are unchanged. Direct Python imports of implementation modules
move from the old flat paths to the program packages; these modules are internal harness code,
and the updated oracle suite covers the new paths. Registry consumers continue to import only
`finum.targets.REGISTRY`.

## Validation

- `uv run python -B -m finum check`: every public target check passes;
- focused moved-target suite: 56 tests pass;
- full `experiments` pytest suite: 91 tests pass, including the slow Monte Carlo lane;
- `python3 -B research/check_ledger.py`: 2 ledgers, 170 nodes, 632 labels, 0 errors;
- `python3 -B -m unittest discover -s research/tests -p 'test_*.py'`: 38 tests pass; and
- active-reference and `git diff --check` audits pass.
