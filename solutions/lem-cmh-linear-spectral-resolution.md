---
title: 'Solution: spectral resolution of the linear-sector gate matrices $\mathsf N,\mathsf D,\mathsf R$'
label: sec:sol-clsr
ledger-node: lem:cmh-linear-spectral-resolution
numbering:
  enumerator: D10.%s
---

*Part of the moment-map mechanism, Chapter [](#sec:cmh-normalization); the reading order is on the [full proofs](#sec:proofs-moment-map) page.*

**Overview.** This dossier proves [](#lem:cmh-linear-spectral-resolution) in the refined form [](#thm:sol-clsr-main). On a single regular isotropic compact-target moment map, it resolves the gate matrices $\mathsf N,\mathsf D,\mathsf R$ along the spectrum of the Stein operator. The key input is that the Hessian columns $Ha$ solve a weak eigen-type column equation, obtained by differentiating the Monge–Ampère equation twice. The dossier also proves the dimension-dependent retention $\mathsf R\succeq\mathsf N-n\Id$ and the sharp bound $\mathsf R\succeq\mathsf D$ on finite products. It relies on the published imports [](#thm:regular-moment-map-compact-target) and the Hessian bound [](#eq:sol-clsr-Hbound). It proves no universal bootstrap, no bound on $\CMH$, and no strong-form column equation on the general class.

1. Pointwise calculus: from [](#eq:sol-clsr-MA1), [](#lem:sol-clsr-symmetric-form) and [](#lem:sol-clsr-pullback) identify the source generator with the Stein generator. [](#lem:sol-clsr-MA2) gives $\calL H+H=A+Q$ with $A,Q\succeq0$.
2. Cutoff calculus ([](#lem:sol-clsr-cutoff)–[](#lem:sol-clsr-form-membership)): finiteness of $\mathsf D$, the trace identity [](#eq:sol-clsr-trace-identity) and the normalization $\int(A+Q)\,\dd\eta=\Id$. The same lemmas give the weak column equation [](#eq:sol-clsr-weak-column).
3. [](#lem:sol-clsr-eigen) and [](#lem:sol-clsr-BL): the coordinates $u_b$ are eigenfunctions with eigenvalue $1$, and Brascamp–Lieb makes $1$ the exact gap.
4. Using Steps 2–3 together with [](#lem:sol-clsr-orthogonality) and [](#lem:sol-clsr-M), the orthogonal decomposition of $Ha$ gives the resolution [](#eq:sol-clsr-resolution). [](#prop:sol-clsr-anticommutator) identifies $\mathsf R$ as an anticommutator integral.
5. Corollaries C1–C5 follow from Step 4. They include $\mathsf R\preceq\Id$ and the channel criterion [](#eq:sol-clsr-channel) for $(\mathrm{AB})_{\rho,\beta}$.
6. Part (f): the cyclic square [](#lem:sol-clsr-cyclic), used under the trace only, with Steps 2 and 4 gives $\Tr\mathsf R\ge\Tr\mathsf D$, $\mathsf R\succeq\mathsf N-n\Id$ and $Q_{\mathrm{lin}}\le n+1$.
7. Part (g): on products everything is diagonal, and $\mathsf R-\mathsf D$ reduces to a nonnegative curvature integral.

**Scope.** This dossier proves the candidate [](#lem:cmh-linear-spectral-resolution) of Chapter [](#sec:cmh-normalization): on one fixed regular isotropic compact-target moment map, the three linear-sector gate matrices resolve exactly along the spectrum of the Stein operator, with the columns of the moment Hessian solving, in the weak (closed-form) sense stated in the manuscript lemma, an eigen-type equation forced by the differentiated Monge–Ampère structure. It also proves the unconditional dimension-dependent retention $\mathsf R\succeq\mathsf N-n\Id$ (hence $Q_{\mathrm{lin}}\le n+1$) and the sharp retention $\mathsf R\succeq\mathsf D$ on regular finite products of one-dimensional laws.

*What this dossier does not prove.* It proves *no* anisotropic bootstrap $(\mathrm{AB})_{\rho,\beta}$ with universal (dimension-free) constants; *no* bound on $Q_{\mathrm{lin}}$ beyond $n+1$; *no* bound on $\CMH$, no statement about [](#conj:kls) (KLS), no statement about `conj:gate-zero` beyond the exact identities below, and nothing about the trace-upgrade cluster (`conj:trace-upgrade`, high-rank `conj:stein-weighted`, `conj:product-alignment`), which is not opened here. All statements are stationary identities and inequalities at one fixed map of the regular class. No numerical evidence is used anywhere.

## 0\. Standing setting, imports, and notation

:::{prf:definition} Regular isotropic compact-target moment map
:label: def:sol-clsr-class
Let $P\subset\R^n$ be a convex body and let

$$
\mu(\dd x)=e^{-V(x)}\one_{\operatorname{int}P}(x)\,\dd x
$$

be a probability measure with $V\in C^\infty(\R^n)$, such that $\mu$ is centered ($\E_\mu X=0$), isotropic ($\Cov\mu=\Id$), and log-concave on its support ($D^2V\succeq0$ on $\operatorname{int}P$). By the imported compact-target regularity theorem ([](#thm:regular-moment-map-compact-target); [@BermanBerndtsson2013RealMA; @Fathi2019SteinMomentMaps]) the canonical moment potential $\psi$ is smooth and strictly convex on $\R^n$,

$$
\nabla\psi:\R^n\longrightarrow\operatorname{int}P
$$

is a diffeomorphism, and the target-coordinate Hessian

$$
\tau(x)=D^2\psi\bigl((\nabla\psi)^{-1}(x)\bigr)
$$

is a smooth positive symmetric Stein kernel: $\Div_\mu\tau=-x$ distributionally with weak zero boundary flux, and $\E_\mu\tau=\Cov\mu=\Id$. We write

$$
\eta(\dd y)=e^{-\psi(y)}\,\dd y,\qquad H(y)=D^2\psi(y)\succ0,\qquad
(\nabla\psi)_\#\eta=\mu ,
$$

so $\eta$ is a probability measure (the moment-measure normalization) and $\tau(\nabla\psi(y))=H(y)$. Set $R=R(P)=\max_{x\in P}\abs x$, $c_V=\sup_{\operatorname{int}P}\abs{\nabla V}<\infty$ and $c_{V''}=\sup_{\operatorname{int}P}\norm{D^2V}_\op<\infty$ (finite because $V$ is smooth on $\R^n$ and $\overline P$ is compact).
:::

:::{prf:remark} Imported pointwise Hessian bound
:label: rem:sol-clsr-klartag-import
Theorem 1.1 of [@Klartag2013MomentMeasures] gives $\Delta\psi\le2R(P)^2$ on $\R^n$ for a centered log-concave target on a bounded convex $P$ whose potential $V$ is smooth with all derivatives bounded on $P$ (his conditions (1), satisfied here because $V\in C^\infty(\R^n)$ and $\overline P$ is compact); since $H\succ0$, this yields $H\preceq(\Tr H)\Id\preceq2R(P)^2\Id$, i.e. the pointwise bound

```{math}
:label: eq:sol-clsr-Hbound
0\prec H(y)\preceq 2R(P)^2\,\Id\qquad\text{for all }y\in\R^n.
```

This published import is load-bearing for every integrability statement below; we flag each use. All constants produced by [](#eq:sol-clsr-Hbound) may depend on the map and on $n$; the lemma asserts no universality of constants.
:::

**Operator data.** Following [](#def:cmh) and the certified conventions of Chapter [](#sec:cmh-normalization), the Stein generator in target coordinates is $L_\mu g=\Div_\mu(\tau\nabla g)=\Tr(\tau D^2g)-x\cdot\nabla g$, the form core is

$$
\mathscr D=\bigl\{F|_{\operatorname{int}P}:F\in\R+C_c^\infty(\R^n)\bigr\},
\qquad
\calE^0(f,g)=\E_\mu\inner{\tau\nabla f}{\nabla g},
$$

$\calE$ is the closed form generated by $(\calE^0,\mathscr D)$ (closable by the certified normalization dossier), and $\Aop\ge0$ is its self-adjoint operator on $L^2(\mu)$, with $\ker\Aop=\R\one$ because $\tau\succ0$ and $\operatorname{int}P$ is connected. Every core element has finite energy since $\calE^0(f,f)\le\norm{\nabla f}_\infty^2\Tr\E_\mu\tau =\norm{\nabla f}_\infty^2\,n<\infty$. The unitary map

$$
U:L^2(\mu)\to L^2(\eta),\qquad Ug=g\circ\nabla\psi
$$

(isometric because $(\nabla\psi)_\#\eta=\mu$, surjective because $\nabla\psi$ is a diffeomorphism) transports $\calE$, $\Aop$, and all spectral objects to $L^2(\eta)$; we use the same symbols on both sides and say in which coordinates a computation is performed. No operator inverse (and no pseudoinverse of $\Aop$) is used anywhere in this dossier.

**The gate matrices.** Write $\psi_{i}$, $\psi_{ij}=H_{ij}$, $\psi_{ijk}=\partial_kH_{ij}$ for source derivatives, Einstein summation throughout, and $(H^{ij})=H^{-1}$ (pointwise matrix inverse of the positive matrix $H(y)$; this is not an operator inverse). Define the source matrices

```{math}
:label: eq:sol-clsr-AQ-def
A=H\,(D^2V\circ\nabla\psi)\,H,\qquad
Q_{k\ell}=\Tr\bigl(H^{-1}\partial_kH\,H^{-1}\partial_\ell H\bigr),
```

and the constant symmetric matrices

```{math}
:label: eq:sol-clsr-NDR-def
\mathsf N=\int H^2\,\dd\eta,\qquad
\mathsf D_{k\ell}=\int H^{bc}(\partial_bH)_{km}(\partial_cH)_{m\ell}\,\dd\eta,\qquad
\mathsf R=\mathsf N-\mathsf D,
```

following the manuscript statement, which *defines* $\mathsf R=\mathsf N-\mathsf D$; [](#prop:sol-clsr-anticommutator) identifies $\mathsf R$ with the anticommutator integral $\tfrac12\int\{H,A+Q\}\,\dd\eta$ used by the route file. $\mathsf N$ is finite by [](#eq:sol-clsr-Hbound); finiteness of $\mathsf D$ is *proved* below ([](#lem:sol-clsr-D-finite)), not assumed. Finally, in isotropic position the linear CMH quotient is

$$
Q_{\mathrm{lin}}(\mu)=\lmax(\mathsf N)
=\sup_{\abs a=1}\int\abs{Ha}^2\dd\eta .
$$

**Refined statement.**

:::{prf:theorem} Spectral resolution of the linear-sector gate matrices; refined form of [](#lem:cmh-linear-spectral-resolution)
:label: thm:sol-clsr-main
Let the map be as in [](#def:sol-clsr-class), with the import [](#eq:sol-clsr-Hbound). For a unit vector $a\in\R^n$ put $u_a=\inner a{\nabla\psi}$, so that the column is $Ha=\nabla\inner a{\nabla\psi}=\nabla u_a$ (componentwise $(Ha)_i=H_{ik}a_k$; for coordinate vectors, $u_b=\partial_b\psi$). Then:

(it:sol-clsr-a)=
(a) (Symmetric form and pullback.) Pointwise on $\R^n$,

$$
\calL f:=H^{ij}f_{ij}-(V_i\circ\nabla\psi)f_i
=e^{\psi}\,\partial_i\bigl(e^{-\psi}H^{ij}\partial_jf\bigr),
$$

and for every smooth $g$ on $\operatorname{int}P$, $\nabla_y(g\circ\nabla\psi)=H\,(\nabla_xg\circ\nabla\psi)$ and $\calL(g\circ\nabla\psi)=(L_\mu g)\circ\nabla\psi$: $\calL$ is the source pullback of the certified Stein generator, $U\Aop U^{-1}$ is the self-adjoint operator of the source form $\calE(f)=\int\inner{H^{-1}\nabla f}{\nabla f}\dd\eta$, and the CMH numerator field $\tau\nabla_xg$ pulls back to the plain Euclidean source gradient $\nabla_yf$ of $f=g\circ\nabla\psi$.

(it:sol-clsr-b)=
(b) (Eigenfunctions and gap.) The functions $u_1,\dots,u_n$ are bounded, centered, orthonormal in $L^2(\eta)$, lie in $\Dom(\Aop)$, and satisfy $\Aop u_b=u_b$. Brascamp–Lieb gives $\inner f{\Aop f}\ge\norm f_2^2$ for every centered $f\in\Dom(\calE)$; hence the spectrum of $\Aop$ on $\one^\perp$ is contained in $[1,\infty)$ and the spectral gap of $\Aop$ equals $1$ exactly, attained at each $u_b$.

(it:sol-clsr-c)=
(c) (Weak column equation, normalization, orthogonality.) $A\succeq0$ and $Q\succeq0$ pointwise, $\calL H+H=A+Q$ pointwise, the entries of $A+Q$ are in $L^1(\eta)$ with

$$
\int(A+Q)\,\dd\eta=\Id ,
$$

so in particular $(A+Q)a\in L^1(\eta;\R^n)$. The columns $Ha=\nabla\inner a{\nabla\psi}$ lie in the form domain $\Dom(\calE)$, componentwise, and satisfy the column equation in the weak form

```{math}
:label: eq:sol-clsr-weak-column
\calE\bigl(f,(Ha)_i\bigr)
=\bigl\langle f,(Ha)_i\bigr\rangle_{L^2(\eta)}
-\bigl\langle f,\bigl((A+Q)a\bigr)_i\bigr\rangle_{L^2(\eta),L^1}
```

for every bounded smooth finite-energy $f$, i.e. every $f\in C^\infty(\R^n)\cap L^\infty$ with $\int\inner{H^{-1}\nabla f}{\nabla f}\dd\eta<\infty$ (the class $\mathfrak B$ of [](#lem:sol-clsr-form-membership), every member of which lies in $\Dom(\calE)$; in particular every core element and every $u_b$). Consequently $(A+Q)a$ is orthogonal to every $u_b$: $\int u_b\,\bigl((A+Q)a\bigr)_i\,\dd\eta=0$ for all $i,b$. This weak form is exactly the column equation asserted by [](#lem:cmh-linear-spectral-resolution); no membership $(Ha)_i\in\Dom(\Aop)$ is asserted ([](#rem:sol-clsr-weak-vs-strong)).

(it:sol-clsr-d)=
(d) (Resolution.) Decompose, componentwise and orthogonally in $L^2(\eta)$,

$$
Ha=a\cdot\one+\sum_b(M_a)_{\cdot b}\,u_b+v,
\qquad
(M_a)_{ib}=\inner{(Ha)_i}{u_b}=a_k\int\psi_{kib}\,\dd\eta,
$$

with each $v_i\perp\one,u_1,\dots,u_n$; here $U:=\operatorname{span}\{u_1,\dots,u_n\}$ (which may be a proper subspace of the full eigenspace $\ker(\Aop-1)$; nothing below assumes otherwise), and the tensor $M_{kib}=\int\psi_{kib}\,\dd\eta$ is totally symmetric with $(M_a)_{ib}=(\Theta_ba)_i$ for $\Theta_b:=\int\partial_bH\,\dd\eta$. Then, with $\norm{M_a}^2:=\sum_{i,b}(M_a)_{ib}^2$, $\norm v^2:=\sum_i\norm{v_i}_{L^2(\eta)}^2$, and all $\Aop$-pairings read as quadratic-form values,

```{math}
:label: eq:sol-clsr-resolution
\boxed{\;
a^\top\mathsf Na=1+\norm{M_a}^2+\norm v^2,\qquad
a^\top\mathsf Da=\norm{M_a}^2+\inner v{\Aop v},\qquad
a^\top\mathsf Ra=1-\inner v{(\Aop-1)v},\;}
```

where $\inner v{\Aop v}:=\sum_i\calE(v_i)$ is the closed-form value (written $\calE(v,v)$ in [](#lem:cmh-linear-spectral-resolution); no membership $v_i\in\Dom(\Aop)$ is asserted) and $T_a:=\inner v{(\Aop-1)v}=\sum_i[\calE(v_i)-\norm{v_i}_2^2]\ge0$. In particular $\mathsf N-\Id\preceq\mathsf D$.

(it:sol-clsr-e)=
(e) (Corollaries C1–C5.)

- $\mathsf R\preceq\Id$, and $a^\top\mathsf Ra=1$ for a unit $a$ if and only if every component of the column fluctuation $Ha-a\cdot\one$ lies in the eigenspace $\ker(\Aop-1)$ (“spectrally pure at the gap”).

- For $\rho>0$, $\beta\in\R$, the bootstrap $(\mathrm{AB})_{\rho,\beta}$: $\mathsf R\succeq\rho\mathsf N-\beta\Id$ holds at the map if and only if for every unit $a$

  ```{math}
  :label: eq:sol-clsr-channel
  T_a+\rho\bigl(\norm{M_a}^2+\norm v^2\bigr)\le1+\beta-\rho .
  ```

  Since $T_a\ge0$, $(\mathrm{AB})_{\rho,\beta}$ implies $Q_{\mathrm{lin}}=\lmax(\mathsf N)\le(1+\beta)/\rho$.

- $\mathsf R\succeq\mathsf D$ holds iff $\norm{M_a}^2+\inner v{(2\Aop-1)v}\le1$ for every unit $a$; it implies $\sum_b\Theta_b^2\preceq\Id$, $\norm v^2\le1$, and $\lmax(\mathsf N)\le2$.

- For the conclusion $Q_{\mathrm{lin}}\le(1+\beta)/\rho$ it suffices that [](#eq:sol-clsr-channel) hold at one top eigendirection $a_*$ of $\mathsf N$.

- Summed over an orthonormal basis, [](#eq:sol-clsr-resolution) shows that the proved trace inequality $\Tr\mathsf R\ge\Tr\mathsf D$ of part [(f)](#it:sol-clsr-f) is exactly the basis-averaged form of [](#eq:sol-clsr-channel) at $(\rho,\beta)=(\tfrac12,0)$; the open content of $(\mathrm{AB})$ is its direction-wise de-averaging.

(it:sol-clsr-f)=
(f) (Unconditional dimension-dependent retention.) $\mathsf D\succeq0$, $\Tr(H(A+Q))\ge\Tr\bigl(H^{bc}(\partial_bH)(\partial_cH)\bigr)$ pointwise (the cyclic square), and consequently

$$
\Tr\mathsf R\ge\Tr\mathsf D,\qquad
\Tr\mathsf N\le2n,\qquad
\Tr\mathsf D\le n,\qquad
\mathsf R\succeq\mathsf N-n\,\Id,\qquad
Q_{\mathrm{lin}}\le n+1 .
$$

(it:sol-clsr-g)=
(g) (Products.) If $\mu=\mu_1\otimes\cdots\otimes\mu_n$ is a finite product of centered, variance-one, one-dimensional laws each of the regular class of [](#def:sol-clsr-class), then all matrices block-diagonalize and

$$
\mathsf R-\mathsf D
=\diag_k\int V_k''(\psi_k')\,(\psi_k'')^3\,e^{-\psi_k}\,\dd y_k\;\succeq\;0,
$$

so $\mathsf R\succeq\mathsf D$, equivalently $\mathsf R\succeq\tfrac12\mathsf N$, holds with the sharp constants on every such product.
:::

:::{prf:remark} Weak versus strong column equation
:label: rem:sol-clsr-weak-vs-strong
[](#lem:cmh-linear-spectral-resolution) states the column equation in the weak form: the columns $Ha$ lie in $\Dom(\calE)$ and satisfy [](#eq:sol-clsr-weak-column) for every bounded smooth finite-energy $f$, with $(A+Q)a\in L^1(\eta)$. That is exactly what part [(c)](#it:sol-clsr-c) proves, and it is what every downstream identity of this dossier uses (the resolution of part [(d)](#it:sol-clsr-d) tests [](#eq:sol-clsr-weak-column) against $f=(Ha)_i$ and $f=u_b$, both in $\mathfrak B$). The strong (operator-domain) form — $(Ha)_i\in\Dom(\Aop)$ with $\Aop(Ha)_i=(Ha)_i-((A+Q)a)_i$ in $L^2(\eta)$, i.e. the operator identity $(1-\Aop)(Ha)=(A+Q)a$ — is *not* part of the lemma and is not claimed here. It is a separate open question on the compact-target class: by [](#rem:sol-clsr-gap) it is *equivalent* to the additional integrability $\Tr Q\in L^2(\eta)$, which this dossier does not establish on the whole class. It does hold for the products of part [(g)](#it:sol-clsr-g), where $\Tr Q$ is bounded ([](#rem:sol-clsr-product-strong)).
:::

## 1\. Pointwise Monge–Ampère calculus (part [(a)](#it:sol-clsr-a) and the pointwise half of [(c)](#it:sol-clsr-c))

All identities in this subsection are pointwise on $\R^n$ and use only smoothness and strict convexity of $\psi$ and smoothness of $V$; no integration is performed.

The Monge–Ampère equation, i.e. the change of variables in $(\nabla\psi)_\#\eta=\mu$, reads

```{math}
:label: eq:sol-clsr-MA
\log\det H(y)=-\psi(y)+V(\nabla\psi(y)) .
```

Differentiating in $y_k$, with $\partial_k\log\det H=H^{ij}\psi_{ijk}$:

```{math}
:label: eq:sol-clsr-MA1
H^{ij}\psi_{ijk}=-\psi_k+(V_i\circ\nabla\psi)H_{ik} .
\tag{MA1}
```

:::{prf:lemma} Symmetric form
:label: lem:sol-clsr-symmetric-form
$\partial_iH^{ij}=\psi_bH^{bj}-(V_j\circ\nabla\psi)$, and consequently, for every $f\in C^\infty(\R^n)$,

$$
\calL f=H^{ij}f_{ij}-(V_j\circ\nabla\psi)f_j
=e^{\psi}\,\partial_i\bigl(e^{-\psi}H^{ij}\partial_jf\bigr).
$$
:::

:::{prf:proof}
$\partial_iH^{ij}=-H^{ia}(\partial_iH_{ab})H^{bj}=-H^{bj}\,(H^{ia}\psi_{iab})$. By [](#eq:sol-clsr-MA1) with $k=b$, $H^{ia}\psi_{iab}=-\psi_b+(V_i\circ\nabla\psi)H_{ib}$, so $\partial_iH^{ij}=H^{bj}\psi_b-(V_i\circ\nabla\psi)H_{ib}H^{bj}=\psi_bH^{bj}-(V_j\circ\nabla\psi)$. Then

$$
e^{\psi}\partial_i(e^{-\psi}H^{ij}f_j)
=H^{ij}f_{ij}+(\partial_iH^{ij})f_j-\psi_iH^{ij}f_j
=H^{ij}f_{ij}-(V_j\circ\nabla\psi)f_j .
$$
:::

:::{prf:lemma} Pullback dictionary
:label: lem:sol-clsr-pullback
For $g\in C^\infty(\operatorname{int}P)$ and $f=g\circ\nabla\psi$:

$$
\nabla_yf=H\,(\nabla_xg\circ\nabla\psi),\qquad
\calL f=(L_\mu g)\circ\nabla\psi,\qquad
(\tau\nabla_xg)\circ\nabla\psi=\nabla_yf,\qquad
\inner{\tau\nabla g}{\nabla g}\circ\nabla\psi=\inner{H^{-1}\nabla f}{\nabla f}.
$$
:::

:::{prf:proof}
Chain rule: $f_i=g_a(\nabla\psi)\psi_{ai}=(H\nabla g)_i$ by symmetry of $H$, which is the first identity; the third follows because $\tau(\nabla\psi(y))=H(y)$, so $\tau\nabla g\circ\nabla\psi=H\cdot H^{-1}\nabla f=\nabla f$; the fourth is then immediate. For the second: $f_{ij}=g_{ab}\psi_{ai}\psi_{bj}+g_a\psi_{aij}$, so $H^{ij}f_{ij}=g_{ab}H_{ab}+g_a\,H^{ij}\psi_{aij} =\Tr\bigl((D^2g)\,H\bigr)+g_a\bigl(-\psi_a+(V_i\circ\nabla\psi)H_{ia}\bigr)$ by [](#eq:sol-clsr-MA1), using $H^{ij}\psi_{ai}\psi_{bj}=(HH^{-1}H)_{ab}=H_{ab}$. Subtracting $(V_i\circ\nabla\psi)f_i=(V_i\circ\nabla\psi)g_aH_{ai}$ leaves $\calL f=\bigl[\Tr(\tau D^2g)-x\cdot\nabla g\bigr]\circ\nabla\psi=(L_\mu g)\circ\nabla\psi$, since $x=\nabla\psi(y)$ and $g_a\psi_a=(x\cdot\nabla g)\circ\nabla\psi$.
:::

[](#lem:sol-clsr-pullback) proves part [(a)](#it:sol-clsr-a): $U$ intertwines $\calL$ with $L_\mu$ on smooth functions, hence intertwines the closed form $\calE(f)=\int\inner{H^{-1}\nabla f}{\nabla f}\dd\eta$ with the certified target form, and the CMH numerator $\E_\mu\abs{\tau\nabla g}^2$ (isotropic $\Sigma=\Id$) is $\int\abs{\nabla_yf}^2\dd\eta$: on this class the CMH inequality for pullback tests reads $\int\abs{\nabla_yf}^2\dd\eta\le C\int(\calL f)^2\dd\eta$.

:::{prf:lemma} Twice-differentiated Monge–Ampère and positivity
:label: lem:sol-clsr-MA2
Pointwise, $\calL H_{k\ell}+H_{k\ell}=A_{k\ell}+Q_{k\ell}$ with $A,Q$ of [](#eq:sol-clsr-AQ-def), and $A\succeq0$, $Q\succeq0$.
:::

:::{prf:proof}
Differentiate [](#eq:sol-clsr-MA1) in $y_\ell$, using $\partial_\ell H^{ij}=-H^{ia}\psi_{ab\ell}H^{bj}$:

$$
-H^{ia}H^{bj}\psi_{ab\ell}\psi_{ijk}+H^{ij}\psi_{ijk\ell}
=-\psi_{k\ell}+(V_{im}\circ\nabla\psi)\psi_{m\ell}H_{ik}
+(V_i\circ\nabla\psi)\psi_{ik\ell} .
$$

Since $\psi_{ijk\ell}=\partial_{ij}H_{k\ell}$ and $\psi_{ik\ell}=\partial_iH_{k\ell}$, rearranging gives

$$
\calL H_{k\ell}
=H^{ia}H^{bj}\psi_{ab\ell}\psi_{ijk}-H_{k\ell}
+H_{ik}(V_{im}\circ\nabla\psi)H_{m\ell},
$$

and the first term equals $\Tr(H^{-1}\partial_kH\,H^{-1}\partial_\ell H)=Q_{k\ell}$ by total symmetry of $\psi_{abc}$, while the last is $A_{k\ell}$. Positivity: for $c\in\R^n$, $c^\top Ac=\inner{(D^2V\circ\nabla\psi)\,Hc}{Hc}\ge0$ by log-concavity of the target ($D^2V\succeq0$ on $\operatorname{int}P$, and $\nabla\psi(y)\in\operatorname{int}P$), and $c^\top Qc=\Tr\bigl(H^{-1}S_cH^{-1}S_c\bigr) =\norm{H^{-1/2}S_cH^{-1/2}}_{\HS}^2\ge0$ with $S_c=c_k\partial_kH$ symmetric.
:::

## 2\. The cutoff calculus

This subsection is the analytic core: it justifies every integration by parts against the non-compactly-supported core, using only the objects of [](#def:sol-clsr-class) and the import [](#eq:sol-clsr-Hbound).

:::{prf:lemma} Coercivity
:label: lem:sol-clsr-coercive
$\psi$ has compact sublevel sets $\{\psi\le t\}$ and attains its minimum.
:::

:::{prf:proof}
Suppose some sublevel set $\{\psi\le t_0\}$ is unbounded. A closed convex unbounded set contains a ray $\{y_0+sv:s\ge0\}$, $\abs v=1$; convexity of $\psi$ with $\sup_s\psi(y_0+sv)\le t_0$ forces the recession slope of $\psi$ in direction $v$ to be $\le0$, i.e. $s\mapsto\psi(y+sv)$ is nonincreasing for *every* $y$. Then by Fubini along lines in direction $v$, $\int e^{-\psi}\dd y\ge\int_0^\infty e^{-\psi(y+sv)}\dd s\cdot (\text{transverse integration})=\infty$ for any $y$ with $e^{-\psi(y)}>0$, contradicting $\eta(\R^n)=1$. Hence all sublevel sets are compact and the (continuous) minimum is attained.
:::

Fix once and for all $m_0>\min\psi+1$ and, for $m\ge m_0$, a smooth nonincreasing $\chi_m:\R\to[0,1]$ with $\chi_m=1$ on $(-\infty,m]$, $\chi_m=0$ on $[2m,\infty)$, and $\abs{\chi_m'}\le2/m$. Set

$$
\zeta_m=\chi_m(\psi)\in C_c^\infty(\R^n),\qquad
S_m=\operatorname{supp}\nabla\zeta_m\subseteq\{m\le\psi\le2m\} .
$$

Along the dyadic subsequence $m=2^jm_0$ we may and do choose the $\chi_m$ nested, so that $\zeta_m\uparrow1$ pointwise. Note $\abs{\nabla\zeta_m}\le(2/m)\abs{\nabla\psi}\le2R/m$ uniformly, since $\nabla\psi\in P$.

:::{prf:lemma} Divergence identities
:label: lem:sol-clsr-ibp
(i) For $u,\phi\in C^\infty(\R^n)$ with $\phi$ compactly supported, $\int\phi\,\calL u\,\dd\eta=-\int\inner{H^{-1}\nabla\phi}{\nabla u}\,\dd\eta$. (ii) For $X\in C^\infty(\R)$ with $X'$ vanishing on $[t,\infty)$ for some $t\in\R$, $\int\calL\bigl(X(\psi)\bigr)\dd\eta=0$, where $\calL(X(\psi))=X''(\psi)\,\Gamma+X'(\psi)\bigl(n-\inner{\nabla V\circ\nabla\psi}{\nabla\psi}\bigr)$ and $\Gamma:=\inner{H^{-1}\nabla\psi}{\nabla\psi}$.
:::

:::{prf:proof}
(i) is the divergence theorem applied to the smooth compactly supported field $\phi\,e^{-\psi}H^{-1}\nabla u$, using [](#lem:sol-clsr-symmetric-form). For (ii): $\partial_i X(\psi)=X'\psi_i$ and $\partial_{ij}X(\psi)=X''\psi_i\psi_j+X'H_{ij}$ give the displayed formula for $\calL(X(\psi))$; the field $e^{-\psi}H^{-1}X'(\psi)\nabla\psi$ is smooth with support in the compact set $\{\psi\le t\}$ ([](#lem:sol-clsr-coercive); no lower bound on $\operatorname{supp}X'$ is needed because $\psi$ is bounded below), so its divergence integrates to zero.
:::

:::{prf:lemma} Cutoff energy lemma
:label: lem:sol-clsr-cutoff
$\displaystyle \kappa_m:=\int\inner{H^{-1}\nabla\zeta_m}{\nabla\zeta_m}\,\dd\eta \;\le\;\frac{2\,(n+c_VR)}{m}\xrightarrow[m\to\infty]{}0 .$
:::

:::{prf:proof}
Apply [](#lem:sol-clsr-ibp)(ii) with $X'=\chi_m$:

$$
\int\chi_m'(\psi)\,\Gamma\,\dd\eta
=-\int\chi_m(\psi)\,\bigl(n-\inner{\nabla V\circ\nabla\psi}{\nabla\psi}\bigr)\dd\eta .
$$

Since $\abs{\inner{\nabla V\circ\nabla\psi}{\nabla\psi}}\le c_VR$ and $0\le\chi_m\le1$, and $\chi_m'\le0$,

$$
\int\abs{\chi_m'(\psi)}\,\Gamma\,\dd\eta\le n+c_VR .
$$

Finally $\inner{H^{-1}\nabla\zeta_m}{\nabla\zeta_m}=\chi_m'(\psi)^2\,\Gamma \le\tfrac2m\abs{\chi_m'(\psi)}\,\Gamma$, and integrate.
:::

:::{prf:lemma} Pointwise dominations
:label: lem:sol-clsr-domination
Let $\mathfrak g:=H^{bc}\,\partial_bH_{ij}\,\partial_cH_{ij}\ge0$ (full contraction; the integrand of $\Tr\mathsf D$). Then, pointwise:

(i) for every $c\in\R^n$, $\inner{H^{-1}\nabla(c^\top Hc)}{\nabla(c^\top Hc)}\le\abs c^4\,\mathfrak g$;

(ii) $\sum_b\norm{\partial_bH}_{\HS}^2\le\norm H_\op\,\mathfrak g\le 2R^2\,\mathfrak g$; in particular each $\abs{\psi_{aib}}\le(2R^2\,\mathfrak g)^{1/2}$;

(iii) $\abs{\sum_{i,j}H_{ij}\,\inner{H^{-1}\nabla\zeta}{\nabla H_{ij}}} \le\norm H_{\HS}\,\inner{H^{-1}\nabla\zeta}{\nabla\zeta}^{1/2}\,\mathfrak g^{1/2}$ for every smooth $\zeta$.
:::

:::{prf:proof}
(i) Let $G_b=c^\top(\partial_bH)c$, so $\nabla(c^\top Hc)=G$. For any $\xi\in\R^n$, with $S_\xi=\xi_b\partial_bH$, $\xi\cdot G=\inner{S_\xi}{cc^\top}_{\HS}\le\norm{S_\xi}_{\HS}\abs c^2$. Hence

$$
\inner{H^{-1}G}G=\sup_{\xi\ne0}\frac{(\xi\cdot G)^2}{\inner{H\xi}\xi}
\le\abs c^4\sup_{\xi\ne0}\frac{\norm{S_\xi}_{\HS}^2}{\inner{H\xi}\xi}
=\abs c^4\sup_{\abs\zeta=1}\norm{S_{H^{-1/2}\zeta}}_{\HS}^2
\le\abs c^4\sum_\beta\norm{S_{H^{-1/2}e_\beta}}_{\HS}^2
=\abs c^4\,\mathfrak g,
$$

because $\sum_\beta\norm{S_{H^{-1/2}e_\beta}}_{\HS}^2 =\sum_{ij}\inner{H^{-1}\nabla H_{ij}}{\nabla H_{ij}}=\mathfrak g$. (ii) With the positive semidefinite Gram matrix $\Gamma_{bc}=\inner{\partial_bH}{\partial_cH}_{\HS}$ one has $\mathfrak g=\Tr(H^{-1}\Gamma)\ge\lmin(H^{-1})\Tr\Gamma=\norm H_\op^{-1}\sum_b\norm{\partial_bH}_{\HS}^2$, and [](#eq:sol-clsr-Hbound) bounds $\norm H_\op$. The entry bound follows since $\psi_{aib}^2\le\norm{\partial_bH}_{\HS}^2$. (iii) Cauchy–Schwarz in the $H^{-1}$-inner product for each $(i,j)$, then Cauchy–Schwarz over the index sum.
:::

:::{prf:lemma} Finite total column energy
:label: lem:sol-clsr-D-finite
$\displaystyle\Tr\mathsf D=\int\mathfrak g\,\dd\eta\le\Tr\mathsf N\le n\,(2R^2)^2<\infty$, and

```{math}
:label: eq:sol-clsr-trace-identity
\int\Tr\bigl(H(A+Q)\bigr)\dd\eta=\Tr\mathsf N-\Tr\mathsf D<\infty,
\qquad \Tr\bigl(H(A+Q)\bigr)\ge0\ \text{pointwise}.
```
:::

:::{prf:proof}
Set $\mathcal D_m=\int\zeta_m^2\,\mathfrak g\,\dd\eta$ and $\mathcal T_m=\int\zeta_m^2\,\Tr(H(A+Q))\,\dd\eta$; both are finite (compact support, smooth integrands) and $\mathcal T_m\ge0$ since $\Tr(H(A+Q))=\Tr\bigl(H^{1/2}(A+Q)H^{1/2}\bigr)\ge0$ pointwise ([](#lem:sol-clsr-MA2)). For each pair $(i,j)$ apply [](#lem:sol-clsr-ibp)(i) with $u=H_{ij}$, $\phi=\zeta_m^2H_{ij}$ and sum:

$$
\mathcal D_m
=-\int\zeta_m^2\,H_{ij}\,\calL H_{ij}\,\dd\eta
-2\int\zeta_m\,H_{ij}\,\inner{H^{-1}\nabla\zeta_m}{\nabla H_{ij}}\,\dd\eta .
$$

By [](#lem:sol-clsr-MA2), $-H_{ij}\calL H_{ij}=\Tr(H^2)-\Tr(H(A+Q))$, so

$$
\mathcal D_m+\mathcal T_m
=\int\zeta_m^2\,\Tr(H^2)\,\dd\eta+\mathrm{Err}_m,
\qquad
\abs{\mathrm{Err}_m}\le2\,\norm{H}_{\HS,\infty}\,\kappa_m^{1/2}\,\mathcal D_m^{1/2}
\le\eps_m\,\mathcal D_m^{1/2},
$$

using [](#lem:sol-clsr-domination)(iii), Cauchy–Schwarz in $\dd\eta$, and $\zeta_m\le1$; here $\norm H_{\HS,\infty}\le\sqrt n\,2R^2$ by [](#eq:sol-clsr-Hbound) and $\eps_m:=2\sqrt n\,2R^2\,\kappa_m^{1/2}\to0$ by [](#lem:sol-clsr-cutoff). Dropping $\mathcal T_m\ge0$, $\mathcal D_m\le\Tr\mathsf N+\eps_m\mathcal D_m^{1/2}$, a quadratic inequality in $\mathcal D_m^{1/2}<\infty$, whence $\mathcal D_m\le\bigl(\eps_m/2+\sqrt{\Tr\mathsf N+\eps_m^2/4}\bigr)^2$. Along the nested dyadic sequence $\zeta_m^2\uparrow1$, monotone convergence gives $\int\mathfrak g\,\dd\eta=\lim\mathcal D_m\le\limsup(\cdots)=\Tr\mathsf N$. Then $\mathrm{Err}_m\to0$, and passing to the limit in the displayed identity (monotone convergence on all three nonnegative terms) yields [](#eq:sol-clsr-trace-identity).
:::

:::{prf:lemma} Normalization
:label: lem:sol-clsr-normalization
$\Tr(A+Q)\in L^1(\eta)$, every entry of $A+Q$ is in $L^1(\eta)$, and $\int(A+Q)\,\dd\eta=\Id$.
:::

:::{prf:proof}
Fix a unit $c$ and let $h=c^\top Hc\in[0,2R^2]$. By [](#lem:sol-clsr-MA2), $c^\top(A+Q)c=\calL h+h\ge0$ pointwise. By [](#lem:sol-clsr-ibp)(i) with $\phi=\zeta_m$, $u=h$:

$$
\int\zeta_m\,c^\top(A+Q)c\,\dd\eta
=\int\zeta_m h\,\dd\eta-\int\inner{H^{-1}\nabla\zeta_m}{\nabla h}\,\dd\eta .
$$

The error term is bounded by $\kappa_m^{1/2}\bigl(\int_{S_m}\inner{H^{-1}\nabla h}{\nabla h}\dd\eta\bigr)^{1/2} \le\kappa_m^{1/2}\bigl(\int\mathfrak g\,\dd\eta\bigr)^{1/2}\to0$ by [](#lem:sol-clsr-domination)(i) and [](#lem:sol-clsr-D-finite). Since $\zeta_m\uparrow1$ and the integrand is nonnegative, monotone convergence on the left and dominated convergence on $\int\zeta_mh\,\dd\eta\to\int h\,\dd\eta=c^\top\Id c=1$ (using $\int H\,\dd\eta=\E_\mu\tau=\Id$, the certified isotropic normalization) give $\int c^\top(A+Q)c\,\dd\eta=1=\abs c^2$. Polarizing over $c$ (all quantities finite) gives $\int(A+Q)\dd\eta=\Id$ and, taking $c=e_k$ and summing, $\Tr(A+Q)\in L^1$; entries are dominated by the trace of a positive semidefinite matrix.
:::

:::{prf:lemma} Form membership and weak pairings
:label: lem:sol-clsr-form-membership
Let $\mathfrak B$ be the set of $f\in C^\infty(\R^n)$ (source coordinates) that are bounded with $\calE^0(f):=\int\inner{H^{-1}\nabla f}{\nabla f}\dd\eta<\infty$. Then:

(i) every $f\in\mathfrak B$ lies in $\Dom(\calE)$ (the closed form domain) with $\calE(f)=\calE^0(f)$, and $\calE(f,g)=\int\inner{H^{-1}\nabla f}{\nabla g}\dd\eta$ for $f,g\in\mathfrak B$;

(ii) every column component $H_{ai}$, every $u_b$, and every core pullback belongs to $\mathfrak B$;

(iii) for every $f\in\mathfrak B$ and every unit $a$, the weak column equation [](#eq:sol-clsr-weak-column) holds, all pairings being absolutely convergent.
:::

:::{prf:proof}
(i) Let $f\in\mathfrak B$ and let $g=f\circ(\nabla\psi)^{-1}$, smooth and bounded on $\operatorname{int}P$. The target-side cutoff $\zeta_m\circ(\nabla\psi)^{-1}$ is smooth with support $\nabla\psi(\{\psi\le2m\})$, a compact subset of $\operatorname{int}P$ ([](#lem:sol-clsr-coercive) and the diffeomorphism property); hence $(\zeta_m\circ(\nabla\psi)^{-1})\,g$ extends by zero to an element of $C_c^\infty(\R^n)$ and $\zeta_mf$ corresponds to a *core* element of $\mathscr D$. Moreover

$$
\calE^0(\zeta_mf-f)
\le2\int(1-\zeta_m)^2\inner{H^{-1}\nabla f}{\nabla f}\dd\eta
+2\norm f_\infty^2\,\kappa_m\longrightarrow0
$$

by dominated convergence and [](#lem:sol-clsr-cutoff), while $\zeta_mf\to f$ in $L^2(\eta)$. Closedness of $\calE$ gives $f\in\Dom(\calE)$ with $\calE(f)=\lim\calE^0(\zeta_mf) =\calE^0(f)$; the bilinear statement follows by polarization ($\mathfrak B$ is a vector space). (ii) $H_{ai}$ is smooth, bounded by [](#eq:sol-clsr-Hbound), and $\calE^0(H_{ai})\le\int\mathfrak g\,\dd\eta<\infty$ ([](#lem:sol-clsr-D-finite)); $u_b=\partial_b\psi$ is smooth, bounded by $R$, with $\calE^0(u_b)=\int H^{cd}H_{bc}H_{bd}\dd\eta=\int H_{bb}\dd\eta=1$; a core pullback $f=c+g\circ\nabla\psi$, $g\in C_c^\infty$, is smooth and bounded with $\nabla f=H\nabla g$ bounded, hence $\calE^0(f)=\int\inner{H\nabla g}{\nabla g}\dd\eta\le\norm{\nabla g}_\infty^2\,n<\infty$. (iii) Fix $f\in\mathfrak B$ and write $w_i=(Ha)_i=a_kH_{ki}$, a linear combination of entries, so $w_i\in\mathfrak B$. [](#lem:sol-clsr-ibp)(i) with $\phi=\zeta_mf$, $u=w_i$:

$$
\int\zeta_mf\,\calL w_i\,\dd\eta
=-\int\zeta_m\inner{H^{-1}\nabla f}{\nabla w_i}\dd\eta
-\int f\inner{H^{-1}\nabla\zeta_m}{\nabla w_i}\dd\eta .
$$

As $m\to\infty$: the left side converges to $\int f\,\calL w_i\,\dd\eta$ by dominated convergence, since $\calL w_i=\bigl((A+Q)a\bigr)_i-w_i$ ([](#lem:sol-clsr-MA2)) is dominated by $\Tr(A+Q)+2R^2\in L^1$ ([](#lem:sol-clsr-normalization), positivity of $A+Q$) and $f$ is bounded; the first right-hand term converges to $-\int\inner{H^{-1}\nabla f}{\nabla w_i}\dd\eta=-\calE(f,w_i)$ by dominated convergence (the integrand is dominated by the product of two $L^2$ functions); the second is bounded in absolute value by $\norm f_\infty\,\kappa_m^{1/2}\,\calE^0(w_i)^{1/2}\to0$. Rearranging gives [](#eq:sol-clsr-weak-column).
:::

## 3\. Eigenstructure and the Brascamp–Lieb gap (part [(b)](#it:sol-clsr-b))

:::{prf:lemma} Linear coordinates are eigenfunctions
:label: lem:sol-clsr-eigen
Each $u_b=\partial_b\psi$ is bounded ($\abs{u_b}\le R$), centered, and the family $(u_b)_{b\le n}$ is orthonormal in $L^2(\eta)$. Moreover $u_b\in\Dom(\Aop)$ with $\Aop u_b=u_b$.
:::

:::{prf:proof}
$u_b=x_b\circ\nabla\psi$ with $x_b$ the target coordinate, so $\int u_b\,\dd\eta=\E_\mu X_b=0$ (centering) and $\int u_bu_c\,\dd\eta=\E_\mu[X_bX_c]=\delta_{bc}$ (isotropy) — no integration by parts is needed. Work in target coordinates. Choose $\chi\in C_c^\infty(\R^n)$ with $\chi=1$ on a neighborhood of $\overline P$; then $\ell_b:=(x_b\chi)|_{\operatorname{int}P}=x_b$ on the support and $\ell_b\in\mathscr D$ is a core element. For any core $f=c+F|_{\operatorname{int}P}$, $F\in C_c^\infty(\R^n)$, the certified weak Stein identity of [](#thm:regular-moment-map-compact-target) (in the ambient test form $\int x_iF\,\dd\mu=\int\tau_{ij}\partial_jF\,\dd\mu$, exactly as used by the certified recovery dossier) gives

$$
\calE^0(f,\ell_b)
=\E_\mu\inner{\tau\nabla f}{e_b}
=\int\tau_{bj}\,\partial_jF\,\dd\mu
=\int x_b\,F\,\dd\mu
=\int x_b\,f\,\dd\mu ,
$$

the last step because $\E_\mu X_b=0$ kills the constant. Both sides are continuous for the form norm of $f$ (Cauchy–Schwarz for the form; $x_b$ bounded for the pairing), and the core is dense in $\Dom(\calE)$ by construction of the closure, so $\calE(f,\ell_b)=\inner f{\ell_b}_{L^2(\mu)}$ for all $f\in\Dom(\calE)$. By definition of the self-adjoint operator of a closed form, $\ell_b\in\Dom(\Aop)$ and $\Aop\ell_b=\ell_b$. Transporting by $U$ gives the source statement; consistently, $\calL u_b=-u_b$ pointwise is exactly [](#eq:sol-clsr-MA1).
:::

:::{prf:lemma} Brascamp–Lieb gap
:label: lem:sol-clsr-BL
For every $f\in\Dom(\calE)$ with $\int f\,\dd\eta=0$, $\norm f_{L^2(\eta)}^2\le\calE(f)$. Hence the spectrum of $\Aop$ restricted to $\one^\perp$ is contained in $[1,\infty)$, and by [](#lem:sol-clsr-eigen) the spectral gap of $\Aop$ equals $1$ exactly, attained at each $u_b$.
:::

:::{prf:proof}
The Brascamp–Lieb inequality [@BrascampLieb1976] for the log-concave probability $\eta=e^{-\psi}\dd y$ with $D^2\psi=H\succ0$ states $\Var_\eta(f)\le\int\inner{H^{-1}\nabla f}{\nabla f}\dd\eta$ for every $C^1$ (or locally Lipschitz) $f$ for which the right side is finite; this applies to every core pullback (smooth, bounded, bounded gradient). For general $f\in\Dom(\calE)$ take core $f_k\to f$ in form norm: then $\Var(f_k)\to\Var(f)$ ($L^2$-convergence of functions and of their means) and $\calE(f_k)\to\calE(f)$, so the inequality passes to the closure. For centered $f$, $\Var(f)=\norm f_2^2$, i.e. $\inner f{\Aop f}\ge\norm f_2^2$ in the form sense on $\one^\perp\cap\Dom(\calE)$, which is the spectral statement. The value $1$ is attained because $\Aop u_b=u_b$ with $u_b\perp\one$.
:::

## 4\. The column equation and its compatibilities (part [(c)](#it:sol-clsr-c))

Parts of [(c)](#it:sol-clsr-c) already proved: positivity and the pointwise identity ([](#lem:sol-clsr-MA2)), $L^1$-normalization ([](#lem:sol-clsr-normalization)), form membership and the weak column equation [](#eq:sol-clsr-weak-column) ([](#lem:sol-clsr-form-membership)). It remains to record orthogonality and the third-moment identity.

:::{prf:lemma} Orthogonality of the source columns to the gap modes
:label: lem:sol-clsr-orthogonality
For all $i,b$ and every unit $a$: $\displaystyle\int u_b\,\bigl((A+Q)a\bigr)_i\,\dd\eta=0$ (absolutely convergent pairing).
:::

:::{prf:proof}
Take $f=u_b\in\mathfrak B$ in [](#eq:sol-clsr-weak-column): $\calE(u_b,w_i)=\inner{u_b}{w_i}-\int u_b\bigl((A+Q)a\bigr)_i\dd\eta$ with $w_i=(Ha)_i$. On the other hand, since $u_b\in\Dom(\Aop)$ with $\Aop u_b=u_b$ and $w_i\in\Dom(\calE)$, the form–operator pairing gives $\calE(u_b,w_i)=\inner{\Aop u_b}{w_i}=\inner{u_b}{w_i}$. Subtracting kills both inner products and leaves the claim. Absolute convergence: $\abs{u_b}\le R$ and $(A+Q)$ entries are in $L^1$.
:::

:::{prf:lemma} Third-moment tensor
:label: lem:sol-clsr-M
The numbers $M_{kib}:=\int\psi_{kib}\,\dd\eta$ are finite and totally symmetric in $(k,i,b)$, and

$$
\inner{H_{ki}}{u_b}_{L^2(\eta)}=M_{kib},\qquad\text{i.e.}\qquad
(M_a)_{ib}:=\inner{(Ha)_i}{u_b}=a_kM_{kib}=(\Theta_ba)_i,\quad
\Theta_b=\int\partial_bH\,\dd\eta .
$$
:::

:::{prf:proof}
Finiteness: $\abs{\psi_{kib}}\le(2R^2\mathfrak g)^{1/2}\in L^2(\eta)\subset L^1(\eta)$ by [](#lem:sol-clsr-domination)(ii) and [](#lem:sol-clsr-D-finite); symmetry is the symmetry of third derivatives. For the identity, integrate by parts with the cutoffs: $u_be^{-\psi}=\psi_be^{-\psi}=-\partial_b(e^{-\psi})$, so for each $m$, by the divergence theorem for the compactly supported field $\zeta_mH_{ki}e^{-\psi}e_b$,

$$
\int\zeta_m\,H_{ki}\,u_b\,\dd\eta
=\int\zeta_m\,\psi_{kib}\,\dd\eta+\int H_{ki}\,\partial_b\zeta_m\,\dd\eta .
$$

The last term is bounded by $2R^2\cdot(2R/m)\to0$ (uniform gradient bound on $\zeta_m$), and the first two converge by dominated convergence ($H_{ki}u_b$ bounded; $\psi_{kib}\in L^1$).
:::

:::{prf:remark} The precise open gap: strong column equation
:label: rem:sol-clsr-gap
For fixed $a$, the following are equivalent by the definition of the operator of a closed form: (a) $(Ha)_i\in\Dom(\Aop)$ for all $i$ with $\Aop(Ha)=(Ha)-(A+Q)a$ in $L^2(\eta;\R^n)$; (b) $(A+Q)a\in L^2(\eta;\R^n)$. Since $\abs{(A+Q)a}\le\Tr(A+Q)$ pointwise and $\Tr A\le n\,c_{V''}(2R^2)^2$ is bounded, (b) holds whenever $\Tr Q\in L^2(\eta)$. This dossier proves $\Tr Q\in L^1(\eta)$ ([](#lem:sol-clsr-normalization)) but *not* $\Tr Q\in L^2(\eta)$ on the general compact-target class. [](#lem:cmh-linear-spectral-resolution) asserts only the weak form [](#eq:sol-clsr-weak-column), which is proved ([](#lem:sol-clsr-form-membership)); the strong form (a) is therefore *not* a claim of the lemma, and whether it holds on the whole class is a separate open question, equivalent to $\Tr Q\in L^2(\eta)$. Every statement of [](#thm:sol-clsr-main) downstream uses only the weak form. On the products of part [(g)](#it:sol-clsr-g) the strong form does hold ([](#rem:sol-clsr-product-strong)).
:::

## 5\. Proof of the resolution (part [(d)](#it:sol-clsr-d))

Fix a unit $a$ and write $w_i=(Ha)_i$. By [](#lem:sol-clsr-form-membership), $w_i\in\Dom(\calE)$; by the certified normalization $\int H\,\dd\eta=\Id$, $\inner{w_i}{\one}=a_i$. Define

$$
v_i:=w_i-a_i\one-\sum_b(M_a)_{ib}\,u_b\;\in\;\Dom(\calE),
$$

so that $v_i\perp\one$ and $v_i\perp u_b$ for all $b$ by construction ([](#lem:sol-clsr-M) and $\int u_b\dd\eta=0$), and $v_i\in\mathfrak B$ (a finite linear combination of $\mathfrak B$-elements). This is the decomposition $Ha=a\cdot\one+\sum_b(M_a)_{\cdot b}u_b+v$ of the statement, with $U=\operatorname{span}\{u_1,\dots,u_n\}$; no claim is made that $U$ exhausts $\ker(\Aop-1)$, and no operator inverse is used.

*First identity.* Pointwise $\sum_iw_i^2=(H^2)_{aa}$, so $a^\top\mathsf Na=\sum_i\norm{w_i}_2^2$. The three parts of $w_i$ are pairwise orthogonal in $L^2(\eta)$ ($\one\perp u_b$ by centering; $\one,u_b\perp v_i$ by construction; $u_b\perp u_c$, $b\ne c$, by isotropy), so Pythagoras gives $\norm{w_i}_2^2=a_i^2+\sum_b(M_a)_{ib}^2+\norm{v_i}_2^2$; summing over $i$ with $\sum_ia_i^2=1$:

$$
a^\top\mathsf Na=1+\norm{M_a}^2+\norm v^2 .
$$

*Second identity.* By definition of $\mathsf D$ and [](#lem:sol-clsr-form-membership)(i),

$$
a^\top\mathsf Da
=\sum_i\int\inner{H^{-1}\nabla w_i}{\nabla w_i}\dd\eta
=\sum_i\calE(w_i).
$$

Expand $\calE(w_i)$ bilinearly. $\calE(\one,\cdot)=0$. For the $u$-modes, the form–operator pairing with $\Aop u_b=u_b$ gives $\calE(u_b,u_c)=\inner{u_b}{u_c}=\delta_{bc}$ and $\calE(u_b,v_i)=\inner{u_b}{v_i}=0$. Hence $\calE(w_i)=\sum_b(M_a)_{ib}^2+\calE(v_i)$, and summing over $i$:

$$
a^\top\mathsf Da=\norm{M_a}^2+\inner v{\Aop v},
\qquad \inner v{\Aop v}:=\sum_i\calE(v_i)<\infty .
$$

*Third identity.* Subtract, using the manuscript definition $\mathsf R=\mathsf N-\mathsf D$:

$$
a^\top\mathsf Ra
=1+\norm v^2-\inner v{\Aop v}
=1-\sum_i\bigl[\calE(v_i)-\norm{v_i}_2^2\bigr]
=1-T_a,
$$

and $T_a\ge0$ because each $v_i$ is centered and [](#lem:sol-clsr-BL) applies. This proves [](#eq:sol-clsr-resolution). Finally $a^\top(\mathsf N-\Id-\mathsf D)a=\norm v^2-\inner v{\Aop v}\le0$, i.e.\ $\mathsf N-\Id\preceq\mathsf D$ (the componentwise Brascamp–Lieb inequality of the probe, here a one-line consequence of the resolution). $\square$

:::{prf:proposition} Anticommutator representation of $\mathsf R$
:label: prop:sol-clsr-anticommutator
For every unit $a$ the integral $\tfrac12\,a^\top\!\int\{H,A+Q\}\,\dd\eta\,a =\int\inner{Ha}{(A+Q)a}\dd\eta$ converges absolutely and equals $a^\top\mathsf Na-a^\top\mathsf Da$. Hence $\mathsf R=\tfrac12\int\{H,A+Q\}\,\dd\eta$ and the identity $\mathsf N=\mathsf D+\mathsf R$ of the route file holds with $\mathsf R$ the anticommutator integral.
:::

:::{prf:proof}
Absolute convergence: $\abs{\inner{Ha}{(A+Q)a}}\le2R^2\,\Tr(A+Q)\in L^1$. Take $f=w_i\in \mathfrak B$ in the weak column equation [](#eq:sol-clsr-weak-column): $\int w_i\bigl((A+Q)a\bigr)_i\dd\eta=\norm{w_i}_2^2-\calE(w_i)$. Summing over $i$ gives $a^\top\mathsf Na-a^\top\mathsf Da$, and $\tfrac12a^\top\{H,A+Q\}a=\inner{Ha}{(A+Q)a}$ pointwise by symmetry of both matrices.
:::

## 6\. Corollaries C1–C5 (part [(e)](#it:sol-clsr-e))

*C1.* $a^\top\mathsf Ra=1-T_a\le1$ for every unit $a$, so $\mathsf R\preceq\Id$. Equality in direction $a$ means $T_a=0$, i.e. $\calE(v_i)=\norm{v_i}_2^2$ for every $i$. Each $v_i$ is centered, so its spectral measure under $\Aop$ is carried by $[1,\infty)$ ([](#lem:sol-clsr-BL)), and $\calE(v_i)-\norm{v_i}_2^2=\int_{[1,\infty)}(\lambda-1)\,\dd\inner{E_\lambda v_i}{v_i}=0$ iff the spectral measure of $v_i$ is concentrated at $\{1\}$, iff $v_i\in\ker(\Aop-1)$ (possibly $v_i=0$). Since each $u_b\in\ker(\Aop-1)$, this holds iff every component of the column fluctuation $Ha-a\cdot\one=\sum_b(M_a)_{\cdot b}u_b+v$ lies in $\ker(\Aop-1)$: spectral purity at the gap. Note the criterion refers to the *full* eigenspace $\ker(\Aop-1)$, of which $U$ may be a proper subspace; the dossier nowhere needs them to coincide.

*C2.* By the resolution, for a unit $a$,

$$
a^\top\mathsf Ra-\rho\,a^\top\mathsf Na+\beta
=1-T_a-\rho\bigl(1+\norm{M_a}^2+\norm v^2\bigr)+\beta,
$$

which is $\ge0$ iff [](#eq:sol-clsr-channel) holds. $(\mathrm{AB})_{\rho,\beta}$ is the conjunction over all unit $a$. If it holds, then since $T_a\ge0$, $\rho\,a^\top\mathsf Na\le1+\beta-T_a\le1+\beta$, so $Q_{\mathrm{lin}}=\lmax(\mathsf N)\le(1+\beta)/\rho$; this recovers the w3c01 bootstrap conclusion without using $\mathsf N-\Id\preceq\mathsf D$.

*C3.* $a^\top(\mathsf R-\mathsf D)a =1-T_a-\norm{M_a}^2-\inner v{\Aop v} =1-\norm{M_a}^2-\inner v{(2\Aop-1)v}$, using $T_a+\inner v{\Aop v}=2\inner v{\Aop v}-\norm v^2$. So $\mathsf R\succeq\mathsf D$ iff $\norm{M_a}^2+\inner v{(2\Aop-1)v}\le1$ for all unit $a$. Since $\inner v{(2\Aop-1)v}\ge\norm v^2\ge0$ ([](#lem:sol-clsr-BL)), this implies $\norm{M_a}^2\le1$ and $\norm v^2\le1$ for all $a$, hence $a^\top\mathsf Na\le2$. Finally $\norm{M_a}^2=\sum_{i,b}(\Theta_ba)_i^2=a^\top\bigl(\sum_b\Theta_b^2\bigr)a$ by [](#lem:sol-clsr-M) ($\Theta_b$ symmetric), so $\norm{M_a}^2\le1$ for all unit $a$ is exactly $\sum_b\Theta_b^2\preceq\Id$. Also, through $\mathsf N=\mathsf D+\mathsf R$ ([](#prop:sol-clsr-anticommutator) or the definition of $\mathsf R$), $\mathsf R\succeq\mathsf D\iff2\mathsf R\succeq\mathsf N\iff \mathsf R\succeq\tfrac12\mathsf N$.

*C4.* Let $a_*$ be a unit eigenvector of $\mathsf N$ at $\lmax(\mathsf N)$. If [](#eq:sol-clsr-channel) holds at $a_*$, then as in C2, $\rho\lmax(\mathsf N)=\rho\,a_*^\top\mathsf Na_*\le1+\beta$. Only the top direction is used.

*C5.* Summing [](#eq:sol-clsr-resolution) over an orthonormal basis $a=e_1,\dots,e_n$: $\Tr\mathsf N=n+\sum_a(\norm{M_{e_a}}^2+\norm{v^{(e_a)}}^2)$ and $\Tr\mathsf R=n-\sum_aT_{e_a}$. Hence the inequality $\sum_aT_{e_a}+\tfrac12\sum_a(\norm{M_{e_a}}^2+\norm{v^{(e_a)}}^2)\le\tfrac n2$ is literally equivalent to $\Tr\mathsf R\ge\tfrac12\Tr\mathsf N$, i.e. (via $\Tr\mathsf N=\Tr\mathsf D+\Tr\mathsf R$) to $\Tr\mathsf R\ge\Tr\mathsf D$ — which part [(f)](#it:sol-clsr-f) proves. Thus the Chen–Klartag-type trace inequality is exactly the orthonormal-basis average of the channel inequality [](#eq:sol-clsr-channel) at $(\rho,\beta)=(\tfrac12,0)$, and the open content of $(\mathrm{AB})$ is its direction-wise de-averaging. $\square$

:::{prf:remark} Linear tests inside CMH
:label: rem:sol-clsr-qlin-cmh
By [](#lem:sol-clsr-eigen), $g=\inner ax$ lies in $\Dom(\Aop)\setminus\ker\Aop$ with $\E_\mu(L_\mu g)^2=\E_\mu\inner ax^2=1$ and CMH numerator $\E_\mu\abs{\tau a}^2=a^\top\mathsf Na$. Hence $Q_{\mathrm{lin}}=\lmax(\mathsf N)\le\CMH(\mu)$ by [](#def:cmh). This dossier proves no bound on $\CMH$.
:::

## 7\. Unconditional dimension-dependent retention (part [(f)](#it:sol-clsr-f))

:::{prf:lemma} Pointwise cyclic square
:label: lem:sol-clsr-cyclic
Pointwise on $\R^n$,

$$
\Tr(HQ)-\Tr\bigl(H^{bc}(\partial_bH)(\partial_cH)\bigr)
=\frac16\sum_{p,q,r}\frac{\widetilde T_{pqr}^2}{\lambda_p\lambda_q\lambda_r}
\Bigl[(\lambda_p-\lambda_q)^2+(\lambda_q-\lambda_r)^2+(\lambda_r-\lambda_p)^2\Bigr]\ge0,
$$

where, at the given point, $H=\sum_p\lambda_pe_pe_p^\top$ is a spectral decomposition and $\widetilde T_{pqr}=e_p^ie_q^je_r^k\,\psi_{ijk}$. Moreover $\Tr(HA)=\Tr(H^3(D^2V\circ\nabla\psi))\ge0$.
:::

:::{prf:proof}
Both sides are scalars; expand in the spectral decomposition. With $\widetilde T$ totally symmetric,

$$
\Tr(HQ)=\sum_{p,q,r}\frac{\lambda_r}{\lambda_p\lambda_q}\,\widetilde T_{pqr}^2,
\qquad
\Tr\bigl(H^{bc}(\partial_bH)(\partial_cH)\bigr)
=\sum_{p,q,r}\frac1{\lambda_p}\,\widetilde T_{pqr}^2 .
$$

(For the first: $Q_{k\ell}=\sum_{p,q}(\lambda_p\lambda_q)^{-1} (\partial_kH)_{ij}e_p^ie_q^j(\partial_\ell H)_{i'j'}e_p^{i'}e_q^{j'}$ and contract $k,\ell$ against $H=\sum_r\lambda_re_re_r^\top$; for the second contract $b,c$ against $H^{-1}=\sum_r\lambda_r^{-1}e_re_r^\top$ and the free matrix indices against $\Id=\sum_pe_pe_p^\top$.) Since $\widetilde T_{pqr}^2$ is symmetric under permutations of $(p,q,r)$, replace each coefficient by its symmetrization:

$$
\frac13\Bigl[\frac{\lambda_r}{\lambda_p\lambda_q}+\frac{\lambda_p}{\lambda_q\lambda_r}
+\frac{\lambda_q}{\lambda_r\lambda_p}\Bigr]
-\frac13\Bigl[\frac1{\lambda_p}+\frac1{\lambda_q}+\frac1{\lambda_r}\Bigr]
=\frac{\lambda_p^2+\lambda_q^2+\lambda_r^2-\lambda_p\lambda_q-\lambda_q\lambda_r
-\lambda_r\lambda_p}{3\lambda_p\lambda_q\lambda_r},
$$

and the numerator is $\tfrac12[(\lambda_p-\lambda_q)^2+(\lambda_q-\lambda_r)^2 +(\lambda_r-\lambda_p)^2]\ge0$. For the last claim, $\Tr(HA)=\Tr(H\cdot H(D^2V\circ\nabla\psi)H)=\Tr\bigl(H^{3/2}(D^2V\circ\nabla\psi)H^{3/2}\bigr)\ge0$ by cyclicity and $D^2V\succeq0$, $H^{3/2}\succ0$.
:::

:::{prf:proof} Proof of part [(f)](#it:sol-clsr-f)
$\mathsf D\succeq0$: for $c\in\R^n$, $c^\top\mathsf Dc=\int H^{bc'}\inner{(\partial_bH)c}{(\partial_{c'}H)c}\dd\eta\ge0$ (Gram sum against the positive matrix $H^{-1}$); alternatively it is a sum of form values. By [](#lem:sol-clsr-cyclic), pointwise $\Tr(H(A+Q))\ge\Tr(HQ)\ge\mathfrak g$, and all three are nonnegative and integrable ([](#lem:sol-clsr-D-finite)), so by [](#eq:sol-clsr-trace-identity)

$$
\Tr\mathsf R=\Tr\mathsf N-\Tr\mathsf D=\int\Tr(H(A+Q))\,\dd\eta\ \ge\ \int\mathfrak g\,\dd\eta
=\Tr\mathsf D .
$$

Hence $\Tr\mathsf N\ge2\Tr\mathsf D$. Tracing $\mathsf N-\Id\preceq\mathsf D$ (part [(d)](#it:sol-clsr-d)) gives $\Tr\mathsf N-n\le\Tr\mathsf D\le\tfrac12\Tr\mathsf N$, whence $\Tr\mathsf N\le2n$ and $\Tr\mathsf D\le n$. Then for every unit $a$, $a^\top\mathsf Ra=a^\top\mathsf Na-a^\top\mathsf Da\ge a^\top\mathsf Na-\Tr\mathsf D \ge a^\top\mathsf Na-n$, i.e. $\mathsf R\succeq\mathsf N-n\Id$ ($a^\top\mathsf Da\le\Tr\mathsf D$ because $\mathsf D\succeq0$). Finally $a^\top\mathsf Na\le1+a^\top\mathsf Da\le1+n$, so $Q_{\mathrm{lin}}=\lmax(\mathsf N)\le n+1$.
:::

:::{prf:remark}
The chain above re-derives the trace bound $\Tr\E H^2\le2n$ on the regular compact-target class self-containedly (from [](#eq:sol-clsr-trace-identity), $\mathsf N-\Id\preceq\mathsf D$, and the pointwise cyclic square), without importing the unreviewed Chen–Klartag preprint. The statement $\mathsf R\succeq\mathsf N-n\Id$ is $(\mathrm{AB})_{1,n}$: dimension-*dependent*. Nothing here approaches a universal pair $(\rho,\beta)$, and no pointwise Loewner promotion of the cyclic square is asserted — the w3c01 two-dimensional jet refutes that promotion, and [](#lem:sol-clsr-cyclic) is used under the trace only.
:::

## 8\. Products of one-dimensional laws (part [(g)](#it:sol-clsr-g))

:::{prf:proof} Proof of part [(g)](#it:sol-clsr-g)
Let $\mu=\bigotimes_{k=1}^n\mu_k$ with each $\mu_k=e^{-V_k}\one_{(\alpha_k,\beta_k)}\dd x_k$ centered, of variance $1$, $V_k\in C^\infty(\R)$ convex on $(\alpha_k,\beta_k)$; then $\mu$ satisfies [](#def:sol-clsr-class) with $P=\prod_k[\alpha_k,\beta_k]$. Let $\psi_k$ be the canonical moment potential of $\mu_k$. The sum $\psi(y)=\sum_k\psi_k(y_k)$ is smooth, strictly convex, satisfies the Monge–Ampère equation [](#eq:sol-clsr-MA) of the product (both sides factorize), and pushes $e^{-\psi}\dd y=\bigotimes_ke^{-\psi_k}\dd y_k$ (a probability) forward to $\mu$; by the essential uniqueness of the moment potential up to source translation [@CorderoErausquinKlartag2015MomentMeasures], and because every matrix in [](#eq:sol-clsr-NDR-def) is invariant under source translations (it is an integral of a function of derivatives of $\psi$ against $e^{-\psi}$), we may compute with this $\psi$.

Now $H=\diag(\psi_k''(y_k))$ and $\psi_{ijk}=0$ unless $i=j=k$, so all objects are diagonal:

$$
A=\diag\bigl(V_k''(\psi_k')\,(\psi_k'')^2\bigr),\qquad
Q=\diag\Bigl(\frac{(\psi_k''')^2}{(\psi_k'')^2}\Bigr),\qquad
H^{bc}(\partial_bH)(\partial_cH)=\diag\Bigl(\frac{(\psi_k''')^2}{\psi_k''}\Bigr),
$$

and $\mathsf N,\mathsf D,\mathsf R$ are diagonal with $k$-th entries equal to the corresponding one-dimensional integrals (Fubini; each integrand depends on $y_k$ alone). In one dimension the pointwise identity

$$
H\,Q=\psi_k''\cdot\frac{(\psi_k''')^2}{(\psi_k'')^2}
=\frac{(\psi_k''')^2}{\psi_k''}=\bigl(H^{bc}(\partial_bH)(\partial_cH)\bigr)_{kk}
$$

holds *exactly* (no inequality). By [](#prop:sol-clsr-anticommutator), applied to the product map (which is in the class, so the proposition is available), the $k$-th diagonal entry of $\mathsf R$ is $\int H(A+Q)_{kk}\dd\eta=\int\bigl(V_k''(\psi_k')(\psi_k'')^3+(\psi_k''')^2/\psi_k''\bigr) e^{-\psi_k}\dd y_k$, whence

$$
(\mathsf R-\mathsf D)_{kk}
=\int V_k''(\psi_k')\,(\psi_k'')^3\,e^{-\psi_k}\,\dd y_k\;\ge\;0
$$

by convexity of $V_k$. Diagonal matrices compare entrywise in the Loewner order, so $\mathsf R\succeq\mathsf D$, and $\mathsf N=\mathsf D+\mathsf R$ gives $\mathsf R\succeq\tfrac12\mathsf N$.
:::

:::{prf:remark} Strong column equation on products
:label: rem:sol-clsr-product-strong
In one dimension, [](#eq:sol-clsr-MA1) reads $\psi_k'''/\psi_k''=-\psi_k'+V_k'(\psi_k')\,\psi_k''$, so $Q_{kk}=\bigl(\psi_k'-V_k'(\psi_k')\psi_k''\bigr)^2\le\bigl(R+c_V\cdot2R^2\bigr)^2$ is *bounded*; hence $\Tr Q$ is bounded on any finite product, $(A+Q)a\in L^2(\eta)$, and by [](#rem:sol-clsr-gap) the strong column equation $(1-\Aop)(Ha)=(A+Q)a$ holds on products in the full operator-domain sense.
:::

## 9\. Calibrations (remarks only; no proof step depends on them)

:::{prf:remark} Exact boundary calibrations
:label: rem:sol-clsr-calibrations
The following one-dimensional laws are *boundary* calibrations: the Gaussian has noncompact target, and the one-sided exponential, symmetric Laplace, and exponential products have nonsmooth or noncompactly-supported densities, so none of them belongs to the regular class of [](#def:sol-clsr-class). They are limits of regular laws and are recorded only to display the exact values of the resolution channels; each value below is an elementary closed-form integral against the classical Stein kernels ($\tau=1$ Gaussian; $\tau(x)=x+1$ for the centered one-sided exponential; $\tau(x)=\abs x/\sqrt2+\tfrac12$ for the isotropic symmetric Laplace).

$$
\begin{array}{l|ccccc}
\text{law} & \mathsf N & \mathsf D & \mathsf R & T_a & \norm{M_a}^2\\\hline
\text{Gaussian (any }n) & \Id & 0 & \Id & 0 & 0\\
\text{one-sided exponential (1D)} & 2 & 1 & 1 & 0 & 1\\
\text{symmetric Laplace (1D)} & 5/4 & 1/2 & 3/4 & 1/4 & 0\\
\text{product of one-sided exponentials} & 2\Id & \Id & \Id & 0 & 1\ (\text{all unit }a)
\end{array}
$$

Three structural observations. (i) The exponential saturates both $\mathsf R\preceq\Id$ and $\mathsf R\succeq\mathsf D$ with zero high-mode excess: its column fluctuation $\tau-1=x$ is exactly the gap eigenfunction, so the extremal configuration of the linear gate is spectrally pure at the Brascamp–Lieb gap; for the product, the totally symmetric tensor $M_{kib}=\delta_{kib}$ gives $\norm{M_a}^2=\abs a^2=1$ for *every* unit $a$. (ii) The Laplace shows $T_a>0$ occurs: the excess channel is real, not vacuous. (iii) All rows satisfy $\mathsf N=\mathsf D+\mathsf R$ and the resolution identities, *provided* the $A$-term is read distributionally where $V$ is nonsmooth — see the next warning.
:::

:::{warning} Distributional curvature of the Laplace
:label: warn:sol-clsr-laplace
The isotropic symmetric Laplace has $V''=2\sqrt2\,\delta_0$ as a measure. The retention $\mathsf R-\mathsf D=\E_\mu[V''\tau^3]$ of the one-dimensional identity is carried entirely by this atom:

$$
\E_\mu[V''\tau^3]
=2\sqrt2\;\tau(0)^3\rho(0)
=2\sqrt2\cdot\tfrac18\cdot\tfrac1{\sqrt2}=\tfrac14,
$$

which is exactly what reconciles $\mathsf R=3/4$ with $\mathsf D=1/2$. Smooth regular approximants spread this atom over a shrinking interval. Any computation on a piecewise-smooth target that discards the $A$-term where $V$ fails to be twice differentiable loses this mass and produces wrong values; this is a concrete audit warning for future work on boundary laws.
:::

:::{prf:remark} Non-certified pointers
:label: rem:sol-clsr-noncertified
An exploratory note of the project additionally proposes a pointwise deficit-kernel formula for $\tfrac12\{H,Q\}-H^{bc}(\partial_bH)(\partial_cH)$ in the eigenframe of $H$ (its P4) and an $f(H)$-corrector hierarchy of integrated identities (its P5). *Neither is certified by this dossier*; they are not part of [](#thm:sol-clsr-main), no statement here depends on them, and they are mentioned only so that a reviewer can distinguish the certified boundary of this dossier from the exploratory content of that note.
:::

## 10\. Audit trail

**Hypotheses actually used.** (1) [](#def:sol-clsr-class) (smooth positive density on a convex body, centered, isotropic, log-concave target), through the imported [](#thm:regular-moment-map-compact-target) (regularity, diffeomorphism, weak Stein identity with zero flux, $\E_\mu\tau=\Id$). (2) The published pointwise bound [](#eq:sol-clsr-Hbound) [@Klartag2013MomentMeasures], used in: finiteness of $\mathsf N$; boundedness of $u_b,H_{ai},A$; [](#lem:sol-clsr-domination)–[](#lem:sol-clsr-form-membership); [](#rem:sol-clsr-product-strong). (3) The classical Brascamp–Lieb inequality [@BrascampLieb1976] ([](#lem:sol-clsr-BL) only). (4) Essential uniqueness of the moment potential [@CorderoErausquinKlartag2015MomentMeasures] (part [(g)](#it:sol-clsr-g) only). (5) [](#def:cmh) operator conventions (form core, closability, self-adjoint $\Aop$); `prop:cmh-bochner` is a listed ledger dependency (`depends_on` of `lem:cmh-linear-spectral-resolution`) but no identity of this dossier consumes it, so under `CLAUDE.md` constraint 8 it should be dropped from `depends_on` when the `proofs[]` record is wired; the repair handoff proposes that delta. No other external input is used; in particular no unreviewed preprint import is load-bearing (the trace bound $\Tr\mathsf N\le2n$ is re-derived, not imported).

**Flagged gaps.** None. The statement of [](#lem:cmh-linear-spectral-resolution) now agrees with [](#thm:sol-clsr-main): the column equation is stated and proved in the weak form [](#eq:sol-clsr-weak-column) (columns in $\Dom(\calE)$, $(A+Q)a\in L^1(\eta)$, bounded smooth finite-energy test functions), and $\inner v{\Aop v}$ is the closed-form value. The strong operator-domain form $(1-\Aop)(Ha)=(A+Q)a$ is not asserted by the lemma; it is equivalent to $\Tr Q\in L^2(\eta)$, open on the general class ([](#rem:sol-clsr-gap)) and proved on products ([](#rem:sol-clsr-product-strong)). No step is conditional: given the published imports above, [](#thm:sol-clsr-main) as stated is unconditional on the class of [](#def:sol-clsr-class).

**Obstructions respected.** The ledger node carries no `bounded_by` edge; the six obstruction statements of the manuscript are scoped to the Eldan fixed-cut program, and the route guardrails are checked one by one. *rem:two-tail-slice-bounds*: no localization cut, slice bound, or covariance-weighted estimate appears; all statements are stationary identities at one fixed map. *rem:projection-ceiling*: the controlled quantities are full column energies $\int\abs{Ha}^2\dd\eta$ and full slice norms $\norm{M_a}$; no scalar projection bound is promoted. *rem:crude-insufficient* and *rem:relative-ceiling*: no stochastic covariance integral, bootstrap, or all-measure relative bound occurs; part [(f)](#it:sol-clsr-f) is explicitly dimension-dependent. *rem:profile-circularity*: no isoperimetric profile or evolving competitor family occurs; Brascamp–Lieb is a certified external input, not an assumed profile bound. *rem:single-coordinate-cuts*: products enter only through exact stationary block-diagonalization. CMH guardrails: no pointwise Loewner promotion of the cyclic square is asserted ([](#lem:sol-clsr-cyclic) is used under the trace only; the w3c01 jet fence is respected); the arguments consume differentiated Monge–Ampère structure throughout, as `prop:letwin-not-gate-zero` requires of any statement of this strength (the eigen-equation for $u_b$, the column equation, and [](#eq:sol-clsr-trace-identity) all come from [](#eq:sol-clsr-MA1)–[](#lem:sol-clsr-MA2)); no canonical kernel is transported through a noninvertible map; no continuity or semicontinuity of $Q_{\mathrm{lin}}$ or $\CMH$ is asserted; boundary laws appear only as calibration remarks; the trace-upgrade cluster is not opened and no comparison with it is made.
