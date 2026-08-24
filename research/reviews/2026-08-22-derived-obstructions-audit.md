# Derived-obstructions independent-agent audit

- **Date:** 2026-08-22
- **Underlying proof authors:** `/root/a1_a2` and `/root/a4_a5`
- **Independent derived-scope reviewer:** `/root/audit_metadata`
- **Certification:** `checked_by: agent`
- **Verdict:** pass for exactly the two derived obstruction nodes below

## Certified scope

1. `obs:gaussian-tail-rigidity` — direct consequence of
   `prop:a2-subquadratic-global` and its finite binary-logistic corollary
   `prop:a2-logistic-global`: the exact global Gaussian-prior logistic constants remain at the
   top prior-covariance scale, so a global Fisher/posterior-scale improvement is impossible
   without changing the tail assumptions or the notion of constant.
2. `obs:symmetry-vs-physical` — direct restatement of the restricted-gap identity in
   `prop:a5-ratio`: when the invariant gap is finite and positive, quotienting strictly improves
   the Poincaré constant exactly when the non-invariant gap is smaller; equality or an invariant
   slower block gives no strict improvement.

The reviewed proof dossiers are
[`solutions/a2-subquadratic-tail-rigidity.tex`](../../solutions/a2-subquadratic-tail-rigidity.tex)
and [`solutions/prop-a5-ratio.tex`](../../solutions/prop-a5-ratio.tex).

## Checks performed

For the Gaussian-tail obstruction, this audit compared the obstruction statement with the exact
equality proved by the directional subquadratic theorem and its binary-logistic corollary. The
obstruction adds no new estimate: its no-improvement conclusion is the immediate logical
consequence of that equality.

For the symmetry obstruction, this audit checked the invariant/non-invariant orthogonal
decomposition, the extended-reciprocal convention, and the finite-positive hypothesis required
to state the ordinary ratio and strict-gain criterion. The obstruction is precisely that
criterion expressed as a theorem-design guardrail.

## Provenance boundary and exclusions

The 2026-08-21 reports certify only their original five A1/A2 and eleven A4/A5 positive nodes.
This 2026-08-22 audit does not attribute the derived obstruction scope to those reviewers. It
uses the previously certified base propositions and independently checks only the two logical
consequences listed above.

No broader A1, A2, A4, or A5 claim is certified here. In particular, this audit does not certify
new tail classes, localized constants, numerical evidence, quotient metastability, eigenvector
stability, or any converse beyond the hypotheses already present in the two base dossiers.
