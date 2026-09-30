---
---
# Synthesis: the aligned initial-layer kernel versus the tight-prefix Carleson estimate

Date: 2026-08-30

Role: `synthesizer`

Run id: `w4y01`

Concurrency key: singleton `knowledge`, granted by the orchestrator for this one comparison
(CLAUDE.md constraint 6: the trace-upgrade cluster has one comparison owner). Scope is strictly
the comparison routed by probe `w4w01`; a broader wave synthesis is a separate later invocation.

Sources converged:

- `research/explorations/2026-08-30-kls-route-prober-weighted-screened-interface-w4w01.md`
  (Sections 1, 3.2–3.3, 4);
- `research/explorations/2026-08-27-kls-route-prober-upgrade-par-01.md`;
- `research/explorations/2026-08-27-kls-route-prober-tight-prefix-soft-projector-w3p01.md`;
- `research/explorations/2026-08-27-synthesizer-kls-first-wave-par-04.md` (discipline and
  directional table conventions);
- `research/kls/ledger.yaml` (nodes `ass:tight-prefix-carleson`, `conj:trace-upgrade`,
  `conj:stein-weighted`, `conj:weighted-excess-rate`, `ass:weighted-package`, `lem:stein-vs-source`,
  `lem:lyapunov-stein-duality`, `lem:pathwise-BL`, `cor:away-from-zero`, `cor:per-direction`,
  `thm:scalar-riccati`, `cor:tight-window-consumption`, `prop:trivial-excess`, `prop:two-tail`,
  `lem:time-weighted-source`), `routes.md`, `gating.md`, `obstructions.md`;
- `modules/kls/20-eldan-statements.tex` (exact `ass:tight-prefix-carleson` statement),
  `modules/kls/27-eldan-open-targets.tex` (`conj:trace-upgrade`, `conj:stein-weighted`,
  `rem:trace-upgrade-unification`);
- `research/knowledge/lemmas.md`.

Live-state audit: `python3 research/check_ledger.py status` reports `conj:trace-upgrade`,
`ass:tight-prefix-carleson`, `conj:stein-weighted`, `conj:product-alignment` all `open`; `conj:weighted-excess-rate` and
`ass:weighted-package` `refuted`; `check_ledger.py` at 0 errors. No numerics are used. This
synthesis changes no ledger, manuscript, route-control, dossier, review, or instance-registry
entry; its only writes are this file and two promotions to `research/knowledge/lemmas.md`.

The parallel prover `w4p01` (`prop:split-screened-supply` dossier) and CMH prober `w4c01` are
not touched, cited as in-flight only.

## Objects in a common normalization

All processes are those of `solutions/kls-localization-riccati-core.tex`. Common currency:
$S_t=s_t\|G_t\|_{\rm HS}^2$, $Q_t=s_t\|K_t\|_{\rm HS}^2=\mathcal S_{\mu_t}(E)/s_t$,
$r_t=s_t|\delta_t|^2$, $D_t=2s_t\delta_t^TA_t\delta_t-r_t^2\ge r_t^2$,
$e_t=P_t-I_{\mu_t}(p_t)$, $W_{\rm cut}=(1+\lambda_{\rm cut}(A_t,K_t))^{5/2}$ with the certified
$\lambda_{\rm cut}(A,0)=0$ convention, and the screen
$\mathcal A_{\kappa,t}=\{Q_t\ge\kappa e_tW_{\rm cut}\}$. The certified two-way conversion
(`lem:stein-vs-source`, $\eta\le1/4$, on $\{t<\tau_\eta\}$) is
$S_t\le2Q_t+64\eta^2D_t$ and $Q_t\le2S_t+64\eta^2D_t$.

**AIK** (aligned initial-layer kernel; `w4w01` Sections 3.2–3.3, Candidate B core). There exist
universal $\kappa\in(0,\kappa_{\rm TT})$, $t_*,T_0,C>0$, $\eta\in(0,1/8)$ such that for every
isotropic log-concave $\mu$ in the near-worst class ($h_\mu\le(1+\varepsilon_{\rm nw})h_n^*$,
$h_n^*\le h_\bullet$), every finite-perimeter cut with $p_0=1/2$ and $e_0\le\varepsilon_Eh_\mu$,
and every $T\le T_0$:
$$
\mathbb E\int_0^{t_*\wedge T\wedge\tau_\eta}Q_t\,\mathbf 1_{\mathcal A_{\kappa,t}}\,dt\le C\,T.
$$
Screened, excess-gated, cut-local weight, initial layer only, **no $r$ or $D$ budget terms**,
strict $O(T)$ right side. By the proved reduction lemma of `w4w01` Section 3.2, AIK implies the
screened supply (21) with $C_E=(1+1/t_*)^{5/2}(1+\varepsilon_Eh_\bullet)+C/\kappa$.

**AIK$^{+}$** (relaxed total-budget form). Same left side, right side $c_1T+c_2$ with universal
$c_1,c_2$. By the constant-supply variant of `w4w01` Section 1, AIK$^{+}$ is still
consumption-sufficient for the screened pair (a one-line uncertified Gronwall restatement of
`cor:tight-window-consumption`).

**TPC** (`ass:tight-prefix-carleson`, `modules/kls/20-eldan-statements.tex`). There exist
universal $\eta\in(0,1/6]$, $T_0,C_0,C_1>0$, $\alpha<1$ such that for **every** isotropic
log-concave $\mu$, every fixed cut with $|p_0-1/2|\le\eta/2$, and every $T\le T_0$:
$$
\mathbb E\int_0^{T\wedge\tau_\eta}S_t\,dt
\le C_0T+C_1\mathbb E\int_0^{T\wedge\tau_\eta}r_t\,dt
+\alpha\mathbb E\int_0^{T\wedge\tau_\eta}D_t\,dt.
$$
Unscreened, no excess variable at all, all-measure/all-balanced-cut, with $r$ and $D$ budgets.

**SW** (`conj:stein-weighted`, high-rank part). Universal $T_0,C_0,C_1,C_2>0$, $\beta\in[0,1/2)$,
$\eta\in(0,1/4]$ with $2\beta+64\eta^2<1$:
$\mathbb E\int Q_t\,dt\le C_0T+C_1\mathbb E\int r_t+\beta\mathbb E\int D_t
+C_2\mathbb E\int e_t(1+\|A_t\|_{\rm op})^{5/2}\,dt$, all-measure, $e_0\le1$. Unscreened,
**global** operator-norm weight; its excess term is a supply with no theorem behind it (the
matching $O(T)$ supply in that weight is exactly the refuted `conj:weighted-excess-rate`).

Certified calibration data used below (`prop:two-tail`, values recomputed and confirmed in
`w4w01` Section 4): the two-tail state at inflation $\Lambda\ge1$ has $r=D=0$,
$Q\approx0.7350\,\Lambda^2$, $e\approx0.2366\,\Lambda^{-1/2}$, $\lambda_{\rm cut}=\Lambda$, and
$Q/(eW_{\rm cut})\ge\kappa_{\rm TT}=2^{-5/2}\cdot\frac{16a^2\varphi(a)^2}{2\varphi(a)-\varphi(0)}
\approx0.5492$ ($a=\Phi^{-1}(3/4)$). Pathwise pin on the aligned set (screen definition plus
`lem:lyapunov-stein-duality`): on $\mathcal A_{\kappa,t}$,
$\kappa e_tW_{\rm cut}\le Q_t\le4\lambda_{\rm cut}/t$, hence
$e_t\le4/(\kappa t(1+\lambda_{\rm cut})^{3/2})$.

## The candidate derivation TPC $\Rightarrow$ AIK$^{+}$, written out

This is the one direction where a complete derivation from certified nodes exists. Every step is
a certified node plus arithmetic; it is prover-formalizable but has **no dossier**, so it yields
no edge. Fix TPC constants $(\eta,T_0,C_0,C_1,\alpha)$ and a cut in AIK's class ($p_0=1/2$
satisfies $|p_0-1/2|\le\eta/2$). All integrals over $[0,T\wedge\tau_\eta]$, $T\le T_0$; write
$\mathcal S=\mathbb E\int S_t\,dt$, $\mathcal D=\mathbb E\int D_t\,dt$,
$\mathcal R=\mathbb E\int r_t\,dt$, $u(t)=\mathbb E r_{t\wedge\tau_\eta}$.

1. *A priori finiteness* (the Step-0 discipline of `w4w01` Section 1): summing
   `cor:per-direction` over an orthonormal basis, $\mathcal S\le\operatorname{Tr}R_0\le n$;
   integrating `thm:scalar-riccati` at the dossier's localizing stopping times,
   $\mathcal D\le r_0+\mathcal S\le1+n$. Dimension-dependent, which suffices for absorption.
2. *Gronwall* (inside the certified `cor:tight-window-consumption` dossier body, using
   $\alpha<1$ and step 1): $u(t)\le(1+C_0t)e^{C_1t}\le C_*:=(1+C_0T_0)e^{C_1T_0}$, hence
   $\mathcal R\le C_*T$ (using $r\ge0$ and $r_t\mathbf 1_{\{t<\tau_\eta\}}\le r_{t\wedge\tau_\eta}$).
3. *Optional stopping* of `thm:scalar-riccati` (exact under the certified regularity
   convention; identity (1) of `upgrade-par-01`): $u(T)=r_0+\mathcal S-\mathcal D$, so
   $\mathcal D\le1+\mathcal S$.
4. *TPC plus absorption*: $\mathcal S\le(C_0+C_1C_*)T+\alpha(1+\mathcal S)$, hence
   $\mathcal S\le\frac{(C_0+C_1C_*)T+\alpha}{1-\alpha}$ and
   $\mathcal D\le\frac{(C_0+C_1C_*)T+1}{1-\alpha}$.
5. *Conversion* (`lem:stein-vs-source`, $\eta\le1/4$):
   $\mathbb E\int Q_t\,dt\le2\mathcal S+64\eta^2\mathcal D
   \le\frac{(2+64\eta^2)(C_0+C_1C_*)}{1-\alpha}\,T+\frac{2\alpha+64\eta^2}{1-\alpha}$.
6. *Monotone restriction*: for any $t_*>0$, any $\kappa>0$, any $\eta'\le\eta$, the AIK left
   side at $\eta'$ is a nonnegative integral over a smaller window
   ($\tau_{\eta'}\le\tau_\eta$), hence bounded by step 5.

Conclusion: TPC implies AIK$^{+}$ with
$c_1=\frac{(2+64\eta^2)(C_0+C_1C_*)}{1-\alpha}$ and
$c_2=\frac{2\alpha+64\eta^2}{1-\alpha}>0$. The strict $O(T)$ form of AIK does **not** follow:
$c_2$ is irreducible in this chain, and removing it would need a universal
$\mathbb E\int_0^{T\wedge\tau_\eta}D_t\,dt=O(T)$ interval-density estimate near $t=0$, which no
certified node provides and which is itself an initial-layer occupation problem ($D_t$ rides
covariance spikes). Note also that this direction is structurally vacuous for KLS: TPC already
feeds `cor:tight-window-consumption` directly, so deriving AIK$^{+}$ from it adds comparison
information only.

## Directional implication table

Status words follow the par-04 discipline: they concern the displayed direction only; `proved
(dossier)` requires an existing certified dossier; nothing else leaves this table as an edge.

| direction | status | exact reason |
|---|---|---|
| TPC $\Rightarrow$ AIK (strict $O(T)$) | open | the six-step chain above leaves the additive constant $c_2=(2\alpha+64\eta^2)/(1-\alpha)>0$; discharging it needs a universal $O(T)$ bound on $\mathbb E\int_0^{T\wedge\tau_\eta}D_t\,dt$, which no certified node supplies |
| TPC $\Rightarrow$ AIK$^{+}$ (constant-plus-linear) | open with a complete candidate one-way derivation | steps 1–6 above; every step certified plus arithmetic; prover-formalizable; no dossier exists, so no edge; consumption-sufficiency of AIK$^{+}$ additionally rests on the uncertified constant-supply Gronwall restatement |
| AIK $\Rightarrow$ TPC | not even conjectured | AIK is supply-side only: it is silent on $\mathcal A_{\kappa,t}^c$, where the whole complement return ($\theta$-clause of the open companion (22)) lives; its class is near-worst with $e_0\le\varepsilon_Eh_\mu$, while TPC is all-measure with $e_0$ unrestricted; no transform from a screened $Q$-occupation bound to an unscreened $S$-estimate is stated anywhere |
| AIK $\wedge$ (22) $\Rightarrow$ TPC restricted to AIK's class | open with a candidate conditional derivation | `w4w01` Section 1 Step 2 output is literally the TPC inequality shape with $\alpha=2\beta/(1-\theta)+64\eta^2<1$, fed by the reduction lemma; both premises (AIK and the screened companion (22)) are open, so this is doubly conditional and warrants no edge; it can never yield full TPC because the class restriction is inherited |
| AIK $\Rightarrow$ SW | not even conjectured | same complement silence as above, and SW's right side carries the **global** weight $(1+\|A\|_{\rm op})^{5/2}\ge W_{\rm cut}$, so no domination in the useful direction exists; SW's weighted-excess supply has no theorem (its $O(T)$ rate form is the refuted `conj:weighted-excess-rate`) |
| SW $\Rightarrow$ AIK | not even conjectured | SW bounds $\mathbb E\int Q$ only against an uncontrolled weighted-excess supply; converting that supply to a numeric $O(T)$ (or constant) bound is exactly the refuted/open supply problem, and the screen gives no help in this direction |
| TPC $\leftrightarrow$ SW, TPC $\leftrightarrow$ `conj:product-alignment`, SW $\leftrightarrow$ `conj:product-alignment` | unchanged from par-04 | all `not even conjectured` / `open` exactly as in the 2026-08-27 table; nothing in `w4w01` touches those directions |

One coefficient-level consistency fact, which is arithmetic, not an implication between open
statements: the audited screened absorption condition $2\beta/(1-\theta)+64\eta^2<1$ degenerates
at $\theta=0$ to the certified-consumption condition $2\beta+64\eta^2<1$ of
`ass:weighted-package`/`conj:stein-weighted`. The screened algebra is therefore a strict
generalization of the refuted package's consumption arithmetic, with the same
`lem:stein-vs-source` constants; this was verified, not corrected, by `w4w01` Section 1
(together with the two additions the gate text does not display: the a priori finiteness Step 0
and the forced window $\eta\in(0,1/8)$).

## Answer to the routed discriminator question

**Does the screen strictly weaken the demand, or does the two-tail calibration force AIK and TPC
to coincide on the hard configurations? Neither: they are formally incomparable with one proved
common hard core.**

1. *The screen cannot be used to evade the configuration that blocks TPC.* For every admissible
   $\kappa<\kappa_{\rm TT}\approx0.5492$, the certified two-tail family lies in
   $\mathcal A_{\kappa,t}$ for all $\Lambda\ge1$ with $r=D=0$. On this family both statements
   collapse to the same demand: bound the expected occupation of two-tail-type source from an
   isotropic start by the $O(T)$ baseline alone, with no damping or information budget to spend.
   Any method that proves either AIK or TPC must solve this aligned zero-damping occupation
   problem. This is the sharpest form to date of the "shared difficulty" that
   `rem:trace-upgrade-unification` records for the cluster: the shared object is now an exact
   family with certified calibration constants, not an analogy.
2. *Where AIK is strictly weaker.* The screen excludes excess-inflated configurations. Concrete
   family: a two-tail base tensorized with independent centered one-sided-exponential spectators.
   Spectator spikes change neither $Q_t$ nor $W_{\rm cut}$ (certified direct-sum invariance) but
   inflate $e_t$; once $e_t>Q_t/(\kappa W_{\rm cut})$ the state leaves $\mathcal A_{\kappa,t}$
   and AIK charges nothing, while its full source $S_t\asymp\Lambda^2$ still counts in TPC's
   left side. The same exclusion mechanism (with exact values) removes the
   `prop:weighted-spectator-obstruction` leakage witnesses, and the exclusion threshold grows
   with the spike size — the worst states leave first. The pathwise pin
   $e_t\le4/(\kappa t(1+\lambda_{\rm cut})^{3/2})$ is a second AIK-only mechanism with no TPC
   analog: TPC has no excess variable, so it cannot confine dangerous occupation to the
   $\lambda^{-1}$-short window the pin provides.
3. *Where AIK is strictly stronger.* AIK's right side has no $r$ or $D$ budget. A state with
   simultaneously large $Q$, small $e$, and large $D$ is charged in full against AIK's bare
   $CT$, whereas TPC may pay $\alpha D_t$ for it. The six-step derivation shows exactly what
   this costs: TPC repays AIK only up to the additive constant $c_2$, which is nonzero for
   every $\alpha>0$.
4. *The "initial-layer only" restriction is not a genuine discriminator.* TPC is also a prefix
   problem whose $t\ge t_*$ layer is already finished by the certified
   `cor:away-from-zero` ($S_t\le8/t^2+D_t/2$), at the price of half the damping budget; AIK's
   $t>t_*$ layer is finished by `prop:trivial-excess` at no damping cost. Both difficulties live
   in the initial layer. The genuine discriminators are the screen (2), the missing budgets (3),
   and the tensor mismatch $Q$ vs $S$, whose certified conversion costs $64\eta^2D_t$ — a cost
   AIK cannot budget and which is precisely where $c_2$ enters.

Verdict for the cluster: AIK shares the cluster's high-rank aligned-occupation core through the
certified two-tail calibration and is hereby recorded as compared; it is **not** identified with
`conj:trace-upgrade`/TPC, with the high-rank part of `conj:stein-weighted`, or with `conj:product-alignment`, and it is
not a fourth equivalent formulation. The single-owner rule continues to apply to any future
comparison involving it. Deciding AIK does not decide TPC, and deciding TPC decides only
AIK$^{+}$, pending a dossier.

## What is now known jointly that was not known per-stream

1. AIK is the first formulation in the trace-cluster's orbit that provably survives both
   certified spectator mechanisms: the `prop:weighted-spectator-obstruction` excess-rate
   witnesses are excluded by the screen (exact values, `w4w01` Section 4), and the `w3p01`
   soft-projector spectator injection cannot occur because spectators change neither $Q_t$ nor
   $W_{\rm cut}$ — while the state remains two-tail-chargeable for every
   $\kappa<\kappa_{\rm TT}$. No earlier interface (raw weighted package, raw prefix injection)
   passed both tests.
2. AIK is at most one additive constant harder than TPC (the six-step chain), and that constant
   is exactly the price of the certified $Q$–$S$ conversion plus damping absorption. In
   particular, a TPC proof would retroactively complete the screened supply route in its
   consumption-sufficient relaxed form; the screened route is not a back-door strengthening of
   TPC.
3. The shared hard core of AIK and TPC is now an exact certified family (zero-damping two-tail
   states, chargeable in both), not a proof-shape analogy — a strict sharpening of
   `rem:trace-upgrade-unification`'s prose for this pair, still without any equivalence.

## Promotions and curation

Promoted to `research/knowledge/lemmas.md` (two entries, with guardrails):

1. **Screened absorption preconditions** — the `w4w01` Section 1 corrections: a priori
   finiteness of $\mathbb E\int Q_t\,dt$ is required before absorption and is certified with a
   dimension-dependent constant; the gate coefficient $2\beta/(1-\theta)+64\eta^2<1$ forces
   $\eta\in(0,1/8)$; a constant (non-$O(T)$) supply also suffices; at $\theta=0$ the condition
   degenerates to the `ass:weighted-package` arithmetic. Reusable by every future consumer-side
   probe on this route; guardrails record the uncertified constant-supply Gronwall restatement.
2. **Aligned screen: initial-layer reduction and pathwise pin** — the proved reduction of the
   screened supply to AIK, the pin $e_t\le4/(\kappa t(1+\lambda_{\rm cut})^{3/2})$, the
   chargeability threshold $\kappa_{\rm TT}\approx0.5492$, and spectator inertness. Guardrails
   record the $p_0=1/2$ requirement, the approximant-only general statement, the
   $\kappa<\kappa_{\rm TT}$ calibration constraint, and the incomparability verdict of this
   file (no equivalence with `ass:tight-prefix-carleson`).

Instance registry: **no change.** The discriminating mixed configuration (two-tail base
tensorized with excess-inflating exponential spectators, item 2 above) is a comparison device,
not yet a curated instance: it has no analytic oracle and no certified failure-mode
construction (the base-contrast verification flagged in `w4w01` Section 2.3 is not done). It
would presently serve only this comparison's prose, which is exactly what constraint 3's
curation bar rejects. If a refutation-seeker or prover later certifies the construction, it can
be proposed for the KLS stress registry with a named failure mode.

Duplicate-attempt audit: no rerun defect. The two 2026-08-30 probes (`w4w01` on
`kls-gate:q:weighted`, `w4s01` on `kls-gate:q:mm-spectral-occupation`) hold distinct keys on
distinct routes; both independently localized their residue in an initial layer, which is
convergent structure worth noting for future prompts (cite the promoted reduction entry rather
than re-deriving time-splitting), not a harness defect.

## Remaining barriers, one line each

- **A1 $\leftrightarrow$ A2:** untouched by this KLS-only comparison.
- **A1-bis $\leftrightarrow$ KLS:** untouched; no cross-program bridge added.
- **Trace-upgrade cluster:** still no proved implication among its members; the new AIK object
  is recorded as incomparable-with-shared-core against TPC, one direction short of an edge (a
  dossier for TPC $\Rightarrow$ AIK$^{+}$ would be the first proved cross-formulation
  implication touching the cluster's orbit, and is only worth writing if the orchestrator wants
  the comparison hardened, since it is KLS-vacuous).
- **Screened route (`conj:weighted-excess-rate` replacement):** blocked by AIK itself (needs-new-idea) and by
  the open companion (22); the split-class supply dossier (`w4p01`) is in flight.

## Proposed ledger delta

**None warranted.** No direction in the table is backed by a certified dossier. In particular,
do not add any edge between `ass:tight-prefix-carleson` (or `conj:trace-upgrade`) and any screened-route
object, and do not change the status of `conj:trace-upgrade`, `conj:stein-weighted`, `conj:product-alignment`, or
`ass:tight-prefix-carleson`. The only dossier-adjacent item is `prop:split-screened-supply`,
already proposed by `w4w01` and owned by the in-flight prover `w4p01`.

## Proposed route-control language (draft only; `route-control` is orchestrator-owned)

If the orchestrator adopts the `w4w01` Section 8 gate line for `conj:weighted-excess-rate`, append to it:

> The aligned initial-layer kernel is formally incomparable with `ass:tight-prefix-carleson`
> (synthesizer comparison, 2026-08-30): the tight-prefix estimate implies it only up to an
> additive constant $(2\alpha+64\eta^2)/(1-\alpha)$, which the constant-supply consumer
> tolerates; the screen excludes excess-inflated states the prefix estimate must count; the
> missing $r$/$D$ budgets cut the other way; and the certified two-tail family lies in both
> charges for every $\kappa<\kappa_{\rm TT}\approx0.549$, so neither statement can be proved by
> a method that fails on aligned zero-damping occupation. No equivalence is proved and no edge
> exists (constraint 6).

Optionally, one cross-reference sentence in the `conj:trace-upgrade` gate paragraph:

> The screened `conj:weighted-excess-rate` interface reduces to an aligned initial-layer $Q$-occupation
> estimate that shares the zero-damping two-tail core of this gate but is formally incomparable
> with `ass:tight-prefix-carleson`; the comparison is owned by the synthesizer and proves no
> implication.

```yaml
outcome: complete
artifacts:
  - research/explorations/2026-08-30-synthesizer-screened-kernel-comparison-w4y01.md
  - research/knowledge/lemmas.md
proposed_deltas:
  - "No ledger delta: no direction in the comparison table is dossier-backed; no status or edge change to ass:tight-prefix-carleson, conj:trace-upgrade, conj:stein-weighted, conj:product-alignment, or any screened-route object."
  - "Route-control (orchestrator-owned): if the w4w01 gate line for conj:weighted-excess-rate is adopted, append the incomparability sentence drafted above; optionally add the one-line cross-reference to the conj:trace-upgrade gate paragraph."
  - "Instance registry: no change; the mixed two-tail/spectator configuration is rejected for curation until a certified construction with a named oracle or failure mode exists."
next_role: orchestrator
next_prompt: |
  Review the screened-kernel comparison in
  research/explorations/2026-08-30-synthesizer-screened-kernel-comparison-w4y01.md. Apply no
  ledger delta: no implication in it is dossier-backed. Decide whether to adopt the two drafted
  route-control sentences together with the w4w01 Section 8 gate line for conj:weighted-excess-rate. Keep the
  w4p01 prover (prop:split-screened-supply) and w4c01 CMH prober running undisturbed. If you
  want the one derivable comparison hardened, a prover may be dispatched later for the
  TPC-implies-relaxed-AIK chain (steps 1-6 of the synthesis record) as a standalone conditional
  lemma with ass:tight-prefix-carleson as an explicit hypothesis; it is KLS-vacuous and low
  priority, and per constraint 7 it would enter as conditional. Preserve the single-owner rule
  for any future trace-cluster comparison, which now includes the AIK object.
```
