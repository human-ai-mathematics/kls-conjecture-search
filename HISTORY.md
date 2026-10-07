# History

The milestones of the search, newest first: results certified, statements refuted,
approaches opened or closed, outside preprints that moved the frontier, and changes to
the manuscript or the harness. One entry per milestone, not per session; the dated
checkpoints in [`research/explorations/`](research/explorations/) hold the detail.

This file only records history. What is proved now is in the
[ledger](research/program/ledger.yaml), and each statement on the
[site](https://human-ai-mathematics.github.io/kls-conjecture-search/) shows its
status. *Certified* means that a passing review independent of the proof's author checked
the proof. Unless a human is named, the author and the reviewer were AI agents.
Statements are named by label; paths are relative to the repository root.

## 2026-10-07: Dossier titles and the last process vocabulary

- The 76 dossier titles, shown in the *Full proofs* sidebar, now match the entries of
  `proofs.md`, with the argument as prefix ("BKL:", "Song–Zhang v2:", "BK:", …); the
  "Solution:" prefix of the template is dropped, here and in `templates/solution.md`.
- Five statements lose their last process words ("consumption", "the source",
  "premise"), among them the title of `cor:tight-window-consumption`; labels unchanged.
  An undefined reference to "soft-projector calculations" left Chapter 28.
- A fresh reviewer found no mathematical change:
  `research/reviews/2026-10-07-editorial-u-dossier-titles.md` and
  `research/reviews/2026-10-07-editorial-u-dossier-titles-window-occupation.md`.

## 2026-10-07: Editorial pass on the whole site

- Each proof is told once in detail, in its chapter (8, 9, 11); the overview keeps a
  calibration and one paragraph of idea per proof (about 20% shorter). Redundant
  summaries, scope caveats and internal vocabulary ("consume", "premise", "pinned",
  "badge", "the source") removed from the prose; obstacles explained once and linked.
- The family chapters (1–6) now say that KLS is proved and what each family does not
  reach alone; the history table of Chapter 2 runs to the three proofs; Chapter 21
  follows the template of the other mechanisms; the glossary's QCTS entry is corrected
  ("quadratic-chaos thin shell").
- Table of contents: "The proofs of KLS"; the map of mechanisms (Chapter 14) opens the
  alternative mechanisms; the fixed-cut archive merged from 11 chapters into 7
  (Chapters 28–34), every former chapter label kept as a section label. The dossiers are
  grouped under *Full proofs* as in `proofs.md`, which now lists all of them in the
  order of the manuscript; the versions table of Chapter 9 keeps dates only.
- Every dossier opens with a line naming its part and chapter; raw `research/` paths
  removed from five dossiers; seven statements reworded ("KLS" for "the KLS conjecture",
  two titles without process vocabulary). A fresh reviewer found no mathematical change:
  `research/reviews/2026-10-07-editorial-site-pass.md`,
  `research/reviews/2026-10-07-editorial-site-pass-window-occupation.md` and, after a
  `sync` audit whose corrections were applied,
  `research/reviews/2026-10-07-editorial-sync-audit.md` carry the certifications over.

## 2026-10-07: Editorial harmonization of the site

- One source per topic: the welcome page says what the site adds and defines
  *reconstructed* (every step a complete statement with a complete proof, checked by a
  separate reviewer agent, not yet reviewed by a person); each proof is summarized once
  (Chapter 0) and compared once (Chapter 12); the standing of the alternative mechanisms
  with respect to KLS is stated once (Chapter 14).
- Proof chapters titled "Authors: mechanism"; moment-map and fixed-cut titles shortened;
  internal vocabulary ("gate matrices", "covariance technology", "layer") removed from the
  prose; the localization prelude opens the fixed-eigenfunction part.
- US spelling and the `\CP` macro throughout the prose. The stale remark on the BK source
  now records its arXiv deposit.
- Statement vocabulary renamed in a second pass: `\CP`, US spelling, "Chapter" for
  references to whole chapters, and "linear test" for "gate" in three titles and five
  bodies. A fresh reviewer found no mathematical change; one grouped editorial note,
  `research/reviews/2026-10-07-editorial-statement-pass.md`, carries the 43 affected
  certifications over. The "… implies KLS" titles of the archive are kept.
- The site names its maintainer, Nicolas Brosse, and the Numina Collaboration as authors.

## 2026-10-07: BK on arXiv; the unconditional case cited

- Balasubramanian–Kasiviswanathan is now arXiv:2610.07728v1 (6 October 2026). Its text
  is identical to the GitHub PDF reconstructed here, apart from the arXiv stamp, so the
  BK certifications are unaffected; the bibliography records both versions.
- Cited Mikulincer–Zadik arXiv:2609.38295v1, a dimension-free bound for unconditional
  log-concave measures through a Dunkl–Langevin operator, in the chapter on structured
  classes. No statement changed.

## 2026-10-06: BK compatible integration certified as a third KLS proof

- Added the pinned Balasubramanian–Kasiviswanathan source and reconstructed its
  compatible-tensor Hodge estimate, uniform integration powers, covariance-normalized
  localization, reverse transfer and direct degree induction in nine dossiers.
- Twelve assertions independently reviewed, including `thm:bk-appell-bound` and
  `thm:bk-explicit-poincare` with constant $1+2\cdot10^{16}$. A separate composition
  adds a third proof record to `conj:kls`; previous proof records received an
  independent dependency-extension review without changing their actual premises.
- The BK chapter sits before the comparison; later chapters shift by one, with stable
  labels. All 178 preexisting statements are unchanged. Alternative mechanisms retain
  their objectives; no claim of priority or journal refereeing is made.
- Source and detail: `research/explorations/2026-10-06-bk-certified.md`.

## 2026-10-06: The manuscript restructured around the two proofs

- The proofs part reads Song–Zhang v1, BKL, Song–Zhang v2 (its technical estimates in a
  chapter of their own), then a new comparison of the two proofs; the overview now
  explains both ("How KLS was proved").
- New prose chapter *KLS after its proofs*: equivalent forms, consequences, the constants
  of the two proofs and the question of the best constant. No new statement.
- The synthesis is dissolved into the comparison and the map of alternative mechanisms;
  three living mechanisms (moment map, fixed eigenfunction, conditional fibers); the fixed
  cut becomes a final archive part.
- No statement changed (`check.py --statements` identical). Legacy statement titles are
  deferred to a separate pass (`TODO-EDITORIAL-POST-KLS.md` §9).
- Source: `research/explorations/2026-10-06-editorial-restructure.md`.

## 2026-10-06: The manuscript repositioned after the proof of KLS

- The site is retitled *The KLS theorem and its methods* and presents itself as a
  reader's companion to the two proofs of `conj:kls`, the methods that led to them, and
  the questions that remain open after KLS.
- The proofs are presented as Song–Zhang v1, Song–Zhang v2, then BKL, along the
  development of the polynomial method (BKL was deposited first). The verification
  caveat is stated once; the four approaches are motivated by what they would add beyond
  KLS; the entry problems open with `conj:gate-zero-sharp`.
- One novelty claim on `thm:cmh-dirichlet` is withdrawn. The AI use declared by the
  authors of both proofs is quoted on the welcome page.
- No statement changed (`check.py --statements` identical).
- Source: `research/explorations/2026-10-06-editorial-post-kls.md`.

## 2026-10-06: Song–Zhang v2 reconstructed; a second KLS proof recorded

- Twelve new proof dossiers and independent agent reviews establish the SZ v2
  chain, including the finite-block estimates, summable losses and final
  composition. `conj:kls` retains its statement and now has two proof records.
- The SZ chain uses no BKL conclusion or previously proved KLS theorem. The
  two closing mechanisms share earlier spectral foundations; their actual
  inputs are recorded separately from the combined dependency graph.
- SZ v1 and v2 have distinct bibliography entries. Earlier dossiers and reviews
  remain unchanged. The BKL composition has a new scoped review covering the
  enlarged dependency union, without changing its mathematical inputs.
- The SZ import route is accomplished. Other route states are preserved, with
  exact comparison tests for the older startup and recovery questions. The
  methodological assessment claims no priority for either proof mechanism.
- Source: `research/explorations/2026-10-06-sz-v2-certified.md`.

## 2026-10-06: BKL reconstructed and certified; KLS proved locally

- Seven proof dossiers and independent agent reviews establish the BKL chain,
  its composition into `conj:kls`, and the unconditional initialization corollary.
  This is local agent certification of BKL v1, distinct from journal refereeing.
- `cand:sz-uniform-conditional-initialization` is promoted to the stronger
  `cor:bkl-uniform-conditional-initialization`. Its research route remains active
  with an explicit independent-proof objective.
- The import route is accomplished. All ten pre-existing active routes and six
  blocked routes retain their states; no open method is closed because KLS is proved.
- Source: `research/explorations/2026-10-06-bkl-certified.md`.

## 2026-10-06: BKL reconstruction opened; alternative proofs remain research objectives

- Bizeul–Klartag–Lehec arXiv:2610.05474v1 announces a proof of KLS. Its
  sections 2–7 are being reconstructed, including the tilt criterion,
  inverse-covariance cumulant dynamics and suspension. The announcement alone
  changes no mathematical status.
- The framework now allows active alternative-proof routes after a target is
  proved. Refuted targets and resolved blockers retain their existing checks.
  All existing active and blocked routes keep their states at this import stage.
- Sources: `research/explorations/2026-10-06-bkl-integration.md` and
  `research/explorations/2026-10-06-post-proof-framework.md`.

## 2026-10-05: The manuscript reorganised by what it has established

- The survey now has six families of methods. A new chapter on the parallel coupling of
  exponential tilts, `sec:family-coupling`, joins them. The polynomial–curvature argument
  of Song and Zhang becomes a separate chapter, *The current frontier*
  (`sec:polynomial-curvature`).
- The four approaches are ordered by what each has established: moment map, fixed
  eigenfunction, conditional fibers, fixed cut. Nine technical chapters of the fixed cut
  move to an appendix.
- The overview gives equal weight to the two arguments that reach every test function,
  `thm:letwin-kls` and `thm:song-zhang-kls`.
- No statement changed. A fresh `sync` review checked the new prose against the ledger.
- The text is licensed under CC BY 4.0 and the code under MIT. The authors are named as
  Collaboration Numina. The harness follows conjecture-search-template v0.5.0.
- Source: `research/explorations/2026-10-05-editorial-restructure.md`.

## 2026-10-04: The August certifications re-reviewed, and Wave A

- **The August-25 certifications were checked again.** On 2026-08-25 the fixed-cut core
  and bootstrap dossiers had been certified by two agents reviewing each other's work,
  which was not an independent check. Fresh grouped reviews were run:
  - The QCTS/Stein core passed.
  - The Riccati and bootstrap dossiers were sent back for revision and passed after repair:
    - a false endpoint claim in the proof of `lem:half` was fixed;
    - `prop:ceiling` was narrowed to a one-way sufficient implication;
    - `thm:bootstrap` was recertified.
  - The survival bridge `lem:survival-implies-kls` was repaired and passed.
  - In the moment-map layer, a proof step of `thm:cmh-1d` failed on the density
    $c(1+x^2)^{-3}$. The step was at fault, not the theorem. The proof was repaired, and
    `thm:cmh-1d`, `thm:cmh-product` and `thm:cmh-dirichlet` were recertified.
  - No statement changed.
- **Wave A certified two results:**
  - `prop:product-simplex-cone-gate`, the sharp linear gate on product-simplex cones;
  - `lem:fiber-polynomial-floor`, a uniform lower bound $1/80$ for fixed-degree simplex
    fiber duals. So no fixed-degree all-frame refuter exists.
- **Priorities after Song–Zhang.** Three approaches were closed as subsumed. The main line
  is now the Song–Zhang loss, through a conditional initialization of their iteration;
  the first attempt at a full induction contract was closed. The decisive tests are
  `conj:gate-zero-sharp` and the all-frame simplex question.
- Sources:
  - `research/explorations/2026-10-04-aug25-grouped-review-synthesis.md`
  - `research/explorations/2026-10-04-cmh-1d-domain-repair.md`
  - `research/explorations/2026-10-04-wave-a-synthesis.md`
  - `research/explorations/2026-10-04-strategy-after-song-zhang.md`

## 2026-10-01 to 2026-10-03: Song–Zhang reconstructed and certified

- Song and Zhang's preprint (arXiv:2610.01447v1, 1 October 2026) bounds the inverse Cheeger
  constant by $O(4^{\log^* n})$, that is $C_P \lesssim 16^{\log^*(n+2)}$.
- It was treated as an import to audit, not as a fifth approach. Its proof was rebuilt here
  in five dossiers, and all eight resulting statements were certified on 2026-10-03:
  - `thm:song-zhang-kls`
  - `thm:sz-curvature-comparison`
  - `thm:sz-curvature-transfer`
  - `cor:sz-affine-poincare`
  - `prop:sz-exponential-coefficients-equivalence`, which is equivalent to KLS and not
    easier
  - and three supporting statements.
- Sources: `research/explorations/2026-10-03-song-zhang-integration.md`,
  `research/explorations/2026-10-03-sz-wrap-up.md`.

## 2026-10-01: The preprint imports certified

- The results imported from recent preprints were proved here and certified. They come
  from:
  - Letwin (arXiv:2607.24164v1), including `thm:letwin-qcts` and the bridge `thm:letwin-kls`;
  - Chen–Klartag (arXiv:2607.23307v1);
  - Klartag–Lehec (arXiv:2507.15495v2).
- Four conditional implications of the fixed cut and `cor:dichotomy` were also certified.
- `prop:mm-window-occupation` no longer depends on an uncertified premise. Its small-gap
  branch turned out to be empty.
- Proved statements went from 86 to 106.
- Sources: `research/explorations/2026-10-01-wrap-up-open-results-certification.md`,
  `research/explorations/2026-10-01-wrap-up-letwin-follow-up.md`.

## 2026-09-29 and 2026-09-30: The manuscript moves to MyST

- The harness migrated to conjecture-search-template v0.2.0, then v0.3.0 and v0.4.0. The
  LaTeX manuscript became a MyST site in which each statement shows its status.
- The weighted-excess approach was formally closed.
- Sources: `research/explorations/2026-09-29-migration-v0.2.0.md`,
  `research/explorations/2026-09-30-migration-v0.3.0.md`,
  `research/explorations/2026-09-30-sync-after-migration.md`.

## 2026-09-06: The linear sector of the moment-map inequality

- `lem:linear-sector-third-moment` was certified. It reduces the linear test of the
  moment-map inequality to a third-moment tensor.
- The exponential-cone statements were also certified, including `prop:cone-moment-map`
  and `prop:cone-linear-sector`, as well as `cor:gate-zero-third-moment`.
- `conj:gate-zero-sharp` was opened.
- Source: `research/explorations/2026-09-06-synthesizer-kls-wave-five-w5y01.md`.

## 2026-09-01 to 2026-09-04: One program per repository

- A second research program was split out of this repository.
- KLS moved to conjecture-search-template v0.1.0. The registry of reusable facts was
  preserved in `research/explorations/2026-09-04-synthesizer-knowledge-registry-preserved.md`.

## 2026-08-30: Window occupation

- `prop:mm-window-occupation` was certified: $C_P \le C\log^2 n$ through the
  fixed-eigenfunction window. At the time it was conditional on Letwin's preprint.
- `prop:split-screened-supply` was also certified.
- Source: `research/explorations/2026-08-31-orchestrator-kls-angles-wave-w4.md`.

## 2026-08-27: The first refutations, and the conditional fibers

- `prop:weighted-spectator-obstruction` was certified. It refutes `conj:weighted-excess-rate`
  and `ass:weighted-package` on product measures, which satisfy KLS. These are still the
  only refuted statements. A fresh review confirmed them on 2026-10-01.
- `prop:spectral-sufficiency` was certified. It reduces KLS to an occupation estimate for
  one eigenfunction followed through stochastic localization.
- The conditional-fiber approach was admitted. `prop:conditional-fiber-root-obstruction`
  was certified: the root frame on the simplex fails. This rules out only that frame,
  not the all-frame question.
- Sources: `research/explorations/2026-08-27-orchestrator-kls-weighted-refutation-sync.md`,
  `research/explorations/2026-08-27-orchestrator-kls-conditional-fiber-route-admission.md`,
  `research/explorations/2026-08-27-orchestrator-kls-wave-three-synthesis-and-stop.md`.

## 2026-08-25: The moment-map inequality and its exact cases

- The canonical moment-Hessian constant `def:cmh` was fixed. It bounds the affine Poincaré
  constant with no loss: `thm:cmh-implies-affine-poincare`.
- Its exact values were certified on the line (`thm:cmh-1d`), on products
  (`thm:cmh-product`) and on every log-concave Dirichlet law (`thm:cmh-dirichlet`), the
  first non-product family.
- `prop:letwin-not-gate-zero` was also certified: matrix inequalities over fixed matrices
  cannot supply the linear stage.
- The same day, 34 fixed-cut statements that had been marked proved without a written proof
  received grouped proofs and reviews, including `thm:bootstrap` and `prop:ceiling`. The
  others were reclassified. These reviews were the cross-reviews re-done on 2026-10-04.
- Sources: `research/explorations/2026-08-25-kls-cmh-normalization-layer.md`,
  `research/explorations/2026-08-25-r2-backbone-certification.md`.

## 2026-08-20 to 2026-08-24: First synthesis and triage

- The first synthesis was written. Letwin's and Chen–Klartag's July preprints were brought
  in as unchecked inputs. The first numerical reading, from June, in favour of
  `conj:taming` was withdrawn: the runs computed a different quantity.
- The approaches were regrouped into the fixed cut, the fixed eigenfunction and the moment
  map.
- Sources: `research/explorations/2026-08-20-kls-program-cycle-1.md`,
  `research/explorations/2026-08-20-kls-frontier-audit.md`,
  `research/explorations/2026-08-24-kls-part3-restructure.md`.

## 2026-06: Start

- The repository was created, with a LaTeX manuscript and a first numerical channel.
