---
verdict: pass
authors:
  - kls-cmh-normalization, unknown, 2026-08-25
  - kls_proof_audit, unknown, 2026-08-25
  - repair_cmh_hodge_domain_w3, unknown, 2026-08-27
reviewer: reviewer, gpt-6-astra, 2026-10-04
fingerprints:
  solutions/thm-cmh-normalization.md: 2185916815f5cb008edc509ac80bdbf9eaf3ab72462e53cafc002fbe9eaa7a17
  prop:cmh-bochner: 237164772a03afb3fb5bfb7a896dbd45f8487332637efa548b827454d8f8ea6c
  def:cmh: 5971e940e93fa8179ce6c80c9817d3b3a88ac7db2ffe56897f1957c02431f9e7
  thm:cmh-implies-affine-poincare: 9210ad8934e1f76e3f1f621274c0be2dc1c9e5fa106146b66584871844acd5e0
  prop:cmh-hodge: e53f8f0d21ff4afad0be69fb034e09db1f7daaa882338a1d927af40c3117410e
  cor:cmh-hodge-comparison: 42676f87e102fd9313af73973dcf29ff5a7f17ccec197c3284254e7cf2c0e0cc
  thm:cmh-1d: 20ca97481f8d3f33bab114618adc59596740cec2d34e37ad9c5c8ec1b9fa9904
  prop:letwin-not-gate-zero: d01d5a5df0ca378b977846fd59185615903c42ec4bf019d71ebb41b5bf8e7c3a
---

## Findings

Fresh full independent `certify` examination, not a retained August verdict.
The reviewer received repository paths and an audit mission without the authoring
conversation. Author identities come from the historical reports and the August-27
repair checkpoints. Both complete CMH dossiers were read against their canonical
statements and ledger edges. The grouped mission has twelve primary nodes and
three additional current consumers, fifteen in total. This passing report covers
only the normalization dossier: three primary nodes and two additional consumers.
The separate exact-cases report records a defect outside the log-concave scope used
here; its general one-dimensional theorem is not certified by this report merely
because it occurs among the required statement fingerprints.

| Node | Conclusion |
| --- | --- |
| `prop:cmh-bochner` | Pass: canonical integrated identity on the stated core and its graph closure. |
| `thm:cmh-implies-affine-poincare` | Pass: regular-class implication, with exactly the same constant. |
| `prop:letwin-not-gate-zero` | Pass: the quantified matrix countermodel for every integer m at least 18. |
| `prop:cmh-hodge` | Pass: closed-operator Hodge identity, minimality and inverse norm. |
| `cor:cmh-hodge-comparison` | Pass within its standing log-concave setting, including its one-dimensional specialization. |

### Operator and endpoint checks

The form uses the same probability density as the divergence. Smooth local positive
coefficients give closability; the no-flux realization includes constants. Positivity
on the connected interior identifies the kernel with constants. The common test
class has finite H-energy because its gradient is bounded and the Stein
normalization gives finite expected trace of H. The endpoint proof then uses the
form/operator pairing at its correct domains. Both spectral cutoffs are needed:
the upper cutoff puts the truncated inverse in the operator domain and the lower
one avoids assuming an inverse bounded on centered L2. Its image under A is
exactly the spectral projection of f. Cauchy–Schwarz uses the covariance and its
inverse in dual positions, with no dimension or factor-two loss. Strong spectral
convergence recovers centered f; density is taken in the covariance Sobolev norm,
not in the H-form norm. The assertion for infinite CMH is immediate.

In the Bochner calculation the drift terms cancel after the second integration by
parts. The residual coefficient identity is the total symmetry of
H_mj partial_j H_kl = phi_mkl in source coordinates. Both remaining terms are
nonnegative, so the stated graph-Cauchy argument carries the identity to the
declared closure. This is an identity for the canonical Hessian, not for arbitrary
positive Stein kernels. Its hypotheses are not needed by the endpoint proof.

For Hodge, the covariance gradient is closed, its adjoint is the weak no-flux
divergence, and the finite flux-norm hypothesis on u lets the core identity extend
to the covariance form domain. Fixed-measure log-concave Poincare finiteness makes
the centered covariance inverse bounded. Thus psi lies in the operator domain,
w lies in the adjoint kernel, and their orthogonality is a legitimate adjoint
pairing. The spectral variational formula gives exactly the affine Poincare
constant. Density of Ran(A) in centered L2 suffices for the comparison when CMH
is finite; when CMH is infinite the comparison is automatic. In one dimension,
rho w is constant and the no-flux convention makes it zero. Here Poincare is finite,
so the inverse step in the one-dimensional dossier is valid and its quadratic form
is continuous on centered L2. This verifies the specialization actually used here
without importing the defective infinite-Poincare branch of that dossier.

All standing hypotheses have a role: centering and covariance finiteness normalize
the operators; full dimension is interpreted intrinsically on an affine support;
positive H and connected support identify constants; regularity and no-flux justify
the local calculus and closure. Log-concavity supplies fixed-measure Poincare
finiteness for Hodge but is unused in the endpoint estimate itself. No universal
CMH premise or regular-approximation premise is assumed in these five results.

### Countermodel and exact logical scope

The Schur complement is c times the identity, with c positive. Spherical second
and fourth moments give the displayed quadratic form for every symmetric B.
Its vector coefficient is at most the comparison coefficient; its traceless
coefficient is 1+(m-2)/((2m-1)(m+2)), at most 2; its scalar deficit is exactly
(a-dt)^2. The first diagonal entry of the expected square is 1+d, and d>3
holds for every integer m at least 18. The commutator trace identity has the
correct sign and factor one half.

The negated assertion is the universal implication from the three algebraic
conditions (positive semidefiniteness, mean identity, and the fixed-matrix quadratic
bound) to expected square at most 4 times identity. Each displayed matrix law
with m at least 18 witnesses its failure. No realization as a moment-map Hessian
is claimed or proved. Consequently neither gate-zero conjecture moves to
`refuted`, and this supplies no strict separation of CMH from KLS. Statements
about needing extra structure are understood at precisely this three-hypothesis
level, not as a classification of all possible proofs.

### Sources, relations and build

The needed external input is ordinary fixed-measure Poincare finiteness and the
finite one-dimensional bound, not a Letwin preprint theorem. I checked
[Cattiaux–Guillin, arXiv v1, equation (2.25)](https://arxiv.org/pdf/1810.08369),
and its [revised author version, equation (2.13)](https://perso.math.univ-toulouse.fr/cattiaux/files/2013/11/cattiaux-guillin-GAFA-revised21.pdf).
The author lists the work as published in *Geometric Aspects of Functional
Analysis*, LNM 2256 (2020), pp. 171–217. It is an established input, not an
unreviewed recent preprint. Its trace-variance bound yields both needed facts.
The [1995 KLS paper](https://www.renyi.hu/~miki/KannanLovSimIso.pdf) was also
retrieved; the exact Poincare normalization is checked in the cited
Cattiaux–Guillin display rather than inferred from differently normalized
isoperimetry.

All five nodes are currently proved; their recorded dependencies are supplied in
the required scope. There are no `assumes` or `bounded_by` edges on them. The
open approximation and gate-zero statements are not proof inputs. The projection
ceiling concerns a different information restriction and is not violated here.
No cycle results from reading the one-dimensional specialization: it uses ordinary
Poincare duality and its external scalar bound, not the Hodge comparison as a premise.
The full `uv run scripts/check.py` completed successfully, with no MyST error.
The fingerprints above were produced by its single-dossier fingerprint command.

## Corrections

No repair is required for the five canonical statements certified here. The
normalization dossier's concluding description of approximation closure as still
open is stale relative to the current conditional proved node; this historical
scope paragraph is not an input or a new approximation theorem. The separate
exact-cases report gives the proof repair required for the wider one-dimensional
claim. This pass does not cure that claim.

## Exclusions

No certification of the exact-cases dossier, the general non-log-concave
one-dimensional claim, regular approximation closure, universal CMH, KLS,
gate zero, strict nonimplication, or perturbative instability. No review of
Letwin's source proof is needed or claimed. Numerical runs supply no evidence.
The downstream fiber-floor proof was inspected only to locate its use of the
Dirichlet Poincare constant, not recertified in full.

## Proposed proof records

For each of `prop:cmh-bochner`, `thm:cmh-implies-affine-poincare`,
`prop:letwin-not-gate-zero`, `prop:cmh-hodge`, and `cor:cmh-hodge-comparison`,
retain `status: proved` and its current relations, and use:

```yaml
artifact: solutions/thm-cmh-normalization.md
review: research/reviews/2026-10-04-cmh-aug25-grouped-normalization-pass.md
```
