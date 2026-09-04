---
type: exploration
date: "2026-08-27"
outcome: proposed
nodes:
  - q:alignment
  - q:stein-weighted
  - q:upgrade
  - thm:letwin-qcts
---
# Synthesis: first parallel KLS gate wave

Date: 2026-08-27

Role: `synthesizer`

Concurrency key: singleton `knowledge`, granted by the orchestrator after the three probes
completed

Sources converged:

- `research/explorations/2026-08-27-kls-route-prober-upgrade-par-01.md`;
- `research/explorations/2026-08-27-kls-route-prober-mm-spectral-occupation-par-02.md`;
- `research/explorations/2026-08-27-kls-route-prober-uniform-cmh-approximants-par-03.md`;
- the live KLS ledger, route registry, gating file, manuscript anchors, and cited certified
  dossiers/reviews.

No numerical result is used. The three target gates remain open. This synthesis changes no
ledger, manuscript, route-control file, bibliography, dossier, review, or instance-registry
entry.

## Live-state audit

`python3 research/check_ledger.py status` reports the first-wave targets exactly as follows:

- `q:upgrade`: `open`;
- `q:mm-spectral-occupation`: `open`;
- `ass:uniform-cmh-approximants`: `open`;
- `q:cmh-approximation`: `conditional`, with a certified dossier and independent review;
- `q:mm-invariant-lift`, `q:mm-square-root-commutator`, `q:stein-weighted`, and `q:alignment`:
  `open`.

The intrinsic quadratic-Poincar\'e inputs `thm:letwin-qcts` and
`thm:letwin-moment-map` remain imported from an unreviewed version-1 preprint. Consequently both
stochastic low-covariance estimates below are preprint-conditional. In particular, the phrase
"maximal unconditional extraction" after equation (9) of the spectral probe must be read as
"maximal algebraic extraction conditional on (2)"; equations (8)--(9) explicitly use that
conditional input. The exact posterior-defect identities themselves do not.

## Common normalization

The duplicate algebra in the two stochastic probes has one abstract form. Let $A\succeq0$ be
the current posterior covariance, let
$$
X=A^{1/2}ZA^{1/2},\qquad
P_L=\mathbf1_{(L,\infty)}(A),\qquad Q_L=I-P_L,
$$
with $X=X^T$. Orthogonality of the four matrix blocks gives
$$
\|X\|_{\mathrm{HS}}^2
=\|Q_LXQ_L\|_{\mathrm{HS}}^2
+\underbrace{\|P_LXP_L\|_{\mathrm{HS}}^2
+2\|P_LXQ_L\|_{\mathrm{HS}}^2}_{\mathcal I_L(X)},
\tag{N1}
$$
while spectral calculus gives
$$
\|Q_LXQ_L\|_{\mathrm{HS}}^2\le L^2\|Z\|_{\mathrm{HS}}^2.
\tag{N2}
$$
Thus an intrinsic estimate bounds only the low--low block. It leaves the complete Euclidean
energy incident to the inflated covariance space, including both high--low entries, in
$\mathcal I_L(X)$. No differentiation of $P_L$ occurs in (N1)--(N2).

| stream | $X$ and intrinsic tensor $Z$ | low block | exact residue | budget that must absorb the residue |
|---|---|---|---|---|
| all-cut `q:upgrade` | $X_t=\sqrt{s_t}K_t$, $Z_t=\sqrt{s_t}A_t^{-1/2}K_tA_t^{-1/2}$ | $\le8L^2$, conditional on `thm:letwin-qcts` | $\mathcal H^K_{t,L}=\mathcal I_L(\sqrt{s_t}K_t)$ | interval density, $r_t$, and less than $D_t/12$ before the $G$--$K$ correction |
| spectral `q:mm-spectral-occupation` | $X_t=H_t$, $Z_t=A_t^{-1/2}H_tA_t^{-1/2}$ | $\le8L^2v_t$, conditional on `thm:letwin-qcts` | $\mathcal R_{t,L}=\mathcal I_L(H_t)$ | $C_Ht$, $\int\mathbb E|g_t|^2$, and a strict fraction of the high damping $2g_t^TP_LA_tP_Lg_t$ |
| product `q:alignment` | $X_t=\sqrt{s_t}G_t$ and $P_t^H$ is the coordinate mask $A_t^{(i)}\ge2$ | not supplied by (N2) in the node statement | $S_t^H$ has the same incident-block formula as (N1), with the node's $\ge2$ coordinate mask | the all-cut interval budget, but only for two-sided-exponential products |
| CMH linear sector | after global whitening $\Sigma_k=I$, test $H_k$ against a fixed $P_a=a\otimes a$ | the aligned scalar term $\mathbb E(a^TH_ka)^2$ is bounded by the constant-matrix input | $\frac12\mathbb E\|[P_a,H_k]\|_{\mathrm{HS}}^2$ | no stochastic-time budget exists; genuine Monge--Amp\`ere/Codazzi structure must give a static operator bound |
| weighted Stein `q:stein-weighted` | a localized boundary/Jacobi trace, not an $A^{1/2}ZA^{1/2}$ tensor identified in either probe | no common low block has been proved | high-rank mean-zero boundary modes and Reilly terms | the covariance-weighted almost-stability estimate required by `ass:weighted-package` |

The first two rows instantiate the same deterministic block lemma, now promoted with guardrails
to `research/knowledge/lemmas.md`. They do **not** instantiate the same stochastic process:
$K_t$ is cut-dependent and differs from the Riccati source tensor $G_t$, whereas $H_t$ is tied to
a fixed eigenfunction. Their lower-order terms and damping are different.

## Correction terms and commutator residues are distinct

### Cut correction

On the coarse balanced window, the upgrade probe proves the pointwise algebra
$$
s_t\|G_t\|_{\mathrm{HS}}^2
\le3s_t\|K_t\|_{\mathrm{HS}}^2+\frac34D_t.
\tag{E1}
$$
Together with (N1)--(N2), this would turn an estimate on $\mathcal H^K_{t,L}$ with damping
coefficient $\beta<1/12$ into the required all-cut estimate. This reduction uses the
preprint-conditional intrinsic bound for its low block and has no dossier of its own.

### Moving spectral projector

For $F_t=\chi(A_t)$, It\^o differentiation creates
$D\chi(A_t)[\mathcal T_{t,k}]g_t$,
$D^2\chi(A_t)[\mathcal T_{t,k},\mathcal T_{t,k}]g_t$, and mixed contractions with $H_t$.
These are dynamic errors caused by the random covariance eigenspaces. They are not the algebraic
commutator $[P_a,H_k]$, and (N1) itself creates none of them because it is used only at a fixed
state.

### Static CMH commutator

The certified normalization dossier proves, for symmetric $B,H$,
$$
\operatorname{Tr}(B^2H^2)
=\operatorname{Tr}(BHBH)+\frac12\|[B,H]\|_{\mathrm{HS}}^2.
\tag{C1}
$$
For $B=P_a$, this is the exact split
$$
\mathbb E|H_ka|^2
=\mathbb E(a^TH_ka)^2
+\frac12\mathbb E\|[P_a,H_k]\|_{\mathrm{HS}}^2.
\tag{C2}
$$
The certified algebraic countermodel `prop:letwin-not-gate-zero` proves that positivity,
$\mathbb EH=I$, and all constant-matrix inequalities do not control the second term. Its law is
not a moment-map Hessian, so it is a method obstruction rather than a refutation of gate zero.

### Square-root/Haar commutator

The formal error
$[N^{1/2},K_M]N^{1/2}u$ in `q:mm-square-root-commutator` is an operator/core and complete-tree
problem downstream of `q:mm-invariant-lift`. Equation (C2) is a static floor on orientation loss,
not a proof that this formal error equals, bounds, or is bounded by $[P_a,H_k]$. The two
commutators are recorded separately in shared knowledge.

## Directional implication table

Write:

- $E_K$ for the proposed all-measure incident-high $K$ occupation estimate in the upgrade probe;
- $S_f$ for the proposed eigenfunction high-incidence estimate in the spectral probe;
- $C_{\mathrm{stat}}$ for a genuine-moment-map uniform bound on the static commutator in (C2);
- $W_J$ for the weighted Jacobi/Reilly statement of `q:stein-weighted`;
- $A_{\mathrm{prod}}$ for the product-only $G$-tensor estimate of `q:alignment`.

The status words in this table concern the displayed direction, not similarity of proof shape.

| direction | status | reason |
|---|---|---|
| $E_K\Rightarrow S_f$ | not even conjectured | fixed cuts do not produce first eigenfunctions or their damping |
| $S_f\Rightarrow E_K$ | not even conjectured | eigenfunction tensors do not control every fixed cut |
| $E_K\Rightarrow C_{\mathrm{stat}}$ | not even conjectured | dynamic cut occupation gives no canonical-Hessian commutator bound |
| $C_{\mathrm{stat}}\Rightarrow E_K$ | not even conjectured | a stationary linear-sector estimate gives no cut-time occupation theorem |
| $E_K\Rightarrow W_J$ | not even conjectured | no bridge from the posterior $K$ tensor to Jacobi/Reilly boundary modes is proved |
| $W_J\Rightarrow E_K$ | not even conjectured | `rem:trace-upgrade-unification` records only shared difficulty, not this implication |
| $E_K\Rightarrow A_{\mathrm{prod}}$ | open | the probe gives a candidate one-way route via (E1), the conditional low block, and full all-cut Carleson; there is no dossier and no edge |
| $A_{\mathrm{prod}}\Rightarrow E_K$ | not even conjectured | the premise is product-only, uses $G$ rather than $K$, and cannot yield the all-measure statement |
| $S_f\Rightarrow C_{\mathrm{stat}}$ | not even conjectured | the localization tensor of an eigenfunction is not the canonical moment Hessian |
| $C_{\mathrm{stat}}\Rightarrow S_f$ | not even conjectured | the static CMH linear sector has no spectral-time damping interface |
| $S_f\Rightarrow W_J$ | not even conjectured | no eigenfunction-to-boundary-mode transform is stated |
| $W_J\Rightarrow S_f$ | not even conjectured | no boundary-mode-to-eigenfunction tensor transform is stated |
| $S_f\Rightarrow A_{\mathrm{prod}}$ | not even conjectured | tensorization sanity does not turn a first eigenfunction into every balanced product cut |
| $A_{\mathrm{prod}}\Rightarrow S_f$ | not even conjectured | a product fixed-cut estimate has neither the scope nor object needed by Route S |
| $C_{\mathrm{stat}}\Rightarrow W_J$ | not even conjectured | static target-coordinate algebra does not control localized boundary Reilly terms |
| $W_J\Rightarrow C_{\mathrm{stat}}$ | not even conjectured | no moment-map-Hessian reconstruction from the boundary trace is available |
| $C_{\mathrm{stat}}\Rightarrow A_{\mathrm{prod}}$ | not even conjectured | the two statements concern different measures, tensors, and time structures |
| $A_{\mathrm{prod}}\Rightarrow C_{\mathrm{stat}}$ | not even conjectured | the product cut model gives no genuine-moment-map differential estimate |
| $W_J\Rightarrow A_{\mathrm{prod}}$ | not even conjectured | common trace language supplies no formal product-cut implication |
| $A_{\mathrm{prod}}\Rightarrow W_J$ | not even conjectured | the product incident-high bound does not control Jacobi zero modes or Reilly errors |
| $C_{\mathrm{stat}}\Rightarrow q{:}\mathrm{mm\mbox{-}square\mbox{-}root\mbox{-}commutator}$ | not even conjectured | the static identity is only a difficulty floor, not the full Haar estimate |
| $q{:}\mathrm{mm\mbox{-}square\mbox{-}root\mbox{-}commutator}\Rightarrow C_{\mathrm{stat}}$ | not even conjectured | the live square-root node has no proved consumer or linear-sector corollary |

Two within-stream implications should not be confused with the table:

| implication | status | guardrail |
|---|---|---|
| a bound $\mathbb E\|[P_a,H_k]\|_{\mathrm{HS}}^2\le C_0$ plus the Letwin constant-matrix input gives $\mathbb E|H_ka|^2\le2+C_0/2$ | proved (dossier) | the algebra is certified in `solutions/thm-cmh-normalization.tex`; the numerical constant-matrix input remains an unreviewed import |
| `ass:uniform-cmh-approximants` plus the certified approximation dossier gives the affine Poincar\'e limit with the same constant | proved (dossier) | this is the existing `conditional` node `q:cmh-approximation`; its premise remains open |
| $E_K$ with $\beta<1/12$ gives `ass:all-cut-carleson` through (E1) and the low block | open | probe derivation only; low block is preprint-conditional and no dossier exists |
| $S_f$ gives `q:mm-spectral-occupation` after the low-block extraction | open | probe derivation only; low block is preprint-conditional and no dossier exists |

Only the first two rows are backed by existing certified dossiers, and both are already represented
without a new cross-route edge. No new ledger edge is warranted.

## Audit of the two candidate lemmas

### `lem:time-weighted-source`

Verdict: analytically sound as a candidate, reusable across fixed cuts in the two-color
localization layer, but not cross-route and not yet certified.

From $B_t\preceq A_t\preceq t^{-1}I$ and the rank-one identity
$\lambda_{\max}(B_t)=r_t$,
$$
r_t\le t^{-1},\qquad
D_t\le\frac{2r_t}{t}-r_t^2.
$$
Multiplication of the certified scalar Riccati identity by $t^2$ then gives
$$
\mathbb E\int_0^Tt^2(S_t+r_t^2)\,dt
\le T^2\mathbb Er_T\le T.
\tag{L1}
$$
The exact guardrails for a dossier are:

- a fixed cut with initial mass strictly between zero and one;
- finite-horizon localization first, with bounded stopping of the local martingale;
- use of $A_t\preceq t^{-1}I$ only for $t>0$, followed by dominated/Fatou and regularization
  passage;
- stopped-window consequences only by positivity;
- no deweighting at zero: a scalar multiplier using only the Riccati identity and the same
  Brascamp--Lieb cap must vanish at least quadratically;
- no use of `thm:letwin-qcts`, and no implication to `q:upgrade`, `q:alignment`, or
  `q:stein-weighted`.

It was not promoted to shared knowledge because its current reusable scope is the single
two-color stochastic layer and its formal node, statement anchor, dossier, and review do not yet
exist. The orchestrator should accept the precise open node and manuscript statement first; only
then should a `prover` receive the report's exact prompt.

### `lem:mm-posterior-defect`

Verdict: analytically sound as a candidate and genuinely new structure for Route S, but
eigenfunction-specific rather than cross-cutting and not yet certified.

For a smooth strongly log-concave isotropic approximant, a normalized eigenfunction
$-Lf=\lambda f$, and the planted channel $c_t=tX+B_t$, define
$$
R_t(x)=(c_t-tx)\cdot\nabla f(x),\qquad r_t=R_t-\mathbb E_tR_t.
$$
The report derives
$$
\lambda g_t=b_t+u_t,\qquad
\lambda H_t=2\operatorname{sym}C_t+K_t,
\tag{L2}
$$
$$
\mathbb E\operatorname{Var}_t(R_t)
=t\lambda-\lambda^2\int_0^t\mathbb E|g_s|^2\,ds,
\tag{L3}
$$
$$
\mathbb E\int_0^t\|C_s\|_{\mathrm{HS}}^2\,ds
\le\lambda-\lambda^2|g_0|^2,
\qquad
\mathbb E\mathbb E_t|\nabla R_t|^2\le t\lambda^2+t^2\lambda.
\tag{L4}
$$
The exact guardrails for a dossier are:

- a genuine sufficiently regular eigenfunction on the regular approximant, with the generator
  and sign convention fixed before localization;
- reconstruction of the planted filtering/innovation coupling, not only a formal substitution
  in the posterior density;
- posterior integration by parts against constants, coordinates, and centered quadratics, with
  the centering in $K_t$ retained;
- stopped martingales and a stated removal argument for $m_t$ and $b_t$;
- the Bochner inequality for (L4), with its regularity/domain assumptions;
- the optional whitened defect-tensor estimate is a separate corollary conditional on
  `thm:letwin-qcts` and must not enter the unconditional node statement;
- no high-incidence unwhitening, occupation estimate, spectral sufficiency, approximation limit,
  or KLS conclusion.

It was not promoted to shared knowledge for the same provenance reason and because its consumer
is currently Route S alone. The orchestrator should first accept an open node whose statement
includes (L2)--(L4), then dispatch a `prover`. The proposed ledger statement in the probe omits
the last bound in (L4) even though its handoff asks the prover to establish it; statement and
handoff should be made consistent at acceptance time.

## Promotion and duplicate-attempt audit

Promoted to `research/knowledge/lemmas.md`:

1. the abstract covariance-threshold block extraction (N1)--(N2), sourced jointly from the
   upgrade and spectral probes, with the conditional-input and no-occupation guardrails;
2. the certified static symmetric-matrix commutator identity (C1), with explicit separation from
   moving-projector and square-root/Haar errors.

Not promoted:

- `lem:time-weighted-source`, pending node acceptance, a dossier, and independent review;
- `lem:mm-posterior-defect`, pending the same workflow;
- either stochastic high-incidence estimate, because both are open;
- any proposed cross-route equivalence, because none is proved.

The two stochastic agents independently re-derived (N1)--(N2). That is a bounded harness
duplication: the targets are genuinely distinct, but future prompts should cite the promoted
block lemma instead of spending a second attack on the same fixed-state algebra. Their surviving
residues are not duplicates. The upgrade residue is cut-specific $K$ occupation with a separate
$G$ correction; the spectral residue is eigenfunction-specific $H$ unwhitening with
moving-projector errors. The CMH residue is stationary and commutator-based.

No report proposes a broadly reusable new adversarial instance. The CMH algebraic countermodel
is already curated as `fence-cmh-algebraic-countermodel`; no instance-registry edit is warranted.

## What is now known jointly

1. Conditional intrinsic QCTS closes the complete low--low covariance block in both stochastic
   routes by the same dimension-free algebra. The common unresolved quantity is therefore an
   oriented high-incidence **occupation**, not another low-sector or global operator-norm bound.
2. This common normal form does not make the two occupations equivalent: their carriers,
   lower-order budgets, damping, and quantifiers differ.
3. The CMH obstruction occurs even before variable gradients: the linear sector needs a genuine
   moment-map transverse commutator bound. It has no stochastic damping reservoir and cannot be
   folded into the two occupation estimates.
4. The upgrade probe has an unconditional $t^2$-weighted budget, and the spectral probe has
   unconditional posterior-defect budgets. Each supplies new structure, but neither removes the
   Euclidean high-incidence residue.

## Remaining barriers, one line each

- **A1 $\leftrightarrow$ A2:** untouched by this KLS-only wave; no asymptotic consistency claim
  was added.
- **A1-bis $\leftrightarrow$ KLS:** untouched; no cross-program bridge or dependency edge was
  added.
- **Trace-upgrade cluster:** still lacks one proved geometric/analytic bridge among
  `q:upgrade`, high-rank `q:stein-weighted`, and `q:alignment`; only analogy is known.
- **Moment-map spectral:** still blocked by asymmetric, orientation-preserving unwhitening of the
  eigenfunction tensor on a universal time window.
- **Moment-map CMH:** still blocked first by the genuine-Hessian static commutator/linear sector,
  and then by variable-gradient, solenoidal, invariant-lift, and complete-Haar estimates.

## Ordered transitions

1. The orchestrator should review and accept or reject the two candidate **open** node statements
   and their manuscript anchors before any prover dispatch. Acceptance changes no mathematical
   status and adds no cross-route edge.
2. If both are accepted, dispatch two `prover` agents in parallel under distinct solution keys:
   one for `lem:time-weighted-source`, one for `lem:mm-posterior-defect`. If only one proof slot is
   available, prioritize the posterior-defect lemma because it supplies route-specific structure
   not already present in the certified Riccati backbone.
3. Send each compiled dossier to a distinct cold `proof-checker`; author and reviewer must differ.
   Only a passing persisted review permits the orchestrator to add `solution`, `checked_by`, and
   proof status.
4. Do not sharpen `gating.md` from the probe reductions before that review cycle: the stochastic
   low-block statements are preprint-conditional and the displayed reductions have no dossier.
   No current gate status changes.
5. After certification, the next exploration wave should use distinct gates: a Route-S prober
   consuming the posterior-defect lemma in an asymmetric high-incidence attack, a CMH prober on
   `q:mm-invariant-lift`, and an Eldan prober on `q:weighted`. Do not simultaneously re-probe
   `q:upgrade`, high-rank `q:stein-weighted`, and `q:alignment`; one owner must retain the shared
   trace-upgrade comparison.

## Proposed ledger and route-control delta

No status change, `depends_on` edge, bridge, or route-control replacement is warranted by this
synthesis. The only certified implications found are already represented by
`prop:letwin-not-gate-zero`/its dossier and the existing conditional node
`q:cmh-approximation`.

The two proposed lemma shells should be treated as orchestrator acceptance decisions before the
proof transition, not as proved deltas. If accepted, they remain `open`, carry no `solution` or
`checked_by` metadata, and create no consumer edge until independently certified.

```yaml
outcome: complete
artifacts:
  - research/explorations/2026-08-27-synthesizer-kls-first-wave-par-04.md
  - research/knowledge/lemmas.md
proposed_deltas:
  - no mathematical status, dependency, bridge, or route-control delta
  - orchestrator to decide acceptance of the two open candidate node statements before prover dispatch; neither is promoted as proved
next_role: orchestrator
next_prompt: |
  Review the first-wave synthesis and first decide whether to accept the candidate open nodes
  `lem:time-weighted-source` and `lem:mm-posterior-defect` with matching manuscript statements.
  For the posterior-defect node, include the averaged gradient-defect bound in the accepted
  statement so it matches the requested dossier, and keep the whitened `K_t` corollary separate
  and conditional on `thm:letwin-qcts`. If accepted, dispatch two distinct provers in parallel,
  then distinct cold proof-checkers; do not mark either node proved before a passing persisted
  review. Apply no cross-route edge and no status change to `q:upgrade`,
  `q:mm-spectral-occupation`, `ass:uniform-cmh-approximants`, `q:stein-weighted`, or
  `q:alignment`. Preserve the single-owner rule for any later work in the trace-upgrade cluster.
```
