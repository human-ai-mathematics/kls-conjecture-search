---
---

# What the polynomial–curvature mechanism adds to the framework

## Question examined

With the mine lens, extract a reusable interface or exact criterion from
`thm:sz-polynomial-variance`, `thm:sz-curvature-comparison` and
`thm:song-zhang-kls`, beyond restating the final dimension-dependent bound.
This continues `ap:polynomial-curvature-audit`. It does not register a new approach.

## What we learned

*Established:* `solutions/prop-sz-exponential-coefficients-equivalence.md` gives an
exact equivalence between KLS and a universal exponential bound for the Appell
coefficients, already when the coefficient condition is tested only on regular
isotropic laws. The forward direction is the derivative recursion for Appell
polynomials; the reverse uses a constant profile in the polynomial–curvature
comparison, followed by arbitrarily large finite dyadic degrees at one fixed regular
measure and then scalar Poincaré approximation. The canonical proposed node is
`prop:sz-exponential-coefficients-equivalence`.

*Established:* the quantifier order matters. The exponential base must be uniform
in degree, measure, dimension and regularization parameters. A coefficient bound at
every fixed degree is insufficient. In the reverse proof one takes the infimum over
degrees before removing regularity, so no uniform positive curvature of approximants
is required. This is an exact target reformulation, not independent evidence for KLS.

*Established:* the final localization mechanism also has a reusable interface,
`thm:sz-curvature-transfer`, proposed to the owner of the final source dossier:
a bound by an arbitrary positive curvature profile on all regular isotropic measures
transfers to general isotropic measures by evaluating the profile at a universal
multiple of the inverse dimension logarithm. No monotonicity or continuity of the
profile is required. Its proof uses the exact curvature lower bound of the selected
posterior and passes only a fixed scalar inequality through approximation. The final
proof owner handles its complete dossier, so this checkpoint is not a duplicate proof.

| Mechanism | Hypothesis and its actual use | Bottleneck |
|---|---|---|
| Appell derivative recursion | Universal Poincaré bound bounds every derivative energy; centering removes the zeroth Appell term | Requires the target itself in this direction |
| Constant-profile curvature comparison | One exponential base works at all degrees; positive curvature is fixed while taking the degree infimum | Proving a uniform exponential base is equivalent to KLS |
| Generic curvature transfer | A profile valid at every positive curvature applies to the selected posterior | The available covariance-controlled time is inverse logarithmic in dimension |

## What resists

The Song–Zhang iterated profiles do not produce a bounded exponential base uniform
in degree. Their depth constants and admissibility thresholds remain relevant; the
new equivalence does not bypass them. The transfer theorem still evaluates its
profile at a dimension-dependent curvature. Nothing here gives a universal-time
occupation estimate or an implication into CMH, and no sufficient-condition arrow
in the framework has been reversed.

## Proposed next step

Independently certify `prop:sz-exponential-coefficients-equivalence`, checking the
factorials and all quantifiers, after its comparison and analytic dependencies have
been reviewed. Expose `thm:sz-curvature-transfer` in the final proof dossier and
manuscript as a reusable interface. Treat the equivalence as an explicit target
criterion, not as a new independent approach. Any proposed coefficient improvement
must provide one base valid at all degrees before it could discharge that criterion.
