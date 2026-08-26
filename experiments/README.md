# finum — numerical research diagnostics

`finum` runs calibrated numerical batteries for the A-series and KLS research programs. Its
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
[`research/knowledge/instances.md`](../research/knowledge/instances.md). It is not executable
configuration; target modules own their effective battery and record it in each artifact.

## Commands

Run from this directory so `uv` uses the tracked lock file:

```bash
uv run python -m finum list
uv run python -m finum check
uv run python -m finum check A3
uv run python -m finum run A3
uv run python -m finum run loc-engine --profile full
uv run python -m finum run kls-align --profile high-n --seed 20260824
uv run pytest -m "not slow"
uv run pytest
```

`selftest` remains a compatibility alias for `check`; `run --target A3` remains a compatibility
form of `run A3`. A run target is otherwise mandatory—there is no silent default.

`check` is the fast installed-package smoke lane. Pytest without the `slow` marker is the normal
development lane. Full pytest includes the expensive localization Monte Carlo regressions.

## Targets and profiles

| target | role | profiles |
|---|---|---|
| `A1` | GLM curvature and flat-direction diagnostics | `standard` |
| `A2` | Bernstein–von Mises transfer diagnostics | `standard` |
| `A3` | weighted-Poincaré heavy-tail diagnostics | `standard` |
| `A4` | restricted transportation-cost diagnostics | `standard` |
| `A5` | quotient and reparameterization diagnostics | `standard` |
| `kls` | SDE-free Poincaré/KLS bridge checks | `standard` |
| `loc-engine` | legacy localization-engine regression; no route observable | `standard`, `full` |
| `kls-align` | product-Laplace tail-union alignment diagnostic | `standard`, `high-n` |
| `cmh-gate-zero` | deterministic necessary-condition CMH battery | `standard` |

Use `finum list` as the executable source of truth. `loc-engine` replaces the misleading public
name `kls-loc`; historical artifacts keep their original target id unchanged.

## Artifact contract

Every run creates a new JSONL file under `research/runs/` unless `--out` is supplied. Existing
files are never overwritten. The lines are:

1. `_provenance`: artifact schema version, target, profile, stochasticity, exact run
   configuration, commit, and interpreter/library environment;
2. target-owned records, each with a string `kind`;
3. one `run-summary` record containing derived run-level outputs.

Inputs never share a mapping with derived results. The current envelope version is
`finum.contract.ARTIFACT_SCHEMA_VERSION`. Historical artifacts are append-only and are not
migrated when the schema changes.

## Package layout

```text
finum/
  contract.py       TargetSpec, RunResult, artifact schema version
  provenance.py     repository paths, environment stamp, exclusive JSONL writer
  run.py            profile resolution and artifact dispatch
  constants.py      empirical Rayleigh and one-dimensional FEM/Hardy primitives
  transport.py      one-dimensional KL and W2 diagnostics
  sampling.py       seeded adaptive/preconditioned MALA
  localization/     localization state, cuts, moments, gates, and alignment observables
  targets/          stable public registry
    a_series/       A1--A5 batteries
    kls/            bridge, localization, alignment, and CMH batteries
tests/              fast deterministic/oracle tests plus explicitly marked slow MC regressions
```

Target-specific mathematical conclusions, limitations, and historical run interpretation belong
in `research/explorations/`, `research/knowledge/`, and the program documents—not in this harness
guide.
