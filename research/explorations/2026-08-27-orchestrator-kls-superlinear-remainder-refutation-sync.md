---
type: exploration
date: "2026-08-27"
outcome: directional
nodes:
  - prop:spectator-excess-rate-obstruction
---
# KLS superlinear excess-remainder refutation sync

Date: 2026-08-27

Role: orchestrator

## Certification

The standalone dossier `solutions/prop-spectator-excess-rate-obstruction.tex`, at reviewed
SHA-256 `b4bf91df9433ce54deb1d025fca4d3e9f978d0e0d3ec818f0d4cdcd986b334be`, passed the
independent review
`research/reviews/2026-08-27-prop-spectator-excess-rate-obstruction-proof-review.md`.

For every proposed $C,T_0,\gamma>0$, every $\eta\in(0,1/2)$, and every $\delta>0$, the proof
constructs a balanced cylinder in an isotropic product of centered one-sided exponentials with
additive and relative initial excess at most $\delta$ and a time $T\le T_0$ such that

$$
\mathbb E\int_0^{T\wedge\tau_\eta}e_t(E)\,dt
>C\bigl(Te_0(E)+T^{1+\gamma}\bigr).
$$

The proof pins an explicit lower-bound constant $(1-e^{-1/2})/128$ and respects the required
base-before-$T$-before-number-of-spectators quantifier order.

## Status and route consequence

`prop:spectator-excess-rate-obstruction` is promoted from `open` to `proved` with its dossier and
review provenance. This node is distinct from the already certified global-weight obstruction.
Together they show that repairing the literal near-Cheeger package requires changing two
independent design choices:

1. the global covariance operator norm must be replaced by a cut-local or tensor-stable scale;
2. the uniform superlinear source-vanishing remainder must be replaced by an $O(T)$ supply, a
   genuinely cut-local source-deficit remainder, or an explicit near-worst-measure premise.

The proposition does not refute the unconditional $O(T)$ upper bound, the externally anchored
near-worst bootstrap, or KLS. Its witnesses are product measures. It also proves no implication
inside the trace-upgrade cluster.

The orchestrator synchronized this interpretation in the ledger, active gates, route
orientation, and the weighted/excess/open-target manuscript modules. The literal conditional
theorem `thm:intro-weighted` remains conditional and visible as an audit trail.
