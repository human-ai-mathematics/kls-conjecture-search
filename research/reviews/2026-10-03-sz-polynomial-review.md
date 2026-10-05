---
verdict: pass
authors:
  - researcher-polynomial, gpt-6-astra, 2026-10-03
reviewer: reviewer, gpt-6-astra, 2026-10-03
fingerprints:
  solutions/thm-sz-polynomial-variance.md: c92951566e91b96e08af41f44ff011b514d0e4ad658d99e745d6a40ef9cd7dcc
  thm:sz-polynomial-variance: ffd52798e616ccd22bb3e4c78d5c382fd5657d3b598e6e4ec3c9afc4f696da8e
  thm:letwin-qcts: 8e2ac0819f46db553fe83a6f3034436816565262316c2e6bde7d81baead1a082
  lem:sz-analytic-foundations: e3b0250c18499cbdf58b3cb609937032b0101d8aa096aac355555309e5e94d3f
---

# Polynomial localization and analytic foundations: independent review

## Findings

The dossier proves both `thm:sz-polynomial-variance` and
`lem:sz-analytic-foundations` as stated in `modules/00-overview.md`.
The context was originally launched without conversation history. Its earlier
assignment was independent synchronization of the literature integration, not
authorship or direction of either proof. The author identity above was supplied
by the assignment. This review was reconstructed from the dossier, canonical
statements, ledger and source; the author's account was not proof evidence.

### Statements, hypotheses and dependencies

The polynomial theorem includes all degrees, full ordered-index tensor norms,
the constants $1024^d(d!)^4$ and $32^k k!$, and centered laws of covariance at
most the identity. The dossier first proves the isotropic case and explicitly
contracts tensors on the linear support to cover singular covariance, including
rank zero. Its formal Appell expansion supplies precisely the derivative-mean
conclusion. The analytic lemmas together contain every assertion of the
canonical analytic-foundations node, including the finite-energy test class in
the weak-limit assertion.

The only nonclassical input is the certified node `thm:letwin-qcts`. Its
canonical quadratic variance constant is exactly the one used. The ledger
records that dependency for the polynomial node and no open antecedent. The
analytic-foundations proof does not use the polynomial estimate or Letwin's
input. No circular dependence between the two jointly reviewed nodes occurs.

Hypotheses used: log-concavity, centering and the covariance upper bound for
the polynomial theorem; finite degree and symmetric coefficient tensors;
smooth positive density and both Hessian bounds for the operator claims;
isotropy for the regular approximation construction; absolute continuity of
the limiting probability and a common finite Poincare bound for scalar
stability. Compact support, invertibility of covariance, and normalized
covariance are intermediate restrictions explicitly removed. The proof uses
no unmentioned uniform curvature or moment-convergence rate. No stated
hypothesis is identified as dispensable by this review.

### Mathematical steps checked

1. Formal division and differentiation of the generating series give the
   expected-derivative identities. Descending homogeneous degree proves the
   exact expansion. The extension to finite Hilbert-valued output uses direct
   sums and Minkowski, not Gaussian orthogonality.
2. Quadratic variance and matrix duality give the directional third-tensor
   estimate. Complete symmetry gives the operator square sum. Its trace
   bounds have the stated dimension factors; no dimension-free bound for the
   full third-tensor norm is inserted.
3. The finite-dimensional SDE coefficients are smooth at finite parameters.
   The Ito quotient drift cancels, and subtracting the mean square contributes
   the required covariance drift. The logarithmic determinant has martingale
   bracket at most $8n^2t$ and drift bounded below by $-5n$. Combining its
   pathwise lower bound with bounded spatial support prevents degeneration
   and explosion. Stopping on the resulting random bounds justifies the
   continuation argument. Bounded posterior tests are true martingales.
4. On tensor products, each unordered covariance pair appears once. The
   normalized metric noise satisfies the operator square bound; weighted
   Bessel controls the derivative-mean noise. The two mixed Ito terms are
   retained and bounded, yielding $4j^2N_j+9j^2L_j$. Compact support bounds
   stochastic integrands and absolute drifts after these estimates, so the
   expectation derivative and removal of parameter stops are justified.
5. Whitening the posterior inserts a covariance factor in every derivative
   slot. This produces the exact $N_{j+k}$ hierarchy without a dimension
   factor. The reciprocal-binomial sum is at most two. The finite maximum
   satisfies the integral Gronwall inequality with coefficient $40d^2$.
6. The variance-survival estimate follows from Bessel and the martingale
   equations for the fixed tests $f,f^2$. Strong convexity at terminal time
   gives the matrix Poincare estimate. Expanding the displayed square proves
   the inverse-integral inequality. The tower step retains the measurable
   random matrix at time $s$ and uses the fixed tests $r_ir_j$; it makes no
   independence assertion. Fubini is justified on compact support.
7. Substitution of $\tau=(40d^2)^{-1}$ gives the displayed factor $600$;
   $d^2((d-1)!)^2=(d!)^2$ closes the bound with $1024^d$. This is analytic
   arithmetic, not a numerical experiment. Conditional moments through
   degree $2d$ and coefficientwise convergence remove compact support.
8. For the analytic claims, cutoff and local mollification identify the
   form domain. Local elliptic regularity and the bounded cutoff commutator
   prove the graph-core assertion. Applying Bochner to differences gives
   convergence of weak Hessians; the upper Hessian bound passes the curvature
   term. Strong convexity puts polynomial tests in the form domain.
9. Unitary conjugation gives a confining Schrodinger potential. Rellich
   compactness on balls together with its quadratic tail estimate gives
   compact resolvent. The one-dimensional kernel, Rayleigh principle and
   spectral calculus give the first eigenfunction and inverse-square-root
   identities with the stated domains.
10. The weak-limit proof first passes compact smooth tests, then truncates
    values and cuts off space. Absolute continuity justifies mollification.
    The independent-copy Fatou argument proves square integrability rather
    than assuming it. Gaussian convolution, quadratic tilt and whitening
    yield regular isotropic approximants with no uniform Hessian bounds
    asserted or required.

### Sources checked

The pinned [Song--Zhang v1](https://arxiv.org/html/2610.01447v1) was read in
Sections 2.3 and 3--4, and compared with its source files
`/tmp/kls-song-zhang-source/10_preli.tex` and `20_upper.tex` (through the proof
of Theorem 4.1). These source proofs themselves were checked, not merely their
theorem statements.

The classical analytic inputs were checked against the actual text of
[Evans, *Partial Differential Equations*, second edition](https://dokumen.pub/partial-differential-equations-19-2nbsped-0821849743-9780821849743.html):
Section 6.3.1 Theorem 1, Section 5.7, and Appendix D.6 Theorem 7. Restricting
to balls supplies the bounded lower-order coefficients needed for interior
regularity; the compact embedding is used locally before the tail estimate.

The stochastic existence, stopping and Ito inputs were checked in
[Bakry--Gentil--Ledoux, *Analysis and Geometry of Markov Diffusion Operators*](https://dokumen.pub/analysis-and-geometry-of-markov-diffusion-operators-9783319002262-9783319002279.html),
Appendix B.1--B.4. In particular, the local-existence discussion following
Theorem B.3.1 permits localization without a global linear-growth hypothesis;
the dossier supplies nonexplosion separately. The same book's Theorem 4.9.1
is the checked published source for the smooth matrix Brascamp--Lieb
inequality. Its inverse-Hessian bound implies the constant-matrix version;
the dossier explains the convex-potential approximation and subsequent test
extensions. The original 1976 article is historical attribution here; the
supplementary BGL citation explicitly supplies the accessible theorem used
in this review. Its proof need not be re-certified as a fresh preprint.

Preservation under convolution and marginalization was checked in
[Prekopa, 1973, Theorems 6--7](https://rutcor.rutgers.edu/Prekopa/pdf/SCIENT2.pdf).
Affine change, convex restriction and multiplication by a convex quadratic
follow directly from the density definition. Standard finite polynomial
moments of log-concave probabilities justify the moment approximation.

### Fences and build

Neither reviewed node has a `bounded_by` edge. The proof estimates the full
polynomial tensor, not only projections; it asserts no cut-source comparison,
universal-time occupation estimate, CMH statement or reverse sufficient-condition
implication. The existing obstructions therefore do not conflict with it.

`UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py --fingerprint
solutions/thm-sz-polynomial-variance.md` completed successfully and printed
the block above. The full `check.py` run reported no MyST error for this
dossier. It reported one separate checkpoint-format error in
`research/explorations/2026-10-03-sz-curvature-proof.md`; that unrelated
research-state formatting issue is not part of either proof and was reported
to the orchestrator. The dossier hash was checked again after the build.

## Corrections

None outstanding in the fingerprinted proof. A multiplication punctuation
error identified while the draft was being finalized was corrected before
fingerprinting; the accessible published matrix-inequality citation was also
added before this review was recorded.

## Exclusions

This review does not certify Song--Zhang Sections 5--7, the curvature
comparison, the all-depth iteration, `thm:song-zhang-kls`, or `conj:kls`.
It does not re-certify the pre-existing Letwin dossier. No numerical artifact
was used as proof evidence. The polynomial constants grow with degree and
do not provide a dimension-free Poincare bound for arbitrary test functions
by polynomial density alone.

## Certification delta

Both reviewed nodes may be `proved` with the record below. Retain
`depends_on: [thm:letwin-qcts]` for `thm:sz-polynomial-variance` and no
dependency or antecedent for `lem:sz-analytic-foundations`. Retain their
source references. No other status or relation changes follow.

```yaml
proofs:
  - artifact: solutions/thm-sz-polynomial-variance.md
    review: research/reviews/2026-10-03-sz-polynomial-review.md
```
