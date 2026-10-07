---
---

# Reconstruction of the BKL cumulant mechanism

## Question examined

On `ap:bkl-reconstruction`, reconstruct Sections 4–6 of Bizeul–Klartag–Lehec,
arXiv:2610.05474v1, for `lem:bkl-cumulant-dynamics`,
`lem:bkl-cumulant-energy` and `thm:bkl-cumulant-bound`. The mission is a proof
reconstruction, not a certification or a new route to `conj:kls`.

Author: plan_framework researcher, unknown, 2026-10-06.

## What we learned

**Established in draft arguments, not certified:** three dossiers now give the
full algebra and probability arguments:

- `solutions/bkl-cumulant-dynamics.md`: inverse-covariance localization,
  posterior density equation, covariance decay, cumulant SDE and third-order
  matrix control. Its external mathematical input is `prop:letwin-kappa` with
  its antecedent discharged by `thm:letwin-qcts`.
- `solutions/bkl-cumulant-energy.md`: the exact inverse-metric Itô expansion,
  its drift bound and the integrated next-order energy estimate.
- `solutions/bkl-cumulant-bound.md`: the simultaneous static/integrated
  induction and passage from compactly supported to arbitrary isotropic
  log-concave laws by conditional truncation and covariance normalization.

The following details are written explicitly because they carry the transition
from formal SDE algebra to a bound on expectations:

1. The third-order matrix inequality bounds the drift and quadratic variation
   of the logarithmic determinant of the covariance. Together with compact
   support, this prevents finite-time degeneration and explosion of the
   parameter SDE.
2. Crude fixed-dimension cumulant bounds follow from one-dimensional
   log-concave marginal tails and the moment-cumulant formula. They bound
   whitened energies on finite intervals and make the local martingale terms
   true square-integrable martingales. These constants never enter the
   dimension-free induction.
3. The infinite-time limit uses a deterministic sequence of terminal times
   along which the expected energy tends to zero. Integrability alone does
   not assert convergence along every time.
4. The coupled induction starts at order two with the bound
   $1+\frac12\int_0^\infty\mathbb E\mathcal E_3(t)\,dt\le5$.
   The split contraction uses a time-integrated estimate for the factor
   containing the distinguished vector and a pointwise estimate for the other
   factor. Their factorials cancel the subset coefficient exactly.
5. Noncompact approximation takes limits only in finite-order static moments;
   no convergence of stochastic localization processes is claimed or needed.

The resulting all-order theorem has the source's exact quantifiers: one
universal constant for every dimension, every isotropic log-concave law,
every cumulant order at least two and every distinguished vector.

**Structural verification:** the fast checker passes. After correcting a
control character in a displayed formula, the complete checker
`uv run --cache-dir /tmp/kls-plan-uv-cache scripts/check.py --impact` exits
successfully and reports no changed certified items. This is structural
validation, not proof validation.

## What resists

No unresolved mathematical step is asserted in these drafts. Their validity
requires an independent reviewer; the author does not issue a verdict.
There are no assigned `bounded_by` fences for these three new nodes. The
construction's compact-support restriction is retained until the last static
approximation argument. The Riccati covariance clock is not substituted for
the inverse-covariance process.

## Proposed next step

A cold reviewer should read all three dossiers and the canonical statements
of `def:bkl-tilt-cumulants`, `lem:bkl-cumulant-dynamics`,
`lem:bkl-cumulant-energy`, and `thm:bkl-cumulant-bound`, together with the
certified Letwin inputs. Particular audit points are nonexplosion, removal of
stops in expectations, the order ranges of the two induction factors, and
moment convergence after covariance normalization. The stronger integrability
conclusions in the dynamics dossier are used in the energy dossier and must
be included in the scope of that review. No ledger or portfolio transition
is proposed before this review.
