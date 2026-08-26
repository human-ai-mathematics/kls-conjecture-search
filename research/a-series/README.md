# A-series control plane

This directory owns the A1--A5 program for Parts I/II. Its ledger id is `a-series`.

## Files

| question | source |
|---|---|
| What is the accepted statement? | [`../../modules/open-targets/`](../../modules/open-targets/) |
| What is its status and dependency graph? | [`ledger.yaml`](ledger.yaml) |
| What constrains an admissible statement? | [`obstructions.md`](obstructions.md) and ledger `bounded_by` |
| What should a refiner do next? | [`targets/`](targets/) |
| What has been attempted? | [`../explorations/`](../explorations/) |
| What reusable tools and instances exist? | [`../knowledge/`](../knowledge/) |
| Where are proofs and reviews? | [`../../solutions/`](../../solutions/), [`../reviews/`](../reviews/) |
| Where are numerical implementations and runs? | [`../../experiments/`](../../experiments/), [`../runs/`](../runs/) |

The ledger and manuscript are authoritative. Target briefs are mutable handoffs and contain no
claim status or proof history.

## Workflow

1. Select a node from the ledger or a target brief.
2. Read its manuscript anchor, `depends_on` closure, and every `bounded_by` obstruction.
3. Record the attempt in a new dated exploration; stage a proposed statement delta in the target
   brief when needed.
4. Send accepted manuscript and ledger changes through the orchestrator.
5. Certify proofs through a standalone dossier and independent review.

Numerical diagnostics must use `finum` and cannot change logical status.

## KLS bridge

`conj:a1-bis` is linked to `kls/conj:kls` by `bridges`. The link is a comparison, not a
proof dependency.

## Verify

```bash
python3 research/check_ledger.py
```
