---
title: Welcome
numbering: false
---

% The site's welcome page: no statement lives here. The mathematical introduction is
% modules/00-overview.md; this page only says what there is and where to go. It is the
% single place for the site's organization and for how results are checked; the list of
% results here is short and without commentary, the full account is Section sec:overview-results.

The Kannan–Lovász–Simonovits (KLS) conjecture, [](#conj:kls), asked whether every isotropic log-concave measure has a Poincaré constant bounded independently of the dimension. For a Gaussian that constant is one; the question was whether a universal bound survives without symmetry or product structure. It is now a theorem: three preprints of October 2026 prove it, by Bizeul–Klartag–Lehec (BKL) [@BizeulKlartagLehec2026KLS], by Song–Zhang in the second version of their preprint (SZ v2) [@SongZhang2026ConstantKLS], and by Balasubramanian–Kasiviswanathan (BK) [@BalasubramanianKasiviswanathan2026KLS].

This site adds three things the preprints do not: a complete account of each of the three arguments, a comparison of them, and an account of the methods around them, including three alternative mechanisms for the Poincaré bound with exact computations, conditional reductions and counterexamples of their own. Each argument is rewritten so that every step is a complete statement with a complete proof, or a citation of an established published result, and each of these proofs has been checked against its statement by a separate reviewer agent; no person has yet reviewed or accepted them.

:::{note} How the proofs here are checked
The proofs written for this project are checked by separate reviewer agents, each run in a fresh context, without the conversation that produced the proof. Each statement shows who checked it; details are in [how results are checked](#sec:overview-checking).
:::

(sec:reading-paths)=
## Where to start

Four ways in, depending on what you came for:

- **Discover.** The overview, Chapter [](#sec:overview); what the theorem gives and the question of its constant, Chapter [](#sec:kls-after-proofs); then the map of alternative mechanisms, Chapter [](#sec:frontier-atlas).
- **Read the proofs.** The first version of Song–Zhang, whose spectral criterion underlies BKL and SZ v2, Chapter [](#sec:polynomial-curvature); Bizeul–Klartag–Lehec, the shorter argument from that criterion, Chapter [](#sec:bkl-proof); the second version of Song–Zhang, Chapter [](#sec:sz-v2-proof), with its technical estimates in Chapter [](#sec:sz-v2-blocks); Balasubramanian–Kasiviswanathan, Chapter [](#sec:bk-proof); then their comparison, Chapter [](#sec:kls-synthesis).
- **Read the alternative mechanisms.** The moment map, Chapter [](#sec:moment-map-cmh); the fixed eigenfunction, Chapter [](#sec:spectral-approach); conditional fibers, Chapter [](#sec:conditional-fiber-frame). The fixed cut, an earlier localization argument kept for its obstructions and counterexamples, opens the archive, Chapter [](#sec:introduction).
- **Contribute.** The problems for someone who might take them up, Section [](#sec:overview-open), then how results are checked, below.

Recurring terms and their normalizations are collected in the [glossary](#sec:glossary).

## What this manuscript contributes

**The three proofs.**

- BKL bound cumulants of every order uniformly in the dimension, then encode an arbitrary test function as one extra coordinate (suspension): Chapter [](#sec:bkl-proof).
- SZ v2 refines one coefficient radius repeatedly, with losses whose product stays bounded: Chapters [](#sec:sz-v2-proof) and [](#sec:sz-v2-blocks).
- BK control every power of an integration operator on compatible tensor fields with one common factor, and close a direct induction in the polynomial degree, with an explicit constant: Chapter [](#sec:bk-proof).
- The first version of Song–Zhang, whose spectral criterion the first two proofs use, is worked through as preparation (Chapter [](#sec:polynomial-curvature)); the three proofs are compared in Chapter [](#sec:kls-synthesis).

**Results proved in this manuscript.**

- The moment-Hessian inequality [](#def:cmh) bounds the affine Poincaré constant with no loss ([](#thm:cmh-implies-affine-poincare)).
- Its exact value on the line ([](#thm:cmh-1d)) and on products ([](#thm:cmh-product)), and the bound $4$, sharp over the family, on every log-concave Dirichlet law ([](#thm:cmh-dirichlet), [](#cor:cmh-dirichlet-poincare)).
- Its linear test reduced to a third-moment tensor ([](#lem:linear-sector-third-moment)), and a countermodel for fixed-matrix arguments ([](#prop:letwin-not-gate-zero)).
- A reduction of KLS to an occupation estimate for one eigenfunction ([](#prop:spectral-sufficiency)).
- A reduction of KLS to a gap for resampling along lines ([](#lem:conditional-fiber-form)), and an obstruction on the simplex ([](#prop:conditional-fiber-root-obstruction)).
- In the fixed-cut archive: a bootstrap ([](#thm:bootstrap)), its ceiling ([](#prop:ceiling)) and a product counterexample ([](#prop:weighted-spectator-obstruction)).

Each is explained with the idea of its proof in Section [](#sec:overview-results).

(sec:ai-use)=
:::{note} The use of AI in the three proofs
:class: dropdown
All three sets of authors declare their use of AI.

- BKL write that "most proofs and mathematical ideas in this paper were found by ChatGPT; a notable exception is the idea to use suspension which was suggested by the authors. The role of the authors has been mostly to understand these proofs and improve their exposition" (Acknowledgements, p. 5 of [@BizeulKlartagLehec2026KLS]).
- Song and Zhang write that "the AI tools used in this work were GPT-6 Astra, GPT-5.6 Sol, Claude Fable 5, and Fable 5.1", and that their effort since 28 July 2026 "involved exploring more than 100 approaches in collaboration with AI tools", "with the authors deciding which ones to prioritize" (Acknowledgements and AI Disclosure, pp. 138–139 of [@SongZhang2026ConstantKLS]).
- Balasubramanian and Kasiviswanathan write: "We developed this proof with substantial assistance from several frontier AI models." "The AI identified the need for estimates uniform in tensor rank and formulated a weighted Hodge comparison for symmetric tensor fields." "The AI proposed Appell coefficient norms to measure repeated centered integration of constant tensors." "We have carefully verified all arguments developed with the assistance of AI and take full responsibility for the content of this work." (§1.2, p. 5 of [@BalasubramanianKasiviswanathan2026KLS]).
:::

(sec:overview-checking)=
## How results are checked, and how to contribute

Every labelled statement is fixed text, and its status, shown next to its title, is kept apart from the prose:

- *Not settled here*: this manuscript does not settle the statement; it says nothing about the literature.
- *Preprint, not yet checked here*: a recent source's announced result, not yet checked by this project.
- *Proved*, or *Proved (from a preprint)* for a source's result checked by this project: a written proof, checked against the statement by a reviewer, linked from the status, which names who checked it and when.
- *Established in the literature*: a result of the field, cited and not reproved.
- *Refuted by*: the statement that refutes it.

A reviewer agent's check is distinct from journal peer review and from a person's review or acceptance, which are recorded separately; computations never count as proof. Since KLS is proved, a counterexample to a statement not settled here refutes that statement, not KLS; the alternative mechanisms aim at other proofs, a sharp constant, or properties that imply KLS. What each certification means is explained on the [full proofs](../proofs.md) page.

**How to contribute.** The site is maintained by Nicolas Brosse and open to collaboration; contributors are credited in the history of the repository. A proof, a counterexample, a partial result, a missed reference or a correction is welcome:

- **On a statement:** next to its title are its label, for instance `conj:gate-zero-sharp`, and links that open a form on the [project repository](https://github.com/human-ai-mathematics/kls-conjecture-search/issues) with the label filled in — *Idea* or *Counterexample* on a statement not settled here, *Correction* on any other.
- **In discussion:** ask a question (*Q&A*), think out loud (*Ideas*) or point at a reference (*Literature*) in the project's [GitHub Discussions](https://github.com/human-ai-mathematics/kls-conjecture-search/discussions), naming a statement by its label.
