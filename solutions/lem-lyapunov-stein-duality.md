---
title: 'Lyapunov–Stein duality'
label: sec:sol-lyapunov-stein-duality
ledger-node: lem:lyapunov-stein-duality
numbering:
  enumerator: D13.%s
---

*Part of the fixed-cut archive, Chapter [](#sec:carleson); the reading order is on the [full proofs](#sec:proofs-archive) page.*

**Overview.** This dossier proves [](#lem:lyapunov-stein-duality) as [](#lem:sol-lyapunov-stein-duality). At every time $t>0$, $s_t\inner{K_t}{\mathscr L_{A_t}^{-1}K_t}\le4/t$; the lemma also gives the cut-oriented source scale and direct-sum invariance of $\lambda_{\rm cut}$. The proof combines the anisotropic Brascamp–Lieb quadratic-form estimate from [](#lem:pathwise-BL) with finite-dimensional Hilbert-space duality for the Lyapunov operator. The proof is unconditional for $t>0$ and asserts nothing at $t=0$.

1. Support convention: $K_t$ lives on the range of $A_t$ ([](#eq:sol-K-on-support)). There the support inverse coincides with the pseudoinverse [](#eq:sol-lyapunov-pseudoinverse).
2. The two-color pairing [](#eq:sol-anisotropic-color-pairing), followed by Cauchy–Schwarz and Brascamp–Lieb on the $t$-uniformly log-concave posterior, gives [](#eq:sol-anisotropic-BL) for every symmetric test matrix $M$.
3. The right side of step 2 is written as $\inner M{\mathscr L_{A_t}M}$ ([](#eq:sol-lyapunov-energy)). The duality identity [](#eq:sol-hilbert-duality), taken at $M=\mathscr L_{A_t}^{-1}K_t$, then gives [](#eq:sol-lyapunov-stein-duality). Multiplying by $\lambda_{\rm cut}$ gives [](#eq:sol-cut-oriented-source-scale).
4. Block-diagonal invariance of $\mathscr L_{A\oplus B}$ proves [](#eq:sol-cut-direct-sum).
5. An auxiliary remark, which is not part of the lemma ([](#rem:sol-cut-scale-calibration)), gives the harmonic-mean formula [](#eq:sol-cut-harmonic-mean) and the two-tail calibration [](#eq:sol-cut-two-tail).

**Setup and covariance-support convention.** Fix a time $t>0$ in the stochastic-localization process and a cut $E$ for which $p_t,q_t>0$. Retain the manuscript notation

$$
A_t=\Cov_{\mu_t}(X),\qquad s_t=p_tq_t,
\qquad K_t=G_t+(q_t-p_t)\delta_t\delta_t^T.
$$

Let $H_t=\operatorname{Ran}(A_t)$ and let $P_t$ be the orthogonal projection onto $H_t$. If $v\in\ker A_t$, then $\E_{\mu_t}(v\cdot(X-a_t))^2=0$. Hence $X-a_t\in H_t$ almost surely, and the conditional means and covariance matrices defining $K_t$ also live on $H_t$. In particular,

```{math}
:label: eq:sol-K-on-support
K_t=P_tK_tP_t.
```

For a positive-semidefinite matrix $A$, write $H=\operatorname{Ran}(A)$. When it is applied to a supported matrix $K=PKP$, the notation $\mathscr L_A^{-1}K$ below means the inverse on the Hilbert space $\mathrm{Sym}(H)$, followed by zero extension to the ambient space. On such inputs this agrees with the ambient Moore–Penrose inverse $\mathscr L_A^\dagger$. Indeed, in an $A$-eigenbasis with eigenvalues $\lambda_i\ge0$, the latter is

```{math}
:label: eq:sol-lyapunov-pseudoinverse
(\mathscr L_A^\dagger C)_{ij}
=
\begin{cases}
\displaystyle\frac{2C_{ij}}{\lambda_i+\lambda_j},&\lambda_i+\lambda_j>0,\\
0,&\lambda_i+\lambda_j=0.
\end{cases}
```

For a covariance contrast $K=PKP$, this is exactly the inverse on $\mathrm{Sym}(H)$ and is independent of the ambient zero extension.

:::{prf:lemma} = [](#lem:lyapunov-stein-duality)
:label: lem:sol-lyapunov-stein-duality
On symmetric matrices over $H_t$, define

$$
\mathscr L_{A_t}(M)=\frac{A_tM+MA_t}{2}.
$$

Then

```{math}
:label: eq:sol-lyapunov-stein-duality
s_t\inner{K_t}{\mathscr L_{A_t}^{-1}K_t}\le\frac4t.
```

For $K\ne0$ set

$$
\lambda_{\rm cut}(A,K)
:=\frac{\norm K_{\HS}^2}{\inner K{\mathscr L_A^{-1}K}},
$$

and set $\lambda_{\rm cut}(A,0)=0$. Then

```{math}
:label: eq:sol-cut-oriented-source-scale
s_t\norm{K_t}_{\HS}^2
\le\frac{4\lambda_{\rm cut}(A_t,K_t)}t.
```

Moreover, if $A,B\succeq0$ and $K$ is supported on $\operatorname{Ran}(A)$, then

```{math}
:label: eq:sol-cut-direct-sum
\lambda_{\rm cut}(A\oplus B,K\oplus0)=\lambda_{\rm cut}(A,K).
```
:::

:::{prf:proof}
We first retain the anisotropic quadratic-form estimate inside the certified proof of [](#lem:pathwise-BL). Let $M\in\mathrm{Sym}(H_t)$ and set

$$
f_M(x)=(x-a_t)^TM(x-a_t)-\Tr(MA_t),
\qquad
g=\frac{\one_E-p_t}{\sqrt{s_t}}.
$$

Then $\E_{\mu_t}g=\E_{\mu_t}f_M=0$, $\E_{\mu_t}g^2=1$, and the two-color covariance identity gives

```{math}
:label: eq:sol-anisotropic-color-pairing
\E_{\mu_t}[g f_M]=\sqrt{s_t}\,\inner{K_t}{M}.
```

The posterior $\mu_t$, considered on its affine support $a_t+H_t$, is $t$-uniformly log-concave. Cauchy–Schwarz and Brascamp–Lieb on that support [@BrascampLieb1976] therefore give

```{math}
:label: eq:sol-anisotropic-BL
\begin{aligned}
s_t\inner{K_t}{M}^2
&\le \Var_{\mu_t}(f_M)\\
&\le \frac1t\E_{\mu_t}\abs{\nabla_{H_t}f_M}^2
=\frac4t\Tr(MA_tM).
\end{aligned}
```

The quadratic test belongs to the Brascamp–Lieb form domain because the finite-time posterior has the Gaussian factor $e^{-t\abs{x}^2/2}$ on its support; alternatively one obtains [](#eq:sol-anisotropic-BL) from smooth truncations and form closure. Thus no boundedness of $f_M$ is being assumed.

We now express the right side of [](#eq:sol-anisotropic-BL) in its exact Hilbert-space form. On $\mathrm{Sym}(H_t)$, equipped with the Hilbert–Schmidt inner product, $\mathscr L_{A_t}$ is self-adjoint and positive definite, and

```{math}
:label: eq:sol-lyapunov-energy
\inner{M}{\mathscr L_{A_t}M}
=\Tr(MA_tM)
=\norm{A_t^{1/2}M}_{\HS}^2.
```

For any positive-definite self-adjoint operator $L$ on a finite-dimensional real Hilbert space, Cauchy–Schwarz after inserting $L^{\pm1/2}$ yields the duality identity

```{math}
:label: eq:sol-hilbert-duality
\sup_{M\ne0}\frac{\inner{K}{M}^2}{\inner{M}{LM}}
=\inner K{L^{-1}K}.
```

More explicitly, $\inner KM=\inner{L^{-1/2}K}{L^{1/2}M}$ gives “$\le$”, and equality is attained at $M=L^{-1}K$ when $K\ne0$; for $K=0$ both sides vanish.

Apply [](#eq:sol-hilbert-duality) to $L=\mathscr L_{A_t}$ in [](#eq:sol-anisotropic-BL). Equivalently, insert $M=\mathscr L_{A_t}^{-1}K_t$. If $K_t\ne0$, positivity gives $d_t:=\inner{K_t}{\mathscr L_{A_t}^{-1}K_t}>0$, and

$$
s_t d_t^2\le\frac4t d_t.
$$

Division by $d_t$ proves [](#eq:sol-lyapunov-stein-duality). If $K_t=0$, that inequality is simply $0\le4/t$. In the nonzero case, multiplication by $\norm{K_t}_{\HS}^2/d_t=\lambda_{\rm cut}(A_t,K_t)$ gives [](#eq:sol-cut-oriented-source-scale). In the zero case, both sides of that source-scale inequality are zero by the separate convention $\lambda_{\rm cut}(A_t,0)=0$.

It remains to verify the direct-sum claim. The block-diagonal subspace is invariant under $\mathscr L_{A\oplus B}$, and the support inverse satisfies

$$
\mathscr L_{A\oplus B}^{-1}(K\oplus0)
=\mathscr L_A^{-1}K\oplus0.
$$

Both the Hilbert–Schmidt numerator and the Lyapunov denominator in the definition of $\lambda_{\rm cut}$ are therefore unchanged, proving [](#eq:sol-cut-direct-sum); the $K=0$ case again follows from the separate convention.
:::

:::{prf:remark} Auxiliary eigenbasis formula and two-tail calibration
:label: rem:sol-cut-scale-calibration
The following identities are useful calibrations, but they are not assertions of [](#lem:sol-lyapunov-stein-duality). Let $A\succeq0$, let $H=\operatorname{Ran}(A)$, and let $K\ne0$ be supported on $H$. In an eigenbasis of $A|_H$ with positive eigenvalues $\lambda_1,\ldots,\lambda_r$, formula [](#eq:sol-lyapunov-pseudoinverse) gives

$$
\inner K{\mathscr L_A^{-1}K}
=\sum_{i,j=1}^r\frac{2\abs{K_{ij}}^2}{\lambda_i+\lambda_j}
=\sum_{i,j=1}^r
\frac{\abs{K_{ij}}^2}{(\lambda_i+\lambda_j)/2}.
$$

Since $\norm K_{\HS}^2=\sum_{i,j=1}^r\abs{K_{ij}}^2$, one obtains the auxiliary identity

```{math}
:label: eq:sol-cut-harmonic-mean
\lambda_{\rm cut}(A,K)
=\frac{\displaystyle\sum_{i,j=1}^r\abs{K_{ij}}^2}
{\displaystyle\sum_{i,j=1}^r
\frac{\abs{K_{ij}}^2}{(\lambda_i+\lambda_j)/2}}.
```

Thus $\lambda_{\rm cut}(A,K)$ is the $\abs{K_{ij}}^2$-weighted harmonic mean of $(\lambda_i+\lambda_j)/2$.

For the anisotropic two-tail pair of [](#prop:two-tail),

$$
A_\Lambda=\diag(\Lambda,1,\ldots,1),
\qquad
K_\Lambda=8a\varphi(a)\Lambda\,e_1e_1^T.
$$

Since $\mathscr L_{A_\Lambda}(e_1e_1^T)=\Lambda e_1e_1^T$, one has $\mathscr L_{A_\Lambda}^{-1}K_\Lambda=K_\Lambda/\Lambda$. Hence

$$
\lambda_{\rm cut}(A_\Lambda,K_\Lambda)
=\frac{\norm{K_\Lambda}_{\HS}^2}
{\norm{K_\Lambda}_{\HS}^2/\Lambda}
=\Lambda,
$$

or equivalently

```{math}
:label: eq:sol-cut-two-tail
\lambda_{\rm cut}(A_\Lambda,K_\Lambda)=\Lambda.
```

This auxiliary calibration is why `prop:two-tail` remains in the dossier's declared dependencies even though the formal lemma itself ends with [](#eq:sol-cut-direct-sum).
:::

**Scope, hypotheses, and initial-time exclusion.** The proof uses only $t>0$, the finite-time posterior Brascamp–Lieb inequality on the covariance support, the two-color identity already contained in the certified dependency [](#lem:pathwise-BL), and finite-dimensional Hilbert-space duality. It is unconditional in the manuscript's localization setup and has no unclosed analytic step. It makes no assertion at $t=0$: the factor $t^{-1}$ is singular, and the pointwise estimate supplies neither an integrable initial-time bound nor an expected covariance-occupation theorem.

**Obstructions respected.** The ledger node has no formal `bounded_by` edge. The formal statement nonetheless remains on the safe side of the known route fences: it uses the full cut-oriented tensor rather than only radial or projection data, and direct-sum invariance removes only genuinely irrelevant spectator blocks. The auxiliary calibration records $\lambda_{\rm cut}(A_\Lambda,K_\Lambda)=\Lambda$, not a false dimension-free scale, on the anisotropic two-tail obstruction. No operator-to-trace upgrade or high-rank occupation estimate is claimed.
