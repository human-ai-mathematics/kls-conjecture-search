---
artifacts:
  - research/runs/2026-08-30T173244.394413Z-fiber-frame-dual.jsonl
---

# Portfolio triage after the Song–Zhang certification

## Question examined

Starting lens: **mine**. With `thm:song-zhang-kls`, `thm:sz-curvature-transfer`,
`cor:sz-affine-poincare` and `prop:sz-exponential-coefficients-equivalence` certified,
what does each non-closed route of the portfolio still buy toward a dimension-free bound
for `conj:kls`? For each one: a verdict, a proposed state, and a discriminating `next` test.
Most routes were last named only in the migration record `2026-09-29-migration-v0.2.0.md`,
which contains no mathematics. Four routes (`ap:c-recovery-envelope`,
`ap:c-uniform-approximants`, `ap:c-invariant-lift`, `ap:c-square-root-commutator`) had
never been named in a checkpoint under their current ids. Their last substantive records
use the v0.1 ids, chiefly `2026-08-27-kls-route-prober-cmh-recovery-envelope-w1c02.md`,
`2026-08-27-synthesizer-kls-first-wave-par-04.md`,
`2026-08-30-synthesizer-screened-kernel-comparison-w4y01.md`,
`2026-08-31-orchestrator-kls-angles-wave-w4.md` and
`2026-09-06-synthesizer-kls-wave-five-w5y01.md`, read here as their predecessors.

There are **18** non-closed routes, not 19. The figure 19 in the migration record counted
`ap:e-weighted-excess`, `ap:s-window-chain` and the routes of that time. The closed
`ap:polynomial-curvature-audit` is not reconsidered. This is triage: no new estimate is
proved, and no ledger status or edge is proposed.

## What we learned

**What the Song–Zhang wave does to the portfolio, in general** (*established* by reading
the certified statements against each route target):

1. *No route target is discharged, and none is weakened.* Every route aims at a statement
   with a universal constant or a universal time. The four certified nodes supply a
   dimension-dependent bound ($16^{\log^*}$) and two interfaces. Brief trap 10 holds route by
   route: no CMH, occupation, trace, frame or seam antecedent appears among the hypotheses
   or conclusions of the four nodes.
2. *No route is converted into an equivalent-strength restatement by
   `prop:sz-exponential-coefficients-equivalence`.* Every route target was already a sufficient
   condition, so it already implies uniform Appell coefficients through `conj:kls`. The
   equivalence only disqualifies a *new* route whose target is the coefficient bound itself
   with no separate mechanism (trap 11).
3. *A longer dimension-dependent covariance window buys nothing on Routes S and E.*
   `prop:spectral-sufficiency` returns $C_P\le2/T_*$ from an occupation window of length
   $T_*$. Feeding it a window derived from a bound $K_n$ therefore returns order $K_n$
   (`prop:mm-window-occupation` is exactly this "frontier reproduction"). The same holds for
   the $c/\log n$ windows of `thm:V2-window`. No route should spend effort turning
   `thm:song-zhang-kls` into a longer window.
4. *`thm:sz-curvature-transfer` is not a route.* It turns any uniform regular curvature
   profile into a general bound, evaluated at curvature $c/\log(en)$. A dimension-free
   result through it needs a profile $F$ bounded as $a\to0$. That is a regular-class KLS
   statement, so it gives no new target. It remains available to `ap:sz-recovery-probe`.

**Per-route triage.** "Kept" means the objective stands as written and only `next` is new.

| route | verdict | proposed state | reason (one or two sentences) | discriminating `next` (short form; exact text in the handoff) |
|---|---|---|---|---|
| `ap:sz-recovery-probe` | kept, unchanged | `active` | It is the only route that works *inside* the certified mechanism. Its current `next` already respects traps 10–11: it calibrates generated symmetry and admits nothing until the recovery estimate and the degree/depth thresholds are paid. | unchanged (coupled potential $W_\delta$) |
| `ap:e-trace-upgrade` | kept; absorbs `ap:e-alignment` and owns the high-rank part of `conj:stein-weighted` (P1 single owner) | `active` | `conj:trace-upgrade` is untouched by the Song–Zhang wave. The cluster's sharpest test is the product-alignment model, and only its prefix form bears on `ass:tight-prefix-carleson` (`rem:product-stress-test`). | decide `conj:product-alignment` in prefix form on the tight window, from time zero, on products of two-sided exponentials |
| `ap:e-alignment` | subsumed by `ap:e-trace-upgrade` | `closed` | Its objective is one model test of the trace-upgrade cluster. Under P1, two routes on one cluster model is the fan-out the rule forbids; the TPC-relevant prefix form becomes the owner's `next`. `conj:product-alignment` stays open. | — |
| `ap:e-screened-supply` | objective restated: its parent `ap:e-weighted-excess` is closed, and the object it pursues is the aligned initial-layer kernel (AIK) of the 2026-08-30 comparison | `active` | It is the only formulation recorded to survive both certified spectator mechanisms (`prop:weighted-spectator-obstruction` and soft-projector injection). `prop:split-screened-supply` is dimension-free only for cuts on boundedly many coordinates, since its budget grows with $k$. | screened supply of a spread halfspace on an $n$-fold product, as a function of $n$ |
| `ap:e-stein-weighted` | subsumed: the "tensor-stable replacement" half by `ap:e-screened-supply`, and the high-rank trace half by the P1 owner `ap:e-trace-upgrade` | `closed` | In its stated global-weight form, `conj:stein-weighted` pairs with a supply whose $O(T)$ rate form is the refuted `conj:weighted-excess-rate`. By `rem:product-stress-test` it "yields nothing toward KLS until a propagation statement that survives such products is formulated", and that statement is the screened route's object. `conj:stein-weighted` and `conj:almost-stability-gap` stay open nodes. | — |
| `ap:e-taming-splitting` | kept | `active` | `cor:dichotomy` is certified with `ass:absolute-geometric-completion` in `assumes`, and the matched-time covariance estimate is still missing (`2026-10-01-wrap-up-cor-dichotomy.md`). No certified result touches near-worst structure. | non-quantitative rigidity half of `conj:splitting` in dimension two |
| `ap:s-occupation` | kept | `active` | `conj:mm-spectral-occupation` needs a universal $T_0$, and item 3 above rules out the Song–Zhang window as a substitute. The residue is the post-spike charge beyond the operator-norm window of `thm:KL-window`. | mine where the operator-norm stopping enters the window-occupation proof, and whether a universal-time stopping can replace it (products as the calibration, see the observation below) |
| `ap:c-recovery-envelope` | objective restated: the linear-sector estimate along the chosen sequence is the first stage; absorbs `ap:c-uniform-approximants` | `active` | `ass:cmh-recovery-envelope` is the weakest CMH premise that closes the target through `cor:cmh-recovery-sequence-suffices`. `conj:gate-zero` already implies its first stage on *every* sequence. Its only resource beyond gate zero is the freedom to choose the sequence, and that freedom is untested. | test whether the choice of recovery sequence can change $\liminf Q_{\rm lin}$ on the exponential cube cone |
| `ap:c-uniform-approximants` | subsumed by `ap:c-recovery-envelope` | `closed` | Its own objective says it is a strictly stronger premise that is not needed once the envelope is discharged. No checkpoint records a mechanism that is easier for the stronger statement. `ass:uniform-cmh-approximants` stays open. | — |
| `ap:c-anisotropic-bootstrap` | kept; a distinct mechanism for the linear sector | `active` | $(\mathrm{AB})_{\rho,\beta}$ bounds $Q_{\rm lin}$ by $(1+\beta)/\rho$, and any proof must consume the Monge–Ampère reservoir $\mathsf R_A$ (2026-08-30 records). It was never tested on the exponential cones, which are the non-product equality cases of `conj:gate-zero-sharp`. | sharp reservoir inequality $\mathsf R\succeq\mathsf N/2$ on the exponential-cone battery at $\beta=n$ |
| `ap:c-invariant-lift` | kept as objective; sequenced after the linear sector | `blocked` on `conj:gate-zero` | `conj:mm-invariant-lift` is one step of a constructive proof of $\mathrm{CMH}(4)$. Gate zero is its cheapest necessary consequence. The first-wave synthesis already ordered the CMH construction "blocked first by the genuine-Hessian static commutator/linear sector". A refutation of `conj:gate-zero` closes the route. | on reopening, specialize the lift to linear tests against `lem:linear-sector-third-moment` |
| `ap:c-square-root-commutator` | sub-route, downstream | `blocked` on `conj:mm-invariant-lift` | The complete-Haar commutator estimate is defined on the retained squares of the invariant lift. Without that lift it has no fixed right-hand side. | on reopening, depth-two Haar tree at the product saturator |
| `ap:c-solenoidal-perturbation` | kept | `active` | `conj:cmh-second-variation` is the cheapest kill test of $\mathrm{CMH}(4)$, and the base direction is spent (wave-five synthesis). The Galerkin quotient at the saturator is $4-\pi^2/(d+1)^2+O(d^{-4})$ (`cand:cmh-exponential-galerkin-rate`), so a fixed-degree second variation means something only beside that deficit. | second variation of the degree-$d$ Galerkin quotient under two-sided admissible radial Gamma-factor perturbations, $d=1..4$, compared with the deficit |
| `ap:c-gate-zero` | kept | `active` | The certified linear-sector tools and the exact cone battery are unchanged. The cheapest promotion is still `cand:cone-transverse-equality-simplex`, a finite algebra problem through the Dirichlet closed forms of `thm:cmh-dirichlet` (wave-five synthesis). | decide `cand:cone-transverse-equality-simplex` by exact algebra |
| `ap:f-frame-construction` | kept | `active` | The Song–Zhang wave says nothing about frames: Appell estimates are not fiber estimates. The only certified obstruction, `prop:conditional-fiber-root-obstruction`, is for the root frame. | do the vertex-cap tests also kill the vertex frame's full $L^2$ gap? |
| `ap:f-simplex-dual` | kept; complementary to `ap:f-frame-construction` on the same quantity, not a duplicate | `active` | `lem:fiber-root-degree-two` rules out degree-two refuters; degree three is the first open degree. | exact all-frame $\Lambda_{m,3}$, $m\le8$, with a preregistered decay criterion |
| `ap:cone-boundary-gap` | kept, parked | `blocked` on `cand:cone-seam-capacity` | Untouched by the Song–Zhang wave. Saturation is not inferred from the five waves without work; the candidate is live and precise. | facet-mean graph Poincaré constant on the isotropic cube and regular simplex |
| `ap:laplace-brenier-simplex` | kept, parked | `blocked` on `cand:brenier-simplex-hessian` | Untouched by the Song–Zhang wave. Its pre-registration gate (37) of the 2026-08-27 probe is unresolved. | directional Lipschitz growth of the semi-discrete optimal map in the Helmert frame, $d=2..6$ |

**Duplicates and overlaps found.**

- `ap:e-trace-upgrade` / `ap:e-alignment` / the high-rank part of `ap:e-stein-weighted`:
  one P1 cluster. The proposal resolves it with one owner (`ap:e-trace-upgrade`).
- `ap:e-stein-weighted` (specification half) = `ap:e-screened-supply`. Both pursue the
  tensor-stable replacement of `ass:weighted-package`.
- `ap:c-uniform-approximants` ⊂ `ap:c-recovery-envelope` (stronger premise, same consumer).
- `ap:c-gate-zero`, `ap:c-anisotropic-bootstrap` and the first stage of
  `ap:c-recovery-envelope` all bound the linear-sector quotient $Q_{\rm lin}$. These are
  distinct mechanisms on one quantity, recorded as overlaps (as at the migration), not merged.
  `conj:gate-zero` implies the recovery-envelope stage outright.
- `ap:c-square-root-commutator` is downstream of `ap:c-invariant-lift`. Both are downstream
  of the linear sector.
- `ap:c-solenoidal-perturbation` and `ap:c-gate-zero` share the cone battery as an
  instrument, not a target.
- `ap:f-frame-construction` and `ap:f-simplex-dual` are the two directions of one
  quantity on the simplex. Keep both, but schedule them together: each `next` names the
  other's frame.
- `ap:sz-recovery-probe` and `ap:s-occupation` both work from a first eigenfunction. They
  are not duplicates: one is deterministic polynomial recovery, the other a stochastic
  source integral, and no implication between them is recorded.

**Observation supporting the `ap:s-occupation` test** (*established*, elementary; not
certified). Let $\mu=\nu^{\otimes n}$ be a product of a regular one-dimensional law $\nu$.
Let $f=n^{-1/2}\sum_i\varphi(x_i)$, where $\varphi$ is a normalized first eigenfunction of
$\nu$; $f$ is a first eigenfunction of $\mu$. Linear tilts preserve products, so the
localization $\mu_t$ is a product of $n$ independent, identically distributed
one-dimensional localizations. By independence and centering,
$H_t=n^{-1/2}\operatorname{diag}(h_i(t))$ and
$g_t=n^{-1/2}(c_i(t))_i$. Hence $\|H_t\|_{\mathrm{HS}}^2$, $|g_t|^2$ and
$g_t^TA_tg_t$ are averages of $n$ i.i.d. one-dimensional terms. Every expectation in
`eq:spectral-occupation` therefore equals its value for $n=1$. Meanwhile, for two-sided exponential factors, $\|A_t\|_{\rm op}$
reaches order $\log n$ at fixed times (`rem:product-stress-test`). So products cannot falsify
`conj:mm-spectral-occupation` with this eigenfunction. They do separate the true source
from any operator-norm majorant, which makes them the right calibration for replacing the
operator-norm stopping.

**Observed** (`research/runs/2026-08-30T173244.394413Z-fiber-frame-dual.jsonl`). The
degree-three quotients of the root and vertex frames decrease over $m=3..8$, the vertex
frame from about $0.76$ to $0.34$ and the root frame from about $0.57$ to $0.21$. At degree
two the root values approach the certified floor $(m+2)(m+3)/(5m^2)$. These are per-frame
upper bounds on restricted subspaces: directional only, and not $\Lambda_{m,3}$ itself.

## What resists

- Every route still faces the obstacle its own records name: AIK and the zero-damping
  two-tail core (`ap:e-screened-supply`, `ap:e-trace-upgrade`); the matched-time estimate
  and `ass:absolute-geometric-completion` (`ap:e-taming-splitting`); universal-time
  occupation beyond the operator-norm window (`ap:s-occupation`); the genuine-Hessian
  linear sector `conj:gate-zero` (all C routes); a frame with a universal gap
  (`conj:conditional-fiber-frame`); `cand:cone-seam-capacity`; and
  `cand:brenier-simplex-hessian`. The Song–Zhang wave removed none of them.
- Two routes rest on a near-worst premise ($h_\mu\le(1+\varepsilon)h^*_n$):
  `ap:e-taming-splitting` (through `conj:taming` and `ass:absolute-geometric-completion`)
  and the AIK class of `ap:e-screened-supply`. No explicit instance can be certified
  near-worst, so their tests must be analytic or must drop the premise, as the proposed
  `next` tests do.
- `ap:c-invariant-lift` is blocked on a conjecture that is itself a route target
  (`ap:c-gate-zero`). The reopen rule then runs one way only: a proof of `conj:gate-zero`
  reopens the lift, while a refutation closes it together with every $\mathrm{CMH}(4)$ route.

## Proposed next step

The orchestrator applies the route deltas of the handoff. They make three closures by
subsumption, two restatements, two new blocks, two parked routes kept blocked, and a `next`
on every route that stays active or blocked. The proposed launch order, cheapest decisive
first:

1. `ap:c-gate-zero` — `cand:cone-transverse-equality-simplex` by algebra. This is a
   promotion or a retirement either way.
2. `ap:f-simplex-dual` — exact $\Lambda_{m,3}$. A decaying floor is the first concrete
   threat to `conj:conditional-fiber-frame`.
3. `ap:e-screened-supply` — spread-halfspace screened supply. It decides whether the
   screen buys coordinate-complexity stability.
4. `ap:sz-recovery-probe` — its existing `next`.

Every other route's `next` is ready when capacity allows. None of them is a reason to
reopen the closed `ap:polynomial-curvature-audit`.
