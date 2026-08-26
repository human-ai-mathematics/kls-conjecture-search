# Route: Eldan stochastic localization

Thesis: follow a fixed balanced cut under stochastic localization and prove that its posterior
mass cannot be identified too quickly. The exact mass-martingale and two-color Riccati backbone is
certified; the universal-time source control is open.

## Two live subroutes

| subroute | conditional endpoint | missing input |
|---|---|---|
| Eldan-A, all cuts | `thm:intro-all-cut` | `q:upgrade`, the operator-to-trace occupation estimate |
| Eldan-B, near-Cheeger cuts | `thm:intro-weighted` | `q:weighted` and `q:stein-weighted` |

The main model residue is `q:alignment`. The unweighted excess bootstrap is proved, but the
weighted covariance/excess interaction and universal-time geometric consumption are not.

The route-specific fences are [`../../obstructions.md`](../../obstructions.md). In particular,
projection/radial data alone,
slice-wise absolute-scale estimates, and crude covariance bootstraps do not close this route.

Work from [`open-problems.md`](open-problems.md). Logical status and dependencies are only in the
central [`../../ledger.yaml`](../../ledger.yaml); the older [`roadmap.md`](roadmap.md) path is a
compatibility pointer.

Numerical implementation status is owned by [`experiments/README.md`](../../../../experiments/README.md).
`kls-loc` is diagnostic, while `kls-align` tests one designated product cut family. Neither
decides a universal ledger node.
