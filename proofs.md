---
title: Full proofs
numbering: false
---

% The introduction to the dossiers under solutions/, which myst.yml lists after it. It
% lives here, not in solutions/, where every page is read as a dossier.

Each proved statement links to its complete written proof, listed below. A proof counts
once an independent reviewer has checked it against the precise statement or a named
human explicitly accepts it, including their own proof. That certification is recorded; a proof still being written or checked is not published.

Next to *Proved*, each statement says who checked its proof, and when:

- *agent review (model, date)*: an AI agent, run in a fresh context with no access to
  the conversation that produced the proof, checked it line by line. The link opens its
  report.
- *reviewed by* a name: a person checked it the same way, and wrote the report.
- *accepted by* a name: a person read the proof and vouches for it, without a written
  report; the person may also be the proof's author.

A statement marked *Established in the literature* is an established result of the field,
cited where it is stated, and not reproved here. A statement marked *Preprint, not yet
checked here* is a result a recent source announces: it is used as that source states it,
but neither the field nor this project has checked its proof yet, and every statement
resting on it says so. Once this project has checked it, with a written proof and a
review or human acceptance, it shows *Proved (from a preprint)* followed by who checked it.

For the polynomial and curvature argument, read the proofs in this order:

1. [Analytic foundations and Appell variance estimates](solutions/thm-sz-polynomial-variance.md).
2. [The comparison from polynomial coefficients to curvature](solutions/thm-sz-curvature-comparison.md).
3. [The iteration of curvature profiles](solutions/thm-sz-iterated-curvature.md).
4. [Gaussian transfer, the all-depth bound and its affine form](solutions/thm-song-zhang-kls.md).

The separate [exponential coefficient criterion](solutions/prop-sz-exponential-coefficients-equivalence.md)
uses the comparison to characterize exactly the coefficient growth equivalent to KLS.
The polynomial and curvature chapter, Section [](#sec:polynomial-curvature),
explains how these arguments fit together and where dimension dependence remains.

The [balanced-survival proof](solutions/lem-survival-implies-kls.md) treats arbitrary
measurable cuts and nonsmooth log-concave posteriors directly. For the other
approaches, the [product-simplex cone calculation](solutions/prop-product-simplex-cone-gate.md)
determines the sharp linear gate and its equality directions, while the
[polynomial fiber bound](solutions/lem-fiber-polynomial-floor.md) excludes
asymptotically vanishing simplex certificates at every fixed polynomial degree.
