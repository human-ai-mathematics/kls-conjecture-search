# The Kannan–Lovász–Simonovits frontier

This repository contains a LaTeX manuscript on routes toward the Kannan–Lovász–Simonovits
conjecture — the dimension-free Poincaré bound $C_P \le K\lambda_{\max}(\mathrm{Cov})$ for an
arbitrary isotropic log-concave measure — together with the research harness used to track open
claims, proofs, reviews, and numerical diagnostics.

The manuscript lives in [`modules/kls/`](modules/kls/) and is organized in eight groups: an
orientation to the conjecture, the August 2026 frontier and the covariance-spike obstruction; a
self-contained survey of the five strategy families in the literature; the shared localization
machinery; then one block per live route — the fixed-cut Eldan program, the fixed-eigenfunction
spectral program, the deterministic moment-map/CMH program, and conditional-fiber frames — and a
synthesis mapping each named gap onto an open ledger node.

## Build

Requires a TeX Live install with `latexmk`, `biber`, `subfiles`, `biblatex`.

```bash
latexmk -pdf -outdir=build main.tex          # the whole document → build/main.pdf
```

Individual modules also compile standalone; unresolved cross-references to other modules are
expected in standalone builds.

## Repository map

| content | source |
|---|---|
| master document and bibliography | [`main.tex`](main.tex), [`references.bib`](references.bib) |
| manuscript modules | [`modules/kls/`](modules/kls/) |
| claim ledger, problem brief, search portfolio | [`research/program/`](research/program/) |
| search checkpoints, reviews, run artifacts | [`research/`](research/) |
| standalone proof dossiers | [`solutions/`](solutions/) |
| numerical diagnostics | [`experiments/`](experiments/) |
| repository contribution contract | [`CLAUDE.md`](CLAUDE.md) |

Current claim counts, the unresolved frontier and what the search is doing are all derived:

```bash
python3 scripts/check.py            # every lane; 0 errors is the invariant
python3 scripts/check.py status     # the unresolved frontier
python3 scripts/check.py portfolio  # families, routes, blockers
python3 scripts/check.py node conj:kls
```

The full verification matrix, including the numerical suite and the standalone dossier builds, is
[`scripts/check.sh`](scripts/check.sh). The checker validates structure, not mathematical
correctness ([`CLAUDE.md`](CLAUDE.md) constraint 4).
