---
numbering:
  enumerator: "33.%s"
---

(sec:stein-dictionary)=
# The two-colour Stein dictionary and the operator-to-trace gap

*Appendix to the fixed cut, Section [](#sec:introduction).*

Both variants of the fixed cut, the all-cut and the near-Cheeger variant, consume the same covariance contrast of a cut, in two normalizations. This short core section records the exact algebraic dictionary relating that contrast to the Riccati source of Section [](#sec:riccati), and isolates — once — the exact gap of the all-cut variant and the covariance contrast that the proposed geometric approach also seeks to control. No argument in this manuscript yet connects Jacobi/Reilly boundary modes to this trace ([](#conj:almost-stability-gap)).

(subsec:one-gap)=
## The operator-to-trace gap

The per-direction Carleson estimate ([](#cor:per-direction)) is the unconditional budget on the two-color source: with the occupation operator

$$
\calM:=\E\int_0^\infty s_tG_t^2\dd t,
$$

estimate [](#eq:loewner-carleson) reads $\calM\preceq R_0\preceq I_n$, a dimension-free bound at the level of quadratic forms. The KLS-strength statement of the all-cut variant is the *trace* $\Tr(\calM)$, whose only a priori bound is $\Tr R_0\le n$. The entire difficulty of the all-cut approach is this operator-to-trace upgrade. In the product model, [](#conj:product-alignment) isolates its incident-high residue; it is not an equivalent reformulation of the full trace target. The weighted Stein-trace estimate of the near-Cheeger variant ([](#conj:stein-weighted)) faces analogous high-rank boundary modes, but the claimed identification with this occupation operator awaits the almost-stability trace bridge of [](#conj:almost-stability-gap). The available product argument does not prove a static effective-rank bound: summing its coordinate budgets loses a factor $n$, whereas the dimension-dependent early-window estimate follows independently from covariance moments. This motivates an occupation-density bound forcing only $O(1)$ directions to be simultaneously active on the early balanced window; it does not yet prove such temporal sparsity. This is the content of [](#rem:trace-upgrade-unification). The dictionary below is the change of variables tying the exact Riccati and Stein formulations together and supplying the common covariance currency for the proposed geometric approach.

## The two-color Stein representation

:::{prf:proposition} Two-color Stein representation
:label: prop:stein-rep
Let $\nu$ be a probability measure on $\R^n$ with finite fourth moment, mean $a$, covariance $A$, $E$ measurable, $p=\nu(E)\in(0,1)$, and let $\delta,G,K=G+(q-p)\delta\delta^T$ be the two-color quantities of Section [](#sec:notation). For a symmetric matrix $M$ set

$$
f_M(x)=(x-a)^TM(x-a)-\Tr(MA).
$$

Then

```{math}
:label: eq:stein-rep
\ell_{\nu,E}(M):=\int_E f_M\dd\nu
=\Cov_\nu\bigl(\one_E,\;(x-a)^TM(x-a)\bigr)
\;=\;s\bigl(\inner GM+(q-p)\,\delta^TM\delta\bigr)
\;=\;s\,\inner{K}{M}.
```

Consequently the *Stein-trace norm*

```{math}
:label: eq:stein-norm-def
\calS_\nu(E):=\sup_{\norm M_\HS\le1}\abs{\ell_{\nu,E}(M)}^2
\;=\;s^2\,\norm{K}_\HS^2 ,
```

and the functional consumed by the geometric approach is $\calS_\nu(E)/s=s\norm K_\HS^2$. At balance $K=G$, so this equals the Riccati source $S=s\norm G_\HS^2$; off balance the two quantities are related, rather than identified, by [](#lem:stein-vs-source).
:::

:::{prf:proof}
Write $m^E,m^F,\Sigma^E,\Sigma^F$ for the conditional means and covariances, so that $p(m^E-a)+q(m^F-a)=0$ and, by the covariance decomposition [](#eq:cov-decomp), $A=p\Sigma^E+q\Sigma^F+s\,\delta\delta^T$. Then

$$
\int_E f_M\dd\nu
=p\,\inner{M}{\Sigma^E+(m^E-a)(m^E-a)^T-A} .
$$

Now $\Sigma^E-A=q(\Sigma^E-\Sigma^F)-s\delta\delta^T=qG-s\delta\delta^T$ and, since $m^E-a=q\delta$, $(m^E-a)(m^E-a)^T=q^2\delta\delta^T$. Hence

$$
\int_E f_M\dd\nu
=p\inner{M}{qG+(q^2-pq)\delta\delta^T}
=s\inner{M}{G+(q-p)\delta\delta^T}=s\inner KM ,
$$

where we used $pq^2-p^2q=pq(q-p)$. The supremum over $\norm M_\HS\le1$ of the linear functional $M\mapsto s\inner KM$ is $s\norm K_\HS$, giving [](#eq:stein-norm-def).
:::

:::{prf:remark}
The identity $\calS_\nu(E)=s^2\norm K_\HS^2$ is a small but clarifying consolidation. The “Stein” functional is the squared norm of the translation-invariant contrast $K$, whereas the Riccati source uses $G$. They coincide at balance; away from balance their difference is the explicit damping term $(q-p)\delta\delta^T$. Thus the all-cut and near-Cheeger variants exchange comparable, not identical, currency on the tight window, with the universal conversion constants below.
:::

:::{prf:lemma} Conversion between Stein norm and Riccati source on the tight window
:label: lem:stein-vs-source
For $0<\eta\le\tfrac14$, on the event $\{t<\tau_\eta\}$, with $S_t=s_t\norm{G_t}_\HS^2$ and $D_t\ge r_t^2$ as in [](#eq:D-ge-r2),

```{math}
:label: eq:conversion
S_t\;\le\;2\,\frac{\calS_{\mu_t}(E)}{s_t}+64\,\eta^2 D_t,
\qquad
\frac{\calS_{\mu_t}(E)}{s_t}\;\le\;2\,S_t+64\,\eta^2 D_t .
```
:::

:::{prf:proof}
On the tight window $\abs{p_t-\tfrac12}\le\eta$, so $\abs{q_t-p_t}\le2\eta$ and $s_t\ge\tfrac14-\eta^2\ge\tfrac3{16}$ for $\eta\le\tfrac14$; we only use $s_t\ge\tfrac14\cdot (1-4\eta^2)\ge\tfrac1{4}\cdot\tfrac34$, and in fact only $r_t^2/s_t\le 8r_t^2$, valid for $s_t\ge\tfrac18$. From $G=K-(q-p)\delta\delta^T$,

$$
s\norm G_\HS^2\le2s\norm K_\HS^2+2s(q-p)^2\abs\delta^4
\le2\,\frac{\calS}{s}+8\eta^2\,\frac{r^2}{s}
\le2\,\frac{\calS}{s}+64\eta^2r^2 ,
$$

and $r^2\le D$ by [](#eq:D-ge-r2). The reverse inequality is identical with the roles of $G$ and $K$ exchanged.
:::
