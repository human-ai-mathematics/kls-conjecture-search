---
title: 'Solution: scale-weighted all-cut source budget'
label: sec:sol-time-weighted-source
ledger-node: lem:time-weighted-source
numbering:
  enumerator: D19.%s
---

**Overview.** This dossier proves [](#lem:time-weighted-source) as [](#thm:sol-time-weighted-source): for any nontrivial cut along Eldan localization of an isotropic log-concave law, $\E\int_0^Tt^2(S_t+r_t^2)\dd t\le T^2\E r_T\le T$ ([](#eq:sol-time-weighted-source)). The same bound holds for any stopped integral ([](#eq:sol-time-weighted-stopped)). The proof multiplies the scalar Riccati identity [](#thm:scalar-riccati) by $t^2$ and uses the posterior Brascamp–Lieb cap to absorb the damping. It is unconditional, keeps the quadratic time weight, and makes no unweighted claim at $t=0$.

1. The covariance decomposition [](#eq:sol-time-weighted-decomposition) and the Brascamp–Lieb cap give $0\le r_t\le1/t$ ([](#eq:sol-time-weighted-r-cap)) and the damping bound [](#eq:sol-time-weighted-D-cap).
2. [](#thm:scalar-riccati), multiplied by $t^2$ and combined with step 1, gives the drift inequality [](#eq:sol-time-weighted-product).
3. Localizing on $[\varepsilon,T]$ and using the terminal bound $\theta_k^2r_{\theta_k}\le T$ from step 1 gives [](#eq:sol-time-weighted-epsilon).
4. Letting $\varepsilon\downarrow0$ proves [](#eq:sol-time-weighted-source); positivity of the integrand gives [](#eq:sol-time-weighted-stopped).
5. A regularization passage, using Fatou and the uniform terminal bound, extends the result to arbitrary isotropic log-concave laws and measurable cuts.

**Scope and notation.** Let $\mu$ be isotropic and log-concave on $\R^n$, and let $E$ be a fixed measurable set with $0<\mu(E)<1$. Along Eldan localization write

$$
p_t=\mu_t(E),\quad q_t=1-p_t,\quad s_t=p_tq_t,
\quad \delta_t=m_t^E-m_t^{E^c},
$$

$$
G_t=\Sigma_t^E-\Sigma_t^{E^c},\qquad
B_t=s_t\delta_t\delta_t^T,\qquad
r_t=\Tr B_t=s_t\abs{\delta_t}^2,
$$

$$
S_t=s_t\norm{G_t}_{\HS}^2,qquad
D_t=2s_t\delta_t^TA_t\delta_t-r_t^2,
\quad A_t=\Cov(\mu_t).
$$

The finite-time localization likelihood is strictly positive relative to $\mu$, so $p_t,q_t>0$ at every finite time. No balance assumption is imposed on the cut.

:::{prf:theorem} refined form of [](#lem:time-weighted-source)
:label: thm:sol-time-weighted-source
For every $T>0$,

```{math}
:label: eq:sol-time-weighted-source
\E\int_0^T t^2\bigl(S_t+r_t^2\bigr)\dd t
\le T^2\E r_T\le T.
```

Consequently, if $\tau$ is any stopping time (in particular, the exit time from any balanced window), then, solely by positivity,

```{math}
:label: eq:sol-time-weighted-stopped
\E\int_0^{T\wedge\tau}t^2\bigl(S_t+r_t^2\bigr)\dd t
\le \E\int_0^Tt^2\bigl(S_t+r_t^2\bigr)\dd t
\le T^2\E r_T\le T.
```

The same conclusion holds if the integrand is further restricted to a deterministic time interval. In particular, this is not an unweighted source estimate at $t=0$.
:::

:::{prf:proof}
The conditional covariance decomposition is

```{math}
:label: eq:sol-time-weighted-decomposition
A_t=p_t\Sigma_t^E+q_t\Sigma_t^{E^c}+B_t.
```

Thus $0\preceq B_t\preceq A_t$. The matrix $B_t$ has rank at most one, and its only possible nonzero eigenvalue is its trace $r_t$. For $t>0$, the posterior is $t$-uniformly log-concave, so the Brascamp–Lieb covariance cap gives

```{math}
:label: eq:sol-time-weighted-r-cap
0\le r_t=\lambda_{\max}(B_t)\le\lambda_{\max}(A_t)\le\frac1t.
```

Moreover, using $A_t\preceq t^{-1}I$ and $B_t\succeq0$,

$$
s_t\delta_t^TA_t\delta_t=\Tr(A_tB_t)
\le\frac1t\Tr B_t=\frac{r_t}{t}.
$$

It follows that the damping has the pathwise upper bound

```{math}
:label: eq:sol-time-weighted-D-cap
D_t\le\frac{2r_t}{t}-r_t^2,
\qquad t>0.
```

By the scalar Riccati identity, [](#thm:scalar-riccati), there is a continuous local martingale $M$ such that

$$
\dd r_t=\dd M_t+(S_t-D_t)\dd t.
$$

Multiplication by the deterministic function $t^2$ and [](#eq:sol-time-weighted-D-cap) give, for $t>0$,

```{math}
:label: eq:sol-time-weighted-product
\begin{aligned}
\dd(t^2r_t)
&=t^2\dd M_t+
\bigl(2tr_t+t^2S_t-t^2D_t\bigr)\dd t \\
&\ge t^2\dd M_t+t^2\bigl(S_t+r_t^2\bigr)\dd t.
\end{aligned}
```

We now justify expectation and the endpoint rather than taking an expectation of the local martingale formally. Fix $0<\varepsilon<T$, and localize the weighted local martingale $L_t=\int_\varepsilon^t u^2\dd M_u$. Choose increasing stopping times $\rho_k\ge\varepsilon$, with $\rho_k\uparrow\infty$ almost surely, such that the stopped increments of $L$ are true martingales on $[\varepsilon,T]$, and put $\theta_k=T\wedge\rho_k$. Integrating [](#eq:sol-time-weighted-product) to $\theta_k$ and taking expectations yields

```{math}
:label: eq:sol-time-weighted-localized
\E\int_\varepsilon^{\theta_k}
t^2\bigl(S_t+r_t^2\bigr)\dd t
\le \E\bigl[\theta_k^2r_{\theta_k}\bigr]
-\varepsilon^2\E r_\varepsilon.
```

The cap [](#eq:sol-time-weighted-r-cap), applied at $\theta_k\ge\varepsilon$, gives

$$
0\le\theta_k^2r_{\theta_k}\le\theta_k\le T.
$$

Since $\theta_k\uparrow T$, dominated convergence applies to this terminal term, while monotone convergence applies to the nonnegative occupation integral. Hence

```{math}
:label: eq:sol-time-weighted-epsilon
\E\int_\varepsilon^Tt^2\bigl(S_t+r_t^2\bigr)\dd t
\le T^2\E r_T-\varepsilon^2\E r_\varepsilon.
```

There is no hidden use of the Brascamp–Lieb cap at $t=0$: isotropy and [](#eq:sol-time-weighted-decomposition) give $B_0\preceq A_0=I$ and $r_0\le1$, while for $\varepsilon>0$ the cap gives $0\le\varepsilon^2\E r_\varepsilon\le\varepsilon$. Letting $\varepsilon\downarrow0$ in [](#eq:sol-time-weighted-epsilon), again by monotone convergence on the left, proves the first inequality in [](#eq:sol-time-weighted-source). Finally $0\le T^2r_T\le T$ pathwise by [](#eq:sol-time-weighted-r-cap), proving the second one. Equation [](#eq:sol-time-weighted-stopped) then follows only from $S_t+r_t^2\ge0$.

For completeness, the preceding calculation is stable under the repository's regularization convention. At the regular level one truncates and smooths the log-concave density and the cut, then puts the measure back in isotropic position; bounded stopping makes every stochastic integral above a true martingale. The scalar Riccati identity is already certified for the general law by precisely this passage. On each strip $[\varepsilon,T]$, its approximation gives convergence of the posterior masses and first and second cut moments (after passage to a subsequence if necessary), hence of $r_t$ and $S_t$ for almost every $(\omega,t)$. Fatou's lemma applies to the nonnegative occupation term. At the terminal time the uniform pathwise bound $0\le T^2r_T\le T$ gives uniform integrability, so the terminal expectations pass to the limit. The constants are independent of the regularization. Sending $\varepsilon\downarrow0$ as above completes the passage for an arbitrary isotropic log-concave law and arbitrary measurable nontrivial cut. Thus no smoothness or compact-support hypothesis remains in the theorem.
:::

**Obstructions respected.** The ledger gives `lem:time-weighted-source` no `bounded_by` edge. The relevant Eldan-route fences are nevertheless respected. No radial or projection-only family is used to infer a tensor trace bound, so `obs:proj-ceiling` is not crossed. The estimate permits source of order $t^{-2}$ and retains the factor $t^2$, so it makes no forbidden slice-wise absolute-scale assertion in the two-tail regime of `obs:two-tail`. It assumes no relative-scale covariance occupation estimate of the kind fenced by `obs:relative-ceiling`. It also uses neither the crude $\Xi_T$ estimate, a localized isoperimetric profile, nor a product-cut counterexample, so `obs:crude-insufficient`, `obs:circularity`, and `obs:rank-one-refuted` are untouched.

**Status and exclusions.** The only ledger dependency is the already certified [](#thm:scalar-riccati); its own dependency `lem:matrix-riccati` is certified as well. The other analytic input is the standard posterior Brascamp–Lieb covariance cap. There is no unresolved hypothesis, so the stated lemma is unconditional. This dossier does not remove the quadratic time weight, does not prove `q:upgrade` or an all-cut Carleson estimate, makes no claim about `q:stein-weighted` or `q:alignment`, and proves no KLS conclusion.
