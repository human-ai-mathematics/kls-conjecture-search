---
title: 'The linear test and the third-moment tensor'
label: sec:sol-lstm
ledger-node:
- lem:linear-sector-third-moment
- cor:gate-zero-third-moment
numbering:
  enumerator: D12.%s
---

*Part of the moment-map mechanism, Chapter [](#sec:cmh-normalization); the reading order is on the [full proofs](#sec:proofs-moment-map) page.*

**Overview.** This dossier proves [](#lem:linear-sector-third-moment) and [](#cor:gate-zero-third-moment) as [](#thm:sol-lstm-main) and [](#cor:sol-lstm-gate), under hypotheses $(\mathrm H)$ of [](#def:sol-lstm-hyp), which the manuscript hypotheses imply. The Stein identity for quadratic tests shows that the mixed tensor $\E_\mu[\tau_{ij}X_k]$ is half the third-moment tensor. Projecting each column $\tau a$ onto the span of $\mathbf 1,X_1,\dots,X_n$ then gives a Pythagorean decomposition, from which the corollary follows. The third-derivative form (c) is proved only under one additional stated hypothesis.

1. [](#lem:sol-lstm-logconcave), via [](#lem:sol-lstm-linear-growth), shows that the manuscript hypotheses imply $(\mathrm H)$.
2. [](#lem:sol-lstm-structure), using [](#lem:sol-lstm-sard), shows that $\nabla\varphi$ is a $C^1$ diffeomorphism between open sets of full measure. So $\tau$ is defined $\mu$-a.e. and satisfies the transport identity between $\mu$ and $\nu$.
3. [](#prop:sol-lstm-stein) proves the Stein identity [](#eq:sol-lstm-stein) for polynomials of degree at most two. The proof uses the divergence theorem on balls and shell selection ([](#lem:sol-lstm-shells)). Its consequences ([](#cor:sol-lstm-stein-consequences)) are $\E_\mu\tau=\Id$ and $T_{ijk}=N_{ijk}+N_{ikj}$.
4. [](#lem:sol-lstm-N): a symmetry argument applied to step 3 shows that $N$ is totally symmetric, so $N=\tfrac12T$.
5. Theorem (a) and (b): the $L^2(\mu)$ projection onto $\mathrm{span}\{\mathbf 1,X_b\}$, with coefficients taken from step 4, yields [](#eq:sol-lstm-pythagoras).
6. Corollary: since $\E_\mu\abs{\tau a}^2=a^\top\E_\mu[\tau^2]a$, step 5 gives the directional bound. Products of centered exponentials ([](#ex:sol-lstm-exponential)) attain the constant for $c=2$.
7. Part (c) is [](#prop:sol-lstm-third-derivative), proved under $\varphi\in C^3$ and $\varphi_{ijk}\in L^1(\nu)$ ([](#rem:sol-lstm-third-derivative-hypothesis)).

**Scope.** This dossier proves [](#lem:linear-sector-third-moment) and [](#cor:gate-zero-third-moment) of Section [](#subsec:gate-zero), verbatim, as [](#thm:sol-lstm-main) and [](#cor:sol-lstm-gate) below. It is self-contained: no ledger node is used, and in particular nothing is taken from the uncertified dossier for [](#lem:cmh-linear-spectral-resolution).

*What this dossier does not prove.* It proves nothing about [](#conj:gate-zero), [](#conj:gate-zero-sharp) or [](#conj:kls) beyond the exact implication stated in [](#cor:sol-lstm-gate); no bound on $\kappa_n$ of [](#eq:kappa-def); no statement about the trace-upgrade cluster (`conj:trace-upgrade`, high-rank `conj:stein-weighted`, `conj:product-alignment`), which is not opened here. The final sentence of the manuscript lemma, which identifies the third-moment tensor with $\E_\nu[\partial_{ijk}\varphi]$, is proved under one additional explicitly stated hypothesis ([](#prop:sol-lstm-third-derivative) and [](#rem:sol-lstm-third-derivative-hypothesis)); everything else is proved under the manuscript's hypotheses exactly.

## 1\. Setting, conventions, and the refined statements

Throughout, $n\ge1$, $\inner{\cdot}{\cdot}$ and $\abs{\cdot}$ are the Euclidean inner product and norm on $\R^n$, $\norm{\cdot}_{\HS}$ is the Hilbert–Schmidt norm on matrices and on $3$-tensors, and $\mathrm{Sym}_n$ is the space of real symmetric $n\times n$ matrices. For a $C^2$ function $\varphi$ we write $\varphi_i=\partial_i\varphi$, $\varphi_{ij}=\partial_{ij}\varphi$, $H=D^2\varphi=(\varphi_{ij})$, and, when $\varphi\in C^3$, $\varphi_{ijk}=\partial_{ijk}\varphi$. $B_R=\{\abs y<R\}$, $\partial B_R$ its boundary, $\sigma_R$ the $(n-1)$-dimensional surface measure on $\partial B_R$ (for $n=1$, counting measure on $\{\pm R\}$), and $\mathbf n(y)=y/\abs y$ the outward unit normal. Repeated indices are *not* summed unless a sum sign is written.

:::{prf:definition} Hypotheses
:label: def:sol-lstm-hyp
The standing hypotheses, written $(\mathrm H)$, are:

$(\mathrm H1)$ $\varphi\in C^2(\R^n)$ is convex and $\nu:=e^{-\varphi(y)}\dd y$ is a probability measure on $\R^n$;

$(\mathrm H2)$ $\mu:=(\nabla\varphi)_\#\nu$ (the moment measure of $\varphi$, [](#eq:moment-measure)) is absolutely continuous with respect to Lebesgue measure, has finite third moment $\E_\mu\abs X^3<\infty$, and is isotropic: $\E_\mu X=0$ and $\E_\mu[X\otimes X]=\Id$;

$(\mathrm H3)$ $\E_\nu\norm{D^2\varphi}_{\HS}^2<\infty$.
:::

:::{prf:lemma} The manuscript hypotheses imply $(\mathrm H)$
:label: lem:sol-lstm-logconcave
Let $\mu$ be an isotropic log-concave probability measure on $\R^n$ which is the moment measure of a convex $\varphi\in C^2(\R^n)$ with $\E_\nu\norm{D^2\varphi}_{\HS}^2<\infty$. Then $(\mathrm H1)$–$(\mathrm H3)$ hold.
:::

:::{prf:proof}
$(\mathrm H1)$ and $(\mathrm H3)$ are the hypotheses. In the convention of Chapter [](#sec:notation), a log-concave measure has a density $e^{-V}$ on its convex support $K$ with $V$ convex; extending $V$ by $+\infty$ off $K$ gives a convex $V:\R^n\to(-\infty,+\infty]$ with $\int e^{-V}=1$. So $\mu\ll\mathrm{Leb}$, and [](#lem:sol-lstm-linear-growth) below gives $\E_\mu\abs X^3<\infty$. Isotropy is the hypothesis.
:::

:::{prf:definition} Third-moment tensor
:label: def:sol-lstm-T3
Under $(\mathrm H2)$ put, exactly as in Section [](#subsec:gate-zero),

$$
T_{ijk}:=\E_\mu[X_iX_jX_k],\qquad T_3(\mu):=(T_{ijk})_{i,j,k},\qquad
T_3(a):=\E_\mu\bigl[\inner Xa\,X\otimes X\bigr]\in\mathrm{Sym}_n\quad(a\in\R^n),
$$

so that $T_3(a)_{ib}=\sum_kT_{kib}\,a_k$. All entries are finite by $\E_\mu\abs X^3<\infty$, $T_{ijk}$ is symmetric in $(i,j,k)$, $T_3(a)$ is symmetric, and $\norm{T_3(a)}_{\HS}^2=\sum_{i,b}T_3(a)_{ib}^2$.
:::

The canonical Stein kernel is defined in Section [](#subsec:mm-stein) as $\tau_\mu=H\circ(\nabla\varphi)^{-1}$, [](#eq:stein-kernel-def). Under $(\mathrm H)$ alone $\nabla\varphi$ need not be injective on all of $\R^n$; [](#lem:sol-lstm-structure) shows that it is injective on an open set of full $\nu$-measure whose image is an open set of full $\mu$-measure, so that [](#eq:stein-kernel-def) defines $\tau$ $\mu$-almost everywhere, which is all that $L^2(\mu)$ statements need. In the compact-target regular class of [](#thm:regular-moment-map-compact-target) the two open sets are $\R^n$ and $\operatorname{int}P$ and nothing is new.

:::{prf:theorem} refined form of [](#lem:linear-sector-third-moment)
:label: thm:sol-lstm-main
Assume $(\mathrm H)$ and let $\tau$ be the canonical Stein kernel of [](#lem:sol-lstm-structure). Then every entry $\tau_{ij}$ lies in $L^2(\mu)$, and:

(a) $\E_\mu[\tau]=\Id$, and for all $i,j,k$,

$$
\E_\mu[\tau_{ij}X_k]=\E_\nu[\varphi_{ij}\varphi_k]=\tfrac12\,\E_\mu[X_iX_jX_k];
$$

in particular $\bigl(\E_\nu[\varphi_{ij}\varphi_k]\bigr)_{i,j,k}$ is totally symmetric.

(b) For every $a\in\R^n$ the column $\tau a$ decomposes in $L^2(\mu;\R^n)$ as

$$
\tau a=a+\tfrac12\,T_3(a)\,X+v_a,\qquad \E_\mu[v_a]=0,\qquad \E_\mu[v_a\otimes X]=0,
$$

the three summands $a$, $\tfrac12T_3(a)X$, $v_a$ being pairwise orthogonal in $L^2(\mu;\R^n)$, and consequently

```{math}
:label: eq:sol-lstm-pythagoras
\E_\mu\abs{\tau a}^2=\abs a^2+\tfrac14\norm{T_3(a)}_{\HS}^2+\E_\mu\abs{v_a}^2 .
```

(c) If in addition $\varphi\in C^3(\R^n)$ and $\varphi_{ijk}\in L^1(\nu)$ for all $i,j,k$, then $\E_\nu[\varphi_{ijk}]=\tfrac12\,\E_\mu[X_iX_jX_k]$.
:::

Part (b) is the display of [](#lem:linear-sector-third-moment); part (a) is the source-coordinate content of its last sentence, and part (c) is that sentence's third-derivative form (see [](#rem:sol-lstm-third-derivative-hypothesis)).

:::{prf:corollary} refined form of [](#cor:gate-zero-third-moment)
:label: cor:sol-lstm-gate
Assume $(\mathrm H)$. Then $\E_\mu[\tau^2]=\E_\nu[H^2]$ is a finite symmetric positive semidefinite matrix and, for every unit vector $a$,

$$
\norm{T_3(a)}_{\HS}^2\le4\bigl(a^\top\E_\mu[\tau^2]\,a-1\bigr)
\le4\bigl(\lmax(\E_\mu[\tau^2])-1\bigr).
$$

In particular, if $\mathcal C$ is any class of measures satisfying $(\mathrm H)$ with $\E_\mu[\tau^2]\preceq c\,\Id$ for every member, then $c\ge1$ and every directional third moment in $\mathcal C$ satisfies $\norm{T_3(a)}_{\HS}\le2\sqrt{c-1}$ for all unit $a$: the constant $c=4$ of [](#eq:gate-zero) gives $2\sqrt3$ and the constant $c=2$ of [](#eq:gate-zero-sharp) gives $2$, which the products of centered exponentials of [](#ex:sol-lstm-exponential) attain in every direction. Conversely, if a measure satisfying $(\mathrm H)$ has $\norm{T_3(a)}_{\HS}>2\sqrt3$ for some unit $a$, then $a^\top\E_\nu[H^2]a>4$, so $\E_\nu[H^2]\not\preceq4\Id$ and $\mu$ violates [](#eq:gate-zero).
:::

## 2\. Preliminaries

:::{prf:lemma} Linear growth of an integrable convex function
:label: lem:sol-lstm-linear-growth
Let $V:\R^n\to(-\infty,+\infty]$ be convex with $0<\int_{\R^n}e^{-V(y)}\dd y<\infty$. Then there are $c>0$ and $C<\infty$ with $V(y)\ge c\abs y-C$ for every $y\in\R^n$. Consequently $\int e^{\eps\abs y}e^{-V}\dd y<\infty$ for every $\eps<c$, and $\int\abs y^ke^{-V}\dd y<\infty$ for every $k\ge0$.
:::

:::{prf:proof}
Let $D=\{V<\infty\}$, a convex set. Since $\int e^{-V}>0$, $D$ has positive Lebesgue measure, hence nonempty interior (a convex set with empty interior lies in an affine hyperplane). Fix $y_0\in\operatorname{int}D$; $V$ is finite and continuous on a neighbourhood of $y_0$ and has a subgradient $g$ at $y_0$: $V(y)\ge V(y_0)+\inner g{y-y_0}$ for all $y$. Put $m_0=V(y_0)$ and $K=\{V\le m_0+1\}$, a convex set containing a ball $B_\delta(y_0)$, $\delta>0$, and of finite Lebesgue measure, since $e^{-(m_0+1)}\mathrm{Leb}(K)\le\int e^{-V}$. If $z\in K$ then $\operatorname{conv}(B_\delta(y_0)\cup\{z\})\subset K$ contains the cone with apex $z$ over the $(n-1)$-disc of radius $\delta$ centred at $y_0$ and orthogonal to $z-y_0$, whose volume is $\frac1n\omega_{n-1}\delta^{n-1}\abs{z-y_0}$ ($\omega_{n-1}$ the volume of the unit ball of $\R^{n-1}$, $\omega_0=1$). Hence $\abs{z-y_0}\le\rho_0:=n\,\mathrm{Leb}(K)/(\omega_{n-1}\delta^{n-1})$ for every $z\in K$. Put $\rho=\rho_0+1$; every $z$ with $\abs{z-y_0}=\rho$ satisfies $V(z)>m_0+1$.

Let $\abs{y-y_0}\ge\rho$ and $V(y)<\infty$. With $t=\rho/\abs{y-y_0}\in(0,1]$ and $z=y_0+t(y-y_0)$, convexity gives $V(z)\le tV(y)+(1-t)m_0$, so $V(y)\ge m_0+(V(z)-m_0)/t\ge m_0+\abs{y-y_0}/\rho$; the same bound is trivial when $V(y)=+\infty$. For $\abs{y-y_0}<\rho$ the subgradient inequality gives $V(y)\ge m_0-\abs g\rho$. Hence $V(y)\ge\abs{y-y_0}/\rho-C_1$ for all $y$, with $C_1=\abs g\rho+\abs{m_0}+1$, and therefore $V(y)\ge c\abs y-C$ with $c=1/\rho$, $C=C_1+\abs{y_0}/\rho$. Finally $e^{\eps\abs y}e^{-V(y)}\le e^{C}e^{-(c-\eps)\abs y}$ is integrable for $\eps<c$, and $\abs y^k\le k!\,\eps^{-k}e^{\eps\abs y}$.
:::

:::{prf:lemma} Critical values of a $C^1$ map are null
:label: lem:sol-lstm-sard
Let $F\in C^1(\R^n;\R^n)$ and $Z=\{y:\det DF(y)=0\}$. Then $F(Z)$ is a Lebesgue-null set.
:::

:::{prf:proof}
$Z$ is closed, so $F(Z)$ is $\sigma$-compact and it suffices to treat $Z\cap Q_0$ for a closed cube $Q_0$ of side $1$. Let $L=\max_{Q_0}\norm{DF}_{\op}$ and $\omega(d)=\sup\{\norm{DF(y)-DF(y')}_{\op}:y,y'\in Q_0,\ \abs{y-y'}\le d\}$, so that $\omega(d)\to0$ as $d\to0$ by uniform continuity of $DF$ on $Q_0$. Partition $Q_0$ into $N^n$ closed subcubes of side $1/N$ and diameter $d=\sqrt n/N$. Let $Q$ be a subcube meeting $Z$ at some $y_0$. For $y\in Q$,

$$
F(y)-F(y_0)-DF(y_0)(y-y_0)=\int_0^1\bigl(DF(y_0+s(y-y_0))-DF(y_0)\bigr)(y-y_0)\dd s
$$

has norm at most $\omega(d)d$, while $DF(y_0)(y-y_0)$ lies in the range of $DF(y_0)$, a linear subspace of dimension at most $n-1$, hence in some hyperplane $E'$, and has norm at most $Ld$. Splitting the remainder into its components along $E'$ and $E'^{\perp}$, $F(Q)-F(y_0)$ is contained in the cylinder $\{e+r:\ e\in E',\ \abs e\le(L+\omega(d))d,\ r\perp E',\ \abs r\le\omega(d)d\}$, whose volume is $2\omega_{n-1}\bigl((L+\omega(d))d\bigr)^{n-1}\omega(d)d$. Summing over at most $N^n$ subcubes,

$$
\mathrm{Leb}\bigl(F(Z\cap Q_0)\bigr)\le N^n\cdot2\omega_{n-1}(L+\omega(d))^{n-1}\omega(d)\,d^n
=2\omega_{n-1}n^{n/2}(L+\omega(d))^{n-1}\,\omega(d)\xrightarrow[N\to\infty]{}0 .
$$
:::

:::{prf:lemma} Structure of the moment map; the canonical Stein kernel
:label: lem:sol-lstm-structure
Assume $(\mathrm H1)$ and $\mu=(\nabla\varphi)_\#\nu\ll\mathrm{Leb}$. Let $G=\{y\in\R^n:\det H(y)>0\}$ and $\Omega=\nabla\varphi(G)$. Then:

(i) if $y_1\ne y_2$ and $\nabla\varphi(y_1)=\nabla\varphi(y_2)$, then $H(y_1)(y_2-y_1)=0$; in particular $\nabla\varphi$ is injective on $G$ and $(\nabla\varphi)^{-1}(\Omega)=G$;

(ii) $G$ is open with $\nu(G)=1$, $\Omega$ is open with $\mu(\Omega)=1$, and $\nabla\varphi|_G:G\to\Omega$ is a $C^1$ diffeomorphism;

(iii) the function $\tau:\R^n\to\mathrm{Sym}_n$ defined by $\tau:=H\circ(\nabla\varphi|_G)^{-1}$ on $\Omega$ and $\tau:=\Id$ on $\R^n\setminus\Omega$ is Borel, continuous and positive semidefinite on $\Omega$, and satisfies $\tau\circ\nabla\varphi=H$ on $G$, hence $\nu$-almost everywhere. It is the canonical Stein kernel [](#eq:stein-kernel-def), and any two versions of it agree $\mu$-a.e.;

(iv) (transport) for every Borel $\Phi:\R^n\times\mathrm{Sym}_n\to[0,\infty]$, $\E_\mu\bigl[\Phi(X,\tau(X))\bigr]=\E_\nu\bigl[\Phi(\nabla\varphi,H)\bigr]$; the same holds for real-valued $\Phi$ whenever either side is absolutely convergent, and then both are.
:::

:::{prf:proof}
(i) Put $p=\nabla\varphi(y_1)=\nabla\varphi(y_2)$ and $w=y_2-y_1\ne0$. The subgradient inequalities $\varphi(y_2)\ge\varphi(y_1)+\inner pw$ and $\varphi(y_1)\ge\varphi(y_2)-\inner pw$ add to $0\ge0$, so both are equalities. The function $g(t)=\varphi(y_1+tw)-\varphi(y_1)-t\inner pw$, $t\in\R$, is $C^2$, convex, nonnegative (by the subgradient inequality at $y_1$), and $g(0)=g(1)=0$; by convexity $g\equiv0$ on $[0,1]$. Hence $g''(0)=\inner{H(y_1)w}{w}=0$ (the two-sided second derivative exists because $\varphi\in C^2$, and it is computed from the right, where $g$ vanishes identically). Since $H(y_1)\succeq0$, $\inner{H(y_1)w}w=0$ forces $H(y_1)w=0$. Thus a point of $G$ shares its gradient with no other point: $\nabla\varphi$ is injective on $G$, and a point outside $G$ cannot map into $\Omega$, i.e. $(\nabla\varphi)^{-1}(\Omega)=G$.

(ii) $G$ is open by continuity of $\det H$. $Z:=\R^n\setminus G=\{\det H=0\}$ is the critical set of the $C^1$ map $\nabla\varphi$, so $\nabla\varphi(Z)$ is Lebesgue-null by [](#lem:sol-lstm-sard), hence $\mu$-null by $\mu\ll\mathrm{Leb}$, hence $0=\mu(\nabla\varphi(Z))=\nu\bigl((\nabla\varphi)^{-1}(\nabla\varphi(Z))\bigr)\ge\nu(Z)$. So $\nu(G)=1$ and $\mu(\Omega)=\nu((\nabla\varphi)^{-1}(\Omega))=\nu(G)=1$ by (i). On $G$ the map $\nabla\varphi$ is $C^1$, injective, with invertible differential $H$; by the inverse function theorem it is open, so $\Omega$ is open, and its inverse is $C^1$ on $\Omega$.

(iii) Continuity on $\Omega$ follows from (ii); Borel measurability on $\R^n$ from that and from $\Omega$ being open; positive semidefiniteness from convexity of $\varphi$. For $y\in G$, $\tau(\nabla\varphi(y))=H\bigl((\nabla\varphi|_G)^{-1}(\nabla\varphi(y))\bigr)=H(y)$. The formula [](#eq:stein-kernel-def) is exactly $H\circ(\nabla\varphi)^{-1}$ on the set $\Omega$ where the inverse is defined, and $\mu(\R^n\setminus\Omega)=0$.

(iv) For $y\in G$, $\Phi(\nabla\varphi(y),\tau(\nabla\varphi(y)))=\Phi(\nabla\varphi(y),H(y))$ by (iii), so the two functions agree $\nu$-a.e. and $\E_\nu[\Phi(\nabla\varphi,\tau\circ\nabla\varphi)]=\E_\nu[\Phi(\nabla\varphi,H)]$; the left side equals $\E_\mu[\Phi(X,\tau(X))]$ by the definition of the pushforward. The real-valued case follows by applying this to $\abs\Phi$, $\Phi^+$ and $\Phi^-$.
:::

:::{prf:lemma} Shell selection
:label: lem:sol-lstm-shells
Assume $(\mathrm H1)$. Let $F_1,\dots,F_m:\R^n\to[0,\infty]$ be Borel with $\int F_l\dd\nu<\infty$ for each $l$. Then there is a sequence $R_k\to\infty$ such that $\int_{\partial B_{R_k}}F_l\,e^{-\varphi}\dd\sigma_{R_k}\to0$ for every $l=1,\dots,m$.
:::

:::{prf:proof}
Put $F=F_1+\dots+F_m$ and $S(R)=\int_{\partial B_R}Fe^{-\varphi}\dd\sigma_R\in[0,\infty]$. By Tonelli's theorem in polar coordinates, $S$ is Borel on $(0,\infty)$ and $\int_0^\infty S(R)\dd R=\int_{\R^n}Fe^{-\varphi}\dd y<\infty$. For each $k\ge1$ the set $\{R\ge k:S(R)\le1/k\}$ has positive Lebesgue measure, since otherwise $S>1/k$ a.e. on $[k,\infty)$ and $S\notin L^1$; pick $R_k$ in it. Then $R_k\ge k$ and $0\le\int_{\partial B_{R_k}}F_le^{-\varphi}\dd\sigma_{R_k}\le S(R_k)\le1/k$.
:::

## 3\. The Stein identity for polynomials of degree at most two

:::{prf:proposition} Quadratic Stein identity
:label: prop:sol-lstm-stein
Assume $(\mathrm H)$ and let $f:\R^n\to\R$ be a polynomial of degree at most $2$. Then for every $i$, $X_if(X)\in L^1(\mu)$, $\tau_{ij}(X)\,\partial_jf(X)\in L^1(\mu)$ for every $j$, and

```{math}
:label: eq:sol-lstm-stein
\E_\mu\bigl[X_if(X)\bigr]=\sum_{j=1}^n\E_\mu\bigl[\tau_{ij}(X)\,\partial_jf(X)\bigr] .
```

In source coordinates: $\E_\nu[\varphi_i\,f(\nabla\varphi)]=\sum_j\E_\nu[\varphi_{ij}\,(\partial_jf)(\nabla\varphi)]$.
:::

:::{prf:proof}
Choose $C_f<\infty$ with $\abs{f(x)}\le C_f(1+\abs x^2)$ and $\abs{\partial_jf(x)}\le C_f(1+\abs x)$ for all $x$ and $j$. *Integrability.* $\abs{X_if(X)}\le C_f\abs X(1+\abs X^2)\in L^1(\mu)$ by $(\mathrm H2)$. Next, $\E_\mu[\tau_{ij}^2]=\E_\nu[\varphi_{ij}^2]\le\E_\nu\norm H_{\HS}^2<\infty$ by [](#lem:sol-lstm-structure)(iv) and $(\mathrm H3)$, so $\abs{\tau_{ij}\partial_jf}\le C_f\abs{\tau_{ij}}(1+\abs X)\le C_f\bigl(\tfrac12\tau_{ij}^2+1+\abs X^2\bigr)\in L^1(\mu)$, using $\E_\mu\abs X^2=\Tr\Id=n$. By [](#lem:sol-lstm-structure)(iv) the source integrands $\varphi_if(\nabla\varphi)$ and $\varphi_{ij}(\partial_jf)(\nabla\varphi)$ are in $L^1(\nu)$ with the same integrals.

*Integration by parts on balls.* The vector field $W=f(\nabla\varphi)e^{-\varphi}e_i$ is $C^1$ on $\R^n$ because $\varphi\in C^2$, with

$$
\Div W=\partial_i\bigl[f(\nabla\varphi)e^{-\varphi}\bigr]
=\Bigl[\sum_j(\partial_jf)(\nabla\varphi)\,\varphi_{ji}-f(\nabla\varphi)\,\varphi_i\Bigr]e^{-\varphi}.
$$

The divergence theorem on $B_R$ and $\varphi_{ji}=\varphi_{ij}$ give, for every $R>0$,

```{math}
:label: eq:sol-lstm-ibp-ball
\sum_j\int_{B_R}\varphi_{ij}(\partial_jf)(\nabla\varphi)\dd\nu-\int_{B_R}\varphi_if(\nabla\varphi)\dd\nu
=\int_{\partial B_R}f(\nabla\varphi)\,\mathbf n_i\,e^{-\varphi}\dd\sigma_R .
```

The right side is bounded in absolute value by $C_f\int_{\partial B_R}(1+\abs{\nabla\varphi}^2)e^{-\varphi}\dd\sigma_R$, and $\int(1+\abs{\nabla\varphi}^2)\dd\nu=1+\E_\mu\abs X^2=1+n<\infty$. Apply [](#lem:sol-lstm-shells) with $F_1=1+\abs{\nabla\varphi}^2$ and let $R=R_k\to\infty$ in [](#eq:sol-lstm-ibp-ball): the right side tends to $0$, and each integral on the left converges to the integral over $\R^n$ by dominated convergence, since the integrands are in $L^1(\nu)$. This is the source-coordinate identity; [](#eq:sol-lstm-stein) follows by [](#lem:sol-lstm-structure)(iv).
:::

:::{prf:corollary} Consequences
:label: cor:sol-lstm-stein-consequences
Assume $(\mathrm H)$. Then, for all $i,j,k$:

(i) $\E_\mu[\tau_{ij}]=\E_\mu[X_iX_j]=\delta_{ij}$, i.e. $\E_\mu\tau=\E_\nu H=\Id$;

(ii) $\E_\mu[X_iX_jX_k]=\E_\mu[\tau_{ij}X_k]+\E_\mu[\tau_{ik}X_j]$.
:::

:::{prf:proof}
Take $f(x)=x_j$ in [](#eq:sol-lstm-stein): $\partial_lf=\delta_{lj}$, so $\E_\mu[X_iX_j]=\E_\mu[\tau_{ij}]$, and $\E_\mu[X_iX_j]=\delta_{ij}$ by isotropy; the source form is [](#lem:sol-lstm-structure)(iv). Take $f(x)=x_jx_k$: $\partial_lf(x)=\delta_{lj}x_k+\delta_{lk}x_j$, so $\E_\mu[X_iX_jX_k]=\E_\mu[\tau_{ij}X_k]+\E_\mu[\tau_{ik}X_j]$.
:::

## 4\. Total symmetry of the mixed tensor

:::{prf:lemma} The mixed tensor is half the third moment
:label: lem:sol-lstm-N
Assume $(\mathrm H)$ and put $N_{ijk}:=\E_\mu[\tau_{ij}X_k]=\E_\nu[\varphi_{ij}\varphi_k]$. Then every $N_{ijk}$ is finite, $N$ is totally symmetric in $(i,j,k)$, and $N_{ijk}=\tfrac12T_{ijk}$ for all $i,j,k$.
:::

:::{prf:proof}
The two expressions for $N_{ijk}$ agree by [](#lem:sol-lstm-structure)(iv), and $\abs{N_{ijk}}\le(\E_\mu\tau_{ij}^2)^{1/2}(\E_\mu X_k^2)^{1/2}<\infty$ by Cauchy–Schwarz, $(\mathrm H3)$ and isotropy. Symmetry in the first two indices, $N_{ijk}=N_{jik}$, is the symmetry of $H$. [](#cor:sol-lstm-stein-consequences)(ii) reads $T_{ijk}=N_{ijk}+N_{ikj}$; the same identity with the roles of $i$ and $j$ exchanged reads $T_{jik}=N_{jik}+N_{jki}$. Since $T_{ijk}=T_{jik}$ and $N_{ijk}=N_{jik}$, subtracting gives $N_{ikj}=N_{jki}$, and applying first-pair symmetry to the right side, $N_{ikj}=N_{kji}$. Relabelling $(i,k,j)\to(a,b,c)$ this is $N_{abc}=N_{cba}$: $N$ is invariant under the transposition of its first and third indices. Together with invariance under the transposition of the first two indices, $N$ is invariant under the group these two transpositions generate, namely all of $S_3$. Finally $T_{ijk}=N_{ijk}+N_{ikj}=2N_{ijk}$.
:::

## 5\. Proof of [](#thm:sol-lstm-main)

:::{prf:proof} Proof of [](#thm:sol-lstm-main)
$\tau_{ij}\in L^2(\mu)$ was shown in the proof of [](#prop:sol-lstm-stein).

*(a)* is [](#cor:sol-lstm-stein-consequences)(i) and [](#lem:sol-lstm-N).

*(b)* By isotropy, the functions $\mathbf 1,X_1,\dots,X_n$ are orthonormal in $L^2(\mu)$: $\E_\mu[\mathbf 1^2]=1$, $\E_\mu[X_b]=0$, $\E_\mu[X_bX_c]=\delta_{bc}$. Let $P$ be the orthogonal projection of $L^2(\mu)$ onto their span $\mathcal V$. For $u\in L^2(\mu)$, $Pu=\E_\mu[u]\,\mathbf 1+\sum_b\E_\mu[uX_b]\,X_b$, and $u-Pu\perp\mathcal V$, i.e.\ $\E_\mu[u-Pu]=0$ and $\E_\mu[(u-Pu)X_b]=0$ for all $b$. Fix $a\in\R^n$ and apply this to $u_i:=(\tau a)_i=\sum_k\tau_{ik}a_k\in L^2(\mu)$. By (a),

$$
\E_\mu[u_i]=\sum_k\delta_{ik}a_k=a_i,
\qquad
\E_\mu[u_iX_b]=\sum_ka_kN_{ikb}=\tfrac12\sum_ka_kT_{kib}=\tfrac12\,T_3(a)_{ib},
$$

using total symmetry $N_{ikb}=N_{kib}$, [](#lem:sol-lstm-N), and [](#def:sol-lstm-T3). Hence $Pu_i=a_i\mathbf 1+\tfrac12\sum_bT_3(a)_{ib}X_b=\bigl(a+\tfrac12T_3(a)X\bigr)_i$. Define $v_a:=\tau a-a-\tfrac12T_3(a)X$, so that $(v_a)_i=u_i-Pu_i$. Then $\E_\mu[(v_a)_i]=0$ and $\E_\mu[(v_a)_iX_b]=0$ for all $i,b$, which is $\E_\mu[v_a]=0$ and $\E_\mu[v_a\otimes X]=0$. Pairwise orthogonality in $L^2(\mu;\R^n)$: $\E_\mu\inner a{T_3(a)X}=\inner a{T_3(a)\E_\mu X}=0$; $\E_\mu\inner a{v_a}=\inner a{\E_\mu v_a}=0$; $\E_\mu\inner{T_3(a)X}{v_a}=\sum_{i,b}T_3(a)_{ib}\E_\mu[X_b(v_a)_i]=0$. Therefore, expanding $\abs{\tau a}^2=\abs{a+\tfrac12T_3(a)X+v_a}^2$ and taking expectations, the cross terms vanish and

$$
\E_\mu\abs{\tau a}^2=\abs a^2+\tfrac14\E_\mu\abs{T_3(a)X}^2+\E_\mu\abs{v_a}^2,
\qquad
\E_\mu\abs{T_3(a)X}^2=\sum_{i,b,c}T_3(a)_{ib}T_3(a)_{ic}\E_\mu[X_bX_c]=\norm{T_3(a)}_{\HS}^2,
$$

which is [](#eq:sol-lstm-pythagoras).

*(c)* is [](#prop:sol-lstm-third-derivative) below.
:::

## 6\. Proof of [](#cor:sol-lstm-gate), and the saturating example

:::{prf:proof} Proof of [](#cor:sol-lstm-gate)
Each entry of $\tau^2$ satisfies $\abs{(\tau^2)_{ij}}\le\norm\tau_{\HS}^2$, which is $\mu$-integrable by $(\mathrm H3)$ and [](#lem:sol-lstm-structure)(iv); the same lemma gives $\E_\mu[\tau^2]=\E_\nu[H^2]$ entrywise, and this matrix is symmetric positive semidefinite as an average of squares of symmetric matrices. Since $\tau$ is symmetric, $\abs{\tau a}^2=a^\top\tau^\top\tau a=a^\top\tau^2a$, so $\E_\mu\abs{\tau a}^2=a^\top\E_\mu[\tau^2]a\le\lmax(\E_\mu[\tau^2])\abs a^2$. For unit $a$, [](#eq:sol-lstm-pythagoras) gives $\norm{T_3(a)}_{\HS}^2=4\bigl(\E_\mu\abs{\tau a}^2-1-\E_\mu\abs{v_a}^2\bigr)\le4\bigl(a^\top\E_\mu[\tau^2]a-1\bigr)\le4\bigl(\lmax(\E_\mu[\tau^2])-1\bigr)$.

If $\E_\mu[\tau^2]\preceq c\,\Id$ on a class, then for any member and unit $a$, $c\ge a^\top\E_\mu[\tau^2]a=\E_\mu\abs{\tau a}^2\ge\abs a^2=1$ by [](#eq:sol-lstm-pythagoras), and $\norm{T_3(a)}_{\HS}^2\le4(c-1)$. With $c=4$ this is $2\sqrt3$ and with $c=2$ it is $2$; [](#ex:sol-lstm-exponential) shows that the products of centered exponentials satisfy $(\mathrm H)$, have $\E_\mu[\tau^2]=2\Id$, and have $\norm{T_3(a)}_{\HS}=2$ for every unit $a$. Conversely, if $\norm{T_3(a)}_{\HS}>2\sqrt3$ for some unit $a$, the first inequality gives $a^\top\E_\nu[H^2]a=a^\top\E_\mu[\tau^2]a>1+3=4$, so $\E_\nu[H^2]\not\preceq4\Id$, which is the negation of [](#eq:gate-zero) for $\mu$ in isotropic position ($\Sigma=\Id$).
:::

:::{prf:example} Products of centered exponentials
:label: ex:sol-lstm-exponential
Let $\varphi(y)=\sum_{j=1}^n(e^{y_j}-y_j)$ on $\R^n$. It is smooth and convex, and $e^{-\varphi(y)}=\prod_je^{y_j}e^{-e^{y_j}}$ is the density of $(\log E_1,\dots,\log E_n)$ for independent $E_j\sim\mathrm{Exp}(1)$, so $\nu$ is a probability measure and $(\mathrm H1)$ holds. $\nabla\varphi(y)=(e^{y_j}-1)_j$, so $\mu$ is the law of $(E_j-1)_j$: a product of centered exponentials, which is log-concave with density $e^{-\sum_j(x_j+1)}$ on $(-1,\infty)^n$, has all moments finite, and is isotropic since $\E E_j=\Var E_j=1$; so $(\mathrm H2)$ holds. $H(y)=\diag(e^{y_j})$, $\E_\nu\norm H_{\HS}^2=\sum_j\E E_j^2=2n<\infty$; so $(\mathrm H3)$ holds. Here $\nabla\varphi$ is a diffeomorphism of $\R^n$ onto $(-1,\infty)^n$ and $\tau(x)=\diag(1+x_j)$ on that set. Using $\E E^k=k!$: $\E_\mu[X_j^3]=\E(E-1)^3=6-6+3-1=2$, and every $T_{ijk}$ with indices not all equal vanishes by independence and centering, so $T_{ijk}=2\delta_{ij}\delta_{jk}$, $T_3(a)=\diag(2a_j)$, and $\norm{T_3(a)}_{\HS}^2=4\abs a^2$: $\norm{T_3(a)}_{\HS}=2$ for every unit $a$. Also $\E_\mu[\tau^2]=\diag(\E(1+X_j)^2)=\diag(\E E_j^2)=2\Id$. Finally $\tau a=(a_j(1+X_j))_j=a+\diag(a_j)X=a+\tfrac12T_3(a)X$, so $v_a=0$ and [](#eq:sol-lstm-pythagoras) reads $2=1+1+0$. Thus this family attains the bound $2\sqrt{c-1}$ of [](#cor:sol-lstm-gate) with $c=2$ in every direction, and has no high-mode term.
:::

## 7\. The third-derivative form

:::{prf:proposition} Third derivatives
:label: prop:sol-lstm-third-derivative
Assume $(\mathrm H)$, $\varphi\in C^3(\R^n)$, and $\varphi_{ijk}\in L^1(\nu)$ for all $i,j,k$. Then $\E_\nu[\varphi_{ijk}]=\E_\nu[\varphi_{ij}\varphi_k]=\tfrac12\E_\mu[X_iX_jX_k]$.
:::

:::{prf:proof}
The vector field $W=\varphi_{ij}e^{-\varphi}e_k$ is $C^1$ since $\varphi\in C^3$, with $\Div W=(\varphi_{ijk}-\varphi_{ij}\varphi_k)e^{-\varphi}$. The divergence theorem on $B_R$ gives $\int_{B_R}\varphi_{ijk}\dd\nu-\int_{B_R}\varphi_{ij}\varphi_k\dd\nu=\int_{\partial B_R}\varphi_{ij}\mathbf n_ke^{-\varphi}\dd\sigma_R$, whose right side is bounded by $\int_{\partial B_R}\norm H_{\HS}e^{-\varphi}\dd\sigma_R$. Since $\int\norm H_{\HS}\dd\nu\le(\E_\nu\norm H_{\HS}^2)^{1/2}<\infty$, [](#lem:sol-lstm-shells) with $F_1=\norm H_{\HS}$ gives $R_k\to\infty$ along which the right side tends to $0$. Both integrands on the left are in $L^1(\nu)$ (the second by [](#lem:sol-lstm-N)), so dominated convergence gives $\E_\nu[\varphi_{ijk}]=\E_\nu[\varphi_{ij}\varphi_k]=N_{ijk}=\tfrac12T_{ijk}$.
:::

:::{prf:remark} Which hypothesis the manuscript's last sentence uses
:label: rem:sol-lstm-third-derivative-hypothesis
The last sentence of [](#lem:linear-sector-third-moment), “$\E_\nu[\partial_{ijk}\varphi]=\tfrac12\E_\mu[X_iX_jX_k]$”, presupposes that $\partial_{ijk}\varphi$ exists and is $\nu$-integrable, which the hypothesis $\varphi\in C^2$ does not provide. This dossier therefore proves it exactly under the additional hypothesis of [](#prop:sol-lstm-third-derivative), and proves *unconditionally* the statement that the manuscript's “gap-mode coefficient” actually uses, namely $\E_\nu[\varphi_{ij}\varphi_k]=\tfrac12\E_\mu[X_iX_jX_k]$ ([](#thm:sol-lstm-main)(a)): in the decomposition of [](#thm:sol-lstm-main)(b) the coefficient of $X_b$ in $(\tau a)_i$ is $\E_\mu[(\tau a)_iX_b]=\sum_ka_k\E_\nu[\varphi_{ik}\varphi_b]$, which involves only second derivatives of $\varphi$. The identification with the coefficient tensor of [](#lem:cmh-linear-spectral-resolution) is a matter of that lemma's definitions and is not asserted here; nothing in this dossier depends on that lemma. On the compact-target regular class the extra hypothesis is a separate claim (bounded $H$ does not by itself bound $D^3\varphi$) and is left to whichever dossier certifies that class.
:::

## 8\. Remarks

:::{prf:remark} Where each hypothesis is used
:label: rem:sol-lstm-hypotheses
Convexity and $C^2$ regularity of $\varphi$: the divergence-theorem computations ([](#prop:sol-lstm-stein)), the structure [](#lem:sol-lstm-structure) (convexity is what makes the fibres of $\nabla\varphi$ segments on which $H$ degenerates), and $\tau\succeq0$. Absolute continuity of $\mu$: only to make $\nabla\varphi$ injective off a $\nu$-null set ([](#lem:sol-lstm-structure)(ii)), i.e. to give [](#eq:stein-kernel-def) a meaning; a reader who prefers to define $\tau$ only where $\nabla\varphi$ is invertible needs nothing else. Finite third moment of $\mu$: absolute convergence of the left side of [](#eq:sol-lstm-stein) for quadratic $f$, and the definition of $T_3$. Isotropy: orthonormality of $\{\mathbf 1,X_b\}$ and $\E_\nu\abs{\nabla\varphi}^2=n$. $(\mathrm H3)$: $\tau_{ij}\in L^2(\mu)$, the domination of the interior integrands, and the shell function $\norm H_{\HS}$. Log-concavity of $\mu$ is used only through [](#lem:sol-lstm-logconcave), i.e. to supply absolute continuity and finite third moments; the theorem holds for any moment measure with those two properties. The essential uniqueness of the moment potential [@CorderoErausquinKlartag2015MomentMeasures] is not used in any proof; it is what identifies the $\varphi$ of the hypothesis with “the” potential of [](#conj:gate-zero) (any two differ by a translation, under which $\E_\nu[H^2]$ is invariant).
:::

:::{prf:remark} Symmetric laws and the compact-target class
:label: rem:sol-lstm-specialisations
If $\mu$ is symmetric ($X$ and $-X$ have the same law) then $T_3(\mu)=0$, so $\tau a=a+v_a$ and $\E_\mu\abs{\tau a}^2=\abs a^2+\E_\mu\abs{v_a}^2$: the whole of $a^\top\E_\mu[\tau^2]a-\abs a^2$ is the high-mode term. For a product of centered exponentials the opposite holds ([](#ex:sol-lstm-exponential)). For a member of the compact-target regular class of [](#thm:regular-moment-map-compact-target) which is isotropic and log-concave, $(\mathrm H)$ holds: $(\mathrm H1)$ and the diffeomorphism property are that theorem, $(\mathrm H2)$ follows from the density and the compact support, and $(\mathrm H3)$ follows from the pointwise bound $0\preceq D^2\varphi\preceq2R(P)^2\Id$ of [@Klartag2013MomentMeasures, Thm. 1.1] ($R(P)$ the radius of a Euclidean ball centred at the origin that contains $P$), as recorded in the manuscript after [](#lem:linear-sector-third-moment). This published bound is used only in this remark.
:::

:::{prf:remark} Source versus target coordinates in gate zero
:label: rem:sol-lstm-coordinates
[](#conj:gate-zero) is written with $\E[H^2]$, the source expectation $\E_\nu[(D^2\varphi)^2]$; [](#cor:gate-zero-third-moment) is written with $\E_\mu[\tau^2]$. [](#lem:sol-lstm-structure)(iv) shows the two matrices coincide under $(\mathrm H)$, so the conversion between the two conjectures' phrasing and the corollary's is exact and not merely up to a Jensen inequality.
:::

**Obstructions respected.** Neither node carries a `bounded_by` or `heuristic_barriers` entry. Of the ledger's six obstruction nodes: `rem:two-tail-slice-bounds`, `rem:projection-ceiling`, `rem:crude-insufficient` and `rem:single-coordinate-cuts` concern localization-route estimates and are not touched, since nothing here is a bound on a Poincaré or Cheeger constant; `rem:relative-ceiling` is respected because nothing here is a statement of KLS-equivalent strength (the theorem is an exact identity on a fixed measure, and the corollary is an implication whose antecedent is the open [](#conj:gate-zero)); `rem:profile-circularity` is respected because no isoperimetric profile is used. The CMH-route guardrail `prop:letwin-not-gate-zero` (the constant-matrix estimate does not imply gate zero) is respected: this dossier neither uses the constant-matrix estimate nor claims gate zero; it proves only that gate zero *implies* a directional third-moment bound. Program constraint P1 is respected: no member of the trace-upgrade cluster is opened, and no transfer between its members is asserted.
