# A-series inline baselines — independent R2 audit

- **Date:** 2026-08-25
- **Proof author:** `/root/ab_legacy_author`
- **Independent reviewer:** `/root/kls_core_author`
- **Reviewed dossiers:** `solutions/glm-linear-baselines.tex`, `solutions/obs-tv-insufficient.tex`, and `solutions/a5-lipschitz-quotient.tex`
- **Certification:** `checked_by: agent`
- **Review type:** exact ledger/manuscript comparison and independent line-by-line mathematical rederivation
- **Verdict:** pass

## Certified scope

This report certifies exactly these five ledger nodes:

1. `lem:linear-test-lower`
2. `thm:glm-fi`
3. `obs:tv-insufficient`
4. `lem:a5-lipschitz`
5. `thm:a5-monotone`

Each dossier statement was compared with its exact entry in `research/ledger.yaml` and with the
corresponding labeled manuscript statement. None of these nodes has a `bounded_by` edge, and no
numerical evidence is used as proof.

## Linear-test and GLM checks

- For `lem:linear-test-lower`, finite covariance puts every linear function
  $f_v(x)=\langle v,x\rangle$ in $L^2(\pi)$ and its Dirichlet energy is exactly $\|v\|^2$.
  Therefore $v^T\operatorname{Cov}_\pi v\leq C_P(\pi)\|v\|^2$, including the extended-valued
  case $C_P=+\infty$. Taking the unit-vector supremum gives the largest covariance eigenvalue.
  The argument does not invert the covariance and remains valid when it is singular; null
  directions simply have zero variance.
- For `thm:glm-fi`, positive definiteness of the Gaussian-prior covariance gives the exact
  curvature floor
  $m=\lambda_{\min}(\Sigma_0^{-1})=\lambda_{\max}(\Sigma_0)^{-1}$. Smooth convex losses add
  positive-semidefinite rank-one Hessian terms, so Bakry--Émery yields
  $C_P\leq C_{LS}\leq\lambda_{\max}(\Sigma_0)$ in the repository normalization
  $\operatorname{Ent}(f^2)\leq2C_{LS}\int|\nabla f|^2$. Otto--Villani then gives
  $C_{TCI}\leq C_{LS}$ under the repository normalization
  $W_2^2\leq2C_{TCI}\operatorname{KL}$.
- The nonsmooth-loss extension is valid. A finite convex loss has a supporting affine minorant;
  after convolution with an even compactly supported mollifier, convexity and that same minorant
  are preserved. The prior quadratic plus the common affine minorants supplies one Gaussian
  integrable majorant. Dominated convergence passes variance, entropy, and energy for bounded
  smooth compactly supported tests, after which truncation and closure give the natural Sobolev
  domains. Thus the manuscript's convexity hypothesis was not silently strengthened to $C^2$.

## Total-variation obstruction

For `obs:tv-insufficient`,
$\mu_n-\gamma=\varepsilon_n(\gamma_{a_n}-\gamma)$ gives
$\|\mu_n-\gamma\|_{TV}\leq\varepsilon_n$ with the supremum-over-events convention (or
$2\varepsilon_n$ for unhalved $L^1$). The mixture variance is exactly
$1+\varepsilon_n(1-\varepsilon_n)a_n^2$, and the admissible linear test $f(x)=x$ has unit
energy. Hence $C_P(\mu_n)$ diverges whenever
$\varepsilon_n\to0$ and $\varepsilon_na_n^2\to\infty$.

During review, the earlier manuscript overstatement about the optimal log-Sobolev and $T_2$
constants was removed. The final warning now matches the ledger and the dossier's certified
proposition exactly: it asserts only Poincaré divergence, and explicitly says that the linear
variance witness makes no claim about log-Sobolev or transportation-cost constants. The dossier's
conservative scope paragraph likewise declines to certify either stronger conclusion.

## Lipschitz images and finite quotients

- For `lem:a5-lipschitz`, variance and entropy are exactly preserved by pullback, and the stated
  closed-form/weak-gradient setting supplies
  $|\nabla(f\circ T)|\leq L|\nabla f|\circ T$. This gives the factors $L^2$ for Poincaré and
  log-Sobolev with the correct entropy normalization.
- The noninjective transport argument is complete. For $h=d\eta/d\mu$, the fiber-constant lift
  $d\widetilde\eta=(h\circ T)d\nu$ has total mass one, pushes forward exactly to $\eta$, and
  preserves relative entropy, including its extended-value interpretation. Pushing any coupling
  through $(T,T)$ contracts quadratic cost by $L^2$. No inverse map, measurable section, or
  choice of preimage is used.
- For `thm:a5-monotone`, the finite isometric action makes
  $d_{\Theta/G}([x],[y])=\min_g d_\Theta(x,gy)$ a well-defined quotient metric and makes the
  quotient map $1$-Lipschitz. The quotient Dirichlet form is defined globally by pullback, so
  equality of energies, variances, and entropies holds on its full closed domain. In particular,
  the proof does not assume that collision strata are smooth or negligible; weak-gradient/orbifold
  behavior there is already encoded in the lifted form. The density lift and coupling pushforward
  then prove the $T_2$ comparison with constant one.

## Validation and exclusions

All three dossiers compiled standalone with exit code 0 under a fresh repository-external build
root:

- `/tmp/ab-inline-r2-audit-20260825/glm-linear-baselines/glm-linear-baselines.pdf`
- `/tmp/ab-inline-r2-audit-20260825/obs-tv-insufficient/obs-tv-insufficient.pdf`
- `/tmp/ab-inline-r2-audit-20260825/a5-lipschitz-quotient/a5-lipschitz-quotient.pdf`

The remaining warnings are the expected unresolved manuscript references from standalone
subfile compilation; there are no TeX errors. This report does not certify any data-informed GLM
sharpening, any log-Sobolev or $T_2$ conclusion for the TV contamination example, strict quotient
improvement, quotient metastability, or any A-series node outside the five IDs above.
