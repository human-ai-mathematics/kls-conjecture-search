# finum — numerical channel for the open targets

`finum` is the Phase-1 numerical tool of the `research/` control plane. Its job:

- **Refine and refute statements** (Part II, A1–A5; and Part III KLS sub-statements):
  produce the provenance-stamped `evidence_run` artifact a ledger node points to.
- **Gate and refute proof routes** (Part III): numerically test a route's central hypothesis
  *before* a proof is attempted, and kill routes that hit a `shared/lower-bounds.md`
  counterexample.

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
    localization/   the Eldan stochastic-localization SDE engine (KLS route channel):
                    tilt1d, state, sde, cuts, observables, gates
    targets/        one module per target: a1..a5 (Part II); kls (Part III SDE-free);
                    kls_localization (Part III localization channel)  — run_records + selftest
    run.py          dispatch run(target) -> research/runs/<date>-<target>.jsonl
    selftest.py     every target's calibration reproduces its closed form, or fail loudly
  tests/            oracle suite (pytest): localization engine oracles + geometry cross-checks
```

## Run it

The repo's base interpreter has no numpy/scipy; use `uv` (it resolves them on the fly):

```bash
cd experiments                                   # the project root: pyproject.toml, uv.lock, .venv
uv run python -m finum selftest                  # all targets' calibration + refuters
uv run python -m finum run --target A3           # writes ../research/runs/<date>-A3.jsonl
uv run pytest                                     # the oracle suite (engine + geometry checks)
# targets: A1 A2 A3 A4 A5 kls kls-loc
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
| kls | (Part III, SDE-free) | Gaussian $C_P=1$ (FEM) | realized $K=C_P/\lambda_{\max}(\mathrm{Cov})=O(1)$; rank-one $K=1$ |
| kls-loc | (Part III, localization) | Gaussian model $A_t=(1+t)^{-1}I$ | thin-shell occupation $\Xi_S/n$ flat/decreasing **SUPPORTS** taming (gated; direction only) |

The 1D weighted-Poincaré constant uses a calibrated P1-FEM tridiagonal gap eigensolve
(`scipy.linalg.eigh_tridiagonal`); A4 transport constants are grid-based 1D `W_2`/`KL`.

## Part III (KLS): two channels

`run --target kls` (SDE-free) computes the **realized $K = C_P/\lambda_{\max}(\mathrm{Cov})$** on
isotropic log-concave test geometries (the A1-bis ↔ KLS bridge) and the rank-one non-refutation.

`run --target kls-loc` (localization) runs the Eldan stochastic-localization engine in
`finum.localization` to produce the per-route DIRECTIONAL quantities ($\Xi_S$ occupation,
per-direction budget, thin-shell taming). Every number is read only behind passing gates
(Gaussian-model calibration + `n_bins_convergence`; the expensive independent `fft_vs_mc`
cross-check with `--`… `heavy=True`); a verdict behind a red gate is recorded `no-verdict`. The
node → quantity → verdict map is in `research/kls/gating.md`.

## How a run becomes evidence

A run writes a provenance-stamped JSONL. `finum` does **not** edit the ledger: an agent reads
the artifact and sets `evidence:` / `evidence_run:` on the node (and, if a refined statement
survives the shared battery, may flip it to `conjectured` with `evidence: numerical-strong`).
Numerics and bookkeeping stay separate, the soundness contract intact. The current runs are
wired onto the obstruction nodes they *demonstrate* (e.g. `obs:heavy-tail-no-classical` →
A3 artifact); no conjecture is promoted to `numerical-strong` yet.

## Notes on accuracy

Heavy-tailed weighted gaps (A3 Student-t with $\nu\le2$, generalized Cauchy with
$\beta\to d/2$) are grid-truncation limited — those use directional tolerances; the exact
calibration anchors (`cal-cauchy` at $\beta\ge1.5$, Student-t $\nu>2$) match to $<1\%$. A5
folded-well and A2 contamination are reported as ratios/trends. MCMC-based cases (A1 stress,
A2 BvM sweep) carry the two-chain convergence gate.
