---
numbering:
  enumerator: "24.%s"
---

(sec:riccati)=
# The two-color Riccati identities

The evolution of $r_t=s_t\abs{\delta_t}^2$ is governed by an exact Riccati identity. The matrix version is the most informative, so it is stated first.

Define the within-class covariance

```{math}
:label: eq:R-def
R_t=A_t-B_t=p_t\Sigma_t^E+q_t\Sigma_t^F\succeq0.
```

Also put

```{math}
:label: eq:K-def
K_t=G_t+(q_t-p_t)\delta_t\delta_t^T.
```

:::{prf:lemma} Matrix two-color Riccati identity
:label: lem:matrix-riccati
Under stochastic localization,

```{math}
:label: eq:dB
\dd B_t=\dd N_t+\bigl(s_tG_t^2-A_tB_t-B_tA_t+r_tB_t\bigr)\dd t,
```

where $N_t$ is a matrix-valued local martingale. Consequently,

```{math}
:label: eq:dR
\dd R_t=\dd\widetilde N_t-\bigl(R_t^2+s_tG_t^2\bigr)\dd t .
```
:::

:::{prf:proof}
Let $v=v_t$ and $s=s_t$. From [](#eq:loc-martingale), [](#eq:mean-sde), and Ito's product rule,

```{math}
:label: eq:dv
\dd v_t=(C_t^E-p_tA_t)\dd W_t-A_tv_t\dd t,
```

where

$$
C_t^E=\int_E(x-a_t)(x-a_t)^T\dd\mu_t(x).
$$

A direct covariance decomposition gives

```{math}
:label: eq:CE-minus-pA
C_t^E-p_tA_t=s_tK_t.
```

Hence $\dd v=sK\dd W-Av\dd t$. Also

$$
\dd s=(q-p)v\cdot\dd W-\abs v^2\dd t.
$$

Since $B=vv^T/s$, Ito's rule gives a drift

$$
sK^2-(AB+BA)+rB+(q-p)^2\frac rsB-(q-p)(KB+BK).
$$

Substituting $K=G+(q-p)B/s$ and using $B^2=rB$, the linear terms in $q-p$ cancel and the quadratic terms in $q-p$ sum to zero, leaving [](#eq:dB).

Subtract [](#eq:dB) from the covariance SDE [](#eq:cov-sde). Since $B^2=rB$,

$$
-A^2+AB+BA-rB=-(A-B)^2=-R^2.
$$

This yields [](#eq:dR).
:::

:::{prf:theorem} Scalar two-color Riccati identity
:label: thm:scalar-riccati
The binary information rate satisfies

```{math}
:label: eq:scalar-riccati
\dd r_t=\dd M_t+(S_t-D_t)\dd t,
```

where $M_t$ is a local martingale,

$$
S_t=s_t\norm{G_t}_{\HS}^2,
\qquad
D_t=2s_t\delta_t^TA_t\delta_t-r_t^2.
$$

Equivalently,

```{math}
:label: eq:scalar-riccati-expanded
\dd r_t=\dd M_t+\bigl[s_t\norm{G_t}_{\HS}^2-2s_t\delta_t^TA_t\delta_t+r_t^2\bigr]\dd t .
```
:::

:::{prf:proof}
Take traces in [](#eq:dB). Since $\Tr B_t=r_t$,

$$
\Tr(A_tB_t)=s_t\delta_t^TA_t\delta_t,
\qquad
\Tr(r_tB_t)=r_t^2,
$$

and the result follows.
:::

The damping is coercive. From $B_t\preceq A_t$,

$$
\delta_t^TA_t\delta_t\ge s_t\abs{\delta_t}^4,
$$

so

```{math}
:label: eq:D-ge-r2
D_t=2s_t\delta_t^TA_t\delta_t-r_t^2\ge r_t^2 .
```

Thus the only positive term in the scalar Riccati identity is the source

$$
S_t=s_t\norm{\Sigma_t^E-\Sigma_t^F}_{\HS}^2.
$$

:::{prf:corollary} Unconditional per-direction Carleson estimate
:label: cor:per-direction
For every $T>0$ and every unit vector $\theta\in\R^n$,

```{math}
:label: eq:per-direction
\E\int_0^T\left(s_t\abs{G_t\theta}^2+\abs{R_t\theta}^2\right)\dd t
\le \theta^TR_0\theta\le1.
```

Equivalently,

```{math}
:label: eq:loewner-carleson
\E\int_0^\infty s_tG_t^2\dd t\preceq R_0\preceq I_n.
```
:::

:::{prf:proof}
Apply [](#eq:dR) to the scalar process $\theta^TR_t\theta$. Its drift is $-\abs{R_t\theta}^2-s_t\abs{G_t\theta}^2$. Take expectations and use $R_T\succeq0$.
:::

:::{prf:corollary} Full matrix dissipation
:label: cor:full-matrix-dissipation
The matrix Riccati identity yields the Loewner-order estimate

```{math}
:label: eq:full-matrix-dissipation
\E\int_0^\infty\bigl(R_t^2+s_tG_t^2\bigr)\dd t\preceq R_0.
```

In particular, [](#eq:loewner-carleson) is obtained by discarding the nonnegative $R_t^2$ term. Taking a trace can still cost the dimension, so this strengthening does not by itself perform the operator-to-trace upgrade.
:::

:::{prf:remark} The missing step is an operator-to-trace upgrade
Estimate [](#eq:loewner-carleson) is dimension-free at the level of quadratic forms. It only implies

$$
\E\int_0^\infty S_t\dd t\le\Tr R_0\le n.
$$

The KLS-strength estimate must upgrade operator occupation to trace occupation on the stopped balanced window. In words, the source $s_tG_t^2$ cannot be allowed to occupy many almost orthogonal directions for a non-negligible set of early balanced times. This is the precise noncommutative Carleson content of the problem.
:::
