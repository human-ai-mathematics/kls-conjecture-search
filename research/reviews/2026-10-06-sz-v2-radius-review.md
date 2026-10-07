---
verdict: pass
authors:
  - sz_v2_height researcher, gpt-6-astra, 2026-10-06
reviewer: reviewer, gpt-6-astra, 2026-10-06
fingerprints:
  solutions/sz-v2-height-reduction.md: 3f8c2fc415bb9116389a905c9d16709cc3df6c10a98296b0eab1a49566250a13
  prop:sz-v2-common-radius: 2ae867703ee8d57f0b0ca660a3af2ef8c37357725d7d5d66e3670c92014d1044
  def:sz-v2-common-radius: 49ae12dc3b61656251736c6d98ed212477348fbfdcfcb5ce82c490131854c2b7
  lem:sz-analytic-foundations: e3b0250c18499cbdf58b3cb609937032b0101d8aa096aac355555309e5e94d3f
  thm:sz-polynomial-variance: ffd52798e616ccd22bb3e4c78d5c382fd5657d3b598e6e4ec3c9afc4f696da8e
  thm:sz-curvature-comparison: 9baf9221ded7767fc4a904b4a582b9804ab1d424bb87914745aaaa6dd0242787
---

# Common coefficient radius: independent certification

## Findings

The dossier proves [](#prop:sz-v2-common-radius), with precisely the
normalization of [](#def:sz-v2-common-radius). This reviewer received a fresh
context containing a mission and artifact paths, without the conversation
that authored or directed the proof. The author identity was supplied in the
assignment. The conclusions below were reconstructed from the proof,
canonical statements, ledger, prior certifications and pinned source.

### Statement agreement and hypotheses

The dossier and canonical proposition agree on every quantifier, the three
radius bounds, the arbitrary nondecreasing majorant with floor one, every
positive integer block length, and the conversion constant $2^{85}$.
The same fixed law and the same supremum over all degrees occur throughout.
The ordered-index Hilbert norms agree with the Appell conventions in
[](#thm:sz-polynomial-variance). In particular there is no extra factorial
in the tensor norm.

Hypotheses used are finite dimension, a centered probability density
$e^{-W}$, smoothness of $W$, positive lower and finite upper Hessian bounds,
and covariance at most the identity. The finite-block conclusion additionally
uses a nondecreasing $G\ge1$ and its coefficient estimate in every positive
degree. Positive lower curvature gives tails and a positive spectral gap;
both Hessian bounds place the law in the certified analytic and curvature
interfaces. Centering identifies the degree-one Appell tensor with $X$.
No common positive lower curvature across measures, no uniform inverse norm,
and no continuity of the coefficient radius are assumed. No unused stated
hypothesis requiring a correction was identified.

All four recorded dependencies supply the claimed inputs. The definition is
`defined`; the three theorem/lemma inputs are `proved`, with existing independent
certifications. There are no open dependencies or `assumes` edges and no
`bounded_by` edge. The absence of a uniform radius bound respects the
coefficient/KLS distinction and does not establish any uniform block
initialization.

### Steps checked

1. On the centered Hilbert space, the certified positive spectral gap gives
   $B=H^{-1}$ bounded, positive and of norm $C_P$. The closed form identity
   gives $\|\nabla Bf\|^2=\langle f,Bf\rangle$ for every centered
   $L^2$ input. Coordinates lie in the form domain. Testing against $x_i$
   gives the exact mean-gradient formula $\mathbb E\partial_iBf=\mathbb E X_if$.
   Subtracting this mean proves $\mathcal T^*\mathcal T=B-L^*L$.
   Covariance duality gives $L^*L\preceq I$, hence the two claimed operator
   norm bounds, even when $C_P-1$ is negative.
2. Strong convexity gives Gaussian tails. Polynomial tests and their first
   derivatives are square integrable; spatial cutoffs converge in the weighted
   form norm. Thus all form integrations by parts used here are legitimate,
   without assuming that $f$ itself is in the form domain. Appell polynomials
   of positive degree have mean zero, so variance equals their squared
   $L^2$ norm. Adjointness on the symmetric tensor Hilbert space gives exactly
   $\|Q_d\|=\sqrt{K_d}$.
3. Differentiation of the formal generating identity gives
   $\partial_iP_d[T]=dP_{d-1}[T_i]$. For $d\ge2$ these lower-degree tests
   are centered. Pairing with every symmetric tensor proves (H1), including
   its factor $d!$. Symmetrization is an orthogonal projection and finite
   orthogonal amplification preserves the scalar operator norm. Thus
   $c_d\le\sqrt R\,c_{d-1}$. Since $c_1^2=\|\operatorname{Cov}(\mu)\|\le1$,
   induction gives a single finite bound for all degrees before the
   supremum defining $\mathcal A$ is taken. The arguments also cover $R<1$
   and the formal zero-norm case.
4. Expanding (H1) finitely gives (H2): componentwise application commutes with
   permutations of existing output slots, and the final full projection
   absorbs the intervening projections. This does not assert that a spatial
   derivative commutes with $B$. The block norm bound is consequently
   $c_d\le\|\mathcal T^m\|c_{d-m}$ with no output-dimension cost.
   Writing $d=jm+r$, $1\le r\le m$, gives exponent
   $jm+r-1=d-1$ after replacing both factors by the displayed maximum.
   This checks degree one, $m=1$, exact multiples of $m$, $j=0$, and zero
   block norm. The floor $G(m)\ge1$ permits the defining supremum.
5. Set $\mathcal R=2^{40}\sqrt{\mathcal A}$. It meets the certified
   curvature theorem's threshold at $\epsilon=1$. The estimate
   $(k+1)^2\le4^k\le2^{40k}\sqrt{\mathcal A}$ gives its all-degree
   hypothesis with $\ell\equiv1$. The conclusion is
   $32\mathcal R^2\max\{1,a^{-1/(d+1)}\}$, and
   $32\mathcal R^2=2^{85}\mathcal A$. Along finite dyadic degrees the last
   factor tends to one for the same fixed $a>0$. This is a scalar limit;
   neither infinite tensor families nor a weak-limit interchange is used.

### Source, provenance and build

The proof of Lemmas 8.17 and 8.18 in Section 8.5 of
[Song–Zhang v2](https://arxiv.org/html/2610.01447v2) was checked in the supplied
full HTML `/tmp/kls-sz-v2.html` and its readable extraction `/tmp/sz-v2.txt`.
The HTML identifies version 2 dated 4 October 2026. Equation (134) and its
integration-by-parts justification were also checked. The local proof
reconstructs that identity and both lemmas rather than importing their
assertions. The coefficient seed and other conclusions surrounding (134)
are not needed. In particular the optional source restriction
$G\le G_*$ from the section's setup is not used in Lemma 8.18's block
comparison or in this proof.

The final conversion uses the already certified v1 curvature theorem,
not an unchecked invocation of the entire v2 theorem. Its canonical
statement and the existing polynomial and curvature certification reports
were inspected; their statement fingerprints agree with those above.
The curvature dossier uses the polynomial estimate and analytic foundations;
the polynomial estimate traces to the certified Letwin quadratic input.
Neither this argument nor those declared inputs use BKL, a BKL coefficient
consequence, or KLS as a premise. The current proved status of KLS elsewhere
in the repository is irrelevant to this proof.

The fingerprint command completed successfully. The full
`UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py` reported no MyST error
for the reviewed dossier. It exited with 13 unrelated errors during concurrent
integration: missing canonical anchors for the height-profile, height-reduction,
small-loss and summable-budget draft nodes, and unresolved references to the
latter two nodes in other draft dossiers. These were reported to the
orchestrator and do not affect the checked statement or proof. No numerical
run was used as evidence.

## Corrections

None in the reviewed proof.

## Exclusions

This report certifies only [](#prop:sz-v2-common-radius). It does not certify
the higher-order raw orbit, block initialization, retained prefixes, energy
budgets, repeated height reduction, small-loss refinement, summable-budget
construction, or the final v2 KLS theorem. The prior analytic, polynomial and
curvature certifications are used as inputs, not reissued by this report.
Weak approximation to nonregular laws is not part of this proposition; only
the polynomial form-domain cutoff and fixed-law scalar limit are checked here.

## Certification delta

Set `prop:sz-v2-common-radius` to `proved`, retain its source reference and
`depends_on: [def:sz-v2-common-radius, lem:sz-analytic-foundations,
thm:sz-polynomial-variance, thm:sz-curvature-comparison]`, and add:

```yaml
proofs:
  - artifact: solutions/sz-v2-height-reduction.md
    review: research/reviews/2026-10-06-sz-v2-radius-review.md
```

Keep `def:sz-v2-common-radius` as `defined`. No other status or relation
change follows from this certification.
