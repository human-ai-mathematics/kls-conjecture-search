# research/ — federated research control plane

This directory coordinates two mathematical programs under one soundness contract and one
structural checker. The manuscript in `../modules/` owns accepted mathematical prose; the
ledgers own claim state and logical edges; `../solutions/` owns independently reviewable proofs.
Numerical artifacts guide research but never certify claims or proofs.

## Programs

The programs are peers. Each has exactly one ledger and its own workflow documentation.

| program | machine id | phase | entry point |
|---|---|---|---|
| A-series (A1--A5, Parts I/II) | `ab` | refine statements, then prove | [`a-series/README.md`](a-series/README.md) |
| KLS (Part III) | `kls` | compare proof routes and discharge assumptions | [`kls/README.md`](kls/README.md) |

The stable machine id `ab` is retained for ledger policy and cross-program bridge references;
the human-facing directory name is `a-series`.

```text
research/
  a-series/       A1--A5 ledger, obstruction prose, schema, and target briefs
  kls/            route-spanning KLS ledger, route registry, and mechanism fences
  knowledge/      reusable analytic tools and the curated A/KLS instance battery
  explorations/   append-only mathematical attempt history, including dead ends
  reviews/        persisted proof-review and non-certifying audit reports
  runs/           provenance-stamped finum artifacts
  decisions/      append-only control-plane and harness decisions
  check_ledger.py shared R0 checker
  tests/          checker regression suite
```

Program-owned material belongs under the corresponding program directory. Root-level planes
exist only when they are intentionally shared across programs or form one repository-wide
archive. Historical explorations, reviews, and runs retain their paths so proof and diagnostic
provenance does not churn during organizational refactors.

## Common graph and status contract

Both ledgers use `depends_on` for premises actually used in a proof, `bounded_by` for applicable
obstructions, and `bridges` for explicit cross-program links written as `program/id`. A program
has exactly one ledger; all ledger writes pass through the singleton orchestrator.

- A-series statuses: `open`, `proved`, `imported`, `refuted`.
- KLS statuses: `proved`, `defined`, `conditional`, `open`, `heuristic`, `refuted`, `imported`.
- Numerical evidence: `none` or `numerical-directional`, orthogonal to logical status.

The A1-bis/KLS bridge connects `ab/conj:a1-bis` to `kls/conj:kls`. It is a bridge between a
structured-posterior claim and its universal log-concave boundary, not a proof dependency.

## Shared planes

- [`knowledge/`](knowledge/) is the curated cross-target battery and reusable analytic memory.
- [`explorations/`](explorations/) records mathematical attempts, including failures, without
  rewriting history.
- [`reviews/`](reviews/) stores structured proof provenance and non-certifying audits.
- [`runs/`](runs/) stores immutable, provenance-stamped numerical diagnostics.
- [`decisions/`](decisions/) records harness, schema, and repository-organization decisions.

The proof output plane remains the repository-root sibling [`../solutions/`](../solutions/).
Every `proved` node points to a certified standalone dossier. Sampled, MCMC, FEM, floating-point,
and finite-grid outcomes never supply proof certification.

## Verify

```bash
python3 research/check_ledger.py
python3 -m unittest discover -s research/tests -p 'test_*.py'
```

The checker validates structure, not mathematical correctness. Independent criticism remains
necessary to compare ledger statements, manuscript labels, dossiers, and obstructions
semantically. The normative contribution rules are in [`../CLAUDE.md`](../CLAUDE.md).
