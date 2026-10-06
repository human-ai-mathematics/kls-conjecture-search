---
verdict: pass
authors:
  - plan_framework researcher, unknown, 2026-10-06
reviewer: reviewer, gpt-6-astra, 2026-10-06
fingerprints:
  solutions/bkl-cumulant-dynamics.md: f8fa7b29a71b831a02568f913d4672d2e03b1294683905f5f0bf3648590857f0
  lem:bkl-cumulant-dynamics: c6d9d767482c117e49dea11d360003958d8b5051e2d2fd8b37c193cbacf1dfcd
  def:bkl-tilt-cumulants: 43636c8506cef53a8ed43a8231a955e160d704cc899cc248c5e08425ab5f449c
  prop:letwin-kappa: 95b731e551b7d7bc79b4aa8f98b04c61ecbd81f2e93797788409e25124ad2187
  thm:letwin-qcts: 8e2ac0819f46db553fe83a6f3034436816565262316c2e6bde7d81baead1a082
---

# Independent certification of the cumulant dynamics

## Findings

**Pass for [](#lem:bkl-cumulant-dynamics).** This certify review began with a fresh
assignment and repository paths, without the authoring conversation. The dossier
implies the canonical statement, including global existence, positive finite-time
covariance and the additional deterministic bounds and true-martingale assertion.
No required step remains unverified.

The source examined directly was Bizeul–Klartag–Lehec, *Presenting a proof of the
Kannan–Lovász–Simonovits conjecture*, arXiv:2610.05474v1, 4 October 2026,
Section 4, Lemmas 4.2–4.3 and equations (65)–(79), including their proofs.
The local HTML copy `/tmp/bkl-2610.05474v1.html` has SHA-256
`fb51ab0d94171ac7de2a3009efb5249e44ee66de5c9a1dc5899bdb843de29df9`.
The dossier reconstructs those identities and supplies independent global-existence
and integrability arguments where the source cites localization literature.
Consequently those historical citations are not missing premises of this proof.

### Statements, premises and hypotheses

The canonical definition uses ordered-index Hilbert–Schmidt norms. Both the
source and dossier use precisely that convention. All orders, vectors, time
intervals, initial conditions, and the constant 8 agree. The dossier's unit-vector
formulation extends to the canonical arbitrary fixed vector by the explicitly
stated homogeneity; the zero vector is included. Its stronger uniqueness claim is
also proved.

The hypotheses actually used are finite dimension, compact support in a ball,
isotropy, log-concavity, fixed deterministic vector, and finite order when bounding
moments. Compact support controls the parameter derivatives and unwhitened
covariance; isotropy supplies full affine support and the initial covariance;
log-concavity supplies the quadratic and marginal-tail estimates. None is an
unstated premise. There is no `bounded_by` fence or open proof dependency.
[](#def:bkl-tilt-cumulants) is defined, and [](#prop:letwin-kappa) and
[](#thm:letwin-qcts) are proved with existing independent certification records.
The latter discharges the former's explicit antecedent. Their canonical statements
were read and their scope checked: arbitrary isotropic log-concave laws and
symmetric matrices give exactly the needed squared third-cumulant norm bound 8.
The dossier additionally reproduces that Cauchy–Schwarz deduction. The upstream
Letwin proof is used at its existing certified scope, not recertified here.

### Steps checked

1. Positive tilts preserve affine support; their covariance is positive definite
   for every finite parameter pair. Differentiation under compactly supported
   integrals makes the SDE coefficients locally smooth. The symmetric matrix
   parameter can be regarded as a finite-dimensional Euclidean coordinate.
   The integral defining its evolution keeps it positive semidefinite, so the
   posterior remains log-concave.
2. The exponential Itô correction cancels the quadratic-potential drift. The
   quotient cross variation cancels the remaining normalizer drift. Applying
   the resulting density equation to first and second moments gives barycenter
   noise equal to the positive covariance square root and covariance drift
   equal to minus the covariance, including its sign and clock.
3. Whitening gives the exact cumulant transformation for orders at least two.
   Contracting the whitened third tensor identifies the matrix quadratic form
   and proves the constant-8 matrix bound without a dimensional factor.
4. For the log determinant, the drift is between minus five times the dimension
   and minus the dimension; the martingale bracket density is at most eight
   times the squared dimension. Extending the stopped integrands by zero gives
   a continuous finite martingale limit at a putative finite lifetime. The
   bounded drift therefore bounds the determinant away from zero pathwise on
   bounded time intervals. The covariance upper bound by the squared support
   radius then bounds its inverse. The parameter drift and stochastic integral
   consequently have finite limits (localize further at each pathwise bound).
   Smooth local existence at those limits excludes explosion.
5. The exponentially rescaled covariance is bounded on every deterministic
   bounded interval, hence is a true martingale. Its expectation gives the
   stated decay, initial isotropic normalization and integral of the second
   energy over the positive half-line.
6. Differentiation of the logarithmic Laplace SDE is legitimate after parameter
   stopping, uniformly on compact sets of its spatial parameter. The quadratic
   drift has exactly twice the order many singleton/co-singleton terms. The
   factor one half gives the claimed linear drift; pairing complementary
   subsets gives precisely the displayed remainder, empty at order three.
7. The marginal survival function is log-concave: the density ratio in its
   hazard representation is decreasing, with support endpoints handled by
   limits. Chebyshev at minus two and two gives the displayed exponential
   tail and hence every fixed absolute moment. Hölder and the finite
   moment–cumulant partition formula then bound each tensor entry. Summing
   over coordinates introduces an allowed dimension-dependent constant.
   Whitening bounds every energy by that constant times the directional
   covariance. Applying the same estimate to the contracted vector in each
   remainder term proves its deterministic squared-norm bound.
8. The inverse-metric noise has the minus sign displayed in the dossier.
   Cauchy–Schwarz, the tensor-slot sum, and the matrix third-moment bound give
   the stated bracket estimate with coefficients 8 and 16. It is bounded on
   every finite time interval. The remaining inverse-metric second-derivative
   terms are finite contractions of the same bounded energies, remainder and
   third-order matrices, so their drift is integrable as well. This proves
   square-integrable martingales and permits removal of stopping in expectations.
   Crucially, these estimates use fixed-dimension moment bounds, not the
   dimension-free induction that will consume the result.

The full checker and fingerprint command were run with
`uv run --cache-dir /tmp/kls-plan-uv-cache scripts/check.py`. MyST completed
without a dossier error. The full check exited 1 solely for a concurrently
authored checkpoint lacking YAML front matter:
`research/explorations/2026-10-06-bkl-analysis-reconstruction.md`.
This unrelated record-format defect was reported to the orchestrator and does
not change any reviewed statement or proof. The fingerprints above reproduce
the successful fingerprint command's output.

## Corrections

None within the reviewed proof. The unrelated checkpoint format must be repaired
by its responsible author before a clean global repository check.

## Exclusions

This report does not certify the cumulant energy inequality, the all-order
dimension-free bound, suspension, tilt criterion, or KLS. No KLS theorem,
polynomial Poincaré bound, higher-order dimension-free cumulant estimate, or
Song–Zhang implication enters the proof. No assertion about global localization
from noncompact initial laws is made. The already certified Letwin source proof
and surrounding manuscript status prose are outside this certification.

## Proposed record and handoff

```yaml
files: [research/reviews/2026-10-06-bkl-dynamics-review.md]
deltas:
  - file: research/program/ledger.yaml
    node: lem:bkl-cumulant-dynamics
    set:
      status: proved
      proofs:
        - artifact: solutions/bkl-cumulant-dynamics.md
          review: research/reviews/2026-10-06-bkl-dynamics-review.md
    preserve:
      references: [BizeulKlartagLehec2026KLS]
      depends_on: [def:bkl-tilt-cumulants, prop:letwin-kappa, thm:letwin-qcts]
```
