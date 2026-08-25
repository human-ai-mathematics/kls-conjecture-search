# A1 — Data-informed GLM Poincaré constant

- **Ledger:** `conj:a1` (+ `q:a1-*`) · **Manuscript:** `modules/open-targets/A1-data-informed-glm.tex` (`sec:a1`)
- **Status:** bounded-Hessian factor one, deterministic mode leverage, and the fixed-dimensional vanishing-leverage limit are proved under independent agent review; the universal bulk--tail comparison, finite-sample improvement regime, and generalizations remain open · **Evidence:** none · **Baseline to beat:** `thm:glm-fi` (`C_P ≤ λmax(Σ₀)`)
- **Reviewed solution:** [`../../solutions/a1-harmonic-mode-leverage.tex`](../../solutions/a1-harmonic-mode-leverage.tex)
- **Review record:** [`../reviews/2026-08-21-a1-a2-independent-agent-audit.md`](../reviews/2026-08-21-a1-a2-independent-agent-audit.md)
- **The flagship.** Most tractable (log-concave), and the entry point for the whole numerical channel.

## Goal (current best statement)

For the Gaussian-prior convex GLM posterior with `H(θ) = Σ₀⁻¹ + XᵀW(θ)X`, `W(θ)=diag(ℓ''ᵢ(xᵢᵀθ))`:
```
C_P(π) ≤ C·{ λmax(A_W̄⁻¹) + E_π[λmax(H⁻¹); G_W̄^c] }
       ≤ C·{ λmax(A_W̄⁻¹) + λmax(Σ₀)·π(G_W̄^c) },
A_W̄ = Σ₀⁻¹ + XᵀW̄X,   G_W̄ = {θ : XᵀW(θ)X ⪰ XᵀW̄X}.
```
This inequality is the analytic draft `prop:a1-bulk-tail`; it is not a ledger-certified proof until
the repository's separate solution/review step is complete. For log-Hessian-Lipschitz GLMs, the
certified mode-leverage theorem supplies a deterministic `W̄` and a one-dimensional radial tail
bound. For globally bounded Hessian (including finite Gaussian-prior logistic), the certified
noncompact spectral-domain theorem supplies factor one and the exact fixed-dimensional A2
coefficient under vanishing maximal leverage. The open goal is a finite-sample regime in which the
computable number beats the prior scale, plus extensions beyond bounded Hessian.

## 2026-08-21 analytic audit and independent review

See
[`../explorations/2026-08-21-a1-bulk-tail-audit.md`](../explorations/2026-08-21-a1-bulk-tail-audit.md)
and
[`../explorations/2026-08-21-a1-harmonic-mean-and-mode-leverage.md`](../explorations/2026-08-21-a1-harmonic-mean-and-mode-leverage.md).

- **Analytically established in draft (modulo the cited Milman comparison):** Brascamp--Lieb applied to every
  1-Lipschitz test gives spread squared at most
  `E λmax(H⁻¹)`; log-concave spread-to-gap self-improvement then proves the two displayed
  bulk--tail inequalities with a universal constant. Repository promotion still requires an
  independently checked solution artifact. The open payload is an explicit constant and a
  computable `W̄` whose certified expression improves on the prior scale.
- **Bounded-Hessian factor-one theorem:** Veysseire's source remains compact and is not applied
  directly. A separate spectral-localization/Bochner--Kato argument gives
  `C_P ≤ E[1/λmin(H)]` under an explicit closed-Bochner-domain contract. Schrödinger conjugation
  verifies that contract when `mI ⪯ H ⪯ MI`, which includes every finite Gaussian-prior logistic
  posterior. Unbounded-Hessian, nonsmooth, and weakly convex extensions remain open.
- **Mode-leverage selection theorem:** if
  `|log ℓᵢ''(s)-log ℓᵢ''(t)| ≤ Lᵢ|s-t|`, define
  `αᵢ=Lᵢ sqrt(xᵢᵀĤ⁻¹xᵢ)` and `η=max αᵢ`. The mode-whitened potential is bracketed by
  `g₋(r;η)=(exp(-ηr)+ηr-1)/η²` and
  `g₊(r;η)=(exp(ηr)-ηr-1)/η²`. This gives computable weights
  `w̄ᵢ(R)=exp(-αᵢR)wᵢ(θ̂)` and an explicit ratio of radial integrals bounding the tail.
- **Exact bounded-Hessian asymptotic corollary:** for fixed `d`, `ηₙ→0` implies
  `C_P(πₙ)=(1+o(1))λmax(Ĥₙ⁻¹)`. The upper bound uses factor one; the lower bound follows because
  the radial envelope gives uniform integrability and covariance convergence of the whitened law.
  If `Ĥₙ/n→I(θ₀)`, this yields the exact A2 coefficient.
- **Analytic obstruction draft, not numerical evidence:** for the one-observation family
  `π_a(dθ) ∝ exp(-θ²/(2σ²)) sigmoid(aθ)dθ`, the posterior tends to a half Gaussian, while the
  inverse Hessian at the mode tends to zero. Hence
  `C_P(π_a) / (σ⁻²+a²w(a θ̂_a))⁻¹ → ∞`; no universal tail-free mode-Hessian bound exists.
- **General sharpness contract:** outside the bounded-Hessian/vanishing-leverage class, if
  `A_W̄/n → I` and the integrated tail is `o_P(1/n)`, the universal comparison still yields the
  A2 scale only up to its fixed factor. No exact claim is made there.
- **Certified global LSI/T₂ obstruction:** for every finite binary-logistic likelihood with a fixed
  Gaussian prior,
  `C_LS(π) = C_TCI(π) = λmax(Σ₀)` exactly. Thus `q:a1-lsi` must target local/restricted
  constants (or a different global tail class) if it is to improve with the data.

## Obstruction it must respect

- `obs:flat-direction` — **narrow saturating-likelihood obstruction.** Logistic likelihood
  curvature vanishes in remote directions, so a positive mode/bulk curvature cannot provide a
  global likelihood floor. The analytic family above rules out a universal inverse-mode-Hessian
  bound; it does not rule out the Gaussian-linear tail-free bound, the prior bound, or
  covariance/full-distribution bounds.
- `obs:gaussian-tail-rigidity` — global logistic LSI/$T_2$ equal the prior scale exactly.

## Sub-questions (ledger)

| node | what | difficulty |
|------|------|-----------|
| `q:a1-poincare` | review the separate bulk--tail comparison, make `C_M` explicit, and extend factor one beyond bounded Hessian | prerequisite |
| `q:a1-barw` | use mode-leverage `W̄(R)` as baseline; improve maximal-row conservatism spectrally | low/medium |
| `q:a1-tail` | optimize the explicit radial tail; extend beyond log-Hessian Lipschitz | medium |
| `q:a1-sharp` | verify random-design leverage hypotheses; handle Poisson/high leverage | medium |
| `q:a1-lsi` | localized/restricted LSI/transport; classify stronger-tail global cases | harder |
| `q:a1-sampling` | translate to Langevin/MALA complexity | applied |

## Numerical plan (finum)

1. Deterministically compute `Ĥ`, row leverages `αᵢ`, `η`, the radial tail ratio, and (when
   `η<1` and bounded Hessian) `K_d(η)λmax(Ĥ⁻¹)`.
2. Optimize `R` in the explicit but unproved split candidate before sampling; never report that
   expression as a certificate. Report failure rather than a number when `η≥1` for the direct
   radial factor.
3. Build `GLMPosterior(X, y, Σ₀, link)`; sample only with an `R̂`/ESS gate. Record
   `λmax(empirical Cov)` as a directional scale estimate. Even with explicit sampling and mixing
   error control, use it as a refutation aid rather than a verdict; compare it separately with the
   proved direct radial bound and the unproved split candidate.
4. In one dimension, use a converged Sturm--Liouville/FEM solve as a calibrated approximation;
   call it two-sided only after supplying truncation and discretization error bounds.
5. Sweep instances from `../knowledge/instances.md`: `cal-glm-linear` (must be tight),
   `stress-logit-separable` (the tail-free inverse-mode-Hessian proposal fails analytically),
   `stress-wide` (`D>n`),
   `stress-logit-bulk` (must beat baseline substantially).
6. Refinement readout: best `R`, `η`, radial tail loss, and the sharpness ratio of the certified
   upper bound to `λmax(Cov_π)`.

**Research use only:** run the full A1 stress tier, not just favorable cases, to diagnose the
comparison factor, tail correction, tightness, and possible improvement over baseline on
bulk-dominated instances. These numerical results are directional research diagnostics and may expose
candidate counterexamples; they never validate or certify the bound or any proof. Rigorous
refutation still requires an analytic argument or exact lower bound.

## Numerical research log

_(none yet — the 2026-08-21 contribution is analytic. Focused deterministic regression tests check
the radial formulas and weight floors but are not evidence. The retired tail-free diagnostic and
its missing wide-instance verdict are preserved only in the
[`2026-08-21 A1 audit`](../explorations/2026-08-21-a1-bulk-tail-audit.md).)_

## Cross-links

- `conj:a2` is the `n→∞` shadow — a bulk-tight A1 bound must reproduce `λmax(I⁻¹)` (`q:a1-sharp`).
- `q:a4-certificate` is the `W₂` analogue at the same bulk scale.
- A3 and the A5 funnel have analogous tail/coordinate failures, governed by
  `obs:heavy-tail-no-classical`; they are not instances of A1's saturating-link obstruction.
