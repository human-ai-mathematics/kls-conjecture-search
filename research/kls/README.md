# KLS control plane

This directory coordinates the Part III proof program. Statements live in `modules/kls/`; this
directory owns logical state, route selection, obstructions, and active acceptance gates.

## Files

| question | source |
|---|---|
| What is the target and each claim's status? | [`ledger.yaml`](ledger.yaml) |
| What ledger fields are valid? | [`../ledger-schema.md`](../ledger-schema.md) |
| Which proof routes are live? | [`routes.md`](routes.md) |
| What must the next contribution deliver? | [`gating.md`](gating.md) |
| Which proof shapes are fenced? | [`obstructions.md`](obstructions.md) and ledger `bounded_by` |
| What has been attempted? | [`../explorations/`](../explorations/) |
| What can be computed numerically? | [`../../experiments/README.md`](../../experiments/README.md) |
| Where are proofs and reviews? | [`../../solutions/`](../../solutions/), [`../reviews/`](../reviews/) |

Every node has one route: `shared`, `eldan-localization`, `moment-map-spectral`, or
`moment-map-cmh`. The route-spanning ledger is single-writer; route documents never carry claim
status or duplicate dependency graphs.

## Workflow

1. Choose a route in `routes.md`, then select an active node and read its gate in `gating.md`.
2. Read the ledger node, manuscript anchor, dependency closure, and every `bounded_by`
   obstruction.
3. Record the attempt in a new dated exploration. Send numerical work through `finum` and treat
   it as directional.
4. Send accepted ledger changes through the orchestrator.
5. Certify proofs through a standalone dossier and independent review.

Imported nodes require publication class and BibTeX references. A certified conditional
implication remains `conditional` while any blocking premise or unreviewed import remains.

## Verify

```bash
python3 research/check_ledger.py
python3 research/check_ledger.py status
python3 -m unittest discover -s research/tests -p 'test_*.py'
```

The checker validates structure, not mathematical correctness.
