# A1 — Data-informed GLM Poincaré constant

## Entry points

- Headline node: `conj:a1`
- Manuscript: [`modules/open-targets/A1-data-informed-glm.tex`](../../../modules/open-targets/A1-data-informed-glm.tex) (`conj:a1`)
- Numerical target: [`finum/targets/a_series/a1.py`](../../../experiments/finum/targets/a_series/a1.py), `finum run A1`
- Baseline: `thm:glm-fi`

## Target-specific guardrails

- `obs:flat-direction` — a saturating likelihood can lose curvature remotely, so a universal
  inverse-mode-Hessian proposal needs a tail term or a genuinely stronger model hypothesis.
- `obs:gaussian-tail-rigidity` — global logistic LSI and $T_2$ remain at the Gaussian-prior
  scale; data-informed versions must be local, restricted, or use a stronger tail class.
- Any finite-sample certificate must state when it beats the prior-scale baseline rather than
  merely reproducing it.

## Active handoff

| node | requested deliverable |
|---|---|
| `conj:a1` | Give a computable $\bar W$ and tail certificate that beats the prior scale on an explicit nontrivial GLM class. |
| `q:a1-poincare` | Certify the bulk--tail comparison and extend factor one beyond bounded Hessians. |
| `q:a1-barw` | Replace conservative maximal-row control by a sharper spectral or posterior-informed construction. |
| `q:a1-tail` | Improve the explicit radial tail control, especially when the direct $\eta<1$ gate fails. |
| `q:a1-sharp` | Quantify the finite-sample route and preserve the A1--A2 Fisher-scale limit. |
| `q:a1-lsi` | Formulate a defensible localized/restricted LSI or transport target. |

## Candidate refinement

None currently. Stage an exact statement delta here before asking the orchestrator to update the
manuscript and ledger. Any proposed diagnostic should use the shared instances and treat sampled
quantities as directional only.
