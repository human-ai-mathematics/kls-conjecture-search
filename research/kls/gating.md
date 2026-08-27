# KLS active gates

This file states the deliverable required to advance each live route. Exact mathematical
statements and status remain in `ledger.yaml`; applicable fences remain in `bounded_by` and
`obstructions.md`.

## Eldan localization

### `q:upgrade`

Produce a uniform absorptive trace estimate that directly discharges
`ass:all-cut-carleson`, with every source and damping term matched to
`thm:scalar-riccati`. The estimate must use cut-aware information and handle small-time
high-rank occupation.

### `q:weighted`

Prove the ledger rate for balanced near-Cheeger cuts with the calibrated
$(1+\|A_t\|)^{5/2}$ weight. The argument must not insert an unproved lower bound for the
localized isoperimetric profile.

### `q:stein-weighted`

Supply the exact weighted input required by `ass:weighted-package`: a
localization-uniform almost-stability trace theorem modulo Jacobi zero modes, with explicit
domains, boundary conventions, and controlled Reilly terms.

### `q:taming` and `q:splitting`

Define an explicit bridge object carrying both the cut-free covariance index and the cut-indexed
boundary geometry. Prove the required covariance control or almost-splitting estimate without
inferring it from product structure alone.

### `q:alignment`

Give either a uniform analytic incident-high bound for fixed balanced product cuts or a certified
counterexample. A finite tail-union diagnostic is not a universal conclusion.

## Moment-map spectral occupation

### `q:mm-spectral-occupation`

Prove the universal-time absorptive source/damping estimate uniformly on regular approximants,
preserving tensor orientation under unwhitening.

### `prop:spectral-sufficiency`

Derive a dimension-free spectral gap from that occupation estimate, including terminal variance
control and the regularization limit.

## Deterministic moment-map / CMH

### `ass:uniform-cmh-approximants`

Prove a universal $C$ such that the centered Gaussian-convolution, Gaussian-tilt, and
growing-ball regular moment-map approximants of every centered log-concave law satisfy
$\sup_k C_{\mathrm{CMH}}(\mu_k)\le C$. The certified conditional node
`q:cmh-approximation` then passes the affine Poincaré inequalities to the limit with no loss,
including proper affine-support degeneration; it asserts no continuity of
$C_{\mathrm{CMH}}$.

### `q:mm-invariant-lift`

Derive the target-flat Schur--Piola multiplier invariantly and reduce arbitrary split dimensions
to controlled Codazzi components paired with named positive squares.

### `q:mm-square-root-commutator`

Control the complete Haar sum of square-root commutators on a common core and account for every
retained positive and error term without double spending.

### `q:cmh-solenoidal-perturbation`

Certify log-concavity and isotropy to second order for an admissible perturbation of the
one-sided-exponential product, then compute the exact second variation through the Hodge split.
A positive variation refutes CMH(4), not KLS.

### `conj:gate-zero`

Give an independently checked analytic moment-map proof or counterexample to
$\mathbb E[H\Sigma^{-1}H]\preceq4\Sigma$. Matrix algebra alone is insufficient, and a floating
Monge--Ampère computation can identify only a candidate.
