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
