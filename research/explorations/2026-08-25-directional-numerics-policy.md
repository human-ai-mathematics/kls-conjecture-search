# Directional-only numerics policy

- **Date:** 2026-08-25
- **Scope:** repository harness and numerical/proof workflow
- **Outcome:** remove the `numerical-strong` category; retain only provenance-stamped,
  directional numerical research diagnostics

## Decision

Numerical work in this repository guides intuition, sharpens candidate statements, stress-tests
implementations, and searches for counterexamples. Passing calibration, convergence checks, or a
finite shared suite does not validate a mathematical claim or any step of a proof. A node reaches
`status: proved` only through a standalone proof dossier and its independent `checked_by` review.

The shared instance registry remains useful for comparability and for avoiding cherry-picked
happy paths, but survival of the registry has no promotion semantics. The former
`numerical-strong` category and its self-declared shared-battery gate have therefore been removed
from the checker, tests, ledger vocabulary, and active workflow documentation.

Exact symbolic, rational, or interval output may reveal a genuine certificate. It acquires
logical force only after the certificate is persisted as an analytic proof or refutation and
checked independently; its appearance in a `finum` run is research provenance, not certification.

Historical exploration records mentioning `numerical-strong` remain unchanged because
`research/explorations/` is append-only. The regression suite intentionally retains the string in
a rejection test so the retired category cannot silently re-enter the schema.

No mathematical claim node, dependency edge, or proof status changed in this policy update.

## Validation

- `python3 research/check_ledger.py`: 172 nodes, 0 errors, 0 warnings.
- `python3 -m unittest discover -s research/tests -p 'test_*.py'`: 22 tests passed.
- `cd experiments && uv run --offline pytest`: 90 tests passed.
- `cd experiments && uv run --offline python -m finum selftest`: 0 failures.

