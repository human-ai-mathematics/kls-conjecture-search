---
---

# Migration to conjecture-search-template v0.3.0

This checkpoint records a harness change. It changes no mathematical status: the ledger
holds the same 138 nodes with the same statuses (86 proved, 46 open, 4 defined,
2 refuted), and no statement of the manuscript changed. It follows
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

**Prose.** Four `writer` passes, on disjoint modules. `modules/00-overview.md` now carries
what the site said: the question, examples by hand, the literature, the obstacle every
method meets, the main results with the idea of each proof, three problems for a newcomer
(`q:mm-spectral-occupation`, `conj:gate-zero-sharp`, `q:conditional-fiber-frame`), how the
manuscript is organised, how results are checked and how to contribute. The site's lettered
theorems became prose pointing at the manuscript's statements, not new directives. Every
other module lost its hand-written statuses and its harness vocabulary; the eight-field
route summaries read as prose; the lettered routes are "Approach E/S/C/F". The order of
the modules did not change. `check.py --statements` is identical before and after.

## What resists

- *observed* **A linked heading enters the fingerprint.** When a statement links to a
  section on another page, MyST resolves `[](#sec:…)` to a `link` node carrying the
  heading's text, and `_statement()` in `scripts/checks/manuscript.py` keeps it
  (`POINTERS` lists `crossReference`, `cite` and `footnoteReference`, not `link`).
  Renaming such a heading changes the fingerprint and lifts certifications: it happened to
  `ass:weighted-package` (through `sec:stein`) and `def:cmh` (through
  `sec:cmh-exact-cases`), and both headings were restored with "Route". A template fix is
  to treat a `link` with an `identifier` as a pointer.
- **Statements that still write a status or harness words.** A writer does not change a
  statement, so these are deltas for the orchestrator, to apply with a `sync` review, since
  each edit lifts the certifications that checked the statement:
  - titles: `ass:weighted-package` ("Refuted literal weighted near-Cheeger package"),
    `q:weighted` ("Refuted global-operator-norm weighted excess rate"; its body also says
    "The answer is negative"), `q:stein-weighted` ("…from the refuted package"),
    `thm:cmh-implies-affine-poincare` ("…; answers [](#q:cmh-normalization)"),
    `cor:dichotomy` ("…of the bootstrap route"), `cor:refutation`, `rem:needle-requirement`,
    `prog:cmh-route`, `rem:spectral-vs-cmh` ("Relation to Route C");
  - bodies saying "certified", "refuted", "route", "fence", "repository" or "ledger node":
    `obs:rank-one-refuted`, `obs:circularity`, `obs:relative-ceiling`, `q:alignment`,
    `hyp:absolute-geometric-completion`, `thm:bootstrap-stopped-interface`,
    `prop:split-screened-supply`, `prop:mm-window-occupation`, `lem:fiber-root-degree-two`,
    `q:literature-PsQs`, `rem:mm-two-preprints`, `rem:weight-explains-rate`,
    `rem:almost-stability-gap`, `rem:obata`, `prop:stein-rep`, `prog:product-test`,
    `q:cmh-solenoidal-perturbation`, `rem:history-table-caveats`;
  - `q:cmh-normalization` is a labelled remark written as a task.
- **Kinds and prefixes.** `obs:two-tail` and `obs:proj-ceiling` are conjectures stated as
  heuristic barriers; `rem:cmh-saturation-risk` and `rem:cmh-stronger-than-kls` label
  corollaries.
- **Ledger against prose.** `thm:intro-all-cut`, `thm:intro-weighted`,
  `thm:centroid-implies-kls` and `thm:carleson-implies-centroid` are `open` although the
  manuscript gives arguments for them; they display *Not settled here*, and the prose no
  longer calls them proved.
- Carried from v0.2.0: the fingerprints of the v0.2.0 migration were recorded without a
  reading; the nineteen converted statements await a `sync` review; the sign in the
  falsification clause of `q:cmh-solenoidal-perturbation` still disagrees with the
  gateway of `modules/40-moment-map-cmh.md` (a *positive* second variation refutes
  $\mathrm{CMH}(4)$ in the statement, a *negative* one in the gateway), now flagged by a
  `%` comment there. Before the `pages` workflow is dispatched, a person reads the
  manuscript, above all the rewritten overview.

## Proposed next step

A `reviewer` with the `sync` lens on the statement deltas above, the nineteen converted
statements and the sign of `q:cmh-solenoidal-perturbation`; the orchestrator applies the
agreed statement edits and the certifications they lift go back through review. Upstream,
the `link` fix in the template's fingerprint.
