---
verdict: pass
authors:
  - bk_hodge, gpt-6-astra, 2026-10-06
  - bk_powers, gpt-6-astra, 2026-10-06
  - orchestrator, gpt-6.1-sol, 2026-10-06
reviewer: reviewer, gpt-6-astra, 2026-10-06
fingerprints:
  solutions/lem-bk-compatible-hodge.md: ec7068a9fcb594e496856ebf37d8009e48e4c91658d2db134c780b9cbccd7e2a
  lem:bk-compatible-hodge: 873b1664cb0ff515fc68ba5c4810258f4eed9b09a6649af529e457d6260ed52e
  def:bk-compatible-calculus: b0bb2905e0f3e30702cd0c5d9d3ff881d59ec3fa87175e4d2b50222b5e865ed1
  solutions/prop-bk-integration-calculus.md: 43576eab721128bee252523fdc841f3b323aa5ed626ddb8813f62d9d2a5a169a
  prop:bk-integration-calculus: 591a8826b560d20e268b65a430aff427ed03b6c8f4b9b03c53272f31dac7b2c4
  def:bk-uniform-appell-coefficients: 0e3be6061878fe05162d23613514cc2211cad0df63d76393c5957b3444776c95
  solutions/lem-bk-uniform-power-bound.md: 60576202137a0af40b4b48d1d2c1ba09f948eb458efb39c03140d34e9c83f8d8
  lem:bk-uniform-power-bound: f29a142254b33ded1c91d84c64d83e2c4814b144d044988e0aa5f6eccf0e802d
  cor:bk-integration-powers: 0d4acc3094b4e0924c4b2342a8bab98ec5b034379f27349fa41a5636c456241e
  cor:bk-quadratic-seed: 85191ed8fa8e019fde7612511ca5d9a87b47a18b1f7269bbe2d575e398864cd3
  thm:letwin-qcts: 8e2ac0819f46db553fe83a6f3034436816565262316c2e6bde7d81baead1a082
---

# BK operators: independent grouped certification

## Findings

**Pass** for all five nodes: `lem:bk-compatible-hodge`,
`prop:bk-integration-calculus`, `lem:bk-uniform-power-bound`,
`cor:bk-integration-powers`, and `cor:bk-quadratic-seed`.
The three dossiers in the fingerprint block prove the corresponding canonical
statements. The Hodge and calculus nodes, currently open, are proved within this
grouped chain, not accepted as open premises. Promote the five nodes together
(or in their dependency order). The only substantive dependency outside the
group is the already certified `thm:letwin-qcts`; definitions supply conventions.
There are no `assumes` or `bounded_by` edges for the five nodes.

Lens: `certify`, full review. This agent was launched with a fresh context and
the assignment, without the authoring conversation. I read `SPECIFICATION.md`
first and the reviewer role instructions, then reconstructed the arguments
from dossiers, canonical statements, ledger, and actual source text. I authored
none of those artifacts. The authors listed above are the identities supplied
in the assignment, including the canonical-statement author.

### Sources and dependency statements

The [pinned BK source](https://github.com/kriznakumar/paper/blob/4837c33649ba2271f43c9684e9350ecbdd725f95/KLS.pdf)
was read from `/tmp/bk-source.pdf` and its extracted text. Its SHA-256 is
`8b298d3b4fd7b565fd35e43032990840c94faa7e03e3bc9aa980b476b2adc14c`,
matching the repository's pinned bibliographic record. I checked Sections 3–5
and the proofs in Appendices A–C, including the domain lemmas, against the
dossiers; the preprint's assertions were not treated as established inputs.

For the published scalar input, I inspected Bakry–Gentil–Ledoux,
*Analysis and Geometry of Markov Diffusion Operators*, Proposition 4.8.1 and
Corollary 4.8.2, pp. 212–213, through a
[full-book text copy](https://dokumen.pub/analysis-and-geometry-of-markov-diffusion-operators-9783319002262-9783319002279.html).
The latter applies to a smooth probability density on Euclidean space whose
potential Hessian is at least a positive scalar times the identity, and gives
the reciprocal Poincaré constant. Taking the potential to be $V+\log Z$ and
the scalar to be $a$ supplies exactly the dossier's initial scalar inequality.
This published theorem is used at its verified statement, not newly certified.

The canonical `thm:letwin-qcts` supplies variance at most eight times the squared
Hilbert–Schmidt norm for every symmetric quadratic form under every isotropic
log-concave law. Its statement fingerprint agrees with the existing independent
pass `research/reviews/2026-10-01-letwin-imports-r2-review.md`; the full checker
validates that certification. I checked its use here, without reopening its
already certified proof or treating the BK quotation of Letwin as evidence.

### Hodge dossier: domains before estimates

The theorem agrees with `lem:bk-compatible-hodge`, including every rank, the
uncentered adjoint domain, the actual adjoint graph core, and the coefficient
$a$ independent of dimension and rank.

The finite-energy argument avoids assuming integrability of a primitive.
Bounded truncations first satisfy scalar Poincaré by cutoff and mollification.
The positive-measure set where the original function is bounded controls their
means; Fatou then gives square integrability, and truncation convergence gives
the sharp variance inequality. Local curl-free primitives exist on the whole
Euclidean space: mollification, a fixed-ball mean normalization, and local
Poincaré make the potentials converge locally in the required Sobolev space.
Centering each primitive fixes the constants. Symmetry of the remaining slots
follows by uniqueness; compatibility follows from symmetry of the original
tensor. Summing component energies gives the inverse bound with no rank factor.

Iterating this construction supplies all lower Sobolev derivatives of a scalar
potential. Cutoff errors involve those lower derivatives and vanish at each
fixed rank; compactly supported mollification is valid because the density and
its reciprocal are locally bounded. This proves potential density, ordinary
derivative cores, closedness, and dense domains.

In the weak high-order equation, the expansion of the weighted operator has
principal part $w\Delta^q$ and remainders of order at most $2q-1$.
The assumed $H^{q-1}_{\rm loc}$ regularity therefore puts its right side in
$H^{-q}_{\rm loc}$. The localized Fourier estimate gains the missing derivative.
Testing with $\eta_R^{2q}\phi$ is consequently legitimate. Each differentiated
cutoff term retains at least $q$ undifferentiated factors; both remainder norms
used in Cauchy–Schwarz have the displayed bound. The quadratic estimate and
Fatou then give the global missing derivative. Applying this to the defining
adjoint equation proves $S_r^*=D_r$ and hence the asserted graph core for
$D_r^*$, rather than merely norm density.

### Hodge dossier: projection and curvature

The weighted divergence has mean zero, so its projections onto $C_m$ and
$G_m$ coincide. The commutator $[\partial_i,\partial_j^*]=V_{ij}$ and full
symmetry of $\nabla F$ give equation (2). Differentiating the divergence gives
equation (3), with all derivatives of $F$ cancelled. At $m=0$ there is no loss.

For $m\ge1$, I checked the normalized creation/annihilation algebra and the
exterior norms. The identity $bb^*+b^*b=(q+p)I$ gives exactly the projection
$bb^*/(m+p-1)$ and the isometry $b/\sqrt m$. The constrained maximal
derivatives form a closed complex. Cutoff commutators tend to zero, and the
local convolution error from $V_i$ is bounded by its local Lipschitz constant
times the mollification scale. This verifies the maximal adjoint expressions
and their joint graph core; no bounded higher derivatives of $V$ are needed.

The Weitzenböck expansion, the removed projection term $m^{-1}\|c\omega\|^2$,
and $[c,c^*]=H-K_{\rm bos}$ all have the stated signs. The creation row has
squared norm $m$, giving the residual gradient coefficient $1/m$ in (4).
Pointwise diagonalization differentiates no moving frame. In a combined
multiplicity block, $b$ is wedge multiplication by
$r=(\sqrt{\alpha_i})$ and $|r|^2=N=m+1$. The exterior-pair expansion for
$r\wedge v$, $v\perp r$, gives $N^2\langle v,Kv\rangle/m$; after the
isometry this is $(N/m)PKP$. Thus the compressed curvature is positive even
though its uncompressed expression includes a negative bosonic term.

The two contractions in the curl have denominator $\sqrt{Nm}$. Their inverse
curvature cost is therefore exactly $|F_\alpha|^2/N$ times the Schur-complement
term in (7). The original curvature contribution is $S|F_\alpha|^2/N$.
Minimization over $r^\perp$ leaves at least $aN$, so the remaining cost is at
least $a|F_\alpha|^2$. Blocks with one coordinate in their support have zero
two-form space and satisfy the same conclusion. No factor depending on rank
or dimension survives.

The Hilbert-complex projection identity uses the form decomposition by
$\ker B$ correctly: its perpendicular space lies in $\ker A^*$, both
projections preserve the domains, and the weak equation gives
$AA^*\mathcal L^{-1}Au=Au$. The variational inverse comparison is valid for
the bounded positive curvature multiplication operator. The Hessian upper
bound justifies passage of that term through the joint graph closure.
Finally, adjoint graph approximation makes the ordinary gradients Cauchy and
extends both the estimate and its domain assertion to every adjoint input.

### Integration calculus

The theorem implies the canonical `prop:bk-integration-calculus` in full.
The inverse of $D_r$ splits on orthogonal constant and centered input spaces
as $(L_r,J_r)$. The covariance bound controls $L_r$ componentwise with constant
one. Both product inverse identities respect the unbounded operator domains.
Splitting the full gradient form into constants and centered fields gives
$0\oplus H_{r+1}$. Inverting the Hodge form order and compressing produces
$J_r^*J_r\preceq g_a(H_{r+1}^{-1})$; scalar spectral calculus at zero also
covers accumulation there.

Uniform inverse bounds justify the Hilbert direct sums. The zero-grade block
of $J^*J$ is zero, all other blocks have the correct shifted index, and
$\|H_0^{-1}\|=C_P$ yields the claimed upper bound on $C_P$. Formal Appell
differentiation and mean zero identify the iterated primitives with the exact
factorial. Polynomial integrability follows from positive curvature. Summing
the fixed-law coefficient estimate over ordered free-index slices preserves
the tensor norm exactly; orthogonal source and target grades then give every
observation bound. There is no appeal to a uniform Appell estimate.

### Abstract powers and applications

The abstract theorem has the same hypotheses, strict condition on $B$, and
prefactor as `lem:bk-uniform-power-bound`. Complexification is legitimate.
Resolvents approaching a maximal-modulus spectral point give approximate
adjoint eigenvectors. Scalar spectral Jensen, followed by the last observation,
yields $as^{D+1}/(1-as)\le\gamma_D^2$, with $as<1$; this supplies the needed
strict spectral-radius separation from $\sqrt B$.

The Cauchy–Schwarz orbit inequality has denominator $x_{m-1}$, and inversion
of $g$ gives the curvature term $aB y_m^3/y_{m-1}^2$ after normalization.
Decay of the normalized orbit forces a finite positive maximum. If its index
is at least $D-1$, the last observation gives a strictly larger next iterate,
a contradiction. For earlier indices, summing the second-difference inequality
backwards from a nonpositive final increment produces precisely the weights
$j\gamma_{j+1}^2/B^{j+1}$. All divisions occur before a positive maximum;
a zero next iterate and the zero Hilbert space cause no omitted case.

For `cor:bk-integration-powers`, the chosen $B$ satisfies the strict hypothesis
even when $a=1$ or $\rho=1$, and the prefactor excess is at most $1/384$.
The rank-zero product is the stated block of $J^q$. For
`cor:bk-quadratic-seed`, the normalized quadratic Appell field has the factor
$1/2$, converting Letwin's constant eight to $c_2\le\sqrt2$. Whitening on
the linear support contracts the Hilbert–Schmidt norm, including the degenerate
support convention. At $D=2$ the sum is empty; taking the infimum of strict
admissible $B$ gives exactly $(2/a)^{1/3}$. The calculus input to both
applications is established earlier in this grouped review, so their dossier's
explicit conditional presentation implies the unconditional canonical statements.

### Hypotheses, fences, and validation

All used hypotheses are present: finite-dimensional Euclidean tensor fibers;
smooth positive density; positive lower and finite upper Hessian bounds;
distributional compatibility; componentwise centering; and, in the calculus
and corollaries, covariance at most identity. The Hodge proof does not need
the law's centering except as part of the shared convention; the calculus
does need it to identify the constant primitive with contraction against $x$.
The abstract argument requires bounded operators, $a>0$, finite nonnegative
observations, integer $D\ge2$, and the strict inequality for $B$, exactly as
stated. No unstated uniform ellipticity ratio, dimension bound, rank bound,
commutation of $R$ and $R^*$, or infinite-degree observation is used.
No fence is assigned to these nodes; no surrounding refutation is contradicted
by these strictly curved statements.

`uv run scripts/check.py` completed with exit 0, including MyST. The grouped
`--fingerprint` command also completed with exit 0 and was repeated immediately
before this report; its output was unchanged and is reproduced above. Concurrent
manuscript rearrangement did not change any checked statement fingerprint or
dossier. No proof, manuscript, ledger, or previous review was edited here.

## Corrections

None required for these five certifications. No required step remains unverified.

## Exclusions

This report does not certify regular approximation, localization, moving Appell
variance, reverse transfer, the uniform coefficient induction, the explicit
Poincaré or Cheeger conclusions, or any other BK section. It supplies no new
review of Letwin's proof or of the published scalar Bakry–Émery theorem.
It is not a manuscript-wide sync audit, nor an assertion that the full BK
proposal follows without separate certification of its remaining steps.

## Proposed certification records and handoff

Preserve existing references and dependency edges for all five nodes. Set each
to `proved` with the following proof record; add no assumptions or refutations.

```yaml
files: [research/reviews/2026-10-06-bk-operators-review.md]
deltas:
  - node: lem:bk-compatible-hodge
    status: proved
    proofs:
      - artifact: solutions/lem-bk-compatible-hodge.md
        review: research/reviews/2026-10-06-bk-operators-review.md
  - node: prop:bk-integration-calculus
    status: proved
    proofs:
      - artifact: solutions/prop-bk-integration-calculus.md
        review: research/reviews/2026-10-06-bk-operators-review.md
  - node: lem:bk-uniform-power-bound
    status: proved
    proofs:
      - artifact: solutions/lem-bk-uniform-power-bound.md
        review: research/reviews/2026-10-06-bk-operators-review.md
  - node: cor:bk-integration-powers
    status: proved
    proofs:
      - artifact: solutions/lem-bk-uniform-power-bound.md
        review: research/reviews/2026-10-06-bk-operators-review.md
  - node: cor:bk-quadratic-seed
    status: proved
    proofs:
      - artifact: solutions/lem-bk-uniform-power-bound.md
        review: research/reviews/2026-10-06-bk-operators-review.md
```
