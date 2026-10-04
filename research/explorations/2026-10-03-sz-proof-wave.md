---
---

# Reconstructing the Song–Zhang proof chain

## Question examined

Can the source announcement `thm:song-zhang-kls` be turned into reusable,
independently checked results in this framework? The mission for
`ap:polynomial-curvature-audit` now includes full proof reconstruction and
certification, rather than only source integration.

## What we learned

*Observed — proof architecture.* The reconstruction separates analytic
foundations, dimension-free Appell variance estimates, polynomial-to-curvature
comparison, iterated curvature profiles, and the final Gaussian localization
transfer. These are the canonical nodes `lem:sz-analytic-foundations`,
`thm:sz-polynomial-variance`, `thm:sz-curvature-comparison`,
`thm:sz-iterated-curvature`, and `thm:song-zhang-kls`.
The affine consequence is `cor:sz-affine-poincare`. Registering statements
does not certify them.

Two proof authors work on disjoint dossiers. A reviewer who was launched in
a fresh context and previously performed only the independent consistency
review begins source verification; that reviewer has authored or directed
none of these proofs. Dossiers are frozen before review fingerprints are
recorded. Further stages follow the completed initial proofs.

*Observed — source provenance.* The source TeX archive of
arXiv:2610.01447v1 was downloaded for exact formula and hypothesis checking.
The published Klartag–Lehec survey, arXiv:2406.01324v2, supplies Theorem 20
and Corollary 21 for the bounded Lipschitz witness and Cheeger comparison;
their statements were checked against the source. Its BibTeX key is `KLnotes`.
Temporary local downloads are conveniences, not substitutes for these pinned
public references.

## What resists

No certification follows from the decomposition itself. Each new analytic
step, the degree/depth uniformity and the final approximation must be covered
by the relevant proof review. Existing CMH, occupation, trace and fiber
antecedents remain unchanged. Even the announced endpoint is not `conj:kls`.

## Proposed next step

Complete and independently review the foundations and polynomial dossier;
then the curvature comparison; then the iterated profiles and final transfer.
Repair any specific defect before applying its status change. Once the proof
chain stabilizes, reorganize the manuscript around the reusable results and
the exact remaining dimension-free difficulty.
