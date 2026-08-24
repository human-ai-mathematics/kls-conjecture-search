# research/kls/ — the KLS control plane (Part III)

The control plane for the Kannan–Lovász–Simonovits conjecture — Part III of the unified
document (`modules/kls/`). Unlike the A-series, Part III is **exploratory**: more than one
attack on KLS may exist, so this plane is organized around *routes* rather than a single fixed
program. An agent who suspects a different route is better should **open a new route** rather
than commandeer an existing one; once sharpened, its targets enter the shared DAG.

## Layout

```
ledger.yaml    one route-spanning KLS claim graph; every write goes through the orchestrator
obstructions.yaml/.md  machine fences, currently scoped to the Eldan fixed-cut route
strategy-map.md        literature frontier, route comparison, and shared bottlenecks
routes.md      the route REGISTRY (one row per attack; how to open a new one)
shared/        route-AGNOSTIC truth — binds every route
  target.md      the KLS statement, h* definition, and the bridge to Part II (ab/conj:a1-bis)
  lower-bounds.md  the universal sound lower bound + clearly route-scoped refuted forms
routes/
  eldan-localization/   Eldan stochastic localization (subroutes Eldan-A/B)
    open-problems.md roadmap.md README.md
  moment-map-spectral/  moment-map / fixed-eigenfunction stochastic route
  moment-map-cmh/       deterministic Haar/Schur--Piola/commutator route
```

Start at [`strategy-map.md`](strategy-map.md), read [`shared/`](shared/) for the target and the
scope of each constraint, and then choose a route from [`routes.md`](routes.md). The August 20
fixed-eigenfunction cycle remains historical context; the current cross-route synthesis is
[`2026-08-24-kls-moment-map-cmh-consolidation.md`](../explorations/2026-08-24-kls-moment-map-cmh-consolidation.md).

## Why this is separate from the A-series

KLS is a **different epistemic phase** from the A1–A5 open targets (`../ledger.yaml`,
`program: ab`):

| | A-series (`../`) | KLS (here) |
|---|---|---|
| phase | **refine** statements, then prove | already **proof** routes |
| status vocab | open → conjectured → proved | proved / conditional / open / heuristic / refuted / imported |
| numerics | `finum` refines/refutes a *statement* | refine a *sub-statement* **and** gate/refute a *route* (`finum`) |
| obstructions | statement-shape constraints (light) | route-agnostic facts (`shared/`) **+** machine-enforced mechanism no-gos (per route) |

The legacy Eldan route uses heavier machinery — the `mechanism`/`forbids` vocabulary in the
colocated KLS `obstructions.yaml` and its no-go clearance discipline — which the A-series
defers. Other routes inherit those fences only when their stated scope applies. Both programs
share one checker (`../check_ledger.py`, program-aware) and the same edge/status grammar where
they overlap.

## The bridge to the A-series

The route-neutral terminal `conj:kls` carries `bridges: [ab/conj:a1-bis]`. A1-bis is the
**structured-posterior** form $C_P\le K\,\lambda_{\max}(\mathrm{Cov})$ for GLM posteriors; the
*same* bound for **every** isotropic log-concave measure, $K$ universal, **is** KLS — Part I's
"Tier-$\infty$" boundary. That single edge is the spine connecting Parts I/II to Part III.
Details in [`shared/target.md`](shared/target.md).

## One route-spanning KLS ledger

The KLS program deliberately has one ledger at [`ledger.yaml`](ledger.yaml). New shared and
non-Eldan nodes carry an explicit `route:` tag, while the untagged legacy nodes default to the Eldan
fixed-cut program; this default is recorded in ledger metadata. The checker rejects a second
`meta.program: kls` ledger, keeping dependency and obstruction semantics unambiguous and
preserving the single-writer rule. A new route may start as a brief, but once it sharpens a target
it adds that target to this central graph through the orchestrator.

The graph also records a legacy certification debt: 41 Eldan nodes marked `proved` have inline
manuscript arguments but predate the current `solutions/` + `checked_by` R2 contract. Their
statuses were preserved rather than silently downgraded or recertified; the August 24 audit
enumerates the limitation. New CMH nodes receive no such grandfathering.

## Verify

```bash
python3 research/check_ledger.py        # validates BOTH ledgers (ab + kls) + bridges + no-go
```
