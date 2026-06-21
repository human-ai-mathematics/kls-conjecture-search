# Shared stress battery — the curated test instances

The instances an agent's refined statement **must** be tested against before it can claim
`evidence: numerical-strong`. These are *project assets*, curated and shared — NOT chosen
per-target by the refining agent (that would let a soft statement be "validated" against a soft
battery). `finum` owns these as fixed, seeded, provenance-stamped generators. Math in LaTeX (`$…$`).

Two tiers: **calibration** (exact ground truth — the pipeline must reproduce these or it emits
no verdict) and **stress** (the adversarial cases each obstruction names).

---

## Calibration tier — exact ground truth

| id | instance | exact answer | checks |
|----|----------|--------------|--------|
| `cal-gauss` | $N(0,\Sigma)$, anisotropic $\Sigma$ | $C_P = C_{\mathrm{LS}} = \lambda_{\max}(\Sigma)$ | linear test $= \lambda_{\max}(\Sigma)$; a claim $C_P \le 0.9\,\lambda_{\max}(\Sigma)$ must be FALSIFIED |
| `cal-glm-linear` | Gaussian-linear GLM ($W \equiv I$) | Gaussian posterior, $\mathrm{Cov} = (\Sigma_0^{-1}+X^\top X)^{-1}$ | A1 bound $\lambda_{\max}((\Sigma_0^{-1}+X^\top X)^{-1})$ is exact $\Rightarrow$ tightness $\approx 1$ |
| `cal-1d-eigen` | 1D/2D posteriors | $C_P$ from finite-difference eigensolve of $-L$ | two-sided ground truth for falsification calibration |
| `cal-cauchy` | generalized Cauchy $\mu_\beta$ | closed-form weighted gap $\lambda_{\beta,d}$ (`thm:a3-student`) | numerical weighted gap matches |

---

## Stress tier — one per obstruction

### A1 / `obs:flat-direction`
- `stress-logit-separable` — near-separable logistic (vary separation margin). The bulk term
  stays small while $\lambda_{\max}(\mathrm{Cov})$ inflates $\Rightarrow$ a tail-free bound is
  FALSIFIED; a correct A1 bound degrades gracefully with the separation geometry and $\lambda_{\max}(\Sigma_0)$.
- `stress-anisotropic-prior` — strongly anisotropic $\Sigma_0$ (matrix bound vs scalar floor).
- `stress-wide` — $D > n$, rank-deficient $X^\top \bar W X$ (bound must revert to prior scale on
  data-blind directions, improve on data-informed ones).
- `stress-logit-bulk` — well-identified, bulk-dominated logistic/Poisson (where the sharpening
  *should* beat $\lambda_{\max}(\Sigma_0)$ by a lot; the case that makes loose-but-true bounds score badly).

### A2 / `obs:tv-insufficient`
- `stress-contamination` — $(1-\varepsilon_n)N(0,1)+\varepsilon_n N(a_n,1)$, $\varepsilon_n a_n^2 \to \infty$.
  A "BvM $\Rightarrow$ constants" claim must be FALSIFIED here.
- `stress-bvm-sweep` — regular logistic/Poisson, $n$-sweep, fixed $d$, repeated over data draws
  (limit is in $\mathbb P_{\theta_0}$-probability).
- `stress-non-fisher-local` — model with a shallow remote near-minimizer, so
  $n\,C_{\mathrm{LS}} \to 1/\mu_{\mathrm{PL}} \neq \lambda_{\max}(I^{-1})$ (exercises `q:a2-lsi`).

### A3 / `obs:heavy-tail-no-classical`
- `stress-student` — Student-$t_\nu$ over $\nu$ (tail index); classical $C_P=\infty$, weighted
  finite, matches $\lambda_{\beta,d}$.
- `stress-horseshoe` — horseshoe marginal (log pole at 0, Cauchy tail); locate $C_{\mathrm{HS}}(\tau)$
  in the factor-4 Hardy bracket.

### A4 / `obs:restricted-not-finite`
- `stress-ep-tails` — $\pi \propto e^{-|x|^p}$, $1 \le p < 2$, Gaussian location family:
  $C_{\mathcal Q}=\infty$ (a global $C_{\mathcal Q}$ claim must be FALSIFIED); $C_{\mathcal Q,r}$
  on a KL sublevel must be finite.
- `stress-sep-mixture` — separated mixture: reweighting witness ($C_{\mathrm{TCI}} \asymp e^{c\Delta^2}$)
  vs mode-collapse witness ($C_{\mathcal Q} \asymp \Delta^2$).

### A5 / `obs:symmetry-vs-physical`
- `stress-folded-well` — $\tfrac12 N(-a,\sigma^2)+\tfrac12 N(a,\sigma^2)$: raw $C_P \gtrsim e^{a^2/2\sigma^2}$,
  folded $O(\sigma^2)$.
- `stress-neal-funnel` — Neal's funnel, centered ($C_P=\infty$) vs non-centered ($\max\{s^2,1\}$);
  half-Cauchy $p(\tau)$ (defeats Poincaré even non-centered) vs $\log\tau$ + Gaussian tails.

---

### Provenance
Every instance carries a seed, git hash, and library versions (as `finum.provenance` does).
A reward verdict is read only after the convergence + independent-estimator gates pass; a verdict
computed with a red gate is discarded, not scored.
