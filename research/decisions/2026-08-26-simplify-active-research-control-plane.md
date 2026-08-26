# Simplify active research control-plane documents

- **Date:** 2026-08-26
- **Type:** harness/control-plane refactor
- **Scope:** active research documentation, obstruction resolution, and ledger presentation
- **Mathematical effect:** none

## Problem

The active control plane mixed current instructions with migration history, dated updates,
compatibility pointers, and duplicated route handoffs. KLS `bounded_by` edges could resolve
against Markdown headings while A-series edges resolved against ledger nodes, so the same field
had two program-specific meanings. Several A-series ledger statements also embedded workflow
phrases such as “proof draft” and “certification pending” even though status and certification
fields already carried that information.

## Decision

1. Active READMEs, obstruction registries, route documents, gates, and ledger comments describe
   current state only. Attempts, reviews, runs, and earlier harness decisions remain in their
   append-only planes.
2. KLS route theses and entry points live in `research/kls/routes.md`. Acceptance criteria live
   in `research/kls/gating.md`. Superseded route-local handoffs and compatibility pointers are
   removed. Two paths referenced by immutable explorations remain as current-navigation shims.
3. Every `bounded_by` reference resolves to a same-ledger node with `kind: obstruction`.
   Markdown headings no longer create machine identifiers. The checker also requires one prose
   heading for every obstruction node. Six KLS obstruction aliases were added as `status: open`
   nodes without promoting a mathematical claim; their statements point to the existing
   manuscript anchors and source nodes.
4. Ledger `statement` values contain only the current mathematical assertion or question.
   Workflow state remains represented by `status` and certification fields.
5. Remove `q:cmh-normalization`, a completed work-package marker with no graph consumers.
   The current definition and endpoint theorem remain represented by `def:cmh` and
   `thm:cmh-implies-affine-poincare`, with their existing certification.
6. Mutable A-series target briefs retain only entry points, guardrails, active deliverables, and
   candidate refinements. Historical context remains discoverable in the canonical append-only
   directories.

## Validation

- `python3 research/check_ledger.py`: 2 ledgers, 170 nodes, 632 labels, 0 errors.
- `python3 -m unittest discover -s research/tests -p 'test_*.py'`: 38 tests pass.
- Active Markdown audit: 29 files checked, 0 missing relative links.
- Obstruction audit: A-series 7 nodes/7 headings; KLS 6 nodes/6 headings.
- `latexmk -pdf -outdir=build main.tex`: the 149-page manuscript compiles.
- `git diff --check`: clean.
