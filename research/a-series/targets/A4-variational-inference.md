# A4 — Transport constants for variational inference

> Mutable refinement brief. The ledger and manuscript are authoritative; dated history belongs
> in `research/explorations/`.

## Entry points

- Headline node: `q:a4-certificate`
- Manuscript: [`modules/open-targets/A4-variational-inference.tex`](../../../modules/open-targets/A4-variational-inference.tex) (`q:a4-certificate`)
- Numerical target: [`finum/targets/a4.py`](../../../experiments/finum/targets/a4.py), `finum run --target A4`
- Baselines: `thm:glm-fi`, `prop:a4-logistic-global`

## Target-specific guardrails

- `obs:restricted-not-finite` — a KL cutoff alone need not give finite $W_2$ radius; state
  family coercivity, compactness, or quadratic-exponential tail control.
- `obs:flat-direction` and `obs:gaussian-tail-rigidity` — global location-rich logistic constants
  remain prior-scale, so posterior-scale claims must be localized.
- `obs:symmetry-vs-physical` — multimodal lower bounds depend on the variational family and should
  be compared with the appropriate quotient problem.
- Keep raw approximation error separate from optimizer-centered excess-KL geometry, and treat an
  upper bound on $\log Z$ as a separate requirement for an end-to-end certificate.

## Active handoff

| node | requested deliverable |
|---|---|
| `q:a4-certificate` | State and prove a finite-radius posterior-scale certificate with explicit coercivity and remainder terms. |
| `q:a4-restricted` | Compute localized raw and optimizer-centered constants for a specified posterior/family pair. |
| `q:a4-mean` | Characterize family-restricted mean constants using the proved cumulant duals. |
| `q:a4-modified` | Match robust-prior tail classes with defensible modified transport costs. |
| `q:a4-multimodal` | Turn component-reweighting and mode-collapse witnesses into family-dependent bounds. |
| `q:a4-elbo` | Pair the localized constant with a computable upper KL certificate. |

## Candidate refinement

None currently. A proposed theorem must name the variational family, the nonempty sublevel
$\delta_{\mathcal Q}+\rho$, the finiteness mechanism, and every approximation/remainder term.

## Context

- [Restricted-transport audit](../../explorations/2026-08-21-a4-restricted-transport-audit.md)
- [Local-VI next cycle](../../explorations/2026-08-21-a4-local-vi-next-cycle.md)
- [Mean-dual solution](../../../solutions/eq-a4-mean-dual.tex)
- [Independent review](../../reviews/2026-08-21-a4-a5-independent-agent-audit.md)
