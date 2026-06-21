# KLS route-gating — node → computable quantity → verdict

How numerics gate the KLS routes. Two regimes:

- **SDE-free (built, sound).** The route-agnostic, Poincaré/bridge-level facts in
  [`shared/lower-bounds.md`](shared/lower-bounds.md), computable from `finum` without the
  localization SDE. Artifact: `research/runs/<date>-kls.jsonl` (via `finum run --target kls`).
- **Localization (built).** The per-route stochastic-localization quantities (the
  occupation budget Ξ_T, alignment, weighted Stein). These need the SDE engine, now in
  `finum.localization` (`experiments/finum/localization/`)
  and driven by the `kls-loc` target (`finum run --target kls-loc`). The functions are named below.

All numerics **refute or give direction; they never prove** (see `shared/target.md`).

## SDE-free signals (finum kls, built)

| fact / node | computable quantity | REFUTES / SUPPORTS |
|---|---|---|
| isotropic linear-test refuter (`shared/lower-bounds.md`) | `lambda_max(Cov) = 1` for isotropic mu (`finum.constants.poincare_lower`) | any claimed KLS upper bound `C_P < 1` is **REFUTED** |
| the bridge `C_P <= K lambda_max(Cov)` (`ab/conj:a1-bis`) | realized `K = C_P / lambda_max(Cov)` across isotropic log-concave geometries (Gaussian, Laplace, uniform) | `K = O(1)` across all geometries **SUPPORTS** the bridge; a geometry with `K` growing in dimension would be directional evidence against |
| `obs:rank-one-refuted` / `cor:refutation` | realized `K` under single-coordinate variance inflation `Lambda -> inf` | `K` stays `= 1` ⇒ rank-one **cannot** refute the K-bound (the counterexample is dead at the Poincaré level) |

`finum.kls` computes each factor's `C_P` by the calibrated 1D FEM gap and combines by
tensorization (`C_P = max_i C_P_i`, `lambda_max = max_i Var_i`). The realized-`K` table in the
artifact is the concrete Part I/II ↔ Part III bridge signal.

## Localization signals (BUILT — finum.localization, target `kls-loc`)

Functions below are `finum.localization.*` (import `from finum.localization import ...`).

| open node | quantity | finum.localization function | REFUTES / SUPPORTS |
|---|---|---|---|
| `q:upgrade` (P1, operator→trace) | source occupation `Xi_S(T) = ∫ S dt` over balanced cuts, across an n-sweep | `observables.integrate_path(...).xi_S`, `ensemble_mean` | `Xi_S` flat in n & negligible past `t_1(n)` SUPPORTS; growth with n REFUTES Route A |
| `q:alignment` (P6) | per-coordinate budgets simultaneously spent on a fixed cut | `integrate_path(direction=i)`, `observables.R0_diag` | budgets summing to ~k simultaneously REFUTES; self-extinguishing spikes SUPPORT |
| `q:weighted` (P2) / `q:stein-weighted` (P3) | weighted excess / Stein source vs damping at high anisotropy | `ProductState.{excess_op_norm,lambda_max}`, `observables.observe` | weighted source dominated by damping SUPPORTS; absolute-scale (slice-wise) control REFUTED by `obs:two-tail` |
| `q:taming` (P4) | relative-scale `Xi_T` for a near-worst (thin-shell) family | `integrate_path` on `cuts.energy_shell` across n (wired in `targets/kls_localization.py`) | sublinear-in-T growth SUPPORTS; linear growth REFUTES |
| `q:splitting` (P5) | boundary Obata / constant-mode curvature | — (boundary differential geometry; no localization path yet) | deferred |

**Gate discipline (both regimes).** A verdict is read only after the gates pass — calibration
reproduces ground truth (the Gaussian model `A_t=(1+t)^{-1}I`) and the `n_bins_convergence`
+ `fft_vs_mc` cross-checks pass (`finum.localization.gates`). A verdict behind a red gate is
discarded (`no-verdict`), not scored.
