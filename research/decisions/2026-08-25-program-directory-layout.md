# Symmetric program-directory layout

- **Date:** 2026-08-25
- **Type:** harness/control-plane refactor
- **Scope:** research program ownership and checker ledger discovery
- **Mathematical effect:** none

## Problem

The A-series program owned root-level `research/ledger.yaml` and `research/targets/`, while KLS
already occupied a self-contained `research/kls/` directory. The asymmetry made the research root
look A-series-specific, obscured which files were program-owned, and forced the root README to mix
repository-wide policy with the complete A-series schema.

## Decision

- Make `research/a-series/` and `research/kls/` peer program homes.
- Retain one ledger per program and the stable machine ids `ab` and `kls`.
- Keep A1--A5 as streams within one A-series ledger rather than creating per-target ledgers.
- Colocate the A-series obstruction prose with its ledger, matching KLS ownership; keep reusable
  lemmas and the mixed A/KLS instance battery in root-level `knowledge/`.
- Keep `knowledge/`, `explorations/`, `reviews/`, and `runs/` at the research root. They are shared
  or provenance-bearing planes whose historical paths should not churn during this migration.
- Keep `solutions/` and `modules/` as repository-root proof and prose planes.
- Introduce this append-only `decisions/` plane for future harness and schema decisions; existing
  harness notes in `explorations/` remain unchanged.
- Configure the production checker with explicit ledger paths. Fixture tests may still discover
  temporary ledgers, but no ledger may infer its program from its directory name.
- Make KLS route ownership explicit on every node and retire the historical implicit-Eldan
  default.

## Migration

The A-series ledger moved to `research/a-series/ledger.yaml`, and its five mutable briefs moved to
`research/a-series/targets/`. Active documentation and machine pointers were updated. Historical
exploration and review prose was not rewritten solely to update old path narration.

## Validation

The required gates are `python3 research/check_ledger.py`, the checker regression suite, a scan
for stale active paths, Markdown relative-link resolution in moved briefs, and `git diff --check`.
