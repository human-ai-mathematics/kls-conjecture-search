---
title: 'Solution: conditional-fiber form structure and the simplex root obstruction'
label: sec:sol-conditional-fiber-frame-structure
ledger-node:
- lem:conditional-fiber-form
- prop:conditional-fiber-root-obstruction
numbering:
  enumerator: D1.%s
---

*Part of the conditional-fiber mechanism, Chapter [](#sec:conditional-fiber-frame); the reading order is on the [full proofs](#sec:proofs-fibers) page.*

**Overview.** This dossier proves [](#lem:conditional-fiber-form) and [](#prop:conditional-fiber-root-obstruction). For an even tight frame $\rho$ it builds the conditional-fiber quadratic form $\mathcal D_{\mu,\rho}$ from line disintegrations of $\mu$, shows it is a closed Markovian Dirichlet form with an explicit generator on a sufficient domain, compares it with the Dirichlet energy with factor $4$ when $\mu$ is log-concave, and calibrates it on linear, Gaussian and product examples. Separately, it shows that the even root frame on the uniform simplex has form gap at most $12/m^2$, so this particular frame cannot give a dimension-free gap.

1. Joint measurability and independence of representatives for the fiber data [](#eq:sol-fiber-disintegration), via orthogonal Fubini [](#eq:sol-fiber-radon).
2. Pair-jump representation [](#eq:sol-fiber-pair-jump) and the factorization [](#eq:sol-fiber-operator-factorization), giving closedness, density (via Lipschitz functions), the Markov property and reversibility.
3. On the sufficient Bochner domain [](#eq:sol-fiber-bochner-domain), the generator formula [](#eq:sol-fiber-generator) and its pointwise resampling form [](#eq:sol-fiber-pointwise-generator).
4. The one-dimensional estimate from [](#thm:cmh-1d), applied on each fiber and averaged with the frame identity [](#eq:sol-fiber-tight-frame), gives [](#eq:sol-fiber-gradient-comparison). Hence a form gap $1/C$ implies $C_P\le4C$.
5. Calibration: linear functions satisfy [](#eq:sol-fiber-linear). Wiener chaos gives gap one for the Gaussian, and Efron–Stein gives gap one for products in the coordinate frame.
6. For the simplex, Dirichlet neutrality gives the root-form formula [](#eq:sol-fiber-root-form). Vertex-cap indicators have finite energy and Rayleigh quotient [](#eq:sol-fiber-cap-rayleigh), which yields [](#eq:sol-fiber-root-gap). This refutes only the root frame on the simplex. It does not refute [](#conj:conditional-fiber-frame) or KLS.

**Scope and refined statement.** We work in a $d$-dimensional Euclidean space, identified with $\R^d$ when coordinates are needed. Let $\mu$ be a full-dimensional probability with a Borel density $r$ and finite second moment. Let $\rho$ be an even Borel probability on $S^{d-1}$ satisfying

```{math}
:label: eq:sol-fiber-tight-frame
d\int_{S^{d-1}}\theta\theta^T\dd\rho(\theta)=I_d.
```

The finite-moment hypothesis is automatic in the isotropic log-concave application. It is included explicitly because the normalization uses conditional second moments and because the linear calibration is an $L^2$ statement.

For $\theta\in S^{d-1}$, write $\pi_\theta=P_{\theta^\perp}$ and set, on the incidence bundle $\mathcal I_d=\{(\theta,z):z\in\theta^\perp\}$,

```{math}
:label: eq:sol-fiber-Z
Z_\theta(z)=\int_\R r(z+t\theta)\dd t,
\qquad
\dd\bar\mu_\theta(z)=Z_\theta(z)\dd z.
```

On the set of fibers for which $0<Z_\theta(z)<\infty$ and the first two $t$-moments are finite, define

```{math}
:label: eq:sol-fiber-disintegration
\dd\mu_{\theta,z}(t)=\frac{r(z+t\theta)}{Z_\theta(z)}\dd t,
\quad
m_\theta(z)=\int t\dd\mu_{\theta,z}(t),
\quad
\sigma_\theta^2(z)=\int(t-m_\theta(z))^2\dd\mu_{\theta,z}(t).
```

On every remaining fiber use the fixed fallback $\delta_0$ and put $m_\theta(z)=\sigma_\theta^2(z)=0$. A zero or nonfinite conditional variance is assigned weight zero. Thus

```{math}
:label: eq:sol-fiber-weight
w_\theta(z+t\theta)
=\begin{cases}
\sigma_\theta(z)^{-2},&0<\sigma_\theta^2(z)<\infty,\\
0,&\text{otherwise}.
\end{cases}
```

For $f\in L^2(\mu)$ define the extended quadratic form

```{math}
:label: eq:sol-fiber-form
\mathcal D_{\mu,\rho}[f]
=d\int_{S^{d-1}}\int_{\theta^\perp}
\frac{\Var_{\mu_{\theta,z}}(f(z+T\theta))}
{\sigma_\theta^2(z)}
\dd\bar\mu_\theta(z)\dd\rho(\theta),
```

with the same zero convention, and take the maximal domain

```{math}
:label: eq:sol-fiber-max-domain
\Dom(\mathcal D_{\mu,\rho})
=\{f\in L^2(\mu):\mathcal D_{\mu,\rho}[f]<\infty\}.
```

:::{prf:theorem} Conditional-fiber form and factor-$4$ bridge
:label: thm:sol-conditional-fiber-form
The definitions above have jointly measurable versions in $(\theta,z)$ and depend only on the $L^2(\mu)$ class of $f$. The form [](#eq:sol-fiber-form) on [](#eq:sol-fiber-max-domain) is densely defined, closed, symmetric, Markovian, conservative, and reversible. Its associated nonnegative self-adjoint operator is denoted $A_{\mu,\rho}$, and its negative Markov generator by $\mathcal L_{\mu,\rho}=-A_{\mu,\rho}$.

Let $P_\theta f=\E[f\mid\pi_\theta X]$. On the sufficient Bochner domain consisting of all $f\in\Dom(\mathcal D_{\mu,\rho})$ such that

```{math}
:label: eq:sol-fiber-bochner-domain
h_\theta:=w_\theta(I-P_\theta)f\in L^2(\mu)
\quad\text{for $\rho$-almost every $\theta$},
\qquad
\int\|h_\theta\|_{L^2(\mu)}\dd\rho(\theta)<\infty,
```

and such that $\theta\mapsto h_\theta$ is strongly measurable, one has

```{math}
:label: eq:sol-fiber-generator
A_{\mu,\rho}f=d\int h_\theta\dd\rho(\theta),
\qquad
\mathcal L_{\mu,\rho}f
=d\int w_\theta(P_\theta f-f)\dd\rho(\theta)
```

as Bochner integrals in $L^2(\mu)$ and, for the jointly measurable versions, pointwise $\mu$-almost everywhere. This formula is asserted on the sufficient domain [](#eq:sol-fiber-bochner-domain); no finite pointwise total jump rate is required.

If $\mu$ is log-concave, then every locally Lipschitz $f\in L^2(\mu)$ satisfies, with the usual extended-value interpretation on the right,

```{math}
:label: eq:sol-fiber-gradient-comparison
\mathcal D_{\mu,\rho}[f]
\le 4\int|\nabla f|^2\dd\mu.
```

Consequently, if $\Var_\mu(f)\le C\mathcal D_{\mu,\rho}[f]$ on the maximal form domain, then $C_P(\mu)\le4C$.

For every $a\in\R^d$ the linear function $f_a(x)=a\cdot x$ has

```{math}
:label: eq:sol-fiber-linear
\mathcal D_{\mu,\rho}[f_a]=|a|^2.
```

Thus its form Rayleigh quotient is one when $\mu$ is isotropic. For the standard Gaussian, every admissible frame has form gap exactly one. For a product of centered variance-one density factors, the coordinate frame has form gap exactly one.
:::

:::{prf:proof}
We prove the measure-theoretic, form, comparison, and calibration assertions in turn.

*Canonical disintegration and joint measurability.* The incidence bundle $\mathcal I_d$ is Borel. Cover the sphere by countably many Borel charts on each of which measurable Gram–Schmidt gives a Borel orthonormal frame of $\theta^\perp$. Pushing Lebesgue measure on $\R^{d-1}$ through this frame gives the Borel kernel $\theta\mapsto\mathcal H^{d-1}\!\restriction\theta^\perp$. The map $(\theta,z,t)\mapsto z+t\theta$ is Borel, so parameterized Tonelli shows that $Z_\theta(z)$ and every truncated moment numerator in [](#eq:sol-fiber-disintegration) are jointly Borel. Passing monotonically through the truncations, dividing on the good set, and using the fixed fallback elsewhere gives the claimed jointly Borel versions.

This construction is also independent of the Borel density representative. If $r$ and $\widetilde r$ agree Lebesgue-almost everywhere, orthogonal Fubini applied to their disagreement set shows, for every fixed $\theta$, that their fiber data agree for $\bar\mu_\theta$-almost every $z$; integrating in $\rho$ leaves the form unchanged.

For each fixed $\theta$, orthogonal Fubini gives

```{math}
:label: eq:sol-fiber-radon
\int h\dd\mu
=\int_{\theta^\perp}\int_\R h(z+t\theta)
\dd\mu_{\theta,z}(t)\dd\bar\mu_\theta(z).
```

The exceptional fibers have $\bar\mu_\theta$-measure zero: integrability of $Z_\theta$ follows from $\int Z_\theta\dd z=1$, and integrability of the conditional second-moment numerator follows from

$$
\int_{\theta^\perp}\int_\R t^2r(z+t\theta)\dd t\dd z
=\int (x\cdot\theta)^2\dd\mu(x)<\infty.
$$

On a good fiber, whenever $0<Z_\theta(z)<\infty$, the conditional law has a Lebesgue density and hence cannot be a point mass; its variance is therefore positive. The zero-variance convention is nevertheless retained so that the formula is version-safe on all fibers.

For a Borel representative of $f\in L^2(\mu)$, the same parameterized integration applied first to bounded truncations gives a jointly measurable version of

```{math}
:label: eq:sol-fiber-P
(P_\theta f)(z+t\theta)
=\int_\R f(z+s\theta)\dd\mu_{\theta,z}(s).
```

If two representatives agree $\mu$-almost everywhere, applying [](#eq:sol-fiber-radon) to the indicator of their disagreement shows, for every fixed $\theta$, that their fiber restrictions agree for $\bar\mu_\theta$-almost every $z$. Integration in $\rho$ then proves that [](#eq:sol-fiber-form) is independent of the chosen representative.

*Pair-jump representation, closedness, and the Markov property.* Polarization of [](#eq:sol-fiber-form) gives, for $f,g$ in the maximal domain,

```{math}
:label: eq:sol-fiber-pair-jump
\begin{aligned}
\mathcal D_{\mu,\rho}(f,g)
=\frac d2\int_{S^{d-1}}\int_{\theta^\perp}
&\frac1{\sigma_\theta^2(z)}
\iint_{\R^2}
\bigl(f(z+s\theta)-f(z+t\theta)\bigr)\\
&\qquad\times
\bigl(g(z+s\theta)-g(z+t\theta)\bigr)
\dd\mu_{\theta,z}(s)\dd\mu_{\theta,z}(t)
\dd\bar\mu_\theta(z)\dd\rho(\theta).
\end{aligned}
```

The integral is absolutely convergent by Cauchy–Schwarz with the two form energies. In particular the jump measure in [](#eq:sol-fiber-pair-jump) is symmetric, which is the explicit reversibility statement.

For a fixed $\theta$, $P_\theta$ is the orthogonal projection in $L^2(\mu)$ onto functions of $\pi_\theta x$. The multiplier $w_\theta$ is measurable with respect to the same sigma-field, so its spectral projections commute with $P_\theta$. Consequently

```{math}
:label: eq:sol-fiber-operator-factorization
\int_{\theta^\perp}
\frac{\Var_{\mu_{\theta,z}}(f)}{\sigma_\theta^2(z)}
\dd\bar\mu_\theta(z)
=\|w_\theta^{1/2}(I-P_\theta)f\|_2^2.
```

The operator $B_\theta=w_\theta^{1/2}(I-P_\theta)$ is closed: if $f_n\to f$ and $B_\theta f_n\to g$ in $L^2(\mu)$, then $(I-P_\theta)f_n\to(I-P_\theta)f$; closedness of the multiplication operator and the preceding commutation give $g=B_\theta f$.

The joint measurability already proved lets us define

$$
Tf(\theta,x)=\sqrt d\,B_\theta f(x)
$$

from $L^2(\mu)$ to $L^2(\rho\otimes\mu)$ on its maximal domain. This direct-integral operator is closed. Indeed, if $f_n\to f$ and $Tf_n\to G$, pass to a subsequence for which $B_\theta f_n\to d^{-1/2}G(\theta,\cdot)$ in $L^2(\mu)$ for $\rho$-almost every $\theta$; fiberwise closedness identifies the limit with $B_\theta f$. Since $\mathcal D_{\mu,\rho}[f]=\|Tf\|_{L^2(\rho\otimes\mu)}^2$, the maximal quadratic form is closed.

It is densely defined without using log-concavity. If $f$ is globally Lipschitz, then on every good fiber, with $T,T'$ independent under $\mu_{\theta,z}$,

```{math}
:label: eq:sol-fiber-lipschitz-density
\Var(f(z+T\theta))
=\frac12\E\bigl(f(z+T\theta)-f(z+T'\theta)\bigr)^2
\le \operatorname{Lip}(f)^2\sigma_\theta^2(z).
```

Thus $C_c^\infty(\R^d)\subset\Dom(\mathcal D_{\mu,\rho})$. Smooth compactly supported functions are dense in $L^2(\mu)$ for every finite Borel measure, so the form is densely defined.

If $\Phi:\R\to\R$ is a normal contraction, the pairwise inequality $|\Phi(u)-\Phi(v)|\le|u-v|$ in [](#eq:sol-fiber-pair-jump) gives $\mathcal D[\Phi\circ f]\le\mathcal D[f]$. Hence the form is Markovian. It is symmetric by construction, and $1\in\Dom(\mathcal D)$ with $\mathcal D(1,g)=0$. The representation theorem for closed Dirichlet forms now supplies $A_{\mu,\rho}$ and its conservative reversible contraction semigroup.

*The sufficient Bochner domain and the generator.* Suppose [](#eq:sol-fiber-bochner-domain) holds. Strong measurability and the norm bound make $h=d\int h_\theta\dd\rho(\theta)$ a well-defined element of $L^2(\mu)$. Since $w_\theta$ is fiber-measurable and $P_\theta(I-P_\theta)=0$, for every $g\in\Dom(\mathcal D)$ one has

```{math}
:label: eq:sol-fiber-generator-pairing
\left\langle w_\theta^{1/2}(I-P_\theta)f,
w_\theta^{1/2}(I-P_\theta)g\right\rangle
=\langle h_\theta,g\rangle.
```

Indeed, truncating the fiber-measurable multiplier $w_\theta$ first gives $P_\theta[w_\theta(I-P_\theta)f]=w_\theta P_\theta(I-P_\theta)f=0$; passage in $L^2$ gives $P_\theta h_\theta=0$ under [](#eq:sol-fiber-bochner-domain), and hence $\langle h_\theta,(I-P_\theta)g\rangle=\langle h_\theta,g\rangle$. The right side is integrable in $\theta$, and therefore $\mathcal D(f,g)=\langle h,g\rangle$. The form characterization of the operator domain gives $f\in\Dom(A_{\mu,\rho})$ and [](#eq:sol-fiber-generator).

Moreover $\int\!\int|h_\theta(x)|\dd\mu(x)\dd\rho(\theta) \le\int\|h_\theta\|_2\dd\rho(\theta)<\infty$. Fubini therefore supplies the pointwise almost-everywhere version. Using [](#eq:sol-fiber-P), its negative is the conditional pair-resampling formula

```{math}
:label: eq:sol-fiber-pointwise-generator
\mathcal L_{\mu,\rho}f(x)
=d\int_{S^{d-1}}w_\theta(x)
\int_\R\bigl(f(\pi_\theta x+s\theta)-f(x)\bigr)
\dd\mu_{\theta,\pi_\theta x}(s)\dd\rho(\theta).
```

The integrability condition concerns the signed update in $L^2$, not the formal total rate $d\int w_\theta(x)\dd\rho(\theta)$, which may be infinite. Outside the sufficient Bochner domain only the closed-form generator is claimed.

*The factor-$4$ comparison.* Assume now that $\mu$ is log-concave. Each good conditional fiber in [](#eq:sol-fiber-disintegration) is a one-dimensional log-concave probability. Translating it by its mean and applying the sharp one-dimensional estimate contained in the certified [](#thm:cmh-1d) gives

```{math}
:label: eq:sol-fiber-one-dimensional
\Var_{\mu_{\theta,z}}(g)
\le4\sigma_\theta^2(z)
\int|g'(t)|^2\dd\mu_{\theta,z}(t).
```

Apply this to $g(t)=f(z+t\theta)$. Orthogonal Fubini, Tonelli, and [](#eq:sol-fiber-tight-frame) yield

```{math}
:label: eq:sol-fiber-tight-comparison-proof
\begin{aligned}
\mathcal D_{\mu,\rho}[f]
&\le4d\int_{S^{d-1}}\int|\partial_\theta f(x)|^2
\dd\mu(x)\dd\rho(\theta)\\
&=4\int\nabla f(x)^T
\left(d\int\theta\theta^T\dd\rho(\theta)\right)
\nabla f(x)\dd\mu(x)
=4\int|\nabla f|^2\dd\mu.
\end{aligned}
```

The fiber inequality applies to locally Lipschitz restrictions; if the final gradient integral is infinite the assertion is automatic. A form-gap inequality followed by [](#eq:sol-fiber-gradient-comparison), first on $C_c^\infty$ and then in the standard Sobolev closure, is exactly the Poincaré inequality with constant $4C$.

*Linear, Gaussian, and product calibrations.* On a good fiber the conditional variance of $a\cdot(z+T\theta)$ is $(a\cdot\theta)^2\sigma_\theta^2(z)$. The exceptional fibers are null, so [](#eq:sol-fiber-tight-frame) gives

$$
\mathcal D_{\mu,\rho}[f_a]
=d\int(a\cdot\theta)^2\dd\rho(\theta)=|a|^2.
$$

If $\mu$ is isotropic, this also equals $\Var_\mu(f_a)$.

For $\mu=\gamma_d$, every conditional line variance is one. Let $Q_\theta=I-\theta\theta^T$. Under the orthogonal Wiener-chaos/Fock identification, conditional expectation $P_\theta$ restricts on the $r$th chaos to the orthogonal projection $Q_\theta^{\otimes r}$ on symmetric $r$-tensors. For $r\ge1$ and such a tensor $u_r$, the range of $Q_\theta^{\otimes r}$ is contained in the range of $Q_\theta\otimes I^{\otimes(r-1)}$. Hence

```{math}
:label: eq:sol-fiber-gaussian-one-leg
\begin{aligned}
\|u_r\|^2-\|Q_\theta^{\otimes r}u_r\|^2
&\ge
\|((\theta\theta^T)\otimes I^{\otimes(r-1)})u_r\|^2.
\end{aligned}
```

Since $(\theta\theta^T)\otimes I^{\otimes(r-1)}$ is an orthogonal projection,

```{math}
:label: eq:sol-fiber-gaussian-frame-average
\begin{aligned}
d\int\|((\theta\theta^T)\otimes I^{\otimes(r-1)})u_r\|^2\dd\rho(\theta)
&=\left\langle u_r,
\left(d\int\theta\theta^T\dd\rho(\theta)\right)
\otimes I^{\otimes(r-1)}u_r\right\rangle
=\|u_r\|^2.
\end{aligned}
```

Summing the orthogonal chaoses and using Tonelli proves $\mathcal D_{\gamma_d,\rho}[f]\ge\Var_{\gamma_d}(f)$ for every $f\in L^2(\gamma_d)$. (Here the form is bounded above by $d\Var(f)$, so its domain is all of $L^2$.) A nonconstant linear function gives equality, proving that the gap is exactly one.

Finally let $\mu=\bigotimes_{i=1}^d\mu_i$, where each $\mu_i$ has a density, mean zero, and variance one, and take

$$
\rho_{\rm coord}=\frac1{2d}\sum_{i=1}^d(\delta_{e_i}+\delta_{-e_i}).
$$

Each coordinate fiber is the fixed law $\mu_i$ and has variance one, so

```{math}
:label: eq:sol-fiber-product-form
\mathcal D_{\mu,\rho_{\rm coord}}[f]
=\sum_{i=1}^d\E\Var\bigl(f(X)\mid X_j,\ j\ne i\bigr).
```

The Efron–Stein inequality bounds $\Var_\mu(f)$ by the right side. Linear functions give equality, and hence the coordinate-frame form gap is exactly one. Log-concavity of the factors is needed only if one also invokes the gradient comparison.
:::

We now prove the separate root-frame obstruction. It is useful to keep its normalization fully explicit because the singular pair rate is the entire mechanism.

:::{prf:proposition} Uniform-simplex root formula and vertex-cap obstruction
:label: prop:sol-conditional-fiber-root-obstruction
Let $m\ge2$, let $P$ be uniform on $\Delta_{m-1}=\{p\in\R_+^m:\sum_i p_i=1\}$, put $H_0=\one^\perp$, $R_m=\sqrt{m(m+1)}$, and

$$
X=R_m\left(P-\frac1m\one\right)\in H_0.
$$

Then $X$ is isotropic in the $(m-1)$-dimensional space $H_0$. For $\theta_{ij}=(e_i-e_j)/\sqrt2$ and

$$
\rho_{\rm root}=\frac1{m(m-1)}\sum_{i\ne j}\delta_{\theta_{ij}},
$$

$\rho_{\rm root}$ is an admissible even frame. If $\Var_{ij}$ denotes conditional variance under uniform redistribution of $(P_i,P_j)$ with their sum and all other coordinates fixed, then

```{math}
:label: eq:sol-fiber-root-form
\mathcal D_{\rm root}[f]
=\frac{12}{m^2(m+1)}\sum_{i<j}
\E\frac{\Var_{ij}(f)}{(P_i+P_j)^2}
=\frac{12}{m+1}\sum_{i<j}
\E\frac{\Var_{ij}(f)}{(\eta_i+\eta_j)^2},
\qquad \eta_i=mP_i.
```

For $\varepsilon\in(0,1)$ set $A_{m,\varepsilon}=\{\eta_1>m-\varepsilon\}$ and $p_{m,\varepsilon}=\P(A_{m,\varepsilon})$. Then

```{math}
:label: eq:sol-fiber-cap-probability
p_{m,\varepsilon}=\left(\frac\varepsilon m\right)^{m-1},
```

the centered cap indicator belongs to the maximal root-form domain, and

```{math}
:label: eq:sol-fiber-cap-rayleigh
\frac{\mathcal D_{\rm root}[\one_{A_{m,\varepsilon}}]}
{\Var(\one_{A_{m,\varepsilon}})}
\le
\frac{12(m-1)}{(m+1)(m-\varepsilon)^2
\left(1-(\varepsilon/m)^{m-1}\right)}.
```

Consequently

```{math}
:label: eq:sol-fiber-root-gap
\operatorname{gap}(\mathcal D_{\rm root})
\le \frac{12(m-1)}{m^2(m+1)}
\le\frac{12}{m^2}.
```
:::

:::{prf:proof}
The Dirichlet covariance formula gives

$$
\Cov(P)=\frac1{m(m+1)}P_{H_0},
$$

so the chosen value of $R_m$ makes $X$ isotropic on $H_0$. Also

$$
\sum_{i<j}(e_i-e_j)(e_i-e_j)^T=mP_{H_0}.
$$

Accounting for both orientations in $\rho_{\rm root}$ shows $(m-1)\int\theta\theta^T\dd\rho_{\rm root}=I_{H_0}$.

Fix $i<j$ and condition on all coordinates other than the pair, equivalently on those coordinates and on $s=P_i+P_j$. Dirichlet neutrality says that $U=P_i/s$ is uniform on $[0,1]$. Along the isotropic root coordinate the conditional chord is uniform on

```{math}
:label: eq:sol-fiber-root-chord
\left[-\frac{R_ms}{\sqrt2},\frac{R_ms}{\sqrt2}\right],
\qquad
\sigma_{ij}^2=\frac{R_m^2s^2}{6}.
```

The two orientations of each unordered pair have total frame mass $2/[m(m-1)]$. Multiplying the reciprocal of [](#eq:sol-fiber-root-chord) by the outer factor $d=m-1$ proves the first identity in [](#eq:sol-fiber-root-form); substituting $P_i+P_j=(\eta_i+\eta_j)/m$ proves the second.

Since $P_1$ has the $\mathrm{Beta}(1,m-1)$ law, [](#eq:sol-fiber-cap-probability) follows by integrating its tail. Pair redistributions not involving coordinate $1$ leave the cap indicator fixed. For a pair $(1,j)$ let $\mathcal F_{1j}$ be the sigma-field held fixed by that redistribution, put $S_{1j}=\eta_1+\eta_j$, and set

$$
q_{1j}=\P(A_{m,\varepsilon}\mid\mathcal F_{1j}).
$$

Then $\Var_{1j}(\one_A)=q_{1j}(1-q_{1j})\le q_{1j}$. The weight $S_{1j}^{-2}$ is $\mathcal F_{1j}$-measurable. Truncate it first and use the tower property, then let the truncation increase. Because $S_{1j}>m-\varepsilon$ on $A_{m,\varepsilon}$, monotone convergence gives

```{math}
:label: eq:sol-fiber-cap-pair-bound
\begin{aligned}
\E\left[S_{1j}^{-2}\Var_{1j}(\one_A)\right]
&\le\E[S_{1j}^{-2}q_{1j}]
=\E[S_{1j}^{-2}\one_A]
\le\frac{p_{m,\varepsilon}}{(m-\varepsilon)^2}.
\end{aligned}
```

Here the expression is assigned value zero on $S_{1j}=0$, consistently with the zero-variance fiber convention. There are $m-1$ contributing pairs. Formula [](#eq:sol-fiber-root-form) and [](#eq:sol-fiber-cap-pair-bound) therefore give

```{math}
:label: eq:sol-fiber-cap-finite-energy
\mathcal D_{\rm root}[\one_A]
\le\frac{12(m-1)}{m+1}
\frac{p_{m,\varepsilon}}{(m-\varepsilon)^2}<\infty.
```

This proves directly that $\one_A-p_{m,\varepsilon}$ lies in the maximal form domain. Dividing [](#eq:sol-fiber-cap-finite-energy) by $\Var(\one_A)=p_{m,\varepsilon}(1-p_{m,\varepsilon})$ proves [](#eq:sol-fiber-cap-rayleigh). Since the spectral gap is bounded above by this quotient for every $\varepsilon\in(0,1)$, letting $\varepsilon\downarrow0$ proves [](#eq:sol-fiber-root-gap). (At $m=2$ the bound is one, which is exactly the gap because the single root update resamples the whole one-dimensional simplex.)
:::

**Fence and conclusion audit.** Neither ledger node has a `bounded_by` edge. The structural theorem uses the proved one-dimensional log-concave estimate in [](#thm:cmh-1d); it has no unresolved premise. The factor-$4$ inequality has the direction $\mathcal D\le4\int|\nabla f|^2$, so a lower spectral gap for one fixed frame is a sufficient condition for KLS, not a consequence of KLS and not an equivalent reformulation.

[](#prop:sol-conditional-fiber-root-obstruction) refutes only the even $A_{m-1}$ root frame on the uniform simplex. It does not address the supremum over all admissible frames, does not show that the root frame is optimal even among permutation-invariant frames, and does not refute [](#conj:conditional-fiber-frame) or KLS. No numerical evidence and no unpublished premise enters either proof.
