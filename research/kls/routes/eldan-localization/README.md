# Route: Eldan stochastic localization

The current attack on KLS, ported from the standalone KLS program's roadmap and re-synced to `modules/kls/`.
This is **one route** among possible attacks (see [`../../routes.md`](../../routes.md)); the
route-agnostic facts it must respect live in [`../../shared/`](../../shared/).

- **Thesis.** Follow the posterior evolution of a fixed candidate cut $E$ under Eldan
  stochastic localization. The mass $p_t=\mu_t(E)$ is a martingale; KLS follows if a balanced
  cut **cannot be identified too fast** by the early Gaussian observation. Proof posture
  throughout: **by contradiction against a near-worst measure** $h_\mu\le(1+\varepsilon)\,h^\star_n$.
- **Status.** Live. Proved backbone in place; two conditional headline implications
  (`thm:intro-all-cut`, `thm:intro-weighted`) with open inputs.

## Files

```
ledger.yaml        canonical logical state + dependency DAG (file: paths → modules/kls/*.tex)
obstructions.yaml  machine-readable no-go set (mechanism vocabulary + forbids)
obstructions.md    the no-go prose (kept in parity with the YAML)
open-problems.md   the P1–P7 dispatchable briefs
roadmap.md         the narrative map (sub-routes A/B, the proved backbone, the dichotomy prize)
```

The checker (`../../../check_ledger.py`) loads `ledger.yaml` here (program `kls`) and its
sibling `obstructions.{yaml,md}`. This is the **only** `kls` ledger today — see
[`../../routes.md`](../../routes.md) for why a second route stays prose-only for now.

## Two sub-routes (within localization)

- **Route A — all-cut stochastic.** Prove `ass:all-cut-carleson` (absorptive two-color
  Carleson for every balanced cut) ⇒ KLS via `thm:intro-all-cut`. Gap: the
  **operator-to-trace upgrade** `q:upgrade` (lift `cor:per-direction` from quadratic-form to
  trace scale). Bounded by `obs:proj-ceiling`, `obs:two-tail`.
- **Route B — near-Cheeger geometric (weighted).** Prove `ass:weighted-package` ⇒ KLS via
  `thm:intro-weighted`. Two open inputs: weighted excess propagation `q:weighted` and weighted
  stable Stein trace `q:stein-weighted`. The weight $(1+\lVert A\rVert)^{5/2}$ is *forced*
  (`obs:two-tail`), not chosen.

See `roadmap.md` for the full dependency graph and `open-problems.md` for the dispatchable
briefs.

## Numerics

`finum.localization` (`finum run --target kls-loc`) — the stochastic-localization engine
(`experiments/finum/localization/`). Refutes / gives
direction on a proof input behind passing gates; never promotes a node — the same role `finum`
plays for the A-series.
