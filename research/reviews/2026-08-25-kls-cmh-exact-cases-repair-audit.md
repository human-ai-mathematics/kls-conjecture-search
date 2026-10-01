---
verdict: pass
authors:
  - kls_ledger_audit, unknown, 2026-08-25
reviewer: cmh_exact_reviewer, unknown, 2026-08-25
fingerprints:
  solutions/thm-cmh-dirichlet.md: a6fde7b910a21d73f2f4a4e56de2a660eda18f47ecab1b12ac44f34dea04661c
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
  thm:cmh-implies-affine-poincare: a977e03d84125ce8a015dfb75d67908808162ecd70b71221781d8a750ec5d9c4
  cor:cmh-product-saturation: 2a3ba80b8cfea460f74c0dbcf122eeafdcf31576b42e60cf7d5507106f2332af
  prop:cmh-hodge: e53f8f0d21ff4afad0be69fb034e09db1f7daaa882338a1d927af40c3117410e
---

*Follows up* `research/explorations/2026-08-25-kls-cmh-normalization-audit.md`.

# Route C exact CMH cases — independent repair audit

The original proof author was `/orchestrator/kls-cmh-normalization`; `/root/kls_ledger_audit`
authored the certified repair. The audit also compared the dossier with
`modules/kls/42-cmh-exact-cases.tex`.

## Certified scope

This follow-up review certifies the repaired proofs and statements of exactly these ten nodes:

1. `thm:cmh-1d` — the identity
   $\CMH(\mu)=\CP(\mu)/\operatorname{Var}(\mu)$, the one-dimensional log-concave bound, and
   sharpness at the centered one-sided exponential.
2. `thm:cmh-product` — the exact maximum formula for block products and its invertible-affine
   consequence.
3. `cor:cmh-linear-images` — closure of the affine Poincaré inequality under products and
   arbitrary linear images, including convolution.
4. `lem:cmh-gamma-completion` — the exact Gamma row completion and the sign of $\delta_i$.
5. `lem:cmh-row-min` — the constrained Hessian-row minimum obtained from differentiated
   homogeneity.
6. `lem:cmh-angular-coefficient` — the sharp two-branch scalar lower bound for $F_A$.
7. `thm:cmh-dirichlet` — $\mathrm{CMH}(4)$ for every log-concave Dirichlet law.
8. `cor:cmh-dirichlet-surplus` — the strict quantitative surplus for every $A>3$, including
   the two-coordinate case.
9. `cor:cmh-dirichlet-poincare` — the affine Poincaré consequences for Dirichlet laws and
   their products, linear images, and convolutions.
10. `cor:cmh-product-saturation` — exact product-exponential saturation together with the explicit
    statement that perturbative instability of the full CMH quotient remains open.

The dossier header enumerates exactly these ten ledger nodes. Each id occurs exactly once as a
manuscript `\label`, and the dossier versions, manuscript statements, and current ledger
statements agree semantically. The shared dossier legitimately refines the Route C program as a
single tightly coupled exact-case package. No `bounded_by` obstruction applies: in particular,
the Dirichlet argument uses the full Hessian row and not a radial-only or projection-only test.

## Independent mathematical checks

### One dimension, products, and linear images

For `thm:cmh-1d`, I checked directly that $u=\tau f'$ is the unique zero-flux solution of
$D_\mu^*u=h$ for $h=-L_\mu f$. If $v=(D_\mu^*D)^{-1}h$, uniqueness gives $u=Dv$ and hence

$$
 \lVert u\rVert_2^2
 =\langle h,(D_\mu^*D)^{-1}h\rangle.
$$

Taking the operator norm on the centered subspace gives $\CP(\mu)$; division by the scalar
covariance gives the displayed CMH identity. For $X=Y-1$, $Y\sim\operatorname{Exp}(1)$, the
printed test functions satisfy

$$
 \frac{\operatorname{Var}(e^{aY})}{\mathbb E|a e^{aY}|^2}
 =\frac1{(1-a)^2}\longrightarrow4,
$$

so the sharp example is centered and the lower bound is exact. The repaired text also gives the
primary Kannan--Lovász--Simonovits attribution and identifies Cattiaux--Guillin as a secondary
pointer, rather than attributing sharpness to the secondary source.

For `thm:cmh-product`, conditioning gives the factor inequality block by block. Two independent
integrations by parts give, for $i\ne j$,

$$
 \mathbb E[(L_i g)(L_j g)]
 =\mathbb E\lVert H_i^{1/2}D^2_{ij}gH_j^{1/2}\rVert_{\mathrm{HS}}^2\ge0.
$$

Thus $\sum_i\mathbb E(L_i g)^2\le\mathbb E(\sum_iL_i g)^2$; testing functions of one block
proves the reverse inequality for the supremum. The repaired manuscript correctly calls the
$L_i$ nonpositive. Standard variance tensorization with block covariance, followed by the
chain rule $\nabla(f\circ T)=T^\top\nabla f$, proves `cor:cmh-linear-images` without requiring
$T$ to be invertible. This is correctly distinguished from CMH invariance, which is asserted
only for invertible affine maps.

### Dirichlet normalization and the Gamma lift

I re-derived the softmax pushforward on the quotient and obtained

$$
 H(p)=\frac1A C(p),\qquad L_\mu=\frac1A L_\alpha,
$$

together with the stated covariance. For tangent $v$, the vector
$A(A+1)\operatorname{diag}(\alpha)^{-1}v$ solves $\Sigma x=v$, so

$$
 v^\top\Sigma^\dagger v=A(A+1)\sum_i\frac{v_i^2}{\alpha_i}.
$$

Consequently the CMH quotient is exactly $A(A+1)d_\alpha/n_\alpha$; all powers of $A$ in the
manuscript and dossier are correct.

For the Gamma completion, integration by parts gives

$$
 \mathbb E[Y^2uu']=-\frac12\mathbb E[((a+1)Y-Y^2)u^2].
$$

Expanding the completed diagonal square therefore subtracts
$a^2(a+1)^{-2}D_i$ from the $i$th Bochner row. Summing the rows and subtracting $D_\Gamma/4$
gives the claimed identity with
$\delta_i=\alpha_i^2/(\alpha_i+1)^2-1/4\ge0$ exactly when $\alpha_i\ge1$. The repaired
discussion correctly limits this sign observation to the product-Gamma consequence and records
that the Dirichlet proof consumes $\alpha_i\ge1$ again in the angular lemma.

Differentiating Euler's identity gives $\sum_jY_jG_{ij}=-G_i$. With the dossier's variables
$t_j$, the reciprocal quadratic weights sum to $S/Y_i$, so constrained Cauchy--Schwarz gives
exactly

$$
 R_i\ge\frac{Y_i}{S}\left(1+\frac{Y_i}{\alpha_i+1}\right)^2|G_i|^2.
$$

The lift dictionary $\mathcal L_\Gamma G=S^{-1}L_\alpha g$ and
$Y_iG_i=u_i(P)$ is also exact. Independence of $S$ and $P$ then yields
$N_\Gamma=n_\alpha/z_A$ and $D_\Gamma=d_\alpha$ with
$z_A=(A-1)(A-2)$.

### Angular minimization, main theorem, and surplus

For fixed $a$, the $p$-dependent part of $F_A$ is minimized at $p=1$ when
$\sqrt z\le a+1$ and at $p=(a+1)/\sqrt z$ otherwise. When $z\le4$, the boundary expression is
increasing in $a$ and its minimum at $a=1$ is $A-1+z/4$. When $z\ge4$, writing
$r=a/(a+1)$ makes the interior expression increasing in $r$; its minimum at $a=1$ is
$A-2+\sqrt z$. The complementary boundary region is increasing from the common interface, so
it cannot lower that value. These are precisely
$A-1/2+s_A$ in the two printed branches, and $s_A\ge0$ for $A\ge3$.

After adding the exact $\delta_iD_i$ term to the integrated row bound, multiplication by
$z_A\alpha_i$ gives the printed $F_A(\alpha_i,P_i)$ with no residual term. Substitution of the
angular bound and the identity

$$
 \frac{z_A}{4}+A-\frac12=\frac{A(A+1)}4
$$

then gives

$$
 n_\alpha(g)\ge\left(\frac{A(A+1)}4+s_A\right)d_\alpha(g).
$$

The branch condition is now correct: the Gamma proof uses only $A\ge3$, not $m\ge3$.
Therefore it applies to $m=2$ whenever $A\ge3$, and in particular proves the stated strict
surplus for every two-coordinate law with $A>3$. Only $m=2$, $A<3$ is sent to the
one-dimensional theorem. Since $z_A>2$ for $A>3$, the printed $s_A$ is strictly positive and
the equivalent CMH ceiling follows by exact rearrangement.

### Closure, prior-art scope, and saturation

The closure paragraph is adequate at the endpoint $A=3$. For a degree-zero lift of a simplex
polynomial, $G_i=O(S^{-1})$ and $G_{ij}=O(S^{-2})$ near the common Gamma origin. The weighted
second-order terms therefore have radial order at worst $S^{-2}$ against the Gamma radial
density $S^{A-1}\,dS$, which is integrable exactly for $A>2$. Radial cutoff errors have the
same vanishing $O(\varepsilon^{A-2})$ scale. Coordinate-face fluxes vanish for
$\alpha_i\ge1$, and polynomial Wright--Fisher eigenspaces form an operator core. Thus the
Gamma identities pass to the homogeneous lift and then to the closed $L_\alpha$ domain. The
residual $m=2$, $A<3$ case is correctly handled by the one-dimensional no-flux closure.

The aggregation formula in the manuscript was also recomputed and is correct. It is a
consistency check, not an input to the theorem.

The prior-art paragraph now makes the required conservative claim: qualitative
dimension-free KLS results for simplices and conservative Gamma systems are acknowledged, with
Kolesnikov--Milman §1.2 explicitly used as a secondary pointer; the text identifies the exact
constant, surplus, and CMH-level estimate as the content of this proof without making a broader
priority assertion.

Finally, products of centered one-sided exponentials have $\CMH=4$ exactly by the certified
one-dimensional identity and product formula. The repaired saturation remark draws no
perturbative inference from the nonnegative Hodge term alone: it records all quantities that
vary and leaves the full second variation as `conj:cmh-second-variation`. Thus exact product
saturation is certified while perturbative instability and universal $\mathrm{CMH}(4)$ remain
open.

## Semantic and mechanical validation

- Compared every certified manuscript statement with its dossier theorem/lemma and current KLS
  ledger statement; no hypothesis, constant, dimension range, or conclusion differs.
- Checked all ten manuscript labels occur exactly once.
- Forced a standalone rebuild of `solutions/thm-cmh-dirichlet.tex`; it succeeds. Its unresolved
  manuscript references are the standalone behavior expressly allowed by `solutions/README.md`.
- Rebuilt `main.tex`; the full 149-page manuscript succeeds with no undefined references or
  citations.
- Ran `python3 research/check_ledger.py`. Its then-current failures were certification wiring to
  the historical partial report (and the separately repaired normalization dossier), not a
  structural or mathematical failure of any exact-case statement. This new report supplies the
  replacement exact-case review artifact; ledger and dossier provenance rewiring is reserved to
  the orchestrator.

## Explicit exclusions

This audit does not recertify the upstream normalization nodes `def:cmh`,
`thm:cmh-implies-affine-poincare`, or `prop:cmh-hodge`; it uses their displayed statements as
the declared dependencies of the exact-case dossier. It does not certify universal
$\mathrm{CMH}(4)$, `conj:gate-zero`, `conj:cmh-second-variation`, the separate Bessel-zero
formula in `rem:cmh-dirichlet-sharp`, or any numerical `finum` artifact. It checks the accuracy
and restraint of the prior-art hedge, but makes no exhaustive novelty claim.

These exclusions do not qualify the verdict for any of the ten nodes listed in the opening
metadata.
