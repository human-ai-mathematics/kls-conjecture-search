# finum — numerical research channel for the open targets

`finum` is the numerical exploration and stress-testing tool of the `research/` control plane.
Its job:

- **Build intuition, guide refinement, and stress-test candidate statements** (Part II, A1–A5;
  and Part III KLS sub-statements): record how they behave on shared calibration and adversarial
  instances in a provenance-stamped run artifact.
- **Prepare route diagnostics** (Part III): exercise numerical primitives for a route's central
  hypothesis before calling the route observable built. `kls-loc` remains a legacy engine
  diagnostic; `kls-align` implements the designated product tail-union observable for P6, but
  remains a one-family research diagnostic.

**Numerical boundary.** Every sampled, MCMC, FEM, quadrature, floating eigensolver, and
finite-grid result is a directional research diagnostic. Passing calibration, convergence, or
the shared suite shows only that the implementation behaved consistently on those checks. It
does not validate a theorem, check a proof, certify a dossier, or contribute to proof status.

The code can also record an exact analytic comparison or an exact rational/interval witness.
That object is not made into proof evidence merely by appearing in a run: any formal proof or
refutation must be written into the proof workflow and checked independently. Sampled and
floating-point quantities go through `verdict.compare_directional`; `verdict.falsify` is reserved
for exact contradictions and is still only a research signal until that separate check. The
headline primitive `constants.poincare_lower` estimates the analytic linear-test quantity
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
                    kls_localization + kls_alignment (Part III); cmh_gate_zero (Part III,
                    moment-map/CMH, fully deterministic) — run_records + selftest
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
uv run python -m finum run --target cmh-gate-zero # deterministic CMH calibration/research suite
uv run pytest                                     # the oracle suite (engine + geometry checks)
# targets: A1 A2 A3 A4 A5 kls kls-loc kls-align cmh-gate-zero
```

(With numpy/scipy already installed, plain `python -m finum ...` works too.)

`experiments/uv.lock` is the tracked dependency lock for reproducible clean checkouts.

## The targets

Each Part II target has a **calibration** tier with closed-form ground truth. If a numerical
calibration fails, sampled/FEM/grid diagnostics downstream of that calibration are skipped;
independent exact analytic records may still be emitted. Passing calibration is a software
sanity check only. The stress tier probes the target's obstruction to guide research:

| target | obstruction | calibration anchor | current result or diagnostic |
|---|---|---|---|
| A1 | `obs:flat-direction` | Gaussian / GLM-linear / 1D-FEM | proved mode-leverage formulas; the split bound remains an explicit candidate; logistic MCMC is directional |
| A2 | `obs:tv-insufficient` | Gaussian-linear $n\,C_P=1/\lambda_{\min}(\Sigma_x)$ | the exact analytic contamination calculation refutes TV-only transfer; Gaussian-tail rigidity is proved; BvM sampling is directional |
| A3 | `obs:heavy-tail-no-classical` | `cal-cauchy` weighted constant $=1/\lambda_{\beta,d}$ | classical failure and the sharp horseshoe $C_{\mathrm{HS}}=4$ are proved; FEM/Hardy grids are directional checks |
| A4 | `obs:restricted-not-finite`; `obs:symmetry-vs-physical` | Gaussian $W_2^2/(2\mathrm{KL})=\sigma^2$ | analytic $C_Q=\infty$ for $p<2$ plus proved local Gaussian formulas; tail/mixture grids are directional illustrations |
| A5 | `obs:symmetry-vs-physical`; `obs:heavy-tail-no-classical` | Neal non-centered $C_P=\max\{s^2,1\}$ | centered Neal $C_P=\infty$ and partial-Gaussian formulas are proved; folded-well FEM is directional |
| kls | (Part III, SDE-free) | Gaussian $C_P=1$ (FEM) | finite-suite bridge diagnostic; Gaussian rank-one normalization sanity |
| kls-loc | (Part III, localization diagnostics) | Gaussian model $A_t=(1+t)^{-1}I$ | source occupation $\Xi_S/n$ checks the legacy engine only; **no route verdict** |
| kls-align | (Part III, product alignment diagnostic) | exact tilted-Laplace moments + filtering path | tail-union $S_t^H,r_t,D_t$ with held-out interval scans; **no proof/general-route verdict** |
| cmh-gate-zero | (Part III, moment-map/CMH) | Gaussian $R_1=1$; $\mathrm{G0ratio}(\mathrm{Dir}(1,\dots,1))=2(m+1)/(m+3)$ | exact analytic calibrations and rational moment matrices, an exact algebraic countermodel, directional floating eigenvalue/Galerkin diagnostics, and exact rational witnesses where emitted; **necessary condition only** |

The 1D weighted-Poincaré constant is approximated with a calibrated P1-FEM tridiagonal
eigensolve (`scipy.linalg.eigh_tridiagonal`); A4 transport ratios use finite-grid 1D `W_2`/`KL`.
Both remain directional. Truncation and discretization studies improve the diagnostic but do not
turn it into proof validation.

## Part III (KLS): four channels

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
run remains diagnostic until a route observable is implemented. This Part III section is the
canonical node → quantity → implementation-status map.

`run --target kls-align` is the isolated product stress test for P6. It computes the full
incident-high source $S_t^H$ (including both copies of high--low entries), $r_t$, and $D_t$ for
$E=\{\max_i|x_i|\ge a_n\}$ in an isotropic Laplace product. Exact one-dimensional truncated
moments and the filtering path $c_t=tX+B_t$ remove the FFT and Euler-drift errors. The target
uses along-path moment checks, paired $dt$ refinement, balance/martingale checks, and selects
adverse deterministic intervals on half the paths before held-out evaluation on the other half.
Its output is a refutation-seeking research diagnostic only: green gates and bounded sampled
margins do not validate the all-product estimate, the all-cut estimate, or KLS.

The 2026-08-20 held-out high-dimensional sweep is
`research/runs/2026-08-20-kls-align-high-n-final.jsonl`. It is a diagnostic-only artifact with no
route verdict, and should be read with its finite-path and node-only stopping limitations.

## Part III (CMH): the deterministic gate-zero research suite

`run --target cmh-gate-zero` implements the *necessary* linear-test consequence of the
moment-map/CMH conjecture $C_{\mathrm{CMH}}(\mu)\le4$. With $H$ Fathi's positive symmetric Stein
kernel ($\mathbb E_\mu H=\Sigma$), testing $g(p)=a\cdot p$ gives

$$(\mathrm{G0})\qquad \mathbb E[H\Sigma^{-1}H]\le 4\Sigma,\qquad
\mathrm{G0ratio}(\mu)=\lambda_{\max}\!\big(\Sigma^{-1/2}\mathbb E[H\Sigma^{-1}H]\Sigma^{-1/2}\big)\le4 .$$

**There is no Monte Carlo anywhere in this target.** Four channels:

1. **1D closed forms.** $\tau$ is derived from $(\tau\rho)'=-x\rho$ in closed form and verified
   against that ODE by adaptive quadrature; $R_1=\mathbb E[\tau^2]/\sigma^4$ is exact (Gaussian 1,
   centered exponential 2, uniform 6/5, Laplace 5/4, Gamma$(a)$ $1+1/a$, Beta$(1,b)$ rational).
   The companion $C_{\mathrm{CMH}}=C_P/\mathrm{Var}$ uses `poincare_1d_fem` and is **directional**.
2. **Dirichlet family** (analytically solvable, non-product): $H=C(p)/A$, $C(p)=\mathrm{diag}(p)-pp^{\!\top}$;
   $\mathbb E[H\Sigma^\dagger H]$ is a degree-4 Dirichlet moment assembled in `fractions.Fraction`,
   while the optimizing generalized eigenvalue is floating point and therefore directional. An
   emitted rational Rayleigh witness is a candidate exact lower bound for independent analytic
   checking. Anchor:
   $\mathrm{G0ratio}(\mathrm{Dir}(1,\dots,1))=2(m+1)/(m+3)$, and $m=2$ must equal the uniform
   interval's $6/5$.
3. **Algebraic countermodel regression.** An exact $O(m)$-sector computation showing that Letwin's
   constant-matrix estimate $\mathbb E\,\mathrm{Tr}(BHBH)\le2\,\mathrm{Tr}(B^2)$ does **not** imply
   gate zero by matrix algebra alone: the same $H$ has $e_1^{\!\top}\mathbb E[H^2]e_1=1+d>4$ for
   $m\ge18$. That $H$ is a random PSD matrix with $\mathbb E H=I$; it is *not* claimed to be a
   moment-map Hessian.
4. **Dirichlet CMH Galerkin regression.** Polynomial test functions on the simplex use exact
   scalar Dirichlet moments, but coefficient expansion, matrix assembly, whitening, and the
   generalized eigensolve are floating point. The entire Galerkin channel is therefore
   directional; it currently emits no exact rational test-function certificate. Conditioning
   checks after whitening are numerical diagnostics.

`verdict.falsify` may flag an exact contradiction only when backed by an analytic identity or an
exact rational/interval witness. The run does not certify that argument; a formal refutation must
enter the independently checked proof workflow. Floating generalized eigenvalues, Galerkin
optima, and FEM $C_P/\mathrm{Var}$ values go through `compare_directional`, even when the
underlying moment matrices are deterministic and no Monte Carlo is used. Gate zero is *necessary
and never sufficient*: results on two structured families plus one algebraic countermodel do not
support $C_{\mathrm{CMH}}\le4$, still less prove it or KLS.

The stored run `research/runs/2026-08-25T070915.854321Z-cmh-gate-zero.jsonl` predates this
certificate hardening, and its recorded commit does not contain the target source. It is retained
unchanged as calibration history and is not linked from the ledger. A future run from recorded,
reproducible source would supply only a new directional research artifact.

## How a run supports research

No finite suite or numerical category qualifies a run for proof validation. The shared suite in
`research/knowledge/instances.md` exists to make exploratory results comparable, expose
implementation errors, and probe known obstructions without cherry-picking favorable cases.
Neither coverage of that suite nor green calibration and convergence gates validate a claim or a
proof. All numerical conclusions remain directional.

A run exclusively creates a uniquely timestamped, provenance-stamped JSONL; it will not
overwrite an existing artifact. Reproducibility rests on the recorded seed, params, and library
versions. `finum` does **not** edit the ledger: an agent may cite the artifact as provenance for a
directional research observation, never as proof validation. Exact symbolic identities or
rational/interval witnesses emitted beside a run are potential inputs to an analytic argument;
they acquire formal force only in an independently checked proof dossier. Historical artifacts
remain diagnostics. A `kls-loc` run is useful only after the corresponding route observable and
its gates exist, and a `kls-align` artifact stresses only its designated product family; neither
settles the universal node.

## Notes on accuracy

Heavy-tailed weighted-constant estimates (A3 Student-t with $\nu\le2$, generalized Cauchy with
$\beta\to d/2$) are grid-truncation limited and use directional tolerances; closed-form values
remain the theorem statements, not consequences of the FEM match. A5 folded-well values are
finite-domain directional estimates. A2 contamination uses an exact analytic variance lower
bound, whereas its BvM sweep is one data set and one chain per $n$ and has no chain-convergence
gate. A1 MCMC stress cases use a two-seed agreement gate, which is only a diagnostic and supplies
neither a mixing proof nor uncertainty bounds.
