# Research control plane

`research/` coordinates the KLS program. The manuscript owns accepted statements, the ledger owns
logical state and graph edges, `solutions/` owns standalone proofs, and numerical runs guide
research without certifying claims.

## Program

| program | ledger id | entry point | purpose |
|---|---|---|---|
| KLS | `kls` | [`kls/README.md`](kls/README.md) | compare proof routes and discharge their open inputs |

There is one ledger. All ledger writes pass through one orchestrator.

The structured end of the same problem — explicit functional-inequality constants for Bayesian
posteriors, including the structured-posterior conjecture `conj:a1-bis` — is pursued in the
companion repository `posterior-inequalities-exploration`. The two programs were split out of a
single repository on 2026-09-01; see
[`decisions/2026-09-01-split-a-series-and-kls-repositories.md`](decisions/2026-09-01-split-a-series-and-kls-repositories.md).
The relationship between `conj:kls` and `conj:a1-bis` is a comparison and is recorded only in
prose: `bridges` resolves within one repository, and no node here may depend on a node there.

## Sources of truth

| content | location |
|---|---|
| ledger fields and invariants | [`ledger-schema.md`](ledger-schema.md) |
| accepted mathematical prose | [`../modules/kls/`](../modules/kls/) |
| claim state and logical edges | `kls/ledger.yaml` |
| route status and gating | `kls/routes.md`, `kls/gating.md` |
| proof dossiers | [`../solutions/`](../solutions/) |
| reusable lemmas and shared instances | [`knowledge/`](knowledge/) |
| mathematical attempts and dead ends | [`explorations/`](explorations/) |
| independent reviews | [`reviews/`](reviews/) |
| numerical artifacts | [`runs/`](runs/) |
| harness decisions | [`decisions/`](decisions/) |

The ledger uses `depends_on` for proof dependencies and `bounded_by` for obstruction nodes.

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
