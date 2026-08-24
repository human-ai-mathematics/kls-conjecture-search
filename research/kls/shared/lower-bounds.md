# Universal lower bounds and route-scoped refuted forms

The linear-test lower bound binds every route. The later refuted forms were discovered within
the Eldan fixed-cut program and are scoped to that mechanism; they are summarized here for
cross-route visibility, not promoted to universal no-go theorems. Canonical mechanism fences
remain in [`../obstructions.md`](../obstructions.md). Math in LaTeX (`$…$`).

`finum` contains an SDE-free finite-battery sanity check for the linear-test bridge. It does not
test the route-scoped fixed-cut refutations below, and the currently stored run artifacts are
historical diagnostics rather than evidence-eligible records; see [`../gating.md`](../gating.md).

## The sound lower bound (the universal refuter)

For any measure, every test function gives a certified Poincaré lower bound
$C_P\ge \mathrm{Var}(f)/\mathbb E\lVert\nabla f\rVert^2$; the linear test
$f=\langle v,\theta\rangle$ gives $C_P\ge\lambda_{\max}(\mathrm{Cov})$ (`ab/lem:linear-test-lower`
in `../../knowledge/lemmas.md`). For isotropic measures $\lambda_{\max}(\mathrm{Cov})=1$, so
this says $C_P\ge 1$ — KLS asks for a matching universal *upper* bound (equivalently, up to
universal Cheeger--Poincaré constants, $h_\mu\ge c$). Consequence for
routes: any claimed dimension-free upper bound must survive this lower bound on every test
instance; `finum` uses it as the go/no-go gate when numerically vetting a route.

## Route-scoped refuted forms

- **Single-coordinate product-localization counterexample — refuted** (`obs:rank-one-refuted`,
  `cor:refutation`). The natural "one inflated coordinate breaks the product budget" attempt
  does **not** refute the program: the product coordinate-budget theorem (`thm:budget`)
  absorbs a rank-one inflation. This kills that counterexample mechanism inside the fixed-cut
  Eldan route; it does not constrain a moment-map, spectral, transport, or needle proof.
- **Relative-scale-for-all-measures is already KLS-sufficient, not intermediate**
  (`obs:relative-ceiling`). Demanding the covariance-excess bound $\Xi_T\le\kappa T$ for
  *every* measure at a sufficiently small universal time directly implies KLS by the fixed-cut
  consumption argument. Only sufficiency is proved, not the converse. This is a ceiling for
  that localization mechanism; the distinct $h_\mu$-weighted, near-worst target `q:taming`
  remains legitimate.

## Why these live here, not in a route

The linear-test lower bound is genuinely route-agnostic. The two items immediately above are
retained here for discoverability but are explicitly scoped to the Eldan/fixed-cut mechanism;
a future non-localization route does not inherit them as no-go theorems. Mechanism-specific
constraints are centralized in [`../obstructions.md`](../obstructions.md) with their route scope
stated explicitly.
