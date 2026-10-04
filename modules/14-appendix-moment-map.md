---
numbering:
  enumerator: "14.%s"
---

(sec:appendix-moment-map)=
# Moment-map operator theory, Dirichlet and Gamma computations

The calculations the moment-map approach rests on, in the order it needs them: the two operator-core arguments of the normalization layer, then the Gamma lift (the simplex rewritten in independent Gamma coordinates, Section [](#subsec:cmh-gamma-lift)) and the angular minimization that produce the exact Dirichlet constant. Every statement whose proof is given here is stated, with a summary of its proof, in Section [](#sec:cmh-normalization) or Section [](#sec:cmh-exact-cases). Nothing is decided here that is not decided there.

:::{prf:proof} Proof of [](#prop:cmh-bochner)
We calculate in target coordinates, use Einstein summation, and first take $g$ in a smooth compactly supported core. Write $\rho$ for the density of $\mu$. The Stein identity is

$$
\partial_i(\rho H_{ij})=-\rho p_j,
\qquad L_\mu g=H_{k\ell}g_{k\ell}-p_k g_k.
$$

One integration by parts, followed by differentiating the displayed formula for $L_\mu g$, gives

$$
\begin{aligned}
\E_\mu(L_\mu g)^2
={}&\E_\mu[H_{ij}g_i g_j]
-\E_\mu[H_{ij}g_j(\partial_iH_{k\ell})g_{k\ell}]\\
&-\E_\mu[H_{ij}g_jH_{k\ell}g_{ik\ell}]
+\E_\mu[H_{ij}g_jp_k g_{ik}].
\end{aligned}
$$

Integrating the third-derivative term by parts in $p_k$ yields

$$
\begin{aligned}
-\E_\mu[H_{ij}g_jH_{k\ell}g_{ik\ell}]
={}&-\E_\mu[p_\ell H_{ij}g_jg_{i\ell}]
+\E_\mu[H_{k\ell}(\partial_kH_{ij})g_jg_{i\ell}]\\
&+\E_\mu[H_{k\ell}H_{ij}g_{jk}g_{i\ell}].
\end{aligned}
$$

The first term here cancels the last term in the preceding display after relabelling $k$ and $\ell$, while the last one equals $\Tr(HD^2g\,HD^2g)$.

It remains to cancel the two terms containing $\partial H$. If $p=\nabla\varphi(y)$, then $H_{k\ell}(p)=\varphi_{k\ell}(y)$ and

```{math}
:label: eq:cmh-codazzi
H_{mj}\partial_jH_{k\ell}
=H_{mj}(H^{-1})_{rj}\varphi_{k\ell r}
=\varphi_{mk\ell}.
```

Thus $H_{mj}\partial_jH_{k\ell}$ is totally symmetric in $m,k,\ell$. Using symmetry of $H$ and [](#eq:cmh-codazzi), the residual is

$$
\E_\mu[g_jg_{i\ell}\varphi_{\ell ij}]
-\E_\mu[g_jg_{k\ell}\varphi_{jk\ell}]=0.
$$

This proves [](#eq:cmh-bochner) on the smooth core. If $g_q$ is graph-norm Cauchy there, apply the identity to $g_q-g_r$. Nonnegativity of the two right-hand terms shows that $H^{1/2}\nabla g_q$ and $H^{1/2}D^2g_qH^{1/2}$ are Cauchy in their respective $L^2$ spaces. Their limits define the closed right-hand side, and passage to the limit proves the identity on the operator-core closure.
:::

:::{prf:proof} Proof of [](#thm:cmh-implies-affine-poincare)
Put $C=\CMH(\mu)$; there is nothing to prove if $C=\infty$. Let $\mathscr C$ be the restrictions to $\operatorname{supp}\mu$ of $\R+C_c^\infty(\R^n)$ and first take a centered $f\in\mathscr C$. This class lies in both form domains even when $H$ is unbounded: the Stein normalization $\E_\mu H=\Sigma$ gives

$$
\E_\mu\inner{H\nabla f}{\nabla f}
\le \norm{\nabla f}_\infty^2\E_\mu\Tr H
=\norm{\nabla f}_\infty^2\Tr\Sigma<\infty.
$$

For $0<\eps<R$ set

$$
\Pi_{\eps,R}=\one_{[\eps,R]}(\Aop),
\qquad g_{\eps,R}=\Pi_{\eps,R}\Aop^{-1}f\in\Dom(\Aop).
$$

Then $\Aop g_{\eps,R}=\Pi_{\eps,R}f$. The form–operator pairing, rather than any commutation of $\Pi_{\eps,R}$ with the $\Sigma$-form, gives

$$
\begin{aligned}
\norm{\Pi_{\eps,R}f}_2^2
&=\inner{f}{\Pi_{\eps,R}f}_{L^2}
=\inner{f}{\Aop g_{\eps,R}}_{L^2}
=\E_\mu\inner{\nabla f}{H\nabla g_{\eps,R}}\\
&\le
\bigl(\E_\mu\inner{\Sigma\nabla f}{\nabla f}\bigr)^{1/2}
\bigl(\E_\mu\inner{H\nabla g_{\eps,R}}
{\Sigma^{-1}H\nabla g_{\eps,R}}\bigr)^{1/2}\\
&\le C^{1/2}
\bigl(\E_\mu\inner{\Sigma\nabla f}{\nabla f}\bigr)^{1/2}
\norm{\Pi_{\eps,R}f}_2.
\end{aligned}
$$

After division (with the zero case harmless) and squaring,

$$
\norm{\Pi_{\eps,R}f}_2^2
\le C\E_\mu\inner{\Sigma\nabla f}{\nabla f}.
$$

Because $H\succ0$ and the support is connected, $\ker\Aop$ consists of the constants. Thus $f\perp\ker\Aop$, and the spectral theorem gives $\Pi_{\eps,R}f\to f$ in $L^2$ as $R\to\infty$ and then $\eps\downarrow0$.

Finally define $H^1_\Sigma(\mu)$ as the closure of $\mathscr C$ for $\norm{f}_2^2+\E_\mu\inner{\Sigma\nabla f}{\nabla f}$ (equivalently the usual $H^1(\mu)$ here, since $\Sigma\succ0$ is constant). Approximate an arbitrary $f\in H^1_\Sigma(\mu)$ by functions in $\mathscr C$ and subtract their means. Both the variances and the $\Sigma$-energies converge, so the preceding inequality passes to the limit. Notice that this density step never asserts that finite $\Sigma$-energy implies finite $H$-energy when $H$ is unbounded.
:::

:::{prf:proof} Proof of [](#lem:cmh-gamma-completion)
For $Y\sim\GammaLaw(a,1)$, integrating $\E[Y^2(u^2)']$ by parts against $y^{a-1}e^{-y}$ gives $\E[Y^2uu']=-\tfrac12\E[((a+1)Y-Y^2)u^2]$. Apply this with $u=G_i$, $u'=G_{ii}$, $a=\alpha_i$ and expand the first square in [](#eq:cmh-Ri-deltai): the cross term equals $\E[Y_iG_i^2]-\E[Y_i^2G_i^2]/(\alpha_i+1)$, so

$$
\E R_i=\E\Bigl[Y_iG_i^2+\sum_jY_iY_jG_{ij}^2\Bigr]
-\frac{\alpha_i}{(\alpha_i+1)^2}\E[Y_i^2G_i^2],
$$

using $\tfrac1{(\alpha_i+1)^2}-\tfrac1{\alpha_i+1}=-\tfrac{\alpha_i}{(\alpha_i+1)^2}$. Summing over $i$ recovers $N_\Gamma(G)$ from [](#eq:cmh-gamma-bochner) and leaves $-\sum_i\alpha_i^2(\alpha_i+1)^{-2}D_i(G)$; subtracting $D_\Gamma/4$ gives [](#eq:cmh-gamma-completion). Finally $\delta_i\ge0$ is equivalent to $\alpha_i/(\alpha_i+1)\ge\tfrac12$, i.e. to $\alpha_i\ge1$.
:::

:::{prf:proof} Proof of [](#lem:cmh-row-min)
Euler's identity $\sum_jY_jG_j=0$, differentiated in $Y_i$, gives the single linear constraint $\sum_jY_jG_{ij}=-G_i$. Set $t_i=Y_i\bigl(G_{ii}-G_i/(\alpha_i+1)\bigr)$ and $t_j=Y_jG_{ij}$ for $j\ne i$, so that $\sum_jt_j=-G_i\bigl(1+Y_i/(\alpha_i+1)\bigr)$ and $R_i=t_i^2+\sum_{j\ne i}(Y_i/Y_j)t_j^2$. The reciprocals of these quadratic weights sum to $1+\sum_{j\ne i}Y_j/Y_i=S/Y_i$, and the minimum of $\sum_jw_jt_j^2$ under $\sum_jt_j=c$ is $c^2/\sum_jw_j^{-1}$, which is the right-hand side of [](#eq:cmh-row-min).
:::

:::{prf:proof} Proof of [](#lem:cmh-angular-coefficient)
For fixed $a$ the $p$-dependent part is $a\bigl(p^{-1}+zp(a+1)^{-2}\bigr)$, minimized on $(0,1]$ at $p=1$ when $\sqrt z\le a+1$ and at $p_*=(a+1)/\sqrt z$ otherwise.

If $z\le4$ then $\sqrt z\le2\le a+1$ for all $a\ge1$, so $p=1$ and $F_A=a+2a(A-2)/(a+1)+za/(a+1)-z/4$, each summand increasing in $a$; the minimum at $a=1$ is $A-1+z/4=A-\tfrac12+(z-2)/4$.

If $z\ge4$, then at $p_*$ the two $p$-terms are equal and sum to $2a\sqrt z/(a+1)$, so with $r=a/(a+1)$ the value is $2r(\sqrt z+A-2)+zr^2-z/4$, increasing in $r$; since $r\ge\tfrac12$ for $a\ge1$ the minimum is at $a=1$, $r=\tfrac12$, and equals $A-2+\sqrt z=A-\tfrac12+\sqrt z-\tfrac32$. In the complementary region the expression is increasing in $a$ with a boundary value no smaller. Finally $A\ge3$ gives $z\ge2$, so $s_A\ge0$ in both branches.
:::

:::{prf:proof} Proof of [](#thm:cmh-dirichlet)
If $m=2$ and $A<3$, the law is one dimensional and [](#thm:cmh-1d) applies. In every remaining case $A\ge3$ (automatically when $m\ge3$), so $z_A\ge2>0$ and the inverse moments $\E S^{-1},\E S^{-2}$ used in [](#eq:cmh-radial-relations) are finite.

Combine [](#eq:cmh-gamma-completion), [](#eq:cmh-Ri-deltai) and [](#eq:cmh-integrated-row). Since $D_i(G)=\E[u_i^2]/\alpha_i$, the total coefficient of $\E_P[u_i^2]$ in $N_\Gamma(G)-\tfrac14D_\Gamma(G)$ is

$$
\frac1{z_AP_i}+\frac2{(A-1)(\alpha_i+1)}+\frac{P_i}{(\alpha_i+1)^2}+\frac{\delta_i}{\alpha_i},
$$

and multiplying it by $z_A\alpha_i$ gives exactly $F_A(\alpha_i,P_i)$ of [](#eq:cmh-FA), using $z_A/(A-1)=A-2$. By [](#lem:cmh-angular-coefficient),

$$
N_\Gamma(G)-\tfrac14D_\Gamma(G)
\ \ge\ \frac{A-\tfrac12+s_A}{z_A}\sum_i\frac{\E_P[u_i^2]}{\alpha_i}
=\frac{A-\tfrac12+s_A}{z_A}\,d_\alpha(g).
$$

Substituting [](#eq:cmh-radial-relations), multiplying by $z_A$ and using the identity $z_A/4+A-\tfrac12=A(A+1)/4$ gives

```{math}
:label: eq:cmh-dirichlet-surplus
n_\alpha(g)\ \ge\ \Bigl(\frac{A(A+1)}4+s_A\Bigr)d_\alpha(g),
```

and $s_A\ge0$ yields [](#eq:cmh-dirichlet-main).
:::
