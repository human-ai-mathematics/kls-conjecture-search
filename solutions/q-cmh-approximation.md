---
title: 'Solution candidate: constant-preserving CMH approximation closure'
label: sec:sol-cmh-approximation
ledger-node: q:cmh-approximation
numbering:
  enumerator: D27.%s
---

**Overview.** This dossier answers [](#q:cmh-approximation) ([](#thm:sol-cmh-approximation)). Every centered log-concave law, including one carried by a proper affine subspace, is a $\Wtwo$-limit of explicit regular compact-target approximants $\mu_k$ with $\CPaff(\mu)\le\liminf_k\CPaff(\mu_k)\le\liminf_k\CMH(\mu_k)$ ([](#eq:sol-cmh-approx-liminf)). A uniform CMH bound on these approximants ([](#eq:sol-cmh-approx-premise)) therefore gives the affine Poincaré inequality for $\mu$ with the same constant. That uniform bound is an explicit hypothesis: no universal $\mathrm{CMH}(4)$, no KLS and no continuity of $\CMH$ is claimed. Only the Poincaré inequality is passed to the limit, never the Stein kernels.

1. Gaussian smoothing, a quadratic tilt, restriction to a ball and centering give $\mu_k$ with $\Wtwo(\mu_k,\mu)<2/k+\sqrt n/k^2$ ([](#eq:sol-cmh-approx-diagonal-bound)). Their potentials are smooth and strictly convex ([](#eq:sol-cmh-approx-strict-target)).
2. [](#thm:regular-moment-map-compact-target) and Fathi's Stein theorem supply the kernel $H_k$ with $\E_{\mu_k}H_k=\Sigma_k$ ([](#eq:sol-cmh-approx-mean-kernel)). The Stein form on the ambient core is closable with constant kernel ([](#lem:sol-cmh-approx-stein-closure)), so [](#thm:cmh-implies-affine-poincare) gives [](#eq:sol-cmh-approx-regular-endpoint).
3. At a singular limit, the intrinsic covariance form on $S=\operatorname{Ran}\Sigma$ is closable and $\R+C_c^\infty(S)$ is a dense core. It agrees with the ambient core because $\Sigma$ and $\Sigma^+$ annihilate normal derivatives ([](#eq:sol-cmh-approx-normal-annihilation)).
4. Convergence of the covariances, variances and energies on the common core ([](#eq:sol-cmh-approx-covariance-convergence)–[](#eq:sol-cmh-approx-energy-convergence)) with the density of step 3 gives the lower semicontinuity of $\CPaff$. Combined with step 2 this gives [](#eq:sol-cmh-approx-liminf).
5. Any whitening is applied only to individual approximants and undone before the limit, since whitening diverges in collapsing directions ([](#eq:sol-cmh-approx-eigenvalues)).

**Scope.** This dossier answers [](#q:cmh-approximation) with the closed-form convention already used by [](#def:cmh) and [](#thm:cmh-implies-affine-poincare). It constructs regular compact-target approximants of every centered log-concave law, including a law carried by a proper affine subspace, and proves that a uniform CMH estimate on those approximants passes to the affine Poincaré inequality with no loss. The uniform CMH estimate is an explicit hypothesis: nothing below proves universal $\mathrm{CMH}(4)$ or [](#conj:kls), and no continuity of $\CMH$ is asserted.

## 1\. Statement and the limiting closed form

Let $\mu$ be a centered log-concave probability measure on $\R^n$, let $\Sigma=\Cov(\mu)$, and put

$$
S=\operatorname{Ran}\Sigma,
\qquad d=\dim S,
\qquad \Sigma_S=\Sigma|_S.
$$

The affine hull of $\mu$ is $S$. Indeed, if $v\in\ker\Sigma$, then $\Var_\mu\inner{v}{X}=0$ and centeredness gives $\inner{v}{X}=0$ almost surely, so the affine hull is contained in $(\ker\Sigma)^\perp=\operatorname{Ran}\Sigma$. Conversely, the covariance is positive definite on the affine hull: otherwise the support would lie in a proper affine hyperplane of its own affine hull. Thus $\Sigma_S\succ0$ when $d>0$.

For $d>0$, start on the globally Lipschitz functions $f:S\to\R$ that belong to $L^2(\mu)$ with the covariance pre-form

```{math}
:label: eq:sol-cmh-approx-covariance-preform
\calE_{\Sigma,\mu}^{0}(f)
=\int_S\inner{\Sigma_S\nabla_S f}{\nabla_S f}\,\dd\mu.
```

Its closed relaxation in $L^2(\mu)$ is denoted by $\calE_{\Sigma,\mu}$, and its domain by $H^1_\Sigma(\mu)$. This is the intrinsic convention throughout the dossier; no equality with a separately defined maximal distributional or Neumann Sobolev domain is claimed. Section 4 below proves both closability and density of

```{math}
:label: eq:sol-cmh-approx-intrinsic-core
\mathscr C_S=\R+C_c^\infty(S)
```

in this domain. Define

```{math}
:label: eq:sol-cmh-approx-affine-constant
\CPaff(\mu)
=\sup_{f\in H^1_\Sigma(\mu)\setminus\R}
\frac{\Var_\mu f}{\calE_{\Sigma,\mu}(f)}.
```

If $d=0$, then $\mu=\delta_0$; by convention $H^1_\Sigma(\mu)=L^2(\mu)=\R$ and $\CPaff(\mu)=0$.

:::{prf:theorem} Approximation closure for CMH
:label: thm:sol-cmh-approximation
For every centered log-concave probability $\mu$ on $\R^n$ there is an explicit sequence of centered, full-dimensional, compactly supported log-concave probabilities $\mu_k$ such that:

(i) $\Wtwo(\mu_k,\mu)\to0$ in the original ambient coordinates;

(ii) each $\mu_k$ belongs to the regular compact-target moment-map class of [](#thm:regular-moment-map-compact-target), with the closed ambient-core Stein form and constant kernel used in [](#def:cmh);

(iii) writing $\Sigma_k=\Cov(\mu_k)$,

```{math}
:label: eq:sol-cmh-approx-liminf
\CPaff(\mu)
\le \liminf_{k\to\infty}\CPaff(\mu_k)
\le \liminf_{k\to\infty}\CMH(\mu_k).
```

Consequently, if the route premise

```{math}
:label: eq:sol-cmh-approx-premise
\sup_k\CMH(\mu_k)\le C
```

holds for this sequence, then

$$
\Var_\mu f\le C\calE_{\Sigma,\mu}(f)
\quad\text{for every }f\in H^1_\Sigma(\mu),
\qquad\text{and hence}\qquad
\CPaff(\mu)\le C.
$$

This conclusion includes degeneration to a proper affine support and preserves the constant exactly.
:::

## 2\. Construction of regular compact-target approximants

Let $X\sim\mu$ and let $G\sim N(0,I_n)$ be independent. For $\delta>0$ write

$$
\lambda_\delta=\mathcal L(X+\sqrt\delta G),
\qquad
q_\delta=\frac{\dd\lambda_\delta}{\dd x}.
$$

The density $q_\delta$ is positive and $C^\infty$ on $\R^n$. It is log-concave by the Prékopa theorem (equivalently, convolution preserves log-concavity). Moreover

```{math}
:label: eq:sol-cmh-approx-gaussian-smoothing
\Wtwo^2(\lambda_\delta,\mu)\le n\delta,
\qquad
\int x\,\dd\lambda_\delta(x)=0,
\qquad
\Cov(\lambda_\delta)=\Sigma+\delta I_n.
```

For $\delta,\eps>0$ and $R<\infty$, define

```{math}
:label: eq:sol-cmh-approx-family
Z_{\delta,\eps,R}
=\int_{B(0,R)}q_\delta(x)e^{-\eps|x|^2/2}\,\dd x,
\qquad
\dd\widetilde\mu_{\delta,\eps,R}(x)
=Z_{\delta,\eps,R}^{-1}\one_{B(0,R)}(x)
q_\delta(x)e^{-\eps|x|^2/2}\,\dd x.
```

Let $m_{\delta,\eps,R}$ be its mean and center it:

```{math}
:label: eq:sol-cmh-approx-centering
\mu_{\delta,\eps,R}
=(x\mapsto x-m_{\delta,\eps,R})_\#
\widetilde\mu_{\delta,\eps,R}.
```

For fixed $\delta$, as $\eps\downarrow0$ and $R\uparrow\infty$, the density ratio in [](#eq:sol-cmh-approx-family) converges pointwise to one relative to $\lambda_\delta$ and is bounded above by $1/Z_{\delta,\eps,R}$, with $Z_{\delta,\eps,R}\to1$. Dominated convergence therefore gives weak convergence to $\lambda_\delta$ and convergence of the second moment: for the latter, apply it to $|x|^2\one_{B(0,R)}e^{-\eps|x|^2/2}$, dominated by the $\lambda_\delta$-integrable function $|x|^2$. The weak-plus-second-moment characterization of quadratic Wasserstein convergence gives

```{math}
:label: eq:sol-cmh-approx-fixed-delta
\Wtwo(\widetilde\mu_{\delta,\eps,R},\lambda_\delta)\longrightarrow0.
```

Here is an explicit diagonal choice. Set $\delta_k=k^{-4}$. By [](#eq:sol-cmh-approx-fixed-delta), choose

$$
0<\eps_k<k^{-1},
\qquad R_k>k,
\qquad
\Wtwo(\widetilde\mu_{\delta_k,\eps_k,R_k},\lambda_{\delta_k})<k^{-1},
$$

and put $m_k=m_{\delta_k,\eps_k,R_k}$ and $\mu_k=\mu_{\delta_k,\eps_k,R_k}$. Since $\lambda_{\delta_k}$ is centered, comparison of means under any coupling gives

$$
|m_k|
\le \Wtwo(\widetilde\mu_{\delta_k,\eps_k,R_k},\lambda_{\delta_k})<k^{-1}.
$$

Translation by $-m_k$, the triangle inequality, and [](#eq:sol-cmh-approx-gaussian-smoothing) now yield the quantitative diagonal estimate

```{math}
:label: eq:sol-cmh-approx-diagonal-bound
\Wtwo(\mu_k,\mu)
\le |m_k|
+\Wtwo(\widetilde\mu_{\delta_k,\eps_k,R_k},\lambda_{\delta_k})
+\Wtwo(\lambda_{\delta_k},\mu)
<\frac2k+\frac{\sqrt n}{k^2}.
```

No whitening has been used.

We next check every target hypothesis. The support of $\mu_k$ is the convex body

$$
P_k=B(-m_k,R_k),
$$

and, on its interior,

```{math}
:label: eq:sol-cmh-approx-density
\dd\mu_k(z)=g_k(z)\,\dd z,
\qquad
g_k(z)=Z_{\delta_k,\eps_k,R_k}^{-1}
q_{\delta_k}(z+m_k)e^{-\eps_k|z+m_k|^2/2}.
```

The function $g_k$ extends to a positive $C^\infty$ function on all of $\R^n$. The measure is centered by construction and full-dimensional because $g_k>0$ on the nonempty open ball $\operatorname{int}P_k$. In particular, its covariance $\Sigma_k$ is positive definite. Also $0\in\operatorname{int}P_k$: the barycenter of a positive density on a full-dimensional convex body cannot lie on a supporting hyperplane of that body.

Writing $V_k=-\log g_k$ on $\operatorname{int}P_k$, log-concavity of $q_{\delta_k}$ gives

```{math}
:label: eq:sol-cmh-approx-strict-target
D^2V_k(z)
=D^2(-\log q_{\delta_k})(z+m_k)+\eps_k I_n
\succeq \eps_k I_n.
```

Thus $\mu_k$ is log-concave, and its interior potential is smooth and strictly convex. (The additional standard convolution identity gives $D^2(-\log q_{\delta_k})\preceq\delta_k^{-1}I_n$, but no uniform Hessian bound is used.)

The published compact-target regularity theorem [@BermanBerndtsson2013RealMA], in the repository form of [](#thm:regular-moment-map-compact-target), now applies to the centered probability $g_k\one_{\operatorname{int}P_k}\,\dd x$. It supplies a smooth strictly convex canonical moment potential $\varphi_k$ on $\R^n$ and a global diffeomorphism

$$
\nabla\varphi_k:\R^n\longrightarrow\operatorname{int}P_k.
$$

With target coordinate $x=\nabla\varphi_k(y)$, define

```{math}
:label: eq:sol-cmh-approx-kernel
H_k(x)=D^2\varphi_k((\nabla\varphi_k)^{-1}(x)).
```

Fathi's moment-map Stein theorem [@Fathi2019SteinMomentMaps] gives a smooth positive symmetric field on $\operatorname{int}P_k$ satisfying, for every scalar ambient test $F\in C_c^\infty(\R^n)$,

```{math}
:label: eq:sol-cmh-approx-stein
\int x_iF(x)\,\dd\mu_k(x)
=\int (H_k)_{ij}(x)\partial_jF(x)\,\dd\mu_k(x).
```

Equivalently, $\operatorname{Div}_{\mu_k}H_k=-x$ distributionally on the ambient space. The absence of a boundary distribution in [](#eq:sol-cmh-approx-stein) is precisely the weak zero-normal-flux convention used by the certified endpoint. Since $P_k$ is bounded, testing with a cutoff that equals the coordinate function $x_j$ near $P_k$ gives

```{math}
:label: eq:sol-cmh-approx-mean-kernel
\E_{\mu_k}H_k=\E_{\mu_k}[X\otimes X]=\Sigma_k.
```

Thus every hypothesis of the imported regular moment-map input has been matched.

## 3\. The exact closed Stein form on each approximant

For fixed $k$, let

$$
\mathscr D_k
=\{F|_{P_k}:F\in\R+C_c^\infty(\R^n)\}
$$

and define on this ambient restriction core

```{math}
:label: eq:sol-cmh-approx-H-form
\calE_{H_k}^0(f,g)
=\int_{P_k}\inner{H_k\nabla f}{\nabla g}\,\dd\mu_k.
```

The value is independent of the ambient extension, because two smooth extensions agreeing on the open set $\operatorname{int}P_k$ have the same gradient there. The core is dense in $L^2(\mu_k)$, and [](#eq:sol-cmh-approx-mean-kernel) shows that every core function has finite energy:

$$
\calE_{H_k}^0(f,f)
\le\norm{\nabla f}_\infty^2\int\Tr H_k\,\dd\mu_k
=\norm{\nabla f}_\infty^2\Tr\Sigma_k<\infty.
$$

:::{prf:lemma} Closability and constant kernel
:label: lem:sol-cmh-approx-stein-closure
The form [](#eq:sol-cmh-approx-H-form) is closable in $L^2(\mu_k)$. Its closure $\calE_{H_k}$ has kernel exactly the constants. We use its nonnegative self-adjoint form operator $\Aop_k$ as the closed Stein generator $-L_{\mu_k}$.
:::

:::{prf:proof}
Suppose $f_j\in\mathscr D_k$, $f_j\to0$ in $L^2(\mu_k)$, and $H_k^{1/2}\nabla f_j$ converges in $L^2(\mu_k;\R^n)$ to a field $u$. Let $K\Subset\operatorname{int}P_k$. On $K$, the density $g_k$ is bounded above and below by positive constants and the smooth positive matrix fields $H_k^{1/2}$ and $H_k^{-1/2}$ are bounded. Hence

$$
f_j\longrightarrow0\quad\text{in }L^2(K,\dd x),
\qquad
\nabla f_j\longrightarrow H_k^{-1/2}u
\quad\text{in }L^2(K,\dd x).
$$

Distributional differentiation is closed, so $H_k^{-1/2}u=0$ on $K$. Exhausting the interior by compact subsets and using that the boundary of a convex body has Lebesgue, hence $\mu_k$, measure zero gives $u=0$. This is the closability criterion.

If $f$ lies in the closed form domain with $\calE_{H_k}(f,f)=0$, take core approximants $f_j\to f$ in $L^2(\mu_k)$ with $H_k^{1/2}\nabla f_j\to0$. The same local argument shows that $f$ has zero distributional gradient on the connected set $\operatorname{int}P_k$, so $f$ is constant almost everywhere. Constants plainly have zero energy.
:::

The weak Stein identity gives, on smooth tests for which the displayed quantities are integrable,

$$
\operatorname{Div}_{\mu_k}(H_k\nabla g)
=\Tr(H_kD^2g)-x\cdot\nabla g,
\qquad
-\int fL_{\mu_k}g\,\dd\mu_k=\calE_{H_k}^0(f,g).
$$

Thus the Friedrichs form operator in [](#lem:sol-cmh-approx-stein-closure) is exactly the closed-form object used by [](#def:cmh); its inverse is understood only on the orthogonal complement of its constant kernel. We do not identify this domain with an unnamed maximal Neumann or maximal distributional domain.

[](#thm:cmh-implies-affine-poincare) is therefore applicable to every $\mu_k$ and gives

```{math}
:label: eq:sol-cmh-approx-regular-endpoint
\CPaff(\mu_k)\le\CMH(\mu_k).
```

This is the only step at which the CMH quantity is used.

## 4\. The intrinsic domain at a singular limit

A log-concave probability whose affine hull is $S$ has a density with respect to $d$-dimensional Lebesgue measure on $S$; that density is positive and locally bounded above and below on the relative interior of its convex support. Consequently the same local distributional-derivative argument as in [](#lem:sol-cmh-approx-stein-closure), now with the constant positive matrix $\Sigma_S$, proves that the pre-form [](#eq:sol-cmh-approx-covariance-preform) is closable. It also shows that the kernel of its closure consists of the constants, because the relative interior of a convex support is connected.

We now prove the promised core density rather than assume it. It is enough to approximate a globally Lipschitz $f\in L^2(\mu)$ in the form norm.

(1) Let $T_Mf=(-M)\vee f\wedge M$. The Lipschitz chain rule and dominated convergence give $T_Mf\to f$ in $L^2(\mu)$ and $\calE_{\Sigma,\mu}^0(T_Mf-f)\to0$.

(2) For bounded $f$, choose $\chi_R\in C_c^\infty(S)$ equal to one on $B_S(0,R)$, supported in $B_S(0,2R)$, with $|\nabla_S\chi_R|\le c/R$. Then $\chi_Rf\to f$ in $L^2(\mu)$ and in energy. Indeed, the tail part containing $(1-\chi_R)\nabla_Sf$ tends to zero by dominated convergence, while

$$
\int f^2\inner{\Sigma_S\nabla_S\chi_R}{\nabla_S\chi_R}\,\dd\mu
\le \norm{f}_\infty^2\norm{\Sigma_S}_\op c^2R^{-2}\longrightarrow0.
$$

(3) A compactly supported Lipschitz function on the Euclidean space $S$ can be mollified inside $S$. The mollifications converge uniformly in value, their gradients converge Lebesgue-almost everywhere, and their gradients are uniformly bounded by the original Lipschitz constant. Since $\mu$ is absolutely continuous on $S$, dominated convergence gives convergence in both $L^2(\mu)$ and the covariance energy.

The resulting functions belong to $C_c^\infty(S)$, proving that $\mathscr C_S$ is dense in $H^1_\Sigma(\mu)$. When $d=0$, the intrinsic space is the singleton space and this statement reduces to density of the constants.

This intrinsic core is exactly the restriction of the one common ambient core

```{math}
:label: eq:sol-cmh-approx-ambient-core
\mathscr C=\R+C_c^\infty(\R^n).
```

Indeed, an ambient test restricts to an element of $\mathscr C_S$. Conversely, in the orthogonal splitting $x=s+t\in S\oplus S^\perp$, extend $\phi\in C_c^\infty(S)$ by

$$
F(s+t)=\phi(s)\eta(t),
$$

where $\eta\in C_c^\infty(S^\perp)$ equals one near $0$. Then $F\in C_c^\infty(\R^n)$, $F|_S=\phi$, and its normal derivative vanishes on $S$.

More generally, if two ambient extensions agree on $S$, their tangential gradients agree and the difference of their ambient gradients lies in $S^\perp$. With $P_S$ denoting orthogonal projection,

```{math}
:label: eq:sol-cmh-approx-normal-annihilation
\Sigma=P_S\Sigma_SP_S,
\qquad
\Sigma^+=P_S\Sigma_S^{-1}P_S,
\qquad
\Sigma P_{S^\perp}=\Sigma^+P_{S^\perp}=0.
```

Hence ambient restriction and intrinsic evaluation agree in the covariance energy, and both $\Sigma$ and its Moore–Penrose inverse annihilate every normal derivative. This is exactly the affine-tangent convention in [](#def:cmh); no inverse is taken in a collapsing normal direction.

## 5\. Constant-preserving lower semicontinuity

Quadratic Wasserstein convergence in [](#eq:sol-cmh-approx-diagonal-bound) implies weak convergence together with convergence of second moments. Since all measures are centered,

```{math}
:label: eq:sol-cmh-approx-covariance-convergence
\Sigma_k=\int xx^\top\,\dd\mu_k(x)
\longrightarrow
\int xx^\top\,\dd\mu(x)=\Sigma
```

in every matrix norm (apply second-moment uniform integrability to each entry, or use polarization).

Fix one $F\in\mathscr C$. Both $F$ and $F^2$ are bounded and continuous, so

```{math}
:label: eq:sol-cmh-approx-variance-convergence
\Var_{\mu_k}F\longrightarrow\Var_\mu F.
```

For the energies, set $h(x)=\inner{\Sigma\nabla F(x)}{\nabla F(x)}$, a bounded continuous function. Then

```{math}
:label: eq:sol-cmh-approx-energy-convergence
\begin{aligned}
&\left|\int\inner{\Sigma_k\nabla F}{\nabla F}\,\dd\mu_k
-\int\inner{\Sigma\nabla F}{\nabla F}\,\dd\mu\right| \\
&\quad\le
\norm{\Sigma_k-\Sigma}_\op\norm{\nabla F}_\infty^2
+\left|\int h\,\dd\mu_k-\int h\,\dd\mu\right|
\longrightarrow0.
\end{aligned}
```

Let $L=\liminf_k\CPaff(\mu_k)$ and select a subsequence along which the constants converge to $L$. If $L=\infty$ there is nothing to prove. Otherwise, the affine Poincaré inequality on each approximant, followed by [](#eq:sol-cmh-approx-variance-convergence)– [](#eq:sol-cmh-approx-energy-convergence), gives on the common core

$$
\Var_\mu F
\le L\int\inner{\Sigma\nabla F}{\nabla F}\,\dd\mu.
$$

Restricting to $S$ and using the core density proved in Section 4 extends the inequality to every $f\in H^1_\Sigma(\mu)$. Therefore

$$
\CPaff(\mu)\le\liminf_k\CPaff(\mu_k).
$$

Combining this with the pointwise certified endpoint [](#eq:sol-cmh-approx-regular-endpoint) proves [](#eq:sol-cmh-approx-liminf). In particular, [](#eq:sol-cmh-approx-premise) yields $\CPaff(\mu)\le C$ with no change of constant. Notice that the argument passes only the Poincaré/Dirichlet-form inequality. It uses neither convergence of $H_k$ nor lower semicontinuity of $\CMH$.

## 6\. Eigenvalues, whitening, and affine-support collapse

Order covariance eigenvalues decreasingly. If $\lambda_1(\Sigma)\ge\cdots\ge\lambda_d(\Sigma)>0$ are the positive eigenvalues, followed by $n-d$ zeros, then [](#eq:sol-cmh-approx-covariance-convergence) and Weyl's inequality give

```{math}
:label: eq:sol-cmh-approx-eigenvalues
\lambda_i(\Sigma_k)\longrightarrow\lambda_i(\Sigma)>0
\quad(1\le i\le d),
\qquad
\lambda_i(\Sigma_k)\longrightarrow0
\quad(d<i\le n).
```

Every $\Sigma_k$ is positive definite, so each approximant may be whitened by the invertible map $A_k=\Sigma_k^{-1/2}$. Invertible affine covariance of both $\CMH$ and $\CPaff$ allows one to apply the regular endpoint in those isotropic coordinates and then pull its inequality back to $\mu_k$.

When $d<n$, however, [](#eq:sol-cmh-approx-eigenvalues) shows that $A_k$ diverges in the collapsing normal directions. The whitened laws all have covariance $I_n$ and therefore cannot converge in $\Wtwo$ to a law with covariance $\Sigma$ singular. The valid order is:

(1) whiten an individual full-dimensional approximant if desired;

(2) use invertible affine covariance to unwhiten its Poincaré inequality;

(3) take the $\Wtwo$ limit in the original coordinates using [](#eq:sol-cmh-approx-energy-convergence).

No canonical moment-map kernel is pushed through a noninvertible limiting map. At the limit, only the intrinsic covariance form on $S=\operatorname{Ran}\Sigma$ remains, with normal directions removed by [](#eq:sol-cmh-approx-normal-annihilation).

:::{prf:proof} Proof of [](#thm:sol-cmh-approximation)
The construction and the quantitative $\Wtwo$ convergence are proved in Section 2. The published compact-target theorem, the Stein identity, and the exact closed-form convention are verified in Sections 2–3, so the certified regular endpoint applies. Sections 4–5 prove the intrinsic affine-support convention, common-core density, and the constant-preserving liminf inequality. Section 6 verifies that optional whitening is undone before the singular limit. These facts prove all three assertions and the conditional consequence.
:::

**Obstructions respected.** The ledger gives `q:cmh-approximation` no `bounded_by` edge. The argument also does not enter the fixed-cut obstruction regime: it uses no tail split, projection-only test, localization occupation estimate, relative trace upgrade, evolving isoperimetric competitor, or rank-one product-cut assertion. In particular, affine-support collapse is handled at the Poincaré form level rather than by transporting a canonical Stein kernel through a noninvertible map.

**Conditional status and exclusions.** The approximation sequence exists unconditionally, and the closure theorem is analytic. The only unresolved premise in the route implication is [](#eq:sol-cmh-approx-premise). Thus this dossier can at most certify the conditional node “uniform CMH on the constructed regular approximants implies the affine Poincaré inequality for the limit.” CMH is used only as a sufficient condition. No converse, no universal $\mathrm{CMH}(4)$ estimate, and no proof of KLS appears here.
