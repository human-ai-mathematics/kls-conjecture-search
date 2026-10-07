---
title: 'Solution: exact CMH constants on the line, on products, and on the log-concave Dirichlet family'
label: sec:sol-cmh-dirichlet
ledger-node:
- thm:cmh-1d
- thm:cmh-product
- cor:cmh-linear-images
- lem:cmh-gamma-completion
- lem:cmh-row-min
- lem:cmh-angular-coefficient
- thm:cmh-dirichlet
- cor:cmh-dirichlet-surplus
- cor:cmh-dirichlet-poincare
- cor:cmh-product-saturation
numbering:
  enumerator: D29.%s
---

*Part of the moment-map mechanism, Chapter [](#sec:cmh-exact-cases); the reading order is on the [full proofs](#sec:proofs-moment-map) page.*

**Overview.** This dossier proves $\mathrm{CMH}(4)$ in three classes where the constant of [](#def:cmh) can be computed: the line ([](#thm:cmh-1d)), products ([](#thm:cmh-product), [](#cor:cmh-linear-images)) and the log-concave Dirichlet family ([](#thm:cmh-dirichlet), with [](#lem:cmh-gamma-completion), [](#lem:cmh-row-min), [](#lem:cmh-angular-coefficient), [](#cor:cmh-dirichlet-surplus), [](#cor:cmh-dirichlet-poincare)). It also records [](#cor:cmh-product-saturation). The Dirichlet case is proved by lifting to independent Gamma variables, completing a square in the Gamma Bochner identity, and using the Euler constraint of degree-$0$ homogeneity. Universal $\mathrm{CMH}(4)$ remains open. Products of centered one-sided exponentials saturate the constant $4$ exactly.

1. On the line, $\CMH=\CP/\Var$ exactly, the KLS bound gives $\CP\le4\Var$, and the centered exponential attains $4$ ([](#thm:sol-cmh-1d)).
2. For products, the cross terms $\E[(L_ig)(L_jg)]$ are nonnegative, so $\CMH$ is the maximum over the factors ([](#thm:sol-cmh-product)). Affine Poincaré passes to linear images ([](#cor:sol-cmh-linear-images)).
3. The Dirichlet data and the tangent pseudo-inverse ([](#lem:sol-dirichlet-pseudoinverse)) reduce the claim to $A(A+1)d_\alpha\le4n_\alpha$.
4. Gamma lift: the Bochner identity [](#eq:sol-cmh-gamma-bochner) and a square completion give $N_\Gamma-\tfrac14D_\Gamma=\sum_i\E R_i+\sum_i\delta_iD_i$ ([](#lem:sol-gamma-completion)). The Euler constraint bounds each $R_i$ from below ([](#lem:sol-row-min)).
5. Using $S\perp P$ and the inverse moments of $S$, step 4 becomes a pointwise coefficient $F_A(\alpha_i,P_i)$. A scalar minimization bounds it by $A-\tfrac12+s_A$ with $s_A\ge0$ ([](#lem:sol-angular)), which proves [](#thm:sol-cmh-dirichlet), with strict surplus for $A>3$.
6. [](#thm:cmh-implies-affine-poincare) with step 2 gives $\CPaff\le4$ for Dirichlet laws, their products, linear images and convolutions.

**Scope.** This dossier proves $\mathrm{CMH}(4)$ in the three classes where the constant of [](#def:cmh) is computable, the third being the first genuinely nonproduct family for which Route C has a theorem. Combined with [](#thm:cmh-implies-affine-poincare) (dossier `solutions/thm-cmh-normalization.md`) each result yields an affine Poincaré bound with the same constant. Nothing here bears on universal $\mathrm{CMH}(4)$, which remains open; [](#cor:cmh-product-saturation) in the manuscript explains why the product case in particular is a warning rather than encouragement.

Notation is that of §[](#subsec:cmh-definition): $H$ is the moment-map Stein kernel in target coordinates, $L_\mu=\Div_\mu(H\nabla\,\cdot\,)$, $\Aop=-L_\mu$, and $\CMH$ is [](#eq:cmh-constant).

## 1\. The line

Let $\mu(\dd x)=\rho\dd x$ be centered on $(\ell,r)$ with variance $\sigma^2$ and Stein kernel $\tau$, the zero-flux solution of $(\tau\rho)'=-x\rho$.

:::{prf:theorem} = [](#thm:cmh-1d)
:label: thm:sol-cmh-1d
$\CMH(\mu)=\CP(\mu)/\Var(\mu)$. Every one-dimensional log-concave law satisfies $\mathrm{CMH}(4)$, and the centered one-sided exponential has $\CMH=4$.
:::

:::{prf:proof}
We use the natural no-flux realizations of §[](#subsec:cmh-conventions).
Let $D$ be the closed maximal derivative in $L^2(\mu)$, with domain
$H^1(\mu)$, and let $\Aop$ be the operator of the natural weighted form
$\mathcal E_\tau(f,q)=\int\tau f'q'\,d\mu$. Constants and bounded
locally absolutely continuous functions whose derivative has compact interior
support belong to these form domains when their displayed energies are finite.
The local density regularity is that of the differential-operator setup
(in particular, locally positive continuous densities suffice, using weak
derivatives); no endpoint regularity, log-concavity, or spectral gap is used.
Both constants in the asserted identity are allowed to be infinite, and the
CMH numerator is understood as an extended nonnegative integral.

Put $p=\tau\rho$. Centering and nonzero finite variance give $p>0$ in the
interior. The following graph core encodes the adjoint's no-flux condition:

$$
\mathscr U=\{u=\phi/\rho:\phi\in C_c^\infty((\ell,r))\},
\qquad D_\mu^*u=-\phi'/\rho.
$$

To verify the core assertion, define $B_0$ by this expression on $\mathscr U$.
Its domain is dense: compact localization and smooth approximation of the
flux $\rho u$ are dense in $L^2(\rho^{-1}dx)$. The adjoint condition,
tested against $\phi$, is precisely that a scalar function have a
distributional derivative in $L^2(\mu)$. Thus $B_0^*=D$, with no
boundary restriction on the scalar function, and
$\overline{B_0}=D_\mu^*$. Also $\ker D$ is exactly the constants.

Every field of this core is attained by an actual CMH test. Fix an interior
$x_0$ and set

$$
f_\phi(x)=\int_{x_0}^x\frac{\phi(t)}{p(t)}\,dt,
\qquad h_\phi=-\frac{\phi'}\rho.
$$

Then $f_\phi$ is bounded and constant near the endpoints, and
$\mathcal E_\tau(f_\phi,f_\phi)=\int\phi^2/p\,dx<\infty$.
For every weighted-form test $q$, compactly supported integration by parts gives

$$
\mathcal E_\tau(f_\phi,q)=\int\phi q'\,dx
=-\int\phi' q\,dx=\inner{h_\phi}{q}.
$$

Since $h_\phi\in L^2(\mu)$, the operator-domain criterion gives
$f_\phi\in\Dom(\Aop)$, $\Aop f_\phi=h_\phi$, and
$\tau f_\phi'=u$. Moreover $h_\phi$ is centered. No replacement of
$\operatorname{Ran}\Aop$ by all of centered $L^2$ has been made.

**Lower bound, including the infinite case.** Put $M=\sigma^2\CMH(\mu)$.
If $M<\infty$, these attained tests give
$\norm u_2^2\le M\norm{D_\mu^*u}_2^2$ on $\mathscr U$, and graph-core
closure extends it to all of $\Dom(D_\mu^*)$. This bound and closedness
make $\operatorname{Ran}D_\mu^*$ closed: if $D_\mu^*u_j$ converges,
then $u_j$ is Cauchy and the closed graph supplies its limiting preimage.
Since the closure of this range is $(\ker D)^\perp=L^2_0(\mu)$, the
range equals $L^2_0(\mu)$. For any centered $v\in\Dom D$, choose
$u$ with $D_\mu^*u=v$. Then

$$
\norm v_2^2=\inner{Dv}{u}
\le\sqrt M\norm{Dv}_2\norm v_2.
$$

Thus $\CP\le M$. If $M=\infty$ that inequality is automatic; in
particular $\CP=\infty$ forces $\CMH=\infty$.

**Upper bound when $\CP<\infty$.** Given $f\in\Dom(\Aop)$, put
$h=\Aop f$. Constants belong to $\ker\Aop$, so $h$ is centered.
Poincaré gives, for every $q\in\Dom D$,

$$
|\inner hq|\le\sqrt{\CP}\norm h_2\norm{Dq}_2.
$$

Apply Riesz representation to the bounded functional
$Dq\mapsto\inner hq$ on the closure of $\operatorname{Ran}D$.
There exists $w\in L^2(\mu)$ such that

$$
\inner w{Dq}=\inner hq\quad(q\in\Dom D),
\qquad \norm w_2\le\sqrt{\CP}\norm h_2.
$$

For $\eta\in C_c^\infty((\ell,r))$, its bounded primitive
$q(x)=\int_{x_0}^x\eta(t)\,dt$ belongs to both scalar form domains.
The defining weak identity for $\Aop f=h$ therefore yields

$$
\int\tau f'\eta\,d\mu=\inner hq=\int w\eta\,d\mu.
$$

The left integrand is locally integrable by weighted Cauchy--Schwarz.
Arbitrariness of $\eta$ proves $\tau f'=w$ almost everywhere, without
assuming square integrability of $\tau f'$ in advance. Consequently
$\norm{\tau f'}_2^2\le\CP\norm{\Aop f}_2^2$ for every CMH test.
Since $H=\tau$ and $\Sigma=\sigma^2$, this proves
$\sigma^2\CMH\le\CP$ in the finite case. In the infinite case equality
was already forced by the lower bound. No operator inverse is used.

The one-dimensional specialization of the Kannan–Lovász–Simonovits bound [@KannanLovaszSimonovits1995], recorded for example in [@cattiaux2018poincare, Eq. (2.25)] with that attribution, is $\CP(\mu)\le4\Var(\mu)$.

For sharpness let $X=Y-1$ with $Y\sim\mathrm{Exp}(1)$. Then $X$ is centered, has density $e^{-(x+1)}\one_{x\ge-1}\dd x$, and $\Var(X)=1$. For $0<a<\tfrac12$ set $f_a(x)=e^{a(x+1)}$. Direct integration gives

$$
\frac{\Var(f_a(X))}{\E\abs{f_a'(X)}^2}
=\frac{(1-2a)^{-1}-(1-a)^{-2}}{a^2(1-2a)^{-1}}
=\frac1{(1-a)^2}\longrightarrow4.
$$

The upper bound therefore gives $\CP(X)=4$, and the identity already proved gives $\CMH(X)=4$.
:::

:::{prf:remark}
This is an identity, not an inequality: in one dimension the solenoidal channel of [](#prop:cmh-hodge) is empty (a square-integrable divergence-free field with vanishing flux is zero), so CMH carries exactly the affine Poincaré information.
:::

## 2\. Products

:::{prf:theorem} = [](#thm:cmh-product)
:label: thm:sol-cmh-product
For $\mu=\bigotimes_{i=1}^m\mu_i$ with centered factors for which the canonical CMH data are defined,

$$
\CMH(\mu)=\max_i\CMH(\mu_i).
$$

For one-dimensional factors this equals $\max_i\CP(\mu_i)/\Var(\mu_i)$. Consequently block products of $\mathrm{CMH}(4)$ factors, and their invertible affine images, satisfy $\mathrm{CMH}(4)$.
:::

:::{prf:proof}
Here $\Sigma=\diag(\Sigma_1,\dots,\Sigma_m)$, $H=\diag(H_1,\dots,H_m)$, and $L_\mu=\sum_iL_i$ with $L_i$ acting in block $i$ only, so the $L_i$ are commuting nonpositive generators. For $i\ne j$, two integrations by parts give

$$
\E[(L_ig)(L_jg)]
=\E\Tr\!\left(H_iD^2_{ij}g\,H_jD^2_{ji}g\right)
=\E\norm{H_i^{1/2}D^2_{ij}g\,H_j^{1/2}}_{\HS}^2\ge0.
$$

Hence $\E(L_\mu g)^2=\sum_i\E(L_ig)^2+2\sum_{i<j}\E[(L_ig)(L_jg)]\ge\sum_i\E(L_ig)^2$.

For the numerator, conditioning on the other blocks and using the defining inequality for $\CMH(\mu_i)$ gives

$$
\E\inner{H_i\nabla_i g}{\Sigma_i^{-1}H_i\nabla_i g}
\le\CMH(\mu_i)\,\E(L_i g)^2.
$$

Summing and using the previous display gives “$\le$”. Testing on $g$ depending on one block gives “$\ge$”. The one-dimensional formula, including factors with infinite Poincaré or CMH constant, follows from the extended-constant identity [](#thm:sol-cmh-1d); the affine-image consequence uses the invertible affine covariance of $\CMH$ from §[](#subsec:cmh-conventions).
:::

:::{prf:corollary} = [](#cor:cmh-linear-images)
:label: cor:sol-cmh-linear-images
If independent factors each satisfy the affine Poincaré inequality with constant $C$, so does every linear image of their product, in particular every sum of independent such factors.
:::

:::{prf:proof}
For $Y=TX$ and smooth $f$, $\Var_Yf=\Var_X(f\circ T)$ and $\E_X\inner{\Cov(X)\nabla(f\circ T)}{\nabla(f\circ T)} =\E\inner{T\Cov(X)T^\top\nabla f}{\nabla f}=\E\inner{\Cov(Y)\nabla f}{\nabla f}$. No invertibility is needed.
:::

## 3\. The Dirichlet family: setup

Let $P\sim\Dir(\alpha)$, $\alpha_i\ge1$, $A=\sum_i\alpha_i$, $q=\alpha/A$. With $C(p)=\diag(p)-pp^\top$ and $L_\alpha$ the Wright–Fisher generator [](#eq:cmh-wright-fisher), the potential $\varphi(y)=A\log\sum_ie^{y_i/A}-q\cdot y$ has $\nabla\varphi=p-q$ and $D^2\varphi=C(p)/A$, and pushes $e^{-\varphi}$ forward to the centered law $P-q$. Hence the canonical data are $H=C(p)/A$, $L_\mu=L_\alpha/A$, and $\Sigma$ as in [](#eq:cmh-dirichlet-data).

:::{prf:lemma} Tangent pseudo-inverse
:label: lem:sol-dirichlet-pseudoinverse
For $v$ with $\sum_iv_i=0$, $v^\top\Sigma^\dagger v=A(A+1)\sum_iv_i^2/\alpha_i$.
:::

:::{prf:proof}
Let $x=A(A+1)\diag(\alpha)^{-1}v$. Then $\Sigma x=\bigl(\diag(\alpha)-\alpha\alpha^\top/A\bigr)\diag(\alpha)^{-1}v =v-(\alpha/A)\sum_iv_i=v$. Since $\ker\Sigma=\mathrm{span}\{\one\}$ and $v^\top\one=0$, the solution's ambiguity pairs to zero, so $v^\top\Sigma^\dagger v=v^\top x$.
:::

With $u_i=(C(P)\nabla g)_i$, $d_\alpha$, $n_\alpha$ as in [](#eq:cmh-dirichlet-dn), the statement $\CMH\le4$ becomes exactly $A(A+1)d_\alpha(g)\le4n_\alpha(g)$: the numerator is $A^{-2}\cdot A(A+1)d_\alpha=\tfrac{A+1}Ad_\alpha$ and the denominator $A^{-2}n_\alpha$.

:::{prf:theorem} = [](#thm:cmh-dirichlet)
:label: thm:sol-cmh-dirichlet
For every $m\ge2$, all $\alpha_i\ge1$, and all $g$ in the core, $A(A+1)\,d_\alpha(g)\le4\,n_\alpha(g)$.
:::

## 4\. The Gamma lift

Let $Y_i\sim\GammaLaw(\alpha_i,1)$ independent, $S=\sum_iY_i$, $P=Y/S$; then $S\sim\GammaLaw(A,1)$, $P\sim\Dir(\alpha)$, and $S\perp P$. Set $G(Y)=g(Y/S)$, homogeneous of degree $0$, and let $\calL_\Gamma G=\sum_i(Y_iG_{ii}+(\alpha_i-Y_i)G_i)$ be the Laguerre generator. To identify the source of its integrated Bochner identity, center the product-Gamma law by writing $X_i=Y_i-\alpha_i$. Its canonical moment Hessian, expressed in the unchanged $Y$ coordinates, is

$$
H_\Gamma=\diag(Y_1,\ldots,Y_m).
$$

Indeed, writing $\rho_\Gamma$ for the product-Gamma density,

$$
\Div_\Gamma(H_\Gamma\nabla G)
=\sum_i\rho_\Gamma^{-1}\partial_i(\rho_\Gamma Y_iG_i)
=\sum_i\bigl(Y_iG_{ii}+(\alpha_i-Y_i)G_i\bigr)=\calL_\Gamma G.
$$

Thus [](#prop:cmh-bochner), specialized to $H_\Gamma$, gives

```{math}
:label: eq:sol-cmh-gamma-bochner
N_\Gamma(G):=\E(\calL_\Gamma G)^2
=\E\left[\sum_iY_iG_i^2+\sum_{i,j}Y_iY_jG_{ij}^2\right].
```

Here the second sum is over ordered pairs: because $D^2G$ is symmetric, each off-diagonal square occurs twice, exactly as in $\Tr(H_\Gamma D^2G\,H_\Gamma D^2G)$. There is no additional factor of $2$ or $1/2$. Finally set $D_i(G)=\E[Y_i^2G_i^2]/\alpha_i$ and $D_\Gamma=\sum_iD_i$.

:::{prf:lemma} = [](#lem:cmh-gamma-completion)
:label: lem:sol-gamma-completion
For $\alpha_i\ge1$, $N_\Gamma(G)-\tfrac14D_\Gamma(G)=\sum_i\E R_i+\sum_i\delta_iD_i(G)$ with $R_i,\delta_i$ as in [](#eq:cmh-Ri-deltai), both nonnegative.
:::

:::{prf:proof}
The occurrence of the first-order row $\E[Y_iG_i^2]$ and the full ordered Hessian row $\E[\sum_jY_iY_jG_{ij}^2]$ below is precisely the $i$th-row contribution to the specialized Bochner identity [](#eq:sol-cmh-gamma-bochner). For $Y\sim\GammaLaw(a,1)$ and smooth $u$ with the usual decay,

$$
\E[Y^2uu']=\tfrac12\E[Y^2(u^2)']
=\tfrac1{2\Gamma(a)}\int y^{a+1}e^{-y}(u^2)'\dd y
=-\tfrac1{2\Gamma(a)}\int u^2\bigl((a+1)y^a-y^{a+1}\bigr)e^{-y}\dd y,
$$

i.e. $\E[Y^2uu']=-\tfrac12\E[((a+1)Y-Y^2)u^2]$. Expanding the first square of $R_i$ and applying this with $u=G_i$, $u'=G_{ii}$, $a=\alpha_i$, the cross term is

$$
-\tfrac2{\alpha_i+1}\E[Y_i^2G_iG_{ii}]
=\tfrac1{\alpha_i+1}\E[((\alpha_i+1)Y_i-Y_i^2)G_i^2]
=\E[Y_iG_i^2]-\tfrac1{\alpha_i+1}\E[Y_i^2G_i^2].
$$

Therefore

$$
\E R_i=\E\Bigl[Y_iG_i^2+\sum_jY_iY_jG_{ij}^2\Bigr]
+\Bigl(\tfrac1{(\alpha_i+1)^2}-\tfrac1{\alpha_i+1}\Bigr)\E[Y_i^2G_i^2],
$$

and $\tfrac1{(\alpha_i+1)^2}-\tfrac1{\alpha_i+1}=-\tfrac{\alpha_i}{(\alpha_i+1)^2}$. Summing over $i$, the bracket sums to $N_\Gamma(G)$ and the correction to $-\sum_i\tfrac{\alpha_i^2}{(\alpha_i+1)^2}D_i(G)$. Subtracting $\tfrac14D_\Gamma$ gives the claim, and $\delta_i=\tfrac{\alpha_i^2}{(\alpha_i+1)^2}-\tfrac14\ge0$ iff $\tfrac{\alpha_i}{\alpha_i+1}\ge\tfrac12$ iff $\alpha_i\ge1$.
:::

This lemma alone proves $\mathrm{CMH}(4)$ for the product-Gamma law; for that consequence, $\alpha_i\ge1$ is used only to make $\delta_i\ge0$. In the Dirichlet proof below the exact $\delta_i$ term is instead retained inside $F_A(\alpha_i,P_i)$, and log-concavity is consumed when [](#lem:sol-angular) is applied with $a=\alpha_i\ge1$.

:::{prf:lemma} = [](#lem:cmh-row-min)
:label: lem:sol-row-min
$R_i\ge\dfrac{Y_i}S\Bigl(1+\dfrac{Y_i}{\alpha_i+1}\Bigr)^2\abs{G_i}^2$.
:::

:::{prf:proof}
Homogeneity of degree $0$ gives Euler's identity $\sum_jY_jG_j=0$; differentiating in $Y_i$ yields $G_i+\sum_jY_jG_{ji}=0$, i.e. the single linear constraint $\sum_jY_jG_{ij}=-G_i$. Set $t_i=Y_i(G_{ii}-G_i/(\alpha_i+1))$ and $t_j=Y_jG_{ij}$ for $j\ne i$. Then

$$
\sum_jt_j=\sum_jY_jG_{ij}-\tfrac{Y_i}{\alpha_i+1}G_i=-G_i\Bigl(1+\tfrac{Y_i}{\alpha_i+1}\Bigr),
\qquad
R_i=t_i^2+\sum_{j\ne i}\tfrac{Y_i}{Y_j}t_j^2 .
$$

The weights are $w_i=1$ and $w_j=Y_i/Y_j$, so $\sum_jw_j^{-1}=1+\sum_{j\ne i}Y_j/Y_i=S/Y_i$. Minimizing $\sum_jw_jt_j^2$ subject to $\sum_jt_j=c$ gives $c^2/\sum_jw_j^{-1}$, which is the stated bound.
:::

Homogeneity further gives $\calL_\Gamma G=S^{-1}L_\alpha g$ and $Y_iG_i=u_i(P)$: indeed $G_i=\partial_{Y_i}g(Y/S)=S^{-1}(g_i-\sum_kP_kg_k)$, so $Y_iG_i=P_ig_i-P_i\sum_kP_kg_k=u_i(P)$. For $A>2$, $\E S^{-1}=(A-1)^{-1}$ and $\E S^{-2}=z_A^{-1}$ with $z_A=(A-1)(A-2)$. Since $S\perp P$,

$$
N_\Gamma(G)=\E[S^{-2}]\,\E(L_\alpha g)^2=\frac{n_\alpha(g)}{z_A},
\qquad
D_\Gamma(G)=\E\sum_i\frac{(Y_iG_i)^2}{\alpha_i}=d_\alpha(g),
$$

the second because $Y_iG_i$ depends on $P$ alone. Substituting $Y_i=SP_i$ and $G_i=u_i/(SP_i)$ into [](#lem:sol-row-min) and taking expectations gives [](#eq:cmh-integrated-row).

## 5\. The scalar minimization

:::{prf:lemma} = [](#lem:cmh-angular-coefficient)
:label: lem:sol-angular
For $A\ge3$, $a\ge1$, $0<p\le1$ and $z=z_A$, the function $F_A$ of [](#eq:cmh-FA) satisfies $F_A(a,p)\ge A-\tfrac12+s_A$ with $s_A$ as in [](#eq:cmh-FA-min), and $s_A\ge0$.
:::

:::{prf:proof}
The $p$-dependent part of $F_A$ is $\phi_a(p)=a\bigl(p^{-1}+zp(a+1)^{-2}\bigr)$, convex on $(0,\infty)$ with unconstrained minimizer $p_*=(a+1)/\sqrt z$. Hence on $(0,1]$ the minimum is at $p=1$ when $p_*\ge1$, i.e. $\sqrt z\le a+1$, and at $p_*$ otherwise.

*Case $z\le4$.* Then $\sqrt z\le2\le a+1$ for every $a\ge1$, so $p=1$ and

$$
F_A(a,1)=a+\frac{2a(A-2)}{a+1}+\frac{za}{a+1}-\frac z4 .
$$

Each of the three terms is increasing in $a$ on $[1,\infty)$, so the minimum is at $a=1$: $1+(A-2)+z/2-z/4=A-1+z/4=A-\tfrac12+\tfrac{z-2}4$.

*Case $z\ge4$.* At $p=p_*$ the two terms of $\phi_a$ are equal, so $\phi_a(p_*)=2a\sqrt z/(a+1)$. Writing $r=a/(a+1)\in[\tfrac12,1)$ for $a\ge1$,

$$
F_A=2r\sqrt z+2r(A-2)+zr^2-\frac z4=2r(\sqrt z+A-2)+zr^2-\frac z4,
$$

increasing in $r$ on $[0,1)$, so the minimum is at $r=\tfrac12$ ($a=1$) and equals $(\sqrt z+A-2)+z/4-z/4=A-2+\sqrt z=A-\tfrac12+\sqrt z-\tfrac32$. In the complementary region $\sqrt z\le a+1$ the value $F_A(a,1)$ is increasing in $a$ and at the interface is not smaller, so the stated minimum stands.

Finally $A\ge3$ gives $z_A=(A-1)(A-2)\ge2$, so $s_A=(z-2)/4\ge0$ when $z\le4$ and $s_A=\sqrt z-\tfrac32\ge2-\tfrac32>0$ when $z\ge4$.
:::

## 6\. Proof of the Dirichlet theorem

:::{prf:proof} Proof of [](#thm:sol-cmh-dirichlet)
If $m=2$ and $A<3$, the law is one dimensional and [](#thm:sol-cmh-1d) applies (a $\mathrm{Beta}$ law is log-concave precisely when both parameters are $\ge1$). In every remaining case $A=\sum_i\alpha_i\ge3$ — automatically so when $m\ge3$ — hence $z_A\ge2>0$ and the inverse moments $\E S^{-1},\E S^{-2}$ are finite.

By [](#lem:sol-gamma-completion) and [](#eq:cmh-integrated-row), since $D_i(G)=\E[u_i^2]/\alpha_i$, the coefficient of $\E_P[u_i^2]$ in $N_\Gamma(G)-\tfrac14D_\Gamma(G)$ is at least

$$
\frac1{z_AP_i}+\frac2{(A-1)(\alpha_i+1)}+\frac{P_i}{(\alpha_i+1)^2}+\frac{\delta_i}{\alpha_i}.
$$

Multiply by $z_A\alpha_i$ and use $z_A/(A-1)=A-2$ together with $z_A\delta_i=z_A\alpha_i^2/(\alpha_i+1)^2-z_A/4$:

$$
\frac{\alpha_i}{P_i}+\frac{2\alpha_i(A-2)}{\alpha_i+1}
+\frac{z_A\alpha_i(\alpha_i+P_i)}{(\alpha_i+1)^2}-\frac{z_A}4
=F_A(\alpha_i,P_i).
$$

[](#lem:sol-angular) bounds this below by $A-\tfrac12+s_A$ pointwise in $P_i$, so

$$
N_\Gamma(G)-\tfrac14D_\Gamma(G)
\ \ge\ \frac{A-\tfrac12+s_A}{z_A}\sum_i\frac{\E_P[u_i^2]}{\alpha_i}
=\frac{A-\tfrac12+s_A}{z_A}\,d_\alpha(g).
$$

Substituting $N_\Gamma=n_\alpha/z_A$ and $D_\Gamma=d_\alpha$, multiplying by $z_A$, and using

$$
\frac{z_A}4+A-\frac12=\frac{A^2-3A+2}4+\frac{4A-2}4=\frac{A(A+1)}4,
$$

we obtain $n_\alpha(g)\ge\bigl(\tfrac{A(A+1)}4+s_A\bigr)d_\alpha(g)$. Since $s_A\ge0$ this gives $A(A+1)d_\alpha(g)\le4n_\alpha(g)$.
:::

:::{prf:corollary} = [](#cor:cmh-dirichlet-surplus)
For $A>3$, $\CMH\le4\bigl(1+4s_A/(A(A+1))\bigr)^{-1}<4$.
:::

:::{prf:proof}
For $A>3$ the Gamma branch of the preceding proof applies, including when $m=2$, and gives $n_\alpha\ge\bigl(A(A+1)/4+s_A\bigr)d_\alpha$. Since $z_A>2$, the definition of $s_A$ gives $s_A>0$, and rearrangement proves the claim.
:::

:::{prf:corollary} = [](#cor:cmh-dirichlet-poincare)
Every log-concave Dirichlet law has $\CPaff\le4$, as does every product, linear image, and convolution of independent such laws.
:::

:::{prf:proof}
[](#thm:cmh-implies-affine-poincare) applied to [](#thm:sol-cmh-dirichlet), then [](#cor:sol-cmh-linear-images).
:::

Qualitative dimension-free KLS bounds for simplices and conservative Gamma models are prior art; see [@KolesnikovMilman2016OrliczKLS, §1.2] as a secondary pointer. The specific content of this proof is the constant $4$, the quantitative surplus, and the CMH-level estimate; no broader priority claim is made.

**Closure.** The argument is written for smooth $g$ with controlled boundary behavior. To close: take polynomials on the simplex, lift them after a radial cutoff $\{S\ge\eps\}$ so that all Gamma integrations by parts in [](#lem:sol-gamma-completion) are justified, and let $\eps\downarrow0$; the inverse moments $\E S^{-1},\E S^{-2}$ used in [](#eq:cmh-radial-relations) are finite because $A\ge3$ throughout the Gamma branch. Polynomials form a core for $L_\alpha$, so the closed forms extend the inequality to $\Dom(L_\alpha)$. Only the residual branch $m=2$, $A<3$ uses the one-dimensional no-flux closure of [](#thm:sol-cmh-1d) instead.

**Obstructions respected.** No `bounded_by` edge applies: the obstruction statements of the manuscript are scoped by their own statements to the fixed-cut Eldan program. The only one with method-level reach, `rem:projection-ceiling`, forbids deriving quadratic-chaos thin shell from radial or projection information alone; the Dirichlet proof uses the full Hessian row through the Euler constraint of [](#lem:sol-row-min), not projection tests, and makes no thin-shell claim. Consistency with the sharp external inputs holds: by [](#thm:cmh-1d), the boundary mechanism forcing the constant $4$ is the one-dimensional exponential, which is also the extremal case of [](#thm:letwin-moment-map).

:::{prf:corollary} = [](#cor:cmh-product-saturation)
:label: rem:sol-cmh-saturation-risk
[](#thm:sol-cmh-1d) and [](#thm:sol-cmh-product) prove that products of centered one-sided exponentials have $\CMH=4$ exactly. [](#prop:cmh-hodge) proves, for each admissible test function, the exact decomposition of the CMH numerator into the affine Poincaré contribution and a nonnegative solenoidal contribution.
:::

:::{prf:remark} Perturbative caveat
It is an open question, not a consequence of this corollary, whether an admissible perturbation raises the full CMH Rayleigh quotient. The covariance, canonical Stein kernel, both numerator channels, denominator, and optimizer all vary, so increasing a solenoidal term in isolation is insufficient. The required full second-variation calculation is [](#conj:cmh-second-variation).
:::

**What this does not show.** [](#thm:sol-cmh-dirichlet) is a family result, not evidence for universal $\mathrm{CMH}(4)$. By [](#cor:cmh-dirichlet-surplus) the Dirichlet family is strictly inside the bound, and by [](#thm:sol-cmh-product) the saturating cases are products of centered one-sided exponentials, where the slack is exactly zero. Whether that endpoint is perturbatively unstable is precisely the open issue just stated.
