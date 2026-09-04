---
type: exploration
date: "2026-08-30"
outcome: proposed
nodes:
  - prop:split-screened-supply
---
# Prover: dossier for the split-class screened weighted supply

Date: 2026-08-30

Role: `prover`

Run id: `w4p01`

Concurrency key: `solution:prop-split-screened-supply`

Task source: probe record
`research/explorations/2026-08-30-kls-route-prober-weighted-screened-interface-w4w01.md`
(Sections 2.1, 5, 9), for the orchestrator-accepted candidate node
`prop:split-screened-supply` (ledger acceptance pending; no ledger entry exists yet and
none is written here).

## Artifact

- `solutions/prop-split-screened-supply.tex` — standalone dossier, `checked_by: none`
  (drafted, unreviewed; **no ledger value yet**), reviewer field left empty.
- Build: `cd solutions && latexmk -pdf -outdir=../build prop-split-screened-supply.tex`
  succeeds — 6-page PDF, zero LaTeX errors, zero overfull boxes; 33 unresolved
  cross-module `\ref`s render as `??`, the expected standalone behaviour per
  `solutions/README.md`.

## What is proved

**Theorem (thm:sol-split-screened-supply, regular split class).** Let
$\mu=\bigotimes_{i=1}^n\mu^{(i)}$ be a product of isotropic one-dimensional log-concave
measures in the compact-smooth product-preserving regular class, $E$ measurable with
respect to a fixed coordinate set $J$ with $|J|=k$ and $0<p_0<1$. For every
$\eta\in(0,1/4]$, every $\kappa>0$, and every $T>0$,
$$
\mathbb E\int_0^{T\wedge\tau_\eta}
 e_t\,(1+\lambda_{\rm cut}(A_t,K_t))^{5/2}\,
 \mathbf 1_{\{Q_t\ge\kappa e_tW_{\rm cut}(A_t,K_t)\}}\,dt
\ \le\ \frac{2k+64\,\eta^2(1+k)}{\kappa},
$$
with $Q_t=s_t\|K_t\|_{\rm HS}^2=\mathcal S_{\mu_t}(E)/s_t$,
$W_{\rm cut}=(1+\lambda_{\rm cut})^{5/2}$, and the certified convention
$\lambda_{\rm cut}(A,0)=0$. The bound is **total-budget**: uniform in $T$, in the ambient
dimension $n$, and in every spectator coordinate; it is explicitly **not** of the form
$C(k)\,T$, and the dossier asserts nothing about the trace-upgrade cluster (constraint 6
disclaimer is in the dossier's Scope paragraph and Remark on shape).

Proof structure (each step audited against the certified dossier it cites, not against the
probe's sketch):

1. Pathwise, $e_tW_{\rm cut}\mathbf 1_{\mathcal A_{\kappa,t}}\le Q_t/\kappa$ — directly
   from the screen's defining inequality plus $Q_t\ge0$ off the set; $e_t\ge0$ from the
   upper-bound direction $I_{\mu_t}(p_t)\le P_t(E)$ ($E$ is a competitor in the profile
   infimum). The $K_t=0$ degenerate state is recorded explicitly: conventions give
   $Q_t=0$, $W_{\rm cut}=1$, membership iff $e_t=0$, both sides vanish.
2. On $\{t<\tau_\eta\}$ with $\eta\le1/4$: $s_t\ge 1/4-\eta^2\ge 3/16>1/8$ and the second
   inequality of `lem:stein-vs-source` (`solutions/kls-qcts-stein-boundary-core.tex`)
   gives $Q_t\le 2S_t+64\eta^2D_t$; the endpoint $t=\tau_\eta$ is Lebesgue-null in time.
3. Source budget $\mathbb E\int_0^\infty S_t\,dt\le\sum_{i\in J}(R_0)_{ii}\le k$: the
   certified `thm:budget`(i) argument reproduced inline from its unconditional inputs
   (`prop:products` pathwise product persistence, `lem:block` at $(\mu_t,E)$ under
   $0<p_t<1$, `cor:per-direction` per supported column, monotone convergence), because the
   packaged `thm:budget` statement carries $p_0\in[2/5,3/5]$ while its dossier audit
   records that part (i) needs only $0<p_0<1$. The inline reproduction removes any
   reliance on the packaged (stronger) hypothesis.
4. Dissipation budget $\mathbb E\int_0^{T\wedge\tau_\eta}D_t\,dt\le 1+k$: integrate
   `thm:scalar-riccati` at the bounded localizing stopping times of the certified regular
   class, optional stopping, discard $\mathbb E\,r\ge0$, use $r_0\le1$ (rank-one
   $B_0\preceq A_0=I$), monotone convergence in the localization index.
5. Chain and divide by $\kappa$; Tonelli throughout on nonnegative progressively
   measurable integrands (no a priori integrability needed).

## Auxiliary lemma (clearly separated)

`lem:sol-constant-supply-consumption`: the constant-supply extension of
`cor:tight-window-consumption` — if
$\mathbb E\int_0^{T\wedge\tau_\eta}S_t\,dt\le c+C_0T+C_1\mathbb E\int r+\alpha\mathbb E\int D$
with $\alpha<1$, a priori finite $\mathbb E\int_0^{T_0\wedge\tau_\eta}D_t\,dt$ (automatic
in the regular class; stated as an explicit hypothesis, echoing the probe's Step 0), and
$|p_0-1/2|\le\eta/2$, $\eta\le1/6$, then Gronwall gives
$u(T)\le(1+c+C_0T)e^{C_1T}\le C_*$ and survival
$\Prob\{\min(p_{T_*},q_{T_*})\ge 1/3\}\ge 1/2$ for every positive
$T_*\le\min(T_0,4\eta^2/(9C_*))$, feeding `lem:survival-implies-kls`. Proof is the
certified corollary's proof re-run in full with the single changed Gronwall line. The
dossier states explicitly (Remark "no companion claimed") that no screened trace companion
is proved or assumed and no KLS conclusion is drawn from the main theorem.

## Measurability conventions adopted (probe Section 5, verbatim)

(M1) augmented right-continuous Brownian filtration; (M2) compact-smooth
product-preserving regular class first, with the certified passage conventions and
regularization-independent constants; (M3) $P_t$ via the countable rational
boundary-layer construction of `kls-excess-audit`, $I_{\mu_t}(p_t)$ jointly measurable via
a fixed countable regular competitor family, *measurability only* — no supermartingale
property of the moving infimum asserted; (M4) Borel $\lambda_{\rm cut}$ on supported pairs
(fixed-rank strata + Borel Moore–Penrose), progressively measurable weight and screened
indicator, both used only inside nonnegative Lebesgue-time integrals, no Itô calculus on
the weight or the indicator.

## Hypotheses actually used (complete list)

- $0<p_0<1$ (block support + budgets; also keeps all two-color quantities defined).
- Isotropy of each factor: $A_0=I$, hence $(R_0)_{ii}\le1$ and $r_0\le1$.
- Product structure + $J$-measurability of $E$, fixed before localization (no adaptive
  cut).
- $\eta\in(0,1/4]$ (certified domain of `lem:stein-vs-source`); if $|p_0-1/2|>\eta$ the
  statement is trivially true ($\tau_\eta=0$) — noted in the proof.
- $\kappa>0$.
- Regular class (M2) for: existence of localizing stopping times, measurability of
  $e_t$ and the screened indicator, $P_0(E)<\infty$.
- No hypothesis is used without being stated; in particular no balance window
  $p_0\in[2/5,3/5]$, no near-worst premise, no excess floor, no companion estimate.

## Unclosed steps, flagged in the dossier

1. **General (non-regular) split laws** (Remark `rem:sol-general-class`): the statement is
   *defined on approximants* per the probe's Section 5(5); the constant is uniform over the
   certified approximation scheme, but the limit interchange for the screened integrand
   itself (the indicator does not converge monotonically) is an explicit open technical
   step. Any consumer of the general-class statement must work with approximants or close
   that interchange separately.
2. No other unclosed analytic step: within the regular split class the theorem's proof is
   complete from certified inputs.

Deviations from the probe's sketch: none mathematically; procedurally, `thm:budget`(i) is
reproduced inline from `lem:block` + `cor:per-direction` + `prop:products` instead of being
cited as a black box, precisely because the packaged theorem statement carries the coarse
balance window that part (i) does not need.

## Fence check

- `obs:two-tail`: time-integrated statement, not slice-wise; retains the calibrated
  $5/2$ weight (two-tail calibration $\lambda_{\rm cut}(A_\Lambda,K_\Lambda)=\Lambda$
  cited); the two-tail initial laws are outside the hypothesis class (non-isotropic
  factor); dynamically reached two-tail-type states stay chargeable and are paid via
  $Q_t/\kappa$. Not violated.
- `obs:circularity`: the only profile fact used is the definitional upper bound
  $I_{\mu_t}(p_t)\le P_t(E)$ (giving $e_t\ge0$); no lower bound on the moving profile, no
  use of the excess identity in the fenced direction. Not violated.
- Constraint 6: explicit disclaimer in the dossier; no occupation estimate, comparison, or
  equivalence involving `q:upgrade` / high-rank `q:stein-weighted` / `q:alignment` is
  claimed.

## Status

Unconditional within the regular split class as stated; the general split class is covered
only in the defined-on-approximants sense with the flagged gap. `checked_by: none` — this
is an unreferenced candidate dossier with **no ledger value** until a cold `proof-checker`
review. Deferred artifact candidate only: a future ledger node
`prop:split-screened-supply` would point at `solution: solutions/prop-split-screened-supply.tex`
once (and only once) certification exists; no ledger file was touched by this session.

```yaml
outcome: complete
artifacts:
  - solutions/prop-split-screened-supply.tex
  - research/explorations/2026-08-30-prover-split-screened-supply-w4p01.md
proposed_deltas:
  - none (ledger acceptance of the candidate node and any solution/checked_by wiring are
    orchestrator-owned and require an independent certification first)
next_role: proof-checker
next_prompt: |
  Cold-review the candidate dossier solutions/prop-split-screened-supply.tex (build:
  cd solutions && latexmk -pdf -outdir=../build prop-split-screened-supply.tex; compiles
  clean, 6 pages, unresolved cross-module refs are the expected standalone "??"). Do not
  consult the prover's session; reconstruct from repository artifacts. The dossier claims,
  for the candidate node prop:split-screened-supply (candidate, ledger acceptance
  pending), in the compact-smooth product-preserving regular class:

  For a product of isotropic one-dimensional log-concave measures, a cut E measurable with
  respect to a fixed coordinate set J with |J|=k and 0<p_0<1, every eta in (0,1/4], every
  kappa>0, and every T>0:
  E int_0^{T wedge tau_eta} e_t (1+lambda_cut(A_t,K_t))^{5/2}
    1{Q_t >= kappa e_t W_cut} dt <= (2k + 64 eta^2 (1+k))/kappa,
  with Q_t = s_t ||K_t||_HS^2, W_cut=(1+lambda_cut)^{5/2}, lambda_cut(A,0)=0 as in
  solutions/lem-lyapunov-stein-duality.tex; total-budget form (uniform in T, dimension,
  spectators; explicitly NOT C(k)T; explicitly no trace-upgrade-cluster content).

  Verify in particular:
  1. Step 1 pathwise domination e_t W_cut 1_{aligned} <= Q_t/kappa, including e_t >= 0 via
     the profile-infimum upper-bound direction only, and the K_t=0 degenerate case under
     the certified conventions.
  2. Step 2's use of the second inequality of lem:stein-vs-source
     (solutions/kls-qcts-stein-boundary-core.tex) on {t<tau_eta}, eta<=1/4, and the
     identification Q_t = calS_{mu_t}(E)/s_t via prop:stein-rep.
  3. Step 3's inline reproduction of thm:budget part (i) under only 0<p_0<1 from
     prop:products + lem:block + cor:per-direction + monotone convergence — check it
     against solutions/kls-product-covariance.tex (including its dependency-audit
     paragraph) and solutions/kls-localization-riccati-core.tex.
  4. Step 4's dissipation budget E int_0^{T wedge tau_eta} D_t dt <= 1+k: localizing
     stopping times, optional stopping, r_0<=1, monotone convergence.
  5. The measurability conventions (M1)-(M4) match Section 5 of
     research/explorations/2026-08-30-kls-route-prober-weighted-screened-interface-w4w01.md,
     and the indicator/weight appear only inside Lebesgue-time integrals (no Ito calculus
     on the weight).
  6. Remark rem:sol-general-class honestly confines the general (non-regular) split class
     to the defined-on-approximants convention and flags the screened-indicator limit
     interchange as open; confirm the theorem statement's class restriction is consistent
     with the candidate node text of the probe's Section 9.
  7. The clearly separated auxiliary Lemma lem:sol-constant-supply-consumption
     (constant-supply extension of cor:tight-window-consumption): one-line Gronwall
     change, explicit a priori finiteness hypothesis, correct constants
     C_*=(1+c+C_0 T_0)e^{C_1 T_0} and T_* <= min(T_0, 4 eta^2/(9 C_*)); confirm it claims
     no companion estimate and draws no KLS conclusion.
  8. Fences: obs:two-tail and obs:circularity per the dossier's closing audit; repository
     constraint 6 disclaimer present and respected.

  Author identity: prover-w4p01 (Claude Fable 5 prover session, 2026-08-30); your review
  must use a distinct reviewer identity, be persisted under research/reviews/ per
  research/reviews/README.md, and you may not edit solutions/. If defects are found,
  return outcome: revise with an exact repair contract; do not certify partially.
```
