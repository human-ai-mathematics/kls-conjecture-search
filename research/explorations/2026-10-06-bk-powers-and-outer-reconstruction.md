---
---

# BK power lemma, coefficient induction, and scalar conclusion

## Question examined

On `ap:bk-reconstruction`, reconstruct the pinned BK abstract power lemma,
its integration corollaries, and the scalar degree induction; then supply
regular approximation and the final composition. The engaged nodes are
`lem:bk-uniform-power-bound`, `cor:bk-integration-powers`,
`cor:bk-quadratic-seed`, `thm:bk-appell-bound`,
`lem:bk-regular-approximation`, `thm:bk-explicit-poincare`,
`cor:bk-cheeger`, and `conj:kls`. Starting lens: **prove**.
Source: Balasubramanian–Kasiviswanathan, repository commit
`4837c33649ba2271f43c9684e9350ecbdd725f95`, Lemma 5.1, Corollaries 5.2–5.3,
Theorem 8.1, Corollary 8.2, Section 9, and Appendices C, E, F, G.

## What we learned

*Established, not certified.* The abstract power proof is written in
`solutions/lem-bk-uniform-power-bound.md`. A spectral-radius estimate makes
normalized adjoint orbits attain their maximum. The curvature recurrence
forces that maximum before the final observation index; two finite sums
then give one prefactor for every power. The same page proves both
integration corollaries conditionally on `prop:bk-integration-calculus`,
using `thm:letwin-qcts` only for the quadratic seed.

*Established, not certified.* `solutions/thm-bk-appell-bound.md` writes the
complete scalar induction with the source's radius and cutoff. Its strict
power-lemma hypothesis and prefactor are checked analytically. Every
coefficient used at degree $d$ has degree strictly below $d$; there is no
initial assumption that the all-degree uniform coefficient sequence is
finite. The explicit inputs are `prop:bk-integration-calculus` and
`prop:bk-reverse-transfer`, together with the preceding power lemma and
quadratic seed. No BKL, SZ v2, or KLS theorem enters.

*Established, not certified.* `solutions/lem-bk-regular-approximation.md`
reconstructs Gaussian curvature bounds, isotropic regularization, moment and
Appell Gram-matrix convergence, and the finite-energy test extension.
Normalized smoothing preserves the given positive lower curvature precisely
under the stated restriction $a\le1$. The test extension proves square
integrability rather than presupposing it.

*Established, not certified.* `solutions/thm-bk-explicit-poincare.md` takes
the degree limit at one fixed regular law before passing a uniform scalar
inequality through approximation. The covariance-at-most-identity case uses
a contraction from isotropic coordinates on the affine support. The Cheeger
conversion uses only `eq:cheeger-two-sided`. Finally,
`solutions/bk-kls-composition.md` handles infinite-energy functions with
extended variance and records the exact composition into `conj:kls`.

## What resists

No unresolved scalar algebraic step is claimed in these drafts, but their
mathematical validity remains for independent review. The integration
calculus and reverse-transfer estimates are expressly treated as inputs,
not certified by the power or induction work. The final dossiers remain
conditional on the upstream BK chain. None changes a ledger status or
closes `ap:bk-reconstruction`.

## Proposed next step

Independently review the abstract operator argument and approximation first.
After the separate Hodge, calculus, and localization reviews, review the
integration corollaries, induction, final scalar bound and target composition
in dependency order. Check the strict threshold, the fixed-law degree limit,
the weak-limit test domain, and the exclusion of BKL/SZ v2/KLS inputs.
