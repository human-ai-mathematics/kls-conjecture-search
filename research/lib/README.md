# numerics — numerical research diagnostics

`numerics` runs calibrated numerical batteries for the KLS research program. Its
output guides exploration; it never changes a ledger status or certifies a proof.

## Boundary

- Sampled, MCMC, FEM, quadrature, finite-grid, and floating-eigensolver values are
  `directional` evidence.
- Closed-form or rationally certified comparisons are `exact` evidence inside the artifact, but
  still require an independently reviewed proof or refutation dossier before they have logical
  force.
- Comparison outcomes are neutral: `match`/`mismatch` for calibration and
  `exceeds`/`within`/`unavailable` otherwise. They are not claim statuses.
- A finite battery can expose a bug or an obstruction. Passing it proves nothing universal.

The canonical, human-reviewed instance registry is
[`instances.md`](instances.md). It is not executable
configuration; target modules own their effective battery and record it in each artifact.

## Commands

Run from this directory so `uv` uses the tracked lock file:

```bash
uv run python -m numerics list
uv run python -m numerics check
uv run python -m numerics check kls
uv run python -m numerics run kls
uv run python -m numerics run loc-engine --profile full
uv run python -m numerics run kls-align --profile high-n --seed 20260824
uv run pytest -m "not slow"
uv run pytest
```

`selftest` remains a compatibility alias for `check`; `run --target kls` remains a compatibility
form of `run kls`. A run target is otherwise mandatory—there is no silent default.

`check` is the fast installed-package smoke lane. Pytest without the `slow` marker is the normal
development lane. Full pytest includes the expensive localization Monte Carlo regressions.

## Targets and profiles

| target | role | profiles |
|---|---|---|
| `kls` | SDE-free Poincaré/KLS bridge checks | `standard` |
| `loc-engine` | legacy localization-engine regression; no route observable | `standard`, `full` |
| `kls-align` | product-Laplace tail-union alignment diagnostic | `standard`, `high-n` |
| `kls-screen` | cut-local screened-supply `conj:weighted-excess-rate` diagnostic (surrogate excess) | `smoke`, `standard`, `high-n` |
| `cmh-gate-zero` | deterministic necessary-condition CMH battery | `standard` |
| `cmh-ab` | CMH anisotropic-bootstrap (N, D, R) and M9 probe | `standard`, `exact-only`, `fast` |
| `fiber-frame-dual` | conditional-fiber-frame all-frame simplex pencil library | `standard`, `deep` |
| `cmh-cone` | exponential-cone gate matrices and CMH Galerkin battery | `standard`, `exact-only` |

Use `numerics list` as the executable source of truth. `loc-engine` replaces the misleading public
name `kls-loc`; historical artifacts keep their original target id unchanged.

## Artifact contract

Every run creates a new JSONL file under `research/runs/` unless `--out` is supplied. Existing
files are never overwritten. The lines are:

1. `_provenance`: artifact schema version, target, profile, stochasticity, exact run
   configuration, commit, and interpreter/library environment;
2. target-owned records, each with a string `kind`;
3. one `run-summary` record containing derived run-level outputs.

An artifact converted from an older schema additionally carries `migrated_from.path` under
`research/legacy-runs/` and the source file's SHA-256. That directory was removed in the v0.2.0
migration; the sources stay in git history (`git show 34b5fcd:research/legacy-runs/<file>`).

Inputs never share a mapping with derived results. The current envelope version is
`numerics.contract.ARTIFACT_SCHEMA_VERSION`. Historical artifacts are append-only and are not
migrated when the schema changes.

## Package layout

```text
numerics/
  contract.py       TargetSpec, RunResult, artifact schema version
  provenance.py     repository paths, environment stamp, exclusive JSONL writer
  run.py            profile resolution and artifact dispatch
  constants.py      empirical Rayleigh and one-dimensional FEM/Hardy primitives
  transport.py      one-dimensional KL and W2 diagnostics
  sampling.py       seeded adaptive/preconditioned MALA
  localization/     localization state, cuts, moments, gates, and alignment observables
  targets/          stable public registry
    kls/            bridge, localization, alignment, and CMH batteries
tests/              fast deterministic/oracle tests plus explicitly marked slow MC regressions
```

Target-specific mathematical conclusions, limitations, and historical run interpretation belong
in `research/explorations/`, `research/program/`, and the manuscript—not in this harness
guide.
