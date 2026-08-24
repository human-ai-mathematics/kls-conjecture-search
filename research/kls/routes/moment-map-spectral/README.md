# Route: moment map, Stein kernel, and the first eigenfunction

Status: **live, secondary**. This route remains distinct from the deterministic
[`moment-map-cmh`](../moment-map-cmh/) route. Its historical derivations are prose-only; any new
sharpened target is added to the central [`../../ledger.yaml`](../../ledger.yaml) with
`route: moment-map-spectral`.

## Thesis

Conditional on the correctness of Letwin's 27 July 2026 version-1 preprint, its moment-map
argument controls every centered quadratic form with a universal constant. Follow a first
spectral mode of a regular approximant through stochastic localization and apply that quadratic
control to its whitened posterior covariance tensor. The target is an absorptive, function-aware
source/damping estimate over a universal amount of localization time. This attacks the spectral
object defining KLS directly while retaining the tensor/covariance orientation discarded by a
global operator-norm bound.

Primary inputs:

- Letwin, arXiv:2607.24164v1, especially Theorems 1.2 and 2.5: dimension-free quadratic
  Poincare and the matrix moment-map estimate. This is a 27 July 2026 version-1 preprint.
- Klartag's log-concave Lichnerowicz argument (arXiv:2303.14938), including the
  preferred-direction branch for the first eigenfunction.
- Barthe--Klartag $H^{-1}$ inequalities and Fathi's positive symmetric Stein kernel, as used in
  the Letwin proof.

## Cycle-1 route decision

The detailed calculations are in
[`2026-08-20-kls-eigenfunction-localization.md`](../../../explorations/2026-08-20-kls-eigenfunction-localization.md)
and
[`2026-08-20-kls-hminus1-models.md`](../../../explorations/2026-08-20-kls-hminus1-models.md).
They change the first subgoal:

- the dynamic first-eigenfunction source/damping criterion is a genuine intermediate theorem;
- the formerly proposed full $H^{-1}$ residual is quantitatively equivalent to KLS and is now
  classified as an endpoint/diagnostic, not the first lemma;
- a direct unweighting of the positive moment-map Stein form is false on truncated-exponential
  first eigenfunctions.

**Current-priority note (24 August 2026).** The cycle-1 ranking is preserved as historical
memory. The deterministic CMH exploration subsequently exposed a separate, more sharply
formulated commutator program. The present route remains live as a secondary strand; no result
merges it into CMH or refutes its absorptive source/damping target.

## Why it may beat the localization route

Conditional on the same version-1 preprint, both fixed-cut and fixed-eigenfunction localization
have the optimal intrinsic static quadratic estimate. For the eigenfunction tensor $H_t$ this is

$$
\|A_t^{-1/2}H_tA_t^{-1/2}\|_{\mathrm{HS}}^2
\le8\operatorname{Var}_{\mu_t}(f).
$$

Crude unwhitening leaves a $\lambda_{\max}(A_t)^2$ factor and hence a universal-time dynamic
alignment problem. Unlike a cut, however, $f$ also satisfies an eigenfunction equation,
$\mathbb E|\nabla f|^2=\lambda$, and
$\mathbb E\|\nabla^2f\|_{\mathrm{HS}}^2\le\lambda^2$. Exploiting those fixed energies inside
the posterior channel is the possible extra structure. The route succeeds only if it controls
the tensor's incidence in inflated covariance spaces or consumes the exact damping; another
global covariance-norm estimate is not enough.

## Exact sufficient headline

Let $\kappa_n$ be the third-moment parameter used by Klartag--Lehec. Conditional on the
preprint, Letwin gives $\kappa_n\le2\sqrt2$. Therefore any dimension-free comparison of the form

$$
C_P(\mu)\le C\bigl(1+\kappa_n^2\bigr)
$$

for every isotropic log-concave $\mu$ would prove KLS. Equivalently, it is enough to remove the
remaining $\sqrt{\log n}$ loss from the current spectral comparison while retaining only a
universal function of $\kappa_n$.

## First concrete subgoal: absorptive eigenfunction localization

The central ledger tracks this headline as `q:mm-spectral-occupation`.

First work on smooth, strongly log-concave isotropic approximants, where the weighted Laplacian
$L=\Delta-\nabla V\cdot\nabla$ has discrete spectrum. Let $f$ be a normalized first
nonconstant eigenfunction, $-Lf=\lambda f$, and define along localization

$$
g_t=\operatorname{Cov}_{\mu_t}(f,X),\qquad
H_t=\mathbb E_t[(f-\mathbb E_tf)(X-a_t)^{\otimes2}],\qquad
A_t=\operatorname{Cov}_{\mu_t}(X).
$$

The exact SDE is

$$
dg_t=H_t\,dW_t-A_tg_t\,dt,
$$

so $\|H_t\|_{\mathrm{HS}}^2$ is the source for $|g_t|^2$ and
$2g_t^TA_tg_t$ is its exact damping. Prove universal $T_0,C_0,C_1>0$ and $\alpha<1$ such that
for every $t\le T_0$,

$$
\mathbb E\int_0^t\|H_s\|_{\mathrm{HS}}^2ds
\le C_0t+C_1\mathbb E\int_0^t|g_s|^2ds
+\alpha\mathbb E\int_0^t2g_s^TA_sg_s\,ds.
$$

The fixed-function SDE, Gronwall, posterior Brascamp--Lieb, and the fixed-gradient density
martingale prove that this estimate implies a universal spectral gap. The estimate itself is
open, and it must hold uniformly through regularization or be formulated for approximate
Rayleigh minimizers.

### The audited $H^{-1}$ endpoint

With $b=\int\nabla f\,d\mu$, the former target

$$
R(f)=\sum_i\|\partial_i f-b_i\|_{H^{-1}(\mu)}^2\le C\lambda
$$

is still sufficient, but it is also quantitatively implied by KLS. Indeed

$$
1+|b|^2-2|b|^2/\lambda\le R(f)\le1-|b|^2/\lambda.
$$

Its exact heat representation controls the short-time and high-frequency parts at the desired
scale; the long-time low-spectrum tail is the complete KLS-strength residue. Keep this as a
calibrated endpoint rather than presenting it as a likely preliminary lemma.

## Fences and comparisons

- The projection ceiling in the Eldan route does not refute this approach: the moment map uses
  information beyond radial/projection tests.
- The rank-one product-budget result is specific to a fixed-cut localization counterexample and
  imposes no no-go on this spectral route.
- A universal Lipschitz Gaussian transport is too strong for exponential tails. The weaker
  expected-Jacobian Brownian-transport criterion is sufficient for KLS, but current derivative
  bounds reuse known KLS estimates, so it is lower priority than the first-eigenfunction target.
- Classical one-dimensional needles do not preserve the full isotropic covariance constraints;
  this is a structural warning, not a theorem excluding all needle arguments.

## Promotion gate

Promote `q:mm-spectral-occupation` or add further internal claims only when at least one of the
following is
established:

1. the absorptive eigenfunction source/damping estimate above (or the weaker one-horizon net
   occupation criterion in the exploration note) uniformly on regular approximants, plus a
   passage to arbitrary log-concave measures; or
2. a route-fatal counterexample to every such function-aware occupation estimate.

Update the central KLS ledger through the orchestrator; do not create a route-local ledger.
