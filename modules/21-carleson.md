---
numbering:
  enumerator: "21.%s"
---

(sec:carleson)=
# The fixed cut, variant E–A: the exact Carleson target

## Consuming the two-color Carleson estimate

This section gives the argument for [](#thm:intro-all-cut).

:::{prf:theorem} Two-color Carleson implies the stopped centroid estimate
:label: thm:carleson-implies-centroid
[](#ass:all-cut-carleson) implies [](#ass:stopped-centroid), and hence KLS.
:::

:::{prf:proof}
By the regularity convention, local martingales may be localized and then limits taken. Define

$$
\widetilde u(t)=\E r_{t\wedge\tau}.
$$

Integrating [](#eq:scalar-riccati) from $a\wedge\tau$ to $b\wedge\tau$ and taking expectations,

$$
\widetilde u(b)-\widetilde u(a)
=\E\int_{[a,b]\cap[0,\tau]}(S_t-D_t)\dd t .
$$

Use [](#ass:all-cut-carleson) on $I=[a,b]$ and discard the nonnegative damping part $(1-\alpha)\E\int D_t\dd t$:

$$
\widetilde u(b)-\widetilde u(a)
\le C_0(b-a)+C_1\int_a^b\widetilde u(t)\dd t .
$$

At time zero, $B_0\preceq A_0=I$ and $B_0$ has rank one, so $r_0\le1$. Gronwall's inequality gives

$$
\widetilde u(t)\le (1+C_0t)e^{C_1t}\le C_*,
\qquad 0\le t\le T_0 .
$$

On $\{t<\tau\}$, $s_t\ge2/9$, hence

$$
\E\int_0^{T\wedge\tau}\abs{\delta_t}^2\dd t
\le\frac92\int_0^T\widetilde u(t)\dd t
\le\frac92C_*T .
$$

This is the stopped centroid estimate. Combining it with [](#eq:qv-p) and Doob's inequality gives a universal time with balanced survival probability at least $1/2$, so [](#lem:survival-implies-kls) concludes.
:::

The same Gronwall mechanism will be reused in Section [](#subsec:consumption) in a slightly generalized form: any estimate of the shape $\E\int\calS_{\mu_t}(E)/s_t\le C_0T+C_1\E\int r_t+\beta\E\int D_t+\mathfrak E(T)$ with an error functional $\mathfrak E(T)\le C_3T$ feeds into the same consumption chain.

The near-Cheeger variant Eldan–B consumes its Carleson estimate on the tight window $\tau_\eta$ rather than the coarse window $\tau$. The following records, once, that the consumption of [](#thm:carleson-implies-centroid) and [](#lem:survival-implies-kls) go through verbatim on $\tau_\eta$, with constants depending only on the fixed (universal) $\eta$.

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
Write $\widetilde u(T)=\E r_{T\wedge\tau_\eta}$. Integrating the scalar Riccati identity [](#eq:scalar-riccati) to $T\wedge\tau_\eta$ gives $\widetilde u(T)=r_0+\E\int_0^{T\wedge\tau_\eta}(S_t-D_t)\dd t$. With [](#eq:tight-carleson), $r_0\le1$ (rank-one $B_0\preceq A_0=I$), and discarding $(1-\alpha)\E\int D_t\dd t\ge0$,

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

The whitened posterior $Y=A_t^{-1/2}(X-a_t)$ has covariance $I$ on the support. A hypothetical quadratic-chaos estimate for $Y$ controls the intrinsic quantity

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
The projection/thin-shell technology and covariance-tail estimates of Guan type explain the earlier logarithmic losses [@Klartag2023Logarithmic; @Guan2025Tail]. Letwin's version-1 preprint now removes the intrinsic quadratic-chaos loss and gives the whitened source bound of [](#cor:qcts-source), but unwhitening still weights the source by $\lmax(A_t)^2$. The KLS-strength improvement would be precisely the replacement of that dynamic spectral-alignment loss by [](#eq:interpolated-source) or by the geometric Stein-trace package of Sections [](#sec:stein)–[](#sec:excess). This paragraph is orientation only; the conditional proof of [](#thm:carleson-implies-centroid) uses [](#ass:all-cut-carleson) directly.
:::
