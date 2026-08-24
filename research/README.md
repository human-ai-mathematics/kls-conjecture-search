# research/ — the open-target control plane

This directory is where agents **refine open targets and certify analytic progress**.
Numerical stress tests and natural-language proofs are complementary channels; Lean remains
deferred. It is the *control plane*: Markdown + YAML that
agents read and edit freely. The *content plane* is the LaTeX in `../modules/` (the
formal statements and proofs that compile into the PDF).

## Refinement and proof channels

```
   open statement (modules/open-targets/*.tex)
        ├── refine / stress with finum ──► conjectured + numerical evidence
        └── analytic proof + independent review ──► proved
```

**Numerics refine and refute; they never prove** — the R1/R2 contract in
[`../CLAUDE.md`](../CLAUDE.md). In this plane's vocabulary, "seems valid numerically" is
`status: conjectured, evidence: numerical-strong`. A complete analytic proof need not wait for
numerical evidence.

## Layout

Two programs, federated under one control plane, one shared checker, cross-linked by a bridge.

```
research/
  ledger.yaml      A-series (Parts I/II, program: ab) — single source of truth for A1-A5:
                   every statement + obstruction, status, evidence, dependency edges.
  check_ledger.py  program-aware checker for BOTH ledgers (unique ids/programs, resolved edges,
                   recursive assumption/status safety, evidence provenance, KLS obstruction
                   reverse parity, cross-program bridges).
  targets/         one working notebook per A-series target (A1-A5).
  knowledge/       the COMMON cross-cutting database (math in LaTeX $…$):
                     obstructions.md  no-go forms / barriers (with numerical demos)
                     lemmas.md        shared tools (linear-test LB, Hardy, Holley-Stroock)
                     instances.md     the shared, curated stress battery
  explorations/    dated attempt log, INCLUDING dead ends (so no one re-runs them)
  reviews/         persisted scope/verdict reports for independent-agent proof certification
  kls/             Part III (program: kls) — EXPLORATORY: organized by route, not one DAG.
                     routes.md            registry of attacks + how to open a new route
                     shared/              route-agnostic truth (target.md, lower-bounds.md)
                     routes/eldan-localization/   the active attack — carries the kls ledger:
                       ledger.yaml obstructions.yaml obstructions.md open-problems.md roadmap.md
                     routes/moment-map-spectral/ prose-only fixed-eigenfunction dynamic route
```

The current KLS route decision, including the completed product-alignment diagnostic and the
audited $H^{-1}$ endpoint, is in
[`explorations/2026-08-20-kls-program-cycle-1.md`](explorations/2026-08-20-kls-program-cycle-1.md).
For A1--A5, the current certified-probe summary records 21 independently reviewed positive
intermediate nodes and the remaining live frontiers:
[`explorations/2026-08-21-a-series-proof-probes.md`](explorations/2026-08-21-a-series-proof-probes.md).

The proof output plane is a **repo-root sibling**, `../solutions/`: standalone,
reviewable `.tex` proofs that a `proved` ledger node points to (via a `solution:` field) —
symmetric with how `evidence_run:` backs `numerical-strong`. Certification may be an independent
agent audit with persisted provenance, human acceptance, or Lean; see `../solutions/README.md`.
New proof promotions should use this plane. Five elementary results predating it---the linear-test
lemma, the data-free GLM baseline, the exact TV-contamination obstruction, and the A5 monotonicity
and Lipschitz anchors---retain narrow, explicitly documented `proof_provenance` exceptions.

**Why two ledgers, not one.** The A-series combines refinement with active proof certification;
KLS is organized as a route-based proof program (crisp statements; discharge assumptions;
numerics only refute/direct). They use the same status/edge grammar and one
checker, but KLS keeps the heavier machine-enforced no-go set it needs. The **bridge** is
`conj:a1-bis` (structured-posterior `C_P ≤ K·λmax(Cov)`) → `kls/thm:intro-all-cut`: the same
bound for *every* isotropic log-concave measure **is** KLS (Part I's "Tier-∞" boundary).
See `kls/README.md`.

## Status & evidence vocabulary

- **A-series status**: `open` → `conjectured` → `proved`, plus `imported` and `refuted`.
- **KLS status**: `proved`, `conditional`, `open`, `heuristic`, `refuted`, or `imported`.
- **evidence** (numerical support, orthogonal): `none` → `numerical-directional` →
  `numerical-strong` (passed the shared `knowledge/instances.md` battery, with
  `evidence_run:` pointing at the provenance-stamped `finum` artifact).

> **`numerical-strong` is not yet reachable.** The checker requires the artifact's provenance
> params to carry `shared_battery_passed: true` and `shared_battery:
> research/knowledge/instances.md`, plus a calibration pass and a verdict record. No `finum`
> target emits the battery flags today, so every current run tops out at
> `numerical-directional`. The gate is deliberately kept in place; closing the gap means
> building a shared-battery runner in `finum` (see `experiments/README.md`).

## How `finum` plugs in

The numerical package (`finum`, implemented under `experiments/`) produces the `evidence` field. An
evidence-eligible run's output is a provenance-stamped JSONL referenced by `evidence_run` in the ledger node.
There is no separate "reward subsystem": the ledger is where the signal lands, and the
signal is *"this refined statement survived the shared stress battery, tightness X."*

## Rules that keep "validated" honest

1. A `proved` node may not inherit an unresolved dependency or `assuming` edge. For KLS this
   explicitly includes `conditional`, `heuristic`, and imported nodes marked
   `import_class: preprint-unreviewed`; conditional nodes must declare and recursively propagate
   a non-empty `assuming` contract. Imported nodes default to `import_class: published`.
2. Evidence-eligible numerics require an existing, valid provenance-stamped JSONL and an
   explicit matching `evidence_target`. Reproducibility rests on the recorded seed, params, and
   library versions; the state of the worktree is not gated. Retired legacy diagnostics belong in the
   dated exploration record, not as live ledger evidence. `numerical-strong` additionally requires
   successful calibration, an explicit shared-battery pass, and a verdict record.
3. Every conjecture lists the obstructions it must respect (`bounded_by`); for KLS the checker
   enforces exact reverse parity with `obstructions.yaml.constrains` and requires clearance for
   both forbidden and methodological-warning mechanisms.
4. A program has exactly one ledger until explicit merge semantics are implemented; duplicate
   program ledgers and duplicate node ids fail rather than overwrite.

## Definition of done for a contribution

The four-step contract and the commands that check it are in [`../CLAUDE.md`](../CLAUDE.md).
