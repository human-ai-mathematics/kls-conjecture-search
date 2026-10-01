---
verdict: pass
authors:
  - researcher_chen_klartag, gpt-6-astra, 2026-10-01
reviewer: reviewer_chen_klartag, gpt-6-astra, 2026-10-01
fingerprints:
  solutions/thm-chen-klartag-imports.md: 2bf442b535913c660c8c4a6d43f1fec44cb059c13310ae0677fc44a2f55dc38c
  thm:chen-klartag-moment-hessian: 5193b5b67e14991a704751ab84d5df038ee38ecb8ffd0f546cd23c20a5aa8946
  thm:chen-klartag-thin-shell: e5ca045da4693f7b43a52d66b6a7ee27bebfb7a4c945ab7f8dc5c8ed3f73449f
  thm:chen-klartag-third-moment: 106e69549a99330692dad468ae43984448efcc68b0cab115c3c54ed835e304f0
---

# Independent certification of the Chen–Klartag imports

## Findings

**Pass**, jointly for the three fingerprinted statements. I reconstructed the argument
from the dossier, checkpoint, manuscript and sources in a fresh review context, without
the conversation that produced the work. No subagents were used. The author's assertion
that no gap remained was not used as evidence.

The dossier theorem agrees with `modules/04-family-moment-map.md:152–183`, including
the convex-body and simplex clause. Its expanded regular class correctly resolves the
Hessian directive's reference to the source's assumptions. Isotropy is essential; the
Hessian statement is read with the isotropic normalization of the cited theorem and
the manuscript's moment-map setup. Source $\psi$ is manuscript $\varphi$, not the
source's Legendre dual. The general conclusions concern moments of the target law,
not a limiting assertion about its moment Hessian.

I read the pinned [Chen–Klartag v1](https://arxiv.org/html/2607.23307v1), including
Section 2, Lemmas 3.1–3.5, Example 3.6, Lemma 3.7, the end-of-Section-3
approximation, Section 4 and Appendix A. (Item 3.6 is an example, not a lemma.)
Theorems 1.5, 1.1 and 1.2 and Corollary 1.3 match the claimed conclusions.
The source proof, rather than only those statements, was checked.

Published inputs were checked as follows:

- [Cordero-Erausquin–Klartag, Theorem 2](https://arxiv.org/pdf/1304.0630), p. 4:
  finite first moments, centering and full dimension hold here, and the normalization
  supplies a probability moment measure.
- [Klartag, condition (2), Theorem 1 and Section 6](https://www.math.tau.ac.il/~klartagb/papers/lc_moment.pdf):
  the compact-target regularity and trace bound apply without smooth boundary or
  strict convexity of $V$. Positive determinant and strict convexity give the inverse
  gradient map. Equation (89) states exactly the Brascamp–Lieb input used here.
  I verified this input in that published treatment; I did not obtain the original
  1976 article through its publisher endpoint. There is no missing inequality or
  hypothesis left to infer from that inaccessible endpoint.
- [Barthe–Klartag, Proposition 10 and definition (3)](https://www.weizmann.ac.il/math/klartag/sites/math.klartag/files/uploads/1907.01823.pdf),
  pp. 5–6: the derivative-centering requirement is present, and is satisfied by
  $f=|x|^2$. This is a published input (Bull. Hellenic Math. Soc. 64 (2020),
  1–31, also recorded in the [author's publication list](https://cv.hal.science/franckbarthe)).
  Its use does not import a recent thin-shell theorem.

The following are my checks of the dossier's proof, in its order.

1. **Local calculus and positivity.** The cofactor calculation gives the stated
   divergence operator, with the negative drift sign. Twice differentiating
   Monge–Ampère gives $LH+H=A+Q$ with both terms positive semidefinite. The product
   rule gives $LG=2(S-G)$ and Cauchy–Schwarz gives $\Gamma(G)\le4BS$.
   None of these local identities alone is used to integrate $LG$ globally.

2. **Cutoffs and integrability.** An unbounded convex sublevel containing a ball
   would have infinite volume, contradicting integrability. Compact sublevels
   justify both cutoff tests. Differentiating $b_R$ gives
   $-b_R'=R^{-2}\eta'(t/R)^2$, so the energy estimate has the correct $R^{-1}$
   scale. The bound on $L\psi$ uses bounded $K$ and bounded $\nabla V$.
   Young's inequality gives $U_R\le2B+4Be_R$. Fatou establishes $S\in L^1$
   before dominated convergence and the vanishing boundary term yield the energy
   balance. There is no circular assumption of finite third-derivative energy.

3. **Form domain and normalization.** Smooth positive coefficients on compact sets
   make the initial symmetric gradient form closable. The displayed difference
   estimate makes $\chi_RF$ Cauchy in the form norm and identifies its energy with
   the integral of $\Gamma(F)$. Thus entrywise Brascamp–Lieb applies after, not
   before, finiteness of $D$. Euclidean cutoffs give $\int H=I$ with errors
   bounded by a constant times $R^{-1}$. Consequently $N-n\le D$ is justified.

4. **Tensor identity and Hessian constant.** The coordinate transformation is fixed
   orthogonal at the point. Cyclic averaging over ordered triples replaces the
   numerator by $(\lambda_a^2+\lambda_i^2+\lambda_j^2-
   \lambda_a\lambda_i-\lambda_i\lambda_j-\lambda_j\lambda_a)/3$.
   This is the displayed sum of three squares divided by six, including repeated
   indices. Therefore $Q_0\ge D$, and the balance implies
   $N\ge2D\ge2(N-n)$, hence $N\le2n$.

5. **Third moments.** The upper bound on $H$ converts finite metric energy to
   $L^2$ integrability of every third derivative. Both Euclidean integrations by
   parts therefore have integrable limits. Centering permits the subtraction of
   $\delta_{ij}$, and isotropy makes the gradient components orthonormal.
   Bessel gives $\sum_{i,j,k}T_{ijk}^2\le4(N-n)\le4n$. No unordered-index
   convention or directional norm is substituted.

6. **Thin shell.** The composed Stein test is bounded and has bounded differentiated
   terms, so the Euclidean cutoff argument works despite its noncompact support.
   Rowwise Cauchy–Schwarz supplies the summed negative-Sobolev bound. The test
   conventions agree: on this bounded convex target the density is bounded above
   and below, and Sobolev extension and smoothing give ambient compactly supported
   smooth approximants. In particular the locally Lipschitz tests in Proposition 10
   cause no enlargement of the norm. The derivatives $2x_i$ have zero mean;
   squaring their factor two gives the required factor four and the constant $8n$.

7. **Approximation.** Full-dimensional log-concavity supplies exponential tails and
   finite fourth moments. Gaussian convolution preserves log-concavity; on each
   fixed closed ball the positive smooth density has a positive minimum, giving
   all the stated derivative bounds. Damping and truncation converge by dominated
   convergence after fixing the convolution parameter. The diagonal construction
   controls every mixed moment through degree four. Covariances remain positive
   definite and tend to $I$, so whitening preserves that convergence and the regular
   class. Passing the polynomial moment inequalities to the limit is valid.
   The optional quadratic variational formula for the summed $H^{-1}$ norm also
   checks: rescaling each test gives the squared norm, and each fixed test tuple
   has bounded continuous integrands. This removes any reliance on an unchecked
   Klartag–Lehec lower-semicontinuity import.

8. **Sharpness and convex bodies.** I recomputed the centered exponential moments
   $0,1,2,9$ and the normalized exponential moment potential. The latter is correctly
   used only as an explicit example outside the regular class. The cone Jacobian
   cancels the Gamma power, proving log-concavity and the asserted isotropy.
   Expanding the Gamma moments gives the two cross/fourth moments in the dossier.
   For the tensor, the mixed term contributes $12(k-1)/k$ and the axial term $4/k$;
   thus the offset is $12-8/k$. Solving the two affine inequalities gives exactly
   $4n(n+1)^2/((n+3)(n+4))$ and $4n(n-1)(n+2)/(n+3)^2$.
   The exponential proportions have the uniform simplex law independently of their
   sum. The square matrix $B$ has $BB^T=I$, so equality transfers by orthogonal
   invariance and then by the exact cone identities. The $n=1$ case gives zero
   third tensor and radial variance $4/5$, as it should.

All operative hypotheses are stated: centering, covariance identity, full dimension,
log-concavity, and the additional bounded-target smooth-potential assumptions for the
Hessian calculation. Uniform laws are allowed. No extra boundary smoothness, uniform
ellipticity, stochastic completeness or Hessian convergence is needed. The all-orders
regularity is inherited from the published input rather than asserted to be minimal.

**Dependency closure.** The two child nodes depend on the Hessian node, proved in this
same dossier. The convex-body clause also uses the thin-shell conclusion, whose proof
is supplied in full here from that same parent and the published inequality. Thus no
additional open theorem is assumed. There are no `assumes` or `bounded_by` entries.
The three nodes must be certified jointly, or the parent first. No Letwin, CMH or
Klartag–Lehec draft is used.

**Build and version check.** Immediately before this report I ran
`UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py`, then
`UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py --fingerprint solutions/thm-chen-klartag-imports.md`.
Both exited zero with escalation for MyST subprocess permissions. The full check had
no `FAIL` or MyST error; it reported 131 nodes and this dossier as an uncertified draft.
The initial sandbox run failed at MyST, and was not treated as a mathematical or
manuscript failure. No checker was changed. The final full-check log is
`/tmp/ck-review-final-check.log`; the fingerprint output is copied verbatim above.

The dossier, checkpoint, role instructions, specification and manuscript module
remained unchanged during review. Concurrent ledger and bibliography edits were
observed; I reread the three entries and relevant references before fingerprinting,
and their mathematical content and dependencies were unchanged. Additional raw
SHA-256 records for the actual materials read are:

| Material | SHA-256 |
|---|---|
| Author checkpoint | `d20bbb31b838ce2b3148c2b0812cc87d7e04ceb3e186ba22afa13a66e8ef3b94` |
| Entire manuscript module | `f79fd06495be5c4c086af8fae50c70ccf9e419816df338ed3bb21bb82fcfd7f1` |
| Pinned source HTML retrieved for this review | `a255abe66bda0b2827d29d874c68c491655d5753567ba157ce354eae54ee1118` |

## Corrections

None required for the certified conclusions. No proof step within scope remains
unverified. Published background theorems are accepted as published inputs with their
applicability checked; this is not a new certification of their entire proofs.

Only the orchestrator may apply the following status changes. Retain existing
references and relations, and add the indicated proof record to each node.

```yaml
files:
  - research/reviews/2026-10-01-chen-klartag-imports-review.md
deltas:
  - file: research/program/ledger.yaml
    id: thm:chen-klartag-moment-hessian
    status: proved
    proofs:
      - artifact: solutions/thm-chen-klartag-imports.md
        review: research/reviews/2026-10-01-chen-klartag-imports-review.md
  - file: research/program/ledger.yaml
    id: thm:chen-klartag-thin-shell
    status: proved
    depends_on: [thm:chen-klartag-moment-hessian]
    proofs:
      - artifact: solutions/thm-chen-klartag-imports.md
        review: research/reviews/2026-10-01-chen-klartag-imports-review.md
  - file: research/program/ledger.yaml
    id: thm:chen-klartag-third-moment
    status: proved
    depends_on: [thm:chen-klartag-moment-hessian]
    proofs:
      - artifact: solutions/thm-chen-klartag-imports.md
        review: research/reviews/2026-10-01-chen-klartag-imports-review.md
```

## Exclusions

This review does not certify directional tensor improvements, a Loewner Hessian-square
bound, CMH, KLS, arbitrary quadratic-form estimates, uniqueness of equality cases,
or any extension of the Hessian-square conclusion to general nonsmooth moment maps.
It is not a review of other dossiers or of the surrounding manuscript's Letwin claims.
The general distributional consequences certified here are the stated moment bounds.
