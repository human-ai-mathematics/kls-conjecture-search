---
verdict: pass
authors:
  - wave_a_survival_repair, gpt-6-astra, 2026-10-04
reviewer: reviewer, gpt-6-astra, 2026-10-04
fingerprints:
  solutions/lem-survival-implies-kls.md: 0e20e1bdd49bfd2ce4437232af0d0046c3f404e54d1238eca107722f558f9333
  lem:survival-implies-kls: fcc0ff284f00b4f7d903900409e37db884463ad15f1f7cbb2c48ecb254e4cc64
---

# Independent certification of the standalone survival repair

## Findings

**Pass for [](#lem:survival-implies-kls), using the standalone dossier only.**
This is a full independent review of the new argument, not a retention or hash
refresh of the historical core certification. The reviewer received a fresh
context containing the mission and artifact paths, without the conversation
that authored or directed the proof. The earlier revise report and repair
checkpoint were read as scope records; all proof steps were checked anew.

The dossier theorem implies the canonical statement with the explicit universal
constant $c=\sqrt{2/\pi}$. Its cut, survival event, positive deterministic time,
and uniform KLS consequence have the canonical quantifiers. The node has no
`depends_on`, `assumes`, or `bounded_by` edges. No open result is used as a
proved dependency. The event remains a displayed antecedent, not a new claim
of uniform survival.

### Measurable sets and localization

Dossier lines 17–116 correctly preserve the actual set in neighborhoods, while
using Borel representatives only for integrals. Positive finite likelihoods
give equivalence of all finite-time posteriors and the original law, including
their completions. The Gaussian bridge argument identifies conditioning on the
whole observation history with conditioning on its endpoint. The innovation
has zero conditional increments and quadratic covariation $tI$; finite first
moment supplies the required integrability. Thus this conditional-law model
has the usual localization law, and each fixed indicator mass is a bounded
martingale.

Since $E\subset E^r$, the neighborhood increment is nonnegative and its
expectation is the original increment. Left continuity of the neighborhood
mass proves that rational radii compute each infimum and the full lower
limit, establishing measurability. When the initial lower content is finite,
a deterministic decreasing sequence realizes it. The pointwise full-liminf
inequality followed by Fatou has exactly the asserted direction. Infinite
initial content needs no estimate. None of these steps identifies Minkowski
content with reduced-boundary perimeter or assumes boundary regularity.

### Curvature comparison and its extension

The actual published smooth input was checked in
[Bakry–Ledoux, Inventiones Mathematicae 123 (1996), Corollary 2.2, equation
(2.10), p. 267](https://www.math.univ-toulouse.fr/~ledoux/LevyGromov.pdf).
For the Euclidean diffusion, its carré du champ is $|\nabla f|^2$ and the
Hessian lower bound supplies curvature $\kappa$. The equation has precisely
the dossier's $\sqrt\kappa$ factor. Equation (2.11), p. 268, also confirms
the lower outer Minkowski convention. Only the functional inequality is
imported; the nonsmooth extension is proved inside the dossier.

Lines 145–206 give a valid curvature-preserving approximation. The affine
minorant makes each Moreau minimization coercive; strict convexity gives a
unique minimizer. Monotonicity of subgradients yields the Lipschitz residual
map and hence the stated gradient bound. The minimizers approach the fixed
point whenever the envelope values remain bounded, so lower semicontinuity
gives convergence even where $W=+\infty$. Centered mollification preserves
convexity, the Hessian upper bound, and the affine lower estimate. Local
approximation error tends to zero. The common Gaussian-affine majorant is
integrable, and normalization therefore gives $L^1$ density convergence.

The smooth approximations have globally Lipschitz drift, finite invariant
probability and strictly positive curvature, so the imported diffusion
inequality applies. Cutoff and mollification extend it to bounded Lipschitz
tests: gradients converge almost everywhere under mollification with a common
bound, and the cutoff derivative contributes at most $C/R$. For a fixed test,
all three integrands are bounded and the density limit passes the inequality.
There is no assertion of continuity of perimeter under total variation.

Lines 208–227 correctly distinguish the case of positive closure mass excess,
which has infinite content, from the case of equal masses. In the latter,
distance cutoffs tend to the closure indicator; their gradients vanish almost
everywhere on their zero and one level sets and are bounded by $1/r$ elsewhere.
Absolute continuity therefore gives the stated neighborhood bound. Dominated
convergence on the left and the lower limit on the right prove the set
inequality for completed-measurable sets as well. The chord from zero to the
Gaussian profile's midpoint gives exactly $\sqrt{2/\pi}$.

### Survival and the uniform consequence

The posterior potential is the original extended convex potential minus a
linear term plus $T_0|x|^2/2$. Hence the just-proved comparison applies directly
to each original posterior. Combining it with the expectation inequality and
the event lower bound proves the claimed individual estimate without changing
the stochastic experiment.

The profile input was checked in
[Milman, Corollaries 6.12 and 6.5, with Theorem 1.8 and Section 6](https://arxiv.org/pdf/0712.4092).
The definition on p. 2 is the same exterior lower Minkowski content.
Corollary 6.12 covers every absolutely continuous log-concave probability on
Euclidean space, including nonsmooth densities and dimension one, and gives
interior concavity. Corollary 6.5 gives symmetry from interior continuity.
This is an established published import: the
[author's publication list](https://emilman.net.technion.ac.il/publications/)
records Inventiones Mathematicae 177 (2009), 1–43; the arXiv PDF is the
accessible source text, not a new preprint being certified here.

A completed-measurable set contains a Borel subset of equal mass whose
neighborhoods are smaller, so the two profile infima coincide. The balanced
premise bounds the midpoint infimum without requiring a minimizer. The
interior-$\varepsilon$ interpolation in lines 264–277, followed by symmetry,
gives $h_\mu\ge2\sqrt{2/\pi}\,c_0b_0\sqrt{T_0}$. No endpoint continuity is
used, including in dimension one.

### Hypotheses and validation

Used hypotheses are full-dimensional log-concavity, finite first moment, a
fixed deterministic completed-measurable cut, the usual posterior, finite
positive deterministic time, and the displayed positive-constant survival
premise. Isotropy supplies the first two properties and specifies the KLS
class; its normalization is unnecessary for the individual boundary estimate.
There is no unstated smoothness, compact-support, finite-perimeter, occupation,
or infinite-time uniform-integrability hypothesis. Impossible choices such as
$b_0>1/2$ or $c_0>1$ make the premise vacuous.

The full `uv run scripts/check.py` completed with exit code zero and no MyST
error. The fingerprint command was run again immediately before this report;
both fingerprints above were unchanged. The checks used the approved
escalated execution path. No numerical artifact is used as proof evidence.

## Corrections

None. All four repair requests in
`research/reviews/2026-10-04-wave-a-survival-independent.md` are resolved by
the new standalone proof, including the source identification and the
endpoint-free balanced-profile deduction.

## Exclusions

This certifies only [](#lem:survival-implies-kls) through
`solutions/lem-survival-implies-kls.md`. It does not certify the shared core
dossier, its other header nodes, downstream proofs, or any Riccati, covariance,
occupation, or moving-family perimeter assertion. It proves neither the
universal survival premise nor KLS itself. No earlier report is amended or
deleted, and no statement or ledger file was edited by this reviewer.

## Handoff

```yaml
files:
  - research/reviews/2026-10-04-wave-a-survival-repair-review.md
deltas:
  - path: research/program/ledger.yaml
    node: lem:survival-implies-kls
    replacement: |
      - id: lem:survival-implies-kls
        status: proved
        proofs:
          - artifact: solutions/lem-survival-implies-kls.md
            review: research/reviews/2026-10-04-wave-a-survival-repair-review.md
```

The replacement has empty dependency, antecedent and fence lists (omitted
fields), and replaces the historical shared-core proof record for this node
only. Other nodes' records remain outside this review's scope.
