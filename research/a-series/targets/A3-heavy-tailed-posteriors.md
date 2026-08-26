# A3 — Heavy-tailed posteriors beyond classical LSI

## Entry points

- Headline node: `conj:a3-dependent`
- Manuscript: [`modules/open-targets/A3-heavy-tailed-posteriors.tex`](../../../modules/open-targets/A3-heavy-tailed-posteriors.tex) (`conj:a3-dependent`)
- Numerical target: [`finum/targets/a_series/a3.py`](../../../experiments/finum/targets/a_series/a3.py), `finum run A3`
- Calibration anchors: `thm:a3-student`, `prop:a3-horseshoe`

## Target-specific guardrails

- `obs:heavy-tail-no-classical` — polynomial tails generally require weighted or weak
  inequalities; do not silently return to a classical Euclidean LSI/$T_2$ target.
- `obs:marginals-not-joint` — coordinate Hardy constants do not control a dependent joint law;
  expose a dependence gap or another joint coupling hypothesis.
- `obs:flat-direction` — a posterior result must account for likelihood directions that do not
  repair the prior geometry.
- The joint metric must include scale derivatives and the structural coefficient--scale cross
  terms induced by non-centering.

## Active handoff

| node | requested deliverable |
|---|---|
| `conj:a3-dependent` | Prove a dependence-aware hierarchical inequality in the non-centered pullback metric. |
| `prop:a3-hierarchical-prior` | Certify the prior pullback inequality, including all cross terms. |
| `q:a3-horseshoe` | Extend the sharp marginal result to specified likelihood tilts under assumptions weaker than bounded density ratio. |
| `q:a3-catalogue` | Separate the tail Hardy floor from the full bulk supremum across named robust priors. |
| `q:a3-weak` | Prove the one-dimensional weak-Poincaré rate and track product-dimension loss. |
| `q:a3-hierarchical` | Obtain explicit conditional Hardy and dependence-gap bounds for horseshoe normal means. |

## Candidate refinement

None currently. The next proposal should specify one posterior model, its complete pullback
Dirichlet form, and the data/dimension dependence of the block coupling contract.
