# A-series target brief simplification

- **Date:** 2026-08-25
- **Type:** harness/control-plane refactor
- **Scope:** `research/targets/`; no mathematical claim or status change

## Problem

The five target notebooks had grown into 844 lines that repeated ledger status, manuscript
exposition, proof audits, and numerical documentation. Their unique orchestration role was
obscured: they are the per-stream writable staging area that lets refiners propose changes while
the singleton orchestrator owns the ledger.

## Decision

- Treat each file as a mutable **refinement brief**, not an archive or source of truth.
- Keep one flat file per A1--A5 stream.
- Retain only entry points, target-specific guardrails, an active handoff table, a candidate
  refinement slot, and links to durable context.
- Read status and dependencies from the ledger; keep accepted mathematics in the manuscript,
  attempts in explorations, diagnostics in `finum`/runs, and certification in solutions/reviews.
- Document the shared outline in `research/targets/README.md` rather than adding a standalone
  template for the fixed five-stream set.

## Outcome

The five briefs now total 224 lines. Relative links and handoff node ids resolve,
`research/check_ledger.py` reports 0 errors and 0 warnings, and all checker regression tests pass.
