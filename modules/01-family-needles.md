---
numbering:
  enumerator: "1.%s"
---

(sec:family-needles)=
# Family 1: classical needle localization

**Object followed.** One-dimensional restrictions of $\mu$ to segments — *needles* — carrying a log-concave weight.

**What it buys.** The KLS localization lemma reduces certain $n$-dimensional integral inequalities to inequalities on a segment [@KannanLovaszSimonovits1995]. Schematically: given two integral constraints

$$
\int_{\R^n}g_1\dd x\ge0,\qquad \int_{\R^n}g_2\dd x\ge0,
$$

it produces points $a,b\in\R^n$ and an affine $\ell>0$ such that both constraints remain valid for the one-dimensional measure

```{math}
:label: eq:needle-measure
\ell(t)^{n-1}\dd t,\qquad 0\le t\le1,
```

carried on the segment $x(t)=(1-t)a+tb$. The weight $\ell^{n-1}$ is log-concave, so the reduced problem is a one-dimensional log-concave problem, and one-dimensional log-concave isoperimetry is completely understood: for a log-concave $\nu$ on $\R$ with coordinate $T$,

```{math}
:label: eq:one-dim-isoperimetry
h_\nu\asymp\frac1{\sqrt{\Var_\nu T}} .
```

**Sharpest result.** Combining [](#eq:one-dim-isoperimetry) with localization gives

```{math}
:label: eq:needle-bound
h_\mu\gtrsim\frac1{\sqrt{\Tr\Cov\mu}},
```

which in isotropic position ($\Tr\Cov\mu=n$) is the classical bound

$$
\PsiKLS_n\lesssim\sqrt n ,
$$

the 1995 entry of the history table in Section [](#subsec:kls-status).

**The precise missing estimate.** A covariance-sensitive decomposition: one whose needles inherit the *operator* covariance of $\mu$, not merely one or two scalar integral constraints.

**Why it stalls.** The obstruction is exact, and it is a counting statement. The localization construction preserves one or two scalar integral constraints. Isotropy is $n(n+1)/2$ constraints. Nothing forces an individual needle to be even approximately isotropic, and in fact a single needle can have variance of order $n$ while the original measure has $\Cov\mu=I$. This is precisely why [](#eq:needle-bound) sees $\Tr\Cov\mu$ — a sum of $n$ eigenvalues — where the affine conjecture [](#eq:kls-affine) asks for $\norm{\Cov\mu}_\op$, the largest one alone. The gap between $\Tr$ and $\norm{\cdot}_\op$ in [](#eq:needle-bound) *is* the factor $\sqrt n$.

Klartag's needle decomposition, built from transport rays rather than from the bisection construction, is substantially more geometric and can be arranged so that a chosen mean-zero function remains mean-zero on almost every needle [@Klartag2014Needle]. That is a genuine strengthening — it is one preserved constraint chosen adaptively rather than arbitrarily — but it still does not deliver uniformly bounded conditional covariance on the needles.

:::{prf:remark} What a deterministic localization proof would have to supply
:label: rem:needle-requirement
A successful deterministic localization proof of KLS would need a genuinely new covariance-sensitive decomposition, not merely sharper one-dimensional inequalities. The one-dimensional theory in [](#eq:one-dim-isoperimetry) is already sharp; there is no slack left to extract there. This is the structural reason the field moved to the stochastic construction of Section [](#sec:family-sl), which preserves covariance information by construction — at the price of preserving it only in law, along a random path.
:::

**Where this family enters the four approaches.** It does not, directly, and that is worth saying plainly: none of this manuscript's four approaches decomposes $\mu$ into one-dimensional pieces. The moment-map approach (Approach C, Section [](#sec:moment-map-cmh)) is the only deterministic approach here, but it works in the moment-map coordinates of Section [](#sec:family-moment-map) rather than by needle decomposition. What the family contributes is the diagnosis — global isotropy is not inherited needle by needle — which is the first instance of the fixed-versus-adaptive difficulty of Section [](#sec:kls-remaining).
