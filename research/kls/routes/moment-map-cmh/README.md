# Route: deterministic moment-map / CMH

Status: live. The route asks whether the canonical moment-Hessian quotient
$C_{\mathrm{CMH}}$ admits a universal bound, with constant $4$ as the sharp headline. On the
regular moment-map class, `thm:cmh-implies-affine-poincare` proves
$C_P^{\mathrm{aff}}\le C_{\mathrm{CMH}}$.

This is a sufficient-condition route, not a proved reformulation of KLS. `prop:cmh-hodge` splits
the numerator into the affine Poincaré channel plus a nonnegative solenoidal channel. No
separating log-concave measure and no strict non-implication theorem is known.

## What is certified

- `def:cmh`, `prop:cmh-bochner`, `thm:cmh-implies-affine-poincare`, and `prop:cmh-hodge` fix the
  normalization and regular-class endpoint.
- `thm:cmh-1d`, `thm:cmh-product`, `cor:cmh-linear-images`, and the Dirichlet nodes give exact
  model classes.
- `prop:letwin-not-gate-zero` proves that constant-matrix control alone cannot imply gate zero;
  genuine differential moment-map structure is necessary.

The corresponding dossiers and proof reviews are linked from the central
[`../../ledger.yaml`](../../ledger.yaml).

## What is open

| layer | active nodes | role |
|---|---|---|
| closure | `q:cmh-approximation` | pass the regular-class endpoint through arbitrary log-concave limits |
| construction | `q:mm-invariant-lift`, `q:mm-square-root-commutator` | derive the all-split multiplier and control the complete Haar/commutator sum |
| route tests | `conj:gate-zero`, `q:cmh-solenoidal-perturbation` | test necessary linear-sector control and the zero-slack product endpoint |

The perturbation test and a genuine gate-zero counterexample could close CMH(4) before the
construction layer is completed. Such a result would not refute KLS.

## Working files

- [`open-problems.md`](open-problems.md) is the active handoff.
- [`claims.md`](claims.md) and [`models.md`](models.md) are compatibility pointers to dated
  archives; they are not current registries.
- [`research/knowledge/instances.md`](../../../knowledge/instances.md) is the shared model battery.
- [`experiments/README.md`](../../../../experiments/README.md) owns numerical implementation status.

The full mathematics is in `modules/kls/40-moment-map-cmh.tex`,
`41-cmh-normalization.tex`, and `42-cmh-exact-cases.tex`. A green checker validates structure and
review metadata, not the mathematics of a CMH claim.
