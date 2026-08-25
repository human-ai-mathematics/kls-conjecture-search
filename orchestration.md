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
> `python3 research/check_ledger.py`, the two ledgers, and the current strategy/cycle summaries:
> [`research/explorations/2026-08-21-a-series-proof-probes.md`](research/explorations/2026-08-21-a-series-proof-probes.md)
> (A-series), plus [`research/kls/strategy-map.md`](research/kls/strategy-map.md),
> [`research/kls/routes.md`](research/kls/routes.md), and the
> [August 24 synthesis](research/explorations/2026-08-24-kls-moment-map-cmh-consolidation.md)
> (KLS). `research/kls/gating.md` records numerical implementation status only.

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
   research/ledger.yaml       research/kls/ledger.yaml
       (program: ab)             (program: kls)
```

### Axis B — the role pipeline within a node

Numerical stress is an optional research loop around refinement. The certification pipeline is
`analysis → NL proof → criticism → Lean`; numerical outcomes are not inputs to its validity.
Different agent types can be pipelined across nodes.

### Axis C — the per-target DAG (respect the edges)

`depends_on` is the ledger's canonical dependency relation. The forward arrows below are a
roadmap view obtained by reversing those dependencies where applicable; they are not stored as a
second forward-edge relation.

```
prop:a1-bulk-tail + prop:a1-mode-leverage ─► q:a1-barw ─► q:a1-tail
prop:a1-euclidean-harmonic ─► q:a1-poincare ─► q:a1-sharp ─┐
cor:a1-leverage-asymptotic ─────────────────────────────────┴──► meets conj:a2
conj:a1 ─► conj:a1-bis
conj:a1-bis ───────────────── bridges ───────────────────► kls/conj:kls
```

`q:a1-tail` ("certify π(G^c) ≤ ε") is flagged in the notebook as **the heart** and is *hard*; it
depends on `q:a1-barw` (choose the `W̄` recipe), which is *low* effort. Sequence accordingly.

### Axis D — KLS route structure (proof-phase; discharge route-specific open targets)

```
Eldan-A:  q:upgrade ──────────────────► ass:all-cut-carleson ─► thm:intro-all-cut ─► KLS
Eldan-B:  q:weighted + q:stein-weighted ─► ass:weighted-package ─► thm:intro-weighted ─► KLS
                         ▲
                q:splitting (constant mode) feeds q:stein-weighted

Spectral:  fixed-eigenfunction source/damping ─► universal-time unwhitening ─► KLS

CMH:  endpoint audit + invariant lift/all-split reduction
                         ─► q:mm-square-root-commutator ─► full Haar sum ─► CMH ─► KLS
```

The Eldan conditional headline theorems already hold in the inline manuscript, subject to the
agent-reviewed R2 dossiers for the former inline KLS backbone. Its open assumptions are
`ass:all-cut-carleson` / `ass:weighted-package` (and `ass:stopped-centroid`). The spectral
sufficiency bridge and the CMH universal headline remain open, although the CMH regular-class
normalization and exact model classes have proved internal nodes. Numerics are
**directional research only**: `kls-align` implements one designated P6 family, while
`cmh-gate-zero` implements calibration observables on already-proved model classes and no
construction-layer CMH observable.

### The three merge barriers (do NOT fan out across these — converge)

1. **A1 ↔ A2 consistency** — `q:a1-sharp` must reproduce `λmax(I⁻¹)` as `n→∞` (`conj:a2`,
   `thm:a2-target`). A bulk-tight A1 bound and the BvM limit must agree.
2. **A1-bis ↔ KLS bridge** — `conj:a1-bis` (`C_P ≤ K·λmax(Cov)` for structured GLM posteriors)
   is the structured shadow of the route-neutral `kls/conj:kls` (the same bound for *every*
   isotropic log-concave measure **is** KLS).
3. **The trace-upgrade cluster** — `q:upgrade`, the high-rank part of `q:stein-weighted`, and
   `q:alignment` exhibit the same high-rank occupation difficulty, but
   `rem:trace-upgrade-unification` explicitly says their formal equivalence is not proved.
   **One team owns the comparison**; propagate only implications that have actually been shown.
   The CMH square-root commutator is related through preservation of matrix orientation, not yet
   identified as a fourth equivalent formulation.

---

## 2. Agent roster (I/O contracts tied to the ledger)

| Role | Reads | Produces | Reward earned | Parallel |
|---|---|---|---|---|
| **Orchestrator / ledger-keeper** | both ledgers, `check_ledger.py` | node assignments; **the only writer of `ledger.yaml`** | keeps R0 green | singleton |
| **Analyst / refiner** | `targets/*.md`, `modules/**/*.tex`, `obstructions.md` | sharpened statement and optional `numerics:` spec | statement respects every `bounded_by` | 1 / target |
| **Numerical** (finum) | the refined spec, `instances.md` | provenance-stamped `runs/*.jsonl` | research direction / candidate refutation | 1 / target |
| **Prover** (NL) | a precise unresolved (`status: open`) node and analytic sources | `solutions/<id>.tex`, `checked_by: none` | supplies a dossier for R2 review | per ready node |
| **Critic / adversary** | a conjecture *or* a draft proof | a candidate refuting instance, a proof-gap report, or an independent `checked_by: agent|human` audit | gates proof certification | N / claim |
| **Lean** (deferred) | `proved` nodes + `LEAN_DESIGN.md` spine | `solutions/<id>.lean`, `checked_by: lean` | R2 (machine) | foundation track |
| **Librarian** | `explorations/`, `knowledge/` | dedup, promote findings, kill dead-end reruns | keeps memory honest | singleton |

**The critic is load-bearing** (the cultural center of this repo):

- *Numerical/refinement channel* → **refutation-seeker.** Find the battery instance — or a new one worth
  curating — that breaks the proposed sharp form. Use the diverse-lens pattern: one skeptic per
  failure mode (tail / anisotropy / heavy-tail / multimodality / funnel), each blind to the
  others. Record surviving and failing cases as directional research diagnostics. Survival of
  the shared battery does not validate the conjecture or any proof.
- *Proof channel* → **checker.** A human may set `checked_by: human`; a distinct critic agent may
  set `checked_by: agent` only with a persisted scope report. This is what caught the
  Klartag–Lehec window citation debt (`rem:kl-window-verified`). The checker audits the analytic
  argument independently of numerical outcomes. Never let a prover grade its own proof.

---

*Companion documents: [`CLAUDE.md`](CLAUDE.md) (the rules),
[`research/README.md`](research/README.md) (control plane),
[`experiments/README.md`](experiments/README.md) (the `finum` numerical channel),
[`solutions/README.md`](solutions/README.md) (the `checked_by` proof ladder),
[`LEAN_DESIGN.md`](LEAN_DESIGN.md) (the deferred Lean channel and Mathlib gap).*
