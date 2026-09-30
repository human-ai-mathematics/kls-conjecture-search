---
verdict: pass
authors:
  - /root/prove_weighted_spectator_obstruction
  - /root/repair_weighted_spectator_w0r2
reviewer: /root/review_weighted_spectator_w0r2
fingerprints:
  solutions/prop-weighted-spectator-obstruction.md: cc9f7110c4e9d869472e4feee4bdd3e753e6f5a22aff99c0b262895b6aa1b261
  prop:weighted-spectator-obstruction: 41f54a097023867b895b5b57f385db284aaeb2a14a297896865c5061566249c0
  prop:covariance-spike: 161bf636e00b06d616360d86e08e775faacc85e3ebd8f62c91289807a22bfbb5
  lem:one-dimensional-density-variance: d815a2b4dd127f6904303d7af11bdff816a4ca70c21541afd80ebd41506343a6
  prop:products: 85b9ec9b7b81c783e52dce9f3edce41396f581da4f7a425bd3df9031860a6c8c
  lem:half: 1d4daf2283e1a1022580a067533d1cc3aae4194fa319d223aa00e4112d031a2f
  ass:weighted-package: 3532efe632a78732299519f2fe94aec60e99945eb186b7aba537603906d8e828
  q:weighted: 9c714d8f4be19c4b63709e43e1ae4a1e5253f9b958b02baaa089df297068283d
---

*Follows up* `research/reviews/2026-08-27-prop-weighted-spectator-obstruction-proof-review.md`.

# Exponential-spectator obstruction repair — independent proof review

This is a cold review of `solutions/prop-weighted-spectator-obstruction.tex` at SHA-256
`8c837c6e8ab677049071a4d5727d82cd7328bafd3d2ef88887e52c30ec672700`.  The proof was
reconstructed from the pinned dossier, the live ledger and manuscript statements, the declared
dependency artifacts, and the actual published sources.  The earlier non-certifying audit was
read only after this reconstruction and is retained unchanged as historical context.  Both proof
authors are distinct from the reviewer, and no exploration names the reviewer as an author.

## Findings

### Statement agreement and logical consequence

The theorem at `solutions/prop-weighted-spectator-obstruction.tex:40`, the ledger statement at
`research/kls/ledger.yaml:765`, and Proposition `prop:weighted-spectator-obstruction` at
`modules/kls/27-eldan-open-targets.tex:44` agree mathematically.  For every proposed
$C,T_0,\gamma>0$, every $\eta\in(0,1/2)$, and every $\delta>0$, the theorem produces a finite
dimension, the isotropic product of centered rate-one exponentials, a balanced finite-perimeter
cylinder with both

$$
e_0(E)\leq\delta,
\qquad
\frac{e_0(E)}{I_\mu(1/2)}\leq\delta,
$$

and a single $0<T\leq T_0$ for which the strict reverse of the proposed weighted rate holds.  The
additional $e_0(E)\leq1$ conclusion puts the witness inside the exact quantified class of
`q:weighted`.  Since the construction works for every $\eta\in(0,1/2)$, it covers every candidate
$\eta\in(0,1/4]$ in that question.  Thus the certified proposition logically refutes the current
literal all-measure, global-$\|A_t\|_{\mathrm{op}}$ formulation of `q:weighted`.

This consequence does not refute KLS.  All witnesses are products of isotropic one-dimensional
log-concave laws, and the independently certified `prop:products` gives them a dimension-free
Cheeger/KLS constant.

### Exact-mass regular base and initial excess

For $a_m=I_{\lambda^{\otimes m}}(1/2)$, the cylinder identity
$(S\times\mathbb R)_r=S_r\times\mathbb R$ gives $a_{m+1}\leq a_m$.  At time zero,
`prop:products` gives a universal product Cheeger lower bound and `lem:half` gives
$a_m=h_{\lambda^{\otimes m}}/2\geq a_*>0$.  Hence $a_m\downarrow a_\infty\geq a_*$.

The regularization lemma correctly starts with a separately named $S^{(0)}$, passes from finite
lower outer Minkowski content to finite relative weighted BV perimeter, uses strict approximation
on compact truncations of $[-1,\infty)^m$, and corrects the small mass error by a compactly
supported smooth flow through an interior regular patch.  The repaired display now states

$$
\nu(S_k)\longrightarrow p,
\qquad
\operatorname{Per}_\nu(S_k)\longrightarrow\operatorname{Per}_\nu(S^{(0)}),
$$

and the selected exact-mass corrected approximant is explicitly renamed $S$.  For this regular
set, the one-sided tube formula counts precisely the relative interface in the interior of the
orthant.  Support facets are not interfaces, and their intersections with the regular boundary
are lower-dimensional, so there is no first-order support-boundary term.  Multiplying by the
positive continuous posterior density multiplies the perimeter measure by the same density.  The
repaired statement restricts this identity to $t\geq0$ and $0<Z(u,t)<\infty$; in the application
$t>0$ makes the tilt bounded after completing the square, while at $t=0$ one has $u=0$.

Choose $M$ with $a_M-a_\infty\leq\varepsilon/2$ and a regular exact-half-mass $E_0$ with
$P_0\leq a_M+\varepsilon/2$.  Then, for every later spectator dimension $N$,

$$
0\leq e_0(E_0\times\mathbb R^N)\leq\varepsilon,
\qquad
\frac{e_0(E_0\times\mathbb R^N)}
     {I_{\lambda^{\otimes(M+N)}}(1/2)}
\leq\frac{\varepsilon}{a_*}.
$$

The choice $2\varepsilon\leq\min\{\delta,1,\delta a_*\}$ gives the two requested tolerances and
$e_0\leq1$, uniformly in the still-unselected $N$.

### Product posterior, common base event, and stopping

In the planted realization $c_t=tX+B_t$, the prior and Gaussian likelihood factor over the base
block and every spectator coordinate.  Consequently the posterior factorization and block
diagonal covariance at dossier equation (8) are exact.  The base and spectator posterior
processes are functions of disjoint latent/Brownian blocks and are independent as processes.
The cylinder distance identity makes $p_t$, $P_t(E)$, and $\tau_\eta$ base-block measurable.

Local exponential integrability gives the uniform small-parameter $L^1$ convergence in repaired
equation (10), with the full subscript $|u|\leq a$, $0\leq t\leq\bar T$.  The reflected-Brownian
union bound is

$$
4M\exp\!\left(-\frac{a^2}{8MT_b}\right)\leq\frac12
$$

under the displayed choice of $T_b$.  Independence from $\{|X^0|\leq L\}$ therefore gives
$\mathbb P(G_b)\geq1/4$.  On $G_b$, the Euclidean Brownian coordinate bound and
$T_bL\leq a/2$ give $|c_s^0|\leq a$ simultaneously for $s\leq T_b$.  Thus
$|p_s-1/2|<\eta$ throughout the closed interval.  The normalized density on the chosen perimeter
patch is at least $(1/2)/2=1/4$, so the exact density-change formula gives

$$
\tau_\eta>T_b,
\qquad
P_s(E_0\times\mathbb R^N)\geq P_0/8
$$

simultaneously on $G_b$.  Neither $G_b$ nor $T_b$ depends on $N$.  The auxiliary event need not
belong to the localization filtration; only its probability and its independence from each
fixed-time spectator event are used.

### Deterministic-time covariance spike and exact-profile competitor

The imported covariance-spike event is used only at each deterministic time.  The observation
conversion is exactly

$$
\frac{c_t}{t}=X+\frac{B_t}{t}\stackrel d=X+t^{-1/2}G,
$$

so the source's Gaussian-channel variance is $s=1/t$.  If $\log N\geq2/T$ and
$t\in[T/2,T]$, then $1/t\leq2/T\leq\log N$ and

$$
N\,\frac12e^{-1/t}\geq\frac12.
$$

Therefore

$$
\mathbb P(H_t)
\geq1-\left(1-\tfrac12e^{-1/t}\right)^N
\geq1-e^{-1/2}=:h_{\mathrm{sp}}.
$$

No event common to the interval is asserted or needed.

At every finite time the posterior is equivalent to the initial product, so $p_t\in(0,1)$.  On
$H_t$, a $p_t$-quantile halfline in the least high-variance spectator coordinate has full-product
mass exactly $p_t$ and outer Minkowski perimeter $f_{i,t}(q_{i,t})$.  The repaired equation (18)
has the correct load-bearing comparison

$$
I_{\mu_t}(p_t)
\leq f_{i,t}(q_{i,t})
\leq\|f_{i,t}\|_\infty
\leq v_{i,t}^{-1/2}
\leq\sqrt{t/c_{\mathrm{sp}}}.
$$

This is an explicit upper competitor for the moving profile, not an assumed lower bound.

### Tonelli, constants, and quantifier order

The regular-cylinder perimeter is a measurable function of the posterior parameters by the
surface-density formula.  For these continuously parameterized positive log-concave densities,
the profile can be written using a fixed countable strictly dense class of regular rational
competitors, with exact mass obtained as the limit of shrinking rational mass windows; hence
$(t,\omega)\mapsto I_{\mu_t}(p_t)$ is Borel measurable.  The variance maps and $H_t$ are likewise
jointly measurable for $t>0$.  Thus the stopped nonnegative integrand is jointly measurable, and
nonnegative Tonelli legitimately integrates the separate deterministic-time events.

The bound $T\leq c_{\mathrm{sp}}P_0^2/256$ gives

$$
e_t(E)\geq P_0/8-\sqrt{t/c_{\mathrm{sp}}}\geq P_0/16
$$

on $G_b\cap H_t$.  Block diagonality gives the weight lower bound
$c_{\mathrm{sp}}^{5/2}t^{-5/2}$, and fixed-time base/spectator independence gives
$\mathbb P(G_b\cap H_t)\geq h_{\mathrm{sp}}/4$.  Therefore

$$
\begin{aligned}
\mathbb E\int_0^{T\wedge\tau_\eta}
e_t(E)(1+\|A_t\|_{\mathrm{op}})^{5/2}\,dt
&\geq \frac{P_0h_{\mathrm{sp}}c_{\mathrm{sp}}^{5/2}}{64}
       \int_{T/2}^Tt^{-5/2}\,dt\\
&=\kappa_{\mathrm{sp}}P_0T^{-3/2},
\end{aligned}
$$

where

$$
\int_{T/2}^Tt^{-5/2}\,dt
=\frac23(2^{3/2}-1)T^{-3/2},
\qquad
\kappa_{\mathrm{sp}}
=\frac{h_{\mathrm{sp}}c_{\mathrm{sp}}^{5/2}}{96}(2^{3/2}-1).
$$

The two final strict small-$T$ conditions separately make $CTP_0$ and $CT^{1+\gamma}$ smaller
than half of this lower bound.  Since $e_0(E)\leq P_0$, their sum is strictly smaller than the
left side.  Every quantity in those conditions is fixed before $T$, and only afterward is a
finite $N$ chosen with $\log N\geq2/T$.  The checked order is therefore

$$
(C,T_0,\gamma,\eta,\delta)
\longrightarrow(\varepsilon,M,E_0,P_0,T_b)
\longrightarrow T
\longrightarrow N.
$$

### Fences, hypothesis accounting, dependencies, and citations

The target has no formal `bounded_by` edge.  Its consumer `q:weighted` has two contextual fences,
both respected:

- `obs:two-tail`: the proof retains the calibrated exponent $5/2$ and demonstrates the tensor
  instability of charging independent spectators through a global operator norm.
- `obs:circularity`: the proof bounds the localized profile from above with an explicit
  exact-mass spectator halfline and never inserts a moving-profile lower bound.

No implication among the trace-upgrade questions is claimed.

All stated theorem parameters are accounted for.  $C,T_0$, and $\gamma$ enter the final time
choice; $\eta>0$ enters the uniform base stability and $\eta<1/2$ gives the stated balanced
window; $\delta>0$ enters the uniform base-excess choice.  The proof in fact only needs
$\gamma>-5/2$ for its final power comparison, so the stated $\gamma>0$ is route-matched slack, not
a defect.  There is no used but unstated mathematical hypothesis.

The four declared dependencies are closed:

- `prop:covariance-spike` is a published import.  The event estimate is proved in Proposition 65
  of Klartag--Lehec, *Bulletin of the American Mathematical Society* 62 (2025), 575--642,
  DOI `10.1090/bull/1869`.  Its proof gives the exact per-coordinate probability
  $\tfrac12e^{-s}$ and the independent-coordinate union event used here.
- `lem:one-dimensional-density-variance` is a published import.  Proposition 2.1 of
  Bobkov--Chistyakov, *Journal of Theoretical Probability* 28 (2015), 976--988,
  DOI `10.1007/s10959-013-0504-1`, proves
  $1/12\leq v\|f\|_\infty^2\leq1$ for a log-concave density.
- `prop:products` is `proved` with agent certification in
  `research/reviews/2026-08-27-kls-geometry-models-repair-proof-review.md`.  The present proof uses
  its time-zero dimension-free product Cheeger bound and independently rechecks the elementary
  posterior factorization.
- `lem:half` is `proved` with agent certification in
  `research/reviews/2026-08-25-kls-excess-bootstrap-r2-audit.md`, whose front matter is
  `type: proof-review`, `verdict: pass`.  It supplies $h_\nu=2I_\nu(1/2)$.

No dependency is open, conditional, or `preprint-unreviewed`.  No numerical artifact supplies a
proof step.  The remaining facts used in the dossier—relative weighted-BV approximation and tube
formulas, local exponential integrability, Gaussian posterior factorization, Brownian reflection,
and Tonelli—were checked directly in the stated finite-dimensional setting.

### Standalone build and repaired output

From `solutions/`, a forced run of

```text
latexmk -g -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=../build prop-weighted-spectator-obstruction.tex
```

exited zero and produced a six-page PDF.  The source hash was unchanged after the build.  All
displays were inspected in layout-preserving extracted text and rendered pages.  The four prior
defects now render correctly: the $0<Z<\infty$ restriction, the two BV convergence arrows and
$S^{(0)}$ target, the two-variable supremum, and the full profile-competitor inequality.  Both
citations resolve.  The remaining `??` entries are only the expected standalone cross-module
references permitted by `solutions/README.md`; there is no TeX error or malformed formula.

## Corrections

None.  All repairs required by the earlier audit are present in the pinned source and were
rechecked mathematically and in the generated PDF.

## Checked and unverified steps

Checked steps: statement/ledger/manuscript agreement; theorem and gate quantifiers; exact-mass
weighted-BV regularization; outer-Minkowski/support-boundary convention; posterior density change;
monotone positive half-profile limit; uniform additive and relative initial excess; planted
posterior factorization; base/spectator process independence; common base stopping/perimeter event;
Brownian probability constant; deterministic-time covariance-spike use with $s=1/t$; the
$\log N\geq2/T$ conversion; exact-$p_t$ quantile competitor; density--variance bound; joint
measurability; nonnegative Tonelli; every displayed constant; final strict inequalities; dependency
closure; citation classification; formal and contextual fences; and the standalone source/PDF.

Unverified steps inside the certified scope: none.

## Exclusions

This review does not certify a replacement tensor-stable or cut-local weight, a gate restricted
to near-worst measures, an exact-minimizer-only formulation, the weighted Stein-trace component of
`ass:weighted-package`, any implication in the trace-upgrade cluster, KLS itself, or any ledger
node other than the proposition listed in the front matter.  In particular, the separately added
`prop:spectator-excess-rate-obstruction` is a distinct candidate and is not reviewed or certified
here.  The logically consequent refutation of `q:weighted` is a proposed orchestrator delta, not a
second proof certification.  Dossier-header, ledger, manuscript, route, gating, bibliography, and
prior-review edits remain outside this reviewer's write surface.

## Proposed header and ledger deltas

The dossier header may change exactly as follows, leaving the author list and all other fields
unchanged:

```text
% checked_by  : agent
% reviewer    : /root/review_weighted_spectator_w0r2
% review      : research/reviews/2026-08-27-prop-weighted-spectator-obstruction-repair-proof-review.md
```

The target node may take unconditional `proved` status with:

```yaml
  - id: prop:weighted-spectator-obstruction
    kind: proposition
    status: proved
    route: eldan-localization
    file: modules/kls/27-eldan-open-targets.tex
    statement: "For every C,T0,gamma>0, eta in (0,1/2), and delta>0, some balanced finite-perimeter cylinder in a centered one-sided-exponential product has additive and relative excess at most delta but violates the q:weighted global-operator-norm rate at a time T<=T0."
    depends_on: [prop:covariance-spike, lem:one-dimensional-density-variance, prop:products, lem:half]
    solution: solutions/prop-weighted-spectator-obstruction.tex
    checked_by: agent
    review: research/reviews/2026-08-27-prop-weighted-spectator-obstruction-repair-proof-review.md
```

The direct logical consequence for the existing question is:

```yaml
  - id: q:weighted
    kind: question
    status: refuted
    route: eldan-localization
    file: modules/kls/27-eldan-open-targets.tex
    statement: "Do universal C,T0,gamma>0 and eta in (0,1/4] exist such that every isotropic log-concave law and every balanced finite-perimeter cut with e0<=1 satisfy E int_0^{T wedge tau_eta} e_t(1+||A_t||_op)^(5/2) dt <= C(T e0+T^(1+gamma)) for all T<=T0?"
    depends_on: [prop:weighted-spectator-obstruction]
    bounded_by: [obs:two-tail, obs:circularity]
    refuted_by: [prop:weighted-spectator-obstruction]
```

```yaml
outcome: complete
artifacts:
  - research/reviews/2026-08-27-prop-weighted-spectator-obstruction-repair-proof-review.md
proposed_deltas:
  - "Update the dossier header to checked_by: agent, reviewer: /root/review_weighted_spectator_w0r2, and the new review path."
  - "Mark prop:weighted-spectator-obstruction proved with its solution, checked_by: agent, and the new review path."
  - "Mark q:weighted refuted; add depends_on and refuted_by edges to prop:weighted-spectator-obstruction while retaining both bounded_by edges."
next_role: orchestrator
next_prompt: |
  Confirm that solutions/prop-weighted-spectator-obstruction.tex still has SHA-256
  8c837c6e8ab677049071a4d5727d82cd7328bafd3d2ef88887e52c30ec672700. Then apply exactly the
  dossier-header and two ledger deltas displayed above. Do not alter the certified theorem or the
  append-only review history. Run python3 research/check_ledger.py after the atomic ledger update.
```
