# Ledger schema simplification: current state and one dependency orientation

- **Date:** 2026-08-25
- **Scope:** A-series/KLS ledger schema and active control-plane documentation
- **Outcome:** retire the A-series `conjectured` status and the untyped `unlocks` field

## Current-state model

The ledgers are snapshots of current logical state, not workflow histories or transition logs.
For the A-series, `open` now means unresolved whether the statement is rough or already precise;
`kind: conjecture` identifies a conjectural statement without introducing a second unresolved
status. The two former `status: conjectured` obstruction nodes, `obs:flat-direction` and
`obs:restricted-not-finite`, were therefore migrated to `status: open`. No statement, dependency,
or mathematical verdict changed.

The descriptive `WORKFLOW` block was removed from the A-series ledger header. The contribution
process remains in `research/README.md`; the checker continues to enforce the proof half through
the standalone solution and independent-review requirements.

## Dependency orientation

`depends_on` is the sole stored proof-dependency orientation: a consuming node points to the
premises it actually uses. Downstream consumers can be derived by reversing that graph.

The 11 former `unlocks` entries were not converted mechanically into dependencies. The audit
found that three were already represented by `refines` or transitive `depends_on`, three recorded
obstruction provenance already present in the obstruction control plane, and the remainder mixed
roadmap, package-component, and partial-contribution relationships. In particular, some would
have overstated logical sufficiency if converted to `depends_on`. Those relationships now remain
in precise prose where needed.

The checker rejects any reintroduced `unlocks` key, including an empty one. It also rejects the
retired A-series `conjectured` status while accepting `kind: conjecture` with `status: open`.

## Validation

- `python3 research/check_ledger.py`: 172 nodes, 0 errors, 0 warnings.
- A-series summary: 39 open, 29 proved, 3 imported, 1 refuted.
- KLS summary: 22 open, 51 proved, 13 conditional, 10 imported, 3 heuristic, 1 defined.
- `python3 -m unittest discover -s research/tests -p 'test_*.py'`: 23 tests passed.
- `git diff --check`: clean.

