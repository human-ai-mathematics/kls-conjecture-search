---
type: exploration
date: "2026-08-30"
outcome: proposed
nodes:
  - q:weighted
---
# KLS route probe: the source-screened weighted interface, audited and partially proved

Date: 2026-08-30

Role: `kls-route-prober`

Run id: `w4w01`

Concurrency key: `kls-gate:q:weighted`

Scope: only the `q:weighted` replacement interface (Candidates A/B of the W3 probe). This probe
does not open `q:upgrade`, `q:alignment`, or the geometric content of `q:stein-weighted`; the
trace-companion algebra below is used strictly as the `q:weighted` consumer side, and the one
place where a comparison with the all-cut/tight-prefix Carleson problem arises is flagged for the
`synthesizer` instead of being decided here (CLAUDE.md constraint 6). No numerics are run; a
decision table for the parallel `finum` run `w4a01` is given at the end.

## Gate, quoted verbatim

From `research/kls/gating.md`, `q:weighted`, current wave:

> The candidate cut scale $\lambda_{\rm cut}(A,K)$ passes exact cylinder tensorization and the
> aligned two-tail test, but is not perturbatively stable:
> $\lambda_{\rm cut}(\operatorname{diag}(1,L),\varepsilon E_{12}^{\rm sym})=(1+L)/2$ for every
> $\varepsilon\ne0$. The preferred unproved replacement is therefore source-screened: charge the
> weighted excess only where $Q_t\ge\kappa e_tW_{\rm cut}$, and on the complement return at most an
> absorbable fraction $\theta Q_t$. A matching trace coefficient must satisfy
> $2\beta/(1-\theta)+64\eta^2<1$. Neither the screened supply nor its trace companion is proved.

Notation, fixed once: $W_{\rm cut}=W_{\rm cut}(A_t,K_t)=(1+\lambda_{\rm cut}(A_t,K_t))^{5/2}$
with the certified convention $\lambda_{\rm cut}(A,0)=0$
(`solutions/lem-lyapunov-stein-duality.tex`);
$Q_t=\mathcal S_{\mu_t}(E)/s_t=s_t\|K_t\|_{\rm HS}^2$ (`prop:stein-rep`,
`modules/kls/13-stein-dictionary.tex`); the aligned set is
$\mathcal A_{\kappa,t}=\{Q_t\ge\kappa\,e_tW_{\rm cut}\}$; all time integrals run over
$[0,T\wedge\tau_\eta]$ with the continuous-exit time
$\tau_\eta=\inf\{t:|p_t-1/2|>\eta\}$ and the conventions of
`solutions/kls-localization-riccati-core.tex`.

## Term-by-term decomposition

| term | role in the screened package | certified control | residue |
|---|---|---|---|
| $Q_t$ | source currency of the trace companion (22) | $Q_t\le 4\lambda_{\rm cut}/t$ pathwise (`lem:lyapunov-stein-duality`); $Q_t\le 2S_t+64\eta^2D_t$ on the window (`lem:stein-vs-source`); $\mathbb E\int S_t\,dt\le\operatorname{Tr}R_0\le n$ (`cor:per-direction`); $\le k$ for $J$-cuts on products (`thm:budget`(i)) | no universal fixed-time or $O(T)$ bound |
| $e_t=P_t-I_{\mu_t}(p_t)$ | screened supply factor | $\mathbb E\int_0^{T\wedge\tau}e_t\,dt\le(1+e_0)T$ for every cut and stopping time (`prop:trivial-excess`); exact identity $\mathbb E e_t=e_0+I_\mu(p_0)-\mathbb E I_{\mu_t}(p_t)$ in the compact-smooth class (`lem:excess-identity`) | identity usable only in the upper-bound direction (`obs:circularity`) |
| $W_{\rm cut}$ | cut-local weight | direct-sum invariance, harmonic-mean formula, two-tail calibration $\lambda_{\rm cut}(A_\Lambda,K_\Lambda)=\Lambda$ (all certified) | discontinuous at $K=0$; leakage identity (8) of W3 |
| $r_t$, $D_t$ | damping and drift currency of the consumer | scalar Riccati $dr=dM+(S-D)dt$, $D\ge r^2$ (`thm:scalar-riccati`) | none new |
| $\mathbf 1_{\mathcal A_{\kappa,t}}$ | screen | Borel in the state (W3, measurability section) | progressive-measurability convention needed (Section 6) |
| absorption $(\theta,\beta,\eta)$ | consumer margin | `cor:tight-window-consumption` needs $\eta\le1/6$, $|p_0-1/2|\le\eta/2$, damping $<1$ | audited in Section 1; $64\eta^2<1$ forces $\eta<1/8$ |

## 1. Re-audit of the consumption algebra (task 1)

Hypotheses, stated in full because each is load-bearing. Fix $\eta\in(0,1/6]$,
$|p_0-1/2|\le\eta/2$, $0\le\theta<1$, $\beta\ge0$, $C_0,C_1,C_2,C_E\ge0$, $T_0>0$, and assume,
for **every** $T\le T_0$, with all integrals over $[0,T\wedge\tau_\eta]$:

- (S) screened supply: $\displaystyle\mathbb E\int e_tW_{\rm cut}\mathbf 1_{\mathcal A_{\kappa,t}}\,dt\le C_ET$;
- (C) screened trace companion:
  $\displaystyle\mathbb E\int Q_t\,dt\le C_0T+C_1\mathbb E\int r_t\,dt+\beta\mathbb E\int D_t\,dt
  +C_2\mathbb E\int e_tW_{\rm cut}\mathbf 1_{\mathcal A_{\kappa,t}}\,dt
  +\theta\mathbb E\int Q_t\mathbf 1_{\mathcal A_{\kappa,t}^c}\,dt$.

**Step 0 (a priori finiteness — a step W3 did not record; it is required and it is certified).**
The absorption below subtracts $\theta\,\mathbb E\int Q\mathbf 1_{\mathcal A^c}$ from both sides,
which is legitimate only if $\mathcal Q:=\mathbb E\int Q_t\,dt<\infty$. This is true with a
dimension-dependent constant: on $\{t<\tau_\eta\}$ the certified conversion
(`lem:stein-vs-source`, second inequality) gives $Q_t\le 2S_t+64\eta^2D_t$; summing
`cor:per-direction` over an orthonormal basis gives
$\mathbb E\int S_t\,dt\le\operatorname{Tr}R_0\le n$; integrating `thm:scalar-riccati` at the
localizing stopping times of the certified dossier gives
$\mathbb E\int D_t\,dt\le r_0+\mathbb E\int S_t\,dt\le 1+n$. Hence
$\mathcal Q\le 2n+64\eta^2(1+n)<\infty$. Similarly
$\mathbb E\int r_t\,dt\le(1+n)T<\infty$. No uniformity in $n$ is needed for this step.

**Step 1 (absorption).** Write
$\mathcal Q=\mathcal Q_{\mathcal A}+\mathcal Q_{\mathcal A^c}$. From (C),
$\mathcal Q_{\mathcal A}+(1-\theta)\mathcal Q_{\mathcal A^c}
\le C_0T+C_1\mathcal R+\beta\mathcal D+C_2\,\mathbb E\int e_tW\mathbf 1_{\mathcal A}$, and since
$1-\theta\le1$,
$$
\mathcal Q\le\frac{(C_0+C_2C_E)T+C_1\mathcal R+\beta\mathcal D}{1-\theta},
$$
using (S). The exact absorption condition is $\theta<1$ together with Step 0; nothing else.

**Step 2 (conversion to the Riccati source).** On $\{t<\tau_\eta\}$ the certified conversion
gives $S_t\le 2Q_t+64\eta^2D_t$ (this direction needs only $s_t\ge1/8$, valid for
$\eta\le1/4$). Integrating,
$$
\mathbb E\int S_t\,dt
\le \frac{2(C_0+C_2C_E)}{1-\theta}\,T
 +\frac{2C_1}{1-\theta}\,\mathbb E\int r_t\,dt
 +\Bigl(\underbrace{\frac{2\beta}{1-\theta}+64\eta^2}_{=:\alpha}\Bigr)\mathbb E\int D_t\,dt .
$$

**Step 3 (consumption).** This is exactly the input `eq:sol-tight-carleson` of the certified
`cor:tight-window-consumption` with
$C_0'=2(C_0+C_2C_E)/(1-\theta)$, $C_1'=2C_1/(1-\theta)$, and damping $\alpha$. The corollary
requires $\alpha<1$, i.e.
$$
\boxed{\ \frac{2\beta}{1-\theta}+64\eta^2<1\ }
$$
**verbatim as the gate states it: verified, not corrected.** Two audit notes the gate text does
not display:

1. $64\eta^2<1$ forces $\eta<1/8$; combined with the corollary's own domain this means the
   admissible window is $\eta\in(0,1/8)$, strictly inside the $\eta\le1/6$ convention, and
   $\beta<(1-\theta)(1-64\eta^2)/2$. There is no admissible choice with $\eta\ge1/8$.
2. The constants $2$ and $64\eta^2$ are those certified in `lem:stein-vs-source`. A refined
   family $(1+\varepsilon)\beta/(1-\theta)+32(1+\varepsilon^{-1})\eta^2<1$ ($\varepsilon>0$)
   would follow from an $\varepsilon$-weighted variant of that conversion; that variant is
   uncertified, so the boxed condition is the correct current gate coefficient.

**Step 4 (Gronwall and endgame, unchanged).** With $u(T)=\mathbb E r_{T\wedge\tau_\eta}$ the
corollary's own proof gives $u(T)\le(1+C_0'T)e^{C_1'T}=:C_*$, then
$\Prob(\tau_\eta\le T)\le 9C_*T/(8\eta^2)$, a survival time $T_*$, and
`lem:survival-implies-kls`. The $\alpha<1$ margin is used only to discard
$(\alpha-1)\mathbb E\int D\le0$ (finite by Step 0); it does not enter the constants.

**Constant-supply variant (needed in Section 2).** If (S) is replaced by
$\mathbb E\int e_tW\mathbf 1_{\mathcal A}\,dt\le c_E$ (a constant, not $\propto T$), the chain
survives with one one-line change: Gronwall reads
$u(T)\le\bigl(1+2C_2c_E/(1-\theta)+C_0'T\bigr)e^{C_1'T}$, still bounded, and
$T_*\asymp\eta^2/C_*$ shrinks with $c_E$. So the consumer does **not** intrinsically require the
$O(T)$ shape; it requires a $T$-uniform bound with at most linear growth. This is a genuine
relaxation of the gate's phrasing (the literal certified corollary has no constant term; the
extension is a trivial Gronwall restatement — technical gap, prover-level, not a new idea).

## 2. The supply in the exact split class (task 2)

Setting: $\mu=\bigotimes_{i=1}^n\mu^{(i)}$, each factor isotropic one-dimensional log-concave;
$E$ measurable with respect to a fixed coordinate set $J$, $|J|=k$, $0<p_0<1$,
$P_0(E)<\infty$; product structure is preserved pathwise, and `lem:block` applied to
$(\mu_t,E)$ gives $K_t=P_JK_tP_J$ pathwise, whence (harmonic-mean formula, certified remark in
the Lyapunov dossier) $\lambda_{\rm cut}(A_t,K_t)\le\max_{i\in J}A_t^{(i)}$.

### 2.1 A theorem-grade screened supply, total-budget form

**Proposition (split-class screened supply; complete analytic sketch).** For every such
$(\mu,E,J,k)$, every $\eta\in(0,1/4]$, every $\kappa>0$, and every $T>0$,
$$
\mathbb E\int_0^{T\wedge\tau_\eta}
 e_tW_{\rm cut}(A_t,K_t)\,\mathbf 1_{\{Q_t\ge\kappa e_tW_{\rm cut}\}}\,dt
\ \le\ \frac{2k+64\eta^2(1+k)}{\kappa}.
$$

*Proof sketch, every step certified.* On $\mathcal A_{\kappa,t}$, pathwise
$e_tW_{\rm cut}\le Q_t/\kappa$ (definition of the screen; at $K_t=0$ both sides vanish under the
conventions). On $\{t<\tau_\eta\}$ with $\eta\le1/4$, $s_t\ge3/16\ge1/8$ and the certified
conversion gives $Q_t\le 2S_t+64\eta^2D_t$. By `lem:block` and `thm:budget`(i) — whose dossier
audit records that part (i) needs only $0<p_0<1$, not the coarse balance window —
$\mathbb E\int_0^\infty S_t\,dt\le\sum_{i\in J}(R_0)_{ii}\le k$. Integrating
`thm:scalar-riccati` at the dossier's localizing stopping times, discarding
$\mathbb E r_{T\wedge\tau_\eta}\ge0$, and using $r_0\le1$:
$\mathbb E\int_0^{T\wedge\tau_\eta}D_t\,dt\le 1+\mathbb E\int_0^{T\wedge\tau_\eta}S_t\,dt\le1+k$.
Combine and divide by $\kappa$. Monotone convergence and Fatou exactly as in the certified
product dossier. $\square$

This is, to my knowledge, the first positive theorem-grade statement for the new weight: the
screened supply (W3's inequality (21)) **holds in the exact split class for every $\kappa>0$**,
with no near-worst hypothesis, in *total-budget* form: the bound is a constant
$c_E(k,\eta,\kappa)=(2k+64\eta^2(1+k))/\kappa$, uniform in $T$, uniform in the ambient dimension
$n$, and uniform in arbitrarily many spectator coordinates (they never enter). It is **not** of
the form $C(k)\,T$.

Consistency calibration (conditional, not a theorem): if the companion (C) also held in this
class, Section 1's constant-supply variant gives $T_*\asymp\eta^2/(1+k)$ and a boundary bound
$\asymp(1+k)^{-1/2}$ — exactly the certified `thm:budget`(iii) scale
$c\min(p_0,q_0)/\sqrt{1+k}$. The screened interface is therefore correctly calibrated against
the one product theorem the repository has; it adds no KLS strength there, as expected.

### 2.2 What blocks the $C(k)\,T$ form

The gap between the constant $c_E(k)$ and a genuine $C(k)T$ bound is a **fixed-time** source
moment: $C(k)T$ for all small $T$ would follow from
$\sup_{t\le T_0}\mathbb E\bigl[Q_t\mathbf 1_{\mathcal A_{\kappa,t}}\mathbf 1_{\{t<\tau_\eta\}}\bigr]\le C(k)$,
which no certified node provides — every certified budget is time-integrated. A heuristic in the
split class says the estimate is plausible: an active-coordinate spike to height $\lambda\sim c/t$
has per-coordinate probability of order $e^{-1/t}$ (the Klartag–Lehec channel event with
$s=1/t$), so the spike contribution to $\mathbb E\int_0^TQ\mathbf 1_{\mathcal A}$ is of order
$k\int_0^Tt^{-2}e^{-1/t}\,dt\le k\,e^{-1/(2T)}\ll kT$, and the bulk contribution is governed by
$\mathbb E Q_t$ near its initial value. Label: **technical gap bordering needs-new-idea**
(a fixed-time expected-source estimate for $J$-cuts on products; self-contained, provable-looking,
but not a consequence of the integrated budgets).

### 2.3 What blocks $C$ independent of $k$, and the unscreened split supply

For the **unscreened** split-class supply $\mathbb E\int e_tW_{\rm cut}\,dt\le C(k)T$, the first
unjustifiable step is a decorrelation: $e_t\le P_t$ and
$W_{\rm cut}\le(1+\max_{i\in J}v_{i,t})^{5/2}$ are **both** $J$-block quantities, so the
spectator-dossier independence trick is unavailable, and:

- Cauchy–Schwarz needs $\mathbb E P_t^2$, which the perimeter-martingale dossier controls only in
  the compact-smooth class with a diameter-dependent $e^{D^2t}$ — not universal (technical gap,
  likely not repairable to a universal constant);
- the alternative route needs a per-coordinate posterior-variance moment
  $\mathbb E v_{i,t}^p\le C_p$ for some $p>3$, uniformly over centered variance-one log-concave
  one-dimensional priors. The supermartingale power trick ($d(v^p)$ has drift
  $\le(\tfrac{p(p-1)}2C_3^2-p)v^{p+1}$ with $|m_3|\le C_3v^{3/2}$) certifies it only up to
  $p\le1+2/C_3^2$, far below $3$. This **one-dimensional posterior-variance tail question** is a
  clean, isolated open estimate and would be a good future candidate node; I do not propose it
  as a ledger delta because no partial theorem is established here.

For $C$ **independent of $k$**: the W3 leakage identity realizes dynamically inside $J$. Take a
balanced symmetric base cut with matched conditional variances so that $K_0=0$ exactly while
$e_0>0$ (two interfaces against a one-interface profile competitor), then couple it with
amplitude $\varepsilon$ to $N=k-M$ in-$J$ exponential coordinates. At a spike time,
$K_t$ is dominated by cross terms, and the leakage identity charges
$\lambda_{\rm cut}\approx(1+v_{\rm spike})/2$ regardless of $\varepsilon$; choosing
$k\simeq e^{2/T}$ after $T$ reproduces the refuter quantifier order. Two honest caveats: (i) the
harmonic-mean structure protects any state whose base entry of $K_t$ retains a fixed relative
weight — the construction must actually drive the base contrast to zero at spike times, which
requires a pathwise nonvanishing-cross-covariance verification not done here; (ii) the whole
construction lands **outside** $\mathcal A_\kappa$ ($Q_t=O(\varepsilon^2)$), so it threatens only
the unscreened (17), never Candidate B. Label: candidate refutation target for unscreened
(17)-in-split-class, needs construction; it is exactly why the screen exists.

## 3. The general screened supply: interpolation audit and the collapse question (task 3)

Available dominations on $\mathcal A_{\kappa,t}\cap\{t<\tau_\eta\}$, all certified:
(i) $e_tW_{\rm cut}\le Q_t/\kappa$; (ii) $\mathbb E\int e_t\,dt\le(1+e_0)T$;
(iii) $Q_t\le4\lambda_{\rm cut}/t$ pathwise; (iv) $\lambda_{\rm cut}\le\lambda_{\max}(A_t)\le1/t$.

### 3.1 Hölder/pointwise interpolation: a quantified no-go

For any $s\in(0,1]$, combining (i), (iii), (iv):
$e_tW\mathbf 1_{\mathcal A}\le(e_tW)^{1-s}(Q/\kappa)^s
\le(4/\kappa)^s\,e_t^{1-s}\,t^{-2s}(1+1/t)^{\frac52(1-s)}$, and Hölder against (ii) leaves the
deterministic factor $h(t)^{1/s}$ with $h(t)\asymp t^{-(5/2-s/2)}$ near zero; $\int_0^Th^{1/s}$
converges iff $(5-s)/(2s)<1$ iff $s>5/3$ — impossible. The same computation for the variant
$e_tW=e_t^{1-s}(e_tW^{1/s})^s$ shows that Hölder interpolation *conserves the total
$\lambda$-exponent*: the target carries exponent $5/2$, the only budgeted quantity with an excess
factor carries exponent $0$ (`prop:trivial-excess`), and every pathwise cap on $\lambda$ costs a
non-integrable power of $t$. **Conclusion: no Hölder/pointwise combination of
(i)–(iv) closes the initial layer.** Any closure must inject a source-side expectation bound.

### 3.2 The reduction lemma (established) and the exact collapse verdict

Time-splitting at $t_*>0$, using (iv) on $\{t>t_*\}$ with (ii), and (i) on $\{t\le t_*\}$:
$$
\mathbb E\int_0^{T\wedge\tau_\eta}e_tW_{\rm cut}\mathbf 1_{\mathcal A_{\kappa,t}}\,dt
\ \le\ \Bigl(1+\tfrac1{t_*}\Bigr)^{5/2}(1+e_0)\,T
\ +\ \frac1\kappa\,\mathbb E\int_0^{t_*\wedge T\wedge\tau_\eta}Q_t\,
      \mathbf 1_{\mathcal A_{\kappa,t}}\,dt .
$$
This is proved (each step is a certified pathwise domination plus `prop:trivial-excess`).
Therefore the screened supply (21) reduces, up to a universal $O(T)$ layer, to the

**aligned initial-layer source estimate:**
$\displaystyle\mathbb E\int_0^{t_*\wedge T\wedge\tau_\eta}Q_t\mathbf 1_{\mathcal A_{\kappa,t}}\,dt\le C\,T$
for all $T\le T_0$ (universal $C$, on the admitted measure class).

Answer to the CRITICAL question, in three sharp parts:

1. **Every pointwise/Hölder route passes through a source-occupation (Carleson-type) estimate.**
   By 3.1 the excess budget cannot carry any positive power of the weight; by 3.2 the entire
   difficulty is the displayed aligned initial-layer estimate. In this sense a collapse is real.
2. **But the estimate reached is not the all-cut Carleson.** It differs in three scope
   restrictions, all coming from the excess factor and the certified Lyapunov bound:
   (a) it is screened to $\mathcal A_\kappa$ — states whose weighted excess dominates their
   source (the leakage states, the spectator-spike states) are excluded from the charge;
   (b) it lives only on the initial layer $[0,t_*]$: the $t>t_*$ layer is *finished* by
   `prop:trivial-excess`, a mechanism no all-cut source estimate contains;
   (c) on $\mathcal A_\kappa$ the excess is pathwise pinned,
   $e_t\le 4/(\kappa t(1+\lambda_{\rm cut})^{3/2})$, so two-tail-calibrated states
   ($e\asymp\lambda^{-1/2}$) can be aligned only for $t\lesssim4/(\kappa\lambda)$: the dangerous
   occupation is automatically confined to a $\lambda^{-1}$-short initial window.
   Whether the residual kernel (occupation of large cut-oriented $\lambda_{\rm cut}$ from
   isotropic start, inside its own $\lambda^{-1}$ window) is strictly easier than, equivalent
   to, or incomparable with `ass:tight-prefix-carleson` is precisely a trace-cluster comparison;
   per constraint 6 I record the reduction and **hand the comparison to the synthesizer**. I do
   not conclude "relabeling of `q:upgrade`" and I do not conclude the contrary.
3. **Where the excess factor gives genuinely different room, exactly.** (a) The whole
   $t>t_*$ layer (see 2 above). (b) The pathwise pinning (c) above, which no unweighted source
   estimate has. (c) *Not* through the excess identity: improving
   $\mathbb E\int_{t_*}^{T}e_t\,dt$ beyond $(1+e_0)T$ via
   $\mathbb E e_t=e_0+I_\mu(p_0)-\mathbb E I_{\mu_t}(p_t)$ requires a lower bound on
   $\mathbb E I_{\mu_t}(p_t)$ — that is the fenced direction of `obs:circularity` and is not
   available; the identity is usable only as the (already implied) upper bound.

### 3.3 The joint estimate actually needed, with quantifiers

Combining 3.1–3.2, the precise candidate inequality behind Candidate B is:

> **Candidate (aligned initial-layer occupation).** There exist universal
> $\kappa\in(0,\kappa_{\rm TT})$, $t_*,T_0,C>0$, $\eta\in(0,1/8)$ such that for every isotropic
> log-concave $\mu$ on $\mathbb R^n$ satisfying the near-worst premise
> $h_n^*\le h_\bullet$, $h_\mu\le(1+\varepsilon_{\rm nw})h_n^*$, every finite-perimeter cut with
> $p_0=1/2$, $e_0\le\varepsilon_Eh_\mu$, and every $T\le T_0$:
> $$
> \mathbb E\int_0^{t_*\wedge T\wedge\tau_\eta}
>   s_t\|K_t\|_{\rm HS}^2\,
>   \mathbf 1_{\{s_t\|K_t\|_{\rm HS}^2\ \ge\ \kappa\,e_t(1+\lambda_{\rm cut}(A_t,K_t))^{5/2}\}}\,dt
> \ \le\ C\,T .
> $$
> Informally: loss of the moving profile (large $e_t$, which *removes* a state from the charge)
> and occupation of a large cut-oriented pair scale (large $\lambda_{\rm cut}$, which by the
> certified $Q_t\le4\lambda_{\rm cut}/t$ can carry a large aligned source only on a
> $\lambda^{-1}$-short window) must not coincide too often from an isotropic start.

By the reduction lemma this implies (21) with
$C_E=(1+1/t_*)^{5/2}(1+\varepsilon_Eh_\bullet)+C/\kappa$, and by Section 1 the pair
(21)+(22) is consumption-complete. In the split class it is proved above in total-budget form.

## 4. Fence-by-fence stress test (task 4)

**`obs:two-tail` — chargeability recomputed and confirmed.** For the certified two-tail state
($a=\Phi^{-1}(3/4)\approx0.67449$): $Q_\Lambda=16a^2\varphi(a)^2\Lambda^2\approx0.7350\Lambda^2$,
$e_\Lambda=(2\varphi(a)-\varphi(0))\Lambda^{-1/2}\approx0.2366\Lambda^{-1/2}$,
$\lambda_{\rm cut}=\Lambda$ (certified calibration), so for every $\Lambda\ge1$
$$
\frac{Q_\Lambda}{e_\Lambda W_{\rm cut}}
=\frac{16a^2\varphi(a)^2}{2\varphi(a)-\varphi(0)}\Bigl(\frac{\Lambda}{1+\Lambda}\Bigr)^{5/2}
\ \ge\ \kappa_{\rm TT}:=2^{-5/2}\cdot3.1066\approx0.5492 .
$$
W3's formula and value check out. Any fixed $\kappa<\kappa_{\rm TT}$ (e.g. $\kappa=1/4$) keeps
every two-tail-calibrated state in $\mathcal A_\kappa$ for all $\Lambda\ge1$: the screen does not
discard the obstruction, and the $5/2$ power is retained. Evaded exactly.

**Leakage state falls outside $\mathcal A_\kappa$ — verified with exact values.** At
$A=\operatorname{diag}(1,L)$, $K=\varepsilon E_{12}^{\rm sym}$:
$Q=2s\varepsilon^2\le\varepsilon^2/2$ and
$W_{\rm cut}=\bigl((3+L)/2\bigr)^{5/2}$. Membership in $\mathcal A_\kappa$ requires
$e_t\le 2s\varepsilon^2/\bigl(\kappa((3+L)/2)^{5/2}\bigr)$; for any excess floor $e_->0$ the
state is excluded for all
$\varepsilon^2<\kappa e_-((3+L)/2)^{5/2}/(2s)$ — and the exclusion threshold *grows* with $L$,
so precisely the worst leakage states are excluded first. The companion may return at most
$\theta Q=2\theta s\varepsilon^2\to0$ there. The gate's design intent is confirmed exactly.

**Centered-exponential spectators inert.** For $E=E_0\times\mathbb R^N$:
$A_t=A_t^0\oplus B_t$, $K_t=K_t^0\oplus0$ pathwise, so by certified direct-sum invariance
$W_{\rm cut}=W_{\rm cut}(A_t^0,K_t^0)$ and $Q_t=s_t\|K_t^0\|^2$: a spectator spike changes
neither, while it inflates $e_t$ (profile crash by the Bobkov–Chistyakov quantile competitor,
upper-bound direction only). The state therefore moves *out of* $\mathcal A_\kappa$ or, if it
stays in, its charge is $\le Q_t/\kappa$ with $Q_t$ bounded on the base-stability event. The
certified refuters' lower bounds are order $T$ (`prop:spectator-excess-rate-obstruction`:
$\kappa_{\rm sp}P_0T$), consistent with an $O(T)$ or constant screened supply; and the
split-class proposition of Section 2.1 is uniform in $N$, as it must be. No tension with either
certified refutation.

**Gaussian halfspaces.** $e_t=0$ and $K_t=0$ at exact balance: $Q_t=0$, $W_{\rm cut}=1$, the
screen reads $0\ge0$ (membership with zero charge under the $\ge$ convention). No false cost.

**`obs:circularity`.** All uses of profile information in this probe are upper bounds
(`prop:trivial-excess` via the perimeter supermartingale; Bobkov–Chistyakov quantile competitors
in fence checks). The single tempting violation — refining the $t>t_*$ layer through the excess
identity — is identified in 3.2(3c) and *not* used. In the split class, a Bobkov–Houdré-type
product profile lower bound would be an external published anchor of the kind the fence permits;
it was not needed and is not imported.

**`obs:relative-ceiling`.** The supply is an absolute-scale bound on a restricted class
(near-worst in Candidate B general form; exact split class in Section 2). It is not an
all-measure relative $\Xi_T$ bound; `prop:ceiling` is not triggered.

**`obs:crude-insufficient`, `obs:proj-ceiling`.** Not used; the interface runs on the full
tensor $K_t$ and the Lyapunov energy, and no $\log n$ bootstrap enters.

**`obs:rank-one-refuted`.** Respected: the split-class theorem concerns fixed $J$-cuts with the
certified budget; nothing is claimed about `q:alignment` or path-adapted cuts.

## 5. Measurability debt, stated as the convention a dossier must adopt (task 5)

1. Work on the usual $\mathbb P$-augmented right-continuous Brownian filtration.
2. $P_t$ is defined as the countable rational infimum limit of continuous bounded mass
   martingales (`kls-excess-audit`, Lemma 1 construction); as a pathwise liminf of a countable
   family of continuous adapted processes it is progressively measurable.
3. $I_{\mu_t}(p_t)$, hence $e_t$: adopt the compact-smooth regular class of the certified
   dossiers for both measure and cut; there $\mu_t$ has a jointly measurable positive density
   field and $I_{\mu_t}(p)$ is jointly measurable in $(t,\omega,p)$ via a fixed countable regular
   competitor family. This is a *measurability* convention only; no supermartingale property of
   the moving infimum is asserted (`lem:inf-martingales` caveat preserved).
4. $Q_t$, $A_t$, $K_t$ are continuous adapted on $\{0<p_t<1\}$ in the regular class;
   $(A,K)\mapsto\lambda_{\rm cut}$ is Borel on supported pairs (fixed-rank strata plus Borel
   Moore–Penrose, per W3), so $W_{\rm cut}(A_t,K_t)$ and the indicator
   $\mathbf 1_{\mathcal A_{\kappa,t}}=\mathbf 1_{\{Q_t-\kappa e_tW_{\rm cut}\ge0\}}$ are
   progressively measurable; both appear only inside nonnegative Lebesgue-time integrals
   (Tonelli), never inside an Itô differential.
5. General laws/cuts: state (21)/(22) for the coordinatewise product-preserving truncated and
   smoothed approximants (the scheme certified in `kls-product-covariance`) and demand constants
   uniform in the approximation. Flag: the screened indicator does **not** pass to the limit
   monotonically, so the general statement must be *defined* on approximants, not obtained by
   limit interchange. This is an explicit technical gap any dossier must carry.

## 6. Directional read-out for the parallel finum run `w4a01`

No numerics were run here. The following measured values decide directions:

| observable | decision rule |
|---|---|
| empirical $\theta(\kappa)$ at $\kappa=\kappa_{\rm TT}/2\approx0.2746$ | if the required return fraction $\theta_{\rm emp}=\mathbb E\int Q\mathbf 1_{\mathcal A^c}$-share tends to $1$ as $n\to4096$, the companion (22) is directionally infeasible (Section 1 forces $\beta<(1-\theta)(1-64\eta^2)/2\to0$); if $\theta_{\rm emp}\le0.9$ stably, $\beta$ up to $0.05(1-64\eta^2)$ remains admissible |
| $\frac1T\int e_tW_{\rm cut}\mathbf 1_{\mathcal A}\,dt$ on the tail-union family | bounded in $n$ supports (21); growth by a factor $\ge4$ from $n=512$ to $n=4096$ is directional evidence against a universal $C_E$ |
| aligned initial-layer source $\int_0^{t_*}Q_t\mathbf 1_{\mathcal A}\,dt$ vs $T$, e.g. $t_*=1/4$ | this is the exact kernel identified in 3.2; $n$-stability of the ratio is the single most decision-relevant number |
| $\lambda_{\rm cut}$ vs $\lambda_{\max}$ trajectories | persistent $\lambda_{\rm cut}\ll\lambda_{\max}$ quantifies the cut-local weight's advantage; $\lambda_{\rm cut}\approx\lambda_{\max}$ at high-source times would say the screen buys little on this family |

## 7. Residue

1. **Established (prover-formalizable now):** (a) the consumption re-audit of Section 1,
   including the previously unrecorded a priori finiteness step and the constant-supply variant;
   (b) the split-class screened supply proposition of Section 2.1; (c) the reduction lemma of
   Section 3.2; (d) all fence computations of Section 4.
2. **Technical gap:** restating `cor:tight-window-consumption` with a constant additive term
   (one-line Gronwall change); the regular-class measurability conventions of Section 5; the
   fixed-time expected-source estimate that would upgrade Section 2.1 to $C(k)T$ form.
3. **Needs new idea:** the general aligned initial-layer occupation candidate of 3.3 — the
   surviving core of Candidate B; and the one-dimensional posterior-variance tail question
   ($\mathbb E v_t^p\le C_p$, $p>3$) behind the unscreened split supply.
4. **Fenced:** any refinement of the $t>t_*$ layer via a lower bound on
   $\mathbb E I_{\mu_t}(p_t)$ (`obs:circularity`); any closure through the crude covariance
   bootstrap or projection-only data; deciding whether the 3.3 kernel equals the tight-prefix
   trace Carleson (constraint 6 — synthesizer's comparison, not mine).
5. **Candidate refuter, needs construction:** the in-$J$ zero-base-contrast leakage witness
   against the *unscreened* (17) with $k$-independent constant (Section 2.3); it does not
   threaten Candidate B.

## 8. Route viability and proposed gate line

The screened interface materially advanced: its consumer algebra is now fully audited (with the
exact coefficient the gate states, plus the forced $\eta<1/8$ and the a priori finiteness step),
its supply is proved in the exact split class in total-budget form, and its general form is
reduced to a single, precisely stated aligned initial-layer occupation estimate whose relation
to the trace-upgrade cluster is a synthesizer question. Candidate B remains open but is now the
best-specified object on this route.

Proposed one-line gate update (orchestrator applies or not):

> The screened consumption algebra is audited: with $\theta<1$, a priori finite
> $\mathbb E\int Q_t\,dt$ (certified, dimension-dependent), and
> $2\beta/(1-\theta)+64\eta^2<1$ (forcing $\eta<1/8$), the pair (21)+(22) feeds
> `cor:tight-window-consumption`, and a constant (non-$O(T)$) supply also suffices. The screened
> supply is proved for $J$-measurable cuts on split products in total-budget form
> $(2k+64\eta^2(1+k))/\kappa$, and in general reduces, modulo the certified $O(T)$ excess layer,
> to the aligned initial-layer estimate
> $\mathbb E\int_0^{t_*\wedge T\wedge\tau_\eta}Q_t\mathbf 1_{\{Q_t\ge\kappa e_tW_{\rm cut}\}}dt\le CT$
> with $\kappa<\kappa_{\rm TT}\approx0.549$; its relation to the tight-prefix trace estimate is a
> trace-cluster comparison owned by the synthesizer, and no localized-profile lower bound may be
> inserted.

## 9. Proposed ledger delta

One new candidate node for the result actually established at sketch level (open until a prover
dossier and a distinct cold review):

```yaml
- id: prop:split-screened-supply
  kind: proposition
  status: open
  route: eldan-localization
  file: modules/kls/27-eldan-open-targets.tex
  statement: "For a product of isotropic one-dimensional log-concave laws, a J-measurable cut with |J|=k and 0<p_0<1, every eta in (0,1/4], kappa>0, and every T>0, the screened weighted excess satisfies E int_0^{T wedge tau_eta} e_t (1+lambda_cut(A_t,K_t))^(5/2) 1{Q_t >= kappa e_t W_cut} dt <= (2k+64 eta^2 (1+k))/kappa, uniformly in the ambient dimension and in every spectator coordinate. Total-budget form, not proportional to T."
  depends_on: [lem:stein-vs-source, thm:budget, lem:block, thm:scalar-riccati, lem:lyapunov-stein-duality, prop:trivial-excess]
  bounded_by: [obs:two-tail, obs:circularity]
```

No `proved`, `refuted`, `solution`, or `checked_by` field is proposed. No change to the status of
`q:weighted` or to any trace-cluster node is proposed. The Section 1 audit and Section 3.2
reduction are recorded here as reusable arguments; they can enter the ledger only inside the
future dossier's body or as later candidates if the orchestrator prefers explicit nodes.

```yaml
outcome: complete
artifacts:
  - research/explorations/2026-08-30-kls-route-prober-weighted-screened-interface-w4w01.md
proposed_deltas:
  - "Add candidate node prop:split-screened-supply exactly as displayed in Section 9; do not change q:weighted status."
  - "Update the q:weighted gate paragraph with the one-line text of Section 8 (route-control, orchestrator-owned)."
  - "Route the Section 3.2 collapse comparison (aligned initial-layer kernel vs ass:tight-prefix-carleson) to the synthesizer as a trace-cluster question; this probe deliberately does not decide it."
next_role: prover
next_prompt: |
  Write a standalone dossier proving prop:split-screened-supply from certified inputs only.
  Statement: for a product of isotropic one-dimensional log-concave measures, a cut E measurable
  with respect to a fixed coordinate set J with |J|=k and 0<p_0<1, every eta in (0,1/4], every
  kappa>0, and every T>0,
  E int_0^{T wedge tau_eta} e_t (1+lambda_cut(A_t,K_t))^{5/2} 1{Q_t >= kappa e_t W_cut} dt
  <= (2k + 64 eta^2 (1+k))/kappa, with Q_t = s_t ||K_t||_HS^2 and the lambda_cut(A,0)=0
  convention of solutions/lem-lyapunov-stein-duality.tex. Proof plan: (1) pointwise on the
  aligned set, e_t W_cut <= Q_t/kappa, including the K_t=0 degenerate case; (2) on {t<tau_eta}
  with eta<=1/4, s_t>=3/16>=1/8, apply the second inequality of lem:stein-vs-source to get
  Q_t <= 2 S_t + 64 eta^2 D_t; (3) apply lem:block pathwise to (mu_t,E) and thm:budget part (i)
  (whose dossier audit records that it needs only 0<p_0<1) for E int_0^infty S_t dt <= k;
  (4) integrate thm:scalar-riccati at the localizing stopping times of the certified
  kls-localization-riccati-core dossier, discard E r >= 0, use r_0 <= 1, to get
  E int_0^{T wedge tau_eta} D_t dt <= 1 + k; (5) combine by Tonelli and monotone convergence.
  Adopt the measurability conventions of Section 5 of
  research/explorations/2026-08-30-kls-route-prober-weighted-screened-interface-w4w01.md:
  augmented filtration, regular compact-smooth class, progressive measurability of the screened
  indicator via Borel lambda_cut on supported pairs, no Ito calculus on the weight. State
  explicitly that the bound is total-budget (uniform in T, dimension, and spectators), is not of
  the form C(k)T, and asserts nothing about the trace-upgrade cluster. Optionally include, as a
  separately stated lemma with its own proof, the constant-supply extension of
  cor:tight-window-consumption (Gronwall with an additive constant) used by the consumption
  audit in Section 1 of the same exploration; keep it clearly separate from the proposition.
  Do not edit ledger.yaml, routes.md, gating.md, or any module file.
```
