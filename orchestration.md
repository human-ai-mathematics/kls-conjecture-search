# Orchestration — deploying an LLM-agent swarm against the open targets

How to run LLM agents against this repo's open problems: what to parallelize, the agent
roles, the dependency structure, the reward surface they optimize, and the constraints the
orchestration must respect. This is the *operations* companion to the control plane described
in [`research/README.md`](research/README.md).

> **Scope.** Parts II (A1–A5, A1-bis; refinement phase) and III (KLS; proof phase). The Lean
> channel ([`LEAN_DESIGN.md`](LEAN_DESIGN.md)) is a deferred long-pole foundation track, not a
> first-wave target.

---

## 0. The key premise: this repo is already a blackboard architecture

The orchestration problem is *not* "bolt agents onto a manuscript." The control plane an agent
swarm needs already exists, and every agent role below maps onto a contract it already enforces:

- **A machine-readable frontier** — two `ledger.yaml` files (104 nodes) with `status`,
  `evidence`, and a typed dependency DAG (`depends_on` / `unlocks` / `bounded_by` / `bridges`).
- **A deterministic reward gate** — `research/check_ledger.py` (acyclicity, no-proved-on-unproved,
  obstruction parity, bridge resolution, the `checked_by` proof ladder).
- **A numerical reward channel with a soundness contract** — `finum` (`experiments/`): the only
  sound verdict is **REFUTED**; corroboration is capped strictly below any checked proof.
- **A shared, fixed adversarial battery** — `research/knowledge/instances.md`, so a soft
  statement cannot be "validated" against a soft, self-chosen test set.
- **An append-only memory of dead ends** — `research/explorations/`, born precisely because two
  earlier agents ran private Monte Carlo, disagreed, and a non-reproducible claim had to be
  retracted.

So the design question is: *map agent roles onto the contracts this plane already enforces.*

---

## 1. The reward surface — what agents optimize

Three reward signals, **strictly ordered**. This ordering is the soundness contract, and it
dictates what can be safely parallelized.

| Signal | Mechanism | Soundness | Earned by |
|---|---|---|---|
| **R0 — structural** | `check_ledger.py` returns 0 errors | cheap, deterministic; necessary, *not* sufficient | every agent, every commit |
| **R1 — numerical** | provenance-stamped `finum` artifact in `research/runs/` | **only REFUTED is sound**; everything else is *direction*, capped | numerical agents |
| **R2 — proof** | `solutions/<id>.tex` (+ later `.lean`) with `checked_by ∈ {human, lean}` flips the node to `proved` | the **only** promotion to `proved` | prover + critic, or Lean |

**The invariant the swarm must never violate: R1 can never masquerade as R2.** An agent that
"passes numerics" has produced *evidence for a prover*, never a proof. Mechanically:
`finum` never edits the ledger; `numerical-strong` requires an `evidence_run`; `proved` requires
`checked_by ∈ {human, lean}` **and** an existing `solution:` file. This single rule is why
**criticism is a first-class role, not QA** (§4).

**Definition of done (Phase 1)**, from `research/README.md`, is the per-node reward target:

1. the target's `.tex` conjecture is sharpened (or confirmed) to its precise form;
2. the `ledger.yaml` node is updated (`status`, `evidence`, `evidence_run`, edges);
3. `python3 research/check_ledger.py` returns 0 errors;
4. the attempt — **including dead ends** — is logged in `explorations/YYYY-MM-DD-slug.md`;
   cross-cutting findings are promoted to `knowledge/`.

---

## 2. Parallelization map

Four orthogonal axes. **A** and **B** are embarrassingly parallel today; **C** and **D** carry
the real dependencies and the merge barriers.

### Axis A — independent targets (fan out 6 wide today)

A1–A5 are *federated, not merged*: separate target notebooks, separate obstructions, separate
`finum` targets. KLS is a separate program (`program: kls`). The six streams share nothing
**writable** except `ledger.yaml` and `knowledge/` (see the contention constraint, §6).

```
A1  A2  A3  A4  A5        KLS
 │   │   │   │   │          │
 └───┴───┴───┴───┘          │   ← 5 A-series Phase-1 squads, fully parallel
   research/ledger.yaml     research/kls/.../ledger.yaml
       (program: ab)             (program: kls)
```

### Axis B — the role pipeline within a node

`analysis → numerical → NL proof → criticism → Lean`. Different agent types; serial *per node*,
but pipelined *across nodes* (A2's analyst runs while A1's numerical agent is sampling).

### Axis C — the per-target DAG (respect the edges)

```
conj:a1 ─unlocks─► q:a1-barw ───────► q:a1-tail        (the heart; gated on barw)
                └► q:a1-poincare ───► q:a1-sharp ──┐
                                                    ├── converges with ──► conj:a2  (n→∞ limit)
conj:a1-bis ───────────────── bridges ────────────► kls/thm:intro-all-cut
```

`q:a1-tail` ("certify π(G^c) ≤ ε") is flagged in the notebook as **the heart** and is *hard*; it
depends on `q:a1-barw` (choose the `W̄` recipe), which is *low* effort. Sequence accordingly.

### Axis D — KLS route structure (proof-phase; the bottleneck is *discharging open assumptions*)

```
Route A:  q:upgrade ──────────────────► ass:all-cut-carleson ─► thm:intro-all-cut ─► KLS
Route B:  q:weighted + q:stein-weighted ─► ass:weighted-package ─► thm:intro-weighted ─► KLS
                         ▲
                q:splitting (constant mode) feeds q:stein-weighted
```

KLS is 38/59 nodes `proved`; the conditional headline theorems already hold. The whole game is
discharging the **open** assumptions `ass:all-cut-carleson` / `ass:weighted-package` (and
`ass:stopped-centroid`). Numerics here are **directional/refutation only** (`finum.localization`,
target `kls-loc`).

### The three merge barriers (do NOT fan out across these — converge)

1. **A1 ↔ A2 consistency** — `q:a1-sharp` must reproduce `λmax(I⁻¹)` as `n→∞` (`conj:a2`,
   `thm:a2-target`). A bulk-tight A1 bound and the BvM limit must agree.
2. **A1-bis ↔ KLS bridge** — `conj:a1-bis` (`C_P ≤ K·λmax(Cov)` for structured GLM posteriors)
   is the structured shadow of `kls/thm:intro-all-cut` (the same bound for *every* isotropic
   log-concave measure **is** KLS).
3. **The trace-upgrade unification** — `rem:trace-upgrade-unification` proves that `q:upgrade`,
   the high-rank part of `q:stein-weighted`, and `q:alignment` are the **same** operator-to-trace
   problem in three coordinate systems. Crack it once, propagate to both routes. **One team owns
   this** — do not spawn three blind teams against the same wall.

---

## 3. Current frontier (where the swarm actually picks up)

Read straight off the ledgers — this is the honest starting state, not an aspiration.

**A-series (`research/ledger.yaml`, program: ab).** Every `conj:a*` is `status: open`,
`evidence: none`. The obstruction nodes (`obs:flat-direction`, `obs:tv-insufficient`,
`obs:heavy-tail-no-classical`, `obs:restricted-not-finite`, `obs:symmetry-vs-physical`) are
`proved`/`imported` and **already carry `evidence_run`** — the `finum` work to date
*demonstrates the obstructions* (refutations), it has **not** validated a positive refined
conjecture. **No conjecture is `numerical-strong` yet.** So the live frontier is Phase-1
*positive* refinement: move `conj:aX` from `open → conjectured` + `evidence: numerical-strong`,
surviving the **shared** battery.

**KLS (`research/kls/.../ledger.yaml`, program: kls).** Open assumptions and questions:
`ass:stopped-centroid`, `ass:all-cut-carleson`, `ass:weighted-package`; `q:upgrade`,
`q:weighted`, `q:stein-weighted`, `q:taming`, `q:splitting`, `q:alignment`; `prog:product-test`.
The single most informative open computation is `q:alignment` (P6) — finite-dimensional in
difficulty, thin-shell test family, `finum run --target kls-loc`.

---

## 4. Agent roster (I/O contracts tied to the ledger)

| Role | Reads | Produces | Reward earned | Parallel |
|---|---|---|---|---|
| **Orchestrator / ledger-keeper** | both ledgers, `check_ledger.py` | node assignments; **the only writer of `ledger.yaml`** | keeps R0 green | singleton |
| **Analyst / refiner** (Phase 1) | `targets/*.md`, `modules/**/*.tex`, `obstructions.md` | sharpened statement + `numerics:` spec | statement respects every `bounded_by` | 1 / target |
| **Numerical** (finum) | the refined spec, `instances.md` | provenance-stamped `runs/*.jsonl` | R1 (REFUTE / direction) | 1 / target |
| **Prover** (Phase 2, NL) | a node that is `conjectured` + `numerical-strong` | `solutions/<id>.tex`, `checked_by: none` | unlocks R2 | per ready node |
| **Critic / adversary** | a conjecture *or* a draft proof | a refuting instance, a proof-gap report, or `checked_by: human` | gates R1→R2 | N / claim |
| **Lean** (deferred) | `proved` nodes + `LEAN_DESIGN.md` spine | `solutions/<id>.lean`, `checked_by: lean` | R2 (machine) | foundation track |
| **Librarian** | `explorations/`, `knowledge/` | dedup, promote findings, kill dead-end reruns | keeps memory honest | singleton |

**The critic is load-bearing** (this is the cultural center of the repo):

- *Refinement phase* → **refutation-seeker.** Find the battery instance — or a new one worth
  curating — that breaks the proposed sharp form. Use the diverse-lens pattern: one skeptic per
  failure mode (tail / anisotropy / heavy-tail / multimodality / funnel), each blind to the
  others. A conjecture is only `numerical-strong` after surviving the *shared* battery, not the
  refiner's happy path.
- *Proof phase* → **checker.** The **only** role permitted to set `checked_by: human`. This is
  what caught the Klartag–Lehec window citation debt (`rem:kl-window-verified`). Never let a
  prover grade its own proof.

---

## 5. Deployment plan — the first wave

What to actually launch now, given §3.

- **6 parallel squads**, each `{analyst + numerical + 2 adversaries}`:
  - **A1** (the flagship — start here as the reference squad; most tractable, log-concave, the
    entry point for the whole numerical channel),
  - **A2, A3, A4, A5**,
  - **KLS-direction** (numerical-only: `q:alignment` thin-shell + `q:upgrade` occupation via
    `kls-loc`; everything else KLS is proof-phase prose).
  - Per A-squad goal: `conj:aX` from `open → conjectured` + `evidence: numerical-strong`,
    surviving the shared battery, beating the `thm:glm-fi` baseline where applicable.
- **1 Lean foundation track** (long pole; "for later"): only the FI vocabulary spine
  (`HasPoincaré`, `HasLSI`, the entropy + Dirichlet functionals) plus the two low-effort nodes
  `lem:linear-test-lower` and `lem:a5-lipschitz`. `LEAN_DESIGN.md` is honest that this is a
  12–18-month, mostly greenfield effort — **do not over-invest agents here in wave 1.**
- **1 orchestrator + 1 librarian** as singletons.
- **Hold all Phase-2 NL provers.** Nothing is `conjectured` + `numerical-strong` yet, so a prover
  has nothing to pick up. Spawn them the moment the first node flips.

**Suggested cadence.** Run A1 end-to-end first as the reference implementation of the squad
contract (analyst sharpens → numerical stress vs `instances.md` → adversaries try to refute →
orchestrator merges the ledger update → librarian logs the exploration). Generalize the squad to
A2–A5 only once A1's loop closes cleanly through `check_ledger`.

---

## 6. Hard constraints the orchestration must respect (anti-patterns)

Specific to *this* repo; a naive swarm will hit every one of these.

1. **`ledger.yaml` is a single-file write-contention point.** Git-worktree isolation (excellent
   for parallel `finum`/`solutions` code) does **not** help a shared YAML. → Funnel *all* ledger
   edits through the orchestrator; squads write only to their `targets/*.md`, `explorations/`,
   `runs/`, and (provers) `solutions/`.
2. **No private Monte Carlo.** The retraction that created `explorations/` is the cautionary
   tale. Every numerical claim flows through `finum` with provenance (git hash + seed + library
   versions), or it does not count. Disagreeing ad-hoc scripts are how you get a retraction.
3. **The battery is fixed and shared.** An agent must not mint its own happy-path instances to
   clear `numerical-strong` — that is reward-hacking the soundness gate. New instances are
   *curated in* by the librarian into `knowledge/instances.md`, not minted by the refiner.
4. **`check_ledger.py` is necessary, not sufficient.** It verifies structure (labels exist, DAG
   acyclic, no proved-on-unproved, obstruction parity) but **not** that the `.tex` prose and the
   ledger `statement:` agree semantically — that is a critic's responsibility.
5. **Respect `bounded_by`.** A refined statement that violates a known obstruction is wrong by
   construction (e.g. any A1 bound without a tail term violates `obs:flat-direction`). The
   analyst checks this *before* the numerical agent spends a run.
6. **Don't fan out across the trace-upgrade unification.** `q:upgrade` = `q:alignment` =
   high-rank `q:stein-weighted` — one team, then propagate (§2, barrier 3).
7. **`conditional` KLS nodes are Lean-certifiable only as conditional implications.** The
   assumption becomes a Lean hypothesis; the node reaches unconditional `proved` only when the
   assumption is discharged. `check_ledger.py` enforces `no proved-on-open`.

---

## 7. Mapping to this harness (how to actually run it)

- **Squads → subagents.** Each squad role is a subagent with the I/O contract from §4 baked into
  its prompt. Independent squads launch concurrently. The empty `.agents/` and `.codex/`
  directories are the natural home for these role definitions.
- **Numerical isolation.** Numerical and prover agents that *write code* (`finum` targets,
  `solutions/*.tex`) should run in **git-worktree isolation** to avoid clobbering each other; the
  orchestrator integrates. The ledger edit itself stays serialized through the orchestrator
  (constraint §6.1) — worktrees do not solve YAML contention.
- **Deterministic fan-out → verify → merge.** The 6-squad wave is a natural pipeline: per target,
  `refine → finum-stress → adversarial-verify (N skeptics) → ledger-merge`, with the three
  barriers of §2 as explicit synchronization points. Per-target chains run independently; only
  the barriers join them.
- **The gate is the test.** After every ledger-touching step, `python3 research/check_ledger.py`
  must return 0 errors — it is the cheap, deterministic R0 signal that fires continuously.

---

*Companion documents: [`research/README.md`](research/README.md) (two-phase control plane),
[`experiments/README.md`](experiments/README.md) (the `finum` numerical channel),
[`solutions/README.md`](solutions/README.md) (the `checked_by` proof ladder),
[`LEAN_DESIGN.md`](LEAN_DESIGN.md) (the deferred Lean channel and Mathlib gap).*
