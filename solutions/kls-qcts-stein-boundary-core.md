---
title: 'Solution: quadratic-chaos, Stein contrast, and boundary flux'
label: sec:sol-kls-qcts-stein-boundary-core
ledger-node:
- prop:qcts-equivalence
- prop:stein-rep
- lem:stein-vs-source
- lem:boundary-rep
- prop:two-tail
numbering:
  enumerator: D8.%s
---

**Overview.** This dossier proves [](#prop:stein-rep), [](#prop:qcts-equivalence), [](#lem:stein-vs-source), [](#lem:boundary-rep) and [](#prop:two-tail). The organizing identity is that testing a two-color cut against a centered quadratic gives $s\inner{K}{M}$. As a result, bounded quadratic-chaos variance is equivalent, up to constants, to a uniform bound on balanced two-color covariance contrasts. The same identity links the Stein quantity to the Riccati source and to boundary flux. An exact Gaussian two-tail example then rules out a universal one-slice Stein bound by absolute excess.

1. [](#prop:sol-stein-rep): the covariance decomposition [](#eq:sol-stein-cov-decomp) gives [](#eq:sol-stein-rep), and duality gives [](#eq:sol-stein-norm).
2. [](#prop:sol-qcts-equivalence): (i)⇒(ii) by Cauchy–Schwarz against the color [](#eq:sol-color-tensor). (ii)⇒(i) uses a deterministic median cut of $X^TMX$, which exists because the law has no atoms, giving [](#eq:sol-median-L1). The Carbery–Wright reverse moment bound [](#eq:sol-CW-reverse) then upgrades $L^1$ to $L^2$.
3. [](#lem:sol-stein-vs-source): with $G=K-(q-p)\delta\delta^T$ and $r^2\le D$, the Stein quantity and the source $S$ are comparable in a tight window, up to $64\eta^2D$.
4. [](#lem:sol-boundary-rep): on a smooth bounded convex domain, the Neumann solution $u_f$ and the divergence theorem give [](#eq:sol-boundary-rep); the support flux vanishes. Cauchy–Schwarz gives [](#eq:sol-trace-CS).
5. [](#prop:sol-two-tail): for $N(0,\diag(\Lambda,1,\dots))$ and a symmetric two-tail cut, $\delta=0$ and $\calS/s\sim\Lambda^2$, while the excess is $O(\Lambda^{-1/2})$. So no universal slice-wise bound of the stated form holds.

**Scope.** This dossier gives complete proofs of the five nodes in the header. The QCTS equivalence is proved for full-dimensional isotropic log-concave laws; this entails no loss, because an isotropic law has positive-definite covariance and hence full-dimensional convex support. The proof explicitly avoids an invalid appeal to an externally randomized median. The boundary result is first proved for smooth data on a smooth bounded domain, precisely the regularity class in its ledger statement.

## 1\. Two-color algebra and the Stein representation

Let $\nu$ be a probability measure on $\R^n$ with finite fourth moment, mean $a$, and covariance $A$. Let $E$ be measurable with $p=\nu(E)\in(0,1)$, put $F=E^c$, $q=1-p$, and $s=pq$. Write

$$
m^E=\E[X\mid E],\quad m^F=\E[X\mid F],\quad \delta=m^E-m^F,
$$

$$
\Sigma^E=\Cov(X\mid E),\quad \Sigma^F=\Cov(X\mid F),\quad
G=\Sigma^E-\Sigma^F,
$$

and

$$
K=G+(q-p)\delta\delta^T.
$$

Then $m^E-a=q\delta$, $m^F-a=-p\delta$, and

```{math}
:label: eq:sol-stein-cov-decomp
A=p\Sigma^E+q\Sigma^F+s\delta\delta^T.
```

:::{prf:proposition} = [](#prop:stein-rep)
:label: prop:sol-stein-rep
For every symmetric matrix $M$, set

$$
f_M(x)=(x-a)^TM(x-a)-\Tr(MA).
$$

Then

```{math}
:label: eq:sol-stein-rep
\ell_{\nu,E}(M):=\int_Ef_M\dd\nu
=\Cov_\nu\!\left(\one_E,(X-a)^TM(X-a)\right)
=s\inner{K}{M}.
```

Consequently

```{math}
:label: eq:sol-stein-norm
\calS_\nu(E):=\sup_{\norm M_\HS\le1}\abs{\ell_{\nu,E}(M)}^2
=s^2\norm K_\HS^2.
```
:::

:::{prf:proof}
The first equality is just $\E f_M=0$. Conditional expectation and [](#eq:sol-stein-cov-decomp) give

$$
\begin{aligned}
\int_E f_M\dd\nu
&=p\inner{M}{\Sigma^E+(m^E-a)(m^E-a)^T-A}\\
&=p\inner{M}{qG-s\delta\delta^T+q^2\delta\delta^T}\\
&=pq\inner{M}{G+(q-p)\delta\delta^T}
=s\inner{K}{M}.
\end{aligned}
$$

The Hilbert–Schmidt dual norm of $M\mapsto s\inner{K}{M}$ is $s\norm K_\HS$, proving [](#eq:sol-stein-norm).
:::

**Normalization precision.** The normalized Stein quantity is exactly $\calS_\nu(E)/s=s\norm K_\HS^2$. The scalar Riccati source is $S=s\norm G_\HS^2$. These are literally equal at balance, when $K=G$; off balance they are two normalizations of the same two-color covariance contrast, not equal expressions. [](#lem:sol-stein-vs-source) below gives the precise tight-window conversion, including its damping error.

## 2\. QCTS is equivalent to all balanced two-color tests

Let now $\nu$ be isotropic and log-concave, $X\sim\nu$, and $Z=XX^T-I_n$. Define

$$
\calQ(\nu)=\sup_{\substack{M=M^T\\\norm M_\HS=1}}
\Var_\nu(X^TMX).
$$

For a color $g=(\one_E-p)/\sqrt{s}$, [](#prop:sol-stein-rep) with $a=0$ and $A=I$ says, as a matrix identity,

```{math}
:label: eq:sol-color-tensor
\E[gZ]=\sqrt{s}\bigl(G+(q-p)\delta\delta^T\bigr).
```

:::{prf:proposition} = [](#prop:qcts-equivalence)
:label: prop:sol-qcts-equivalence
Up to universal changes of constant, the following are equivalent:

(i) $\calQ(\nu)\le C$;

(ii) for every measurable $E$ with $\nu(E)=1/2$, $pq\norm{\Sigma^E-\Sigma^F}_\HS^2\le C$.
:::

:::{prf:proof}
Assume (i). At balance $q-p=0$ and $\sqrt{s}=1/2$. For every symmetric $M$ with $\norm M_\HS=1$, Cauchy–Schwarz gives

$$
\abs{\inner{\E[gZ]}{M}}
=\abs{\E\bigl[g(X^TMX-\Tr M)\bigr]}
\le\sqrt{\Var(X^TMX)}\le\sqrt C,
$$

because $\E g=0$ and $\E g^2=1$. Taking the Hilbert–Schmidt dual supremum and using [](#eq:sol-color-tensor) yields $pq\norm G_\HS^2=\norm{\E[gZ]}_\HS^2\le C$, which is (ii).

Conversely assume (ii), fix a symmetric $M$ with $\norm M_\HS=1$, and put

$$
Y=X^TMX-\Tr M.
$$

Then $\E Y=0$. Since $\nu$ is isotropic, its convex support has nonempty interior and it is absolutely continuous there. The polynomial $x\mapsto x^TMx$ is nonconstant when $M\ne0$; every one of its level sets has Lebesgue measure zero. Thus the law of $Y$ has no atoms. Its distribution function is continuous, so there is a median $m$ for which the deterministic set $E=\{Y\ge m\}$ has exactly mass $1/2$. No auxiliary random variable or randomized slice of a median level set is needed. (For a law originally presented on a proper affine subspace one first works in its affine hull; ambient isotropy already excludes that case.)

For this cut, $g=2\one_E-1=\operatorname{sgn}(Y-m)$ almost surely and $\E g=0$. Hence

```{math}
:label: eq:sol-median-L1
\E[gY]=\E[g(Y-m)]=\E\abs{Y-m}.
```

On the other hand, (ii) and [](#eq:sol-color-tensor) imply $\norm{\E[gZ]}_\HS\le\sqrt C$, and therefore

$$
\E\abs{Y-m}=\inner{\E[gZ]}{M}\le\sqrt C.
$$

Theorem 7 of Carbery–Wright [@CarberyWright2001], applied with their moment parameters $q=2d$ and $r=d$ to a polynomial of degree $d\le2$, gives the reverse-moment consequence

```{math}
:label: eq:sol-CW-reverse
\norm P_{L^2(\nu)}\le C_2\norm P_{L^1(\nu)}
```

for every polynomial $P$ of degree at most two, with a numerical $C_2$ (indeed their theorem first gives $\norm P_2^{1/d}\le2C\norm P_1^{1/d}$). Apply it to $P=Y-m$. Since the mean is the best constant in $L^2$,

$$
\sqrt{\Var(Y)}=\norm{Y-\E Y}_2\le\norm{Y-m}_2
\le C_2\norm{Y-m}_1\le C_2\sqrt C.
$$

Taking the supremum over $M$ proves (i) with constant $C_2^2C$.
:::

**Obstruction audit for `rem:projection-ceiling`.** The converse does not infer QCTS from radial or projection tests. It assumes the full family of balanced measurable color tests and selects a cut adapted to each arbitrary symmetric matrix $M$; Carbery–Wright then upgrades an $L^1$ polynomial estimate to $L^2$. Thus the proof does not cross the projection-only ceiling recorded by `rem:projection-ceiling`.

## 3\. Tight-window conversion

In a localization posterior retain the notation $p,q,s,\delta,G,K$ above and put

$$
r=s\abs\delta^2,\qquad S=s\norm G_\HS^2,
\qquad D=2s\delta^TA\delta-r^2.
$$

Covariance decomposition gives $B=s\delta\delta^T\preceq A$. Thus $\delta^TA\delta\ge s\abs\delta^4$, and consequently $D\ge r^2$. Let $\tau_\eta=\inf\{t:\abs{p_t-1/2}>\eta\}$.

:::{prf:lemma} = [](#lem:stein-vs-source)
:label: lem:sol-stein-vs-source
For $0<\eta\le1/4$, on $\{t<\tau_\eta\}$,

$$
S_t\le2\frac{\calS_{\mu_t}(E)}{s_t}+64\eta^2D_t,
\qquad
\frac{\calS_{\mu_t}(E)}{s_t}\le2S_t+64\eta^2D_t.
$$
:::

:::{prf:proof}
On the tight window, $\abs{q-p}\le2\eta$ and $s\ge1/4-\eta^2\ge3/16>1/8$. From $G=K-(q-p)\delta\delta^T$ and [](#eq:sol-stein-norm),

$$
\begin{aligned}
s\norm G_\HS^2
&\le2s\norm K_\HS^2+2s(q-p)^2\abs\delta^4\\
&=2\frac{\calS}{s}+2(q-p)^2\frac{r^2}{s}
\le2\frac{\calS}{s}+64\eta^2r^2
\le2\frac{\calS}{s}+64\eta^2D.
\end{aligned}
$$

The reverse estimate follows from $K=G+(q-p)\delta\delta^T$ by the identical calculation.
:::

## 4\. Boundary representation with the support flux included

:::{prf:lemma} = [](#lem:boundary-rep)
:label: lem:sol-boundary-rep
Let $K\subset\R^n$ be a smooth bounded convex domain and $\nu=Z^{-1}e^{-V}\one_K\,dx$, where $V$ is smooth and convex on $\overline K$. Let $E$ be smooth relative to $K$, write $\Sigma=\partial^*E\cap\operatorname{int}K$, and choose on $\Sigma$ the unit normal $n$ pointing *into* $E$. For smooth $f$, put $\bar f=\int f\dd\nu$, and let $u_f$ be the mean-zero solution of

$$
Lu_f=f-\bar f\quad\hbox{in }K,
\qquad \partial_{n_K}u_f=0\quad\hbox{on }\partial K,
\qquad L=\Delta-\nabla V\cdot\nabla.
$$

With $\dd\sigma_\nu=Z^{-1}e^{-V}\dd\mathcal H^{n-1}$,

```{math}
:label: eq:sol-boundary-rep
\Cov_\nu(\one_E,f)=-\int_\Sigma\partial_nu_f\dd\sigma_\nu.
```

In particular, for the centered quadratic $f_M$ of [](#prop:sol-stein-rep),

```{math}
:label: eq:sol-trace-CS
\abs{\ell_{\nu,E}(M)}^2
\le\nu^+(E)\int_\Sigma\abs{\partial_nu_M}^2\dd\sigma_\nu,
\qquad u_M=u_{f_M}.
```
:::

:::{prf:proof}
The compatibility condition for the Neumann problem is $\int_K(f-\bar f)\dd\nu=0$. Standard uniformly elliptic Neumann theory on a smooth bounded connected domain therefore gives a weak solution unique modulo constants; the mean-zero condition fixes it. Smooth coefficients and smooth data give the boundary regularity needed for the normal traces below (or the same identity follows first weakly and then by density).

Since

$$
e^{-V}Lu_f=\operatorname{div}(e^{-V}\nabla u_f),
$$

the divergence theorem on $E\cap K$ yields two boundary pieces. On the relative interface $\Sigma$, the outward normal of $E$ is $-n$, contributing $-\int_\Sigma\partial_nu_f\dd\sigma_\nu$. On $\partial K\cap E$, the outward normal is $n_K$, and its contribution vanishes exactly by $\partial_{n_K}u_f=0$. Thus

$$
\int_E(f-\bar f)\dd\nu
=\int_E Lu_f\dd\nu
=-\int_\Sigma\partial_nu_f\dd\sigma_\nu,
$$

which is [](#eq:sol-boundary-rep). Cauchy–Schwarz on the weighted surface measure, whose total mass is $\nu^+(E)$ for a smooth relative cut, gives [](#eq:sol-trace-CS).
:::

## 5\. The exact anisotropic two-tail obstruction

Let $\Phi$ and $\varphi$ denote the standard Gaussian distribution function and density. For a probability $\nu$ and a set $E$ define the isoperimetric excess at its mass by

$$
e_\nu(E)=\nu^+(E)-I_\nu(\nu(E)).
$$

:::{prf:proposition} = [](#prop:two-tail)
:label: prop:sol-two-tail
Let $\Lambda\ge1$, $\nu_\Lambda=N(0,\diag(\Lambda,1,\ldots,1))$, and

$$
E_\Lambda=\{x:\abs{x_1}\ge a\sqrt\Lambda\},
\qquad a=\Phi^{-1}(3/4).
$$

Then $\nu_\Lambda(E_\Lambda)=1/2$ and:

(i) $\delta=0$, hence $r=D=0$ and $K=G$;

(ii) $G=8a\varphi(a)\Lambda e_1e_1^T$, and therefore $\calS_{\nu_\Lambda}(E_\Lambda)/s =16a^2\varphi(a)^2\Lambda^2$;

(iii) $\nu_\Lambda^+(E_\Lambda)=2\varphi(a)\Lambda^{-1/2}$ and

$$
e_{\nu_\Lambda}(E_\Lambda)
=\bigl(2\varphi(a)-\varphi(0)\bigr)\Lambda^{-1/2};
$$

(iv)

$$
\frac{e_{\nu_\Lambda}(E_\Lambda)}{I_{\nu_\Lambda}(1/2)}
=\frac{2\varphi(a)}{\varphi(0)}-1.
$$

Consequently no constants independent of $\nu$ can make

$$
\frac{\calS_\nu(E)}s\le C_0+C_1r+\beta D+C_2e_\nu(E)
$$

hold for every log-concave $\nu$ and every half-mass set $E$.
:::

:::{prf:proof}
Write $Z=X_1/\sqrt\Lambda\sim N(0,1)$. Since $\Prob(\abs Z\ge a)=2(1-\Phi(a))=1/2$, the set is balanced. Both colors are invariant under $x\mapsto-x$, so their conditional means vanish and (i) follows.

Only the first conditional variance changes between the colors. Integration by parts gives

$$
\int_a^\infty z^2\varphi(z)\dd z=a\varphi(a)+1-\Phi(a)
=a\varphi(a)+\frac14.
$$

After dividing the two-sided tail second moment by its probability $1/2$,

$$
\E[Z^2\mid\abs Z\ge a]=1+4a\varphi(a).
$$

Subtracting the unnormalised tail contribution from $\E Z^2=1$ gives

$$
\E[Z^2\mid\abs Z<a]=1-4a\varphi(a).
$$

Thus $G_{11}=8a\varphi(a)\Lambda$ and all other entries vanish. Since $s=1/4$ and $K=G$, [](#prop:sol-stein-rep) gives

$$
\frac{\calS}s=s\norm G_\HS^2=16a^2\varphi(a)^2\Lambda^2,
$$

proving (ii).

The relative boundary consists of the two hyperplanes $x_1=\pm a\sqrt\Lambda$; each has Gaussian boundary density $\varphi(a)/\sqrt\Lambda$. Hence $\nu_\Lambda^+(E_\Lambda)=2\varphi(a)/\sqrt\Lambda$. To determine the profile, write $\nu_\Lambda=T_\#\gamma_n$ with $T=\diag(\sqrt\Lambda,1,\ldots,1)$. If $A=T^{-1}E$, then $(A)_{\eps/\norm T_\op}\subseteq T^{-1}(E_\eps)$, so Gaussian isoperimetry implies

$$
\nu_\Lambda^+(E)\ge\frac1{\norm T_\op}I_{\gamma_n}(\nu_\Lambda(E))
=\Lambda^{-1/2}I_{\gamma_n}(\nu_\Lambda(E)).
$$

At mass $1/2$ this lower bound is $\varphi(0)\Lambda^{-1/2}$, and the halfspace $\{x_1\le0\}$ attains it. Therefore

$$
I_{\nu_\Lambda}(1/2)=\varphi(0)\Lambda^{-1/2}.
$$

Subtracting this from the computed two-tail perimeter proves (iii), and division proves (iv). Finally the proposed left side grows as $\Lambda^2$, whereas with $r=D=0$ its right side is $C_0+C_2O(\Lambda^{-1/2})$; letting $\Lambda\to\infty$ is the contradiction.
:::

The same exact powers explain the covariance weight recorded with this node. If an absolute-excess term is multiplied by a pure power $(1+\lmax(A))^\alpha$, then on this family it scales as $\Lambda^{\alpha-1/2}$. Matching a left side of order $\Lambda^2$ requires $\alpha\ge5/2$, and $\alpha=5/2$ is the threshold power. This is a static calibration only; it supplies no dynamical occupation estimate.

**Regularity and provenance audit.** The QCTS converse uses an exact deterministic median cut and a stated degree-two Carbery–Wright consequence; it does not hide a random extension of the probability space. The boundary proof includes both pieces of the relative boundary and records why the support piece vanishes. The two-tail calculation is exact and uses no floating generalized-eigenvalue or sampled evidence.
