# Orchestration — parallelizing agents across the open targets

What can run concurrently, where the merge barriers are, and what each agent role reads and
produces. The rules every agent works under — the soundness contract, the definition of done,
the hard constraints — are in [`CLAUDE.md`](CLAUDE.md).

> **Scope.** Parts II (A1–A5, A1-bis; refinement plus active proof certification) and III
> (KLS; route-based proof program). The Lean channel
> ([`LEAN_DESIGN.md`](LEAN_DESIGN.md)) is a deferred long-pole foundation track, not a
> first-wave target.
>
> **The live frontier is not narrated here** — it goes stale. Read it off
> `python3 research/check_ledger.py`, the two ledgers, and the current cycle summaries:
> [`research/explorations/2026-08-21-a-series-proof-probes.md`](research/explorations/2026-08-21-a-series-proof-probes.md)
> (A-series) and [`research/kls/gating.md`](research/kls/gating.md) (KLS).

---

## 1. Parallelization map

Four orthogonal axes. **A** and **B** are embarrassingly parallel today; **C** and **D** carry
the real dependencies and the merge barriers.

### Axis A — independent target streams

A1–A5 are *federated, not merged*: separate target notebooks, separate obstructions, separate
`finum` targets. KLS is a separate program (`program: kls`). The six streams share nothing
**writable** except `ledger.yaml` and `knowledge/` (see hard constraint 1 in [`CLAUDE.md`](CLAUDE.md)).

```
A1  A2  A3  A4  A5        KLS
 │   │   │   │   │          │
 └───┴───┴───┴───┘          │   ← 5 A-series target streams, fully parallel
   research/ledger.yaml     research/kls/.../ledger.yaml
       (program: ab)             (program: kls)
```

### Axis B — the role pipeline within a node

`analysis → {numerical stress and/or NL proof} → criticism → Lean`. Different agent types can be
pipelined across nodes; numerical stress is optional when a complete analytic argument is ready.

### Axis C — the per-target DAG (respect the edges)

```
prop:a1-bulk-tail + prop:a1-mode-leverage ─► q:a1-barw ─► q:a1-tail
prop:a1-euclidean-harmonic ─► q:a1-poincare ─► q:a1-sharp ─┐
cor:a1-leverage-asymptotic ─────────────────────────────────┴──► meets conj:a2
conj:a1 ─► conj:a1-bis
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

KLS is 41/68 nodes `proved`; the conditional headline theorems already hold. The whole game is
discharging the **open** assumptions `ass:all-cut-carleson` / `ass:weighted-package` (and
`ass:stopped-centroid`). Numerics here are **directional/refutation only** (`finum.localization`,
target `kls-loc`). The single most informative open computation is `q:alignment` (P6):
finite-dimensional in difficulty, thin-shell test family, `finum run --target kls-align`.

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

## 2. Agent roster (I/O contracts tied to the ledger)

| Role | Reads | Produces | Reward earned | Parallel |
|---|---|---|---|---|
| **Orchestrator / ledger-keeper** | both ledgers, `check_ledger.py` | node assignments; **the only writer of `ledger.yaml`** | keeps R0 green | singleton |
| **Analyst / refiner** | `targets/*.md`, `modules/**/*.tex`, `obstructions.md` | sharpened statement and optional `numerics:` spec | statement respects every `bounded_by` | 1 / target |
| **Numerical** (finum) | the refined spec, `instances.md` | provenance-stamped `runs/*.jsonl` | R1 (REFUTE / direction) | 1 / target |
| **Prover** (NL) | a precise open/conjectured node; numerical evidence if available | `solutions/<id>.tex`, `checked_by: none` | unlocks R2 | per ready node |
| **Critic / adversary** | a conjecture *or* a draft proof | a refuting instance, a proof-gap report, or an independent `checked_by: agent|human` audit | gates proof certification | N / claim |
| **Lean** (deferred) | `proved` nodes + `LEAN_DESIGN.md` spine | `solutions/<id>.lean`, `checked_by: lean` | R2 (machine) | foundation track |
| **Librarian** | `explorations/`, `knowledge/` | dedup, promote findings, kill dead-end reruns | keeps memory honest | singleton |

**The critic is load-bearing** (the cultural center of this repo):

- *Numerical/refinement channel* → **refutation-seeker.** Find the battery instance — or a new one worth
  curating — that breaks the proposed sharp form. Use the diverse-lens pattern: one skeptic per
  failure mode (tail / anisotropy / heavy-tail / multimodality / funnel), each blind to the
  others. A conjecture is only `numerical-strong` after surviving the *shared* battery, not the
  refiner's happy path.
- *Proof channel* → **checker.** A human may set `checked_by: human`; a distinct critic agent may
  set `checked_by: agent` only with a persisted scope report. This is what caught the
  Klartag–Lehec window citation debt (`rem:kl-window-verified`). Never let a prover grade its
  own proof.

---

*Companion documents: [`CLAUDE.md`](CLAUDE.md) (the rules),
[`research/README.md`](research/README.md) (control plane),
[`experiments/README.md`](experiments/README.md) (the `finum` numerical channel),
[`solutions/README.md`](solutions/README.md) (the `checked_by` proof ladder),
[`LEAN_DESIGN.md`](LEAN_DESIGN.md) (the deferred Lean channel and Mathlib gap).*
