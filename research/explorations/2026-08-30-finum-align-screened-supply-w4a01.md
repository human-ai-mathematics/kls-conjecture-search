---
---
# finum: cut-local screened supply on the product tail-union model (`kls-screen`)

Date: 2026-08-30

Role: `finum`

Run id: `w4a01`

Concurrency keys held: `finum-code`, `exploration:research/explorations/2026-08-30-finum-align-screened-supply-w4a01.md`

Requested by the orchestrator to feed prober `w4w01` on `conj:weighted-excess-rate`. Everything below is
**directional research evidence**. No ledger status, dossier, manuscript statement, or proof step
is affected. `CLAUDE.md` constraint 2 applies to every number here.

## 1. What was asked

Extend the `kls-align` machinery, or add a sibling target, so that along the same
isotropic-Laplace-product tail-union localization paths one can read off

1. cut-scale trajectories $\lambda_{\rm cut}(A_t,K_t)$, $W_{\rm cut}=(1+\lambda_{\rm cut})^{5/2}$
   and $\lambda_{\max}(A_t)$, with $K_t=G_t+(q_t-p_t)\delta_t\delta_t^T$ evaluated exactly through
   its diagonal-plus-rank-one structure;
2. a surrogate excess $\hat e_t=P_t-\hat I_t$, with $P_t$ the exact weighted perimeter of the cut
   and $\hat I_t$ a competitor-based profile bound;
3. screening observables $Q_t=s_t\|K_t\|_{\rm HS}^2$, the aligned indicator
   $\mathbf1\{Q_t\ge\kappa\hat e_tW_{\rm cut}\}$, the aligned supply, the complement source
   fraction $\hat\theta(\kappa,I)$, and the plain supply;
4. a joint-occurrence diagnostic between a large cut scale and a large excess;
5. a spectator cylinder control $E=\{\max_{i\le n_0}|x_i|\ge a\}\times\mathbb R^{n-n_0}$.

A **sibling target `kls-screen`** was built. `kls-align` is untouched; a regression test asserts
that its gate set and record schema are unchanged.

## 2. Restatement, and one correction to the brief

### 2.1 The cut tensor is exactly diagonal plus rank one

In the product model $A_t=\operatorname{diag}(A_1,\dots,A_n)$, and with
$\delta_i=(m_i-u_i)/p$, $d_i=(A_i-w_i)/p$ the pre-existing engine's $G=\operatorname{diag}(d)-q\delta\delta^T$
satisfies $G=\operatorname{Cov}(\mu_E)-\operatorname{Cov}(\mu_F)$. Hence
$$
 K=G+(q-p)\delta\delta^T=\operatorname{diag}(d)-p\,\delta\delta^T,
 \qquad
 K_{ii}=\kappa_i:=d_i-p\delta_i^2,\quad K_{ij}=-p\delta_i\delta_j\ (i\ne j).
$$
Writing $g_i=\delta_i^2$ and $a_i=A_i$, the two scalars in $\lambda_{\rm cut}$ split exactly as
$$
 \|K\|_{\rm HS}^2=\sum_i\kappa_i^2+p^2\Bigl[\bigl(\textstyle\sum_ig_i\bigr)^2-\sum_ig_i^2\Bigr],
 \tag{D1}
$$
$$
 \langle K,\mathscr L_A^{-1}K\rangle
 =\sum_i\frac{\kappa_i^2}{a_i}
 +2p^2\Bigl[C(g,a)-\tfrac12\sum_i\frac{g_i^2}{a_i}\Bigr],
 \qquad
 C(g,a)=\sum_{i,j}\frac{g_ig_j}{a_i+a_j}.
 \tag{D2}
$$
(D1) is $O(n)$. **(D2) is not reducible to $O(n)$**: the cross term is a Cauchy-kernel quadratic
form which genuinely couples all pairs and has no closed form in the $a_i$. It is evaluated
*exactly* in blocks over the support $\{g_i>0\}$, at $O(|\{g_i>0\}|^2)$ cost — which for a
cylinder cut is $O(n_0^2)$, not $O(n^2)$. This is stated because the brief asked for an $O(n)$
analytic split; the honest split is $O(n)$ diagonal plus an exact $O(n^2)$ Cauchy form.
Oracle test: agreement with the dense $n=8$ double sum to $2.2\cdot10^{-16}$ relative.

### 2.2 The surrogate excess UNDERSTATES the excess (brief had the sign inverted)

The brief stated that a competitor-based $\hat I_t$ is "an UPPER bound on the profile, so
$\hat e_t\ge e_t$ ... OVERSTATES excess". The first half is right, the conclusion is inverted:
$$
 \hat I_t\ \ge\ I_{\mu_t}(p_t)
 \quad\Longrightarrow\quad
 \hat e_t=(P_t-\hat I_t)_+\ \le\ P_t-I_{\mu_t}(p_t)=e_t .
$$
Consequences, all recorded in the artifacts and in the module docstring:

* $\int\hat e_tW_{\rm cut}\,dt\le\int e_tW_{\rm cut}\,dt$: every supply reported is a **lower
  bound** for the true supply;
* $\hat{\mathcal A}_\kappa=\{Q\ge\kappa\hat eW\}\supseteq\mathcal A_\kappa$, so
  $\hat\theta(\kappa)\le\theta(\kappa)$: every complement fraction reported is a **lower bound**.

Therefore **growth is the robust direction and boundedness is the weak direction**: a surrogate
supply that grows in $n$, or a surrogate $\hat\theta$ approaching one, is directional evidence
against; a bounded surrogate supply or $\hat\theta=0$ is only weakly consistent with Candidate B.
The pre-registered "directional support" branch is, for this reason, epistemically much weaker
than the "directional against" branch. This was fixed before the runs and is written into the
artifacts.

### 2.3 The requested half-line competitor family is inadmissible on its own

Exact closed form, verified two ways (see gate `perimeter_vs_minkowski_finite_difference`):
for the balanced tail-union cut at $t=0$,
$$
 P_0=\frac{n\sqrt2}{2}\bigl(2^{1/n}-1\bigr)
 \ \searrow\ \frac{\sqrt2\ln2}{2}=0.4901\ldots,
 \qquad
 P_0<\frac1{\sqrt2}=0.7071\ldots\ \text{for }n\ge2,
$$
with equality at $n=1$. The right-hand side is exactly the weighted perimeter of *every*
coordinate half-space at mass $1/2$. So the balanced tail-union cut has strictly smaller
perimeter than any coordinate half-space, the half-line family gives $P_0-\hat I^{\rm hl}_0<0$,
and the "excess" against half-lines alone is a negative number for the very cut being studied.

The requested family is therefore implemented and reported, but a second competitor family was
added: the **equal-per-coordinate-tail product box** of matching mass, which at $t=0$ *is* the cut
and gives $\hat e_0=0$ exactly. The screening uses
$\hat I^{\rm rich}=\min(\hat I^{\rm hl},\hat I^{\rm eq})$. Empirically the two coincide for every
$t>0$ on every path: the half-line family wins immediately once a single coordinate acquires an
extreme tilt.

## 3. Pre-registered decision values (fixed in code before any run)

Emitted verbatim as `screen-preregistration` and inside `_provenance.config`; the module constant
`PREREGISTERED_DECISION` in `experiments/finum/targets/kls/screening.py` is the source of truth.

| item | value |
|---|---|
| $\kappa$ of record | $0.05$ |
| directional support | $\hat\theta(0.05)\le0.5$ on **every** selected interval at both $n$, **and** aligned supply over $[0,T\wedge\tau]$ grows by $<1.5$ from the smaller to the larger $n$ |
| directional against | $\hat\theta(0.05)$ increasing in $n$ **and** $>0.8$ at the top $n$ on the $S_H$-pulse window, **or** aligned supply growth $\ge0.5\times$ the dimension ratio (i.e. $\ge2.0$ for a $4\times$ step) |
| spectator hard gate | base-block invariance of $\lambda_{\rm cut}$ to $10^{-10}$; block-family supply $n$-independence (implemented pathwise, tolerance $10^{-12}$, strictly stronger than the requested 3 stderr) |

## 4. Artifacts

| path | profile | seed | dimensions |
|---|---|---|---|
| `research/runs/2026-08-30T175028.209516Z-kls-screen.jsonl` | `high-n` | `20260830` | $n\in\{1024,4096\}$; spectators $n\in\{256,4096\}$, $n_0=32$ |
| `research/runs/2026-08-30T175419.597477Z-kls-screen.jsonl` | `standard` | `20260830` | $n\in\{256,1024\}$; spectators $n\in\{256,1024\}$, $n_0=32$ |

Recorded environment (both): Python 3.13.12, numpy 2.4.6, scipy 1.18.0,
Linux-6.17.0-1032-oem-x86_64. Recorded `git_commit` is `cd4a894`, the worktree **base** commit:
the `kls-screen` target itself was uncommitted when the runs were produced and is being handed to
the orchestrator as a diff. Reproducibility rests on the seed, the profile configuration in the
`_provenance` header, and the library versions — not on that commit id.

Run configuration (both profiles): $T=0.4$, path step $dt=0.005$ (exact filtering representation
$c_t=tX+B_t$, no Euler drift error), 16 paths per dimension split 8 discovery / 8 held-out,
balanced stopping $\tau$ at $p_t\notin[1/3,2/3]$ detected on the full path grid,
$\kappa\in\{0.01,0.05,0.1,0.25,0.5,1.0\}$, window widths $\{0.04,0.1,0.2,0.4\}$.

**Deviation from the suggested profile, with reason.** The brief suggested snapshot observables
every 5th step of a $dt=0.01$ grid. That fails this target's own paired snapshot-refinement gate
(normalized drift $1.11$ and $1.25$ against a tolerance of $1$), and so does a uniform $0.02$
grid ($1.19$, $1.93$). The surrogate excess has a steep initial layer — the half-line competitor
collapses as soon as the first extreme tilt appears — so the snapshot grid is refined:
spacing $0.005$ on $[0,0.06]$, spacing $0.02$ afterwards, 30 snapshots per path. With that grid
the refinement gate passes at $0.42$–$0.75$ across all four configurations. Wall time: 7 min
(`high-n`), 2 min (`standard`).

## 5. Gate results

All gates pass in both artifacts.

| gate | worst measured | tol | what it compares |
|---|---|---|---|
| `initial_balance` | $8.9\cdot10^{-16}$ | $2\cdot10^{-11}$ | closed-form balanced mass at $t=0$ |
| `mass_vectorized_vs_scalar_engine` | $1.1\cdot10^{-13}$ | $10^{-11}$ | new vectorized log-tail $p_t$ vs the pre-existing scalar truncation engine |
| `lambda_cut_bracket` | $1.1\cdot10^{-15}$ | $10^{-12}$ | probe eq. (5): $\lambda_{\min}(A)\le\lambda_{\rm cut}\le\lambda_{\max}(A)$ |
| `two_colour_vs_reference_engine` | $0$ | $10^{-12}$ | $S,S_H,r,D,p$ reproduced from `observe_tail_union` |
| `lambda_cut_decomposition_vs_dense` | $2.2\cdot10^{-16}$ | $10^{-12}$ | (D1)–(D2) vs the dense $n=8$ double sum |
| `perimeter_vs_minkowski_finite_difference` | $2.1\cdot10^{-9}$ | $5\cdot10^{-8}$ | closed-form $P_t$ vs central difference of $a\mapsto\mu_t(F_a)$ |
| `mass_martingale` | $0.085$ | $0.24$ | $\mathbb E p_T=1/2$ |
| `snapshot_stride_refinement` | $0.75$ | $1$ | every channel, snapshot grid vs its 2:1 subsample |
| `spectator_lambda_cut_block_invariance` | $0$ | $10^{-10}$ | $\lambda_{\rm cut}$(full cylinder) vs $\lambda_{\rm cut}$(base block) |
| `spectator_pathwise_block_supply_invariance` | $0$ | $10^{-12}$ | block-family supply, identical base-block path across $n$ |

The two spectator gates measure exactly $0$: for a cylinder cut, $\delta_i$ and $d_i$ vanish
bit-for-bit on spectator coordinates when routed through the generic per-coordinate pipeline, so
the direct-sum identity is exact in floating point. The gate therefore verifies that the
implementation propagates the direct sum, not a delicate cancellation. Independent oracle tests
also check $\lambda_{\rm cut}$ of the cylinder against a dense *full-dimensional* $n\times n$
evaluation.

Additional oracle tests (in `experiments/tests/test_18_screening_cut_scale.py`) reproduce the
probe's own calibrations exactly: $\lambda_{\rm cut}(\sigma^2I,K)=\sigma^2$ (eq. 9),
$\lambda_{\rm cut}(\operatorname{diag}(\Lambda,1,\dots,1),c\,e_1e_1^T)=\Lambda$ (eq. 11), and the
leakage identity $\lambda_{\rm cut}(\operatorname{diag}(1,L),\varepsilon(e_{12}+e_{21}))=(1+L)/2$
for every $\varepsilon\ne0$ (eq. 8), including $\varepsilon=10^{-9}$, $L=10^4$.

## 6. Numbers

### 6.1 Cut-scale trajectories

Path-ensemble means, $t$ in $[0,0.4]$; peak values and values at $T$.

| $n$ | $\lambda_{\rm cut}$ peak | $\lambda_{\max}$ peak | $\lambda_{\rm cut}/\lambda_{\max}$ at $T$ | $\hat e_t$ at $T$ | $P_t$ range |
|---|---|---|---|---|---|
| 256 | 1.74 | 2.43 | $1.70/2.12=0.80$ | 0.258 | 0.491–0.53 |
| 1024 | 2.20 (std) / 2.33 (high-n) | 2.95 / 3.29 | $2.05/2.32=0.88$ | 0.266 | 0.490–0.52 |
| 4096 | 2.76 | 3.72 | $2.27/2.44=0.93$ | 0.274 | 0.490–0.52 |

Readings:

* $\lambda_{\rm cut}$ **tracks the top of the spectrum** on this cut: it is $0.74$–$0.93$ of
  $\lambda_{\max}$ over the whole path. The cut-local scale buys essentially nothing relative to
  the refuted global operator norm here, because the tail-union cut has $\delta_t$ a *full*
  vector and therefore is aligned with every coordinate. The spectator repair of
  `prop:weighted-spectator-obstruction` is real (Section 6.4) but does not apply to this cut.
* $\lambda_{\rm cut}$ **grows with $n$** roughly like $\log n$: $1.74\to2.20/2.33\to2.76$ across
  $256\to1024\to4096$, against $\log n$ ratios $1.25$ and $1.20$.
* $P_t$ is essentially $n$-independent ($0.490$ at $t=0$, drifting to $\approx0.52$), and
  $\hat e_t\le P_t$ by construction, so the excess factor cannot itself grow with $n$. All the
  $n$-growth of the supply comes from $W_{\rm cut}$.

### 6.2 Screening: $\hat\theta$ and the aligned supply

Held-out half, full window $[0,T\wedge\tau]$.

| $n$ | plain supply $\int\hat eW$ | $\kappa=0.25$ | $\kappa=0.5$ | $\kappa=1$ |
|---|---|---|---|---|
| 256 | 0.7406 | aligned 0.7406, $\hat\theta=0$ | aligned 0.6752, $\hat\theta=0.052$ | aligned 0.1009, $\hat\theta=0.715$ |
| 1024 (std) | 1.3887 | aligned 1.3887, $\hat\theta=0$ | aligned 0.7421, $\hat\theta=0.384$ | aligned 0.0163, $\hat\theta=0.954$ |
| 1024 (high-n) | 1.2261 | aligned 1.2261, $\hat\theta=0$ | aligned 0.7301, $\hat\theta=0.320$ | aligned 0.0131, $\hat\theta=0.955$ |
| 4096 | 2.2645 | aligned 2.2645, $\hat\theta=0$ | aligned 0.0455, $\hat\theta=0.965$ | aligned 0.0021, $\hat\theta=0.992$ |

$\hat\theta(\kappa)=0$ exactly for $\kappa\in\{0.01,0.05,0.1,0.25\}$ on every selected interval,
at every dimension, in both artifacts.

Aligned-supply growth at the $\kappa$ of record ($0.05$), within-run so the ensembles are
comparable:

* $256\to1024$: $0.7406\to1.3887$, factor $\mathbf{1.875}$;
* $1024\to4096$: $1.2261\to2.2645$, factor $\mathbf{1.847}$.

Two independent $4\times$ steps give the same factor, i.e. a clean $\approx n^{0.44}$ power law
over $256\to4096$. Part of it is a longer stopped horizon at larger $n$ ($\tau$-hit fraction
$0.375\to0.125$, mean $\tau\wedge T$ $0.353\to0.389$); the growth survives that normalization —
on the *fixed-length* discovery-selected windows the held-out supply grows
$0.186\to0.328$ (width $0.04$) and $0.902\to1.499$ (width $0.2$) from $n=1024$ to $n=4096$,
factors $1.76$ and $1.66$.

The two $n=1024$ rows differ ($1.389$ vs $1.226$) because the per-dimension RNG streams are
spawned by position, so $n=1024$ draws a different 16-path ensemble in the two profiles. That
$12\%$ spread is the honest scale of ensemble noise at 8 held-out paths, and it is smaller than
the $85\%$ growth being measured.

### 6.3 Joint occurrence

Per path, over its snapshot times in $[0,\tau]$, the $\phi$-correlation between
$\{\lambda_{\rm cut}$ above its own median$\}$ and $\{\hat e$ above its own median$\}$:

| $n$ | correlation (mean $\pm$ stderr over paths) | fraction of $\int\hat eW$ carried by $\lambda_{\rm cut}\ge2$ |
|---|---|---|
| 256 | $0.966\pm0.015$ | $0.00$ |
| 1024 | $0.920\pm0.025$ / $0.926\pm0.026$ | $0.849$ / $0.533$ |
| 4096 | $0.908\pm0.026$ | $1.000$ |

**Caveat that must travel with these numbers.** Both $\lambda_{\rm cut}$ and $\hat e$ increase
monotonically with $t$ over most of $[0,T]$ on most paths, so a within-path indicator correlation
near $0.9$ is largely explained by a shared monotone time trend rather than by a genuine
coincidence beyond it. The diagnostic as specified does not decorrelate that trend. What it does
establish without ambiguity is the second column: at $n=4096$, **100%** of the surrogate supply
mass is deposited at times with $\lambda_{\rm cut}\ge2$, i.e. the weight is never in a cheap
regime while the supply is being accumulated.

### 6.4 Spectator cylinder control

$n_0=32$, cut $E=\{\max_{i\le32}|x_i|\ge a_{32}\}\times\mathbb R^{n-32}$, base-block tilt path
held **pathwise identical** across $n$ (separate RNG streams for base and spectators).

* $\lambda_{\rm cut}$ on the full model equals $\lambda_{\rm cut}$ of the base block to $0$
  (exact in floating point); mean $1.0947$, max $1.5456$, identical for $n=256$, $1024$, $4096$.
* Supply with the **block-restricted** competitor family: $0.448693\pm0.039$ at every $n$;
  pathwise difference exactly $0$.
* Supply with the **all-coordinate** competitor family, paired over the 8 identical base paths:

| step | paired mean increase | paired stderr | relative | paths increasing |
|---|---|---|---|---|
| $256\to1024$ | $+0.0975$ | $0.0212$ | $+17.7\%$ | 8/8 |
| $256\to4096$ | $+0.1354$ | $0.0168$ | $+24.6\%$ | 8/8 |

This is the sharpest structural finding of the run, and it is **not** an artifact of the
surrogate. For a product measure and a cylinder cut $E=E_0\times\mathbb R^m$:

* $P_t(E)=P_t(E_0)$ is independent of $m$, and $\lambda_{\rm cut}$, $W_{\rm cut}$ are exactly
  spectator-blind by the probe's direct-sum identity (eq. 6, case 1);
* every competitor in $\mathbb R^{n_0}$ extends to a cylinder in $\mathbb R^{n_0+m}$ with the same
  mass and the same weighted perimeter, so $I_{\mu_t}(p_t)$ is **non-increasing** in $m$;
* hence $e_t=P_t-I_{\mu_t}(p_t)$ is **non-decreasing** in the spectator dimension.

So $W_{\rm cut}$ is spectator-blind but $e_tW_{\rm cut}$ is not. The numbers above are a measured
lower bound on that increase. **This is not a refutation**: since $0\le e_t\le P_t$ and $P_t$ is
spectator-independent, the cylinder direction can inflate the supply by at most the bounded
factor $P_t/e_t$, so this family alone cannot break an $O(T)$ supply bound. It does mean that
"cut-local, tensor-stable covariance weight that ignores independent spectators" is only accurate
about the *weight*; the *product* $e_tW_{\rm cut}$ retains a spectator dependence that no choice
of weight can remove.

## 7. Interpretation against the pre-registered rule

**Verdict at $\kappa=0.05$: inconclusive.** The $\hat\theta$ half of the support criterion is met
($\hat\theta=0$ everywhere), the supply half is not ($1.85$ against a threshold of $1.5$); the
against criterion is also not met ($1.85$ against a threshold of $2.0$, and $\hat\theta$ is flat
at $0$, not increasing). The artifacts record `outcome: inconclusive` from the code, not from
this prose.

Three readings that go beyond the rule and that the prober should have:

1. **The screening of Candidate B is inert or self-defeating on this model.** At every
   $\kappa\le0.25$ the aligned set is the whole time axis: $\hat\theta=0$ and the screened supply
   equals the plain supply, which grows like $n^{0.44}$. At $\kappa=0.5$ the screened supply
   collapses ($2.2645\to0.0455$ at $n=4096$) but $\hat\theta$ rises to $0.965$, and at $\kappa=1$
   to $0.992$. The crossover $\kappa$ is the typical value of $Q_t/(\hat e_tW_{\rm cut})$, which
   is $\approx0.39$ at $n=1024$ and $\approx0.35$ at $n=4096$ and **decreases with $n$**. So for
   any fixed $\kappa$ the model eventually lands on the wrong side. There is no $\kappa$ visible
   here that simultaneously bounds the supply and keeps $\hat\theta$ away from $1$ uniformly in
   $n$. Since $\hat\theta\le\theta$, the true complement fractions are at least these.
   A $\theta$ near $1$ does not by itself contradict (22)–(23) — $\theta$ there is a coefficient
   in a claimed inequality, not the measured fraction — but it does mean the screened term (21)
   carries none of the burden and the whole estimate falls back on the unscreened trace terms
   $C_0T+C_1\int r+\beta\int D$.
2. **Under the probe's own admissibility constraint $\kappa<\kappa_{\rm TT}$, $\kappa=0.5$ is the
   interesting end of the admissible range.** Reading the probe's $\kappa_{\rm TT}$ with the
   balanced two-tail radius $a=z_{3/4}=0.67449$ gives
   $\kappa_{\rm TT}=2^{-5/2}\cdot16a^2\varphi(a)^2/(2\varphi(a)-\varphi(0))\approx0.549$. That
   reading is **mine and unverified** — the probe does not fix $a$ numerically — so the run sweeps
   $\kappa$ rather than relying on it. If $\kappa_{\rm TT}\approx0.55$ is right, then the entire
   admissible range is exactly the range in which this model shows the tradeoff of reading 1.
3. **This model is not a witness against Candidates A or B as stated.** Both are conditioned on
   the near-worst premise (18): $h_n^*\le h_\bullet$ and $h_\mu\le(1+\varepsilon_{\rm nw})h_n^*$.
   The isotropic two-sided-exponential product has $h_\mu\asymp1$ and is explicitly excluded by
   the admissible choice $h_\bullet<c_{\rm prod}/(1+\varepsilon_{\rm nw})$ from `prop:products`.
   What the run stresses is the **unconditional** form of (17)/(21) and the *mechanism* of the
   screening, and it shows precisely where the near-worst premise has to do the work: it must
   exclude the joint occurrence of a $\log n$-growing $\lambda_{\rm cut}$ with a non-vanishing
   excess on a balanced near-minimizing cut.

**Outcome for the orchestrator: consistent-but-adverse-in-mechanism. No exact contradiction, no
refutation dossier is warranted, no status change is implied by these runs.**

## 8. Two exact analytic candidates worth a prover

Neither is asserted proved here; both are elementary and independent of any sampling.

**(E1) The balanced tail-union cut beats every coordinate half-space.** For the isotropic product
of two-sided exponentials on $\mathbb R^n$ with the balanced radius $a_n$,
$P_0=\frac{n\sqrt2}{2}(2^{1/n}-1)$, strictly decreasing in $n$ to $\frac{\sqrt2\ln2}{2}$, and
strictly below the common coordinate-half-space perimeter $1/\sqrt2$ for all $n\ge2$, with
equality at $n=1$. Consequence: any argument that upper-bounds $I_{\mu}(1/2)$ by a coordinate
half-space and calls the difference an excess produces a negative number on this cut.
Verified numerically two independent ways to $5\cdot10^{-10}$.

**(E2) Cylinder spectator monotonicity of the excess.** For $\mu=\mu_0\otimes\nu$ and a cylinder
cut $E=E_0\times\mathbb R^m$: $P_\mu(E)=P_{\mu_0}(E_0)$ and $W_{\rm cut}(A,K)$ are independent of
$m$, while $I_\mu(p)$ is non-increasing in $m$ (cylinder extension of competitors); hence
$e(E)=P-I$ is non-decreasing in $m$, and $eW_{\rm cut}$ is not spectator-blind even though
$W_{\rm cut}$ is. The inflation is bounded: $0\le e\le P$ with $P$ spectator-independent.
This sharpens the `conj:weighted-excess-rate` gate prose from "ignores independent spectators" to "the *weight*
ignores independent spectators; the *excess* does not, but only by a bounded factor".

## 9. Proposed adversarial instances (for the `synthesizer` only)

The KLS stress registry in `research/knowledge/instances.md` currently contains only
moment-map/CMH models; it has no entry for the tail-union product cut used by `kls-align` and now
by `kls-screen`, and none for a cylinder cut. Two proposals:

| proposed id | route | adversarial property | `finum` |
|---|---|---|---|
| `stress-tailunion-cut-scale` | localization / `conj:weighted-excess-rate` | balanced tail-union cut in the isotropic Laplace product: exact perimeter $\frac{n\sqrt2}{2}(2^{1/n}-1)$ strictly below every coordinate half-space for $n\ge2$, and $\lambda_{\rm cut}$ within $0.74$–$0.93$ of $\lambda_{\max}$, so a cut-local scale gives no reduction on a cut aligned with all coordinates | `kls-screen / stress-tailunion-cut-scale` |
| `stress-cylinder-spectator-excess` | localization / `conj:weighted-excess-rate` | cylinder cut $E_0\times\mathbb R^{n-n_0}$: $\lambda_{\rm cut}$ is exactly spectator-blind while $e_t$ is monotone non-decreasing in the spectator dimension, so it separates weight stability from excess stability — the calibration the refuted global weight fails, plus the one the repaired weight still fails | `kls-screen / stress-cylinder-spectator-excess` |

Neither is a happy-path instance: the first is the model on which the cut-local repair provably
buys nothing, and the second is the model on which the repair is exactly correct for the weight
and exactly insufficient for the product. `finum` does not edit the registry.

## 10. Limitations

* $\hat e\le e$: every supply and every $\hat\theta$ is a lower bound (Section 2.2). "Support"
  readings from this target are structurally weak.
* The profile bound is the minimum over two explicit competitor families only. A richer family
  would lower $\hat I$, raise $\hat e$, and *increase* the supply — i.e. all reported supplies can
  only move in the adverse direction under refinement.
* Balanced exit is detected at path-grid nodes with linear crossing interpolation; an exit and
  re-entry entirely between nodes is not controlled. This is inherited from the `kls-align`
  convention and is not a Brownian-bridge bound.
* 16 paths per dimension (8 held-out). The $n=1024$ cross-profile spread of $12\%$ is the honest
  ensemble noise scale.
* Two dimensions per profile; the power-law reading in Section 6.2 rests on two $4\times$ steps.
* The joint-occurrence correlation is confounded by a shared monotone time trend (Section 6.3).
* Time quadrature is trapezoidal on a two-scale snapshot grid; the residual paired drift is
  largest, as expected, on the indicator-gated channels (`supply_big_scale`, `aligned_supply@1`).

## 11. Repository changes made

Only inside the `finum` write surface.

* new `experiments/finum/localization/screening.py`: cancellation-free vectorized tilted-Laplace
  log-tail / log-interval primitives, exact weighted perimeter, two competitor families,
  the exact Cauchy quadratic form, $\lambda_{\rm cut}$, and a dense reference path;
* new `experiments/finum/targets/kls/screening.py`: target `kls-screen` with profiles
  `smoke`, `standard`, `high-n`;
* registration and exports in `experiments/finum/targets/__init__.py`,
  `experiments/finum/targets/kls/__init__.py`, `experiments/finum/localization/__init__.py`;
* new `experiments/tests/test_18_screening_cut_scale.py` (45 oracle tests, including a regression
  asserting the `kls-align` gate set and schema are unchanged).

`uv run python -m finum check` passes for every target; `uv run pytest` passes in full.
A draft decision record for this harness addition was returned to the orchestrator; `finum` does
not write `research/decisions/`.

## 12. Statement of status

No ledger status, manuscript statement, route-control file, dossier, or knowledge file is changed
or proposed to be changed by this record beyond the two instance proposals in Section 9, which
only the `synthesizer` may act on. Every number above is directional research evidence produced
under `CLAUDE.md` constraint 2, and remains so even where the underlying arithmetic is exact.

```yaml
outcome: complete
artifacts:
  - research/runs/2026-08-30T175028.209516Z-kls-screen.jsonl
  - research/runs/2026-08-30T175419.597477Z-kls-screen.jsonl
  - research/explorations/2026-08-30-finum-align-screened-supply-w4a01.md
  - experiments/finum/localization/screening.py
  - experiments/finum/targets/kls/screening.py
  - experiments/tests/test_18_screening_cut_scale.py
proposed_deltas:
  - synthesizer only: add `stress-tailunion-cut-scale` and `stress-cylinder-spectator-excess` to the KLS stress registry in research/knowledge/instances.md, as drafted in Section 9
  - orchestrator only: apply the draft decision record for the kls-screen harness addition returned with this run
next_role: orchestrator
next_prompt: |
  Route these results to the kls-route-prober holding `kls-gate:q:weighted` (run w4w01).
  Artifacts: research/runs/2026-08-30T175028.209516Z-kls-screen.jsonl (profile high-n, seed
  20260830, n in {1024,4096}) and research/runs/2026-08-30T175419.597477Z-kls-screen.jsonl
  (profile standard, seed 20260830, n in {256,1024}).

  Correct the brief that generated this run before reusing it: a competitor-based profile bound
  is an UPPER bound on the isoperimetric profile, so the surrogate excess ehat = (P - Ihat)_+
  satisfies ehat <= e and therefore UNDERSTATES the excess. Every supply integral and every
  theta_hat in these artifacts is a lower bound for the true one. Growth is the robust direction;
  boundedness is the weak one.

  Pre-registered thresholds, fixed in code before the runs: kappa of record 0.05; support iff
  theta_hat(0.05) <= 0.5 on every selected interval at both n AND aligned supply growth < 1.5;
  against iff theta_hat(0.05) increasing in n and > 0.8 at the top n, OR aligned supply growth
  >= 2.0 for a 4x dimension step. Measured: theta_hat(0.05) = 0 exactly at every n on every
  selected interval; aligned supply growth 1.875 (256->1024) and 1.847 (1024->4096). Recorded
  outcome: inconclusive. No status change is implied.

  The decision-relevant findings for the gate are three, and none of them is a refutation:
  (a) lambda_cut sits at 0.74-0.93 of lambda_max on the balanced tail-union cut and grows like
      log n (1.74 -> 2.33 -> 2.76 across n = 256, 1024, 4096), so the cut-local scale buys nothing
      relative to the refuted global operator norm on a cut aligned with all coordinates; at
      n = 4096, 100% of the surrogate supply mass is deposited while lambda_cut >= 2.
  (b) the Candidate B screening is inert or self-defeating on this model: theta_hat = 0 for every
      kappa <= 0.25 with the screened supply equal to the plain supply, while at kappa = 0.5 the
      screened supply collapses from 2.2645 to 0.0455 at n = 4096 but theta_hat rises to 0.965.
      The crossover kappa is the typical Q/(ehat W), about 0.39 at n = 1024 and 0.35 at n = 4096,
      decreasing in n, so no fixed kappa keeps both quantities controlled uniformly in n.
  (c) exact and independent of the surrogate: for a cylinder cut E_0 x R^m in a product measure,
      P and W_cut are spectator-independent while the profile is non-increasing in m (cylinder
      extension of competitors), so e is non-decreasing in m and e*W_cut is NOT spectator-blind
      even though W_cut is. Measured paired increase in the surrogate supply with the base-block
      path held pathwise identical: +17.7% +- 2.1% (256->1024) and +24.6% +- 1.7% (256->4096),
      8/8 paths. The inflation is bounded because 0 <= e <= P with P spectator-independent, so
      the cylinder family alone cannot break an O(T) supply bound.

  State explicitly in the prober's record that the isotropic two-sided-exponential product has
  h_mu of order one and is excluded by the near-worst premise (18), so none of this refutes
  Candidate A or Candidate B as stated; it constrains the unconditional forms of (17) and (21)
  and identifies exactly what premise (18) must exclude.

  Do not open a refutation dossier from this run. If the prober wants either exact statement
  restated analytically, hand E1 (the balanced tail-union perimeter
  P_0 = n*sqrt(2)*(2^{1/n}-1)/2 < 1/sqrt(2) for n >= 2, so coordinate half-spaces are an
  inadmissible profile surrogate for this cut) or E2 (cylinder spectator monotonicity of the
  excess) to a prover; both are elementary and neither changes any status by itself. Do not infer
  any implication involving conj:trace-upgrade, conj:stein-weighted, or conj:product-alignment.
```
