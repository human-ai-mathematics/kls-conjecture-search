---
verdict: pass
authors:
  - /root/kls_ledger_audit
  - /root/repair_cmh_hodge_domain_w3
reviewer: /root/review_cmh_gamma_dependency_w3
fingerprints:
  solutions/thm-cmh-dirichlet.md: 00e9585188cbec4718447563f778bc889eaa0670b93c06aa38646db3f018530d
  thm:cmh-1d: 20ca97481f8d3f33bab114618adc59596740cec2d34e37ad9c5c8ec1b9fa9904
  def:cmh: 5971e940e93fa8179ce6c80c9817d3b3a88ac7db2ffe56897f1957c02431f9e7
  thm:cmh-product: 93367af0f91020a7189581ccf6821eafd93c5bb734d06bfb114187be354d08a7
  cor:cmh-linear-images: 4a8e460a9f137e2c3bfcd012669e8a658f242d5dcd19ba480849ffc13abef452
  lem:cmh-gamma-completion: 322e41a5312dc60bb984ccaa9e90cf3ba7598ef853f353546520666f45aa8a33
  prop:cmh-bochner: 237164772a03afb3fb5bfb7a896dbd45f8487332637efa548b827454d8f8ea6c
  lem:cmh-row-min: 3747422f61e31d367dbc910511a078a463c6440ae445f61324e00e45f812e05f
  lem:cmh-angular-coefficient: b2dd0851b76505e3182d0b1472b8d5102a420f78b16abdb8ae23fde0456de475
  thm:cmh-dirichlet: 0950144e400e4a077e8ae82686d149d0a736b6ec651e7c588e4e867146a8db94
  cor:cmh-dirichlet-surplus: fdd4f0dcfccd11cb61eceeec922bc50c8ed87bb4a9faa496901201eef7ea9424
  cor:cmh-dirichlet-poincare: 0295ebca6004666831c2db752ae739c062b86f6097e7b9f5152902d1765820c6
  thm:cmh-implies-affine-poincare: 4ca4161533a8e140c1e3302d067c0ba1672754860e21a237009c1df910d1dbbc
  rem:cmh-saturation-risk: 2a3ba80b8cfea460f74c0dbcf122eeafdcf31576b42e60cf7d5507106f2332af
  prop:cmh-hodge: e53f8f0d21ff4afad0be69fb034e09db1f7daaa882338a1d927af40c3117410e
---

*Follows up* `research/reviews/2026-08-25-kls-cmh-exact-cases-repair-audit.md`.

# CMH Gamma--Bochner provenance repair -- independent supplementary review

## Scope and immutable bytes

This is a cold supplementary review of `solutions/thm-cmh-dirichlet.tex` at SHA-256
`d7289c45bac18b0faea999d2642cfe04b4b7b1341526a25f69722e05c3a756ec`. The preceding passing
review covered SHA-256
`093a075de109d732f711468b3879cf5e2cda2c931027e15e0464e23d92704f46`; the present repair makes
the previously implicit Gamma--Bochner input explicit, adds it to the dossier header, and resets
the dossier certification pending this review.

The certifying scope here is exactly `lem:cmh-gamma-completion`. I also traced the repaired input
through the Hessian-row minimum, the Dirichlet theorem, and its two immediate corollaries to check
that the new provenance changes no coefficient or conclusion. Those downstream nodes, the other
exact-case nodes in the shared dossier, and the proof of `prop:cmh-bochner` itself are outside this
report's front-matter scope; their existing independent reports remain their certification
provenance.

## Canonical product-Gamma moment Hessian

The repaired assertion is genuinely about the canonical moment Hessian, not merely an arbitrary
Stein kernel. For one coordinate and shape $\alpha>0$, take the source potential

$$
 \varphi_\alpha(z)=e^z-\alpha z+\log\Gamma(\alpha).
$$

Then

$$
 x=\varphi_\alpha'(z)=e^z-\alpha=Y-\alpha,
 \qquad \varphi_\alpha''(z)=e^z=Y.
$$

Under $y=e^z$, the source measure transforms as

$$
 e^{-\varphi_\alpha(z)}\,dz
 =\frac{y^{\alpha-1}e^{-y}}{\Gamma(\alpha)}\,dy.
$$

Thus the gradient pushes the source measure to the centered Gamma law $X=Y-\alpha$, and its
canonical moment Hessian in target coordinates is $H_\Gamma(Y)=Y$. Summing these separable
potentials proves for the independent product that

$$
 H_\Gamma=\operatorname{diag}(Y_1,\ldots,Y_m).
$$

This also follows from the dossier's already certified one-dimensional zero-flux uniqueness and
product construction. The density computation newly printed in the dossier is therefore a check
of the transported generator, not an illicit inference that every multivariate Stein kernel is a
moment Hessian.

Writing
$\rho_\Gamma(y)=\prod_i\Gamma(\alpha_i)^{-1}y_i^{\alpha_i-1}e^{-y_i}$ gives, coordinate by
coordinate,

$$
 \rho_\Gamma^{-1}\partial_i(\rho_\Gamma Y_iG_i)
 =Y_iG_{ii}+(\alpha_i-Y_i)G_i.
$$

Because the centered target coordinate is $X_i=Y_i-\alpha_i$, this is exactly the Stein drift
$-X_iG_i$. Hence

$$
 \operatorname{Div}_\Gamma(H_\Gamma\nabla G)=\mathcal L_\Gamma G
$$

with the Laguerre generator and the sign convention used throughout the dossier.

## Bochner specialization and ordered-pair convention

The certified upstream proposition states

$$
 \mathbb E(L_\mu G)^2
 =\mathbb E\!\left[\langle H\nabla G,\nabla G\rangle
 +\operatorname{Tr}(HD^2G\,HD^2G)\right].
$$

For $H=H_\Gamma$ the first term is $\sum_iY_iG_i^2$. For the Hessian term,

$$
 \operatorname{Tr}(H_\Gamma D^2G\,H_\Gamma D^2G)
 =\sum_{i,j}Y_iY_jG_{ij}G_{ji}
 =\sum_{i,j}Y_iY_jG_{ij}^2.
$$

The sum is over ordered pairs. Each off-diagonal square therefore occurs once in row $i$ and
once in row $j$, exactly as it does in the matrix trace. No extra factor of $2$ or $1/2$ is
present. As a direct compatibility check with the Codazzi step in `prop:cmh-bochner`, the tensor
$H_{mj}\partial_jH_{k\ell}$ is nonzero only when $m=k=\ell$, and is consequently totally
symmetric.

It follows exactly that

$$
 N_\Gamma(G)=\mathbb E(\mathcal L_\Gamma G)^2
 =\mathbb E\left[\sum_iY_iG_i^2+
                   \sum_{i,j}Y_iY_jG_{ij}^2\right].
$$

## Row completion

For one Gamma coordinate, integration by parts against
$y^{\alpha_i-1}e^{-y}/\Gamma(\alpha_i)$ gives

$$
 \mathbb E[Y_i^2G_iG_{ii}]
 =-\frac12\mathbb E[((\alpha_i+1)Y_i-Y_i^2)G_i^2].
$$

Consequently the cross term in the completed diagonal square is

$$
 -\frac{2}{\alpha_i+1}\mathbb E[Y_i^2G_iG_{ii}]
 =\mathbb E[Y_iG_i^2]
  -\frac1{\alpha_i+1}\mathbb E[Y_i^2G_i^2].
$$

Adding its diagonal square and all $j\ne i$ squares yields precisely the $i$th ordered Bochner
row:

$$
 \mathbb E R_i
 =\mathbb E\left[Y_iG_i^2+\sum_jY_iY_jG_{ij}^2\right]
  -\frac{\alpha_i}{(\alpha_i+1)^2}\mathbb E[Y_i^2G_i^2].
$$

Since $D_i=\mathbb E[Y_i^2G_i^2]/\alpha_i$, summing over $i$ gives

$$
 N_\Gamma=\sum_i\mathbb E R_i
 +\sum_i\frac{\alpha_i^2}{(\alpha_i+1)^2}D_i.
$$

Subtracting $D_\Gamma/4$ proves the ledger, manuscript, and dossier identity with

$$
 \delta_i=\frac{\alpha_i^2}{(\alpha_i+1)^2}-\frac14\ge0
 \quad\Longleftrightarrow\quad \alpha_i\ge1.
$$

Every sign and coefficient is therefore correct. $R_i$ is a sum of weighted squares. The
homogeneity of $G$ is unused in this identity and is only consumed by the downstream Euler-row
minimum; this is a legitimate sharpening opportunity, not a hidden premise. The identity itself
needs only positive Gamma shapes and the usual core/decay or closed-form approximation needed for
the displayed integration by parts; the hypothesis $\alpha_i\ge1$ is used exactly for the claimed
nonnegativity of $\delta_i$.

## Direct downstream compatibility

The row-minimum proof uses the same $R_i$ and the differentiated homogeneous Euler identity, so
the ordered-pair convention introduces no change there. For the Gamma branch of
`thm:cmh-dirichlet`, substituting the row bound and $D_i=\mathbb E_Pu_i^2/\alpha_i$ gives the
coefficient

$$
 \frac1{z_AP_i}+\frac2{(A-1)(\alpha_i+1)}
 +\frac{P_i}{(\alpha_i+1)^2}+\frac{\delta_i}{\alpha_i}.
$$

Multiplication by $z_A\alpha_i$, with $z_A=(A-1)(A-2)$, gives exactly

$$
 F_A(\alpha_i,P_i)
 =\frac{\alpha_i}{P_i}+\frac{2\alpha_i(A-2)}{\alpha_i+1}
  +\frac{z_A\alpha_i(\alpha_i+P_i)}{(\alpha_i+1)^2}-\frac{z_A}{4}.
$$

Thus the certified angular lower bound still yields

$$
 n_\alpha(g)\ge
 \left(\frac{A(A+1)}4+s_A\right)d_\alpha(g),
$$

using $z_A/4+A-1/2=A(A+1)/4$. The main Dirichlet theorem and its quantitative-surplus and
affine-Poincare consequences therefore inherit the repaired provenance without a constant or
range change. The Gamma branch is used only for $A\ge3$, where the stated inverse moments and
the previously reviewed cutoff closure are finite; the residual two-coordinate branch with
$A<3$ remains handled by the one-dimensional theorem.

## Statement, dependency, fences, and build

- The dossier lemma, the manuscript lemma at `lem:cmh-gamma-completion`, and the ledger statement
  agree in identity, parameter range, homogeneity context, definitions, and nonnegativity.
- The dossier header names `prop:cmh-bochner`; the manuscript explicitly invokes it; and the
  ledger now has `depends_on: [prop:cmh-bochner]`. That upstream node is repository-certified and
  unconditional. No external source or unreviewed preprint enters this repair.
- The node has no `bounded_by` edge. The repair uses the full ordered Hessian matrix, so it does
  not evade the projection-only fence `obs:proj-ceiling`, and it makes no stochastic-localization
  or universal-CMH claim.
- A forced standalone build with
  `latexmk -g -pdf -outdir=../build thm-cmh-dirichlet.tex` succeeded and produced the six-page
  PDF. Cross-manuscript references remain unresolved standalone exactly as allowed by
  `solutions/README.md`.

## Corrections and exclusions

Corrections required: none.

This supplementary report does not re-review the proof of `prop:cmh-bochner`, the independent
angular minimization, the one-dimensional endpoint, product tensorization, the complete closure
theory, universal $\mathrm{CMH}(4)$, or any numerical artifact. It checked the direct downstream
algebra only to exclude a provenance-induced regression; it does not replace the active reviews
for those downstream nodes.

## Proposed ledger delta

Keep `lem:cmh-gamma-completion` at `status: proved` and retain
`depends_on: [prop:cmh-bochner]`, with

```yaml
solution: solutions/thm-cmh-dirichlet.tex
checked_by: agent
review: research/reviews/2026-08-27-lem-cmh-gamma-bochner-repair-proof-review.md
```

No other node requires a status change from this supplementary review.
