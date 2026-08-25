# A5 — Quotient and reparameterization constants

> Mutable refinement brief. The ledger and manuscript are authoritative; dated history belongs
> in `research/explorations/`.

## Entry points

- Headline node: `conj:a5-metastable`
- Manuscript: [`modules/open-targets/A5-quotient-and-reparameterization.tex`](../../../modules/open-targets/A5-quotient-and-reparameterization.tex) (`conj:a5-metastable`)
- Numerical target: [`finum/targets/a5.py`](../../../experiments/finum/targets/a5.py), `finum run --target A5`
- Certified spectral anchor: `prop:a5-ratio`

## Target-specific guardrails

- `obs:symmetry-vs-physical` — quotient improvement is governed by the invariant and
  non-invariant restricted gaps, not by the symmetry label of one fitted eigenfunction.
- `obs:heavy-tail-no-classical` — a funnel may have infinite Euclidean $C_P$ for tail reasons;
  reparameterization and quotient effects must remain separate.
- Every symmetry claim requires both the prior and likelihood to be group-invariant.
- Compare parameterizations only under a fixed normalization, such as $\kappa_P=L_VC_P$ or a
  stated bi-Lipschitz distortion; raw $C_P$ alone is defeated by dilation.

## Active handoff

| node | requested deliverable |
|---|---|
| `conj:a5-metastable` | Prove the raw connectivity-barrier law and quotient Fisher-scale law under explicit quantitative hypotheses. |
| `q:a5-qbvm` | Establish the A2 limit on the orbit space, including collision-stratum control. |
| `q:a5-metastable` | Prove the logarithmic raw-gap law before seeking prefactors. |
| `q:a5-detect` | Estimate invariant and non-invariant spectral blocks with residual and degeneracy control. |
| `q:a5-stratified` | Develop LSI/$T_2$ on stratified or orbifold quotients. |
| `q:a5-reparam` | Extend the normalized Gaussian partial-centering optimum and classify likelihood tail regularization. |

## Candidate refinement

None currently. A metastability proposal must use the worst-cut/connectivity height for a general
orbit, state its empirical-to-population transfer, and keep the quotient and raw conclusions
logically separate.

## Context

- [Quotient/reparameterization audit](../../explorations/2026-08-21-a5-quotient-reparameterization-audit.md)
- [Connectivity next cycle](../../explorations/2026-08-21-a5-connectivity-partial-next-cycle.md)
- [Spectral-ratio solution](../../../solutions/prop-a5-ratio.tex)
- [Independent review](../../reviews/2026-08-21-a4-a5-independent-agent-audit.md)
- [Funnel second review](../../reviews/2026-08-21-a5-funnel-second-agent-audit.md)
