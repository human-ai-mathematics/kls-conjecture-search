---
title: Welcome
numbering: false
---

% The site's welcome page: no statement lives here. The mathematical introduction is
% modules/00-overview.md; this page only says what there is and where to go.

The Kannan–Lovász–Simonovits (KLS) conjecture, [](#conj:kls), asks whether every isotropic log-concave measure satisfies a Poincaré inequality with a constant independent of the dimension — equivalently, whether convex bodies have no bottlenecks beyond those a hyperplane already sees. The best published bound grows like $\log n$, and the question is a central open problem of high-dimensional convex geometry.

(sec:reading-paths)=
## Where to start

Three ways in, depending on what you came for:

- **Discover.** The overview, Section [](#sec:overview), then the comparison of approaches, Section [](#sec:frontier-atlas).
- **Read the results.** The four entry chapters listed below, each opening with the same summary, then the synthesis, Section [](#sec:kls-synthesis).
- **Contribute.** The problems for someone who might take them up, Section [](#sec:overview-open), then how results are checked, below.

After the overview come *the literature*, one chapter per family of methods; *the four approaches*, opened by their comparison and a prelude on stochastic localization; *synthesis and perspectives*; and *shared technical foundations*, best read where first linked. The full proofs come last.

## The four approaches

Each approach responds to the same obstacle, explained in Section [](#sec:kls-remaining): known methods control a fixed or averaged object, while the conjecture needs control of one that adapts.

- **Fixed eigenfunction** — follow a first eigenfunction through stochastic localization: Section [](#sec:spectral-approach).
- **Moment map** — a deterministic second-order inequality for the Hessian of the moment map: Section [](#sec:moment-map-cmh).
- **Fixed cut** — follow one would-be bottleneck set through stochastic localization: Section [](#sec:introduction).
- **Conditional fibers** — a spectral gap for resampling along lines chosen from the measure: Section [](#sec:conditional-fiber-frame).

Section [](#sec:frontier-atlas) compares them side by side: what each gives, and what blocks it.

## What this manuscript contributes

- An inequality for the Hessian of the moment map, the canonical moment-Hessian constant of [](#def:cmh), which by [](#thm:cmh-implies-affine-poincare) bounds the affine Poincaré constant with no loss.
- Exact values of that constant on the line ([](#thm:cmh-1d)), on products ([](#thm:cmh-product)) and on every log-concave Dirichlet law ([](#thm:cmh-dirichlet)), the first non-product family, with the Poincaré consequence [](#cor:cmh-dirichlet-poincare).
- An identity, [](#lem:linear-sector-third-moment), reducing the linear test of that inequality to a third-moment tensor, and a countermodel, [](#prop:letwin-not-gate-zero), saying that matrix inequalities over fixed matrices cannot supply it.
- A reduction of KLS to an occupation estimate for one eigenfunction followed through stochastic localization, [](#prop:spectral-sufficiency).
- A reduction of KLS to a spectral gap for resampling along conditional lines, [](#lem:conditional-fiber-form), and an obstruction for the most natural frame of lines on the simplex, [](#prop:conditional-fiber-root-obstruction).
- For the oldest localization argument, which follows one cut: a bootstrap, [](#thm:bootstrap), its ceiling, [](#prop:ceiling), and a product counterexample to a natural weighted estimate, [](#prop:weighted-spectator-obstruction).

The overview explains each with the idea of its proof (Section [](#sec:overview-results)).

(sec:overview-checking)=
## How results are checked, and how to contribute

**Statements and their status.** Every labelled statement is fixed text, and its status is shown next to its title from a record kept apart from the prose. *Not settled here* says only that this manuscript does not settle the statement, nothing about the literature. *Preprint, not yet checked here* marks a recent source's announced result, used as stated there but not yet checked by the field or by this project; every statement using one names it. Once this project has checked such a result with its own written proof and review, it shows *Proved (from a preprint)*. *Established in the literature* marks a result of the field, cited and not reproved. *Refuted by* names the statement that refutes it.

**What counts as proved.** A statement shows *Proved*, linked to its complete written proof, only once someone other than the proof's author has checked that proof against the statement; next to it is who checked it: an agent review, with its model and date, a review by a named person, or a person's acceptance. An edited statement loses that check until reviewed again. Computations never count as proof.

**How to contribute.** A proof, a counterexample, a partial result, a missed reference or a correction:

- **On a statement:** next to its title are its label, for instance `conj:gate-zero-sharp`, and links that open a form on the [project repository](https://github.com/numina-functional-inequalities/kls-conjecture-search/issues) with the label filled in — *Idea* or *Counterexample* on a statement not settled here, *Correction* on any other.
- **In discussion:** ask a question (*Q&A*), think out loud (*Ideas*) or point at a reference (*Literature*) in the project's [GitHub Discussions](https://github.com/numina-functional-inequalities/kls-conjecture-search/discussions), naming a statement by its label.
