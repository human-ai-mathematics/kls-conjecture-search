---
title: 'Solution: window occupation with $C_0=34$, $C_1=0$, and the Route-S reproduction of the polylog frontier'
label: sec:sol-prop-mm-window-occupation
ledger-node: prop:mm-window-occupation
numbering:
  enumerator: D22.%s
---

**Overview.** Conditional on the unreviewed preprint input [](#thm:letwin-qcts), this dossier proves for [](#prop:mm-window-occupation) that the occupation hypothesis of [](#q:mm-spectral-occupation) holds on the shrinking window $[0,T_0(n)]$, $T_0(n)=\min\{t_c,1/(\bar C\log^2n)\}$, with $C_0=34$, $C_1=0$ and no damping consumed, on the small-gap branch $\lambda\le3/(8K_n)$ ([](#thm:sol-prop-mm-window-occupation)). Rerunning the bridge argument at fixed $n$ then gives $\CP\le C\log^2n$ ([](#thm:sol-mwo-frontier)), which is weaker than the published $C_K\log n$ bound it uses as an input; the question itself stays open. The assembly also depends on three companion dossiers, [(I4)](#inp:stopped)–[(I6)](#inp:fourth).

1. The exit time $\tau=\tau_2$ of $\norm{A_t}_\op$ from level $2$ is an a.s. positive stopping time ([](#lem:sol-mwo-exit)), and the imported window bound [](#thm:KL-window) transfers to the planted realization ([](#lem:sol-mwo-law)).
2. Optional projection bounds $\E[v_\sigma^2\one_E]$ by $\E_\mu f^4$ ([](#lem:sol-mwo-optional-projection)); a tail integral bounds $\E[\tau^{-2}\one_{\{\tau\le T\}}]$ using step 1 ([](#lem:sol-mwo-tail)), which fixes the universal cap $t_c$ ([](#def:sol-mwo-tc)).
3. The source is split at $\tau$: the pre-exit part costs $32T$ by the stopped-window input, and the post-exit part costs $\sqrt2\,T$ by the restart input, Cauchy–Schwarz, step 2 and the small-gap bound $\E_\mu f^4\le2$. Together these give [](#eq:sol-mwo-occupation).
4. On regular approximants, the fixed-$n$ bridge ($q$-identity, terminal variance, posterior Brascamp–Lieb) with step 3 gives $\lambda\ge T_*(n)/2$ on the small-gap branch; the large-gap branch is immediate. This yields [](#eq:sol-mwo-approximant-bound).
5. The certified approximation passage at fixed dimension carries the bound to every isotropic log-concave law.

**Refined statement and standing.** Conditional on the imported, unreviewed preprint input [](#thm:letwin-qcts) [@Letwin2026QuadraticKLS, Thm. 1.2], this dossier proves that the occupation hypothesis of [](#q:mm-spectral-occupation) holds on the covariance window $[0,T_0(n)]$, $T_0(n)=\min\{t_c,1/(\bar C\log^2n)\}$, with constants $C_0=34$ and $C_1=0$ and *no damping consumed*, for every first eigenfunction on the small-gap branch $\lambda\le3/(8K_n)$; and that, combined with the certified bridge argument of `solutions/prop-spectral-sufficiency.md` rerun at fixed $n$ and the trivial large-gap branch, every isotropic log-concave probability on $\R^n$ ($n\ge2$) satisfies

$$
\CP\ \le\ C\log^2n,
\qquad\text{conditional on the preprint input},
$$

with $C$ universal; the conditional input is [](#thm:letwin-qcts).

**Scope fences (stated up front).** This dossier does *not* claim, and must not be read as claiming:

- **Not the gate.** [](#q:mm-spectral-occupation) demands universal constants $T_0,C_0,C_1$; here $T_0(n)\to0$ as $n\to\infty$. The question remains open and its status is unchanged by this dossier.

- **No universal-time statement and no beyond-window bound.** Nothing is asserted for $t>T_0(n)$. By the imported [](#prop:covariance-spike), the exit event $\{\tau_2\le t\}$ ceases to be rare past times of order $1/\log n$, so the rarity mechanism used here provably cannot be extended; this dossier does not attempt it.

- **No improvement of the published frontier.** The conclusion $\CP\le C\log^2n$ is strictly *weaker* than the published unconditional bound $\CP\le C_K\log n$ [@Klartag2023Logarithmic], which is itself an input here. The result is a *route-health certificate*: Route S, on certified repository lemmas, two published imports, and the Letwin preprint, reproduces a polylog frontier. It adds no new knowledge about $\CP$ itself.

- **Nothing about the trace-upgrade cluster.** No statement is made or implied about [](#q:upgrade), [](#q:stein-weighted), or `q:alignment` (repository constraint 6).

- **Conditional standing.** The occupation estimate and the frontier reproduction are conditional on the version-1, unreviewed preprint import [](#thm:letwin-qcts); by repository constraint 7 the corresponding node can be at most `conditional`.

**Setting.** Throughout, $\mu$ is a *regular isotropic approximant* on $\R^n$, $n\ge2$, in the class of Section [](#subsec:spectral-sde): $\dd\mu=Z^{-1}e^{-V}\dd x$ with $V\in C^\infty$, $\nabla^2V\succeq\varepsilon I_n$ for some $\varepsilon>0$, centered and isotropic, with Friedrichs generator $L=\Delta-\nabla V\cdot\nabla$ of compact resolvent, and $f$ a normalized first nonconstant eigenfunction, $-Lf=\lambda f$, $\E_\mu f=0$, $\E_\mu f^2=1$. The localization is realized by the planted channel $c_t=tX+B_t^{\mathrm{obs}}$ with $X\sim\mu$ and $B^{\mathrm{obs}}$ an independent Brownian motion; $(\mathcal F_t)$ is the usual augmentation of the observation filtration, and the pathwise posterior kernel $\mu_t$, the quantities $m_t,a_t,v_t,A_t,g_t,H_t$, and the zero-convention for $H_t$ are exactly as in the companion restart dossier ([](#thm:sol-lem-mm-restart-deweighting)). Write $S_t=\norm{H_t}_{\HS}^2$, $q(t)=\E\abs{g_t}^2$, $D_t=g_t^TA_tg_t\ge0$, and

$$
\tau_L=\inf\{t\ge0:\norm{A_t}_\op\ge L\},\qquad \tau:=\tau_2 .
$$

**Inputs and their exact standing.**

(inp:letwin)=
(I1) [](#thm:letwin-qcts) [@Letwin2026QuadraticKLS, Thm. 1.2]: $\Var(Y^TMY)\le8\norm M_{\HS}^2$ for isotropic log-concave $Y$ and symmetric $M$. *Imported, preprint-unreviewed; the conditional hypothesis of this dossier.*

(inp:window)=
(I2) [](#thm:KL-window) [@KLnotes, Thm. 61]: there is a universal $\bar C$ such that for every isotropic log-concave $\mu$ on $\R^n$ and every $t\le t_1(n):=1/(\bar C\log^2n)$, $\Prob(\exists s\le t:\norm{A_s}_\op\ge2)\le e^{-1/(\bar Ct)}$. *Imported, published.* Without loss of generality $\bar C\ge1$: enlarging $\bar C$ shrinks the window and weakens the bound, so the statement with any $\bar C$ implies the statement with $\max\{\bar C,1\}$.

(inp:klartag)=
(I3) `thm:klartag-logn` [@Klartag2023Logarithmic] (published import; ledger acceptance pending): every isotropic log-concave probability on $\R^n$, $n\ge2$, satisfies $\CP\le K_n:=C_K\log n$ with $C_K$ universal, via the Cheeger bound $\psi_n\le C\sqrt{\log n}$ and Cheeger's inequality. *Cited as an import; not proved here.*

(inp:stopped)=
(I4) Companion dossier `lem-mm-stopped-window-source.md` in `solutions/` ([](#thm:sol-lem-mm-stopped-window-source); conditional on [(I1)](#inp:letwin)): for every regular approximant, fixed unit-variance $f\in L^2(\mu)$, $L\ge1$, $T>0$: $\E\int_0^{T\wedge\tau_L}S_t\dd t\le8L^2T$.

(inp:restart)=
(I5) Companion dossier `lem-mm-restart-deweighting.md` in `solutions/` ([](#thm:sol-lem-mm-restart-deweighting); unconditional): for every a.s.\ positive stopping time $\sigma$, a.s. on $\{\sigma<\infty\}$, $\E[\int_\sigma^\infty S_t\dd t\mid\mathcal F_\sigma] \le\Var_{\mu_\sigma}(f)/(\varepsilon+\sigma)\le v_\sigma/\sigma$, together with the optional-time identification $\int\phi\dd\mu_\sigma=\E[\phi(X)\mid\mathcal F_\sigma]$ a.s. on $\{\sigma<\infty\}$ for every measurable $\phi\ge0$, and the deterministic solution map $\mathsf S_\mu$ of the observation equation with its pathwise uniqueness.

(inp:fourth)=
(I6) Companion dossier `lem-mm-smallgap-fourth-moment.md` in `solutions/` ([](#thm:sol-lem-mm-smallgap-fourth-moment); uses [(I3)](#inp:klartag)): if $\lambda\le3/(8K_n)$ then $\E_\mu f^4\le2$.

(inp:certified)=
(I7) Certified nodes: [](#lem:mm-time-weighted-fixed-source) (consumed inside [(I5)](#inp:restart)) and the certified bridge dossier for [](#prop:spectral-sufficiency), namely the file `prop-spectral-sufficiency.md` in `solutions/`, whose internal steps ($q$-identity, Bessel bound, terminal-variance identity, posterior Brascamp–Lieb, and the fixed-test approximation passage) are rerun here at fixed $n$; the certified theorem itself is *not* invoked as a black box, because its hypothesis requires dimension-free constants.

Inputs [(I4)](#inp:stopped)–[(I6)](#inp:fourth) are companion *candidate* dossiers with `checked_by: none`; any certification of the present dossier is contingent on their independent certification. This dossier's own contribution is the assembly: the exit-time bookkeeping, the optional projection step, the tail integral, the constant audit, and the fixed-$n$ rerun of the bridge.

## Preliminary lemmas

:::{prf:lemma} Path regularity of the exit time
:label: lem:sol-mwo-exit
Almost surely, $t\mapsto A_t$ is continuous. Consequently: (i) $\tau_L$ is an $(\mathcal F_t)$-stopping time for every $L\ge1$; (ii) $\tau=\tau_2>0$ everywhere on the continuity event, hence a.s.; (iii) for every $t\ge0$, $\{\tau\le t\}=\{\exists s\le t:\norm{A_s}_\op\ge2\}$ up to a null set, and $\norm{A_\tau}_\op\ge2$ on $\{\tau<\infty\}$; (iv) $\{\tau\le T\}\in\mathcal F_\tau$.
:::

:::{prf:proof}
On any compact time interval $\sup_{s\le U}\abs{c_s}<\infty$ pathwise, and the entries of $A_t$ are ratios of integrals of $(1+\abs x^2)e^{c_t\cdot x-t\abs x^2/2}$-type integrands against $\mu$; dominated convergence (domination by $(1+\abs x^2)e^{R\abs x}\in L^1(\mu)$, by strong log-concavity) gives continuity of $t\mapsto A_t$, hence of $t\mapsto\norm{A_t}_\op$. (i): by continuity, $\{\tau_L\le t\}=\{\sup_{s\in([0,t]\cap\mathbb Q)\cup\{t\}}\norm{A_s}_\op\ge L\} \in\mathcal F_t$. (ii): $A_0=\Cov(\mu)=I_n$ by isotropy, so $\norm{A_0}_\op=1<2$ and continuity forces $\tau>0$. (iii): if $\tau\le t$ then continuity gives $\norm{A_\tau}_\op\ge2$ at a time $\le t$; conversely if $\norm{A_s}_\op\ge2$ for some $s\le t$ then $\tau\le s\le t$. (iv): $\{\tau\le T\}\cap\{\tau\le t\} =\{\tau\le T\wedge t\}\in\mathcal F_{t}$ for every $t$, which is the definition of membership in $\mathcal F_\tau$.
:::

:::{prf:lemma} The imported window bound applies to the planted realization
:label: lem:sol-mwo-law
For the regular isotropic approximant $\mu$ and every $t\le t_1(n)$,

$$
\Prob(\tau\le t)\ \le\ e^{-1/(\bar Ct)} .
$$
:::

:::{prf:proof}
[](#thm:KL-window) is a statement about the law of $\sup_{s\le t}\norm{A_s}_\op$ for the stochastic localization of $\mu$ as defined in Section [](#subsec:sl-process): the tilt density [](#eq:sl-density) driven by the tilt process solving $\dd c_t=a_t\dd t+\dd W_t$ for a standard Brownian motion $W$, $c_0=0$. For the $\varepsilon$-strongly log-concave $\mu$, the drift $c\mapsto\mathsf a(\mu;t,c)$ of this equation is globally Lipschitz uniformly in $t$ (Brascamp–Lieb, constant $\varepsilon^{-1}$), so by the deterministic solution map of the companion restart dossier ([](#thm:sol-lem-mm-restart-deweighting), Step 6), *every* solution driven by *any* standard Brownian motion is the pathwise image $\mathsf S_\mu(W)$ of its driver; its law is therefore the fixed push-forward $\mathsf S_\mu\#\mathbb W$ of Wiener measure, the same for every realization. The planted channel realizes this equation with the innovation Brownian motion ([](#thm:sol-lem-mm-restart-deweighting), Steps 4 and 7(a), at $\sigma=0$), and the posterior kernel equals the tilt density [](#eq:sl-density) evaluated on the tilt path. Hence the law of $(A_s)_{s\ge0}$ — a fixed measurable functional of the tilt path — is identical in the two realizations, and the imported bound transfers verbatim. Combining with [](#lem:sol-mwo-exit)(iii) gives the display.
:::

:::{prf:lemma} Optional projection of the squared posterior variance
:label: lem:sol-mwo-optional-projection
Assume $\E_\mu f^4<\infty$. Then for every stopping time $\sigma$ and every $E\in\mathcal F_\sigma$ with $E\subseteq\{\sigma<\infty\}$,

$$
\E\bigl[v_\sigma^2\,\one_E\bigr]\ \le\ \E\bigl[f(X)^4\,\one_E\bigr]
\ \le\ \E_\mu f^4 .
$$
:::

:::{prf:proof}
By the optional-time identification of the companion restart dossier ([(I5)](#inp:restart), applied with the nonnegative integrable test functions $f^2$ and $f^4$), almost surely on $\{\sigma<\infty\}$,

$$
\int f^2\dd\mu_\sigma=\E\bigl[f^2(X)\mid\mathcal F_\sigma\bigr],
\qquad
\int f^4\dd\mu_\sigma=\E\bigl[f^4(X)\mid\mathcal F_\sigma\bigr].
$$

Pathwise, $0\le v_\sigma\le\int f^2\dd\mu_\sigma$, and by conditional Jensen ($Z=f^2(X)$),

$$
v_\sigma^2\le\Bigl(\E\bigl[f^2(X)\mid\mathcal F_\sigma\bigr]\Bigr)^2
\le\E\bigl[f^4(X)\mid\mathcal F_\sigma\bigr]
\quad\text{a.s.\ on }\{\sigma<\infty\}.
$$

Multiplying by $\one_E$ (which is $\mathcal F_\sigma$-measurable) and taking expectations, the tower property gives the first inequality; the second is trivial.
:::

:::{prf:lemma} Window tail integral
:label: lem:sol-mwo-tail
With $\bar C\ge1$ as in [(I2)](#inp:window), for every $T\le\min\{1,t_1(n)\}$,

$$
\E\bigl[\tau^{-2}\one_{\{\tau\le T\}}\bigr]
\ \le\ \bigl(T^{-2}+2\bar CT^{-1}+2\bar C^2\bigr)e^{-1/(\bar CT)}
\ \le\ 5\bar C^2\,T^{-2}e^{-1/(\bar CT)} .
$$
:::

:::{prf:proof}
Write $F(s)=\Prob(\tau\le s)$; by [](#lem:sol-mwo-law), $F(s)\le e^{-1/(\bar Cs)}$ for $0<s\le T\le t_1(n)$, and $\tau>0$ a.s. by [](#lem:sol-mwo-exit)(ii). For $0<\delta<\tau\le T$ one has the calculus identity $\tau^{-2}=T^{-2}+2\int_\tau^Ts^{-3}\dd s$, so by Tonelli's theorem

$$
\E\bigl[\tau^{-2}\one_{\{\delta<\tau\le T\}}\bigr]
=T^{-2}\,\Prob(\delta<\tau\le T)
+2\int_\delta^Ts^{-3}\,\Prob(\delta<\tau\le s)\dd s
\le T^{-2}F(T)+2\int_0^Ts^{-3}F(s)\dd s .
$$

Letting $\delta\downarrow0$ by monotone convergence bounds the left-hand side of the lemma by the right-hand side above. Substituting $u=1/s$,

$$
\int_0^Ts^{-3}e^{-1/(\bar Cs)}\dd s
=\int_{1/T}^\infty u\,e^{-u/\bar C}\dd u
=\Bigl(\frac{\bar C}{T}+\bar C^2\Bigr)e^{-1/(\bar CT)},
$$

using $\int_a^\infty ue^{-u/\bar C}\dd u=(a\bar C+\bar C^2)e^{-a/\bar C}$. Hence

$$
\E\bigl[\tau^{-2}\one_{\{\tau\le T\}}\bigr]
\le\Bigl(T^{-2}+\frac{2\bar C}T+2\bar C^2\Bigr)e^{-1/(\bar CT)} .
$$

Finally, for $T\le1$ and $\bar C\ge1$: $1+2\bar C+2\bar C^2\le5\bar C^2$, because $3\bar C^2-2\bar C-1=(3\bar C+1)(\bar C-1)\ge0$; so the bracket is at most $5\bar C^2T^{-2}$.
:::

:::{prf:definition} The universal window cap $t_c$
:label: def:sol-mwo-tc
Let $h(t)=\sqrt5\,\bar C\,t^{-2}e^{-1/(2\bar Ct)}$ for $t>0$. Then $h(t)\to0$ as $t\downarrow0$, and $\frac{\dd}{\dd t}\log h(t) =t^{-1}\bigl(\tfrac1{2\bar Ct}-2\bigr)>0$ for $t<1/(4\bar C)$, so $h$ is continuous and increasing on $(0,1/(4\bar C)]$. Define

$$
t_c\ :=\ \sup\bigl\{t\in(0,\tfrac1{4\bar C}]:\ h(t)\le1\bigr\}\ \in\ (0,1).
$$

By monotonicity and continuity, $h(t)\le1$ for every $t\in(0,t_c]$, and $t_c\le1/(4\bar C)<1$. The number $t_c$ depends only on the universal constant $\bar C$, hence is universal.
:::

## The window occupation estimate

:::{prf:theorem} Window occupation with $C_0=34$, $C_1=0$; conditional on [](#thm:letwin-qcts)
:label: thm:sol-prop-mm-window-occupation
Assume [](#thm:letwin-qcts). Set

$$
T_0(n)=\min\Bigl\{t_c,\ \frac1{\bar C\log^2n}\Bigr\} .
$$

Then for every regular isotropic approximant $\mu$ on $\R^n$ ($n\ge2$), every normalized first eigenfunction $f$ with $\lambda\le\dfrac3{8K_n}$, and every $T\le T_0(n)$,

```{math}
:label: eq:sol-mwo-occupation
\E\int_0^TS_t\dd t\ \le\ 34\,T .
```

In particular the occupation hypothesis [](#eq:spectral-occupation) of [](#q:mm-spectral-occupation) holds on $[0,T_0(n)]$ with

$$
C_0=34,\qquad C_1=0,
$$

and with no damping consumed: the nonnegative terms $C_1\int_0^Tq+2\E\int_0^TD_t\dd t$ are not needed on the right-hand side.
:::

:::{prf:proof}
Fix $T\le T_0(n)$. Since $f\in L^2(\mu)$ with $\Var_\mu(f)=\E_\mu f^2=1$ ($\E_\mu f=0$), input [(I4)](#inp:stopped) applies. Split the source at the exit time $\tau=\tau_2$ (a stopping time, a.s. positive, by [](#lem:sol-mwo-exit)): pathwise,

$$
\int_0^TS_t\dd t
=\int_0^{T\wedge\tau}S_t\dd t+\one_{\{\tau<T\}}\int_\tau^TS_t\dd t
\le\int_0^{T\wedge\tau}S_t\dd t+\one_{\{\tau\le T\}}\int_\tau^\infty S_t\dd t .
$$

*Pre-exit term.* By [(I4)](#inp:stopped) with $L=2$,

```{math}
:label: eq:sol-mwo-pre
\E\int_0^{T\wedge\tau}S_t\dd t\ \le\ 8\cdot2^2\cdot T=32\,T .
```

*Post-exit term.* Since $\{\tau\le T\}\in\mathcal F_\tau$ ([](#lem:sol-mwo-exit)(iv)) and $\{\tau\le T\}\subseteq\{\tau<\infty\}$, the tower property and input [(I5)](#inp:restart) at $\sigma=\tau$ give

```{math}
:label: eq:sol-mwo-post-1
\E\Bigl[\one_{\{\tau\le T\}}\int_\tau^\infty S_t\dd t\Bigr]
=\E\Bigl[\one_{\{\tau\le T\}}\,
\E\Bigl[\int_\tau^\infty S_t\dd t\Bigm|\mathcal F_\tau\Bigr]\Bigr]
\le\E\Bigl[\frac{v_\tau}{\tau}\,\one_{\{\tau\le T\}}\Bigr].
```

By Cauchy–Schwarz,

```{math}
:label: eq:sol-mwo-post-2
\E\Bigl[\frac{v_\tau}{\tau}\,\one_{\{\tau\le T\}}\Bigr]
\le\Bigl(\E\bigl[v_\tau^2\,\one_{\{\tau\le T\}}\bigr]\Bigr)^{1/2}
\Bigl(\E\bigl[\tau^{-2}\,\one_{\{\tau\le T\}}\bigr]\Bigr)^{1/2}.
```

On the small-gap branch $\lambda\le3/(8K_n)$, input [(I6)](#inp:fourth) gives $\E_\mu f^4\le2<\infty$, so [](#lem:sol-mwo-optional-projection) with $E=\{\tau\le T\}$ yields

```{math}
:label: eq:sol-mwo-post-3
\E\bigl[v_\tau^2\,\one_{\{\tau\le T\}}\bigr]\ \le\ \E_\mu f^4\ \le\ 2 .
```

Since $T\le T_0(n)\le\min\{1,t_1(n)\}$, [](#lem:sol-mwo-tail) applies, and combining [](#eq:sol-mwo-post-1)–[](#eq:sol-mwo-post-3),

$$
\E\Bigl[\one_{\{\tau\le T\}}\int_\tau^\infty S_t\dd t\Bigr]
\le\sqrt2\cdot\Bigl(5\bar C^2T^{-2}e^{-1/(\bar CT)}\Bigr)^{1/2}
=\sqrt2\cdot\sqrt5\,\bar C\,T^{-1}e^{-1/(2\bar CT)}
=\sqrt2\,T\cdot h(T),
$$

with $h$ as in [](#def:sol-mwo-tc). Since $T\le t_c$, $h(T)\le1$, so

```{math}
:label: eq:sol-mwo-post
\E\Bigl[\one_{\{\tau\le T\}}\int_\tau^\infty S_t\dd t\Bigr]\ \le\ \sqrt2\,T .
```

Adding [](#eq:sol-mwo-pre) and [](#eq:sol-mwo-post),

$$
\E\int_0^TS_t\dd t\ \le\ \bigl(32+\sqrt2\bigr)T\ \le\ 34\,T,
$$

which is [](#eq:sol-mwo-occupation). Since $q(t)\ge0$ and $D_t\ge0$, the form [](#eq:spectral-occupation) with $C_0=34$, $C_1=0$ follows a fortiori, with the entire damping budget untouched.
:::

## The fixed-$n$ bridge and the frontier reproduction

:::{prf:theorem} Route-S polylog reproduction; conditional on [](#thm:letwin-qcts)
:label: thm:sol-mwo-frontier
Assume [](#thm:letwin-qcts). There is a universal constant $C$ such that every isotropic log-concave probability measure $\nu$ on $\R^n$, $n\ge2$, satisfies

$$
\CP(\nu)\ \le\ C\log^2n .
$$
:::

:::{prf:proof}
Fix $n\ge2$ and set $M_*=1+34\,t_c$ and

$$
T_*(n)=\min\Bigl\{T_0(n),\ \frac1{2M_*}\Bigr\}
=\min\Bigl\{t_c,\ \frac1{\bar C\log^2n},\ \frac1{2M_*}\Bigr\}.
$$

*Step 1: the eigenvalue bound on regular isotropic approximants.* Let $\mu$ be any regular isotropic approximant on $\R^n$ with first eigenvalue $\lambda$.

*Large-gap branch.* If $\lambda>3/(8K_n)$ then directly

$$
\CP(\mu)=\frac1\lambda<\frac{8K_n}3=\frac{8C_K}3\log n .
$$

*Small-gap branch.* If $\lambda\le3/(8K_n)$, run the certified bridge argument of `prop-spectral-sufficiency.md` at this fixed $\mu$, with [](#thm:sol-prop-mm-window-occupation) in place of the universal occupation hypothesis. The certified dossier's $q$-identity for the regular class,

$$
q(t)=\abs{g_0}^2+\E\int_0^t\bigl(S_s-2D_s\bigr)\dd s,
$$

holds with all displayed integrals finite: $\E\int_0^tS\le34t$ by [](#thm:sol-prop-mm-window-occupation) for $t\le T_0(n)$, while the certified posterior covariance cap $(\varepsilon+s)A_s\preceq I$ and the terminal cap $(\varepsilon+s)\abs{g_s}^2\le v_s$ give the crude ($\varepsilon$-dependent, finiteness-only) bounds $q(s)\le\varepsilon^{-1}$ and $\E D_s\le\varepsilon^{-2}$. The certified Bessel bound gives $\abs{g_0}^2\le1$. Dropping the nonnegative damping and applying [](#thm:sol-prop-mm-window-occupation),

$$
q(t)\ \le\ 1+34\,t\ \le\ 1+34\,t_c=M_*,
\qquad 0\le t\le T_0(n)
$$

(no Grönwall step is needed since $C_1=0$). The certified terminal-variance identity $\E\Var_{\mu_t}(f)=1-\int_0^tq(s)\dd s$ then gives, at $t=T_*(n)\le T_0(n)$,

$$
\E\Var_{\mu_{T_*(n)}}(f)\ \ge\ 1-T_*(n)\,M_*\ \ge\ \frac12,
$$

while the certified posterior Brascamp–Lieb step (the posterior Hessian is $\succeq(\varepsilon+t)I\succeq tI$) with the fixed-test tower property bounds the same quantity above by $\lambda/T_*(n)$. Hence

$$
\lambda\ \ge\ \frac{T_*(n)}2 .
$$

*Both branches.* For $n\ge2$ one has $\log^2n\ge\log^22>0$, so each of the three terms in $T_*(n)$ is bounded below by a universal multiple of $1/\log^2n$:

$$
T_*(n)\ \ge\ \frac{c_1}{\log^2n},
\qquad
c_1:=\min\Bigl\{t_c\log^22,\ \frac{\log^22}{2M_*},\ \frac1{\bar C}\Bigr\},
$$

and on the large-gap branch $1/\lambda<\tfrac{8C_K}3\log n\le\bigl(\tfrac{8C_K}{3\log2}\bigr)\log^2n$. Therefore every regular isotropic approximant on $\R^n$ satisfies

```{math}
:label: eq:sol-mwo-approximant-bound
\CP(\mu)=\frac1\lambda\ \le\ C_2\,\log^2n,
\qquad
C_2:=\max\Bigl\{\frac{8C_K}{3\log2},\ \frac2{c_1}\Bigr\}\ \text{universal}.
```

*Step 2: passage to an arbitrary isotropic log-concave law at fixed $n$.* Let $\nu$ be isotropic log-concave on $\R^n$. The certified bridge dossier constructs regular isotropic approximants $\nu_j\to\nu$ in $W_2$, *in the same dimension $n$*, each lying in the regular class with compact resolvent and a first nonconstant eigenfunction, and shows that a Poincaré inequality holding for every $\nu_j$ with a constant independent of $j$ passes to $\nu$ on fixed locally Lipschitz test functions (value truncation, Lipschitz cutoffs, mollification, and lower semicontinuity; no eigenfunction convergence is used). By [](#eq:sol-mwo-approximant-bound) the constant $C_2\log^2n$ is independent of $j$ (the dimension $n$ is fixed along the approximation), so exactly that certified passage yields

$$
\Var_\nu(h)\le C_2\log^2n\int\abs{\nabla h}^2\dd\nu
$$

for every locally Lipschitz $h$, i.e. $\CP(\nu)\le C_2\log^2n$. Taking $C=C_2$ completes the proof.
:::

:::{prf:remark} Constant audit
:label: rem:sol-mwo-constants
The probe's proposed constants are confirmed by this audit: pre-exit budget $8L^2T=32T$ at $L=2$; post-exit budget $\sqrt2\cdot\sqrt{5}\,\bar C\,T^{-1}e^{-1/(2\bar CT)}\le\sqrt2\,T$ on $(0,t_c]$; total $32+\sqrt2\le34$; tail integral constant $5\max\{\bar C^2,1\}=5\bar C^2$ under the loss-free normalization $\bar C\ge1$, valid for $T\le\min\{1,t_1(n)\}$; $t_c$ as in [](#def:sol-mwo-tc) is well defined because $h$ is increasing on $(0,1/(4\bar C)]$ and vanishes at $0^+$. No constant required correction.
:::

:::{prf:remark} Where each dimension dependence enters
:label: rem:sol-mwo-dimension
Exactly two inputs carry the dimension: the window length $t_1(n)=1/(\bar C\log^2n)$ of the published import [(I2)](#inp:window), and the frontier constant $K_n=C_K\log n$ of the published import [(I3)](#inp:klartag) (which sets the branch point $3/(8K_n)$ and, through the small-gap branch, contributes only inside $T_*(n)$ via universal constants). All other constants ($8L^2$, $34$, $\sqrt2$, $M_*$, $t_c$) are universal and $\varepsilon$-free. The regularization $\varepsilon$ appears only in finiteness-only bounds and in the favorable denominator shift of the restart lemma; it enters no final constant, so the estimate is uniform through approximation as [](#q:mm-spectral-occupation) requires on its window.
:::

:::{prf:remark} Unclosed steps: none within scope; external standings restated
:label: rem:sol-mwo-gaps
Within its declared scope the argument has no unclosed analytic step. Its standing is nonetheless bounded by four external facts, restated for the reviewer: (i) conditionality on the unreviewed import [(I1)](#inp:letwin); (ii) dependence on the three companion dossiers [(I4)](#inp:stopped)–[(I6)](#inp:fourth), each certified since by its own review; (iii) the published import node `thm:klartag-logn`, accepted in the ledger since; (iv) the law identification of [](#lem:sol-mwo-law), which relies on the manuscript's definition of the localization by the tilt equation of Section [](#subsec:sl-process) — the same convention used by the certified dossiers — and on the pathwise solution map; a reviewer should confirm that the imported [@KLnotes, Thm. 61] indeed concerns that process, as the manuscript's Section [](#sec:covariance-tech) records.
:::

**Obstructions respected.** The candidate node carries no `bounded_by` edge; the registered fences were checked one by one. *`obs:two-tail`*: no cut, slice, or absolute-scale excess estimate occurs; the estimate is a stopped expectation bound plus a rare-event charge. *`obs:proj-ceiling`*: the only tensor input is the full symmetric-matrix Letwin bound, consumed inside the companion dossier with its conditional standing displayed; no projection test is promoted. *`obs:crude-insufficient`*: no crude covariance integral $\Xi_T$ and no logarithmic bootstrap appears; the window import is an exit-probability bound. *`obs:relative-ceiling`*: no all-measure relative occupation premise is inserted; the a priori input is the published frontier $K_n$, and the output is strictly weaker than that input. *`obs:circularity`*: no localized isoperimetric profile or moving competitor family occurs. *`obs:rank-one-refuted`*: no product-cut claim is made. *Covariance spike ([](#prop:covariance-spike))*: respected constructively — it is the stated reason the mechanism stops at the window edge and no beyond-window claim is made. *Recorded dead ends*: the marginal-probability independence step is avoided (the post-exit charge is a joint Cauchy–Schwarz through [](#lem:sol-mwo-optional-projection), not a product of marginals); no unstopped $\norm{A_t}_\op$ moment, no moving projector, and no rank-tail entrance loss occurs. *Constraint 6*: only `q:mm-spectral-occupation` is touched; no assertion crosses to the trace-upgrade cluster.
