# Decision: add the finum target `cmh-ab` next to `cmh-gate-zero`

Date: 2026-08-30

Role: orchestrator, applying the draft decision record from the `finum` run `w4c02`
(`research/explorations/2026-08-30-finum-cmh-ab-m9-w4c02.md`, Section 7).

## Decision

Add the finum target `cmh-ab` next to `cmh-gate-zero`.

## Rationale

The CMH linear-recovery probe reduced its gate to one matrix inequality
$(\mathrm{AB})$: $\mathsf R\succeq\rho\mathsf N-\beta I$. That inequality is computable exactly
on the two exactly solvable moment-map families (one-dimensional laws and Dirichlet) and
directionally on analytic source potentials, and the two Monge–Ampère reservoirs
$\mathsf R_A,\mathsf R_Q$ can be separated, which the existing gate-zero battery cannot do. The
M9 second-variation probe shares the same source-potential engine.

## Scope

`experiments/finum/targets/kls/cmh_ab/**` and `experiments/tests/test_18_cmh_ab.py`;
`cmh_gate_zero` is imported read-only and unmodified. One registry entry and one
`experiments/README.md` table row.

## Validation

`uv run python -m finum check` green on every target; the 34 new oracle tests pass at harvest
into the wave branch (recorded in the wave commits). Four independent cross-checks pin the
index placement of $\mathsf D$; the Gaussian-product Galerkin anchor is exact and attained.

## Boundary

Exact Loewner verdicts are refutation candidates only; all quadrature is directional; no
ledger, manuscript, routes, gating, bibliography, or review file is touched by the target.
Harness work changes no mathematical status.
