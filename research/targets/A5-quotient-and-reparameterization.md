# A5 — Quotient and reparameterization constants

- **Ledger:** `thm:a5-monotone`, `prop:a5-ratio` (proved), `conj:a5-metastable` (+ `q:a5-*`) · **Manuscript:** `A5-quotient-and-reparameterization.tex` (`sec:a5`)
- **Status:** mixed (monotonicity proved; metastability open) · **Evidence:** none
- The escape hatch the other targets invoke (separates symmetry artifacts from physical structure).

## Goal (current best statements)

**Proved (manuscript):** monotonicity `C_P(π/G) ≤ C_P(π)` (`thm:a5-monotone`); the spectral ratio
`C_P(π)/C_P(π/G) = λ_inv / min(λ_inv, λ_noninv)` (`prop:a5-ratio`).

**Open (`conj:a5-metastable`):**
```
C_P(π_Θ)        ≍ e^{nΓ} poly(n)                  (raw — exponential barrier Γ)
C_P(π_{Θ/S_K}) = (1+o_P(1))/n · λmax(I(θ_*)⁻¹)    (quotient — A2 re-emerges)
```

## Obstruction it must respect

- `obs:symmetry-vs-physical` — quotient helps **iff** the slow eigenfunction is non-invariant.
  Importing a global metastability bound without checking the representation type is the error.

## Sub-questions (ledger)

| node | what | difficulty |
|------|------|-----------|
| `q:a5-qbvm` | prove the quotient line (A2 on the orbit space) | bridge to A2 |
| `q:a5-metastable` | prove the raw line with explicit barrier Γ (Eyring–Kramers) | hard |
| `q:a5-detect` | from samples, test whether the slow mode is invariant or not | numeric |
| `q:a5-stratified` | `C_LS`/`C_TCI` on stratified/orbifold quotient spaces | hard |
| `q:a5-reparam` | finite-sample centered/non-centered funnel comparison | medium |

## Numerical plan (finum)

1. `stress-folded-well`: estimate raw vs folded `C_P`; confirm `e^{a²/2σ²}` vs `O(σ²)`.
2. `q:a5-detect`: estimate the slowest eigenfunction from samples and test its `G`-invariance —
   the practical discriminator (uses `lem:linear-test-lower` / hard-direction estimators).
3. `stress-neal-funnel`: `C_P` in centered (`∞`) vs non-centered (`max{s²,1}`) coords; half-Cauchy
   `p(τ)` (heavy-tail obstruction, defeats Poincaré even non-centered) vs `log τ` + Gaussian tails.
4. Sanity (proved nodes): estimated quotient `C_P ≤ raw C_P`.

**Promotion to `numerical-strong`:** the raw/quotient gap and the funnel reparameterization
behaviour reproduced across the A5 stress tier, with `evidence_run` set.

## Evidence log

_(none yet)_

## Cross-links

- `conj:a5-metastable` quotient line = `conj:a2` `eq:a2-target`; supplies the escape for A2
  `q:a2-multimodal` and A4 `q:a4-multimodal`. Funnel half reuses A1 `obs:flat-direction` and A3
  heavy-tail obstruction.
