# Split the A-series and KLS programs into two repositories

- **Date:** 2026-09-01
- **Type:** repository organization
- **Scope:** the whole repository; mirrored in `posterior-inequalities-exploration`
- **Mathematical effect:** none — no statement, status, dependency, or proof changed
- **Contract exception:** authorized by the repository owner despite hard constraint 8; each
  repository retains only the append-only records of its own program (see *Append-only history*)

## Problem

One repository carried two programs that shared a harness but almost nothing else. Measurement
before the split, not assumption:

| seam | measurement |
|---|---|
| `\ref` from `modules/kls/` into Parts I/II | **0** of 258 |
| `\ref` from Parts I/II into `modules/kls/` | 12, all in `modules/00-overview.tex:47-59` |
| prose "Part I/II" inside `modules/kls/` | 6 lines across 2 files |
| cross-program `depends_on` in either ledger | **0** |
| `solutions/*.tex` claimed by both ledgers | **0** of 45 (24 A-series, 21 KLS) |
| reviews naming nodes of both programs | **1** of 49 |
| importers of `finum/localization/` | `targets/kls/*` only |

The one logical link was `bridges: a-series/conj:a1-bis ↔ kls/conj:kls`, which
`research/README.md` already defined as a comparison rather than a proof dependency. Everything
else that looked shared was infrastructure: the preamble, the bibliography, the checkers, the
`finum` core, and the agent roster.

Keeping both programs together therefore bought no mathematical coupling while forcing every
contributor, ledger read, and validator run to carry the other program's surface.

## Decision

`functional-inequalities-exploration` was renamed `kls-exploration` on GitHub and keeps Part III,
its ledger, its 21 dossiers, its 30 reviews, its 67 explorations, all four run artifacts, the
localization engine, and the two `kls-route-*` roles. Parts I and II move to
`posterior-inequalities-exploration` with the A-series ledger, 24 dossiers, 17 reviews, 19
explorations, the `a_series` finum targets, and the `refiner` role.

Infrastructure is **copied, not shared**: `shared/`, `fi_references.bib` (all 126 keys, a superset
for each side), `check_ledger.py`, `check_agents.py`, `ledger-schema.md`, `research/tests/`, the
`finum` core, the eleven program-neutral agent roles, and all 22 `research/decisions/` records.
There is no third repository and no submodule; the machinery that would have justified one is a
few hundred lines that diverge on their own schedule.

### The comparison is now prose

`bridges` resolves only within one repository, so the field was removed from `conj:kls` here and
from `conj:a1-bis` there. Each ledger carries a comment at that node naming the counterpart, each
`research/README.md` states the relationship, and each `CLAUDE.md` gains a constraint 9 forbidding
a `depends_on`/`bridges` edge or an imported dependency across the boundary. This is a
demotion in machine-checkability, accepted deliberately: the alternative was to teach the checker
an external-reference form for an edge that was never a proof dependency.

### Constraint numbering

Hard constraints 1-8 are unchanged here. Constraints 2, 3, 4, 6, and 7 are cited by four
explorations and four reviews in this repository, and constraint 6 governs the trace-upgrade
cluster, which is KLS-only. In `posterior-inequalities-exploration`, constraint 6 becomes a
reserved slot rather than being renumbered, so the two contracts stay diffable; no A-series
append-only record cites any constraint number, so nothing there breaks.

### Append-only history

Each repository keeps only its own program's explorations and reviews. This is a one-time
owner-authorized exception to hard constraint 8, in the same spirit as
`2026-08-26-prune-obsolete-exploration-harness-notes.md`: nothing is rewritten, and the complete
pre-split history remains reachable in the git history of this repository at commit `cd4a894`.
`posterior-inequalities-exploration` starts from a single initial commit naming that source, since
the pre-split history is twelve squashed commits that interleave both programs and would not give
the A-series side a usable log.

The one review naming nodes of both programs,
`research/reviews/2026-08-25-legacy-r2-debt-triage.md`, is referenced by neither ledger and is kept
in both repositories.

## Latent coupling repaired

The split surfaced two hardcoded program names in `check_ledger.py` that were invisible while both
ledgers existed: a `PROGRAMS["a-series"]` fallback for a ledger with an unknown program, which
crashed with `KeyError` instead of reporting, and a `program == "a-series"` guard on the obsolete
`conjectured` status, which silently gave the KLS ledger a worse error message. Both are now
program-agnostic (`DEFAULT_PROGRAM_CFG`, and an unconditional obsolete-status check) in both
repositories.

## Validation

In this repository:

- `python3 research/check_ledger.py` — 1 ledger, 121 nodes, 429 labels, 0 errors.
- `python3 research/check_agents.py` — 0 errors, 12 roles.
- `python3 -m unittest discover -s research/tests -p 'test_*.py'` — 42 tests, OK.
- `uv run pytest` in `experiments/` — 69 passed.
- `uv run python -m finum check` — PASS, 0 failures.
- `latexmk -pdf -outdir=build main.tex` — 100-page PDF, 0 undefined references, 0 undefined
  citations.

In `posterior-inequalities-exploration`: 1 ledger, 74 nodes, 246 labels, 0 errors; 0 errors and 11
roles; 42 tests OK; 29 pytest passed; `finum check` PASS; a 63-page PDF with 0 undefined
references and 0 undefined citations.

The checkers establish structure only. No mathematical claim was revalidated by this decision, and
none changed.
