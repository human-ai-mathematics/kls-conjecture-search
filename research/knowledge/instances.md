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
| `cal-1d-eigen` | 1D Gaussian | exact $C_P=\sigma^2$ | calibrated finite-domain FEM must approximate $\sigma^2$; it is not a certified two-sided solver without truncation/discretization error bounds |
| `cal-cauchy` | generalized Cauchy $\mu_\beta$ | closed-form weighted gap $\lambda_{\beta,d}$ (`thm:a3-student`) | numerical weighted gap matches |
| `cal-logit-global` | any finite Gaussian-prior binary-logistic posterior | $C_{\mathrm{LS}}=C_{\mathrm{TCI}}=\lambda_{\max}(\Sigma_0)$ | global entropy/transport estimates may not claim a smaller Fisher-scale value |
| `cal-mode-leverage` | finite logistic GLM with mode Hessian $\widehat H$ | radial $g_-\le U-U(\hat\theta)\le g_+$; $K_d(0)=1$ and $K_d(\eta)\to1$ | rowwise curvature floors hold throughout the mode ellipsoid; $\eta\ge1$ triggers the explicit failure gate |
| `cal-horseshoe-scale` | exact horseshoe marginal $h_\tau\propto\tau^{-1}e^aE_1(a)$, weight $\tau^2+x^2$ | $C_{\mathrm{HS}}(\tau)=4$ for every $\tau$ (`prop:a3-horseshoe`) | standardized grids reproduce scale covariance and the positive E1/Barta residual; finite-domain FEM is directional only |
| `cal-vi-gaussian-local` | $\pi=N(\mu,\Sigma)$, $\mathcal Q_S=\{N(\mu+m,S)\}$ | exact raw misspecified, localized-mean, and optimizer-centred excess constants | excess constants equal $\lambda_{\max}(\Sigma)$; raw constant retains $D_S/(2\delta_S)$ |
| `cal-gaussian-hierarchy` | unit Gaussian hierarchy, normalized data precision $r$ | centered/non-centered $C_P$ and $\kappa_P$ cross exactly at $r=1$ | any reparameterization diagnostic must reproduce the phase diagram |
| `cal-partial-noncentering` | scalar Gaussian hierarchy with variances $A,B$ and data precision $r$ | $\alpha_*=1/(1+rB)$ minimizes both $C_P$ and $\kappa_P$ | grid optimization must recover $\alpha_*$ and the determinant must remain invariant |
| `cal-orbit-connectivity` | finite symmetric matrix of pair communication heights | $\Gamma_{\rm conn}=\max_A\min_{i\in A,j\notin A}H_{ij}$ | distinguish the easiest pair from the threshold at which the full orbit graph connects |

---

## Stress tier — one per obstruction

### A1 / `obs:flat-direction`
- `stress-logit-separable` — near-separable logistic (vary separation margin). The bulk term
  can stay below the covariance lower bound. This falsifies a *specified* local/mode-curvature
  upper bound when its right-hand side is smaller than an exactly evaluated or rigorously
  controlled $\lambda_{\max}(\mathrm{Cov})$; raw sampled covariance is directional only. It does
  not falsify all tail-free data-informed formulas. A correct A1 certificate must survive the
  analytic one-observation logistic family and revert gracefully toward the prior scale.
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
- `stress-non-fisher-local` — deterministic low-temperature potentials satisfying the published
  global PL/growth hypotheses, with a shallow remote near-minimizer. This calibrates the
  $1/\mu_{\mathrm{PL}}$ alternative; transferring it to random posterior potentials is itself part
  of `q:a2-lsi`.

### A3 / `obs:heavy-tail-no-classical`
- `stress-student` — Student-$t_\nu$ over $\nu$ (tail index); classical $C_P=\infty$, weighted
  finite, matches $\lambda_{\beta,d}$.
- `stress-horseshoe` — the **exact** exponential-integral horseshoe marginal (not the historical
  logarithmic proxy); test scale covariance and the proved value $C_{\mathrm{HS}}=4$ in
  intrinsic `asinh` coordinates. Numerics guard the implementation of the closed residual; proof
  status comes from the standalone independently reviewed argument.
- `stress-fixed-marginal-copula` — hold every heavy-tailed marginal fixed while the copula
  bottleneck tends to zero. Any marginal-only joint constant must be FALSIFIED.

### A4 / `obs:restricted-not-finite`
- `stress-ep-tails` — $\pi \propto e^{-|x|^p}$, $1 \le p < 2$, Gaussian location family:
  $C_{\mathcal Q}=\infty$ (a global $C_{\mathcal Q}$ claim must be FALSIFIED); $C_{\mathcal Q,r}$
  on a KL sublevel is finite only because this parameter family is coercive. An unrestricted
  tail-reweighting entropy ball remains infinite.
- `stress-sep-mixture` — the Gaussian mixture with centers $\pm a$ (separation $2a$): compare an
  actual component-reweighting lower witness with a mode-collapse lower witness. These are
  directional growth diagnostics, not two-sided estimates of $C_{\mathrm{TCI}}$ or
  $C_{\mathcal Q}$; require $a/\sigma$, reweighting, and resolution sweeps.

### A5 / `obs:symmetry-vs-physical`
- `stress-folded-well` — $\tfrac12 N(-a,\sigma^2)+\tfrac12 N(a,\sigma^2)$:
  $\log(C_P/\sigma^2)=a^2/(2\sigma^2)+O(\log(a/\sigma))$ as $a/\sigma\to\infty$; folding gives
  $C_P\le\sigma^2$ and the folded constant tends to $\sigma^2$.

### A5 / `obs:heavy-tail-no-classical`
- `stress-neal-funnel` — Neal's funnel, centered ($C_P=\infty$) vs non-centered ($\max\{s^2,1\}$);
  half-Cauchy $p(\tau)$ (defeats Poincaré even non-centered) vs $\log\tau$ + Gaussian tails.
  Finite variance witnesses do not numerically establish infinity; that conclusion is analytic.
  The prior-only partial coordinates remain infinite for every $\alpha<1$, so tests must not
  invent a smooth global partial-noncentring crossover without a likelihood tail calculation.

---

## KLS / deterministic moment-map CMH route — registered battery

These instances are the fixed battery for `research/kls/routes/moment-map-cmh/`. Registration
freezes the models; it does **not** claim that a `finum` backend or an eligible R1 artifact exists.
Exact algebra belongs in a persisted dossier. Any sampled, FEM, or grid calculation must first be
implemented in `finum` with the repository gates.

| id | instance | required role | present evidence status |
|---|---|---|---|
| `cal-kls-gauss-moment-map` | isotropic Gaussian, $\phi(y)=|y|^2/2$ and $H=I$ | calibrate adjoints, square roots, Haar normalization, and zero commutators | exact calibration |
| `cal-kls-centered-exp` | product of centered standard **one-sided** exponentials $Y_i-1$ | reproduce $C_P=4$ and equality in $\operatorname{Var}(|X|^2)\le8n$; keep distinct from the two-sided Laplace product used by P6 | exact one-dimensional/product facts |
| `stress-cmh-aligned-product` | product moment maps with coordinate-aligned multipliers | test tensorization and the commuting reduction | analytic calibration; does not activate eigenframe rotation |
| `stress-cmh-rotated-exp` | an orthogonal rotation of a centered one-sided-exponential product | detect illegal nodewise sibling positivity | originating exploration reports negative nodes; dossier pending |
| `stress-cmh-laguerre` | Gamma/Laguerre near-extremizing modes | detect fixed fractional spending of descendant or leaf slack | originating exploration reports near-exhaustion; dossier pending |
| `stress-cmh-high-frequency-exp` | localized high-frequency tests in the product-exponential moment map | detect separation of the conformal reservoir from traceless/corrector terms | originating exploration reports a negative leading term for the separated form; dossier pending |
| `stress-cmh-45deg-child` | $45^\circ$ projection of two exponentials with a one-dimensional child | isolate the conditional/scalar residual; scalar Stein uniqueness with boundary decay forces $S=K$ | structural calibration; cannot test Airy mismatch |
| `stress-cmh-gamma-gaussian` | rotated independent Gamma--Gaussian factors | detect the withdrawn local vector-conservation law | originating exploration reports an analytic violation; dossier pending |
| `stress-cmh-three-exp` | $\xi_1=Y_1-Y_3$, $\xi_2=Y_2-Y_3$ for independent standard exponentials | activate the canonical-versus-inherited Stein-kernel mismatch | density and inherited kernel checked algebraically; canonical $K$ reconstruction open |

The existing `kls-align` model instead uses an isotropic **two-sided Laplace** product and a fixed
tail-union cut. It belongs to the Eldan-A alignment gate and must not be used as a substitute for
the one-sided-exponential CMH models above.

---

### Provenance
Every instance carries a seed, git hash, and library versions (as `finum.provenance` does).
A reward verdict is read only after the convergence + independent-estimator gates pass; a verdict
computed with a red gate is discarded, not scored.
