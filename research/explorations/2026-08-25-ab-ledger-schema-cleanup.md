# A-series ledger schema cleanup

- **Date:** 2026-08-25
- **Scope:** `research/ledger.yaml`, its field contract, and R0 enforcement
- **Outcome:** separate mathematical kind from epistemic status; make imported provenance and
  manuscript anchors explicit; retire the untyped A-series `related` graph

## Audit findings

The A-series ledger had 72 nodes and passed R0, but several distinctions existed only in prose.
The `kind` vocabulary mixed mathematical form (`theorem`, `lemma`) with comparison role
(`baseline`) and provenance (`imported`). Of the three imported-status nodes, two repeated
`imported` as their kind while the third correctly retained `kind: obstruction`. None carried a
machine-readable bibliography field.

The manuscript-location contract had also drifted. Nine stable node ids were not the intended
statement label: most used `refines` as an alias, one obstruction had no explicit anchor, and the
certified `eq:a4-mean-dual` node named the displayed equation rather than the enclosing theorem.
Renaming certified ids would invalidate dossier and review provenance, so the migration retained
those ids and introduced an exceptional `label` anchor. New ids remain equal to their manuscript
labels.

Finally, `related` had become a large untyped, mostly one-way navigation graph. It had no logical
effect, overlapped with prose roadmaps, and conflicted with the rule that `depends_on` is the sole
stored proof-dependency orientation.

## Decisions and migration

1. `kind` now records mathematical form only. `thm:glm-fi` is a proved theorem used as a baseline;
   `thm:hardy-1d` and `thm:a3-student` are imported theorems.
2. Every A-series import explicitly declares `import_class` and a non-empty `references` list of
   keys from `fi_references.bib`. Huguet's 2024 theorem is published in *Bernoulli*; its entry was
   upgraded from arXiv-only metadata, and the Bonnefont--Joulin--Ma DOI was corrected.
3. Synthetic ids declare `label`; the checker requires the effective label (`label` or `id`) to
   occur in the declared `file`. `refines` is reserved for genuine semantic sharpening.
4. All A-series `related` fields were removed. No entry was converted into `depends_on`: doing so
   would overstate proof use. Cross-program `bridges` and obstruction `bounded_by` edges remain.
5. The A-series node schema is allowlisted. Unknown fields, scalar values for list fields, and the
   retired `evidence_eligible`, `proof_file`, `proof_provenance`, `unlocks`, and `related` fields
   now fail R0.
6. Directional artifacts require the complete triplet `evidence`, `evidence_target`, and
   `evidence_run`; an artifact path without an explicit directional classification is invalid.
7. Proof certification metadata is valid on A-series nodes only with `status: proved`.

The complete field dictionary is now in `research/README.md`. The short ledger header states only
the organizing distinctions and canonical edges.

## Logical effect

No mathematical statement, status, proof dependency, obstruction edge, bridge, solution dossier,
or certification verdict changed. This is a schema and provenance migration of the ledger itself,
not a proof or numerical contribution. Historical exploration and review files were not rewritten.

## Validation

- `python3 research/check_ledger.py`: 172 nodes, 0 errors, 0 warnings.
- `python3 -m unittest discover -s research/tests -p 'test_*.py'`: 27 tests passed.
- The A-series counts remain 39 open, 29 proved, 3 imported, and 1 refuted.

