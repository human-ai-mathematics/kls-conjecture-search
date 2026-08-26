# Simplify the `finum` harness boundary

- **Date:** 2026-08-26
- **Type:** numerical-harness refactor
- **Scope:** `experiments/` execution interface, artifacts, package layout, tests, and harness docs
- **Mathematical effect:** none

## Problem

The numerical kernels were mostly cohesive, but the outer harness exposed accidental complexity.
Targets returned an undocumented `(records, extra)` pair whose second mapping mixed run inputs
with derived results. JSONL records had no artifact-level schema version. The CLI silently
defaulted to A1, exposed a target-specific `--heavy` flag, and described the legacy localization
engine as if it were a KLS route target. Comparison objects used theorem-like `REFUTED` language
even though numerical artifacts cannot change logical status.

The README duplicated changing mathematical route summaries, the advertised geometry/instance
abstractions were not actually shared by targets, and three Monte Carlo regressions accounted for
most of the default pytest runtime without being identified as a separate validation lane.

## Decision

1. Every target returns `RunResult(records, config, summary)`. `RunResult.validate()` enforces the
   minimal common record boundary: every target-owned record has a string `kind`.
2. `TargetSpec` is the executable registry entry. It records the target description,
   stochasticity, and named profiles. The CLI provides `list`, `check`, and explicit
   `run TARGET --profile PROFILE`; there is no default target.
3. Future JSONL artifacts use a versioned `_provenance` envelope separating configuration from
   environment, followed by target records and one `run-summary`. Historical artifacts remain
   unchanged.
4. Artifact comparisons use evidence classes `exact`, `directional`, and `calibration`, with
   neutral outcomes `exceeds`, `within`, `unavailable`, `match`, and `mismatch`. These are not
   ledger statuses. The old `Verdict`/`falsify` vocabulary is removed.
5. The public `kls-loc` target becomes `loc-engine`, accurately identifying a retained legacy
   engine regression with no route observable. The old `--target kls-loc --heavy` spelling remains
   a CLI compatibility path; historical artifacts retain their original id.
6. The unused geometry zoo is removed. The sample-based `Instance` type is folded into A1, its
   only consumer, and the logistic helper moves beside the MALA sampler used by A1 and A2.
7. The CMH target becomes an internal package, with exact-certificate and algebraic-countermodel
   code separated from the remaining target orchestration. Its public target id and mathematical
   battery do not change.
8. `finum check` is the smoke lane, `pytest -m "not slow"` is the normal development lane, and
   full pytest retains the expensive Monte Carlo oracle regressions. `selftest` and `run --target`
   remain compatibility spellings for active repository instructions and historical notes.
9. `experiments/README.md` describes only the harness boundary, commands, targets, artifact
   contract, and package layout. Mathematical conclusions and historical interpretation remain in
   the research planes.

## Compatibility

Append-only explorations, reviews, and run artifacts are not edited. Artifact schema version 1
applies only to future runs. Direct Python callers of target `run_records()` must consume
`RunResult`; this is an intentional internal API break covered by the oracle suite.

## Validation

- `uv run python -m finum check`: every target check passes;
- `uv run pytest -m "not slow"`: 88 pass, 3 deselected in 11.66 seconds;
- `.venv/bin/pytest`: 91 pass in 62.37 seconds, including the slow Monte Carlo lane;
- an end-to-end `finum run kls` produces schema version 1 with separate config and summary;
- `python3 -B research/check_ledger.py`: 2 ledgers, 170 nodes, 632 labels, 0 errors;
- `python3 -B -m unittest discover -s research/tests -p 'test_*.py'`: 38 pass; and
- `git diff --check`: clean.
