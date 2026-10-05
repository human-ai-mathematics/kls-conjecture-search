---
numbering:
  enumerator: "10.%s"
---

(sec:cmh-normalization)=
# The moment map, normalization layer: CMH made precise, its Hodge content, and gate zero

Section [](#sec:moment-map-cmh) said what normalizing the schematic estimate $\norm{\Sigma^{-1/2}H\nabla g}_2^2\le4\norm{-Lg}_2^2$ requires ([](#rem:cmh-normalization)): every object in it fixed, so that the resulting statement implies a universal Poincaré bound. This section does so. The estimate is named, its operator data are fixed, the reduction to the affine Poincaré inequality is [](#thm:cmh-implies-affine-poincare), and three structural consequences are recorded that were not visible while the endpoint was a schema:

- an exact weighted Hodge decomposition showing that CMH dominates the affine Poincaré constant and contains an additional solenoidal channel in dimension at least two; this manuscript does not decide whether that channel makes CMH genuinely stronger than KLS ([](#prop:cmh-hodge), [](#cor:cmh-hodge-comparison));

- a necessary linear-sector condition, *gate zero*, which is an operator-to-trace upgrade of exactly the kind catalogued in [](#rem:trace-upgrade-unification), and which [](#thm:letwin-moment-map) does not supply by matrix algebra alone ([](#conj:gate-zero), [](#prop:letwin-not-gate-zero)). Its natural sharp form, the operator version of the Chen–Klartag trace bound, is [](#conj:gate-zero-sharp), and the constant $4$ is not the natural one for this sector;

- an exact resolution of that sector. The gate matrix's quadratic form splits as one plus a quarter of the squared directional third moment plus a named high-mode remainder ([](#lem:linear-sector-third-moment)), so any gate-zero constant already contains a directional third-moment bound ([](#cor:gate-zero-third-moment)) and the sharp form is at least as strong as the sharp third-moment estimate. The spectral resolution of the three gate matrices that the anisotropic-bootstrap approach works from is [](#lem:cmh-linear-spectral-resolution).

Throughout, $\mu$ is centered, full-dimensional and log-concave with covariance $\Sigma=\Cov_\mu\succ0$, and $\varphi$, $\nu$, $H$ are the moment-map data of [](#eq:moment-measure)–[](#eq:MA) in Section [](#sec:family-moment-map), transported to target coordinates as in [](#eq:stein-kernel-def). Regularity is assumed only to justify pointwise calculation; Appendix-level conventions for the weighted divergence, the closed forms, and the affine covariance are collected in §[](#subsec:cmh-conventions).

(subsec:cmh-definition)=
## The Stein generator and the CMH constant

Recall the affine Poincaré constant

```{math}
:label: eq:affine-poincare-constant
\CPaff(\mu)
=\sup_{f\in H^1(\mu),\,f\not\equiv\mathrm{const}}
\frac{\Var_\mu f}{\E_\mu\inner{\Sigma\nabla f}{\nabla f}},
```

so that [](#conj:kls) is the assertion that $\CPaff$ is bounded by a universal constant over all dimensions and all log-concave $\mu$.

Transporting the source diffusion [](#eq:calL-def) to the target gives the *Stein generator*

```{math}
:label: eq:stein-generator
L_\mu g=\Div_\mu(H\nabla g)=\Tr(HD^2g)-p\cdot\nabla g,
\qquad \Div_\mu u=\rho^{-1}\Div(\rho u),
```

where $\rho$ is the density of $\mu$. With the sign convention that $\Aop=-L_\mu\ge0$, the associated Dirichlet form is

```{math}
:label: eq:stein-dirichlet-form
-\E_\mu[fL_\mu g]=\E_\mu\inner{H\nabla f}{\nabla g}.
```

That $L_\mu$ is symmetric for $\mu$ — rather than for some auxiliary measure — is exactly the Stein-kernel identity $\Div_\mu H=-p$ of [](#eq:stein-identity); it is what makes the following definition canonical rather than a choice.

:::{prf:proposition} Integrated Bochner identity for the Stein generator
:label: prop:cmh-bochner
For $g$ in the operator core,

```{math}
:label: eq:cmh-bochner
\E_\mu(L_\mu g)^2
=\E_\mu\!\left[\inner{H\nabla g}{\nabla g}+\Tr(HD^2g\,HD^2g)\right].
```
:::

*Proof.* One integration by parts in target coordinates against the Stein identity, on a smooth compactly supported core, followed by a graph-norm Cauchy argument that carries the identity to the operator-core closure. The calculation is carried out in Appendix [](#sec:appendix-moment-map).

For $\mu$ Gaussian, $H=\Id$ and [](#eq:cmh-bochner) specializes to the familiar Ornstein–Uhlenbeck identity $\E(Lg)^2=\E[\abs{\nabla g}^2+\norm{D^2g}_{\HS}^2]$. This is a calibration of the formula; the proof above is analytic and uses no numerical evidence.

:::{prf:definition} The canonical moment-Hessian constant
:label: def:cmh
The *canonical moment-Hessian constant* of $\mu$ is

```{math}
:label: eq:cmh-constant
\CMH(\mu)
=\sup_{g\in\Dom(\Aop)\setminus\ker\Aop}
\frac{\E_\mu\inner{H\nabla g}{\Sigma^{-1}H\nabla g}}{\E_\mu(L_\mu g)^2}.
```

The assertion $\CMH(\mu)\le C$ is written $\mathrm{CMH}(C)$. Here $L^2$ means $L^2(\mu)$, $\Aop=-L_\mu$ is the nonnegative self-adjoint operator of the closed form [](#eq:stein-dirichlet-form), and every inverse is the pseudoinverse on $(\ker\Aop)^\perp$. For a measure supported on a proper affine subspace — the simplex laws of Section [](#sec:cmh-exact-cases) are the case of interest — $\Sigma^{-1}$ denotes the inverse on that affine tangent space, equivalently the Moore–Penrose inverse in ambient coordinates.
:::

Writing $K=-\Div_\mu(H\Sigma^{-1}H\nabla\,\cdot\,)$, the definition is the quadratic-form comparison $K\preceq C\Aop^2$, equivalently the second-order Riesz-transform bound

```{math}
:label: eq:cmh-riesz
\norm{\Sigma^{-1/2}H\nabla\Aop^{-1}}_{L^2(\mu)\to L^2(\mu;\R^n)}\le\sqrt C.
```

This is the precise content of the schema [](#eq:cmh4-schema): $\Sigma$ is the covariance, $L$ is the Stein generator [](#eq:stein-generator), the measure is $\mu$ itself, and the admissible class is $\Dom(\Aop)$.

(subsec:cmh-implies)=
## CMH implies the affine Poincaré inequality

:::{prf:theorem} CMH bounds the affine Poincaré constant, normalized as in [](#rem:cmh-normalization)
:label: thm:cmh-implies-affine-poincare
For every centered log-concave $\mu$ in the regular moment-map class described above,

```{math}
:label: eq:cmh-implies-poincare
\CPaff(\mu)\le\CMH(\mu).
```

In particular a universal bound $\CMH\le4$ over all isotropic log-concave measures in all dimensions would prove [](#conj:kls) with affine Poincaré constant $4$.
:::

*Proof.* Test the quotient on centered functions in $\R+C_c^\infty$, a class that lies in both form domains because the Stein normalization $\E_\mu H=\Sigma$ bounds the $H$-energy by $\Tr\Sigma$; then a two-parameter cut-off and a density step in $H^1_\Sigma(\mu)$. The density step is where care is needed, and it never asserts that finite $\Sigma$-energy forces finite $H$-energy when $H$ is unbounded. The calculation is carried out in Appendix [](#sec:appendix-moment-map).

The proof uses no Bochner identity, no positivity of the Monge–Ampère remainder, and no property of $H$ beyond symmetry, positivity, and $\Div_\mu H=-p$. That economy is the reason the constant transfers with no loss: the reduction is exactly one Cauchy–Schwarz.

(subsec:cmh-hodge)=
## The Hodge content: the affine channel and the solenoidal excess

Let

$$
\Aop_1=-\Div_\mu(\Sigma\nabla\,\cdot\,)
$$

denote the closed nonnegative covariance generator on $L^2(\mu)$, and write $L^2_0(\mu)=(\ker\Aop_1)^\perp$.

:::{prf:proposition} Weighted Hodge identity
:label: prop:cmh-hodge
Let $g\in\Dom(\Aop)$ be such that $u=H\nabla g\in L^2(\mu;\Sigma^{-1})$, and set

$$
h=\Aop g=-\Div_\mu u\in L^2_0(\mu),\qquad
\psi=\Aop_1^{-1}h,\qquad
w=u-\Sigma\nabla\psi,
$$

where

$$
\Aop_1^{-1}:L^2_0(\mu)\longrightarrow
\Dom(\Aop_1)\cap L^2_0(\mu)
$$

is the inverse on the centered subspace. Then $\Div_\mu w=0$, the fields $\Sigma\nabla\psi$ and $w$ are orthogonal in $L^2(\mu;\Sigma^{-1})$, and

```{math}
:label: eq:cmh-hodge
\E_\mu\inner{u}{\Sigma^{-1}u}
=\E_\mu\inner{\Sigma\nabla\psi}{\nabla\psi}
+\E_\mu\inner{w}{\Sigma^{-1}w}.
```

Moreover,

$$
\sup_{0\ne h\in L^2_0(\mu)}
\frac{\E_\mu\inner{\Sigma\nabla\Aop_1^{-1}h}
{\nabla\Aop_1^{-1}h}}
{\norm h_2^2}
=\CPaff(\mu).
$$
:::

:::{prf:proof}
Weighted integration by parts gives $\E\inner{\Sigma\nabla\psi}{\Sigma^{-1}w}=\E\inner{\nabla\psi}{w}=-\E[\psi\Div_\mu w]=0$, and expanding the square proves [](#eq:cmh-hodge). For the last claim, $\psi=\Aop_1^{-1}h$ and $\E\inner{\Sigma\nabla\psi}{\nabla\psi}=\inner{h}{\Aop_1^{-1}h}$; the supremum over $h$ of the ratio to $\norm{h}_2^2$ is $\norm{\Aop_1^{-1}}$, which is $\CPaff(\mu)$ by [](#eq:affine-poincare-constant).
:::

:::{prf:corollary} The exact Hodge consequence
:label: cor:cmh-hodge-comparison
$\Sigma\nabla\psi$ is the least-$L^2(\Sigma^{-1})$ field with divergence $-h$, and by [](#prop:cmh-hodge) controlling it *is* the affine Poincaré inequality. CMH demands in addition that the solenoidal excess $w$ be paid for within the same budget.

In dimension one a square-integrable divergence-free field with the no-flux convention of §[](#subsec:cmh-conventions) vanishes identically, so $w=0$ and CMH degenerates exactly to the Poincaré inverse-divergence problem — this is why [](#thm:cmh-1d) is an identity rather than an inequality. In every dimension the decomposition proves the exact comparison

$$
\CMH(\mu)\ge\CPaff(\mu).
$$

In dimension at least two the divergence-free subspace is nontrivial, so the identity displays an additional channel that CMH must control.
:::

:::{prf:remark} What the Hodge identity does not prove
The identity does *not* show that this channel is nonzero for a CMH extremizing sequence, nor does it exhibit a measure separating CMH from $\CPaff$. Thus $\mathrm{CMH}(4)$ is sufficient for KLS with constant $4$ ([](#thm:cmh-implies-affine-poincare)), and this manuscript establishes neither equivalence nor strict nonimplication. $\mathrm{CMH}(4)$ is the target of this approach, not an established reformulation of KLS or a strict strengthening of it.
:::

The product formula below shows that products of one-sided exponentials saturate $\mathrm{CMH}(4)$ with zero slack. [](#cor:cmh-product-saturation) therefore turns the possible solenoidal gap into a concrete perturbative test, but not into a proved separation.

(subsec:gate-zero)=
## Gate zero: the necessary linear-sector condition

Take $g(p)=a\cdot p$ in [](#eq:cmh-constant). Then $D^2g=0$, $L_\mu g=-a\cdot p$, so $\E(L_\mu g)^2=a^\top\Sigma a$ while the numerator is $a^\top\E[H\Sigma^{-1}H]a$. Hence:

:::{prf:conjecture} Gate zero
:label: conj:gate-zero
Every centered log-concave moment measure satisfies

```{math}
:label: eq:gate-zero
\E\bigl[H\Sigma^{-1}H\bigr]\preceq4\Sigma,
```

equivalently $\E H^2\preceq4\Id$ in isotropic position.
:::

This is necessary for universal $\mathrm{CMH}(4)$ and is not a known consequence of KLS. It is the cheapest falsifiable consequence of the whole approach: a single matrix expectation, with no test function and no operator inverse. A measure with $\lmax(\Sigma^{-1/2}\E[H\Sigma^{-1}H]\Sigma^{-1/2})>4$ would disprove $\mathrm{CMH}(4)$ without disproving [](#conj:kls).

:::{prf:remark} Gate zero is a trace-upgrade problem
:label: rem:gate-zero-trace-upgrade
[](#thm:chen-klartag-moment-hessian) gives $\E_\nu\norm{H}_{\HS}^2\le2n$, that is $\Tr(\E H^2)\le2n$: the *average* eigenvalue of $\E H^2$ is already at most $2$ in isotropic position. Gate zero asks for the *largest* eigenvalue to be at most $4$. It is therefore an operator-to-trace upgrade carrying a factor-$2$ budget.
:::

The trace bound is sharp — products of centered exponentials give $\Tr(\E H^2)=2n$ exactly — so the constant $4$ in [](#eq:gate-zero) is not the natural one for the linear sector. The natural statement is the operator form of the Chen–Klartag inequality.

:::{prf:conjecture} Sharp gate zero
:label: conj:gate-zero-sharp
Every centered log-concave moment measure satisfies

```{math}
:label: eq:gate-zero-sharp
\E\bigl[H\Sigma^{-1}H\bigr]\preceq2\,\Sigma,
```

equivalently $\E H^2\preceq2\,\Id$ in isotropic position.
:::

[](#conj:gate-zero-sharp) refines [](#conj:gate-zero) and implies it, and its trace is exactly [](#thm:chen-klartag-moment-hessian). Its equality set is not small: products of centered exponentials attain [](#eq:gate-zero-sharp) in every direction, and every exponential cone measure of Section [](#subsec:cmh-cones) attains it in its axis direction ([](#prop:cone-linear-sector)), with the constant strictly below $2$ on the same family as soon as the radial exponent moves off the cone value. The constant $2$ is half the CMH constant $4$: on the line, $\E\tau^2=2$ for the centered exponential while $\CMH=4$ by [](#thm:cmh-1d), so the linear sector saturates at half the full constant. By [](#cor:gate-zero-third-moment) below, the sharp form would improve the directional third-moment bound of [](#prop:letwin-kappa) from $\kappa_n\le2\sqrt2$ to the sharp $\kappa_n\le2$; it is therefore at least as strong as a sharp third-moment estimate, which calibrates its difficulty.

The linear sector's three gate matrices can be resolved spectrally. In isotropic source coordinates write $Q_{\rm lin}(\mu):=\lmax(\mathsf N)$ for the linear CMH quotient, $\mathsf N=\int H^2\,d\eta$, and write $(\mathrm{AB})_{\rho,\beta}$ for the anisotropic-bootstrap inequality $\mathsf R\succeq\rho\mathsf N-\beta I$ with $\mathsf R=\mathsf N-\mathsf D$ as in the lemma below; its sharp form is $(\rho,\beta)=(\tfrac12,0)$, which is equivalent to [](#conj:gate-zero-sharp) together with the high-mode excess bound recorded in the lemma. In the lemma, $A=H\,(D^2V\circ\nabla\psi)\,H$ and $Q_{k\ell}=\Tr(H^{-1}\partial_kH\,H^{-1}\partial_\ell H)$ are the two nonnegative terms of [](#eq:differentiated-MA), and $\sum_bM_{ab}u_b$ abbreviates $\sum_b(M_a)_{\cdot b}u_b$.

:::{prf:lemma} Spectral resolution of the linear-sector gate matrices
:label: lem:cmh-linear-spectral-resolution
For a regular isotropic compact-target moment map with source potential $\psi$, source density $e^{-\psi}$, and Stein generator $\mathsf A_{\rm op}=-\mathcal L$ in source coordinates, where $\mathcal Lf=e^{\psi}\operatorname{div}(e^{-\psi}H^{-1}\nabla f)$ and $H=D^2\psi$: the functions $u_b=\partial_b\psi$ are centered orthonormal eigenfunctions of $\mathsf A_{\rm op}$ at its Brascamp–Lieb spectral gap $1$; the columns $Ha=\nabla\langle a,\nabla\psi\rangle$ lie in the form domain $\Dom(\calE)$ and satisfy the column equation in the weak form $\calE(f,(Ha)_i)=\langle f,(Ha)_i\rangle-\langle f,((A+Q)a)_i\rangle$ for every bounded smooth finite-energy $f$, with $(A+Q)a\in L^1(\eta)$ orthogonal to every $u_b$ and $\int(A+Q)\,d\eta=I$; and, with the induced decomposition $Ha=a+\sum_bM_{ab}u_b+v$, the gate matrices $\mathsf N=\int H^2$, $\mathsf D=\int H^{ab}(\partial_aH)(\partial_bH)$, $\mathsf R=\mathsf N-\mathsf D$ resolve as

$$
a^T\mathsf Na=1+\norm{M_a}^2+\norm v^2,\qquad
a^T\mathsf Da=\norm{M_a}^2+\langle v,\mathsf A_{\rm op}v\rangle,\qquad
a^T\mathsf Ra=1-\langle v,(\mathsf A_{\rm op}-1)v\rangle ,
$$

where $\langle v,\mathsf A_{\rm op}v\rangle$ denotes the closed-form value $\calE(v,v)$. Consequently $\mathsf R\preceq I$, with equality in a direction exactly when the column fluctuation is spectrally pure at the gap; the bootstrap $(\mathrm{AB})_{\rho,\beta}$ is equivalent to the channel inequality $\langle v,(\mathsf A_{\rm op}-1)v\rangle+\rho(\norm{M_a}^2+\norm v^2)\le1+\beta-\rho$ for all unit $a$; $\mathsf R\succeq\mathsf N-nI$ holds unconditionally, so $Q_{\rm lin}\le n+1$; and $\mathsf R\succeq\mathsf D$ holds for every regular finite product of one-dimensional laws.
:::

The gap-mode part of the column decomposition above has a description that needs no source coordinates at all. Write

$$
T_3(\mu)=\bigl(\E_\mu[X_iX_jX_k]\bigr)_{i,j,k},
\qquad
T_3(a)=\E_\mu\bigl[\inner Xa\,X\otimes X\bigr],
$$

for the third-moment tensor and its contraction with $a\in\R^n$, so that the directional third-moment parameter of [](#eq:kappa-def) is $\kappa_n=\sup_{\mu,\theta}\norm{T_3(\theta)}_{\HS}$.

:::{prf:lemma} The linear sector and the third moment
:label: lem:linear-sector-third-moment
Let $\mu$ be an isotropic log-concave probability on $\R^n$ which is the moment measure of a convex $\varphi\in C^2(\R^n)$ with $\E_\nu\norm{D^2\varphi}_{\HS}^2<\infty$, and let $\tau=\tau_\mu$ be its canonical Stein kernel [](#eq:stein-kernel-def). Then for every $a\in\R^n$ the column $\tau a$ decomposes orthogonally in $L^2(\mu;\R^n)$ as

$$
\tau a=a+\tfrac12\,T_3(a)\,X+v_a,
\qquad
\E_\mu[v_a]=0,\qquad \E_\mu[v_a\otimes X]=0,
$$

and consequently

```{math}
:label: eq:linear-sector-third-moment
\E_\mu\abs{\tau a}^2=\abs a^2+\tfrac14\norm{T_3(a)}_{\HS}^2+\E_\mu\abs{v_a}^2 .
```

Equivalently, $\E_\nu[\partial_{ij}\varphi\,\partial_k\varphi]=\tfrac12\,\E_\mu[X_iX_jX_k]$; when moreover $\varphi\in C^3$ with $D^3\varphi\in L^1(\nu)$, this says that the gap-mode coefficient tensor $\E_\nu[\partial_{ijk}\varphi]$ of [](#lem:cmh-linear-spectral-resolution) is one half of the third-moment tensor.
:::

The identity $\E_\nu[\partial_{ijk}\varphi]=\tfrac12\E_\mu[X_iX_jX_k]$ is Lemma 3.7 of [@ChenKlartag2026SharpThinShell], and the orthogonal decomposition above is the exact form of the Bessel step in the proof of their Theorem 1.2; what is added here is the directional statement with the remainder $v_a$ named. The compact-target regular class of [](#thm:regular-moment-map-compact-target) satisfies the hypothesis, since its Hessian is bounded [@Klartag2013MomentMeasures]; so does every exponential cone measure of Section [](#subsec:cmh-cones), whose kernel [](#eq:cone-stein-kernel) is the Gamma radial variable times a matrix bounded by the same result applied to the base. For a symmetric $\mu$ the third moment vanishes and the entire gate-zero content is the high-mode term $\E\abs{v_a}^2$; for a product of centered exponentials the high-mode term vanishes and the entire content is the third moment.

:::{prf:corollary} Gate zero controls the directional third moment
:label: cor:gate-zero-third-moment
Under the hypotheses of [](#lem:linear-sector-third-moment), for every unit vector $a$,

$$
\norm{T_3(a)}_{\HS}^2
\le4\bigl(a^\top\E_\mu[\tau^2]\,a-1\bigr)
\le4\bigl(\lmax(\E_\mu\tau^2)-1\bigr).
$$

In particular, on any class of such measures with $\E\tau^2\preceq c\,\Id$, every directional third moment satisfies $\norm{T_3(a)}_{\HS}\le2\sqrt{c-1}$: gate zero [](#eq:gate-zero) gives $2\sqrt3$ and the sharp form [](#eq:gate-zero-sharp) gives $2$, which products of centered exponentials attain. Conversely, any isotropic law in the class with $\norm{T_3(a)}_{\HS}>2\sqrt3$ for some unit $a$ refutes gate zero.
:::

Summing the corollary over an orthonormal basis recovers $\norm{T_3(\mu)}_{\HS}^2\le4(\Tr\E\tau^2-n)\le4n$, the chain in the proof of Theorem 1.2 of [@ChenKlartag2026SharpThinShell]. [](#cor:gate-zero-third-moment) places gate zero relative to the literature input it does not use: gate zero at constant $c$ contains a directional third-moment bound at $2\sqrt{c-1}$, so any proof of [](#eq:gate-zero-sharp) proves a sharper constant than [](#thm:letwin-qcts) supplies, and any proof of [](#eq:gate-zero) must at least reproduce a bound of that type. The reverse channel is what makes the corollary a falsification tool: it is a lower bound on the gate matrix that needs no moment map, only third moments.

:::{prf:remark} Relation to the shared trace-upgrade difficulty
Gate zero belongs to the same difficulty family as [](#conj:trace-upgrade), the high-rank part of [](#conj:stein-weighted), and [](#conj:product-alignment); no equivalence is asserted, exactly as in [](#rem:trace-upgrade-unification). The practical consequence is a split verdict: gate zero is cheap to *test* on a model and is expected to be as hard to *prove* as the rest of the program.
:::

% Agent note: research/lib/README.md records the numerical channel for testing gate zero on models.

(subsec:gate-zero-countermodel)=
## Why the constant-matrix estimate cannot supply gate zero

In isotropic position define the positive self-adjoint superoperator $\calT(B)=\E[HBH]$ on symmetric matrices with the Hilbert–Schmidt inner product. [](#thm:letwin-moment-map) says $\calT\preceq2\,\Id$; gate zero asks instead for $\calT(\Id)=\E H^2\preceq4\,\Id$. The two differ by the order of the noncommuting factors, and the gap is exactly one commutator:

```{math}
:label: eq:static-commutator
\Tr(B^2H^2)=\Tr(BHBH)+\tfrac12\norm{[B,H]}_{\HS}^2
\qquad(B,H\ \text{symmetric}).
```

Indeed $[B,H]$ is antisymmetric, so $\norm{[B,H]}_{\HS}^2=-\Tr([B,H]^2)=2\Tr(B^2H^2)-2\Tr(BHBH)$. The first term of [](#eq:static-commutator) is what Letwin's theorem controls; the second is the *static transverse commutator*, and the following shows it is genuinely unconstrained by matrix moments.

:::{prf:proposition} Algebraic countermodel
:label: prop:letwin-not-gate-zero
For every $m\ge18$ there is a random positive semidefinite $(m+1)\times(m+1)$ matrix $H$ with $\E H=\Id$ and

$$
\E\Tr(BHBH)\le2\Tr(B^2)\quad\text{for every symmetric }B,
$$

yet $\lmax(\E H^2)>4$.
:::

:::{prf:proof}
Let $z$ be uniform on $S^{m-1}$ and set

$$
d=\frac m{\sqrt{2m-1}},\qquad c=1-\frac dm,\qquad
H(z)=\begin{pmatrix}1&\sqrt d\,z^\top\\\sqrt d\,z&c\,\Id_m+d\,zz^\top\end{pmatrix}.
$$

The Schur complement of the upper-left entry is $c\,\Id_m\succ0$ because $c>0$, so $H\succeq0$; since $\E z=0$ and $\E zz^\top=\Id_m/m$ we get $\E H=1\oplus(c+d/m)\,\Id_m=\Id_{m+1}$.

Write $B=\left(\begin{smallmatrix}a&r^\top\\r&D\end{smallmatrix}\right)$ with $D$ symmetric. Using $\E(z^\top Dz)^2=\bigl((\Tr D)^2+2\Tr(D^2)\bigr)/(m(m+2))$,

$$
\begin{aligned}
\E\Tr(BHBH)
&=a^2+\frac{2d}ma\Tr D+2\Bigl(c+\frac{2d}m\Bigr)\abs r^2\\
&\quad+\Bigl(c^2+\frac{2cd}m+\frac{2d^2}{m(m+2)}\Bigr)\Tr(D^2)
+\frac{d^2}{m(m+2)}(\Tr D)^2.
\end{aligned}
$$

Writing $D=t\,\Id_m+D_0$ with $\Tr D_0=0$ splits the form into three $O(m)$-invariant sectors that do not interact: the cross-vector sector, the traceless-$D$ sector, and the two-dimensional scalar sector $(a,t)$. Comparing with $2\Tr(B^2)=2a^2+4\abs r^2+2\Tr(D^2)$ sector by sector: the vector coefficient is $2(c+2d/m)=2(1+d/m)\le4$ since $d\le m$; the traceless coefficient is $c^2+2cd/m+2d^2/(m(m+2))=1+(m-2)/((2m-1)(m+2))\le2$; and on the scalar sector, using $mc^2+2cd+d^2=m+d^2-d^2/m$, the deficit is

$$
2(a^2+mt^2)-\E\Tr(BHBH)=a^2-2dat+\Bigl[m-d^2\Bigl(1-\frac1m\Bigr)\Bigr]t^2=(a-dt)^2\ge0,
$$

the last equality because $d^2(2-1/m)=m$ by the choice $d^2=m^2/(2m-1)$. Hence $\E\Tr(BHBH)\le2\Tr(B^2)$ for every symmetric $B$, with equality on the scalar ray $a=dt$.

Finally $e_1^\top\E H^2e_1=1+d\abs z^2=1+d$, and $1+d>4$ is equivalent to $m^2>9(2m-1)$, i.e. $m^2-18m+9>0$, which holds precisely for $m\ge18$.
:::

:::{prf:remark} Scope of the countermodel
:label: rem:countermodel-scope
The matrices above are *not* claimed to be moment-map Hessians; no Monge–Ampère, Codazzi, or Hessian-compatibility condition is imposed. The proposition proves only that positivity, the normalization $\E H=\Id$, and the constant-matrix estimate [](#eq:letwin-matrix) do not imply gate zero by matrix algebra. Any proof of [](#eq:gate-zero) must therefore consume differential moment-map structure. Equivalently, by [](#eq:static-commutator), it must control $\E\norm{[B,H]}_{\HS}^2$, and [](#prop:letwin-not-gate-zero) exhibits an admissible law where that quantity is maximal on the scalar ray. This is the same obstruction as [](#conj:mm-square-root-commutator) in its most elementary, static, finite-dimensional form.
:::

:::{prf:remark} Gate zero on genuine moment maps
:label: rem:gate-zero-dichotomy
Decide [](#eq:gate-zero). Either prove $\E[H\Sigma^{-1}H]\preceq4\Sigma$ for every log-concave moment measure using differentiated Monge–Ampère structure — which by [](#rem:countermodel-scope) means a dimension-free bound on the static commutator $\E\norm{[B,H]}_{\HS}^2$ for the relevant multiplier class — or exhibit a genuine moment map with $\lmax(\Sigma^{-1/2}\E[H\Sigma^{-1}H]\Sigma^{-1/2})>4$, which refutes $\mathrm{CMH}(4)$ without refuting [](#conj:kls).
:::

(subsec:cmh-conventions)=
## Conventions, domains, and affine covariance

**Weighted divergence and boundary flux.** $\Div_\mu u=\rho^{-1}\Div(\rho u)$. All integrations by parts are justified first for compactly supported fields or fields with vanishing normal flux, and the closed forms are obtained by completion. The no-flux convention is essential in dimension one, where it is what rules out a nonzero constant divergence-free field and forces $w=0$ in [](#cor:cmh-hodge-comparison).

**Closed operators.** $\calE_H(f,g)=\E_\mu\inner{H\nabla f}{\nabla g}$ is closable under the smooth moment-map hypotheses of §[](#subsec:mm-coordinates); $\Aop=-L_\mu$ is its nonnegative self-adjoint operator, and $\Aop^{-1}$ always means the pseudoinverse on $(\ker\Aop)^\perp$. The spectral truncation in the proof of [](#thm:cmh-implies-affine-poincare) avoids assuming a spectral gap.

**Affine covariance.** If $T$ is invertible and $Y=TX$, then $\Sigma_Y=T\Sigma_XT^\top$ and $H_Y(Tx)=TH_X(x)T^\top$; with $g_Y(y)=g_X(T^{-1}y)$ both the numerator and denominator of [](#eq:cmh-constant) are unchanged. Hence $\CMH$ is an invariant of the affine equivalence class, matching the affine invariance of $\CPaff$. For a *noninvertible* map the transported Stein kernel need not be the canonical moment-map kernel of the image, so only the Poincaré-level statement of [](#cor:cmh-linear-images) is available there.

**Conditional closure for general log-concave measures.** The argument behind [](#prop:cmh-approximation-closure) runs at the Poincaré level as follows. For an arbitrary centered log-concave $\mu$, centered Gaussian-convolution, Gaussian-tilt, and growing-ball approximants $\mu_q$ belong to the published compact-target regular class of [](#thm:regular-moment-map-compact-target) and converge to $\mu$ in ambient $W_2$ with second moments, hence $\Sigma_q\to\Sigma$. If $\sup_q\CMH(\mu_q)\le C$, then for every smooth compactly supported $f$,

$$
\Var_{\mu_q}f\le C\int\inner{\Sigma_q\nabla f}{\nabla f}\,d\mu_q.
$$

Both sides converge because $f$ and $\nabla f$ are bounded and continuous and the covariances converge. Intrinsic smooth-core density on $S=\operatorname{Ran}\Sigma$ extends the inequality to the closed covariance-form relaxation $H^1_\Sigma(\mu)$, while $\Sigma$ and $\Sigma^+$ annihilate ambient normal derivatives. This gives constant-preserving closure, including singular covariance. It does not give the uniform premise and asserts no continuity of $\CMH$.

:::{prf:lemma} Affine Poincaré lower semicontinuity along regular recovery
:label: lem:affine-poincare-w2-liminf
Every centered log-concave probability $\mu$ admits centered, full-dimensional, compactly-supported regular moment-map approximants $\mu_k$ such that $W_2(\mu_k,\mu)\to0$ in the original ambient coordinates and

```{math}
:label: eq:affine-poincare-w2-liminf
\CPaff(\mu)\le\liminf_{k\to\infty}\CPaff(\mu_k),
```

including when the limit is carried by a proper affine subspace. The limit passage uses only the covariance Dirichlet forms; it asserts neither convergence nor lower semicontinuity of $\CMH$.
:::

:::{prf:proposition} CMH recovery calculus
:label: prop:cmh-recovery-calculus
For a centered log-concave probability $\mu$ in a declared ambient Euclidean space, define its CMH recovery envelope by

$$
\mathfrak R_{\rm CMH}(\mu)
:=\inf_{(\mu_k)}
\liminf_{k\to\infty}\CMH(\mu_k),
$$

where the infimum runs over centered, full-dimensional, compactly supported regular moment-map laws in that ambient space with $W_2(\mu_k,\mu)\to0$. Then:

(i) $\CPaff(\mu)\le\mathfrak R_{\rm CMH}(\mu)$;

(ii) $\mathfrak R_{\rm CMH}$ is invariant under invertible linear maps, is nonincreasing under singular square linear limits in the same ambient dimension, and satisfies

$$
\mathfrak R_{\rm CMH}(\mu_1\otimes\cdots\otimes\mu_m)
\le\max_i\mathfrak R_{\rm CMH}(\mu_i);
$$

(iii) an intrinsic recovery sequence on a proper affine support with envelope at most $C$ extends to an ambient full-dimensional recovery sequence with envelope at most $\max\{C,1\}$ by tensoring compact Gaussian normal factors whose scale vanishes.

Consequently the envelope equals $1$ for centered Gaussian laws and equals $4$ for finite products of one-dimensional log-concave laws containing a centered one-sided-exponential factor. It is at most $4$ for invertible linear images, same-ambient singular square linear images, and affine-support embeddings of finite products built from one-dimensional log-concave laws and uniform-simplex blocks. This calculus does not assert a universal bound for arbitrary log-concave laws and therefore does not discharge [](#ass:cmh-recovery-envelope).
:::

:::{prf:assumption} Bounded CMH recovery envelope
:label: ass:cmh-recovery-envelope
There is a universal $C$ such that every centered log-concave probability $\mu$ has at least one regular recovery sequence as in [](#lem:affine-poincare-w2-liminf) satisfying

$$
\liminf_{k\to\infty}\CMH(\mu_k)\le C.
$$

Only one well-chosen recovery sequence is required; no uniform bound over every regularization parameter or every canonical approximation family is assumed.
:::

:::{prf:corollary} One CMH recovery sequence suffices
:label: cor:cmh-recovery-sequence-suffices
Under [](#ass:cmh-recovery-envelope), every centered log-concave probability satisfies $\CPaff(\mu)\le C$. In particular the assumption implies [](#conj:kls).
:::
