---
title: 'Solution: affine-Poincaré recovery and one-sequence CMH closure'
label: sec:sol-affine-poincare-w2-liminf
ledger-node:
- lem:affine-poincare-w2-liminf
- cor:cmh-recovery-sequence-suffices
numbering:
  enumerator: D9.%s
---

*Part of the moment-map mechanism, Chapter [](#sec:cmh-normalization); the reading order is on the [full proofs](#sec:proofs-moment-map) page.*

**Overview.** This dossier proves [](#lem:affine-poincare-w2-liminf) and, conditional on the unresolved [](#ass:cmh-recovery-envelope), [](#cor:cmh-recovery-sequence-suffices). It works with the intrinsic covariance form on the affine support, which makes the affine Poincaré constant $\CPaff$ lower semicontinuous along every centered log-concave $W_2$-convergent sequence. Regular compact-target approximants come from smoothing, tilting and truncation, together with the published moment-map theorem [](#thm:regular-moment-map-compact-target). No bound on $\CMH$ and no semicontinuity of $\CMH$ is claimed.

1. [](#lem:sol-cmh-recovery-common-core): the covariance pre-form [](#eq:sol-cmh-recovery-preform) is closable and its kernel is the constants. The class $\R+C_c^\infty$ is a common intrinsic and ambient core, and [](#eq:sol-cmh-recovery-normal-annihilation) makes the energy independent of the extension.
2. [](#thm:sol-affine-poincare-w2-liminf) (i): Gaussian smoothing, Gaussian tilt, ball truncation and recentering [](#eq:sol-cmh-recovery-family) give regular compact-target laws with [](#eq:sol-cmh-recovery-diagonal). [](#thm:regular-moment-map-compact-target) then supplies the kernel [](#eq:sol-cmh-recovery-stein).
3. [](#thm:sol-affine-poincare-w2-liminf) (ii): convergence of covariances, variances and energies on the core, [](#eq:sol-cmh-recovery-variance-convergence) and [](#eq:sol-cmh-recovery-energy-convergence), gives [](#eq:sol-affine-poincare-w2-liminf) by Step 1, including for singular $\Sigma$.
4. For regular laws, the closed Stein form matches [](#def:cmh), so [](#thm:cmh-implies-affine-poincare) gives [](#eq:sol-cmh-recovery-regular-endpoint).
5. [](#cor:sol-cmh-recovery-sequence-suffices): Steps 3–4 applied to the sequence supplied by [](#ass:cmh-recovery-envelope) give $\CPaff\le C$, which is [](#conj:kls). This step is conditional on that assumption.

**Scope and certification boundary.** The first result below proves [](#lem:affine-poincare-w2-liminf). In fact, its lower-semicontinuity assertion is proved along every centered log-concave $W_2$-convergent sequence, while the existence of compact-target regular approximants uses the published moment-map result recorded as [](#thm:regular-moment-map-compact-target). The second result proves [](#cor:cmh-recovery-sequence-suffices) under the unresolved [](#ass:cmh-recovery-envelope). No bound on $\CMH$ is proved, and no convergence or semicontinuity of $\CMH$ is asserted.

## 1\. The covariance form on an affine support

Let $\mu$ be a centered log-concave probability on $\R^n$, set

$$
\Sigma=\Cov(\mu),\qquad S=\operatorname{Ran}\Sigma,\qquad d=\dim S,
$$

and, when $d>0$, write $\Sigma_S=\Sigma|_S$. The affine hull of $\mu$ is the linear space $S$. Indeed, if $v\in\ker\Sigma$, then centeredness and $\Var_\mu\langle v,X\rangle=0$ give $\langle v,X\rangle=0$ almost surely. Conversely, the covariance is positive definite on the linear span of the centered support. Thus $\Sigma_S\succ0$ for $d>0$.

On the globally Lipschitz functions on $S$ that belong to $L^2(\mu)$, consider the pre-form

```{math}
:label: eq:sol-cmh-recovery-preform
\calE^0_{\Sigma,\mu}(f)
=\int_S\inner{\Sigma_S\nabla_S f}{\nabla_S f}\,\dd\mu.
```

We denote its closure by $\calE_{\Sigma,\mu}$, its closed domain by $H^1_\Sigma(\mu)$, and define

```{math}
:label: eq:sol-cmh-recovery-cpaff
\CPaff(\mu)
=\sup_{f\in H^1_\Sigma(\mu)\setminus\R}
\frac{\Var_\mu f}{\calE_{\Sigma,\mu}(f)}.
```

When $d=0$, centeredness gives $\mu=\delta_0$; we set $H^1_\Sigma(\mu)=L^2(\mu)=\R$ and $\CPaff(\mu)=0$.

:::{prf:lemma} Intrinsic and ambient common core
:label: lem:sol-cmh-recovery-common-core
For $d>0$, the pre-form [](#eq:sol-cmh-recovery-preform) is closable, its closed-form kernel consists of the constants, and

$$
\mathscr C_S=\R+C_c^\infty(S)
$$

is a form core. Moreover, $\mathscr C_S$ is exactly the restriction to $S$ of the one ambient class

```{math}
:label: eq:sol-cmh-recovery-ambient-core
\mathscr C=\R+C_c^\infty(\R^n),
```

and the covariance energy of a restriction is independent of its ambient extension.
:::

:::{prf:proof}
A log-concave probability with affine hull $S$ has a density with respect to Lebesgue measure on $S$ which is positive and locally bounded above and below on the relative interior of its convex support. Suppose that $f_j$ is Lipschitz, $f_j\to0$ in $L^2(\mu)$, and $\Sigma_S^{1/2}\nabla_Sf_j\to u$ in $L^2(\mu;S)$. On every compact subset of the relative interior, the density is equivalent to Lebesgue measure and $\Sigma_S^{-1/2}$ is bounded. Hence $f_j\to0$ and $\nabla_Sf_j\to\Sigma_S^{-1/2}u$ in local Lebesgue $L^2$. Closedness of distributional differentiation gives $u=0$. This proves closability. The same local argument applied to a zero-energy element of the closure shows that its distributional gradient vanishes on a connected open convex set, so the element is constant almost everywhere.

It remains to verify the asserted core rather than assume it. Start with a Lipschitz $f\in L^2(\mu)$. The value truncations $T_Mf=(-M)\vee f\wedge M$ converge to $f$ in $L^2$ and in the energy [](#eq:sol-cmh-recovery-preform), by the Lipschitz chain rule and dominated convergence. For bounded $f$, choose $\chi_R\in C_c^\infty(S)$ which equals one on $B_S(0,R)$, is supported in $B_S(0,2R)$, and satisfies $|\nabla_S\chi_R|\le c/R$. Then $\chi_Rf\to f$ in $L^2$, while

$$
\begin{aligned}
\calE^0_{\Sigma,\mu}(\chi_Rf-f)
&\le 2\int_{S\setminus B_S(0,R)}
\inner{\Sigma_S\nabla_Sf}{\nabla_Sf}\,\dd\mu \\
&\quad+\frac{2c^2}{R^2}\norm{f}_\infty^2\norm{\Sigma_S}_\op
\longrightarrow0.
\end{aligned}
$$

Finally, a compactly supported Lipschitz function on the Euclidean space $S$ can be mollified inside $S$. Its mollifications converge in value and gradient almost everywhere, and their gradients are bounded by the original Lipschitz constant. Absolute continuity of $\mu$ on $S$ and dominated convergence give convergence in the form norm. Therefore $\mathscr C_S$ is a core.

An ambient function in $\mathscr C$ plainly restricts to $\mathscr C_S$. Conversely, in the orthogonal splitting $x=s+t\in S\oplus S^\perp$, extend $\phi\in C_c^\infty(S)$ by

$$
F(s+t)=\phi(s)\eta(t),
$$

where $\eta\in C_c^\infty(S^\perp)$ equals one near zero. This is an ambient compactly supported smooth extension. If two ambient extensions agree on $S$, the difference of their gradients on $S$ lies in $S^\perp$. Since

```{math}
:label: eq:sol-cmh-recovery-normal-annihilation
\Sigma=P_S\Sigma_SP_S,
\qquad
\Sigma^+=P_S\Sigma_S^{-1}P_S,
```

both $\Sigma$ and its Moore–Penrose inverse annihilate that normal difference. Thus the ambient covariance energy is exactly the intrinsic energy and is independent of the extension.
:::

## 2\. A regular compact-target recovery sequence

:::{prf:theorem} Affine-Poincaré $W_2$ lower semicontinuity and regular recovery
:label: thm:sol-affine-poincare-w2-liminf
Let $\mu$ be a centered log-concave probability on $\R^n$.

(i) There are centered, full-dimensional, compactly supported log-concave probabilities $\mu_k$ in the regular compact-target moment-map class such that $\Wtwo(\mu_k,\mu)\to0$ in the original ambient coordinates.

(ii) More generally, for every sequence of centered log-concave probabilities $\nu_k$ with $\Wtwo(\nu_k,\mu)\to0$,

```{math}
:label: eq:sol-affine-poincare-w2-liminf
\CPaff(\mu)\le\liminf_{k\to\infty}\CPaff(\nu_k).
```

In particular, the sequence in (i) has the lower-semicontinuity property required by [](#lem:affine-poincare-w2-liminf), including when $\mu$ is carried by a proper affine subspace. The assertion concerns only covariance Dirichlet forms and makes no claim about $\CMH(\mu_k)$ or its limit.
:::

:::{prf:proof}
Let $X\sim\mu$ and let $G\sim N(0,I_n)$ be independent. For $\delta>0$, put

$$
\lambda_\delta=\mathcal L(X+\sqrt\delta G),
\qquad q_\delta=\frac{\dd\lambda_\delta}{\dd x}.
$$

The density $q_\delta$ is positive and smooth, and it is log-concave because convolution preserves log-concavity [@BrascampLieb1976]. The displayed coupling also gives

```{math}
:label: eq:sol-cmh-recovery-smoothing
\Wtwo^2(\lambda_\delta,\mu)\le n\delta,
\qquad \int x\,\dd\lambda_\delta(x)=0,
\qquad \Cov(\lambda_\delta)=\Sigma+\delta I_n.
```

For $\delta,\eps>0$ and $R<\infty$, define

```{math}
:label: eq:sol-cmh-recovery-family
Z_{\delta,\eps,R}
=\int_{B(0,R)}q_\delta(x)e^{-\eps|x|^2/2}\,\dd x,
\qquad
\dd\widetilde\mu_{\delta,\eps,R}(x)
=Z_{\delta,\eps,R}^{-1}\one_{B(0,R)}(x)
q_\delta(x)e^{-\eps|x|^2/2}\,\dd x,
```

and let $m_{\delta,\eps,R}$ be its mean. For fixed $\delta$, as $\eps\downarrow0$ and $R\uparrow\infty$, the density ratio in [](#eq:sol-cmh-recovery-family) relative to $\lambda_\delta$ tends pointwise to one, its normalizer tends to one, and it is eventually bounded by two. Dominated convergence, first with bounded continuous tests and then with $|x|^2$, gives weak convergence and convergence of second moments. Hence

```{math}
:label: eq:sol-cmh-recovery-fixed-delta
\Wtwo(\widetilde\mu_{\delta,\eps,R},\lambda_\delta)\longrightarrow0.
```

Take $\delta_k=k^{-4}$ and use [](#eq:sol-cmh-recovery-fixed-delta) to choose $0<\eps_k<k^{-1}$ and $R_k>k$ such that

$$
\Wtwo(\widetilde\mu_{\delta_k,\eps_k,R_k},\lambda_{\delta_k})<k^{-1}.
$$

Set $m_k=m_{\delta_k,\eps_k,R_k}$ and recenter:

$$
\mu_k=(x\mapsto x-m_k)_\#\widetilde\mu_{\delta_k,\eps_k,R_k}.
$$

Comparison of means under any quadratic-cost coupling and centeredness of $\lambda_{\delta_k}$ give $|m_k|<k^{-1}$. Therefore the triangle inequality and [](#eq:sol-cmh-recovery-smoothing) yield the ambient estimate

```{math}
:label: eq:sol-cmh-recovery-diagonal
\Wtwo(\mu_k,\mu)<\frac2k+\frac{\sqrt n}{k^2}.
```

We verify the regular class before using the words “regular recovery.” The support of $\mu_k$ is the convex body $P_k=B(-m_k,R_k)$, and on its interior

$$
\dd\mu_k(z)=g_k(z)\,\dd z,
\qquad
g_k(z)=Z_{\delta_k,\eps_k,R_k}^{-1}
q_{\delta_k}(z+m_k)e^{-\eps_k|z+m_k|^2/2}.
$$

The function $g_k$ extends to a positive smooth function on $\R^n$. It is log-concave, $\mu_k$ is centered by construction, and it is full-dimensional because $g_k>0$ on the open ball. Its barycenter zero lies in $\operatorname{int}P_k$: a positive density on a full-dimensional convex body cannot have its barycenter on a supporting hyperplane. The published compact-target theorem [@BermanBerndtsson2013RealMA; @Fathi2019SteinMomentMaps], in the repository form of [](#thm:regular-moment-map-compact-target), now supplies a smooth strictly convex moment potential $\varphi_k$, a diffeomorphism $\nabla\varphi_k:\R^n\to\operatorname{int}P_k$, and the smooth positive symmetric kernel

$$
H_k(x)=D^2\varphi_k((\nabla\varphi_k)^{-1}(x))
$$

with weak zero flux,

```{math}
:label: eq:sol-cmh-recovery-stein
\Div_{\mu_k}H_k=-x,
\qquad \E_{\mu_k}H_k=\Sigma_k:=\Cov(\mu_k).
```

Thus (i) is proved.

We next prove the stronger assertion (ii). Write $\Sigma_k^\nu=\Cov(\nu_k)$. Quadratic Wasserstein convergence gives convergence of second moments. Since the measures are centered, it follows that

```{math}
:label: eq:sol-cmh-recovery-covariance-convergence
\Sigma_k^\nu\longrightarrow\Sigma
```

in every matrix norm. For completeness, under couplings with $\E|X_k-X|^2\to0$, Cauchy–Schwarz gives convergence of each $\E[X_{k,i}X_{k,j}]$ to $\E[X_iX_j]$, because the second moments of $X_k$ remain bounded.

If $d=0$, then $\CPaff(\mu)=0$ by convention and [](#eq:sol-affine-poincare-w2-liminf) is immediate. We may therefore assume $d>0$ for the remaining common-core argument.

Fix $F\in\mathscr C$ from [](#eq:sol-cmh-recovery-ambient-core). Both $F$ and $F^2$ are bounded and continuous, so weak convergence gives

```{math}
:label: eq:sol-cmh-recovery-variance-convergence
\Var_{\nu_k}F\longrightarrow\Var_\mu F.
```

Also, with $h(x)=\inner{\Sigma\nabla F(x)}{\nabla F(x)}$, which is bounded and continuous,

```{math}
:label: eq:sol-cmh-recovery-energy-convergence
\begin{aligned}
&\left|\int\inner{\Sigma_k^\nu\nabla F}{\nabla F}\,\dd\nu_k
-\int\inner{\Sigma\nabla F}{\nabla F}\,\dd\mu\right| \\
&\quad\le
\norm{\Sigma_k^\nu-\Sigma}_\op\norm{\nabla F}_\infty^2
+\left|\int h\,\dd\nu_k-\int h\,\dd\mu\right|
\longrightarrow0.
\end{aligned}
```

Let $L=\liminf_k\CPaff(\nu_k)$. If $L=\infty$, there is nothing to prove. Otherwise choose one subsequence, independent of the test function, along which $\CPaff(\nu_k)\to L$. The affine Poincaré inequality for $\nu_k$, followed along this fixed subsequence by [](#eq:sol-cmh-recovery-variance-convergence) and [](#eq:sol-cmh-recovery-energy-convergence), gives for every $F\in\mathscr C$

$$
\Var_\mu F
\le L\int\inner{\Sigma\nabla F}{\nabla F}\,\dd\mu.
$$

[](#lem:sol-cmh-recovery-common-core) identifies the restriction of $\mathscr C$ with the intrinsic core on $S$ and extends the inequality in the closed form norm to all $H^1_\Sigma(\mu)$. Hence $\CPaff(\mu)\le L$, proving (ii). If $\Sigma$ is singular, [](#eq:sol-cmh-recovery-normal-annihilation) removes all normal derivatives; no inverse is taken in a collapsing direction and no whitening is performed before the limit.
:::

## 3\. Verification of the regular CMH endpoint

Although [](#thm:sol-affine-poincare-w2-liminf) itself does not use $\CMH$, the conditional corollary needs the exact regular endpoint. We record why the compact-target objects above have the closed-form realization required by [](#def:cmh).

Here a regular recovery sequence means a sequence of centered, full-dimensional, compact-target moment-map laws carrying the canonical kernel and weak zero-flux convention of [](#thm:regular-moment-map-compact-target). For one such law $\nu$, with target $P$, density $g$, covariance $\Sigma_\nu\succ0$, and canonical kernel $H$, let

$$
\mathscr D=\{F|_P:F\in\R+C_c^\infty(\R^n)\},
\qquad
\calE_H^0(f)=\int_P\inner{H\nabla f}{\nabla f}\,\dd\nu.
$$

This core is dense in $L^2(\nu)$ because it contains the restrictions of $C_c^\infty(\operatorname{int}P)$ and the convex boundary is null. The form is finite there because $\E_\nu H=\Sigma_\nu$. It is closable: if $f_j\to0$ in $L^2(\nu)$ and $H^{1/2}\nabla f_j\to u$ in $L^2(\nu;\R^n)$, then on each compact subset of $\operatorname{int}P$, the density is bounded above and below and $H^{\pm1/2}$ are bounded. Thus $f_j\to0$ and $\nabla f_j\to H^{-1/2}u$ in local Lebesgue $L^2$; closedness of distributional differentiation forces $u=0$. The same argument shows that a zero-energy element of the closure is constant, because $\operatorname{int}P$ is connected. Finally, the global weak Stein identity in [](#eq:sol-cmh-recovery-stein) identifies the Friedrichs form operator with the closed Stein generator used in [](#def:cmh); there is no hidden boundary distribution or unnamed maximal-domain convention. Consequently the already-certified [](#thm:cmh-implies-affine-poincare) applies and gives

```{math}
:label: eq:sol-cmh-recovery-regular-endpoint
\CPaff(\nu)\le\CMH(\nu)
```

for every member of a regular recovery sequence.

:::{prf:corollary} One bounded CMH recovery sequence suffices
:label: cor:sol-cmh-recovery-sequence-suffices
Assume [](#ass:cmh-recovery-envelope): there is a universal $C$ such that, for every centered log-concave $\mu$, at least one centered regular recovery sequence $\mu_k$ satisfies

$$
\Wtwo(\mu_k,\mu)\to0,
\qquad
\liminf_{k\to\infty}\CMH(\mu_k)\le C.
$$

Then every centered log-concave probability, including one carried by a proper affine subspace, satisfies

$$
\CPaff(\mu)\le C.
$$

Thus the recovery-envelope assumption implies [](#conj:kls) with the same constant.
:::

:::{prf:proof}
Apply the general lower-semicontinuity assertion [](#eq:sol-affine-poincare-w2-liminf) to the one sequence supplied by the assumption, and apply [](#eq:sol-cmh-recovery-regular-endpoint) to each of its regular members. Pointwise comparison of the two sequences of constants gives

$$
\CPaff(\mu)
\le\liminf_k\CPaff(\mu_k)
\le\liminf_k\CMH(\mu_k)
\le C.
$$

All limits are taken in the original ambient coordinates. The singular-support convention is therefore exactly that of [](#lem:sol-cmh-recovery-common-core), and the constant does not change. A universal bound on $\CPaff$ is the affine-invariant Poincaré formulation of KLS.
:::

**Hypotheses and conditional status.** The lemma uses centeredness, log-concavity, finite-dimensionality, and the published regular compact-target moment-map theorem. Centeredness identifies the affine hull with $\operatorname{Ran}\Sigma$ and is preserved by the construction. Log-concavity supplies the intrinsic density and is preserved by smoothing, tilt, convex truncation, translation, and $W_2$ limits. No isotropy, spectral gap, smoothness of the limiting law, or full-dimensionality of the limit is assumed. The corollary additionally uses [](#def:cmh), the certified endpoint [](#thm:cmh-implies-affine-poincare), and the unresolved [](#ass:cmh-recovery-envelope). The lemma is unconditional relative to its published imported moment-map input; the corollary remains conditional precisely on that open recovery-envelope assumption.

**Obstructions respected.** Neither ledger node has a `bounded_by` edge. The proof uses no localization occupation estimate, fixed cut, projection-only test, trace upgrade, or evolving isoperimetric competitor. Affine-support collapse is handled solely by ambient $W_2$ convergence and the intrinsic closed covariance form. No canonical moment-map kernel is transported through a noninvertible map, and no lower semicontinuity of $\CMH$ is claimed.

**Unclosed step and deferred ledger artifact.** The analytic proof of the lemma has no unclosed step. The only unclosed mathematical premise in the corollary is [](#ass:cmh-recovery-envelope). Since this dossier has `checked_by: none`, it has no ledger value. The future shared `solution: solutions/lem-affine-poincare-w2-liminf.md` is only a deferred artifact candidate pending independent review; no ledger delta is applicable now.
