---
title: 'Solution: full matrix Riccati dissipation'
label: sec:sol-full-matrix-dissipation
ledger-node: cor:full-matrix-dissipation
numbering:
  enumerator: D2.%s
---

**Overview.** This dossier proves a refined form of [](#cor:full-matrix-dissipation): under Eldan localization of an isotropic log-concave $\mu$ with a nontrivial cut $E$, the full matrix dissipation $\E\int_0^\infty(R_t^2+s_tG_t^2)\dd t$ is bounded by $R_0\preceq I_n$ in Loewner order, with no balance or stopping hypothesis. The proof feeds the certified matrix Riccati identity into a general positive-drift lemma for matrix semimartingales.

1. [](#lem:sol-positive-matrix-drift): a positive semidefinite process with local-martingale part and positive drift $Q$ satisfies [](#eq:sol-abstract-finite) and [](#eq:sol-abstract-infinite). The proof scalarizes along each direction, then uses localization, optional sampling, Fatou and monotone convergence. Positive semidefiniteness gives integrability of the off-diagonal entries.
2. The certified identity [](#lem:matrix-riccati) gives [](#eq:sol-certified-matrix-riccati) with $Q_t=R_t^2+s_tG_t^2\succeq0$. Step 1 then yields [](#eq:sol-full-matrix-finite) and [](#eq:sol-full-matrix-infinite), and isotropy gives $R_0\preceq I_n$.
3. Testing against a direction gives [](#eq:sol-full-matrix-directional), which recovers and strengthens [](#cor:per-direction). A Gaussian halfspace example shows that the extra $R_t^2$ term is not vacuous.
4. The trace [](#eq:sol-full-matrix-trace) is only bounded by $n$. The result gives no dimension-free operator-to-trace upgrade.

**Scope and notation.** Let $\mu$ be an isotropic log-concave probability measure on $\R^n$, let $E$ be a fixed measurable set with $0<\mu(E)<1$, and run Eldan stochastic localization. We use the standing two-color notation

$$
p_t=\mu_t(E),\qquad q_t=1-p_t,\qquad s_t=p_tq_t,
$$

$$
B_t=s_t\delta_t\delta_t^T,
\qquad
R_t=A_t-B_t=p_t\Sigma_t^E+q_t\Sigma_t^{E^c}\succeq0,
\qquad
G_t=\Sigma_t^E-\Sigma_t^{E^c}.
$$

The finite-time localization density is strictly positive relative to $\mu$, so the two conditional laws, and hence these matrices, are defined at every finite time. All matrix integrals below are understood entrywise; the proof shows their absolute integrability rather than assuming it.

:::{prf:theorem} refined form of [](#cor:full-matrix-dissipation)
:label: thm:sol-full-matrix-dissipation
For every finite $T\geq0$,

```{math}
:label: eq:sol-full-matrix-finite
\E R_T+
\E\int_0^T\bigl(R_t^2+s_tG_t^2\bigr)\dd t
\preceq R_0.
```

Consequently,

```{math}
:label: eq:sol-full-matrix-infinite
\E\int_0^\infty\bigl(R_t^2+s_tG_t^2\bigr)\dd t
\preceq R_0\preceq I_n.
```

No balance or stopping-window hypothesis is required.
:::

We first isolate the only stochastic expectation argument that is needed.

:::{prf:lemma} Positive matrix drift survives localization
:label: lem:sol-positive-matrix-drift
Let $(X_t)_{t\geq0}$ be a continuous adapted process with values in the positive semidefinite symmetric matrices, with deterministic initial matrix $X_0$. Suppose that, entrywise,

```{math}
:label: eq:sol-abstract-matrix-decomposition
X_t=X_0+N_t-\int_0^tQ_u\dd u,
```

where $N_0=0$ is a matrix local martingale and $Q_t\succeq0$ is progressively measurable and locally integrable. Then the matrices in the following display are integrable and, for every finite $T$,

```{math}
:label: eq:sol-abstract-finite
\E X_T+\E\int_0^TQ_t\dd t\preceq X_0.
```

Moreover the improper integral $\int_0^\infty Q_t\dd t$ exists entrywise and absolutely almost surely, is integrable, and

```{math}
:label: eq:sol-abstract-infinite
\E\int_0^\infty Q_t\dd t\preceq X_0.
```
:::

:::{prf:proof}
Fix a deterministic vector $\theta\in\R^n$ and set

$$
x_t^\theta=\theta^TX_t\theta,
\qquad
M_t^\theta=\theta^TN_t\theta,
\qquad
a_t^\theta=\int_0^t\theta^TQ_u\theta\dd u.
$$

Thus $x^\theta,a^\theta\geq0$, $a^\theta$ is increasing, and

```{math}
:label: eq:sol-scalarized-decomposition
x_t^\theta+a_t^\theta=x_0^\theta+M_t^\theta.
```

Choose increasing localizing times $\sigma_k\uparrow\infty$ almost surely such that $(M^\theta)^{\sigma_k}$ is a true martingale. At the bounded time $T\wedge\sigma_k$, [](#eq:sol-scalarized-decomposition) and optional sampling give

```{math}
:label: eq:sol-stopped-expectation
\E\bigl[x_{T\wedge\sigma_k}^\theta+a_{T\wedge\sigma_k}^\theta\bigr]
=x_0^\theta.
```

There is no integrability assumption hidden here: the right-hand side of [](#eq:sol-scalarized-decomposition) is integrable after stopping, while its left-hand side is nonnegative, so both terms on that side are integrable.

Continuity of $X$ and local integrability of $Q$ imply convergence of the stopped left-hand side to $x_T^\theta+a_T^\theta$. Fatou's lemma, applied to that nonnegative sum, now yields

```{math}
:label: eq:sol-directional-finite
\E x_T^\theta+\E a_T^\theta\leq x_0^\theta.
```

In particular this estimate does not require uniform integrability of the unstopped local martingale or of the terminal matrix process.

For completeness, the scalar quadratic-form estimates really do reconstruct ordinary integrable matrices. Apply [](#eq:sol-directional-finite) to the coordinate vectors $e_i$. It gives integrability of the diagonal entries of $X_T$ and $H_T:=\int_0^TQ_t\dd t$. Positivity gives, pathwise,

$$
\abs{(X_T)_{ij}}\leq\frac{(X_T)_{ii}+(X_T)_{jj}}2,
\qquad
\int_0^T\abs{(Q_t)_{ij}}\dd t
\leq\frac{(H_T)_{ii}+(H_T)_{jj}}2.
$$

Hence all entries are absolutely integrable. Polarization, or simply testing [](#eq:sol-directional-finite) for every deterministic $\theta$, gives

$$
\theta^T\left(\E X_T+\E H_T\right)\theta
\leq\theta^TX_0\theta
\qquad(\theta\in\R^n),
$$

which is exactly the Loewner inequality [](#eq:sol-abstract-finite).

Finally $a_T^\theta\uparrow a_\infty^\theta$ as $T\uparrow\infty$. Monotone convergence in [](#eq:sol-directional-finite) gives

$$
\E a_\infty^\theta\leq x_0^\theta.
$$

For $\theta=e_i$, this says that every diagonal integral is finite almost surely and in $L^1$. The positive-semidefinite entry bound just used, now on $[0,\infty)$, makes every off-diagonal integral absolutely convergent and integrable. Polarization reconstructs the matrix expectation, and the preceding inequality for all $\theta$ proves [](#eq:sol-abstract-infinite).
:::

:::{prf:proof} Proof of [](#thm:sol-full-matrix-dissipation)
The certified matrix Riccati identity, [](#lem:matrix-riccati), is

```{math}
:label: eq:sol-certified-matrix-riccati
\dd R_t=\dd\widetilde N_t-\bigl(R_t^2+s_tG_t^2\bigr)\dd t,
```

for a symmetric matrix local martingale $\widetilde N$. Covariance decomposition gives $R_t\succeq0$. Both $R_t$ and $G_t$ are symmetric and $s_t\geq0$, so

$$
Q_t:=R_t^2+s_tG_t^2\succeq0.
$$

[](#lem:sol-positive-matrix-drift), with $X=R$ and this $Q$, proves [](#eq:sol-full-matrix-finite) and the first inequality in [](#eq:sol-full-matrix-infinite). At time zero, $R_0=A_0-B_0\preceq A_0=I_n$ by isotropy, proving the second one.
:::

**Relation to the per-direction estimate and the trace gate.** Testing [](#eq:sol-full-matrix-infinite) against any deterministic $\theta$ gives

```{math}
:label: eq:sol-full-matrix-directional
\E\int_0^\infty
\left(\abs{R_t\theta}^2+s_t\abs{G_t\theta}^2\right)\dd t
\leq\theta^TR_0\theta.
```

Restricting the integral to $[0,T]$ recovers the first display of [](#cor:per-direction); discarding the nonnegative $R_t^2$ term recovers its source-only Loewner display. Thus the new conclusion is the infinite-horizon matrix form of the full directional dissipation and retains strictly more information than the source-only bound.

The extra information is non-vacuous. For the standard Gaussian measure and the halfspace $E=\{x_1\leq0\}$, every localization posterior remains a product across the coordinate axes and has covariance $(1+t)^{-1}I_n$. For each spectator direction $e_j$, $j\geq2$, conditioning on $E$ does not change that coordinate, and hence

$$
G_te_j=0,
\qquad
R_te_j=(1+t)^{-1}e_j,
\qquad
\int_0^\infty\abs{R_te_j}^2\dd t=1.
$$

The source-only estimate sees zero in those directions, whereas the full dissipation estimate uses their entire unit budgets.

Taking a trace in [](#eq:sol-full-matrix-infinite) gives only

```{math}
:label: eq:sol-full-matrix-trace
\E\int_0^\infty
\left(\norm{R_t}_{\HS}^2+s_t\norm{G_t}_{\HS}^2\right)\dd t
\leq\Tr R_0\leq n.
```

Indeed, the Gaussian halfspace example already contributes $n-1$ from its spectator $R_t^2$ directions. The result therefore supplies a genuine matrix coercivity budget but no dimension-free operator-to-trace upgrade.

**Hypotheses and fences.** The only mathematical input beyond the standing two-color setup is the already certified matrix Riccati identity. Isotropy is used solely for $R_0\preceq I_n$; the estimate with right side $R_0$ holds for any initial law for which that identity and the two-color covariances are defined. Nontriviality of the cut is exactly what makes the conditional covariances meaningful. No balance, smooth-boundary, compact-support, stopping-time, fourth-moment, or endpoint uniform- integrability hypothesis is used. The ledger node has no `bounded_by` edge. The dimension-dependent trace consequence [](#eq:sol-full-matrix-trace) explicitly respects the operator-to-trace obstruction emphasized immediately after the manuscript corollary.
