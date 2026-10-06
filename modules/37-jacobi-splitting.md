---
numbering:
  enumerator: "37.%s"
---

(sec:jacobi)=
# Reilly, Jacobi, and splitting formulas

*Appendix to the fixed cut, Section [](#sec:introduction).*

This section assembles the geometric mechanisms intended to prove the weighted Stein-trace estimate for near-minimal cuts. The second-variation and Reilly identities are imported with exact normal conventions from the cited sources; the statements specific to this section are exact model statements, and their quantitative versions are among the problems of Section [](#sec:open). Throughout, $\nu=e^{-V}dx$ is smooth log-concave with smooth convex support, and $\Sigma=\partial^*E$ with the notation of Section [](#sec:notation).

## Second variation and stability of near-minimizers

:::{prf:proposition} Second variation; stability inequality
:label: prop:second-variation
Let $E$ be a smooth critical set of the weighted perimeter under the volume constraint, so that the weighted mean curvature $H_\nu=H-\partial_nV$ is constant on $\Sigma$. For a normal variation with speed $u$ satisfying the linearized volume constraint $\int_\Sigma u\dd\sigma_\nu=0$, the second variation of weighted perimeter is the index form $\calI_\Sigma(u,u)$ of [](#eq:jacobi-form) with Jacobi potential $\qJac_\Sigma=\abs{II_\Sigma}^2+\nabla^2V(n,n)$. If $E$ is a local minimizer, then

```{math}
:label: eq:stability
\calI_\Sigma(u,u)\ \ge\ 0
\qquad\text{for all }u\in C_c^\infty(\Sigma)\text{ with }\int_\Sigma u\dd\sigma_\nu=0 .
```

For log-concave $\nu$ with convex support, the Hessian and free-boundary contributions have the corresponding convex signs, so the constant mode is destabilizing: $\calI_\Sigma(1,1)=-\mathfrak K_\Sigma\le0$, with $\mathfrak K_\Sigma$ the constant-mode curvature of [](#eq:constant-mode-K). Stability of minimizers is carried entirely by the volume constraint, which removes the constant mode.
:::

:::{prf:proof} Published input
This is Lemma 4.1(ii) and the index form (4.1) of [@Rosales2014], with its inner-unit-normal convention and density $f=e^{-V}$, so $\operatorname{Ric}_f=\nabla^2V$. That formula includes the free-boundary term $-\int_{\partial\Sigma}II_{\partial K}(N,N)u^2$; convexity of the support and $\nabla^2V\succeq0$ give the signs used in [](#eq:jacobi-form). The local-minimum conclusion is precisely nonnegativity of this index form on mean-zero compactly supported variations.
:::

:::{prf:remark} The constant mode is the obstruction, again
:label: rem:constant-mode
The stability inequality [](#eq:stability) gives nonnegativity, not quantitative coercivity, of the mean-zero modes of an *exact* local minimizer. It may have a nontrivial kernel: for a Gaussian halfspace, tangential linear functions are mean-zero Jacobi zero modes. Any trace estimate must therefore project out and control such geometric modes in addition to the constant mode, which is absent from the volume-preserving test space and whose curvature is measured by $\mathfrak K_\Sigma$. The possible relation of these boundary modes to the dynamic operator-to-trace problem of Section [](#sec:carleson) is a guiding heuristic, not an established equivalence. The splitting mechanism below supplies only an exact sufficient model for the flat branch.
:::

## Constant-mode trace control and profile curvature

The following elementary Schur-complement estimate is the local form of the constant-mode problem. Let

$$
P=\sigma_\nu(\Sigma),\qquad
T(\psi)=\int_\Sigma\psi\dd\sigma_\nu,\qquad
\mathfrak K_\Sigma=-\calI_\Sigma(1,1)>0 .
$$

For $\psi=\bar\psi+\psi_0$ with $\bar\psi=P^{-1}T(\psi)$ and $\int_\Sigma\psi_0\dd\sigma_\nu=0$, stability of $\psi_0$ gives the quadratic constraint

$$
\mathfrak K_\Sigma\bar\psi^2
+2\calI_\Sigma(\psi,1)\bar\psi-\calI_\Sigma(\psi,\psi)\le0 .
$$

Solving it yields

```{math}
:label: eq:Jsharp-control
\abs{T(\psi)}^2
\le
\frac{2P^2}{\mathfrak K_\Sigma}
\left(
\calI_\Sigma(\psi,\psi)
+\frac{2}{\mathfrak K_\Sigma}\abs{\calI_\Sigma(\psi,1)}^2
\right).
```

Thus the relevant boundary energy is

```{math}
:label: eq:Jsharp-def
\Jsharp_\Sigma(\psi)
=
\calI_\Sigma(\psi,\psi)
+\frac{2}{\mathfrak K_\Sigma}\abs{\calI_\Sigma(\psi,1)}^2 .
```

The coefficient $2/\mathfrak K_\Sigma$ is not cosmetic: with coefficient $1/\mathfrak K_\Sigma$, pure constants are not controlled. In the Gaussian halfspace model $\mathfrak K_\Sigma=P$ and [](#eq:Jsharp-control) has the correct constant-mode scaling, with a factor-two slack for a pure constant test.

The same curvature controls the local concavity of the isoperimetric profile.

:::{prf:lemma} Profile bound
:label: lem:profile-bound
Suppose that at volume $p$ there is a smooth volume-constrained minimizer $E_p$ with boundary $\Sigma_p$, weighted area $P=I(p)$, and that $I$ is twice differentiable at $p$. Then

```{math}
:label: eq:profile-bound
\mathfrak K_{\Sigma_p}\le -I''(p)I(p)^2 .
```
:::

:::{prf:proof}
Flow $\Sigma_p$ with unit normal speed. Let $v(s)$ be the enclosed volume and $P(s)$ the weighted area. Then $v'(0)=P$ and $P'(0)=\lambda P$, where $\lambda=H_\nu$ is the constant weighted mean curvature. The Riccati variation of weighted mean curvature gives $P''(0)=-\mathfrak K_{\Sigma_p}+\lambda^2P$, with support terms included in $\mathfrak K_{\Sigma_p}$. Writing $\Psi(w)=P(v^{-1}(w))$ gives a smooth upper barrier for $I$ at $p$, and the chain rule gives $\Psi''(p)=-\mathfrak K_{\Sigma_p}/P^2$. Since $I\le\Psi$ and $I(p)=\Psi(p)$, twice differentiability gives $I''(p)\le\Psi''(p)$.
:::

:::{prf:corollary} Constant-mode degeneracy in the small-Cheeger regime
:label: cor:generic-degeneracy
Grant smooth minimizers at almost every balanced volume. If $h_\nu\le1$, then

```{math}
:label: eq:K-average
\int_{1/3}^{2/3}\mathfrak K_{\Sigma_p}\dd p\le C h_\nu^3 .
```
:::

:::{prf:proof}
For a concave profile with $I(0)=I(1)=0$, one has $\sup_{[1/3,2/3]}I\le C h_\nu$ and $\int_{1/3}^{2/3}(-I'')\dd p\le C h_\nu$ in the distributional sense. Combine these estimates with [](#eq:profile-bound).
:::

Thus, under the smooth-minimizer grant, many balanced volumes have small $\mathfrak K_{\Sigma_p}$ when $h_\nu$ is small. This averaged statement does not show that a selected near-Cheeger cut, or the same cut followed under localization, lies in that branch; transferring it to the tracked cut is a further step, not taken here. It nevertheless identifies the small-curvature branch as one that a geometric approach must address.

## The weighted Reilly identity

:::{prf:proposition} Generalized Reilly identity
:label: prop:reilly
Let $\Omega$ be a smooth bounded domain compactly contained in the smooth support of $\nu$, with boundary $\Sigma$ and *outer* unit normal $N$. Use the convention $II_\Sigma(X,Y)=\inner{\nabla_XN}{Y}$, and let $u$ be smooth on $\overline\Omega$. Then, with $L=\Delta-\nabla V\cdot\nabla$, $u_N=\partial_Nu$, and $H_\nu=H-\partial_NV$,

```{math}
:label: eq:reilly
\int_\Omega(Lu)^2\dd\nu
=\int_\Omega\Bigl(\norm{\nabla^2u}_\HS^2+\nabla u^T\nabla^2V\,\nabla u\Bigr)\dd\nu
+\int_\Sigma\Bigl(H_\nu\,u_N^2+2u_N\,L_\Sigma u
+II_\Sigma(\nabla_\Sigma u,\nabla_\Sigma u)\Bigr)\dd\sigma_\nu ,
```

where $L_\Sigma$ is the induced weighted Laplacian on $\Sigma$. This is [@MaDu2010, Thm. 1], followed by weighted integration by parts on the closed boundary $\Sigma$, in the source's outer-normal convention. In particular, for log-concave $\nu$ the interior terms are nonnegative and [](#eq:reilly) converts boundary trace data of $\nabla u$ into the interior Dirichlet quantity $\int(Lu)^2\dd\nu$, up to curvature boundary terms.
:::

:::{prf:remark} Dirichlet form of the trace estimate
:label: rem:dirichlet-trace
When $E$ is compactly contained in the support, apply [](#eq:reilly) on $\Omega=E$ to the Poisson solution $u_M$ of [](#lem:boundary-rep), with centered quadratic data $f_M$. The left side is computable: $\int_E(Lu_M)^2\dd\nu=\int_E f_M^2\dd\nu\le\Var_\nu(f_M)$, hence is controlled by quadratic-chaos information (Section [](#sec:qcts)). The interior terms have a sign. The boundary terms involve $u_N^2$ weighted by $H_\nu$, the mixed term $2u_NL_\Sigma u$, and $II_\Sigma(\nabla_\Sigma u,\nabla_\Sigma u)$. The intrinsic quadratic-chaos input is now dimension-free by [](#thm:letwin-qcts), conditional on its version-1 preprint status, but neither [](#eq:stability) nor the Schur energy [](#eq:Jsharp-def) currently controls all of these boundary terms for the localized fixed cut. In particular, the global Poisson solution has no boundary condition on $\Sigma$ that removes the mixed term. Thus Reilly suggests a mechanism rather than furnishing a reduction: a quantitative trace/almost-stability lemma, uniform under localization and modulo all Jacobi zero modes, is still required before the mean-zero and constant-mode branches can be chained. This foundational gap is part of [](#conj:stein-weighted). If $E$ meets $\partial K$, the generalized Reilly formula also has support-boundary and corner/free-boundary terms. The Neumann condition in [](#lem:boundary-rep) removes the first-order flux there but does not by itself control these second-order terms; they belong to the same missing bridge.
:::

:::{prf:conjecture} Foundational almost-stability target
:label: conj:almost-stability-gap
[](#prop:second-variation) applies to a smooth critical local minimizer. A fixed near-Cheeger set transported through stochastic localization is generally neither critical nor a minimizer for $\mu_t$, and small perimeter excess alone does not imply [](#eq:stability). Smoothing a finite-perimeter set also need not preserve criticality, stability, or uniform Jacobi constants. An almost-stability trace theorem nevertheless holds along the localization: perimeter excess controls the failure of the index-form inequality for $\partial_nu_M$, after projecting out constants and geometric zero modes, with the projected coefficients paid for by the centroid or damping terms. The Reilly–Jacobi mechanism of Section [](#sec:jacobi) requires it.
:::

## Splitting: exact model statements

:::{prf:proposition} Flat cylindrical direction yields splitting; split halfspaces are flat
:label: prop:exact-splitting
Let $\nu=e^{-V}dx$ be log-concave with convex support $K$ under the smooth/free-boundary convention of Section [](#sec:notation), let $\theta\in S^{n-1}$, and suppose $K$ is a cylinder in the $\theta$-direction: in coordinates $x=(y,z)$, $z=\inner x\theta$, $K=K_1\times J$ with $K_1\subset\theta^\perp$ convex and $J\subseteq\R$ an interval. If $\nabla^2V(\theta,\cdot)\equiv0$ on $\operatorname{int}K$, then the potential splits as $V(y,z)=V_1(y)+cz$ for some $c\in\R$, and $\nu=\nu_1\otimes\nu_2$ is a product of a log-concave measure $\nu_1\propto e^{-V_1}$ on $K_1$ and a log-affine factor $\nu_2\propto e^{-cz}$ on $J$; normalizability of $\nu_2$ forces $J$ to be a proper interval — a half-line when $c\ne0$, or a bounded interval — and not all of $\R$. Separately, if $\nu$ already has this product form, $z_0\in\operatorname{int}J$, and $E=\{z\le z_0\}$ is a halfspace cut orthogonal to such a direction, then $\Sigma$ is totally geodesic ($II\equiv0$), $\nabla^2V(n,n)\equiv0$ on $\Sigma$, and the constant-mode curvature vanishes: $\mathfrak K_\Sigma=0$.
:::

:::{prf:proof}
On $\operatorname{int}K$, $\nabla^2V(\theta,\cdot)=0$ means $\partial_z\nabla V\equiv0$, so every $\partial_{x_j}V$ is independent of $z$; in particular $\partial_zV$ is independent of $z$, and since $\partial_{x_j}(\partial_zV)=0$ it is independent of $y$ as well, hence a constant $c$. Integrating on the cylinder $K_1\times J$ gives $V=V_1(y)+cz$, so $\nu=\nu_1\otimes\nu_2$ with $\nu_2\propto e^{-cz}$ on $J$, a finite measure only if $J\ne\R$ (a half-line when $c\ne0$, or a bounded interval). The converse statements are immediate from $II=0$ for a hyperplane and $\qJac_\Sigma=\abs{II}^2+\nabla^2V(n,n)=0$ on $\Sigma$. The support-boundary term also vanishes: the lateral boundary of the cylinder is flat in the $\theta$ direction, and the cut does not meet an endpoint of $J$.
:::

The two implications above have different hypotheses. In particular, no converse $\mathfrak K_\Sigma=0\Rightarrow$ global cylindrical or log-affine splitting is available here: the left-hand side is boundary-local data, whereas the first implication assumes global product geometry and Hessian flatness. That rigidity statement is part of [](#conj:splitting).

:::{prf:proposition} Persistence of splitting under localization
:label: prop:persistent-splitting
Fix $\theta\in S^{n-1}$ and write $x=y+z\theta$. Suppose there are proper lower-semicontinuous convex extended-valued functions $V_1$ on $\theta^\perp$ and $V_2$ on $\R$, each with positive finite normalizer, such that the global identity $V(y+z\theta)=V_1(y)+V_2(z)$ holds for every $(y,z)$. Thus the effective support as well as the density has product form. Then the localized potential has the same additive splitting at every time: $V_t(x)=V(x)+\tfrac t2\abs x^2-c_t\cdot x$ splits as $\bigl(V_1(y)+\tfrac t2\abs y^2-c_t'\cdot y\bigr)+\bigl(V_2(z)+\tfrac t2z^2-c_t''z\bigr)$. In particular, the splitting direction is preserved pathwise, the covariance $A_t$ is block-diagonal across $\theta^\perp\oplus\R\theta$ for all $t$, and every fixed nontrivial halfspace $E_a=\{y+z\theta:z\le a\}$ has $\delta_t=d_t\theta$, $G_t=g_t\theta\theta^T$, and $K_t=\kappa_t\theta\theta^T$, hence rank at most one, for all $t$.
:::

:::{prf:proof}
The tilt $\tfrac t2\abs x^2-c_t\cdot x$ is itself additively separable in any orthogonal decomposition. The block structure of $A_t$ and the alignment of $\delta_t$ follow from the product structure of $\mu_t$ and of the cut.
:::

:::{prf:remark} Boundary Obata and quantitative splitting
:label: rem:obata
[](#prop:exact-splitting)–[](#prop:persistent-splitting) identify a sufficient flat model for the constant mode: an already split log-affine factor and its orthogonal halfspace have $\mathfrak K_\Sigma=0$, and the splitting persists under localization. Vanishing of the integrated boundary curvature alone does not force that global model. The splitting philosophy of the geometric approach is the conjectural rigidity and stability assertion that a near-worst measure with a near-minimal cut of small constant-mode curvature should be quantitatively close, along the relevant directions, to such a split structure — where the two-color quantities are rank-one, the per-direction Carleson estimate ([](#cor:per-direction)) already controls the source, and the variance dynamics are one-dimensional. A rigidity statement of Obata type would require hypotheses substantially stronger than global completeness and minimality alone: already in one dimension the density proportional to $e^{-z^4}$ has a median halfline with boundary-local second-order curvature zero but no log-affine factor. Any valid theorem must rule out such higher-order flatness. Its quantitative version, with constants uniform along localization, is [](#conj:splitting). We claim neither direction here beyond the explicit sufficient model of [](#prop:exact-splitting).
:::
