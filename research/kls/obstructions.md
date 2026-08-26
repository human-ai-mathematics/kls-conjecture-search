# KLS obstructions

These fences constrain KLS proof shapes through ledger `bounded_by` edges. Each heading names a
ledger node with `kind: obstruction`; the ledger owns its status and manuscript source. The
obstructions currently apply to the Eldan-localization route unless another node lists them
explicitly.

## `obs:two-tail` — absolute-scale slice bounds fail

**Source:** `prop:two-tail`.
**Constrains:** `ass:all-cut-carleson`, `ass:weighted-package`, `q:upgrade`, `q:weighted`,
`q:stein-weighted`.

For the anisotropic Gaussian two-tail cut, $r=D=0$ while the Stein source is order $\Lambda^2$
and the excess is order $\Lambda^{-1/2}$. A slice-wise excess estimate therefore needs covariance
weight at least $(1+\|A\|_{\mathrm{op}})^{5/2}$. An unweighted proof must instead control the
expected occupation of inflated configurations.

## `obs:proj-ceiling` — projection tests lose $\log n$

**Source:** `eq:qcts-log` and the adjacent operator construction.
**Constrains:** `ass:all-cut-carleson`, `q:upgrade`, `prop:qcts-equivalence`.

Radial or projection-only information yields at best
$\operatorname{Var}(X^TMX)\lesssim\log n\,\|M\|_{\mathrm{HS}}^2$. A proof requiring
dimension-free quadratic-chaos control must use tensor-aware information beyond projection tests.

## `obs:crude-insufficient` — the crude covariance integral cannot bootstrap

**Source:** `lem:crude`, `rem:insufficiency`.
**Constrains:** `lem:crude` and any consumer using it as the closing estimate.

The bound $\Xi_T\lesssim\log n$ is too large to certify the required excess estimate at known
KLS lower-bound scales. A viable bootstrap input must improve the logarithm; the available
polylogarithmic technology reaches the `cor:loglog` scale.

## `obs:relative-ceiling` — an all-measure relative bound already implies KLS

**Source:** `prop:ceiling`.
**Constrains:** `ass:all-cut-carleson`, `q:taming`.

A universal bound $\Xi_{T_0}(\mu)\le\kappa T_0$ at sufficiently small fixed time already closes
KLS. It is not a weaker bootstrap input. The `q:taming` target must instead use near-worst
structure and the $h_\mu$-weighted absolute scale.

## `obs:circularity` — localized profile insertion may assume the target

**Source:** `lem:excess-identity`, `lem:inf-martingales`, `rem:circularity`.
**Constrains:** `thm:bootstrap`, `q:weighted`.

Excess propagation requires a lower bound on the expected isoperimetric profile of the random
posterior. The available supermartingale statement applies only to a fixed competitor family,
whereas the balanced family changes with time. A proof must supply additional structure or an
external non-circular anchor.

## `obs:rank-one-refuted` — single-coordinate product cuts self-extinguish

**Source:** `cor:refutation`.
**Constrains:** `q:alignment`.

For a product measure and a fixed balanced cut depending on one coordinate,
$\mathbb E\int_0^\infty S_t\,dt\le1$. Such a cut cannot sustain a covariance-inflation
counterexample. Any surviving witness or proof must treat high-complexity cuts and occupation
across many coordinates.
