---
title: 'Solution: the CMH recovery calculus'
label: sec:sol-cmh-recovery-calculus
ledger-node: prop:cmh-recovery-calculus
numbering:
  enumerator: D20.%s
---

*Part of the moment-map mechanism, Chapter [](#sec:cmh-normalization); the reading order is on the [full proofs](#sec:proofs-moment-map) page.*

**Overview.** This dossier proves [](#prop:cmh-recovery-calculus) as [](#thm:sol-cmh-recovery-calculus) for the recovery envelope $\mathfrak R_n$ of [](#eq:sol-cmh-recovery-envelope). It proves the lower bounds [](#eq:sol-cmh-recovery-lower-bounds), invariance and monotonicity under linear maps, the product bound, and an affine-support extension. It also computes the envelope for Gaussians, for one-dimensional products and for uniform-simplex blocks. Every estimate is made on selected finite-stage regular laws before a liminf is taken, and no semicontinuity of $\CMH$ is used. The results cover only these closure operations and model blocks and do not discharge [](#ass:cmh-recovery-envelope).

1. Preliminaries: a diagonal lemma extracts a single good regular law without attainment ([](#lem:sol-cmh-recovery-diagonal)). The universal floor $\CMH\ge1$ follows from linear tests ([](#lem:sol-cmh-recovery-floor)).
2. Lower bound: [](#lem:affine-poincare-w2-liminf) and [](#thm:cmh-implies-affine-poincare) give $\CPaff(\mu)\le\mathfrak R_n(\mu)$.
3. Linear images: affine covariance gives invertible invariance [](#eq:sol-cmh-recovery-invertible). Invertible approximants $T_j\to T$, combined with step 1, give singular monotonicity [](#eq:sol-cmh-recovery-singular).
4. Products: a simultaneous good-member selection and [](#thm:cmh-product) give [](#eq:sol-cmh-recovery-product).
5. Truncated Gaussians have $\CMH\to1$ ([](#lem:sol-cmh-recovery-truncated-gaussian)). Tensoring with scaled normal factors, via step 4, gives [](#eq:sol-cmh-recovery-affine-support).
6. Calibrations: centered Gaussians have envelope $1$. By [](#thm:cmh-1d), one-dimensional products have envelope at most $4$, with equality when a one-sided exponential factor is present. By [](#thm:cmh-dirichlet), uniform-simplex blocks have envelope at most $4$. Steps 3–5 extend these bounds to the stated images and embeddings.

**Regular recovery and the declared ambient space.** Fix a centered log-concave probability $\mu$ on a declared copy of $\R^n$. Write $\operatorname{Rec}_n(\mu)$ for the sequences $(\mu_k)$ which converge to $\mu$ in the ambient $W_2$ metric and whose members are centered, full-dimensional, compactly supported log-concave regular moment-map laws on $\R^n$. Thus, for every $k$, there are a convex body $P_k$ and a positive $g_k\in C^\infty(\R^n)$ such that

$$
\dd\mu_k(x)=g_k(x)\one_{\operatorname{int}P_k}(x)\,\dd x,
$$

and the canonical Hessian kernel and Stein generator carry the weak zero-flux closed-form convention of [](#thm:regular-moment-map-compact-target) and [](#def:cmh). The certified regular-recovery theorem in [](#lem:affine-poincare-w2-liminf) makes $\operatorname{Rec}_n(\mu)$ nonempty. Define the extended-real number

```{math}
:label: eq:sol-cmh-recovery-envelope
\mathfrak R_n(\mu)
:=\inf_{(\mu_k)\in\operatorname{Rec}_n(\mu)}
\liminf_{k\to\infty}\CMH(\mu_k).
```

This is the envelope $\mathfrak R_{\rm CMH}$ of [](#prop:cmh-recovery-calculus), with the ambient dimension displayed because it is part of the definition.

:::{prf:theorem} CMH recovery calculus
:label: thm:sol-cmh-recovery-calculus
For every centered log-concave probability $\mu$ in its declared ambient Euclidean space:

(i)

```{math}
:label: eq:sol-cmh-recovery-lower-bounds
\CPaff(\mu)\le \mathfrak R_n(\mu),
\qquad \mathfrak R_n(\mu)\ge1.
```

(ii) If $T:\R^n\to\R^n$ is invertible, then

```{math}
:label: eq:sol-cmh-recovery-invertible
\mathfrak R_n(T_\#\mu)=\mathfrak R_n(\mu).
```

If $T$ is any square linear map on the same $\R^n$, possibly singular, then

```{math}
:label: eq:sol-cmh-recovery-singular
\mathfrak R_n(T_\#\mu)\le\mathfrak R_n(\mu).
```

For finitely many centered log-concave laws $\mu_i$ on $\R^{n_i}$,

```{math}
:label: eq:sol-cmh-recovery-product
\mathfrak R_{n_1+\cdots+n_m}
\left(\bigotimes_{i=1}^m\mu_i\right)
\le\max_{1\le i\le m}\mathfrak R_{n_i}(\mu_i).
```

(iii) Let $S\subset\R^n$ be a $d$-dimensional linear subspace, let $\iota:S\hookrightarrow\R^n$ be inclusion, and regard the centered law $\mu$ intrinsically on $S$. If an intrinsic regular recovery has CMH liminf at most $C$, or more generally if $\mathfrak R_d(\mu)\le C$, then

```{math}
:label: eq:sol-cmh-recovery-affine-support
\mathfrak R_n(\iota_\#\mu)\le\max\{C,1\}.
```

The ambient recovery in [](#eq:sol-cmh-recovery-affine-support) is obtained by tensoring the intrinsic one with scaled symmetric truncated-Gaussian normal factors.

Consequently $\mathfrak R_n(\gamma)=1$ for every centered Gaussian law $\gamma$, including singular Gaussians in their declared ambient spaces. The envelope equals $4$ for every finite product of one-dimensional log-concave laws which contains a centered one-sided-exponential factor. It is at most $4$ for invertible linear images, same-ambient singular square linear images, and affine-support embeddings of finite products whose blocks are one-dimensional log-concave laws or centered uniform-simplex laws.

These conclusions are restricted to the displayed closure operations and model blocks. They assert neither a universal recovery bound for arbitrary log-concave laws nor [](#ass:cmh-recovery-envelope).
:::

## 1\. Two preliminary facts

The first fact is the diagonal device needed whenever the infimum in [](#eq:sol-cmh-recovery-envelope), or a liminf inside it, is not attained.

:::{prf:lemma} One-shot extraction without attainment
:label: lem:sol-cmh-recovery-diagonal
Suppose $r=\mathfrak R_n(\mu)<\infty$. Given positive numbers $\epsilon$ and $\eta$, there is a single centered full-dimensional compact-target regular law $\nu$ such that

```{math}
:label: eq:sol-cmh-recovery-one-shot
W_2(\nu,\mu)<\epsilon,
\qquad
\CMH(\nu)<r+\eta.
```

The same conclusion with $r$ replaced by $C$ holds if one starts from a specified recovery sequence whose CMH liminf is at most $C$.
:::

:::{prf:proof}
By the definition of an infimum, choose $(\nu_k)\in\operatorname{Rec}_n(\mu)$ with

$$
L:=\liminf_k\CMH(\nu_k)<r+\eta/2.
$$

There are arbitrarily large $k$ for which $\CMH(\nu_k)<L+\eta/2$, while recovery gives $W_2(\nu_k,\mu)<\epsilon$ for all sufficiently large $k$. One index satisfies both requirements. This proves [](#eq:sol-cmh-recovery-one-shot). If a specified sequence has liminf at most $C$, the same argument selects an arbitrarily far member with CMH constant below $C+\eta$. In particular, applying the lemma with $\epsilon=\eta=j^{-1}$ constructs one diagonal recovery sequence with CMH limsup at most $r$ even when neither infimum is attained.
:::

:::{prf:lemma} Universal floor
:label: lem:sol-cmh-recovery-floor
If $\nu$ is a full-dimensional law in the regular moment-map class, then $\CMH(\nu)\ge1$. Consequently $\mathfrak R_n(\mu)\ge1$ for every target $\mu$ in a nonzero declared ambient space.
:::

:::{prf:proof}
Let $\Sigma=\Cov(\nu)\succ0$ and let $H$ be the canonical Hessian kernel. For $a\in\R^n\setminus\{0\}$, the linear function $g_a(x)=a\cdot x$ belongs to the closed Stein operator domain. Indeed, it is bounded on the compact target, and the global weak Stein identity gives $-L_\nu g_a=a\cdot x\in L^2(\nu)$ with zero boundary flux. Therefore it is an admissible test in [](#def:cmh). Centering and $\E_\nu H=\Sigma$ give

$$
\E_\nu(L_\nu g_a)^2=a^\top\Sigma a
$$

and, by Jensen's inequality in $L^2(\nu;\R^n)$,

$$
\begin{aligned}
\E_\nu\inner{Ha}{\Sigma^{-1}Ha}
&=\E_\nu\lvert\Sigma^{-1/2}Ha\rvert^2\\
&\ge\lvert\Sigma^{-1/2}\E_\nu[H]a\rvert^2
=a^\top\Sigma a.
\end{aligned}
$$

The corresponding CMH quotient is at least one. Every member of every recovery sequence has this property, so taking first a liminf and then the infimum proves the envelope floor. Notice that this argument still supplies the lower bound for a point-mass target, for which $\CPaff=0$ by convention.
:::

## 2\. Lower semicontinuity and affine covariance

:::{prf:proof} Proof of [](#eq:sol-cmh-recovery-lower-bounds)
Take an arbitrary $(\mu_k)\in\operatorname{Rec}_n(\mu)$. The certified stronger sequential part of [](#lem:affine-poincare-w2-liminf) gives

$$
\CPaff(\mu)\le\liminf_k\CPaff(\mu_k).
$$

For clarity, the argument applies to every recovery sequence, not merely to the particular sequence constructed in that lemma: ambient $W_2$ convergence and centeredness give $\Cov(\mu_k)\to\Cov(\mu)$; variances and covariance Dirichlet energies converge for every fixed ambient smooth compactly supported test; one first takes a subsequence realizing the liminf of the constants and then passes all tests along that same subsequence; intrinsic smooth-core density closes the inequality on a singular affine support. No CMH limit is used.

Each $\mu_k$ is in the regular class, so the certified endpoint [](#thm:cmh-implies-affine-poincare) gives $\CPaff(\mu_k)\le\CMH(\mu_k)$. Hence

$$
\CPaff(\mu)
\le\liminf_k\CPaff(\mu_k)
\le\liminf_k\CMH(\mu_k).
$$

Taking the infimum over all regular recoveries proves the first inequality in [](#eq:sol-cmh-recovery-lower-bounds); [](#lem:sol-cmh-recovery-floor) proves the second.
:::

:::{prf:proof} Proof of invertible invariance [](#eq:sol-cmh-recovery-invertible)
Let $T$ be invertible and let $(\mu_k)$ be any recovery of $\mu$. The laws $T_\#\mu_k$ are centered and full-dimensional. If $\mu_k$ has target $P_k$ and positive smooth density on $P_k$, then $T_\#\mu_k$ has target $TP_k$ and a positive smooth density there, so it remains in the compact-target regular class. Moreover

$$
W_2(T_\#\mu_k,T_\#\mu)\le\lVert T\rVert_{\rm op}W_2(\mu_k,\mu)\longrightarrow0.
$$

The certified affine covariance of the canonical data is

$$
\Sigma_{T_\#\mu_k}=T\Sigma_{\mu_k}T^\top,
\qquad
H_{T_\#\mu_k}(Tx)=T H_{\mu_k}(x)T^\top.
$$

Under the bijection $g\mapsto g\circ T$ of closed operator domains, the numerator and the denominator in [](#def:cmh) are unchanged. Thus $\CMH(T_\#\mu_k)=\CMH(\mu_k)$ and

$$
\mathfrak R_n(T_\#\mu)\le\mathfrak R_n(\mu).
$$

Apply the same argument to $T^{-1}$ for the reverse inequality. Linear maps preserve centering; an affine map between centered laws reduces to this statement after recentering.
:::

:::{prf:proof} Proof of singular-square monotonicity [](#eq:sol-cmh-recovery-singular)
The assertion is vacuous if $r:=\mathfrak R_n(\mu)=\infty$, so assume $r<\infty$. Invertible matrices are dense among square matrices; choose invertible $T_j\to T$. By [](#lem:sol-cmh-recovery-diagonal), choose a regular law $\nu_j$ with

```{math}
:label: eq:sol-cmh-recovery-singular-diagonal
W_2(\nu_j,\mu)<j^{-1},
\qquad
\CMH(\nu_j)<r+j^{-1}.
```

Every $(T_j)_\#\nu_j$ is centered, full-dimensional and regular, and invertible invariance at the finite stage gives

```{math}
:label: eq:sol-cmh-recovery-singular-constant
\CMH((T_j)_\#\nu_j)=\CMH(\nu_j)<r+j^{-1}.
```

If $X_j\sim\nu_j$ and $X\sim\mu$ are coupled so that $\E\lvert X_j-X\rvert^2\to0$, then

$$
\begin{aligned}
\E\lvert T_jX_j-TX\rvert^2
&\le2\lVert T_j\rVert_{\rm op}^2\E\lvert X_j-X\rvert^2
+2\E\lvert(T_j-T)X\rvert^2\\
&\longrightarrow0.
\end{aligned}
$$

Thus $(T_j)_\#\nu_j\to T_\#\mu$ in ambient $W_2$. It is a recovery sequence for the possibly singular target, and [](#eq:sol-cmh-recovery-singular-constant) proves [](#eq:sol-cmh-recovery-singular).

No canonical kernel is pushed through the singular map $T$: every finite-stage map $T_j$ is invertible. Nor is any convergence or semicontinuity of CMH used. This is why the statement is dimension-preserving and does not imply a rectangular projection theorem.
:::

## 3\. Products and simultaneous good members

:::{prf:proof} Proof of the product bound [](#eq:sol-cmh-recovery-product)
If some $r_i:=\mathfrak R_{n_i}(\mu_i)$ is infinite, the bound is vacuous. Suppose all $r_i$ are finite. For every pair $(i,j)$, apply [](#lem:sol-cmh-recovery-diagonal) to choose a regular $\nu_{i,j}$ satisfying

```{math}
:label: eq:sol-cmh-recovery-product-diagonal
W_2(\nu_{i,j},\mu_i)<j^{-1},
\qquad
\CMH(\nu_{i,j})<r_i+j^{-1}.
```

This is a simultaneous good-member selection over the finitely many factors: it does not assume that low-CMH indices in unrelated original sequences coincide.

Set $\nu_j=\bigotimes_i\nu_{i,j}$. Products of centered full-dimensional compact-target regular laws remain in that class. Indeed, their convex target bodies and positive smooth densities multiply, their moment potentials add, and their canonical Hessians and covariances are block diagonal. Product couplings give

```{math}
:label: eq:sol-cmh-recovery-product-w2
W_2^2\!\left(\nu_j,\bigotimes_i\mu_i\right)
\le\sum_iW_2^2(\nu_{i,j},\mu_i)
<\frac{m}{j^2}.
```

The certified product formula, [](#thm:cmh-product), gives

$$
\CMH(\nu_j)=\max_i\CMH(\nu_{i,j})
<\max_i r_i+j^{-1}.
$$

The sequence $(\nu_j)$ is therefore an admissible recovery and proves [](#eq:sol-cmh-recovery-product).
:::

## 4\. Compact Gaussian normal factors

Let $\gamma_1$ be the standard Gaussian law and, for $R>0$, let

```{math}
:label: eq:sol-cmh-recovery-truncated-gaussian
\dd\zeta_R(x)
=Z_R^{-1}e^{-x^2/2}\one_{(-R,R)}(x)\,\dd x.
```

This law is centered by symmetry and belongs to the one-dimensional compact-target regular class: its density is the restriction to $[-R,R]$ of a globally positive smooth function.

:::{prf:lemma} Truncated-Gaussian CMH calibration
:label: lem:sol-cmh-recovery-truncated-gaussian
Writing $v_R=\Var(\zeta_R)$, one has

```{math}
:label: eq:sol-cmh-recovery-truncated-gaussian-bound
1\le\CMH(\zeta_R)
=\frac{\CP(\zeta_R)}{v_R}
\le\frac1{v_R},
\qquad
v_R\longrightarrow1,
\qquad
\CMH(\zeta_R)\longrightarrow1.
```

Moreover, $(x\mapsto\epsilon x)_\#\zeta_R$ has the same CMH constant for every $\epsilon>0$.
:::

:::{prf:proof}
The one-dimensional identity, [](#thm:cmh-1d), gives the equality in [](#eq:sol-cmh-recovery-truncated-gaussian-bound). We verify the Neumann Bakry–Émery estimate $\CP(\zeta_R)\le1$, including its boundary convention. The ordinary Dirichlet form $\int_{-R}^R|f'|^2\,\dd\zeta_R$ has Neumann generator

$$
A_Rf=-f''+xf',
\qquad f'(-R)=f'(R)=0.
$$

For a smooth Neumann operator-core function $f$, two weighted integrations by parts, with the boundary terms killed by $f'(\pm R)=0$, give

```{math}
:label: eq:sol-cmh-recovery-neumann-bochner
\lVert A_Rf\rVert_{L^2(\zeta_R)}^2
=\int_{-R}^R\bigl((f'')^2+(f')^2\bigr)\,\dd\zeta_R
\ge\langle f,A_Rf\rangle_{L^2(\zeta_R)}.
```

The Friedrichs closure has constants as kernel. By the spectral theorem, [](#eq:sol-cmh-recovery-neumann-bochner) places its nonzero spectrum in $[1,\infty)$ and hence proves the Neumann Poincaré inequality with constant one. This is the hard-boundary form of the Bakry–Émery argument; it does not apply a full-space inequality across the two endpoints.

Testing the Poincaré quotient with $f(x)=x$ gives $\CP(\zeta_R)\ge v_R$, which also proves the left inequality. If $G\sim\gamma_1$, then $v_R=\E[G^2\mid |G|<R]\to1$ by dominated convergence. The squeeze in [](#eq:sol-cmh-recovery-truncated-gaussian-bound) follows. Finally, nonzero scaling is an invertible linear map, so direct affine covariance of CMH gives the last assertion.
:::

:::{prf:proof} Proof of affine-support extension [](#eq:sol-cmh-recovery-affine-support)
Because $\mu$ is centered, its affine hull contains the origin and is the linear subspace $S$. First assume $d>0$. Use [](#lem:sol-cmh-recovery-diagonal), or its specified-sequence variant, to choose intrinsic regular laws $\nu_j$ on $S$ such that

```{math}
:label: eq:sol-cmh-recovery-intrinsic-good
W_2(\nu_j,\mu)<j^{-1},
\qquad
\CMH(\nu_j)<C+j^{-1}.
```

Choose $R_j\uparrow\infty$ so that $\CMH(\zeta_{R_j})<1+j^{-1}$ and put $\epsilon_j=j^{-1}$. On the orthogonal splitting $\R^n=S\oplus S^\perp$, with $q=n-d$, define

```{math}
:label: eq:sol-cmh-recovery-normal-product
\widehat\nu_j
:=\nu_j\otimes
\left((x\mapsto\epsilon_jx)_\#\zeta_{R_j}\right)^{\otimes q}.
```

Every $\widehat\nu_j$ is centered and full-dimensional in the declared ambient $\R^n$. Its support is the product of the intrinsic convex target of $\nu_j$ with a compact normal cube, and its density is the restriction of a positive smooth product density. It is therefore a regular compact-target moment-map law. Coupling each normal coordinate to zero yields

$$
\begin{aligned}
W_2^2(\widehat\nu_j,\iota_\#\mu)
&\le W_2^2(\nu_j,\mu)+q\epsilon_j^2v_{R_j}
\longrightarrow0.
\end{aligned}
$$

Scaling invariance, the product formula, and [](#lem:sol-cmh-recovery-truncated-gaussian) give

$$
\CMH(\widehat\nu_j)
=\max\{\CMH(\nu_j),\CMH(\zeta_{R_j})\}
<\max\{C+j^{-1},1+j^{-1}\}.
$$

Taking the liminf proves [](#eq:sol-cmh-recovery-affine-support).

If $d=0$, centeredness forces $\mu=\delta_0$. Omit $\nu_j$ from [](#eq:sol-cmh-recovery-normal-product) and take the $n$-fold product of scaled $\zeta_{R_j}$ factors. It converges in $W_2$ to $\delta_0$ and has CMH constant tending to one. Thus the point mass has ambient envelope one, consistently with [](#lem:sol-cmh-recovery-floor).
:::

## 5\. Exact calibrations and the $4$-closed model class

:::{prf:proof} Proof of the Gaussian conclusion
The conditioning in [](#eq:sol-cmh-recovery-truncated-gaussian) converges to $\gamma_1$ weakly and in second moment, hence in $W_2$. Thus $\zeta_R^{\otimes n}$ is a regular recovery of the standard Gaussian $\gamma_n$, by product couplings, and

$$
\CMH(\zeta_R^{\otimes n})=\CMH(\zeta_R)\longrightarrow1.
$$

The universal floor proves $\mathfrak R_n(\gamma_n)=1$. Every nondegenerate centered Gaussian is an invertible linear image of $\gamma_n$, so [](#eq:sol-cmh-recovery-invertible) applies. Every singular centered Gaussian with covariance $Q\succeq0$ is $(Q^{1/2})_\#\gamma_n$ in the same ambient $\R^n$, so [](#eq:sol-cmh-recovery-singular) gives an upper bound of one and the universal floor gives equality. This includes $Q=0$.
:::

:::{prf:proof} Proof of the one-dimensional-product conclusions
Let $\lambda$ denote the centered one-sided exponential, the law of $Y-1$ for $Y\sim\operatorname{Exp}(1)$. For every nondegenerate centered one-dimensional log-concave law $\rho$, [](#lem:affine-poincare-w2-liminf) supplies a one-dimensional regular compact-target recovery $(\rho_k)$. The exact identity and sharp one-dimensional bound in [](#thm:cmh-1d) give, member by member,

$$
\CMH(\rho_k)
=\frac{\CP(\rho_k)}{\Var(\rho_k)}\le4.
$$

Hence $\mathfrak R_1(\rho)\le4$. A degenerate one-dimensional factor is a point mass and has envelope one by the Gaussian conclusion.

The product upper bound now gives envelope at most four for every finite product of such factors. Ordinary variance tensorization, with the covariance-normalized energy, gives

$$
\CPaff\!\left(\bigotimes_i\rho_i\right)
=\max_i\frac{\CP(\rho_i)}{\Var(\rho_i)}
$$

over the nondegenerate factors: the upper bound is the usual conditional-variance argument and the reverse bound follows by tests depending on one coordinate. [](#thm:cmh-1d) proves $\CP(\lambda)/\Var(\lambda)=4$. Thus a product containing $\lambda$ has $\CPaff=4$, and the first inequality in [](#eq:sol-cmh-recovery-lower-bounds) supplies the matching envelope lower bound. Its envelope is exactly four.
:::

:::{prf:proof} Proof of the uniform-simplex and closure conclusions
Let $U_m$ be the centered uniform law on an $(m-1)$-dimensional simplex, viewed intrinsically on its affine tangent space. It is itself a compact-target regular moment-map law: after translation to its centroid, its density is the restriction of a positive constant smooth function to a convex body. The constant sequence is therefore an intrinsic recovery.

For $m=2$, the simplex is an interval and [](#thm:cmh-1d) gives $\CMH(U_2)=12/\pi^2<4$. For $m=3$, the main Dirichlet theorem [](#thm:cmh-dirichlet) applies with $A=3$; its angular surplus is $s_3=0$, but its non-strict estimate still gives $\CMH(U_3)\le4$. For $m>3$, the same theorem gives the bound, and [](#cor:cmh-dirichlet-surplus) even makes it strict. Consequently

$$
\mathfrak R_{m-1}(U_m)\le4
\qquad(m\ge2).
$$

Only the uniform Dirichlet law is used here. No boundary stability or regular-class membership is claimed for a nonuniform Dirichlet density which vanishes on a face.

Take now any finite product of one-dimensional centered log-concave factors and centered uniform-simplex blocks. The preceding arguments and [](#eq:sol-cmh-recovery-product) give intrinsic envelope at most four. Invertible linear images retain this bound by [](#eq:sol-cmh-recovery-invertible); singular square images in the same declared ambient dimension retain it by [](#eq:sol-cmh-recovery-singular). Finally, consider an injective affine-support embedding into a larger Euclidean space and recenter the image. Intrinsically, the resulting map onto its image tangent space is invertible, so its intrinsic envelope is at most four. Applying [](#eq:sol-cmh-recovery-affine-support) adds vanishing normal factors at cost $\max\{4,1\}=4$.

This last argument is intrinsic extension, not CMH monotonicity under a rectangular dimension-lowering projection. It never transports a noncanonical projected kernel.
:::

**Boundary, core, and hypothesis audit.** All finite-stage laws used above belong to the stated compact-target class. The linear floor uses the global weak Stein identity to place affine tests in the closed operator domain. The product step uses the certified direct-sum closed forms and canonical block Hessian. The truncated-Gaussian estimate is for the ordinary Neumann Poincaré form on the interval, and [](#thm:cmh-1d) then identifies its canonical CMH constant; these two operators are not silently conflated. The uniform-simplex estimate uses the Wright–Fisher zero-flux core and its certified closure in [](#thm:cmh-dirichlet). Every approximant is centered and full-dimensional in the ambient space declared at that finite stage; singularity occurs only in the $W_2$ target.

The hypotheses actually used are finite-dimensional centered log-concavity, finite second moment, the published compact-target regular moment-map theorem, affine covariance of CMH, the certified affine-Poincaré $W_2$ lower-semicontinuity and regular endpoint, and the certified one-dimensional, product, and Dirichlet CMH theorems. No numerical evidence is used.

**Obstructions and exclusions.** The ledger assigns this proposition no `bounded_by` obstruction. The route fences are nevertheless respected:

- no convergence, lower semicontinuity, or upper semicontinuity of $\CMH$ is asserted; all estimates hold on selected finite-stage laws before a liminf is taken;

- no canonical kernel is transported through a singular map, and no rectangular projection monotonicity is claimed;

- the solenoidal part of CMH is never discarded: it is already included in each certified finite-stage CMH constant;

- the calculus covers only the displayed Gaussian, one-dimensional-product, and uniform-simplex-generated classes. It supplies no bounded recovery for a general log-concave target and therefore does not discharge [](#ass:cmh-recovery-envelope).
