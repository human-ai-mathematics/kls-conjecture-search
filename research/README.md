# Research control plane

`research/` holds the three domains the root contract keeps apart. The manuscript owns accepted
statements, the ledger owns logical state and graph edges, the portfolio owns what the search is
doing, `solutions/` owns standalone proofs, and numerical runs guide research without certifying
anything.

> Ledger = what is mathematically claimed. Portfolio = what the search is doing.
> Checkpoints = why the portfolio changed.

## Program

One program, `kls`, and one ledger. All ledger writes pass through one orchestrator
(`CLAUDE.md` constraint 1).

## Sources of truth

| content | location |
|---|---|
| accepted mathematical prose | [`../modules/kls/`](../modules/kls/) |
| claim state and logical edges | [`program/ledger.yaml`](program/ledger.yaml) |
| ledger fields and invariants | [`program/ledger-schema.md`](program/ledger-schema.md) |
| the target, its negation, completion criteria, traps | [`program/brief.md`](program/brief.md) |
| route families, states, blockers, saturation | [`program/portfolio.yaml`](program/portfolio.yaml) |
| portfolio and brief field contract | [`program/portfolio-schema.md`](program/portfolio-schema.md) |
| proof dossiers | [`../solutions/`](../solutions/) |
| the shared calibration and adversarial battery | [`instances.md`](instances.md) |
| search checkpoints, including dead ends | [`explorations/`](explorations/) |
| independent reviews | [`reviews/`](reviews/) |
| numerical artifacts | [`runs/`](runs/) |
| byte-preserved sources of migrated numerical artifacts | [`legacy-runs/`](legacy-runs/) |

The ledger uses `depends_on` for facts a proof used, `assumes` for antecedents that govern
applicability rather than truth, `bounded_by` for proved obstructions, and `heuristic_barriers`
for unproved ones.

There is no separate registry of reusable lemmas and no mutable route or gating document. A
finding reusable enough to be cited elsewhere earns a ledger node and a manuscript statement; a
statement not yet stable enough for that is a `cand:` in the checkpoint that proposed it.

## Contribution flow

1. Read [`program/brief.md`](program/brief.md), then select a route from
   [`program/portfolio.yaml`](program/portfolio.yaml) or a node from the ledger.
2. Read that node's manuscript statement, dependencies, and barriers before spending work.
3. Record the attempt in a new dated checkpoint under [`explorations/`](explorations/), including
   dead ends; put numerical work through the `numerics` harness.
4. Send accepted statement and ledger changes through the orchestrator; return a
   `portfolio_delta` rather than editing the portfolio.
5. For a proof, supply a standalone dossier and an independent review.

## Verify

```bash
python3 scripts/check.py            # every lane
python3 scripts/check.py ready      # can a sustained search start here?
python3 scripts/check.py status     # the unresolved frontier
python3 scripts/check.py portfolio  # what the search is doing
python3 scripts/check.py node conj:kls
python3 -m unittest discover -s scripts/tests -p 'test_*.py'
```

The checker validates repository structure, not mathematical correctness
(`CLAUDE.md` constraint 4). The contribution rules are in [`../CLAUDE.md`](../CLAUDE.md).
