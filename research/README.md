# Research control plane

`research/` coordinates two mathematical programs. The manuscript owns accepted statements,
the ledgers own logical state and graph edges, `solutions/` owns standalone proofs, and numerical
runs guide research without certifying claims.

## Programs

| program | ledger id | entry point | purpose |
|---|---|---|---|
| A-series (A1--A5, Parts I/II) | `a-series` | [`a-series/README.md`](a-series/README.md) | refine statements and prove structured-posterior results |
| KLS (Part III) | `kls` | [`kls/README.md`](kls/README.md) | compare proof routes and discharge their open inputs |

Each program has one ledger. All ledger writes pass through one orchestrator.

## Sources of truth

| content | location |
|---|---|
| ledger fields and invariants | [`ledger-schema.md`](ledger-schema.md) |
| accepted mathematical prose | [`../modules/`](../modules/) |
| claim state and logical edges | `a-series/ledger.yaml`, `kls/ledger.yaml` |
| proof dossiers | [`../solutions/`](../solutions/) |
| reusable lemmas and shared instances | [`knowledge/`](knowledge/) |
| mathematical attempts and dead ends | [`explorations/`](explorations/) |
| independent reviews | [`reviews/`](reviews/) |
| numerical artifacts | [`runs/`](runs/) |
| harness decisions | [`decisions/`](decisions/) |

The ledgers use `depends_on` for same-program proof dependencies, `bounded_by` for obstruction
nodes in the same ledger, and `bridges` for non-logical cross-program comparisons written as
`program/id`. The A1-bis/KLS bridge is `a-series/conj:a1-bis` ↔ `kls/conj:kls`.

## Contribution flow

1. Select a ledger node and read its manuscript statement, dependencies, and obstructions.
2. Record the attempt in a new dated exploration; put numerical work through `finum`.
3. Send accepted statement and ledger changes through the orchestrator.
4. For a proof, supply a standalone dossier and independent review.
5. Run the structural checker.

## Verify

```bash
python3 research/check_ledger.py
python3 research/check_ledger.py status
python3 research/check_ledger.py node q:upgrade
python3 -m unittest discover -s research/tests -p 'test_*.py'
```

The checker validates repository structure, not mathematical correctness. The contribution rules
are in [`../CLAUDE.md`](../CLAUDE.md).
