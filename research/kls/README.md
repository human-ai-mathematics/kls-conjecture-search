# research/kls/ — the KLS control plane (Part III)

The control plane for the Kannan–Lovász–Simonovits conjecture — Part III of the unified
document (`modules/kls/`, grouped as: `00-orientation` = Group 0; `01-…`–`05-family-transport` =
Group 1, the literature survey; `1x-*` = Group 2, shared machinery; `2x-*` = Group 3, Route E;
`30-spectral-route` = Group 4, Route S; `40-`/`41-`/`42-` = Group 5, Route C; `50-synthesis` =
Group 6). Unlike the A-series, Part III is **exploratory**: more than one
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
  moment-map-cmh/       deterministic moment-map route, TWO layers:
                          construction  = Haar/Schur--Piola/commutator (modules/kls/40-*)
                          normalization = CMH definition, endpoint reduction, Hodge splitting,
                                          gate zero, exact classes (modules/kls/41-*, 42-*)
```

Start at [`strategy-map.md`](strategy-map.md), read [`shared/`](shared/) for the target and the
scope of each constraint, and then choose a route from [`routes.md`](routes.md). The August 20
fixed-eigenfunction cycle remains historical context. The cross-route synthesis is
[`2026-08-24-kls-moment-map-cmh-consolidation.md`](../explorations/2026-08-24-kls-moment-map-cmh-consolidation.md);
the Route C normalization layer and its triage of an adjacent directional-quotient exploration are
[`2026-08-25-kls-cmh-normalization-layer.md`](../explorations/2026-08-25-kls-cmh-normalization-layer.md)
and
[`2026-08-25-kls-directional-quotient-triage.md`](../explorations/2026-08-25-kls-directional-quotient-triage.md).

**One thing to internalize before working on Route C.** Its headline $\mathrm{CMH}(4)$ is a
sufficient condition for KLS on the regular moment-map class, not a proved reformulation of the
conjecture. `prop:cmh-hodge` exhibits an additional nonnegative solenoidal channel, but no
separating log-concave measure is known, so strict non-implication is open. Three questions isolate
the remaining risks: approximation closure (`q:cmh-approximation`), gate zero (`q:gate-zero`),
and the solenoidal perturbation test (`q:cmh-solenoidal-perturbation`).

## Why this is separate from the A-series

KLS is a **different epistemic phase** from the A1–A5 open targets (`../ledger.yaml`,
`program: ab`):

| | A-series (`../`) | KLS (here) |
|---|---|---|
| phase | **refine** statements, then prove | already **proof** routes |
| status vocab | open (unresolved) / proved / refuted / imported | proved / defined / conditional / open / heuristic / refuted / imported |
| numerics | `finum` guides refinement and searches for failure modes | guide a *sub-statement* and stress a *route* (`finum`); never validate either |
| obstructions | statement-shape constraints (light) | route-agnostic facts (`shared/`) **+** machine-enforced mechanism no-gos (per route) |

The original Eldan route uses heavier machinery — the `mechanism`/`forbids` vocabulary in the
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
non-Eldan nodes carry an explicit `route:` tag, while nodes predating route metadata default to the
Eldan fixed-cut program; this default is recorded in ledger metadata. The checker rejects a second
`meta.program: kls` ledger, keeping dependency and obstruction semantics unambiguous and
preserving the single-writer rule. A new route may start as a brief, but once it sharpens a target
it adds that target to this central graph through the orchestrator.

Every `proved` KLS node now carries a standalone `solution:` dossier and certified `checked_by`
metadata. The 34 formerly inline Eldan proofs were regrouped into six dependency-coherent
dossiers and passed three independent agent reviews on 2026-08-25; claims that were actually a
definition, published imports, an open target, or heuristic diagnostics were reclassified instead
of being grandfathered. There is no historical proof exception.

Every future `proved` node, CMH or otherwise, must likewise carry a matching dossier and
certification. Agent certification additionally requires a distinct `reviewed_by` and an
unqualified persisted report under `../reviews/`. The checker validates the artifacts; the
orchestrator must still reconcile the mathematical scope and content of every verdict.

## Verify

```bash
python3 research/check_ledger.py        # validates BOTH ledgers (ab + kls) + bridges + no-go
```
