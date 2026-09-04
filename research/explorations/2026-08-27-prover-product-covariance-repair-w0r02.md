---
type: exploration
date: "2026-08-27"
outcome: proposed
nodes:
  - lem:block
  - thm:budget
  - cor:refutation
  - lem:product-qcts
  - cor:KI-discharged
---
# Prover repair: product covariance dossier

Date: 2026-08-27

Role: `prover`

Concurrency key: `solution:kls-product-covariance`

Author provenance: original author `/root/kls_proof_audit`; repair author
`/root/repair_product_dossier`

Dossier: `solutions/kls-product-covariance.tex`

Status: complete candidate repair with `checked_by: none`; the current bytes have no proof
certification until a distinct cold reviewer audits all five nodes.

## Scope and source audit

The shared dossier covers exactly these ledger nodes:

1. `lem:block`;
2. `thm:budget`;
3. `cor:refutation`;
4. `lem:product-qcts`;
5. `cor:KI-discharged`.

The first three have manuscript anchors in `modules/kls/22-product-stress.tex`; the last has its
anchor in `modules/kls/15-covariance-technology.tex`. The quadratic-chaos lemma is also in
`modules/kls/22-product-stress.tex`. None of these five nodes carries a formal `bounded_by`
edge.

The repair found two genuine specification omissions in the former dossier:

- the conditional means and covariances in `lem:block` require a nontrivial cut and finite
  second moments, but the former theorem statement assumed only a product probability measure;
- `thm:budget` used the stopping time $\tau$ without defining it inside the standalone dossier.

The repaired block lemma now assumes that $\nu=\bigotimes_i\nu_i$ has finite second moment and
$0<\nu(E)<1$. These are domain hypotheses, not a mathematical downgrade: without them the
two-color quantities in the conclusion are not all defined. The coordinate-budget theorem now
defines

$$
\tau=\inf\{t\ge0:p_t\notin[1/3,2/3]\},\qquad\inf\varnothing=\infty,
$$

and states $p_0=\mu(E)\in[2/5,3/5]$ and $q_0=1-p_0$ explicitly. The fixed-coordinate
corollary spells out that its word "balanced" means the same interval.

## Analytic audit of `lem:block`

Since $E$ is measurable with respect to $(X_j)_{j\in J}$, the outside vector
$(X_i)_{i\notin J}$ is independent of both that vector and $\mathbf 1_E$. Hence its law is
unchanged after conditioning on either $E$ or $E^c$, and it remains independent of the
inside coordinates under either conditional law. Therefore

$$
\delta_i=0\quad(i\notin J),
$$

the conditional cross-covariances vanish when one index is outside $J$ and the other is
inside, and the two conditional covariance matrices agree on the outside block. It follows
that $G$ is supported on $J\times J$. Since $\delta\delta^T$ has the same support, so is
$K=G+(q-p)\delta\delta^T$.

Finite second moment makes every displayed conditional covariance finite, while
$0<\nu(E)<1$ makes both colors meaningful. Along localization, the likelihood is strictly
positive relative to the initial law at every finite time, so the initially nontrivial cut
continues to have $0<p_t<1$; the Gaussian factor gives finite posterior moments.

## Analytic audit of `thm:budget`

The theorem assumes a product of isotropic one-dimensional log-concave factors and a fixed cut
measurable with respect to a fixed set $J$ of $k$ coordinates. Product structure persists
pathwise. Block support therefore gives

$$
S_t=s_t\|G_t\|_{\mathrm{HS}}^2
=\sum_{i\in J}s_t|G_te_i|^2.
$$

The certified per-direction estimate, summed only over those fixed columns, yields

$$
\mathbb E\int_0^\infty S_t\,dt
\le\sum_{i\in J}(R_0)_{ii}\le k,
$$

because $0\preceq R_0\preceq A_0=I$.

For the stopped information-rate estimate, take an increasing bounded localizing sequence
$\sigma_m$ for the local martingale in

$$
dr_t=dM_t+(S_t-D_t)dt,
\qquad D_t\ge0.
$$

Expectation at $t\wedge\tau\wedge\sigma_m$, followed by Fatou on the nonnegative terminal
value and monotone convergence for the source, gives

$$
\mathbb E r_{t\wedge\tau}
\le r_0+\mathbb E\int_0^{t\wedge\tau}S_u\,du
\le1+k.
$$

Here $B_0\preceq I$ and $B_0$ has rank at most one, so $r_0\le1$. No unlocalized local
martingale is assigned expectation zero.

The mass martingale satisfies

$$
[p]_{T\wedge\tau}=\int_0^{T\wedge\tau}s_tr_t\,dt.
$$

Since $s_t\le1/4$ and
$\mathbf1_{\{t<\tau\}}r_t\le r_{t\wedge\tau}$,

$$
\mathbb E[p]_{T\wedge\tau}
\le\frac{(1+k)T}{4}.
$$

The interval $[2/5,3/5]$ is at distance $1/15$ from the complement of
$[1/3,2/3]$. Continuity and Doob's $L^2$ maximal inequality consequently give
$\mathbb P(\tau\le T)\le C_0(1+k)T$. At
$T_k=[2C_0(1+k)]^{-1}$ the posterior survives with probability at least $1/2$, and then has
mass in $[1/3,2/3]$. Posterior $T_k$-uniform log-concavity and the fixed-set perimeter
supermartingale give

$$
\mu^+(E)\ge \frac{c}{\sqrt{1+k}}
\ge \frac{c}{\sqrt{1+k}}\min(p_0,q_0),
$$

after adjusting the universal constant.

The balance interval is used only by the survival/boundary part. The total source budget in
part (i) works for every nontrivial cut, and the stopped Riccati estimate in part (ii) does not
use the nested distance. The dossier deliberately retains the manuscript's packaged balanced
statement rather than silently promoting those stronger subparts to a new ledger claim.

For general product log-concave factors, the stochastic identities are first used under bounded
localization. Product-preserving coordinatewise approximation handles the localization
construction and Fatou handles the nonnegative occupation. For the only perimeter passage, the
fixed-set inequality
$\mathbb E\mu_T^+(E)\le\mu^+(E)$ follows directly by applying Fatou to the likelihood
martingale on outer neighborhoods of $E$; if the initial perimeter is infinite, the boundary
claim is immediate.

## Audit of the three collateral nodes

### `cor:refutation`

The corollary now explicitly inherits $p_0\in[2/5,3/5]$, a cut and coordinate chosen before
localization, and a deterministic threshold $L$. Setting $k=1$ gives the budget and boundary
bound. Tonelli and

$$
\mathbf1_{\{S_t\ge L^2/2\}}\le\frac{2S_t}{L^2}
$$

give expected occupation at most $2/L^2$. The result still does not cover a cut, coordinate, or
level selected after seeing the localization path, nor the literal interval-by-interval
all-cut Carleson estimate. There is no mathematical downgrade.

### `lem:product-qcts`

For centered independent factors and symmetric $M$,

$$
\operatorname{Var}(Y^TMY)
=\sum_iM_{ii}^2\operatorname{Var}(Y_i^2)
+4\sum_{i<j}M_{ij}^2\sigma_i^2\sigma_j^2.
$$

Every omitted cross-covariance has a centered singleton factor. The one-dimensional
log-concave fourth-moment estimate gives
$\operatorname{Var}(Y_i^2)\le(C_4-1)\sigma_i^4$, hence the claimed bound with
$C_*=\max\{C_4-1,2\}$. The argument remains valid for each centered product posterior. No
statement or proof change was needed.

### `cor:KI-discharged`

For $n\ge3$, the published sup-over-time input gives

$$
\mathbb P\!\left(\sup_{0\le s\le t}\|A_s\|_{\mathrm{op}}\ge2\right)
\le e^{-1/(Ct)},
\qquad t\le(C\log^2n)^{-1}.
$$

Together with the pathwise Brascamp--Lieb cap
$\|A_t\|_{\mathrm{op}}\le t^{-1}$, this yields

$$
\mathbb E\|A_t\|_{\mathrm{op}}
\le2+t^{-1}e^{-1/(Ct)}
\le2+C/e.
$$

At $t=0$, $A_0=I$. Choosing $c_0\le C^{-1}$ gives exactly `hyp:KI` with $C_2=2$. No Letwin
preprint input is used and no mathematical change was needed.

Because all five nodes share one dossier, changing its bytes invalidates the applicability of
the old review to all five, even though these three proofs were unchanged. Their mathematical
content survives the audit, but each needs inclusion in the new cold review before the current
dossier can again carry `checked_by: agent`.

## Dependencies, consumers, and balance reconciliation

The accepted dependency closure is unconditional:

- `thm:budget` uses `lem:block`, `cor:per-direction`, `thm:scalar-riccati`, and
  `prop:products`, all currently proved and agent-certified;
- `cor:refutation` uses `thm:budget`;
- `cor:KI-discharged` uses the published imported `thm:KL-window` and the posterior
  Brascamp--Lieb cap;
- `lem:block` and `lem:product-qcts` have no ledger dependencies.

The consumers were checked one by one.

- `cor:refutation` inherits the balance interval explicitly in the repaired dossier.
- The residual paragraph leading to `q:alignment` already assumes a fixed balanced cut, and
  `q:alignment` itself quantifies only over balanced cuts.
- The trace-upgrade comparison in `modules/kls/27-eldan-open-targets.tex` refers to the
  per-coordinate source budgets only inside that same product-cut setting; it makes no
  unbalanced boundary claim.
- The product case of `thm:covariance-bound` cites "a product as in `thm:budget`" only to select
  the initial measure class. Its actual proof uses `lem:product-qcts` and is valid for every
  nontrivial cut on the coarse window; it does not consume the budget theorem or its balance
  hypothesis.
- `obs:rank-one-refuted` consumes the explicitly fixed balanced-cut corollary.
- `thm:covariance-bound` consumes the unchanged `lem:product-qcts`, and `cor:loglog` consumes
  the unchanged `cor:KI-discharged`.

For exact manuscript/ledger agreement, the orchestrator should consider the following source
sync after review. These are statement-clarification proposals, not certification deltas and
were not applied by this role.

1. In manuscript `lem:block`, replace its opening sentence by:

   > Let $\nu$ be a product probability measure on $\mathbb R^n$ with finite second moment,
   > and let $E$ be measurable with respect to the coordinates in
   > $J\subset\{1,\dots,n\}$. Assume $0<\nu(E)<1$.

2. In manuscript `cor:refutation`, replace "any fixed balanced cut" by "any fixed cut with
   $p_0\in[2/5,3/5]$".

3. In the product clause of manuscript `thm:covariance-bound`, replace "when $\mu$ is a
   product as in Theorem `thm:budget`" by "when $\mu$ is a product of isotropic
   one-dimensional log-concave measures". This makes clear that only the measure class, not
   the cut-balance hypothesis, is imported.

4. Clarify the ledger summaries, without changing their logical strength, to:

   - `lem:block`: "For a finite-second-moment product $\nu$ and a nontrivial
     $J$-measurable cut, $\delta_i=0$ off $J$ and $G,K$ are supported on $J\times J$."
   - `thm:budget`: "For $p_0\in[2/5,3/5]$, a $k$-coordinate cut of a product has
     $\mathbb E\int_0^\infty S_tdt\le k$,
     $\mathbb E r_{t\wedge\tau}\le1+k$ for the coarse balanced exit time, and
     $\mu^+(E)\ge c\min(p_0,q_0)/\sqrt{1+k}$."
   - `cor:refutation`: "For a cut with $p_0\in[2/5,3/5]$ and one coordinate fixed before
     localization, the rank-one dynamic two-tail candidate is refuted: total source budget is
     at most one and deterministic-level spikes self-extinguish at rate $O(\Lambda^{-2})$; no
     pathwise adaptive choice is covered."

No other consumer requires a hypothesis change.

## Fence check, gaps, and logical status

There are no formal `bounded_by` edges on these five nodes. The nearby rank-one fence was
checked explicitly: `cor:refutation` covers only fixed pre-localization choices and a
deterministic source level. It does not rule out the high-rank, path-adapted incidence problem
in `q:alignment`. The proofs use no projection-to-tensor upgrade, no all-measure relative
covariance bound, no changing isoperimetric profile, and no numerical evidence.

Hypotheses actually used are all now stated in the dossier:

- finite second moments and $0<\nu(E)<1$ for the block lemma;
- isotropic one-dimensional log-concave product factors, a fixed $J$-measurable cut, and
  $p_0\in[2/5,3/5]$ for the packaged budget theorem;
- fixed pre-localization cut/coordinate and deterministic threshold for the refutation;
- centering, product independence, one-dimensional log-concavity, and symmetric $M$ for the
  quadratic-chaos lemma;
- isotropic log-concavity, $n\ge3$, the published sup-time covariance window, and posterior
  Brascamp--Lieb for the `hyp:KI` discharge.

No analytic step remains unclosed in the repaired statements. All five results are
unconditional relative to their already proved or published dependencies. The dossier itself
remains an unchecked candidate with `checked_by: none`; the author does not certify it.

## Build and certification disposition

The required standalone command

```bash
cd solutions && latexmk -pdf -outdir=../build kls-product-covariance.tex
```

returned exit code 0 and produced `build/kls-product-covariance.pdf` (four pages). The log has
no TeX error, overfull box, underfull box, or package warning. Its warnings are only the expected
standalone references to labels in manuscript subfiles; the console also reports the expected
missing citation-link destination because standalone dossiers deliberately do not print the
shared bibliography.

There is no applicable ledger certification delta while `checked_by: none`. The future
`solution: solutions/kls-product-covariance.tex` is only a deferred artifact candidate until a
distinct reviewer passes all five current proofs. The ledger's historical certification fields
still point to the older review, but that review predates these bytes and must not be treated as
certifying this repair.

```yaml
outcome: complete
artifacts:
  - solutions/kls-product-covariance.tex
  - research/explorations/2026-08-27-prover-product-covariance-repair-w0r02.md
proposed_deltas:
  - no applicable ledger certification delta while checked_by is none; the exact manuscript and ledger statement-clarification proposals are recorded above for orchestrator synchronization after review
next_role: proof-checker
next_prompt: |
  Cold-review the current bytes of `solutions/kls-product-covariance.tex`, independently of
  original author `/root/kls_proof_audit` and repair author
  `/root/repair_product_dossier`. Audit all five nodes: `lem:block`, `thm:budget`,
  `cor:refutation`, `lem:product-qcts`, and `cor:KI-discharged`. The old
  `research/reviews/2026-08-25-kls-geometry-product-r2-audit.md` predates the repaired bytes and
  supplies no certification for this review.

  For `lem:block`, verify that finite second moment and `0<nu(E)<1` are exactly sufficient to
  define all two-color moments, and that conditioning a product law on a J-measurable event
  leaves the outside block unchanged and independent. For `thm:budget`, verify product
  persistence, finite-time nontriviality of the cut, the exact column sum from the certified
  per-direction estimate, the bounded localizing sequence and Fatou/monotone-convergence
  removal in the scalar Riccati step, `r_0<=1`, the explicitly defined coarse exit time
  `tau=inf{t:p_t notin [1/3,2/3]}`, the stopped quadratic-variation estimate, the distance
  `1/15`, Doob's inequality, posterior uniform-convexity isoperimetry, and the fixed-set
  perimeter supermartingale/regularization passage. Confirm the packaged theorem assumes
  `p_0 in [2/5,3/5]`, although its source-budget subpart is stronger.

  For `cor:refutation`, confirm it retains `p_0 in [2/5,3/5]`, a cut and coordinate chosen
  before localization, and a deterministic level; it must not claim an adaptive or
  interval-by-interval refutation. For `lem:product-qcts`, recompute every covariance in the
  diagonal/off-diagonal expansion and the coefficient
  `C_*=max(C_4-1,2)`. For `cor:KI-discharged`, check the published sup-over-time event, its
  range `n>=3` and `t<=1/(C log^2 n)`, the bad-event use of `||A_t||<=1/t`, the uniform
  maximization `t^{-1}exp(-1/(Ct))<=C/e`, and the endpoint `A_0=I`; exclude all Letwin-v1
  input.

  Check the full dependency closure and every consumer described in
  `research/explorations/2026-08-27-prover-product-covariance-repair-w0r02.md`. In particular,
  reconcile the budget theorem's balance hypothesis with `cor:refutation`, the residual
  `q:alignment` prose, the trace-upgrade comparison, and the product clause of
  `thm:covariance-bound`. Verify the exact proposed source clarifications before recommending
  them to the orchestrator. None of the five nodes has a formal `bounded_by` edge; nevertheless
  check that the result respects the downstream `obs:rank-one-refuted` scope and asserts
  nothing about adaptive high-rank occupation.

  Re-run `cd solutions && latexmk -pdf -outdir=../build kls-product-covariance.tex`. If and only
  if every node and the shared regularization discussion pass, persist a new structured review
  naming both authors and yourself as a distinct reviewer, covering all five nodes and the
  current dossier bytes. Return any manuscript/ledger synchronization proposal to the
  orchestrator; do not edit the dossier, manuscript, routes, or ledger. On failure, return a
  verbatim `next_prompt` listing every defect for the repair author.
```
