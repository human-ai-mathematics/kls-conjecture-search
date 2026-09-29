---
title: 'Solution candidate: time-weighted fixed-function source budget'
label: sec:sol-lem-mm-time-weighted-fixed-source
ledger-node: lem:mm-time-weighted-fixed-source
numbering:
  enumerator: D18.%s
---

**Overview.** This dossier proves [](#lem:mm-time-weighted-fixed-source) as [](#thm:sol-lem-mm-time-weighted-fixed-source). The setting is a smooth log-concave law with $\nabla^2V\succeq\kappa I_n$, $\kappa\ge0$, an arbitrary fixed test $f\in L^2(\mu)$ and the planted channel. The time-weighted source $\E\int_0^T(\kappa+t)\norm{H_t}_{\HS}^2\dd t$, plus a nonnegative remainder, is bounded by $\Var_\mu(f)-\kappa\abs{g_0}^2$ ([](#eq:sol-mm-time-weighted-fixed-source)); for $\kappa=0$ this gives [](#eq:sol-mm-time-weighted-infinite). The proof applies Itô's formula to $(\kappa+t)\abs{g_t}^2$ and pays the terms with the posterior variance budget. It then closes from $C_c^\infty$ tests to $L^2(\mu)$. The weight is kept, and no unweighted initial-layer claim is made.

1. The posterior equations and the Brascamp–Lieb cap [](#eq:sol-mm-weighted-covariance-cap) make the remainder nonnegative ([](#eq:sol-mm-weighted-remainder)) and give the terminal cap [](#eq:sol-mm-weighted-terminal-cap).
2. For $f\in C_c^\infty$, the vector $g_t$ solves [](#eq:sol-mm-weighted-g-sde), and Itô's formula gives [](#eq:sol-mm-weighted-product).
3. Localizing, taking expectations, and using step 1 with the variance identity [](#eq:sol-mm-weighted-variance-budget) gives [](#eq:sol-mm-weighted-stopped-bound). Monotone convergence then removes the stopping.
4. Closure to $L^2(\mu)$: $g^j\to g$ strongly ([](#eq:sol-mm-weighted-g-closure)) and $H^j\to H$ in $L^1$ ([](#eq:sol-mm-weighted-H-L1)). Weak lower semicontinuity then passes the step-3 bound to the limit.
5. Setting $\kappa=0$, dropping the remainder and letting $T\uparrow\infty$ gives [](#eq:sol-mm-time-weighted-infinite).

**Refined statement and admissible class.** The following theorem makes the square-integrable admissible class and the posterior coupling in [](#lem:mm-time-weighted-fixed-source) explicit. No centering, isotropy, or eigenfunction hypothesis is imposed.

:::{prf:theorem} = [](#lem:mm-time-weighted-fixed-source)
:label: thm:sol-lem-mm-time-weighted-fixed-source
Let

$$
\dd\mu(x)=Z^{-1}e^{-V(x)}\dd x
$$

be a smooth log-concave probability measure on $\R^n$, where $V\in C^\infty(\R^n)$ and $\nabla^2V\succeq\kappa I_n$ for some $\kappa\ge0$. Take $X\sim\mu$ and an independent standard Brownian motion $B^{\mathrm{obs}}$, and set

$$
c_t=tX+B_t^{\mathrm{obs}},
\qquad
\mathcal F_t^{\mathrm{obs}}=\sigma(c_s:0\le s\le t),
\qquad
\mu_t=\mathcal L(X\mid\mathcal F_t^{\mathrm{obs}}).
$$

For an arbitrary fixed $f\in L^2(\mu)$, write $\E_t$ for integration against $\mu_t$ and put

$$
m_t=\E_tf,
\qquad a_t=\E_tX,
\qquad v_t=\Var_{\mu_t}(f),
\qquad A_t=\Cov_{\mu_t}(X),
$$

$$
g_t=\E_t[(f-m_t)(X-a_t)],
\qquad
H_t=\E_t[(f-m_t)(X-a_t)^{\otimes2}].
$$

The tensor $H$ belongs on every finite horizon to

$$
L^2\bigl(\Omega\times(0,T),(\kappa+t)\,\dd\Prob\,\dd t;
\operatorname{Sym}_n\bigr),
$$

and, for every $T>0$,

```{math}
:label: eq:sol-mm-time-weighted-fixed-source
\begin{aligned}
&\E\int_0^T(\kappa+t)\norm{H_t}_{\HS}^2\dd t
+2\E\int_0^T\left(\abs{g_t}^2-(\kappa+t)g_t^TA_tg_t\right)\dd t \\
&\hspace{7em}\le \Var_\mu(f)-\kappa\abs{g_0}^2.
\end{aligned}
```

Both integrands on the left are nonnegative. In particular, when $\kappa=0$,

```{math}
:label: eq:sol-mm-time-weighted-infinite
\E\int_0^\infty t\norm{H_t}_{\HS}^2\dd t\le\Var_\mu(f).
```

The conclusion retains one power of time and makes no unweighted initial-layer assertion.
:::

:::{prf:proof}
*Posterior equations and curvature bounds.* Conditional on $X=x$, the observation likelihood up to time $t$ is proportional to $\exp(c_t\cdot x-t\abs{x}^2/2)$. Hence

```{math}
:label: eq:sol-mm-weighted-posterior
\dd\mu_t(x)
=\frac{\exp(c_t\cdot x-t\abs{x}^2/2)}
{\int\exp(c_t\cdot y-t\abs{y}^2/2)\dd\mu(y)}\,\dd\mu(x).
```

The innovation process

$$
W_t=c_t-\int_0^ta_s\dd s
$$

is an $n$-dimensional Brownian motion in the observation filtration, and the filtering identity for a fixed integrable test $\phi$ is

```{math}
:label: eq:sol-mm-weighted-filtering
\dd\E_t\phi=\Cov_{\mu_t}(\phi,X)\cdot\dd W_t,
```

first for bounded tests and then, in the square-integrable cases used below, by $L^2$ closure.

The posterior potential in [](#eq:sol-mm-weighted-posterior) has Hessian $\nabla^2V+tI_n\succeq(\kappa+t)I_n$. Brascamp–Lieb applied to linear functions therefore gives, with $w_t=\kappa+t$,

```{math}
:label: eq:sol-mm-weighted-covariance-cap
w_tA_t\preceq I_n.
```

When $w_t=0$, this is read as the trivial positive-semidefinite inequality. Consequently

```{math}
:label: eq:sol-mm-weighted-remainder
\mathcal R_t:=\abs{g_t}^2-w_tg_t^TA_tg_t
=g_t^T(I_n-w_tA_t)g_t\ge0.
```

There is also a terminal covariance bound. If $g_t\ne0$, set $u_t=g_t/\abs{g_t}$. Conditional Cauchy–Schwarz and [](#eq:sol-mm-weighted-covariance-cap) yield

$$
\abs{g_t}^2
=\Cov_{\mu_t}(f,u_t\cdot X)^2
\le v_t\,u_t^TA_tu_t
\le\frac{v_t}{w_t}
$$

when $w_t>0$; the case $g_t=0$ is immediate. Thus, also with the evident convention at $w_t=0$,

```{math}
:label: eq:sol-mm-weighted-terminal-cap
w_t\abs{g_t}^2\le v_t.
```

*Compact smooth core and the fixed-function SDE.* Assume temporarily that $f\in C_c^\infty(\R^n)$. Applying [](#eq:sol-mm-weighted-filtering) to $f$, to the coordinates, and to the components of $fX$ gives

$$
\dd m_t=g_t\cdot\dd W_t,
\qquad
\dd a_t=A_t\dd W_t.
$$

Moreover, with matrices oriented by $\Cov_t(fX,X)_{ij}=\Cov_t(fX_i,X_j)$,

$$
\Cov_t(fX,X)=H_t+m_tA_t+a_t\otimes g_t.
$$

Since $g_t=\E_t(fX)-m_ta_t$, Itô's product rule, including $\dd[m,a]_t=A_tg_t\dd t$, now gives the exact equation

```{math}
:label: eq:sol-mm-weighted-g-sde
\dd g_t=H_t\dd W_t-A_tg_t\dd t.
```

Itô's formula and multiplication by $w_t$ give

```{math}
:label: eq:sol-mm-weighted-product
\begin{aligned}
\dd\bigl(w_t\abs{g_t}^2\bigr)
&=2w_tg_t^TH_t\dd W_t \\
&\quad+
\left(w_t\norm{H_t}_{\HS}^2+2\mathcal R_t-\abs{g_t}^2\right)\dd t.
\end{aligned}
```

We justify taking expectations in this identity on a finite horizon. Fix $T>0$ and let

$$
L_t=\int_0^t2w_sg_s^TH_s\dd W_s.
$$

The compact support of $f$ and the Gaussian factor in [](#eq:sol-mm-weighted-posterior) make all posterior coefficients finite and continuous on compact time intervals. In particular $L$ is a continuous local martingale with finite quadratic variation on $[0,T]$. Choose increasing stopping times $\tau_N$ that simultaneously localize $L$ and all finite-variation terms in [](#eq:sol-mm-weighted-product), so that $L^{\tau_N}$ is a square-integrable martingale and $\tau_N\uparrow\infty$ almost surely, and write $\theta_N=T\wedge\tau_N$. Integrating [](#eq:sol-mm-weighted-product) to $\theta_N$ gives

```{math}
:label: eq:sol-mm-weighted-stopped-ito
\E\int_0^{\theta_N}
\left(w_t\norm{H_t}_{\HS}^2+2\mathcal R_t\right)\dd t
=\E\bigl[w_{\theta_N}\abs{g_{\theta_N}}^2\bigr]
-\kappa\abs{g_0}^2
+\E\int_0^{\theta_N}\abs{g_t}^2\dd t.
```

The stopped posterior variance pays exactly for the last two terms. Indeed, $m$ is a bounded martingale for the present compactly supported $f$, so the stopped Itô isometry and the conditional-law property at $\theta_N$ imply

$$
\E m_{\theta_N}^2-m_0^2
=\E\int_0^{\theta_N}\abs{g_t}^2\dd t,
\qquad
\E v_{\theta_N}=\E_\mu f^2-\E m_{\theta_N}^2.
$$

Therefore

```{math}
:label: eq:sol-mm-weighted-variance-budget
\E v_{\theta_N}
+\E\int_0^{\theta_N}\abs{g_t}^2\dd t
=\Var_\mu(f).
```

Using [](#eq:sol-mm-weighted-terminal-cap) in [](#eq:sol-mm-weighted-stopped-ito), followed by [](#eq:sol-mm-weighted-variance-budget), yields

```{math}
:label: eq:sol-mm-weighted-stopped-bound
\E\int_0^{\theta_N}
\left(w_t\norm{H_t}_{\HS}^2+2\mathcal R_t\right)\dd t
\le\Var_\mu(f)-\kappa\abs{g_0}^2.
```

Both terms in the integrand are nonnegative by [](#eq:sol-mm-weighted-remainder). Since $\theta_N\uparrow T$, monotone convergence removes the stopping and proves [](#eq:sol-mm-time-weighted-fixed-source) for $f\in C_c^\infty(\R^n)$.

*Closure from $C_c^\infty$ to $L^2(\mu)$.* Let now $f\in L^2(\mu)$ be arbitrary, and choose $f_j\in C_c^\infty(\R^n)$ with $f_j\to f$ in $L^2(\mu)$. Denote by $m^j,g^j,H^j$ the corresponding posterior quantities. For $\delta_j=f_j-f$, put $M_t^j=\E_t\delta_j$. The $L^2$ closure of [](#eq:sol-mm-weighted-filtering) and the martingale isometry give

```{math}
:label: eq:sol-mm-weighted-g-closure
\E\int_0^T\abs{g_t^j-g_t}^2\dd t
=\E\left|M_T^j-M_0^j\right|^2
\le\norm{\delta_j}_{L^2(\mu)}^2.
```

Thus $g^j\to g$ strongly in $L^2(\Omega\times(0,T))$. Because $0\preceq I_n-w_tA_t\preceq I_n$, this also gives

```{math}
:label: eq:sol-mm-weighted-remainder-closure
\E\int_0^T\mathcal R_t(f_j)\dd t
\longrightarrow
\E\int_0^T\mathcal R_t(f)\dd t.
```

We next identify the tensor limit without assuming any weighted moment of $f$. A smooth log-concave probability has finite fourth moment. Conditional Jensen gives, uniformly in $t\ge0$,

```{math}
:label: eq:sol-mm-weighted-residual-fourth
\E\abs{X-a_t}^4
\le8\left(\E\abs X^4+\E\abs{a_t}^4\right)
\le16\E\abs X^4.
```

Linearity of the centered posterior covariance shows that

$$
H_t^j-H_t
=\E_t\left[(\delta_j-\E_t\delta_j)(X-a_t)^{\otimes2}\right].
$$

Conditional Jensen, Cauchy–Schwarz, the tower property, and [](#eq:sol-mm-weighted-residual-fourth) therefore imply, for a finite constant depending only on the fourth moment of this fixed $\mu$,

```{math}
:label: eq:sol-mm-weighted-H-L1
\sup_{t\ge0}\E\norm{H_t^j-H_t}_{\HS}
\le C_\mu\norm{\delta_j}_{L^2(\mu)}\longrightarrow0.
```

For completeness, the two terms bounded here are

$$
\E\!\left[\abs{\delta_j(X)}\abs{X-a_t}^2\right]
\quad\text{and}\quad
\E\!\left[\abs{\E_t\delta_j}\,\E_t\abs{X-a_t}^2\right];
$$

each is at most a fixed multiple of $\norm{\delta_j}_{L^2(\mu)}(\E\abs X^4)^{1/2}$.

The already proved estimate and nonnegativity of $\mathcal R_t(f_j)$ show that $H^j$ is bounded in the weighted Hilbert space appearing in the theorem. Extract a weakly convergent subsequence. The strong $L^1(\Omega\times(0,T))$ convergence in [](#eq:sol-mm-weighted-H-L1) identifies its weak limit with the displayed posterior tensor $H$. Weak lower semicontinuity, together with [](#eq:sol-mm-weighted-remainder-closure), gives

$$
\begin{aligned}
&\E\int_0^Tw_t\norm{H_t}_{\HS}^2\dd t
+2\E\int_0^T\mathcal R_t(f)\dd t\\
&\qquad\le
\liminf_{j\to\infty}\left(
\E\int_0^Tw_t\norm{H_t^j}_{\HS}^2\dd t
+2\E\int_0^T\mathcal R_t(f_j)\dd t\right)\\
&\qquad\le
\lim_{j\to\infty}\left(\Var_\mu(f_j)-\kappa\abs{g_0^j}^2\right)
=\Var_\mu(f)-\kappa\abs{g_0}^2.
\end{aligned}
$$

Here $g_0^j\to g_0$ because $X\in L^2(\mu)$. This proves the finite-horizon assertion for every $f\in L^2(\mu)$ and, at the same time, proves the asserted weighted $L^2$ membership of $H$.

Finally set $\kappa=0$. Dropping the nonnegative remainder term from the finite-horizon bound gives

$$
\E\int_0^Tt\norm{H_t}_{\HS}^2\dd t\le\Var_\mu(f)
$$

for every $T$. Monotone convergence as $T\uparrow\infty$ proves [](#eq:sol-mm-time-weighted-infinite).
:::

:::{prf:remark} What the weight does not provide
The factor $t$ vanishes at the initial endpoint when $\kappa=0$. Thus [](#eq:sol-mm-time-weighted-infinite) alone does not bound $\E\int_0^\varepsilon\norm{H_t}_{\HS}^2\dd t$ uniformly in $\varepsilon$, nor does it imply the unweighted source estimate in [](#q:mm-spectral-occupation). Analytically, finiteness of $\int_0^1tF(t)\dd t$ for a nonnegative function does not imply finiteness of $\int_0^1F(t)\dd t$; no deweighting step has been used or claimed here.
:::

:::{prf:remark} Hypotheses actually used
The proof uses only the planted Gaussian posterior, the curvature bound $\nabla^2V\succeq\kappa I_n$, square-integrability of the fixed test, and the finite fourth moment of the fixed smooth log-concave law for the $L^2$ approximation. It uses no eigenfunction equation, isotropy, Letwin input, cut, numerical evidence, or unresolved premise. There is no approximation of the measure and no conclusion for nonsmooth or lower-dimensional limiting laws in this dossier.
:::

**Obstructions respected.** The ledger node has no formal `bounded_by` edge. The proof nevertheless stays on the permitted side of all recorded KLS fences: it contains no slice or cut estimate (`obs:two-tail`, `obs:circularity`, and `obs:rank-one-refuted`), no radial or projection reduction (`obs:proj-ceiling`), and no covariance occupation bootstrap (`obs:crude-insufficient` and `obs:relative-ceiling`). It uses the posterior covariance cap only to keep the explicitly weighted remainder nonnegative; it neither unweights the tensor nor claims dimension-free control of the initial layer.
