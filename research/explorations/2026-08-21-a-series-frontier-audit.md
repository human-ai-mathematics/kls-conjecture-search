# A1–A5 frontier audit — resolved reductions, refutations, and next proof targets

- **Date:** 2026-08-21
- **Scope:** `conj:a1` through `q:a5-reparam`
- **Type:** coordinator synthesis of the five target audits
- **Evidence:** analytic only; no clean run artifact and no `numerical-strong` promotion

> **Superseded frontier map:** the follow-up proof probes close several items listed below on
> paper (factor one in the bounded-Hessian class, the sharp horseshoe constant, local-VI regime
> separation, and connectivity/partial-noncentring calibrations). See
> [`2026-08-21-a-series-proof-probes.md`](2026-08-21-a-series-proof-probes.md). This file is kept
> as the first-cycle audit rather than rewritten retrospectively.
> The project owner subsequently authorized independent-agent certification; the reviewed subset
> is now `status: proved` with standalone dossiers and persisted reports under `research/reviews/`.
> The certification boundary below records the earlier snapshot, not the current ledger state.

The target-specific derivations are in the same directory:

- `2026-08-21-a1-bulk-tail-audit.md`
- `2026-08-21-a2-strong-laplace-and-global-constants.md`
- `2026-08-21-a3-weighted-pi-audit.md`
- `2026-08-21-a4-restricted-transport-audit.md`
- `2026-08-21-a5-quotient-reparameterization-audit.md`

## Executive map

| target | resolved in this cycle | statement that remains open |
|---|---|---|
| A1 | an analytic proof draft gives the abstract inverse-Hessian bulk–tail Poincaré certificate; a one-observation logistic family refutes universal inverse-mode-Hessian bounds | settle the sharp/source-dependent prefactor, construct a computable $\bar W$ and certified tail that beats the prior scale, and add exact-coefficient spectral stability |
| A2 | an analytic proof draft establishes the conditional global-oscillation theorem; another gives exact prior-scale logistic $C_{\rm LS}=C_{\rm TCI}$ | find the weakest random-posterior condition for the Fisher-scale $C_P$ limit; classify priors/tails or localized notions that restore entropy/transport scaling |
| A3 | the marginal-only joint conjecture is refuted analytically; proof drafts cover product Hardy tensorization and a constant-4 hierarchical-prior pullback inequality | certify those drafts; prove $C_{\rm HS}=4$; formulate a dependence-bearing posterior theorem with scale derivatives and cross terms |
| A4 | proof drafts give the unrestricted linear-mean dual and global logistic variational constants; KL localization alone is insufficient | under an explicit coercivity/tail contract, control small optimizer-centred sublevels by the Wasserstein/Fisher tangent eigenvalue plus a uniform remainder |
| A5 | the spectral-sector criterion for strict quotient gain is exact; proof drafts solve the folded quotient and normalized Gaussian crossover | prove the raw logarithmic barrier law for a smooth statistical model and quotient spectral stability; optimize partial non-centring under fixed normalization |

## Certification boundary

At the time of this first-cycle snapshot, `status: proved` required a standalone `solution:`
artifact and `checked_by: human|lean`, and no independent check had yet occurred. The later
owner-authorized workflow adds `checked_by: agent` with distinct author/reviewer provenance and a
persisted report. The audited subset was promoted in the follow-up proof-probe cycle; unaudited
derivations below remain drafts.

## Cross-target deductions

### 1. Global entropy/transport and local posterior concentration separate

For a finite Gaussian-prior binary-logistic posterior,

$$
C_{\rm LS}=C_{\rm TCI}=\lambda_{\max}(\Sigma_0),
$$

although $C_P$ and the posterior covariance can be $O(n^{-1})$. The same remote translations
force, for every Gaussian variational family containing all translates of one fixed covariance,

$$
C_{\mathrm{mean},\mathcal Q}=C_{\mathcal Q}
=C_{\mathrm{mean},\mathrm{all}}=C_{\rm TCI}
=\lambda_{\max}(\Sigma_0).
$$

This single tail calculation redirects three targets at once: A1's entropy stage and A4's
transport stage must be localized/restricted, and A2's global LSI/$T_2$ line requires a genuinely
global Gaussian comparison or an $n$-shrinking prior.

### 2. One-dimensional information does not survive arbitrary dependence

A3's Hardy programme has a complete analytic tensorization draft for products:

$$
C_w\le4\max_jB_j.
$$

It is false for arbitrary dependent laws with the same marginals. The fixed-marginal copula
counterexample makes the joint constant diverge while every $B_j$ stays fixed. This is also an A4
and A5 warning: restricting coordinate tails or changing coordinates does not remove a physical
joint bottleneck. A hierarchical theorem needs a joint metric and a quantitative coupling
assumption.

### 3. The correct local objects are generalized eigenproblems

Two targets reduce locally to explicit spectral calculations:

- A4: if $\pi=q_0$ lies in a smooth variational family, the infinitesimal conversion factor is
  $\lambda_{\max}(F^{-1/2}GF^{-1/2})$, with $F$ the KL Fisher metric and $G$ the Wasserstein
  tangent metric.
- A5: group averaging splits the Ritz problem into invariant and non-invariant blocks; strict
  quotient improvement is decided by comparing their two restricted gaps, not by labelling one
  possibly degenerate eigenfunction.

Both now have a sound numerical contract: compute two-sided/residual-controlled generalized
eigenvalues, then prove a global or finite-radius remainder.

## Recommended proof order

1. **A3 horseshoe:** rule out a sub-threshold bound state after
   $y=\operatorname{arsinh}(x/\tau)$ and prove or refute $C_{\rm HS}=4$. This is the crispest
   standalone spectral problem.
2. **A1 prefactor and selection theorem:** first decide whether Veysseire's factor-one compact
   harmonic-mean argument extends directly to the noncompact Euclidean posterior setting; otherwise
   retain an explicit universal spread-to-gap factor. Then choose a concrete well-identified
   logistic design class, construct $\bar W$, and certify the integrated tail as $o(1/n)$.
3. **A4 local VI:** for a well-specified Gaussian family, prove a uniform expansion around the
   tangent eigenvalue on $r=\delta_{\mathcal Q}+\rho$; only then treat misspecification.
4. **A2 Poincaré stability:** weaken global oscillation to local quadratic comparison plus a
   Lyapunov/capacity tail estimate, uniformly over the random empirical potential.
5. **A5 barriers:** prove $n^{-1}\log C_P\to\Gamma$ for a smooth finite-group multiwell model
   before attempting Eyring–Kramers prefactors or singular mixture strata.
6. **A3/A5 hierarchy:** optimize partial non-centring in the exact Gaussian calibration, then use
   the constant-4 horseshoe-prior pullback metric as the nonlinear prior anchor.

## Numerical and provenance verdict

Three diagnostic implementations were corrected:

- A2 now measures endpoint error to the Fisher target instead of asserting the wrong monotone trend.
- A3 now uses the exact exponential-integral horseshoe marginal and a scale-covariant grid.
- A4 now uses genuine component-weight perturbations rather than a broad single Gaussian.

Focused regressions protect these corrections, but the worktree is intentionally dirty during the
audit and no new JSONL was created. Historical 2026-06-20 artifacts remain diagnostic-only.

## Primary-source checks

- Cattiaux–Guillin, *On the Poincaré Constant of Log-Concave Measures*:
  <https://arxiv.org/abs/1810.08369>.
- Chewi–Stromme, *The Ballistic Limit of the Log-Sobolev Constant Equals the
  Polyak–Łojasiewicz Constant*: <https://arxiv.org/abs/2411.11415>.
- Huguet, *Poincaré Inequalities and Integrated Curvature-Dimension Criterion for Generalised
  Cauchy and Convex Measures*: <https://arxiv.org/abs/2302.02684>.
- Veysseire, *A Harmonic Mean Bound for the Spectral Gap of the Laplacian on Riemannian
  Manifolds*: <https://arxiv.org/abs/1105.6080>. Its compact positive-curvature theorem motivates
  the A1 factor-one question; direct noncompact applicability is not asserted here.
