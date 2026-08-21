# KLS route-gating — node → computable quantity → verdict

Implementation status of the numerical channel for KLS. Three regimes:

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

All numerics **refute or give direction; they never prove** (see `shared/target.md`).

## SDE-free signals (finum kls, built)

| fact / node | computable quantity | REFUTES / SUPPORTS |
|---|---|---|
| isotropic linear-test refuter (`shared/lower-bounds.md`) | `lambda_max(Cov) = 1` for isotropic mu (`finum.constants.poincare_lower`) | any claimed KLS upper bound `C_P < 1` is **REFUTED** |
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

The paired-grid gate is empirical convergence evidence, not a crossing theorem: exits and
re-entries between fine grid nodes are not detected. The final 2026-08-20 run used 16 discovery
and 16 held-out paths, so its uncertainty is also too large for a universal trend claim. The
artifact [`2026-08-20-kls-align-high-n-final.jsonl`](../runs/2026-08-20-kls-align-high-n-final.jsonl)
is dirty, `evidence_eligible: false`, and records `no-proof/no-route-verdict`. It therefore does
not change the ledger status of `q:alignment`.
