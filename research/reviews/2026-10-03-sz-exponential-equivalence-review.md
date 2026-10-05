---
verdict: pass
authors:
  - researcher-polynomial, gpt-6-astra, 2026-10-03
reviewer: reviewer, gpt-6-astra, 2026-10-03
fingerprints:
  solutions/prop-sz-exponential-coefficients-equivalence.md: 7560b924b47376f4b55abdfc294c6e37a9517eead4023a7bef52f716de4a2704
  prop:sz-exponential-coefficients-equivalence: b35523c7152cb78a2e221807ee2fb43636ac5f74907e1d8cfc15ec420c5c186e
  lem:sz-analytic-foundations: e3b0250c18499cbdf58b3cb609937032b0101d8aa096aac355555309e5e94d3f
  thm:sz-polynomial-variance: ffd52798e616ccd22bb3e4c78d5c382fd5657d3b598e6e4ec3c9afc4f696da8e
  thm:sz-curvature-comparison: 9baf9221ded7767fc4a904b4a582b9804ab1d424bb87914745aaaa6dd0242787
---

# Exponential Appell growth equivalence: independent review

## Findings

The dossier proves `prop:sz-exponential-coefficients-equivalence` exactly as
stated in `modules/32-polynomial-curvature.md`. This is an equivalence,
including its two quantitative implications, and not an unconditional
bound for either quantity. The reviewer was originally launched without
authoring conversation and has only synchronized and reviewed the related
proofs. The author identity was supplied by the assignment. No author's
account or computational artifact was used as proof evidence.

### Statement, hypotheses and dependencies

Both statements put a single finite constant outside the quantifiers over
dimension, degree and regular isotropic law. The curvature bounds in the
coefficient assertion may depend on the law. They agree on full symmetric
tensors, ordered-index Hilbert--Schmidt norms, division by $k!$, and the
constants $C^{(k-1)/2}$ and $32\max\{4A,2^{40}\}^2$.

The dependencies are `lem:sz-analytic-foundations`,
`thm:sz-polynomial-variance`, and `thm:sz-curvature-comparison`.
All three now have proved status and independent proof records. Their
canonical statements were reread and are exactly sufficient for the uses
below. The polynomial node supplies the Appell convention and identities;
its factorial upper estimate alone is not used to conclude the equivalence.

The forward direction uses the assumed uniform scalar Poincare inequality,
isotropy, log-concavity and the regularity of the coefficient test class.
The reverse uses one constant $A$ simultaneously for every degree and
regular isotropic measure, each fixed measure's strictly positive curvature,
and the analytic approximation and scalar stability statements. No uniform
curvature bound across approximants is used. No unstated or dispensable
hypothesis was identified. The node has no `bounded_by` edges. Its explicit
discussion respects the relative-strength and projection limitations:
the criterion concerns every symmetric tensor and has the strength of KLS.

### Line-by-line mathematical check

1. For a symmetric $k$-tensor, differentiation of the formal generating
   identity yields $\partial_iP_k[T]=kP_{k-1}[T_i]$ with no change of tensor
   normalization. Summing the squared norms of $T_i$ counts each ordered
   entry of $T$ exactly once. For $k\ge2$, the derivative polynomials
   have zero mean, so their second moments equal their variances. Strong
   convexity gives the integrability needed for the polynomial tests.
2. Applying the assumed Poincare bound gives
   $K_k\le Ck^2K_{k-1}$. Isotropy gives $K_1=1$ exactly. Induction yields
   $K_k\le C^{k-1}(k!)^2$, hence $c_k\le C^{(k-1)/2}$. Linear tests
   imply $C\ge1$, so $A=\sqrt C$ proves the exponential assertion.
   This includes degree one without invoking a variance for the constant
   degree-zero polynomial.
3. Conversely, degree one forces $A\ge1$. The induction
   $k+1\le2^k$ gives $(k+1)^2\le4^k$. Thus with
   $R=\max\{4A,2^{40}\}$ the assumed estimate implies
   $c_k\le R^k/(k+1)^2$ for every degree simultaneously.
4. The curvature theorem applies with $\varepsilon=1$ and $\ell=1$.
   Isotropy supplies centering and covariance equal to the identity; all
   regularity hypotheses and the $R$ threshold hold. Its conclusion is
   $C_P(\nu)\le32R^2\max\{1,a_\nu^{-1/(d+1)}\}$ for each finite
   dyadic $d\ge2$.
5. Fixing $\nu$ fixes $a_\nu>0$. The infimum along these finite dyadic
   degrees is therefore $32R^2$. This is a scalar infimum, with no
   exchange of measure and degree limits and no convergence of inverse
   operators. Its value is independent of the fixed measure and dimension.
6. For an arbitrary isotropic log-concave measure in a fixed dimension,
   the analytic lemma supplies regular isotropic approximants. Every
   approximant satisfies the same scalar bound already obtained. Isotropy
   precludes lower-dimensional support, so the limiting log-concave law
   has a density. The scalar stability clause then applies to all the
   stated locally Lipschitz finite-energy tests, and also provides their
   square integrability. It proves the claimed quantitative converse.

There are no unchecked proof steps. The only source comparison needed here
is the exact interface of the previously reviewed dependencies. In
particular, the fresh Song--Zhang Section 5 source proof was independently
checked in `research/reviews/2026-10-03-sz-curvature-review.md`; this dossier
does not introduce a further preprint import or invoke its final theorem.

The fingerprint command completed successfully and printed the block above.
The full `UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py` run during
this review completed with exit code zero and built this unchanged dossier
without MyST errors. Its content hash was checked again after the curvature
dependency's ledger transition. Moving the canonical statement to module 32
did not change its fingerprint; the moved statement was reread.

## Corrections

None.

## Exclusions

Neither assertion in the equivalence is established unconditionally. This
review does not certify KLS, exponential coefficient growth, the iterated
curvature theorem, the final localization transfer, or the Song--Zhang
all-law estimate. There is no CMH or occupation conclusion. In particular,
degree-dependent constants and constants chosen separately at each
iteration depth do not satisfy the exponential-growth assertion.

## Certification delta

Set `prop:sz-exponential-coefficients-equivalence` to `proved`, retain
`depends_on: [lem:sz-analytic-foundations, thm:sz-polynomial-variance,
thm:sz-curvature-comparison]`, and add the following proof record. No
`assumes: conj:kls` edge is appropriate: the proved object is the
equivalence itself. No transition of `conj:kls` follows.

```yaml
proofs:
  - artifact: solutions/prop-sz-exponential-coefficients-equivalence.md
    review: research/reviews/2026-10-03-sz-exponential-equivalence-review.md
```
