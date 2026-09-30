---
numbering:
  enumerator: "45.%s"
---

(sec:conditional-fiber-frame)=
# Approach F: inverse-variance conditional-fiber frames

## Overview of the approach

**The idea.** Replace Euclidean directions by one isotropic frame of conditional line resamplings, chosen from the measure but not from the test function, and normalized by the conditional variances; then ask for a dimension-free spectral gap of the resulting form.

**The link to KLS.** A *sufficient condition*, and the diagram must be read as such:

$$
\text{conditional-fiber frame gap}
\ \xRightarrow[\ \text{sufficient, not equivalent}\ ]{}\
\text{KLS},
$$

where the left-hand side is [](#q:conditional-fiber-frame) and the arrow is [](#eq:conditional-fiber-gradient-comparison). The normalization is designed so that linear functions carry exactly the Euclidean energy, while the sharp one-dimensional log-concave Poincaré inequality bounds the form above by the usual gradient form. A counterexample to the frame question would therefore say nothing about KLS. This matters here more than for the other approaches, because the sharpest result of this one is negative ([](#prop:conditional-fiber-root-obstruction)).

**What it builds on.** The sharp one-dimensional log-concave Poincaré inequality, from the literature. Set up here: [](#lem:conditional-fiber-form), that the inverse-conditional-variance line-resampling form is densely defined and closable, which is what makes the question well posed at all.

**What it gives.** A precise question and one rigorous negative result. The frame formalism is set up with its isotropy constraint [](#eq:conditional-frame-isotropy) and its form [](#eq:conditional-fiber-form), and the most natural choice — the $A_{m-1}$ root frame on the isotropic uniform simplex — fails: by [](#prop:conditional-fiber-root-obstruction) its form gap is $O(m^{-2})$. Knowing which frame does not work, and why, is what turned this from a slogan into a question with a stated domain.

**What blocks it.** [](#q:conditional-fiber-frame): exhibit, for every isotropic log-concave $\mu$, one even test-independent admissible frame with a universal lower form gap on the maximal closed form domain — or decide the all-frame simplex dual against it.

**What fails, and why.** [](#prop:conditional-fiber-root-obstruction) rules out the root frame outright: a vertex-cap indicator drives the normalized Rayleigh quotient down. The dual attack is narrowed by [](#lem:fiber-root-degree-two): its exact degree-two floor excludes every degree-two dual certificate, so a certificate must have degree at least three. [](#prop:sasada-negative-exchange) is the same vertex-cap mechanism for a related negative-exponent exchange model, from the literature.

**What would settle it.** A universal form gap for a constructed frame would complete the approach. In the other direction, a counterexample on the simplex needs, by [](#lem:fiber-root-degree-two), an all-frame dual certificate of polynomial degree at least three whose objective tends to zero; none is known.

% Agent note: this is the objective of ap:f-simplex-dual in research/program/portfolio.yaml.

**How to read it.** Self-contained: this approach uses none of Appendices [](#sec:notation)–[](#sec:models) and no moment-map machinery. The one external dependency is the sharp one-dimensional Poincaré inequality. Read Section [](#subsec:fiber-root-failure) for the root-frame obstruction, which is the shortest complete argument in Part IV.

This approach asks whether one can choose a single isotropic frame of directions, depending on the measure but not on the test function, so that normalized conditional line resampling has a dimension-free spectral gap. It gives a sufficient condition rather than a reformulation of KLS. Its normalization is designed so that linear functions have exactly the Euclidean energy, while the sharp one-dimensional log-concave Poincaré inequality compares the form from above with the usual gradient form.

Let $\mu$ be a full-dimensional probability on $\R^d$ with finite second moment. For $\theta\in S^{d-1}$, disintegrate along the affine lines parallel to $\theta$:

$$
\int h(x)\dd\mu(x)
=\int_{\theta^\perp}\int_\R h(z+t\theta)
\dd\mu_{\theta,z}(t)\dd\bar\mu_\theta(z).
$$

Write $\sigma_{\theta,z}^2=\Var_{\mu_{\theta,z}}(T)$. An *admissible frame* is an even Borel probability $\rho$ on $S^{d-1}$ satisfying

```{math}
:label: eq:conditional-frame-isotropy
d\int_{S^{d-1}}\theta\theta^T\dd\rho(\theta)=I_d.
```

For such a frame define

```{math}
:label: eq:conditional-fiber-form
\mathcal D_{\mu,\rho}(f)
:=d\int_{S^{d-1}}\int_{\theta^\perp}
\frac{\Var_{\mu_{\theta,z}}(f(z+T\theta))}
{\Var_{\mu_{\theta,z}}(T)}
\dd\bar\mu_\theta(z)\dd\rho(\theta).
```

Null fibers and fibers with zero denominator contribute zero. The maximal form domain is $\{f\in L^2(\mu):\mathcal D_{\mu,\rho}(f)<\infty\}$, using jointly measurable conditional versions.

:::{prf:lemma} Conditional-fiber form and factor-$4$ bridge
:label: lem:conditional-fiber-form
For a full-dimensional probability with density and finite second moment, and an admissible frame, the quadratic form [](#eq:conditional-fiber-form) is densely defined, closed, symmetric, Markovian, and reversible. Its nonlocal self-adjoint generator is understood in form sense, and agrees with the conditional pair-jump formula on the natural sufficient Bochner domain even when pointwise total jump rates are infinite.

If $\mu$ is log-concave, then for every locally Lipschitz $f$ in the form domain,

```{math}
:label: eq:conditional-fiber-gradient-comparison
\mathcal D_{\mu,\rho}(f)
\le4\int\abs{\nabla f}^2\dd\mu.
```

Consequently, a form gap $\Var_\mu(f)\le C\mathcal D_{\mu,\rho}(f)$ implies $C_P(\mu)\le4C$. For every linear test $f_a(x)=a\cdot x$, one has $\mathcal D_{\mu,\rho}(f_a)=\abs{a}^2$; hence linear tests have quotient one when $\mu$ is isotropic. Every admissible frame has form gap one for the standard Gaussian, and the coordinate frame has form gap one for a standardized product law.
:::

:::{prf:conjecture} Conditional-fiber frame
:label: q:conditional-fiber-frame
There is a universal constant $C$ such that every full-dimensional isotropic log-concave $\mu$ on $\R^d$, in every dimension $d$, admits an admissible frame $\rho_\mu$, chosen independently of $f$, with

```{math}
:label: eq:conditional-fiber-gap
\Var_\mu(f)\le C\mathcal D_{\mu,\rho_\mu}(f)
```

for every $f$ in the maximal closed form domain.
:::

[](#q:conditional-fiber-frame) implies KLS, with $\CP\le4C$, by [](#lem:conditional-fiber-form) ([](#eq:conditional-fiber-gradient-comparison)). The order of quantifiers is essential: $\rho_\mu$ may depend on $\mu$, but it must be fixed before the test $f$ is chosen.

(subsec:fiber-root-failure)=
## Why the simplex root frame fails

Let $P$ be uniform on the simplex $\Delta_{m-1}$, put $H_0=\mathbf1^\perp$ and

$$
X=\sqrt{m(m+1)}\left(P-\frac1m\mathbf1\right)\in H_0.
$$

Then $X$ is isotropic in dimension $d=m-1$. The even $A_{m-1}$ root frame is

$$
\theta_{ij}=\frac{e_i-e_j}{\sqrt2},
\qquad
\rho_{\rm root}=\frac1{m(m-1)}\sum_{i\ne j}\delta_{\theta_{ij}}.
$$

It satisfies $d\int\theta\theta^T\dd\rho_{\rm root}=I_{H_0}$. If $\Var_{ij}$ denotes conditional variance under redistribution of $(P_i,P_j)$ with their sum fixed, then

```{math}
:label: eq:conditional-root-form
\mathcal D_{\rm root}(f)
=\frac{12}{m^2(m+1)}\sum_{i<j}
\E\frac{\Var_{ij}(f)}{(P_i+P_j)^2}.
```

:::{prf:proposition} Vertex-cap obstruction for the root frame
:label: prop:conditional-fiber-root-obstruction
For $m\ge2$ and $\varepsilon\in(0,1)$, let $\eta_i=mP_i$ and $A_{m,\varepsilon}=\{\eta_1>m-\varepsilon\}$. Then

$$
p_{m,\varepsilon}:=\mu(A_{m,\varepsilon})
=\left(\frac\varepsilon m\right)^{m-1},
$$

and the centered cap indicator belongs to the maximal root-form domain and satisfies

```{math}
:label: eq:conditional-root-cap
\frac{\mathcal D_{\rm root}(\one_{A_{m,\varepsilon}})}
{\Var(\one_{A_{m,\varepsilon}})}
\le
\frac{12(m-1)}{(m+1)(m-\varepsilon)^2
\left(1-(\varepsilon/m)^{m-1}\right)}.
```

Consequently $\operatorname{gap}(\mathcal D_{\rm root})=O(m^{-2})$.
:::

The vertex-cap failure is an $L^2$ phenomenon and does not descend to fixed polynomial degree. At polynomial degree two the root-frame pencil can be computed exactly.

:::{prf:lemma} Root-frame degree-two pencil identity
:label: lem:fiber-root-degree-two
For every $m\ge3$, on the degree-$\le2$ quotient $V_{m,2}$ of $L^2$ of the isotropic uniform simplex modulo constants, the $A_{m-1}$ root-frame pair form $K(f,f)=\tfrac{12}{m^2(m+1)}\sum_{i<j}\E\bigl[\Var_{ij}(f)/(P_i+P_j)^2\bigr]$ and $G=\Var$ satisfy

$$
\lambda_{\min}(K,G)=\frac{(m+2)(m+3)}{5m^2},
$$

attained exactly on the radial line $\R\,[\abs X^2-(m-1)]$. Consequently, granting the identification of $K$ with the conditional-fiber root pencil [](#eq:conditional-root-form), every degree-two dual certificate in the all-frame min–max framework has objective at least $(m+2)(m+3)/(5m^2)>1/5$: no sequence of degree-two dual certificates has objective tending to zero, any such fixed-degree polynomial sequence requires degree at least three, and $\Lambda_{m,2}\ge(m+2)(m+3)/(5m^2)$. No upper bound on $\Lambda_{m,2}$, no degree-three statement, and no claim about the full $L^2$ gap (where the vertex-cap obstruction stands) is asserted.
:::

The same failure mechanism has published prior art in negative-rate energy-exchange models.

:::{prf:proposition} Negative-rate simplex exchange obstruction, imported
:label: prop:sasada-negative-exchange
For a symmetric-Dirichlet law of shape $a>0$, a complete-graph heat-bath form with pair rate $(\eta_i+\eta_j)^s$ and $s<0$ has spectral gap at most $2^{-s}m^s$ in the exchange normalization. In particular, at $a=1$ and $s=-2$, the corresponding $A_{m-1}$ root conditional-fiber form has gap at most

$$
\frac{48}{m(m+1)}.
$$
:::

This is a published consequence of Sasada's vertex-cap argument [@Sasada2015EnergyExchange]. Caputo proves a dimension-free gap for the unweighted flat simplex heat bath, while Carlen–Posta–Tóth prove uniform gaps for nonnegative exponents $s\in[0,1]$ [@Caputo2008BinaryCollision; @CarlenPostaToth2025Exchange]. The inverse-variance root form lies at $s=-2$, outside those positive results.

The root calculation does *not* refute [](#q:conditional-fiber-frame). A general permutation-invariant admissible frame may mix continuously many direction orbits, and no proof shows that the root orbit is optimal. The decisive simplex alternative is an exact all-frame dual certificate with objective tending to zero, or a uniform lower bound after optimizing over all admissible frames. Floating-point computations over finitely many frames, and tests restricted to the root frame, decide neither alternative.
