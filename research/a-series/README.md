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
  README.md      program workflow
```

| information | canonical location |
|---|---|
| claim, status, dependencies, obstructions, certification/refutation pointers | [`ledger.yaml`](ledger.yaml) |
| shared ledger kinds, statuses, fields, and invariants | [`../ledger-schema.md`](../ledger-schema.md) |
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
   certification under the repository proof contract.

Numerics may guide a refinement or expose a candidate refutation. Passing a finite battery does
not validate a statement or proof.

## Ledger schema

The A-series ledger uses the unified schema in [`../ledger-schema.md`](../ledger-schema.md).
That document also owns the A-series extensions `meta.scope` and `refines`.

## Bridge to KLS

`conj:a1-bis` asks for `C_P <= K lambda_max(Cov)` on structured GLM posteriors. The same bound
for every isotropic log-concave measure is KLS. The ledger therefore carries the explicit bridge
`kls/conj:kls`; neither side is recorded as a proof dependency of the other.

## Verify

```bash
python3 research/check_ledger.py
```
