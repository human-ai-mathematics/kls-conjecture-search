# A-series control plane (A1--A5)

This directory owns the Part I/II open-target program. Its stable machine id is `ab`; the
human-facing name is A-series. The program refines structured statistical and machine-learning
statements and then certifies analytic proofs independently of numerical diagnostics.

## Layout and ownership

```text
a-series/
  ledger.yaml    canonical A-series claim graph and certification pointers
  obstructions.md  cross-target statement-shape barriers
  targets/       one mutable refinement brief per A1--A5 stream
  README.md      program workflow and ledger schema
```

| information | canonical location |
|---|---|
| claim, status, dependencies, obstructions, diagnostic pointers | [`ledger.yaml`](ledger.yaml) |
| accepted statement and exposition | [`../../modules/open-targets/`](../../modules/open-targets/) |
| proposed statement delta awaiting promotion | [`targets/`](targets/) |
| dated mathematical attempts | [`../explorations/`](../explorations/) |
| A-series obstruction prose | [`obstructions.md`](obstructions.md) |
| reusable lemmas and shared stress instances | [`../knowledge/`](../knowledge/) |
| numerical implementation and artifacts | [`../../experiments/finum/`](../../experiments/finum/), [`../runs/`](../runs/) |
| proof and independent certification | [`../../solutions/`](../../solutions/), [`../reviews/`](../reviews/) |

The ledger and manuscript win if a target brief drifts. A1--A5 are parallel streams inside one
program, not separate programs or separate ledgers. Their cross-target proof dependencies remain
visible in this single graph.

## Workflow

1. The orchestrator assigns a ledger node and remains the only ledger writer.
2. A refiner reads the ledger node, manuscript statement, target brief, and every listed
   `bounded_by` obstruction.
3. The refiner records the mathematical attempt in a dated exploration and stages only the
   proposed statement delta or numerical specification in the target brief.
4. The orchestrator promotes an accepted change to the manuscript and ledger, runs the checker,
   and clears or replaces the staged candidate.
5. A `proved` node enters the ledger only after a standalone dossier receives independent
   certification under the repository R2 contract.

Numerics may guide a refinement or expose a candidate refutation. Passing a finite battery does
not validate a statement or proof.

## Status vocabulary

- `open`: unresolved, whether rough or already precise.
- `proved`: certified through a standalone proof dossier.
- `imported`: accepted from named literature with explicit source metadata.
- `refuted`: independently certified false in the stated form.

`kind: conjecture` describes mathematical form; it is not a second unresolved status.

## Ledger schema

The ledger has exactly two top-level sections, `meta` and `nodes`. `meta.program: ab` selects the
A-series checker policy; `meta.scope` states the graph boundary. Unknown fields are rejected so a
spelling mistake cannot silently create a second schema.

### Identity and statement fields

| field | requirement | meaning |
|---|---|---|
| `id` | required non-empty string | Stable claim id, normally the exact LaTeX statement label. |
| `kind` | required enum | Mathematical form: theorem, proposition, lemma, corollary, conjecture, question, obstruction, or example. |
| `status` | required enum | `open`, `proved`, `imported`, or `refuted`. |
| `file` | required existing repo-relative path | Manuscript file containing the effective LaTeX label. |
| `label` | exceptional single label | Manuscript anchor for a stable synthetic id; omit when `id` is the label. |
| `statement` | required non-empty string | Concise restatement of the manuscript claim. |
| `refines` | optional single label | A genuinely broader statement sharpened by this node. |

The effective manuscript label is `label` when present and `id` otherwise. Semantic agreement
between ledger, manuscript, and dossier remains a critic responsibility.

### Logical graph fields

| field | meaning |
|---|---|
| `depends_on` | Premises actually used by the proof; this sole stored dependency direction is acyclic. |
| `bounded_by` | Obstruction ids constraining the admissible statement or proof. |
| `bridges` | Cross-program claim links written as `program/id`. |

Non-logical roadmap links belong in target briefs or other prose. Downstream consumers are
derived by reversing `depends_on`; the retired `related` and `unlocks` graphs must not return.

### Imported-result provenance

| field | requirement |
|---|---|
| `import_class` | Required for `status: imported`; `published` or `preprint-unreviewed`. |
| `references` | Required non-empty list of keys in `fi_references.bib`. |

An imported node has no repository proof-certification metadata. If the repository supplies and
certifies its own proof, the node is `proved` instead.

### Proof certification fields

| field | requirement |
|---|---|
| `solution` | Existing standalone dossier; required for `status: proved`. |
| `checked_by` | `agent`, `human`, or `lean` for a certified solution. |
| `authored_by` | Required named author for agent certification. |
| `reviewed_by` | Required distinct named reviewer for agent certification. |
| `review` | Required `research/reviews/*.md` proof-review with exact ledger/report parity. |

These fields are valid only on proved A-series nodes. An unwired draft dossier may declare
`checked_by: none` in its own header, but it does not enter the ledger.

### Research-direction and navigation fields

| field | meaning |
|---|---|
| `numerics` | Proposed `finum` stress test, calibration, or refutation search. |
| `evidence` | `none` or `numerical-directional`. |
| `evidence_target` | Expected `finum` target recorded by directional artifact provenance. |
| `evidence_run` | Existing provenance-stamped JSONL path; invalid without directional classification. |
| `target_doc` | Primary A1--A5 refinement brief, normally only on a stream headline. |
| `note` | Short exceptional locator, caveat, or retirement pointer—not workflow history. |

Exact analytic certificates still enter through the proof/refutation plane. Numerical fields can
never replace a dossier or independent review.

## Bridge to KLS

`conj:a1-bis` asks for `C_P <= K lambda_max(Cov)` on structured GLM posteriors. The same bound
for every isotropic log-concave measure is KLS. The ledger therefore carries the explicit bridge
`kls/conj:kls`; neither side is recorded as a proof dependency of the other.

## Verify

```bash
python3 research/check_ledger.py
```
