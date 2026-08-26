# Delegate details from the root agent contract

- **Date:** 2026-08-26
- **Type:** harness documentation refactor
- **Scope:** `CLAUDE.md` / `AGENTS.md`
- **Mathematical effect:** none

## Problem

After the root-contract rewrite, `CLAUDE.md` still repeated repository orientation, the canonical
location table, the full proof checklist, validation commands, and ledger syntax. Each item
already had a narrower canonical owner. Keeping both copies created a drift surface and obscured
the small set of rules that every agent must load.

## Decision

1. Remove the project-subject description; repository and manuscript READMEs provide context.
2. Replace the location table with one link to `research/README.md`.
3. Delegate the detailed proof checklist to `solutions/README.md`, retaining globally only the
   author/reviewer separation requirement.
4. Remove the validation table. Ledger navigation and checks live in `research/README.md`,
   numerical commands in `experiments/README.md`, manuscript compilation in the root README, and
   dossier compilation in `solutions/README.md`.
5. Delegate node-label and `depends_on` semantics to `research/ledger-schema.md`.
6. Retain the Markdown math convention because it applies repository-wide.
7. Preserve the universal mathematical and harness workflow and all eight hard constraints with
   their existing numbers.

## Validation

- Delegated-owner audit: routing, proof, numerical, manuscript-build, label, and dependency details
  all resolve in their declared owners.
- `AGENTS.md` resolves to byte-identical `CLAUDE.md`; all eight constraint numbers remain.
- Root-contract relative-link audit: 0 missing links.
- `python3 research/check_ledger.py`: 2 ledgers, 170 nodes, 632 labels, 0 errors.
- `python3 -m unittest discover -s research/tests -p 'test_*.py'`: 38 tests pass.
- `git diff --check`: clean.
