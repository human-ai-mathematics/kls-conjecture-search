---
numbering:
  enumerator: "2.%s"
---

(sec:family-sl)=
# Family 2: stochastic localization

**Object followed.** A measure-valued martingale $t\mapsto\mu_t$, together with its centroid $a_t$ and covariance $A_t$, along a Brownian filtration.

**What it buys.** Every general improvement of the KLS bound since 2012 has come from this construction. It replaces the needle dichotomy of Section [](#sec:family-needles) — “one dimension, no covariance” — by a process that keeps the ambient dimension and tracks covariance explicitly, at the price of controlling it only in law.

This section fixes the process and the three identities used by the two stochastic approaches of Part III, Approaches E and S. This manuscript's own two-color refinement of them is Section [](#sec:notation) onward; what follows is the scalar/matrix backbone as it appears in the literature.

(subsec:sl-process)=
## The process

In the Lee–Vempala form of Eldan's process [@LeeVempala2018; @LeeVempala2024], start from $p_0=p$ and define

```{math}
:label: eq:sl-density
p_t(x)=\frac{\exp\bigl(\inner{c_t}{x}-\frac t2|x|^2\bigr)\,p(x)}
{\int\exp\bigl(\inner{c_t}{y}-\frac t2|y|^2\bigr)\,p(y)\dd y},
```

where

$$
\dd c_t=\dd W_t+a_t\dd t,
\qquad
a_t=\E_{p_t}X,
\qquad
A_t=\Cov(p_t).
$$

Itô calculus gives the three identities that carry the whole method:

```{math}
:label: eq:sl-density-sde
\begin{aligned}
\dd p_t(x)&=p_t(x)\inner{x-a_t}{\dd W_t},
\end{aligned}
```

```{math}
:label: eq:sl-centroid-sde
\begin{aligned}
\dd a_t&=A_t\dd W_t,
\end{aligned}
```

```{math}
:label: eq:sl-covariance-sde
\begin{aligned}
\dd A_t&=\calT_t(\dd W_t)-A_t^2\dd t,
\end{aligned}
```

where the matrix-valued third-moment tensor is

```{math}
:label: eq:third-moment-tensor
\calT_t(u)=\E_{p_t}\bigl[(X-a_t)^{\otimes2}\inner{X-a_t}{u}\bigr].
```

Two features are decisive, and they pull in opposite directions:

(i) By [](#eq:sl-density-sde), $p_t(x)$ is a *measure-valued martingale*: $\E p_t(x)=p_0(x)$ for every $x$. Whatever is proved about $p_t$ can therefore be averaged back to time zero.

(ii) The factor $e^{-t|x|^2/2}$ in [](#eq:sl-density) makes $p_t$ *$t$-strongly log-concave*. Curvature is manufactured, at a known rate, out of nothing.

Feature (ii) creates the good event; feature (i) transports it back. The entire difficulty is that the drift $-A_t^2\dd t$ in [](#eq:sl-covariance-sde) that would keep $A_t$ small competes with the noise $\calT_t(\dd W_t)$, which is a third-moment quantity.

:::{prf:remark} Filtering interpretation
:label: rem:sl-filtering
The process is a nonlinear filter. The observation $c_t$ has the law of $tX+W_t$, and $p_t$ is exactly the posterior law of $X$ given that noisy observation up to time $t$. Localization is therefore “observe $X$ through Gaussian noise of decreasing variance $1/t$ and watch the posterior sharpen”. Under this reading $A_t$ is a conditional covariance, which is what makes [](#prop:covariance-spike) directly relevant: it is a statement about $\Cov(X\mid X+\sqrt sG)$.
:::

(subsec:sl-transfer)=
## How isoperimetry is transferred back

Fix a Borel set $E$ and let $g_t=p_t(E)$. By [](#eq:sl-density-sde), $g_t$ is a martingale with

```{math}
:label: eq:mass-martingale-sde
\dd g_t=\Bigl\langle\int_E(x-a_t)\,p_t(x)\dd x,\ \dd W_t\Bigr\rangle,
```

whose quadratic variation is controlled by $A_t$. Lee–Vempala's criterion is the clean statement of the transfer [@LeeVempala2018]:

```{math}
:label: eq:lv-criterion
\Prob\Bigl\{\int_0^T\norm{A_s}_\op\dd s\le\tfrac1{64}\Bigr\}\ge\tfrac34
\qquad\Longrightarrow\qquad
\PsiKLS_{p_0}\lesssim T^{-1/2}.
```

The mechanism has three steps, and it is worth separating them because Approaches E and S modify exactly one of them each:

(1) the covariance bound keeps $g_T$ away from $0$ and $1$ with positive probability — the cut is not identified too fast;

(2) $p_T$ is $T$-strongly log-concave, hence $h(p_T)\gtrsim\sqrt T$ by Bakry–Émery;

(3) averaging the boundary measure of $E$ under $p_T$ back to time zero, using the martingale property, transfers that expansion to $p_0$.

So KLS becomes a question about the covariance process — and specifically about its largest eigenvalue, which is where [](#eq:lv-criterion) charges its cost. Approach E replaces step (1) by a two-color estimate for one fixed $E$ (Section [](#sec:mass-martingale)); Approach S replaces the set $E$ by a first eigenfunction (Section [](#sec:spectral-approach)).

(subsec:sl-third-moments)=
## Why third moments appear

Take the basic Schatten-2 potential $\Phi_t=\Tr(A_t^2)$. Itô's formula applied to [](#eq:sl-covariance-sde) gives

```{math}
:label: eq:trace-potential-ito
\dd\Phi_t
=\dd M_t
-2\Tr(A_t^3)\dd t
+\E_{X,Y\sim p_t}\inner{X-a_t}{Y-a_t}^3\dd t ,
```

with $M_t$ a martingale. The term $-2\Tr(A_t^3)$ is the stabilizing drift inherited from $-A_t^2$. The positive Itô correction is exactly the squared Hilbert–Schmidt norm of the third-moment tensor: writing $a=a_t$,

```{math}
:label: eq:third-moment-identity
\E_{X,Y\sim p_t}\inner{X-a}{Y-a}^3
=\sum_{i,j,k}\Bigl(\E\bigl[(X-a)_i(X-a)_j(X-a)_k\bigr]\Bigr)^2 .
```

Controlling this noise term *while retaining information about $\lmax(A_t)$* is the central stochastic-localization calculation, and it is why a sharp bound on the third-moment tensor — the parameter $\kappa_n$ of [](#eq:kappa-def) — is the crucial input rather than an incidental one.

(subsec:sl-evolution)=
## Evolution of the method

| Paper | Main technical device | Result for $\PsiKLS_n$ |
|---|---|---|
| Eldan [@Eldan2013ThinShell] | Covariance-normalized localization $C_t=A_t^{-1}$, high Schatten powers, relation to thin shell | $n^{1/3}\sqrt{\log n}$ with then-known thin-shell bounds |
| Lee–Vempala [@LeeVempala2018; @LeeVempala2024] | Fixed Gaussian tilt and the $\Tr(A_t^2)$ stopping argument | $n^{1/4}$ |
| Chen [@Chen2021] | Iterated high-Schatten potentials, affine preconditioning, induction on dimension | $\exp(C\sqrt{\log n\log\log n})$ |
| Klartag–Lehec [@KlartagLehec2022Polylog] | Heat-flow duality, spectral projections, $H^{-1}$, covariance growth | $(\log n)^5$ |
| Jambulapati–Lee–Vempala [@JambulapatiLeeVempala2022KLS] | Two localization representations and spiked-spectrum estimates | $(\log n)^{3.2226}$ |
| Klartag [@Klartag2023Logarithmic] | Improved Lichnerowicz plus short-time covariance control | $\sqrt{\log n}$ (published record) |
| Letwin, v1 [@Letwin2026QuadraticKLS] | Sharp quadratic Poincaré $\Rightarrow\kappa_n=O(1)$, inserted into Klartag's bridge | $(\log n)^{1/4}$ (preprint record) |

(subsec:sl-where-the-log-lives)=
## Where the surviving logarithm lives

This subsection makes precise the claim of Section [](#subsec:kls-architecture), because it is what target 3 of the synthesis acts on.

To use [](#eq:lv-criterion) one needs a potential that both dominates $\lmax(A_t)$ and admits an Itô calculus. Klartag–Lehec use log-trace-exp,

```{math}
:label: eq:logtraceexp
\Phi_t=\frac1\beta\log\Tr\bigl(e^{\beta A_t}\bigr),
\qquad
\norm{A_t}_\op\le\Phi_t\le\norm{A_t}_\op+\frac{\log n}\beta .
```

The two-sided bound in [](#eq:logtraceexp) is the whole story. Approximating $\lmax$ to within a constant requires $\beta\asymp\log n$. The Itô drift generated by the noise [](#eq:third-moment-tensor) then has size $O(\kappa_n^2\log n)$, so covariance control survives only up to

```{math}
:label: eq:tstar
t_*\asymp\frac1{\kappa_n^2\log n} .
```

Improved Lichnerowicz ([](#thm:improved-lichnerowicz)) converts a curvature time into a Poincaré constant,

$$
\CP(\mu)\lesssim t_*^{-1/2}\lesssim\kappa_n\sqrt{\log n},
$$

which is the bridge [](#eq:kls-bridge).

:::{prf:remark} The logarithm is an entropy cost, not a moment cost
:label: rem:log-is-entropy
The $\log n$ in [](#eq:logtraceexp) is the entropy of the uniform distribution on $n$ directions: it is what one pays to replace a maximum over $n$ eigenvalues by a smooth surrogate, and it would be present even if $\kappa_n$ were known exactly and equal to $1$. Since $\kappa_n=O(1)$ is now available ([](#prop:letwin-kappa)), this term is the *entire* remaining gap between the preprint record and the conjecture. A potential that depends only on the directions actually relevant to a near-extremizer, or on an effective rank rather than the ambient dimension $n$, would convert $\kappa_n=O(1)$ into $\CP=O(1)$.
:::

**The precise missing estimate.** Control of $\lmax(A_t)$ along the whole path at a universal time, without paying the $\log n$ of [](#eq:logtraceexp).

**Why it stalls.** By [](#prop:covariance-spike), the naive strengthening — a uniform pathwise bound on $\norm{A_t}_\op$ — is false, even for measures that satisfy KLS. So the missing estimate cannot be obtained by sharpening the covariance bound; it has to come from a potential that recognizes when a covariance spike is harmless. Products of centered exponentials are the canonical instance of a harmless spike, which is why they recur as the stress test throughout Part III (Sections [](#sec:models) and [](#sec:product-stress)).

**Where this family enters the four approaches.** It is the engine of both approaches of Part III, which differ only in what they refuse to average away. Approach E (Section [](#sec:introduction)) keeps one fixed cut and its two-colour covariance; Approach S (Section [](#sec:spectral-approach)) keeps one fixed eigenfunction and its covariance tensor. The conceptual summary they share is Section [](#sec:localization-prelude), and the apparatus is in the appendices.
