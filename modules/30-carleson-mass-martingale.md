---
numbering:
  enumerator: "30.%s"
---

(sec:carleson)=
# The fixed cut: the mass martingale and the Carleson estimate

Part of the fixed-cut archive (Chapter [](#sec:introduction)); this chapter holds the stochastic identities of a fixed cut and the all-cut argument: the mass martingale reduces KLS to the survival of a balanced cut up to a universal time, and an absorptive two-color Carleson estimate gives that survival.

(sec:mass-martingale)=
## The mass martingale

### Quadratic variation and information rate

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

### Intrinsic covariance control

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

Hence a constant-time estimate of $\E\int_0^T\lmax(A_t)\dd t$ would already imply KLS by Doob's inequality. Any noncircular proof of the two-color Carleson estimate must exploit the cut-specific quantities $G_t,B_t,r_t,D_t$, not first assume constant-time spectral control of $A_t$. [](#prop:ceiling) sharpens this warning for the scalar-bootstrap mechanism: the estimate $\E\int_0^T\lmax(A_t)\dd t\le(1+\kappa)T$ is already sufficient for KLS, while bounding relative-scale excess through the estimate in Chapter [](#sec:bootstrap) would demand the same scale of covariance input. Thus it is not an independent intermediate target for that particular argument; no claim about every possible propagation argument is made.

### Stopped centroid estimate

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
Finally, concavity and symmetry of the original log-concave law's isoperimetric profile turn the uniform bound at mass $1/2$ into a Cheeger bound. The argument establishes the implication; the uniform survival hypothesis is not proved here.
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

The same proof shows that it is enough to establish [](#eq:stopped-centroid) for a sequence of balanced near-minimizers of the isoperimetric profile. This observation is what makes the near-Cheeger variant possible.

## From the Carleson estimate to survival

This section gives the argument for [](#thm:intro-all-cut).

:::{prf:theorem} Two-color Carleson implies the stopped centroid estimate
:label: thm:carleson-implies-centroid
[](#ass:all-cut-carleson) implies [](#ass:stopped-centroid), and hence KLS.
:::

:::{prf:proof}
First establish finiteness without using the Carleson hypothesis. Summing [](#cor:per-direction) over the fixed coordinate vectors and applying Tonelli gives

$$
\E\int_0^\infty S_t\dd t\le\Tr R_0\le n.
$$

Put $\widetilde u(T)=\E r_{T\wedge\tau}$. Localize [](#eq:scalar-riccati) at increasing times that also bound $r$, the martingale, and the accumulated source and damping. At each localized horizon the martingale has zero expectation. Remove these auxiliary stops using continuity and Fatou for the nonnegative terminal and damping terms, and monotone convergence for the source. Since $B_0\preceq I$ has rank at most one, this yields

$$
\widetilde u(T)+\E\int_0^{T\wedge\tau}D_t\dd t
\le r_0+\E\int_0^{T\wedge\tau}S_t\dd t\le1+n.
$$

Thus $\widetilde u$ is measurable and locally integrable, and Tonelli gives
$\E\int_0^{T\wedge\tau}r_t\dd t\le\int_0^T\widetilde u(t)\dd t<\infty$.
The dimension-dependent budget is used only for finiteness.

Now apply [](#ass:all-cut-carleson) to each deterministic prefix $I=[0,T]$, after the auxiliary stops have been removed. All terms are finite, so absorption gives

$$
\widetilde u(T)+(1-\alpha)\E\int_0^{T\wedge\tau}D_t\dd t
\le1+C_0T+C_1\int_0^T\widetilde u(t)\dd t.
$$

Discarding the nonnegative damping term and applying integral Gronwall gives the dimension-free bound

$$
\widetilde u(t)\le(1+C_0t)e^{C_1t}\le C_*:=(1+C_0T_0)e^{C_1T_0},
\qquad 0\le t\le T_0.
$$

On $\{t<\tau\}$, $s_t\ge2/9$, hence

$$
\E\int_0^{T\wedge\tau}\abs{\delta_t}^2\dd t
\le\frac92\int_0^T\widetilde u(t)\dd t
\le\frac92C_*T .
$$

This is the stopped centroid estimate. Combining it with [](#eq:qv-p) and Doob's inequality gives a universal time with balanced survival probability at least $1/2$, so [](#lem:survival-implies-kls) concludes.
:::

The same Gronwall mechanism will be reused in Section [](#subsec:consumption) in a slightly generalized form: any estimate of the shape $\E\int\calS_{\mu_t}(E)/s_t\le C_0T+C_1\E\int r_t+\beta\E\int D_t+\mathfrak E(T)$ with an error functional $\mathfrak E(T)\le C_3T$ feeds into the same chain of implications.

The near-Cheeger variant uses its Carleson estimate on the tight window $\tau_\eta$ rather than the coarse window $\tau$. The arguments of [](#thm:carleson-implies-centroid) and [](#lem:survival-implies-kls) go through verbatim on $\tau_\eta$, with constants depending only on the fixed (universal) $\eta$:

:::{prf:corollary} Tight-window consumption
:label: cor:tight-window-consumption
Fix $\eta\in(0,\tfrac16]$. Suppose that for an isotropic log-concave $\mu$ and a set $E$ with $\abs{p_0-\tfrac12}\le\eta/2$ an absorptive two-color Carleson estimate holds on the *tight* window from time zero: for some constants $C_0,C_1$, some $\alpha<1$, and every $T\le T_0$,

```{math}
:label: eq:tight-carleson
\E\int_0^{T\wedge\tau_\eta}S_t\dd t
\le C_0T+C_1\E\int_0^{T\wedge\tau_\eta}r_t\dd t
+\alpha\E\int_0^{T\wedge\tau_\eta}D_t\dd t .
```

Then the conclusion of [](#lem:survival-implies-kls) holds for $(\mu,E)$, with the universal boundary constant depending only on $T_0,C_0,C_1,\alpha$ and the fixed $\eta$.
:::

:::{prf:proof}
Write $\widetilde u(T)=\E r_{T\wedge\tau_\eta}$. The same coordinate source budget and localization–Fatou argument, with $\tau_\eta$ in place of $\tau$, give
$\widetilde u(T)+\E\int_0^{T\wedge\tau_\eta}D_t\dd t\le r_0+\E\int_0^{T\wedge\tau_\eta}S_t\dd t\le1+n$.
Thus all occupation terms are finite before [](#eq:tight-carleson) is used on deterministic prefixes. With $r_0\le1$ (rank at most one and $B_0\preceq I$), discard $(1-\alpha)\E\int D_t\dd t\ge0$ to obtain

$$
\widetilde u(T)\le 1+C_0T+C_1\E\int_0^{T\wedge\tau_\eta}r_t\dd t
\le 1+C_0T+C_1\int_0^T\widetilde u(s)\dd s ,
$$

using $\E\int_0^{T\wedge\tau_\eta}r_t\dd t\le\int_0^T\widetilde u(s)\dd s$. Gronwall gives $\widetilde u(T)\le(1+C_0T)e^{C_1T}\le C_*$ on $[0,T_0]$. On $\{t<\tau_\eta\}$, $s_t\ge\tfrac14-\eta^2\ge\tfrac29$, hence $\E\int_0^{T\wedge\tau_\eta}\abs{\delta_t}^2\dd t\le\tfrac92\int_0^T\widetilde u\le\tfrac92C_*T$. For survival, if $\tau_\eta\le T$ then $\sup_{t\le T\wedge\tau_\eta}\abs{p_t-p_0}\ge\eta/2$, so by the exit identity and $s_t\le\tfrac14$,

$$
\Prob(\tau_\eta\le T)\le\frac4{\eta^2}\E[p]_{T\wedge\tau_\eta}
=\frac4{\eta^2}\E\int_0^{T\wedge\tau_\eta}s_t^2\abs{\delta_t}^2\dd t
\le\frac1{4\eta^2}\E\int_0^{T\wedge\tau_\eta}\abs{\delta_t}^2\dd t
\le\frac{9C_*T}{8\eta^2}.
$$

Choose a universal $T\le T_0$, depending only on the fixed $\eta$, so small that this is $\le\tfrac12$; then $\Prob(\tau_\eta>T)\ge\tfrac12$ and on this event $\min(p_T,q_T)\ge\tfrac12-\eta\ge\tfrac13$. [](#lem:survival-implies-kls) now yields a universal boundary lower bound.
:::

## Unconditional control away from zero

The Carleson estimate is only difficult in the initial time layer. The reason is that $\mu_t$ is $t$-uniformly log-concave for every $t>0$.

:::{prf:lemma} Pathwise Brascamp–Lieb source bound
:label: lem:pathwise-BL
For every $t>0$,

```{math}
:label: eq:BL-source
s_t\norm{K_t}_{\HS}^2
\le \frac{4\lmax(A_t)}{t}
\le \frac4{t^2},
```

where $K_t=G_t+(q_t-p_t)\delta_t\delta_t^T$.
:::

:::{prf:proof}
Since the potential of $\mu_t$ has Hessian at least $tI$, the Brascamp–Lieb inequality gives

$$
\Var_{\mu_t}(f)\le\frac1t\E_{\mu_t}\abs{\nabla f}^2
$$

for smooth $f$ [@BrascampLieb1976]. Apply this to

$$
f_M(x)=(x-a_t)^TM(x-a_t)-\Tr(MA_t).
$$

Then $\E\abs{\nabla f_M}^2=4\Tr(MA_tM)$. With $g=(\one_E-p_t)/\sqrt{s_t}$, one computes

$$
\E_{\mu_t}[g f_M]=\sqrt{s_t}\,\inner{K_t}{M}.
$$

Cauchy–Schwarz gives

$$
s_t\inner{K_t}{M}^2
\le \Var_{\mu_t}(f_M)
\le\frac4t\Tr(MA_tM)
\le\frac{4\lmax(A_t)}t\norm M_{\HS}^2 .
$$

Choose $M=K_t/\norm{K_t}_{\HS}$. The second inequality follows from $A_t\preceq t^{-1}I$, the Brascamp–Lieb bound applied to linear functions, recorded as [](#eq:BL-cap).
:::

:::{prf:lemma} Cut-oriented Lyapunov–Stein duality
:label: lem:lyapunov-stein-duality
For $t>0$, let $\mathscr L_{A_t}$ be the Lyapunov operator on symmetric matrices,

$$
\mathscr L_{A_t}(M)=\frac{A_tM+MA_t}{2}.
$$

Then, on the covariance support,

```{math}
:label: eq:lyapunov-stein-duality
s_t\inner{K_t}{\mathscr L_{A_t}^{-1}K_t}\le\frac4t.
```

For $K\ne0$ define the cut-oriented covariance scale

$$
\lambda_{\rm cut}(A,K)
:=\frac{\norm K_{\HS}^2}{\inner K{\mathscr L_A^{-1}K}},
$$

and set it to zero for $K=0$. Then

```{math}
:label: eq:cut-oriented-source-scale
s_t\norm{K_t}_{\HS}^2
\le\frac{4\lambda_{\rm cut}(A_t,K_t)}t.
```

The scale ignores independent spectator blocks:

$$
\lambda_{\rm cut}(A\oplus B,K\oplus0)=\lambda_{\rm cut}(A,K).
$$
:::

In an $A$-eigenbasis, $\lambda_{\rm cut}(A,K)$ is the $|K_{ij}|^2$-weighted harmonic mean of $(\lambda_i(A)+\lambda_j(A))/2$. Thus it equals the inflated variance in the anisotropic two-tail example while remaining unchanged under irrelevant direct sums. It is a calibrated, tensor-stable possible replacement for the global operator norm, not an initial-layer occupation estimate: [](#eq:cut-oriented-source-scale) still has a singular $t^{-1}$ factor.

:::{prf:corollary} The source is pathwise controlled away from zero
:label: cor:away-from-zero
There exists a universal $\eta_0>0$ such that, for $0<\eta\le\eta_0$ and on $\{t<\tau_\eta\}$,

```{math}
:label: eq:away-source
S_t\le\frac8{t^2}+\frac12D_t .
```

Consequently, for every interval $I\subset[t_0,T_0]$,

$$
\E\int_{I\cap[0,\tau_\eta]}S_t\dd t
\le \frac8{t_0^2}\abs I+\frac12\E\int_{I\cap[0,\tau_\eta]}D_t\dd t .
$$
:::

:::{prf:proof}
Use

$$
\norm G_{\HS}\le\norm K_{\HS}+\abs{q-p}\abs\delta^2.
$$

On the tight window, $s_t$ is bounded below and $\abs{q_t-p_t}\le2\eta$. Hence

$$
S_t\le2s_t\norm{K_t}_{\HS}^2+C\eta^2r_t^2.
$$

Choose $\eta$ so that $C\eta^2r_t^2\le\frac12D_t$, using [](#eq:D-ge-r2), and apply [](#lem:pathwise-BL).
:::

This shows that no pointwise pathwise improvement is possible in general: the remaining problem is probabilistic and small-time.

## A non-alignment formulation

The whitened posterior $Y=A_t^{-1/2}(X-a_t)$ has covariance $I$ on the support. The quadratic-chaos input [](#thm:letwin-qcts), applied as in [](#cor:qcts-source), controls the intrinsic quantity

$$
s_t\Tr(\WH_t^2),
\qquad \WH_t=A_t^{-1/2}G_tA_t^{-1/2}.
$$

But the Riccati source is Euclidean:

```{math}
:label: eq:euclidean-source
S_t=s_t\norm{G_t}_{\HS}^2=s_t\Tr(A_t\WH_tA_t\WH_t).
```

Thus the missing estimate is not merely intrinsic size control. It is a non-alignment statement between the color Hessian $\WH_t$ and the large spectral windows of $A_t$.

A pointwise KLS-strength target would be

```{math}
:label: eq:pointwise-nonalignment
\E\left[\one_{\{t<\tau\}}s_t\Tr(A_t\WH_tA_t\WH_t)\right]
\le C\left(1+\E[\one_{\{t<\tau\}}r_t]\right),
\qquad 0<t<T_0 .
```

The Riccati identity suggests a more flexible small-time estimate with damping absorption:

```{math}
:label: eq:interpolated-source
\E\left[\one_{\{t<\tau_\eta\}}S_t\right]
\le
C t^{\eps-1}\left(1+\E[\one_{\{t<\tau_\eta\}}r_t]\right)
+\alpha\E\left[\one_{\{t<\tau_\eta\}}D_t\right],
\qquad \alpha<1,
```

for some universal $\eps>0$. Unlike an $A_t$-weighted estimate such as $\Tr(K_tA_tK_t)$, [](#eq:interpolated-source) directly controls the Euclidean source $S_t$ and therefore integrates to the Carleson estimate near zero. This is a sharp stochastic formulation of the non-alignment problem.

:::{prf:remark} Relation with logarithmic-scale results
The projection/thin-shell technology and covariance-tail estimates of Guan type explain the earlier logarithmic losses [@Klartag2023Logarithmic; @Guan2025Tail]. The quadratic estimate [](#thm:letwin-qcts), from Letwin's version-1 preprint, gives the whitened source bound of [](#cor:qcts-source), but unwhitening still weights the source by $\lmax(A_t)^2$. The KLS-strength improvement would be precisely the replacement of that dynamic spectral-alignment loss by [](#eq:interpolated-source) or by the geometric Stein-trace package of Chapter [](#sec:stein). This paragraph is orientation only; the conditional proof of [](#thm:carleson-implies-centroid) uses [](#ass:all-cut-carleson) directly.
:::
