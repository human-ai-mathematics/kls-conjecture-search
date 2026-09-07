# site/ — the human-facing half

The frontend of the published website. Four files, and a rule that explains all of them:

> The site is a derived view of the repository, never another source of mathematical or
> search state.

| file | what it is |
|---|---|
| [`index.html`](index.html) | the shell: masthead, nav, colophon. No mathematics. |
| [`site.css`](site.css) | presentation. Colour never carries meaning alone. |
| [`site.js`](site.js) | the router, the two maps, and every view. Knows no mathematics. |
| [`tex4ht.cfg`](tex4ht.cfg) | what preserves the anchor invariant through LaTeX → HTML. |

Nothing substantive is written here. Everything a reader sees — statements, standings,
titles, approaches, blockers, checkpoints, certifications, and which four routes the
front page leads with — arrives at load time in `data.json` (and, for one record at a
time, `records/<slug>.json`), which
[`../scripts/site.py`](../scripts/site.py) derives from the same validated report
[`../scripts/check.py`](../scripts/check.py) prints from. A gloss or an approach objective
typed into these files would drift from the ledger and the portfolio the first time
either changed, and the prettier copy would win the argument.
[`../scripts/tests/test_site.py`](../scripts/tests/test_site.py) asserts that no claim
gloss, candidate statement, approach objective or node id appears in this directory.

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

## Long-form text: the statement, and the record

Two things a reader actually came for used to be reachable only by leaving. A claim page
showed a one-line gloss stamped *not the statement* and a `file:line`, so knowing what
any of 138 claims says meant 138 trips into a LaTeX module; and each of the 92 durable
records was a link to a code host's blob view, where the front matter is a bare table,
the `$...$` is untypeset, and every id in the prose is inert text.

Both are now derived at build time by [`../scripts/site.py`](../scripts/site.py) into one
small block model — `paragraph`, `heading`, `math`, `list`, `quote`, `code`, `table`,
`rule`, and spans — which `site.js` draws and understands nothing else about. One model,
two producers (a LaTeX claim environment, a Markdown record), one renderer.

**The statement** is sliced verbatim out of the `\label` in `modules/` and printed above
the gloss, labelled as the copy it is. This is the projection [`../CLAUDE.md`](../CLAUDE.md)
constraint 7 permits and the gloss already is — the same permission the problem brief
uses to quote its target — and not a second home: nothing is authored, the copy is taken
fresh on every build, and `statement_failures` re-reads `modules/` afterwards and
compares digests. A statement that no longer matches its source, or a claim whose anchor
yields none, fails the build and nothing is written. The gloss stays exactly where it
was, with its own tag: it is a different thing and is still not the statement.

**A record** gets a page at `#/record/<slug>`: the front matter as a header — date,
outcome, approach, engaged claims, artifacts, what it proposed, retired, promoted and
supersedes — and the body rendered beneath it. Ids written in the prose become links to
the node, approach or candidate they name; a link to a sibling record becomes navigation
between two pages; supersession is drawn as the relation it is rather than a filename;
and the GitHub blob view stays as a secondary *Source* affordance, the way node pages
keep theirs. Rendering is derivation and rewrites nothing, so `research/explorations/`
stays append-only (constraint 6).

Record bodies are **fetched, not carried**: rendered, the 92 records are several times
the size of everything else the site knows, and a reader opening the front page should
not pay for all of them to read one. `data.json` holds each record's envelope and the
path of its document; `records/<slug>.json` holds the prose and is loaded when that page
is opened, then typeset in its own scope.

Once records are pages, a route can have a **timeline** — and that is most of what
"focus on one route" means. A route page ends with the records that touched it, newest
first, on either of two declared grounds, named on each row: the record names one of the
route's portfolio approaches, or it engaged a claim the route is built on (one the
editorial guide features under it, or one an approach of the route is blocked on). Both
are joins over data already published; neither is a judgment `site.js` makes.

The Markdown subset is the one the records actually use, counted rather than guessed, and
the LaTeX subset likewise. Anything outside either is passed through as text, which is
the failure that loses the least. There is no Markdown library and no LaTeX-to-HTML
library; see **Dependencies**.

One dependency is external and deliberate. Statements are written against the ~60 macros
in `preamble.tex`, which MathJax does not know, and generating that table from the
preamble belongs to the HTML manuscript conversion — a second extractor here would be
the duplicate parser the whole design avoids. So it arrives from outside:
`python3 scripts/site.py --macros <file.json>` (an object mapping a macro name, without
its backslash, to what `MathJax.tex.macros` accepts) puts it in `data.json`, `site.js`
installs it before MathJax starts, and until a build is given one every claim page says
plainly that an unexpanded command is a missing build input rather than a defect in the
statement.

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
python3 scripts/site.py --macros macros.json   # attach a generated MathJax macro table
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

None at build time beyond the checker's own PyYAML — including for the two long-form
renderers above. The Markdown and LaTeX subsets are read in `scripts/site.py` in about
three hundred lines of Python, scoped to what the records and the statements actually
contain. A Markdown library or a LaTeX-to-HTML converter would be a build dependency, a
larger surface than the input, and a second opinion about the repository's own prose.

The graph layouts are computed in
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
glosses, candidate statements, copied manuscript statements and rendered records. It is
deliberately optional: the raw source is placed in the DOM first and typeset afterwards,
so a blocked or missing CDN leaves the mathematics visible and readable rather than
blank. Its startup and the site's data load shake hands — `index.html` holds MathJax
until `data.json` is read, because a build may carry the macro table and the TeX input
reads its macro list once; `site.js` typesets each view when MathJax says it is ready
rather than when a view happens to be drawn. When the CDN never answers, neither
promise settles, nothing is typeset, and the source stays on screen, which is the
intended degradation.

`index.html` puts `pre` and `code` in MathJax's `skipHtmlTags`, so a `$` inside a YAML
snippet in a record is never mistaken for a formula. Rendered code blocks and inline code
use exactly those elements for that reason.

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
