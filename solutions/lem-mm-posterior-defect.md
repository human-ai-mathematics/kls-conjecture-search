---
title: 'Solution: posterior eigenfunction-defect calculus'
label: sec:sol-lem-mm-posterior-defect
ledger-node: lem:mm-posterior-defect
numbering:
  enumerator: D14.%s
---

*Part of the fixed-eigenfunction mechanism, Chapter [](#sec:spectral-approach); the reading order is on the [full proofs](#sec:proofs-eigenfunction) page.*

**Overview.** This dossier proves [](#lem:mm-posterior-defect) as [](#thm:sol-lem-mm-posterior-defect). The setting is a smooth, strongly log-concave, isotropic law, a normalized first eigenfunction $f$, and the planted Gaussian observation channel. The posterior defect $R_t$ obeys three exact integration-by-parts identities [](#eq:sol-mm-defect-identities), two variance budgets [](#eq:sol-mm-defect-budgets) and an averaged gradient bound [](#eq:sol-mm-defect-gradient). The identities come from pairing a posterior generator relation with constant, linear and quadratic tests. The budgets come from filtering martingales and the planted cancellation $R_t(X)=B_t^{\mathrm{obs}}\cdot\nabla f(X)$. The imported node [](#thm:letwin-qcts) is not used.

1. The posterior density [](#eq:sol-mm-posterior-density) and the innovation Brownian motion give the filtering equation [](#eq:sol-mm-filtering). The posterior generator is [](#eq:sol-mm-Lt), with its domains justified by cutoffs and stopping.
2. The generator relation [](#eq:sol-mm-generator-defect) is paired with constants, coordinates and centered quadratics $Q_D$. This gives the three identities [](#eq:sol-mm-defect-identities).
3. The planted cancellation [](#eq:sol-mm-planted-defect) gives $\E\E_tR_t^2=t\lambda$ ([](#eq:sol-mm-defect-second-moment)). Combined with the Itô isometry for $m_t$ and the first identity of step 2, this yields the centered-defect budget.
4. Filtering applied to $\nabla f$ gives the isometry [](#eq:sol-mm-C-isometry). Conditional Jensen, together with $b_0=\lambda g_0$ from step 2, bounds the $C_t$ budget.
5. The gradient of $R_t$ is evaluated at the planted point ([](#eq:sol-mm-gradient-defect-exact)). The weighted Bochner identity and convexity bound $\E_\mu\norm{\nabla^2f}_{\HS}^2\le\lambda^2$, which proves [](#eq:sol-mm-defect-gradient).

**Refined statement.** The regular setting in the following theorem makes explicit the domain and normalization conventions implicit in [](#lem:mm-posterior-defect). For vectors $v,w\in\R^n$ we use $(v\otimes w)_{ij}=v_iw_j$, and $\operatorname{sym}M=(M+M^T)/2$.

:::{prf:theorem} = [](#lem:mm-posterior-defect)
:label: thm:sol-lem-mm-posterior-defect
Let

$$
\dd\mu(x)=Z^{-1}e^{-V(x)}\dd x
$$

be a smooth, strongly log-concave, centered isotropic probability measure on $\R^n$: $V\in C^\infty(\R^n)$ and $\nabla^2V\succeq\varepsilon I_n$ for some $\varepsilon>0$. Let $L=\Delta-\nabla V\cdot\nabla$ denote its Friedrichs self-adjoint realization in $L^2(\mu)$, and let $f$ be a normalized first nonconstant eigenfunction,

$$
-Lf=\lambda f,
\qquad \E_\mu f=0,
\qquad \E_\mu f^2=1.
$$

In particular, $f$ is understood in the generator domain; all identities below use the closed Dirichlet-form interpretation, so there is no boundary condition hidden at infinity.

Take $X\sim\mu$ and an independent standard Brownian motion $B^{\mathrm{obs}}$, set

$$
c_t=tX+B_t^{\mathrm{obs}},
\qquad
\mathcal F_t^{\mathrm{obs}}=\sigma(c_s:0\le s\le t),
$$

and let $\mu_t=\mathcal L(X\mid\mathcal F_t^{\mathrm{obs}})$. Write $\E_t$ for integration against $\mu_t$, $a_t=\E_tX$, and

$$
m_t=\E_tf,
\qquad
g_t=\E_t[(f-m_t)(X-a_t)],
\qquad
H_t=\E_t[(f-m_t)(X-a_t)^{\otimes2}].
$$

For the posterior defect

$$
R_t(x)=(c_t-tx)\cdot\nabla f(x),
\qquad
\rho_t=R_t-\E_tR_t,
$$

define, with the displayed tensor orientation,

$$
b_t=\E_t\nabla f,
\qquad
C_t=\E_t[(X-a_t)\otimes\nabla f],
\qquad
u_t=\E_t[\rho_t(X-a_t)],
\qquad
K_t=\E_t[\rho_t(X-a_t)^{\otimes2}].
$$

Then, for every $t\ge0$, almost surely in the pointwise posterior identities,

```{math}
:label: eq:sol-mm-defect-identities
\begin{aligned}
\E_tR_t&=\lambda m_t,
&\lambda g_t&=b_t+u_t,
&\lambda H_t&=2\operatorname{sym}C_t+K_t,
\end{aligned}
```

```{math}
:label: eq:sol-mm-defect-budgets
\begin{aligned}
\E\Var_t(R_t)
&=t\lambda-\lambda^2\int_0^t\E\abs{g_s}^2\dd s,
&\E\int_0^t\norm{C_s}_{\HS}^2\dd s
&\le \lambda-\lambda^2\abs{g_0}^2,
\end{aligned}
```

```{math}
:label: eq:sol-mm-defect-gradient
\begin{aligned}
\E\E_t\abs{\nabla R_t}^2
&\le t\lambda^2+t^2\lambda.
\end{aligned}
```

Here the un-subscripted expectation averages the planted observation model, and $\Var_t(R_t)=\E_t\rho_t^2$.
:::

:::{prf:proof}
*Posterior and innovation equations.* The likelihood of the observation path up to time $t$, conditional on $X=x$, depends on that path only through $c_t$ and is proportional to $\exp(c_t\cdot x-t\abs{x}^2/2)$. Hence

```{math}
:label: eq:sol-mm-posterior-density
\dd\mu_t(x)
=\frac{\exp(c_t\cdot x-t\abs{x}^2/2)}
{\int\exp(c_t\cdot y-t\abs{y}^2/2)\dd\mu(y)}\,\dd\mu(x).
```

Put

$$
W_t=c_t-\int_0^ta_s\dd s.
$$

Since $\E[X\mid\mathcal F_t^{\mathrm{obs}}]=a_t$, the process $W$ is a continuous $\mathcal F_t^{\mathrm{obs}}$-local martingale with quadratic covariation $[W^i,W^j]_t=\delta_{ij}t$. Lévy's characterization therefore makes $W$ an $n$-dimensional Brownian motion. Applying Itô's formula to [](#eq:sol-mm-posterior-density) gives

```{math}
:label: eq:sol-mm-density-sde
\dd\mu_t(x)=\mu_t(x)(x-a_t)\cdot\dd W_t.
```

Consequently, for every fixed scalar $\phi\in L^2(\mu)$,

```{math}
:label: eq:sol-mm-filtering
\dd\E_t\phi=\Cov_t(\phi,X)\cdot\dd W_t.
```

We record the localization and domain justification used throughout. First take bounded smooth truncations of $\phi$ and stop at the first time when the stochastic-integral quadratic variation or the posterior moments occurring in the calculation reach level $N$. Equations [](#eq:sol-mm-density-sde)–[](#eq:sol-mm-filtering) are then ordinary bounded Itô identities. Conditional expectation is a contraction in $L^2$, so bounded truncations of $f$ and of each component of $\nabla f$ converge to their square-integrable conditional-expectation martingales. Their stopped stochastic integrals therefore converge in $L^2$, and the stopping times increase to infinity. This removes the stopping without losing any equality below.

For the spatial integrations by parts, the posterior potential is

$$
V_t(x)=V(x)-c_t\cdot x+\frac t2\abs{x}^2,
\qquad \nabla^2V_t\succeq(\varepsilon+t)I_n.
$$

Thus $\mu_t$ has all polynomial moments. The closed Dirichlet form

$$
\mathcal E_t(h,k)=\E_t[\nabla h\cdot\nabla k],
\qquad h,k\in W^{1,2}(\mu_t),
$$

has generator

```{math}
:label: eq:sol-mm-Lt
L_t=\Delta-\nabla V_t\cdot\nabla
=L+(c_t-tx)\cdot\nabla.
```

The identities below are first paired with compactly supported cutoffs of the coordinate and centered-quadratic tests. The Gaussian tails of $\mu_t$, the $L^2$ bounds established by the planted coupling below, and closedness of $\mathcal E_t$ let the cutoff radius tend to infinity. Equivalently, the coordinates and centered quadratics belong to the required local form domain, and $f$ belongs to the maximal generator domain of $L_t$ because both $f$ and $L_tf$ are in $L^2(\mu_t)$. This specifies the domain in every use of posterior integration by parts.

*The defect identities.* The eigenfunction equation and [](#eq:sol-mm-Lt) give the exact generator relation

```{math}
:label: eq:sol-mm-generator-defect
-L_tf=\lambda f-R_t.
```

Pairing this identity with the constant function in the posterior Dirichlet form yields

$$
0=\E_t[-L_tf]=\lambda m_t-\E_tR_t,
$$

which is the first identity in [](#eq:sol-mm-defect-identities).

Pair next with the coordinate $x_i-a_{t,i}$. Posterior integration by parts gives

$$
\E_t[(-L_tf)(X_i-a_{t,i})]=\E_t\partial_i f=(b_t)_i.
$$

Because $\E_t(X-a_t)=0$ and $\rho_t=R_t-\lambda m_t$, the same left-hand side, evaluated with [](#eq:sol-mm-generator-defect), is $(\lambda g_t-u_t)_i$. Thus $\lambda g_t=b_t+u_t$.

Finally fix an arbitrary symmetric matrix $D$ and set

$$
Q_D(x)=(x-a_t)^TD(x-a_t)-\Tr(DA_t).
$$

Then $\E_tQ_D=0$, $\nabla Q_D=2D(x-a_t)$, and our orientation for $C_t$ gives

$$
\begin{aligned}
\E_t[(-L_tf)Q_D]
&=\E_t[\nabla f\cdot\nabla Q_D]
=2\langle D,\operatorname{sym}C_t\rangle_{\HS},\\
\E_t[(\lambda f-R_t)Q_D]
&=\langle D,\lambda H_t-K_t\rangle_{\HS}.
\end{aligned}
$$

The two expressions agree by [](#eq:sol-mm-generator-defect). Since they agree for every symmetric $D$ and both $H_t,K_t$ are symmetric, we obtain $\lambda H_t=2\operatorname{sym}C_t+K_t$.

*The centered-defect budget.* At the planted point, the definition of the observation gives the cancellation

```{math}
:label: eq:sol-mm-planted-defect
R_t(X)=B_t^{\mathrm{obs}}\cdot\nabla f(X).
```

The usual energy identity for the normalized eigenfunction is

```{math}
:label: eq:sol-mm-gradient-energy
\E_\mu\abs{\nabla f}^2
=\langle f,-Lf\rangle_{L^2(\mu)}=\lambda.
```

Since $B_t^{\mathrm{obs}}$ is independent of $X$, has mean zero, and has covariance $tI_n$, the conditional-law property and [](#eq:sol-mm-planted-defect) imply

```{math}
:label: eq:sol-mm-defect-second-moment
\E\E_tR_t^2
=\E\abs{B_t^{\mathrm{obs}}\cdot\nabla f(X)}^2
=t\lambda.
```

In particular, the $L^2(\mu_t)$ assertion used in the domain paragraph holds for almost every observation.

Apply [](#eq:sol-mm-filtering) to $f$. Since $m_0=0$ and $\Cov_t(f,X)=g_t$, the square-integrable martingale $m$ satisfies

$$
\dd m_t=g_t\cdot\dd W_t,
\qquad
\E m_t^2=\int_0^t\E\abs{g_s}^2\dd s.
$$

The second equality is first the stopped Itô isometry; it remains an equality after removal because $m_t=\E[f(X)\mid\mathcal F_t^{\mathrm{obs}}]$ is bounded in $L^2$. Using $\E_tR_t=\lambda m_t$ and conditional variance decomposition in [](#eq:sol-mm-defect-second-moment) now gives

$$
\E\Var_t(R_t)
=\E\E_tR_t^2-\E(\E_tR_t)^2
=t\lambda-\lambda^2\int_0^t\E\abs{g_s}^2\dd s.
$$

*The $C_t$ martingale budget.* Apply the vector form of [](#eq:sol-mm-filtering) to the fixed vector field $\nabla f$. With the orientation specified in the theorem,

$$
\dd b_t=C_t^T\dd W_t.
$$

The martingale $b_t=\E[\nabla f(X)\mid\mathcal F_t^{\mathrm{obs}}]$ is square-integrable by [](#eq:sol-mm-gradient-energy). The stopped vector Itô isometry and the same $L^2$ stopping-removal argument therefore give

```{math}
:label: eq:sol-mm-C-isometry
\E\int_0^t\norm{C_s}_{\HS}^2\dd s
=\E\abs{b_t}^2-\abs{b_0}^2.
```

Conditional Jensen and the tower property show that $\E\abs{b_t}^2\le\E\abs{\nabla f(X)}^2=\lambda$. At time zero, $c_0=0$ and hence $R_0=\rho_0=u_0=0$; the already proved coordinate identity gives $b_0=\lambda g_0$. Substitution in [](#eq:sol-mm-C-isometry) proves the second estimate in [](#eq:sol-mm-defect-budgets).

*The averaged gradient-defect budget.* Differentiating $R_t$ with respect to its spatial argument gives

```{math}
:label: eq:sol-mm-gradient-defect-formula
\nabla R_t(x)=\nabla^2f(x)(c_t-tx)-t\nabla f(x).
```

Evaluate at the planted point and use $c_t-tX=B_t^{\mathrm{obs}}$. Independence and centering of $B_t^{\mathrm{obs}}$ make the cross term vanish, while its covariance is $tI_n$. Therefore

```{math}
:label: eq:sol-mm-gradient-defect-exact
\E\E_t\abs{\nabla R_t}^2
=t\E_\mu\norm{\nabla^2f}_{\HS}^2+t^2\E_\mu\abs{\nabla f}^2.
```

For the Friedrichs realization, the integrated weighted Bochner identity, justified by the same compact cutoff approximation, is

$$
\E_\mu(Lf)^2
=\E_\mu\norm{\nabla^2f}_{\HS}^2
+\E_\mu\langle\nabla^2V\nabla f,\nabla f\rangle.
$$

Convexity of $V$, the eigenfunction equation, and normalization consequently imply

$$
\E_\mu\norm{\nabla^2f}_{\HS}^2
\le\E_\mu(Lf)^2=\lambda^2.
$$

Combining this with [](#eq:sol-mm-gradient-energy) and [](#eq:sol-mm-gradient-defect-exact) gives [](#eq:sol-mm-defect-gradient). All limiting operations used here are either $L^2$ limits of the two conditional-expectation martingales or closed-form $L^2$ limits of the spatial cutoff approximations, so the auxiliary stopping and spatial cutoffs have now been removed completely.
:::

:::{prf:remark} Excluded conditional consequence
No use is made of the imported, unreviewed node `thm:letwin-qcts`. In particular, a whitened quadratic estimate for $K_t$ conditional on that node is outside this theorem and this dossier. The identities proved here do not unwhiten the high-covariance part of $H_t$, do not establish the high-incidence occupation estimate, and supply no approximation passage to an arbitrary log-concave law.
:::

**Obstructions respected.** The ledger node has no formal `bounded_by` edge. The route fences were nevertheless checked individually. The proof uses no cut or slice estimate, so `rem:two-tail-slice-bounds`, `rem:profile-circularity`, and `rem:single-coordinate-cuts` are not engaged. It derives exact coordinate and full symmetric-matrix integration-by-parts identities rather than a dimension-free quadratic-chaos theorem from radial or projection tests, so it does not cross `rem:projection-ceiling`. It uses neither the crude covariance integral nor a relative covariance occupation bound, respecting `rem:crude-insufficient` and `rem:relative-ceiling`. Finally, it never bounds a posterior covariance operator norm, never unwhitens a tensor, and never invokes the refuted truncated-exponential variable-weight Stein shortcut; hence it also respects the covariance-spike and spectral-unwhitening warnings. The transport and needle warnings are inapplicable because neither mechanism occurs.
