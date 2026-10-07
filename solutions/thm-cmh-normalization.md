---
title: 'The moment-Hessian inequality, its operator data, and $\CPaff\le\CMH$'
label: sec:sol-cmh-normalization
ledger-node:
- prop:cmh-bochner
- thm:cmh-implies-affine-poincare
- prop:cmh-hodge
- cor:cmh-hodge-comparison
- prop:letwin-not-gate-zero
numbering:
  enumerator: D30.%s
---

*Part of the moment-map mechanism, Chapter [](#sec:cmh-normalization); the reading order is on the [full proofs](#sec:proofs-moment-map) page.*

**Overview.** This dossier fixes the operator data of Route C, which answers [](#rem:cmh-normalization). It proves the Bochner identity [](#prop:cmh-bochner), the endpoint reduction [](#thm:cmh-implies-affine-poincare) ($\CPaff\le\CMH$), the Hodge decomposition [](#prop:cmh-hodge) with its consequence [](#cor:cmh-hodge-comparison), and the algebraic countermodel [](#prop:letwin-not-gate-zero). The work is done in the regular moment-map class. The reduction is a spectral duality argument. $\mathrm{CMH}(4)$ itself is not proved, and neither is a strict nonimplication between CMH and KLS. The passage beyond the regular class is only a conditional template, deferred to [](#prop:cmh-approximation-closure).

1. The Stein identity $\Div_\mu H=-p$ makes $L_\mu$ symmetric and nonpositive with Dirichlet form $\E\inner{H\nabla f}{\nabla g}$ ([](#lem:sol-cmh-dirichlet)).
2. Bochner identity: $\E(L_\mu g)^2=\E[\inner{H\nabla g}{\nabla g}+\Tr(HD^2gHD^2g)]$. It uses the total symmetry [](#eq:sol-cmh-codazzi) of the moment map ([](#prop:sol-cmh-bochner)) and is not needed for step 3.
3. Endpoint: pairing $f$ with the spectrally truncated $\Aop^{-1}f$ and applying Cauchy–Schwarz gives $\CPaff\le\CMH$ ([](#thm:sol-cmh-implies)). This uses only step 1.
4. Hodge: $H\nabla g$ splits orthogonally into $\Sigma\nabla\Aop_1^{-1}h$ and a divergence-free $w$ ([](#prop:sol-cmh-hodge)), using [](#eq:sol-cmh-a1-inverse). The first channel is exactly $\CPaff$, and $w$ is the only possible gap ([](#cor:sol-cmh-strictly-stronger)).
5. Linear test functions show that $\mathrm{CMH}(4)$ implies gate zero. [](#lem:sol-static-commutator) isolates the commutator. An explicit random $H\succeq0$ with $\E H=\Id$ satisfies the Letwin matrix bound but has $\lmax(\E H^2)>4$ for $m\ge18$ ([](#prop:sol-countermodel)). It is not claimed to be a moment-map Hessian, so [](#conj:gate-zero) is not refuted ([](#cor:sol-countermodel-scope)).

**Scope.** This dossier discharges [](#rem:cmh-normalization) of Chapter [](#sec:moment-map-cmh): it fixes every operator datum in the schematic Route C endpoint $\norm{\Sigma^{-1/2}H\nabla g}_2^2\le4\norm{-Lg}_2^2$ and proves the reduction to the affine Poincaré inequality. It then proves two structural facts about the resulting statement: that it dominates the affine Poincaré constant and has an additional solenoidal channel in dimension at least two (without proving a strict nonimplication), and that its linear-sector consequence is not implied by Letwin's constant-matrix estimate through matrix algebra alone. It does *not* prove $\mathrm{CMH}(4)$, which remains open ([](#conj:gate-zero) is only its necessary linear sector).

**Standing hypotheses.** $\mu$ is a centered, full-dimensional log-concave probability measure on $\R^n$ with density $\rho=e^{-V}/Z$ and covariance $\Sigma=\Cov_\mu\succ0$, lying in the regular moment-map class of §[](#subsec:mm-coordinates): the moment potential $\varphi$ of [](#eq:moment-measure) is smooth and strictly convex, $\nabla\varphi$ is a diffeomorphism, and the integrations by parts below are justified for compactly supported fields or fields of vanishing normal flux, the general case following by completion. $H$ is the moment-map Hessian in target coordinates [](#eq:stein-kernel-def), so that $H=H^\top\succ0$, $\Div_\mu H=-p$, and $\E_\mu H=\Sigma$. The final paragraph records a conditional limiting template. Existence of approximants with all the required uniformity, affine-support control, and limiting core density is the separate open [](#prop:cmh-approximation-closure), not a theorem of this dossier.

## 1\. The operator data

Define the Stein generator and its nonnegative form

$$
L_\mu g=\Div_\mu(H\nabla g)=\Tr(HD^2g)-p\cdot\nabla g,
\qquad \Aop=-L_\mu,
\qquad \Div_\mu u=\rho^{-1}\Div(\rho u).
$$

:::{prf:lemma} Symmetry and the Dirichlet form
:label: lem:sol-cmh-dirichlet
For $f,g$ smooth with the flux convention above, $-\E_\mu[fL_\mu g]=\E_\mu\inner{H\nabla f}{\nabla g}$. In particular $L_\mu$ is symmetric and nonpositive on $L^2(\mu)$, the form $\calE_H(f,g)=\E_\mu\inner{H\nabla f}{\nabla g}$ is closable, and $\Aop$ is its nonnegative self-adjoint operator.
:::

:::{prf:proof}
$\E_\mu[fL_\mu g]=\int f\Div(\rho H\nabla g)=-\int\rho\inner{H\nabla f}{\nabla g}$ by the divergence theorem and the vanishing flux. Symmetry and nonpositivity follow from $H=H^\top$ and $H\succ0$; closability of a densely defined nonnegative symmetric form with smooth positive coefficients is standard.
:::

That the *same* measure $\mu$ appears in the form and in the generator is exactly the Stein identity $\Div_\mu H=-p$; this is what makes [](#def:cmh) canonical rather than a choice of reference measure.

:::{prf:definition}
$\CMH(\mu)$ is defined by [](#eq:cmh-constant), with $L^2=L^2(\mu)$, admissible class $\Dom(\Aop)\setminus\ker\Aop$, and every inverse the pseudoinverse on $(\ker\Aop)^\perp$. For $\mu$ supported on a proper affine subspace, $\Sigma^{-1}$ is the inverse on the affine tangent space, equivalently the Moore–Penrose inverse in ambient coordinates.
:::

## 2\. The Bochner identity

:::{prf:proposition} = [](#prop:cmh-bochner)
:label: prop:sol-cmh-bochner
For $g$ in the core, $\E_\mu(L_\mu g)^2=\E_\mu\bigl[\inner{H\nabla g}{\nabla g}+\Tr(HD^2g\,HD^2g)\bigr]$.
:::

:::{prf:proof}
We calculate in target coordinates, use Einstein summation, and first take $g$ in a smooth compactly supported core. The Stein identity and the generator formula are

$$
\partial_i(\rho H_{ij})=-\rho p_j,
\qquad L_\mu g=H_{k\ell}g_{k\ell}-p_k g_k.
$$

Integrating once and differentiating $L_\mu g$ gives

$$
\begin{aligned}
\E_\mu(L_\mu g)^2
={}&\E_\mu[H_{ij}g_i g_j]
-\E_\mu[H_{ij}g_j(\partial_iH_{k\ell})g_{k\ell}]\\
&-\E_\mu[H_{ij}g_jH_{k\ell}g_{ik\ell}]
+\E_\mu[H_{ij}g_jp_k g_{ik}].
\end{aligned}
$$

Integrating the third-derivative term in $p_k$ gives

$$
\begin{aligned}
-\E_\mu[H_{ij}g_jH_{k\ell}g_{ik\ell}]
={}&-\E_\mu[p_\ell H_{ij}g_jg_{i\ell}]
+\E_\mu[H_{k\ell}(\partial_kH_{ij})g_jg_{i\ell}]\\
&+\E_\mu[H_{k\ell}H_{ij}g_{jk}g_{i\ell}].
\end{aligned}
$$

The first term on the right cancels the preceding $p_k$ term after relabelling, and the last one is $\Tr(HD^2g\,HD^2g)$.

The remaining cancellation is exactly where the moment-map structure enters. If $p=\nabla\varphi(y)$ and $H_{k\ell}(p)=\varphi_{k\ell}(y)$, then

```{math}
:label: eq:sol-cmh-codazzi
H_{mj}\partial_jH_{k\ell}
=H_{mj}(H^{-1})_{rj}\varphi_{k\ell r}
=\varphi_{mk\ell},
```

which is totally symmetric in $m,k,\ell$. Hence the two residual terms are

$$
\E_\mu[g_jg_{i\ell}\varphi_{\ell ij}]
-\E_\mu[g_jg_{k\ell}\varphi_{jk\ell}]=0.
$$

This proves the identity on the smooth core. If $g_q$ is graph-norm Cauchy there, apply the identity to $g_q-g_r$. Since its two right-hand terms are nonnegative, $H^{1/2}\nabla g_q$ and $H^{1/2}D^2g_qH^{1/2}$ are Cauchy in their respective $L^2$ spaces. Their limits define the closed right-hand side, and passage to the limit proves the identity on the operator-core closure.
:::

For $\mu$ Gaussian, $H=\Id$ and the proposition specializes to the familiar Ornstein–Uhlenbeck identity $\E(Lg)^2=\E[\abs{\nabla g}^2+\norm{D^2g}_{\HS}^2]$. This is a calibration of the formula; the proof above is analytic and uses no numerical evidence.

:::{prf:remark} Calibration and role
[](#prop:sol-cmh-bochner) is *not* used in the endpoint reduction below. It is recorded because it exhibits the CMH denominator as a sum of two nonnegative pieces, which is what makes the pointwise criterion $\CMH\le\operatorname*{ess\,sup}\lmax(\Sigma^{-1/2}H\Sigma^{-1/2})$ available. The total symmetry in [](#eq:sol-cmh-codazzi) is the only place moment-map structure enters. For a general positive symmetric Stein kernel the same calculation leaves an additional $\partial H$ term with no prescribed sign, so neither this equality nor a one-sided replacement follows from the Stein identity alone.
:::

## 3\. The endpoint reduction

:::{prf:theorem} = [](#thm:cmh-implies-affine-poincare)
:label: thm:sol-cmh-implies
$\CPaff(\mu)\le\CMH(\mu)$. In particular $\mathrm{CMH}(C)$ implies $\Var_\mu f\le C\,\E_\mu\inner{\Sigma\nabla f}{\nabla f}$ for every $f\in H^1(\mu)$.
:::

:::{prf:proof}
Write $C=\CMH(\mu)$; the assertion is automatic if $C=\infty$. Let $\mathscr C$ be the restrictions to $\operatorname{supp}\mu$ of $\R+C_c^\infty(\R^n)$ and first take a centered $f\in\mathscr C$. This class lies in both form domains even when $H$ is globally unbounded: the Stein normalization $\E_\mu H=\Sigma$ gives

$$
\E_\mu\inner{H\nabla f}{\nabla f}
\le \norm{\nabla f}_\infty^2\E_\mu\Tr H
=\norm{\nabla f}_\infty^2\Tr\Sigma<\infty.
$$

For $0<\eps<R<\infty$ put

$$
\Pi_{\eps,R}=\one_{[\eps,R]}(\Aop),
\qquad g_{\eps,R}=\Pi_{\eps,R}\Aop^{-1}f\in\Dom(\Aop).
$$

Then $\Aop g_{\eps,R}=\Pi_{\eps,R}f$. Since $f$ is in the $H$-form domain and $g_{\eps,R}\in\Dom(\Aop)$, the form–operator pairing and [](#lem:sol-cmh-dirichlet) give

$$
\begin{aligned}
\norm{\Pi_{\eps,R}f}_2^2
&=\inner{f}{\Pi_{\eps,R}f}_{L^2}
=\inner{f}{\Aop g_{\eps,R}}_{L^2}
=\E_\mu\inner{\nabla f}{H\nabla g_{\eps,R}}\\
&\le\Bigl(\E_\mu\inner{\Sigma\nabla f}{\nabla f}\Bigr)^{1/2}
\Bigl(\E_\mu\inner{H\nabla g_{\eps,R}}
{\Sigma^{-1}H\nabla g_{\eps,R}}\Bigr)^{1/2}\\
&\le C^{1/2}
\Bigl(\E_\mu\inner{\Sigma\nabla f}{\nabla f}\Bigr)^{1/2}
\norm{\Pi_{\eps,R}f}_2.
\end{aligned}
$$

After division (unless the projected norm is zero, when the conclusion is immediate) and squaring,

$$
\norm{\Pi_{\eps,R}f}_2^2
\le C\E_\mu\inner{\Sigma\nabla f}{\nabla f}.
$$

Because $H\succ0$ and the support is connected, the kernel of $\Aop$ consists of the constants. Thus $f\perp\ker\Aop$, and the spectral theorem gives $\Pi_{\eps,R}f\to f$ in $L^2$ as $R\to\infty$ and then $\eps\downarrow0$.

For completeness, let $H^1_\Sigma(\mu)$ be the closure of $\mathscr C$ for the norm $\norm f_2^2+\E_\mu\inner{\Sigma\nabla f}{\nabla f}$. Since $\Sigma\succ0$ is constant, this is the usual $H^1(\mu)$ in the present regular setting. Approximate an arbitrary $f\in H^1_\Sigma(\mu)$ by functions in $\mathscr C$ and subtract their means. Variances and $\Sigma$-energies converge, so the inequality passes to the limit. Crucially, this argument does not claim that finite $\Sigma$-energy places $f$ in the $H$-form domain when $H$ is unbounded.
:::

:::{prf:remark} What the proof does and does not use
Only three properties of $H$ enter: symmetry, positivity, and $\Div_\mu H=-p$. Neither log-concavity, nor the Monge–Ampère positivity [](#eq:differentiated-MA), nor [](#prop:sol-cmh-bochner) is used. Consequently the constant transfers with no loss, and the same reduction applies verbatim to any positive symmetric Stein kernel, not only the moment-map one.
:::

## 4\. The Hodge content: the affine channel and the solenoidal excess

Let

$$
\Aop_1=-\Div_\mu(\Sigma\nabla\,\cdot\,)
$$

be the closed nonnegative self-adjoint operator associated with the covariance form

$$
\calE_\Sigma(f,k)=\E_\mu\inner{\Sigma\nabla f}{\nabla k},
\qquad \Dom(\calE_\Sigma)=H^1_\Sigma(\mu),
$$

and set $L^2_0(\mu)=(\ker\Aop_1)^\perp$. The support is connected and $\Sigma\succ0$, so $\ker\Aop_1$ consists of the constants. Moreover $\CPaff(\mu)<\infty$ for each fixed full-dimensional log-concave probability measure (only a dimension-free bound is open). Consequently the restriction of $\Aop_1$ to $L^2_0(\mu)$ has a bounded, everywhere-defined inverse

```{math}
:label: eq:sol-cmh-a1-inverse
\Aop_1^{-1}:L^2_0(\mu)\longrightarrow
\Dom(\Aop_1)\cap L^2_0(\mu).
```

:::{prf:proposition} = [](#prop:cmh-hodge)
:label: prop:sol-cmh-hodge
Let $g\in\Dom(\Aop)$ be such that $u=H\nabla g\in L^2(\mu;\Sigma^{-1})$, and set

$$
h=\Aop g=-\Div_\mu u\in L^2_0(\mu),\qquad
\psi=\Aop_1^{-1}h,\qquad
w=u-\Sigma\nabla\psi.
$$

Then $\Div_\mu w=0$,

$$
\E_\mu\inner{u}{\Sigma^{-1}u}
=\E_\mu\inner{\Sigma\nabla\psi}{\nabla\psi}+\E_\mu\inner{w}{\Sigma^{-1}w},
$$

and

$$
\sup_{0\ne h\in L^2_0(\mu)}
\frac{\E_\mu\inner{\Sigma\nabla\Aop_1^{-1}h}
{\nabla\Aop_1^{-1}h}}
{\norm h_2^2}
=\CPaff(\mu).
$$
:::

:::{prf:proof}
Put $\mathscr H_\Sigma=L^2(\mu;\Sigma^{-1})$ and let

$$
G_\Sigma:H^1_\Sigma(\mu)\subset L^2(\mu)\longrightarrow\mathscr H_\Sigma,
\qquad G_\Sigma f=\Sigma\nabla f.
$$

This is a densely defined closed operator, its adjoint is the weak weighted divergence $G_\Sigma^*=-\Div_\mu$, and $\Aop_1=G_\Sigma^*G_\Sigma$. Here the assertion $h=-\Div_\mu u\in L^2$ means precisely that $u\in\Dom(G_\Sigma^*)$ and $G_\Sigma^*u=h$: the usual integration-by-parts identity is first valid on the smooth core and extends to $H^1_\Sigma(\mu)$ by closed-form density. Since $\psi\in\Dom(\Aop_1)$ and $\Aop_1\psi=h$, we also have $G_\Sigma\psi\in\Dom(G_\Sigma^*)$ and $G_\Sigma^*G_\Sigma\psi=h$. Therefore

$$
w=u-G_\Sigma\psi\in\Dom(G_\Sigma^*),
\qquad G_\Sigma^*w=h-h=0,
$$

which is the weak statement $\Div_\mu w=0$. The required integration by parts is now the adjoint identity at exactly these domains:

$$
\E_\mu\inner{\Sigma\nabla\psi}{\Sigma^{-1}w}
=\inner{G_\Sigma\psi}{w}_{\mathscr H_\Sigma}
=\inner{\psi}{G_\Sigma^*w}_{L^2(\mu)}=0.
$$

Thus $G_\Sigma\psi$ and $w$ are orthogonal in $\mathscr H_\Sigma$, and expanding $u=G_\Sigma\psi+w$ gives the displayed Hodge identity. The same argument shows minimality: if $v\in\Dom(G_\Sigma^*)$ and $G_\Sigma^*v=h$, then $v-G_\Sigma\psi\in\ker G_\Sigma^*$ and hence

$$
\norm v_{\mathscr H_\Sigma}^2
=\norm{G_\Sigma\psi}_{\mathscr H_\Sigma}^2
+\norm{v-G_\Sigma\psi}_{\mathscr H_\Sigma}^2.
$$

Finally, for every $h\in L^2_0(\mu)$,

$$
\E_\mu\inner{\Sigma\nabla\psi}{\nabla\psi}
=\norm{G_\Sigma\psi}_{\mathscr H_\Sigma}^2
=\inner{\Aop_1\psi}{\psi}_{L^2(\mu)}
=\inner{h}{\Aop_1^{-1}h}_{L^2(\mu)}.
$$

The spectral theorem for the positive self-adjoint restriction of $\Aop_1$ to $L^2_0(\mu)$ therefore gives

$$
\sup_{0\ne h\in L^2_0(\mu)}
\frac{\inner{h}{\Aop_1^{-1}h}}{\norm h_2^2}
=\norm{\Aop_1^{-1}}
=\left(
\inf_{\substack{0\ne f\in H^1_\Sigma(\mu)\\ f\perp\ker\Aop_1}}
\frac{\calE_\Sigma(f,f)}{\norm f_2^2}
\right)^{-1}
=\CPaff(\mu),
$$

where the last equality is exactly the variational definition [](#eq:affine-poincare-constant). This also verifies that no integration by parts has been applied outside the form/operator domains declared above.
:::

:::{prf:corollary} Exact consequence of the Hodge decomposition
:label: cor:sol-cmh-strictly-stronger
$\Sigma\nabla\psi$ is the minimal-$L^2(\Sigma^{-1})$ field with divergence $-h$, and controlling it is precisely the affine Poincaré inequality. Hence $\CMH(\mu)\ge\CPaff(\mu)$, and $\mathrm{CMH}(C)$ implies $\CPaff(\mu)\le C$. The only possible gap in the Hodge identity is the solenoidal excess $\E\inner{w}{\Sigma^{-1}w}$. In dimension one the no-flux convention forces $w=0$, so $\CMH=\CP/\Var$ exactly. In dimension at least two the divergence-free subspace is nontrivial, but the decomposition alone neither proves that $w$ contributes at a CMH extremizer nor gives a measure for which $\CMH>\CPaff$. Equivalence and strict nonimplication therefore remain open; in particular this corollary does not prove that $\mathrm{CMH}(4)$ can fail while KLS holds.
:::

## 5\. Gate zero and the algebraic countermodel

Testing [](#eq:cmh-constant) on $g(p)=a\cdot p$ (so $D^2g=0$, $L_\mu g=-a\cdot p$) gives $\E(L_\mu g)^2=a^\top\Sigma a$ and numerator $a^\top\E[H\Sigma^{-1}H]a$. Hence $\mathrm{CMH}(4)$ implies *gate zero*, $\E[H\Sigma^{-1}H]\preceq4\Sigma$, i.e. $\E H^2\preceq4\Id$ in isotropic position ([](#conj:gate-zero)).

:::{prf:lemma} The static commutator
:label: lem:sol-static-commutator
For symmetric $B,H$: $\Tr(B^2H^2)=\Tr(BHBH)+\tfrac12\norm{[B,H]}_{\HS}^2$.
:::

:::{prf:proof}
$[B,H]^\top=(BH-HB)^\top=HB-BH=-[B,H]$, so $[B,H]$ is antisymmetric and $\norm{[B,H]}_{\HS}^2=\Tr([B,H][B,H]^\top)=-\Tr([B,H]^2)$. Expanding $[B,H]^2=BHBH-BH^2B-HB^2H+HBHB$ and taking traces gives $\Tr([B,H]^2)=2\Tr(BHBH)-2\Tr(B^2H^2)$.
:::

:::{prf:proposition} = [](#prop:letwin-not-gate-zero)
:label: prop:sol-countermodel
For every $m\ge18$ there is a random $H\succeq0$ of size $(m+1)$ with $\E H=\Id$ and $\E\Tr(BHBH)\le2\Tr(B^2)$ for all symmetric $B$, yet $\lmax(\E H^2)\ge1+d>4$ where $d=m/\sqrt{2m-1}$.
:::

:::{prf:proof}
Let $z$ be uniform on $S^{m-1}$, $d=m/\sqrt{2m-1}$, $c=1-d/m$, and $H(z)=\left(\begin{smallmatrix}1&\sqrt d\,z^\top\\ \sqrt d\,z&c\Id_m+d\,zz^\top\end{smallmatrix}\right)$.

*Positivity.* $c>0$ since $d/m=1/\sqrt{2m-1}<1$, and the Schur complement of the $(1,1)$ entry is $c\Id_m+d\,zz^\top-d\,zz^\top=c\Id_m\succ0$; hence $H\succeq0$.

*Normalization.* $\E z=0$ kills the off-diagonal blocks and $\E zz^\top=\Id_m/m$ gives $\E H=1\oplus(c+d/m)\Id_m=\Id_{m+1}$.

*The quadratic form.* With $B=\left(\begin{smallmatrix}a&r^\top\\r&D\end{smallmatrix}\right)$, expanding $\Tr(BHBH)$ and using $\E z=0$, $\E zz^\top=\Id_m/m$ and $\E(z^\top Dz)^2=\bigl((\Tr D)^2+2\Tr(D^2)\bigr)/(m(m+2))$,

$$
\begin{aligned}
\E\Tr(BHBH)&=a^2+\tfrac{2d}ma\Tr D+2\bigl(c+\tfrac{2d}m\bigr)\abs r^2\\
&\quad+\Bigl(c^2+\tfrac{2cd}m+\tfrac{2d^2}{m(m+2)}\Bigr)\Tr(D^2)
+\tfrac{d^2}{m(m+2)}(\Tr D)^2 .
\end{aligned}
$$

Decompose $D=t\Id_m+D_0$ with $\Tr D_0=0$. Then $\Tr D=mt$ and $\Tr(D^2)=mt^2+\Tr(D_0^2)$, so the form splits into three $O(m)$-invariant sectors that do not interact: the vector sector $\abs r^2$, the traceless sector $\Tr(D_0^2)$, and the two-dimensional scalar sector $(a,t)$.

*Vector sector.* Coefficient $2(c+2d/m)=2(1+d/m)$, to be compared with $4$ from $2\Tr(B^2)$. Since $d\le m$ (equivalently $\sqrt{2m-1}\ge1$), it is at most $4$.

*Traceless sector.* Coefficient $c^2+2cd/m+2d^2/(m(m+2))$. Substituting $c=1-d/m$ and $d^2=m^2/(2m-1)$ gives $1+\frac{m-2}{(2m-1)(m+2)}$, which is $\le2$ for all $m\ge1$; the comparison value is $2$.

*Scalar sector.* With $r=0$, $D=t\Id_m$, the above reduces to $\E\Tr(BHBH)=a^2+2dat+t^2\bigl(mc^2+2cd+d^2\bigr)$, and $mc^2+2cd+d^2=m-2d+\tfrac{d^2}m+2d-\tfrac{2d^2}m+d^2=m+d^2-\tfrac{d^2}m$. Hence the deficit is

$$
2(a^2+mt^2)-\E\Tr(BHBH)=a^2-2dat+\Bigl[m-d^2\Bigl(1-\tfrac1m\Bigr)\Bigr]t^2 .
$$

The choice $d^2=m^2/(2m-1)$ is exactly $d^2(2-\tfrac1m)=m$, i.e. $m-d^2(1-\tfrac1m)=d^2$, so the deficit equals $(a-dt)^2\ge0$ — a perfect square, vanishing on the ray $a=dt$.

Combining the three sectors, $\E\Tr(BHBH)\le2\Tr(B^2)$ for every symmetric $B$.

*Failure of gate zero.* $(H^2)_{11}=1+d\abs z^2=1+d$ deterministically, so $e_1^\top\E H^2e_1=1+d$. Now $1+d>4\iff d>3\iff m^2>9(2m-1)\iff m^2-18m+9>0$, whose positive root is $9+6\sqrt2\approx17.49$; hence the inequality holds exactly for integers $m\ge18$.
:::

:::{prf:corollary} Scope
:label: cor:sol-countermodel-scope
The law above is not claimed to be a moment-map Hessian: no Monge–Ampère or Codazzi compatibility is imposed, and the proposition does not refute [](#conj:gate-zero). What it proves is that positivity, $\E H=\Id$, and [](#eq:letwin-matrix) do not imply gate zero by matrix algebra. By [](#lem:sol-static-commutator) the residual quantity any proof must control is $\E\norm{[B,H]}_{\HS}^2$, and here it is maximal on the scalar ray $a=dt$ where the Letwin deficit vanishes identically.
:::

**Obstructions respected.** Route C carries no `bounded_by` edges: the six obstruction statements of the manuscript are scoped by their own statements to the fixed-cut Eldan program. The one with a method-level reach beyond it, `rem:projection-ceiling`, forbids proving quadratic-chaos thin shell from radial or projection information alone; nothing above uses projection tests — the endpoint reduction is a duality argument and the countermodel is exact finite-dimensional algebra. [](#rem:gate-zero-trace-upgrade) records that gate zero is an operator-to-trace upgrade of the same family as `conj:trace-upgrade` and `conj:product-alignment`; per the single-owner discipline of `CLAUDE.md`, no claim of equivalence with those nodes is made here.

**Numerical status.** The `cmh-gate-zero` numerics target computes $\lmax(\Sigma^{-1/2}\E[H\Sigma^{-1}H]\Sigma^{-1/2})$ in closed form on one-dimensional laws, products, and from exact moment matrices on the Dirichlet family, and regression-tests the sector identities of [](#prop:sol-countermodel). Only an exact rational certificate may refute [](#conj:gate-zero); floating eigenvalues and Galerkin optima are directional. The current battery lies inside already-proved classes and contributes nothing to the analytic theorems above.

**Conditional template beyond the regular class.** Let $\mu_q$ be the regular approximants from §[](#subsec:mm-audit), chosen so that $\mu_q\to\mu$ with second moments and therefore $\Sigma_q\to\Sigma$. If $\sup_q\CMH(\mu_q)\le C$, [](#thm:sol-cmh-implies) applied to a fixed $f\in C_c^\infty$ gives

$$
\Var_{\mu_q}f\le C\int\inner{\Sigma_q\nabla f}{\nabla f}\,d\mu_q.
$$

The two sides converge because $f$ and $\nabla f$ are bounded and continuous and the second moments converge. Subject to a limiting $H^1_\Sigma(\mu)$ core-density theorem, the endpoint argument then extends the inequality to the full Sobolev domain. No continuity of $\CMH$ is used or claimed. A complete proof must still construct approximants with the asserted moment and affine-support behavior and justify this density passage; those obligations are precisely [](#prop:cmh-approximation-closure).
