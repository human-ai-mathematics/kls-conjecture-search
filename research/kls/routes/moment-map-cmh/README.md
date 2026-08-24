# Route: deterministic moment map, Haar aggregation, and CMH

Status: **live, tracked but unproved**. This route is represented in the central
[`../../ledger.yaml`](../../ledger.yaml); it has no proved internal node and makes no claim to
have proved KLS.

## Thesis

Chen--Klartag control the trace direction $B=I$, while Letwin controls the moment-map Hessian
against every **constant symmetric matrix** $B$. The proposed extension is to allow the
multiplier to depend on the test function, decompose that field through a full Haar tree, and pay
for the resulting noncommutation with positive Monge--Ampère and variable-multiplier squares
extending that constant input. If this can be done dimension-freely, an appropriate
covariance--moment--Hessian estimate (abbreviated CMH) is intended to imply a universal Poincaré
bound.

The route is deterministic: its principal objects are the moment-map Hessian metric, weighted
elliptic operators, Schur fibers, Stein-kernel residuals, and square-root commutators. It is not
the older [`moment-map-spectral`](../moment-map-spectral/) route, which follows a fixed first
eigenfunction under stochastic localization.

## Current diagnosis

The originating exploration reports counterexamples to several simplifying narratives; their
repository dossiers are still pending:

- individual Haar nodes need not have nonnegative deficit;
- descendant slack cannot be allocated by a fixed fraction at every split;
- the conformal mode cannot be isolated from traceless and corrector terms;
- a guessed local vector conservation law is false;
- the cubic commutator symbol does not vanish in general.

The displayed fixed-target $1+2$ principal algebra has been independently expanded and is
positive, and the Schur--Piola calculation shows that the apparent scalar conformal derivative is
constrained by fiber transport. The best identified analytic bottleneck is global and
noncommutative: control $[N^{1/2},K_M]$ after summing the complete Haar tree and retaining all
positive Letwin, Codazzi, and Monge--Ampère squares. Calling it the *only* remaining obstruction
would be premature: the invariant lift, operator domains, and a dimension-free reduction from
higher-dimensional splits to controlled irreducible pieces are still open.

That diagnosis is promising, not a theorem. In particular, the originating consolidated notes
do not yet freeze every operator domain, the exact definition of the symbol $\Sigma$ in the
headline CMH inequality, or the complete retained remainder. Those are the first formal tasks,
not cosmetic details.

## Route chain

```text
external moment-map matrix bounds
        |
        v
define CMH and prove CMH => KLS with all domains fixed
        |
        v
Haar/Bessel aggregation + one-edge Schur/Hodge decomposition
        |
        v
local invariant multiplier algebra + positive global reservoirs
        |
        v
dimension-free square-root commutator inequality
        |
        v
full-tree summation => CMH
```

Every non-external arrow in this chain remains uncertified. Several middle identities are formal
and algebraically consistent, but the invariant lift, Hodge/one-edge domains, all-split reduction,
resolvent bound, and full-tree closure are open; none has been promoted to `proved` under the
repository's R2 contract.

## Files

- [`claims.md`](claims.md): normalized formulas and an epistemic audit of every major claim.
- [`open-problems.md`](open-problems.md): dispatchable proof tasks and their acceptance gates.
- [`models.md`](models.md): regression models, what each detects, and what it cannot decide.
- [`../../strategy-map.md`](../../strategy-map.md): comparison with the other KLS strategies.
- [`../../../explorations/2026-08-24-kls-moment-map-cmh-consolidation.md`](../../../explorations/2026-08-24-kls-moment-map-cmh-consolidation.md): dated consolidation and audit record.

## Promotion gate

No structural identity from the independent summary becomes a proved ledger node merely by being
copied here. Promotion requires:

1. a fully quantified statement with conventions and domains;
2. a standalone dossier in `solutions/`;
3. an independent reviewer and persisted report;
4. matching ledger metadata; and
5. a green `python3 research/check_ledger.py` run.

Regression calculations may refute or guide the route. Sampled/FEM calculations must flow through
`finum`; exact finite-dimensional algebra may be recorded analytically. Neither is a substitute
for the commutator proof.
