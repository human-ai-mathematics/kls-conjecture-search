# KLS harness simplification

## Scope

Simplify `research/kls/` without changing manuscript mathematics or promoting/refuting a claim.
The branch already had the A-series move, explicit KLS `route:` ownership, and structured exact
proof-review provenance; those stronger contracts were preserved.

## Ledger and checker changes

- Made `depends_on` the only logical intra-program graph. Removed duplicated `assuming` contracts
  and non-logical `related`, `entry_point`, and `discharged_by` fields. Conditional premises are
  now derived recursively from dependency closure, including unreviewed preprints.
- Made ledger `bounded_by` the canonical obstruction direction and removed the hand-maintained
  reverse `obstructions.yaml.constrains` lists.
- Required explicit `import_class` and verified BibTeX `references` for imported nodes in both
  programs, then supplied all nine KLS imports with provenance.
- Applied the proof-metadata scope rule uniformly: certification fields are valid only on
  `status: proved` nodes.
- Removed seven ledger records that did not carry independent claim state:
  `prog:product-test`, `prog:cmh-route`, `q:gate-zero`, `rem:kl-window-verified`,
  `heur:V2-fails`, `rem:trace-upgrade-unification`, and `rem:taming-type-mismatch`. Their
  manuscript labels and substantive prose remain; live mathematical questions are represented by
  `q:alignment`, `conj:gate-zero`, and the other precise nodes.

The KLS ledger now has 93 nodes: 51 proved, 19 open, 13 conditional, 9 imported, and 1 defined.

## Documentation changes

`research/kls/routes.md` is now the single route registry. The root README is an ownership map;
route READMEs state thesis and status; open-problem files contain only active handoffs and
acceptance gates. Numerical implementation status moved to `experiments/README.md`.

During this pass, active KLS Markdown was reduced from 2,344 to 453 lines. Compatibility pointers
preserve old paths used by historical reports. The unique 648-line CMH construction claim
inventory and 115-line model inventory were preserved as dated attempt memory in:

- `research/explorations/2026-08-25-kls-cmh-construction-claim-archive.md`;
- `research/explorations/2026-08-25-kls-cmh-model-archive.md`.

## Validation

- `python3 research/check_ledger.py`: 2 ledgers, 165 nodes, 0 errors, 0 warnings.
- `python3 -m unittest discover -s research/tests -p 'test_*.py'`: 33 tests passed.
- `python3 -m py_compile research/check_ledger.py research/tests/test_check_ledger.py`: passed.
- `cd experiments && UV_CACHE_DIR=/tmp/kls-harness-uv-cache uv run pytest`: 90 tests passed.

These are R0 checks only. No numerical result was used, and no proof status was changed.
