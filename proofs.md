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
checked here* is a result a recent source announces whose proof has not yet been
certified in this project. This label makes no claim about checks performed elsewhere.
An uncertified input cannot support a locally proved result. Once this project has
checked it, with a written proof and a
review or human acceptance, it shows *Proved (from a preprint)* followed by who checked it.

The BKL proof is reconstructed and independently checked here in the following order:

1. [Analytic foundations and tensor symmetrization](solutions/bkl-analytic-foundations.md).
2. [The tilt criterion and Appell duality](solutions/bkl-tilt-criterion.md).
3. [Inverse-covariance cumulant dynamics](solutions/bkl-cumulant-dynamics.md).
4. [Cumulant energy estimates](solutions/bkl-cumulant-energy.md).
5. [The all-order cumulant bound](solutions/bkl-cumulant-bound.md).
6. [Suspension, uniform coefficients and KLS](solutions/bkl-suspension-kls.md).
7. [The unconditional initialization consequence](solutions/cor-bkl-uniform-conditional-initialization.md).

Section [](#sec:bkl-proof) explains how the two branches meet. These are
reconstructions of BKL v1, with independent agent reviews recorded for the
precise local statements; they are not a claim of a new proof independent of BKL.

For the earlier polynomial and curvature argument, read the proofs in this order:

1. [Analytic foundations and Appell variance estimates](solutions/thm-sz-polynomial-variance.md).
2. [The comparison from polynomial coefficients to curvature](solutions/thm-sz-curvature-comparison.md).
3. [The iteration of curvature profiles](solutions/thm-sz-iterated-curvature.md).
4. [Gaussian transfer, the all-depth bound and its affine form](solutions/thm-song-zhang-kls.md).

The separate [exponential coefficient criterion](solutions/prop-sz-exponential-coefficients-equivalence.md)
uses the comparison to characterize exactly the coefficient growth equivalent to KLS.
The polynomial and curvature chapter, Section [](#sec:polynomial-curvature),
explains how these arguments fit together and where dimension dependence remains.

The [balanced-survival proof](solutions/lem-survival-implies-kls.md) treats arbitrary
measurable cuts and nonsmooth log-concave posteriors directly.

The separate reconstruction of Song–Zhang v2 is explained in
Section [](#sec:sz-v2-proof). Its independently checked proofs follow this order:

1. [The common coefficient radius](solutions/sz-v2-height-reduction.md) and
   [static transfer, joint frames and skew credit](solutions/sz-v2-inner-foundations.md).
2. [The improved inner iteration](solutions/sz-v2-inner-refinement.md) and
   [its dimension bound](solutions/sz-v2-dimension-bound.md).
3. [Block construction and propagation](solutions/sz-v2-block-foundations.md),
   [joint loss estimates](solutions/sz-v2-joint-loss.md), and
   [fixed-cost repeated height reduction](solutions/sz-v2-height-blocks.md).
4. [Finite chains with retained bounds](solutions/sz-v2-chain-blocks.md) and
   [near-unit refinement](solutions/sz-v2-small-loss.md).
5. [Summable budgets and starting depths](solutions/sz-v2-summable-budgets.md),
   [the uniform Poincaré bound](solutions/sz-v2-kls.md), and
   [its composition with the KLS statement](solutions/sz-v2-kls-composition.md).

These are local independent agent reviews of a reconstruction, distinct from
journal refereeing. This argument uses no BKL conclusion or previously proved
KLS theorem. Both source proofs reuse earlier spectral foundations. The v1
proofs above remain attached to v1; the new certifications cover the v2
statements separately.

For the other approaches, the [product-simplex cone calculation](solutions/prop-product-simplex-cone-gate.md)
determines the sharp linear gate and its equality directions, while the
[polynomial fiber bound](solutions/lem-fiber-polynomial-floor.md) excludes
asymptotically vanishing simplex certificates at every fixed polynomial degree.

The proof of Balasubramanian–Kasiviswanathan is reconstructed and independently
checked in Chapter [](#sec:bk-proof), with the following reading order:

1. [Approximation with covariance and curvature control](solutions/lem-bk-regular-approximation.md).
2. [Compatible-tensor Hodge estimates and domains](solutions/lem-bk-compatible-hodge.md),
   then [integration and Appell observations](solutions/prop-bk-integration-calculus.md).
3. [Uniform operator powers and the quadratic seed](solutions/lem-bk-uniform-power-bound.md).
4. [Covariance-normalized localization and moving Appell variance](solutions/lem-bk-localization-covariance.md),
   then [reverse coefficient transfer](solutions/prop-bk-reverse-transfer.md).
5. [The explicit degree induction](solutions/thm-bk-appell-bound.md),
   [the Poincaré and Cheeger constants](solutions/thm-bk-explicit-poincare.md),
   and [the composition with KLS](solutions/bk-kls-composition.md).

The BK reconstruction uses Letwin's quadratic inequality and the same Appell
normalization as the earlier proofs, but no BKL or SZ v2 conclusion and no
previously proved KLS theorem. The constant $1+2\cdot10^{16}$ follows from its
own integration estimate and approximation, not from the older qualitative
exponential criterion. As with the other proofs, the checks are independent
agent reviews of the pinned preprint, distinct from journal refereeing.
