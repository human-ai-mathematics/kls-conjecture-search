---
---

# BK localization and reverse transfer reconstruction

## Question examined

On route `ap:bk-reconstruction`, reconstruct `lem:bk-localization-covariance`,
`lem:bk-moving-appell-variance`, and `prop:bk-reverse-transfer` from BK source
commit `4837c33649ba2271f43c9684e9350ecbdd725f95`, Sections 6–7 and Appendix D.
The starting lens was prove. This record makes no review verdict.

## What we learned

*Established, uncertified.* The argument is written in
`solutions/lem-bk-localization-covariance.md` and
`solutions/prop-bk-reverse-transfer.md`.
The only inequality input to covariance control is `thm:letwin-qcts`.
Its third-tensor bound holds on the entire ordered tensor product, permitting
conditional time coalescence and the inverse accumulated-curvature bound.
The log-determinant argument gives pathwise continuation without requiring
an expected inverse-covariance bound.

*Established, uncertified.* The moving Appell drift separates the degree-one
lowering term and highest cumulant term before estimating intermediate terms.
Bessel's inequality controls the highest cumulant by the moving variance
itself; no degree-$d$ coefficient upper bound enters the error. Compact support
makes the variance a polynomial of bounded moment martingales and justifies
expectation of the drift despite inverse covariance in its formal expression.

*Established, uncertified.* Reverse transfer uses the common metric
$M=A+\delta B^{-1}$ and pays the full centered-integration product norm once.
Its final input derivative must be centered, imposing $q\le d-1$.
The exact error is $\eta\Sigma_d/d^2$, from time $t=\eta/d^2$.
Truncation, whitening and convergence of the fixed-dimensional Appell Gram
matrix remove compact support; support restriction handles degenerate covariance.

## What resists

No mathematical gap has been isolated in this reconstruction. Independent
review remains required, as do the separate proof interfaces
`prop:bk-integration-calculus` and `lem:bk-regular-approximation`.
Uniform numerical coefficient and integration-product bounds are hypotheses
of the transfer proposition, not discharged by it.
The attempted full checker hit an environment-level Node/NPM version failure
and concurrent not-yet-registered anchors; this is not evidence about mathematics.

## Proposed next step

Independently review the ordered two-slot Loewner inequality, continuation at
finite lifetime, the moving highest-cumulant Bessel endpoint, and exact
covariance/curvature preservation in approximation. Review the integrated
canonical claims and rerun the full build in the orchestrator's working
Node environment. No route-state or certification delta is proposed here.
