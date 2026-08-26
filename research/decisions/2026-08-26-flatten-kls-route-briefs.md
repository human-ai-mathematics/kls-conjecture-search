# Flatten the KLS route briefs

- **Date:** 2026-08-26
- **Type:** repository-organization refactor
- **Scope:** `research/kls/routes.md`, `research/kls/routes/`, and `research/kls/gating.md`
- **Mathematical effect:** none

## Problem

The route tree mixed deleted multi-file route directories with two surviving navigation shims.
The central route registry also repeated every active node already described more precisely in
the gate file. This made it unclear whether a route directory, `routes.md`, or `gating.md` owned
the active handoff.

## Decision

1. `research/kls/routes/` contains exactly one flat Markdown brief per allowed route:
   `eldan-localization.md`, `moment-map-spectral.md`, and `moment-map-cmh.md`.
2. Each route brief contains only its thesis, active-node map, main obstruction boundary, and any
   essential non-equivalence warning. It contains no status, proof history, numerical status, or
   detailed acceptance criteria.
3. `routes.md` is the route index and cross-route ownership map. `gating.md` is the sole owner of
   node-specific acceptance criteria. The ledger remains authoritative for statements, status,
   dependencies, and `bounded_by` edges.
4. Repository-wide proof and promotion requirements are not repeated in `gating.md`; `AGENTS.md`
   remains their normative source.
5. The nested compatibility shims are removed. Append-only explorations and reviews retain their
   original path text as historical provenance; active navigation uses only the flat files.

## Validation

- Route layout audit: exactly three flat Markdown files and no nested directories.
- Active-document relative-link audit: 0 missing links.
- `python3 research/check_ledger.py`: 2 ledgers, 170 nodes, 632 labels, 0 errors.
- `python3 -m unittest discover -s research/tests -p 'test_*.py'`: 38 tests pass.
- `git diff --check`: clean.
