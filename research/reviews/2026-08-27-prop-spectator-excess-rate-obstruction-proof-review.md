---
verdict: pass
authors:
  - /root/prove_spectator_excess_rate_w2
reviewer: /root/review_spectator_excess_rate_w2
fingerprints:
  solutions/prop-spectator-excess-rate-obstruction.md: 9596ce5965ea49a577a2294f2814c6c18ba72fb3c570c7d695c71e784cb0dfb7
  prop:spectator-excess-rate-obstruction: 01dde6249073cccf904b9b0fcfa59aebf330ffeff4880e5b9850d36349c30d2a
  prop:covariance-spike: 161bf636e00b06d616360d86e08e775faacc85e3ebd8f62c91289807a22bfbb5
  lem:one-dimensional-density-variance: d815a2b4dd127f6904303d7af11bdff816a4ca70c21541afd80ebd41506343a6
  prop:products: 85b9ec9b7b81c783e52dce9f3edce41396f581da4f7a425bd3df9031860a6c8c
  lem:half: 1d4daf2283e1a1022580a067533d1cc3aae4194fa319d223aa00e4112d031a2f
---

# Spectator excess-rate obstruction — independent proof review

This is a cold review of `solutions/prop-spectator-excess-rate-obstruction.tex` at SHA-256
`b4bf91df9433ce54deb1d025fca4d3e9f978d0e0d3ec818f0d4cdcd986b334be`.  The proof was
reconstructed from the pinned dossier, the current manuscript and ledger statements, the four
declared dependency artifacts, the primary published sources, and the relevant obstruction and
product context.  The proof author is distinct from the reviewer, and no exploration names this
reviewer as an author.

## Findings

### Statement agreement and quantifiers

The dossier theorem at `solutions/prop-spectator-excess-rate-obstruction.tex:38`, Proposition
`prop:spectator-excess-rate-obstruction` at `modules/kls/27-eldan-open-targets.tex:64`, and the
ledger statement at `research/kls/ledger.yaml:773` agree mathematically.  For every proposed
$C,T_0,\gamma>0$, every $\eta\in(0,1/2)$, and every $\delta>0$, they produce one finite dimension,
one product of centered rate-one exponentials, one balanced finite-perimeter cylinder satisfying

$$
e_0(E)\leq\delta,
\qquad
\frac{e_0(E)}{I_\mu(1/2)}\leq\delta,
$$

and one $0<T\leq T_0$ for which

$$
\mathbb E\int_0^{T\wedge\tau_\eta}e_t(E)\,dt
>C\bigl(Te_0(E)+T^{1+\gamma}\bigr).
$$

The additional dossier conclusion $e_0(E)\leq1$ is stronger than the proposition and puts every
witness in the normalized cut class used by the nearby propagation gate.  Since a normalized
replacement weight $W_t\geq1$ can only increase the left-hand side, the unweighted theorem also
justifies the manuscript and ledger consequence that changing the covariance weight alone cannot
retain this uniform source-vanishing superlinear remainder.  No conclusion is made for weights
allowed to fall below one.

The logical negation has the correct order: the base is chosen after the proposed constants but
before $T$, the single violating $T$ is then chosen, and only afterward is the finite spectator
dimension selected.  Producing one such $T$ is exactly what negates an estimate required for every
$T\leq T_0$.

### Regular exact-mass base and near-minimality

Let $a_m=I_{\lambda^{\otimes m}}(1/2)$.  The exact identity
$(S\times\mathbb R)_r=S_r\times\mathbb R$ preserves mass and lower outer Minkowski perimeter and
gives $a_{m+1}\leq a_m$.  The certified product KLS bound gives
$h_{\lambda^{\otimes m}}\geq h_*>0$, and certified `lem:half` gives

$$
a_m=\frac12h_{\lambda^{\otimes m}}\geq a_*:=\frac{h_*}{2}>0.
$$

Thus $a_m\downarrow a_\infty\geq a_*$.  This is the only profile lower bound used: it is a
deterministic time-zero product floor for selecting the base, not a lower bound on the moving
localized profile.

The regularization lemma is valid in the exact noncompact exponential product.  Finite lower outer
Minkowski content dominates relative weighted BV perimeter.  Strict weighted-BV approximation on
compact truncations of $K_m=[-1,\infty)^m$, followed by a compactly supported flow through an
interior regular boundary patch, gives an exact-mass regular representative with arbitrarily small
perimeter loss.  For that representative the one-sided tube formula counts precisely
$\partial^*S\cap\operatorname{int}K_m$.  Support facets are not relative interfaces, and their
intersections with the regular interface are lower-dimensional, so there is no first-order
$\partial K_m$ term.  Multiplying the density by the finite positive continuous tilt $F_{u,t}$
multiplies the same relative perimeter measure by $F_{u,t}$.  In the application $t>0$ makes the
tilt bounded after completing the square, while $(u,t)=(0,0)$ at the initial endpoint.

Choose $M$ with $a_M-a_\infty<\varepsilon/2$ and an exact-half-mass regular $E_0$ with
$P_0\leq a_M+\varepsilon/2$.  Since $P_0\geq a_M\geq a_*$, every later cylinder
$E_0\times\mathbb R^N$ satisfies

$$
0\leq e_0(E_0\times\mathbb R^N)
=P_0-a_{M+N}<\varepsilon,
\qquad
\frac{e_0(E_0\times\mathbb R^N)}{a_{M+N}}
<\frac{\varepsilon}{a_*}.
$$

The strict choice

$$
\varepsilon<\min\left\{\delta,\delta a_*,1,
\frac{\kappa_{\rm sp}a_*}{4C}\right\}
$$

therefore proves both additive and relative $\delta$-near-minimality and $e_0\leq1$, uniformly in
the still-unselected spectator dimension.

### Planted posterior, filtrations, and the common base event

In the planted observation realization $c_t=tX+B_t$, Bayes' formula gives

$$
d\mu_t(x)=Z_t^{-1}e^{c_t\cdot x-t|x|^2/2}\,d\mu(x).
$$

The endpoint $c_t$ is sufficient for the observation filtration.  Because both prior and
likelihood factor across the base block and spectator coordinates, the posterior factorization
and block-diagonal covariance in dossier equation (8) are pathwise identities.  The full base
posterior process is a function only of $(X^0,B^0)$; the spectator posterior processes are
functions of the disjoint independent pairs $(X^i,B^i)$.  Hence the base and spectator
sigma-fields are independent as processes.  The cylinder distance identity makes $p_t$, the
tracked perimeter, and $\tau_\eta$ base-block measurable.

The finite base exponential product has a local exponential moment, so the normalized tilts
$F_{u,t}$ converge to one uniformly in $L^1$ as $(|u|,t)\to(0,0)$.  Choose a finite perimeter patch
with $\sigma_0(B_R)\geq P_0/2$.  The conditions

$$
\int e^{a|x|}\,d\lambda^{\otimes M}\leq2,
\qquad
aR+\frac{\bar T R^2}{2}\leq\log2
$$

give $F_{u,t}\geq1/4$ on that patch whenever $|u|\leq a$ and $t\leq\bar T$.

For

$$
G_b=\{|X^0|\leq L\}\cap
\left\{\max_j\sup_{s\leq T_b}|B_s^{0,j}|\leq\frac{a}{2\sqrt M}\right\},
$$

the reflection principle and union bound give

$$
\mathbb P(G_b)\geq\frac14
$$

under the displayed choice
$T_b\leq a^2/(8M\log(8M))$ and $T_bL\leq a/2$.  On $G_b$,
$|c_s^0|\leq a$ for all $s\leq T_b$.  The $L^1$ estimate controls the base mass, and the exact
density-change formula controls the perimeter, simultaneously yielding

$$
\tau_\eta>T_b,
\qquad
P_s(E_0\times\mathbb R^N)\geq\frac{P_0}{8}
\quad(0\leq s\leq T_b).
$$

Neither the event nor $T_b$ depends on $N$.  The auxiliary planted event need not itself belong to
the observation filtration; only its implication for the posterior path, its probability, and its
independence from spectator events are used.

### Deterministic-time spectator spike and exact-mass competitor

The proof of Proposition 65 in Klartag--Lehec gives the event-level estimate

$$
\mathbb P\!\left(
\|\operatorname{Cov}(X\mid X+\sqrt{s}G)\|_{\rm op}\geq c_{\rm sp}s
\right)
\geq1-\left(1-\frac12e^{-s}\right)^N.
$$

The source proof obtains the exact one-coordinate probability $\frac12e^{-s}$ from
$\{Y_i\geq s,G_i\geq0\}$ and then uses coordinate independence.  In localization,

$$
\frac{c_t}{t}=X+\frac{B_t}{t}\stackrel d=X+t^{-1/2}G,
$$

so the Gaussian-channel noise variance is exactly $s=1/t$.  If
$H_t=\{\max_i v_{i,t}\geq c_{\rm sp}/t\}$ and $\log N\geq2/T$, then for each deterministic
$t\in[T/2,T]$ separately,

$$
Ne^{-1/t}\geq Ne^{-2/T}\geq1,
\qquad
\mathbb P(H_t)\geq1-e^{-1/2}=:h_{\rm sp}.
$$

This is only a family of marginal fixed-time probability estimates.  No common or persistent
spike event is asserted.

At finite time the base posterior is equivalent to its prior, so $0<p_t<1$.  On $H_t$, take a
$p_t$-quantile halfline in a spectator coordinate with variance
$v_{i,t}\geq c_{\rm sp}/t$.  Its full-product cylinder has mass exactly $p_t$ and lower outer
Minkowski perimeter $f_{i,t}(q_{i,t})$.  Proposition 2.1 of Bobkov--Chistyakov gives
$v\|f\|_\infty^2\leq1$, hence

$$
I_{\mu_t}(p_t)
\leq f_{i,t}(q_{i,t})
\leq\|f_{i,t}\|_\infty
\leq v_{i,t}^{-1/2}
\leq\sqrt{\frac{t}{c_{\rm sp}}}.
$$

This is a pointwise upper bound using an explicit exact-mass competitor.  No lower bound on the
moving localized profile enters.

### Tonelli, the exact constant, and the final choices

On $[T/2,T]$, the choice $T\leq c_{\rm sp}P_0^2/256$ makes

$$
e_t(E)\geq\frac{P_0}{8}-\sqrt{\frac{t}{c_{\rm sp}}}
\geq\frac{P_0}{16}
$$

on $G_b\cap H_t$.  Base/spectator independence at each deterministic time gives
$\mathbb P(G_b\cap H_t)\geq h_{\rm sp}/4$.

The relevant maps are jointly measurable: the tracked perimeter is the surface integral of a
continuously parameterized density, the posterior moment ratios and $H_t$ are continuous in the
finite-time posterior parameters, and the isoperimetric value is universally measurable through
the standard Polish-BV formulation of the mass-constrained perimeter infimum.  Thus the completed
product measure supports Tonelli.  Since excess is nonnegative,

$$
\begin{aligned}
\mathbb E\int_0^{T\wedge\tau_\eta}e_t(E)\,dt
&=\int_0^T\mathbb E\bigl[e_t(E)\mathbf1_{\{t<\tau_\eta\}}\bigr]\,dt\\
&\geq\frac{P_0}{16}\frac{h_{\rm sp}}4\frac T2
=\frac{1-e^{-1/2}}{128}P_0T.
\end{aligned}
$$

Hence the dossier constant is exactly

$$
\kappa_{\rm sp}=\frac{1-e^{-1/2}}{128}.
$$

No time-event interchange other than nonnegative Tonelli is used.  The base choice gives

$$
Ce_0(E)<\frac{\kappa_{\rm sp}P_0}{4},
$$

and after the base is fixed one can choose a positive $T\leq\min\{T_0,T_b,
c_{\rm sp}P_0^2/256,1\}$ with

$$
CT^\gamma<\frac{\kappa_{\rm sp}P_0}{4}.
$$

Only then choose finite $N$ with $\log N\geq2/T$.  The strict final comparison is

$$
C\bigl(Te_0(E)+T^{1+\gamma}\bigr)
<\frac{\kappa_{\rm sp}P_0T}{2}
<\mathbb E\int_0^{T\wedge\tau_\eta}e_t(E)\,dt.
$$

The verified dependency order is therefore

$$
(C,T_0,\gamma,\eta,\delta)
\longrightarrow(\varepsilon,M,E_0,P_0,T_b)
\longrightarrow T
\longrightarrow(N,d,\mu,E).
$$

### Hypotheses, dependencies, and citation debt

Every stated theorem parameter is accounted for.  $C$ enters the base and final time margins;
$T_0$ bounds the selected time; $\gamma>0$ permits $T^\gamma\to0$; $\eta>0$ fixes the base
$L^1$ stability tolerance; and $\delta>0$ fixes the two near-minimality tolerances.  The upper
restriction $\eta<1/2$ is the manuscript's nondegenerate tight-window convention and is stronger
than the local stability calculation needs.  There is no used but unstated theorem hypothesis.

The four declared dependencies are closed.

- `prop:covariance-spike` is a `published` import.  Its exact event estimate was checked in the
  proof of Proposition 65 of Klartag--Lehec, *Bulletin of the American Mathematical Society* 62
  (2025), 575--642, DOI `10.1090/bull/1869` (arXiv:2406.01324v2).
- `lem:one-dimensional-density-variance` is a `published` import.  Proposition 2.1 of
  Bobkov--Chistyakov, *Journal of Theoretical Probability* 28 (2015), 976--988, DOI
  `10.1007/s10959-013-0504-1`, proves
  $1/12\leq v\|f\|_\infty^2\leq1$ for a log-concave density.
- `prop:products` is `proved` with agent certification in
  `research/reviews/2026-08-27-kls-geometry-models-repair-proof-review.md`.  Its time-zero
  dimension-free product Cheeger bound was reconstructed from Poincare tensorization, the
  published affine one-dimensional log-concave Poincare estimate, and the published reverse
  Cheeger--Poincare comparison.  Its elementary posterior factorization was also rechecked here.
- `lem:half` is `proved` with agent certification in
  `research/reviews/2026-08-25-kls-excess-bootstrap-r2-audit.md`, whose front matter is
  `type: proof-review` with `verdict: pass`.  Symmetry and generalized concavity of the
  log-concave isoperimetric profile give $h_\nu=2I_\nu(1/2)$.

No dependency is open, conditional, or `preprint-unreviewed`.  The redundant survey citation in
the product dossier is not a logical premise; the product review checked the needed facts in
published sources.  The remaining inputs--finite-dimensional weighted-BV approximation and tube
formulas, local exponential integrability, the planted Gaussian filter, the Brownian reflection
principle, and Tonelli--were checked directly in the form used here.  No numerical artifact or
empirical agreement supplies a proof step.

### Fences and compatibility

The target node has no formal `bounded_by` edge.  The nearby contextual fences and interfaces are
nevertheless respected.

- `obs:circularity`: the proof upper-bounds $I_{\mu_t}(p_t)$ with an explicit exact-mass
  spectator halfline.  It never assumes a lower isoperimetric bound for the moving posterior.
- `obs:two-tail`: the anisotropic two-tail construction and its $5/2$ weight calibration are not
  used or contradicted.  This is an independent unweighted rate obstruction.
- Product stress context: the fixed cut lives in the base block while the competitor lives in an
  independent spectator coordinate.  No cut-aware Riccati source, single-coordinate source
  budget, or persistent covariance occupation is inferred, so `cor:refutation` is untouched.
- Trace-upgrade cluster: no implication among `q:upgrade`, the high-rank part of
  `q:stein-weighted`, and `q:alignment` is asserted or used.

There is no conflict with `prop:trivial-excess`.  That proposition gives the order-$T$ upper bound
$(1+e_0)T$; this proof gives an order-$T$ lower bound with coefficient
$\kappa_{\rm sp}P_0$, and $P_0=I_\mu(1/2)+e_0\leq1+e_0$.  The result rules out only a coefficient
that vanishes uniformly with $e_0$ and $T^\gamma$.

There is also no conflict with the near-worst `thm:bootstrap`.  The construction supplies no
near-worst-measure premise, and the bootstrap retains the external measure-scale term
$h_\mu(T^{4/3}+\Xi_T)$ rather than the uniform superlinear remainder refuted here.  Finally, every
witness is a product of isotropic one-dimensional log-concave factors, so certified
`prop:products` gives a dimension-free KLS constant.  KLS does not assert this excess-propagation
rate.

### Standalone build and rendered inspection

From `solutions/`, the required command

```text
latexmk -pdf -outdir=../build prop-spectator-excess-rate-obstruction.tex
```

returned zero.  A forced rebuild with `-g -interaction=nonstopmode -halt-on-error` also returned
zero and produced a six-page PDF.  The dossier SHA-256 was unchanged.  Layout-preserving text and
all six rendered pages were inspected; the density-change formula, two BV convergence arrows,
two-variable supremum, covariance-spike event, exact profile comparison, time choice, constant
$1/128$, and final strict inequality all render correctly.  Both citations resolve.  The remaining
`??` marks are only the expected standalone cross-module references permitted by
`solutions/README.md`; there is no TeX error or malformed display.

After the mathematical review and before this report was added,
`python3 research/check_ledger.py` parsed 189 nodes and 660 labels but reported one unrelated
pre-existing control-plane error: `ass:weighted-package.refuted_by` names
`prop:weighted-spectator-obstruction` without the same node in `depends_on`.  This reviewer did not
edit the ledger.  The error does not involve the reviewed proposition or this report.  After this
report was added, a fresh rerun returned zero errors for 189 nodes and 660 labels; the unrelated
error had been resolved concurrently.  A final rerun after further concurrent repository changes
likewise returned zero errors.

## Corrections

None.

## Checked and unverified steps

Checked steps: dossier hash and author/reviewer separation; theorem/ledger/manuscript agreement;
all theorem quantifiers; lower-Minkowski cylinder identity; monotone positive half-profile limit;
exact-mass weighted-BV regularization; support-boundary convention and posterior density change;
uniform additive and relative near-minimality; planted posterior representation and endpoint
sufficiency; base/spectator process and sigma-field independence; common base mass/perimeter event;
Brownian probability constant; deterministic-time covariance spike; exact $s=1/t$ conversion;
$\log N\geq2/T$; exact-$p_t$ quantile competitor; density--variance inequality; joint
measurability; nonnegative Tonelli; the exact constant
$(1-e^{-1/2})/128$; the two strict smallness choices; base-before-$T$-before-$N$ order; hypothesis
accounting; dependency closure and publication classification; formal and contextual fences;
compatibility with `prop:trivial-excess`, `thm:bootstrap`, and product KLS; and the standalone
source/PDF.

Unverified steps inside the certified scope: none.

## Exclusions

This review does not certify a particular replacement covariance weight, a weight allowed below
one, a gate restricted to near-worst measures, a source-deficit formulation, an exact-minimizer-only
statement, any weighted Stein-trace estimate, any persistent spike or covariance-occupation bound,
any lower bound for a moving localized profile, any implication in the trace-upgrade cluster, KLS
itself, or any numerical artifact.  It does not recertify the four dependency nodes, any other
ledger node, the full manuscript, the bibliography, or the unrelated concurrent ledger repair.
Dossier-header, manuscript, ledger, route, gating, bibliography, exploration, knowledge, and prior
review edits remain outside this reviewer's write surface.

## Proposed certification delta

The dossier header may change exactly as follows, leaving the author and all mathematical fields
unchanged:

```text
% checked_by  : agent
% reviewer    : /root/review_spectator_excess_rate_w2
% review      : research/reviews/2026-08-27-prop-spectator-excess-rate-obstruction-proof-review.md
```

Because every premise is discharged, the target node may take unconditional `proved` status with
the following atomic field delta, leaving its statement and four dependency edges unchanged:

```yaml
status: proved
solution: solutions/prop-spectator-excess-rate-obstruction.tex
checked_by: agent
review: research/reviews/2026-08-27-prop-spectator-excess-rate-obstruction-proof-review.md
```

```yaml
outcome: complete
artifacts:
  - research/reviews/2026-08-27-prop-spectator-excess-rate-obstruction-proof-review.md
proposed_deltas:
  - "For prop:spectator-excess-rate-obstruction, set status: proved, solution: solutions/prop-spectator-excess-rate-obstruction.tex, checked_by: agent, and review: research/reviews/2026-08-27-prop-spectator-excess-rate-obstruction-proof-review.md; preserve its statement and depends_on edges."
  - "Update only the dossier provenance header to checked_by: agent, reviewer: /root/review_spectator_excess_rate_w2, and the new review path; preserve the pinned mathematical bytes."
next_role: orchestrator
next_prompt: |
  Confirm that solutions/prop-spectator-excess-rate-obstruction.tex still has SHA-256
  b4bf91df9433ce54deb1d025fca4d3e9f978d0e0d3ec818f0d4cdcd986b334be. Then apply exactly the
  dossier-header and target-node certification deltas displayed above, preserving the theorem,
  statement, four dependency edges, and append-only review history. Run
  python3 research/check_ledger.py after the atomic update and keep it at zero errors.
```
