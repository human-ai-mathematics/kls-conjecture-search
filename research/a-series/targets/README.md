# A-series target briefs

Each file is a mutable handoff for one A-series stream. It contains entry points, target-specific
guardrails, active deliverables, and at most one proposed statement delta.

## Sources of truth

| content | location |
|---|---|
| accepted statement | [`../../../modules/open-targets/`](../../../modules/open-targets/) |
| status, dependencies, and certification | [`../ledger.yaml`](../ledger.yaml) |
| cross-target fences | [`../obstructions.md`](../obstructions.md) |
| attempts | [`../../explorations/`](../../explorations/) |
| numerical work | [`../../../experiments/`](../../../experiments/), [`../../runs/`](../../runs/) |
| proofs and reviews | [`../../../solutions/`](../../../solutions/), [`../../reviews/`](../../reviews/) |

The ledger and manuscript override a drifting brief. Do not copy status, dependency graphs,
attempt logs, or proof histories into these files.

## Streams

| stream | headline node | brief |
|---|---|---|
| A1 | `conj:a1` | [`A1-data-informed-glm.md`](A1-data-informed-glm.md) |
| A2 | `conj:a2` | [`A2-bernstein-von-mises.md`](A2-bernstein-von-mises.md) |
| A3 | `conj:a3-dependent` | [`A3-heavy-tailed-posteriors.md`](A3-heavy-tailed-posteriors.md) |
| A4 | `q:a4-certificate` | [`A4-variational-inference.md`](A4-variational-inference.md) |
| A5 | `conj:a5-metastable` | [`A5-quotient-and-reparameterization.md`](A5-quotient-and-reparameterization.md) |

## Editing rule

One file covers one stream. Record each attempt in a new dated exploration. Put only an exact
proposed statement or concise delta under **Candidate refinement**; the orchestrator promotes an
accepted change to the manuscript and ledger.
