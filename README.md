# Functional inequalities for statistical and machine-learning distributions

This repository contains a unified LaTeX manuscript on Poincaré, log-Sobolev, and quadratic
transportation-cost inequalities for probability measures used in statistics and machine
learning. It also contains the research harness used to track open claims, proofs, reviews, and
numerical diagnostics.

The manuscript has three parts:

- [`modules/`](modules/) develops the general toolkit and structured model families;
- [`modules/open-targets/`](modules/open-targets/) studies the A1--A5 statistical targets; and
- [`modules/kls/`](modules/kls/) develops four routes toward the KLS conjecture.

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
| manuscript modules | [`modules/`](modules/) |
| research programs and claim ledgers | [`research/`](research/) |
| standalone proof dossiers | [`solutions/`](solutions/) |
| numerical diagnostics | [`experiments/`](experiments/) |
| repository contribution contract | [`CLAUDE.md`](CLAUDE.md) |

Current claim counts and research frontiers are derived from the ledgers:

```bash
python3 research/check_ledger.py status
```

See [`research/README.md`](research/README.md) for the source of truth for each research plane.
