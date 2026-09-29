---
---
# KLS route probe: the global weighted-excess gate and exponential spectators

Date: 2026-08-27

Role: `kls-route-prober`

Run id: `w0w01`

Concurrency key: `kls-gate:q:weighted`

Scope: the literal global-operator-norm rate in `q:weighted`. This probe does not address
`q:upgrade`, `q:stein-weighted`, or `q:alignment`, and it asserts no implication among them.

## Gate, quoted verbatim

The active gate in `research/kls/gating.md` is:

> Prove the ledger rate for balanced near-Cheeger cuts with the calibrated
> $(1+\|A_t\|)^{5/2}$ weight. The argument must not insert an unproved lower bound for the
> localized isoperimetric profile.

The manuscript statement at `q:weighted` is
$$
 \mathbb E\int_0^{T\wedge\tau_\eta}
 e_t(E)(1+\|A_t\|_{\mathrm{op}})^{5/2}\,dt
 \le C\bigl(Te_0(E)+T^{1+\gamma}\bigr),
 \qquad T\le T_0. \tag{W}
$$
The constants $C,T_0,\gamma>0$ and the tight-window parameter $\eta\in(0,1/4]$ are to be
universal, uniformly in the dimension, the isotropic log-concave initial measure, and the
initial cut.

### The missing quantifier in the literal statement

Neither the manuscript, ledger, nor gate defines `near-Cheeger`. The only quantitative use in
the existing consumption proof is $e_0\le1$, while the contradiction discussion also speaks of
sequences with $e_0\to0$. The natural precise interpretations are:

1. additive: $e_0(E)\le\delta$ for a prescribed $\delta>0$;
2. relative: $e_0(E)\le\delta I_\mu(1/2)$;
3. exact: $e_0(E)=0$;
4. one of the preceding conditions together with an additional near-worst-measure condition.

The construction below contradicts (W) for every prescribed additive or relative tolerance,
and therefore in particular for the explicit $e_0\le1$ consumption convention. It does not
claim that the cylinder is an exact minimizer. It also does not satisfy an unstated
near-worst-measure hypothesis. Those two narrower readings would be different gates and must be
written explicitly before being assessed.

## Term-by-term decomposition

For a fixed cylinder cut $E$ under stochastic localization:

| term | demanded role | status before this probe | disposition here |
|---|---|---|---|
| $p_t=\mu_t(E)$ and $\tau_\eta$ | retain balance on the interval of integration | mass martingale and continuous paths are certified | made entirely base-measurable and kept in the window on a fixed positive-probability base event |
| $P_t=\mu_t^+(E)$ | positive part of $e_t=P_t-I_{\mu_t}(p_t)$ | perimeter martingale is certified, but gives no pathwise lower bound | bounded below for all $t\le T_b$ on the same base event by continuity of a weighted finite-perimeter measure under a small tilt |
| $I_{\mu_t}(p_t)$ | moving posterior profile | no usable lower bound because of `obs:circularity` | upper-bounded by an explicit spectator-coordinate $p_t$-quantile half-line |
| $e_t(E)$ | absolute profile excess | nonnegative by definition | bounded below by a fixed fraction of the base perimeter when a spectator variance is large |
| $\|A_t\|_{\mathrm{op}}^{5/2}$ | calibrated covariance weight | Brascamp--Lieb only gives the cap $t^{-5/2}$ | a centered-exponential spectator attains size $c\,t^{-5/2}$ with fixed probability |
| $Te_0$ | transports initial near-minimality | harmless if $e_0$ is small | the cylinder has arbitrarily small additive and relative $e_0$, uniformly in every later spectator dimension |
| $T^{1+\gamma}$ | demanded superlinear initial-layer rate | open | contradicted by a lower bound of order $T^{-3/2}$ after the dimension is chosen as $N\simeq e^{2/T}$ |

The failure is not caused by the cut itself having dangerous covariance. It is caused by the
global weight charging covariance spikes in independent coordinates that the cut does not use.

## Input 1: near-minimal cylinders survive every later spectator extension

Let $\lambda$ be the law of $Y-1$ for $Y\sim\operatorname{Exp}(1)$. It is centered, has variance
one, and is one-sided exponential. Put
$$
 a_d:=I_{\lambda^{\otimes d}}(1/2).
$$
Cylinder extension gives $a_{d+1}\le a_d$: any half-volume competitor in $\mathbb R^d$ extends
to one in $\mathbb R^{d+1}$ with unchanged mass and perimeter. Moreover the certified product
bound `prop:products`, combined with `lem:half`, gives
$$
 a_d=\frac12h_{\lambda^{\otimes d}}\ge a_*>0
$$
for a universal $a_*$. Hence $a_d\downarrow a_\infty$ with $a_\infty\ge a_*>0$.

Fix $\varepsilon>0$. Choose a finite $M$ with
$$
 a_M-a_\infty\le\varepsilon
$$
and a finite-perimeter set $E_0\subset\mathbb R^M$ such that
$$
 \lambda^{\otimes M}(E_0)=\frac12,
 \qquad
 P_0:=P_{\lambda^{\otimes M}}(E_0)\le a_M+\varepsilon. \tag{1}
$$
The usual weighted-BV approximation permits the competitor to be taken in the repository's
regularity convention without changing the right side by more than another arbitrarily small
amount.

For every integer $N\ge1$, define
$$
 \mu^{M,N}:=\lambda^{\otimes M}\otimes\lambda^{\otimes N},
 \qquad
 E^{M,N}:=E_0\times\mathbb R^N.
$$
Then $\mu^{M,N}$ is isotropic and log-concave, the cylinder has mass $1/2$ and perimeter $P_0$,
and
$$
 \begin{aligned}
 0\le e_0(E^{M,N})
 &=P_0-a_{M+N}\\
 &\le P_0-a_\infty
 \le2\varepsilon. \tag{2}
 \end{aligned}
$$
This estimate is uniform in every $N$ chosen later. Since $a_{M+N}\ge a_\infty>0$, it also gives
$$
 \frac{e_0(E^{M,N})}{I_{\mu^{M,N}}(1/2)}
 \le\frac{2\varepsilon}{a_\infty}. \tag{3}
$$
Thus the same cylinders are arbitrarily near-minimal in both the additive and relative senses.
This proves the required convergence of the half-profile constants and, crucially, fixes the
base block before the time and spectator dimension are selected.

## Input 2: exact product localization and independence

Use the planted filtering realization. Split
$$
 X=(X^0,X^1,\ldots,X^N),
 \qquad
 B=(B^0,\beta_1,\ldots,\beta_N),
$$
where $X^0\sim\lambda^{\otimes M}$, the $X^i\sim\lambda$, and all latent and Brownian blocks are
independent.
The localization parameter is
$$
 c_t=tX+B_t.
$$
The posterior normalizer factorizes, so pathwise
$$
 \mu_t=\nu_t^0\otimes\bigotimes_{i=1}^N\lambda_{i,t},
 \qquad
 A_t=\operatorname{diag}(A_t^0,v_{1,t},\ldots,v_{N,t}), \tag{4}
$$
where $v_{i,t}=\operatorname{Var}(\lambda_{i,t})$. The base posterior process is independent of
all spectator posterior processes. For the cylinder,
$$
 p_t=\nu_t^0(E_0),
 \qquad
 P_t=P_{\nu_t^0}(E_0), \tag{5}
$$
because
$\operatorname{dist}((x,z),E_0\times\mathbb R^N)=\operatorname{dist}(x,E_0)$. In particular,
$\tau_\eta$ is base-filtration measurable and independent of every fixed-time spectator spike
event.

This is stronger than merely saying that $A_t$ is block diagonal: it supplies the independence
needed to multiply a base survival event by the Klartag--Lehec fixed-time event.

## Input 3: a common stopping-window and perimeter-stability event

The following elementary lemma supplies the part not contained in the perimeter-martingale
identity.

### Base stability lemma

Let $\nu$ be a full-dimensional log-concave probability on $\mathbb R^M$, and let $E_0$ have
$\nu(E_0)=1/2$ and finite positive weighted perimeter $P_0$. For every
$\eta\in(0,1/2)$, there are $T_b>0$ and a base-block event $G_b$ in the planted realization with
$\mathbb P(G_b)\ge1/4$ such that, simultaneously for all $0\le t\le T_b$,
$$
 |\nu_t(E_0)-1/2|<\eta,
 \qquad
 P_{\nu_t}(E_0)\ge\frac{P_0}{8}. \tag{6}
$$
Consequently $\tau_\eta>T_b$ on $G_b$.

### Proof with explicit domains

For deterministic tilt parameter $u$, write
$$
 F_{u,t}(x)
 =\frac{\exp(u\cdot x-t|x|^2/2)}
 {Z(u,t)},
 \qquad
 Z(u,t)=\int\exp(u\cdot x-t|x|^2/2)\,d\nu(x). \tag{7}
$$
Log-concavity supplies a local exponential moment. Choose $R$ so that the finite weighted
perimeter measure $\sigma_{E_0}$ satisfies
$$
 \sigma_{E_0}(B_R)\ge P_0/2.
$$
Choose small $a,\bar T>0$ such that
$$
 \int e^{a|x|}\,d\nu(x)\le2,
 \qquad
 aR+\frac{\bar T R^2}{2}\le\log2, \tag{8}
$$
and
$$
 \sup_{|u|\le a,\ 0\le t\le\bar T}
 \|F_{u,t}-1\|_{L^1(\nu)}<\eta. \tag{9}
$$
The uniform convergence in (9) follows by dominated convergence using a slightly larger local
exponential moment.

Choose $L$ with $\nu(B_L)\ge1/2$ and then choose
$$
 T_b\le
 \min\left\{
 \bar T,\frac{a}{2L},\frac{a^2}{8M\log(8M)}
 \right\}. \tag{10}
$$
For $c_t^0=tX^0+B_t^0$, set
$$
 G_b={|X^0|\le L\}
 \cap
 \left\{
 \max_{1\le j\le M}\sup_{s\le T_b}|B_s^{0,j}|
 \le\frac{a}{2\sqrt M}
 \right\}. \tag{11}
$$
The reflection principle and a union bound give
$$
 \mathbb P\left(
 \max_j\sup_{s\le T_b}|B_s^{0,j}|>\frac{a}{2\sqrt M}
 \right)
 \le4M\exp\left(-\frac{a^2}{8MT_b}\right)\le\frac12.
$$
Independence of $X^0$ and $B^0$ therefore yields $\mathbb P(G_b)\ge1/4$. On $G_b$,
$|c_s^0|\le a$ for every $s\le T_b$. Equation (9) gives the mass window in (6). On
$\partial^*E_0\cap B_R$, equations (7)--(8) give
$$
 F_{c_s^0,s}(x)
 \ge\frac{e^{-aR-T_bR^2/2}}{\int e^{a|y|}\,d\nu(y)}
 \ge\frac14.
$$
The weighted finite-perimeter density-change formula now gives
$$
 P_{\nu_s}(E_0)
 =\int F_{c_s^0,s}\,d\sigma_{E_0}
 \ge\frac14\sigma_{E_0}(B_R)
 \ge\frac{P_0}{8}.
$$
This proves (6). The compact-smooth version is immediate; the displayed weighted-BV formula is
the precise general regularization step a dossier should retain.

## Input 4: the fixed-time spectator spike and the profile competitor

Klartag--Lehec, Proposition 65 in the published lecture notes (accessible as
[arXiv:2406.01324v2](https://arxiv.org/html/2406.01324v2)), uses $Y_i=1+X_i\sim\operatorname{Exp}(1)$
and proves the following event-level estimate for Gaussian-channel noise variance $s$:
$$
 \mathbb P\left(
 \left\|\operatorname{Cov}(X\mid X+\sqrt sG)\right\|_{\mathrm{op}}
 \ge c_{\mathrm{sp}}s
 \right)
 \ge1-\left(1-\frac12e^{-s}\right)^N. \tag{12}
$$
Indeed, for one coordinate,
$$
 \operatorname{Var}(X_i\mid X_i+\sqrt sG_i)
 =s\,v\left(\sqrt s-\frac{Y_i}{\sqrt s}-G_i\right),
$$
and the event $\{Y_i\ge s,G_i\ge0\}$ has probability $e^{-s}/2$ and makes the argument of
$v$ nonpositive. Thus $c_{\mathrm{sp}}=\inf_{u\le0}\operatorname{Var}(G\mid G\ge u)>0$ is
admissible. The source has a typographical loss of the factor $s$ in the expectation line after
this event computation; (12), rather than that line, is the input used here.

The repository localization time is exactly $t=1/s$. Therefore, with
$$
 H_t:=\left\{\max_{1\le i\le N}v_{i,t}\ge\frac{c_{\mathrm{sp}}}{t}\right\},
$$
equation (12) gives
$$
 \mathbb P(H_t)
 \ge1-\left(1-\frac12e^{-1/t}\right)^N. \tag{13}
$$
If $\log N\ge2/T$, then for every fixed $t\in[T/2,T]$,
$$
 \mathbb P(H_t)\ge h_{\mathrm{sp}}:=1-e^{-1/2}>0. \tag{14}
$$
No persistent-in-time spike event is claimed or needed.

On $H_t$, choose an index $i$ with $v_{i,t}\ge c_{\mathrm{sp}}/t$, and choose a half-line in
that spectator coordinate having mass exactly $p_t$. Bobkov--Chistyakov's sharp
density--variance inequality gives, for every one-dimensional log-concave density $f$ of
variance $v$,
$$
 \|f\|_\infty\le v^{-1/2}.
$$
The corresponding cylinder is therefore an explicit profile competitor of mass $p_t$ and
perimeter at most
$$
 I_{\mu_t}(p_t)\le\sqrt{\frac{t}{c_{\mathrm{sp}}}}. \tag{15}
$$
This works for the actual random $p_t$, not only for mass $1/2$.

## The contradiction with the claimed rate

Fix arbitrary proposed constants $C,T_0,\gamma>0$ and $\eta\in(0,1/2)$, and fix any requested
additive or relative near-Cheeger tolerance. First choose $\varepsilon$, then $M,E_0$ as in
(1)--(3), small enough to meet that tolerance. This fixes $P_0>0$ and the base-stability time
$T_b$ before any spectators are appended.

Now choose $T>0$ so small that
$$
 T\le\min\left\{T_0,T_b,\frac{c_{\mathrm{sp}}P_0^2}{256},1\right\}. \tag{16}
$$
Only after $T$ is fixed, choose a finite $N$ with $\log N\ge2/T$. For every deterministic
$t\in[T/2,T]$, on $G_b\cap H_t$, equations (6) and (15) give
$$
 t<\tau_\eta,
 \qquad
 e_t(E^{M,N})
 \ge\frac{P_0}{8}-\sqrt{\frac{t}{c_{\mathrm{sp}}}}
 \ge\frac{P_0}{16}, \tag{17}
$$
and (4) gives
$$
 (1+\|A_t\|_{\mathrm{op}})^{5/2}
 \ge c_{\mathrm{sp}}^{5/2}t^{-5/2}. \tag{18}
$$
The events $G_b$ and $H_t$ are independent. Tonelli, used separately at each deterministic time,
therefore yields
$$
 \begin{aligned}
 &\mathbb E\int_0^{T\wedge\tau_\eta}
 e_t(E^{M,N})(1+\|A_t\|_{\mathrm{op}})^{5/2}\,dt\\
 &\quad\ge
 \frac{P_0h_{\mathrm{sp}}c_{\mathrm{sp}}^{5/2}}{64}
 \int_{T/2}^Tt^{-5/2}\,dt\\
 &\quad=
 \kappa_{\mathrm{sp}}P_0T^{-3/2}, \tag{19}
 \end{aligned}
$$
where
$$
 \kappa_{\mathrm{sp}}
 :=\frac{h_{\mathrm{sp}}c_{\mathrm{sp}}^{5/2}}{96}
 (2^{3/2}-1)>0.
$$

Since $0\le e_0(E^{M,N})\le P_0$, shrink $T$ further, still before choosing $N$, so that
$$
 T^{5/2}<\frac{\kappa_{\mathrm{sp}}}{2C},
 \qquad
 T^{\gamma+5/2}<\frac{\kappa_{\mathrm{sp}}P_0}{2C}. \tag{20}
$$
Then
$$
 C\bigl(Te_0+T^{1+\gamma}\bigr)
 <\kappa_{\mathrm{sp}}P_0T^{-3/2},
$$
contradicting (W). The complete quantifier order is
$$
 (C,T_0,\gamma,\eta,\text{near tolerance})
 \longrightarrow (M,E_0,P_0,T_b)
 \longrightarrow T
 \longrightarrow N.
$$
There is no return from $N$ to the base, because (2)--(3) are uniform in all later dimensions.

## What is established

The preceding argument gives the following dossier-ready statement.

> **Exponential-spectator obstruction.** For every $C,T_0,\gamma>0$,
> $\eta\in(0,1/2)$, and $\delta>0$, there are a dimension $d$, an isotropic log-concave product
> of centered one-sided exponentials $\mu$ on $\mathbb R^d$, a cylinder $E$ with
> $\mu(E)=1/2$ and both $e_0(E)\le\delta$ and
> $e_0(E)/I_\mu(1/2)\le\delta$, and a time $0<T\le T_0$ such that
> $$
> \mathbb E\int_0^{T\wedge\tau_\eta}
> e_t(E)(1+\|A_t\|_{\mathrm{op}})^{5/2}\,dt
> >C\bigl(Te_0(E)+T^{1+\gamma}\bigr).
> $$

The result refutes the global-operator-norm rate for every standard additive or relative meaning
of an initial near-minimizer. It does not refute KLS: the witness measures are products and
satisfy dimension-free KLS by tensorization.

## Residue

1. **Technical gap (routine dossier layer):** formalize the selection of the approximate
   half-profile competitor in the weighted finite-perimeter class and the density-change formula
   under the repository's compact-smooth approximation convention. The displayed base lemma
   identifies the exact formula and domains; no new inequality is missing.
2. **Semantic gap:** `near-Cheeger` is undefined in the current gate. The theorem covers arbitrary
   additive and relative tolerances, including $e_0\le1$, but not the exact-minimizer-only reading.
3. **Needs a different gate, not a repair of this proof:** an additional near-worst-measure
   restriction is absent from (W). If intended, it must be stated and its role in consumption
   re-audited. The product witness is not asserted to meet it.
4. **Control-plane gap:** the event-level form of `prop:covariance-spike` and the sharp
   one-dimensional density--variance lemma have published sources but are not yet ledger nodes.
   The accompanying literature report supplies exact import and bibliography deltas.

There is no remaining stochastic persistence gap: the proof uses only fixed-time events and
Tonelli.

## Fence-by-fence check

### `obs:two-tail`

Respected. The argument retains the required $5/2$ exponent. In fact that calibrated global
weight is exactly what makes independent spectators fatal: the cut remains in the base block,
while an unrelated covariance spike contributes $t^{-5/2}$. The obstruction says that an aligned
two-tail mode needs this power; the present construction says the power cannot be charged through
the global operator norm.

### `obs:circularity`

Evaded. No lower bound on the random posterior profile is inserted, and no moving-family
supermartingale is claimed. Equation (15) is an upper bound supplied by an explicit posterior
spectator half-line of the exact random mass $p_t$.

### Other named fences

`obs:proj-ceiling`, `obs:crude-insufficient`, `obs:relative-ceiling`, and
`obs:rank-one-refuted` are not used or contradicted. The construction contains no projection-only
quadratic-chaos step, no covariance bootstrap, no all-measure relative bound, and no claim about
the trace-upgrade cluster.

## Route viability and proposed gate text

The literal `q:weighted` rate is a refutation candidate, and the weighted package cannot retain
the global operator-norm weight unchanged. This does not kill the near-Cheeger geometric idea. It
identifies a tensor-instability requirement for any replacement.

Proposed one-line gate update for the orchestrator:

> First certify the centered-exponential spectator-cylinder refuter of the literal global-weight
> rate. Any replacement must either state and exploit an explicit near-worst-measure hypothesis,
> or use a cut-local, tensor-stable covariance weight that ignores independent spectators while
> still dominating the aligned two-tail mode.

No corrected cut-local weight is established in this probe.

## Proposed ledger delta

After the two published input nodes proposed by the literature scout are imported, add the
following candidate anchor. It remains open until a prover writes a dossier and a distinct
proof-checker passes it.

```yaml
- id: prop:weighted-spectator-obstruction
  kind: proposition
  status: open
  route: eldan-localization
  file: modules/kls/27-eldan-open-targets.tex
  statement: "For every proposed universal weighted-excess constants and every additive or relative near-Cheeger tolerance, a balanced cylinder in a sufficiently high product of centered one-sided exponentials violates the q:weighted global-operator-norm rate; the lower bound is c P0 T^(-3/2) with the base chosen before T and N."
  depends_on: [prop:covariance-spike, lem:one-dimensional-density-variance, prop:products, lem:half]
```

No `proved`, `refuted`, `solution`, `checked_by`, or `refuted_by` delta is proposed at the probe
stage. If the dossier and cold review pass, the orchestrator can then apply the atomic refutation
transition to `q:weighted` under the sharpened additive/relative statement.

```yaml
outcome: complete
artifacts:
  - research/explorations/2026-08-27-kls-route-prober-weighted-spectator-w0w01.md
proposed_deltas:
  - "Add candidate prop:weighted-spectator-obstruction with the exact statement and dependencies displayed above; do not change q:weighted status before proof and cold review."
  - "Replace the q:weighted gate by the displayed tensor-stability/refutation text after resolving the near-Cheeger quantifier explicitly."
next_role: prover
next_prompt: |
  Write a standalone refutation dossier for the literal q:weighted global-operator-norm rate.
  Prove the monotone convergence of a_d=I_{lambda^d}(1/2) for centered one-sided exponential
  products and use certified product KLS to keep its limit positive; choose the base near-minimizer
  before T and N. Prove product posterior independence and the finite-perimeter base event keeping
  tau_eta>T and perimeter at least P0/8. Import Klartag--Lehec Proposition 65 only in its
  fixed-time event form with exact conversion s=1/t, and use the Bobkov--Chistyakov density bound
  to construct a spectator p_t-quantile profile competitor. Integrate by Tonelli and preserve the
  quantifier order base -> T -> N. Treat the weighted-BV/compact-smooth regularization explicitly.
  State that the result refutes the global weighted gate, not KLS, and do not claim a persistent
  spike event. Use prop:weighted-spectator-obstruction as the candidate node; do not edit the
  ledger, route-control files, or manuscript.
```
