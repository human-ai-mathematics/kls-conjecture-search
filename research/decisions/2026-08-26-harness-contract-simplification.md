# Simplified research-harness contract

- **Date:** 2026-08-26
- **Type:** harness/control-plane refactor
- **Scope:** ledger semantics, proof provenance, obstruction declarations, checker interface, and active documentation
- **Mathematical effect:** none

## Problem

The structurally green harness still mixed three different concerns. Logical status doubled as a
proof-certification switch, so a reviewed conditional implication could not remain
`status: conditional` and a `refuted` node had no explicit certified refuter. Immutable review
reports were required to have exact parity with mutable current ledger references, which made an
honest later downgrade awkward. The ledgers also carried unused numerical-evidence fields,
free-form numerical and note prose, and an opt-in KLS mechanism vocabulary whose omission could
not be detected.

The checker exposed only aggregate counts, so the documented instruction to read the live
frontier from it still required manual YAML inspection.

## Decision

1. Logical status and certification are separate concerns. `proved` still requires certification;
   `conditional` may also carry a certified dossier without becoming unconditional. A `refuted`
   node names one or more proved/imported refuters through `refuted_by`.
2. A node carries only the active certification pointer. Agent identities and certified scope are
   canonical in the immutable proof-review front matter. Current ledger references must be
   contained in that historical scope, but a report may retain extra formerly active nodes and a
   proof review may remain unreferenced.
3. `checked_by: human` remains available and requires a named `accepted_by`. `checked_by: lean`
   remains available and requires an adjacent `.lean` file. Ledger-level `checked_by: none` is
   retired; `none` remains valid only in an unwired draft dossier header.
4. `depends_on` contains only nodes in the same program ledger. Manuscript equations and ordinary
   literature citations remain in dossiers/manuscript prose rather than masquerading as graph
   nodes. Cross-program comparison remains `bridges`.
5. `bounded_by` is the sole obstruction declaration. Applicability and semantic clearance are a
   critic responsibility. The opt-in KLS `mechanism`/`clearance` layer and its YAML mirror are
   removed; KLS obstruction ids are the headings in `obstructions.md`.
6. Remove ledger `evidence`, `evidence_target`, `evidence_run`, `numerics`, and `note`. R1
   provenance belongs to immutable `research/runs/` artifacts and dated explorations; active
   numerical implementation belongs to `experiments/`.
7. Keep the existing checker command compatible and add derived `status` and `node` views. These
   views never become a second stored graph.

## Compatibility

Historical explorations, reviews, runs, and compatibility-pointer Markdown files are not
rewritten or moved. Existing proof-review front matter remains valid. Human and Lean modes stay in
the public vocabulary so their stronger validators can be extended without another schema rename.

## Validation

Validated on the current branch after migration:

- `python3 -B research/check_ledger.py`: 2 ledgers, 165 nodes, 632 labels, 0 errors;
- `python3 -B -m unittest discover -s research/tests -p 'test_*.py'`: 34 tests pass;
- the derived `status` and `node q:upgrade` views run without writing repository files;
- all active relative Markdown links resolve; and
- `git diff --check` is clean.
