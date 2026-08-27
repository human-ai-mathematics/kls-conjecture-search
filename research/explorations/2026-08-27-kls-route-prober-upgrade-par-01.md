# KLS route probe: the all-cut operator-to-trace upgrade

Date: 2026-08-27

Role: `kls-route-prober`

Concurrency key: `kls-gate:q:upgrade` plus the trace-upgrade `knowledge` reservation

Target: `q:upgrade`

This probe owns only `q:upgrade`. It makes no transfer to `q:stein-weighted` or `q:alignment`
and proposes no edge among those nodes.

## Gate, verbatim

> Produce a uniform absorptive trace estimate that directly discharges
> `ass:all-cut-carleson`, with every source and damping term matched to
> `thm:scalar-riccati`. The estimate must use cut-aware information and handle small-time
> high-rank occupation.

The live ledger statement of `q:upgrade` is:

> Operator-to-trace upgrade: prove `ass:all-cut-carleson` by upgrading
> `cor:per-direction` from quadratic-form to trace scale, uniformly over balanced cuts.

The demanded assumption is the following exact interval estimate. There must be universal
$T_0,C_0,C_1$ and $\alpha<1$ such that, for every isotropic log-concave initial law, every fixed
balanced cut $E$, every interval $I\subset[0,T_0]$, and the coarse exit time
$\tau=\inf\{t:p_t\notin[1/3,2/3]\}$,

$$
 \mathbb E\int_{I\cap[0,\tau]}S_t\,dt
 \le C_0|I|+C_1\mathbb E\int_{I\cap[0,\tau]}r_t\,dt
       +\alpha\mathbb E\int_{I\cap[0,\tau]}D_t\,dt.
 \tag{AC}
$$

The constants may not depend on the dimension, cut, measure, interval, or approximation.

## Live inputs and dependency closure used here

The exact stochastic layer is already certified in
`solutions/kls-localization-riccati-core.tex`, independently reviewed in
`research/reviews/2026-08-25-kls-core-r2-audit.md`:

- `lem:matrix-riccati` gives
  $dR_t=d\widetilde N_t-(R_t^2+s_tG_t^2)\,dt$ for
  $R_t=A_t-B_t\succeq0$.
- `thm:scalar-riccati` gives
  $dr_t=dM_t+(S_t-D_t)\,dt$, with
  $S_t=s_t\|G_t\|_{\mathrm{HS}}^2$ and
  $D_t=2s_t\delta_t^TA_t\delta_t-r_t^2\ge r_t^2$.
- `cor:per-direction` gives, for every deterministic unit vector $\theta$,
  $$
  \mathbb E\int_0^\infty s_t|G_t\theta|^2\,dt
  \le \theta^TR_0\theta\le1.
  \tag{PD}
  $$
- `lem:pathwise-BL` gives
  $s_t\|K_t\|_{\mathrm{HS}}^2\le4\lambda_{\max}(A_t)/t\le4/t^2$,
  where $K_t=G_t+(q_t-p_t)\delta_t\delta_t^T$.
- `cor:away-from-zero` already closes the source on every fixed positive-time window, in the
  tighter balance convention used by that node.
- `thm:carleson-implies-centroid` and `cor:tight-window-consumption` show that the strict
  inequality $\alpha<1$ is load-bearing: it leaves positive Riccati damping after the source is
  inserted and permits Gronwall and balanced survival.

The Stein/QCTS algebra is certified in
`solutions/kls-qcts-stein-boundary-core.tex`, under the same review, while the actual
dimension-free quadratic Poincare input `thm:letwin-qcts` is imported from an unreviewed
version-1 preprint. Conditional on that import, `cor:qcts-source` gives

$$
 s_t\|A_t^{-1/2}K_tA_t^{-1/2}\|_{\mathrm{HS}}^2\le8.
 \tag{QCTS}
$$

Thus every conclusion below that invokes (QCTS) retains the preprint-conditional status. The
time-weighted Riccati estimate proved below does not use that import.

## Term-by-term decomposition

Fix an interval $I=[a,b]\subset[0,T_0]$ and write
$J=I\cap[0,\tau]$.

- **Source.** $S_t=s_t\|G_t\|_{\mathrm{HS}}^2$ is the complete positive drift in the scalar
  Riccati equation. No column, diagonal, or low-rank surrogate is enough unless the discarded
  entries are separately controlled.
- **Damping.** $D_t=2s_t\delta_t^TA_t\delta_t-r_t^2\ge r_t^2$ is subtracted with coefficient
  one in `thm:scalar-riccati`. Estimate (AC) may spend only a strict fraction $\alpha<1$ of it.
- **Information term.** $r_t=s_t|\delta_t|^2$ is the binary information rate. The certified
  entropy identity gives $\int_0^\infty\mathbb E r_t\,dt\le2\log2$, but this total budget does
  not control arbitrarily short source bursts.
- **Baseline.** $C_0|I|$ must be an interval-density bound. A bound independent of $|I|$, even
  if dimension-free, does not meet the gate.
- **Boundary in stochastic time.** If
  $u(t)=\mathbb E r_{t\wedge\tau}$ and
  $\bar u(t)=\mathbb E[\mathbf1_{\{t<\tau\}}r_t]$, optional stopping in the certified
  regularity convention gives exactly
  $$
  u(b)-u(a)=\mathbb E\int_J(S_t-D_t)\,dt.
  \tag{1}
  $$
  Consequently (AC) is equivalent to the reverse-damping, or anti-burst, estimate
  $$
  u(b)-u(a)+(1-\alpha)\mathbb E\int_JD_t\,dt
  \le C_0(b-a)+C_1\int_a^b\bar u(t)\,dt.
  \tag{2}
  $$
  This identity makes clear why merely integrating the scalar Riccati equation leaves
  coefficient one in front of $D_t$.
- **Approximation boundary.** All calculations first take place for the smooth compactly
  supported approximation used by the certified dossiers. Constants below are independent of
  that approximation; localization, Fatou, and monotone convergence then give the general
  inequalities for nonnegative occupation terms.

## Attack I: exact coarse-window absorption and spectral incidence

### The $G$--$K$ correction spends strictly less than all damping

On the coarse window, $s=pq\ge2/9$ and $|q-p|\le1/3$. For every $\varepsilon>0$,

$$
 \begin{aligned}
 S
 &=s\|K-(q-p)\delta\delta^T\|_{\mathrm{HS}}^2\\
 &\le(1+\varepsilon)s\|K\|_{\mathrm{HS}}^2
 +(1+\varepsilon^{-1})\frac{(q-p)^2}{s}\,r^2.
 \end{aligned}
 \tag{3}
$$

The scalar function $(q-p)^2/(pq)$ is maximized at $p=1/3,2/3$ on this window, where it equals
$1/2$. Taking $\varepsilon=2$ and using $r^2\le D$ gives the pointwise estimate

$$
 \boxed{S_t\le3s_t\|K_t\|_{\mathrm{HS}}^2+\frac34D_t}
 \qquad (t<\tau).
 \tag{4}
$$

This already extends the positive-time estimate to the exact coarse window of (AC): by the
Brascamp--Lieb source bound,

$$
 S_t\le\frac{12}{t^2}+\frac34D_t,
 \qquad t>0,\ t<\tau.
 \tag{5}
$$

Hence for every deterministic $t_*>0$ and every
$I\subset[t_*,T_0]$,

$$
 \mathbb E\int_J S_t\,dt
 \le12t_*^{-2}|I|+\frac34\mathbb E\int_JD_t\,dt.
 \tag{6}
$$

There is no late-time residue. The dependence $t_*^{-2}$ identifies the initial layer as the
only unresolved domain.

### Low covariance is paid; incident-high occupation is the exact remaining tensor

Fix a universal spectral level $L>1$ and let

$$
 P_t^L=\mathbf1_{[0,L]}(A_t),
 \qquad P_t^H=I-P_t^L.
$$

Define the full $K$-energy incident to the random high-covariance space by

$$
 \mathcal H_{t,L}^K
 :=s_t\left(
 \|P_t^HK_tP_t^H\|_{\mathrm{HS}}^2
 +2\|P_t^HK_tP_t^L\|_{\mathrm{HS}}^2
 \right).
 \tag{7}
$$

The factor two retains both high--low matrix entries. There is the exact orthogonal block
decomposition

$$
 s_t\|K_t\|_{\mathrm{HS}}^2
 =s_t\|P_t^LK_tP_t^L\|_{\mathrm{HS}}^2+\mathcal H_{t,L}^K.
 \tag{8}
$$

Conditional on (QCTS), put
$Z_t=\sqrt{s_t}A_t^{-1/2}K_tA_t^{-1/2}$. Then
$\|Z_t\|_{\mathrm{HS}}^2\le8$, and spectral calculus gives

$$
 s_t\|P_t^LK_tP_t^L\|_{\mathrm{HS}}^2
 =\|P_t^LA_t^{1/2}Z_tA_t^{1/2}P_t^L\|_{\mathrm{HS}}^2
 \le8L^2.
 \tag{9}
$$

Combining (4), (8), and (9) gives the pointwise, term-matched reduction

$$
 \boxed{
 S_t\le24L^2+3\mathcal H_{t,L}^K+\frac34D_t
 }
 \qquad (t<\tau).
 \tag{10}
$$

Therefore the following cut-aware estimate would directly discharge (AC): for one universal
$L>1$, prove constants $C_H,C_r$ and $\beta<1/12$ such that for every admissible interval,

$$
 \mathbb E\int_J\mathcal H_{t,L}^K\,dt
 \le C_H|I|+C_r\mathbb E\int_Jr_t\,dt
       +\beta\mathbb E\int_JD_t\,dt.
 \tag{11}
$$

Indeed (10)--(11) give (AC) with

$$
 C_0=24L^2+3C_H,
 \qquad C_1=3C_r,
 \qquad \alpha=\frac34+3\beta<1.
 \tag{12}
$$

For example $L=2$ makes the already-controlled baseline $96|I|$. No estimate in the live graph
proves (11). The fixed-direction budget (PD) cannot be tested against the random adapted
projection $P_t^H$, and it controls $G_t$, not the full incident $K_t$ tensor. Summing (PD) in a
fixed basis recovers only $\operatorname{Tr}R_0\le n$.

The known covariance-moment window controls the full source only through a
dimension-dependent initial interval (conditional on Letwin v1, $t\lesssim1/\log n$), while
(6) controls every interval bounded away from zero. Thus (11) is needed precisely in the band
where covariance-only control has ended but no fixed positive-time cutoff has yet been reached.
It is the small-time high-rank occupation clause of the gate, with all low spectral entries and
all allowed damping already removed.

## Attack II: a universal scale-weighted source budget

There is a dimension-free source estimate available directly from the scalar Riccati equation,
but its quadratic time weight is fatal for (AC).

### Candidate lemma established in this probe

For every isotropic log-concave initial law, every fixed cut with nontrivial mass, and every
$T>0$,

$$
 \boxed{
 \mathbb E\int_0^T t^2\bigl(S_t+r_t^2\bigr)\,dt
 \le T^2\mathbb E r_T\le T.
 }
 \tag{13}
$$

In particular, by positivity, the same upper bound holds when $S_t$ is restricted to any
balanced stopped window.

To prove (13), covariance decomposition gives $B_t\preceq A_t$. Since $B_t$ has rank one and
its nonzero eigenvalue is $r_t$,

$$
 r_t\le\lambda_{\max}(A_t)\le\frac1t,
 \tag{14}
$$

where the last step is the posterior Brascamp--Lieb cap. The same cap gives

$$
 D_t
 =2s_t\delta_t^TA_t\delta_t-r_t^2
 \le\frac{2r_t}{t}-r_t^2.
 \tag{15}
$$

Multiplying `thm:scalar-riccati` by $t^2$ yields

$$
 d(t^2r_t)
 =t^2dM_t+
 \left(2t r_t+t^2S_t-t^2D_t\right)dt.
 \tag{16}
$$

By (15), the drift in (16) is at least
$t^2(S_t+r_t^2)$. Stop the local martingale at bounded levels, take expectations, and let the
levels increase. Fatou applies to the nonnegative left side; (14) bounds the terminal term by
$T^2r_T\le T$. This proves (13), uniformly through the repository's regularization convention.

### Why the time weight cannot be removed by this scalar method

The loss is structural, not an unfortunate choice of multiplier. Let $w\ge0$ be $C^1$ and
multiply the scalar Riccati equation by $w(t)$. If the only upper control on damping is (15),
then making the drift of $w(t)r_t$ dominate $w(t)(S_t+r_t^2)$ requires

$$
 w'(t)\ge\frac{2w(t)}t.
 \tag{17}
$$

Equivalently $(w(t)/t^2)'\ge0$. If $w$ is finite at a positive time, then for all earlier $t$
it satisfies $w(t)\le Ct^2$; in particular $w(0)=0$. Thus every multiplier proof using only
`thm:scalar-riccati` and the pathwise cap $A_t\preceq t^{-1}I$ loses at least a quadratic weight
at the initial endpoint. It cannot yield the unweighted interval density in (AC).

The estimate (13) is nevertheless informative: it proves that large two-tail-type source at
time $t$ is affordable only at heat scale $t^{-2}$, but it gives no upper Lipschitz control on
how the resulting budget is distributed among short intervals or covariance directions. That
deweighting is exactly the missing cut-aware occupation input, not a remaining Ito calculation.

## Exact residue

- **Needs new idea — first unsupported step.** Prove the incident-high estimate (11), or an
  equally strong cut-aware alternative, on a universal window. It must retain tensor
  orientation, work for every fixed balanced cut, and leave damping coefficient
  $\beta<1/12$ in the normalization (7). No live node supplies it.
- **Needs new idea — initial-time deweighting.** Upgrade (13) from $t^2S_t\,dt$ to an
  unweighted interval-density estimate. The multiplier calculation (17) proves that the scalar
  Riccati identity plus the Brascamp--Lieb cap cannot do this by themselves.
- **Fenced — adaptive summation of per-direction budgets.** Replacing $P_t^H$ in (7) by the
  currently large eigenspace and summing (PD) is invalid: (PD) tests deterministic directions,
  while $P_t^H$ is random and correlated with the source. Abstractly, orthogonal directions can
  spend their unit budgets sequentially, leaving the occupation operator bounded by $I$ but its
  trace of order $n$.
- **Fenced — slice-wise high-state control.** Bounding $\mathcal H_{t,L}^K$ at each posterior by
  an absolute-scale excess term is contradicted by `obs:two-tail`. Such states must be controlled
  through their expected occupation, not declared pointwise harmless.
- **Fenced — cut-free covariance substitution.** Replacing (11) by a universal relative-scale
  bound on $\int\lambda_{\max}(A_t)\,dt$ invokes the mechanism of `obs:relative-ceiling`, which
  is already KLS-sufficient and is not a weaker input to this gate.
- **Technical/epistemic gap.** The clean low/high reduction (9)--(12) uses
  `thm:letwin-qcts`, currently an unreviewed preprint import. Without that import, the live
  projection technology pays the logarithm fenced by `obs:proj-ceiling`. This does not affect
  the unconditional candidate lemma (13).

The stopping convention, the $G$--$K$ correction, the low spectral block, the positive-time
domain, and the regularization limit leave no additional residue in the displayed reductions.

## Fence-by-fence evasion check

### `obs:proj-ceiling`

The low block in (9) uses the full matrix quadratic-Poincare input (QCTS), not radial or
projection tests. The random incident-high tensor is retained explicitly in (7) rather than
estimated by a union of projections. The argument therefore respects the fence; it also shows
exactly where the proof stops if the full tensor input is unavailable.

### `obs:two-tail`

No slice-wise absolute-scale estimate is asserted. In the anisotropic two-tail configuration,
$r=D=0$ and the large source lies in $\mathcal H_{t,L}^K$ once the long covariance direction
exceeds $L$, so (10) does not hide the obstruction in its baseline or damping. Estimate (13)
allows a source of order $t^{-2}$ and only constrains its scale-weighted occupation, which is
consistent with the fence.

### `obs:relative-ceiling` on `ass:all-cut-carleson`

No all-measure bound on $\Xi_T$ or $\int\lambda_{\max}(A_t)\,dt$ is inserted. The unresolved
quantity (7) is indexed by the fixed cut through $K_t$ and by the contemporaneous tensor
orientation. Thus the reduction remains cut-aware and does not assume the route's conclusion in
cut-free form.

The remaining obstruction registry does not bind `q:upgrade` or `ass:all-cut-carleson`, but it
was checked for accidental use: no crude $\Xi_T\lesssim\log n$ bootstrap is used
(`obs:crude-insufficient`), no localized profile is inserted (`obs:circularity`), and no
single-coordinate product witness is claimed (`obs:rank-one-refuted`).

## Numerical disposition

No `finum` handoff is proposed. The permitted `kls-align` target concerns one designated product
family and cannot certify the all-measure, all-cut estimate (11). This probe produced neither an
analytic counterexample family nor a fixed universal refuting threshold. A finite interval/seed
sweep would therefore be directional only and would not discriminate the gate.

## Route viability and proposed gate text

The all-cut route remains viable, but this probe does not discharge it. It removes three pieces
from the live uncertainty: the exact coarse-window $G$--$K$ absorption margin, the complete low
spectral block, and every fixed positive-time interval. It also supplies the unconditional
scale-weighted budget (13) and proves why that scalar estimate cannot be deweighted at time zero.
The surviving task is one cut-aware incident-high occupation theorem, not another trace of (PD)
or another Brascamp--Lieb estimate.

Proposed one-line gate update for the orchestrator:

> Prove, for one universal $L>1$, the coarse-window incident-high $K$-occupation estimate
> $\mathbb E\int_J\mathcal H_{t,L}^K\le C_H|I|+C_r\mathbb E\int_Jr_t+
> \beta\mathbb E\int_JD_t$ with $\beta<1/12$; conditional on the full intrinsic QCTS input,
> $S_t\le24L^2+3\mathcal H_{t,L}^K+3D_t/4$ then directly discharges
> `ass:all-cut-carleson`. A scalar Riccati/BL argument supplies only the $t^2$-weighted budget
> (13), so the initial layer requires a genuinely cut-aware deweighting mechanism.

## Proposed ledger delta

The following is a candidate node only. It remains `open` until a `prover` writes a standalone
dossier and a distinct `proof-checker` certifies it; this probe proposes no `solution` or
`checked_by` field.

```yaml
- id: lem:time-weighted-source
  kind: lemma
  status: open
  route: eldan-localization
  file: modules/kls/27-eldan-open-targets.tex
  statement: "Scale-weighted all-cut source budget: for every isotropic log-concave initial law, every fixed cut of nontrivial mass, and every T>0, E int_0^T t^2(S_t+r_t^2) dt <= T^2 E r_T <= T; hence the same source bound holds under any balanced stopping."
  depends_on: [thm:scalar-riccati]
```

No status change or new relation is proposed for `q:upgrade`.

```yaml
outcome: blocked
artifacts:
  - research/explorations/2026-08-27-kls-route-prober-upgrade-par-01.md
proposed_deltas:
  - add the open candidate node lem:time-weighted-source exactly as displayed above
  - sharpen the q:upgrade route-control gate with the proposed incident-high statement; do not change its open status
next_role: prover
next_prompt: |
  Write a standalone dossier for the proposed node `lem:time-weighted-source` only. Prove for
  every fixed nontrivial cut that
  `E int_0^T t^2(S_t+r_t^2) dt <= T^2 E r_T <= T` by combining
  `thm:scalar-riccati`, `B_t <= A_t`, the rank-one identity
  `lambda_max(B_t)=r_t`, and the posterior Brascamp--Lieb cap `A_t <= t^{-1}I`.
  Retain the bounded-stopping/Fatou and regularization passage explicitly. State the stopped
  source consequence only by positivity; do not claim that the quadratic time weight can be
  removed, do not claim `q:upgrade`, and do not compare or transfer the result to
  `q:stein-weighted` or `q:alignment`. Compile the dossier and hand it to a distinct
  `proof-checker`; do not edit either ledger, the manuscript, route-control files, or this
  exploration.
```
