# KLS research control plane

This directory coordinates the exploratory KLS proof program in Part III. It does not duplicate
the mathematics: statements and proofs live in `modules/kls/` and `solutions/`.

## Sources of truth

| question | authoritative file |
|---|---|
| What is the mathematical statement? | `modules/kls/**/*.tex` |
| What is proved, open, conditional, or imported? | [`ledger.yaml`](ledger.yaml) |
| Which route owns a node? | its explicit `route:` field in the ledger |
| What routes are live and where should work start? | [`routes.md`](routes.md) |
| Which statement/proof shapes are fenced? | [`obstructions.md`](obstructions.md), referenced by ledger `bounded_by` |
| What has already been tried? | [`research/explorations/`](../explorations/) |
| What can `finum` currently compute? | [`experiments/README.md`](../../experiments/README.md) |

The ledger is deliberately route-spanning and single-writer. Every node declares one of
`shared`, `eldan-localization`, `moment-map-spectral`, or `moment-map-cmh`; route directories
contain briefs, never local ledgers.

## Working contract

Choose a route in [`routes.md`](routes.md), then work from that route's open-problem brief. Before
proposing a KLS ledger change:

1. check the manuscript statement and its exact `\label`;
2. follow only same-ledger logical `depends_on` edges; conditional premises are derived from that closure;
3. check every applicable `bounded_by` obstruction;
4. keep numerical observations inside `finum` and treat them as directional;
5. funnel the central ledger edit through the orchestrator and log the attempt.

Imported nodes require an explicit publication class and BibTeX references. Every `proved` node
requires a standalone dossier and the certification metadata specified in `solutions/README.md`.
A reviewed conditional implication may carry the same certification while remaining conditional.

## Verify

```bash
python3 research/check_ledger.py
python3 -m unittest discover -s research/tests -p 'test_*.py'
```

The checker establishes structural consistency only. It does not certify that manuscript,
ledger statement, and proof dossier agree mathematically.
