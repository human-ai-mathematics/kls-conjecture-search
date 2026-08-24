# A4/A5 independent-agent proof audit

- **Date:** 2026-08-21
- **Proof author:** `/root/a4_a5`
- **Independent reviewer:** `/root/review_a4_a5`
- **Certification:** `checked_by: agent`
- **Verdict:** pass for the eleven nodes listed below

## Certified scope

### A4

1. `eq:a4-mean-dual` — exact extended-valued unrestricted posterior-mean dual.
2. `prop:a4-mean-local` — exact entropy-localized mean-tilt formula and its covariance limit.
3. `prop:a4-local-wellspecified` — well-specified tangent generalized-eigenvalue laws.
4. `prop:a4-local-misspecified` — raw misspecified baseline and generic square-root correction.
5. `prop:a4-local-excess` — optimizer-centered excess-KL generalized-eigenvalue laws.
6. `ex:a4-gaussian-local` — exact fixed-covariance Gaussian calibration.
7. `lem:a4-symmetrization` — invariant-observable, KL, and Wasserstein effects of group averaging.

### A5

1. `prop:a5-ratio` — invariant/non-invariant restricted-gap decomposition.
2. `prop:a5-block-stability` — density-ratio stability of both symmetry blocks.
3. `ex:a5-gaussian-crossover` — exact centered/noncentered Gaussian crossover.
4. `prop:a5-partial-gaussian` — the exact scalar partial-noncentering optimizer.

Each certified claim points to a standalone TeX dossier under `solutions/`. The final dossiers
identify `/root/a4_a5` as author and `/root/review_a4_a5` as the distinct reviewer.

## Checks performed

For A4, the review checked the Gibbs/Donsker--Varadhan duality step, attainable exponential
tilts, endpoint conventions, uniform cumulant expansion, compact isolation of local KL
sublevels, well-specified and misspecified ratio expansions, optimizer-centered normalization,
the exact Gaussian formulas, and both convexity arguments in the symmetrization lemma. For A5,
it checked orthogonal symmetry-block decomposition with extended reciprocals, density and
variance comparison on fixed blocks, ordering margins, the two Gaussian precision matrices, and
fixed-determinant trace minimization for partial noncentering.

The review required explicit compactness/continuity/separation in the local sublevel contract,
corrected two missing signs in the misspecified expansion, and corrected minor TeX/provenance
defects. No substantive gap remains for the certified statements under their displayed
hypotheses.

## Explicit exclusions

This report does not certify `prop:a4-logistic-global`, `ex:a5-folding`, `ex:a5-z2-bridge`, or
`conj:a5-metastable`. The first A5 audit also excluded `ex:a5-neal` and
`prop:a5-partial-funnel` pending a second independent check of their newly supplied
Poincaré-to-exponential-integrability lemma. That later check is recorded separately in
[`2026-08-21-a5-funnel-second-agent-audit.md`](2026-08-21-a5-funnel-second-agent-audit.md).
