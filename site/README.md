# site/ — the human-facing half

The frontend of the published website. Four files, and a rule that explains all of them:

> The site is a derived view of the repository, never another source of mathematical or
> search state.

| file | what it is |
|---|---|
| [`index.html`](index.html) | the shell: masthead, nav, colophon. No mathematics. |
| [`site.css`](site.css) | presentation. Colour never carries meaning alone. |
| [`site.js`](site.js) | the router, the two maps, and every view. Knows no mathematics. |
| [`tex4ht.cfg`](tex4ht.cfg) | what preserves the anchor invariant, and the manuscript's macros, through LaTeX → HTML. |

Nothing substantive is written here. Everything a reader sees — statements, standings,
titles, approaches, blockers, checkpoints, certifications, and which four routes the
front page leads with — arrives at load time in `data.json`, which
[`../scripts/site.py`](../scripts/site.py) derives from the same validated report
[`../scripts/check.py`](../scripts/check.py) prints from. A gloss or an approach objective
typed into these files would drift from the ledger and the portfolio the first time
either changed, and the prettier copy would win the argument.
[`../scripts/tests/test_site.py`](../scripts/tests/test_site.py) asserts that no claim
gloss, candidate statement, approach objective or node id appears in this directory.

The one block of generated text that does live here follows the same rule for the same
reason. `tex4ht.cfg` carries [`../preamble.tex`](../preamble.tex)'s macros into MathJax,
because `make4ht` does not and the manuscript's own notation reached the reader as red
source without it — but the macro list is *derived* by
[`../scripts/checks/mathjax.py`](../scripts/checks/mathjax.py) and rewritten by
`python3 scripts/new.py mathjax`, and `check.py --lane editorial` fails the tree when it
and the preamble disagree. A macro list typed here by hand would drift exactly the way a
gloss typed here would.

The status badge is the derived **standing**, not the schema status: eight tones from
[`../scripts/checks/editorial.py`](../scripts/checks/editorial.py), the same projection
that prints the badge beside every statement in the PDF. `proved` is 86 nodes here and
means four different things, and a published theorem, an unreviewed preprint, a result
certified against a dossier and an implication with an open antecedent are not one green
badge. Headings are the manuscript's own theorem titles; the stable id stays visible
beside them, because that is what cross-references are quoted by.

## Explore and Audit

The nav is a split, and the split is the design:

| section | what it is for |
|---|---|
| Overview, Routes, Key results, Manuscript | orient a reader in one screen, then send them into the manuscript at an anchor |
| Audit | the complete research state, unreduced — claims, portfolio, evidence |

"In one screen" is what decides how much the Overview draws. It lists the four routes as
a row apiece — name, composition, the exact bottleneck — and the full cards, with the
bridge and the way into the manuscript gateway, are what Routes is for. Drawing the same
card in both made Routes a copy of a section the reader had already scrolled past. For
the same reason the recent records on the front page carry their dates, outcomes and
engaged claims but not their excerpts: a checkpoint's opening paragraph is written by
the roles running the search, and its proper home is Evidence.

Audit's three views link to each other directly. The index page stays, because what it
explains — claims, portfolio and evidence are three domains and are never merged — is
worth a page; it is just no longer the only road between them.

The **Explore** half is a selection, and a selection needs a selector: it is driven by
[`../research/program/editorial.yaml`](../research/program/editorial.yaml), which holds
identifiers, display names and manuscript anchors and no mathematics at all. A repository
that publishes none still builds; every Explore view degrades to the Audit views it
indexes, which is what a template does and is not a defect.

One word carries a load here. On this site a **route** is one of the four the manuscript
is organized into — E, S, C, F — and the nineteen objects in the portfolio are
**approaches**. The portfolio schema calls those `routes:` internally and keeps doing so;
renaming a validated schema to fix a caption would be the tail wagging the dog. What is
not allowed is a reader meeting nineteen things under a name the manuscript gives to
four.

## Build it

```bash
python3 scripts/site.py                        # -> build/site/
python3 scripts/site.py --root example         # the worked example, fully populated
python3 scripts/site.py --serve                # build, then serve it at :8000
```

Output goes under `build/`, which is gitignored: a built site is a build artifact, never
committed state. The full pipeline — PDFs, HTML conversion, deployment — is
[`../docs/PUBLISHING-THE-SITE.md`](../docs/PUBLISHING-THE-SITE.md).

## What it will not do

- **Publish a repository that does not validate.** `site.py` runs every lane of the
  checker first and refuses on any error, writing nothing at all. An invalid revision is
  not this repository's research state.
- **Merge the two maps.** The claim graph and the search portfolio are drawn on separate
  canvases with separate vocabularies. A route is not a theorem, `completed` means a
  route's objective ended rather than that anything was settled, and `saturated` is a
  judgment about effort.
- **Flatten certification.** `mode: agent` shows the persisted review, its reviewer and
  its distinct authors; `mode: human` shows a name and says plainly that it carries no
  report on disk. They are not drawn as equal evidence.
- **Dress a candidate as a claim.** A candidate is labelled as one, has no status, and
  carries the note that unlike a node's gloss its text is canonical.
- **Let a contribution change anything by itself.** Every action link opens a public
  inbox. Triage is [`../docs/PUBLISHING-THE-SITE.md`](../docs/PUBLISHING-THE-SITE.md),
  and the boundary is [`../CLAUDE.md`](../CLAUDE.md) constraint 12.

## Dependencies

None at build time beyond the checker's own PyYAML. The graph layouts are computed in
Python and drawn as plain SVG — a research program's claim graph has tens of nodes, not
thousands, and a deterministic layout is diffable, works offline, and cannot silently
fail to load.

Both maps open on a neighbourhood chosen to show something. Centring on the declared
target is right only when the target has neighbours: a conjecture nothing has yet been
proved *from* has one edge, and a map that opens there draws two boxes in a wide empty
stage and tells the reader the program has no structure. `openingView` keeps the
preferred centre when it reaches a few nodes and otherwise takes the best-connected one,
growing the depth until the view is not degenerate; the stage then takes the shape of
what was drawn rather than letterboxing it into a fixed height. Nothing is hidden by
either: the centre, the depth and the scope are controls, and the whole list is below.

The one thing loaded from a network is MathJax, and only to typeset the LaTeX `$...$` in
glosses and candidate statements. It is deliberately optional: the raw source is placed
in the DOM first and typeset afterwards, so a blocked or missing CDN leaves the
mathematics visible and readable rather than blank.

It only has something to do because the glosses are written in `$...$`. They were not
always: 103 of 138 spelled their mathematics in ASCII, MathJax typeset two elements on
the whole site, and a reader met `E[H Sigma^{-1} H] <= 4 Sigma` where the claim says
something legible. That is a ledger property, not a frontend one, so the fix was in the
ledger and the guard is in the editorial lane —
[`../scripts/checks/editorial.py`](../scripts/checks/editorial.py) fails on a bare ASCII
spelling, and `check.py glosses` still prints the length budget, which stays advisory.

## Editing it

Change presentation freely. Before adding a *field* to a view, check that
`scripts/site.py` already exports it — if it does not, the addition belongs there, in
the derivation, not here in a hand-written string.
