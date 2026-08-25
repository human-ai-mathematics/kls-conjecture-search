# Shared adversarial research suite — curated test instances

These project assets keep numerical exploration comparable and reduce selection bias. They are
curated and shared rather than chosen ad hoc by the agent refining a statement: an agent must not
mint favorable cases and present them as validation. Running the suite is not a soundness gate,
and no outcome validates a theorem or proof. When a registered instance has a numerical backend,
`finum` owns its fixed, seeded, provenance-stamped generator. Registration alone does not assert
that a backend exists. Math in LaTeX (`$…$`).

Two tiers: **calibration** (exact ground truth used to catch implementation errors) and **stress**
(the adversarial cases named by each obstruction). Passing either tier only licenses further
exploration; every numerical conclusion remains directional.

---

## Calibration tier — exact ground truth

| id | instance | exact answer | checks |
|----|----------|--------------|--------|
| `cal-gauss` | $N(0,\Sigma)$, anisotropic $\Sigma$ | $C_P = C_{\mathrm{LS}} = \lambda_{\max}(\Sigma)$ | linear test $= \lambda_{\max}(\Sigma)$; the implementation must reject the inconsistent candidate $C_P \le 0.9\,\lambda_{\max}(\Sigma)$, while a formal refutation uses the exact Gaussian argument |
| `cal-glm-linear` | Gaussian-linear GLM ($W \equiv I$) | Gaussian posterior, $\mathrm{Cov} = (\Sigma_0^{-1}+X^\top X)^{-1}$ | A1 bound $\lambda_{\max}((\Sigma_0^{-1}+X^\top X)^{-1})$ is exact $\Rightarrow$ tightness $\approx 1$ |
| `cal-1d-eigen` | 1D Gaussian | exact $C_P=\sigma^2$ | calibrated finite-domain FEM must approximate $\sigma^2$; truncation/discretization studies improve this directional check but do not make it a proof validator |
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
  candidate upper bound when its right-hand side falls below the observed covariance scale; raw
  sampled covariance is directional only. A formal refutation requires a separately checked
  exact or rigorously controlled lower bound. The diagnostic does not refute all tail-free
  data-informed formulas. Any proposed A1 bound should also be checked analytically on the
  one-observation logistic family and revert gracefully toward the prior scale.
- `stress-anisotropic-prior` — strongly anisotropic $\Sigma_0$ (matrix bound vs scalar floor).
- `stress-wide` — $D > n$, rank-deficient $X^\top \bar W X$ (bound must revert to prior scale on
  data-blind directions, improve on data-informed ones).
- `stress-logit-bulk` — well-identified, bulk-dominated logistic/Poisson (where the sharpening
  *should* beat $\lambda_{\max}(\Sigma_0)$ by a lot; the case that makes loose-but-true bounds score badly).

### A2 / `obs:tv-insufficient`
- `stress-contamination` — $(1-\varepsilon_n)N(0,1)+\varepsilon_n N(a_n,1)$, $\varepsilon_n a_n^2 \to \infty$.
  The suite illustrates why a "BvM $\Rightarrow$ constants" claim fails; the formal refutation
  comes from the exact contamination calculation, not the numerical run.
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
  bottleneck tends to zero. The diagnostic targets marginal-only joint constants; any formal
  refutation must use a separately checked analytic obstruction.

### A4 / `obs:restricted-not-finite`
- `stress-ep-tails` — $\pi \propto e^{-|x|^p}$, $1 \le p < 2$, Gaussian location family:
  $C_{\mathcal Q}=\infty$ analytically; numerical runs only illustrate the failure of a finite
  global candidate. $C_{\mathcal Q,r}$ on a KL sublevel is finite only because this parameter
  family is coercive. An unrestricted tail-reweighting entropy ball remains infinite.
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

## KLS / deterministic moment-map CMH route — registered research suite

These are the fixed consistency and adversarial instances for
`research/kls/routes/moment-map-cmh/`. Registration freezes the models for comparable research;
it does **not** validate the route or claim that a `finum` backend exists. Exact algebra belongs
in a persisted, independently checked dossier. Any sampled, FEM, or grid calculation must first
be implemented in `finum` with the repository gates and remains directional.

| id | instance | research role | current status |
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

### Normalization-layer suite (implemented by `finum run --target cmh-gate-zero`)

Added 2026-08-25. Unlike the construction-layer rows above, these have a built backend that can
produce a future provenance-stamped research artifact. The only stored run predates the hardened
source, its recorded commit does not contain the target, and it remains unlinked calibration
history. The backend uses **no Monte Carlo**, but this is a repeatability fact, not a rigor
certificate.
Closed-form rational $R_1$ values and exact rational Rayleigh witnesses can suggest inputs to a
separately checked analytic refutation; the run itself does not certify one. Floating generalized
eigenvalues, quadrature cross-checks, FEM, and the present Galerkin computation remain
directional.

| id | instance | research role | current status |
|---|---|---|---|
| `cal-cmh-gauss-1d` | $N(0,1)$, $\tau\equiv1$ | gate-zero ratio must be exactly $1$ | exact; run calibration anchor |
| `cal-cmh-uniform-simplex` | $\mathrm{Dir}(1,\dots,1)$ on $\Delta_{m-1}$ | gate-zero ratio must be exactly $2(m+1)/(m+3)$, and $1.2$ at $m=2$ agreeing with the uniform interval | exact formula; a future reproducible run must recover it as a calibration check |
| `stress-cmh-1d-closed-form` | centered exponential, uniform, Laplace, $\Gamma(a)$, $\mathrm{Beta}(1,b)$ with closed-form $\tau$ | exercise $R_1=\mathbb E\tau^2/\sigma^4$ and `thm:cmh-1d` across the one-dimensional log-concave range | exact $R_1$ (max $2$); the companion $C_P$ is FEM, hence **directional only** |
| `stress-cmh-dirichlet-asymmetric` | $\alpha=(1,1,10),(1,1,100),(1,1,1000),(1,5,25),(1,2,3,4,5),(1,1,1,1,50)$ | test whether a nonproduct family can drive the gate-zero ratio toward $4$ | exact moment matrices; the hardened backend emits an exact rational Rayleigh lower-bound witness on future runs — **calibration, not support** (all inside `thm:cmh-dirichlet`) |
| `stress-cmh-dirichlet-galerkin` | polynomial test functions to degree $4$--$6$ on the above | regression-test the surplus of `cor:cmh-dirichlet-surplus` | exact scalar moments feed floating coefficients, matrices, whitening, and eigensolve; the result remains **directional only** |
| `fence-cmh-algebraic-countermodel` | the $O(m)$-invariant random PSD law of `prop:letwin-not-gate-zero`, $m\ge18$ | verify the three sector coefficients and the perfect-square scalar deficit | exact three-sector algebra, $z$ never sampled; $1+d=4.0426$ at $m=18$ |

**Scope rule for this suite.** Every instance except the countermodel lies **inside** a class
already proved (`thm:cmh-1d`, `thm:cmh-product`, `thm:cmh-dirichlet`). Such an instance can detect
an implementation error; it cannot be cited as support for universal $\mathrm{CMH}(4)$ or for
`conj:gate-zero`. Useful new stress diagnostics require moment maps outside those classes — task
M10 — and those need a numerically solved Monge--Ampère equation, hence remain directional.
The countermodel is a **fence**, not a counterexample to `conj:gate-zero`: it imposes no
Monge--Ampère or Codazzi compatibility, so citing it against that node is a category error.

---

### Provenance
Every future CMH run carries a seed, git hash, library versions, and the effective instance lists,
Dirichlet parameters, dimension ranges, Galerkin degrees, FEM grids, quadrature settings,
rational-witness denominator cap, and numerical tolerances (as `finum.provenance` does).
A numerical summary is interpreted only after the convergence and independent-estimator gates
pass; an output with a red gate is discarded. A green gate establishes software consistency, not
mathematical validity.
