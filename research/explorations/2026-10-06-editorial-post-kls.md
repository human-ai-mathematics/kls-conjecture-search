---
---

# The manuscript repositioned after the proof of KLS

<!-- Orchestrator checkpoint for a writer's pass. No node, statement or status changes. -->

## Question examined

How should the published manuscript present itself now that `conj:kls` is proved, here
through two reconstructed proofs (`thm:sz-v2-kls` and the BKL chain)? Before this pass the
site still read as a report on an open problem, with notes announcing the proofs added on
top: a title naming a "frontier", motivations of the form "it implies KLS", the
verification caveat repeated in every chapter, one unestablished novelty claim, and no
mention of the AI use the authors of both proofs declare.

## What we learned

*Judgment (orchestrator, with the project owner's decisions).*

1. **Purpose.** The site is now a reader's companion to the two proofs, reconstructed,
   checked and compared, to the methods that led to them, and to the questions that remain
   open after KLS. Title: "The KLS theorem and its methods" (`myst.yml`, `sec:overview`,
   README).
2. **Order.** The proofs are presented along the development of the polynomial method:
   Song–Zhang v1 (`sec:polynomial-curvature`), Song–Zhang v2 (`sec:sz-v2-proof`), then
   BKL (`sec:bkl-proof`), which uses the spectral criterion of v1. This is not the
   deposit order: BKL v1 was submitted at 19:30:34 UTC on 4 October 2026, Song–Zhang v2 at
   21:21:03 UTC. The prose does not call the order chronological; the submission table in
   `sec:sz-v2-proof` keeps timestamp order.
3. **Verification wording.** Stated once, on the welcome page and in
   `sec:overview-checking`; each proof chapter keeps one pointer. Status badges carry the
   rest.
4. **Motivations after KLS.** The four approaches are presented by what they would add:
   a deterministic inequality with constant 4 (`def:cmh`), a localization mechanism that
   ignores covariance spikes (`conj:mm-spectral-occupation`), an elementary
   one-dimensional mechanism (`conj:conditional-fiber-frame`), and the fixed cut as the
   record of a method whose obstructions and ceiling are its results. The entry problems
   now open with `conj:gate-zero-sharp`, whose sharp constant 2 neither proof gives.
5. **Novelty.** The simplex sentence claiming what `thm:cmh-dirichlet` "adds" is replaced
   by "proved here", with Kolesnikov–Milman cited as earlier qualitative work, in line
   with `2026-10-06-post-bkl-dissemination.md`.
6. **AI use declared by the authors.** Quoted verbatim on the welcome page, checked
   against the arXiv PDFs: BKL v1, Acknowledgements, p. 5; Song–Zhang v2,
   Acknowledgements and AI Disclosure, pp. 138–139.

*Observed.* `check.py --statements` is identical before and after the pass (178
statements); `check.py` reports 0 errors. Module files renamed: the Song–Zhang v2 chapter
is now `07b`, the BKL chapter `07c`.

## What resists

- Statement titles still carry the older vocabulary, which a writer may not change:
  "Gate zero", "Sharp gate zero", "Gate zero controls the directional third moment"
  (`conj:gate-zero`, `conj:gate-zero-sharp`, `cor:gate-zero-third-moment`); "… implies
  KLS" in the fixed-cut chapters; "frontier" in two fixed-eigenfunction statements and
  in `sec:covariance-tech`. Renaming them changes fingerprints and lifts
  certifications; it is a separate decision.
- The welcome page says each approach "targets a property stronger than KLS"; for the
  conditional fibers and the fixed cut this overstates. To revisit in a later pass.

## Proposed next step

A human reading of the welcome page, the overview and the two composition proofs of
`conj:kls` before the `pages` workflow is dispatched.
