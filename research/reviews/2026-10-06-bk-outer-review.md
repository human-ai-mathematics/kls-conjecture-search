---
verdict: pass
authors:
  - bk_powers, gpt-6-astra, 2026-10-06
  - orchestrator, gpt-6.1-sol, 2026-10-06
reviewer: reviewer, gpt-6-astra, 2026-10-06
fingerprints:
  solutions/thm-bk-appell-bound.md: 005e053559713854bfc9112c01c93937dd2e8581041f8718d72d465ae5ee9f14
  thm:bk-appell-bound: 48e24f5baec93f476789f276b76233bbb3b1dffdb6778c0c7e20c1d161264026
  def:bk-uniform-appell-coefficients: 0e3be6061878fe05162d23613514cc2211cad0df63d76393c5957b3444776c95
  def:bk-compatible-calculus: b0bb2905e0f3e30702cd0c5d9d3ff881d59ec3fa87175e4d2b50222b5e865ed1
  prop:bk-integration-calculus: 591a8826b560d20e268b65a430aff427ed03b6c8f4b9b03c53272f31dac7b2c4
  prop:bk-reverse-transfer: be684c7356c9b9c9ceef5017794c511c778ad4c5f8f0525aa7bf5a33550dfb73
  lem:bk-uniform-power-bound: f29a142254b33ded1c91d84c64d83e2c4814b144d044988e0aa5f6eccf0e802d
  cor:bk-quadratic-seed: 85191ed8fa8e019fde7612511ca5d9a87b47a18b1f7269bbe2d575e398864cd3
  solutions/thm-bk-explicit-poincare.md: 096fcce29cbaa6ba7ab7f1cd6ffc0b3534a9d39b0e49af09c44c4b83f702a54c
  thm:bk-explicit-poincare: ed29bf2fbe5c374559d511d8ce54e010095503ae0794aff0218b323e1062045a
  lem:bk-regular-approximation: e9223378a723c866b083fb0fa5996cb2e392d23932416eab367590c580110758
  cor:bk-integration-powers: 0d4acc3094b4e0924c4b2342a8bab98ec5b034379f27349fa41a5636c456241e
  cor:bk-cheeger: 284d8b5797c9620eca2df31ce215efda2707723408774f64fbad61f48caccd5e
---

# BK outer induction and explicit constants

## Findings

**Pass** for `thm:bk-appell-bound`, `thm:bk-explicit-poincare`, and
`cor:bk-cheeger`. The two fingerprinted dossiers establish their canonical
statements, with radius $10^8$, scalar constant $1+2\cdot10^{16}$, and inverse
Cheeger bound $\sqrt{\pi(1+2\cdot10^{16})}$.

This is a full `certify` review. The reviewer retained the independent context
used for `research/reviews/2026-10-06-bk-operators-review.md`, received only a
new path-based assignment, and saw no conversation producing or directing
these dossiers. I authored none of the reviewed work. I reconstructed the
proofs from the dossiers, canonical statements, dependency records, and the
pinned source, not the author's report.

### Scope and dependency agreement

The actual [BK source at commit
4837c33649ba2271f43c9684e9350ecbdd725f95](https://github.com/kriznakumar/paper/blob/4837c33649ba2271f43c9684e9350ecbdd725f95/KLS.pdf)
was available as `/tmp/bk-source.pdf` and its text extraction, SHA-256
`8b298d3b4fd7b565fd35e43032990840c94faa7e03e3bc9aa980b476b2adc14c`.
I checked Sections 8–9, the full numerical proof in Appendix E, and Appendix G
against the dossiers. The approximation theorem is used through its separate
certification, not by accepting Appendix F on the source's authority.

The integration calculus, abstract power theorem, quadratic seed, and
integration-power corollary have the interface certified in the operator
report above. The approximation and reverse-transfer statements are now
proved in `research/reviews/2026-10-06-bk-localization-review.md`, which I read
along with the current canonical statements and ledger. Their fingerprints
match the interfaces used here. In particular, reverse transfer permits
$q=1$, requires only finite bounds below degree $d$, and concludes for the
full covariance-at-most-identity supremum, including proper supports.
Approximation supplies regular isotropic approximants and the finite-energy
extension including square integrability. Its clarified polynomial-limit
wording was reread before fingerprinting; the scalar consequence uses its
unchanged final two sentences.

The two dossiers state their upstream inputs explicitly. Those external
inputs are now certified; the coefficient theorem and scalar theorem are
proved in sequence within this group. Thus no open premise remains in the
proposed grouped transition. None of these nodes has an `assumes` or
`bounded_by` edge. The fixed-law coefficient and operator definitions agree
in tensor normalization, centering, and grade indexing.

### The degree induction

I checked every bound in `solutions/thm-bk-appell-bound.md` analytically.
The convolution estimate counts the endpoint once and may count the middle
term twice. The tail integral beginning at three gives exactly
$1+32(1/16+1/81+1/81)=307/81<4$. Applying it at $s=d+1$ gives the stated
bound on $\Sigma_d$; the omitted endpoint terms are nonnegative. For $d=2$
the actual sum is empty.

The linear base is $c_1^*\le1<10^8/16$. At an arbitrary induction step,
every coefficient in $\Sigma_d$ has degree between two and $d-1$. Setting
$C_k=\beta_k$ therefore uses only finite constants already supplied by the
induction hypothesis. It never assumes that $c_d^*$ is finite before applying
reverse transfer, nor starts from dimensionwise finiteness of a supremum.

For $2\le d\le D_0=10^7$, the choice $\eta=d/(100R)$ gives
$\eta\le1/1000$ and $\delta=(100R)^{-2}$. Taking square roots of the
quadratic seed yields the required integration norm $(2/\delta)^{1/6}$.
Its upper bound $10\sqrt R$ follows from the displayed sixth-power inequality.
The ratio $\beta_{d-1}/\beta_d<16/R$ and the drift ratio at most $1/25$
are valid at both endpoints of the range. The exponential and square-root
factors are each below $21/20$. Since $160/\sqrt R=2/125$, the final
ratio is below $1491/25000<1$. Hence the initial range closes without an
additional finite-degree assumption.

For $d>D_0$, the integer choices $q=\lfloor d/2\rfloor$ and
$D=\lfloor\sqrt d\rfloor$ obey $1\le q<d$ and $2\le D<d$. The coefficient
observations through $D$ are therefore available by induction for every law
in the curvature class. With the stated $\eta,\delta,B$, direct substitution
gives
$\delta B^{D+1}=R^{2D}/[e(100C_w)^2d^3]$.
The inequalities $(D+1)^8>d^4$ and
$e(100C_w)^2<480000<D_0<d$ establish the strict power-lemma hypothesis.
No asymptotic estimate is substituted for that strict finite-degree check.

Cancellation of the powers of $R$ in $Q_D(B)$ leaves the displayed exponential
sum; $(j+1)/(D+1)<1$ and the integral of $x^{-7}$ from two give
$Q_D(B)<1+e/384<2$. Consequently the proposed $M_q$ controls the entire
curvature class, uniformly in dimension and law, as reverse transfer requires.
The weight ratio is at most sixteen. The estimates
$\eta(D+1)<1/2$, $q\ge d/3$, and $D+1\le2\sqrt d$ bound the principal
ratio by $32\exp(3/100-\sqrt d/24)<1/4$. The final strict comparison follows
already from $d>10^6$ and $e>2$. The drift ratio is below $1/50$.
Their sum is less than one. The single radius was chosen before the degree,
law, or dimension, proving exactly the canonical all-degree assertion.

All hypotheses of the transfer estimate are checked in both ranges:
$0<\eta\le1$, $\delta=\eta^2/d^2$, integer $1\le q\le d-1$, finite
lower-degree constants, and a finite uniform operator-product bound. There
is no reverse use of KLS or of an all-degree coefficient estimate.

### Scalar limit, approximation, and support

In `solutions/thm-bk-explicit-poincare.md`, one regular law and one positive
lower curvature bound $a$ remain fixed while $D\to\infty$. The coefficient
theorem supplies every finite observation range, so the integration corollary
gives the same scalar Poincaré constant bounded by each member of the displayed
sequence. Its limit is exactly $1+2R^2$ for every $a>0$. This is not an
exchange of a measure limit with a varying operator norm.

The certified approximation statement supplies regular isotropic measures.
For compact smooth tests, function, square, and squared gradient are bounded
continuous, so weak convergence passes all three integrals. The same
dependency explicitly extends the scalar inequality to locally Lipschitz
finite-energy tests and proves their square integrability. No uniform Hessian
bound is needed for the approximants, because the scalar constant already
lost both curvature bounds.

For a general law of covariance at most identity, centering and restriction
to the linear affine-support space make covariance invertible unless the law
is a point mass. Whitening there preserves log-concavity. The inverse
coordinate map has squared norm at most one, and the chain rule gives exactly
the energy with $\Sigma$ inserted between the two gradients. Absolute
continuity on the support justifies the almost-everywhere statement. Applying
the isotropic finite-energy result first gives square integrability of the
pulled-back function, and hence of the original one; the variance comparison
then follows. Translation does not change it. Point masses and intrinsic
gradients agree with the canonical boundary conventions.

### Cheeger normalization and published sources

I checked [Klartag, *Logarithmic bounds for isoperimetry and slices of convex
sets*, published 2023 version, equation (1.4), p. 3](https://arxiv.org/pdf/2303.14938).
With its inverse isoperimetric scale $\psi=h^{-1}$, it states the exact
comparison $1/4\le\psi^2/C_P\le\pi$ for log-concave measures. Thus the
factor $\pi$ and the direction of the inequality in the dossier are correct.
The source attributes this numerical upper constant to De Ponti–Mondino;
it is not being inferred from an unspecified universal constant.

I also checked [Milman's published comparison source](https://arxiv.org/pdf/0712.4092),
the definitions and Theorems 1.1, 1.4, and 1.5. Its exterior Minkowski
boundary and expansion constant match the manuscript normalization, and its
Poincaré constant is the inverse square root of this manuscript's $C_P$.
It supplies the universal comparison for the log-concave class; the precise
numerical factor used here is supplied by Klartag's displayed equation.
These are established published results used at their statements. No new
certification of their historical proofs is asserted.

### Hypotheses and validation

Every required hypothesis is stated or supplied by a certified dependency:
fixed finite-dimensional coefficient tests, log-concavity, centering and
covariance control; regularity and positive curvature for the operator step;
uniform lower-degree data for transfer; and local Lipschitz regularity with
finite intrinsic energy for the final scalar statement. The all-law conclusion
has no curvature hypothesis. There is no unstated full-dimensionality condition
at the conclusion and no use of extrinsic gradients to strengthen an intrinsic
estimate. No problematic unused theorem hypothesis was found.

The full `uv run scripts/check.py` completed with exit 0 after registration
of the operator and localization groups (192 nodes, 159 proved), with no MyST
error. The grouped fingerprint command for these two dossiers also completed
with exit 0; its output is the front matter above. The upstream interfaces
were checked against their current certified fingerprints before this report.

## Corrections

None required in the statements or dossiers. An incidental prose error outside
the certified claim directives was reported to the orchestrator: the integration
length above the cutoff is of order $d$, while only the observation degree is
of order $\sqrt d$. The dossier itself uses the correct distinct choices.

## Exclusions

This report newly certifies only the degree induction and its explicit scalar
and Cheeger consequences. It relies on, rather than re-reviews, the registered
operator and localization/approximation groups. The final dossier attaching
this result to `conj:kls` is assigned a separate report, including its
infinite-energy convention. No optimality of $10^8$ or $1+2\cdot10^{16}$,
moment-map strengthening, occupation estimate, or comparison of unrelated KLS
proofs is asserted. There is no incomplete step in the present certified scope.

## Proposed records and handoff

Promote these three nodes together or in dependency order, preserving their
current references and dependency edges. Add no `assumes`, `bounded_by`, or
`refuted_by` relation.

```yaml
files: [research/reviews/2026-10-06-bk-outer-review.md]
deltas:
  - node: thm:bk-appell-bound
    status: proved
    proofs:
      - artifact: solutions/thm-bk-appell-bound.md
        review: research/reviews/2026-10-06-bk-outer-review.md
  - node: thm:bk-explicit-poincare
    status: proved
    proofs:
      - artifact: solutions/thm-bk-explicit-poincare.md
        review: research/reviews/2026-10-06-bk-outer-review.md
  - node: cor:bk-cheeger
    status: proved
    proofs:
      - artifact: solutions/thm-bk-explicit-poincare.md
        review: research/reviews/2026-10-06-bk-outer-review.md
```
