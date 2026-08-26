# Deterministic moment-map / CMH

**Thesis.** Bound the canonical moment-Hessian quotient $C_{\mathrm{CMH}}$ and apply
`thm:cmh-implies-affine-poincare`.

## Active nodes

| node | role |
|---|---|
| `q:cmh-approximation` | pass the regular-class endpoint to arbitrary log-concave limits |
| `q:mm-invariant-lift` | construct the target-flat multiplier invariantly |
| `q:mm-square-root-commutator` | control the complete Haar commutator sum |
| `q:cmh-solenoidal-perturbation` | test the solenoidal channel at a saturating product |
| `conj:gate-zero` | decide the necessary linear moment-map inequality |

Detailed deliverables are in [`../gating.md`](../gating.md); exact statements and dependencies
are in [`../ledger.yaml`](../ledger.yaml).

## Main fence

The route must handle approximation, square-root commutators, and the nonnegative solenoidal
channel. CMH is a sufficient-condition route, not a reformulation of KLS: refuting
$C_{\mathrm{CMH}}\le4$ would not refute `conj:kls`.
