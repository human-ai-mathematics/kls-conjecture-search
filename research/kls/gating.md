# KLS route-gating — node → computable quantity → research readout

Implementation status of the numerical channel for KLS. Four regimes:

- **SDE-free (built, sound).** The route-agnostic, Poincaré/bridge-level facts in
  [`shared/lower-bounds.md`](shared/lower-bounds.md), computable from `finum` without the
  localization SDE. Artifact: `research/runs/<timestamp>-kls.jsonl` (via `finum run --target kls`).
- **Localization engine diagnostics (built; route gates not built).** The generic SDE, two-color moments,
  source occupation, and numerical cross-checks live in `finum.localization`
  (`experiments/finum/localization/`) and are exercised by `finum run --target kls-loc`.
  The target does not yet compute the complete observable of P2, P3, P4, or P6 and therefore
  always emits `no-verdict`.
- **Product alignment stress test (designated family built).** `finum run --target kls-align`
  computes the complete P6 margin for the balanced tail union in an isotropic Laplace product.
  This tests one explicit cut family only; it neither implements the universal quantifier in
  `q:alignment` nor yields a route or proof verdict.
- **Deterministic moment-map/CMH battery (normalization layer built; construction layer not).**
  `finum run --target cmh-gate-zero` computes the gate-zero ratio
  $\lambda_{\max}(\Sigma^{-1/2}\mathbb E[H\Sigma^{-1}H]\Sigma^{-1/2})$ in closed form on
  one-dimensional laws and from exact moment matrices on the Dirichlet family, verifies the
  algebraic countermodel's sector identities, and regression-tests the Dirichlet surplus by
  Galerkin. There is **no Monte Carlo**, but deterministic does not mean rigorous: FEM, floating
  generalized eigenvalues, and Galerkin output are directional. Only a closed-form rational value
  or an exact rational Rayleigh witness evaluated against the exact Dirichlet matrices can supply
  a candidate analytic certificate for independent review. The construction-layer models (Haar,
  Schur--Hodge, commutator) in
  [`routes/moment-map-cmh/models.md`](routes/moment-map-cmh/models.md) remain unbuilt, so reported
  behavior for those is still only an informal research report.

All numerical output **gives research direction; it never validates, proves, or formally refutes
a node** (see `shared/target.md`). An exact witness emitted by the code can become part of an
analytic refutation only after it is persisted and independently checked in the proof workflow.

## Deterministic CMH implementation status

### Normalization layer (built, `cmh-gate-zero`)

| node / claim | computable quantity | research readout |
|---|---|---|
| `conj:gate-zero` | exact rational $R_1$ in 1D; on Dirichlet, a floating top eigenvalue plus an exact rational Rayleigh lower-bound certificate | an exact lower-bound witness $>4$ on a genuine moment map identifies a candidate refutation of `conj:gate-zero` and universal $\mathrm{CMH}(4)$ — but **not** `conj:kls`; logical status changes only after independent certificate review, and a floating eigenvalue above $4$ is directional only |
| `thm:cmh-dirichlet` | $A(A+1)d_\alpha/n_\alpha$ using exact scalar Dirichlet moments but floating polynomial coefficients, matrix assembly, whitening, and eigensolve | exceeding the surplus ceiling $4/(1+4s_A/(A(A+1)))$ is **directional only** until an exact rational test-function/Rayleigh certificate is supplied; staying under it is a regression pass, not support for universal CMH |
| `thm:cmh-1d` | $C_{\mathrm{CMH}}=C_P/\operatorname{Var}$ against closed-form Stein kernels | the FEM $C_P$ is uncertified, so this comparison is **directional only** |
| `prop:letwin-not-gate-zero` | the three $O(m)$ sector coefficients and the perfect-square scalar deficit | exact identities; a mismatch means an implementation error, since the proposition is proved |

**Calibration anchors:** the Gaussian one-dimensional ratio is exactly $1$; the uniform simplex
$\mathrm{Dir}(1,\dots,1)$ on $\Delta_{m-1}$ gives exactly $2(m+1)/(m+3)$; and at $m=2$ that equals
$1.2$, which must agree with the uniform-interval channel. The provenance header records
`calibration_passed`; consumers must discard directional comparisons when it is false. Exact
rational certificates remain separately checkable from the matrices and witnesses they persist.

**Stored-artifact status.** The existing
`research/runs/2026-08-25T070915.854321Z-cmh-gate-zero.jsonl` predates the certificate hardening,
and its recorded commit does not contain the target source. It is retained unchanged as
calibration history and is not linked from the ledger. A future provenance-stamped run from
recorded source may be linked only as a directional research diagnostic.

**Scope discipline.** Every model currently in the target lies **inside** a proved class
(`thm:cmh-1d`, `thm:cmh-product`, `thm:cmh-dirichlet`) or is the countermodel. Such a model can
detect an implementation error; it cannot validate the headline. Testing moment maps outside
those classes — task M10 — requires a numerically solved Monge--Ampère equation and therefore
remains **directional research only** regardless of outcome.

### Construction layer (not built)

The construction layer currently uses exact or symbolic calculations plus reported exploratory
witnesses. It has no sanctioned private Monte Carlo channel. Before a sampled, FEM, or finite-grid
observation can be cited as research direction, a `finum` target must implement the registered
battery with fixed parameters, calibration failures, convergence gates, and provenance-stamped
JSONL output. In particular:

- Gaussian and aligned products are calibration cases because their commutators vanish;
- a negative individual Haar node is not a verdict on the complete-tree inequality;
- the rotated exponential, Laguerre, high-frequency, and Gamma--Gaussian behaviors remain
  informal until directional artifacts are persisted or analytic dossiers are independently checked;
- the exact three-exponential density and inherited Stein kernel activate the intended mismatch,
  but reconstruction of the canonical kernel is an open analytic problem, not a numerical gate.

## SDE-free signals (finum kls, built)

| fact / node | computable quantity | research readout |
|---|---|---|
| isotropic linear-test refuter (`shared/lower-bounds.md`) | analytically, `lambda_max(Cov) = 1` for isotropic $\mu$; `finum.constants.poincare_lower` is only an empirical calibration | the exact analytic identity, not the numerical calibration, refutes any claimed KLS upper bound `C_P < 1` |
| the bridge `C_P <= K lambda_max(Cov)` (`ab/conj:a1-bis`) | realized `K = C_P / lambda_max(Cov)` across Gaussian, Laplace, and uniform products | `K = O(1)` on this finite benign battery is directional **non-refutation**, not support for the universal theorem |
| rank-one bridge sanity (no obstruction node) | realized `K` under single-coordinate Gaussian variance inflation `Lambda -> inf` | `K=1` checks tensorization/normalization only; it does not test a cut, source budget, `cor:refutation`, or `obs:rank-one-refuted` |

`finum.kls` computes each factor's `C_P` by the calibrated 1D FEM gap and combines by
tensorization (`C_P = max_i C_P_i`, `lambda_max = max_i Var_i`). The realized-`K` table in the
artifact is the concrete Part I/II ↔ Part III bridge signal.

## Localization implementation status (`finum.localization`)

Functions below are `finum.localization.*` (import `from finum.localization import ...`).

| open node | required route observable | implemented primitive | status |
|---|---|---|---|
| `q:upgrade` (P1) | all-cut, interval-wise absorptive source occupation at meaningful dimension/time scales | `observables.integrate_path(...).xi_S`, `ensemble_mean` | **primitive only** — current small product thin-shell sweep is an engine diagnostic, not a route verdict |
| `q:alignment` (P6) | $\int_I S_t^Hdt$, where $S_t^H$ counts all matrix entries incident to a coordinate with $A_t^{(i)}\ge2$, together with $\int_Ir_tdt$ and $\int_ID_tdt$ for a fixed high-complexity cut | `tail_union` + `alignment`; exact $O(n)$ formulas and held-out interval scans in `kls-align` | **designated tail-union family built and non-refuting through $n=1024$; universal all-cut statement remains open** |
| `q:weighted` (P2) | covariance-weighted isoperimetric excess along a stopped path | covariance norm and two-color moments exist | **not built** — $e_t(E)$ / the localized isoperimetric profile is unavailable |
| `q:stein-weighted` (P3) | weighted Stein source versus damping and excess, integrated on the tight window | `observables.observe` supplies $S,r,D$ for product cuts | **not built** — no weighted Stein/excess path functional or route inequality |
| `q:taming` (P4) | cut-free $h_\mu(T^{4/3}+\Xi_T(\mu))$ for a near-worst measure | `ProductState.excess_op_norm` supplies pointwise $X_t$ on products | **not built** — product energy-shell $\Xi_S/n$ is cut-specific and products are not near-worst |
| `q:splitting` (P5) | boundary Obata / constant-mode curvature | — | **deferred** — boundary differential geometry, not a localization-engine observable |

**Gate discipline.** A `kls-loc` engine diagnostic is inspectable only when the following four
engine gates ran and passed:

1. Gaussian calibration $A_t=(1+t)^{-1}I$;
2. `initial_n_bins_convergence`;
3. the independent `initial_fft_vs_mc` cross-check;
4. $dt\mapsto dt/2$ occupation refinement within Monte-Carlo uncertainty.

The two quadrature gates currently test only the initial state. Dynamic tilted-state quadrature
convergence is explicitly unavailable, so these four gates are not route-verdict eligibility.
The CLI flag `--heavy` enables the initial FFT/MC gate. The default lightweight run omits
expensive gates and therefore records them as `not-run`. A
missing or red gate produces `no-verdict`; an all-green run also remains `no-verdict` until the
relevant route observable and dynamic gates above are implemented. Historical files retain their
original schema; new artifacts use unique timestamps and exclusive creation, so reruns do not
overwrite them.

## Dedicated P6 tail-union gate (`kls-align`)

The separate target uses exact tilted-Laplace full and truncated moments and the filtering
representation $c_t=tX+B_t$. A diagnostic is inspectable only if all of the following run:

1. exact initial balance of the tail union;
2. analytic tilted moments versus independent quadrature along sampled paths;
3. the terminal mass-martingale check;
4. pathwise source/damping identities and the Brascamp--Lieb cap;
5. paired $dt\mapsto dt/2$ checks for $S^H,r,D$, every combined
   $S^H-C_1r-\alpha D$ margin, and the stopping time;
6. discovery/held-out separation for interval selection and evaluation.

The paired-grid gate is an empirical convergence diagnostic, not a crossing theorem: exits and
re-entries between fine grid nodes are not detected. The final 2026-08-20 run used 16 discovery
and 16 held-out paths, so its uncertainty is also too large for a universal trend claim. The
artifact [`2026-08-20-kls-align-high-n-final.jsonl`](../runs/2026-08-20-kls-align-high-n-final.jsonl)
records `no-proof/no-route-verdict` and is a diagnostic only. It therefore does
not change the ledger status of `q:alignment`.
