# CMH route — dispatchable open problems

The tasks are ordered. A later task may use an earlier one only after its exact conventions are
persisted; model success never skips a proof gate.

Tasks M1--M8 belong to the **construction layer**; M9--M11 to the **falsification layer** opened
by the normalization results. The two are independent: M9 or M10 could close the route before any
of M1--M8 is attempted.

## M0 — freeze CMH and prove the regular-class endpoint reduction — **DISCHARGED 2026-08-25**

*Was:* specify $\Sigma$, $L$, the $L^2$ measure, centering conditions, and operator domains in
CMH(4), then prove CMH(4) $\Rightarrow C_P^{\mathrm{aff}}(\mu)\le4$ on the regular moment-map
class.

*Outcome:* `def:cmh` fixes the data and `thm:cmh-implies-affine-poincare` proves
$C_P^{\mathrm{aff}}\le C_{\mathrm{CMH}}$ — by a dual pairing plus spectral truncation, with no
spectral gap assumed. Dossier `solutions/thm-cmh-normalization.tex`; the original partial review
is retained at `research/reviews/2026-08-25-kls-cmh-normalization-audit.md`, and the repaired
proofs are certified by the unqualified
`research/reviews/2026-08-25-kls-cmh-normalization-repair-audit.md`.

*Residue.* Two items are **not** closed and are not to be treated as closed:

1. **Uniformity through approximation (`q:cmh-approximation`).** The reduction is proved on the
   regular moment-map class. A universal bound on $C_{\mathrm{CMH}}$ must be uniform along an
   approximating sequence, and the affine Poincar\'e inequality must then be passed to the limit,
   including affine-support degeneration. Any future proof of the headline owes this.
2. **No strict-separation theorem.** `prop:cmh-hodge` proves a decomposition into affine
   Poincar\'e and nonnegative solenoidal channels. It does not exhibit a measure with
   $C_P^{\mathrm{aff}}\le4<C_{\mathrm{CMH}}$ or prove non-implication. M9 is the open test.

## M0b — approximation closure — **OPEN**

Discharge `q:cmh-approximation`: formulate regular moment-map approximants with uniform affine
normalization, prove the needed lower-semicontinuity/closure statement, and handle limits whose
support lies in a proper affine subspace. This task is logically separate from proving a
universal CMH bound on the approximants.

**Acceptance gate:** a standalone argument with explicit topology, core approximation, and
constant preservation; numerical convergence is not a substitute.

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

Combine M0, the approximation/closure task M0b, and M6 to prove the fully defined CMH estimate
on arbitrary log-concave laws and then KLS.

**Acceptance gate:** separate author and critic, standalone solution dossiers, ledger promotions,
and full-document compilation. This task is terminal; it cannot be inferred from finite-dimensional
checks or a successful regression battery.

---

# Falsification layer (opened 2026-08-25)

## M9 — second-order solenoidal excess at the product endpoint

**The route's sharpest probe.** By `thm:cmh-product`, a product of one-sided exponentials has
$C_{\mathrm{CMH}}=4$ **exactly** — zero slack. By `prop:cmh-hodge`, the CMH numerator is an
affine Poincaré part plus a solenoidal excess $\mathbb E\langle w,\Sigma^{-1}w\rangle$.

Take $\psi_0(s,t)=\phi(s)+t^2/2$ with $\phi$ the one-sided exponential moment potential and
perturb by $\psi_\varepsilon=\psi_0+\varepsilon a(s)b(t)$ inside the smooth strictly convex
class. Compute the second variation of $C_{\mathrm{CMH}}$ at $\varepsilon=0$, split through the
Hodge decomposition. Either

- exhibit an admissible perturbation with strictly positive second variation — which **refutes
  $\mathrm{CMH}(4)$**, forcing the route to a larger constant or to abandonment, without saying
  anything about KLS; or
- identify the structural reason the solenoidal part vanishes to second order at a saturating
  product, which would be the first real evidence *for* the headline.

**Acceptance gate:** an exact second-variation computation with the perturbation's log-concavity
and isotropy certified, not merely asserted. Isotropy to second order is the delicate part: the
first covariance variation must be shown to vanish, so that whitening is $I+O(\varepsilon^2)$ and
does not move the quadratic coefficients. A numerical second variation is directional only and
must go through `finum`.

**Why this is cheap:** both ingredients are already exact theorems. Unlike M1--M8 it needs no
Haar tree, no invariant lift, and no operator domains beyond those already fixed by `def:cmh`.

## M10 — decide gate zero on genuine moment maps

Decide $\mathbb E[H\Sigma^{-1}H]\preceq4\Sigma$ (`conj:gate-zero`, `q:gate-zero`).

*Directional counterexample search (dispatchable now).* Compute
$\lambda_{\max}(\Sigma^{-1/2}\mathbb E[H\Sigma^{-1}H]\Sigma^{-1/2})$ on moment maps outside the
proved classes: log-concave laws whose moment potential is known or numerically solvable —
skew polygons, entropic barriers, asymmetric log-sum-exp models, non-simplex polytopes. A value
above $4$ is a directional candidate counterexample. Only an independently checked exact or
analytic witness refutes $\mathrm{CMH}(4)$, **without** refuting KLS. Channel: the
`cmh-gate-zero` finum target, extended beyond its current exact classes. Anything requiring a
numerically solved Monge--Ampère equation remains research guidance only.

*Proof side (NOT dispatchable as an independent effort).* By `prop:letwin-not-gate-zero` and
the static commutator identity, proving gate zero means bounding
$\mathbb E\lVert[B,H]\rVert_{\mathrm{HS}}^2$ using differentiated Monge--Ampère structure. In
isotropic position gate zero is $\lambda_{\max}(\mathbb EH^2)\le4$ against Chen--Klartag's
$\operatorname{tr}(\mathbb EH^2)\le2n$ — an operator-to-trace upgrade with a factor-2 budget,
hence inside the ownership cluster of `rem:trace-upgrade-unification`. **Hard constraint 6 of
`CLAUDE.md` applies: do not open a parallel effort.** Route it to that cluster's owner.

**Acceptance gate (falsification):** a persisted witness — an exact moment map, or a `finum`
artifact whose numerical Monge--Ampère solve is convergence-gated and reported as directional.
Do not report a directional exceedance as a refutation.

## M11 — literature reconciliation for the exact classes

`thm:cmh-dirichlet` and `cor:cmh-dirichlet-poincare` assert an affine Poincaré constant $4$ for
every log-concave Dirichlet law. The Wright--Fisher spectral gap is classical and KLS is known for
several structured families. Before any external write-up, establish exactly which parts are new:
the affine (covariance-normalized) constant for Dirichlet laws, the Riesz-transform formulation
for the moment-map Stein generator, and KLS for simplices by other routes.

**Acceptance gate:** a citation-level reconciliation recorded in the audit report. A novelty claim
made on top of existing literature is a defect, not a shortfall.
