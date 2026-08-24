# finum — numerical channel for the open targets

`finum` is the numerical refinement and stress-testing tool of the `research/` control plane.
Its job:

- **Refine and stress-test statements** (Part II, A1–A5; and Part III KLS sub-statements):
  produce the provenance-stamped `evidence_run` artifact a ledger node points to.
- **Prepare route diagnostics** (Part III): exercise numerical primitives for a route's central
  hypothesis before calling the route observable built. `kls-loc` remains a legacy engine
  diagnostic; `kls-align` implements the designated product tail-union observable for P6, but is
  still a one-family diagnostic rather than a verdict on the universal node.

**Soundness contract** (the general rule is in [`../CLAUDE.md`](../CLAUDE.md); this is how it
is implemented here). Uppercase **REFUTED** is reserved for a rigorous analytic or exact
lower bound that exceeds a claimed upper bound — `verdict.falsify`. Sample covariance, MCMC,
FEM, and finite-grid values go through `verdict.compare_directional`: without explicit error
bounds they cannot certify a lower bound or issue that verdict. The headline primitive
`constants.poincare_lower` estimates the analytic linear-test quantity
$\lambda_{\max}(\mathrm{Cov})\le C_P$ (`research/knowledge/lemmas.md`,
`lem:linear-test-lower`).

## Layout

```
experiments/          the uv project root (pyproject.toml, uv.lock, .venv)
  finum/              the package
    provenance.py   git/seed/version stamp + repo-path resolution; write_jsonl artifact
    constants.py    empirical Rayleigh estimates; poincare_1d_fem (1D weighted constant, FEM);
                    hardy_1d (Muckenhoupt B± criterion)
    transport.py    kl_1d, w2_sq_1d (quantile L^2), transport_ratio  (A4 W2^2/(2KL))
    sampling.py     preconditioned + adaptive MALA for posteriors without a closed-form draw
    instance.py     the shared sample-based Instance dataclass
    verdict.py      analytic falsify(), directional comparison, closed-form calibration + gates
    geometries/     the measure zoo + named test functions (ONE place to add a test measure):
                    distributions (Gaussian/DoubleWell1D/PerturbedGaussian1D), test_functions,
                    rayleigh (named-witness estimates), references (analytic upper-bound oracles)
    localization/   the Eldan stochastic-localization SDE engine (KLS diagnostic channel):
                    tilt1d, state, sde, cuts, observables, gates, tail_union, alignment
    targets/        one module per target: a1..a5 (Part II); kls (Part III SDE-free);
                    kls_localization + kls_alignment (Part III) — run_records + selftest
    run.py          dispatch run(target) -> research/runs/<timestamp>-<target>.jsonl
    selftest.py     every target's calibration reproduces its closed form, or fail loudly
  tests/            oracle suite (pytest): localization engine oracles + geometry cross-checks
```

## Run it

The repo's base interpreter has no numpy/scipy; use `uv` (it resolves them on the fly):

```bash
cd experiments                                   # the project root: pyproject.toml, uv.lock, .venv
uv run python -m finum selftest                  # target calibration + diagnostic checks
uv run python -m finum run --target A3           # writes a unique timestamped JSONL
uv run python -m finum run --target kls-loc --heavy  # enables the initial FFT/MC gate
uv run python -m finum run --target kls-align     # exact product tail-union alignment diagnostic
uv run pytest                                     # the oracle suite (engine + geometry checks)
# targets: A1 A2 A3 A4 A5 kls kls-loc kls-align
```

(With numpy/scipy already installed, plain `python -m finum ...` works too.)

`experiments/uv.lock` is the tracked dependency lock for reproducible clean checkouts.

## The targets

Each Part II target has a **calibration** tier with closed-form ground truth. If a numerical
calibration fails, sampled/FEM/grid diagnostics downstream of that calibration are skipped;
independent exact analytic records may still be emitted. The stress tier probes the target's
obstruction without turning a finite numerical battery into a proof:

| target | obstruction | calibration anchor | current result or diagnostic |
|---|---|---|---|
| A1 | `obs:flat-direction` | Gaussian / GLM-linear / 1D-FEM | proved mode-leverage formulas; the split bound remains an explicit candidate; logistic MCMC is directional |
| A2 | `obs:tv-insufficient` | Gaussian-linear $n\,C_P=1/\lambda_{\min}(\Sigma_x)$ | exact contamination variance **REFUTES** TV-only transfer; Gaussian-tail rigidity is proved; BvM sampling is directional |
| A3 | `obs:heavy-tail-no-classical` | `cal-cauchy` weighted constant $=1/\lambda_{\beta,d}$ | classical failure and the sharp horseshoe $C_{\mathrm{HS}}=4$ are proved; FEM/Hardy grids are directional checks |
| A4 | `obs:restricted-not-finite`; `obs:symmetry-vs-physical` | Gaussian $W_2^2/(2\mathrm{KL})=\sigma^2$ | analytic $C_Q=\infty$ for $p<2$ plus proved local Gaussian formulas; tail/mixture grids are directional illustrations |
| A5 | `obs:symmetry-vs-physical`; `obs:heavy-tail-no-classical` | Neal non-centered $C_P=\max\{s^2,1\}$ | centered Neal $C_P=\infty$ and partial-Gaussian formulas are proved; folded-well FEM is directional |
| kls | (Part III, SDE-free) | Gaussian $C_P=1$ (FEM) | finite-battery bridge non-refutation; Gaussian rank-one normalization sanity |
| kls-loc | (Part III, localization diagnostics) | Gaussian model $A_t=(1+t)^{-1}I$ | source occupation $\Xi_S/n$ checks the legacy engine only; **no route verdict** |
| kls-align | (Part III, product alignment diagnostic) | exact tilted-Laplace moments + filtering path | tail-union $S_t^H,r_t,D_t$ with held-out interval scans; **no proof/general-route verdict** |

The 1D weighted-Poincaré constant is approximated with a calibrated P1-FEM tridiagonal
eigensolve (`scipy.linalg.eigh_tridiagonal`); A4 transport ratios use finite-grid 1D `W_2`/`KL`.
Both remain directional unless supplied with truncation and discretization error bounds.

## Part III (KLS): three channels

`run --target kls` (SDE-free) computes the **realized $K = C_P/\lambda_{\max}(\mathrm{Cov})$** on
isotropic log-concave test geometries (the A1-bis ↔ KLS bridge). Its Gaussian rank-one case is
a tensorization/normalization sanity check, not evidence for the cut-specific dynamic obstruction.

`run --target kls-loc` exercises the Eldan stochastic-localization engine in
`finum.localization`. It currently reports source-occupation and settled-budget diagnostics, not
the open-node observables:

- P6 / `q:alignment` is not built *in this legacy target*; use `kls-align` for the product
  tail-union model described below;
- P2/P3 are **not built**: they still need weighted excess / Stein path functionals;
- P4 / `q:taming` is **not built**: its dynamic input is the cut-free $h_\mu\Xi_T$ on near-worst measures,
  which a product energy-shell experiment does not represent.

Every new `kls-loc` record is therefore explicit `no-verdict`. Missing or red Gaussian,
initial-state bin/FFT checks, or $dt\mapsto dt/2$ refinement gates prevent even a gated
diagnostic; tilted-state quadrature convergence is still unavailable, and an all-green engine
run remains diagnostic until a route observable is implemented. The
node → quantity → implementation-status map is in `research/kls/gating.md`.

`run --target kls-align` is the isolated product stress test for P6. It computes the full
incident-high source $S_t^H$ (including both copies of high--low entries), $r_t$, and $D_t$ for
$E=\{\max_i|x_i|\ge a_n\}$ in an isotropic Laplace product. Exact one-dimensional truncated
moments and the filtering path $c_t=tX+B_t$ remove the FFT and Euler-drift errors. The target
uses along-path moment checks, paired $dt$ refinement, balance/martingale checks, and selects
adverse deterministic intervals on half the paths before held-out evaluation on the other half.
Its output is refutation-seeking model evidence only: green gates and bounded sampled margins do
not prove the all-product estimate, the all-cut estimate, or KLS.

The 2026-08-20 held-out high-dimensional sweep is
`research/runs/2026-08-20-kls-align-high-n-final.jsonl`. It is a diagnostic-only artifact with no
route verdict, and should be read with its finite-path and node-only stopping limitations.

## How a run becomes evidence

**`numerical-strong` is not implemented yet.** `check_ledger.py` will only accept that rung
from a run whose provenance params carry `calibration_passed`, `shared_battery_passed: true`,
and `shared_battery: research/knowledge/instances.md`, together with a `verdict` record. Targets
emit `calibration_passed`, but no target yet walks the shared stress tier of
`research/knowledge/instances.md` and sets the battery flags, so artifacts can currently back
`numerical-directional` only. Closing this means adding a battery runner that executes the stress
instances per target and defines what a pass is — not a per-target ad-hoc check, which is exactly
the reward-hacking the shared battery exists to prevent.

A run exclusively creates a uniquely timestamped, provenance-stamped JSONL; it will not
overwrite an existing artifact. Reproducibility rests on the recorded seed, params, and library
versions. `finum` does **not** edit the ledger: an agent reads
the artifact and may attach it as directional evidence. Promotion to `proved` requires a checked
analytic proof, never survival of a finite battery. Numerics and bookkeeping stay separate, the
soundness contract intact. Any retained historical pointers to superseded
artifacts are diagnostics, not promotion evidence. A `kls-loc` diagnostic is not
eligible for ledger evidence until the corresponding route observable and its full gates exist.
A `kls-align` artifact can stress the designated product family, but cannot by itself promote the
universal `q:alignment` node.

## Notes on accuracy

Heavy-tailed weighted-constant estimates (A3 Student-t with $\nu\le2$, generalized Cauchy with
$\beta\to d/2$) are grid-truncation limited and use directional tolerances; closed-form values
remain the theorem statements, not consequences of the FEM match. A5 folded-well values are
finite-domain directional estimates. A2 contamination uses an exact analytic variance lower
bound, whereas its BvM sweep is one data set and one chain per $n$ and has no chain-convergence
gate. A1 MCMC stress cases use a two-seed agreement gate, which is only a diagnostic and supplies
neither a mixing proof nor uncertainty bounds.
