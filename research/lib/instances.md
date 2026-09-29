# Shared calibration and stress instances

This is the canonical registry used to keep research diagnostics comparable. Calibration
instances have an analytic oracle; stress instances expose a named failure mode. Passing either
tier validates neither a claim nor a proof. The numerical-validity and provenance rules live in
[`../experiments/README.md`](../experiments/README.md).

The `numerics` column gives `target / emitted instance id`. An em dash means that the mathematical
instance is registered but has no backend. When a backend exists, its emitted id is canonical.

## Calibration registry

| id | route | object | oracle | `numerics` |
|---|---|---|---|---|
| `cal-kls-gauss` | KLS | isotropic Gaussian | $C_P=1$ | `kls / cal-kls-gauss` |
| `cal-kls-loc-gaussian` | KLS | Gaussian localization model | $A_t=(1+t)^{-1}I$ | `loc-engine / cal-kls-loc-gaussian` |
| `cal-cmh-gauss-R1` | KLS/CMH | $N(0,1)$ with $\tau=1$ | $R_1=1$ | `cmh-gate-zero / cal-cmh-gauss-R1` |
| `cal-cmh-uniform-simplex` | KLS/CMH | $\mathrm{Dir}(1,\ldots,1)$ | gate-zero ratio $2(m+1)/(m+3)$ | `cmh-gate-zero / cal-cmh-uniform-simplex` |
| `cal-cmh-m2-vs-uniform-interval` | KLS/CMH | $\mathrm{Dir}(1,1)$ | gate-zero ratio $6/5$ | `cmh-gate-zero / cal-cmh-m2-vs-uniform-interval` |
| `cal-kls-centered-exp` | KLS/CMH | centred one-sided exponential product | $C_P=4$ and $\operatorname{Var}(|X|^2)=8n$ | — |
| `cal-fiber-root-degree-two` | conditional-fiber | isotropic uniform simplex, $A_{m-1}$ root frame, degree-two quotient | $\lambda_{\min}(K,G)=(m+2)(m+3)/(5m^2)$ on the radial line, and quotient $1$ on linear tests (`lem:fiber-root-degree-two`) | `fiber-frame-dual / cal-root-anchors-m{m}-k2` |
| `cal-cmh-cone-axis` | KLS/CMH | exponential cone $\bar\mu_{K,\beta}$, any base $K$ | axis gate value $1+n/\beta$ (`prop:cone-linear-sector`(ii)) | `cmh-cone / cal-cmh-cone-axis` |
| `cal-cmh-cone-cube-closed-form` | KLS/CMH | cube cone, $K=[-1,1]^{n-1}$ | gate matrix $(1+n/\beta)\oplus\frac{6\beta^2+11\beta+5n+4}{5\beta(\beta+1)}\mathrm{Id}_{n-1}$ exactly (`cor:cube-cone-gate-zero`) | `cmh-cone / cal-cmh-cone-cube-closed-form` |
| `cal-cmh-cone-simplex-product` | KLS/CMH | simplex cone $K=\Delta_{n-1}$, $\beta=n$: the centred exponential product of `cal-kls-centered-exp` up to an orthogonal map | gate matrix $M=2\Sigma$ exactly (`cor:gate-zero-third-moment`, saturating example) | `cmh-cone / cal-cmh-cone-simplex-product` |
| `cal-cmh-cone-galerkin-chebyshev` | KLS/CMH | centred exponential product, CMH Galerkin on total degree $\le d$ | $2+2\cos(\pi/(d+1))$ — a **candidate oracle**, `cand:cmh-exponential-galerkin-rate`: exact on the line by the Laguerre tridiagonal reduction, the product transfer unproved; the row moves to the stress tier if the candidate is retired | `cmh-cone / cal-cmh-cone-galerkin-chebyshev` |
| `cal-cmh-cone-ball-1d` | KLS/CMH | $m=1$ radial moment-map ODE of the ball cone | $\Lambda'(s)=2\tanh s$, $\tau(r)=(4-r^2)/2$ (affine image of the $\mathrm{Unif}[-1,1]$ kernel $\tfrac12(1-t^2)$ derived in `solutions/prop-cone-moment-map.tex`) | `cmh-cone / cal-cmh-cone-ball-1d` |

## KLS stress registry

These models are route diagnostics, not substitutes for the universal KLS problem. The
one-sided exponential CMH models below are distinct from the two-sided Laplace product used by
`kls-align`.

| id | route | adversarial property | `numerics` |
|---|---|---|---|
| `stress-cmh-aligned-product` | moment-map/CMH | commuting product calibration | — |
| `stress-cmh-rotated-exp` | moment-map/CMH | detects illegal nodewise sibling positivity | — |
| `stress-cmh-laguerre` | moment-map/CMH | tests exhaustion of descendant or leaf slack | — |
| `stress-cmh-high-frequency-exp` | moment-map/CMH | separates conformal and traceless/corrector terms | — |
| `stress-cmh-45deg-child` | moment-map/CMH | isolates the conditional scalar residual | — |
| `stress-cmh-gamma-gaussian` | moment-map/CMH | tests local vector-conservation identities | — |
| `stress-cmh-three-exp` | moment-map/CMH | exposes canonical versus inherited Stein-kernel mismatch | — |
| `gaussian`, `exponential-centered`, `uniform`, `laplace`, `gamma-a*`, `beta-1-*` | moment-map/CMH | closed-form one-dimensional Stein-kernel ratios | same ids under `cmh-gate-zero` |
| `dir({alpha})` | moment-map/CMH | asymmetric Dirichlet gate-zero and Galerkin tests | `cmh-gate-zero / dir({alpha})` |
| `fence-cmh-algebraic-countermodel` | moment-map/CMH | shows that the constant-matrix estimate alone cannot imply gate zero | — |
| `stress-cmh-ab-exponential-limit` | moment-map/CMH | $\mathrm{Dir}(1,1,K)$, $K\in\{10^3,10^4\}$: the only exactly computable approach, *inside* the compact-target class, to the equality case of the anisotropic bootstrap — $\lambda_{\max}(\mathcal D,\mathcal N)\uparrow\tfrac12$ and the gate-zero ratio $\uparrow2$ in lockstep, neither attained | `cmh-ab / dir(1,1,1000)`, `cmh-ab / dir(1,1,10000)` |
| `stress-cmh-ab-reservoir-split` | moment-map/CMH | perturbed Gaussian product: first admissible non-product moment map on which the integrated matrix cyclic square $\mathsf R_Q\succeq\mathsf D$ fails directionally while its certified trace form holds; separates the two Monge–Ampère reservoirs, so any proof of $(\mathrm{AB})$ near $\rho=\tfrac12$ must spend target log-concavity (quadrature; directional) | `cmh-ab / gauss-gauss+y-bump(c=2.5,w=1.2) x He2*exp(-t^2/4)@-0.1` (and `@+0.1`) |
| `fence-cmh-m9-boundary` | moment-map/CMH | moment-potential perturbation of the $\mathrm{CMH}(4)$ saturator whose Galerkin quotient reads $4.052$ **and** whose target leaves the log-concave class (pointwise Hessian test; the averaged test wrongly passes it) — the false refutation candidate every M9 attempt rediscovers | `cmh-ab / exp-gauss+u-bump(c=2.5,w=1.2) x He0*exp(-t^2/4)@+0.05` |
| `stress-cmh-cube-cone` | moment-map/CMH | cube cone $\bar\mu_{[-1,1]^{n-1},\beta}$, $n\ge3$: non-product, unbounded support, saturates the sharp linear sector on the axis at $\beta=n$; its CMH Galerkin quotients sit strictly below the exponential product at equal degree | `cmh-cone / cone-cube-n{n}-b{beta}` |
| `stress-cmh-simplex-product-cone` | moment-map/CMH | cone over $\Delta_{k_1}\times\cdots\times\Delta_{k_r}\times[-1,1]^s$ at $\beta=n$: saturating and non-product for $r\ge2$; separates axis equality from transverse equality (`cand:cone-transverse-equality-simplex`); exact rational $LDL^\top$ decides the Loewner test either way | `cmh-cone / cone-{base}-n{n}-b{beta}`, base code `S{k}`/`I` concatenated, e.g. `cone-S2S3-n6-b6` |
| `stress-cmh-ball-cone` | moment-map/CMH | ball cone: smooth, non-polytopal, non-product base, tests the kernel away from facets; transverse margin below $2$ widens with $m$ (quadrature; directional) | `cmh-cone / cone-ball-m{m}-b{beta}` |
| `stress-fiber-frame-simplex-pencil` | conditional-fiber | fixed-degree all-frame min–max $\Lambda_{m,k}$ on the isotropic uniform simplex: exact rational root-frame pencil certificates plus a directional spherical frame; the certified degree-two floors mean any fixed-degree dual refuter needs $k\ge3$ | `fiber-frame-dual / cal-root-anchors-m{m}-k{k}`, `fiber-frame-dual / sph-m{m}-k{k}` |
| `stress-tailunion-cut-scale` | localization / `q:weighted` | balanced tail-union cut in the isotropic Laplace product: exact perimeter $\tfrac{n\sqrt2}{2}(2^{1/n}-1)$ strictly below every coordinate half-space for $n\ge2$, and $\lambda_{\rm cut}$ within $0.74$–$0.93$ of $\lambda_{\max}$, so a cut-local scale buys no reduction on a cut aligned with all coordinates | `kls-screen`, records with `model: isotropic-laplace-product/tail-union/cut-local-screened` (the target emits no instance ids) |
| `stress-cylinder-spectator-excess` | localization / `q:weighted` | cylinder cut $E_0\times\mathbb R^{n-n_0}$: $\lambda_{\rm cut}$ is exactly spectator-blind while the excess $e_t$ is non-decreasing in the spectator dimension — separates weight stability (which the cut-local repair gets right) from excess stability (which it does not); companion to brief edge case 2 | `kls-screen`, records with `model: isotropic-laplace-product/tail-union/cut-local-screened/cylinder` |

## Interpretation rules

- Check `bounded_by` before running a stress instance.
- Do not add a favorable instance during statement refinement; propose it for registry review.
- An exact oracle catches implementation errors. A finite stress battery only guides research.
- A calibration row whose oracle is a `cand:` id is provisional: a disagreement indicts the
  candidate as readily as the code. It stays in this tier only while the candidate is live.
- Formal proof or refutation provenance belongs in the ledger and proof workflow, not here.
