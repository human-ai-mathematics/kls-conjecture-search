---
verdict: pass
authors:
  - /root/kls_proof_audit
  - /root/repair_splitting_dossier
reviewer: /root/review_splitting_w0
fingerprints:
  solutions/kls-geometry-models.md: 51f2adca44f986ee352d1f7e98544442cdd4993adff9977847a5d5f268fcc811
  lem:profile-bound: edaf5f0b76adaf78959e02db87ee943f5ff1a7a8b54831c0aa33bdfcf4d293d6
  cor:generic-degeneracy: 1103100221b4bf047150e63ccddaa04ec4c2ec9fefad01135905132ef7d93252
  prop:exact-splitting: 7a3cbda8f27037b4c8c2aba75fe4fcd19fd746f2e479e6a26e2a41298b3eb008
  prop:persistent-splitting: 5aa02982b1ba2c12bcd728b05e39ff5096e0bec02d5b22114480ba116cc2346c
  prop:gaussian-model: b36d81c4dcd6e7eff5e90fe7e95689cd454e8559454889d33b593beeafdfa213
  prop:products: 85b9ec9b7b81c783e52dce9f3edce41396f581da4f7a425bd3df9031860a6c8c
---

# KLS geometry models repair — independent proof review

This is a cold review of `solutions/kls-geometry-models.tex`, whose reviewed SHA-256 is
`e241ed74fbe061763b0c5ac84b779bf56ddc16e3d93cb97866da9aadaa9d5346`. The proof was
reconstructed from the dossier, current manuscript statements, ledger, shared definitions, and
actual sources; the repair exploration was consulted only to identify provenance and was not used
as mathematical evidence. Both listed authors are distinct from the reviewer.

## Findings

### Statement agreement, fences, and dependency closure

For all six nodes, the dossier theorem, the manuscript theorem at the ledger's effective label,
and the ledger `statement:` agree mathematically.

In particular, all three current statements of `prop:persistent-splitting` fix a unit direction
$\theta$, require proper lower-semicontinuous convex extended-valued factors $V_1$ and $V_2$ with
positive finite normalizers, and impose

$$
V(y+z\theta)=V_1(y)+V_2(z)
$$

globally for every $(y,z)$, including the value $+\infty$ off the effective support. They assert
pathwise preservation of the product, block diagonality of $A_t$, and, for every fixed nontrivial
$E_a=\{z\le a\}$, the forms

$$
\delta_t=d_t\theta,
\qquad G_t=g_t\theta\theta^T,
\qquad K_t=\kappa_t\theta\theta^T.
$$

Thus “rank one” is used structurally and the precise conclusion is rank at most one.

None of the six nodes has a `bounded_by` edge. The only same-ledger dependency is
`cor:generic-degeneracy -> lem:profile-bound`; the lemma is proved in this same dossier, so that
edge is discharged. The other five nodes have no `depends_on` entry. In particular, the Gaussian
proof derives its balanced-posterior estimate directly and does not assume the open stopped-
centroid hypothesis merely because its conclusion is described using
`thm:centroid-implies-kls`. No open, conditional, or preprint-unreviewed premise enters the
dependency closure. No numerical artifact is cited or used.

### Profile curvature

For `lem:profile-bound`, the stated smooth minimizing-branch, free-boundary, and twice-
differentiable-profile hypotheses supply an admissible unit-normal variation. With
$P=I(p)>0$, the checked first and second variations are

$$
v'(0)=P,
\qquad P'(0)=\lambda P,
\qquad v''(0)=\lambda P,
\qquad P''(0)=-\mathfrak K_{\Sigma_p}+\lambda^2P.
$$

The last formula includes the lateral support term in
$\mathfrak K_{\Sigma_p}=-\mathcal I_{\Sigma_p}(1,1)$. Since $v'(0)>0$, the volume parameter has
a local inverse. For $\Psi=P\circ v^{-1}$ the full second-order chain rule gives

$$
\Psi''(p)
=\frac{P''(0)v'(0)-P'(0)v''(0)}{v'(0)^3}
=-\frac{\mathfrak K_{\Sigma_p}}{P^2};
$$

the two mean-curvature terms cancel. The competitor branch satisfies $I\le\Psi$ with equality at
$p$, so $I''(p)\le\Psi''(p)$ and multiplication by $-P^2$ has the claimed direction.

For `cor:generic-degeneracy`, symmetry and concavity of the log-concave isoperimetric profile
give

$$
h_\nu=2I(1/2),
\qquad \sup_{[1/3,2/3]}I\le h_\nu/2.
$$

If $-I''_{\mathrm{dist}}$ is the nonnegative distributional curvature measure, the endpoint
chord bounds give

$$
(-I''_{\mathrm{dist}})((1/3,2/3))
\le I'_+(1/3)-I'_-(2/3)\le3h_\nu.
$$

The almost-everywhere classical $-I''$ is the density of the absolutely continuous part of this
measure. Applying the preceding lemma wherever both granted regularities hold and integrating
therefore yields the sharper bound

$$
\int_{1/3}^{2/3}\mathfrak K_{\Sigma_p}\,dp
\le\frac{h_\nu^2}{4}\int_{1/3}^{2/3}(-I''(p))\,dp
\le\frac34h_\nu^3.
$$

The stated hypothesis $h_\nu\le1$ is not spent by this calculation; it is harmless route-context
slack and a sharpening opportunity, not a defect. The smooth-minimizer grant is retained, and no
claim about a fixed cut transported under localization is inferred.

### Exact splitting

For `prop:exact-splitting`, on the connected interior of $K_1\times J$ the tensor identity
$\nabla^2V(\theta,\cdot)=0$ says $\partial_z\nabla V=0$. Hence $\partial_zV$ is independent of
$z$, the mixed identities make it independent of $y$, and it is a constant $c$. Integration
gives $V(y,z)=V_1(y)+cz$. Tonelli factorizes the normalizing integral. The one-dimensional
integral of $e^{-cz}$ diverges on $J=\mathbb R$; an unbounded proper interval must be a half-line
with $c\ne0$ in the decaying orientation.

Conversely, for the already split law and $z_0\in\operatorname{int}J$, the cut boundary is the
flat slice $K_1\times\{z_0\}$. Its second fundamental form and the $zz$ Hessian of the log-affine
factor vanish. It misses the endpoints of $J$, and the lateral cylinder has zero support-boundary
curvature in the $\theta$ direction. Thus every term in the constant-mode curvature vanishes.
The proof does not reverse this implication and does not infer global splitting from
$\mathfrak K_\Sigma=0$.

### Persistent splitting

For `prop:persistent-splitting`, properness excludes $-\infty$, so the global extended-real
identity gives exactly

$$
\operatorname{dom}V=\operatorname{dom}V_1\times\operatorname{dom}V_2,
\qquad
\overline{\operatorname{dom}V}
=\overline{\operatorname{dom}V_1}\times\overline{\operatorname{dom}V_2}.
$$

Tonelli and the assumed positive finite factor normalizers then give
$\mu=\mu_1\otimes\mu_2$. This excludes the invalid interpretation in which an additive formula
is asserted only on a nonproduct support.

Writing $c_t=c_t'+c_t''\theta$, orthogonality gives the displayed additive decomposition of
$V_t$. At $t=0$, $c_0=0$ and the factor normalizers are finite and positive by hypothesis. For
$t>0$, completing the square gives the pointwise bounds

$$
e^{c_t'\cdot y-t|y|^2/2}\le e^{|c_t'|^2/(2t)},
\qquad
e^{c_t''z-tz^2/2}\le e^{|c_t''|^2/(2t)}.
$$

Multiplication by $e^{-V_1}$ or $e^{-V_2}$ proves finiteness, and strict positivity of the tilt
proves positivity. Thus the full normalizer is the product of the factor normalizers for every
realized finite $c_t$, and $\mu_t=\mu_{1,t}\otimes\mu_{2,t}$ pathwise. Independence gives the
block form of $A_t$.

The Radon--Nikodym derivative of $\mu_t$ with respect to $\mu$ is finite and strictly positive
on the effective domain, so the two laws are equivalent. Consequently the assumption
$0<\mu(E_a)<1$ implies $0<p_t,q_t<1$ at every realized localized time. Conditioning on $E_a$
or its complement changes only the $z$ factor. The two conditional $y$ means and covariances
therefore agree and the conditional cross-covariances vanish. If $d_t$ and $g_t$ are the
differences of the conditional $z$ means and variances, respectively, then

$$
\delta_t=d_t\theta,
\qquad G_t=g_t\theta\theta^T.
$$

Using the repository definition, with its exact sign,

$$
K_t=G_t+(q_t-p_t)\delta_t\delta_t^T
=\bigl(g_t+(q_t-p_t)d_t^2\bigr)\theta\theta^T.
$$

All conditional first and second moments exist: an integrable log-concave density has finite
moments, and for $t>0$ the Gaussian factor gives the stronger tail bound. Lower semicontinuity
is used to state canonical closed extended-valued factors and their effective support; the
factorization algebra itself only needs the global identity and finite positive normalizers. No
unstated support, integrability, nontriviality, or averaging hypothesis remains.

### Gaussian model

For `prop:gaussian-model`, completing the square gives the posterior mean
$c_t/(1+t)$ and deterministic covariance $A_t=(1+t)^{-1}I$. Hence
$\int_0^T\lambda_{\max}(A_t)\,dt=\log(1+T)\le T$.

Under the repository's balanced-cut convention $p_0=1/2$, covariance decomposition gives
$B_t\preceq A_t$ and therefore

$$
\mathbb E[p]_{T\wedge\tau}
=\mathbb E\int_0^{T\wedge\tau}s_tr_t\,dt
\le\frac14\int_0^T\lambda_{\max}(A_t)\,dt\le\frac T4.
$$

The exit displacement is $1/6$, so Doob's $L^2$ inequality gives
$\mathbb P(\tau\le T)\le36(T/4)=9T$. At $T\le1/18$, survival has probability at least one
half. The published isoperimetric comparison for the $T$-strongly log-concave posterior and the
fixed-cut perimeter supermartingale then give the claimed time-zero boundary conclusion. This is
a direct model proof; it does not consume the open general stopped-centroid assumption.

Every posterior is a translate of a scalar-covariance Gaussian, so Gaussian isoperimetry makes
every finite-level halfspace an exact minimizer at its posterior mass and $e_t(E)=0$. Direct
truncated-normal integration gives

$$
|\delta_t|=\frac{\sigma_t\varphi(\alpha_t)}{s_t},
\qquad
r_t=\frac{\sigma_t^2\varphi(\alpha_t)^2}{s_t}.
$$

The dossier's quarter-disk comparison proves
$\operatorname{erf}(x)^2\le1-e^{-2x^2}$, equivalently
$\varphi(\alpha)^2\le(2/\pi)\Phi(\alpha)\Phi(-\alpha)$. Thus
$r_t\le(2/\pi)\sigma_t^2$. Substitution into the definition of $D_t$ gives

$$
D_t=2\sigma_t^2r_t-r_t^2
\ge(2-2/\pi)\sigma_t^2r_t>0
$$

for every nontrivial halfspace. The strict inequality correctly excludes only the degenerate
infinite-level cuts.

### Product model

For `prop:products`, the Gaussian-linear tilt separates coordinatewise. The one-dimensional
normalizers are positive and finite by the same completing-the-square bound used above, so the
posterior is a product for every realized tilt and $A_t$ is diagonal. Independence eliminates
all cross-coordinate terms in the covariance SDE, leaving

$$
dA_t^{(i)}=m_{3,t}^{(i)}\,dW_t^{(i)}-(A_t^{(i)})^2dt.
$$

Each variance is therefore a nonnegative local supermartingale, hence a supermartingale. Initial
one-dimensional isotropy gives $A_0^{(i)}=1$, and the nonnegative-supermartingale maximal
inequality yields
$\mathbb P(\sup_{s\le t}A_s^{(i)}\ge\lambda)\le1/\lambda$ for $\lambda\ge1$.

The Poincar\'e constant tensorizes, the published one-dimensional log-concave estimate gives
$C_{\mathrm P}(\mu_t^{(i)})\le C A_t^{(i)}$, and the published reverse
Cheeger--Poincar\'e comparison under log-concavity gives

$$
h_{\mu_t}\ge c C_{\mathrm P}(\mu_t)^{-1/2}
\ge c\bigl(\max_iA_t^{(i)}\bigr)^{-1/2}
=c\lambda_{\max}(A_t)^{-1/2}.
$$

At $t=0$ this is dimension-free by isotropy. Adding the nonnegative profile excess gives the
claimed direct cutwise propagation without a bootstrap.

### Citation accounting

The variational and isoperimetric inputs were checked against their actual sources. Bayle 2004,
the journal version of Bayle--Rosales (Indiana University Mathematics Journal 54 (2005), DOI
`10.1512/IUMJ.2005.54.2575`), Rosales 2014, Bobkov 1999, Milman 2009, and the
Bakry--Gentil--Ledoux 2014 monograph are published. They support, respectively, the profile
upper-barrier/second-variation method including convex-boundary terms, the weighted free-boundary
index form, concavity and one-dimensional log-concave estimates, Gaussian/strong-convexity
isoperimetry, and the reverse Cheeger--Poincar\'e comparison used here.

The repository entry `BayleRosales2003` points to the arXiv version of the subsequently published
paper just identified, so it has no preprint debt. `LeeVempala2018` is a preprint-unreviewed survey,
but no result from that survey is a logical premise: the two standard facts beside that citation
were independently verified in the published Bobkov and Bakry--Gentil--Ledoux sources. Excluding
the redundant survey leaves every external premise published. No numerical agreement is used as
evidence.

### Standalone build and structural check

From `solutions/`, both the required command

```text
latexmk -pdf -outdir=../build kls-geometry-models.tex
```

and a forced rebuild with `-g -interaction=nonstopmode -halt-on-error` returned exit code zero.
The latter produced a five-page PDF. The unresolved cross-subfile labels and citation destinations
are the expected standalone warnings; there is no TeX error. Before this report was added,
`python3 research/check_ledger.py` reported 0 errors for 180 nodes and 648 labels.

## Corrections

None. The unused assumption $h_\nu\le1$ and the redundant Lee--Vempala survey citation are
sharpening/editorial opportunities only; neither changes a theorem or supplies an unresolved
premise.

## Exclusions

This review does not prove existence or smoothness of the minimizing branches assumed in the
profile statements. It does not certify a converse from $\mathfrak K_\Sigma=0$ to global
splitting, a quantitative almost-splitting or Obata theorem, control of a localization-tracked cut
by the averaged profile branch, an all-cut Carleson estimate, or any result in
`solutions/kls-product-covariance.tex`. It certifies no nearby remark, route claim, bibliography
metadata, numerical artifact, or node outside the six listed in the front matter. Updating the
dossier header and ledger certification pointers is outside this reviewer's write surface.

Every proof step within the declared six-node scope was verified; there is no unverified step
inside that scope.
