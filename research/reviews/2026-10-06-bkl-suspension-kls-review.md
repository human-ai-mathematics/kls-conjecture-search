---
verdict: pass
authors:
  - bkl_suspension_author, gpt-6-astra, 2026-10-06
reviewer: reviewer, gpt-6-astra, 2026-10-06
fingerprints:
  solutions/bkl-suspension-kls.md: dc4bcc0cfacfcb4a77548af89df6247179cc497ee2f7fb32ed398eb6f2d02b99
  prop:bkl-suspension: e63452cb08c1c930757ec5b8733c971f652626daf45e0ccbc3c9fbe292be084e
  def:bkl-tilt-cumulants: 43636c8506cef53a8ed43a8231a955e160d704cc899cc248c5e08425ab5f449c
  thm:bkl-tilt-bound: b14ed0af1b0f660928c9d507b8567b89ff97bbbd8620a138eba3fecf5aadf82f
  thm:bkl-cumulant-bound: f494b6a9fe460588d0b885054be670483c49ffb759e6239e6f9b3651303ce275
  lem:bkl-analytic-foundations: 7657fb2bb9597db83ab252a2b5ba773b834bf96f7d71f6cc27377648b7e2314d
  prop:bkl-tilt-appell-duality: 200cfcdd5bc5aed9562b945189b1ccd942730024ac955f0988db40841d86755e
  conj:kls: b34221c5440f365f12cb6529324aed7a62b355236e5a037761de51f02adeab69
  thm:bkl-tilt-criterion: 050f47b3ff5487f31a0b08990786dee5bef2a5ce39b8c85bb5982ea1410ab344
---

# Suspension, uniform coefficients and the KLS composition

## Findings

Pass jointly for `prop:bkl-suspension`, `thm:bkl-tilt-bound` and
`conj:kls`. Each dossier theorem implies its canonical statement,
including singular covariance contractions for the coefficient bound
and locally Lipschitz finite-energy tests for KLS. The three results
are proved in order in the same dossier; their currently open internal
dependencies are not assumed. Register all three together, or in that
order. Every external proof dependency is already proved or defined.

The reviewer began in a fresh context without authoring history and has
only reviewed, never authored or directed, these dossiers. The source
read in full was [BKL v1, Section 7](https://arxiv.org/html/2610.05474v1#S7),
Proposition 7.1 and the proof of Theorem 1.1. The local source HTML has
SHA-256 `fb51ab0d94171ac7de2a3009efb5249e44ee66de5c9a1dc5899bdb843de29df9`.
The local reconstruction supplies the density, moment and singular-support
arguments needed for its somewhat wider coefficient statement.

### Suspension proof

1. The normalized smooth test is orthogonal to all affine functions.
   Independence gives variance one for its normalized sum, and the
   independent Laplace variable has mean zero and variance `2/beta^2`.
   The stated division therefore makes the added coordinate have variance
   one. Its cross covariance with each original coordinate is zero.
   All covariance blocks of the enlarged law are exactly those of the
   identity matrix, with no missing scaling or independence assertion.
2. The displayed joint density includes only a constant Jacobian from
   the added coordinate. Its potential is the maximum of two functions
   whose Hessians in each original block are positive semidefinite
   whenever the stated integer N is chosen. Both are affine in the new
   coordinate. Thus the potential is convex, including across the cusp
   of the absolute value. Smoothness of the enlarged law is not needed:
   the premise applies to every isotropic log-concave law.
3. Bounded Hessian of the test bounds its growth quadratically. Positive
   curvature of the original measure absorbs its sufficiently small
   exponential perturbations. Together with the open interval of
   Laplace integrability of the added noise this justifies the joint
   transform and every fixed derivative near zero. The first derivative
   in the added coordinate is the stated sum of tilted averages;
   the noise's first derivative vanishes by centering.
4. The further derivatives vanish when they use different replication
   blocks. Within one block, their coefficient is exactly `d!` divided
   by `sigma_beta sqrt(N)`. There are N disjoint ordered-index tensor
   supports, and entries containing another added-coordinate index
   are orthogonal to them. Squaring the norm therefore cancels N,
   giving the asserted lower bound for the full directional cumulant.
   The premise is applied in dimension `N n+1`, which is why its
   dimension-uniform quantifier is essential. For every beta one can
   choose an integer N; taking the infimum of the resulting numerical
   bounds needs no convergence of the enlarged measures.
5. Each entry of the Taylor map is pairing with a fixed polynomial in
   the original variable, so it defines a continuous functional on
   `L^2` at this fixed measure and degree. The finite tensor map is
   continuous as well. Compact smooth approximations are dense because
   the original density is smooth and positive. The explicit affine
   projection is the orthogonal projection by isotropy. Subtracting it
   does not change a Hessian; normalizing the projected approximants
   preserves bounded Hessian and their convergence. This verifies the
   passage to every affine-orthogonal test without assuming a uniform
   Taylor bound in the density step.
6. The linear component is controlled by the same cumulant premise at
   the original law and the exact derivative of its log Laplace
   transform. The constant component contributes zero. Orthogonality
   of constant, linear and residual parts, followed by the two-term
   Cauchy--Schwarz inequality, gives precisely the factor 2 in the
   squared conclusion. No unwarranted orthogonality of their Taylor
   images is asserted.

The implication uses isotropy, the positive smooth regular density and
its positive curvature, finite dimension, a positive cumulant constant
uniform over all dimensions and laws, and the specified degree. Bounded
test Hessian and affine orthogonality are temporary restrictions removed
by the argument. Higher polynomial-growth requirements on the potential
are part of the declared regular class but are stronger than this
suspension argument alone needs. No unstated hypothesis was found.

### Uniform coefficients and all-law extensions

At every degree at least two, substituting the certified cumulant
estimate with order `d+1` gives `2 K^d`, which is bounded by `(2K)^d`.
Degree one is supplied directly by the covariance identity and scalar
duality, with no dimension factor. The same base `sqrt(2K)` works for
all degrees and every regular isotropic law.

The Appell generating identity has constant term one in its denominator.
Formal inversion therefore makes every degree-d coefficient a polynomial
in moments through degree d. Its contraction with a fixed tensor is a
polynomial of degree at most d; its square requires moments only through
degree `2d`. The certified all-moment regular approximation consequently
passes each fixed-tensor variance inequality to an arbitrary isotropic
law. The supremum is taken only after this inequality holds for every
fixed tensor; no limit of suprema or of tests in changing `L^2` spaces
is taken. Positive-degree Appell polynomials have mean zero. The exact
adjoint identity from `prop:bkl-tilt-appell-duality`, also reproduced
locally, returns the claimed operator norm bound for all tests.

For a covariance contraction, centering puts the law on the range of
its covariance. On that range the inverse square root exists. Whitening
there gives an isotropic law, and the map back has operator norm at most
one. The chain rule transforms the Taylor tensor by its d-fold tensor
power, whose Hilbert--Schmidt operator norm is the dth power of that
operator norm. This proves the ambient estimate, including directions
normal to the support. Rank zero is treated separately and has all
positive-degree coefficients zero. Exponential moments on the support
justify the ambient derivatives for arbitrary `L^2` tests. The same
polynomial adjoint identity also gives the claimed coefficient
equivalence in this singular case.

### Composition audit and KLS

The following audit uses the existing independent certifications at
their stated scope. It does not replace them with assertions from an
author's narrative.

| Interface | Evidence and exact use |
| --- | --- |
| Quadratic variance and third cumulants | `2026-10-01-letwin-imports-r2-review.md` certifies the all-law quadratic estimate with constant 8; `2026-10-01-letwin-covariance-windows-review.md` certifies its Cauchy--Schwarz third-moment consequence. The latter's explicit antecedent is discharged by the former. Their canonical statements and ledger edges agree. |
| Cumulant dynamics | `2026-10-06-bkl-dynamics-review.md` certifies global finite-time covariance invertibility and genuine bounded-time martingales for compact initial laws. Its bounds are dimension dependent only where used to justify operations, and assume no high-order uniform bound. |
| Energy and induction | `2026-10-06-bkl-energy-review.md` retains both integrability hypotheses. `2026-10-06-bkl-cumulants-review.md` certifies their discharge by the stronger induction and the all-moment removal of compact support. Its one universal K precedes all dimension, law, order and vector quantifiers. |
| Analytic and tensor foundations | `2026-10-06-bkl-foundations-review.md` certifies the inverse and eigenfunction at each fixed regular measure, full tensor recovery, regular approximation and scalar stability. No uniform spectral gap is an input. |
| Spectral criterion and normalization | `2026-10-06-bkl-criterion-review.md` certifies the implication from one simultaneous all-degree Taylor bound and its exact full-tensor Appell normalization. It does not assume that bound unconditionally. |
| Suspension and composition | The present proof establishes the suspension implication, discharges its premise using the all-law cumulant theorem, and supplies the resulting single Taylor base to the criterion. |

The accepted upstream statements were read along with these reports.
The certified Letwin chain rests on the established compact-target
moment-map input, not on a general KLS theorem. The SZ analytic input
and Appell convention introduce no general KLS premise either. Thus
the chain has no circular use of its conclusion, no open external
dependency and no undischarged antecedent.

For regular isotropic measures the criterion applies with
`R = sqrt(2K) >= 1`, so the Poincare constant is at most `2 C K`,
with C and K universal. For arbitrary isotropic log-concave laws,
the approximants remain isotropic and have the same bound. Weak
convergence passes the inequality for compact smooth tests because
the test, its square and its gradient square are bounded continuous.
The certified scalar stability assertion extends it to locally
Lipschitz finite-energy tests, including their square integrability.
Infinite energy supplies no additional finite-bound assertion.
This is the canonical Poincare claim with the required order of
quantifiers and one dimension-independent constant.

The canonical statement also records equivalence with uniform positive
Cheeger constants. The established comparison in `eq:cheeger-two-sided`
was checked against the actual published
[Klartag 2023 paper, equation (1.4), page 3](https://arxiv.org/pdf/2303.14938),
whose reciprocal-isoperimetric normalization agrees with the manuscript.
It supplies both directions with universal constants for log-concave
laws. This background equivalence requires no new KLS input.

### Fences and validation

None of these three nodes has a `bounded_by` edge. Full tensor norms
respect the projection warning. No moving-profile estimate, occupation
bound, covariance-time converse or CMH premise is inserted. The brief's
dimension-uniform target is met by the single constant above; its
warnings do not assert a converse from KLS to the structural premises.

The full `uv run --cache-dir /tmp/kls-plan-uv-cache scripts/check.py`
completed with exit 0 and no MyST errors. The fingerprints above are
the actual output for this dossier and its required canonical statements.
All steps in this scope were verified; no unavailable source remains.

## Corrections

None.

## Exclusions

This review relies on, rather than recertifies, the full proofs covered
by the upstream reports named above. It certifies their logical
composition with the suspension dossier and the three named conclusions.
It does not certify conditional initialization, a BKL-independent
Song--Zhang argument, sharp CMH or gate-zero inequalities, occupation
or conditional-fiber assumptions, or any route closure. Certification
here is not a claim of journal refereeing of BKL v1.

## Proposed registration

Set `prop:bkl-suspension`, `thm:bkl-tilt-bound` and `conj:kls` to
`proved` in dependency order or atomically, preserving their existing
references and dependencies. Add to each:

```yaml
proofs:
  - artifact: solutions/bkl-suspension-kls.md
    review: research/reviews/2026-10-06-bkl-suspension-kls-review.md
```

No other status or route transition follows from this report.
