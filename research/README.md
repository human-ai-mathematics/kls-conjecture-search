# research/ — the open-target control plane

This directory is where agents **refine the open targets into sharp, numerically
validated theorems** (Phase 1), so another agent can **prove them later** (Phase 2;
natural language first, Lean deferred). It is the *control plane*: Markdown + YAML that
agents read and edit freely. The *content plane* is the LaTeX in `../modules/` (the
formal statements and proofs that compile into the PDF).

## The two-phase workflow

```
   open statement (modules/open-targets/*.tex)
        │   Phase 1 — refine + numerically validate  (this directory + finum)
        ▼
   conjectured + evidence: numerical-strong   ←  the handoff artifact
        │   Phase 2 — prove  (natural language; Lean later)
        ▼
   proved
```

**Numerics refine and refute; they never prove.** "Seems valid numerically" is
`status: conjectured, evidence: numerical-strong` — it is evidence for a prover to pick
up, never a substitute for a proof.

## Layout

Two programs, federated under one control plane, one shared checker, cross-linked by a bridge.

```
research/
  ledger.yaml      A-series (Parts I/II, program: ab) — single source of truth for A1-A5:
                   every statement + obstruction, status, evidence, dependency edges.
  check_ledger.py  program-aware checker for BOTH ledgers (ids resolve, acyclic, file paths
                   exist, no proved-on-unproved, KLS no-go set, cross-program bridges).
  targets/         one working notebook per A-series target (A1-A5).
  knowledge/       the COMMON cross-cutting database (math in LaTeX $…$):
                     obstructions.md  no-go forms / barriers (with numerical demos)
                     lemmas.md        shared tools (linear-test LB, Hardy, Holley-Stroock)
                     instances.md     the shared, curated stress battery
  explorations/    dated attempt log, INCLUDING dead ends (so no one re-runs them)
  kls/             Part III (program: kls) — EXPLORATORY: organized by route, not one DAG.
                     routes.md            registry of attacks + how to open a new route
                     shared/              route-agnostic truth (target.md, lower-bounds.md)
                     routes/eldan-localization/   the active attack — carries the kls ledger:
                       ledger.yaml obstructions.yaml obstructions.md open-problems.md roadmap.md
```

The Phase-2 output plane is a **repo-root sibling**, `../solutions/`: standalone,
human-checkable `.tex` proofs that a `proved` ledger node points to (via a `solution:` field) —
symmetric with how `evidence_run:` backs `numerical-strong`. See `../solutions/README.md`.

**Why two ledgers, not one.** The A-series is in the *refinement* phase (sharpen statements;
`finum` validates/refutes); KLS is already a *proof* program (crisp statements; discharge
assumptions; numerics only refute/direct). They use the same status/edge grammar and one
checker, but KLS keeps the heavier machine-enforced no-go set it needs. The **bridge** is
`conj:a1-bis` (structured-posterior `C_P ≤ K·λmax(Cov)`) → `kls/thm:intro-all-cut`: the same
bound for *every* isotropic log-concave measure **is** KLS (Part I's "Tier-∞" boundary).
See `kls/README.md`.

## Status & evidence vocabulary

- **status** (logical state): `open` → `conjectured` → `proved`; plus `imported`
  (literature anchor) and `refuted` (the form was shown false).
- **evidence** (numerical support, orthogonal): `none` → `numerical-directional` →
  `numerical-strong` (passed the shared `knowledge/instances.md` battery, with
  `evidence_run:` pointing at the provenance-stamped `finum` artifact).

## How `finum` plugs in

The numerical package (`finum`, to be built) produces the `evidence` field. A run's
output is a provenance-stamped JSONL referenced by `evidence_run` in the ledger node.
There is no separate "reward subsystem": the ledger is where the signal lands, and the
signal is *"this refined statement survived the shared stress battery, tightness X."*

## Rules that keep "validated" honest

1. A `proved` node may not depend on an `open`/`conjectured`/`refuted` node (enforced).
2. `numerical-strong` requires passing the **shared** stress instances in
   `knowledge/instances.md` — not an agent's own happy-path cases (prevents a soft
   statement being "validated" against a soft battery).
3. Every conjecture lists the obstructions it must respect (`bounded_by`); a statement
   that violates a known obstruction is wrong by construction.

## Definition of done for a Phase-1 contribution

1. The target's `.tex` conjecture is sharpened (or confirmed) to its precise form.
2. `ledger.yaml` node updated: `status`, `evidence`, `evidence_run`, edges.
3. `python3 research/check_ledger.py` returns 0 errors.
4. The attempt (incl. dead ends) is logged in `explorations/YYYY-MM-DD-slug.md`;
   cross-cutting findings promoted to `knowledge/`.
