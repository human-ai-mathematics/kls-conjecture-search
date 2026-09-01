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

## Relation to `posterior-inequalities-exploration`

This repository and
[`posterior-inequalities-exploration`](https://github.com/numina-functional-inequalities/posterior-inequalities-exploration)
were one repository until 2026-09-01. The structured-posterior program — explicit Poincaré,
log-Sobolev and transportation-cost constants for statistical and machine-learning families, and
the A1–A5 open targets — now lives there with its own ledger and proof dossiers.

The two programs are mathematically disjoint in this repository's sense: no claim here depends on
a claim there, and the split introduced no dangling cross-reference. What connects them is a
comparison. `conj:kls` asks for the affine bound over *every* isotropic log-concave measure;
`conj:a1-bis` asks for the same bound over a structured class of GLM posteriors. KLS is the
Tier-$\infty$ limit of a difficulty gradation in which structure is exactly what buys an explicit
constant. That comparison is recorded in prose only — never as a ledger edge — and neither program
may import the other's result as a dependency.

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
| master document and bibliography | [`main.tex`](main.tex), [`fi_references.bib`](fi_references.bib) |
| manuscript modules | [`modules/kls/`](modules/kls/) |
| research program and claim ledger | [`research/`](research/) |
| standalone proof dossiers | [`solutions/`](solutions/) |
| numerical diagnostics | [`experiments/`](experiments/) |
| repository contribution contract | [`CLAUDE.md`](CLAUDE.md) |

Current claim counts and research frontiers are derived from the ledger:

```bash
python3 research/check_ledger.py status
```
