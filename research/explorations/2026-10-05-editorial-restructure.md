---
---

# Editorial restructuring: six families, a frontier chapter, approaches ordered by results

<!-- Orchestrator checkpoint. Editorial decisions on the manuscript only; no node, statement,
     status or route changes. Statements were moved, never edited (check.py --statements
     identical before and after). -->

## Question examined

Does the manuscript's organisation say what the search has established, and in which order?
An editorial reading of the welcome page, `sec:overview`, the family chapters,
`sec:frontier-atlas` and `sec:kls-synthesis` found four defects: the survey's sixth family was one
recent argument (`thm:song-zhang-kls`) while the parallel coupling behind the thin-shell theorem
had no chapter; three orders of the approaches disagreed (the table of contents, the `myst.yml`
comment and `subsec:atlas-assessment`, besides the portfolio); the fixed cut filled eleven
chapters for mostly conditional or negative content; and the narrative ran two threads
(reduce the loss of the frontier argument, or make a restricted estimate adaptive) without
saying which the manuscript's own work served.

## What we learned

*Judgment (orchestrator), on the manuscript as it stood; no new mathematics.*

1. **The survey is now six families plus a frontier.** A new prose chapter `sec:family-coupling`
   (no labelled statement) presents the parallel coupling of exponential tilts
   [@KlartagLehec2025ThinShell], checked against the arXiv abstract of 2507.15495v2: it sees a
   test function only through its correlation with linear functions, which is enough for
   $|x|^2$ and is the fixed-family instance of `subsec:kls-adaptive-residue`. Target 4 of
   `sec:kls-synthesis` now points to it. `sec:polynomial-curvature` is retitled *The current
   frontier* and placed in its own part.
2. **The approaches are ordered by what each has established**: the moment map, the fixed
   eigenfunction, conditional fibers, the fixed cut. The criterion is stated once, in
   `subsec:atlas-approaches`. `subsec:atlas-assessment` is now *Research priorities*, in the
   order of the 2026-10-04 strategy checkpoint: the Song–Zhang loss; the decisive tests
   (`conj:gate-zero-sharp`, the all-frame simplex question); `conj:mm-spectral-occupation`;
   the fixed cut. The duplicated "motivation, not difficulty" caveats were reduced to one.
3. **The fixed cut keeps two chapters in the main text** (`sec:introduction`, rewritten as a
   self-contained summary of the bootstrap, its interface, the ceiling and the obstructions;
   `sec:open`) and moves nine to a final part, *Appendix: the fixed cut in detail*
   (`sec:carleson` … `sec:appendix-fixed-cut`).
4. **The overview's backbone is the two ways forward** of `subsec:kls-adaptive-residue`, with
   the remark that `prop:sz-exponential-coefficients-equivalence` is equivalent to KLS and not
   easier. `prop:mm-window-occupation` is presented as a limitation of the fixed eigenfunction,
   not as one of its results. Dated phrases ("July 2026 inputs", "the October preprint") are
   replaced by authors' names outside the history table and the source-version paragraphs.
5. **The overview presents two conversions of equal weight** (`sec:kls-conversions`): the
   localization–Lichnerowicz argument of `thm:letwin-kls` (`subsec:kls-architecture`, figure
   `fig:kls-architecture` kept) and the polynomial–curvature argument of `thm:song-zhang-kls`
   (`subsec:song-zhang-mechanism`, promoted from a paragraph under the history table). Both
   localize to curvature of order $1/\log n$ and use `thm:letwin-qcts`; they differ in the
   curvature-to-gap step, and each loss is located. The log-trace-exp computation is left to
   `subsec:sl-where-the-log-lives`.

## What resists

- The moment-map results (`thm:cmh-dirichlet`, `lem:linear-sector-third-moment`,
  `prop:letwin-not-gate-zero`, the cone statements) are the manuscript's main publishable
  content; a separate article on them was considered and deferred by the user.
- The frontier and two of the approaches lean on version-1 preprints (`thm:letwin-qcts`,
  `thm:song-zhang-kls`); the text already says so where they are used.

## Proposed next step

A fresh `reviewer` with the `sync` lens on the modules touched by this restructuring, to
check that the new prose agrees with the ledger and the brief.
