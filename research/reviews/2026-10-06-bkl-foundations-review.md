---
verdict: pass
authors:
  - plan_import (researcher), unknown, 2026-10-06
reviewer: reviewer, gpt-6-astra, 2026-10-06
fingerprints:
  solutions/bkl-analytic-foundations.md: 8f4988de1c782dd2d5c085cd8508084789f3264fce198180065865e253e3d4f0
  lem:bkl-analytic-foundations: 7657fb2bb9597db83ab252a2b5ba773b834bf96f7d71f6cc27377648b7e2314d
  def:bkl-tilt-cumulants: 43636c8506cef53a8ed43a8231a955e160d704cc899cc248c5e08425ab5f449c
  lem:sz-analytic-foundations: e3b0250c18499cbdf58b3cb609937032b0101d8aa096aac355555309e5e94d3f
  lem:bkl-tensor-symmetrization: c662cf2f521aea0cf8f48cc2d00a7022f9af1935edbe171e98b8c7f3963c0f1a
---

# Independent review of the BKL analytic and tensor foundations

## Findings

Pass for both `lem:bkl-analytic-foundations` and
`lem:bkl-tensor-symmetrization`. This reviewer was launched in a fresh
context with paths and a review assignment, without the authoring
conversation. Both dossier theorems imply their canonical statements,
including all-moment approximation and the sharper binomial recovery
constant. The definition of regularity agrees exactly.

The actual proof of Section 2, including Lemmas 2.1 and 2.2, of
[BKL, arXiv:2610.05474v1](https://arxiv.org/html/2610.05474v1#S2)
was read alongside the reconstruction. Its analytic assertions are not
accepted merely on the authority of that new preprint. The local proof
supplies a weak eigenfunction barrier and a compact-support approximation
argument. The already certified `lem:sz-analytic-foundations` supplies
the graph core, form domain, compact resolvent, Bochner identity and
scalar stability. Its exact canonical scope and certification were
checked; its Gaussian-convolution calculation was also inspected.
No open dependency or assumed KLS bound enters either proof.

Steps checked:

1. Strong convexity supplies Gaussian integrability of every derivative
   occurring in the cutoffs. The gradient and drift terms have polynomial
   growth, so integration by parts has vanishing cutoff errors. Membership
   in the operator domain follows from the weak identity and the form
   domain; the certified Bochner identity consequently applies.
2. For the eigenfunction barrier, the sign in the transformed equation is
   correct: its zeroth-order term is `-Lw/w-lambda`. The quotient belongs
   to the weighted Sobolev space since the logarithmic gradient of `w`
   is bounded. Taking a positive constant above the quotient on a ball
   places the positive-part test entirely where that term is uniformly
   positive. The cutoff error is bounded by the weighted square norm
   divided by the squared radius. Exhaustion therefore kills the positive
   part. Applying the argument to both signs proves polynomial growth;
   no pointwise boundary condition at infinity was assumed.
3. On balls of radius `(1+|x|)^{-1}`, the rescaled drift and its first
   derivatives are bounded. The usual local gradient estimate for the
   Laplacian with bounded smooth drift and bounded forcing applies.
   Differentiating the equation introduces derivatives of the solution
   only through the order already controlled. Polynomial bounds on the
   coefficient derivatives and the reciprocal radius close the induction
   at every finite order. No estimate uniform in dimension or order is
   required or claimed.
4. Spectral inversion is on the centered subspace. The inverse barrier
   uses a polynomial of degree exceeding that of the forcing. The positive
   part of `u-Cw` is in the form domain, vanishes on a ball and is dominated
   by `|u|`; its cutoff gradient estimate gives a globally constant positive
   part, necessarily zero. Repeating with the other sign and differentiating
   yields the claimed class membership. The energy identity, spectral norm
   bound, uniqueness and centered-gradient contraction give every part of
   (A1). Direct sums establish precisely the finite tensor extension.
5. Conditioning on growing balls preserves log-concavity, and eventually
   preserves full dimensionality. All moments converge before centering
   and whitening. For a fixed compact intermediate law, logarithmic
   derivatives of its damped Laplace transform are finite cumulant
   polynomials of bounded variables, uniformly bounded in the tilt.
   Thus Gaussian convolution followed by a positive quadratic tilt has
   every required derivative bound. The Gaussian-convolution Hessian
   calculation gives the upper bound, and preserved log-concavity the
   lower bound before tilting. The diagonal choice controls finitely many
   moments and determining tests at each stage. Subsequent affine
   normalization tends to the identity, retaining every fixed moment.
   Only the scalar Poincare inequality passes to the weak limit.
6. In (A7), a pair of blocks with intersection size `r` has left
   coefficient `binom(d+r,r)` and right coefficient
   `sum_s binom(d,s)binom(r,s)`. Vandermonde makes these identical.
   Retaining the term of order `d` is legitimate because every summand
   is a squared Hilbert-space norm with nonnegative weight. Block
   symmetries make the tensors well-defined and make every left inner
   sum a permutation of the same symmetrized tensor. The two counts
   cancel, proving the binomial constant and then `4^d`. Extra slots are
   untouched throughout.

Hypotheses used are finite dimension; smooth potential; positive lower
and finite upper Hessian bounds; polynomial growth of every potential
derivative; centering of the forcing and inverse; isotropy and
log-concavity for approximation; and, for tensor recovery, the two exact
block symmetries and at least `3d` slots. These are all stated.
The tensor result needs no probabilistic hypothesis. No omitted
hypothesis or sharpening from an unused substantive hypothesis was found.

There are no ledger `bounded_by` edges for these nodes. The cited
projection warning is respected by full tensor recovery. The occupation,
relative-bound and profile warnings are not used as estimates.

The full `uv run --cache-dir /tmp/kls-plan-uv-cache scripts/check.py`
completed successfully with no MyST error. The fingerprint command was
run on the reviewed versions. All proof steps in this scope were verified.

## Corrections

None.

## Exclusions

This report does not certify the tilt criterion, the all-degree Taylor
premise, cumulant localization, suspension, KLS or conditional
initialization. It relies on the existing independent certification of
the SZ analytic node rather than issuing a new review of its entire
dossier. No stochastic or numerical claim is certified here.

## Proposed registration

Set both `lem:bkl-analytic-foundations` and
`lem:bkl-tensor-symmetrization` to `proved`, preserve their current
dependencies and references, and add to each:

```yaml
proofs:
  - artifact: solutions/bkl-analytic-foundations.md
    review: research/reviews/2026-10-06-bkl-foundations-review.md
```
