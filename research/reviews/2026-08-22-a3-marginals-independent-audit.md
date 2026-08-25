---
type: proof-review
date: "2026-08-22"
verdict: pass
authors:
  - /root/a3
reviewer: /root/audit_latex
nodes:
  - obs:marginals-not-joint
solutions:
  - solutions/obs-marginals-not-joint.tex
---

# A3 fixed-marginal obstruction independent-agent audit

## Certified scope

The audit certifies the fixed-marginal counterexample in
[`solutions/obs-marginals-not-joint.tex`](../../solutions/obs-marginals-not-joint.tex): for every
$0<\varepsilon<1$ there is a positive, piecewise-smooth density on $\mathbb R^3$ with standard
Cauchy coordinate marginals whose joint weighted Poincaré constant in the diagonal
$1+x_j^2$ metric is $\Theta(\varepsilon^{-1})$. It also certifies the elementary degeneracy of a
coefficient-only Dirichlet form on a joint law with a nondegenerate scale marginal.

## Checks performed

The review checked normalization and positivity of the copula, its exactly uniform coordinate
marginals, the Cauchy-CDF pullback, and the angular test's $H^1$ admissibility at the common corner
in dimension three. It checked the reflection-symmetry mean, the uniform variance lower bound,
the fact that the gradient is supported in the $\varepsilon$-density mixed octants, and the
transformed weighted-energy estimate
$(1+x^2)p(x)^2\le\pi^{-2}$. It also checked smooth-test approximation with squared $H^1$ error
$o(\varepsilon)$ and the matching density-comparison upper bound. The coefficient-only claim was
checked by testing a bounded nonconstant function of the scale coordinates.

## Scope boundary and exclusions

The constructed density is positive almost everywhere and piecewise smooth; it is not asserted
to be a globally smooth copula. This fully refutes the unrestricted marginal-only claim as
stated. A theorem restricted to globally smooth copulas would require a separately reviewed
smoothing argument. The scale-degeneracy statement assumes a nondegenerate scale marginal.

This audit does not certify `thm:a3-product`, `prop:a3-hierarchical-prior`, the bounded-likelihood
corollary, or a positive posterior-specific lower bound on the block gap.
