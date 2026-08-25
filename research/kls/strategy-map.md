# KLS strategy map — landscape, routes, and shared bottlenecks

This is the canonical route-level **status** registry for Part III. The **exposition** now lives in
the manuscript: `modules/kls/00-orientation.tex` (Group 0) states the conjecture, the frontier, the
proof architecture, and the covariance-spike obstruction, and
`modules/kls/01-…`–`05-family-transport.tex` (Group 1) survey the five strategy families with
derivations. This file deliberately does **not** restate that mathematics; it records which routes
are live, what each is blocked on, and the epistemic discipline attached to each status word. The
formal claim graph is [`ledger.yaml`](ledger.yaml); dated attempts remain append-only in
`../explorations/`.

## 1. Target and normalization

Route-agnostic statement and the bridge to A1-bis: [`shared/target.md`](shared/target.md).
Manuscript: `\label{conj:kls}` and `\label{eq:hstar-def}` in
`modules/kls/00-orientation.tex`, §"The conjecture". This repository writes $h_n^\star$ for the
worst Cheeger constant and $\Psi_{\mathrm{KLS}}=h^{-1}$ for the inverse scale, avoiding the
convention-dependent symbol $\psi_n$; the manuscript states the convention trap explicitly as
`rem:psi-convention`.

## 2. Frontier as of 24 August 2026

- **Published benchmark.** $h_n^\star\gtrsim(\log n)^{-1/2}$, i.e. $\sup_\mu C_P\lesssim\log n$
  (Klartag, arXiv:2303.14938).
- **Current preprint benchmark.** Conditional on Letwin arXiv:2607.24164v1,
  $h_n^\star\gtrsim(\log n)^{-1/4}$ and $\sup_\mu C_P\lesssim\sqrt{\log n}$.
- **Sharp thin shell / third tensor.** Chen–Klartag arXiv:2607.23307v1:
  $\operatorname{Var}(|X|^2)\le8n$ and $\lVert T_3(X)\rVert_{\mathrm{HS}}^2\le4n$.
- **Sharp homogeneous quadratic chaos.** Letwin: $\operatorname{Var}\langle MX,X\rangle\le
  8\operatorname{tr}(M^2)$ for every constant symmetric $M$. "Homogeneous" matters: the same sharp
  constant is not asserted for arbitrary affine degree-two polynomials.

Only Letwin's paper supplies the announced improvement of the general KLS bound. The two preprints
share the moment-map estimate at $B=I$; neither subsumes the other. Full derivations, the exact
bridge $C_{P,n}\lesssim\kappa_n\sqrt{\log n}$, and the audit of the delicate points are in
`modules/kls/04-family-moment-map.tex`, §"Audit and epistemic status".

## 3. Strategy families

Surveyed with derivations in Group 1 of the manuscript; the table below is the
route-ownership view only.

| family | object followed | established gain | live loss | repository route |
|---|---|---|---|---|
| classical needle localization | one-dimensional needles | reduces many convex-geometric inequalities to 1D | isotropy is global and is not preserved needle by needle | background only |
| stochastic localization, fixed cut | mass and two-color covariance of a candidate bottleneck set | exact martingale/Riccati backbone and conditional KLS implications | high-rank source occupation / operator-to-trace upgrade | [`eldan-localization`](routes/eldan-localization/) |
| stochastic localization, fixed eigenfunction | covariance tensor of a first spectral mode | exact fixed-function SDE and Letwin-whitened tensor control | unwhiten for universal time without losing tensor/covariance alignment | [`moment-map-spectral`](routes/moment-map-spectral/), manuscript `sec:spectral-route` |
| deterministic moment map | Hessian metric, Haar multipliers, Schur fibers, and Stein-kernel residuals | constant-matrix input, exact formal decompositions, positive local principal algebra | lift/domain and all-split audits; leading global square-root commutator target | [`moment-map-cmh`](routes/moment-map-cmh/), construction layer |
| deterministic moment map, normalization | the Stein generator $\operatorname{div}_\mu(H\nabla\cdot)$, its Hodge splitting, and the linear sector | **proved on the regular class**: $C_P^{\mathrm{aff}}\le C_{\mathrm{CMH}}$, with exact formulas on the line, on products, and on every log-concave Dirichlet law | approximation closure and universal $\mathrm{CMH}(4)$ open; Hodge exposes an extra solenoidal channel but does not prove strict non-implication; gate zero is a factor-2 trace upgrade | [`moment-map-cmh`](routes/moment-map-cmh/), normalization layer |
| spectral/Bochner/$H^{-1}$ methods | first eigenspace and derivative energies | improved Lichnerowicz comparison; quadratic-chaos consequences | known comparisons retain a polylogarithmic loss | inputs to the two moment-map routes |
| transport/Föllmer processes | Jacobians or conditional covariance along a transport | alternative representations of functional inequalities | current derivative bounds reuse KLS-scale information or lose alignment | background; no live route yet |

The three live directories are genuinely different. The fixed-eigenfunction route still uses
stochastic localization. The CMH route is a deterministic extension of moment-map geometry from
constant matrix multipliers to test-dependent fields. They should cross-feed, but one must not be
renamed into the other.

**Route C has two layers (25 August 2026).** The construction layer (Haar tree, Schur--Piola,
$[N^{1/2},K_M]$) and the normalization layer (Stein generator, Hodge splitting, gate zero, exact
classes) share the target $\mathrm{CMH}(4)$ and almost no machinery. A result in one does not
transfer to the other, and a reader should start with the normalization layer, which is logically
prior. This is the route's first block of `proved` nodes under the current R2 contract. The Hodge
decomposition records why the headline has extra content beyond the affine Poincar\'e channel;
whether that extra channel produces a genuine separation is an open perturbative problem, not a
proved theorem. Neither the exact-family results nor this risk diagnosis proves KLS on its own.

## 4. How the live bottlenecks relate

The July inputs close the static homogeneous quadratic layer:

```text
constant symmetric multiplier
        |
        +--> fixed cut under Eldan localization
        |      remaining loss: covariance/high-rank occupation in time
        |
        +--> fixed eigenfunction under localization
        |      remaining loss: unwhitening with tensor alignment
        |
        +--> variable multiplier in moment-map coordinates
               remaining loss: [N^{1/2}, K_M] and its full-tree sum
```

All three losses concern promotion of matrix-quadratic information without discarding orientation,
but no theorem in the repository identifies them as equivalent. In particular,
`q:upgrade`, the high-rank part of `q:stein-weighted`, and `q:alignment` form one ownership
cluster because they share an occupation difficulty; `rem:trace-upgrade-unification` explicitly
records that their formal equivalence is still open. The deterministic square-root commutator is
a related, not yet identified, fourth coordinate system.

**Gate zero joins that cluster, and hard constraint 6 applies to it.** In isotropic position
`conj:gate-zero` reads $\lambda_{\max}(\mathbb EH^2)\le4$, while Chen--Klartag already give
$\operatorname{tr}(\mathbb EH^2)\le2n$ — the average eigenvalue is $\le2$. So it is an
operator-to-trace upgrade with a factor-2 budget. `prop:letwin-not-gate-zero` shows the entire gap
is the static commutator $\tfrac12\lVert[B,H]\rVert_{\mathrm{HS}}^2$ and that no amount of matrix
moment information closes it. The verdict splits: **falsifying** gate zero on a model is cheap and
dispatchable (task M10, `finum` target `cmh-gate-zero`); **proving** it is not, and must be routed
to the cluster's owner rather than opened as a parallel effort. No equivalence with `q:upgrade` is
asserted.

## 5. Reading order and epistemic discipline

1. Read [`shared/target.md`](shared/target.md) for the route-agnostic conjecture and bridge to A1-bis.
2. Read this file and [`routes.md`](routes.md) to choose a route.
3. Read the selected route's README and its named open problem.
4. Consult [`obstructions.md`](obstructions.md) only with its stated scope: the current
   machine-enforced mechanisms are Eldan-route fences, not universal no-go theorems.
5. Consult [`gating.md`](gating.md) before making a numerical claim.

The status words are literal:

- **imported** means an external theorem, with version and review status recorded;
- **proved** always means the repository's R2 proof contract is satisfied; the former inline
  Eldan backbone now has standalone dossiers and independent reviews, with no grandfathering;
- **formal identity** in a prose-only derivation means algebraically consistent subject to
  domains/regularity, not a ledger promotion;
- **reported retraction** records a failed idea from independent notes until its witness is
  persisted analytically or through `finum`;
- **open** and **heuristic** never inherit authority from a successful model calculation.
