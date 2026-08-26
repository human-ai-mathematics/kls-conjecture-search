# Agent role definitions replace the orchestration narrative

**Date:** 2026-08-26

## Problem

`orchestration.md` held a roster table describing what each agent role reads and produces. It was
prose: nothing enforced it, nothing loaded it, and it duplicated rules that `CLAUDE.md`,
`research/README.md`, `solutions/README.md`, and `research/kls/routes.md` already owned. Its
parallelization diagrams restated a dependency graph the ledger derives, so they drifted — the
committed version still named the pre-rename program id `ab`.

The repository's real invariants are write-surface invariants. Hard constraint 1 (single-writer
ledger), constraint 2 (no private Monte Carlo), constraint 3 (curated shared battery), and
constraint 8 (append-only history) all say *who may write what*. A table in a Markdown file cannot
carry that; an agent definition with a `tools:` frontmatter and an explicit write surface can.

## Decision

Role definitions live in `.claude/agents/*.md`, one file per role, each stating mission, write
surface, method, and a report contract. `.codex/agents` is a symlink to that directory, mirroring
the existing `AGENTS.md` → `CLAUDE.md` arrangement, so both harnesses read identical roles.
`orchestration.md` is deleted and `CLAUDE.md` points at `.claude/agents/README.md` in its place.

Thirteen roles: `scout`, `refiner`, `finum`, `prover`, `refutation-seeker`, `proof-checker`,
`synthesizer`, `latex-sync`, `janitor`, `proof-miner`, `literature-scout`, `kls-route-scout`,
`kls-route-prober`.

Four invariants shape the set:

1. **The orchestrator is the main session, not a spawnable agent.** No role writes a `ledger.yaml`,
   `research/kls/routes.md`, or `research/kls/gating.md`. Each role ends its report with a
   proposed ledger delta; the orchestrator applies it and runs the checker.
2. **Author and reviewer cannot coincide.** `prover` has no write access to `research/reviews/`;
   `proof-checker` has none to `solutions/`. `proof-checker` defaults to `type: audit` and must
   earn `proof-review`/`pass`.
3. **Numerics have exactly one door.** Only `finum` runs computation; every other role specifies a
   diagnostic and hands it over. This is constraint 2 made structural rather than hoped for.
4. **The cleaning role cannot clean.** `janitor` has no `Write` or `Edit` tool at all. It returns a
   change list and a draft decision record; the orchestrator applies. Cleaning is the role whose
   natural instinct — delete what looks stale — is exactly wrong next to `explorations/`,
   `decisions/`, `reviews/`, and `runs/`.

Exploration is split three ways rather than bundled: `scout` (read-only orientation, no writes),
`refiner` (A-series statement deltas), and, for the KLS program, `kls-route-scout` (propose a new
route under the five-part contract in `routes.md`), `kls-route-prober` (one gate from `gating.md`,
in depth), `proof-miner` (repository proofs → unused hypotheses, bottlenecks, generalizations),
and `literature-scout` (external results, classified `published` / `preprint-unreviewed`, with
citation debt reported).

## Migration boundary

Content rescued from `orchestration.md` before deletion:

- the three merge barriers → `synthesizer.md`, which now owns them explicitly;
- the fan-out/converge summary → `.claude/agents/README.md`;
- the roster's I/O columns → the individual role files.

Content deliberately dropped: the per-target DAG art and the KLS route diagrams (derivable from
`depends_on` and already narrated in `routes.md`), and the frontier narration, which
`orchestration.md` itself warned goes stale.

Historical references to `orchestration.md` inside `research/explorations/` and
`research/decisions/` are left untouched — those directories are append-only.

## Compatibility

`.gitignore` previously excluded `.claude/`, `.codex/`, and `.agents/` wholesale. It now excludes
`.claude/*` and `.codex/*` with negations for the two `agents` paths, so the role definitions are
tracked while local session state stays ignored. The empty, superseded `.agents/` directory was
removed.

No ledger, schema, checker, manuscript, or dossier semantics change.

## Known limit

`tools:` frontmatter grants `Bash` wholesale; it cannot restrict a role to specific commands. So
"no ad-hoc numerics" is enforced by prompt for every role that needs the checker or `latexmk`,
and structurally only for `scout` and `janitor` in respect of file writes. A `permissions.deny`
entry in `.claude/settings.json` for ad-hoc interpreter invocation would close that gap; it is not
adopted here because it would also constrain the human operator's own session.

## Validation

```bash
python3 research/check_ledger.py                                # 0 errors
python3 -m unittest discover -s research/tests -p 'test_*.py'   # pass
```

Both re-run after the deletion and the `CLAUDE.md` edit; neither reads `orchestration.md`. No
remaining tracked document links to the deleted file.

## Addendum — `CLAUDE.md` pass

Same date, same change set. The role files made two references in `CLAUDE.md` stale and one
rule redundant:

- Constraint 3 named a `librarian` role that no longer exists; the shared-battery registry is
  curated by `synthesizer`. Constraint 4 attributed semantic checking to "a critic"; it is now
  `latex-sync` (prose ↔ ledger ↔ dossier agreement) and `proof-checker` (the argument itself).
- Constraint 1 enumerated squad write surfaces. That list was already incomplete — it omitted
  `research/reviews/`, `research/knowledge/`, `experiments/finum/`, and `fi_references.bib` — and
  would drift against the role files, which now declare each surface. Replaced by the invariant:
  no role's write surface includes a ledger.
- "Numerics certify nothing" was stated three times (ledger contract, constraint 2, constraint 3).
  It now lives once, in constraint 2, stated more broadly: not a claim status, not a proof step,
  not a dossier.
- The proof-contribution paragraph restated the four requirements it had just delegated to
  `solutions/README.md`. Reduced to the delegation plus the requirement parallelism erodes first:
  distinct author and reviewer.

One rule was **generalized, not narrowed**: constraint 7 previously read "`conditional` nodes are
Lean-certifiable only as conditional implications", which was already the general rule in
`solutions/README.md` and `ledger-schema.md` restricted to one certification mode. It now reads
"a certified conditional implication stays `conditional` … for every certification mode, Lean
included". No node's current status changes.

The eight constraints keep their numbers and order: `research/reviews/` and
`research/explorations/` cite them by number and are append-only, so renumbering would silently
invalidate history. A note to that effect is now in the section preamble.

Net: 1008 → 952 words. The file is largely load-bearing; the pass removed duplication and
staleness rather than rules.
