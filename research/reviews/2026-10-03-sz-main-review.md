---
verdict: pass
authors:
  - researcher-curvature, gpt-6-astra, 2026-10-03
reviewer: reviewer, gpt-6-astra, 2026-10-03
fingerprints:
  solutions/thm-song-zhang-kls.md: f94b0504479ee59358fa4d7de2a36366ab2ae831685a5423918bf138cf4d5c73
  thm:sz-curvature-transfer: c65a989b9e3b583ef639f2c95d7a8b60a3c0355b8434b57685bef57c626f41a9
  lem:sz-analytic-foundations: e3b0250c18499cbdf58b3cb609937032b0101d8aa096aac355555309e5e94d3f
  thm:letwin-qcts: 8e2ac0819f46db553fe83a6f3034436816565262316c2e6bde7d81baead1a082
  thm:song-zhang-kls: 1176d9fa27f282a7e51177cbbf5e6f4efbccbfb3c7c103a53a9dc00df7cae830
  thm:sz-iterated-curvature: e1c597ce3da1e94ebc6e1fbde16ce86114991cd711e6eb3f7a9550bb161fdef8
  cor:sz-affine-poincare: 05e08a5fa93c6c076067c41ca0e905f76dce28c345514e7a2397f5a68911aa8e
---

# Gaussian transfer, all-depth bound and affine corollary: independent review

## Findings

The dossier proves `thm:sz-curvature-transfer`, `thm:song-zhang-kls`, and
`cor:sz-affine-poincare` as canonically stated in `modules/32-polynomial-curvature.md`
and `modules/00-overview.md`. This reviewer was launched without the authoring
conversation and has neither written nor directed these proofs. The assignment
supplied the author identity. The frozen dossier and actual source proofs were
read independently.

### Agreement, hypotheses and dependency order

The generic transfer preserves the exact quantifiers over arbitrary positive
finite-valued functions $F$, all dimensions, regular isotropic measures, and
every admissible lower curvature bound. It asserts neither continuity nor
monotonicity of $F$. Its antecedent is part of the universal implication, not
an unproved dependency. The main theorem has one pair of constants independent
of both dimension and finite depth, with the correct squared Poincare and
unsquared reciprocal-Cheeger powers. The affine assertion assumes positive
definite covariance and multiplies only the Poincare bounds by its operator norm.
The ordinary-log stopping convention agrees with the manuscript's $\log^*$.

Hypotheses used are isotropy, log-concavity, finite positive dimension and finite
integer depth; positive definite covariance in the affine assertion; and the
universally quantified profile hypothesis for transfer. Smoothness and both
Hessian bounds are used at regular approximants, not imposed on the final
law. Boundedness and the Lipschitz estimate for the witness are derived from
the published input. No unstated hypothesis or unused stated hypothesis was
identified.

The proof order is acyclic: the generic transfer uses certified
`lem:sz-analytic-foundations` and `thm:letwin-qcts`; the main result uses this
transfer and `thm:sz-iterated-curvature`, certified in
`research/reviews/2026-10-03-sz-iteration-review.md`; the affine corollary uses
the main result. The transfer and main result are proved earlier in this same
jointly reviewed dossier before they are used. Thus the batch has no open
external proof dependency. The established witness and Cheeger comparison
are recorded by `KLnotes`. No `bounded_by` edge occurs.

### Mathematical steps checked

1. The bounded $1$-Lipschitz witness has variance at least $c_1k/4$ by the
   stated direction of the Cheeger inequality. Centering and normalization
   give variance one, supremum at most $2\sqrt{C_1}$ and Lipschitz constant
   at most $2/\sqrt{c_1k}$. Clipping an essential bound is legitimate.
2. Multiplication of Gaussian increment likelihoods gives the endpoint
   posterior formula on cylinder sets and then on the observation filtration.
   Conditional Jensen supplies square integrability. The innovation is a
   continuous martingale with quadratic covariation $tI$, so it is Brownian.
   Gaussian tails justify the differentiated integrals around time zero.
3. The quotient Ito correction cancels the conditional-mean drift. The fourth
   moment bound on the covariance integrand removes the parameter stops.
   Applying the formula to coordinates and coordinate products gives the third
   central moment noise and drift $-A_t^2$ with the displayed sign. The
   posterior retains both Hessian bounds.
4. Whitening Letwin's quadratic bound and applying matrix duality gives
   $\|S_z\|_{\rm HS}^2\le8\|A\|_{\rm op}^2z^TAz$. Complete third-tensor
   symmetry gives the operator square sum, bounded by $64I$ before exit.
   There is no illicit bound on the full third-tensor Hilbert--Schmidt norm.
5. Diagonalization gives the logarithmic-mean coefficients of the trace
   exponential Hessian; convexity bounds them by arithmetic means, including
   repeated eigenvalues by continuity. Ito then gives compensator
   $32\theta^2t$. Nonnegative supermartingale stopping, optimization at
   $\theta=\rho/(64t)$, and the same argument for $-M$ give (8).
6. The upper covariance exit forces a martingale quadratic form at least one.
   For a lower exit, the accumulated drift is at most $4tI$, so its exit
   eigenvector gives at most $-1/2+4t\le-1/4$. Both exits are therefore
   covered by the stated probability bound, including the boundary time.
7. Stopped variance has derivative bounded below by minus twice its expected
   value. The global supremum bound controls the stopped exit contribution.
   The exact choice of $c_0$ yields probability at most $1/(8B_0^2)$, leaving
   expected variance at least $3/4$ on the no-exit event. Hence a realization
   with variance greater than $1/2$ exists; no measurable choice of such a
   realization is required.
8. Whitening that posterior gives curvature at least $t/2$ using the lower
   covariance bound, while the upper covariance bound gives witness energy at
   most $2B_0^2/k$. Thus $k\le4B_0^2F(t/2)$. The hypothesis is invoked at
   exactly this deterministic admissible lower bound, so no comparison of
   nearby values of $F$ is needed.
9. Every regular isotropic approximant has the same scalar bound with the
   same argument of $F$. Full-dimensional log-concave limits are absolutely
   continuous. Certified scalar stability extends the inequality and proves
   square integrability of all finite-energy locally Lipschitz tests. Neither
   spectral objects nor the profile are passed through a continuity argument.
10. Substitution of each finite-depth profile and its elementary scaling
    estimate gives (11) with constants independent of depth and dimension.
    The published comparison $\psi_\mu^2\le\pi C_P(\mu)$ and the supremum
    over isotropic laws give the reciprocal-Cheeger bound.
11. The shifted logarithm estimate applies at every ordinary iterate above
    four. The cases $m=0,1$ are covered by invariance of $[0,5]$ under $g$.
    The selected depth is at least one and at most $\log^*(n+2)$, retaining
    the factor $16^r$ and absorbing only the bounded logarithm factor.
12. The affine chain rule gives energy $\int\nabla f^T\Sigma\nabla f$,
    bounded by $\|\Sigma\|_{\rm op}$ times the original energy. The isotropic
    finite-energy test class applies and gives both asserted affine bounds.

### Sources and build

Section 7 and the witness normalization in Section 2 of
[Song--Zhang v1](https://arxiv.org/src/2610.01447v1) were checked directly in
`/tmp/kls-song-zhang-source/20_upper.tex` and `10_preli.tex`. This includes
the posterior construction, covariance exit proof and final transfer, rather
than only the imported theorem's statement. The generic-$F$ assertion follows
from the same proof with its curvature bound evaluated at the fixed argument.

The actual [Klartag--Lehec v2 source](https://arxiv.org/src/2406.01324v2),
`/tmp/kls-song-zhang-source/survey/lectures_IHP_v5.tex`, contains the bounded
witness in Theorem 20 and both explicit comparison constants after Corollary
21. The normalization used here follows from those statements. This is an
established publication in *Bulletin of the AMS* 62 (2025), 575--642, also
listed on [Lehec's author webpage](https://lehec.pages.math.cnrs.fr/website/).
Its classical theorem is an input, not a new-preprint claim requiring another
repository proof. Standard Ito and stopping tools are used in their usual
continuous finite-dimensional form, with the needed integrability verified
in the dossier; the trace exponential inequality is proved explicitly.

The full `UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py` passed
without MyST errors. The corrected frozen dossier was reread and fingerprinted;
the block above is the fingerprint command's output. No numerical artifact
was used as proof evidence.

## Corrections

None outstanding. The stochastic differential spacing, product spacing and
missing `\qquad` in the draft were corrected before fingerprinting.

## Exclusions

This report does not re-certify Letwin's proof, the analytic foundations, or
the iteration dossier, and it does not certify the exponential-coefficient
equivalence. It proves no dimension-free KLS bound, CMH statement, or
universal-time occupation estimate. No infinite-depth limit is taken. No
step within the stated scope remains unverified.

## Certification delta

Set the three reviewed nodes to `proved` as one closed dependency batch and
give each the following record:

```yaml
proofs:
  - artifact: solutions/thm-song-zhang-kls.md
    review: research/reviews/2026-10-03-sz-main-review.md
```

Retain the transfer's dependencies
`[lem:sz-analytic-foundations, thm:letwin-qcts]`, the main theorem's
`[thm:sz-curvature-transfer, thm:sz-iterated-curvature]`, and the affine
corollary's `[thm:song-zhang-kls]`. Retain existing references. No `assumes`
edge is needed for the universally quantified profile implication.
