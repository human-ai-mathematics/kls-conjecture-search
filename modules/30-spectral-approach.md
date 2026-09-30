---
numbering:
  enumerator: "30.%s"
---

(sec:spectral-approach)=
# Approach S: fixed-eigenfunction localization

## The approach at a glance

**The idea.** Follow a fixed first eigenfunction, rather than a cut, through stochastic localization, and keep its tensor orientation alive in the posterior covariance.

**How it would give KLS.** Through one implication, [](#prop:spectral-sufficiency), whose hypothesis is the occupation estimate [](#conj:mm-spectral-occupation):

$$
\text{fixed-eigenfunction full-damping occupation}
\ \Longrightarrow\
\text{KLS}.
$$

The implication is a theorem about a hypothesis: it brings [](#conj:kls) exactly as close as [](#conj:mm-spectral-occupation) does.

% Agent note: prop:spectral-sufficiency is proved with a non-empty `assumes` list, i.e.
% applicability-blocked in the ledger; its ledger node says so.

**What it uses.** From the literature, and load-bearing: the sharp quadratic/third-moment input $\kappa_n=O(1)$ ([](#thm:letwin-qcts)), taken from an *unreviewed version-1 preprint*; and the published polylogarithmic covariance window. Developed here: the exact fixed-function SDE and the posterior-defect calculus ([](#lem:mm-posterior-defect)).

**What it gives.** The initial-layer window chain, [](#prop:mm-window-occupation): conditional on the same preprint input, the occupation estimate *does* hold on the published polylogarithmic window. The approach therefore meets its difficulty only in the gap between a polylogarithmic time and a universal one, which is a sharper statement of the difficulty than the one it started from. The supporting chain is the time-weighted fixed source, the stopped window source, and restart de-weighting ([](#lem:mm-time-weighted-fixed-source), [](#lem:mm-stopped-window-source), [](#lem:mm-restart-deweighting)).

**What blocks it.** [](#conj:mm-spectral-occupation) at a *universal* time: the full-damping source estimate, uniformly on regular approximants, without losing tensor/covariance alignment under unwhitening. The whole difficulty is the word universal; the polylogarithmic window is the content of [](#prop:mm-window-occupation).

**What rules out the obvious variants.** No variant of this approach is known to fail, which reflects how little it has been explored rather than its strength. The binding constraint is external: [](#prop:covariance-spike) forbids the uniform operator-norm bound that a coarser version of this argument would want, which is precisely why the approach keeps the eigenfunction's tensor rather than the covariance's top eigenvalue.

**What would settle it.** [](#conj:mm-spectral-occupation) settles it through [](#prop:spectral-sufficiency); a family of measures on which the unwhitening step provably loses alignment would badly damage it. It also rests on a premise: if [](#thm:letwin-qcts) does not survive review, the approach does not become wrong, but its arithmetic reverts to $\CP\lesssim\log n$.

**Where to read.** Conceptual prelude: Section [](#sec:localization-prelude) — Approach S shares it entirely with Approach E and differs only in the object followed. Moment-map control it uses: Section [](#sec:family-moment-map). Apparatus: Appendices [](#sec:notation)–[](#sec:models).

**The idea, in more detail.** Follow a first eigenfunction — rather than a cut — through stochastic localization, and apply the moment-map quadratic control of Section [](#sec:family-moment-map) to its whitened posterior covariance tensor. The target is an absorptive, function-aware source/damping estimate over a universal amount of localization time.

This approach attacks the spectral object that *defines* KLS directly, and it retains the tensor/covariance orientation that a global operator-norm bound discards — the property Section [](#subsec:kls-spike-obstruction) showed to be necessary. It shares the localization backbone of Section [](#sec:localization-prelude) with Approach E and differs only in the object it tracks.

% Agent note: the approach is live, secondary. Its entry points are the approaches of
% research/program/portfolio.yaml; each approach's `objective` states what closing it delivers.

(subsec:spectral-sde)=
## Setup and the exact fixed-function SDE

Work first on smooth, strongly log-concave isotropic approximants, where the weighted Laplacian $L=\Delta-\nabla V\cdot\nabla$ has discrete spectrum. Let $f$ be a normalized first nonconstant eigenfunction, $-Lf=\lambda f$, and define along the localization of Section [](#subsec:sl-process)

```{math}
:label: eq:spectral-quantities
g_t=\Cov_{\mu_t}(f,X),
\qquad
H_t=\E_t\bigl[(f-\E_tf)(X-a_t)^{\otimes2}\bigr],
\qquad
A_t=\Cov_{\mu_t}(X).
```

Here $g_t\in\R^n$ is the covariance of $f$ with the coordinates, and $H_t$ is the symmetric-matrix-valued tensor coupling $f$ to the second-order posterior structure.

The exact evolution is

```{math}
:label: eq:spectral-sde
\dd g_t=H_t\dd W_t-A_tg_t\dd t .
```

So $\norm{H_t}_{\HS}^2$ is the *source* for $\abs{g_t}^2$ and $2g_t^TA_tg_t$ is its *exact damping*. This is the fixed-function analogue of the two-color Riccati identity of Section [](#sec:riccati): source and damping are separated exactly, with no inequality spent.

(subsec:spectral-whitened)=
## What the July 2026 input gives, and what it leaves

Conditional on the version-1 preprint of [](#thm:letwin-qcts), the eigenfunction tensor satisfies the optimal *intrinsic* static estimate in whitened coordinates,

```{math}
:label: eq:whitened-tensor
\norm{A_t^{-1/2}H_tA_t^{-1/2}}_{\HS}^2\le8\,\Var_{\mu_t}(f).
```

This is the exact analogue, for the fixed-eigenfunction object, of the static quadratic-chaos input that Section [](#sec:qcts) supplies for the fixed-cut object.

Crude unwhitening of [](#eq:whitened-tensor) — multiplying back by $A_t^{1/2}$ on both sides — leaves a factor $\lmax(A_t)^2$, and hence exactly the universal-time dynamic alignment problem that Section [](#subsec:sl-where-the-log-lives) identified as the residual cost. So this approach does not escape the difficulty by importing the preprint; it relocates it to an object with more structure.

:::{prf:remark} The extra structure a cut does not have
:label: rem:spectral-extra-structure
Unlike an indicator, the eigenfunction satisfies an equation, and that equation fixes two energies which the cut has no analogue of:

$$
\E\abs{\nabla f}^2=\lambda,
\qquad
\E\norm{\Hess f}_{\HS}^2\le\lambda^2 .
$$

Exploiting these fixed energies inside the posterior channel is the possible advantage of this approach over Approach E. It succeeds only if it controls the tensor's incidence in inflated covariance spaces, or consumes the exact damping in [](#eq:spectral-sde). Another global covariance-norm estimate is not enough, and by [](#prop:covariance-spike) could not be.
:::

:::{prf:lemma} Posterior eigenfunction-defect calculus
:label: lem:mm-posterior-defect
In the regular setting above, realize localization through the planted channel $c_t=tX+B_t^{\mathrm{obs}}$, where $X\sim\mu$ and $B^{\mathrm{obs}}$ is an independent Brownian motion, and put

$$
R_t(x)=(c_t-tx)\cdot\nabla f(x),
\qquad \rho_t=R_t-\E_tR_t,
\qquad m_t=\E_tf.
$$

Define

$$
b_t=\E_t\nabla f,
\quad C_t=\E_t[(X-a_t)\otimes\nabla f],
\quad u_t=\E_t[\rho_t(X-a_t)],
\quad K_t=\E_t[\rho_t(X-a_t)^{\otimes2}].
$$

Then, for every $t\ge0$,

```{math}
:label: eq:mm-posterior-defect-identities
\begin{aligned}
\E_tR_t&=\lambda m_t,
&\lambda g_t&=b_t+u_t,
&\lambda H_t&=2\operatorname{sym}C_t+K_t,
\end{aligned}
```

```{math}
:label: eq:mm-posterior-defect-budgets
\begin{aligned}
\E\Var_t(R_t)
&=t\lambda-\lambda^2\int_0^t\E\abs{g_s}^2\dd s,
&\E\int_0^t\norm{C_s}_{\HS}^2\dd s
&\le\lambda-\lambda^2\abs{g_0}^2,
\end{aligned}
```

```{math}
:label: eq:mm-posterior-defect-gradient
\begin{aligned}
\E\E_t\abs{\nabla R_t}^2
&\le t\lambda^2+t^2\lambda.
\end{aligned}
```

These identities do not by themselves unwhiten the high-covariance part of $H_t$.
:::

(subsec:spectral-headline)=
## The central problem

:::{prf:conjecture} Fixed-eigenfunction full-damping occupation
:label: conj:mm-spectral-occupation
On smooth strongly log-concave isotropic approximants, let $-Lf=\lambda f$ be a normalized first nonconstant eigenfunction and let $g_t,H_t,A_t$ be as in [](#eq:spectral-quantities). There exist universal constants $T_0,C_0,C_1>0$ such that, for every $t\le T_0$,

```{math}
:label: eq:spectral-occupation
\E\int_0^t\norm{H_s}_{\HS}^2\dd s
\le C_0t+C_1\E\int_0^t\abs{g_s}^2\dd s
+\E\int_0^t2g_s^TA_sg_s\dd s,
```

uniformly through approximation.
:::

:::{prf:proposition} Full-damping sufficiency bridge
:label: prop:spectral-sufficiency
Suppose [](#conj:mm-spectral-occupation) holds with constants $T_0,C_0,C_1>0$ uniformly through regularization. Set

$$
M_*=(1+C_0T_0)e^{C_1T_0},
\qquad
T_* = \min\left\{T_0,\frac1{2M_*}\right\}.
$$

Then every isotropic log-concave probability satisfies $\CP\le2/T_*$. In particular, the occupation estimate implies [](#conj:kls); no strict damping surplus is required.
:::

:::{prf:proof}
For a normalized first eigenfunction in the regular class, the fixed-function SDE [](#eq:spectral-sde) and Itô's formula give

$$
q(t)=\abs{g_0}^2+
\E\int_0^t\bigl(\norm{H_s}_{\HS}^2-2g_s^TA_sg_s\bigr)\dd s,
\qquad q(t)=\E\abs{g_t}^2.
$$

Bessel's inequality gives $\abs{g_0}^2\le1$. The full-damping occupation hypothesis cancels the entire last term and Grönwall yields $q(t)\le M_*$ on $[0,T_0]$. Since

$$
\E\Var_{\mu_t}(f)=1-\int_0^tq(s)\dd s,
$$

the left side is at least $1/2$ at $t=T_*$. Posterior Brascamp–Lieb and the fixed-test tower property bound it above by $T_*^{-1}\E\abs{\nabla f}^2=\lambda/T_*$, so the first eigenvalue satisfies $\lambda\ge T_*/2$. Smooth strongly convex approximants, whitening, and passage of the uniform Poincaré inequality on fixed smooth tests give the same bound for every isotropic log-concave law, without convergence of eigenfunctions. The full domain and approximation argument is in the full proof linked from the statement.
:::

The endpoint structure of [](#eq:spectral-occupation) is worth emphasizing. Here the source may be charged against the *full* exact damping. In the evolution of $\E|g_t|^2$ those two terms then cancel, leaving a closed Grönwall inequality from the linear budget and the lower-order term. A strict damping surplus would be useful but is not required for the KLS sufficiency bridge; this differs from the absorption margins required in the two-color setting of Approach E.

:::{prf:lemma} Time-weighted fixed-function source budget
:label: lem:mm-time-weighted-fixed-source
Let $\mu=e^{-V}\dd x$ be a smooth probability with $\Hess V\succeq\kappa I$, $\kappa\ge0$, and let $f$ be a fixed square-integrable test for which the posterior identities are justified. Put $g_t=\Cov_{\mu_t}(f,X)$, $H_t=\E_t[(f-\E_tf)(X-a_t)^{\otimes2}]$, and $A_t=\Cov_{\mu_t}(X)$. Then, for every $T>0$,

```{math}
:label: eq:mm-time-weighted-fixed-source
\begin{aligned}
&\E\int_0^T(\kappa+t)\norm{H_t}_{\HS}^2\dd t
+2\E\int_0^T\left(\abs{g_t}^2-(\kappa+t)g_t^TA_tg_t\right)\dd t \\
&\hspace{7em}\le \Var_\mu(f)-\kappa\abs{g_0}^2.
\end{aligned}
```

In particular, for $\kappa=0$, $\E\int_0^\infty t\norm{H_t}_{\HS}^2\dd t\le\Var_\mu(f)$. This estimate retains one power of time and by itself gives no unweighted initial-layer bound.
:::

(subsec:spectral-window-chain)=
## The initial-layer window chain

The following four statements assemble the initial layer of [](#conj:mm-spectral-occupation) completely up to the published covariance window. The first and last are conditional on the quadratic-Poincaré input [](#thm:letwin-qcts), taken from an unreviewed preprint; that conditionality is part of the statements.

% Agent note: isolated in the 2026-08-30 initial-layer probe.

:::{prf:lemma} Stopped initial-layer source bound; conditional on [](#thm:letwin-qcts)
:label: lem:mm-stopped-window-source
For every regular approximant, every fixed unit-variance test $f$, every $L\ge1$ and $T>0$, let $\tau_L=\inf\{t:\norm{A_t}_\op\ge L\}$. Then $\E\int_0^{T\wedge\tau_L}\norm{H_t}_{\HS}^2\dd t\le 8L^2T$, uniformly in the dimension and in the regularization.
:::

:::{prf:lemma} Restart deweighting at a stopping time
:label: lem:mm-restart-deweighting
For every almost surely positive stopping time $\sigma$ of the observation filtration on an $\eps$-regular approximant and every fixed $L^2$ test,

$$
\E\Bigl[\int_\sigma^\infty\norm{H_t}_{\HS}^2\dd t\ \Big|\ \F_\sigma\Bigr]
\ \le\ \frac{\Var_{\mu_\sigma}(f)}{\eps+\sigma}\ \le\ \frac{v_\sigma}{\sigma},
$$

by conditional application of [](#lem:mm-time-weighted-fixed-source) with $\kappa=\eps+\sigma$ after the strong-Markov restart of the planted localization channel.
:::

:::{prf:lemma} Small-gap fourth moment from the published frontier
:label: lem:mm-smallgap-fourth-moment
Let $K_n$ be the constant of [](#thm:klartag-logn), so that every isotropic log-concave law in dimension $n$ satisfies $\CP\le K_n$. Then every normalized first eigenfunction of a regular isotropic approximant with $\lambda\le 3/(8K_n)$ satisfies $\E f^4\le2$, via the eigen-identity $\lambda\,\E f^4=3\,\E f^2\abs{\nabla f}^2$ and the Poincaré inequality applied to $f^2$.
:::

:::{prf:proposition} Window occupation and frontier reproduction; conditional on [](#thm:letwin-qcts)
:label: prop:mm-window-occupation
With $T_0(n)=\min\bigl(t_c,\,1/(\bar C\log^2n)\bigr)$ from [](#thm:KL-window), the occupation hypothesis [](#eq:spectral-occupation) holds on $[0,T_0(n)]$ with $C_0=34$ and $C_1=0$ for every first eigenfunction with $\lambda\le3/(8K_n)$. Combined with the bridge argument of [](#prop:spectral-sufficiency) run at fixed $n$ and the trivial large-gap branch, every isotropic log-concave law on $\R^n$, $n\ge2$, satisfies $\CP\le C\log^2n$, conditional on [](#thm:letwin-qcts).
:::

[](#prop:mm-window-occupation) is a consistency check on the approach: it reproduces the polylogarithmic frontier through Approach S machinery without improving it, and it does not decide [](#conj:mm-spectral-occupation), whose remaining content is exactly the post-spike charge beyond the covariance window. The budgets above are exactly saturated by the profile $q(t)=\lambda/t^2$ ($t\ge\lambda$), so the small-gap branch admits no shortcut from those budgets alone.

% Agent note: the saturation profile was found in the 2026-08-30 initial-layer probe.

(subsec:spectral-kappa-form)=
## An equivalent sufficient reformulation

There is a second, coarser way to state what this approach needs. By [](#prop:letwin-kappa), $\kappa_n\le2\sqrt2$ conditional on the preprint. Hence *any* dimension-free comparison of the form

```{math}
:label: eq:spectral-kappa-sufficient
\CP(\mu)\le C\bigl(1+\kappa_n^2\bigr)
```

valid for every isotropic log-concave $\mu$ would prove KLS. Equivalently: it suffices to remove the residual $\sqrt{\log n}$ from the current spectral comparison [](#eq:kls-bridge) while retaining only a universal function of $\kappa_n$. Formulation [](#eq:spectral-kappa-sufficient) is useful as a target statement but supplies no mechanism; [](#conj:mm-spectral-occupation) is the mechanism-bearing form.

(subsec:spectral-h-minus-one)=
## The audited $H^{-1}$ endpoint

(subsec:spectral-hminus1-endpoint)=

A natural first lemma for this approach is an $H^{-1}$ residual bound. It is worth recording why it is not one: it is itself of KLS strength, although it looks like a preliminary step.

% Agent note: reclassified by the cycle-1 audit.

With $b=\int\nabla f\dd\mu$, the proposed target was

```{math}
:label: eq:spectral-residual
R(f)=\sum_i\norm{\partial_if-b_i}_{H^{-1}(\mu)}^2\le C\lambda .
```

It is still sufficient for KLS. But it is also quantitatively *implied* by KLS: one has the two-sided relation

```{math}
:label: eq:spectral-residual-two-sided
1+\abs b^2-\frac{2\abs b^2}\lambda\ \le\ R(f)\ \le\ 1-\frac{\abs b^2}\lambda .
```

Its exact heat representation controls the short-time and high-frequency parts at the desired scale; the long-time low-spectrum tail is the complete KLS-strength residue. Accordingly [](#eq:spectral-residual) is retained as a *calibrated endpoint and diagnostic*, not advertised as a likely preliminary lemma.

A second natural first attempt fails outright: a direct unweighting of the positive moment-map Stein form is *false* on truncated-exponential first eigenfunctions. This is why [](#eq:whitened-tensor) is stated in whitened form.

(subsec:spectral-barriers)=
## Which obstructions apply here, and comparison with the other approaches

The obstructions proved elsewhere in this document are scoped, and it matters which of them bind here.

- The projection ceiling of Section [](#sec:qcts) does *not* obstruct this approach: the moment map uses information beyond radial and projection tests.

- The single-coordinate product-budget result of Section [](#sec:product-stress) ([](#cor:single-coordinate-cuts)) is specific to a fixed-cut localization counterexample and imposes no no-go here.

- A universal Lipschitz Gaussian transport is too strong for exponential tails ([](#rem:no-lipschitz-transport)); the weaker expected-Jacobian criterion [](#eq:brownian-derivative) is sufficient for KLS but currently reuses KLS-scale input, so it ranks below the target of this section.

- Classical needles do not preserve the isotropic covariance constraints (Section [](#sec:family-needles)); that is a structural warning, not a theorem excluding all needle arguments.

:::{prf:remark} Relation to Approach C
:label: rem:spectral-vs-cmh
Approaches S and C both consume moment-map information and both must ultimately handle a test-dependent object rather than a constant matrix, which is the shared lesson of Section [](#subsec:mm-audit). They are nonetheless different programs: Approach S keeps stochastic localization and makes the test dependence dynamic, while Approach C (Section [](#sec:moment-map-cmh)) is deterministic and makes it geometric, through Haar fields on Schur fibers. Similarity of the residual loss is *not* evidence that the two target statements are equivalent, and no result merges them.
:::

% Promotion gate (agent note). The control plane promotes conj:mm-spectral-occupation, or admits
% further internal claims on this route, only when one of the following is established: the
% absorptive source/damping estimate eq:spectral-occupation uniformly on regular approximants
% together with a passage to arbitrary log-concave measures; or a route-fatal counterexample to
% every such function-aware occupation estimate.
