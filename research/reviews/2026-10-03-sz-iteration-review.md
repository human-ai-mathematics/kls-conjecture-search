---
verdict: pass
authors:
  - researcher-curvature, gpt-6-astra, 2026-10-03
reviewer: reviewer, gpt-6-astra, 2026-10-03
fingerprints:
  solutions/thm-sz-iterated-curvature.md: 74577ac285681736e1b62e14e49bef090275073471f24c9c5cb4f3b02ab45a94
  thm:sz-iterated-curvature: e1c597ce3da1e94ebc6e1fbde16ce86114991cd711e6eb3f7a9550bb161fdef8
  lem:sz-analytic-foundations: e3b0250c18499cbdf58b3cb609937032b0101d8aa096aac355555309e5e94d3f
  thm:sz-polynomial-variance: ffd52798e616ccd22bb3e4c78d5c382fd5657d3b598e6e4ec3c9afc4f696da8e
  thm:sz-curvature-comparison: 9baf9221ded7767fc4a904b4a582b9804ab1d424bb87914745aaaa6dd0242787
---

# Iterated curvature: independent review

## Findings

The frozen dossier proves `thm:sz-iterated-curvature` in
`modules/32-polynomial-curvature.md`. This reviewer was launched in a fresh
context without the authoring conversation and neither wrote nor directed the
proof. The author identity is supplied by the assignment. The source proof,
dossier, canonical statements and dependency records were independently read.

### Statement, hypotheses and dependencies

The canonical and dossier statements agree: one universal envelope $C_0 4^r$
works at every finite integer depth, in every dimension, for centered regular
measures with covariance at most $I$ and both displayed Hessian bounds.
Smoothness, positive lower curvature, finite upper curvature, log-concavity,
centering and the covariance bound are used. Continuity is required only for
the auxiliary profile-inflation lemma and holds for each iterated profile.
Compact support and positive covariance in the localization argument are
intermediate restrictions removed before completing each degree induction.
There are no unstated hypotheses or identified unused stated hypotheses.

All three recorded dependencies are certified. Their statements supply the
scalar stability and regular analytic class, the all-degree Appell bound and
its certified localization/hierarchy lemmas, and the exact curvature comparison
with threshold $R\ge2^{40}\epsilon^{-2}$. No open dependency, antecedent, or
`bounded_by` edge occurs.

### Steps checked

1. The convolution conditional-covariance formula gives lower Hessian
   $a/(1+at)$ and upper Hessian $t^{-1}$. Rescaling produces the stated $a_t$.
   Continuity and the common bound $F(a)+\zeta$ permit scalar stability. For
   $M=A+\delta B^{-1}$, inversion and congruence give the required curvature
   without commuting matrices. The chain rule gives exactly the weighted energy.
2. The scaling and logarithmic-derivative inequalities hold for all required
   arguments, including depth zero in the latter. The reciprocal-square
   convolution includes its endpoint, and the adjacent-degree ratio includes
   degree one with $b_0=1$.
3. Lower-degree bounds apply simultaneously to all whitened posteriors.
   Appell expansion and Minkowski on the full tensor output give (5), inserting
   covariance in every new derivative slot. The initial data and finite-maximum
   integral inequality give $2308=4+9\cdot256$ and the bound (6).
4. Bessel gives variance survival. Expanding the square verifies the inverse
   integral inequality. The tower step uses fixed derivative products and an
   earlier measurable covariance; it preserves their correlation. Compact
   support justifies the expectations and time integrals. Substitution in (9)
   closes the coarse induction since even replacing $e^2$ by $8$ keeps
   $16\cdot2e^2\cdot257\cdot100<2^{24}$.
5. Conditioning, whitening and fixed-order moment convergence pass both the
   moments and Appell coefficients to the limit. Affine contraction bounds
   Hilbert--Schmidt norms; restriction to the affine support handles singular
   covariance (a point mass has zero positive-degree Appell variance).
6. Variation of constants with zero lower-order initial data gives (10).
   Separating the top derivative gives $A(\eta)=1+O(\sqrt\eta)$ with a
   universal constant. Taking $\eta=c r^{-4}$ makes its logarithmic cost at
   most $\alpha/2$. The remaining iterated-log ratio is bounded independently
   of degree and costs $\alpha/4$ after squaring; the degree denominator costs
   at most $\alpha/8$. Thus $7\alpha/8\le2\log(1+\alpha)$ closes the step.
7. Every degree below $D_r$ is initialized using the universal polynomial
   theorem, with $K\ge128\cdot33$. The induction consequently never presumes
   its desired estimate at an uninitialized smaller degree.
8. The first dyadic comparison supplies depth one independently of the final
   conclusion. Coarse induction supplies every fixed preliminary depth. At
   large depth, the dyadic choice yields the curvature cost $e^{\alpha_r}$
   and the log-ratio cost stated in the proof. Taking square roots gives
   $4e^{3/r^2}$. A single finite initial constant dominates both polynomial
   thresholds divided by $4^r$ for all later depths. Summability of $r^{-2}$
   and a finite enlargement for the initial depths give the universal envelope.
   The quantifier order is finite-depth induction, not an infinite-depth limit.

### Sources and build

The proof of Section 6 of [Song--Zhang v1](https://arxiv.org/src/2610.01447v1)
was checked directly in `/tmp/kls-song-zhang-source/20_upper.tex`, including
the coefficient feedback, summable loss and depth induction. Its statements
alone were not treated as evidence.

The smooth Brascamp--Lieb input was checked in the actual text of
[Bakry--Gentil--Ledoux, Theorem 4.9.1](https://dokumen.pub/analysis-and-geometry-of-markov-diffusion-operators-9783319002262-9783319002279.html).
The inverse-Hessian bound implies the constant-curvature version; the
convex-potential approximation and finite-energy extension are written in the
certified polynomial dossier and apply to the conditional law here. The 1976
citation is historical attribution; the supplementary published source
supplies the checked theorem.

The full `UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py` passed with
no MyST errors. The frozen dossier was reread after its final citation and
transcription changes; the fingerprint command then completed successfully
and supplied exactly the block above. No numerical artifact was used.

## Corrections

None outstanding. The draft's missing mathematical spacing command was
corrected before this frozen review.

## Exclusions

This report does not re-certify the three prerequisite proofs, the transfer
or main theorem, any exponential-coefficient equivalence, CMH, occupation
estimates, or dimension-free KLS. The growing admissibility thresholds are
paid by an exponentially growing sequence, not a bounded sequence. No step
within the stated scope remains unverified.

## Certification delta

Set `thm:sz-iterated-curvature` to `proved`, retain its three current
dependencies and source reference, and add:

```yaml
proofs:
  - artifact: solutions/thm-sz-iterated-curvature.md
    review: research/reviews/2026-10-03-sz-iteration-review.md
```
