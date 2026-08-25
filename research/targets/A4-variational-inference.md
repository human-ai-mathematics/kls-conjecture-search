# A4 — Transport constants for variational inference

- **Ledger:** `q:a4-certificate` (+ supporting `q:a4-*` nodes) · **Manuscript:** `A4-variational-inference.tex` (`sec:a4`)
- **Status:** mixed: seven local/dual/symmetry nodes independently agent-certified; the
  finite-radius posterior theorem remains open · **Evidence:** none · **Baseline to beat:**
  `thm:glm-fi` (prior-scale `C_TCI`)
- **Review record:** [`../reviews/2026-08-21-a4-a5-independent-agent-audit.md`](../reviews/2026-08-21-a4-a5-independent-agent-audit.md)

## Goal (current best statement)

Let `A_Wbar = Σ₀⁻¹+XᵀWbar X`. The local conjecture asks for an explicit `ρ₀>0` and a
coercivity–tail contract: the family parameter sublevel through `δ_Q+ρ₀` is compact and uniformly
`P₂`-integrable, posterior curvature dominates `A_Wbar` on a stated bulk set, and the complement
has quantitative transport and mean remainders. For every `0<ρ≤ρ₀`, the target is
```
C_{Q,δ_Q+ρ}(π)      ≤ K λmax(A_Wbar⁻¹) + R₂(ρ),       (W₂ certificate)
C_mean,Q,δ_Q+ρ(π)   ≤ K λmax(A_Wbar⁻¹) + R_mean(ρ),   (mean certificate)
```
giving `W₂²(q*,π) ≤ 2 C_{Q,r} KL` and `‖E_{q*}θ − E_π θ‖² ≤ 2 C_mean,Q,r KL`, *given* a computable
KL upper bound (`rem:a4-elbo` — a separate hypothesis). For a misspecified family, both
remainders must retain the nonzero baseline and possible linear terms described below.

Hierarchy: `C_mean,Q ≤ C_Q ≤ C_TCI`, and the gaps can be huge. `C_mean,Q` is a
linear-observable entropy constant, not a `T₁` constant (which would control every Lipschitz
observable).

## Obstructions it must respect

- `obs:restricted-not-finite` — even a fixed-KL entropy ball can have infinite $W_2$ radius;
  localization also needs family coercivity or quadratic-exponential tails.
- `obs:flat-direction` — the bulk vs prior-scale gap is the same vanishing-curvature story as A1.
- `obs:gaussian-tail-rigidity` — global location-rich logistic constants are exactly prior-scale.
- `obs:symmetry-vs-physical` — multimodal lower bounds are **family-dependent**; quotient first.

## Analytic refinement (2026-08-21)

See
[`2026-08-21-a4-restricted-transport-audit.md`](../explorations/2026-08-21-a4-restricted-transport-audit.md)
and the next-cycle analysis
[`2026-08-21-a4-local-vi-next-cycle.md`](../explorations/2026-08-21-a4-local-vi-next-cycle.md).

**Analytic proof draft (pending repository certification):** for a Gaussian-prior logistic
posterior and any Gaussian family containing every translation of one fixed covariance
(including mean-field Gaussian),

$$
C_{\mathrm{mean},\mathcal Q}=C_{\mathcal Q}
=C_{\mathrm{mean},\mathrm{all}}=C_{\mathrm{TCI}}
=\lambda_{\max}(\Sigma_0).
$$

Thus the global restricted constant is still prior-scale; only $C_{\mathcal Q,r}$ can carry the
posterior-scale A4 claim. Separately, for a target with a finite first moment, the unrestricted
mean constant has the following independently agent-certified extended-valued identity (an
infinite linear MGF makes the right side infinite):

$$
C_{\mathrm{mean},\mathrm{all}}
=\sup_{\|u\|=1,t\ne0}\frac{2}{t^2}
  \log\mathbb E_\pi e^{t u^\top(\theta-\mathbb E\theta)}.
$$

Under a Legendre cumulant hypothesis, its localized version is also exact. With
$\psi_u(t)=\log\mathbb E e^{tX_u}$ and
$r_u(t)=t\psi_u'(t)-\psi_u(t)$,

$$
C_{\mathrm{mean},\mathrm{all},r}
=\sup_{\|u\|=1}\sup_{0<r_u(t)\le r}
  \frac{\psi_u'(t)^2}{2r_u(t)}.
$$

If a common exponential moment exists and the covariance is positive definite, this equals
$\lambda_{\max}(\operatorname{Cov}_\pi\theta)+O(\sqrt r)$ as $r\downarrow0$. For a Gaussian it
is exactly $\lambda_{\max}(\Sigma)$ for every $r>0$. The global and localized results are
independently agent-certified in
[`eq-a4-mean-dual.tex`](../../solutions/eq-a4-mean-dual.tex) and
[`prop-a4-mean-local.tex`](../../solutions/prop-a4-mean-local.tex)
(`eq:a4-mean-dual`, `prop:a4-mean-local`).

**Well-posedness correction:** a KL cutoff alone does not bound $W_2$ for an unrestricted or
tail-reweighting family when $\pi\propto e^{-|x|^p}$, $p<2$; $C_{\mathrm{all},r}=\infty$ for
every $r>0$. The current Gaussian-location stress family is finite on sublevels because its KL is
coercive in its finite-dimensional parameters. Also record the variational gap
$\delta_{\mathcal Q}=\inf_{q\in\mathcal Q}\mathrm{KL}(q\|\pi)$ and use
$r=\delta_{\mathcal Q}+\rho$; the sublevel is empty below $\delta_{\mathcal Q}$.

**Three local regimes (independently agent-certified):** assume a unique interior
optimizer, a compact parameter sublevel on which KL is continuous and quantitatively separated
from its minimum off every optimizer neighborhood, uniform cubic KL/transport expansions, and a
positive-definite KL Hessian $F$. In the well-specified case $q_*=\pi$, finite
$L^2\cap H^{-1}$ scores and finite-energy Poisson solutions give

$$
C_{Q,\rho}=\lambda_{\max}(F^{-1/2}GF^{-1/2})+O(\sqrt\rho).
$$

For a misspecified raw sublevel, if
$D(q_{*+h},\pi)=D_*+b_D^\top h+O(\|h\|^2)$ and $\delta_Q>0$, then

$$
C_{Q,\delta_Q+\rho}
=\frac{D_*}{2\delta_Q}
+\frac{\sqrt{2\rho}}{2\delta_Q}\|F^{-1/2}b_D\|+O(\rho),
$$

with the analogous mean formula. For the optimizer-centred excess-KL ratio
$W_2^2(q,q_*)/[2\{\mathrm{KL}(q\|\pi)-\delta_Q\}]$, the generalized eigenvalue reappears with
the Wasserstein tangent at $q_*$. Boundary or multiple optimizers are explicitly outside these
statements (`prop:a4-local-wellspecified`, `prop:a4-local-misspecified`,
`prop:a4-local-excess`).

Standalone dossiers:
[`prop-a4-local-wellspecified.tex`](../../solutions/prop-a4-local-wellspecified.tex),
[`prop-a4-local-misspecified.tex`](../../solutions/prop-a4-local-misspecified.tex), and
[`prop-a4-local-excess.tex`](../../solutions/prop-a4-local-excess.tex).

**Exact Gaussian calibration (independently agent-certified):** for
$\pi=N(\mu,\Sigma)$ and $Q_S=\{N(\mu+m,S):m\in\mathbb R^d\}$, let
$\delta_S=\mathrm{KL}(N(\mu,S)\|\pi)$,
$D_S=W_2^2(N(\mu,S),\pi)$, and $\lambda=\lambda_{\max}(\Sigma)$. If $S\ne\Sigma$,

$$
C_{Q_S,\delta_S+\rho}
=\max\left\{\frac{D_S}{2\delta_S},
\frac{D_S+2\rho\lambda}{2(\delta_S+\rho)}\right\},
\qquad
C_{\mathrm{mean},Q_S,\delta_S+\rho}
=\lambda\frac{\rho}{\delta_S+\rho}.
$$

Both optimizer-centred excess constants equal $\lambda$ for every $\rho>0$; if $S=\Sigma$,
both ordinary localized constants do too (`ex:a4-gaussian-local`). This example separates
approximation baseline from optimization geometry exactly; see
[`ex-a4-gaussian-local.tex`](../../solutions/ex-a4-gaussian-local.tex).

**Symmetrization (independently agent-certified):** for invariant $\pi$ and
$\bar q=|G|^{-1}\sum_g g_\#q$, invariant observables are preserved while both
$\mathrm{KL}(\bar q\|\pi)\le\mathrm{KL}(q\|\pi)$ and
$W_2^2(\bar q,\pi)\le W_2^2(q,\pi)$. This is usable inside VI only when the family admits the
average, and it does not order the ratio of the two decreasing quantities
(`lem:a4-symmetrization`; solution
[`lem-a4-symmetrization.tex`](../../solutions/lem-a4-symmetrization.tex)).

**ELBO correction:** since $\log Z=\mathrm{ELBO}+\mathrm{KL}$, an end-to-end upper error bar needs
an **upper** bound on $\log Z$, not a lower bound beyond the ELBO.

**Diagnostic retraction/repair:** the retired `stress-sep-mixture` diagnostic used a broad
Gaussian, not a weight-perturbed mixture, and its verdict contradicted its note. The corrective
history is preserved in the
[`2026-08-21 A4 audit`](../explorations/2026-08-21-a4-restricted-transport-audit.md). The current
contract calls for genuine $\varepsilon$-reweighted mixtures; no clean artifact or asymptotic
separation sweep exists yet.

## Sub-questions (ledger)

| node | what | difficulty |
|------|------|-----------|
| `q:a4-restricted` | distinguish raw `C_{Q,δ_Q+ρ}` from optimizer-centred excess-KL geometry | entry |
| `q:a4-mean` | exact cumulant dual plus localized/per-functional family constants | medium |
| `q:a4-modified` | modified transport cost for heavy tails (W₂ counterpart of A3) | hard |
| `q:a4-multimodal` | centers `±a`, separation `D=2a`: certify lower witnesses and determine their sharp scaling | hard |
| `q:a4-elbo` | couple `C_{Q,r}` to a computable KL certificate → end-to-end error bar | applied |

## Numerical plan (finum)

1. Mean-field Gaussian `Q`; first compute the variational gap `δ_Q`, then form finite-grid lower
   estimates of
   `sup_{q∈Q, KL≤δ_Q+ρ} W₂²(q,π)/(2 KL)` and compare its small-`ρ` behavior with the tangent
   misspecified baseline expansion. Separately compare optimizer-centred excess ratios with the
   generalized eigenvalue. These are lower estimates, never numerical upper bounds on `C_{Q,r}`.
   Do not target a posterior-scale global `C_Q` for logistic posteriors.
2. GLM instances: compare directional lower witnesses with `λmax(A_Wbar⁻¹)` and with any separately
   proved upper bound; a grid search alone cannot certify posterior-scale `C_{Q,r}`.
3. `stress-ep-tails`: show directional growth of the location witnesses. Global divergence and
   localized finiteness for this coercive location family are analytic claims, not finite-grid
   falsification verdicts; the unrestricted entropy ball remains infinite analytically.
4. `stress-sep-mixture`: compute genuine component-weight perturbations
   `q_ε=(1/2+ε)N(−a,σ²)+(1/2−ε)N(a,σ²)` and the mode-collapse witness, recording
   separation `D=2a`. Sweep `ε`, `a/σ`, and numerical resolution. Both are lower witnesses: do not
   infer a sharp exponential or polynomial asymptotic without matching upper bounds.

**Research use only:** lower-witness sweeps and resolution/tail stability checks are directional
diagnostics for choosing conjectures, identifying failure modes, and suggesting analytic
refutations. Agreement with independently proved upper control does not validate or certify that
proof, and numerical diagnostics alone never establish the claimed constant. Rigorous refutation
still requires an analytic argument or exact lower bound.

## Numerical research log

_(none yet)_

## Cross-links

- Consumes A1 (bulk scale), A2 (Fisher limit), A3 (modified cost), A5 (quotient escape).
