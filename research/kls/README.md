# research/kls/ — the KLS control plane (Part III)

The control plane for the Kannan–Lovász–Simonovits conjecture — Part III of the unified
document (`modules/kls/`). Unlike the A-series, Part III is **exploratory**: more than one
attack on KLS may exist, so this plane is organized around *routes* rather than a single fixed
program. An agent who suspects a different route is better should **open a new route**, not
edit the existing one's DAG.

## Layout

```
routes.md      the route REGISTRY (one row per attack; how to open a new one)
shared/        route-AGNOSTIC truth — binds every route
  target.md      the KLS statement, h* definition, and the bridge to Part II (ab/conj:a1-bis)
  lower-bounds.md  the universal sound lower bound + clearly route-scoped refuted forms
routes/
  eldan-localization/   Eldan stochastic localization (sub-routes A/B; owns current ledger)
    ledger.yaml obstructions.yaml obstructions.md open-problems.md roadmap.md README.md
  moment-map-spectral/  prose-only moment-map / fixed-eigenfunction localization route
```

Start at [`routes.md`](routes.md) for the map; read [`shared/`](shared/) for the target and the
scope of each constraint; then choose the cut-localization or moment-map/fixed-eigenfunction
route. The current cross-route decision and completed first research cycle are summarized in
[`2026-08-20-kls-program-cycle-1.md`](../explorations/2026-08-20-kls-program-cycle-1.md).

## Why this is separate from the A-series

KLS is a **different epistemic phase** from the A1–A5 open targets (`../ledger.yaml`,
`program: ab`):

| | A-series (`../`) | KLS (here) |
|---|---|---|
| phase | **refine** statements, then prove | already **proof** routes |
| status vocab | open → conjectured → proved | proved / conditional / open / heuristic / refuted / imported |
| numerics | `finum` refines/refutes a *statement* | refine a *sub-statement* **and** gate/refute a *route* (`finum`) |
| obstructions | statement-shape constraints (light) | route-agnostic facts (`shared/`) **+** machine-enforced mechanism no-gos (per route) |

A route keeps the heavier machinery it needs — the `mechanism`/`forbids` vocabulary in its
`obstructions.yaml` and the no-go clearance discipline — which the A-series defers. Both
programs share one checker (`../check_ledger.py`, program-aware) and the same edge/status
grammar where they overlap.

## The bridge to the A-series

`thm:intro-all-cut` and `thm:intro-weighted` carry `bridges: [ab/conj:a1-bis]`. A1-bis is the
**structured-posterior** form $C_P\le K\,\lambda_{\max}(\mathrm{Cov})$ for GLM posteriors; the
*same* bound for **every** isotropic log-concave measure, $K$ universal, **is** KLS — Part I's
"Tier-$\infty$" boundary. That single edge is the spine connecting Parts I/II to Part III.
Details in [`shared/target.md`](shared/target.md).

## One `kls` ledger for now (deferred limitation)

Only one route carries a `ledger.yaml` today (`eldan-localization`). `check_ledger.py` now rejects
a duplicate `meta.program: kls` ledger explicitly; new routes stay prose-only until the checker
is extended with deliberate merge and obstruction-union semantics. See
[`routes.md`](routes.md#limitation-one-kls-ledger-for-now-deferred).

## Verify

```bash
python3 research/check_ledger.py        # validates BOTH ledgers (ab + kls) + bridges + no-go
```
