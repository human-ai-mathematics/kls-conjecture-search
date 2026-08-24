# CMH route — dispatchable open problems

The tasks are ordered. A later task may use an earlier one only after its exact conventions are
persisted; model success never skips a proof gate.

## M0 — freeze CMH and prove the endpoint reduction

Specify $\Sigma$, $L$, the $L^2$ measure, centering conditions, operator domains, and the
regularization class in CMH(4). Prove the claimed divergence-duality implication
CMH(4) $\Rightarrow C_P(\mu)\le4$, including passage from regular moment measures to arbitrary
isotropic log-concave measures.

**Acceptance gate:** standalone dossier plus independent review. Until this is done, the route's
headline is a schema, not a theorem.

## M1 — invariant tensorial lift

Derive the actual multiplier field from fixed target coordinates in a Schur--Piola frame. Fix all
moving-frame conventions and compute the transport coefficient $\alpha$ without choosing it by
hand. Reproduce the $1+2$ completion of squares and state the $\alpha$-dependent form omitted from
the summary.

**Acceptance gate:** invariant formula agrees in two independently chosen frames and specializes
correctly to Gaussian, conformal, and inverse-metric lifts.

## M2 — cubic symbol decomposition

Starting from $[N,Q_M]$, compute the full cubic principal symbol on a common core and decompose it
into irreducible Codazzi shape components. Verify the proposed commutator expression involving
$[\Omega_k,M]$ and track lower-order terms separately.

**Acceptance gate:** the formula vanishes in the commuting/conformal cases and transforms
covariantly under orthogonal changes of frame; no cancellation is asserted beyond the proved
one.

## M3 — exact finite-dimensional forms

Construct the coefficient matrices for $1+2$, $1+3$, and $2+2$ splits and compare every negative
commutator component with a named retained Letwin/Codazzi square.

**Acceptance gate:** exact rational or symbolic certificates of positive semidefiniteness. Floating
point eigenvalues may guide the calculation but are not proof and must not be called R2.

## M4 — Hodge and one-edge audit

Fix topology and boundary conditions for the Airy representation; define $A_S$, $A_K$,
$\Pi_K$, $F_0$, and all conditional flux spaces. Prove

$$
r_h=r_{\mathrm{cond}}+(I-\Pi_K)(S-K)\nabla v
$$

and the complete one-edge deficit on the same Hilbert spaces.

**Acceptance gate:** both solenoidal channels are sign-consistently identified. Any claimed
orthogonality must name and justify the weighted metric, since $\Pi_K$ need not be orthogonal in
ordinary $L^2$. The rotated Gamma--Gaussian model violates the old vector law but satisfies the
corrected tensor law.

## M5 — resolvent commutator bound

Insert the M2/M3 estimates into

$$
[N^{1/2},K_M]=\frac1\pi\int_0^\infty
t^{1/2}(N+t)^{-1}[N,K_M](N+t)^{-1}\,dt.
$$

Control low and high resolvent scales without losing dimension, and state exactly which positive
reservoir is consumed.

**Acceptance gate:** a closed quadratic-form estimate on a core, stable under approximation, with
constants independent of dimension and tree depth.

## M6 — full Haar and descendant ledger

Sum the one-edge estimate over the complete Haar tree. Use the exact Bessel deficit and retain
descendant/leaf slack; do not assume nodewise positivity or allocate a fixed slack fraction.

**Acceptance gate:** every positive term is spent at most once, every negative term is assigned,
and the final constant is dimension-free.

## M7 — regression suite

Continuously test M1--M6 against the curated models in [`models.md`](models.md). Implement sampled
or FEM observables only through `finum`, with provenance and convergence gates. Exact analytic
counterexamples belong in a proof/exploration dossier.

**Acceptance gate:** Gaussian and commuting products calibrate; rotated exponentials detect
nodewise sign errors; Laguerre modes detect illegal slack allocation; Gamma--Gaussian detects the
false local conservation law; the three-exponential projection activates the Airy mismatch.

## M8 — close CMH

Combine M0 and M6 to prove the fully defined CMH estimate and then KLS.

**Acceptance gate:** separate author and critic, standalone solution dossiers, ledger promotions,
and full-document compilation. This task is terminal; it cannot be inferred from finite-dimensional
checks or a successful regression battery.
