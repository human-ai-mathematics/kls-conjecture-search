---
verdict: revise
authors:
- /root/prove_weighted_spectator_obstruction
reviewer: /root/review_weighted_spectator_w0
fingerprints:
  solutions/prop-weighted-spectator-obstruction.md: cc9f7110c4e9d869472e4feee4bdd3e753e6f5a22aff99c0b262895b6aa1b261
  prop:weighted-spectator-obstruction: 43186945070f01440b94ed29e452f474290ea070a94c9874921fbc1b8e3329ab
  prop:covariance-spike: 161bf636e00b06d616360d86e08e775faacc85e3ebd8f62c91289807a22bfbb5
  lem:one-dimensional-density-variance: d815a2b4dd127f6904303d7af11bdff816a4ca70c21541afd80ebd41506343a6
  prop:products: 85b9ec9b7b81c783e52dce9f3edce41396f581da4f7a425bd3df9031860a6c8c
  lem:half: 1d4daf2283e1a1022580a067533d1cc3aae4194fa319d223aa00e4112d031a2f
  ass:weighted-package: f916708933f4ae70aafa69f26c84f8c0e7b52cb4a1558108d192fb80bcce2f95
  q:weighted: 40ee4d80f7dc31b49cd2cd25eb91816dfce7d539960ac0bef3721eeab86aa998
---

# Exponential-spectator obstruction — cold proof audit

This is an independent cold audit by `/root/review_weighted_spectator_w0` of
`solutions/prop-weighted-spectator-obstruction.tex`, authored by
`/root/prove_weighted_spectator_obstruction`.  The audited source has SHA-256
`7bce5bdadd0aba23785d0befa234c8e930b7069c1a01c04fd7503986c34b1816`.  The dossier,
ledger, manuscript statements, dependency dossiers, and primary sources were inspected before the
prover exploration was read.

This report is non-certifying.  The intended analytic argument can be reconstructed, but two
displayed formulas in the standalone dossier are malformed, including the critical profile
comparison on which the excess lower bound depends.  A repaired dossier must receive a fresh cold
review in a new append-only report.

## Findings

### Statement agreement and exact gate scope

The theorem at `solutions/prop-weighted-spectator-obstruction.tex:39` agrees mathematically with
the ledger statement of `prop:weighted-spectator-obstruction` and with Proposition
`prop:weighted-spectator-obstruction` at `modules/kls/27-eldan-open-targets.tex:44`.  It has the
correct quantifier directions: for every proposed $C,T_0,\gamma>0$, every
$\eta\in(0,1/2)$, and every $\delta>0$, it produces one finite dimension, one balanced cylinder,
and one positive $T\leq T_0$ violating the proposed upper bound.  The two estimates

$$
e_0(E)\leq\delta,
\qquad
\frac{e_0(E)}{I_\mu(1/2)}\leq\delta
$$

match both the additive and relative near-minimizer readings recorded in the candidate
proposition.

The current literal `q:weighted` at `modules/kls/27-eldan-open-targets.tex:64` and item (i-w) of
`ass:weighted-package` at `modules/kls/20-eldan-statements.tex:117` quantify over every balanced
finite-perimeter cut with $e_0(E)\leq1$, use a fixed
$\eta\in(0,1/4]$, and demand the estimate for all $0<T\leq T_0$.  The intended theorem covers
that range because it treats every $\eta\in(0,1/2)$ and additionally arranges $e_0(E)\leq1$.
Thus, once a corrected dossier is certified, the result would negate precisely the literal
global-operator-norm weighted-excess component.  It would not negate a differently stated gate
with an explicit near-worst-measure hypothesis or a cut-local tensor-stable weight.

The conclusion does not refute KLS.  Every witness is a product of isotropic one-dimensional
log-concave factors, and the proved `prop:products` gives a dimension-free Cheeger/KLS bound for
such products.

### Reconstructed mathematical steps

The following steps were checked independently.

1. **Regular base selection.**  For
   $a_m=I_{\lambda^{\otimes m}}(1/2)$, cylinder extension gives
   $a_{m+1}\leq a_m$.  The proved product KLS bound and `lem:half` give a universal floor
   $a_m\geq a_*>0$, hence $a_m\downarrow a_\infty\geq a_*$.  Choosing $M$ near this limit and
   an exact-half-mass regular competitor with perimeter at most $a_M+\varepsilon/2$ gives, for
   every later $N$,
   $$
   0\leq e_0(E_0\times\mathbb R^N)\leq\varepsilon,
   \qquad
   \frac{e_0(E_0\times\mathbb R^N)}{I_{\lambda^{\otimes(M+N)}}(1/2)}
   \leq\frac{\varepsilon}{a_*}.
   $$
   The choice $2\varepsilon\leq\min\{\delta,1,\delta a_*\}$ is stronger than needed and gives
   both requested tolerances and $e_0\leq1$ uniformly in $N$.

2. **Minkowski/BV change of density.**  The intended regularization is valid: finite lower outer
   Minkowski content dominates relative weighted BV perimeter; weighted strict approximation on
   compact truncations of $K_m=[-1,\infty)^m$, followed by a compactly supported mass-correcting
   flow, yields a regular exact-mass competitor with arbitrarily small perimeter loss.  For a
   regular relative boundary, the one-sided tube formula identifies ambient outer Minkowski
   content with the weighted area of
   $\partial^*S\cap\operatorname{int}K_m$.  Facets of $\partial K_m$ are support boundary, not an
   interface, and corners are lower-dimensional, so no first-order support-boundary term occurs.
   Multiplication by a finite positive continuous posterior density multiplies this relative
   perimeter measure by the same density.  This justifies the formula used later for the exact
   noncompact exponential product.  The dossier's written approximation display nevertheless
   fails to state this convergence correctly; that source defect is recorded below.

3. **Product posterior and independence.**  In the planted observation representation
   $c_t=tX+B_t$, the posterior density factorizes into the base block and the $N$ spectator
   coordinates.  The covariance is block diagonal, while $p_t$, the tracked-cylinder perimeter,
   and $\tau_\eta$ depend only on the base block.  The base posterior process is independent of
   every spectator posterior process, which is exactly the independence used later at each fixed
   time.

4. **Common base event.**  Local exponential integrability gives uniform small-tilt
   $L^1$ continuity of the base posterior.  The reflected-Brownian union bound with
   $T_b\leq a^2/(8M\log(8M))$ makes the Brownian part of the base event have probability at least
   $1/2$; independence from $\{|X^0|\leq L\}$ gives $\mathbb P(G_b)\geq1/4$.  On $G_b$ one has
   $|c_s^0|\leq a$ for every $s\leq T_b$, hence $|p_s-1/2|<\eta$.  On the selected perimeter
   patch, the normalized tilt is at least $1/4$, so simultaneously
   $$
   \tau_\eta>T_b,
   \qquad
   P_s(E_0\times\mathbb R^N)\geq P_0/8.
   $$
   Neither this event nor $T_b$ depends on $N$.

5. **Fixed-time covariance spike.**  Klartag--Lehec Proposition 65 is used only in its proved
   event form.  The Gaussian-channel noise variance is exactly $s=1/t$, because
   $c_t/t=X+B_t/t\stackrel d=X+t^{-1/2}G$.  If $\log N\geq2/T$, then for each deterministic
   $t\in[T/2,T]$ separately,
   $$
   \mathbb P\!\left(\max_i v_{i,t}\geq c_{\rm sp}/t\right)
   \geq1-e^{-1/2}.
   $$
   No common or persistent spike event is inferred from the source.

6. **Exact-mass profile competitor.**  On a spectator spike, a $p_t$-quantile halfline in a
   high-variance posterior coordinate has full-product mass exactly $p_t$ and perimeter
   $f_{i,t}(q_{i,t})$.  Bobkov--Chistyakov Proposition 2.1 gives
   $\|f_{i,t}\|_\infty\leq v_{i,t}^{-1/2}$, so the intended comparison is
   $$
   I_{\mu_t}(p_t)\leq f_{i,t}(q_{i,t})
   \leq\sqrt{t/c_{\rm sp}}.
   $$
   This is an upper profile competitor and does not invoke the forbidden moving-profile lower
   bound.  The first inequality is not actually typeset in the audited source; the PDF prints the
   letters `le` instead.

7. **Tonelli and constants.**  Choosing
   $T\leq c_{\rm sp}P_0^2/256$ gives $e_t(E)\geq P_0/16$ on
   $G_b\cap H_t$, and block diagonality gives weight at least
   $c_{\rm sp}^{5/2}t^{-5/2}$.  Fixed-time base/spectator independence gives
   $\mathbb P(G_b\cap H_t)\geq h_{\rm sp}/4$.  Nonnegative Tonelli, not a persistent event,
   then yields
   $$
   \mathbb E\int_0^{T\wedge\tau_\eta}
   e_t(E)(1+\|A_t\|_{\rm op})^{5/2}\,dt
   \geq\kappa_{\rm sp}P_0T^{-3/2},
   $$
   where
   $$
   \kappa_{\rm sp}
   =\frac{h_{\rm sp}c_{\rm sp}^{5/2}}{96}(2^{3/2}-1).
   $$
   The factor is correct because
   $\int_{T/2}^Tt^{-5/2}dt=(2/3)(2^{3/2}-1)T^{-3/2}$.
   The two final small-$T$ inequalities separately dominate $CTP_0$ and
   $CT^{1+\gamma}$.  The construction respects the load-bearing order
   $$
   (C,T_0,\gamma,\eta,\delta)
   \longrightarrow(M,E_0,P_0,T_b)
   \longrightarrow T
   \longrightarrow N.
   $$

### Fences, hypotheses, and dependency closure

The proposition itself has no `bounded_by` edge.  The two fences on `q:weighted` are respected.
`obs:two-tail` is not contradicted: the proof retains the calibrated $5/2$ power and shows that
charging it through a global operator norm is tensor-unstable.  `obs:circularity` is avoided by
using an explicit upper profile competitor, not an unproved lower bound.  No implication among
`q:upgrade`, `q:stein-weighted`, and `q:alignment` is asserted.

The ledger lists exactly four dependencies, and all are discharged:

- `prop:covariance-spike` is a published import.  The event-level estimate was checked in the
  proof of Proposition 65 of Klartag--Lehec, *Bulletin of the American Mathematical Society* 62
  (2025), DOI `10.1090/bull/1869` (arXiv:2406.01324v2).
- `lem:one-dimensional-density-variance` is a published import.  The sharp inequality
  $1/12\leq v\|f\|_\infty^2\leq1$ was checked in Proposition 2.1 of Bobkov--Chistyakov,
  *Journal of Theoretical Probability* 28 (2015), DOI `10.1007/s10959-013-0504-1`.
- `prop:products` is proved and agent-reviewed.  Its factorization and product-KLS conclusion are
  also reconstructed directly here from Poincaré tensorization, the published one-dimensional
  log-concave Poincaré estimate, and the published reverse Cheeger--Poincaré comparison.
- `lem:half` is proved and agent-reviewed; symmetry and generalized concavity of the log-concave
  isoperimetric profile give $h_\nu=2I_\nu(1/2)$.

No preprint-unreviewed premise and no numerical artifact enters this proof.  The remaining facts
actually used are deterministic weighted-BV approximation/tube formulas, local exponential
integrability, the planted Gaussian posterior representation, the Brownian reflection principle,
and nonnegative Tonelli.  The density-change lemma should explicitly restrict to parameters for
which $0<Z(u,t)<\infty$; this is automatic in the small-tilt application but false for arbitrary
$u$ at $t=0$ for the one-sided exponential product.

## Corrections required before certification

1. At `solutions/prop-weighted-spectator-obstruction.tex:93-110`, name the initial BV competitor
   separately, for example $S^{(0)}$, and replace the malformed literal
   `\operatorname{Per}_\nu(S_k)longrightarrow \operatorname{Per}_\nu(S)` by
   `\operatorname{Per}_\nu(S_k)\longrightarrow
   \operatorname{Per}_\nu(S^{(0)})`.  After the exact-mass flow, explicitly rename the selected
   corrected regular approximant as the lemma's final $S$.  The current PDF contains the word
   `longrightarrow` rather than a convergence relation and leaves the role of $S$ ambiguous.

2. At `solutions/prop-weighted-spectator-obstruction.tex:74-80`, state that the tilted probability
   $\nu_{u,t}$ and its density-change identity are asserted whenever $0<Z(u,t)<\infty$.  For
   $t=0$, the exponential-product moment generating function is not finite for arbitrary $u$.

3. At `solutions/prop-weighted-spectator-obstruction.tex:240`, replace
   `$\sup_{|u|\le a,,t\le\bar T}$` by
   `$\sup_{|u|\le a,\ 0\le t\le\bar T}$`.

4. At `solutions/prop-weighted-spectator-obstruction.tex:343`, replace
   `I_{\mu_t}(p_t)le f_{i,t}(q_{i,t})` by
   `I_{\mu_t}(p_t)\le f_{i,t}(q_{i,t})`.  This is the critical profile comparison used at lines
   375--380; as built, equation (18) has no relation between the profile and the competitor.

5. Keep `checked_by: none`, record the repair author accurately, create a new append-only prover
   exploration, force a fresh standalone build, and inspect the resulting PDF rather than relying
   only on TeX's exit code.  A distinct proof-checker must then write a new review; this audit is
   immutable and cannot become proof provenance.

## Standalone build

The required standalone command was forced with

```text
cd solutions && latexmk -g -pdf -outdir=../build prop-weighted-spectator-obstruction.tex
```

and exited successfully.  The unresolved cross-module references are the expected standalone
subfile warnings, and both bibliography entries resolve.  Successful TeX compilation does not
clear the defects above: the generated PDF visibly prints
`Per(S_k)longrightarrow Per(S)` and `I_{\mu_t}(p_t)le f_{i,t}(q_{i,t})`.

## Exclusions and certification delta

No step remains mathematically unresolved after supplying the literal repairs above, but the
audited artifact itself is not a complete human-checkable proof.  This audit certifies neither
`prop:weighted-spectator-obstruction` nor a refutation of `q:weighted`.  It proposes no `solution`,
`checked_by`, `review`, status, ledger, manuscript, route, or gating delta.

It also does not check a replacement tensor-stable weight, an exact-minimizer-only gate, an
unstated near-worst-measure restriction, the weighted Stein-trace component of
`ass:weighted-package`, any claim in the trace-upgrade cluster, KLS itself, or the neighbouring
two-sided-exponential attribution in the product-stress discussion.

```yaml
outcome: revise
artifacts:
  - research/reviews/2026-08-27-prop-weighted-spectator-obstruction-proof-review.md
proposed_deltas:
  - none
next_role: prover
next_prompt: |
  Repair only solutions/prop-weighted-spectator-obstruction.tex and add a new append-only prover
  exploration; do not edit this audit, any existing exploration, the ledger, manuscript, routes,
  gating, or bibliography. At lines 93--110, name the initial BV competitor separately, typeset
  Per_nu(S_k) \longrightarrow Per_nu(S_initial), and explicitly rename the exact-mass corrected
  regular approximant as the lemma's final S. At lines 74--80, restrict nu_{u,t} and the
  density-change identity to 0<Z(u,t)<infinity. At line 240, change the malformed supremum to
  sup_{|u|<=a, 0<=t<=bar T}. At line 343, insert the missing \le between I_{mu_t}(p_t) and
  f_{i,t}(q_{i,t}). Preserve the theorem, the four dependency edges, the base -> T -> N order,
  fixed-time-only Klartag--Lehec use with s=1/t, exact-p_t quantile competitor, Tonelli argument,
  additive and relative near-minimality, and all scope exclusions. Keep checked_by: none and
  record every proof author/repair author accurately. Force the standalone LaTeX build and inspect
  the PDF formulas. Then request a new cold proof review by an agent distinct from every author;
  the new reviewer must persist a new append-only report and must not overwrite this audit.
```
