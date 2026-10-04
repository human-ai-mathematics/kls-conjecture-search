---
numbering:
  enumerator: "12.%s"
---

(sec:cmh-exact-cases)=
# The moment map, exact cases: one dimension, products, the log-concave Dirichlet family, and exponential cones

Section [](#sec:cmh-normalization) fixed the CMH estimate and showed that it dominates the affine Poincaré constant ([](#thm:cmh-implies-affine-poincare)). This section computes it — or, in the fourth class, its linear sector — exactly, in the four classes where it is tractable. Two of them — the line and products — are the expected calibrations, and they already pin the constant: $\mathrm{CMH}(4)$ holds there and no smaller universal constant is possible. The third is the first genuinely nonproduct family on which the approach has an exact result: every log-concave Dirichlet law satisfies $\mathrm{CMH}(4)$ ([](#thm:cmh-dirichlet)). Its proof is a homogeneous lift to independent Gamma variables — a function on the simplex is rewritten as a function of independent Gamma variables, homogeneous of degree zero, where the generator is that of a product — followed by a sharp Hessian-row minimization; in the Dirichlet argument the log-concavity hypothesis is consumed in the final scalar angular minimization.

The fourth class is solvable in a weaker but more pointed sense. The exponential cones of §[](#subsec:cmh-cones) attach a Gamma radial variable to an arbitrary centered base, and their moment map is explicit in terms of the base's own ([](#prop:cone-moment-map)); unlike the first three classes they are not compactly supported and, for a general base, not affine images of products. What is computed exactly on them is the linear sector rather than the full constant: the axis gate value is $1+n/\beta$, so every cone with $\beta=n$ saturates sharp gate zero ([](#conj:gate-zero-sharp)) in its axis direction ([](#prop:cone-linear-sector)), and over a cube base the entire gate matrix is a closed form bounded by $2$ ([](#cor:cube-cone-gate-zero)). They are the first non-product equality set the sharp linear sector has, which is what makes them a constraint on any argument for it.

The section closes at the exact product endpoint, the extreme case where the inequality holds with equality: centered one-sided exponentials saturate $\mathrm{CMH}(4)$ with *zero* slack. Whether a log-concave perturbation raises the full CMH Rayleigh quotient is a separate second-variation problem, [](#conj:cmh-second-variation); changing its solenoidal term alone is not decisive ([](#cor:cmh-product-saturation)). The cone family bears on where to look for such a perturbation, and §[](#subsec:cmh-cones) reports what a first computation over it suggests.

(subsec:cmh-1d)=
## The line

Let $\mu(\dd x)=\rho(x)\dd x$ be centered on an interval $(\ell,r)$ with variance $\sigma^2$. Its canonical Stein kernel is the unique zero-flux solution of $(\tau\rho)'=-x\rho$,

```{math}
:label: eq:cmh-1d-stein
\tau(x)=-\frac1{\rho(x)}\int_\ell^xt\rho(t)\dd t,
```

and it coincides with the moment-map Hessian in target coordinates. The Stein generator is $L_\mu f=\tau f''-xf'=\rho^{-1}(\tau\rho f')'$, so that $h=-L_\mu f$ has

```{math}
:label: eq:cmh-1d-flux
\tau(x)f'(x)=-\frac1{\rho(x)}\int_\ell^xh(t)\rho(t)\dd t.
```

:::{prf:theorem} Exact one-dimensional CMH constant
:label: thm:cmh-1d
For every centered one-dimensional law for which the operators above are defined,

```{math}
:label: eq:cmh-1d-exact
\CMH(\mu)=\frac{\CP(\mu)}{\Var(\mu)}.
```

In particular every one-dimensional log-concave law satisfies $\mathrm{CMH}(4)$, and the constant $4$ cannot be lowered.
:::

:::{prf:proof}
On the centered subspace let $D=\dd/\dd x$ and let $D_\mu^*u=-\rho^{-1}(\rho u)'$ be its weighted adjoint, so that the inverse norm of the nonnegative Langevin operator $D_\mu^*D$ is $\CP(\mu)$. If $v=(D_\mu^*D)^{-1}h$, then $Dv$ is the zero-boundary-flux solution of $D_\mu^*u=h$; by [](#eq:cmh-1d-flux) it is the field $u=\tau f'$. Therefore

$$
\norm u_2^2=\norm{Dv}_2^2
=\inner{v}{D_\mu^*Dv}
=\inner{h}{(D_\mu^*D)^{-1}h},
\qquad
\sup_{h\perp1}\frac{\norm u_2^2}{\norm h_2^2}=\CP(\mu).
$$

The CMH numerator is $\norm u_2^2/\sigma^2$ and its denominator is $\norm h_2^2$, which gives [](#eq:cmh-1d-exact). The one-dimensional specialization of the Kannan–Lovász–Simonovits bound [@KannanLovaszSimonovits1995], recorded for example in [@cattiaux2018poincare, Eq. (2.25)] with that attribution, is $\CP(\mu)\le4\Var(\mu)$ and hence gives $\mathrm{CMH}(4)$.

For sharpness, let $X=Y-1$ with $Y\sim\mathrm{Exp}(1)$, so that $X$ is centered, has density $e^{-(x+1)}\one_{x\ge-1}\dd x$, and has variance $1$. For $0<a<\tfrac12$, the test function $f_a(x)=e^{a(x+1)}$ satisfies

$$
\frac{\Var(f_a(X))}{\E\abs{f_a'(X)}^2}
=\frac{(1-2a)^{-1}-(1-a)^{-2}}{a^2(1-2a)^{-1}}
=\frac1{(1-a)^2}\longrightarrow4.
$$

Thus $\CP(X)=4$ by the preceding upper bound, and [](#eq:cmh-1d-exact) gives $\CMH(X)=4$.
:::

[](#thm:cmh-1d) is an *identity*, not an inequality: on the line CMH carries exactly the information of the affine Poincaré inequality and nothing more. This is [](#cor:cmh-hodge-comparison) seen from the other side — the solenoidal channel is empty in dimension one.

(subsec:cmh-product)=
## Products

Let $\mu=\bigotimes_{i=1}^m\mu_i$ be a product of centered factors for which the canonical CMH data are defined. Then $\Sigma=\diag(\Sigma_1,\dots,\Sigma_m)$, $H=\diag(H_1,\dots,H_m)$, and $L_\mu=\sum_iL_i$, where the $L_i$ are commuting nonpositive generators acting in their respective blocks.

:::{prf:theorem} Product formula
:label: thm:cmh-product
For a product of centered CMH factors,

```{math}
:label: eq:cmh-product
\CMH\Bigl(\bigotimes_i\mu_i\Bigr)=\max_i\CMH(\mu_i).
```

In particular, for centered one-dimensional factors this is $\max_i\CP(\mu_i)/\Var(\mu_i)$. Consequently $\mathrm{CMH}(4)$ holds for every product of one-dimensional log-concave laws, for block products of $\mathrm{CMH}(4)$ factors, and for their invertible affine images.
:::

:::{prf:proof}
Write $\nabla_i$ for the gradient in the $i$th block. Conditioning on all other blocks and using the definition of $\CMH(\mu_i)$ gives

$$
\E\inner{H_i\nabla_i g}{\Sigma_i^{-1}H_i\nabla_i g}
\le \CMH(\mu_i)\,\E(L_i g)^2.
$$

For $i\ne j$, two integrations by parts give the block cross-term identity

```{math}
:label: eq:cmh-product-cross
\E[(L_ig)(L_jg)]
=\E\Tr\!\left(H_iD^2_{ij}g\,H_jD^2_{ji}g\right)
=\E\norm{H_i^{1/2}D^2_{ij}g\,H_j^{1/2}}_{\HS}^2\ge0,
```

whence $\sum_i\E(L_ig)^2\le\E\bigl(\sum_iL_ig\bigr)^2=\E(L_\mu g)^2$. Summing the conditional estimates proves “$\le$” in [](#eq:cmh-product); testing on functions of a single block proves “$\ge$”. The one-dimensional formula now follows from [](#thm:cmh-1d), and the final affine-image claim uses only the invertible affine invariance proved in §[](#subsec:cmh-conventions).
:::

:::{prf:corollary} Poincaré closure under linear images and convolution
:label: cor:cmh-linear-images
If independent factors each satisfy the affine Poincaré inequality with constant $C$, then so does every linear image of their product — in particular every sum of independent such factors.
:::

:::{prf:proof}
For $Y=T(X_1,\dots,X_m)$ apply the product affine Poincaré inequality to $f\circ T$. The gradient energy is $\nabla f^\top T\Cov(X)T^\top\nabla f=\inner{\Cov(Y)\nabla f}{\nabla f}$, and $\Var_Yf=\Var_X(f\circ T)$.
:::

Note that [](#cor:cmh-linear-images) is a statement about $\CPaff$, which is stable under noninvertible maps; the canonical CMH constant itself is claimed invariant only under invertible affine maps (§[](#subsec:cmh-conventions)).

(subsec:cmh-dirichlet-setup)=
## The Dirichlet family: geometry and normalization

Let $P\sim\Dir(\alpha_1,\dots,\alpha_m)$ with $\alpha_i\ge1$, which is exactly the log-concave parameter range, and put $A=\sum_i\alpha_i$, $q_i=\alpha_i/A$. Write

```{math}
:label: eq:cmh-wright-fisher
C(p)=\diag(p)-pp^\top,
\qquad
L_\alpha g=\Tr\bigl(C(p)D^2g\bigr)+\inner{\alpha-Ap}{\nabla g}
```

for the Wright–Fisher generator; both expressions are independent of the ambient extension of $g$ because $C(p)\one=0$ and $\sum_i(\alpha_i-Ap_i)=0$.

On $\R^m/\mathrm{span}\{\one\}$ consider $\varphi(y)=A\log\bigl(\sum_ie^{y_i/A}\bigr)-q\cdot y$. Its gradient is $p-q$ with $p_i=e^{y_i/A}/\sum_je^{y_j/A}$, its Hessian is $C(p)/A$, and the softmax Jacobian identifies the pushforward of $e^{-\varphi}$ with the centered law $P-q$. Hence the canonical moment-map data are

```{math}
:label: eq:cmh-dirichlet-data
H(p)=\tfrac1AC(p),\qquad L_\mu=\tfrac1AL_\alpha,
\qquad
\Sigma=\frac1{A(A+1)}\Bigl(\diag(\alpha)-\frac{\alpha\alpha^\top}A\Bigr).
```

For every tangent vector $v$, meaning $\sum_iv_i=0$,

```{math}
:label: eq:cmh-dirichlet-pseudoinverse
v^\top\Sigma^\dagger v=A(A+1)\sum_i\frac{v_i^2}{\alpha_i},
```

because $x=A(A+1)\diag(\alpha)^{-1}v$ satisfies $\Sigma x=v$ exactly, and the remaining $\ker\Sigma=\mathrm{span}\{\one\}$ ambiguity pairs to zero against $v$.

Setting

```{math}
:label: eq:cmh-dirichlet-dn
u_i(p)=\bigl(C(p)\nabla g(p)\bigr)_i,
\qquad
d_\alpha(g)=\E\sum_i\frac{u_i^2}{\alpha_i},
\qquad
n_\alpha(g)=\E(L_\alpha g)^2,
```

equations [](#eq:cmh-dirichlet-data)–[](#eq:cmh-dirichlet-pseudoinverse) turn [](#def:cmh) into the statement $A(A+1)d_\alpha(g)\le4n_\alpha(g)$.

:::{prf:theorem} Log-concave Dirichlet CMH
:label: thm:cmh-dirichlet
For every $m\ge2$, every $\alpha_1,\dots,\alpha_m\ge1$, and every $g$ in the core,

```{math}
:label: eq:cmh-dirichlet-main
A(A+1)\,\E\sum_{i=1}^m
\frac{\bigl(C(P)\nabla g(P)\bigr)_i^2}{\alpha_i}
\le4\,\E\bigl(L_\alpha g(P)\bigr)^2.
```

Equivalently, every log-concave Dirichlet law satisfies $\mathrm{CMH}(4)$.
:::

(subsec:cmh-gamma-lift)=
## The independent Gamma lift

Let $Y_i\sim\GammaLaw(\alpha_i,1)$ be independent, $S=\sum_iY_i\sim\GammaLaw(A,1)$ and $P_i=Y_i/S$; then $P\sim\Dir(\alpha)$ and $S\perp P$. Lift $g$ homogeneously of degree zero by $G(Y)=g(Y/S)$. The product-Gamma (Laguerre) generator is $\calL_\Gamma G=\sum_i\bigl(Y_iG_{ii}+(\alpha_i-Y_i)G_i\bigr)$. [](#prop:cmh-bochner), specialized to the Gamma moment Hessian $H_\Gamma=\diag(Y_i)$, gives the integrated Bochner identity

```{math}
:label: eq:cmh-gamma-bochner
N_\Gamma(G):=\E(\calL_\Gamma G)^2
=\E\Bigl[\sum_iY_iG_i^2+\sum_{i,j}Y_iY_jG_{ij}^2\Bigr].
```

Put $D_i(G)=\E[Y_i^2G_i^2]/\alpha_i$ and $D_\Gamma(G)=\sum_iD_i(G)$.

:::{prf:lemma} Exact Gamma row completion
:label: lem:cmh-gamma-completion
For $\alpha_i\ge1$,

```{math}
:label: eq:cmh-gamma-completion
N_\Gamma(G)-\tfrac14D_\Gamma(G)=\sum_i\E R_i+\sum_i\delta_iD_i(G),
```

where

```{math}
:label: eq:cmh-Ri-deltai
R_i=Y_i^2\Bigl\lvert G_{ii}-\frac{G_i}{\alpha_i+1}\Bigr\rvert^2
+\sum_{j\ne i}Y_iY_j\abs{G_{ij}}^2\ \ge0,
\qquad
\delta_i=\frac{\alpha_i^2}{(\alpha_i+1)^2}-\frac14\ \ge0.
```
:::

*Proof.* One integration by parts for the Gamma law, applied coordinatewise and summed, which recovers $N_\Gamma$ and leaves an explicit negative multiple of $D_i$. The calculation is carried out in Appendix [](#sec:appendix-moment-map).

:::{prf:remark} Where log-concavity is spent
:label: rem:cmh-dirichlet-logconcavity
[](#lem:cmh-gamma-completion) already proves $\mathrm{CMH}(4)$ for the product-Gamma law, since $R_i\ge0$ and $\delta_i\ge0$; for that product-Gamma consequence, $\alpha_i\ge1$ is used only in the sign of $\delta_i$. The Dirichlet proof does not discard $\delta_i$: it retains its exact value inside $F_A(\alpha_i,P_i)$. There the log-concavity hypothesis is consumed when [](#lem:cmh-angular-coefficient) is applied with $a=\alpha_i\ge1$.
:::

:::{prf:lemma} Hessian-row minimization
:label: lem:cmh-row-min
With $G$ homogeneous of degree zero,

```{math}
:label: eq:cmh-row-min
R_i\ \ge\ \frac{Y_i}S\Bigl(1+\frac{Y_i}{\alpha_i+1}\Bigr)^2\abs{G_i}^2 .
```
:::

*Proof.* Euler's identity, differentiated once, leaves a single linear constraint; the row minimum is then the elementary minimum of a weighted sum of squares subject to one linear constraint. The calculation is carried out in Appendix [](#sec:appendix-moment-map).

Homogeneity also gives the exact dictionary between the lift and the simplex: $\calL_\Gamma G=S^{-1}L_\alpha g$ and $Y_iG_i=u_i(P)$. With $A>2$ one has $\E S^{-1}=(A-1)^{-1}$ and $\E S^{-2}=z_A^{-1}$ where

```{math}
:label: eq:cmh-zA
z_A=(A-1)(A-2),
```

so independence of $S$ and $P$ yields

```{math}
:label: eq:cmh-radial-relations
N_\Gamma(G)=\frac{n_\alpha(g)}{z_A},
\qquad
D_\Gamma(G)=d_\alpha(g),
```

and, substituting $Y_i=SP_i$ and $G_i=u_i/(SP_i)$ into [](#eq:cmh-row-min),

```{math}
:label: eq:cmh-integrated-row
\E R_i\ \ge\ \E_P\,u_i^2
\Bigl[\frac1{z_AP_i}+\frac2{(A-1)(\alpha_i+1)}+\frac{P_i}{(\alpha_i+1)^2}\Bigr].
```

(subsec:cmh-dirichlet-proof)=
## The scalar angular inequality and the proof

:::{prf:lemma} Angular coefficient
:label: lem:cmh-angular-coefficient
Let $A\ge3$, $a\ge1$, $0<p\le1$, $z=(A-1)(A-2)$, and

```{math}
:label: eq:cmh-FA
F_A(a,p)=\frac ap+\frac{2a(A-2)}{a+1}+\frac{za(a+p)}{(a+1)^2}-\frac z4 .
```

Then

```{math}
:label: eq:cmh-FA-min
F_A(a,p)\ \ge\ A-\tfrac12+s_A,
\qquad
s_A=\begin{cases}\dfrac{z-2}4,&z\le4,\\\sqrt z-\dfrac32,&z\ge4,\end{cases}
```

and $s_A\ge0$ for $A\ge3$.
:::

*Proof.* Minimize in $p$ first — the minimizer is interior only when $\sqrt z>a+1$ — and then check monotonicity in $a$ separately on the two branches $z\le4$ and $z\ge4$. The calculation is carried out in Appendix [](#sec:appendix-moment-map).

*Proof of [](#thm:cmh-dirichlet).* Reduce $m=2$ to the line, then combine the Gamma completion, the row minimum and the integrated row bound: the total coefficient of $\E_P[u_i^2]$ is exactly $F_A(\alpha_i,P_i)$, and [](#lem:cmh-angular-coefficient) bounds that below. The calculation is carried out in Appendix [](#sec:appendix-moment-map).

:::{prf:corollary} Quantitative surplus
:label: cor:cmh-dirichlet-surplus
For $A>3$, $n_\alpha(g)\ge\bigl(\tfrac14+\eps_A\bigr)A(A+1)d_\alpha(g)$ with $\eps_A=s_A/(A(A+1))>0$. Equivalently $\CMH\le4\bigl(1+4s_A/(A(A+1))\bigr)^{-1}<4$: the constant $4$ is attained only in the limit.
:::

:::{prf:proof}
When $A>3$ the Gamma branch of the preceding proof applies, including when $m=2$, and [](#eq:cmh-dirichlet-surplus) gives the asserted estimate. Moreover $z_A>2$, so either $s_A=(z_A-2)/4>0$ or $s_A=\sqrt{z_A}-3/2>0$.
:::

:::{prf:corollary} Affine Poincaré consequences
:label: cor:cmh-dirichlet-poincare
Every log-concave Dirichlet law satisfies $\CPaff\le4$; so does every linear image, product, and convolution of independent such laws.
:::

:::{prf:proof}
Combine [](#thm:cmh-implies-affine-poincare) and [](#thm:cmh-dirichlet) with [](#cor:cmh-linear-images).
:::

Qualitative dimension-free KLS bounds for simplices and conservative Gamma models are prior art; see [@KolesnikovMilman2016OrliczKLS, §1.2] as a secondary pointer to that literature. The specific content of this proof is the constant $4$, the quantitative surplus, and the CMH-level estimate; no broader priority claim is intended.

:::{prf:remark} Closure and aggregation
:label: rem:cmh-dirichlet-closure
The proof is written for smooth $g$ with controlled boundary behavior. The closure argument takes polynomials on the simplex, lifts them after a radial cutoff $S\ge\eps$, applies the Gamma identities and lets $\eps\downarrow0$; the required inverse Gamma moments are finite because $A\ge3$ throughout the Gamma branch. Polynomials form a core for $L_\alpha$, so the closed forms extend [](#eq:cmh-dirichlet-main) to $\Dom(L_\alpha)$; only the residual branch $m=2$, $A<3$ uses the one-dimensional no-flux closure instead.

The estimate is also compatible with Dirichlet aggregation. If $Q\sim\Dir(\beta_1,\dots,\beta_N)$, the coordinates are partitioned into blocks $G_i$, and $P_i=\sum_{a\in G_i}Q_a$, $\alpha_i=\sum_{a\in G_i}\beta_a$, then for functions of $P$ alone the generator is the coarse one and $\E\bigl[\sum_{a\in G_i}Q_a^2/\beta_a\mid P\bigr] =P_i^2(\alpha_i+\abs{G_i})/(\alpha_i(\alpha_i+1))\ge P_i^2/\alpha_i$, so CMH for the fine law implies CMH for its aggregation. This is a consistency check on [](#thm:cmh-dirichlet), not an ingredient of it.
:::

:::{prf:remark} Sharpness on simplex faces
:label: rem:cmh-dirichlet-sharp
The constant $4$ cannot be improved uniformly over the family. The face law $\mathrm{Beta}(1,b)$ is one dimensional, so [](#thm:cmh-1d) applies; its Neumann spectral problem reduces to Bessel's equation and gives $\CMH(\mathrm{Beta}(1,b))=(b+1)^2(b+2)/\bigl(b\,j_{b/2,1}^2\bigr)$ with $j_{\nu,1}$ the first positive zero of $J_\nu$. Since $j_{b/2,1}\sim b/2$, this tends to $4$; after rescaling $\mathrm{Beta}(1,b)$ converges to the one-sided exponential. The extremal mechanism on the simplex is therefore the same one-dimensional exponential boundary mechanism that fixes the constant in [](#thm:cmh-1d). [](#cor:cmh-dirichlet-surplus) says the interior of the family is strictly safer.
:::

(subsec:cmh-cones)=
## Exponential cones: a second solvable non-product family

The Dirichlet family is solvable because the simplex lifts to independent Gamma variables. A lift in the opposite direction — attach a Gamma radial variable to a fixed base — produces measures on cones whose moment map is explicit in terms of the moment map of the base, and on which the linear sector of the moment-map inequality is computed exactly. Unlike products and Dirichlet laws these measures are not compactly supported, and for a general base they are not invertible affine images of products.

:::{prf:definition} Exponential cone measures
:label: def:exponential-cone
Let $n\ge2$, let $K\subset\R^{n-1}$ be a convex body with barycenter at the origin, let

$$
C_K=\bigl\{(x_1,x')\in\R\times\R^{n-1}:\ x_1>0,\ x'/x_1\in\operatorname{int}K\bigr\}
$$

be the open cone over $K$, and let $\beta\ge n$. The *exponential cone measure* $\mu_{K,\beta}$ is the probability measure on $\R^n$ with density proportional to $x_1^{\beta-n}e^{-x_1}\one_{C_K}(x)$, and $\bar\mu_{K,\beta}$ is its centering, the law of $X-\beta e_1$ for $X\sim\mu_{K,\beta}$.
:::

The measure $\mu_{K,\beta}$ is log-concave because $\beta\ge n$, and $X\sim\mu_{K,\beta}$ has the representation $X=S\,(1,U)$ with $S\sim\GammaLaw(\beta,1)$ and $U$ uniform on $K$ independent. Hence $\E X=\beta e_1$ and

```{math}
:label: eq:cone-covariance
\Sigma=\Cov(X)=\beta\,e_1e_1^\top\oplus\beta(\beta+1)\Cov(U).
```

For $\beta=n$ the density is $e^{-x_1}$ on the cone; that case is the cone construction of Lemma 4.2 of [@ChenKlartag2026SharpThinShell], whose conical integration formula they attribute to [@Klartag2018IsotropicMahler, Lem. 2.1], and the general family $\beta\ge n$ and its moment map are not treated there. When $K$ is a simplex and $\beta=n$ this is an affine image of a product of centered exponentials; for a square base it is not an invertible affine image of any product of one-dimensional laws, since its support has four pairwise non-parallel facets.

:::{prf:proposition} Cone lift of the moment map
:label: prop:cone-moment-map
Let $\lambda$ be the moment potential of the uniform probability on $\beta K$, so that $\lambda$ is smooth and strictly convex on $\R^{n-1}$ and $\nabla\lambda$ is a diffeomorphism onto $\beta\operatorname{int}K$ by [](#thm:regular-moment-map-compact-target). Then the moment potential of $\bar\mu_{K,\beta}$ is

```{math}
:label: eq:cone-moment-potential
\varphi(y_1,y')=\exp\bigl(y_1+\lambda(y')/\beta\bigr)-\beta y_1+\log\Gamma(\beta),
```

$\nabla\varphi$ is a diffeomorphism of $\R^n$ onto $C_K-\beta e_1$, and the canonical Stein kernel of $\bar\mu_{K,\beta}$ at the point $x-\beta e_1$, $x=(x_1,x_1u)\in C_K$, is

```{math}
:label: eq:cone-stein-kernel
\tau(x-\beta e_1)=x_1
\begin{pmatrix}1&u^\top\\ u&uu^\top+\beta\,\tau_K(u)\end{pmatrix},
```

where $\tau_K$ is the canonical Stein kernel of the uniform probability on $K$. In particular the first column is the position vector itself, $\tau(x-\beta e_1)\,e_1=x$.
:::

:::{prf:proposition} The linear sector of an exponential cone
:label: prop:cone-linear-sector
Let $\mu=\bar\mu_{K,\beta}$, with $\Sigma$ and $\tau$ as in [](#eq:cone-covariance) and [](#eq:cone-stein-kernel), and write $\bar x=x-\beta e_1$ for the centered coordinate.

(i) The field $x=\tau e_1$ satisfies $\Div_\mu x=-\bar x_1$ with zero boundary flux, and $x=\Sigma\nabla\psi$ for $\psi=\tfrac12\,x^\top\Sigma^{-1}x$. Hence the first Stein column is a covariance gradient with no solenoidal part in the sense of [](#prop:cmh-hodge), and

$$
\sup_{f}\frac{\bigl(\E_\mu[\bar x_1f]\bigr)^2}{\E_\mu\inner{\Sigma\nabla f}{\nabla f}}
=\E_\mu\bigl[x^\top\Sigma^{-1}x\bigr]=\beta+n,
$$

the supremum over $f$ of finite covariance energy being attained at $f=\psi$.

(ii) The gate matrix is exact in the axis direction:

$$
\frac{e_1^\top\,\E_\mu[\tau\Sigma^{-1}\tau]\,e_1}{e_1^\top\Sigma\,e_1}
=1+\frac n\beta\ \le\ 2,
$$

with equality if and only if $\beta=n$; this is also the value of the CMH Rayleigh quotient [](#eq:cmh-constant) at the linear test function $g=x_1$.

(iii) In isotropic coordinates $Z=\Sigma^{-1/2}\bar x$, with kernel $\tau_Z=\Sigma^{-1/2}\tau\Sigma^{-1/2}$, the axis column is exactly its gap-mode projection: $T_3(e_1)=\E[Z_1\,Z\otimes Z]=2\beta^{-1/2}\,\Id$ and $\tau_Ze_1=e_1+\tfrac12T_3(e_1)Z$. Hence $\norm{T_3(e_1)}_{\HS}^2=4n/\beta$ and the high-mode term of [](#lem:linear-sector-third-moment) vanishes, $v_{e_1}=0$, for every base $K$ and every $\beta\ge n$.

In particular every exponential cone measure with $\beta=n$ saturates the sharp gate-zero inequality [](#eq:gate-zero-sharp) in its axis direction and attains $\norm{T_3(e_1)}_{\HS}=2$.
:::

At $\beta=n$, part (iii) is the third-moment computation of Lemma 4.2 of [@ChenKlartag2026SharpThinShell], which gives $T(Y)_{ijk}=2\delta_{ij}/\sqrt k$, $T(Y)_{ikk}=0$ and $T(Y)_{kkk}=2/\sqrt k$ with $k=\beta$; parts (i)–(ii) and the general $\beta$ are new here. [](#prop:cone-linear-sector) gives a family of equality cases of [](#conj:gate-zero-sharp) that are not products, and it gives them for every base: the axis direction of a cone sees only the Gamma radial law, which is why the value $1+n/\beta$ does not depend on $K$. The transverse block does depend on $K$, through the base kernel $\tau_K$; when the base is a cube it is explicit.

:::{prf:corollary} The cube cone, exactly
:label: cor:cube-cone-gate-zero
For $K=[-1,1]^{n-1}$ the base kernel is $\tau_K(u)=\tfrac12\operatorname{diag}(1-u_j^2)$, and the normalized gate matrix $\Sigma^{-1/2}\,\E[\tau\Sigma^{-1}\tau]\,\Sigma^{-1/2}$ of $\bar\mu_{K,\beta}$ equals

$$
\Bigl(1+\frac n\beta\Bigr)\ \oplus\ \frac{6\beta^2+11\beta+5n+4}{5\beta(\beta+1)}\,\Id_{n-1}.
$$

Both eigenvalues are at most $2$ for all $n\ge2$ and $\beta\ge n$: every cube cone satisfies [](#eq:gate-zero-sharp). Equality holds in the axis direction exactly when $\beta=n$, and in the transverse directions only for $n=\beta=2$, where the matrix is $2\,\Id_2$ and the measure is a product of two centered exponentials.
:::

The cube cones are the first non-product family in this document on which the sharp linear sector is saturated while every object entering $\CMH$ — the kernel, the generator, and all moments — is a rational function of independent Gamma and uniform variables. They are therefore the natural place to test $\mathrm{CMH}(4)$ itself beyond the product endpoint of [](#cor:cmh-product-saturation): numerical experiments suggest that the product-potential perturbations of [](#conj:cmh-second-variation) leave the log-concave class for both signs of $\eps$, whereas here the base supplies a non-product perturbation inside it, and a Galerkin quotient above $4$ on a cube cone would point to a counterexample to $\mathrm{CMH}(4)$, which would still have to be verified by an exact argument. A first computation over this family points the other way: on cube cones the polynomial Galerkin quotients sit strictly below the exponential-product values at equal degree, so a non-product base appears to dilute the one-dimensional exponential mechanism rather than add to it, and the pressure on $\mathrm{CMH}(4)$ within this family, if any, lies in the radial factor. This is numerical evidence at finite degree, not a proof.

% Agent note: the computation is research/explorations/2026-09-06-numerics-cmh-cone-w5n01.md; a refuting witness would go through solutions/README.md.

(subsec:cmh-saturation)=
## The saturation risk and the decisive test

:::{prf:corollary} Exact product saturation and Hodge splitting
:label: cor:cmh-product-saturation
By [](#thm:cmh-1d) and [](#thm:cmh-product), a product of centered one-sided exponentials has $\CMH=4$ *exactly*. [](#prop:cmh-hodge) gives, for every admissible test function, the exact splitting of the CMH numerator into its affine Poincaré part and the nonnegative solenoidal term $\E\inner{w}{\Sigma^{-1}w}$.
:::

:::{prf:remark} Why saturation leaves a perturbative test
No perturbative conclusion follows from those two facts alone. Under a perturbation the covariance and its inverse, the canonical Stein kernel, both numerator channels, the denominator, and the optimizing test function may all vary. In particular, an increase of the solenoidal term for one test function does not by itself imply an increase of the full CMH Rayleigh quotient. Whether an admissible perturbation raises $\CMH$ above $4$ is the second-variation problem of [](#conj:cmh-second-variation), which conjectures that none does to second order; a perturbation that does would refute $\mathrm{CMH}(4)$ but would not by itself refute [](#conj:kls).
:::

:::{prf:conjecture} Second variation of CMH at products, where it equals 4
:label: conj:cmh-second-variation
Take the product moment potential $\psi_0(s,t)=\phi(s)+t^2/2$ with $\phi$ the one-sided exponential moment potential, and perturb it by $\psi_\eps=\psi_0+\eps\,a(s)b(t)$. Call the perturbation admissible if, for all sufficiently small $\abs\eps$, $\psi_\eps$ is smooth and strictly convex and its moment measure $\mu_\eps$ is log-concave and belongs to the regular moment-map class on which [](#def:cmh) is set. Then, for every admissible perturbation,

$$
\limsup_{\eps\to0}\frac{\CMH(\mu_\eps)+\CMH(\mu_{-\eps})-2\CMH(\mu_0)}{\eps^2}\le0,
$$

where $\CMH(\mu_0)=4$ by [](#cor:cmh-product-saturation).
:::

Since $\CMH(\mu_0)=4$, a strictly positive value of this second variation for one admissible perturbation would give $\CMH(\mu_\eps)>4$ for some small $\eps$: a counterexample to $\mathrm{CMH}(4)$, forcing a constant larger than $4$ in the endpoint, though not by itself a counterexample to [](#conj:kls). The computation splits the CMH numerator through [](#prop:cmh-hodge) into its gradient and solenoidal parts; a vanishing of the solenoidal part to second order would not by itself decide the sign, since the gradient part, the denominator and the optimizing test function vary too.

[](#conj:cmh-second-variation) is the sharpest available probe of the approach because it attacks the target inequality $\mathrm{CMH}(4)$ itself rather than the machinery built to prove it, and because both ingredients are already exact: the saturation value comes from [](#thm:cmh-product) and the splitting from [](#prop:cmh-hodge). Together with [](#rem:gate-zero-dichotomy) it forms the falsification layer of the moment-map approach; [](#conj:mm-invariant-lift) and [](#conj:mm-square-root-commutator) form the construction layer.
