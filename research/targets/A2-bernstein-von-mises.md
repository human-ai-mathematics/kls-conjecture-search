# A2 — Asymptotic constants via Bernstein–von Mises

- **Ledger:** `conj:a2`, `thm:a2-target` (+ `q:a2-*`) · **Manuscript:** `A2-bernstein-von-mises.tex` (`sec:a2`)
- **Status:** vanishing-leverage logistic Poincaré and subquadratic/logistic tail rigidity are proved under independent agent review; the general strong-Laplace transfer and broader asymptotic programme remain open · **Evidence:** none
- **Reviewed solutions:** [`../../solutions/a1-harmonic-mode-leverage.tex`](../../solutions/a1-harmonic-mode-leverage.tex) and [`../../solutions/a2-subquadratic-tail-rigidity.tex`](../../solutions/a2-subquadratic-tail-rigidity.tex)
- **Review record:** [`../reviews/2026-08-21-a1-a2-independent-agent-audit.md`](../reviews/2026-08-21-a1-a2-independent-agent-audit.md)
- The `n→∞` shadow of A1; the cleanest place to read a scaling law off numerics.

## Goal (current best statement)

```
n·C_P(π_n) --P_{θ₀}--> λmax(I(θ₀)⁻¹) = 1/λmin(I(θ₀)),
```
and, under global hypotheses (`osc(r_n)=o_P(1)`), the same limit for `n·C_LS`, `n·C_TCI`
(`thm:a2-target`). The content is the limit of the **rescaled** constant, not the `1/n`
(`eq:a2-scaling`).

For fixed-dimensional Gaussian-prior logistic regression, the certified model-specific theorem
replaces global oscillation by vanishing maximal mode leverage and proves the Poincaré line only.
Global LSI/$T_2$ remain prior-tail quantities.

## 2026-08-21 analytic audit and independent review

See
[`../explorations/2026-08-21-a2-strong-laplace-and-global-constants.md`](../explorations/2026-08-21-a2-strong-laplace-and-global-constants.md)
and
[`../explorations/2026-08-21-a2-subquadratic-tail-rigidity.md`](../explorations/2026-08-21-a2-subquadratic-tail-rigidity.md).

- **Analytic conditional-implication draft:** `thm:a2-target` follows directly from
  Holley--Stroock, affine pushforward, and covariance lower bounds once
  `osc(r_n)=o_P(1)` is assumed. The open work is verifying that hypothesis in a useful model
  class, or proving a weaker Poincaré-only stability theorem. A generic tail/no-bottleneck
  condition is not logically equivalent to global vanishing oscillation. Repository proof
  certification is a separate step.
- **Source correction:** the cited Chewi--Stromme Poincaré theorem assumes a unique global
  minimizer, a finite inverse global PL constant `C_PL < ∞` (equivalently a positive PL rate),
  normalizability, and a Laplacian/gradient growth condition; a unique nondegenerate minimizer
  alone is insufficient. Applying its fixed-potential limit to random posterior potentials also
  requires a uniform transfer theorem.
- **Certified logistic dichotomy:** for every finite binary-logistic data set with finite
  covariates and fixed positive-definite Gaussian prior covariance, large exponential tilts retain
  the prior's quadratic log-MGF coefficient. Consequently
  `C_LS(π_n)=C_TCI(π_n)=λmax(Σ₀)` for every `n`, so their `n`-rescalings diverge. The
  Fisher limit remains the Poincaré target, but global LSI/T₂ are Fisher-local only in a
  genuinely global Gaussian-comparison/quadratic-tail class.
- **T₂ lower-bound lemma:** the transport sandwich uses
  `T₂(C) ⇒ Cov(π) ⪯ C I`, not the Poincaré linear-test lemma.
- **Certified vanishing-leverage logistic theorem:** with `Ĥₙ=∇²Vₙ(θ̂ₙ)` and
  `ηₙ=maxᵢ sqrt(xₙᵢᵀĤₙ⁻¹xₙᵢ)`, fixed-dimensional `ηₙ→0` implies
  `C_P(πₙ)=(1+o(1))λmax(Ĥₙ⁻¹)`. A1 supplies the bounded-Hessian factor-one upper bound and a
  radial envelope whose exponential domination gives whitened covariance convergence for the
  lower bound. With `Ĥₙ/n→I(θ₀)`, this proves the exact Fisher coefficient.
- **Certified subquadratic-tail extension:** the exact prior-scale identity holds for any finite convex
  perturbation whose Gaussian average along one top prior-covariance translate is `o(t²)`; uniform
  `O(1+‖θ‖ᵖ)`, `0≤p<2`, is sufficient. Centering changes only the linear MGF term.
- **Shrinking-prior no-go:** if `‖Σ₀,n⁻¹‖/n→0`, the Gaussian prior is negligible at curvature
  order but
  `n·C_LS=n·C_TCI=n·λmax(Σ₀,n)→∞`. Making the global constants `O(1/n)` forces order-`n` prior
  precision and changes the ordinary Fisher target. Moving prior means additionally require the
  prior-score term to be `o(√n)` for full local negligibility.

## Obstruction it must respect

- `obs:tv-insufficient` — **BvM-in-TV does not give the constants.** The refined statement needs
  a strong-Laplace / tail hypothesis, never TV alone.
- `obs:gaussian-tail-rigidity` — fixed Gaussian-prior logistic has prior-scale global LSI/$T_2$.

## Sub-questions (ledger)

| node | what | difficulty |
|------|------|-----------|
| `q:a2-poincare` | verify random-design vanishing leverage; extend beyond bounded-Hessian logistic and maximal-row control | entry |
| `q:a2-lsi` | classify genuinely quadratic-tail/global-PL positive cases and localized alternatives | hard |
| `q:a2-multimodal` | exponential `C_P` vs removable symmetry artifact (→ A5) | hard |
| `q:a2-highdim` | growing dimension `d = d_n` | open |

## Numerical plan (finum)

1. For logistic, record `ηₙ`, `n·λmax(Ĥₙ⁻¹)`, and the deterministic radial upper factor before
   sampling. Treat `ηₙ≥1` as certificate failure, not posterior failure.
2. `sweep(make_post, n=[…], reps)` over regular logistic (`stress-bvm-sweep`). Record
   `n*λmax(empirical Cov)` as a directional scale estimate and pair it with the radial upper
   bound. Even with explicit sampling and mixing error control, use it as a refutation aid rather
   than a verdict; an error-controlled one-dimensional spectral estimate remains a research
   diagnostic. Poisson remains directional until the unbounded-Hessian factor-one domain step is
   closed.
3. **Refutation diagnostic:** on `stress-contamination`, the computation should expose the
   divergent linear test behind the analytic obstruction to a bare “BvM ⇒ limit” claim.
4. `C_LS` discriminator (`q:a2-lsi`): use the analytic subquadratic identity and the
   `Σ₀,n=n^{-α}I` prior phase diagram; compare Fisher-local models only after changing the global
   tail contract.
5. **A1↔A2 consistency:** report `|n·(A1 bulk bound) − λmax(I⁻¹)|` as `n→∞`.

**Research use only:** use data-draw and `n`-sweeps, spectral diagnostics when available, and the
contamination trap to study the proposed limit and locate possible failure modes. Convergence of a
covariance lower estimate, or agreement with an independently proved sandwich, remains a
directional research diagnostic: it does not validate or certify the theorem or its proof. Rigorous refutation
still requires an analytic argument or exact lower bound.

## Numerical research log

_(none yet — the 2026-08-21 contribution is analytic; the prior-scaling test is deterministic
algebra, not evidence. The retired one-chain logistic diagnostic, its obsolete trend flag, and the
missing repeated-draw/two-sided checks are preserved in the
[`2026-08-21 A2 audit`](../explorations/2026-08-21-a2-strong-laplace-and-global-constants.md), not as live
ledger evidence.)_

## Cross-links

- `conj:a1` finite-sample counterpart; `q:a4-certificate` consumes this scale; on the symmetry quotient,
  this limit re-emerges from `conj:a5-metastable`.
