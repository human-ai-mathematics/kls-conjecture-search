---
title: 'Solution: stopped initial-layer source bound (conditional on the Letwin import)'
label: sec:sol-lem-mm-stopped-window-source
ledger-node: lem:mm-stopped-window-source
numbering:
  enumerator: D17.%s
---

**Overview.** This dossier proves [](#lem:mm-stopped-window-source) as [](#thm:sol-lem-mm-stopped-window-source), *conditionally* on the unreviewed preprint input [](#thm:letwin-qcts), which is carried as [](#ass:sol-sws-letwin). For a regular approximant and a unit-variance fixed test, the source is integrated only up to the covariance exit time $\tau_L$, and the bound is $\E\int_0^{T\wedge\tau_L}\norm{H_t}_{\HS}^2\dd t\le8L^2T$ ([](#eq:sol-sws-main)). The proof has three parts: a pathwise whitened duality bound from the Letwin inequality, unwhitening only where $\norm{A_t}_\op<L$, and integration against the posterior variance budget. No moment of $\norm{A_t}_\op$ is used.

1. Posterior facts: the tilt [](#eq:sol-sws-posterior) is the conditional law ([](#eq:sol-sws-bayes)). It is strongly log-concave, with positive-definite covariance and all moments.
2. $H_t$ is defined by an absolutely convergent integral off a $\dd t\otimes\dd\Prob$-null set.
3. Whitening the posterior produces an isotropic log-concave vector. Duality over symmetric $M$ together with [](#ass:sol-sws-letwin) gives the pathwise bound [](#eq:sol-sws-whitened).
4. Before $\tau_L$, the ideal property of the Hilbert–Schmidt norm unwhitens step 3, giving [](#eq:sol-sws-pathwise).
5. The variance budget $\E v_t\le1$ ([](#eq:sol-sws-variance-budget)) and Tonelli integrate step 4 to [](#eq:sol-sws-main).

**Refined statement and standing.** This dossier proves the stopped, unweighted source bound for the fixed-test localization tensor on the initial layer, *conditional* on the imported and unreviewed preprint input [](#thm:letwin-qcts) [@Letwin2026QuadraticKLS, Thm. 1.2]. The conditional standing is carried as the explicit [](#ass:sol-sws-letwin) below; by repository constraint the corresponding ledger node can be at most `conditional` even after independent review. The statement is uniform in the dimension and in the regularization: the constant $8L^2$ contains no $n$, no $\varepsilon$, and no property of the test beyond its variance. No unstopped moment of $\norm{A_t}_\op$ is used, and no independence between the posterior variance and the covariance operator norm is asserted anywhere.

**Setting.** Throughout, $\mu$ is a *regular approximant*: a probability measure

$$
\dd\mu(x)=Z^{-1}e^{-V(x)}\dd x
\qquad\text{on }\R^n,
\qquad V\in C^\infty(\R^n),\qquad \nabla^2V\succeq\varepsilon I_n,\ \varepsilon>0,
$$

as in the regular class of Section [](#subsec:spectral-sde). (Centering and isotropy are part of that class but are not used in this lemma; the proof only uses smoothness and strong log-concavity. We record this so the lemma can be consumed verbatim after the restart of the companion dossier, where the posterior prior is no longer isotropic.) Take $X\sim\mu$, an independent standard Brownian motion $B^{\mathrm{obs}}$, and the planted observation channel

$$
c_t=tX+B_t^{\mathrm{obs}},
\qquad
\mathcal F_t=\sigma(c_s:0\le s\le t).
$$

Define the pathwise posterior kernel by the explicit tilt formula

```{math}
:label: eq:sol-sws-posterior
\dd\mu_t(x)
=\frac{\exp\bigl(c_t\cdot x-t\abs{x}^2/2\bigr)}
{\int\exp\bigl(c_t\cdot y-t\abs{y}^2/2\bigr)\dd\mu(y)}\,\dd\mu(x),
\qquad t\ge0,
```

and write $\E_t$ for integration against $\mu_t$,

$$
m_t=\E_tf,\qquad a_t=\E_tX,\qquad v_t=\Var_{\mu_t}(f),\qquad
A_t=\Cov_{\mu_t}(X),
$$

$$
g_t=\E_t[(f-m_t)(X-a_t)],
\qquad
H_t=\E_t\bigl[(f-m_t)(X-a_t)^{\otimes2}\bigr],
$$

for a fixed test $f\in L^2(\mu)$. When the defining integral of $H_t$ fails to converge absolutely we set $H_t=0$; Step 1 of the proof shows this happens only on a $\dd\Prob\otimes\dd t$-null set, so the convention does not affect any integral below. For $L\ge1$ put

$$
\tau_L=\inf\bigl\{t\ge0:\norm{A_t}_\op\ge L\bigr\},
\qquad \inf\emptyset=\infty .
$$

Only the elementary implication $t<\tau_L\Rightarrow\norm{A_t}_\op<L$, immediate from the definition of the infimum, is used; no stopping-time property of $\tau_L$ is needed in this dossier.

:::{prf:assumption} Imported quadratic Poincaré inequality; conditional input
:label: ass:sol-sws-letwin
For every isotropic log-concave random vector $Y$ on $\R^n$ and every symmetric matrix $M$,

$$
\Var\bigl(Y^TMY\bigr)\le8\norm M_{\HS}^2 .
$$

This is [](#thm:letwin-qcts), imported from [@Letwin2026QuadraticKLS, Thm. 1.2], currently an unreviewed version-1 arXiv preprint. Everything below is an elementary deduction from this display and carries the same caveat.
:::

:::{prf:theorem} Stopped initial-layer source bound; conditional on [](#ass:sol-sws-letwin)
:label: thm:sol-lem-mm-stopped-window-source
Assume [](#ass:sol-sws-letwin). Let $\mu$ be any regular approximant on any $\R^n$, let $f\in L^2(\mu)$ be any fixed test with $\Var_\mu(f)=1$, and let $L\ge1$, $T>0$. Then

```{math}
:label: eq:sol-sws-main
\E\int_0^{T\wedge\tau_L}\norm{H_t}_{\HS}^2\dd t\ \le\ 8L^2\,T .
```

The constant $8L^2$ is independent of $n$, of $\varepsilon$, of $T$, and of the test. Moreover the intermediate pathwise estimate

```{math}
:label: eq:sol-sws-whitened
\bigl\|A_t^{-1/2}H_tA_t^{-1/2}\bigr\|_{\HS}^2\ \le\ 8\,v_t
```

holds for almost every $(t,\omega)$, without any stopping.
:::

:::{prf:proof}
*Step 0: posterior facts.* Conditional on $X=x$, the path $(c_s)_{s\le t}$ is a Brownian motion with constant drift $x$; by the Cameron–Martin theorem its law on path space has, with respect to the Wiener measure, the density $\exp\bigl(x\cdot c_t-t\abs x^2/2\bigr)$. Bayes' rule for conditional laws therefore identifies [](#eq:sol-sws-posterior), for each fixed $t\ge0$, as a version of the conditional law $\mathcal L(X\mid\mathcal F_t)$:

```{math}
:label: eq:sol-sws-bayes
\E_t\phi=\E[\phi(X)\mid\mathcal F_t]\quad\text{a.s.}
```

for every $\phi\in L^1(\mu)$ (first for bounded $\phi$, then by monotone convergence for nonnegative integrable $\phi$, then by linearity). This is the same convention as in the certified dossiers for [](#lem:mm-time-weighted-fixed-source) and [](#lem:mm-posterior-defect).

The posterior potential $V(x)-c_t\cdot x+\tfrac t2\abs x^2$ has Hessian $\succeq(\varepsilon+t)I_n\succ0$, so $\mu_t$ is a smooth strongly log-concave probability measure with everywhere positive density; in particular it has all polynomial moments and its covariance $A_t$ is positive definite (a nontrivial linear functional cannot be $\mu_t$-a.s. constant when the density is positive on all of $\R^n$).

All posterior moments in this proof are jointly measurable in $(t,\omega)$: by [](#eq:sol-sws-posterior) they are explicit ratios of integrals of jointly measurable integrands against the fixed measure $\mu$, evaluated at the jointly measurable pair $(t,c_t(\omega))$.

*Step 1: the tensor is defined off a null set.* Fix $t\ge0$. By [](#eq:sol-sws-bayes) applied to $f^2$ and the tower property, $\E[\E_tf^2]=\E_\mu f^2<\infty$, so $\E_tf^2<\infty$ almost surely. By Tonelli's theorem the set of pairs $(t,\omega)$ with $\E_tf^2=\infty$ is $\dd t\otimes\dd\Prob$-null. Off this null set, conditional Cauchy–Schwarz gives

$$
\E_t\bigl[\abs{f-m_t}\,\abs{X-a_t}^2\bigr]
\le v_t^{1/2}\,\bigl(\E_t\abs{X-a_t}^4\bigr)^{1/2}<\infty,
$$

because $\mu_t$ has all moments. Hence $H_t$ is defined by an absolutely convergent integral and is a symmetric matrix, for almost every $(t,\omega)$.

*Step 2: pathwise whitened duality.* Work at a fixed pair $(t,\omega)$ off the null set of Step 1. Since $A_t\succ0$, the whitened variable

$$
Y=A_t^{-1/2}(X-a_t),
\qquad X\sim\mu_t,
$$

is well defined; its law is an affine image of the log-concave law $\mu_t$, hence log-concave, and it is centered with covariance $A_t^{-1/2}A_tA_t^{-1/2}=I_n$: it is isotropic log-concave. Write $\widehat H_t=A_t^{-1/2}H_tA_t^{-1/2}$. For any symmetric matrix $M$,

$$
\begin{aligned}
\inner{M}{\widehat H_t}_{\HS}
&=\E_t\bigl[(f-m_t)\,(X-a_t)^TA_t^{-1/2}MA_t^{-1/2}(X-a_t)\bigr]\\
&=\E_t\bigl[(f-m_t)\,Y^TMY\bigr]
=\Cov_{\mu_t}\bigl(f,\,Y^TMY\bigr),
\end{aligned}
$$

the last equality because the first factor is centered. The quadratic polynomial $Y^TMY$ lies in $L^2(\mu_t)$, so conditional Cauchy–Schwarz and [](#ass:sol-sws-letwin) applied to the isotropic log-concave law of $Y$ give

$$
\inner{M}{\widehat H_t}_{\HS}
\le v_t^{1/2}\,\Var_{\mu_t}\bigl(Y^TMY\bigr)^{1/2}
\le v_t^{1/2}\,\sqrt8\,\norm M_{\HS}.
$$

Since $\widehat H_t$ is symmetric, taking the supremum over symmetric $M$ with $\norm M_{\HS}\le1$ recovers its full Hilbert–Schmidt norm and yields [](#eq:sol-sws-whitened):

$$
\norm{\widehat H_t}_{\HS}^2\le8v_t .
$$

This is a pathwise, per-time inequality; no expectation, no stopping, and no independence statement has been used.

*Step 3: unwhitening strictly before the exit time.* On the event $\{t<\tau_L\}$ the definition of the infimum gives $\norm{A_t}_\op<L$. Writing $H_t=A_t^{1/2}\widehat H_tA_t^{1/2}$ and using the ideal property of the Hilbert–Schmidt norm,

$$
\norm{H_t}_{\HS}
\le\norm{A_t^{1/2}}_\op^2\,\norm{\widehat H_t}_{\HS}
=\norm{A_t}_\op\,\norm{\widehat H_t}_{\HS},
$$

so that, combining with Step 2, for almost every $(t,\omega)$,

```{math}
:label: eq:sol-sws-pathwise
\norm{H_t}_{\HS}^2\,\one_{\{t<\tau_L\}}\ \le\ 8L^2\,v_t .
```

The operator norm was used only where it is deterministically below $L$; no moment of $\norm{A_t}_\op$ appears.

*Step 4: the variance budget and integration.* Fix $t\ge0$. By [](#eq:sol-sws-bayes), $m_t=\E[f(X)\mid\mathcal F_t]$ a.s., so $\E m_t=\E_\mu f$ and, by Jensen's inequality, $\E m_t^2\ge(\E_\mu f)^2$. Hence

```{math}
:label: eq:sol-sws-variance-budget
\E v_t=\E\bigl[\E_tf^2-m_t^2\bigr]
=\E_\mu f^2-\E m_t^2
\le\E_\mu f^2-(\E_\mu f)^2
=\Var_\mu(f)=1 .
```

Finally, since $\one_{\{t<T\wedge\tau_L\}}\le\one_{\{t<\tau_L\}}\one_{\{t<T\}}$, Tonelli's theorem for the nonnegative integrand, [](#eq:sol-sws-pathwise), and [](#eq:sol-sws-variance-budget) give

$$
\E\int_0^{T\wedge\tau_L}\norm{H_t}_{\HS}^2\dd t
\le\int_0^T\E\bigl[\norm{H_t}_{\HS}^2\one_{\{t<\tau_L\}}\bigr]\dd t
\le8L^2\int_0^T\E v_t\dd t
\le8L^2\,T .
$$

This proves [](#eq:sol-sws-main).
:::

:::{prf:remark} What is, and is not, claimed
:label: rem:sol-sws-scope
The bound [](#eq:sol-sws-main) is confined to times strictly before the covariance exit time $\tau_L$; it makes *no* assertion about $\E\int_0^T\norm{H_t}_{\HS}^2\dd t$ without the stop, no universal-time occupation claim, and no claim about [](#conj:mm-spectral-occupation) itself. The fenced product $\E\bigl[v_t\norm{A_t}_\op^2\bigr]$ is never formed: the operator norm enters only through the deterministic pathwise bound of Step 3, so the recorded marginal-probability independence fallacy is not engaged. By [](#prop:covariance-spike), the event $\{\tau_2\le t\}$ ceases to be rare past times of order $1/\log n$, so this mechanism cannot be extended to universal time; that limitation is inherited, not violated, here.
:::

:::{prf:remark} Hypotheses actually used
:label: rem:sol-sws-hypotheses
The proof uses: the planted Gaussian channel and the Bayes identification [](#eq:sol-sws-bayes); smoothness and $\varepsilon$-strong log-concavity of $\mu$ (only to guarantee positive-definite posterior covariances and all posterior moments — $\varepsilon$ enters no constant); square-integrability and unit variance of the fixed test; and [](#ass:sol-sws-letwin) (the unreviewed Letwin import), which is the sole unresolved premise. Centering and isotropy of $\mu$, the eigenfunction equation, and every other property of the regular class are unused. The result is a *conditional* implication: it certifies [](#thm:letwin-qcts) $\Rightarrow$ [](#eq:sol-sws-main) and nothing unconditional.
:::

**Obstructions respected.** The candidate node carries no `bounded_by` edge; the registered route fences were checked individually. No cut, slice, or excess estimate occurs (`rem:two-tail-slice-bounds`, `rem:profile-circularity`, `rem:single-coordinate-cuts`). The only tensor input is the full symmetric-matrix quadratic-chaos bound of [](#ass:sol-sws-letwin), used with its preprint-conditional standing displayed; no radial or projection test is promoted to a dimension-free chaos bound (`rem:projection-ceiling`). No crude covariance integral, no relative occupation bound, and no covariance bootstrap appears (`rem:crude-insufficient`, `rem:relative-ceiling`). The covariance-spike obstruction ([](#prop:covariance-spike)) is respected constructively: the estimate stops at the exit time precisely because operator-norm control past the window is false.
