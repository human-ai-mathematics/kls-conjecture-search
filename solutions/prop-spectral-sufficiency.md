---
title: 'Solution: full-damping spectral sufficiency'
label: sec:sol-prop-spectral-sufficiency
ledger-node: prop:spectral-sufficiency
numbering:
  enumerator: D24.%s
---

*Part of the fixed-eigenfunction mechanism, Chapter [](#sec:spectral-approach); the reading order is on the [full proofs](#sec:proofs-eigenfunction) page.*

**Overview.** This dossier proves a refined form of [](#prop:spectral-sufficiency) ([](#thm:sol-prop-spectral-sufficiency)). If the occupation estimate [](#eq:sol-spectral-occupation-hypothesis) of [](#conj:mm-spectral-occupation) holds with dimension- and regularization-free constants and with damping coefficient one, then every isotropic log-concave law satisfies $\CP\le2/T_*$. So a uniform affirmative answer to that open question implies [](#conj:kls). The implication is conditional on that still-open estimate. The method follows the fixed first eigenfunction along stochastic localization, bounds how much of it is learned by time $T_*$, and compares this with posterior Brascamp–Lieb.

1. Fixed-function filtering along the planted observation channel gives $\dd g_t=H_t\dd W_t-A_tg_t\dd t$ ([](#eq:sol-spectral-fixed-function-sde)), hence the $q$-identity [](#eq:sol-spectral-q-identity).
2. Bessel's inequality ([](#eq:sol-spectral-initial-bessel)) and the hypothesis cancel the full damping. Grönwall then gives $q\le M_*$ on $[0,T_0]$ ([](#eq:sol-spectral-gronwall)).
3. The terminal-variance identity [](#eq:sol-spectral-total-variance) with step 2 gives $\E\Var_{\mu_{T_*}}(f)\ge\tfrac12$. Posterior Brascamp–Lieb bounds the same quantity by $\lambda/T_*$ ([](#eq:sol-spectral-terminal-upper)), so $\lambda\ge T_*/2$ on regular laws ([](#eq:sol-spectral-regular-gap)).
4. Gaussian smoothing, a quadratic tilt and isotropization give regular approximants with compact resolvent that converge to any isotropic log-concave $\nu$ in $W_2$ ([](#eq:sol-spectral-isotropization)). Step 3 applies to each of them.
5. The uniform Poincaré inequality, not the eigenfunctions, passes to $\nu$ on fixed test functions by truncation, cutoff, mollification and lower semicontinuity. This gives [](#eq:sol-spectral-gap-conclusion).

**Refined statement.** The following theorem gives constants for the endpoint form of [](#conj:mm-spectral-occupation). In particular, the coefficient of the exact damping is one: no strict damping surplus is assumed.

:::{prf:theorem} Conditional full-damping sufficiency; refines [](#prop:spectral-sufficiency)
:label: thm:sol-prop-spectral-sufficiency
Suppose that there are constants $T_0,C_0,C_1>0$, independent of the dimension and of the regularization, with the following property. Let

$$
\dd\mu(x)=Z^{-1}e^{-V(x)}\dd x
$$

be any smooth strongly log-concave centered isotropic probability measure on $\R^n$ in the regular class of Section [](#subsec:spectral-sde). Let $L=\Delta-\nabla V\cdot\nabla$ be its Friedrichs realization and let

$$
-Lf=\lambda f,
\qquad \E_\mu f=0,
\qquad \E_\mu f^2=1
$$

be a first nonconstant eigenfunction. Along stochastic localization, put

$$
m_t=\E_tf,
\qquad
a_t=\E_tX,
\qquad
A_t=\Cov_{\mu_t}(X),
$$

and define

$$
g_t=\E_t[(f-m_t)(X-a_t)],
\qquad
H_t=\E_t[(f-m_t)(X-a_t)^{\otimes2}].
$$

Assume that, for every $0\le t\le T_0$,

```{math}
:label: eq:sol-spectral-occupation-hypothesis
\E\int_0^t\norm{H_s}_{\HS}^2\dd s
\le C_0t+C_1\int_0^t\E\abs{g_s}^2\dd s
+\E\int_0^t2g_s^TA_sg_s\dd s,
```

with all displayed occupation integrals finite. Define

```{math}
:label: eq:sol-spectral-constants
M_*=(1+C_0T_0)e^{C_1T_0},
\qquad
T_* = \min\left\{T_0,\frac1{2M_*}\right\}.
```

Then every isotropic log-concave probability measure $\nu$ on every $\R^n$ satisfies

```{math}
:label: eq:sol-spectral-gap-conclusion
\CP(\nu)\le \frac2{T_*}.
```

Thus an affirmative, regularization-uniform answer to [](#conj:mm-spectral-occupation) implies [](#conj:kls). The theorem is conditional on that still-open occupation estimate.
:::

:::{prf:proof}
*The fixed-function filter.* We first prove the assertion for a regular $\mu$. Realize its localization by taking $X\sim\mu$, an independent standard Brownian motion $B^{\mathrm{obs}}$, and the observation

$$
c_t=tX+B_t^{\mathrm{obs}},
\qquad
\mathcal F_t^{\mathrm{obs}}=\sigma(c_s:0\le s\le t).
$$

The conditional law $\mu_t=\mathcal L(X\mid\mathcal F_t^{\mathrm{obs}})$ has density

```{math}
:label: eq:sol-spectral-posterior
\dd\mu_t(x)=
\frac{\exp(c_t\cdot x-t\abs{x}^2/2)}
{\int\exp(c_t\cdot y-t\abs{y}^2/2)\dd\mu(y)}\,\dd\mu(x).
```

Let

$$
W_t=c_t-\int_0^ta_s\dd s.
$$

It is the innovation Brownian motion. Applying Itô's formula to [](#eq:sol-spectral-posterior) gives, for every fixed admissible scalar or vector test $\phi$,

```{math}
:label: eq:sol-spectral-filtering
\dd\E_t\phi=\Cov_{\mu_t}(\phi,X)\cdot\dd W_t.
```

In particular,

$$
\dd m_t=g_t\cdot\dd W_t,
\qquad
\dd a_t=A_t\dd W_t.
$$

For completeness, set $r_t=\E_t(fX)$. The vector form of [](#eq:sol-spectral-filtering) and Itô's product rule give

$$
\dd r_t=\Cov_{\mu_t}(fX,X)\dd W_t,
$$

and

$$
\dd(m_ta_t)=m_tA_t\dd W_t+a_t(g_t\cdot\dd W_t)+A_tg_t\dd t.
$$

Since $g_t=r_t-m_ta_t$, expansion of the stochastic coefficient shows that it is exactly

$$
\E_t[(f-m_t)(X-a_t)^{\otimes2}]=H_t.
$$

Consequently

```{math}
:label: eq:sol-spectral-fixed-function-sde
\dd g_t=H_t\dd W_t-A_tg_t\dd t.
```

These filtering identities are first applied to bounded truncations and before the stopping time at which the relevant posterior moments or quadratic variations reach a fixed level. The stopping level is then sent to infinity. In the present regular class this loses no equality: strong log-concavity gives all polynomial moments, while Bakry–Émery hypercontractivity and $P_sf=e^{-\lambda s}f$ put the eigenfunction in every finite $L^p(\mu)$. Thus the products of $f$ with the coordinate polynomials above are integrable to the required orders. The assumed finite occupation bound and the nonnegative damping complete the usual stopped Itô passage.

*Full damping cancels exactly.* Put

$$
q(t)=\E\abs{g_t}^2.
$$

Itô's formula applied to [](#eq:sol-spectral-fixed-function-sde), followed by the stopped expectation passage just described, yields

```{math}
:label: eq:sol-spectral-q-identity
q(t)=\abs{g_0}^2+
\E\int_0^t\left(\norm{H_s}_{\HS}^2-2g_s^TA_sg_s\right)\dd s.
```

The centered isotropic coordinates $X_1,\ldots,X_n$ are an orthonormal family in $L^2(\mu)$. Since $(g_0)_i=\E_\mu(fX_i)$, Bessel's inequality gives

```{math}
:label: eq:sol-spectral-initial-bessel
\abs{g_0}^2=\sum_{i=1}^n\abs{\langle f,X_i\rangle_{L^2(\mu)}}^2
\le\E_\mu f^2=1.
```

Combining [](#eq:sol-spectral-q-identity) with [](#eq:sol-spectral-occupation-hypothesis) cancels the entire damping budget and gives

```{math}
:label: eq:sol-spectral-gronwall-input
q(t)\le1+C_0t+C_1\int_0^tq(s)\dd s,
\qquad 0\le t\le T_0.
```

The integral form of Grönwall's lemma therefore implies

```{math}
:label: eq:sol-spectral-gronwall
q(t)\le(1+C_0t)e^{C_1t}\le M_*,
\qquad 0\le t\le T_0.
```

No negative remainder was discarded here: the coefficient one in [](#eq:sol-spectral-occupation-hypothesis) is precisely what cancels the full exact damping in [](#eq:sol-spectral-q-identity).

*Terminal posterior variance.* Because $m_t=\E[f(X)\mid\mathcal F_t^{\mathrm{obs}}]$ is a square-integrable martingale and $\dd m_t=g_t\cdot\dd W_t$, the Itô isometry and conditional variance decomposition give

```{math}
:label: eq:sol-spectral-total-variance
\E\Var_{\mu_t}(f)
=\E_\mu f^2-\E m_t^2
=1-\int_0^tq(s)\dd s.
```

By [](#eq:sol-spectral-constants) and [](#eq:sol-spectral-gronwall),

```{math}
:label: eq:sol-spectral-terminal-lower
\E\Var_{\mu_{T_*}}(f)\ge1-T_*M_*\ge\frac12.
```

On the other hand, the potential of $\mu_t$ is

$$
V_t(x)=V(x)-c_t\cdot x+\frac t2\abs{x}^2.
$$

It has Hessian at least $tI_n$. Posterior Brascamp–Lieb, followed by the tower property for the fixed test $\abs{\nabla f}^2$, gives for every $t>0$

```{math}
:label: eq:sol-spectral-terminal-upper
\begin{aligned}
\E\Var_{\mu_t}(f)
&\le\frac1t\E\E_t\abs{\nabla f}^2
=\frac1t\E_\mu\abs{\nabla f}^2
=\frac\lambda t.
\end{aligned}
```

The last equality is the Dirichlet-form identity $\E_\mu\abs{\nabla f}^2=\langle f,-Lf\rangle=\lambda$. At $t=T_*$, [](#eq:sol-spectral-terminal-lower) and [](#eq:sol-spectral-terminal-upper) imply

```{math}
:label: eq:sol-spectral-regular-gap
\lambda\ge\frac{T_*}{2}.
```

Thus every regular law covered by the hypothesis has $\CP(\mu)=\lambda^{-1}\le2/T_*$.

*A regular isotropic approximation.* Let now $\nu$ be an arbitrary isotropic log-concave probability measure on $\R^n$. Isotropy implies full-dimensionality. We construct regular isotropic $\nu_j\to\nu$ in $W_2$.

Let $\gamma_\varepsilon=N(0,\varepsilon I_n)$ and let $\rho_\varepsilon$ be the smooth positive log-concave density of $\nu*\gamma_\varepsilon$. For fixed $\varepsilon>0$ and $\delta>0$ set

```{math}
:label: eq:sol-spectral-tilted-approximation
\dd\widetilde\nu_{\varepsilon,\delta}(x)
=Z_{\varepsilon,\delta}^{-1}
e^{-\delta\abs{x}^2/2}\rho_\varepsilon(x)\dd x.
```

Its potential

$$
U_{\varepsilon,\delta}=-\log\rho_\varepsilon+\frac\delta2\abs{x}^2
$$

is smooth and satisfies $\nabla^2U_{\varepsilon,\delta}\succeq\delta I_n$. For fixed $\varepsilon$, dominated convergence of the normalizing constant and of the second moment shows that

$$
\widetilde\nu_{\varepsilon,\delta}\longrightarrow
\nu*\gamma_\varepsilon
\quad\text{in }W_2\quad\text{as }\delta\downarrow0.
$$

Also $W_2(\nu*\gamma_\varepsilon,\nu)\le\sqrt{n\varepsilon}$, using the coupling $X+\sqrt\varepsilon G$ with $X\sim\nu$ and $G\sim N(0,I_n)$ independent. We may therefore choose $\varepsilon_j\downarrow0$ and then $\delta_j\downarrow0$ diagonally so that

$$
\widetilde\nu_j:=\widetilde\nu_{\varepsilon_j,\delta_j}\longrightarrow\nu
\quad\text{in }W_2.
$$

We also record why these laws lie in the spectral regular class rather than merely being smooth and strongly log-concave. Gaussian differentiation gives

$$
0\preceq\nabla^2(-\log\rho_\varepsilon)(y)
=\varepsilon^{-1}I_n-\varepsilon^{-2}
\Cov(X\mid X+\sqrt\varepsilon G=y)
\preceq\varepsilon^{-1}I_n.
$$

Hence $\nabla^2U_{\varepsilon,\delta}$ is bounded above as well as bounded below by a positive matrix. Under the ground-state transform, $-L$ becomes a Schrödinger operator whose potential is

$$
\frac14\abs{\nabla U_{\varepsilon,\delta}}^2
-\frac12\Delta U_{\varepsilon,\delta}.
$$

Strong convexity makes the first term grow quadratically at infinity, while the displayed upper Hessian bound keeps the second term bounded. The Schrödinger potential therefore tends to $+\infty$, so the Friedrichs realization has compact resolvent and a first nonconstant eigenfunction.

Let $b_j$ and $\Sigma_j$ be the mean and covariance of $\widetilde\nu_j$. The $W_2$ convergence implies $b_j\to0$ and $\Sigma_j\to I_n$. Define

```{math}
:label: eq:sol-spectral-isotropization
\nu_j=\bigl(x\mapsto\Sigma_j^{-1/2}(x-b_j)\bigr)_\#\widetilde\nu_j.
```

Then $\nu_j$ is centered and isotropic, its potential remains smooth and strongly convex, its generator still has compact resolvent, and $\nu_j\to\nu$ in $W_2$. The occupation hypothesis and the regular-law argument above apply separately to the first eigenfunction of each $\nu_j$; they give

```{math}
:label: eq:sol-spectral-approximant-poincare
\Var_{\nu_j}(h)\le\frac2{T_*}\int\abs{\nabla h}^2\dd\nu_j
```

for every locally Lipschitz $h$.

*Passage of the inequality, not of eigenfunctions.* Fix $h\in C_c^\infty(\R^n)$. Both $h,h^2$ and $\abs{\nabla h}^2$ are bounded continuous functions. Weak convergence in [](#eq:sol-spectral-isotropization) therefore lets $j\to\infty$ in [](#eq:sol-spectral-approximant-poincare) and gives

$$
\Var_\nu(h)\le\frac2{T_*}\int\abs{\nabla h}^2\dd\nu.
$$

The same inequality holds for every locally Lipschitz $h$: first truncate its values, then multiply by Lipschitz cutoffs tending to one, and finally mollify. Value truncation decreases the gradient almost everywhere; for a bounded truncation the cutoff-gradient error is $O(R^{-2})$; and dominated convergence together with lower semicontinuity removes the three approximations. If the gradient energy is infinite the desired inequality is vacuous. If it is finite, the same value truncations and Fatou's lemma force the variance to be finite and pass the bound to $h$. This proves [](#eq:sol-spectral-gap-conclusion).

At no point was an eigenfunction of $\nu_j$ required to converge. Only the uniform Poincaré inequality obtained on each approximant was passed to fixed test functions of the limiting law.
:::

**Obstructions respected.** The ledger assigns this node no formal `bounded_by` edge. The proof nevertheless respects every listed KLS fence. It contains no cut, slice, excess, or localized isoperimetric-profile estimate, so `rem:two-tail-slice-bounds` and `rem:profile-circularity` are not engaged. It derives no tensor estimate from radial or projection-only tests, uses no crude or relative covariance occupation integral, and makes no product-cut assertion. Thus the projection, crude-occupation, relative-occupation, and rank-one-product fences remain untouched. In particular, the argument never bounds $\norm{A_t}_\op$ along a universal time interval and does not contradict the covariance-spike obstruction. Posterior Brascamp–Lieb is used only at the single terminal time and only after the function-aware occupation hypothesis has controlled how much of the fixed eigenfunction was learned.

**Status, dependencies, and exclusions.** The sole ledger dependency is the open spectral-occupation node. It appears here as the explicit hypothesis [](#eq:sol-spectral-occupation-hypothesis). The result is therefore a conditional implication, not an unconditional proof of KLS. The remaining inputs are the exact fixed-function filtering identities, classical Brascamp–Lieb, Grönwall's lemma, and the variational lower-semicontinuity passage above. No Letwin preprint input is used. The dossier does not prove the occupation estimate, an unweighted source bound, any member of the trace-upgrade cluster, or any assertion about the deterministic CMH route.
