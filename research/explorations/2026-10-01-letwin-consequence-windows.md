---
---

# Letwin consequences: exact source loss and covariance windows

## Question examined

Prepare proofs for `cor:qcts-source`, `thm:covariance-bound`,
`cor:V2-implies`, `prop:letwin-kappa`, `cor:letwin-window`,
`cor:KI-letwin`, and `thm:V2-window`. This is a mine/prove mission on
the existing covariance and fixed-cut inputs, not a new portfolio route.

## What we learned

*Established, not certified.* Whitening gives the intrinsic two-color
estimate; unwhitening retains the square of the operator covariance norm.
The exact coarse-window correction gives the manuscript source constant.
The product proof uses only `lem:product-qcts` and the color identity.
Finite-time posteriors of isotropic laws have positive-definite covariance,
because their likelihoods are strictly positive on the initial support.
These arguments are in `solutions/letwin-source-consequences.md`.

*Observed from primary sources.* Klartag--Lehec, arXiv:2203.15551v2,
Corollary 5.4, has a time constant independent of the real moment exponent
and a moment constant depending only on that exponent. Its third-moment
parameter uses exactly the manuscript Hilbert--Schmidt normalization.
The notes arXiv:2406.01324v2, Theorem 61, instead give a supremum-over-time
tail on the shorter window. Their roles are kept separate.

*Established, not certified.* The third-moment bound follows by duality from
the quadratic input. The published fixed-time moments then yield the first-
and second-moment interfaces. A Gaussian observation coupling passes those
fixed-time moments from smooth positive laws to arbitrary isotropic
log-concave laws by Fatou, without convergence of entire localization paths.
These arguments are in `solutions/letwin-covariance-windows.md`.

*Observed from the statements.* Dimension one makes the printed logarithmic
denominators undefined. The orchestrator has restricted `cor:letwin-window`
and `thm:V2-window` to dimensions at least two, and `cor:KI-letwin` to
dimensions at least three as in `ass:KI`. The original conditional statements
retain their quadratic input in `assumes`; the two originally unconditional
corollaries retain proof dependencies on that input.

## What resists

The dossiers do not establish the Letwin source theorem themselves. The
unconditional corollaries must not acquire a proved status before their
source dependency is certified. The strengthened covariance window still
shrinks with dimension and establishes no universal-horizon Carleson
assumption. None of these deductions controls the missing cut-dependent
temporal alignment.

## Proposed next step

Review the two dossiers independently after stabilizing the upstream Letwin
certification. Check the source constants, product branch, dimension fences,
real moment exponent, fixed-time smoothing argument, and separation between
conditional antecedents and discharged dependencies. No route transition is
proposed by this checkpoint.
