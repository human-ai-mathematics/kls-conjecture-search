---
title: 'Solution: profile curvature, exact splitting, and the Gaussian and product models'
label: sec:sol-kls-geometry-models
ledger-node:
- lem:profile-bound
- cor:generic-degeneracy
- prop:exact-splitting
- prop:persistent-splitting
- prop:gaussian-model
- prop:products
numbering:
  enumerator: D5.%s
---

**Overview.** This dossier proves [](#lem:profile-bound), [](#cor:generic-degeneracy), [](#prop:exact-splitting), [](#prop:persistent-splitting), [](#prop:gaussian-model) and [](#prop:products). A second variation along a smooth minimizing branch bounds the constant-mode curvature $\mathfrak K$ by the profile's second derivative, and an average of this bound over volumes controls $\mathfrak K$ by $h_\nu^3$. Both statements are conditional on the granted smooth minimizers. The rest of the dossier treats exactly split laws and the Gaussian and product models, whose localization posteriors are computed explicitly.

1. [](#lem:sol-profile-bound): first and second variation of a normal flow give a competitor branch $\Psi$ with $\Psi''(p)=-\mathfrak K/P^2$, and $I\le\Psi$ gives the bound.
2. [](#cor:sol-generic-degeneracy): by concavity of the profile, $h_\nu=2I(1/2)$ and $-I''$ has mass at most $3h_\nu$ on $[1/3,2/3]$. Step 1 then gives $\int\mathfrak K_{\Sigma_p}\,dp\le\tfrac34h_\nu^3$.
3. [](#prop:sol-exact-splitting): $\nabla^2V(\theta,\cdot)\equiv0$ forces $V=V_1(y)+cz$. Conversely, orthogonal cuts of a split law have $\mathfrak K_\Sigma=0$. The dossier does not claim the reverse implication from $\mathfrak K_\Sigma=0$ to splitting.
4. [](#prop:sol-persistent-splitting): under the global additive identity [](#eq:sol-global-additive-potential), the localized posterior stays a product along every path. For orthogonal halfspaces $\delta_t,G_t,K_t$ are then multiples of $\theta$ or $\theta\theta^T$, so $K_t$ has rank at most one.
5. [](#prop:sol-gaussian-model): Gaussian posteriors have $A_t=(1+t)^{-1}I_n$. A Doob exit bound gives the conclusion of [](#thm:centroid-implies-kls). Halfspaces have zero excess, and an erf inequality gives the bounds on $r_t$ and $D_t$.
6. [](#prop:sol-products): product posteriors stay products with supermartingale coordinate variances. Tensorization and the Cheeger–Poincaré comparison give $h_{\mu_t}\ge c\lmax(A_t)^{-1/2}$, and hence KLS for products.

**Scope and conventions.** This dossier proves exactly the six statements listed in the header. It does not supply the regularity hypotheses in [](#lem:profile-bound) or [](#cor:generic-degeneracy), and it does not infer a global splitting from the boundary-local condition $\mathfrak K_\Sigma=0$. For the profile calculation, the smooth free-boundary convention is the one in §[](#sec:notation): all support-boundary contributions are included in $\mathfrak K_\Sigma=-\calI_\Sigma(1,1)$. Stochastic-localization notation is also that of §[](#sec:notation). The repair dated 2026-08-27 changes only the statement and proof of [](#prop:sol-persistent-splitting), by making its global product-support hypothesis explicit. The other five proofs are retained from the previously reviewed version, but the modified coupled dossier has `checked_by: none` pending a fresh independent review.

## 1\. Curvature of a smooth minimizing branch

:::{prf:lemma} = [](#lem:profile-bound)
:label: lem:sol-profile-bound
Suppose that at volume $p$ there is a smooth volume-constrained minimizer $E_p$ with boundary $\Sigma_p$, weighted area $P=I(p)$, and that the isoperimetric profile $I$ is twice differentiable at $p$. Then

$$
\mathfrak K_{\Sigma_p}\le -I''(p)I(p)^2.
$$
:::

:::{prf:proof}
Choose the admissible normal flow $E_s$ whose boundary has unit normal speed at $s=0$; when the minimizer meets the support boundary, the flow is taken in the free-boundary class. Let $v(s)=\nu(E_s)$ and $P(s)=\nu^+(E_s)$. The first-variation formulas, with the orientation used in §[](#sec:jacobi) [@Bayle2004; @BayleRosales2003; @Rosales2014; @Milman2009Isoperimetric], give

$$
v'(0)=P,\qquad P'(0)=\lambda P,
$$

where the weighted mean curvature $\lambda=H_\nu$ is constant on $\Sigma_p$. In particular $v'(0)>0$, so $v$ has a local smooth inverse. The Riccati variation of $H_\nu$, including the free-boundary term already present in $\mathfrak K_{\Sigma_p}$, gives

$$
P''(0)=-\mathfrak K_{\Sigma_p}+\lambda^2P.
$$

Also $v''(0)=P'(0)=\lambda P$.

The competitor branch defines $\Psi(w)=P(v^{-1}(w))$. Since $E_s$ is an admissible competitor at volume $v(s)$,

$$
I(w)\le\Psi(w)\quad\text{near }p,
\qquad I(p)=\Psi(p)=P.
$$

The chain rule, now retaining both second-derivative terms, yields

$$
\begin{aligned}
\Psi''(p)
&=\frac{P''(0)v'(0)-P'(0)v''(0)}{v'(0)^3}\\
&=\frac{(-\mathfrak K_{\Sigma_p}+\lambda^2P)P-(\lambda P)^2}{P^3}
=-\frac{\mathfrak K_{\Sigma_p}}{P^2}.
\end{aligned}
$$

Because $\Psi-I$ has a local minimum $0$ at $p$ and $I$ is twice differentiable there, $I''(p)\le\Psi''(p)$. Multiplication by $-P^2$ proves the claim.
:::

:::{prf:corollary} = [](#cor:generic-degeneracy)
:label: cor:sol-generic-degeneracy
Grant smooth volume-constrained minimizers at almost every $p\in[1/3,2/3]$. If $h_\nu\le1$, then

$$
\int_{1/3}^{2/3}\mathfrak K_{\Sigma_p}\,dp\le C h_\nu^3.
$$

This is an averaged statement about the minimizing branches; it gives no control of a fixed cut tracked by localization.
:::

:::{prf:proof}
The log-concave isoperimetric profile is nonnegative, concave, symmetric under $p\leftrightarrow1-p$, and vanishes at $0$ and $1$. Concavity makes $I(p)/p$ nonincreasing on $(0,1/2]$, hence

$$
h_\nu=\inf_{0<p<1}\frac{I(p)}{\min(p,1-p)}=2I(1/2).
$$

Symmetry and concavity also make $I(1/2)$ the maximum, so $\sup_{[1/3,2/3]}I\le h_\nu/2$. If $-I''_{\rm dist}$ denotes the nonnegative distributional second derivative measure, concavity and the chord bounds at $1/3$ and $2/3$ give

$$
(-I''_{\rm dist})((1/3,2/3))
\le I'_+(1/3)-I'_-(2/3)
\le 3h_\nu.
$$

For example, $I'_+(1/3)\le I(1/3)/(1/3)\le3h_\nu/2$, and symmetry gives the other endpoint bound. A concave function is twice differentiable at Lebesgue-almost every point; the density $-I''(p)$ of the absolutely continuous part is bounded in integral by the displayed distributional mass. At almost every point where both the granted smooth minimizer and $I''(p)$ exist, [](#lem:sol-profile-bound) gives

$$
\mathfrak K_{\Sigma_p}\le-I''(p)I(p)^2.
$$

Consequently

$$
\int_{1/3}^{2/3}\mathfrak K_{\Sigma_p}\,dp
\le \frac{h_\nu^2}{4}\int_{1/3}^{2/3}(-I''(p))\,dp
\le\frac34h_\nu^3.
$$

The hypothesis $h_\nu\le1$ is retained from the manuscript, although the displayed calculation does not need it.
:::

## 2\. Exact splitting and its persistence

:::{prf:proposition} = [](#prop:exact-splitting)
:label: prop:sol-exact-splitting
Let $\nu=e^{-V}dx$ be log-concave with convex support $K=K_1\times J$ in orthogonal coordinates $x=(y,z)\in\theta^\perp\oplus\R\theta$. If $\nabla^2V(\theta,\cdot)\equiv0$ on $\operatorname{int}K$, then

$$
V(y,z)=V_1(y)+cz
$$

for some constant $c$, and $\nu$ is the product of a log-concave law on $K_1$ and the log-affine law proportional to $e^{-cz}$ on $J$. Normalizability forces $J\ne\R$; an unbounded $J$ can only be a half-line with the decaying orientation and $c\ne0$.

Conversely, for an already split law of this form and $z_0\in\operatorname{int}J$, the cut $E=\{z\le z_0\}$ has $II_\Sigma=0$, $\nabla^2V(n,n)=0$, and $\mathfrak K_\Sigma=0$.
:::

:::{prf:proof}
On the connected set $\operatorname{int}(K_1\times J)$, the Hessian assumption says $\partial_z\nabla V=0$. Thus $\partial_zV$ is independent of $z$, while the mixed identities $\partial_{y_j}\partial_zV=0$ show that it is also independent of $y$. Hence $\partial_zV=c$ and integration gives $V(y,z)=V_1(y)+cz$ (up to an irrelevant additive constant). Both the density and its normalizing integral factorize. If $J=\R$, the integral $\int_\R e^{-cz}\,dz$ diverges for every $c$; the remaining assertions about $J$ follow immediately.

For the converse, $\Sigma=K_1\times\{z_0\}$ is a hyperplane in the product cylinder, so $II_\Sigma=0$, and the log-affine factor gives $\nabla^2V(n,n)=0$. The cut does not meet an endpoint of $J$. Along the lateral support boundary, the cylinder is flat in the $\theta$ direction, so the free-boundary contribution to the constant mode is also zero. Therefore $\mathfrak K_\Sigma=-\calI_\Sigma(1,1)=0$.
:::

The converse proved here starts from the global product. Nothing in the argument proves $\mathfrak K_\Sigma=0\Rightarrow$ global cylindrical or log-affine splitting.

:::{prf:proposition} = [](#prop:persistent-splitting)
:label: prop:sol-persistent-splitting
Fix $\theta\in S^{n-1}$ and write $x=y+z\theta$ in $\theta^\perp\oplus\R\theta$. Let

$$
V_1:\theta^\perp\longrightarrow(-\infty,+\infty],
\qquad
V_2:\R\longrightarrow(-\infty,+\infty]
$$

be proper lower-semicontinuous convex functions satisfying $0<\int e^{-V_i}<\infty$, and suppose that the extended-valued potential of $\mu$ obeys the global identity

```{math}
:label: eq:sol-global-additive-potential
V(y+z\theta)=V_1(y)+V_2(z)
\qquad\text{for every }(y,z)\in\theta^\perp\times\R.
```

Thus the identity includes the value $+\infty$ off the effective domain; in particular $\overline{\operatorname{dom}V}=\overline{\operatorname{dom}V_1} \times\overline{\operatorname{dom}V_2}$ and $\mu=\mu_1\otimes\mu_2$.

Then, at every time for which stochastic localization is defined and for every sample path, the localized extended-valued potential remains additively split and $\mu_t$ remains a product across $\theta^\perp\oplus\R\theta$. Consequently $A_t$ is block diagonal. Moreover, for every fixed orthogonal halfspace

$$
E_a=\{y+z\theta:z\le a\}
\qquad\text{with}\qquad 0<\mu(E_a)<1,
$$

there are real scalars $d_t,g_t,\kappa_t$ such that

$$
\delta_t=d_t\theta,
\qquad G_t=g_t\theta\theta^T,
\qquad K_t=\kappa_t\theta\theta^T.
$$

In particular $K_t$ has rank at most one for every $t$.
:::

:::{prf:proof}
The global identity [](#eq:sol-global-additive-potential) and Tonelli's theorem give $\mu=\mu_1\otimes\mu_2$; crucially, this also records the product effective domain rather than merely an additive formula on an unspecified support. Decompose $c_t=c_t'+c_t''\theta$, with $c_t'\in\theta^\perp$. Pointwise in the extended reals, the localized potential is

$$
\begin{aligned}
V_t(y,z)
&=V_1(y)+V_2(z)+\frac t2(\abs y^2+z^2)-c_t'\cdot y-c_t''z\\
&=\left(V_1(y)+\frac t2\abs y^2-c_t'\cdot y\right)
+\left(V_2(z)+\frac t2z^2-c_t''z\right).
\end{aligned}
$$

The two summands are again proper convex extended-valued functions. Their normalizing integrals are positive and finite: at $t=0$ this is an assumption and $c_0=0$, while at $t>0$ the positive quadratic term makes every linear tilt integrable, since

$$
e^{c_t'\cdot y-t\abs y^2/2}\le e^{\abs{c_t'}^2/(2t)},
\qquad
e^{c_t''z-tz^2/2}\le e^{\abs{c_t''}^2/(2t)}.
$$

Hence the normalizer factorizes and, for every realized $c_t$,

$$
\mu_t=\mu_{1,t}\otimes\mu_{2,t}.
$$

This is a pathwise identity, not an identity obtained after averaging over the localization noise. It proves the asserted block form of $A_t$.

The localization density is strictly positive and finite on $\operatorname{dom}V$, so $\mu_t$ and $\mu$ have the same null sets. Thus $0<p_t,q_t<1$ for the nontrivial fixed halfspace $E_a$. Since $E_a$ depends only on $z$, its two conditional laws factor as

$$
\mu_t(\,dy\,dz\mid E_a)
=\mu_{1,t}(dy)\,\mu_{2,t}(dz\mid z\le a),
\qquad
\mu_t(\,dy\,dz\mid E_a^c)
=\mu_{1,t}(dy)\,\mu_{2,t}(dz\mid z>a).
$$

The $y$-conditional means and covariances therefore coincide on the two colors, and all conditional cross-covariances vanish. If $d_t$ is the difference of the two conditional means in the $z$ coordinate and $g_t$ the difference of their conditional variances, then

$$
\delta_t=d_t\theta,
\qquad G_t=g_t\theta\theta^T.
$$

Finally, by the definition [](#eq:K-def),

$$
K_t=G_t+(q_t-p_t)\delta_t\delta_t^T
=\bigl(g_t+(q_t-p_t)d_t^2\bigr)\theta\theta^T.
$$

Taking $\kappa_t=g_t+(q_t-p_t)d_t^2$ proves the claim.
:::

## 3\. Gaussian localization

:::{prf:proposition} = [](#prop:gaussian-model)
:label: prop:sol-gaussian-model
For the standard Gaussian $\mu=\gamma_n$:

(i) $A_t=(1+t)^{-1}I_n$ deterministically;

(ii) $\E\int_0^T\lmax(A_t)\,dt\le T$, and the mass-martingale argument gives $\Prob(\tau\le T)\le9T\le1/2$ for $T\le1/18$, hence the conclusion of [](#thm:centroid-implies-kls) without Carleson input;

(iii) every halfspace cut has $e_t(E)=0$ for every $t$;

(iv) for every nontrivial halfspace, with $\sigma_t^2=(1+t)^{-1}$ and $r_t=\sigma_t^2\varphi(\alpha_t)^2/s_t$,

$$
r_t\le\frac2\pi\sigma_t^2,
\qquad
D_t=r_t(2\sigma_t^2-r_t)
\ge\left(2-\frac2\pi\right)\sigma_t^2r_t>0.
$$
:::

:::{prf:proof}
The posterior density is

$$
Z_t^{-1}\exp\left(-\frac{1+t}{2}\abs x^2+c_t\cdot x\right),
$$

so it is Gaussian with mean $a_t=c_t/(1+t)$ and covariance $A_t=(1+t)^{-1}I_n$. This proves (i), and $\int_0^T\lmax(A_t)dt=\log(1+T)\le T$.

For a balanced cut started at $p_0=1/2$ and stopped on exiting $[1/3,2/3]$, covariance decomposition gives $B_t\preceq A_t$, so the mass quadratic variation satisfies

$$
\E[p]_{T\wedge\tau}
=\E\int_0^{T\wedge\tau}s_tr_t\,dt
\le\frac14\int_0^T\lmax(A_t)\,dt\le\frac T4.
$$

Exiting requires a fluctuation of at least $1/6$; Doob's $L^2$ inequality therefore gives $\Prob(\tau\le T)\le36(T/4)=9T$. At $T\le1/18$ the posterior remains balanced with probability at least $1/2$. Its $T$-uniform log-concavity gives a boundary lower bound of order $\sqrt T$ [@BakryGentilLedoux2014; @Bobkov1999LogConcave; @Milman2009Isoperimetric], and the perimeter supermartingale transfers it to time zero. This is precisely the stopped centroid conclusion in (ii); the same argument handles the nested balanced window with changed universal constants.

For a fixed halfspace, every posterior is a scalar-covariance Gaussian, and Gaussian halfspaces minimize perimeter at their mass. Thus $\mu_t^+(E)=I_{\mu_t}(p_t)$ and $e_t(E)=0$, proving (iii).

After rotation, the halfspace depends on one $N(0,\sigma_t^2)$ marginal. If $\alpha_t$ is its normalized level, direct truncated-normal integration gives

$$
\abs{\delta_t}=\frac{\sigma_t\varphi(\alpha_t)}{s_t},
\qquad r_t=s_t\abs{\delta_t}^2
=\frac{\sigma_t^2\varphi(\alpha_t)^2}{s_t}.
$$

The inequality $\varphi(\alpha)^2\le(2/\pi)\Phi(\alpha)\Phi(-\alpha)$ follows from

$$
\operatorname{erf}(x)^2\le1-e^{-2x^2},\qquad x\ge0.
$$

For completeness, the left side equals $(4/\pi)\int_{[0,x]^2}e^{-(u^2+v^2)}\,du\,dv$; the square is contained in the quarter disk of radius $\sqrt2x$, whose normalized Gaussian integral is $1-e^{-2x^2}$. Taking $x=\abs\alpha/\sqrt2$ proves $r_t\le(2/\pi)\sigma_t^2$. Finally $A_t=\sigma_t^2I$ gives

$$
D_t=2s_t\delta_t^TA_t\delta_t-r_t^2
=2\sigma_t^2r_t-r_t^2,
$$

and (iv) follows.
:::

## 4\. Product localization and product KLS

:::{prf:proposition} = [](#prop:products)
:label: prop:sol-products
Let $\mu=\bigotimes_{i=1}^n\mu^{(i)}$ be a product of isotropic one-dimensional log-concave measures. Then, pathwise:

(i) $\mu_t$ remains a product and $A_t=\operatorname{diag}(A_t^{(1)},\ldots,A_t^{(n)})$;

(ii) each $A^{(i)}$ is a nonnegative supermartingale and $\Prob(\sup_{s\le t}A_s^{(i)}\ge\lambda)\le1/\lambda$ for $\lambda\ge1$;

(iii)

$$
h_{\mu_t}\ge c\min_i(A_t^{(i)})^{-1/2}
=c\lmax(A_t)^{-1/2}.
$$

In particular KLS holds for products, and the profile bound propagates the excess of any cut directly, with no bootstrap.
:::

:::{prf:proof}
For each realization of $c_t$, the unnormalized posterior density factorizes:

$$
\prod_{i=1}^n
\exp\left(-V_i(x_i)+c_{t,i}x_i-\frac t2x_i^2\right).
$$

Its normalizer is the product of the one-dimensional normalizers, proving (i). The diagonal covariance SDE reduces coordinatewise to

$$
dA_t^{(i)}=m_{3,t}^{(i)}\,dW_t^{(i)}-(A_t^{(i)})^2dt,
$$

where $m_{3,t}^{(i)}$ is the third centered moment of the $i$th posterior. Thus $A^{(i)}\ge0$ is a local supermartingale and hence a supermartingale. Since $A_0^{(i)}=1$, the nonnegative-supermartingale maximal inequality gives (ii).

The Poincaré constant tensorizes, while the one-dimensional log-concave bound is affine [@BakryGentilLedoux2014; @LeeVempala2018]:

$$
\CP(\mu_t)=\max_i\CP(\mu_t^{(i)})
\le C\max_i A_t^{(i)}=C\lmax(A_t).
$$

The reverse Cheeger–Poincaré comparison for log-concave measures [@BakryGentilLedoux2014; @LeeVempala2018] then yields $h_{\mu_t}\ge c\CP(\mu_t)^{-1/2}$, proving (iii). At $t=0$, isotropy makes the right side universal, which is KLS for product measures. More explicitly, for any cut $E$,

$$
\mu_t^+(E)=I_{\mu_t}(p_t)+e_t(E)
\ge c\lmax(A_t)^{-1/2}\min(p_t,q_t)+e_t(E),
$$

which is the asserted direct propagation statement.
:::

**Dependency and regularity audit.** The only ledger edge internal to this dossier runs from `cor:generic-degeneracy` to `lem:profile-bound`. The remaining proofs use the standard localization identities, Gaussian isoperimetry, tensorization, the one-dimensional log-concave Poincaré bound, and the log-concave Cheeger–Poincaré comparison already imported in the manuscript. The profile statements are expressly conditional on their smooth branch; no smoothing argument is used to manufacture minimizers. Product factorization is an identity of densities and survives the usual coordinatewise truncation/regularization. For [](#prop:sol-persistent-splitting), that identity is assumed globally for the extended-valued potential, so it includes product factorization of the effective support; an additive formula asserted only on a nonproduct support would not suffice. None of these statements uses numerical evidence or asserts a quantitative splitting converse. The manuscript phrase “rank-one $K_t$” in [](#prop:persistent-splitting) is understood structurally as $K_t=\kappa_t\theta\theta^T$; its actual rank can be zero (for example at a symmetric median cut), so an exact-rank-one reading would be false.
