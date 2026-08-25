# CMH route — active handoff

The ledger owns exact statements. These tasks record sequencing and acceptance gates only.

## Closure: `q:cmh-approximation`

Construct regular moment-map approximants with uniform affine normalization, prove the required
closure/lower-semicontinuity statement, and handle degeneration to a proper affine support.

Acceptance: explicit topology, common/core approximation, and constant preservation. Numerical
convergence is not a substitute.

## Construction: invariant lift

### `q:mm-invariant-lift`

Derive the target-flat Schur–Piola multiplier invariantly, audit all moving-frame coefficients,
and reduce arbitrary split dimensions to Codazzi shape components paired with named retained
positive squares.

Acceptance: frame-independent formulas that specialize correctly to Gaussian, conformal, and
inverse-metric cases; every domain and boundary convention must be stated.

### `q:mm-square-root-commutator`

Control the full Haar sum of $[N^{1/2},K_M]$ using the resolvent representation, then account for
every retained Letwin/Codazzi/corrector/descendant term without spending slack twice.

Acceptance: a closed dimension-free quadratic-form estimate on a common core, stable under
approximation and complete-tree summation. Floating spectra or model success are diagnostics only.

## Route test: `q:cmh-solenoidal-perturbation`

Perturb a product of centered one-sided exponentials, which satisfies
$C_{\mathrm{CMH}}=4$ exactly, and compute the second variation of the full quotient through the
Hodge split.

Acceptance: certify log-concavity and isotropy to second order. A positive exact variation refutes
CMH(4), not KLS. A numerical variation must flow through `finum` and remains directional.

## Route test: `conj:gate-zero`

Decide $\mathbb E[H\Sigma^{-1}H]\preceq4\Sigma$ on genuine moment maps. Counterexample searches
must leave the already-proved one-dimensional, product, affine-image, and Dirichlet classes.

The proof side is part of the shared operator-to-trace ownership cluster: by
`prop:letwin-not-gate-zero`, matrix algebra alone is insufficient. Do not fan it out as an
independent duplicate of `q:upgrade`/`q:stein-weighted`/`q:alignment` work.

Acceptance: an independently checked exact/analytic moment-map witness or proof. A floating
Monge–Ampère computation can only identify a candidate.

## Literature task

Before external claims, reconcile the exact Dirichlet and simplex results with the classical
Wright–Fisher spectrum, existing KLS results for structured families, and prior moment-map
Riesz-transform formulations. Record citation conclusions in an audit, not as a ledger node.

## Handoff discipline

Use the shared instances in `research/knowledge/instances.md`. New sampled/FEM work goes through
`finum`; exact algebra belongs in a dossier or dated exploration. Promotion still requires a
standalone solution, independent review, matching ledger metadata, and a green checker.
