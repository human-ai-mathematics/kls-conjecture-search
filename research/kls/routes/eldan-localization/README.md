# Route: Eldan stochastic localization

The detailed fixed-cut attack on KLS, ported from the standalone KLS program's roadmap and
re-synced to `modules/kls/`.
This is **one route** among possible attacks (see [`../../routes.md`](../../routes.md)); the
route-agnostic facts it must respect live in [`../../shared/`](../../shared/).

- **Thesis.** Follow the posterior evolution of a fixed candidate cut $E$ under Eldan
  stochastic localization. The mass $p_t=\mu_t(E)$ is a martingale; KLS follows if a balanced
  cut **cannot be identified too fast** by the early Gaussian observation. Proof posture
  throughout: **by contradiction against a near-worst measure** $h_\mu\le(1+\varepsilon)\,h^\star_n$.
- **Status.** Live. Proved backbone in place; two conditional headline implications
  (`thm:intro-all-cut`, `thm:intro-weighted`) with open inputs. Letwin's July 2026 version-1
  preprint closes the intrinsic QCTS input and extends the fixed-time covariance-moment window
  to $c/\log n$, but leaves the universal-time alignment problem open.

## Files

```
open-problems.md   the P1–P7 dispatchable briefs
roadmap.md         the narrative map (Eldan-A/B, R2-certified backbone, the dichotomy prize)
```

The route-spanning checker state is now centralized at [`../../ledger.yaml`](../../ledger.yaml),
with the machine fences at [`../../obstructions.md`](../../obstructions.md) and
[`../../obstructions.yaml`](../../obstructions.yaml). Those obstruction mechanisms remain scoped
to this fixed-cut route. This directory owns only its narrative roadmap and dispatchable briefs;
all ledger writes still flow through the single orchestrator.

## Two subroutes (within localization)

- **Eldan-A — all-cut stochastic.** Prove `ass:all-cut-carleson` (absorptive two-color
  Carleson for every balanced cut) ⇒ KLS via `thm:intro-all-cut`. Gap: the
  **operator-to-trace upgrade** `q:upgrade` (lift `cor:per-direction` from quadratic-form to
  trace scale). Bounded by `obs:proj-ceiling`, `obs:two-tail`.
- **Eldan-B — near-Cheeger geometric (weighted).** Prove `ass:weighted-package` ⇒ KLS via
  `thm:intro-weighted`. Two open inputs: weighted excess propagation `q:weighted` and weighted
  stable Stein trace `q:stein-weighted`. The two-tail model calibrates exponent $5/2$ as the
  minimum pure covariance power for an absolute-excess term in this slice-wise package; this is
  not a route-agnostic necessity. The Jacobi/Reilly proposal additionally lacks the foundational
  almost-stability trace bridge recorded in `rem:almost-stability-gap`.

See `roadmap.md` for the full dependency graph and `open-problems.md` for the dispatchable
briefs.

## Numerics

`finum.localization` (`finum run --target kls-loc`) is currently a diagnostic engine only. It
does not compute `q:taming`, the incident-high `q:alignment` source, weighted excess, or the Stein
trace, so it emits `no-verdict` even when its calibration gates pass. The separate
`finum run --target kls-align` target does compute the full alignment margin for the designated
Laplace-product tail union. Its held-out run through $n=1024$ is non-refuting but remains a
dirty, finite-family diagnostic with `no-proof/no-route-verdict`. Neither target promotes a node.
