# Deterministic moment-map / CMH

**Thesis.** Bound the canonical moment-Hessian quotient $C_{\mathrm{CMH}}$ and apply
`thm:cmh-implies-affine-poincare`.

## Active nodes

| node | role |
|---|---|
| `ass:cmh-recovery-envelope` | find one regular recovery sequence with bounded CMH liminf |
| `ass:uniform-cmh-approximants` | bound CMH uniformly along the certified regular approximation family |
| `q:mm-invariant-lift` | construct the target-flat multiplier invariantly |
| `q:mm-square-root-commutator` | control the complete Haar commutator sum |
| `q:cmh-solenoidal-perturbation` | test the solenoidal channel at a saturating product |
| `conj:gate-zero` | decide the necessary linear moment-map inequality |

`q:cmh-approximation` is certified conditionally: it closes the limit passage without loss under
`ass:uniform-cmh-approximants`, but does not establish that premise or continuity of
$C_{\mathrm{CMH}}$. The weaker `ass:cmh-recovery-envelope` asks only for one well-chosen sequence;
its lower-semicontinuity and sufficiency bridge are tracked separately. Detailed remaining deliverables are in [`../gating.md`](../gating.md);
exact statements and dependencies are in [`../ledger.yaml`](../ledger.yaml).

## Main fence

The remaining route must establish uniform CMH control on the certified regular approximants,
control square-root commutators, and handle the nonnegative solenoidal channel. CMH is a
sufficient-condition route, not a reformulation of KLS: refuting
$C_{\mathrm{CMH}}\le4$ would not refute `conj:kls`.
