---
---

# Reconstructing the polynomial localization input

## Question examined

On `ap:polynomial-curvature-audit`, reconstruct source Sections 3–4 toward
`thm:song-zhang-kls`, starting with the prove lens. The output is the draft
`solutions/thm-sz-polynomial-variance.md` for `thm:sz-polynomial-variance` and
`lem:sz-analytic-foundations`. This checkpoint records arguments, not certification.

## What we learned

*Established:* the quadratic input `thm:letwin-qcts` bounds the operator square sum of
whitened third moments. The same bound prevents finite-time covariance collapse in
covariance-adapted localization through the logarithmic determinant. The support
bound and finite quadratic variation then prevent parameter explosion.

*Established:* the derivative hierarchy must retain the cross variation between the
conditional derivative mean and the covariance tensor metric. Its norm is bounded
using the operator square sum and weighted Bessel inequality, giving the stated
quadratic-degree hierarchy without any dimension factor. The factorial weights close
the finite induction. The terminal strong-convexity estimate uses a martingale tower
identity for the fixed gradient products, preserving correlation with past covariance.

*Established:* the full derivative-mean expansion is Appell, not an orthogonal-chaos
expansion. All tensor norms use ordered indices. Affine-support reduction extends
the estimate to singular centered covariance bounded by the identity.

*Established:* the analytic preparation needs two distinct limiting arguments:
polynomial moments for coefficient inequalities, and scalar weak Poincaré stability
for arbitrary finite-energy locally Lipschitz tests. Graph-core approximation and the
confining Schrödinger transform justify all inverse-operator domain claims at a fixed
regular measure. No uniform regularization curvature is required.

## What resists

There is no unclosed step asserted in this block, but it remains unreviewed. The
polynomial constants grow with degree, so this block alone does not imply a universal
Poincaré bound and discharges no occupation, CMH, or trace-upgrade target. Source
Sections 5–7 and their simultaneous degree/depth admissibility remain separate work.

## Proposed next step

Independently certify both canonical nodes against the draft dossier, with particular
attention to global SDE continuation, removal of stopping times in the tensor drift,
the full tensor cross variation, and the terminal martingale tower calculation.
Check the operator-domain and scalar approximation claims independently. Then use
these precisely stated inputs in the curvature comparison and finite-depth iteration.
