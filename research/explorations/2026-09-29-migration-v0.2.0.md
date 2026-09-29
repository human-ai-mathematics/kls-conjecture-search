---
---

# Migration to conjecture-search-template v0.2.0

This checkpoint records a harness change. It changes no mathematical status: the ledger
holds the same 138 nodes with the same statuses (86 proved, 46 open, 4 defined,
2 refuted). It is the first record to read on anything that looks different since
`2026-09-06-synthesizer-kls-wave-five-w5y01.md`.

## Question examined

How to move the KLS search from the v0.1 LaTeX harness to the v0.2.0 template (MyST
manuscript, three roles, a ledger of statuses and edges only) without losing a statement,
a label, a cross-reference, a citation or a certification.

The old harness was replaced by the template tree, and the kls content was converted into
it. Anything not converted left with the old harness: `CLAUDE.md` and `AGENTS.md` (the
contract is now `SPECIFICATION.md`), `.codex/`, `docs/`, `packs/`, the lenses, the roles
other than `researcher`, `reviewer` and `writer`, the ledger and portfolio schemas,
`editorial.yaml`, the glosses, `status.tex`, the tex4ht site and `research/legacy-runs/`.
All of it stays readable in git history at `34b5fcd`.

## What we learned

**Manuscript** (*established*, checked mechanically). The 33 LaTeX modules are
`modules/*.md`, listed in `myst.yml` in the reading order of the former `main.tex`;
`reading-paths` and the orientation form `modules/00-overview.md`, whose abstract is the
former one. The 59 math macros of `preamble.tex` are in `myst.yml`. A conversion oracle
compared the LaTeX inventory (1064 labels, 2193 references, 194 citations) with the AST of
`myst build`: nothing is lost, in the modules or in the dossiers. The converter, the oracle
and the hand edits applied after conversion lived outside the repository; they are harness
tooling for this one move, not part of the harness.

**Claim kinds.** The environments without a `prf:` equivalent were converted as follows:

| LaTeX | MyST | nodes |
|---|---|---|
| `question`, open or refuted | `prf:conjecture`, stated in the direction the search tries to establish | `q:alignment`, `q:cmh-solenoidal-perturbation`, `q:conditional-fiber-frame`, `q:mm-invariant-lift`, `q:mm-spectral-occupation`, `q:mm-square-root-commutator`, `q:splitting`, `q:stein-weighted`, `q:taming`, `q:upgrade`, `q:weighted` (refuted), `rem:almost-stability-gap` |
| `question`, proved | `prf:proposition` | `q:cmh-approximation` |
| `obstruction` (all open) | `prf:conjecture` | `obs:circularity`, `obs:crude-insufficient`, `obs:proj-ceiling`, `obs:rank-one-refuted`, `obs:relative-ceiling`, `obs:two-tail` |
| `hypothesis` (dossiers only) | `prf:assumption`, not a node | — |
| `program`, `heuristic` | `prf:remark` titled "Program — …", "Heuristic — …" | — |
| `warning` | `{warning}` admonition, same label | — |

Ids did not change, so `q:`, `obs:`, `rem:` and `hyp:` prefixes remain on claims of other
kinds. Rewording a question as an assertion changed its text only as far as the
orientation required; the statements concerned are the eighteen open or refuted ones
above plus `q:cmh-approximation`.

**Ledger.** `kind`, `file`, `summary`, `provenance`, `import_class`, `meta` and the
`mode`/`id` of proof records are gone. The old `summary` glosses remain readable with
`git show 34b5fcd:research/program/ledger.yaml`; a `writer` looking for a one-line gloss of
a node starts there. `heuristic_barriers` became `bounded_by` edges to open nodes. Two
edges have no v0.2 field and now live in the text: `prop:spectral-sufficiency` implies
`conj:kls` (its antecedent `q:mm-spectral-occupation` stays in `assumes`, and the brief's
neighbourhood says it), and `conj:gate-zero-sharp` refines `conj:gate-zero` (said at the
statement in `modules/41-cmh-normalization.md`, in the glossary and in the brief).

**Portfolio.** The five families and nineteen routes are flat approaches; the route letter
is kept in the id. `queued` became `active`, `completed` became `closed`, and `parent` became
a "Sub-route of …" prefix of the objective. The `related: overlaps` links were:
`ap:c-gate-zero` with `ap:e-trace-upgrade`, `ap:c-anisotropic-bootstrap` and
`ap:c-solenoidal-perturbation`; they are recorded here and nowhere else.

| v0.1 | v0.2 |
|---|---|
| `ap:eldan-trace-upgrade`, `-weighted-excess`, `-screened-supply`, `-stein-weighted`, `-taming-splitting`, `-alignment` | `ap:e-trace-upgrade`, `ap:e-weighted-excess`, `ap:e-screened-supply`, `ap:e-stein-weighted`, `ap:e-taming-splitting`, `ap:e-alignment` |
| `ap:spectral-occupation`, `ap:spectral-window-chain` | `ap:s-occupation`, `ap:s-window-chain` |
| `ap:cmh-*` (seven routes) | `ap:c-*`, same suffixes |
| `ap:fiber-frame-construction`, `ap:fiber-simplex-dual` | `ap:f-frame-construction`, `ap:f-simplex-dual` |
| `ap:cone-boundary-gap`, `ap:laplace-brenier-simplex` (parked probes) | unchanged ids, still blocked on their candidates |

`ap:e-weighted-excess` was blocked on `prop:weighted-spectator-obstruction`, which is
proved: the route is **closed** on that obstruction. It reopens if a cut-local,
tensor-stable covariance weight that ignores independent spectators while still dominating
the aligned two-tail mode is proposed, or if a replacement carrying an explicit
near-worst-measure premise is certified; `ap:e-screened-supply` is the live sub-route that
pursues the first option.

**Records.** Exceptions to the append-only rule and to certification were made for this move and for
no other purpose.

1. The front matter of every checkpoint and review was rewritten to the v0.2 format; bodies
   are unchanged, except for a one-line *Follows up* mention where the dropped `follows_up`
   field said something the body did not. The six cold dossier audits that had no verdict
   now carry `verdict: revise`, with `authors` and `reviewer` read from their opening
   paragraph; the three programme audits (`2026-08-24-kls-consolidation-audit.md`,
   `2026-08-25-kls-cmh-normalization-audit.md`, `2026-08-25-legacy-r2-debt-triage.md`) are
   now checkpoints in this directory, under the same names.
2. **Fingerprints were recorded without a reading.** The conversion changed the bytes of
   every dossier and statement, so every certification would have lapsed. By a human
   decision of the migration, each review received the fingerprints of the MyST versions
   of the dossiers it covered, and of the statements those dossiers are checked against,
   as printed by `check.py --fingerprint` on 2026-09-29. No reviewer read these versions.
   The certifications therefore rest on the LaTeX reviews plus the conversion oracle, which
   checks structure, not mathematics. The reviews concerned:
   - cited by proof records (32): every file of `research/reviews/` except the seven below;
   - cited by none (7): the six audits now `revise`
     (`2026-08-27-cor-full-matrix-dissipation-proof-review.md`,
     `2026-08-27-kls-excess-repair-w0-audit.md`,
     `2026-08-27-lem-lyapunov-stein-duality-proof-review.md`,
     `2026-08-27-prop-weighted-spectator-obstruction-proof-review.md`,
     `2026-09-06-lem-cmh-linear-spectral-resolution-audit.md`,
     `2026-09-06-prop-cone-moment-map-audit.md`) and the superseded
     `2026-08-25-kls-geometry-product-r2-audit.md`.

   Any later edit of a dossier or of a statement lifts the certification in the ordinary
   way; the next review of a dossier is its first review of the MyST text.
3. **Stale "candidate" wording removed**, at the owner's request, after the fingerprints
   of item 2 were first recorded. The eleven dossiers titled "Solution candidate: …", all
   named by proof records, are now "Solution: …"; the manuscript titles of
   `thm:bootstrap-stopped-interface`, `lem:conditional-fiber-form` and
   `prop:conditional-fiber-root-obstruction` lost their trailing "candidate"; in
   `solutions/prop-mm-window-occupation.md` the three companion dossiers are no longer
   called candidates and uncertified, and `thm:klartag-logn` no longer pending, since all
   four were certified or accepted afterwards. The fingerprints of item 2 were recomputed
   on these versions, under the same decision.
4. **One candidate statement corrected in place.** In
   `2026-09-06-numerics-cmh-cone-w5n01.md`, `cand:cone-transverse-equality-simplex` said
   that `prop:cone-moment-map` "is still open"; it now says the node was open when the
   candidate was proposed and has been proved since. Nothing else in the candidate changed.

**Dossiers.** The 30 dossiers are `solutions/*.md` under their old basenames. Each now opens
with an **Overview** written from the dossier by a separate agent; it adds no claim and
states no status, and it was fingerprinted with the rest.

**Numerics.** `experiments/` is `research/lib/` (package `numerics`, its tests, its own
`pyproject.toml` and `uv.lock`), with the instance registry at `research/lib/instances.md`.
The eleven runs under `research/runs/` keep their timestamped names. None has a
`<date>-<slug>.py` script: each was produced by `uv run python -m numerics run <target>`
from the package, and its first line records the target, profile, seed, configuration and
commit.

**Programme rules.** The former program constraints P1 and P2 are under *Traps* in the
brief, with their old names, since earlier records cite them.

## What resists

- *observed* The sign in the falsification clause of `q:cmh-solenoidal-perturbation`
  disagrees between two places of the v0.1 text: the statement says a *positive* second
  variation refutes $\mathrm{CMH}(4)$, the gateway of `modules/40-moment-map-cmh.md` says a
  *negative* one does. The oriented statement follows the former; a `sync` review should
  settle which convention is meant.
- The conversion of the nineteen statements listed above (the six obstructions kept their wording) was done during the migration, not
  by a reviewer; `q:cmh-approximation` is the only one with a proof record.
- The site (`index`, `problem`, `results`, written by the `writer` at this milestone) says
  each proof was checked by an independent reviewer. That holds of the LaTeX versions; before
  publishing, the person who dispatches the site decides whether to wait for fresh `certify`
  reviews. The writer proposed cards for `q:mm-spectral-occupation`,
  `conj:gate-zero-sharp` and `q:conditional-fiber-frame`.

## Proposed next step

A `reviewer` with the `sync` lens on the nineteen converted statements above and on this sign;
then fresh `certify` reviews of the dossiers with the most proof records
(`kls-localization-riccati-core.md`, `thm-cmh-dirichlet.md`, `kls-excess-audit.md`) to replace
the migration's fingerprints with fingerprints someone read.
