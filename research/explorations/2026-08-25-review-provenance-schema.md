# Review provenance schema

- **Date:** 2026-08-25
- **Scope:** `research/reviews/`, agent R2 review metadata, and checker enforcement
- **Outcome:** replace free-form pass-token matching with typed, exact-scope review provenance

## Audit findings

The review archive contained 15 substantive reports: 12 operative agent proof reviews referenced
by 80 ledger nodes, plus three historical or diagnostic audits. The mathematical reports were
detailed and the ledger passed R0, but the certification boundary depended on text search. A
report qualified when its prose contained a generic Markdown `Verdict: pass` line, the node id
somewhere, and the reviewer identity somewhere. Consequently, a node mentioned only as an
exclusion or a non-certifying audit containing “pass” could syntactically satisfy the gate. The
checker did not compare report scope with `authored_by` or `solution`.

Header vocabulary had also drifted among “Proof author,” “Original proof author,” “Repair
author,” several reviewer labels, and singular/plural dossier fields. One operative report stated
only that its eleven dossiers lived under `solutions/`, despite the README requiring pointers to
the reviewed artifacts.

## Decisions and migration

1. Every report now begins with YAML front matter and has an explicit `type`.
2. The 12 operative certificates use `type: proof-review`, exact `verdict: pass`, a quoted ISO
   `date`, and structured `authors`, `reviewer`, `nodes`, and `solutions` fields.
3. The consolidation audit, original partial CMH audit, and legacy debt triage use `type: audit`.
   Their narrative outcomes have no mechanical proof effect.
4. Repair certificates use the optional `follows_up` pointer rather than changing the earlier
   audit's historical outcome.
5. The checker derives the nodes, authors, reviewer, and solutions associated with each report
   from the ledgers and requires exact set parity with the front matter. It also confines agent
   reports to Markdown files under `research/reviews/`, rejects orphaned proof reviews, and
   validates report dates and the small allowlisted schema.
6. Report bodies remain free-form mathematical prose. The README recommends findings,
   corrections, and exclusions without making editorial headings part of R0.

## Logical effect

No theorem statement, logical status, dependency, obstruction, solution dossier, author/reviewer
assignment, or certification verdict changed. Existing report bodies and filenames were
preserved apart from replacing redundant free-form opening metadata with the structured envelope
and short provenance prose where historical participants were not ledger authors.

No numerical experiment was run or used.

## Validation

- `python3 research/check_ledger.py`: 172 nodes, 0 errors, 0 warnings.
- `python3 -m unittest discover -s research/tests -p 'test_*.py'`: 30 tests passed.
- `git diff --check`: clean.
