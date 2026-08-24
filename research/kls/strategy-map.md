# KLS strategy map — landscape, routes, and shared bottlenecks

This is the canonical route-level orientation for Part III. It separates established literature,
repository-certified reductions, live conjectural routes, and historical dead ends. The formal
claim graph is [`ledger.yaml`](ledger.yaml); detailed mathematics lives in `modules/kls/`; dated
attempts remain append-only in `../explorations/`.

## 1. Target and normalization

For an isotropic log-concave probability measure $\mu$ on $\mathbb R^n$, KLS asks for a
universal $C$ such that

$$
\operatorname{Var}_\mu(f)\le C\int |\nabla f|^2\,d\mu
$$

for every locally Lipschitz $f$. Equivalently up to universal constants, the Cheeger constant is
bounded below. This repository writes $h_n^\star$ for the worst Cheeger constant and
$\Psi_{\mathrm{KLS}}=h^{-1}$ for the inverse scale, avoiding the convention-dependent symbol
$\psi_n$.

Applying Poincaré to $f(x)=|x|^2$ gives

$$
\operatorname{Var}(|X|^2)\le 4nC_P(\mu).
$$

The reverse implication is not known with a dimension-free constant. A thin-shell estimate is
one radial test; KLS quantifies over every test function. It is therefore sound to say that radial
control alone does not currently prove KLS, but not that a converse has been disproved inside the
class of log-concave measures.

## 2. Frontier as of 24 August 2026

- **Published benchmark.** Klartag's improved Lichnerowicz argument gives
  $h_n^\star\gtrsim(\log n)^{-1/2}$, equivalently
  $\sup_\mu C_P(\mu)\lesssim\log n$.
- **Current preprint benchmark.** Conditional on Letwin's 27 July 2026 version-1 preprint,
  $h_n^\star\gtrsim(\log n)^{-1/4}$ and
  $\sup_\mu C_P(\mu)\lesssim\sqrt{\log n}$.
- **Sharp thin shell.** Chen--Klartag's 25 July 2026 version-1 preprint proves
  $\operatorname{Var}(|X|^2)\le8n$ and the sharp full third-moment-tensor bound
  $\lVert T_3(X)\rVert_{\mathrm{HS}}^2\le4n$.
- **Sharp homogeneous quadratic chaos.** Letwin proves, for every constant symmetric $M$,
  $\operatorname{Var}\langle MX,X\rangle\le8\operatorname{tr}(M^2)$. The word
  “homogeneous” matters: this does not assert the same sharp constant for arbitrary affine
  degree-two polynomials.

Only Letwin's paper supplies the announced improvement of the general KLS bound. The two
preprints share the moment-map estimate at $B=I$, but neither subsumes all the results of the
other. In particular, Letwin's quadratic Poincaré theorem alone does not give the sharp
$4n$ full third-tensor estimate.

Stochastic localization supplies the main historical quantitative line from power-law through
subpolynomial and polylogarithmic estimates to Klartag's published
$O(\!\sqrt{\log n})$ inverse-Cheeger scale. The relevant primary sources are Lee--Vempala's
localization/survey account, Chen, Klartag--Lehec, Jambulapati--Lee--Vempala, and Klartag; the
repository bibliography records their exact versions. The two live stochastic routes below ask
what additional cut- or eigenfunction-specific orientation survives beyond a global covariance
potential.

Primary sources:

- [Chen--Klartag, arXiv:2607.23307v1](https://arxiv.org/abs/2607.23307)
- [Letwin, arXiv:2607.24164v1](https://arxiv.org/abs/2607.24164)
- [Klartag, arXiv:2303.14938](https://arxiv.org/abs/2303.14938)

## 3. Strategy families

| family | object followed | established gain | live loss | repository route |
|---|---|---|---|---|
| classical needle localization | one-dimensional needles | reduces many convex-geometric inequalities to 1D | isotropy is global and is not preserved needle by needle | background only |
| stochastic localization, fixed cut | mass and two-color covariance of a candidate bottleneck set | exact martingale/Riccati backbone and conditional KLS implications | high-rank source occupation / operator-to-trace upgrade | [`eldan-localization`](routes/eldan-localization/) |
| stochastic localization, fixed eigenfunction | covariance tensor of a first spectral mode | exact fixed-function SDE and Letwin-whitened tensor control | unwhiten for universal time without losing tensor/covariance alignment | [`moment-map-spectral`](routes/moment-map-spectral/) |
| deterministic moment map | Hessian metric, Haar multipliers, Schur fibers, and Stein-kernel residuals | constant-matrix input, exact formal decompositions, positive local principal algebra | endpoint/lift/domain and all-split audits; leading global square-root commutator target | [`moment-map-cmh`](routes/moment-map-cmh/) |
| spectral/Bochner/$H^{-1}$ methods | first eigenspace and derivative energies | improved Lichnerowicz comparison; quadratic-chaos consequences | known comparisons retain a polylogarithmic loss | inputs to the two moment-map routes |
| transport/Föllmer processes | Jacobians or conditional covariance along a transport | alternative representations of functional inequalities | current derivative bounds reuse KLS-scale information or lose alignment | background; no live route yet |

The three live directories are genuinely different. The fixed-eigenfunction route still uses
stochastic localization. The CMH route is a deterministic extension of moment-map geometry from
constant matrix multipliers to test-dependent fields. They should cross-feed, but one must not be
renamed into the other.

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

## 5. Reading order and epistemic discipline

1. Read [`shared/target.md`](shared/target.md) for the route-agnostic conjecture and bridge to A1-bis.
2. Read this file and [`routes.md`](routes.md) to choose a route.
3. Read the selected route's README and its named open problem.
4. Consult [`obstructions.md`](obstructions.md) only with its stated scope: the current
   machine-enforced mechanisms are Eldan-route fences, not universal no-go theorems.
5. Consult [`gating.md`](gating.md) before making a numerical claim.

The status words are literal:

- **imported** means an external theorem, with version and review status recorded;
- **proved** requires the repository's R2 proof contract for every new promotion; 41 legacy
  Eldan nodes retain historical `proved` statuses but are explicitly recorded as certification
  debt until standalone dossiers and reviews exist;
- **formal identity** in a prose-only derivation means algebraically consistent subject to
  domains/regularity, not a ledger promotion;
- **reported retraction** records a failed idea from independent notes until its witness is
  persisted analytically or through `finum`;
- **open** and **heuristic** never inherit authority from a successful model calculation.
