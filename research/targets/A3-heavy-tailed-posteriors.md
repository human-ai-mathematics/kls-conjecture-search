# A3 — Heavy-tailed posteriors beyond classical LSI

- **Ledger:** `conj:a3`, `prop:a3-horseshoe` (+ `q:a3-*`) · **Manuscript:** `A3-heavy-tailed-posteriors.tex` (`sec:a3`)
- **Status:** open · **Evidence:** none · **Calibration anchor:** `thm:a3-student` (sharp, imported)

## Goal (current best statement)

Weighted Poincaré with a tail-growing weight:
```
Var_π(f) ≤ C_w · Σ_j ∫ a_j(θ_j) |∂_j f|² dπ,   a_j ≍ τ² + θ_j²,
```
with `C_w` from the 1D Hardy quantities (`thm:hardy-1d`), tail scaling `C_w ≍ max_j α_j⁻²`,
**sharp** for Student-t/generalized-Cauchy (`thm:a3-student`), Hardy-certified up to factor 4 for
the horseshoe (`prop:a3-horseshoe`).

## Obstructions it must respect

- `obs:heavy-tail-no-classical` — classical Poincaré/LSI/T₂ fail; only weighted/weak inequalities.
- `obs:flat-direction` (tail reading) — a light-tailed likelihood can *restore* classical
  inequalities (`warn:a3-likelihood`); A3 is about regimes where the tail *survives* into the
  posterior.

## Sub-questions (ledger)

| node | what | difficulty |
|------|------|-----------|
| `q:a3-student` | record the solved Student-t case as the calibration statement | calibration |
| `q:a3-horseshoe` | close the factor-4 Hardy gap → sharp `C_HS(τ)` (log pole at 0) | **cleanest open 1D** |
| `q:a3-catalogue` | scale-mixture catalogue (tail index, Hardy const, Stein-kernel) | medium |
| `q:a3-weak` | weak Poincaré rate `β_WPI(s) ≍ s^{−2/α}` for unweighted dynamics | medium |
| `q:a3-hierarchical` | propagate through likelihood + global-local dependence (non-product) | **frontier** |

## Numerical plan (finum)

1. Hardy-evaluator: numerically compute `sup_x μ(tail)∫^x dt/(a(t)p(t))` for any 1D marginal.
2. Calibration: `cal-cauchy` weighted spectral gap must match closed-form `λ_{β,d}`.
3. `stress-student` over `ν`: classical `C_P = ∞`, weighted finite, scaling `C_w ≍ α⁻²`.
4. `stress-horseshoe`: locate `C_HS(τ)` inside `[B_HS, 4B_HS]` against candidate closed forms.
5. Tensorization check: product priors are dimension-free in the weighted metric.

**Promotion to `numerical-strong`:** weighted PI holds where classical fails across the heavy-tail
stress tier, tail scaling confirmed, calibration matched, `evidence_run` set.

## Evidence log

_(none yet)_

## Cross-links

- `conj:a4` `q:a4-modified` is the `W₂` counterpart (modified transport cost).
- Shares `obs:flat-direction` with A1; the funnel half of A5 (`q:a5-reparam`) reuses the
  half-Cauchy heavy-tail obstruction.
