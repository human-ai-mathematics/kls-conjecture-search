---
numbering:
  enumerator: "3.%s"
---

(sec:family-bochner)=
# Family 3: Bochner, heat flow, and the $H^{-1}$ calculus

**Object followed.** The first eigenspace of the diffusion generator, and the energy of derivatives of test functions, measured in the negative Sobolev norm attached to that generator.

**What it buys.** Two things that no other family supplies. First, the conversion device: an inequality that turns “curvature $t$ plus covariance $\norm{\Cov\mu}_\op$” into a spectral gap, sharper than Bakry–Émery. This is the box marked *Improved Lichnerowicz* in Figure [](#fig:kls-architecture) and it is the reason short-time localization is usable at all. Second, a calculus in which coordinate functions and quadratic functions have computable spectral mass, which is what makes the moment-map input of Section [](#sec:family-moment-map) consumable.

(subsec:improved-lichnerowicz)=
## The improved Lichnerowicz inequality

Let $\mu=e^{-U}\dd x$ with $\Hess U\succeq tI$. Bakry–Émery, equivalently Brascamp–Lieb, gives $\CP(\mu)\le1/t$. Klartag's sharper geometric-mean estimate is the following [@Klartag2023Logarithmic].

:::{prf:theorem} Improved Lichnerowicz; Klartag
:label: thm:improved-lichnerowicz
Let $\mu=e^{-U}\dd x$ be a probability measure on $\R^n$ with $\Hess U\succeq tI$ for some $t>0$. Then

```{math}
:label: eq:improved-lichnerowicz
\CP(\mu)\le\sqrt{\frac{\norm{\Cov\mu}_\op}{t}} .
```
:::

This is Klartag's theorem, quoted from [@Klartag2023Logarithmic]; the argument is short enough to record, because the shape of it explains where each factor in the bridge [](#eq:kls-bridge) comes from.

:::{prf:proof} Sketch, following {[@Klartag2023Logarithmic]}
Let $-Lf=\lambda f$ with $f$ a normalized first nonconstant eigenfunction, so that $\int|\nabla f|^2\dd\mu=\lambda$ and $\lambda=\CP(\mu)^{-1}$. The integrated Bochner formula, combined with the Poincaré inequality applied to each partial derivative of $f$, gives

```{math}
:label: eq:bochner-step
\int\inner{\Hess U\,\nabla f}{\nabla f}\dd\mu
\le\lambda\Bigl|\int\nabla f\dd\mu\Bigr|^2 .
```

Integration by parts bounds the right-hand side by the covariance:

```{math}
:label: eq:ibp-step
\Bigl|\int\nabla f\dd\mu\Bigr|^2\le\lambda^2\norm{\Cov\mu}_\op .
```

Strong convexity bounds the left-hand side from below by $t\int|\nabla f|^2\dd\mu=t\lambda$. Chaining the three gives $t\lambda\le\lambda^3\norm{\Cov\mu}_\op$, that is $\lambda^2\ge t/\norm{\Cov\mu}_\op$, which is [](#eq:improved-lichnerowicz).
:::

Note the two places the argument spends: [](#eq:bochner-step) is where a *gradient* energy is converted into information about $\int\nabla f\dd\mu$, a single vector, and [](#eq:ibp-step) is where that vector is charged to the operator norm of the covariance. Both steps are sharp for the Gaussian; neither knows anything about $f$ beyond its first moments. That is the sense in which this family “averages away” the test function, and it is the source of the limitation recorded at the end of this section.

(subsec:hminus1)=
## The $H^{-1}$ norm and the Barthe–Klartag inequality

Let $L=\Delta-\nabla V\cdot\nabla$ be the reversible generator of $\mu=e^{-V}\dd x$, so that $\CP(\mu)=\lambda_1(-L)^{-1}$. For centered $g$ define

```{math}
:label: eq:hminus1-def
\norm{g}_{H^{-1}(\mu)}^2
=\inner{g}{(-L)^{-1}g}
=\int_0^\infty\inner{e^{sL}g}{g}\dd s
=\int_{\lambda_1}^\infty\frac{\dd\nu_g(\lambda)}\lambda ,
```

where $\nu_g$ is the spectral measure of $g$. The last expression is the useful one: the $H^{-1}$ norm is the spectral mass of $g$ weighted by $1/\lambda$, so it is large exactly when $g$ loads the bottom of the spectrum.

Barthe and Klartag proved that, when the derivatives of $f$ are centered [@BartheKlartag2019SpectralGaps],

```{math}
:label: eq:barthe-klartag
\Var_\mu f\le\sum_i\norm{\partial_if}_{H^{-1}(\mu)}^2 .
```

Applied to $f(x)=|x|^2$, whose derivatives are the coordinate functions up to a factor $2$, this gives

```{math}
:label: eq:bk-radial
\Var(|X|^2)\le4\sum_i\norm{x_i}_{H^{-1}(\mu)}^2 ,
```

so the thin-shell problem becomes a statement about the low spectral mass of *coordinate* functions. This is the entry point through which the moment-map estimates of Section [](#sec:family-moment-map) are consumed.

:::{prf:remark} Why quadratics are special
:label: rem:quadratics-special
The derivatives of a quadratic function are linear. Inequality [](#eq:barthe-klartag) therefore reduces a quadratic test function to $H^{-1}$ norms of *linear* functions, which the Stein kernel controls directly (Section [](#subsec:mm-stein)). For a general $f$ the derivatives $\partial_if$ are arbitrary functions and [](#eq:barthe-klartag) reduces nothing. This one sentence is the quadratic-to-all-functions gap, in its sharpest available form.
:::

(subsec:heat-flow)=
## Heat flow and spectral monotonicity

Smooth the measure by Gaussian convolution, $\mu_s=\mu*\gamma_s$, and define the conditional expectation operator

```{math}
:label: eq:Qs-def
Q_sf(y)=\frac{P_s(f\rho)(y)}{P_s\rho(y)}=\E\bigl[f(X)\mid X+\sqrt sG=y\bigr],
```

with $\rho$ the density of $\mu$ and $P_s$ the heat semigroup. The operator $Q_s$ is the deterministic, time-reversed counterpart of stochastic localization; concretely,

```{math}
:label: eq:Qs-localization-dictionary
\sum_i\norm{Q_sx_i}_{L^2(\mu_s)}^2=\E|a_{1/s}|^2,
\qquad
\frac{\dd}{\dd t}\E|a_t|^2=\E\Tr(A_t^2),
```

the second identity being [](#eq:sl-centroid-sde) in expectation. So the two families are two readings of the same object.

Klartag and Putterman proved that the Rayleigh quotient of $Q_sg$ decreases under the heat flow [@KlartagPutterman2021SpectralMonotonicity]; consequently low-frequency modes cannot disappear too fast,

```{math}
:label: eq:spectral-monotonicity
\norm{Q_sg}_2^2\ge e^{-sE(g)}\norm{g}_2^2 ,
```

with $E(g)$ the Rayleigh quotient of $g$. This converts covariance estimates into bounds on the low spectral mass of coordinate functions; integrating that mass against $1/\lambda$ as in [](#eq:hminus1-def) is how Klartag–Lehec obtained their polylogarithmic thin-shell and KLS bounds [@KlartagLehec2022Polylog].

:::{prf:remark} An unresolved operator comparison
:label: q:literature-PsQs
Klartag–Lehec prove Rayleigh-quotient and spectral-trace inequalities related to, but weaker than, the operator inequality

$$
P_sQ_s\succeq e^{sL} .
$$

A suitable strengthening would remove some of the spectral-projection losses in their argument. This is a question from the literature [@KlartagLehec2022Polylog], recorded here for orientation.
:::

**The precise missing estimate.** Uniform control of $\norm{\partial_if}_{H^{-1}}$ for the derivatives of an *arbitrary* test function, rather than for coordinates and for derivatives of quadratics.

**Why it stalls.** Every step above is an averaging step. Bochner in [](#eq:bochner-step) keeps only $\int\nabla f\dd\mu$; [](#eq:barthe-klartag) keeps only the spectral masses of the $\partial_if$; [](#eq:spectral-monotonicity) is a statement about a single Rayleigh quotient. Trace, coordinate, or averaged spectral information does not bound every slow mode, and a near-extremizing eigenfunction of a general log-concave measure is exactly the object about which these averages say least.

**Where this family enters the four approaches.** Approach S (Section [](#sec:spectral-route)) is exactly the attempt to keep the eigenfunction itself in the argument rather than averaging it away, and it is the approach this family points at most directly: it carries the first spectral mode through localization instead of replacing it by a spectral mass. The $H^{-1}$ endpoint audited in Section [](#subsec:spectral-h-minus-one) is where the two meet.
