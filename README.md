# numina-functional-inequalities

A unified LaTeX treatment of functional inequalities --- the Poincaré (`C_P`), log-Sobolev
(`C_LS`), and quadratic transportation-cost (`C_TCI`) constants --- for the probability
measures `P ∝ e^{-U}` used in statistics and machine learning, organized as a single document
with a difficulty gradation.

- **Part I** (`modules/`) — structured statistical/ML families, by increasing difficulty:
  definitions and normalization, the imported toolkit and known landscape, then Tiers 1–5
  (Gaussian/linear-regression → perturbations/products → the Gaussian-prior GLM-posterior
  flagship → heavy tails → mixtures/hierarchical), and the open research agenda.
- **Part II** (`modules/open-targets/`) — proved A-series results and open-target deep dives:
  one section per flagship problem from the agenda (data-informed GLM constants,
  Bernstein–von Mises, heavy-tailed posteriors, variational inference,
  quotient/reparameterization).
- **Part III** (`modules/kls/`) — an exploratory proof program for the
  Kannan–Lovász–Simonovits conjecture (the "Tier-∞" boundary of Part I): a route-neutral
  literature/strategy map, a detailed Eldan fixed-cut program, the fixed-eigenfunction
  localization route, and a deterministic moment-map/Haar/Schur--Piola route.

The A1--A5 control plane currently records 21 independently reviewed positive intermediate
results. The main A1, A2, A4, and A5 selection targets remain open; the original marginal-only
A3 conjecture is refuted and replaced by a dependence-aware target. See the canonical
[`research/ledger.yaml`](research/ledger.yaml) and the concise
[`certified-probe summary`](research/explorations/2026-08-21-a-series-proof-probes.md).

## Build

Requires a TeX Live install with `latexmk`, `biber`, `subfiles`, `biblatex`.

```bash
latexmk -pdf -outdir=build main.tex          # the whole document → build/main.pdf
```

Each `modules/NN-*.tex` and `modules/kls/NN-*.tex` also compiles standalone (cross-references
to the other modules appear as `??`, which is expected).

## Layout

```
main.tex            unified master (subfiles); Part I + Part II + Part III
fi_references.bib   single shared bibliography
shared/
  preamble.tex      packages, theorem environments, macros
  notation.md       symbol glossary (reference only, not compiled)
modules/            Part I: 00-overview … 08-open-targets
modules/open-targets/  Part II: A1 … A5 deep dives
modules/kls/        Part III: three-route strategy map, Eldan dossier, and deterministic CMH route
research/           the control plane: ledger.yaml, knowledge/, targets/, reviews/, kls/,
                    runs/ (eligible numerical evidence artifacts), check_ledger.py
experiments/        the `finum` numerical channel (uv project) that produces the
                    provenance-stamped run artifacts in research/runs/
solutions/          proof plane: standalone .tex (+ .lean) proofs, checked_by ladder
CLAUDE.md           the rules an agent works under (soundness contract, done, constraints)
LEAN_DESIGN.md      the Lean (L2) channel plane: Mathlib gap → first solutions/*.lean targets
build/              compiled artifacts (gitignored)
```
