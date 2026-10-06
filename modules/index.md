---
title: Welcome
numbering: false
---

% The site's welcome page: no statement lives here. The mathematical introduction is
% modules/00-overview.md; this page only says what there is and where to go.

This site is a reader's companion to the two proofs of the Kannan–Lovász–Simonovits (KLS) theorem — reconstructed, checked and compared here — to the methods that led to them, and to the questions that remain open after KLS.

:::{note} How the proofs here are checked
Proofs reconstructed here by agents are checked by separate reviewer agents. This is distinct from journal peer review or human acceptance. Each statement shows who checked it; details are in [how results are checked](#sec:overview-checking).
:::

The KLS conjecture, [](#conj:kls), asked whether every isotropic log-concave measure has a Poincaré constant independent of the dimension. For a Gaussian that constant is one; the question was whether a universal bound survives without symmetry or product structure. Two preprints deposited on 4 October 2026 answer it: Bizeul–Klartag–Lehec (BKL), through all-order cumulant estimates, suspension and the spectral criterion of the first version of Song–Zhang, proved again in exponential form [@BizeulKlartagLehec2026KLS], and the second version of Song–Zhang, through repeated refinement with summable losses [@SongZhang2026ConstantKLS].

:::{note} The use of AI in the two proofs
Both sets of authors declare their use of AI.

- BKL write that "most proofs and mathematical ideas in this paper were found by ChatGPT; a notable exception is the idea to use suspension which was suggested by the authors. The role of the authors has been mostly to understand these proofs and improve their exposition" (Acknowledgements, p. 5 of [@BizeulKlartagLehec2026KLS]).
- Song and Zhang write that "the AI tools used in this work were GPT-6 Astra, GPT-5.6 Sol, Claude Fable 5, and Fable 5.1", and that their effort since 28 July 2026 "involved exploring more than 100 approaches in collaboration with AI tools", "with the authors deciding which ones to prioritize" (Acknowledgements and AI Disclosure, pp. 138–139 of [@SongZhang2026ConstantKLS]).
:::

Besides these proofs, the manuscript develops three alternative mechanisms for the Poincaré bound, which would give KLS by other means or with stronger conclusions. Their exact moment-Hessian calculations, conditional reductions and counterexamples keep their meaning now that KLS is proved.

(sec:reading-paths)=
## Where to start

Four ways in, depending on what you came for:

- **Discover.** The overview, Chapter [](#sec:overview); what the theorem gives and the question of its constant, Chapter [](#sec:kls-after-proofs); then the map of alternative mechanisms, Chapter [](#sec:frontier-atlas).
- **Read the proofs.** The first version of Song–Zhang, whose spectral criterion both proofs use, Chapter [](#sec:polynomial-curvature); Bizeul–Klartag–Lehec, the shorter argument from that criterion, Chapter [](#sec:bkl-proof); the second version of Song–Zhang, Chapter [](#sec:sz-v2-proof), with its technical estimates in Chapter [](#sec:sz-v2-blocks); then their comparison, Chapter [](#sec:kls-synthesis).
- **Read the alternative mechanisms.** The three entry chapters listed below.
- **Contribute.** The problems for someone who might take them up, Section [](#sec:overview-open), then how results are checked, below.

After the overview come *the literature*, one chapter for each of six families of methods; *two proofs of KLS*: the first version of Song–Zhang, Bizeul–Klartag–Lehec, the second version of Song–Zhang, then their comparison; *after KLS*, what the theorem gives and the question of its constant, then the map of alternative mechanisms; the *alternative mechanisms* themselves; *shared technical foundations*, best read where first linked; and an *archive* holding the fixed cut and its technical chapters. The full proofs come last.

## Three alternative mechanisms, and an archive

Each mechanism needs an argument of its own: neither proof of KLS gives its sufficient condition.

- **Moment map** — a deterministic inequality for the Hessian of the moment map, which implies KLS and is not known to be equivalent to it, and which would give the Poincaré bound with constant $4$ and no stochastic localization: Chapter [](#sec:moment-map-cmh).
- **Fixed eigenfunction** — a localization mechanism that follows a first eigenfunction and so ignores covariance spikes in directions it does not use: Chapter [](#sec:spectral-approach).
- **Conditional fibers** — an elementary mechanism, a spectral gap for resampling along lines chosen from the measure, resting only on one-dimensional inequalities: Chapter [](#sec:conditional-fiber-frame).

The **fixed cut**, which follows one would-be bottleneck set through stochastic localization, is kept as an archive for its obstructions, its ceiling and its counterexamples: Chapter [](#sec:introduction).

Chapter [](#sec:frontier-atlas) compares the three mechanisms side by side — what each would add, and what blocks it.

## What this manuscript contributes

**The proofs, reconstructed, checked and compared.**

- A reconstruction of the first version of Song–Zhang's polynomial–curvature mechanism, Chapter [](#sec:polynomial-curvature), with its reusable profile transfer [](#thm:sz-curvature-transfer), affine bound [](#cor:sz-affine-poincare), and exponential coefficient characterization of KLS [](#prop:sz-exponential-coefficients-equivalence).
- A reconstruction of the Bizeul–Klartag–Lehec cumulant and suspension argument, Chapter [](#sec:bkl-proof), including its exact comparison with Appell coefficients.
- A reconstruction of the universal bound of the second version of Song–Zhang, [](#thm:sz-v2-kls), with the finite-block estimates and summable-cost argument explained in Chapters [](#sec:sz-v2-proof) and [](#sec:sz-v2-blocks).
- A comparison of the two proofs, Chapter [](#sec:kls-synthesis), and an account of what the theorem gives and of the question of its constant, Chapter [](#sec:kls-after-proofs).

**Results proved here.**

- An inequality for the Hessian of the moment map, the canonical moment-Hessian constant of [](#def:cmh), which by [](#thm:cmh-implies-affine-poincare) bounds the affine Poincaré constant with no loss.
- Exact values of that constant on the line ([](#thm:cmh-1d)), on products ([](#thm:cmh-product)) and on every log-concave Dirichlet law ([](#thm:cmh-dirichlet)), with the Poincaré consequence [](#cor:cmh-dirichlet-poincare).
- An identity, [](#lem:linear-sector-third-moment), reducing the linear test of that inequality to a third-moment tensor, and a countermodel, [](#prop:letwin-not-gate-zero), saying that matrix inequalities over fixed matrices cannot supply it.
- A reduction of KLS to an occupation estimate for one eigenfunction followed through stochastic localization, [](#prop:spectral-sufficiency).
- A reduction of KLS to a spectral gap for resampling along conditional lines, [](#lem:conditional-fiber-form), and an obstruction for the most natural frame of lines on the simplex, [](#prop:conditional-fiber-root-obstruction).
- In the fixed-cut archive: a bootstrap, [](#thm:bootstrap), its ceiling, [](#prop:ceiling), and a product counterexample to a natural weighted estimate, [](#prop:weighted-spectator-obstruction).

The overview explains each with the idea of its proof (Section [](#sec:overview-results)).

(sec:overview-checking)=
## How results are checked, and how to contribute

Every labelled statement is fixed text, and its status, shown next to its title, is kept apart from the prose:

- *Not settled here*: this manuscript does not settle the statement; it says nothing about the literature.
- *Preprint, not yet checked here*: a recent source's announced result, not yet checked by this project.
- *Proved*, or *Proved (from a preprint)* for a source's result checked here: a written proof, checked against the statement by a reviewer, linked from the status, which names who checked it and when.
- *Established in the literature*: a result of the field, cited and not reproved.
- *Refuted by*: the statement that refutes it.

A reviewer agent's check is distinct from journal peer review and from a person's review or acceptance, which are recorded separately; computations never count as proof. What each certification means is explained on the [full proofs](../proofs.md) page.

**How to contribute.** A proof, a counterexample, a partial result, a missed reference or a correction:

- **On a statement:** next to its title are its label, for instance `conj:gate-zero-sharp`, and links that open a form on the [project repository](https://github.com/human-ai-mathematics/kls-conjecture-search/issues) with the label filled in — *Idea* or *Counterexample* on a statement not settled here, *Correction* on any other.
- **In discussion:** ask a question (*Q&A*), think out loud (*Ideas*) or point at a reference (*Literature*) in the project's [GitHub Discussions](https://github.com/human-ai-mathematics/kls-conjecture-search/discussions), naming a statement by its label.
