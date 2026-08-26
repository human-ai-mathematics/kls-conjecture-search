# Shared calibration and stress instances

This is the canonical registry used to keep research diagnostics comparable. Calibration
instances have an analytic oracle; stress instances expose a named failure mode. Passing either
tier validates neither a claim nor a proof. The numerical-validity and provenance rules live in
[`../../experiments/README.md`](../../experiments/README.md).

The `finum` column gives `target / emitted instance id`. An em dash means that the mathematical
instance is registered but has no backend. When a backend exists, its emitted id is canonical.

## Calibration registry

| id | program | object | oracle | `finum` |
|---|---|---|---|---|
| `cal-gauss` | A1 | $N(0,\Sigma)$ | $C_P=C_{\mathrm{LS}}=\lambda_{\max}(\Sigma)$ | `A1 / cal-gauss` |
| `cal-glm-linear` | A1 | Gaussian-linear GLM | posterior covariance $(\Sigma_0^{-1}+X^TX)^{-1}$ | `A1 / cal-glm-linear` |
| `cal-1d-eigen` | A1 | one-dimensional Gaussian | $C_P=\sigma^2$ | `A1 / cal-1d-eigen` |
| `mode-leverage-reference` | A1 | finite logistic GLM | exact mode-leverage formulas and the $\eta<1$ gate | `A1 / mode-leverage-reference` |
| `cal-logit-global` | A1 | Gaussian-prior logistic posterior | $C_{\mathrm{LS}}=C_{\mathrm{TCI}}=\lambda_{\max}(\Sigma_0)$ | — |
| `cal-bvm-gausslinear` | A2 | Gaussian-linear model | $nC_P=1/\lambda_{\min}(\Sigma_x)$ | `A2 / cal-bvm-gausslinear` |
| `cal-cauchy` | A3 | generalized Cauchy law | weighted gap from `thm:a3-student` | `A3 / cal-cauchy` |
| `cal-horseshoe-scale` | A3 | exact horseshoe marginal | $C_{\mathrm{HS}}(\tau)=4$ for every $\tau$ | — |
| `cal-gauss-t2` | A4 | Gaussian target and location shifts | $W_2^2/(2\mathrm{KL})=\sigma^2$ | `A4 / cal-gauss-t2` |
| `gaussian-local-wellspecified` | A4 | Gaussian location family | exact raw and optimizer-centred local constants | `A4 / gaussian-local-wellspecified` |
| `gaussian-local-misspecified` | A4 | misspecified Gaussian location family | exact baseline and excess constants | `A4 / gaussian-local-misspecified` |
| `cal-neal-ncp` | A5 | non-centred Neal funnel | $C_P=\max\{s^2,1\}$ | `A5 / cal-neal-ncp` |
| `partial-noncentering-reference` | A5 | scalar Gaussian hierarchy | $\alpha_*=1/(1+rB)$ minimizes $C_P$ and $\kappa_P$ | `A5 / partial-noncentering-reference` |
| `orbit-connectivity-reference` | A5 | finite communication-height matrix | exact orbit-connectivity threshold | `A5 / orbit-connectivity-reference` |
| `cal-kls-gauss` | KLS | isotropic Gaussian | $C_P=1$ | `kls / cal-kls-gauss` |
| `cal-kls-loc-gaussian` | KLS | Gaussian localization model | $A_t=(1+t)^{-1}I$ | `loc-engine / cal-kls-loc-gaussian` |
| `cal-cmh-gauss-R1` | KLS/CMH | $N(0,1)$ with $\tau=1$ | $R_1=1$ | `cmh-gate-zero / cal-cmh-gauss-R1` |
| `cal-cmh-uniform-simplex` | KLS/CMH | $\mathrm{Dir}(1,\ldots,1)$ | gate-zero ratio $2(m+1)/(m+3)$ | `cmh-gate-zero / cal-cmh-uniform-simplex` |
| `cal-cmh-m2-vs-uniform-interval` | KLS/CMH | $\mathrm{Dir}(1,1)$ | gate-zero ratio $6/5$ | `cmh-gate-zero / cal-cmh-m2-vs-uniform-interval` |
| `cal-kls-centered-exp` | KLS/CMH | centred one-sided exponential product | $C_P=4$ and $\operatorname{Var}(|X|^2)=8n$ | — |

## A-series stress registry

| id | obstruction | adversarial property | `finum` |
|---|---|---|---|
| `stress-logit-separable` | `obs:flat-direction` | local curvature can miss a covariance-scale direction | `A1 / stress-logit-separable` |
| `stress-anisotropic-prior` | `obs:flat-direction` | separates matrix information from a scalar curvature floor | `A1 / stress-anisotropic-prior` |
| `stress-wide` | `obs:flat-direction` | $D>n$ leaves data-blind directions at the prior scale | `A1 / stress-wide` |
| `stress-logit-bulk` | `obs:flat-direction` | a useful certificate should improve in a well-identified bulk regime | `A1 / stress-logit-bulk` |
| `stress-contamination` | `obs:tv-insufficient` | total variation can vanish while the variance diverges | `A2 / stress-contamination` |
| `stress-bvm-sweep` | `obs:tv-insufficient` | repeated fixed-dimensional posterior scaling check | `A2 / stress-bvm-sweep` |
| `stress-non-fisher-local` | `obs:tv-insufficient` | a remote near-minimizer separates Fisher and global PL scales | — |
| `stress-student` | `obs:heavy-tail-no-classical` | the classical gap fails while the weighted gap remains finite | `A3 / stress-student` |
| `stress-horseshoe` | `obs:heavy-tail-no-classical` | tests scale covariance and the exact horseshoe constant | `A3 / stress-horseshoe` |
| `stress-fixed-marginal-copula` | `obs:marginals-not-joint` | fixed marginals do not control a collapsing joint bottleneck | — |
| `stress-ep-tails` | `obs:restricted-not-finite` | Gaussian-location transport ratio diverges for $e^{-|x|^p}$, $p<2$ | `A4 / stress-ep-tails` |
| `stress-sep-mixture` | `obs:symmetry-vs-physical` | contrasts component reweighting with mode collapse | `A4 / stress-sep-mixture` |
| `stress-folded-well` | `obs:symmetry-vs-physical` | folding removes the two-well bottleneck | `A5 / stress-folded-well` |
| `stress-neal-funnel` | `obs:heavy-tail-no-classical` | centred and non-centred coordinates have different tail obstructions | `A5 / stress-neal-funnel` |

## KLS stress registry

These models are route diagnostics, not substitutes for the universal KLS problem. The
one-sided exponential CMH models below are distinct from the two-sided Laplace product used by
`kls-align`.

| id | route | adversarial property | `finum` |
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

## Interpretation rules

- Check `bounded_by` before running a stress instance.
- Do not add a favorable instance during statement refinement; propose it for registry review.
- An exact oracle catches implementation errors. A finite stress battery only guides research.
- Formal proof or refutation provenance belongs in the ledger and proof workflow, not here.
