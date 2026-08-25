# A2 — Asymptotic constants via Bernstein–von Mises

> Mutable refinement brief. The ledger and manuscript are authoritative; dated history belongs
> in `research/explorations/`.

## Entry points

- Headline node: `conj:a2`
- Manuscript: [`modules/open-targets/A2-bernstein-von-mises.tex`](../../../modules/open-targets/A2-bernstein-von-mises.tex) (`conj:a2`)
- Numerical target: [`finum/targets/a2.py`](../../../experiments/finum/targets/a2.py), `finum run --target A2`
- Finite-sample counterpart: `conj:a1`

## Target-specific guardrails

- `obs:tv-insufficient` — Bernstein--von Mises convergence in total variation does not control
  functional-inequality constants; every positive target needs explicit spectral/tail stability.
- `obs:gaussian-tail-rigidity` — fixed Gaussian-prior logistic posteriors have prior-scale global
  LSI and $T_2$, even when their Poincaré constant is Fisher-local.
- The target is the limit of the rescaled constant $nC_P$, not a statement that the limit is
  $1/n$.

## Active handoff

| node | requested deliverable |
|---|---|
| `conj:a2` | Identify a useful spectral-stability/tail contract giving the Fisher-scale Poincaré limit. |
| `thm:a2-target` | Certify the existing global Gaussian-comparison implication or sharpen its hypotheses. |
| `q:a2-poincare` | Extend the proved fixed-dimensional logistic route to random designs, unbounded Hessians, or growing dimension. |
| `q:a2-lsi` | Classify Fisher-local global-tail models and localized alternatives without contradicting logistic rigidity. |
| `q:a2-multimodal` | Separate physical metastability from removable symmetry before applying a local limit. |
| `q:a2-highdim` | State a growing-dimension regime with explicit uniformity requirements. |

## Candidate refinement

None currently. A proposal must distinguish the Poincaré target from global LSI/$T_2$ and state
the topology or comparison hypothesis that transfers the constant.

## Context

- [Strong-Laplace audit](../../explorations/2026-08-21-a2-strong-laplace-and-global-constants.md)
- [Tail-rigidity exploration](../../explorations/2026-08-21-a2-subquadratic-tail-rigidity.md)
- [Tail-rigidity solution](../../../solutions/a2-subquadratic-tail-rigidity.tex)
- [Independent review](../../reviews/2026-08-21-a1-a2-independent-agent-audit.md)
