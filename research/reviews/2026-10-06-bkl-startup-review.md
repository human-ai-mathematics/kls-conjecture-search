---
verdict: pass
authors:
  - bkl_suspension_author, gpt-6-astra, 2026-10-06
reviewer: reviewer, gpt-6-astra, 2026-10-06
fingerprints:
  solutions/cor-bkl-uniform-conditional-initialization.md: bcea2855d4518222c35d787c73e8b5a5301658131ff36096367a7daad03e8a40
  cor:bkl-uniform-conditional-initialization: 445928a7fab5cfe614092d5368d075765390653aa5b2e4253b69281ef8c9a41a
  thm:bkl-tilt-bound: b14ed0af1b0f660928c9d507b8567b89ff97bbbd8620a138eba3fecf5aadf82f
  prop:bkl-tilt-appell-duality: 200cfcdd5bc5aed9562b945189b1ccd942730024ac955f0988db40841d86755e
---

# Uniform initialization: independent certification

## Findings

Pass for `cor:bkl-uniform-conditional-initialization`. The stronger
unconditional canonical statement follows from the dossier. It also
implies the exact candidate `cand:sz-uniform-conditional-initialization`
in `research/explorations/2026-10-04-wave-a-sz-contract.md`.
The reviewer has a fresh independent context, has authored none of
these proofs, and received only paths and a review mission. The dossier,
canonical statement, candidate and dependency records were read directly.

Both ledger dependencies are proved with passing independent reviews.
`thm:bkl-tilt-bound` was registered before this verdict on
`research/reviews/2026-10-06-bkl-suspension-kls-review.md`.
That report covers the exact coefficient bound and its ambient
normalization for singular covariance contractions. The already
certified duality gives the same full symmetric Hilbert--Schmidt
normalization for full-dimensional laws. No quantitative SZ polynomial
bound or open premise is required here.

### Proof and canonical statement

Take `A = sqrt(2K)`, using the universal constant of the certified
cumulant theorem and tilt bound. It is at least one, and
`c_d(mu) <= A^d` holds simultaneously for all positive integer degrees
and all centered log-concave covariance contractions in every dimension,
including rank zero and measures on proper linear subspaces.

The induction on lines 48--50 proves `d+1 <= 2^d` for every positive
integer d, including equality at one. Its square gives the exact
denominator estimate. All iterates are well-defined on nonnegative
arguments, and `log(e+x) >= 1` makes `ell_r(d) >= 1` for every
positive integer r. Since `1+r^(-2) >= 1`, each inequality on lines
55--58 has the correct direction. For `Gamma >= 4A`, the displayed
right side is at least `Gamma^d/4^d >= A^d`, proving the claim.

The same choice `G = 4 sqrt(2K)` works before all quantifiers over
depth, degree, dimension and measure. Since K is at least one, this
is exactly the permitted canonical choice
`max{1,4 sqrt(2K)}`. No threshold depends on depth or on the moving
degree range. Ambient Appell coefficients for singular measures are
included by the certified coefficient input rather than assumed from
the full-dimensional duality alone.

Hypotheses used are the universal exponential coefficient bound,
positive integer degree, positive integer depth, and `Gamma >= 4A`.
The measure hypotheses are precisely those of that coefficient bound.
There is no unstated hypothesis. The restriction `r >= 2` and the
inflation factor `1+r^(-2)` are stronger than this elementary proof
needs; the same estimate works for `r >= 1` even with that factor
replaced by one. This is only a sharpening observation, not a defect.
The curvature-profile premise is intentionally unused because the
claimed conclusion is unconditional.

### Exact comparison with the candidate

The candidate's quantifier order is: there exist universal G and an
integer `r0 >= 2`; for every integer `r >= r0` and every
`Gamma >= G`, a curvature-profile antecedent implies a coefficient
conclusion for every centered log-concave covariance contraction and
every integer `1 <= d < ceil(32 r^2)`. Its coefficient norm is the
full ordered-index symmetric Appell norm divided by `d!`. Its
iterated logarithm starts at the identity and repeatedly applies
`x -> log(e+x)`.

The certified conclusion uses exactly this norm, logarithm and
right-hand side. Choose `r0 = 2` and the single G above. The
corollary holds for all positive degrees, so restriction to the
candidate's strict upper endpoint gives its degree quantifier.
Its measure class is identical and includes singular covariance.
The candidate's regularity convention occurs only in its antecedent;
the stronger conclusion has no antecedent and therefore implies
the candidate regardless of whether that antecedent holds. In
particular no positive lower curvature, stronger BKL regularity,
or bound on Gamma from above is imposed on its conclusion.

This proves the candidate as a mathematical implication, with BKL
provenance. It does not prove that the older curvature-profile method
produces the coefficients independently of BKL.

### Fences and validation

The node has no `bounded_by` edge. The same universal threshold
answers the brief's uniform-admissibility requirement over the entire
moving startup range. The coefficient/KLS equivalence is not used to
prove its own premise. The input has already been established by the
cumulant-and-suspension chain without a KLS hypothesis, even though
the same upstream dossier subsequently derives KLS.

The full `uv run --cache-dir /tmp/kls-plan-uv-cache scripts/check.py`
completed with exit 0 and no MyST errors after registration of the
dependencies. The front matter is the checker's fingerprint output
for the versions examined. No source or proof step in this scope
remains unverified; beyond the certified inputs, the proof is
elementary and requires no external citation.

## Corrections

None.

## Exclusions

This certifies the stated initialization estimate and the logical
implication to the candidate. It does not establish the remaining
comparison or propagation hypotheses of a bounded-loss SZ iteration,
a new proof independent of BKL, or any structural CMH, gate-zero or
occupation claim. No research route is closed by this verdict.

## Proposed registration and candidate record

Set `cor:bkl-uniform-conditional-initialization` to `proved`, retain
its current dependencies, and add:

```yaml
proofs:
  - artifact: solutions/cor-bkl-uniform-conditional-initialization.md
    review: research/reviews/2026-10-06-bkl-startup-review.md
```

The orchestrator may append a checkpoint with
`closes: [cand:sz-uniform-conditional-initialization]`, recording
promotion to the stronger proved canonical corollary and citing
this report. Preserve the independent-proof objective of
`ap:sz-conditional-initialization`; closure of the candidate's
mathematical assertion does not close that method objective.
