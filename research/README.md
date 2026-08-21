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
  check_ledger.py  program-aware checker for BOTH ledgers (unique ids/programs, resolved edges,
                   recursive assumption/status safety, evidence provenance, KLS obstruction
                   reverse parity, cross-program bridges).
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
                     routes/moment-map-spectral/ prose-only fixed-eigenfunction dynamic route
```

The current KLS route decision, including the completed product-alignment diagnostic and the
audited $H^{-1}$ endpoint, is in
[`explorations/2026-08-20-kls-program-cycle-1.md`](explorations/2026-08-20-kls-program-cycle-1.md).

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

- **A-series status**: `open` → `conjectured` → `proved`, plus `imported` and `refuted`.
- **KLS status**: `proved`, `conditional`, `open`, `heuristic`, `refuted`, or `imported`.
- **evidence** (numerical support, orthogonal): `none` → `numerical-directional` →
  `numerical-strong` (passed the shared `knowledge/instances.md` battery, with
  `evidence_run:` pointing at the provenance-stamped `finum` artifact).

## How `finum` plugs in

The numerical package (`finum`, implemented under `experiments/`) produces the `evidence` field. A run's
output is a provenance-stamped JSONL referenced by `evidence_run` in the ledger node.
There is no separate "reward subsystem": the ledger is where the signal lands, and the
signal is *"this refined statement survived the shared stress battery, tightness X."*

## Rules that keep "validated" honest

1. A `proved` node may not inherit an unresolved dependency or `assuming` edge. For KLS this
   explicitly includes `conditional`, `heuristic`, and imported nodes marked
   `import_class: preprint-unreviewed`; conditional nodes must declare and recursively propagate
   a non-empty `assuming` contract. Imported nodes default to `import_class: published`.
2. Evidence-eligible numerics require an existing, valid provenance-stamped JSONL from a clean
   commit and an explicit matching `evidence_target`. A dirty artifact may remain attached only
   as historical diagnostics with `evidence: none`; `evidence_eligible: false` does not override
   a non-`none` evidence claim. `numerical-strong` additionally requires successful calibration,
   an explicit shared-battery pass, and a verdict record.
3. Every conjecture lists the obstructions it must respect (`bounded_by`); for KLS the checker
   enforces exact reverse parity with `obstructions.yaml.constrains` and requires clearance for
   both forbidden and methodological-warning mechanisms.
4. A program has exactly one ledger until explicit merge semantics are implemented; duplicate
   program ledgers and duplicate node ids fail rather than overwrite.

## Definition of done for a Phase-1 contribution

1. The target's `.tex` conjecture is sharpened (or confirmed) to its precise form.
2. `ledger.yaml` node updated: `status`, `evidence`, `evidence_run`, edges.
3. `python3 research/check_ledger.py` returns 0 errors.
4. The attempt (incl. dead ends) is logged in `explorations/YYYY-MM-DD-slug.md`;
   cross-cutting findings promoted to `knowledge/`.

Focused checker regressions run with
`python3 -m unittest discover -s research/tests -p 'test_*.py'`.
