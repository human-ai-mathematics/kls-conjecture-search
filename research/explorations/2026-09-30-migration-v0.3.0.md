---
---

# Migration to conjecture-search-template v0.3.0

This checkpoint records a harness change. It changes no mathematical status: the ledger
holds the same 138 nodes with the same statuses (86 proved, 46 open, 4 defined,
2 refuted). It follows
`2026-09-29-migration-v0.2.0.md`, whose open items it carries forward.

## Question examined

How to move from v0.2.0 to v0.3.0 — the reader's site removed, the manuscript the one text
a reader reads, each statement's status displayed from the ledger — without losing what
the site told a reader and without lifting a certification.

## What we learned

**Harness.** `scripts/`, `SPECIFICATION.md`, the `reviewer` and `writer` roles,
`templates/module.md`, `package.json`, the `pages` workflow, the issue forms and `example/`
are those of the template at v0.3.0. `site/`, `templates/site/` and the site checker are
gone; `scripts/status.mjs` displays the status next to each statement, `proofs.md`
introduces the full proofs, and `myst.yml` lists the manuscript, then the full proofs. In
the build, 86 statements show *Proved* (with a link to the full proof when a proof record
names one), 46 *Not settled here* and 2 *Refuted by*, matching the ledger.

**Fingerprints** (*established*, checked mechanically). The v0.3.0 fingerprint ignores the
page a cross-reference's target lives on. With `modules/` unchanged, 39 statements that
cite another module got a new fingerprint, and 35 certifications lapsed. Under the
decision of the v0.2.0 migration (item 2 of its *Records*), the 48 affected entries in 25
reviews were updated to the v0.3.0 values; each value replaced was the v0.2.0 fingerprint
of the same, unchanged statement. No reviewer read anything anew. The reviews are those
changed by commit `9b7502d` (`git show --stat 9b7502d -- research/reviews`).

A second fix, taken from the template before its release (under `Unreleased` there): a
statement that links to a section on another page no longer fingerprints the heading's
text, so renaming a heading lifts nothing. Seven statements holding such a link got a new
fingerprint with no change to their text; 15 entries in 15 reviews were updated the same
way (commit `0bc5d06`).

**Statements.** Statements that wrote their own status or harness words were reworded,
after a `sync` review checked that each rewording keeps the mathematics: titles such as
"Refuted literal weighted near-Cheeger package" lose "Refuted", sentences narrating a
status ("The answer is negative", "is not itself certified", "no such implication is
proved in this report") go, and "route", "fence", "certified", "repository" become
mathematical words. In `prop:split-screened-supply`, "the split class of the certified
dossier" pointed at convention (M2) of its dossier, which the statement did not state: it
now writes the class out (compactly supported factors with smooth density, a cut
$E_J\times\R^{J^c}$ with $C^2$ relative boundary and a tubular neighbourhood), so it says
exactly what the dossier proves. 22 statements changed; exceptionally, as part of this
migration, the 24 entries of their fingerprints in 20 reviews were updated without a new
review.

**Prose.** Four `writer` passes, on disjoint modules. `modules/00-overview.md` now carries
what the site said: the question, examples by hand, the literature, the obstacle every
method meets, the main results with the idea of each proof, three problems for a newcomer
(`conj:mm-spectral-occupation`, `conj:gate-zero-sharp`, `conj:conditional-fiber-frame`), how the
manuscript is organised, how results are checked and how to contribute. The site's lettered
theorems became prose pointing at the manuscript's statements, not new directives. Every
other module lost its hand-written statuses and its harness vocabulary; the eight-field
route summaries read as prose; the lettered routes are "Approach E/S/C/F". The order of
the modules did not change. `check.py --statements` is identical before and after the
prose pass.

## What resists

- **A conclusion that may be out of date.** `rem:product-stress-test` says that if the all-cut
  estimate fails on products, the weighted near-Cheeger approach is "forced"; the prose of
  `modules/22-product-stress.md` says the same ("a failure would force the geometric
  variant", "leaving Eldan–B as the surviving variant"). The literal form of that approach,
  `ass:weighted-package`, is refuted, so only a repaired form such as `conj:stein-weighted`
  would remain. Saying so changes what the text claims, not its wording.
- **Kinds and labels.** The `obs:` nodes are conjectures stated as methodological
  warnings; `rem:cmh-normalization`, `rem:literature-psqs` and `rem:gate-zero-dichotomy` are remarks and
  `prop:cmh-approximation-closure` a proposition under a `q:` prefix; `rem:gate-zero-trace-upgrade`,
  `cor:cmh-product-saturation` and `cor:cmh-hodge-comparison` label corollaries; some labels
  carry a harness word (`rem:single-coordinate-cuts`, `rem:cmh-program`,
  `rem:covariance-only-saturates`, `cor:single-coordinate-cuts`).
- **Ledger against prose.** `thm:intro-all-cut`, `thm:intro-weighted`,
  `thm:centroid-implies-kls` and `thm:carleson-implies-centroid` are `open` although the
  manuscript gives arguments for them; they display *Not settled here*, and the prose no
  longer calls them proved.
- Carried from v0.2.0: the fingerprints of the v0.2.0 migration were recorded without a
  reading; the nineteen converted statements await a `sync` review; the sign in the
  falsification clause of `conj:cmh-second-variation` still disagrees with the
  gateway of `modules/40-moment-map-cmh.md` (a *positive* second variation refutes
  $\mathrm{CMH}(4)$ in the statement, a *negative* one in the gateway), now flagged by a
  `%` comment there. Before the `pages` workflow is dispatched, a person reads the
  manuscript, above all the rewritten overview.

## Proposed next step

A `reviewer` with the `sync` lens on the nineteen statements converted in v0.2.0 and on the
sign of `conj:cmh-second-variation`, and on the conclusion of `rem:product-stress-test`. Fresh `certify` reviews would replace the fingerprints the
two migrations recorded without a reading.
