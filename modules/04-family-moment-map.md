---
numbering:
  enumerator: "4.%s"
---

(sec:family-moment-map)=
# Family 4: moment maps, Monge–Ampère, and Stein kernels

KLS is now proved, by three different arguments compared in Chapter [](#sec:kls-synthesis); all three start from the quadratic estimate of this family. This chapter describes what the moment map controls on its own and what it does not give without them.

**Object followed.** The Hessian $H=\Hess\varphi$ of the moment-map potential of $\mu$, in the coordinates in which $\mu$ is the pushforward of its own moment measure.

**What it buys.** The July 2026 moment-map estimates isolate a useful static component of the problem. In moment-map coordinates the statement “$\mu$ is isotropic” becomes “$\E_\nu H=I$”, and the Monge–Ampère equation, differentiated twice, produces two manifestly positive semidefinite source terms. Exploiting that positivity yields a sharp bound on $\E\Tr(BHBH)$ for every *constant* symmetric matrix $B$ — from which the sharp thin-shell constant, the sharp third-moment tensor, and the all-quadratic Poincaré inequality all follow.

This chapter presents the mechanism. The two consequences used elsewhere in this manuscript are [](#thm:letwin-qcts) (Chapter [](#sec:qcts)) and [](#prop:letwin-kappa) (Chapter [](#sec:covariance-tech)); they are not restated here.

(subsec:mm-coordinates)=
## Moment-map coordinates

For a centered, full-dimensional $\mu=e^{-V}\dd x$, the moment-measure theorem supplies an essentially unique convex $\varphi$ with

```{math}
:label: eq:moment-measure
(\nabla\varphi)_\#\nu=\mu,
\qquad
\dd\nu(y)=e^{-\varphi(y)}\dd y
```

[@CorderoErausquinKlartag2015MomentMeasures; @Klartag2013MomentMeasures]. Set

$$
H(y)=\Hess\varphi(y).
$$

Change of variables in [](#eq:moment-measure) is the Monge–Ampère equation

```{math}
:label: eq:MA
e^{-V(\nabla\varphi(y))}\det H(y)=e^{-\varphi(y)},
\qquad\text{that is}\qquad
\log\det H=-\varphi+V(\nabla\varphi).
```

If $Y\sim\nu$ and $X=\nabla\varphi(Y)$, then $X\sim\mu$, and integration by parts under $\nu$ gives

```{math}
:label: eq:mean-hessian-identity
\E_\nu H(Y)=\E_\nu\bigl[\nabla\varphi(Y)\otimes\nabla\varphi(Y)\bigr]=\Cov\mu=I
```

when $\mu$ is isotropic. So *“average Hessian equals identity” replaces isotropy* in moment-map coordinates. This is the structural payoff: isotropy, which Chapter [](#sec:family-needles) showed is not inherited by needles, becomes a single linear identity for the object being estimated.

:::{prf:theorem} Compact-target regular moment map
:label: thm:regular-moment-map-compact-target
Let $P\subset\R^n$ be a convex body and let $\mu(dx)=g(x)\mathbf 1_{\operatorname{int}P}(x)\,dx$ be a centered probability measure, where $g\in C^\infty(\R^n)$ is positive. Then the canonical moment potential $\varphi$ is smooth and strictly convex on $\R^n$, and

$$
\nabla\varphi:\R^n\longrightarrow\operatorname{int}P
$$

is a diffeomorphism. Moreover,

$$
\tau_\mu(x)=D^2\varphi\bigl((\nabla\varphi)^{-1}(x)\bigr)
$$

is a smooth positive symmetric Stein kernel: $\Div_\mu\tau_\mu=-x$ distributionally, with weak zero boundary flux, and $\E_\mu\tau_\mu=\Cov(\mu)$.
:::

The moment-potential regularity and global gradient-image statement are Theorem 1.1 of [@BermanBerndtsson2013RealMA]; the target-coordinate Stein identity and weak zero-flux formulation are Theorem 2.3 of [@Fathi2019SteinMomentMaps]. This compact-target class is the published regularity input used by the approximation closure in [](#prop:cmh-approximation-closure).

(subsec:mm-differentiated)=
## Differentiating Monge–Ampère

Introduce the elliptic operator associated with the Hessian metric,

```{math}
:label: eq:calL-def
\calL f=\varphi^{ij}\partial_{ij}f-(V_i\circ\nabla\varphi)\,\partial_if,
\qquad (\varphi^{ij})=H^{-1},
```

which is symmetric in $L^2(\nu)$:

```{math}
:label: eq:calL-symmetric
\E_\nu[(\calL f)g]=-\E_\nu\bigl[\varphi^{ij}(\partial_if)(\partial_jg)\bigr].
```

Differentiating [](#eq:MA) twice gives the key identity

```{math}
:label: eq:differentiated-MA
\calL H_{ij}+H_{ij}
=\bigl(H\,\Hess V(\nabla\varphi)\,H\bigr)_{ij}
+\varphi^{ac}\varphi^{bd}\varphi_{abi}\varphi_{cdj} .
```

Both terms on the right are positive semidefinite: the first by convexity of $V$, the second because it is a Gram matrix of normalized third derivatives. *This positivity is the PDE source of the new estimate*; everything below is a way of harvesting it.

(subsec:mm-fixed-matrix)=
## The fixed-matrix Hessian bound

Let $B\succeq0$ and define

$$
S_B=\Tr(BHBH),
\qquad
D_B=\varphi^{ab}\Tr\bigl(B(\partial_aH)B(\partial_bH)\bigr).
$$

Applying $\calL$ to $S_B$, integrating against $\nu$, and using the two positive sources of [](#eq:differentiated-MA) yields

```{math}
:label: eq:SB-DB
\E S_B\ge2\,\E D_B .
```

The nontrivial point is a third-derivative comparison. At a fixed point, normalize $H=I$ and diagonalize $B=\diag(b_i)$; writing $T_{ijk}=\varphi_{ijk}$, the difference between the two sides reduces to

```{math}
:label: eq:third-derivative-comparison
\tfrac12\sum_{i,j,k}(b_i-b_j)^2T_{ijk}^2\ \ge\ 0 .
```

Next apply Brascamp–Lieb entrywise to $F=B^{1/2}HB^{1/2}$. Since $\E F=B$ by [](#eq:mean-hessian-identity),

$$
\E\norm{F-B}_{\HS}^2=\E S_B-\Tr(B^2),
$$

and the Brascamp–Lieb energy of $F$ is exactly $D_B$, so

$$
\E S_B-\Tr(B^2)\ \le\ \E D_B\ \le\ \tfrac12\E S_B ,
$$

the last step by [](#eq:SB-DB). Rearranging gives the main new theorem inside Letwin's proof.

:::{prf:theorem} Letwin matrix moment-map estimate
:label: thm:letwin-moment-map
Under the regular moment-map assumptions used in [@Letwin2026QuadraticKLS], for every constant symmetric matrix $B$,

```{math}
:label: eq:letwin-matrix
\E_\nu\Tr\bigl(BH(Y)BH(Y)\bigr)\le2\Tr(B^2).
```
:::

For indefinite $B$ the statement still holds: diagonalizing gives the pointwise bound $\Tr(BHBH)\le\Tr(\abs BH\abs BH)$, and [](#eq:letwin-matrix) applies to $\abs B\succeq0$.

The $B=I$ case of [](#eq:letwin-matrix) is the moment-Hessian estimate shared with the contemporaneous Chen–Klartag preprint.

:::{prf:theorem} Chen–Klartag moment-Hessian estimate
:label: thm:chen-klartag-moment-hessian
Under the regularity assumptions of [@ChenKlartag2026SharpThinShell],

$$
\E_\nu\norm H_{\HS}^2\le2n.
$$

The general log-concave conclusions below follow by the approximation argument in that preprint.
:::

:::{prf:theorem} Chen–Klartag sharp thin shell
:label: thm:chen-klartag-thin-shell
For every isotropic log-concave $X\in\R^n$,

$$
\Var(|X|^2)\le8n.
$$

The constant is attained by products of standard centered one-sided exponential variables.
:::

:::{prf:theorem} Chen–Klartag sharp third tensor
:label: thm:chen-klartag-third-moment
If $X\in\R^n$ is isotropic and log-concave and $T_3(X)=(\E X_iX_jX_k)_{i,j,k}$, then

$$
\norm{T_3(X)}_{\HS}^2\le4n.
$$

The preprint also proves sharper convex-body estimates with equality for the regular simplex.
:::

:::{prf:remark} What each preprint contributes
:label: rem:mm-two-preprints
[](#thm:letwin-moment-map)–[](#thm:chen-klartag-third-moment) are imported from contemporaneous version-1 preprints [@ChenKlartag2026SharpThinShell; @Letwin2026QuadraticKLS]. Letwin's $B=I$ case contains the shared moment-Hessian estimate, while Chen–Klartag's sharp third-tensor, cone, simplex, and equality analysis is additional. Conversely, Letwin controls every constant symmetric homogeneous quadratic form. Neither subsumes the other. Letwin's general bound is stated as [](#thm:letwin-kls).
:::

(subsec:mm-stein)=
## The Stein kernel and the $H^{-1}$ inequality

Fathi observed that the moment-map Hessian, read in target coordinates,

```{math}
:label: eq:stein-kernel-def
\tau_\mu(x)=H\bigl((\nabla\varphi)^{-1}(x)\bigr),
```

is a positive symmetric Stein kernel for $\mu$ [@Fathi2019SteinMomentMaps]:

```{math}
:label: eq:stein-identity
\E[X_if(X)]=\E\sum_j\tau_{ij}(X)\,\partial_jf(X).
```

Combining [](#eq:stein-identity) with the $H^{-1}$ calculus of Section [](#subsec:hminus1) gives, for a linear function $\ell_v(x)=\inner xv$,

```{math}
:label: eq:stein-hminus1
\norm{\ell_v}_{H^{-1}(\mu)}^2\le\E\abs{\tau_\mu(X)v}^2 .
```

By [](#rem:quadratics-special), quadratic test functions have linear derivatives, so [](#eq:stein-hminus1) can be fed into the Barthe–Klartag inequality [](#eq:barthe-klartag). This is the junction at which the two families meet.

(subsec:mm-noncommutativity)=
## The noncommutativity trick

There is one genuine obstacle between [](#eq:letwin-matrix) and a quadratic Poincaré inequality. For $q_M(x)=\inner{Mx}x$, applying [](#eq:stein-hminus1) directly produces

$$
\E\norm{\tau_\mu(X)M}_{\HS}^2 ,
$$

which is *not* the expression controlled by [](#eq:letwin-matrix), because $M$ and $\tau_\mu(X)$ need not commute.

First work on a regular target and suppose $M$ is invertible. The resolution is a change of variables. Write $M=\operatorname{sgn}(M)\abs M$ and set $Z=\abs M^{1/2}X$, with $\eta$ the law of $Z$. Then

$$
q_M(X)=\inner{\operatorname{sgn}(M)Z}Z ,
$$

and the Stein kernel transforms by congruence,

```{math}
:label: eq:stein-congruence
\tau_\eta(Z)=\abs M^{1/2}\,\tau_\mu(X)\,\abs M^{1/2},
```

so that

```{math}
:label: eq:conjugated-bound
\E\norm{\tau_\eta(Z)}_{\HS}^2=\E\Tr\bigl(\abs MH\abs MH\bigr)\le2\Tr(M^2)
```

by [](#thm:letwin-moment-map) applied with $B=\abs M$. The conjugation has moved $M$ inside the trace in exactly the pattern [](#eq:letwin-matrix) controls.

The law $\eta$ is centered and log-concave, but generally not isotropic; the Barthe–Klartag $H^{-1}$ inequality requires no isotropy. Apply it to $F(z)=\inner{\operatorname{sgn}(M)z}z-\Tr M$, whose derivatives are centered. Since $M$ is invertible, $\operatorname{sgn}(M)$ is orthogonal, giving

$$
\Var\inner{MX}X\le4\,\E\norm{\tau_\eta(Z)}_{\HS}^2\le8\Tr(M^2),
$$

For singular $M$, let $P_0$ project onto its kernel and apply this bound to $M_\varepsilon=M+\varepsilon P_0$, $\varepsilon>0$. Then

$$
\Tr(M_\varepsilon^2)=\Tr(M^2)+\varepsilon^2\dim\ker M,
\qquad
\norm{X^T(M_\varepsilon-M)X}_{L^2}
\le\varepsilon(\E|X|^4)^{1/2}\longrightarrow0.
$$

Variance therefore passes to the limit. Finally, Gaussian smoothing, convex truncation and affine normalization approximate any isotropic log-concave law by regular targets with convergence of moments through degree four. This transfers the quadratic estimate without requiring convergence of moment Hessians. Isotropy gives $\E\abs{\nabla\inner{MX}X}^2=4\Tr(M^2)$, yielding the formulation in [](#thm:letwin-qcts), with constant $2$ attained by products of centered exponentials at $M=I$.

The reduction from there to $\kappa_n\le2\sqrt2$ is short and purely algebraic; it is carried out as [](#prop:letwin-kappa). The further bridge [](#eq:kls-bridge) gives the general bound [](#thm:letwin-kls), Theorem 1.1 of the preprint.

The constant $2\sqrt2$ is not sharp, and the moment-map approach says exactly what would sharpen it. On the regular moment-map class, [](#cor:gate-zero-third-moment) turns any bound $\E[\tau^2]\preceq c\,\Id$ into the directional third-moment bound $\norm{T_3(a)}_{\HS}\le2\sqrt{c-1}$, so the sharp linear test of the moment-Hessian inequality, $c=2$ ([](#conj:gate-zero-sharp)), would give the sharp $\kappa_n\le2$, attained by products of centered exponentials. The implication runs one way only: a sharp third-moment bound does not return that sharp linear test, because the high-mode remainder of [](#lem:linear-sector-third-moment) is not zero off the cone axis.

:::{prf:theorem} Letwin's general KLS bound
:label: thm:letwin-kls
There is a universal constant $C>0$ such that, for every integer $n\ge2$,

$$
C_{\mathrm P,n}\le C\sqrt{\log n},
\qquad
\PsiKLS_n\le C(\log n)^{1/4},
$$

where the suprema are over all isotropic log-concave probability measures on $\R^n$, with the Poincaré and inverse-Cheeger normalizations of Section [](#sec:kls-orientation).
:::

The bridge must respect a restriction on the observation time. For a regular isotropic law, put $P=\CP(\mu)$. Gaussian observation, conditional variance, the Lipschitz-variance comparison and improved Lichnerowicz give

$$
c_M P\le\frac{2+tP}{\sqrt t}\,\E\sqrt{\norm{A_t}_{\op}}.
$$

The factor $2+tP$ prevents using the whole time range of covariance control without checking the initial spectral gap. Set $T=a/(\kappa_n^2\log n)$ and $t=\min\{T,P^{-1}\}$. The fixed-time covariance estimate bounds the expectation by a universal constant, while $tP\le1$. If $t=T$, the result is $P\lesssim\kappa_n\sqrt{\log n}$; if $t=P^{-1}$, it is $P\lesssim\sqrt P$, hence a universal bound. Regular approximation and whitening pass the estimate to all isotropic log-concave laws. Combining [](#prop:letwin-kappa) with [](#thm:letwin-qcts), and then the two-sided Cheeger comparison, gives the two exponents above. This argument does not use [](#thm:klartag-logn) and retains the residual logarithmic loss.

**What it does not reach alone.** Control of $\E\inner{\tau_\mu(X)\nabla f(X)}{\nabla f(X)}$ for an arbitrary $f$, in place of $\E\Tr(BHBH)$ for a constant matrix $B$. Brascamp–Lieb in moment-map coordinates already gives

```{math}
:label: eq:mm-brascamp-lieb
\Var_\mu f\le\E_\mu\inner{\tau_\mu(X)\nabla f(X)}{\nabla f(X)},
```

so the bound $\E\inner{\tau_\mu\nabla f}{\nabla f}\lesssim\E\abs{\nabla f}^2$ would give KLS within this family. The identity $\E\tau_\mu=I$ of [](#eq:mean-hessian-identity) is *not* sufficient for this, because $\tau_\mu(X)$ can correlate with $\nabla f(X)$. Letwin controls a deterministic $B$; the missing theorem must handle an $X$-dependent matrix or direction field.

**Where this family meets the alternative mechanisms.** It supplies two of them. The moment map (Chapter [](#sec:moment-map-cmh)) attacks the gap above head-on, replacing constant multipliers by test-dependent Haar fields, and its endpoint — the target inequality $\mathrm{CMH}(4)$ for the constant $\CMH$, which everything in that mechanism serves to prove — is defined in these coordinates. The fixed eigenfunction uses the family's quadratic control as the estimate it feeds its whitened posterior tensor to. The fixed-matrix bound ([](#thm:letwin-moment-map)) is therefore the single literature input both mechanisms are trying to make adaptive.

(subsec:mm-audit)=
## Sources

The imports follow the first versions of the preprints of Letwin [@Letwin2026QuadraticKLS] (arXiv:2607.24164v1), whose Theorems 2.5, 1.2 and 1.1 are [](#thm:letwin-moment-map), [](#thm:letwin-qcts) and [](#thm:letwin-kls), and of Chen–Klartag [@ChenKlartag2026SharpThinShell] (arXiv:2607.23307v1), Theorems 1.5, 1.1 and 1.2 with Corollary 1.3 for convex bodies. In both, the passage from regular targets to general log-concave laws goes through convergence of polynomial moments under Gaussian smoothing, convex truncation and affine normalization; it asserts no convergence of the moment-map Hessian. The full third-tensor norm bounded by Chen–Klartag is distinct from the directional parameter of [](#prop:letwin-kappa).
