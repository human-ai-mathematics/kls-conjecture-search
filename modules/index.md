---
title: Welcome
numbering: false
---

% The site's welcome page: no statement lives here. The mathematical introduction is
% modules/00-overview.md; this page only says what there is and where to go.

:::{note} Two reconstructed proofs and their verification
Bizeul–Klartag–Lehec v1 and Song–Zhang v2, both deposited on
4 October 2026, give two proofs of the universal KLS bound
[@BizeulKlartagLehec2026KLS; @SongZhang2026ConstantKLS]. Both have been
reconstructed here by agents and checked by separate reviewer agents.
This local verification is distinct from journal peer review and human
acceptance. The proof and review information appears beside each statement.
BKL close the argument through cumulants and suspension
([](#sec:bkl-proof)); SZ v2 use repeated refinement with summable costs
([](#sec:sz-v2-proof)). The two mechanisms share spectral foundations.
:::

The Kannan–Lovász–Simonovits (KLS) conjecture, [](#conj:kls), asks whether every isotropic log-concave measure has a Poincaré constant independent of dimension. For a Gaussian that constant is one; the question is whether a universal bound survives without symmetry or product structure. BKL’s proof combines all-order cumulant estimates, suspension and a spectral criterion from Song–Zhang.

This manuscript develops the proof mechanisms of Song–Zhang and BKL and four approaches to alternative proofs and structural inequalities. The exact moment-Hessian calculations, conditional reductions and counterexamples below retain their meaning after the proof of KLS.

(sec:reading-paths)=
## Where to start

Three ways in, depending on what you came for:

- **Discover.** The overview, Section [](#sec:overview), then the comparison of approaches, Section [](#sec:frontier-atlas).
- **Read the results.** The four entry chapters listed below, for this manuscript's own approaches; polynomial estimates and curvature, Section [](#sec:polynomial-curvature), followed by Song–Zhang v2, Section [](#sec:sz-v2-proof), and the BKL argument, Section [](#sec:bkl-proof); then the synthesis, Section [](#sec:kls-synthesis).
- **Contribute.** The problems for someone who might take them up, Section [](#sec:overview-open), then how results are checked, below.

After the overview come *the literature*, one chapter for each of six families of methods; *polynomial methods and two proofs of KLS*, from the original iteration to repeated refinement and to cumulants and suspension; *the four approaches*, opened by their comparison; *synthesis and perspectives*; *shared technical foundations*, best read where first linked; and an *appendix* holding the technical chapters of the fixed cut. The full proofs come last.

## The four approaches

Two arguments already reach every test function, [](#thm:letwin-kls) and [](#thm:song-zhang-kls), at a cost that grows with the dimension. The approaches below seek distinct mechanisms and structural estimates. Neither KLS proof establishes their sufficient conditions: moment-Hessian, occupation and conditional-frame bounds each need their own argument.

- **Moment map** — a deterministic second-order inequality for the Hessian of the moment map: Section [](#sec:moment-map-cmh).
- **Fixed eigenfunction** — follow a first eigenfunction through stochastic localization: Section [](#sec:spectral-approach).
- **Conditional fibers** — a spectral gap for resampling along lines chosen from the measure: Section [](#sec:conditional-fiber-frame).
- **Fixed cut** — follow one would-be bottleneck set through stochastic localization: Section [](#sec:introduction).

They are listed in the order of what each has established, not of their prospects. Section [](#sec:frontier-atlas) compares them side by side — what each gives, and what blocks it — and states the current research priorities separately.

## What this manuscript contributes

- An inequality for the Hessian of the moment map, the canonical moment-Hessian constant of [](#def:cmh), which by [](#thm:cmh-implies-affine-poincare) bounds the affine Poincaré constant with no loss.
- Exact values of that constant on the line ([](#thm:cmh-1d)), on products ([](#thm:cmh-product)) and on every log-concave Dirichlet law ([](#thm:cmh-dirichlet)), the first non-product family, with the Poincaré consequence [](#cor:cmh-dirichlet-poincare).
- An identity, [](#lem:linear-sector-third-moment), reducing the linear test of that inequality to a third-moment tensor, and a countermodel, [](#prop:letwin-not-gate-zero), saying that matrix inequalities over fixed matrices cannot supply it.
- A reduction of KLS to an occupation estimate for one eigenfunction followed through stochastic localization, [](#prop:spectral-sufficiency).
- A reduction of KLS to a spectral gap for resampling along conditional lines, [](#lem:conditional-fiber-form), and an obstruction for the most natural frame of lines on the simplex, [](#prop:conditional-fiber-root-obstruction).
- For the oldest localization argument, which follows one cut: a bootstrap, [](#thm:bootstrap), its ceiling, [](#prop:ceiling), and a product counterexample to a natural weighted estimate, [](#prop:weighted-spectator-obstruction).
- A reconstruction of the BKL cumulant and suspension argument checked by independent agent reviews, Chapter [](#sec:bkl-proof), including its exact comparison with Appell coefficients.
- A reconstruction of the Song–Zhang v2 universal bound checked by separate reviewer agents, [](#thm:sz-v2-kls), with the finite-block estimates and summable-cost argument explained in Chapter [](#sec:sz-v2-proof).
- A reconstruction of Song–Zhang's pinned v1 polynomial–curvature mechanism, with its reusable profile transfer [](#thm:sz-curvature-transfer), affine bound [](#cor:sz-affine-poincare), and exponential coefficient characterization of KLS [](#prop:sz-exponential-coefficients-equivalence).

The overview explains each with the idea of its proof (Section [](#sec:overview-results)).

(sec:overview-checking)=
## How results are checked, and how to contribute

**Statements and their status.** Every labelled statement is fixed text, and its status is shown next to its title from a record kept apart from the prose. *Not settled here* says only that this manuscript does not settle the statement, nothing about the literature. *Preprint, not yet checked here* marks a recent source's announced result whose proof has not yet been checked by this project; every statement using one names it. Once this project has checked such a result with its own written proof and review, it shows *Proved (from a preprint)*. *Established in the literature* marks a result of the field, cited and not reproved. *Refuted by* names the statement that refutes it.

**What counts as proved.** For proofs reconstructed here by agents, a separate reviewer agent checks the written proof against its statement; the status names the reviewer's model and date. This is distinct from journal peer review or human acceptance. A named person's review or explicit acceptance is recorded separately; a human acceptor may also be the proof's author. Substantive changes require renewed review or acceptance. Each proved statement links to its full proof. Computations never count as proof.

**How to contribute.** A proof, a counterexample, a partial result, a missed reference or a correction:

- **On a statement:** next to its title are its label, for instance `conj:gate-zero-sharp`, and links that open a form on the [project repository](https://github.com/human-ai-mathematics/kls-conjecture-search/issues) with the label filled in — *Idea* or *Counterexample* on a statement not settled here, *Correction* on any other.
- **In discussion:** ask a question (*Q&A*), think out loud (*Ideas*) or point at a reference (*Literature*) in the project's [GitHub Discussions](https://github.com/human-ai-mathematics/kls-conjecture-search/discussions), naming a statement by its label.
