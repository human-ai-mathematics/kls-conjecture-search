# finum — numerical channel for the open targets

`finum` is the Phase-1 numerical tool of the `research/` control plane. Its job:

- **Refine and refute statements** (Part II, A1–A5; and Part III KLS sub-statements):
  produce the provenance-stamped `evidence_run` artifact a ledger node points to.
- **Prepare route diagnostics** (Part III): exercise numerical primitives for a route's central
  hypothesis before calling the route observable built. `kls-loc` remains a legacy engine
  diagnostic; `kls-align` implements the designated product tail-union observable for P6, but is
  still a one-family diagnostic rather than a verdict on the universal node.

**Soundness contract.** The only sound verdict is **REFUTED** — a claimed upper bound
$C_P\le B$ is false when a *certified lower bound* exceeds it. Everything else is *direction*,
capped below any checked proof. Numerics **never** promote a node to proved. The headline
primitive is `constants.poincare_lower` — the linear-test lower bound
$C_P\ge\lambda_{\max}(\mathrm{Cov})$ (`research/knowledge/lemmas.md`, `lem:linear-test-lower`).

## Layout

```
experiments/          the uv project root (pyproject.toml, uv.lock, .venv)
  finum/              the package
    provenance.py   git/seed/version stamp + repo-path resolution; write_jsonl artifact
    constants.py    poincare_lower (sound refuter); poincare_1d_fem (1D weighted gap, FEM);
                    hardy_1d (Muckenhoupt B± criterion)
    transport.py    kl_1d, w2_sq_1d (quantile L^2), transport_ratio  (A4 W2^2/(2KL))
    sampling.py     preconditioned + adaptive MALA for posteriors without a closed-form draw
    instance.py     the shared sample-based Instance dataclass
    verdict.py      falsify() (REFUTED), matches() (closed-form calibration) + gates
    geometries/     the measure zoo + named test functions (ONE place to add a test measure):
                    distributions (Gaussian/DoubleWell1D/PerturbedGaussian1D), test_functions,
                    rayleigh (named-witness lower bound), references (refutable upper-bound oracles)
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
uv run python -m finum selftest                  # all targets' calibration + refuters
uv run python -m finum run --target A3           # writes a unique timestamped JSONL
uv run python -m finum run --target kls-loc --heavy  # enables the initial FFT/MC gate
uv run python -m finum run --target kls-align     # exact product tail-union alignment diagnostic
uv run pytest                                     # the oracle suite (engine + geometry checks)
# targets: A1 A2 A3 A4 A5 kls kls-loc kls-align
```

(With numpy/scipy already installed, plain `python -m finum ...` works too.)

## The targets

Each Part II target has a **calibration** tier (exact closed-form ground truth — if it does not
reproduce, the run emits no verdict) and a **stress** tier demonstrating that target's
obstruction:

| target | obstruction | calibration anchor | headline stress verdict |
|---|---|---|---|
| A1 | `obs:flat-direction` | Gaussian / GLM-linear / 1D-FEM | tail-free bound **REFUTED** on near-separable logistic |
| A2 | `obs:tv-insufficient` | Gaussian-linear $n\,C_P=1/\lambda_{\min}(\Sigma_x)$ | contamination **REFUTES** "BvM(TV)⇒constants" |
| A3 | `obs:heavy-tail-no-classical` | `cal-cauchy` weighted gap $=1/\lambda_{\beta,d}$ | Student-t classical gap diverges, weighted finite & matches |
| A4 | `obs:restricted-not-finite` | Gaussian $W_2^2/(2\mathrm{KL})=\sigma^2$ | $e^{-|x|^p}$ global $C_Q$ **REFUTED** ($\gg$ restricted $C_{Q,r}$) |
| A5 | `obs:symmetry-vs-physical` | Neal non-centered $C_P=\max\{s^2,1\}$ | folded-well raw $\gg$ quotient; Neal centered **REFUTED** |
| kls | (Part III, SDE-free) | Gaussian $C_P=1$ (FEM) | finite-battery bridge non-refutation; Gaussian rank-one normalization sanity |
| kls-loc | (Part III, localization diagnostics) | Gaussian model $A_t=(1+t)^{-1}I$ | source occupation $\Xi_S/n$ checks the legacy engine only; **no route verdict** |
| kls-align | (Part III, product alignment diagnostic) | exact tilted-Laplace moments + filtering path | tail-union $S_t^H,r_t,D_t$ with held-out interval scans; **no proof/general-route verdict** |

The 1D weighted-Poincaré constant uses a calibrated P1-FEM tridiagonal gap eigensolve
(`scipy.linalg.eigh_tridiagonal`); A4 transport constants are grid-based 1D `W_2`/`KL`.

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
`research/runs/2026-08-20-kls-align-high-n-final.jsonl`. It is marked dirty and
evidence-ineligible, and should be read with its finite-path and node-only stopping limitations.

## How a run becomes evidence

A run exclusively creates a uniquely timestamped, provenance-stamped JSONL; it will not
overwrite an existing artifact. Dirty runs are marked evidence-ineligible. `finum` does **not**
edit the ledger: an agent reads
the artifact and sets `evidence:` / `evidence_run:` on the node (and, if a refined statement
survives the shared battery, may flip it to `conjectured` with `evidence: numerical-strong`).
Numerics and bookkeeping stay separate, the soundness contract intact. Some nodes retain
historical pointers to the current dirty, evidence-ineligible artifacts; these are diagnostics,
not promotion evidence, and no conjecture is `numerical-strong`. A `kls-loc` diagnostic is not
eligible for ledger evidence until the corresponding route observable and its full gates exist.
A `kls-align` artifact can stress the designated product family, but cannot by itself promote the
universal `q:alignment` node.

## Notes on accuracy

Heavy-tailed weighted gaps (A3 Student-t with $\nu\le2$, generalized Cauchy with
$\beta\to d/2$) are grid-truncation limited — those use directional tolerances; the exact
calibration anchors (`cal-cauchy` at $\beta\ge1.5$, Student-t $\nu>2$) match to $<1\%$. A5
folded-well and A2 contamination are reported as ratios/trends. MCMC-based cases (A1 stress,
A2 BvM sweep) carry the two-chain convergence gate.
