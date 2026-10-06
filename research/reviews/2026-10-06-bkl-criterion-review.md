---
verdict: pass
authors:
  - plan_import (researcher), unknown, 2026-10-06
reviewer: reviewer, gpt-6-astra, 2026-10-06
fingerprints:
  solutions/bkl-tilt-criterion.md: bb340d9e2feb1c11185348bba1fdb65e686040d414f0e46e5d1c93cf71d385db
  thm:bkl-tilt-criterion: 050f47b3ff5487f31a0b08990786dee5bef2a5ce39b8c85bb5982ea1410ab344
  def:bkl-tilt-cumulants: 43636c8506cef53a8ed43a8231a955e160d704cc899cc248c5e08425ab5f449c
  lem:bkl-analytic-foundations: 7657fb2bb9597db83ab252a2b5ba773b834bf96f7d71f6cc27377648b7e2314d
  lem:bkl-tensor-symmetrization: c662cf2f521aea0cf8f48cc2d00a7022f9af1935edbe171e98b8c7f3963c0f1a
  prop:bkl-tilt-appell-duality: 200cfcdd5bc5aed9562b945189b1ccd942730024ac955f0988db40841d86755e
  thm:sz-polynomial-variance: ffd52798e616ccd22bb3e4c78d5c382fd5657d3b598e6e4ec3c9afc4f696da8e
---

# Independent review of the tilt criterion and Appell duality

## Findings

Pass for `thm:bkl-tilt-criterion` and `prop:bkl-tilt-appell-duality`.
The dossier implies both canonical statements with their exact
quantifiers and full ordered-index Hilbert--Schmidt conventions.
This is a full independent review in a fresh context, without the
authoring conversation. The author identity was supplied by the mission
and appears in the dossier. The review reconstructed the argument from
the local proof, statements, ledger and versioned source.

The proof in [BKL v1, Section 3](https://arxiv.org/html/2610.05474v1#S3),
including Theorem 3.1 and Lemmas 3.2--3.9, was read and checked. The
local argument gives explicit constants at each absorption and addresses
zero successors. It is a reconstruction of the source proof, not a
deduction from the preprint's announcement. Foundations and tensor
recovery were independently reviewed in
`research/reviews/2026-10-06-bkl-foundations-review.md` and registered
proved before this report. All required dependencies are now defined or
proved. The SZ polynomial node supplies the Appell convention; its
quantitative variance bound is not used.

### Spectral sequence and defects

The certified foundations give a real centered unit eigenfunction in
the polynomial-growth class and the componentwise inverse on centered
inputs. The denominator defining each positive normalization is
nonzero by uniqueness of that inverse. A vanishing centered gradient
is handled explicitly, so no division by a zero normalization occurs.
The inverse energy bound gives the lower normalization bound. The
normalization preserves exactly the centered-gradient energy, yielding
the nonnegative losses (T3).

The index conventions in the integration by parts preceding (T5) agree:
the Hessian is the gradient of the centered gradient. Its scalar
product with the next gradient is the normalization times the latter's
squared norm. Expanding the defect and applying Bochner gives (T5),
including the positive curvature term. Finite telescoping then gives
both budgets and summability of the gradient energies. This proves
existence of the exit index without a uniform curvature assumption.
Before that index, the next gradient energy is at least half the initial
one, giving exactly the upper normalization bound `2 lambda` in (T7).
The possible case `N=1` is covered by the empty-sum conventions.

Centering the Hessian defect is an orthogonal projection. A tensor at
distance `e` from a tensor fixed by a transposition has transposition
displacement at most `2e`. For later slots, inverse centered
differentiation shifts the transposition one slot toward the front;
its norm on the relevant prefix is at most the square root of two.
The iteration therefore gives precisely the index `i-ell` and factor
`2^(ell+1)` of (T10). Telescoping a product of adjacent exchanges uses
only isometries on the unpermuted displacements. Its squared cost is
bounded by `q^4` times their sum, and `q^4 <= 16^q` gives (T11).

### Taylor transfer, tensor recovery and finite summation

Gaussian tails and Cauchy--Schwarz justify differentiation of the tilt
average for arbitrary square-integrable tests. Integration by parts
under a tilt gives the sign in (T12). Exactly one derivative lands on
the explicit tilt coordinate; dividing by `(d+1)!` leaves precisely
symmetrization of the normalized order-`d` Taylor tensor. There is no
missing factor of `d+1`.

Successive symmetrizations absorb their subgroups, proving (T14).
When `2d <= i <= N`, every normalization used has index between 2 and
N. The auxiliary tensor in (T16) has `d` Taylor slots and at least
`2d` symmetric input slots. Thus it satisfies both hypotheses of the
certified tensor recovery lemma. Applying the scalar Taylor premise
componentwise loses no dimension factor. The triangle inequality and
the contraction of symmetrization give (T17); the displayed coefficient
estimates are valid with `C_0 = 2^17`, including degree one.

The first loss is bounded using the coordinate test of the eigenfunction
equation and the covariance upper bound, not a trace bound. All later
losses use (T12) and the normalization bound. In the sum defining `S_d`,
there are at most `2d-1` small-index terms. The remaining higher-order
terms form a sub-sum of `S_(2d)`, and every defect is counted at most
`2d` times. This proves (T19) for all degrees, including empty sums.

Multiplication by `(C_0 lambda)^(d-1)` aligns the higher-degree term
exactly with the next dyadic left side. At a finite dyadic degree at
least N, the terminal sum is zero. Under the contradictory small-gap
assumption the error series is at most `400/9801 < 1/20`. Together
with `lambda <= 1/100`, this bounds the total loss below half the
initial energy, contradicting (T8). Hence the proof supplies the
universal constant `100 C_0^2`. No infinite spectral iteration is
interchanged with a measure approximation.

### Appell duality

For a full-dimensional log-concave law, a bounded convex superlevel
set and log-concavity along rays give an exponential tail, hence an
exponential radial moment of some positive order. This justifies all
fixed-order differentiated integrals near zero by Cauchy--Schwarz.
The normalized exponential generating function agrees with the
canonical Appell convention, so its derivative tensor is exactly the
Appell tensor. Pairing and integration give (T20) for every symmetric
tensor and every square-integrable test. Positive-degree Appell
polynomials have mean zero, by differentiating the constant normalized
integral.

The adjoint of the map taking `T` to `P_d[T]/d!` is consequently
the Taylor map into the full symmetric tensor space. Equality of
operator and adjoint norms proves (T21). No rank-one restriction,
additional factorial, covariance bound or centering assumption is
inserted into this proposition. Its proof needs only a local exponential
moment; log-concavity is a sufficient stated hypothesis for that fact,
and a possible broader formulation is not needed for certification.

### Hypotheses, fences and build

The criterion uses the specified smooth regular class, positive
curvature at the fixed measure, the covariance upper bound, `R >= 1`,
and one Taylor constant simultaneously for every degree and every
square-integrable scalar test. Centering is the declared normalization
for the coordinate estimate. The duality uses finite dimension,
full dimensionality and log-concavity to obtain the exponential moment,
integer positive degree, symmetric tensors and square-integrable tests.
No unstated hypothesis was found. Neither theorem assumes the
unconditional Taylor bound as already proved; it remains the explicit
premise of the criterion.

No `bounded_by` edges are present. The projection warning is respected
by recovering full tensors, while the cited covariance-occupation and
profile warnings supply no input and are not contradicted. The full
`uv run --cache-dir /tmp/kls-plan-uv-cache scripts/check.py` passed
after foundations registration, with no MyST error. Fingerprints are
the checker's output for the versions read; subsequent manuscript
exposition was inspected and left the canonical statements unchanged.
All steps in this scope were verified.

## Corrections

None in either proof or canonical statement.

## Exclusions

This report does not establish the all-degree Taylor premise,
cumulant bounds, stochastic localization, suspension, KLS or uniform
conditional initialization. It does not recertify the SZ polynomial
variance estimate. The surrounding manuscript is not subjected to a
complete synchronization audit by this report.

## Proposed registration

Set both `thm:bkl-tilt-criterion` and `prop:bkl-tilt-appell-duality`
to `proved`, preserving their current references and dependencies, and
add to each:

```yaml
proofs:
  - artifact: solutions/bkl-tilt-criterion.md
    review: research/reviews/2026-10-06-bkl-criterion-review.md
```
