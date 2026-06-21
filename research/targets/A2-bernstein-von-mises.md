# A2 — Asymptotic constants via Bernstein–von Mises

- **Ledger:** `conj:a2`, `thm:a2-target` (+ `q:a2-*`) · **Manuscript:** `A2-bernstein-von-mises.tex` (`sec:a2`)
- **Status:** open · **Evidence:** none
- The `n→∞` shadow of A1; the cleanest place to read a scaling law off numerics.

## Goal (current best statement)

```
n·C_P(π_n) --P_{θ₀}--> λmax(I(θ₀)⁻¹) = 1/λmin(I(θ₀)),
```
and, under global hypotheses (`osc(r_n)=o_P(1)`), the same limit for `n·C_LS`, `n·C_TCI`
(`thm:a2-target`). The content is the limit of the **rescaled** constant, not the `1/n`
(`eq:a2-scaling`).

## Obstruction it must respect

- `obs:tv-insufficient` — **BvM-in-TV does not give the constants.** The refined statement needs
  a strong-Laplace / tail hypothesis, never TV alone.

## Sub-questions (ledger)

| node | what | difficulty |
|------|------|-----------|
| `q:a2-poincare` | weakest tail hypothesis for the `C_P` limit (random-posterior Chewi–Stromme) | entry |
| `q:a2-lsi` | when is the `C_LS` limit Fisher-local (`λmax(I⁻¹)`) vs global (`1/μ_PL`)? | hard |
| `q:a2-multimodal` | exponential `C_P` vs removable symmetry artifact (→ A5) | hard |
| `q:a2-highdim` | growing dimension `d = d_n` | open |

## Numerical plan (finum)

1. `sweep(make_post, n=[…], reps)` over regular logistic/Poisson (`stress-bvm-sweep`).
2. `law = sweep.fit("n*cp -> a")`; compare `a` to `a2_fisher_target = λmax(I(θ₀)⁻¹)`.
3. **Falsification gate:** on `stress-contamination`, a "BvM ⇒ limit" claim must come back
   FALSIFIED (linear test diverges).
4. `C_LS` discriminator (`q:a2-lsi`): on a Fisher-local and a `stress-non-fisher-local` model,
   compare `n·C_LS` estimate to `λmax(I⁻¹)` vs `1/μ_PL`.
5. **A1↔A2 consistency:** report `|n·(A1 bulk bound) − λmax(I⁻¹)|` as `n→∞`.

**Promotion to `numerical-strong`:** the limit is reproduced across data draws and `n`-sweep, the
contamination trap is correctly falsified, with `evidence_run` set.

## Evidence log

_(none yet)_

## Cross-links

- `conj:a1` finite-sample counterpart; `conj:a4` consumes this scale; on the symmetry quotient,
  this limit re-emerges from `conj:a5-metastable`.
