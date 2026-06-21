# Notation glossary

Symbols used throughout `modules/` (Part I) and `modules/kls/` (Part II). The authoritative
definitions for Part I are in `modules/01-definitions.tex`; the LaTeX macros are in
`shared/preamble.tex`. The fixed normalization below must not be silently changed.

## Measures and potentials

| Symbol | Meaning |
|---|---|
| `P` | target probability measure on `ℝ^D`, `P(dx) ∝ e^{-U(x)} dx` |
| `U` | potential (`= -log` density up to a constant) |
| `L` | reversible generator `Δ − ∇U·∇` of the overdamped Langevin diffusion |
| `Hess U` | Hessian `∇²U`; `m`-strong convexity means `Hess U ⪰ m I_D` (`m>0`) |
| `Σ`, `Σ_0` | a covariance; `Σ_0` is the Gaussian-prior covariance in the GLM spine |
| `‖Σ‖_op`, `λmax(Σ)` | operator norm = largest eigenvalue of a symmetric PSD matrix |

## The three constants (fixed normalization)

| Symbol | Definition |
|---|---|
| `C_P` | Poincaré: `Var_P(f) ≤ C_P · E_P|∇f|²`. `C_P^{-1}` is the spectral gap of `L`. |
| `C_LS` | log-Sobolev: `Ent_P(f²) ≤ 2 C_LS · E_P|∇f|²`. |
| `C_TCI` | transportation-cost (Talagrand `T₂`): `W₂²(Q,P) ≤ 2 C_TCI · KL(Q‖P)`, all `Q ≪ P`. |

Consequences of this normalization (proved in `modules/01-definitions.tex`):
`C_P ≤ C_LS` (linearize LSI around constants) and `C_TCI ≤ C_LS` (Otto–Villani).

## Imported proof mechanisms (Part I toolkit, `modules/02`)

| Label | Mechanism | One-line content |
|---|---|---|
| `thm:bakry-emery` | Bakry–Émery | `Hess U ⪰ m I ⇒ C_P ≤ C_LS ≤ 1/m` |
| `thm:brascamp-lieb` | Brascamp–Lieb | `Var_P(f) ≤ E_P⟨(Hess U)^{-1}∇f, ∇f⟩` (varying curvature) |
| `thm:holley-stroock` | Holley–Stroock | bounded perturbation `e^{-W}`: constants `× e^{osc(W)}` |
| `thm:tensorization` | tensorization | `C_P(⊗_i μ_i) = max_i C_P(μ_i)` |
| `thm:otto-villani` | Otto–Villani | LSI `⇒` `T₂`, `C_TCI ≤ C_LS` |
| `thm:hardy-1d` | Hardy/Muckenhoupt | sharp two-sided `C_P` in 1D and 1D reductions |
| `cor:ccnw-mixture-lsi` | Chen–Chewi–Niles-Weed | bounded-`χ²` mixtures have dimension-free LSI |

## The tier curriculum (Part I)

| Section | Tier | Family |
|---|---|---|
| `sec:tier1` | 1 | Gaussian, strongly log-concave, Bayesian linear regression (exact) |
| `sec:tier2` | 2 | bounded perturbations (Holley–Stroock), products (tensorization) |
| `sec:tier3` | 3 | Gaussian-prior GLM posterior — flagship `thm:glm-fi` |
| `sec:tier4` | 4 | heavy-tailed priors; LSI/`T₂` obstruction `thm:heavy-tail-no-lsi` |
| `sec:tier5` | 5 | mixtures, label-switching, hierarchical funnels |
| `sec:agenda` | — | open research agenda; bridge to KLS |

## Part II (KLS) — key symbols

| Symbol | Meaning |
|---|---|
| `h*_n` | worst-case Cheeger constant over isotropic log-concave measures on `ℝ^n` |
| `p_t = μ_t(E)` | mass martingale of a fixed cut `E` under Eldan stochastic localization |
| `A_t` | covariance process of the localization, `dA_t = Θ_t dW_t − A_t² dt` |
| `Ξ_T` | interface functional `∫_0^T E (λmax(A_t) − 1)_+ dt` |

The KLS macros (`\hstar`, `\PsiKLS`, `\Per`, `\HS`, `\cal*`, …) live in `shared/preamble.tex`.

## Conventions

- `‖M‖_op = λmax(M)` for symmetric PSD `M`; `A ⪰ B` is the Loewner order.
- `φ`, `Φ` are the standard Gaussian density and CDF.
- Dimension is `D` (Part I, statistics convention) or `n` (Part II); `n` in Part I is the
  number of data points.
- The dimension-free Poincaré bound for *arbitrary* isotropic log-concave measures is the
  KLS conjecture — the Tier-∞ boundary of Part I, and the subject of Part II.
