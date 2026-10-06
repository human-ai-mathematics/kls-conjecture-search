---
verdict: pass
authors:
  - bk_powers, gpt-6-astra, 2026-10-06
  - bk_localization, gpt-6-astra, 2026-10-06
  - orchestrator, gpt-6.1-sol, 2026-10-06
reviewer: reviewer, gpt-6-astra, 2026-10-06
fingerprints:
  solutions/lem-bk-regular-approximation.md: 44ab0fdc4f73b90e312b166f1505f7b8117b99d4099237ae2a1b45ad84408767
  lem:bk-regular-approximation: e9223378a723c866b083fb0fa5996cb2e392d23932416eab367590c580110758
  def:bk-compatible-calculus: b0bb2905e0f3e30702cd0c5d9d3ff881d59ec3fa87175e4d2b50222b5e865ed1
  def:bk-uniform-appell-coefficients: 0e3be6061878fe05162d23613514cc2211cad0df63d76393c5957b3444776c95
  solutions/lem-bk-localization-covariance.md: 2df801cad144cb04a9de71ee1c232431d60667bfa347a2eeb11e5d13a94ac68b
  lem:bk-localization-covariance: 0153466c7ce5e92a428f0d119f0f4e8dc65727508cdd3dfa468afac74d652b88
  thm:letwin-qcts: 8e2ac0819f46db553fe83a6f3034436816565262316c2e6bde7d81baead1a082
  lem:bk-moving-appell-variance: 213338b49a2d095dbdbc9ac97ac60741e9e57ad4ef2b98bcdda393873e1e6285
  solutions/prop-bk-reverse-transfer.md: b8226a5f2c2fcfa305aea6a6bd5e207e01aa35320e9fdd6a9fa4c97eacba52c2
  prop:bk-reverse-transfer: be684c7356c9b9c9ceef5017794c511c778ad4c5f8f0525aa7bf5a33550dfb73
  prop:bk-integration-calculus: 591a8826b560d20e268b65a430aff427ed03b6c8f4b9b03c53272f31dac7b2c4
---

# Findings

**Pass** for `lem:bk-regular-approximation`, `lem:bk-localization-covariance`,
`lem:bk-moving-appell-variance`, and `prop:bk-reverse-transfer`, proved by the
three fingerprinted dossiers. Their theorems imply their canonical manuscript
statements, with matching quantifiers, tensor conventions and constants.
Promote this grouped chain together or in dependency order. The integration
calculus is now independently certified in
`research/reviews/2026-10-06-bk-operators-review.md`; its statement fingerprint
matches the interface checked here. Letwin's quadratic theorem is an already
certified input. No open external dependency is accepted as a theorem.

This is a full `certify` review in a fresh context without the authoring
conversation. I authored none of the dossiers. I read `SPECIFICATION.md` first
and reconstructed the arguments from the dossiers, canonical statements,
ledger, checkpoints and the actual pinned BK source at commit
`4837c33649ba2271f43c9684e9350ecbdd725f95`, Sections 2, 6, 7 and Appendices D
and F, using `/tmp/bk-source.pdf` and its text extraction. No numerical
artifact supplies a proof step.

## Approximation and finite-energy limits

The theorem in `solutions/lem-bk-regular-approximation.md` implies
`lem:bk-regular-approximation`, including the clarified fixed-leading-tensor,
fixed-degree and fixed-derivative-order limit. Completing the square leaves a
jointly log-concave integrand, giving lower curvature
$a/(1+a\varepsilon)$ before rescaling. The posterior covariance formula gives
the upper Hessian bound $\varepsilon^{-1}I$. Rescaling gives covariance at most
identity and lower curvature $a(1+\varepsilon)/(1+a\varepsilon)\ge a$, using
$a\le1$ exactly here. Gaussian smoothness and strict positivity hold globally.
The quadratic tilt and whitening have strictly positive finite Hessian bounds;
convergence of normalizers, means, covariances and every fixed moment justifies
the isotropic approximation. The reciprocal formal series and finite Gram
matrix justify convergence of derivative integrals and the supremum over
leading tensors. No integration-operator convergence is asserted.

The established marginal theorem was checked against
[Prékopa (1973), Theorem 6, page 8 of the PDF](https://rutcor.rutgers.edu/~prekopa/SCIENT2.pdf).
Its joint log-concavity hypothesis applies to both the half-space indicator
times the density and the completed-square integrand. The resulting coordinate
survival-function argument supplies all fixed moments. Appendix F's remaining
proofs were checked directly. Weak convergence is applied only to compact
smooth tests. Absolute continuity permits mollification; spatial cutoffs
extend to bounded finite-energy functions. Value truncation and a
positive-measure bounded-value set bound the truncation means, proving square
integrability before passage of the variance. The conclusion does not
presuppose that the target finite-energy function is in $L^2$.

## Global localization and ordered tensor estimates

Both theorems in `solutions/lem-bk-localization-covariance.md` agree with their
canonical nodes. Smooth finite tilt parameters have positive covariance since
the initial isotropic law is full dimensional. Direct Itô differentiation
gives the normalized-density, mean and covariance equations. The canonical
`thm:letwin-qcts` supplies exactly
$\operatorname{Var}(Y^THY)\le8\|H\|_{\rm HS}^2$ for every symmetric $H$ under
every isotropic log-concave law. Duality and symmetry of the third tensor give
$\sum_iS_i^2\preceq8I$. The sum of squares on two ordered slots gives
$\sum_iS_i\otimes S_i\preceq8I$ on the full tensor space; congruence yields
the covariance-noise inequality.

For continuation, the log-determinant drift is in $[-5n,-n]$ and its
martingale quadratic-variation rate is at most $8n^2$. Its continuous
extension to an alleged finite lifetime and $A_t\preceq R^2I$ bound the
least eigenvalue away from zero pathwise. Integer stopping of the
inverse-covariance integrand gives convergence of the stochastic tilt
parameter. The finite limiting parameters extend the smooth SDE,
contradicting explosion. Bounded posterior tests are then true martingales.

The tensor drift coefficient is $-k+8\binom{k}{2}\le4k^2$. Compact support
and the noise bound make each tested stochastic integral a true martingale,
so the conditional estimate is valid. Conditioning the latest equal-time
block backwards, tensoring with positive measurable earlier factors, gives
the mixed-time bound without commuting different covariance matrices.
The integrated positive block matrix gives
$\Lambda_t^{-1}\preceq t^{-2}\int_0^tA_s\,ds$. Inserting this separately into
ordered slots, integrating and expanding gives exactly
$(1+\delta/t)^q e^{4d^2t}$, including $q=0$ and $q=d$.

## Moving Appell variance

Finite formal coefficient comparison gives the polynomial SDE. Its product
with the moving density includes the cross-variation term and yields the
stated drift. The raising identity and cumulant/Appell identity have the
correct factorials. Fixed-time whitening evaluates the already computed
drift; it is not used as an unaccounted stochastic change of variables.
The $k=1$ term contributes $d p_t$. The $k=d$ term pairs to
$|E_t[p_t\xi_t]|^2\le E_tp_t^2$, so no degree-$d$ coefficient bound is used.
For the middle terms, slice-wise cumulant contraction and orthogonal
symmetrization give
$d!(d-k+1)C_kC_{d-k+1}\|\widetilde T\|$. Thus $\Sigma_d$ and the drift
lower bound have exactly the stated constants, including the empty sum
at $d=2$.

Moments through order $2d$ are bounded martingales whose diffusion
coefficients are bounded by Bessel's inequality. The moving variance is a
polynomial of this finite moment vector, so its drift and diffusion have
deterministic bounds without an inverse-covariance expectation bound.
This justifies removal of stopping and expectation. The equal-time tensor
estimate, Cauchy--Schwarz, positivity of a nonzero leading polynomial under a
full-dimensional law, and integration of the square-root inequality give
the exact asserted exponential and error term.

## Reverse transfer

The theorem in `solutions/prop-bk-reverse-transfer.md` agrees with
`prop:bk-reverse-transfer`, including uniformity in dimension and law.
The upstream integration calculus supplies existence and the inverse identity
for centered compatible derivatives. For a degree-$d$ Appell polynomial, all
derivatives through $q$ are compatible weighted Sobolev fields and are centered
because $q<d$. Thus $p=J_0\cdots J_{q-1}D^qp$ is valid: its final input is
centered, rather than constant. The uniform $M_q$ bound remains an explicit
hypothesis. The approximation above preserves precisely its covariance and
curvature requirements and passes polynomial norms without approximating $J$.

For $M=A+\delta B^{-1}$, inversion gives $B\succeq\delta M^{-1}$. Hence
the coordinate change has covariance at most identity and curvature at least
$\delta I$. The chain rule puts $M$ in the derivative slots and $A_t$ in
the remaining polynomial slots. Applying the degree-$(d-q)$ bound to each
symmetric remaining slice gives exactly $(d!)^2C_{d-q}^2$, without a
commutation assumption or dimension factor. The ordered covariance and moving
variance estimates give exponent $(2d^2+d+1)t$. At $t=\eta/d^2$ one has
$\delta/t=\eta$, that exponent is at most $3\eta$, and the error is exactly
$\eta\Sigma_d/d^2$. Truncation on convex balls, whitening, finite Gram-matrix
convergence and contraction from isotropic coordinates on the linear support
justify the full supremum $c_d^*$. Point masses have zero positive-degree
Appell variances.

## Hypotheses, fences and build

Approximation uses full dimension, log-concavity, centering and covariance at
most identity, $0<a\le1$ for exact curvature preservation, fixed dimension,
degree and derivative order for polynomial limits, and a common finite scalar
Poincaré bound for the weak-limit conclusion. Localization uses compact
support, isotropy, log-concavity and the certified quadratic variance input.
Moving variance uses $d\ge2$ and finite lower-degree bounds uniform over all
isotropic log-concave laws. Its stated $C_1$ hypothesis is unused, a harmless
strengthening of the premise. Reverse transfer uses $1\le q\le d-1$,
$0<\eta\le1$ and the stated uniform $M_q,C_k$ hypotheses. These antecedents
are not discharged here or replaced by an all-degree coefficient bound.
All other stated hypotheses are used; no unstated hypothesis was found.

These nodes have no `bounded_by` or `assumes` edges. The ordered-tensor
argument and explicit uniform quantifiers respect the relevant projection
and uniform-admissibility cautions. The existing `depends_on` edges supply
the inputs actually used, with the three internal predecessor nodes proved
in this grouped review. The command `uv run scripts/check.py` completed with
exit code zero and no MyST errors. The final fingerprint command for all
three dossiers also completed successfully after upstream registration.

# Corrections

None. Retain all current dependency edges and quantified antecedents. The
proposed proof records and statuses are:

```yaml
- id: lem:bk-regular-approximation
  status: proved
  proofs:
    - artifact: solutions/lem-bk-regular-approximation.md
      review: research/reviews/2026-10-06-bk-localization-review.md
- id: lem:bk-localization-covariance
  status: proved
  proofs:
    - artifact: solutions/lem-bk-localization-covariance.md
      review: research/reviews/2026-10-06-bk-localization-review.md
- id: lem:bk-moving-appell-variance
  status: proved
  proofs:
    - artifact: solutions/lem-bk-localization-covariance.md
      review: research/reviews/2026-10-06-bk-localization-review.md
- id: prop:bk-reverse-transfer
  status: proved
  proofs:
    - artifact: solutions/prop-bk-reverse-transfer.md
      review: research/reviews/2026-10-06-bk-localization-review.md
```

# Exclusions

The compatible Hodge and integration-calculus proofs are not independently
certified here; only the supplied interface is checked. Letwin's proof is
retained as an already certified input, not re-reviewed. The abstract power
lemma, integration-power corollaries, uniform coefficient induction, final
scalar Poincaré and Cheeger bounds, and final KLS composition are outside
scope. The stronger locally Sobolev extension in Appendix F is not claimed
by this dossier and is not certified here. No source assertion outside the
specified reconstruction is certified wholesale.
