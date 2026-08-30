# Decision: add a sibling finum target `kls-screen` instead of extending `kls-align`

Date: 2026-08-30

Role: orchestrator, applying the draft decision record proposed by the `finum` agent of run
`w4a01` (see `research/explorations/2026-08-30-finum-align-screened-supply-w4a01.md`).

## Decision

Add a sibling `finum` target `kls-screen` rather than extending `kls-align`.

## Rationale

`kls-align` answers `q:alignment` with a recorded schema cited by prior artifacts; the
`q:weighted` screening question needs different observables ($\lambda_{\rm cut}$,
$W_{\rm cut}$, the exact weighted perimeter, competitor-based surrogate excess,
$\hat\theta(\kappa)$), a different time grid (two-scale, to pass a paired snapshot-refinement
gate the alignment integrands do not need), and a cylinder-cut spectator mode. A sibling target
keeps both record schemas stable; a regression test asserts the `kls-align` gate set and schema
are unchanged.

## New code

- `experiments/finum/localization/screening.py` — cancellation-free vectorized tilted-Laplace
  log-tail primitives; exact weighted perimeter; two competitor families; exact Cauchy quadratic
  form; $\lambda_{\rm cut}$ with a dense reference.
- `experiments/finum/targets/kls/screening.py` — profiles `smoke`/`standard`/`high-n`.
- `experiments/tests/test_18_screening_cut_scale.py` — oracle tests.

## Validation

At harvest into the wave branch: `uv run python -m finum check` passes for all targets and the
full pytest suite passes (recorded below in the wave commits). Both record runs
(`research/runs/2026-08-30T175028.209516Z-kls-screen.jsonl`,
`research/runs/2026-08-30T175419.597477Z-kls-screen.jsonl`) pass all ten target gates.

## Epistemic note

The target's excess observable is a competitor surrogate with $\hat e\le e$ (it understates the
true excess; growth is the robust direction). Every record is labeled `diagnostic_only` with
`proof_status: no-proof/no-universal-conclusion`. Harness work changes no mathematical status.
