# Shared calibration and stress instances

This is the canonical registry used to keep research diagnostics comparable. Calibration
instances have an analytic oracle; stress instances expose a named failure mode. Passing either
tier validates neither a claim nor a proof. The numerical-validity and provenance rules live in
[`../../experiments/README.md`](../../experiments/README.md).

The `finum` column gives `target / emitted instance id`. An em dash means that the mathematical
instance is registered but has no backend. When a backend exists, its emitted id is canonical.

## Calibration registry

| id | route | object | oracle | `finum` |
|---|---|---|---|---|
| `cal-kls-gauss` | KLS | isotropic Gaussian | $C_P=1$ | `kls / cal-kls-gauss` |
| `cal-kls-loc-gaussian` | KLS | Gaussian localization model | $A_t=(1+t)^{-1}I$ | `loc-engine / cal-kls-loc-gaussian` |
| `cal-cmh-gauss-R1` | KLS/CMH | $N(0,1)$ with $\tau=1$ | $R_1=1$ | `cmh-gate-zero / cal-cmh-gauss-R1` |
| `cal-cmh-uniform-simplex` | KLS/CMH | $\mathrm{Dir}(1,\ldots,1)$ | gate-zero ratio $2(m+1)/(m+3)$ | `cmh-gate-zero / cal-cmh-uniform-simplex` |
| `cal-cmh-m2-vs-uniform-interval` | KLS/CMH | $\mathrm{Dir}(1,1)$ | gate-zero ratio $6/5$ | `cmh-gate-zero / cal-cmh-m2-vs-uniform-interval` |
| `cal-kls-centered-exp` | KLS/CMH | centred one-sided exponential product | $C_P=4$ and $\operatorname{Var}(|X|^2)=8n$ | — |

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
