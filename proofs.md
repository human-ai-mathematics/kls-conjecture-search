---
title: Full proofs
numbering: false
---

% The introduction to the dossiers under solutions/, which myst.yml lists after it. It
% lives here, not in solutions/, where every page is read as a dossier. The groups below
% follow the order of the manuscript and match the groups of the toc in myst.yml; a new
% dossier is added to both.

Each statement marked *Proved* links to its complete written proof; this page lists them
all, grouped by argument in the order of the manuscript. Next to *Proved*, each statement says who checked
the proof, and when:

- *agent review (model, date)*: an AI agent, run without the conversation that produced
  the proof, checked it line by line against the statement; the link opens its report.
- *reviewed by* a name: a person checked it the same way and wrote the report.
- *accepted by* a name: a person read the proof and vouches for it, without a report.

*Proved (from a preprint)* marks a preprint's result whose proof has been written out and
checked here. *Preprint, not yet checked here* marks one that has not, and that no proof
here relies on; *Established in the literature* marks a published result, cited and not
reproved. An agent review is not journal refereeing, and no person has yet reviewed the
proofs of KLS below.

(sec:proofs-sz-v1)=
## Song–Zhang, first version

The spectral criterion and the iterated-logarithm bound of Chapter
[](#sec:polynomial-curvature):

1. [Analytic foundations and Appell variance estimates](solutions/thm-sz-polynomial-variance.md).
2. [Polynomial coefficients control the spectral gap](solutions/thm-sz-curvature-comparison.md).
3. [The iteration of curvature profiles](solutions/thm-sz-iterated-curvature.md).
4. [Gaussian transfer, the all-depth bound and its affine form](solutions/thm-song-zhang-kls.md).
5. [KLS and exponential growth of Appell coefficients](solutions/prop-sz-exponential-coefficients-equivalence.md),
   the end point that the next proofs reach.

(sec:proofs-bkl)=
## Bizeul–Klartag–Lehec

The proof of Chapter [](#sec:bkl-proof), which explains how its two branches, the tilt
criterion and the cumulant bound, meet in the suspension:

1. [Analytic foundations and tensor symmetrization](solutions/bkl-analytic-foundations.md).
2. [The tilt criterion and Appell duality](solutions/bkl-tilt-criterion.md).
3. [Inverse-covariance cumulant dynamics](solutions/bkl-cumulant-dynamics.md).
4. [Cumulant energy estimates](solutions/bkl-cumulant-energy.md).
5. [The all-order cumulant bound](solutions/bkl-cumulant-bound.md).
6. [Suspension, uniform coefficients and KLS](solutions/bkl-suspension-kls.md).
7. [A consequence: uniform conditional initialization](solutions/cor-bkl-uniform-conditional-initialization.md).

(sec:proofs-sz-v2)=
## Song–Zhang, second version

The proof of Chapters [](#sec:sz-v2-proof) and [](#sec:sz-v2-blocks); it uses no BKL
conclusion. The first-version proofs above stay attached to the first version.

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
   [KLS](solutions/sz-v2-kls-composition.md).

(sec:proofs-bk)=
## Balasubramanian–Kasiviswanathan

The proof of Chapter [](#sec:bk-proof); it uses Letwin's quadratic inequality and the
Appell normalization, but no BKL or SZ v2 conclusion, and its explicit constant
$1+2\cdot10^{16}$ comes from its own integration estimate.

1. [Approximation with covariance and curvature control](solutions/lem-bk-regular-approximation.md).
2. [Compatible-tensor Hodge estimates and domains](solutions/lem-bk-compatible-hodge.md),
   then [integration and Appell observations](solutions/prop-bk-integration-calculus.md).
3. [Uniform operator powers and the quadratic seed](solutions/lem-bk-uniform-power-bound.md).
4. [Covariance-normalized localization and moving Appell variance](solutions/lem-bk-localization-covariance.md),
   then [reverse coefficient transfer](solutions/prop-bk-reverse-transfer.md).
5. [The explicit degree induction](solutions/thm-bk-appell-bound.md),
   [the Poincaré and Cheeger constants](solutions/thm-bk-explicit-poincare.md),
   and [KLS](solutions/bk-kls-composition.md).

(sec:proofs-literature)=
## Results of the literature

Preprint results that the chapters use, with their proofs written out here; each
statement's status says whether its proof has been checked:

- [Letwin's matrix and quadratic estimates](solutions/thm-letwin-imports.md),
  [his third-moment bound and covariance control](solutions/letwin-covariance-windows.md),
  and [his bound $\CP\lesssim\sqrt{\log n}$](solutions/thm-letwin-kls.md)
  (Chapters [](#sec:family-moment-map) and [](#sec:family-sl)).
- [The Chen–Klartag moment-Hessian, thin-shell and third-tensor bounds](solutions/thm-chen-klartag-imports.md)
  (Chapter [](#sec:family-moment-map)).
- [Klartag–Lehec: stopped rank tails and integrated covariance](solutions/thm-kl-rank-imports.md)
  (Chapter [](#sec:covariance-tech)).

(sec:proofs-moment-map)=
## The moment map

The results of Chapters [](#sec:moment-map-cmh)–[](#sec:appendix-moment-map):

- [The moment-Hessian inequality, its operator data, and $\CPaff\le\CMH$](solutions/thm-cmh-normalization.md).
- [Exact constants on the line and on products, and the bound $4$ on Dirichlet laws](solutions/thm-cmh-dirichlet.md).
- [The linear test and the third-moment tensor](solutions/lem-linear-sector-third-moment.md),
  and [its spectral resolution](solutions/lem-cmh-linear-spectral-resolution.md).
- [The exponential cones](solutions/prop-cone-moment-map.md) and
  [cones over products of simplices](solutions/prop-product-simplex-cone-gate.md).
- [Approximation closure](solutions/prop-cmh-approximation-closure.md),
  [the recovery calculus](solutions/prop-cmh-recovery-calculus.md), and
  [lower semicontinuity of the affine Poincaré constant](solutions/lem-affine-poincare-w2-liminf.md).

(sec:proofs-eigenfunction)=
## The fixed eigenfunction

The results of Chapter [](#sec:spectral-approach):

- [Spectral sufficiency: the occupation estimate implies KLS](solutions/prop-spectral-sufficiency.md).
- [The posterior eigenfunction defect](solutions/lem-mm-posterior-defect.md),
  [restart deweighting](solutions/lem-mm-restart-deweighting.md), and
  [a small-gap fourth-moment bound](solutions/lem-mm-smallgap-fourth-moment.md).
- [The time-weighted source budget](solutions/lem-mm-time-weighted-fixed-source.md),
  [the stopped source bound](solutions/lem-mm-stopped-window-source.md), and
  [the occupation implication](solutions/prop-mm-window-occupation.md).

(sec:proofs-fibers)=
## Conditional fibers

The results of Chapter [](#sec:conditional-fiber-frame):

- [The resampling form and the simplex root obstruction](solutions/conditional-fiber-frame-structure.md).
- [A uniform floor at every fixed polynomial degree](solutions/lem-fiber-polynomial-floor.md).
- [The degree-two value for the root frame](solutions/lem-fiber-root-degree-two.md).

(sec:proofs-archive)=
## Foundations and the fixed-cut archive

The localization identities of Chapters [](#sec:notation)–[](#sec:models), and the results
of the fixed-cut archive, which opens with Chapter [](#sec:introduction):

- Foundations: [localization and Riccati identities](solutions/kls-localization-riccati-core.md),
  [full matrix dissipation](solutions/cor-full-matrix-dissipation.md),
  [quadratic chaos, Stein contrast and boundary flux](solutions/kls-qcts-stein-boundary-core.md),
  [consequences of Letwin's quadratic estimate](solutions/letwin-source-consequences.md), and
  [profile curvature and the model geometries](solutions/kls-geometry-models.md).
- From survival of one cut to KLS: [balanced survival](solutions/lem-survival-implies-kls.md),
  [Carleson control implies centroid control](solutions/thm-carleson-implies-centroid.md),
  [centroid control implies KLS](solutions/thm-centroid-implies-kls.md), and
  [the weighted near-Cheeger implication](solutions/thm-intro-weighted.md).
- The bootstrap: [the near-worst bootstrap](solutions/kls-bootstrap-interface.md),
  [its stopped covariance quantity](solutions/thm-bootstrap-stopped-interface.md), and
  [its residual dichotomy](solutions/cor-dichotomy.md).
- Budgets and products: [the scale-weighted source budget](solutions/lem-time-weighted-source.md),
  [Lyapunov–Stein duality](solutions/lem-lyapunov-stein-duality.md),
  [product coordinate budgets](solutions/kls-product-covariance.md),
  [split-class screened supply](solutions/prop-split-screened-supply.md), and
  [the excess and the perimeter martingale](solutions/kls-excess-audit.md).
- Counterexamples: [the exponential-spectator obstruction](solutions/prop-weighted-spectator-obstruction.md)
  and [its superlinear-remainder form](solutions/prop-spectator-excess-rate-obstruction.md).
