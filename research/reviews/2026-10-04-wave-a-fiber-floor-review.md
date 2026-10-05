---
verdict: pass
authors:
  - wave_a_fiber_dual, gpt-6-astra, 2026-10-04
reviewer: reviewer, gpt-6-astra, 2026-10-04
fingerprints:
  solutions/lem-fiber-polynomial-floor.md: 35b2b4025b979903a7397c8e8004e8429b399bce571e40422c98c4562ad15b4e
  lem:fiber-polynomial-floor: 50f764d580b958c67cd3fe22c414d4893a38766b58a000ca50bc03d5e37c1269
  lem:conditional-fiber-form: f2110f8c5c36056fda52257a3ad145a50f7c460b5bdc6b9ec4146e907db3cec2
  cor:cmh-dirichlet-poincare: 0295ebca6004666831c2db752ae739c062b86f6097e7b9f5152902d1765820c6
---

## Findings

Pass for [](#lem:fiber-polynomial-floor), after a full independent review in
a fresh context containing the assignment and repository artifacts, without
the authoring conversation. The dossier theorem agrees with the canonical
statement in every quantifier, constant, normalization and domain assertion.
Both dependencies are proved with existing independent certifications;
there is no `assumes` premise and no recorded `bounded_by` edge.

The proof was checked line by line, including the following points.

1. Rodrigues' formula gives the stated leading coefficient, endpoint values
   and orthogonality. Integrating against the degree-$n$ polynomial gives
   the factor $(2n)!/(2^{2n}(n!)^2)$ times the beta integral, hence norm
   $2/(2n+1)$. Expanding $P_n'$ against the lower Legendre polynomials gives
   coefficients $2j+1$ exactly when $n-j$ is odd. The derivative squared
   norm under the uniform probability is $n(n+1)/2$.
2. Pointwise Cauchy--Schwarz on the finite expansion gives the derivative
   operator bound by its squared Hilbert--Schmidt norm. The sum is
   $\sum_{n=1}^k n(n+1)(2n+1)/2=k(k+1)^2(k+2)/4$.
   The change of variables from $[-1,1]$ to an interval of length $L$
   contributes $4/L^2$ to derivative energy; the interval variance is
   $L^2/12$. Thus the constant in the reverse form inequality is exactly
   $12/A_k$. Centering removes only the constant coefficient.
3. Orthogonal Fubini for the uniform full-dimensional convex body in
   $H_0$ gives uniform conditional intervals for marginal-almost every
   fiber of every fixed direction. Zero-length fibers have zero marginal
   mass. The line parameter is Euclidean arc length because $|\theta|=1$.
   Restriction preserves the degree bound and its derivative is
   $\partial_\theta f$. The joint conditional versions are supplied by
   [](#lem:conditional-fiber-form); applying Tonelli to the nonnegative
   quantities is legitimate for arbitrary Borel frames, including atoms.
4. Compactness puts each polynomial in $L^2$ and bounds its gradient.
   Convexity then gives a Lipschitz constant $M$ on every chord. The
   independent-copy variance identity gives the upper bound $M^2$ for
   each conditional variance ratio, so the form is at most $dM^2$.
   This directly proves membership in the maximal domain, without a
   core approximation or a generator-domain claim.
5. Averaging the lower bound with the factor $d$ and the frame identity
   gives the full intrinsic gradient energy. No frame optimization or
   direction-dependent choice of the test is made in this step.
6. The uniform simplex is Dirichlet with all parameters one. Its moments
   are $\mathbb E P_i=1/m$, $\mathbb E P_i^2=2/(m(m+1))$, and
   $\mathbb E P_iP_j=1/(m(m+1))$ for $i\ne j$, giving covariance
   $P_{H_0}/(m(m+1))$. The stated scaling is therefore isotropic on
   $H_0$. Centering is realizable as a linear map on the affine simplex
   by $p\mapsto\sqrt{m(m+1)}P_{H_0}p$. The canonical affine Poincaré
   normalization has covariance in the gradient energy, so
   [](#cor:cmh-dirichlet-poincare) supplies ordinary constant at most
   four on $H_0$. Combining the inequalities gives $3/A_k$, with no
   universal CMH assumption.
7. The admissible set is nonempty, including for $m=2$: the probability
   uniform on the signed orthonormal basis has second moment $I/d$.
   The lower bound survives the infimum over nonconstant polynomials and
   the supremum over frames. Nonzero linear tests belong to every such
   polynomial space and have quotient one by the certified form lemma
   and isotropy. Hence the upper bound is one. Constants satisfy both
   original inequalities with zero on both sides; all $k\ge1$ are covered.
   Finally $A_3=240$, giving $1/80$.
8. An all-frame upper certificate, in the sense asserted, bounds
   $\Lambda_{m,k}$ from above. Its objective is therefore at least the
   positive floor for fixed $k$. No minimax interchange, existence of
   an optimizer, or construction of a dual certificate is needed.

Every used hypothesis is present: integers $m\ge2$, $k\ge1$, uniform
simplex density and its intrinsic full dimension, compact convex support,
the stated isotropic scale, real polynomials of degree at most $k$, unit
directions, Borel probability frames and their second-moment identity.
Evenness is part of admissibility but is unused in the estimate itself;
it is a harmless sharpening opportunity. No unstated hypothesis was found.

There is no external theorem imported by this dossier beyond its two
certified repository dependencies. The Legendre and beta-integral identities
are derived in the dossier and were checked directly; no unavailable source
or numerical artifact supports a step. The prior dependency proofs are
retained as certified results, not recertified here.

The full `uv run scripts/check.py` exited zero with no MyST error. The
fingerprints above were produced by the prescribed fingerprint command
on the examined versions.

## Corrections

None required.

## Exclusions

This certifies only [](#lem:fiber-polynomial-floor). It does not certify
the checkpoint's additional symmetry-reduction argument, exact finite
dimensional min-max values, any particular dual certificate, growing-degree
limits, or a full-domain gap. The unrestricted root-cap and negative-exchange
obstructions are compatible with the fixed-degree floor. Neither
[](#conj:conditional-fiber-frame) nor KLS is settled, and the sufficient
fiber-to-gradient bridge is not reversed.

## Proposed ledger delta

For `lem:fiber-polynomial-floor`, change `status` to `proved`, retain
`depends_on: [lem:conditional-fiber-form, cor:cmh-dirichlet-poincare]`, and add:

```yaml
proofs:
  - artifact: solutions/lem-fiber-polynomial-floor.md
    review: research/reviews/2026-10-04-wave-a-fiber-floor-review.md
```

No `assumes`, `bounded_by`, or `refuted_by` relation is introduced.
