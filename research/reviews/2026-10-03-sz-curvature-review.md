---
verdict: pass
authors:
  - researcher-curvature, gpt-6-astra, 2026-10-03
reviewer: reviewer, gpt-6-astra, 2026-10-03
fingerprints:
  solutions/thm-sz-curvature-comparison.md: ee01afb7899f542cde9741e7095f19927a4e634b682528d0c588c6dca7a907b6
  thm:sz-curvature-comparison: 9baf9221ded7767fc4a904b4a582b9804ab1d424bb87914745aaaa6dd0242787
  lem:sz-analytic-foundations: e3b0250c18499cbdf58b3cb609937032b0101d8aa096aac355555309e5e94d3f
  thm:sz-polynomial-variance: ffd52798e616ccd22bb3e4c78d5c382fd5657d3b598e6e4ec3c9afc4f696da8e
---

# Curvature comparison: independent review

## Findings

The dossier proves `thm:sz-curvature-comparison`, now located in
`modules/32-polynomial-curvature.md`. The review context was originally
launched without authoring history. Earlier assignments were independent
source synchronization and review of its two dependencies; this reviewer
neither authored nor directed the construction of this proof. The assignment
supplied the author identity above. The proof was reconstructed from the
frozen dossier and the pinned source, not from the author's account.

### Statement and inputs

The canonical statement and dossier agree on the regular centered law,
covariance bound, all-degree coefficient hypothesis, monotone profile,
threshold $R\ge2^{40}\varepsilon^{-2}$, dyadic degrees, and constant
$16(1+\varepsilon)$. Both use the full ordered-index Hilbert--Schmidt norm
and Appell coefficients divided by $k!$. The supremum in the dossier is
understood on the symmetric tensor space on which its Appell map is defined.

The two ledger dependencies are now proved and are used exactly as stated:
`lem:sz-analytic-foundations` supplies spectral calculus, the first
eigenfunction, form tests, and Bochner's identity; `thm:sz-polynomial-variance`
supplies $c_k\le32^k k!$ including covariance contraction. There is no open
dependency, no `assumes` antecedent, and no `bounded_by` edge. The polynomial
profile hypothesis is an explicit hypothesis of this theorem, not an
assertion that the profile holds for arbitrary laws.

Hypotheses used are finite dimension, a smooth probability density, positive
lower and finite upper Hessian bounds, centering, covariance at most the
identity, $0<\varepsilon\le1$, monotonicity and lower bound one for $\ell$,
the stated threshold for $R$, and the coefficient estimate for every degree.
All analytic restrictions are retained in the conclusion. No uniform lower
curvature across laws is used. No unused hypothesis was identified.

### Mathematical checks

1. The centered-gradient map $D=P_+\nabla H^{-1/2}$ is a contraction.
   Testing against coordinate functions gives the asserted relation between
   the mean gradient and the coordinate map. For a whole finite tensor
   family, the normalization $\beta=\|u\|_2^2/\|H^{-1/2}u\|_2^2$ and
   excess $\chi=\langle u,Hu\rangle-\beta\|u\|_2^2$ give the displayed
   energy and defect identities by spectral calculus. The same scalar is
   frozen when permutations and differences of that family are considered.
2. Centering removes exactly $p_j$. Bochner's identity subtracts
   $a v_j+\chi_j$ from the next energy. Subtracting $\lambda v_j$ and
   telescoping gives $aV_N+X_N\le\lambda P_N$, with all excesses
   nonnegative. Applying the first step separately gives
   $a\le\lambda p_0\le\lambda^2$, including a zero successor. Operator
   domains follow from the analytic input; subsequent weak Hessians are
   justified before they are used.
3. The two-block recovery lemma is proved in the dossier. On subset levels,
   the up/down commutator is $(N-2k)I$. Orthogonal harmonic decomposition and
   repeated raising give the squared singular values
   $\binom{q-j}{s-j}\binom{N-s-j}{q-s}$. Their successive ratio is at
   most one, so the minimum is $\binom{N-2s}{q-s}$. The range
   $s\le q\le l$ ensures all factorials and raising steps are valid,
   even when $q>N/2$. Embedding the tensor as its list over $s$-subsets
   turns incidence summation into $\binom qs$ times block symmetrization.
   Counting the copies of each tensor norm gives exactly the stated
   recovery coefficient. The argument is unchanged for finite
   Hilbert-valued entries.
4. The approximate recovery estimate is the triangle inequality applied
   before and after projection. In insertion sorting, any neighboring swap
   is used at most $l$ times. Telescoping a product of permutation operators
   bounds each term by the defect of the original tensor, so it does not
   assume that intermediate permutations have the same adjacent defects.
5. The Appell testing identity follows by form integration by parts and
   the expected-derivative identity. Polynomial tests belong to the form
   domain by Gaussian tails from the positive curvature. The inverse square
   root and centered-gradient maps act in their stated domains. The newest
   swap is a symmetric weak Hessian plus a remainder of norm
   $2\sqrt{\chi_j/\lambda}$. A swap in slots $a,a+1$ of $u^J$ was created
   from $\chi_{J-a}$ and undergoes exactly $a-1$ later maps. Each map has
   norm at most $\sqrt b$ and commutes with the old permutation. This proves
   equation (4) without differentiating an old defect.
6. At a dyadic step, there are at least $Lk$ available derivative slots.
   The block coefficient is at most $B^k$; the testing coefficient is
   $(b\lambda)^{k/2}k!/(2k)!$. The preceding degrees sum to $k-1$ and
   factorials telescope. Multiplication of the stage error gives exactly
   $t_k=(4Lk/B)J^{k/2}c_k\lambda^{(k-1)/2}$. Terminal terms have an
   extra factor $1/B$ which is safely dropped. All defect indices are
   nonnegative at $j=m_d$, including $d=2$.
7. The chosen $L,p_*,b$ give $\log(J/16)\le3\varepsilon/32$,
   $J/C\le1-3\varepsilon/8$, and $A/C\le1/3$. The startup count for
   degree $k$ is $(L+1)k/2$. A single nonnegative lag kernel and weighted
   Cauchy--Schwarz bound the full error sum by $W_*^2X_N$; there is no
   factor depending on overlapping intervals or iteration length.
8. Splitting at $k_0$ uses the factorial estimate below $k_0$ and the
   hypothesized profile above it. The small-degree series is evaluated by
   the generating function for $\sum k^3x^k$; its contribution is at
   most $2^{-15}$. The geometric tail is at most
   $2^{17}\varepsilon^{-3}(\varepsilon/2)^{192}<1/8$.
   Thus $2\lambda W_*^2\le1/8$. The analogous startup series uses
   $\sum k^5x^k$ and yields $\delta_d\le p_*/16$. These bounds follow
   analytically from the displayed threshold, with no numerical evidence.
9. The stopping argument assumes the contrary curvature lower bound and
   chooses $M=\lceil\lambda/a\rceil$. Before a first exit of $P_N$ past
   $p_*/2$, the single-step bound $p_j\le\lambda\le p_*/2$ ensures
   $P_j\le p_*$. Hence $v_j\ge1-p_*$ and the successor has positive
   norm before any normalization is performed. This validates
   $\beta_j\le b\lambda$ on the needed prefix, rather than assuming it
   to construct that prefix. Absorption then gives $P_N\le p_*/7$,
   excluding the exit. At $M$, $aV_M\ge(1-p_*/6)\lambda$ contradicts
   $aV_M\le\lambda P_M<p_*\lambda/6$.
10. Substituting the coefficient bound and $A/C\le1/3$ into the resulting
    inequality gives the required $(d+1)$st power bound. The complementary
    large-gap case supplies the maximum with one. This checks the precise
    exponent $a^{-1/(d+1)}$, not an asymptotic substitute.

### Source and build

The actual proof of Section 5 of
[Song--Zhang, arXiv:2610.01447v1](https://arxiv.org/html/2610.01447v1)
was independently read and compared with the local source
`/tmp/kls-song-zhang-source/20_upper.tex`. The dossier reconstructs the
incidence and analytic estimates rather than using the preprint's theorem
as an unproved input. No additional external mathematical theorem beyond
the two certified dependencies is needed.

The fingerprint command completed successfully with the block above. A
subsequent full `UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py`
completed with exit code zero and no MyST errors. The moved canonical
statement was reread in its new module; its fingerprint is unchanged.

## Corrections

None outstanding. Four malformed dyadic sum qualifiers in the draft were
repaired by the author before freezing; the repaired expressions were
reread before this report. No mathematical repair was required.

## Exclusions

This report certifies only the curvature comparison. It does not certify
the iterated-curvature theorem, the exponential-coefficient equivalence,
the final all-law localization transfer, `thm:song-zhang-kls`, or `conj:kls`.
It gives no CMH or occupation estimate. The lower threshold for $R$ remains
part of the theorem and cannot be discarded during iteration.

## Certification delta

Set `thm:sz-curvature-comparison` to `proved`, retain dependencies
`[lem:sz-analytic-foundations, thm:sz-polynomial-variance]` and the source
reference, and add exactly this proof record. No other transition follows.

```yaml
proofs:
  - artifact: solutions/thm-sz-curvature-comparison.md
    review: research/reviews/2026-10-03-sz-curvature-review.md
```
