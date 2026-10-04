---
---

# Finite-depth bootstrap and a reusable curvature transfer

## Question examined

On `ap:polynomial-curvature-audit`, reconstruct Sections 6–7 of
Song–Zhang arXiv:2610.01447v1, proving `thm:sz-iterated-curvature`,
`thm:song-zhang-kls`, and `cor:sz-affine-poincare` from the polynomial and
curvature comparisons. The starting lens was **prove**, unchanged.
Extract the more general implication `thm:sz-curvature-transfer` established
by the same Gaussian posterior argument.

## What we learned

- *Established (written argument, not independently certified):* the affine
  profile extension uses $M=A+\delta B^{-1}$ and matrix inversion, without
  commuting $A$ and $B$. A continuous regular profile extends to nonsmooth
  strongly log-concave posteriors, and the posterior tower property keeps the
  earlier covariance correlated with terminal derivative products.
- *Established (written argument, not independently certified):* a coarse
  polynomial induction supplies an initial curvature profile at every fixed
  depth. Retaining zero initial conditions in the derivative hierarchy removes
  the fixed loss in the refined coefficient feedback. The logarithmic
  contraction bound eliminates degree from the large-depth error estimate;
  small degrees are initialized separately using the universal polynomial bound.
- *Established (written argument, not independently certified):* both growing
  admissibility thresholds are paid by choosing one sufficiently large
  initial constant at a fixed universal depth. The exponentially growing
  sequence then satisfies all subsequent hypotheses, and the remaining
  multiplicative losses have bounded product. This explicitly separates the
  summability statement from the admissibility statement.
- *Established (written argument, not independently certified):* Letwin's
  quadratic bound yields a matrix quadratic-variation estimate and the
  covariance exit probability for Gaussian observations. The established
  bounded Lipschitz witness theorem supplies global control on exceptional
  paths. One posterior both retains variance and has controlled covariance.
- *Established (written argument, not independently certified):*
  `thm:sz-curvature-transfer` needs no continuity or monotonicity of its
  function $F$. Its proof evaluates $F$ at one prescribed admissible lower
  curvature bound, then passes the identical scalar inequality through a
  regular isotropic approximation. This is stronger than the special profile
  application needed for the iterated-logarithm result.
- *Established (written argument, not independently certified):* the ordinary
  logarithm stopping rule supplies a finite depth in each dimension, while
  the constants have already been bounded uniformly over every finite depth.
  Whitening gives the exact covariance operator factor in the affine result.

The complete arguments are in `solutions/thm-sz-iterated-curvature.md` and
`solutions/thm-song-zhang-kls.md`. Classical external inputs are the matrix
Brascamp–Lieb inequality and the bounded-witness/Cheeger comparison from
`KLnotes`; the source proof of the latter was checked separately from the
new preprint.

## What resists

These arguments do not produce bounded profile constants over all depths.
The explicit admissibility thresholds still exclude inserting a bounded
sequence into the written induction. The generic transfer is a proved-form
implication only after review, and needs an actual curvature profile as its
premise. The particular profile reconstructed here yields dimension-dependent
bounds, not CMH, sharp gate zero, or universal-time occupation estimates.
No identified mathematical gap remains in the written reconstructions;
independent review of the complete dependency chain remains necessary.

## Proposed next step

Have a fresh reviewer examine both dossiers and their canonical statements.
For the iteration, inspect the nonsmooth affine profile extension, the
simultaneous induction over all laws, the terminal conditional-expectation
identity, the uniform degree/depth estimate, small-degree initialization and
all thresholds before each application. For the transfer, inspect the
published bounded witness, posterior likelihood and stochastic integrability,
trace-exponential Hessian estimate, stopped variance calculation, fixed-argument
use of $F$, all-law approximation and affine pullback. Review prerequisites
before making any unconditional theorem status transition. Then apply the
reusable transfer only to genuinely established profiles.
