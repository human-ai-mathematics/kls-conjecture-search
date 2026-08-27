# KLS active gates

This file states the deliverable required to advance each live route. Exact mathematical
statements and status remain in `ledger.yaml`; applicable fences remain in `bounded_by` and
`obstructions.md`.

## Eldan localization

### `q:upgrade`

Produce the tight-prefix absorptive trace estimate `ass:tight-prefix-carleson`, with every source
and damping term matched to `thm:scalar-riccati`. The raw prefix soft-projector injection staged
in Wave 2 is withdrawn: a Gaussian halfspace cylinder with arbitrarily many independent
one-sided-exponential spectators has $B=G=0$ in every spectator block but positive
$D^2\chi/D\chi$ injection growing linearly with the number of spectators. This does not refute
the source estimate, because the discarded terminal and favorable drift terms cancel those
blocks exactly. The next gate is therefore a spectator-cancelling cut-relative or net-injection
estimate, retaining that cancellation and producing a strict damping surplus $\gamma<1/8$.
For any retained cutoff one must state $0\le\chi\le1$ and $\chi'\ge0$. Subtracting only
$\operatorname{Tr}(A\chi(A))$ is insufficient: the remaining deterministic $AB$ term can consume
the full damping $D$. Rank tails alone still do not control the cut orientation.

### `q:weighted`

The literal $e_0\le1$ global-operator-norm rate is refuted by the certified
`prop:weighted-spectator-obstruction`. Formulate a replacement that either uses an explicit
near-worst-measure hypothesis and re-audits consumption, or uses a cut-local, tensor-stable
covariance weight that ignores independent spectators while still dominating the aligned
two-tail mode. It must not insert an unproved lower bound for the localized profile. The
certified `prop:spectator-excess-rate-obstruction` also refutes every uniform superlinear
source-vanishing remainder even with weight one. The consumer only needs an $O(T)$ supply, so a
surviving statement must allow that scale, make the remainder vanish with a genuinely cut-local
source deficit, or impose an explicit near-worst-measure premise. The candidate cut scale
$\lambda_{\rm cut}(A,K)$ passes exact cylinder tensorization and the aligned two-tail test, but is
not perturbatively stable:
$\lambda_{\rm cut}(\operatorname{diag}(1,L),\varepsilon E_{12}^{\rm sym})=(1+L)/2$ for every
$\varepsilon\ne0$. The preferred unproved replacement is therefore source-screened: charge the
weighted excess only where $Q_t\ge\kappa e_tW_{\rm cut}$, and on the complement return at most an
absorbable fraction $\theta Q_t$. A matching trace coefficient must satisfy
$2\beta/(1-\theta)+64\eta^2<1$. Neither the screened supply nor its trace companion is proved.

### `q:stein-weighted`

First specify the tensor-stable replacement for the refuted `ass:weighted-package`, then supply
the matching localization-uniform almost-stability trace theorem modulo Jacobi zero modes, with
explicit domains, boundary conventions, and controlled Reilly terms. The old weighted trace
formula remains a candidate analytic ingredient, not a complete live package.

### `q:taming` and `q:splitting`

Define an explicit bridge object carrying both the cut-free covariance index and the cut-indexed
boundary geometry. Prove the required covariance control or almost-splitting estimate without
inferring it from product structure alone.

### `q:alignment`

Give either a uniform analytic incident-high bound for fixed balanced product cuts or a certified
counterexample. A finite tail-union diagnostic is not a universal conclusion.

## Moment-map spectral occupation

### `q:mm-spectral-occupation`

Prove the universal-time full-damping source estimate uniformly on regular approximants,
preserving tensor orientation under unwhitening. The source may consume the entire exact damping;
a strict damping surplus is not required for the KLS bridge.

### `prop:spectral-sufficiency`

This bridge is now certified: full damping, terminal variance control, and the regularization
limit give $C_P\le2/T_*$.  No independent deliverable remains here; the live gate is exactly
`q:mm-spectral-occupation`.

## Deterministic moment-map / CMH

### `ass:cmh-recovery-envelope`

Construct, for every centered log-concave law, at least one regular compact-target moment-map
recovery sequence with a universal bound on $\liminf C_{\mathrm{CMH}}$. The unconditional affine
Poincar\'e lower-semicontinuity lemma and the regular CMH endpoint then pass the bound to the
limit. This is the preferred approximation gate; it does not demand control of every
regularization choice. The current proof-ready linear subgate is anisotropic source retention:
in isotropic source coordinates the exact matrices
$\mathsf N=\int H^2$, $\mathsf D=\int H^{ab}(\partial_aH)(\partial_bH)$, and
$\mathsf R=\tfrac12\int\{H,A+Q\}$ satisfy the candidate identities
$\mathsf N=\mathsf D+\mathsf R$ and $\mathsf N-I\preceq\mathsf D$; a universal estimate
$\mathsf R\succeq\rho\mathsf N-\beta I$ would give
$Q_{\rm lin}\le(1+\beta)/\rho$. This reduction is parked pending proof certification. The
scalar cyclic-square argument has no pointwise Loewner promotion, so any proof needs an
integrated corrector or nonlocal coercivity, not matrix polarization alone.

### `ass:uniform-cmh-approximants`

Prove a universal $C$ such that the centered Gaussian-convolution, Gaussian-tilt, and
growing-ball regular moment-map approximants of every centered log-concave law satisfy
$\sup_k C_{\mathrm{CMH}}(\mu_k)\le C$. The certified conditional node
`q:cmh-approximation` then passes the affine Poincaré inequalities to the limit with no loss,
including proper affine-support degeneration; it asserts no continuity of
$C_{\mathrm{CMH}}$.

This remains a stronger sufficient premise for the already-certified
`q:cmh-approximation`; it is not necessary if `ass:cmh-recovery-envelope` is discharged.

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

## Conditional-fiber frame

### `q:conditional-fiber-frame`

For every full-dimensional isotropic log-concave $\mu$ on $\mathbb R^d$, construct one even
probability $\rho_\mu$, independent of the test function, with
$d\int\theta\theta^T\,d\rho_\mu=I_d$, and prove
$\operatorname{Var}_\mu(f)\le C\mathcal D_{\mu,\rho_\mu}(f)$ on the maximal closed form domain
with universal $C$. Alternatively, refute the route by an exact fixed-degree uniform-simplex
dual certificate whose objective tends to zero. A root-frame-only argument or a floating finite
computation does not decide the all-frame gate.
