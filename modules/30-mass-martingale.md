---
numbering:
  enumerator: "30.%s"
---

(sec:mass-martingale)=
# The mass martingale, Itô calculations, and the stopped centroid reduction

*Appendix to the fixed cut, Section [](#sec:introduction).*

## Quadratic variation and information rate

By [](#eq:loc-martingale),

$$
\dd p_t=v_t\cdot\dd W_t,
\qquad
v_t=\int_E(x-a_t)\dd\mu_t(x).
$$

Since $a_t=p_tm_t^E+q_tm_t^F$, one has

```{math}
:label: eq:v-s-delta
v_t=s_t\delta_t .
```

Consequently,

```{math}
:label: eq:qv-p
\dd[p]_t=\abs{v_t}^2\dd t=s_t^2\abs{\delta_t}^2\dd t=s_tr_t\dd t.
```

This is the first cut-specific identity: the martingale volatility of the mass is precisely the centroid gap of the two posterior colors.

Let

$$
\mathsf h(p)=-p\log p-(1-p)\log(1-p)
$$

be binary entropy. Since $\mathsf h''(p)=-1/(p(1-p))$, Ito's formula and [](#eq:qv-p) give

```{math}
:label: eq:entropy-rate
\frac{\dd}{\dd t}\E\,\mathsf h(p_t)=-\frac12\E r_t .
```

Therefore

```{math}
:label: eq:total-info
\int_0^\infty \E r_t\dd t\le2\mathsf h(p_0)\le2\log2 .
```

This exact information identity says that localization gradually reveals the binary label $\one_E(X)$. It is too weak for KLS: the total information may be bounded while a large initial spike forces the cut to leave the balanced window rapidly.

## Intrinsic covariance control

For any probability measure $\nu$, any set $E$ of mass $p$, and $F=E^c$ of mass $q$, covariance decomposition gives

```{math}
:label: eq:cov-decomp
A=p\Sigma_E+q\Sigma_F+pq\delta\delta^T.
```

Thus

```{math}
:label: eq:B-le-A
B:=pq\delta\delta^T\preceq A.
```

In particular, on the support of $A$,

```{math}
:label: eq:intrinsic-bound
pq\,\delta^TA^{-1}\delta\le1.
```

The centroid separation is always controlled in the covariance metric of the posterior. KLS needs Euclidean control; the danger is alignment of $\delta_t$ with large-eigenvalue directions of $A_t$.

A useful warning follows from [](#eq:B-le-A): since $B_t$ has rank one and eigenvalue $r_t$,

```{math}
:label: eq:trivial-lambda
\abs{v_t}^2=s_tr_t\le s_t\lmax(A_t)\le\tfrac14\lmax(A_t).
```

Hence a constant-time estimate of $\E\int_0^T\lmax(A_t)\dd t$ would already imply KLS by Doob's inequality. Any noncircular proof of the two-color Carleson estimate must exploit the cut-specific quantities $G_t,B_t,r_t,D_t$, not first assume constant-time spectral control of $A_t$. [](#prop:ceiling) sharpens this warning for the scalar-bootstrap mechanism: the estimate $\E\int_0^T\lmax(A_t)\dd t\le(1+\kappa)T$ is already sufficient for KLS, while bounding relative-scale excess through the estimate in Section [](#sec:bootstrap) would demand the same scale of covariance input. Thus it is not an independent intermediate target for that particular argument; no claim about every possible propagation argument is made.

## Stopped centroid estimate

:::{prf:lemma} A balanced posterior event gives boundary; uniformly, KLS
:label: lem:survival-implies-kls
Let $\mu$ be isotropic log-concave and $E$ measurable. If, for some $T_0,c_0,b_0>0$,

$$
\Prob\bigl(\min(p_{T_0},q_{T_0})\ge b_0\bigr)\ge c_0,
$$

then $\mu^+(E)\ge c\,c_0b_0\sqrt{T_0}$. Consequently, if $T_0,c_0,b_0$ are universal and the event holds for every balanced cut of every isotropic log-concave measure, KLS follows.
:::

:::{prf:proof}
Keep the actual measurable set $E$ when taking its neighborhoods $E^r$: changing a null subset can change lower outer Minkowski content. For each fixed $r>0$, the posterior mass of $E^r\setminus E$ is a bounded conditional-expectation martingale. Choose deterministic radii realizing the original lower limit. Nonnegativity and Fatou then give

$$
\mathbb E\mu_{T_0}^+(E)\le
\liminf_{j\to\infty}\mathbb E\frac{\mu_{T_0}(E^{r_j}\setminus E)}{r_j}
=\mu^+(E).
$$

The posterior potential has curvature at least $T_0$, even when its convex support has a boundary. Gaussian isoperimetric comparison therefore gives
$\mu_{T_0}^+(E)\ge c\sqrt{T_0}\min(p_{T_0},q_{T_0})$.
For nonsmooth potentials, the proof first approximates the convex part while retaining this quadratic curvature, passes the functional comparison for bounded Lipschitz tests, and only then takes distance cutoffs of $E$. It does not assume continuity of set perimeters under approximation. Averaging the comparison on the survival event yields
$\mu^+(E)\ge c c_0b_0\sqrt{T_0}$.
Finally, concavity and symmetry of the original log-concave law's isoperimetric profile turn the uniform bound at mass $1/2$ into a Cheeger bound. The argument establishes the implication; the uniform survival premise remains to be proved.
:::

:::{prf:assumption} Stopped centroid estimate
:label: ass:stopped-centroid
There exist universal constants $T_0>0$ and $C\ge0$ such that for every isotropic log-concave $\mu$ and every measurable set $E$ with $p_0\in[2/5,3/5]$,

```{math}
:label: eq:stopped-centroid
\E\int_0^{T\wedge\tau}\abs{\delta_t}^2\dd t\le CT,
\qquad 0<T\le T_0 .
```
:::

:::{prf:theorem} Stopped centroid estimate implies KLS
:label: thm:centroid-implies-kls
[](#ass:stopped-centroid) implies a dimension-free lower bound on $h_\mu$ for every isotropic log-concave $\mu$.
:::

:::{prf:proof}
It is enough to prove a universal boundary lower bound for balanced cuts. We give the proof for $p_0=1/2$; the nested interval $p_0\in[2/5,3/5]$ changes only constants.

If $\tau\le T$, then $\sup_{t\le T\wedge\tau}\abs{p_t-p_0}\ge1/6$. Doob's $L^2$ inequality and [](#eq:qv-p) yield

$$
\Prob(\tau\le T)
\le36\E[p]_{T\wedge\tau}
=36\E\int_0^{T\wedge\tau}s_t^2\abs{\delta_t}^2\dd t
\le36CT .
$$

Choose a universal $T\le T_0$ so small that $36CT\le1/2$. Then $\Prob(\tau>T)\ge1/2$, and on this event $\min(p_T,q_T)\ge1/3$. [](#lem:survival-implies-kls) applies with this universal time and survival probability $1/2$.
:::

The same proof shows that it is enough to establish [](#eq:stopped-centroid) for a sequence of balanced near-minimizers of the isoperimetric profile. This observation is what permits the near-Cheeger geometric approach.
