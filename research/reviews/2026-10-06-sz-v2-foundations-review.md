---
verdict: pass
authors:
  - sz_v2_inner, gpt-6-astra, 2026-10-06
reviewer: reviewer, gpt-6-astra, 2026-10-06
fingerprints:
  solutions/sz-v2-inner-foundations.md: 6f1d7f796d88d606872f0c030662b811bd722d3a3c4c0d1929b9decd8b028c6a
  prop:sz-v2-static-coefficient-transfer: bc15d851517e3f5214ddf15d70fc42328b860a6b0d5655ba0898aa0ee1d040c0
  def:sz-v2-common-radius: 49ae12dc3b61656251736c6d98ed212477348fbfdcfcb5ce82c490131854c2b7
  lem:sz-analytic-foundations: e3b0250c18499cbdf58b3cb609937032b0101d8aa096aac355555309e5e94d3f
  thm:sz-polynomial-variance: ffd52798e616ccd22bb3e4c78d5c382fd5657d3b598e6e4ec3c9afc4f696da8e
  lem:sz-v2-joint-frame: aaf5c36182ce8cdc5e342504d9f86ea34e8ed764bf63b01f6b3ad29edbb1bc2d
  lem:sz-v2-skew-credit: e9510673a1e46fd5d998b3b77b212371ad779546264a1b2f0db5a68e585ea5c3
---

## Findings

Independent full certification of `solutions/sz-v2-inner-foundations.md` for
`prop:sz-v2-static-coefficient-transfer`, `lem:sz-v2-joint-frame`, and
`lem:sz-v2-skew-credit`: **pass for all three**. This reviewer received repository
paths and a review mission in a fresh context, without the authoring conversation.
Each dossier theorem implies its canonical statement, with the same quantifiers,
dimension range, constants, and ordered-index tensor normalization.

I read the actual proofs in the supplied local rendering of arXiv:2610.01447v2
(` /tmp/kls-sz-v2.html ` and its text extraction `/tmp/sz-v2.txt`): Lemma 6.6,
Lemmas 6.11–6.14 and Theorem 6.15, Lemmas 6.25–6.26 and Proposition 6.27,
and the generic transfer in Proposition 8.3. These arguments were checked,
not imported merely on the strength of their statements. The source's special
block-radius premise is used only to provide the coefficient premise; the
dossier legitimately retains that premise directly and needs no block-radius
construction.

### Static coefficient transfer

The affine posterior normalization is valid without commuting covariance and
precision: $M\succeq\delta\Lambda^{-1}$ implies
$M^{1/2}\Lambda M^{1/2}\succeq\delta I$. The Appell expansion has exactly
the coefficient $\sqrt{K_k}/k!$ on the full ordered derivative tensor.
Componentwise estimates and Minkowski give the claimed Hilbert-valued version
without an output-dimension loss. Gaussian convolution and rescaling have
the displayed lower curvature and upper Hessian bounds. Continuity of the
coefficient profile passes each finite-degree inequality to the nonsmooth
posterior. Monotonicity of a general profile is unnecessary at this step.

The localization construction, covariance-noise estimate $\sum_iS_i^2\preceq8I$,
and posterior martingale identities are supplied by the certified polynomial
dossier. I checked the new accumulated-metric calculation independently:
$C^TC\preceq I$ gives the noise contraction, tensor-slot pair terms contribute
$8\binom j2$, and the metric/mean cross variation contributes at most
$N_j+8j^2L_j$. Including the mean quadratic variation gives (2). Compact
support bounds the actual stochastic integrands through the stated Bessel
and noise estimates, so stopping does not leave an expectation error.

In (3) the old output slots retain $M_t$ and only newly differentiated slots
are enlarged from $A_t$ to $M_t$. All comparisons occur at the same time.
The weights $w_0=w_1=1$ and $w_l=A^{2(l-1)}$ for $l\ge2$ give the
Gronwall and zero-initial-value estimates (4). The square expansion for the
inverse precision is exact. The choices of $\tau,s,\delta$ give the stated
$14\varepsilon$ and $5\varepsilon$ exponents. In particular, the lower
terminal terms have power $A^{d-2}$, including the endpoint $k=d-1$;
there is no lost factorial or exceptional degree-two initialization.

The variance martingale lower bound yields (5). With
$g(x)=\log(e+x)$, its logarithmic elasticity is at most $1/2$; iterating
this estimate gives (6) uniformly in degree and amplitude. For
$\varepsilon=2^{-20}r^{-4}$, the two normalized contributions are at most
$1-r^{-2}/8$ and $r^{-2}/128$. Thus one universal depth threshold closes
the induction for every $\Gamma\ge1$. Conditioning and affine normalization
pass the estimate at each fixed degree; no supremum over degrees crosses a
limit. Singular measures reduce to smaller supporting dimensions, with a
point mass trivial. This respects both allowed dimension ranges.

### Joint partial symmetrization

The subset up/down identity gives the harmonic decomposition and dimensions.
The $s+1$-dimensional commutant proves irreducibility, real scalar commutants,
and inequivalence, so the subgroup average is rank one precisely in the
listed harmonics. The inclusion singular value and transitivity calculation
give (8), also beyond the middle level by complementation. Taking invariants
under the last half and subtracting successive subset modules gives the
multiplicity-one local branching used in (11).

I checked the two branching weights, the $j=2$ and $j=3$ expressions, and
the bounds $h\ge4w_0$ and $h\ge w_1$ for every $2\le j\le m$.
The Schur minimizations are finite because their eliminated blocks equal
the already positive shifted frame on the kernel of $P_m$. The operators
preserve the last-half invariant sectors and the relevant local sectors;
the rank-one perturbation is zero on their orthogonal complements.
Restriction multiplicities in arbitrary ambient representations do not
alter the induction, since it is asserted for every representation.

Eliminating the positive blocks gives (11), and the rank-one inverse formula
gives (12). For $j=1$ it reduces exactly to the displayed recurrence for
$b_{2m}$. The error above $2b_m$ is bounded by
$96c^2/(1-12c)\le c$. For higher harmonics the bound
$D_{m,j}\ge w_0+h/(9m)>0$ and the lower estimate for $a_{2m,j}$ close
the strengthened induction. The cases $m=1$, the trivial representation,
and $j>m$ have the asserted boundary values and are positive after the final
$2m$ contribution. This proves the constant $10^4$ at every dyadic scale,
including finite direct sums.

### Skew normalization credit

The analytic foundations ensure a positive spectral gap on the centered
space, hence finite positive $e$ and $\beta$. Linear functions belong to the
form domain. For a unit skew matrix, $V=CX$ has energy one and is form
orthogonal to $U$ by symmetry of $\mathbb E\nabla U$. The pairing of
$H^{-1/2}U$ with $H^{1/2}U$ is one, so its orthogonal residual has squared
norm exactly $\beta^{-1}-e^{-1}$. Duality over skew matrices is the
Hilbert–Schmidt norm of $(LU-(LU)^T)/2$; it introduces no factor two.
The direct-sum version uses jointly normalized collections of skew matrices.
In dimension one the skew part vanishes and spectral Cauchy–Schwarz gives
the nonnegative right side. No $HU\in L^2$ hypothesis is needed.

### Hypotheses, dependencies, and build

The transfer uses the uniform regular coefficient premise at every lower
curvature bound and degree, log-concavity, the covariance normalization,
positive integer degree, and integer logarithmic depth above a universal
threshold. Compact support and nondegeneracy are temporary, removed as
proved. The frame uses only a finite-dimensional real orthogonal permutation
representation and positive dyadic scale. The skew argument uses centered
unit form-domain vectors, symmetry of their mean gradients, finite coordinate
second moments, and the analytic spectral gap. The upper Hessian bound enters
through the established analytic setting; the covariance upper bound is
actually unused in the skew estimate, a harmless possible strengthening.
There are no unstated hypotheses affecting the conclusions.

The existing direct dependencies are defined or proved. The localization
and nonsmooth Brascamp–Lieb inputs used here are explicitly present in the
certified analytic/polynomial dossier. No open dependency is used and no
`bounded_by` edge applies. The transfer is a proved implication with its
coefficient premise still visible, not a certification that the premise holds.

The full `UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py` completed
with exit status zero and no MyST errors. The dossier's dependency paragraph
was corrected during the review to remove unused curvature inputs; I reread
the complete current dossier and repeated the fingerprint command afterwards.
The fingerprints above are its output. No proof step remains unverified
within this scope.

## Corrections

No mathematical correction is required. The symbol $g$ in (6) is the
one-step logarithm $g(x)=\log(e+x)$; explicitly declaring it would improve
readability, but its meaning and the checked calculation are unambiguous.

## Exclusions

This report does not certify the inner curvature iteration, operator-block
construction, dimension theorem, retained-bound iteration, or KLS conclusion
of SZ v2. It neither imports BKL nor uses the already proved KLS endpoint or
coefficient bounds derived from it. It does not independently re-certify the
entire existing analytic/polynomial dossier or conduct a global prose audit.

## Proposed proof records

For each of `prop:sz-v2-static-coefficient-transfer`, `lem:sz-v2-joint-frame`,
and `lem:sz-v2-skew-credit`, set `status: proved` and add:

```yaml
proofs:
  - artifact: solutions/sz-v2-inner-foundations.md
    review: research/reviews/2026-10-06-sz-v2-foundations-review.md
```

Retain their existing `references` and `depends_on` fields. No new
`assumes`, `bounded_by`, or `refuted_by` relation is warranted.
