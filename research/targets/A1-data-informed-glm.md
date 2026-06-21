# A1 — Data-informed GLM Poincaré constant

- **Ledger:** `conj:a1` (+ `q:a1-*`) · **Manuscript:** `modules/open-targets/A1-data-informed-glm.tex` (`sec:a1`)
- **Status:** open · **Evidence:** none · **Baseline to beat:** `thm:glm-fi` (`C_P ≤ λmax(Σ₀)`)
- **The flagship.** Most tractable (log-concave), and the entry point for the whole numerical channel.

## Goal (current best statement)

For the Gaussian-prior convex GLM posterior with `H(θ) = Σ₀⁻¹ + XᵀW(θ)X`, `W(θ)=diag(ℓ''ᵢ(xᵢᵀθ))`:
```
C_P(π) ≤ C·{ λmax(A_W̄⁻¹) + E_π[λmax(H⁻¹); G_W̄^c] }
       ≤ C·{ λmax(A_W̄⁻¹) + λmax(Σ₀)·π(G_W̄^c) },
A_W̄ = Σ₀⁻¹ + XᵀW̄X,   G_W̄ = {θ : XᵀW(θ)X ⪰ XᵀW̄X}.
```
Refinement question marks: the universal constant `C`; the right `W̄` recipe; whether the clean
`λmax(Σ₀)·π(G^c)` form or the sharper integrated tail is needed; the `1/n` scale.

## Obstruction it must respect

- `obs:flat-direction` — **no tail-free bound exists.** Likelihood curvature vanishes in tail
  directions, so the bound *must* carry a penalty term. A refined statement without one is wrong.

## Sub-questions (ledger)

| node | what | difficulty |
|------|------|-----------|
| `q:a1-poincare` | specialize Brascamp–Lieb + log-concave self-improvement; make `C` explicit | entry |
| `q:a1-barw` | computable `W̄` from `(X,y,Σ₀)`: rowwise vs quantile vs spectral | low |
| `q:a1-tail` | certify `π(G_W̄^c) ≤ ε` — **the heart** | hard |
| `q:a1-sharp` | correct `1/n` scale; A1↔A2 consistency | medium |
| `q:a1-lsi` | data-informed `C_LS` (bulk LSI + prior drift), then `C_TCI` | harder |
| `q:a1-sampling` | translate to Langevin/MALA complexity | applied |

## Numerical plan (finum)

1. Build `GLMPosterior(X, y, Σ₀, link)`; sample (MALA/NUTS, `R̂`/ESS gate).
2. `cp_low = poincare_lower(samples) = λmax(Cov)`; `cp_est = poincare(samples)`.
3. For each `W̄` recipe: evaluate `λmax(A_W̄⁻¹)`, `E_π λmax(H⁻¹)`, `π(G_W̄^c)` → the bound.
4. `check(cp_low, cp_est, bound, baseline=glm_data_free)` → `{holds, tightness, beats_baseline}`.
5. Sweep instances from `../knowledge/instances.md`: `cal-glm-linear` (must be tight),
   `stress-logit-separable` (tail-free bound must be falsified), `stress-wide` (`D>n`),
   `stress-logit-bulk` (must beat baseline substantially).
6. Refinement readout: best `W̄`, realized `C`, and the sharpness ratio `λmax(Σ₀)/λmax(Cov_π)`.

**Promotion to `numerical-strong`:** holds across the whole A1 stress tier (not just happy cases),
tightness bounded below, beats baseline on the bulk-dominated instances, with `evidence_run` set.

## Evidence log

_(none yet — append `YYYY-MM-DD` rows: instance set, holds/tightness, witness, run artifact)_

## Cross-links

- `conj:a2` is the `n→∞` shadow — a bulk-tight A1 bound must reproduce `λmax(I⁻¹)` (`q:a1-sharp`).
- `conj:a4` is the `W₂` analogue at the same bulk scale.
- Shares `obs:flat-direction` with A3 (tail) and A5 (funnel).
