# A4 — Transport constants for variational inference

- **Ledger:** `conj:a4` (+ `q:a4-*`) · **Manuscript:** `A4-variational-inference.tex` (`sec:a4`)
- **Status:** open · **Evidence:** none · **Baseline to beat:** `thm:glm-fi` (prior-scale `C_TCI`)

## Goal (current best statement)

Certified VB error bars at **posterior** (not prior) scale, on a KL sublevel covering the VB
optimizer:
```
C_{Q,r}(π) ≲ λmax(A_W̄⁻¹) + tail,      (W₂ certificate)
C_mean,Q(π) ≤ sup_{‖u‖=1} K(u),         (posterior-mean certificate)
```
giving `W₂²(q*,π) ≤ 2 C_{Q,r} KL` and `‖E_{q*}θ − E_π θ‖² ≤ 2 C_mean,Q KL`, *given* a computable
KL upper bound (`rem:a4-elbo` — a separate hypothesis).

Hierarchy: `C_mean,Q ≤ C_{T₁,Q} ≤ C_Q ≤ C_TCI`, and the gaps can be huge.

## Obstructions it must respect

- `obs:restricted-not-finite` — even `C_Q` can be `∞` (heavy tails); finiteness needs the KL
  sublevel / bounded `Q` / modified cost.
- `obs:flat-direction` — the bulk vs prior-scale gap is the same vanishing-curvature story as A1.
- `obs:symmetry-vs-physical` — multimodal lower bounds are **family-dependent**; quotient first.

## Sub-questions (ledger)

| node | what | difficulty |
|------|------|-----------|
| `q:a4-restricted` | bulk-scale `C_Q`, `C_{Q,r}` for GLM posteriors (W₂ analogue of A1) | entry |
| `q:a4-mean` | first-moment `C_mean,Q` — the number a VB user reports | medium |
| `q:a4-modified` | modified transport cost for heavy tails (W₂ counterpart of A3) | hard |
| `q:a4-multimodal` | family-dependent barriers: `e^{cΔ²}` vs `Δ²` (mode collapse) | hard |
| `q:a4-elbo` | couple `C_{Q,r}` to a computable KL certificate → end-to-end error bar | applied |

## Numerical plan (finum)

1. Mean-field Gaussian `Q`; estimate `sup_{q∈Q, KL≤r} W₂²(q,π)/(2 KL)` and `C_mean,Q`.
2. GLM instances: confirm `C_{Q,r}` reaches posterior scale `λmax(A_W̄⁻¹)`, beating the
   prior-scale `thm:glm-fi`.
3. `stress-ep-tails`: a global `C_Q` claim must be FALSIFIED; `C_{Q,r}` on a KL sublevel finite.
4. `stress-sep-mixture`: compute the reweighting witness (`≍ e^{cΔ²}`) and the mode-collapse
   witness (`≍ Δ²`) — confirm the two barrier scalings.

**Promotion to `numerical-strong`:** posterior-scale `C_{Q,r}` confirmed on GLM, the global-`C_Q`
infinite case correctly falsified, the two multimodal scalings reproduced, `evidence_run` set.

## Evidence log

_(none yet)_

## Cross-links

- Consumes A1 (bulk scale), A2 (Fisher limit), A3 (modified cost), A5 (quotient escape).
