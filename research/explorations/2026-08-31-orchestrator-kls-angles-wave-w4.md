---
---
# Orchestrator: KLS angles-of-attack wave `w4` — outcomes, interruption, resume queue

Date: 2026-08-31

Role: `orchestrator` (sole ledger writer for the wave)

Run id: `w4`

Branch: `explore/kls-angles-2026-08-30`, commits `454e2bc..723c5d0` (13 commits).

Write scope of this record: this append-only file only. The ledger, manuscript, dossier,
review, and numerical writes of the wave were made in the commits listed below and are not
restated as changes here.

## Task

The user asked for a careful analysis of the KLS exploration, then for the ranked angles of
attack to be *executed* — with numerical experiments where useful, agents at model/effort
matched to the task, on a dedicated branch, pipelining rather than waiting for each agent to
finish. This record closes the wave's mathematical accounting and records **why the wave
stopped where it did**, so the next orchestrator does not re-derive the queue.

## Angles executed

Ranked list from the analysis phase; the ones actually attacked this wave:

- **(2.1) CMH anisotropic bootstrap.** Probe `w4c01`. With
  $\mathsf N=\int H^2$, $\mathsf D=\int H^{ab}(\partial_aH)(\partial_bH)$,
  $\mathsf R=\mathsf N-\mathsf D$: the gate reduces to the single matrix inequality
  $(\mathrm{AB})_{\rho,\beta}$, $\mathsf R\succeq\rho\mathsf N-\beta I$, giving
  $Q_{\mathrm{lin}}\le(1+\beta)/\rho$. Split $\mathsf R=\mathsf R_A+\mathsf R_Q$ into the
  log-concavity (Monge–Ampère) reservoir and the cyclic-square part.
- **(2.2) Spectral occupation.** Probes `w4w01`/`w4s01`: `q:mm-spectral-occupation` recast as
  weight removal on the initial layer plus a Grönwall bound on $q(t)=\mathbb E|g_t|^2$,
  producing the four-statement **initial-layer window chain** (Lemmas A–D + Theorem E).
- **(2.3) Screened weighted interface.** Cut scale $\lambda_{\mathrm{cut}}(A,K)$,
  $W_{\mathrm{cut}}=(1+\lambda_{\mathrm{cut}})^{5/2}$, aligned set
  $\mathcal A_\kappa=\{Q_t\ge\kappa e_tW_{\mathrm{cut}}\}$, admissibility
  $2\beta/(1-\theta)+64\eta^2<1$.
- **(2.5) All-frame simplex dual.** $\Lambda_{m,k}$ and the root-frame degree-2 identity
  $\lambda^{\mathrm{root}}_{m,2}=(m+2)(m+3)/(5m^2)$.

Not opened, deliberately: the trace-upgrade cluster (`q:upgrade`, high-rank
`q:stein-weighted`, `q:alignment`, and the gate-zero proof half), per hard constraint 6. No
fan-out occurred across it and no comparison between its members was asserted.

## Outcome — five certifications

All five went through the full chain (prober → orchestrator node acceptance → prover dossier
with `checked_by: none` → *distinct, cold* proof-checker → orchestrator atomic wiring). No
author reviewed their own dossier.

| node | status | content | review |
|---|---|---|---|
| `prop:split-screened-supply` | **proved** | screened supply $\le(2k+64\eta^2(1+k))/\kappa$; spectator-inert; dimension-free; on the regular split class | `2026-08-30-prop-split-screened-supply-proof-review.md` |
| `lem:mm-restart-deweighting` | **proved** | unconditional strong-Markov restart de-weighting | `2026-08-30-lem-mm-restart-deweighting-proof-review.md` |
| `lem:mm-smallgap-fourth-moment` | **proved** | fourth-moment small-gap control | `2026-08-30-lem-mm-smallgap-fourth-moment-proof-review.md` |
| `lem:mm-stopped-window-source` | conditional | stopped-window source term, conditional on `thm:letwin-qcts` | `2026-08-30-lem-mm-stopped-window-source-proof-review.md` |
| `prop:mm-window-occupation` | conditional | $C_P\le C\log^2n$ for **every** isotropic log-concave law on $\mathbb R^n$, $n\ge2$, conditional on `thm:letwin-qcts` | `2026-08-30-prop-mm-window-occupation-proof-review.md` |

`prop:mm-window-occupation` is the wave's headline: Route S (`moment-map-spectral`) now has a
complete end-to-end route-health certificate at polylog strength, with a single named residue,
the **post-spike charge**. Per hard constraint 7 it stays `conditional`; the Letwin hypothesis
is an explicit hypothesis of the statement, not an ambient assumption.

Also imported and wired: `thm:klartag-logn` (`imported`, published,
[Klartag2023Logarithmic]), which is what makes the $\log^2$ bookkeeping legible.

Ledger after the wave: **203 nodes, 684 labels, 0 errors**; kls plane 129 nodes
(proved 64, conditional 18, open 27, imported 16, refuted 2, defined 2).

## Outcome — structural findings (no status change)

- **`(AB)` decomposes.** `(AB)` $\iff$ a gate-zero-type inequality plus a high-mode excess
  term. Two channels, not one; a proof must control both (`w4c01`).
- **AIK is incomparable with tight-prefix-carleson** (`w4y01`). Neither implies the other.
  Consequence: Candidate B is a genuinely distinct route, not a relabeling of an existing one.
  Two entries promoted to `research/knowledge/lemmas.md` (screened-absorption preconditions;
  aligned-screen initial-layer reduction with the pathwise pin).
- **Fiber frames are pro-route at fixed degree** (`w4f01`): exact rational floors
  $\Lambda_{m,2}\ge0.344$, so no degree-2 dual certificate can refute the route; any
  fixed-degree polynomial refuter needs $k\ge3$.
- **Screening is inert-or-self-defeating on the tail-union model** (`w4a01`) — but that family
  is excluded by the near-worst premise, so this is a scope finding, not an obstruction. The
  run also corrected the brief: the coordinate-half-line surrogate excess *understates*
  ($\hat e\le e$), and the originally requested competitor family was inadmissible alone
  ($P_0=n\sqrt2(2^{1/n}-1)/2<1/\sqrt2$).
- **The log-concavity reservoir is load-bearing** (`w4c02`): the sharp form
  $\mathsf R\succeq\mathsf N/2$ is supported on every exactly solvable family; the exact 1D
  identity is $\mathsf N=2\mathsf D+\mathbb E[H^3V'']$; $M_9$ is pinned below $4$ by the
  log-concave boundary; and $\mathsf R_Q\succeq\mathsf D$ **fails directionally**. Hence any
  proof of `(AB)` must consume $\mathsf R_A$ — the cyclic-square part alone does not suffice.

Numerical work: three new `finum` targets (`kls-screen`, `cmh-ab`, `fiber-frame-dual`), 5
provenance-stamped artifacts under `research/runs/` (2 fiber-frame-dual, 2 kls-screen, 1
cmh-ab), decision records `2026-08-30-kls-screen-target.md` and
`2026-08-30-finum-cmh-ab-target.md`. Per hard constraint 2, none of it certifies anything: the
exact Loewner verdicts are refutation *candidates* awaiting an independently reviewed dossier.

## Why the wave stopped — interruption of 2026-08-30 (~22:00 Europe/Paris)

Three `fable` agents were terminated mid-run by an API rate limit,
`429 session limit · resets 11:30pm (Europe/Paris)`. This is a harness/quota event, not a
mathematical outcome, and it changed no status. State left on disk:

1. **prover `w4p03`** — `lem:cmh-linear-spectral-resolution`. Killed at the compile-and-record
   step, *after* writing the dossier. `solutions/lem-cmh-linear-spectral-resolution.tex`
   survives complete: 1114 lines through `\end{document}`, standalone `latexmk` build clean
   (11 unresolved `\ref`s, all cross-module manuscript labels, expected `??` standalone).
   Header carries `checked_by: none`, `reviewer:` empty — **no ledger value**. The agent's own
   exploration record was never written; this record substitutes for its provenance. The
   dossier is committed alongside this file so the work is not lost. Node stays `open`.
2. **proof-checker `w4r05`** — review of `solutions/lem-fiber-root-degree-two.tex` (dossier by
   `w4p04`, committed at `8edb752`). Wrote nothing; no review file exists. Node
   `lem:fiber-root-degree-two` stays `open` with an unreviewed dossier on disk.
3. **prover `w4p05`** — cyclic-square dossier deciding $\mathsf R_Q\succeq\mathsf D$ via
   Gaussian-product perturbation, following the `w4c02` directional failure. Killed early;
   wrote nothing. The intended node `rem:cmh-cyclic-square-not-loewner-integrated` was never
   accepted into the ledger and does not exist.

Nothing partial or corrupt was left in the ledger, manuscript, reviews, knowledge, targets, or
run artifacts. `check_ledger.py` is at 0 errors across the interruption.

## Resume queue (unblocked; the three tasks are mutually parallel)

1. **Cold proof-checker for `solutions/lem-cmh-linear-spectral-resolution.tex`.** Must be a
   distinct agent from `w4p03`. Review to
   `research/reviews/2026-08-31-lem-cmh-linear-spectral-resolution-proof-review.md`. On pass,
   the orchestrator wires `solution`/`checked_by`/`review`/`status` atomically; note the
   dossier's claim set is P0–P3, P6, P7 of the `w4c01` record, so a scope check against the
   manuscript statement in `modules/kls/41-cmh-normalization.tex` is mandatory (the analogous
   check caught a real scope mismatch on `prop:split-screened-supply` at `w4r01`).
2. **Relaunch proof-checker `w4r05`** for `solutions/lem-fiber-root-degree-two.tex` →
   `research/reviews/2026-08-31-lem-fiber-root-degree-two-proof-review.md`. On pass the node
   becomes `proved` (its content is unconditional).
3. **Relaunch prover `w4p05`** for the cyclic-square decision. Requires orchestrator ledger
   acceptance of the node *first* — it does not yet exist, so `check_ledger.py` would reject a
   dossier pointing at it.

Remaining close-out, orchestrator-owned and not agent-blocked:

- batch the `research/kls/gating.md` updates (drafts exist in `w4w01` §8, the `w4y01` record,
  the `w4c01` two-channel line, the `w4s01` post-spike-charge line, and the fiber degree-2
  note);
- a **singleton** wave-end `synthesizer` to curate the six proposed adversarial instances into
  `research/knowledge/instances.md`: `stress-fiber-frame-simplex-pencil`,
  `stress-tailunion-cut-scale`, `stress-cylinder-spectator-excess`,
  `stress-cmh-ab-exponential-limit`, `stress-cmh-ab-reservoir-split`, `fence-cmh-m9-boundary`
  (per hard constraint 3, only the synthesizer curates the registry);
- full manuscript `latexmk` build plus `check_ledger.py` plus the `finum` test lane.

## Standing risk carried forward

Two of the five certifications, including the headline $C_P\le C\log^2n$, hang on
`thm:letwin-qcts`, imported from a v1 preprint. The user has judged that preprint solid and
accepted the risk explicitly. It remains recorded here because a withdrawal would demote
`lem:mm-stopped-window-source` and `prop:mm-window-occupation` together, and with them the
whole Route-S certificate. The conditional statuses, per hard constraint 7, already make that
dependency explicit rather than ambient.
