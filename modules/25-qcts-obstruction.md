---
numbering:
  enumerator: "25.%s"
---

(sec:qcts)=
# The static quadratic-chaos input and the two-tail obstruction

The time-zero version of two-color covariance control is already a strong statement. The intrinsic estimate used here is [](#thm:letwin-qcts), from Letwin's July 2026 version-1 preprint [@Letwin2026QuadraticKLS]. Its application to a localized posterior separates intrinsic quadratic control from the covariance-alignment problem created by unwhitening. The quantified two-tail configuration at the end of the section is the static obstruction that both branches of the fixed-cut approach must respect: it fixes the covariance weight of the near-Cheeger variant and marks the boundary of what slice-wise verification can establish for the all-cut variant.

Let $X\sim\nu$ be isotropic and log-concave, and put

$$
Z=XX^T-I.
$$

For a color

$$
g=\frac{\one_E-p}{\sqrt{pq}},
\qquad p=\nu(E),\quad q=1-p,
$$

one computes

```{math}
:label: eq:color-tensor
\E[gZ]=\sqrt{pq}\left(\Sigma_E-\Sigma_F+(q-p)\delta\delta^T\right).
```

At exact balance, $p=q=1/2$, this is $\frac12(\Sigma_E-\Sigma_F)$.

:::{prf:definition} Quadratic-chaos thin shell
:label: def:qcts
For isotropic log-concave $\nu$, define

$$
\calQ(\nu)=\sup_{\norm M_{\HS}=1}\Var_\nu(X^TMX).
$$

The quadratic-chaos thin-shell assertion is

```{math}
:label: eq:QCTS
\calQ(\nu)\le C
```

with a universal constant $C$.
:::

:::{prf:theorem} Quadratic Poincaré inequality; Letwin
:label: thm:letwin-qcts
If $X$ is isotropic and log-concave on $\R^n$, then for every symmetric matrix $M$,

```{math}
:label: eq:letwin-qcts
\Var(X^TMX)
\ \le\ 2\,\E\abs{\nabla(X^TMX)}^2
\ =\ 8\norm M_{\HS}^2.
```

Consequently $\calQ(\nu)\le8$ in [](#def:qcts).
:::

:::{prf:remark} Epistemic status
:label: rem:letwin-status
The source of [](#thm:letwin-qcts) is [@Letwin2026QuadraticKLS, Thm. 1.2], pinned to arXiv:2607.24164v1. This identifies the preprint version; the statement's badge and proof link separately record its verification here. The proof uses the moment measure of $\nu$, its positive symmetric Stein kernel, congruence, and an $H^{-1}$ inequality (Section [](#subsec:mm-noncommutativity)). The deductions below use this quadratic statement, not source Theorem 1.1 on general KLS.
:::

:::{prf:corollary} Whitened two-color control and its exact alignment loss
:label: cor:qcts-source
Let $\nu$ be centered and log-concave with positive-definite covariance $A$, let $E$ have mass $p\in(0,1)$, put $s=p(1-p)$, and let $K$ be the translation-invariant two-color contrast from [](#prop:stein-rep). Then

```{math}
:label: eq:letwin-whitened-source
s\norm{A^{-1/2}KA^{-1/2}}_{\HS}^2\le8,
\qquad
s\norm K_{\HS}^2\le8\lmax(A)^2.
```

If in addition $p\in[1/3,2/3]$, then

```{math}
:label: eq:letwin-euclidean-source
s\norm G_{\HS}^2\le17\lmax(A)^2.
```

At exact balance, where $K=G$, the constant in the last display is $8$.
:::

:::{prf:proof}
Whiten $Y=A^{-1/2}X$. For any symmetric $N$, [](#prop:stein-rep) and Cauchy–Schwarz give

$$
s\inner{A^{-1/2}KA^{-1/2}}{N}^2
\le \Var\bigl(Y^TNY\bigr)
\le 8\norm N_{\HS}^2,
$$

where the last step is [](#thm:letwin-qcts). Taking the supremum over $\norm N_{\HS}\le1$ proves the first estimate in [](#eq:letwin-whitened-source). Since $K=A^{1/2}(A^{-1/2}KA^{-1/2})A^{1/2}$, the ideal property of the Hilbert–Schmidt norm gives the second estimate. Finally $G=K-(q-p)\delta\delta^T$, so on the coarse balanced window, using $s\ge2/9$, $\abs{q-p}\le1/3$, and $r=s\abs{\delta}^2\le\lmax(A)$ from $B\preceq A$,

$$
s\norm G_{\HS}^2
\le2s\norm K_{\HS}^2+2s(q-p)^2\abs{\delta}^4
\le16\lmax(A)^2+\frac{2(q-p)^2}{s}r^2
\le17\lmax(A)^2.
$$

At balance the correction term vanishes.
:::

:::{prf:proposition} Time-zero equivalence, modulo standard regularization
:label: prop:qcts-equivalence
Up to universal constants, [](#eq:QCTS) is equivalent to the balanced two-color estimate

```{math}
:label: eq:balanced-two-color-static
pq\norm{\Sigma_E-\Sigma_F}_{\HS}^2\le C
```

for all balanced cuts $E$.
:::

:::{prf:proof}
Assume [](#eq:QCTS). For $\norm M_{\HS}=1$,

$$
\inner{\E[gZ]}{M}
=\E\left[g\left(X^TMX-\Tr M\right)\right]
\le \sqrt{\Var(X^TMX)}\le\sqrt C .
$$

Taking the supremum over $M$ and using [](#eq:color-tensor) gives the two-color bound at balance; the slightly unbalanced case is handled by the explicit $(q-p)\delta\delta^T$ term and $B\preceq A$.

Conversely, fix $M$ with $\norm M_{\HS}=1$ and set $Y=X^TMX-\Tr M$. Since $\nu$ is isotropic, its convex support has nonempty interior and $\nu$ is absolutely continuous there. The polynomial $x\mapsto x^TMx$ is nonconstant, because $M\ne0$, and each of its level sets has Lebesgue measure zero. Thus the law of $Y$ is atomless, and there is a median $m$ for which the deterministic cut $E=\{Y\ge m\}$ has mass exactly $1/2$.

For this cut, $g=2\one_E-1=\operatorname{sgn}(Y-m)$ almost surely and $\E g=0$, so

$$
\E[gY]=\E[g(Y-m)]=\E\abs{Y-m}.
$$

The balanced two-color estimate and [](#eq:color-tensor) give $\norm{\E[gZ]}_{\HS}\le\sqrt C$, hence $\E\abs{Y-m}=\inner{\E[gZ]}M\le\sqrt C$. The Carbery–Wright reverse moment inequality for polynomials of degree at most two [@CarberyWright2001] now gives

$$
\sqrt{\Var(Y)}
\le\norm{Y-m}_{L^2}
\lesssim\norm{Y-m}_{L^1}
\lesssim\sqrt C.
$$

Taking the supremum over symmetric $M$ with $\norm M_{\HS}=1$ proves $\Var(X^TMX)\lesssim C\norm M_{\HS}^2$.
:::

## Why ordinary thin shell did not suffice

The thin-shell theorem controls the radial quadratic form:

$$
\Var(\abs X^2)\le Cn,
$$

which is [](#eq:QCTS) only for $M=I/\sqrt n$. Applying thin shell to every projection $P$ gives

$$
\Var(X^TPX)\le C\operatorname{rank}(P).
$$

For a positive semidefinite matrix $M=\int_0^\infty P_s\dd s$, where $P_s=\one_{\{M\ge s\}}$, Minkowski yields

$$
\norm{X^TMX-\Tr M}_{L^2}
\le C\int_0^\infty\sqrt{\operatorname{rank}(P_s)}\dd s.
$$

The right-hand side is the Lorentz $\ell_{2,1}$ norm of the eigenvalue sequence of $M$, bounded by $C\sqrt{\log n}\norm M_{\HS}$. Thus projection thin-shell estimates by themselves give only

```{math}
:label: eq:qcts-log
\Var(X^TMX)\lesssim \log n\,\norm M_{\HS}^2,
```

which matches the former logarithmic scale rather than the dimension-free conclusion of [](#thm:letwin-qcts).

## Projection tests cannot remove the logarithm

The logarithm is not merely an artifact of the integration. There is an abstract positive operator $T$ on symmetric matrices such that

$$
\inner{P}{TP}\le C\operatorname{rank}(P)
$$

for every orthogonal projection $P$, while $\norm T_{\op}\simeq\log n$.

Let

$$
H_n=\sum_{i=1}^n\frac1i,
\qquad
N=\diag\left(\frac1{\sqrt{H_n}},\frac1{\sqrt{2H_n}},\ldots,\frac1{\sqrt{nH_n}}\right),
$$

so that $\norm N_{\HS}=1$, and define

$$
T(M)=H_n\inner{M}{N}N.
$$

Ky Fan's principle gives, for every rank-$r$ projection $P$,

$$
\inner{P}{N}\le\sum_{i=1}^r\frac1{\sqrt{iH_n}}\le2\sqrt{\frac r{H_n}}.
$$

Therefore $\inner{P}{TP}\le4r$, whereas $\norm T_{\op}=H_n\simeq\log n$. This is not a log-concave counterexample. It shows that projection tests alone cannot imply quadratic-chaos thin shell; Letwin's proof escapes the obstruction by using moment measures and a matrix Stein kernel rather than only projection data.

## Static lesson

A proof of KLS through this approach still cannot rely only on radial information or on projection tests. [](#thm:letwin-qcts) supplies the full *intrinsic* quadratic-chaos estimate, but [](#cor:qcts-source) shows exactly what whitening loses: the Euclidean Riccati source may still be amplified by $\lmax(A_t)^2$. The remaining task is therefore dynamic or geometric control of the alignment with $A_t$, attached to the fixed cut $E$.

## The quantified two-tail obstruction and the weight calibration

The following sharpens the qualitative two-tail warning above by tracking the excess of the configuration, not only its covariance contrast. It is the static obstruction consumed in covariance-weighted form by the near-Cheeger variant (Section [](#sec:stein)) and the configuration whose dynamical occupation the all-cut variant must control (Section [](#sec:carleson)).

:::{prf:proposition} Quantified two-tail configuration
:label: prop:two-tail
Let $\Lambda\ge1$, $\nu_\Lambda=N(0,\diag(\Lambda,1,\dots,1))$ on $\R^n$, and

$$
E_\Lambda=\bigl\{x:\abs{x_1}\ge a\sqrt\Lambda\bigr\},
\qquad a=\Phi^{-1}(3/4)\approx0.6745,
$$

so that $\nu_\Lambda(E_\Lambda)=\tfrac12$. Write $\varphi$ for the standard Gaussian density. Then:

(i) $\delta=0$, hence $r=D=0$ and $K=G$;

(ii) $G=8a\varphi(a)\,\Lambda\,e_1e_1^T$, hence $\calS_{\nu_\Lambda}(E_\Lambda)/s=16a^2\varphi(a)^2\Lambda^2\approx0.735\,\Lambda^2$;

(iii) $\nu_\Lambda^+(E_\Lambda)=2\varphi(a)\Lambda^{-1/2}$ and, exactly,

$$
e_0(E_\Lambda)=\bigl(2\varphi(a)-\varphi(0)\bigr)\Lambda^{-1/2}
\approx0.237\,\Lambda^{-1/2}\to0;
$$

(iv) the relative excess is constant uniformly in $\Lambda$ and $n$:

$$
\frac{e_0(E_\Lambda)}{I_{\nu_\Lambda}(1/2)}\ =\ \frac{2\varphi(a)}{\varphi(0)}-1
\ \approx\ 0.593 .
$$

Consequently, no inequality of the slice-wise form $\calS_\nu(E)/s\le C_0+C_1r+\beta D+C_2\,e(E)$, with constants independent of the measure, can hold for all log-concave $\nu$ and all sets of mass $\tfrac12$.
:::

:::{prf:proof}
(i) is symmetry. (ii): conditioning on $\{\abs Z\ge a\}$ for $Z=X_1/\sqrt\Lambda\sim N(0,1)$ affects only the first coordinate, and the Gaussian integrations $\int_a^\infty z^2\varphi=a\varphi(a)+1-\Phi(a)$, $1-\Phi(a)=\tfrac14$, give $\E[Z^2\mid\abs Z\ge a]=1+4a\varphi(a)$ and $\E[Z^2\mid\abs Z<a]=1-4a\varphi(a)$, hence $G_{11}=8a\varphi(a)\Lambda$ with all other entries zero; then $\calS/s=s\norm G_\HS^2=\tfrac14\cdot64a^2\varphi(a)^2\Lambda^2$. (iii): the boundary consists of the two hyperplanes $\{x_1=\pm a\sqrt\Lambda\}$, each of boundary density $\varphi(a)\Lambda^{-1/2}$. To compute the excess, write $\nu_\Lambda=T_\#\gamma_n$ with $\norm T_\op=\sqrt\Lambda$. Gaussian isoperimetry and whitening give $I_{\nu_\Lambda}(1/2)\ge\varphi(0)\Lambda^{-1/2}$, while the long-axis halfspace $\{x_1\le0\}$ attains the reverse inequality. Thus $I_{\nu_\Lambda}(1/2)=\varphi(0)\Lambda^{-1/2}$, proving (iii) and (iv). The final claim follows by letting $\Lambda\to\infty$: the left side grows like $\Lambda^2$, the right side is $C_0+C_2O(\Lambda^{-1/2})$.
:::

:::{prf:remark} Weight calibration and the rate $T^{1+\gamma}$
:label: rem:weight-explains-rate
Three consequences.

*(a) No slice-wise proof.* At $t=0$ the initial measure is isotropic and the configuration of [](#prop:two-tail) cannot occur; but anisotropic posteriors $\mu_t$ with $\lmax(A_t)=\Lambda\gg1$ are exactly the states the dynamics may visit, and there the slice-wise inequality fails. Any proof of the Stein-trace estimate must therefore show that such configurations carry negligible expected occupation — a covariance-occupation statement of the same nature as the Carleson problem itself. Thus the same stress configuration constrains both the excess-propagation and operator-to-trace proposals; no equivalence between them is asserted.

*(b) The weight $(1+\norm A_\op)^{5/2}$ is calibrated, not chosen.* Matching powers of $\Lambda$ ($\calS/s\asymp\Lambda^2$ against $e\asymp\Lambda^{-1/2}$) identifies $(1+\norm{A}_\op)^{5/2}$ as the minimal pure power of $\lmax(A)$ multiplying absolute excess that is statically consistent with this slice inequality: indeed $e_0\Lambda^{5/2}=(2\varphi(a)-\varphi(0))\Lambda^2$, and the ratio of the leading $\calS/s$ coefficient to this coefficient is approximately $3.11$. The uniform value in (iv) of the *relative* excess is consistent evidence: two-tail sets are never relatively near-minimal in the Gaussian model, so a stability theory normalized at the Cheeger scale of the posterior is not contradicted by the example.

*(c) What a $T^{1+\gamma}$ rate would require.* By the Brascamp–Lieb cap [](#eq:BL-cap) the weight is at most $(1+t^{-1})^{5/2}$ pathwise. If that cap were saturated deterministically, the pointwise condition $\E e_t\lesssim t^{5/2+\gamma}$ would be sufficient to produce a $T^{1+\gamma}$ integral; the formerly suggested $t^{3/2}$ rate would instead leave the nonintegrable factor $t^{-1}$. A realistic proof would more likely need a joint rare-event bound coupling excess to large $\norm{A_t}_\op$, rather than separate pointwise estimates. Thus the $T^{1+\gamma}$ term in [](#eq:intro-weighted-excess) is a deliberately strong requirement, not a consequence of the static power matching in part (b).
:::

(subsec:qcts-barriers)=
## What this section argues against

The two remarks below name the proof shapes the computations of this section argue against. Each records what a proof should not try to do, not a theorem about KLS; later sections cite them as heuristic barriers, never as a step in a proof.

:::{prf:remark} Absolute-scale slice bounds fail
:label: rem:two-tail-slice-bounds
The anisotropic Gaussian two-tail cut of [](#prop:two-tail) rules out a slice-wise stable Stein estimate carrying an absolute-scale excess term. On that cut $r=D=0$ while the Stein source is of order $\Lambda^{2}$ and the excess of order $\Lambda^{-1/2}$, so a slice-wise excess estimate needs covariance weight at least $(1+\norm{A}_{\op})^{5/2}$. An unweighted proof must instead control the expected occupation of inflated configurations.
:::

:::{prf:remark} Projection tests lose a logarithm
:label: rem:projection-ceiling
Radial and projection-only information yields at best $\Var(X^{T}MX)\lesssim\log n\,\norm{M}_{\HS}^{2}$, by [](#eq:qcts-log) and the adjacent operator construction. A proof requiring dimension-free quadratic-chaos control must therefore use tensor-aware information beyond projection tests.
:::
