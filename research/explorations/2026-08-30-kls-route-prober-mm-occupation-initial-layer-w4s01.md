---
type: exploration
date: "2026-08-30"
approach: ap:spectral-window-chain
outcome: proposed
nodes:
  - q:mm-spectral-occupation
---
# Route-S probe: the initial layer closes up to the covariance window; the residue is one post-spike charge

Date: 2026-08-30

Role: `kls-route-prober`

Run id: `w4s01`

Concurrency key: `kls-gate:q:mm-spectral-occupation`

Status: the gate is not closed at universal time. This probe assembles, from certified and
imported repository inputs only, a complete prover-ready argument for the occupation estimate on
the polylog covariance window $[0,\,c/\log^2 n]$, reproducing a Letwin-conditional
$C_P=O(\log^2 n)$ through Route S. It then proves that the certified scalar budgets are exactly
saturated by an explicit enemy profile, so the small-gap branch admits no shortcut, and isolates
the entire remaining gate in a single post-spike source charge. No numerics are used or
requested.

## The gate, verbatim

From `research/kls/gating.md`:

> Prove the universal-time full-damping source estimate uniformly on regular approximants,
> preserving tensor orientation under unwhitening. The source may consume the entire exact
> damping; a strict damping surplus is not required for the KLS bridge.

Manuscript form (`q:mm-spectral-occupation`, `modules/kls/30-spectral-route.tex`): on smooth
strongly log-concave centered isotropic regular approximants with normalized first eigenfunction
$-Lf=\lambda f$, $\mathbb E_\mu f=0$, $\mathbb E_\mu f^2=1$, and localization quantities
$$
 g_t=\operatorname{Cov}_{\mu_t}(f,X),\qquad
 H_t=\mathbb E_t[(f-\mathbb E_tf)(X-a_t)^{\otimes2}],\qquad
 A_t=\operatorname{Cov}_{\mu_t}(X),
$$
find universal $T_0,C_0,C_1>0$ with, for every $t\le T_0$,
$$
 \mathbb E\int_0^t\|H_s\|_{\mathrm{HS}}^2\,ds
 \le C_0t+C_1\,\mathbb E\int_0^t|g_s|^2\,ds
 +2\,\mathbb E\int_0^t g_s^TA_sg_s\,ds,
 \tag{G}
$$
uniformly through approximation. Write $S_t=\|H_t\|_{\mathrm{HS}}^2$, $q(t)=\mathbb E|g_t|^2$,
$D_t=g_t^TA_tg_t$, $v_t=\operatorname{Var}_{\mu_t}(f)$,
$\widehat H_t=A_t^{-1/2}H_tA_t^{-1/2}$.

## Inputs and their exact standing

1. `prop:spectral-sufficiency` — certified conditional bridge (`solutions/prop-spectral-sufficiency.tex`):
   (G) with coefficient one on the damping gives $C_P\le2/T_*$,
   $M_*=(1+C_0T_0)e^{C_1T_0}$, $T_*=\min\{T_0,1/(2M_*)\}$, via
   $q(t)\le M_*$, $\mathbb E\operatorname{Var}_{\mu_t}(f)=1-\int_0^tq$, and posterior
   Brascamp--Lieb $\mathbb E\operatorname{Var}_{\mu_t}(f)\le\lambda/t$.
2. `lem:mm-time-weighted-fixed-source` — certified, **all fixed $L^2$ tests**, every smooth
   $\kappa$-uniformly log-concave law:
   $\mathbb E\int_0^T(\kappa+t)\|H_t\|^2dt+2\mathbb E\int_0^T(|g_t|^2-(\kappa+t)D_t)dt
   \le\operatorname{Var}_\mu(f)-\kappa|g_0|^2$.
3. `lem:mm-posterior-defect` — certified: $\lambda g_t=b_t+u_t$,
   $\lambda H_t=2\operatorname{sym}C_t+K_t$,
   $\mathbb E\int_0^t\|C_s\|^2ds\le\lambda-\lambda^2|g_0|^2$,
   $\mathbb E\operatorname{Var}_t(R_t)=t\lambda-\lambda^2\int_0^tq$,
   $\mathbb E\mathbb E_t|\nabla R_t|^2\le t\lambda^2+t^2\lambda$.
4. `thm:letwin-qcts` — imported, **preprint-unreviewed**: $\operatorname{Var}(X^TMX)\le8\|M\|_{\mathrm{HS}}^2$
   for isotropic log-concave $X$. Applied to the whitened posterior it gives the pathwise
   duality bound $\|\widehat H_t\|_{\mathrm{HS}}^2\le8v_t$ for **every** fixed test, and likewise
   $\|A_t^{-1/2}K_tA_t^{-1/2}\|^2\le8\operatorname{Var}_t(R_t)$.
5. `thm:KL-window` — imported, **published**:
   $\mathbb P(\exists s\le t:\|A_s\|_{\mathrm{op}}\ge2)\le e^{-1/(\bar Ct)}$ for
   $t\le t_1(n):=1/(\bar C\log^2n)$.
6. `Klartag2023Logarithmic` — published, in `fi_references.bib` but **not yet a ledger node**:
   every isotropic log-concave law on $\mathbb R^n$ ($n\ge2$) satisfies $C_P\le K_n:=C_K\log n$
   (Cheeger constant $\gtrsim1/\sqrt{\log n}$ plus Cheeger's inequality).
7. Proved structural equivalence (w1s03 exploration): at the full-damping endpoint, (G) is
   equivalent, up to the Letwin-conditional low block $8L^2$, to the local growth bound
   $q(T)-|g_0|^2\le a_0T+a_1\int_0^Tq$.
8. No-go inputs respected, not rerun: the scalar-multiplier weight-removal no-go
   (upgrade-par-01: any argument from the martingale calculus plus $A_t\preceq t^{-1}I$ forces
   weight $\le Ct^2$ at zero), the moving-projector error ledger, the marginal-probability
   independence fallacy, the rank-entrance Cauchy--Schwarz $(\log n)^8$ loss, and the
   one-sided-projector $\alpha\ge2$ coefficient failure (all in w1s03/par-02);
   `prop:covariance-spike` (published import): exponential products have
   $\|A_t\|_{\mathrm{op}}\gtrsim1/t$ with universal probability once $t\gtrsim1/\log n$.

The node `q:mm-spectral-occupation` carries no formal `bounded_by` edge; the full obstruction
registry is checked below anyway.

## Term-by-term decomposition of (G)

- **Source $S_t$.** Quadratic-variation density of $g$. In the covariance eigenbasis
  $S_t=\sum_{ij}a_i(t)a_j(t)(\widehat H_t)_{ij}^2$: two covariance weights on an intrinsic
  tensor whose total unweighted energy is $\le8v_t$ (input 4, conditional).
- **Exact damping $2D_t$, coefficient one.** No surplus is available and none is required.
- **Linear budget $C_0t$.** Must be uniform in the regularization; the cap
  $A_t\preceq(\varepsilon+t)^{-1}I$ is inadmissible at $t=0$ (its use diverges as
  $\varepsilon\downarrow0$; recorded in par-02).
- **Grönwall budget $C_1\int q$.** May absorb lower-order terms only.
- **Boundary.** $|g_0|^2\le1$ (Bessel; certified in the bridge dossier).
- **Uniformity.** All constants free of $n$, the approximant, and $\varepsilon$. This is where
  every prior attempt died: the certified time-weighted lemma controls $\int tS_t$ only, and the
  weight cannot be removed at zero by the recorded scalar methods.

The controlled/uncontrolled ledger before this probe: low-covariance block controlled
(Letwin-conditional, $8L^2v_t$); time-weighted total controlled (certified); high-incidence
unweighted initial layer uncontrolled; equivalently local growth of $q$ uncontrolled.

## Established, part I: the window chain

All statements below are for a regular approximant ($V\in C^\infty$,
$\nabla^2V\succeq\varepsilon I$, centered isotropic) under the planted channel
$c_t=tX+B_t^{\mathrm{obs}}$. Constants never depend on $n$, $\varepsilon$, or the test except
where displayed. Fix $L\ge1$ and the exit time
$$
 \tau_L=\inf\{t\ge0:\|A_t\|_{\mathrm{op}}\ge L\},\qquad \tau:=\tau_2 .
$$

### Lemma A (stopped initial-layer source bound; conditional on `thm:letwin-qcts`)

For every fixed test $f\in L^2(\mu)$ with $\operatorname{Var}_\mu(f)=1$ and every $T>0$,
$$
 \mathbb E\int_0^{T\wedge\tau_L}\|H_t\|_{\mathrm{HS}}^2\,dt\ \le\ 8L^2\,T .
$$

*Proof.* $\mu_t$ is log-concave with $A_t\succ0$; whitening $Y=A_t^{-1/2}(X-a_t)$ is isotropic
log-concave, and for symmetric $M$ with $\|M\|_{\mathrm{HS}}=1$,
$\langle M,\widehat H_t\rangle=\operatorname{Cov}_{\mu_t}(f,Y^TMY)
\le v_t^{1/2}\operatorname{Var}_{\mu_t}(Y^TMY)^{1/2}\le\sqrt{8v_t}$ by input 4 applied to
$\mu_t$ pathwise. Hence $\|\widehat H_t\|_{\mathrm{HS}}^2\le8v_t$ a.s. On $\{t<\tau_L\}$,
$\|H_t\|_{\mathrm{HS}}\le\|A_t\|_{\mathrm{op}}\|\widehat H_t\|_{\mathrm{HS}}\le L\|\widehat H_t\|_{\mathrm{HS}}$,
so $\|H_t\|^2\mathbf 1_{t<\tau_L}\le8L^2v_t$. Since
$\mathbb Ev_t=1-\int_0^tq\le1$, integrate. $\square$

This is the correlation-free replacement for the fenced product
$\mathbb E[v_t\|A_t\|_{\mathrm{op}}^2]$: before $\tau_L$ the operator norm is deterministic and
no independence step occurs. It is dimension-free and $\varepsilon$-free, and it is exactly the
place where `prop:covariance-spike` will later forbid extension: beyond $t\asymp1/\log n$ the
event $\{\tau\le t\}$ is no longer rare.

### Lemma B (restart deweighting at a stopping time; unconditional)

Let $\sigma$ be an a.s. strictly positive stopping time of the observation filtration. Then,
almost surely on $\{\sigma<\infty\}$,
$$
 \mathbb E\Bigl[\int_\sigma^\infty\|H_t\|_{\mathrm{HS}}^2\,dt\ \Big|\ \mathcal F_\sigma\Bigr]
 \ \le\ \frac{v_\sigma}{\varepsilon+\sigma}\ \le\ \frac{v_\sigma}{\sigma}.
$$

*Proof sketch (prover-formalizable).* The posterior density gives, for $u\ge0$,
$\mu_{\sigma+u}\propto\exp\bigl((c_{\sigma+u}-c_\sigma)\cdot x-\tfrac u2|x|^2\bigr)\,d\mu_\sigma$,
so conditionally on $\mathcal F_\sigma$ the process $(\mu_{\sigma+u})_{u\ge0}$ is the stochastic
localization of the fixed (given $\mathcal F_\sigma$) measure $\mu_\sigma$, driven by the
post-$\sigma$ innovation increments, which by the strong Markov property of the innovation
Brownian motion form a Brownian motion independent of $\mathcal F_\sigma$; weak uniqueness of the
localization SDE identifies the conditional law with the planted realization for the prior
$\mu_\sigma$. The potential of $\mu_\sigma$ has Hessian $\succeq(\varepsilon+\sigma)I$, and
$f\in L^2(\mu_\sigma)$ a.s. Apply the certified `lem:mm-time-weighted-fixed-source` with
$\kappa=\varepsilon+\sigma$ conditionally: since the restarted weight satisfies
$\kappa+u\ge\varepsilon+\sigma$,
$$
 (\varepsilon+\sigma)\,
 \mathbb E\Bigl[\int_0^\infty\|H_{\sigma+u}\|^2du\,\Big|\,\mathcal F_\sigma\Bigr]
 \le\operatorname{Var}_{\mu_\sigma}(f)-(\varepsilon+\sigma)|g_\sigma|^2\le v_\sigma. \square
$$

Flagged technical steps for the dossier: (i) conditional application of a fixed-measure lemma at
a random measure via regular conditional distributions; (ii) optional-time identification
$\mu_\sigma=\mathcal L(X\mid\mathcal F_\sigma)$ (continuous paths, standard filtering); (iii)
weak uniqueness / strong Markov of the measure-valued SDE. All are standard; none needs a new
estimate. Note the contrast with the recorded dead end: w1s03 correctly observed that
optional sampling controls $\mathbb Ev_{\sigma}$ but not $\mathbb E[v_\sigma/\sigma]$; Lemmas C
and D below supply exactly the missing joint control **inside the window**, where the exit
probability is superexponentially small — they claim nothing at universal time.

### Lemma C (optional projection of the posterior variance; unconditional)

For a stopping time $\sigma$ and $E\in\mathcal F_\sigma$:
$\mathbb E[v_\sigma\mathbf 1_E]\le\mathbb E[f(X)^2\mathbf 1_E]$ and
$\mathbb E[v_\sigma^2\mathbf 1_E]\le\mathbb E[f(X)^4\mathbf 1_E]$.

*Proof.* $v_\sigma\le\mathbb E_\sigma f^2=\mathbb E[f(X)^2\mid\mathcal F_\sigma]$ and
$v_\sigma^2\le(\mathbb E_\sigma f^2)^2\le\mathbb E_\sigma f^4$ (conditional Jensen); take
expectations against $\mathbf 1_E$. $\square$

So the "posterior variance on a rare covariance event" is exactly "eigenfunction mass on a rare
event of the base measure" — a uniform-integrability question about $f$ alone.

### Lemma D (small-gap fourth moment from the published frontier; unconditional)

Let $K$ be any valid uniform Poincaré bound for isotropic log-concave laws in dimension $n$
(published: $K=K_n=C_K\log n$, `Klartag2023Logarithmic`). If $-Lf=\lambda f$ is a normalized
first eigenfunction of a regular isotropic approximant and $\lambda\le\dfrac3{8K}$, then
$\mathbb E_\mu f^4\le2$.

*Proof.* On the regular approximant $f\in L^4$ qualitatively ($\varepsilon$-dependent, used only
for finiteness). Integration by parts with the eigenequation gives
$\lambda\,\mathbb Ef^4=\mathbb E[f^3(-Lf)]=3\,\mathbb E[f^2|\nabla f|^2]$. Poincaré for the
locally Lipschitz function $f^2$ with constant $K$:
$$
 \mathbb Ef^4-1=\operatorname{Var}(f^2)\le K\,\mathbb E|\nabla f^2|^2
 =4K\,\mathbb E[f^2|\nabla f|^2]=\tfrac{4K\lambda}3\,\mathbb Ef^4\le\tfrac12\,\mathbb Ef^4 .
 \square
$$

Two remarks. (i) With $K=1/\lambda$ (the trivial choice for a first eigenfunction) the
coefficient is $4/3>1$ and the bootstrap fails for **every** $L^p$, $p>2$; the published external
frontier bound is what makes it close, and only on the small-gap branch. This is not circular:
the pipeline's output below is $O(\log^2n)$, strictly weaker than its input $O(\log n)$. (ii)
The large-gap branch $\lambda>3/(8K_n)$ needs no occupation estimate at all — those measures
already satisfy the target conclusion at the frontier scale.

### Theorem E (window occupation and frontier reproduction; conditional on `thm:letwin-qcts`)

There are universal constants $t_c\in(0,1)$ and $n_0$ with the following property. Let
$T_0(n)=\min\{t_c,\,t_1(n)\}$, $t_1(n)=1/(\bar C\log^2n)$ from `thm:KL-window`. Then for every
regular isotropic approximant in dimension $n$ and every normalized first eigenfunction with
$\lambda\le3/(8K_n)$, the occupation estimate (G) holds on $[0,T_0(n)]$ with
$$
 C_0=34,\qquad C_1=0,
$$
with **no damping consumed**. Consequently, rerunning the certified bridge argument of
`solutions/prop-spectral-sufficiency.tex` at fixed $n$ and splitting each approximant on
$\lambda\lessgtr3/(8K_n)$, every isotropic log-concave law on $\mathbb R^n$ satisfies,
conditional on `thm:letwin-qcts`,
$$
 C_P\ \le\ C\log^2n .
$$

*Proof.* Fix $T\le T_0(n)$. Split at $\tau=\tau_2$:
$$
 \mathbb E\int_0^TS_t\,dt
 \le\mathbb E\int_0^{T\wedge\tau}S_t\,dt
 +\mathbb E\Bigl[\mathbf 1_{\tau\le T}\int_\tau^\infty S_t\,dt\Bigr]
 \le 32\,T+\mathbb E\Bigl[\frac{v_\tau}{\tau}\mathbf 1_{\tau\le T}\Bigr]
$$
by Lemma A ($L=2$) and Lemma B (tower property). Cauchy–Schwarz, Lemma C with
$E=\{\tau\le T\}\in\mathcal F_\tau$, and Lemma D give
$$
 \mathbb E\Bigl[\frac{v_\tau}{\tau}\mathbf 1_{\tau\le T}\Bigr]
 \le\bigl(\mathbb E[v_\tau^2\mathbf 1_{\tau\le T}]\bigr)^{1/2}
   \bigl(\mathbb E[\tau^{-2}\mathbf 1_{\tau\le T}]\bigr)^{1/2}
 \le\sqrt2\,\bigl(\mathbb E[\tau^{-2}\mathbf 1_{\tau\le T}]\bigr)^{1/2}.
$$
By `thm:KL-window`, $\mathbb P(\tau\le t)\le e^{-1/(\bar Ct)}$ for $t\le t_1(n)$; integration by
parts and $u=1/t$ give
$$
 \mathbb E[\tau^{-2}\mathbf 1_{\tau\le T}]
 =T^{-2}\mathbb P(\tau\le T)+2\int_0^Tt^{-3}\mathbb P(\tau\le t)\,dt
 \le\bigl(T^{-2}+2\bar CT^{-1}+2\bar C^2\bigr)e^{-1/(\bar CT)}
 \le5\max(\bar C^2,1)\,T^{-2}e^{-1/(\bar CT)} .
$$
Choose $t_c$ universal so that
$\sqrt5\max(\bar C,1)\,e^{-1/(2\bar Ct)}\le t^2$ for all $t\le t_c$; then the tail term is
$\le\sqrt2\,T$ and (G) holds with $C_0=32+\sqrt2\le34$, $C_1=0$, for every $t\le T_0(n)$.

Bridge: with $C_1=0$ the certified Grönwall gives $q(t)\le1+34t\le M_*:=1+34t_c$ on
$[0,T_0(n)]$; $T_*(n)=\min\{T_0(n),1/(2M_*)\}=T_0(n)$ for $n\ge n_0$; the certified
terminal-variance and Brascamp--Lieb steps give $\lambda\ge T_*(n)/2$ for every small-gap
approximant. Every approximant therefore has
$\lambda\ge\min\{3/(8K_n),\,T_0(n)/2\}=T_0(n)/2$ for $n\ge n_0$, i.e.
$C_P\le2\bar C\log^2n$; small $n$ is absorbed by $K_n$. The passage from regular approximants to
an arbitrary isotropic log-concave law is verbatim the certified dossier's
lower-semicontinuity argument at fixed $n$ (fixed smooth tests; no eigenfunction convergence).
$\square$

**What Theorem E is and is not.** It is a route-health certificate: Route S, with only certified
repository lemmas, one published window import, one published frontier import, and the Letwin
preprint, reproduces the polylog frontier — the first complete conditional KLS-scale output of
this route. It is **not** the gate: $T_0(n)\to0$, and the gate demands universal time. The gate
wording "uniformly on regular approximants" is respected ($C_0,C_1$ and the window constant
$\bar C$ are $\varepsilon$-free); the failure is confined to the $n$-dependence of $T_0$.

### Where each dimension enters, and the single missing estimate

The only $n$-dependent inputs are: (a) the window length $t_1(n)$ in `thm:KL-window`; (b) the
frontier constant $K_n$ in Lemma D. Improving (b) alone cannot help: even $K_n=O(1)$ would leave
$T_0(n)=t_1(n)$. Improving (a) to a universal window is **false**: `prop:covariance-spike` gives
$\|A_t\|_{\mathrm{op}}\gtrsim1/t$ with universal probability for exponential products once
$t\gtrsim1/\log n$, so $\mathbb P(\tau\le T)$ is not small at universal $T$ and no exit-rarity
argument survives. Therefore the unique remaining deliverable, in the exact form this
decomposition produces, is the **post-spike source charge**
$$
 \mathbb E\Bigl[\mathbf 1_{\tau\le T}\int_\tau^TS_t\,dt\Bigr]
 \ \le\ C_0T+C_1\int_0^Tq+2\,\mathbb E\int_0^TD_t\,dt,
 \qquad T\le T_0\ \text{universal},
 \tag{N}
$$
uniformly on regular approximants (Letwin may be assumed). By the proved w1s03 equivalence, (N)
plus Lemma A is equivalent, up to the low block, to local growth of $q$; unlike the pre-$\tau$
regime, (N) must genuinely consume damping, by the saturation result below.

## Established, part II: the certified budgets are exactly saturated — the small-gap branch has no shortcut

Direction 3 of the assignment conjectured that for $\lambda\le T_0/2$ the terminal-variance
argument already contradicts the certified budgets. This is **false**, and the failure is
sharp.

### The extremal profile

The two strongest certified scalar consequences are:

- terminal Brascamp--Lieb (bridge dossier, unconditional):
  $1-\int_0^tq\;=\;\mathbb E\operatorname{Var}_{\mu_t}(f)\;\le\;\lambda/t$ for all $t>0$;
- the integrated time-weighted identity (w1s03 eq. (38), from
  `lem:mm-time-weighted-fixed-source` and the $q$-identity):
  $t\,q(t)+\int_0^tq\;\le\;1$.

At any $t$, the two combine to $t\,q(t)\le\lambda/t$, i.e. $q(t)\le\lambda/t^2$. The profile
$$
 q(t)=\frac\lambda{t^2}\ \ (t\ge\lambda),\qquad q(t)=0\ \ (t<\lambda)
$$
satisfies $\int_0^tq=1-\lambda/t$ and $tq(t)+\int_0^tq=1$: it **simultaneously saturates both
constraints with equality** for all $t\ge\lambda$. Its remaining budget checks: the source burst
of total mass $q(\lambda)=1/\lambda$ occurs at times $\asymp\lambda$, so its time-weighted cost
is $\asymp\lambda\cdot(1/\lambda)=1$ — the certified budget is exactly exhausted, not violated;
the decay $-q'=2\lambda/t^3$ is exactly $2D_t$ with $D_t=q(t)\cdot(1/t)$, i.e. full alignment of
$g_t$ with a Brascamp--Lieb-saturating covariance spike $\|A_t\|_{\mathrm{op}}=1/t$; the
posterior-defect budgets are respected at these scales (the w1s03 scale model (39) with
$\varepsilon=\lambda$ is this profile's tensor realization); the C-channel can be taken zero and
the whitened K-budget $8t\lambda$ is respected since
$\|A^{-1/2}KA^{-1/2}\|^2\asymp t^2\lambda^2S_t$.

Consequences:

1. **No combination of the certified budgets refutes the small-$\lambda$ branch.** The claimed
   "direct contradiction from certified budgets alone" does not exist; every certified scalar
   inequality is met, two of them with equality. Any argument closing the small-gap branch is
   the gate itself in disguise.
2. **The gate is precisely burst exclusion.** The profile violates (G) at $T\asymp\lambda$:
   source $1/\lambda$ against budget $C_0\lambda+C_1+2\int_0^\lambda D\approx C_1$. All certified
   time-weighted budgets are blind exactly as $t\downarrow0$, in agreement with the recorded
   multiplier no-go (weight $\le Ct^2$ at zero). Theorem E excludes the burst for
   $\lambda\lesssim t_1(n)$ only because the spike carrying it cannot occur before $t_1(n)$.
3. **Damping repays the burst in arrears.** In the profile, $\int_\lambda^\infty 2D_t\,dt
   =q(\lambda)=1/\lambda$: the source is repaid by the exact damping in full, but only on a
   dilated horizon. A horizon-dilated variant of (G), charging $\int_0^{Ct}D$, would be satisfied
   up to a factor $1-1/C^2$ by this profile; but such a variant does not feed the certified
   Grönwall bridge (the damping term would reference the future), so this is an observation about
   the shape of the residue, not a viable weakening. Any successful (N) must couple the spike's
   damping to the spike's source with essentially no time lag — that is the quantitative content
   of "the fixed eigenfunction's tensor does not follow the covariance spike": if $H$ acquires
   spike-incident energy, $g$ must already be spike-aligned, engaging $D$ contemporaneously.

### Channel accounting on the window is strictly dominated (direction 2(iii), settled negatively)

From $\lambda H_t=2\operatorname{sym}C_t+K_t$:
$\lambda^2S_t\le8\|C_t\|^2+2\|K_t\|^2$. The certified C-budget and the Letwin-conditional
whitened K-budget give, on $\{t<\tau\}$ (so $\|A_t\|_{\mathrm{op}}\le2$),
$$
 \mathbb E\int_0^{T\wedge\tau}S_t\,dt
 \ \le\ \frac{8\lambda+32\int_0^T(t\lambda-\lambda^2\int_0^tq)\,dt}{\lambda^2}
 \ \le\ \frac{8+16T^2}{\lambda}.
$$
Compare Lemma A's direct bound $32T$: the channel bound is better only when
$T\ge\frac1{4\lambda}\ge\frac14$, i.e. **never on any admissible window** ($T\le t_c<\tfrac14$).
The exact leftover of the channel decomposition is therefore zero on the initial layer: the
$1/\lambda^2$ unwhitening makes both channels strictly worse than the direct whitened bound
wherever the latter exists, and beyond the window both channels face the identical unwhitening
fence. Recorded to prevent a rerun.

### The supermartingale attempt (direction 2(ii)) and its single uncontrolled term

For $Y_t=v_t\operatorname{Tr}\phi(A_t)$ with $\phi$ smooth increasing convex, Itô's formula
gives drift
$$
 -|g_t|^2\operatorname{Tr}\phi(A_t)
 -v_t\operatorname{Tr}\bigl(\phi'(A_t)A_t^2\bigr)
 +\frac{v_t}2\Gamma_t^\phi
 +\zeta_t\cdot\xi_t,
$$
where $\Gamma_t^\phi\ge0$ is the Daleckii--Krein Itô correction driven by the covariance third
moments $\mathcal T_{t,k}$, $\xi_{t,k}=\operatorname{Tr}(\phi'(A_t)\mathcal T_{t,k})$, and
$\zeta_t=\mathbb E_t[(f-m_t)^2(X-a_t)]$ is the test's third-moment vector. The first two terms
are good; $\Gamma^\phi$ is the same object the Klartag--Lehec trace potentials control (imported
only as endpoint theorems, not as a differential inequality). The genuinely new obstacle is the
cross term $\zeta_t\cdot\xi_t$: bounding $|\zeta_t|$ by $v_t\cdot(\text{covariance scale})$ is a
posterior reverse-Hölder / uniform-integrability statement for $(f-m_t)^2$ — moments of $f$
beyond the second under the random posterior. This is the same missing ingredient as the tail
term in Theorem E, where Lemmas C–D discharge it at the base measure on the small-gap branch.
Beyond the window, however, even perfect UI is insufficient: $\mathbb P(\tau\le T)$ is order one
there, so rarity arguments end and only the damping charge (N) remains. Labelled below.

## Established, part III: tensorization and subclasses (direction 4)

- **Products, common constants.** The par-02 factorization (its eqs. (28)–(29)) shows (G)
  tensorizes with no loss over products whose bottom eigenspace is spanned by factor
  eigenfunctions, provided all factors satisfy factor gates with common
  $(T_0,C_0,C_1)$ — identical or not. The gate's universal quantifier is tensorization-stable.
- **Uniformly convex subclass (calibration).** If $\nabla^2V\succeq\kappa_0I$ with $\kappa_0$
  universal, then $A_t\preceq\kappa_0^{-1}I$ pathwise for all $t$, and Lemma A's argument with
  $L=\kappa_0^{-1}$ gives (G) with $C_0=8\kappa_0^{-2}$, $C_1=0$, $T_0=\infty$
  (Letwin-conditional). Not progress (Bakry–Émery already covers the subclass) but a correct
  shape calibration.
- **Products of one-dimensional factors.** In fixed dimension one the window is universal, so
  the Theorem E pipeline gives a universal-window 1D gate **modulo one missing bound**: a
  dimension-free $2+\epsilon$ moment for 1D isotropic log-concave first eigenfunctions. Lemma D
  does not apply (1D has $\lambda\ge1/K_1$ universal: every 1D factor is large-gap, and the
  bootstrap coefficient $\frac{4K\lambda}{3}$ with $K=1/\lambda$ is $4/3>1$ in every dimension
  — a curious structural fact: the first eigenfunction's moment bootstrap fails marginally and
  dimension-independently). The 1D moment bound looks prover-tractable from
  $(e^{-V}f')'=-\lambda e^{-V}f$ and monotonicity of $f$; if certified, the product subclass
  (arbitrary mixtures of 1D factor types, arbitrary $n$) satisfies the full universal-time gate
  with common constants, Letwin-conditional. This would be the first nontrivial-beyond-convexity
  certified subclass. Left as a proposed follow-up, not claimed.

## Residue

1. **Needs new idea — the post-spike charge (N).** Bound
   $\mathbb E[\mathbf 1_{\tau\le T}\int_\tau^TS_t\,dt]$ by $C_0T+C_1\int q$ plus the full
   contemporaneous damping, at universal $T$. Equivalent (up to the low block, by the proved
   w1s03 equivalence) to local growth of $q$. The saturation profile shows: rarity arguments are
   unavailable, the damping must be engaged with no time lag, and the estimate must distinguish
   the fixed eigenfunction from an adaptively spike-following test. This is the fence
   (high-rank occupation) in its sharpest recorded form.
2. **Technical gap — restart machinery (Lemma B).** Strong Markov / weak uniqueness of the
   measure-valued SDE, optional-time posterior identification, conditional application of the
   certified lemma at a random measure. Standard; needs a dossier, not an idea.
3. **Technical gap — optional projection (Lemma C) and window integration (in Theorem E).**
   Routine; state stopping conventions as in the certified dossiers.
4. **Technical gap — ledger import for the published frontier.** `Klartag2023Logarithmic` is in
   the bibliography but has no ledger node; Lemma D needs it as a published import node.
5. **Technical gap — 1D eigenfunction $2+\epsilon$ moment.** Optional; unlocks the product
   subclass at universal time.
6. **Fenced — everything else attempted here.** Channel accounting (dominated on the window,
   $1/\lambda$ beyond), the $v_t\phi(A_t)$ supermartingale (uncontrolled $\zeta\cdot\xi$ cross
   term; and insufficient beyond the window even if controlled), any small-$\lambda$ shortcut
   from certified budgets (refuted by the saturation profile), any extension of exit-rarity past
   $c/\log n$ (`prop:covariance-spike`). The five dead ends listed in the assignment were cited,
   not rerun.

No route-fatal counterexample exists at this gate: the saturation profile is a scalar
consistency model, not a log-concave localization path, and refutes only proof shapes.

## Fence-by-fence evasion check

The node has no formal `bounded_by` edge; all registered obstructions checked.

- `obs:two-tail` (fixed cuts, absolute-scale slice bounds): no cut, slice, or excess estimate is
  used; Lemma A is a stopped expectation bound, not a slice-wise absolute claim, and the
  post-spike regime is explicitly left to occupation form (N).
- `obs:proj-ceiling`: the only tensor input is the full symmetric-matrix Letwin bound, used with
  its preprint-conditional standing displayed; no radial/projection test is promoted to a
  dimension-free chaos bound. Where Letwin is withheld nothing dimension-free is claimed.
- `obs:crude-insufficient`: no crude covariance integral $\Xi_T$ or logarithmic bootstrap
  appears; the window import is an exit-probability bound, not $\Xi_T$.
- `obs:relative-ceiling`: no all-measure relative occupation bound is inserted as a premise. The
  a priori input is the published frontier $K_n$, whose use produces a strictly weaker output
  ($\log^2n$ from $\log n$) — it is a calibrated import, not a hidden KLS assumption.
- `obs:circularity`: no localized isoperimetric profile or moving competitor family occurs.
- `obs:rank-one-refuted`: no product-cut counterexample claim; products enter only through the
  exact eigenfunction tensorization identity.
- `prop:covariance-spike` and the covariance-spike warning: respected constructively — it is the
  stated reason Lemma A's mechanism dies at the window edge and (N) is the residue.
- Recorded dead ends: the marginal-probability step is avoided (Lemma C is an identity, the tail
  is a joint Cauchy--Schwarz); the rank-entrance $(\log n)^8$ loss is avoided (window exit
  probability, not rank tails, and only inside the window); no moving projector, no one-sided
  projector energy, no crude $\|A\|_{\mathrm{op}}^2$ unwhitening (the operator norm is used only
  where it is $\le2$ by stopping), no integrated-exponential rank bound.
- Trace-upgrade cluster: this probe touches only `q:mm-spectral-occupation`. One transfer note
  for the `synthesizer`, without conclusion: the stopped-window/restart mechanism of Lemmas A–B
  is stated for a fixed test and may have a fixed-cut analogue; whether it interacts with
  `q:upgrade`'s prefix estimate is for the cluster owner to assess, and nothing here asserts it.

## Route viability and proposed gate update

Route S is strengthened. It now has, on repository inputs, a complete conditional
polylog-frontier reproduction ($C_P\le C\log^2n$ given Letwin) — evidence that its bookkeeping
is not lossy up to the genuine open difficulty — together with an exact saturation profile
showing that difficulty is irreducible to certified budgets. The gate should name the post-spike
charge rather than the generic full-damping estimate.

Proposed one-line gate update for the orchestrator (route-control text only; drafted, not
applied):

> The initial layer is charted: conditional on Letwin, the stopped bound
> $\mathbb E\int_0^{T\wedge\tau_2}\|H\|^2\le32T$, the $\tau$-restart of the certified
> time-weighted lemma, and the small-gap fourth-moment bootstrap give (G) with $C_0=34$, $C_1=0$
> on $[0,c/\log^2n]$ and reproduce $C_P=O(\log^2n)$; the sole remaining deliverable is the
> post-spike charge
> $\mathbb E[\mathbf 1_{\tau_2\le T}\int_{\tau_2}^T\|H_t\|^2dt]\le C_0T+C_1\int q+2\mathbb E\int D$
> at universal $T$, which must engage the damping with no time lag (the budgets are saturated by
> $q(t)=\lambda/t^2$); exit-rarity beyond $c/\log n$ is fenced by `prop:covariance-spike`.

## Proposed ledger delta

Candidate nodes only; all `open` (or the displayed conditional standing) pending prover and
independent review; no `proved`, `solution`, or `checked_by` metadata is proposed.

```yaml
- id: thm:klartag-logn
  kind: theorem
  status: imported
  import_class: published
  references: [Klartag2023Logarithmic]
  route: shared
  file: modules/kls/15-covariance-technology.tex
  statement: "Every isotropic log-concave probability on R^n (n>=2) satisfies C_P <= C log n, via the Cheeger bound psi_n <= C sqrt(log n) and Cheeger's inequality."

- id: lem:mm-stopped-window-source
  kind: lemma
  status: open
  route: moment-map-spectral
  file: modules/kls/30-spectral-route.tex
  statement: "Conditional on thm:letwin-qcts: for every regular approximant, every fixed unit-variance test, every L>=1 and T>0, with tau_L the first time ||A_t||_op reaches L, E int_0^{T wedge tau_L} ||H_t||_HS^2 dt <= 8 L^2 T, uniformly in dimension and regularization."
  depends_on: [thm:letwin-qcts]

- id: lem:mm-restart-deweighting
  kind: lemma
  status: open
  route: moment-map-spectral
  file: modules/kls/30-spectral-route.tex
  statement: "For every a.s. positive stopping time sigma of the observation filtration on a regular approximant and every fixed L^2 test, E[int_sigma^infty ||H_t||_HS^2 dt | F_sigma] <= Var_{mu_sigma}(f)/(eps+sigma) <= v_sigma/sigma, by conditional application of lem:mm-time-weighted-fixed-source with kappa = eps+sigma after the strong-Markov restart of the localization."
  depends_on: [lem:mm-time-weighted-fixed-source]

- id: lem:mm-smallgap-fourth-moment
  kind: lemma
  status: open
  route: moment-map-spectral
  file: modules/kls/30-spectral-route.tex
  statement: "If every isotropic log-concave law in dimension n satisfies C_P <= K_n (thm:klartag-logn), then every normalized first eigenfunction of a regular isotropic approximant with lambda <= 3/(8 K_n) satisfies E f^4 <= 2, via lambda E f^4 = 3 E f^2 |grad f|^2 and Poincare for f^2."
  depends_on: [thm:klartag-logn]

- id: prop:mm-window-occupation
  kind: proposition
  status: open
  route: moment-map-spectral
  file: modules/kls/30-spectral-route.tex
  statement: "Conditional on thm:letwin-qcts: with T0(n)=min(t_c, 1/(Cbar log^2 n)) from thm:KL-window, q:mm-spectral-occupation holds on [0,T0(n)] with C0=34, C1=0 for every first eigenfunction with lambda <= 3/(8 K_n); combined with the certified bridge argument at fixed n and the large-gap branch, every isotropic log-concave law satisfies C_P <= C log^2 n conditional on thm:letwin-qcts."
  depends_on: [thm:letwin-qcts, thm:KL-window, thm:klartag-logn, lem:mm-stopped-window-source, lem:mm-restart-deweighting, lem:mm-smallgap-fourth-moment, lem:mm-time-weighted-fixed-source]
```

`q:mm-spectral-occupation` remains `open`; no status change and no new `bounded_by` edge is
proposed for it.

## Numerical handoff

None. The residue (N) is a universal analytic estimate with no fixed refuting threshold; the
saturation profile is exact arithmetic already displayed. The parallel `kls-align` and
`cmh-gate-zero` runs are unaffected; no eigenfunction-tensor computation is requested.

```yaml
outcome: complete
artifacts:
  - research/explorations/2026-08-30-kls-route-prober-mm-occupation-initial-layer-w4s01.md
proposed_deltas:
  - Add the five candidate nodes displayed above (one published import, three open lemmas, one open conditional proposition); statuses exactly as displayed, no proof metadata.
  - Route-control: replace the q:mm-spectral-occupation gate paragraph with the proposed one-line update quoted above (orchestrator-owned; drafted only).
next_role: prover
next_prompt: |
  Write standalone dossiers for the Route-S window chain, in this order and under distinct
  solution keys: (1) lem:mm-stopped-window-source, (2) lem:mm-restart-deweighting,
  (3) lem:mm-smallgap-fourth-moment, then (4) prop:mm-window-occupation consuming (1)-(3).
  Work from research/explorations/2026-08-30-kls-route-prober-mm-occupation-initial-layer-w4s01.md.
  For (1): prove the pathwise whitened duality ||A_t^{-1/2} H_t A_t^{-1/2}||_HS^2 <= 8 v_t on the
  log-concave posterior via thm:letwin-qcts applied to the whitened variable, keep the
  conditional standing explicit, and use only the stopped operator-norm bound and E v_t <= 1; no
  independence step, no unstopped ||A_t||_op moment. For (2): reconstruct the strong-Markov
  restart of the planted channel at a stopping time sigma (weak uniqueness of the localization
  SDE, optional-time posterior identification, regular conditional distributions), verify
  mu_sigma is (eps+sigma)-strongly log-concave, and apply the certified
  lem:mm-time-weighted-fixed-source conditionally with kappa = eps+sigma; state stopping and
  removal conventions as in the certified dossiers. For (3): first add or request the published
  import node thm:klartag-logn; then prove lambda E f^4 = 3 E f^2 |grad f|^2 by integration by
  parts on the regular approximant (qualitative L^4 finiteness from the epsilon-regular class,
  used only for finiteness) and close the bootstrap for lambda <= 3/(8 K_n). For (4): assemble
  with tau = tau_2, Cauchy-Schwarz, the optional projection E[v_tau^2 1] <= E f^4, the
  thm:KL-window tail integral E[tau^{-2} 1_{tau<=T}] <= 5 max(Cbar^2,1) T^{-2} exp(-1/(Cbar T)),
  and a universal t_c; then rerun the prop:spectral-sufficiency bridge argument at fixed n with
  C0=34, C1=0 and the lambda-branch split at 3/(8 K_n), concluding C_P <= C log^2 n conditional
  on thm:letwin-qcts. Do not claim q:mm-spectral-occupation, any universal-time statement, any
  beyond-window bound, or anything about q:upgrade, q:stein-weighted, or q:alignment. Hand each
  compiled dossier to a distinct cold proof-checker.
```
