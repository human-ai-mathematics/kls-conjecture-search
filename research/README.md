# research/ — the open-target control plane

This directory is where agents **refine open targets and certify analytic progress**.
Numerical stress tests are a research aid; natural-language or Lean proofs are the certification
channels. It is the *control plane*: Markdown + YAML that
agents read and edit freely. The *content plane* is the LaTeX in `../modules/` (the
formal statements and proofs that compile into the PDF).

## Refinement and proof channels

```
   open statement (modules/open-targets/*.tex)
        ├── refine / stress with finum ──► directional research diagnostics
        └── analytic proof + independent review ──► proved
```

**Numerics guide intuition, stress candidate statements, and suggest refutations; they never
validate a claim or a proof** — the R1/R2 contract in [`../CLAUDE.md`](../CLAUDE.md). An
unresolved node remains `open` whether its statement is broad or already precise;
`kind: conjecture` identifies the statement type, not a separate resolution state. A node is
`proved` only through its independently checked proof dossier.

## Layout

Two programs, federated under one control plane, one shared checker, cross-linked by a bridge.

```
research/
  ledger.yaml      A-series (Parts I/II, program: ab) — single source of truth for A1-A5:
                   every statement + obstruction, status, diagnostic pointers, dependency edges.
  check_ledger.py  program-aware checker for BOTH ledgers (unique ids/programs, resolved edges,
                   recursive assumption/status safety, diagnostic artifact provenance, KLS obstruction
                   reverse parity, cross-program bridges).
  targets/         one working notebook per A-series target (A1-A5).
  knowledge/       the COMMON cross-cutting database (math in LaTeX $…$):
                     obstructions.md  no-go forms / barriers (with numerical demos)
                     lemmas.md        shared tools (linear-test LB, Hardy, Holley-Stroock)
                     instances.md     the shared, curated stress battery
  explorations/    dated attempt log, INCLUDING dead ends (so no one re-runs them)
  reviews/         persisted scope/verdict reports for independent-agent proof certification
  kls/             Part III (program: kls) — EXPLORATORY: one graph, organized by route.
                     ledger.yaml         one route-spanning claim graph (single writer)
                     strategy-map.md     current frontier and comparison of proof strategies
                     obstructions.*      machine fences, currently Eldan-route scoped
                     routes.md            registry of attacks + how to open a new route
                     shared/              route-agnostic truth (target.md, lower-bounds.md)
                     routes/eldan-localization/   fixed-cut subroutes + roadmap/open problems
                     routes/moment-map-spectral/ fixed-eigenfunction dynamic route
                     routes/moment-map-cmh/      deterministic Haar/Schur--Piola route
```

The August 20 fixed-eigenfunction cycle, including the completed product-alignment diagnostic and
the audited $H^{-1}$ endpoint, remains in
[`explorations/2026-08-20-kls-program-cycle-1.md`](explorations/2026-08-20-kls-program-cycle-1.md).
The current cross-route synthesis is
[`explorations/2026-08-24-kls-moment-map-cmh-consolidation.md`](explorations/2026-08-24-kls-moment-map-cmh-consolidation.md).
For A1--A5, the current certified-probe summary records 21 independently reviewed positive
intermediate nodes and the remaining live frontiers:
[`explorations/2026-08-21-a-series-proof-probes.md`](explorations/2026-08-21-a-series-proof-probes.md).

The proof output plane is a **repo-root sibling**, `../solutions/`: standalone,
reviewable `.tex` proofs that a `proved` ledger node points to (via a `solution:` field).
Certification may be an independent agent audit with persisted provenance, human acceptance, or
Lean; see `../solutions/README.md`. Numerical artifacts are not part of this certification.
Every `proved` node uses this plane, including the former inline baselines. The checker requires a
certified dossier and rejects narrative provenance or historical status as alternatives to R2.

**Why two ledgers, not one.** The A-series combines refinement with active proof certification;
KLS is organized as a route-based proof program (crisp statements; discharge assumptions;
numerics only guide research and stress possible failure modes). They use the same status/edge grammar and one
checker, but KLS keeps the heavier machine-enforced no-go set it needs. The **bridge** is
`conj:a1-bis` (structured-posterior `C_P ≤ K·λmax(Cov)`) → the route-neutral
`kls/conj:kls`: the same bound for *every* isotropic log-concave measure **is** KLS (Part I's
"Tier-∞" boundary).
See `kls/README.md`.

## Status & diagnostic vocabulary

- **A-series status**: `open` (unresolved), `proved`, `imported`, or `refuted`. Refinement may
  sharpen an `open` node without changing its status; `kind: conjecture` records that the
  statement itself is conjectural.
- **KLS status**: `proved`, `conditional`, `open`, `heuristic`, `refuted`, or `imported`.
- **numerical diagnostic** (orthogonal to logical status): `none` or
  `numerical-directional`, with `evidence_run:` pointing at the provenance-stamped `finum`
  artifact. Directional means research guidance only; it cannot promote or certify a node.

## How `finum` plugs in

The numerical package (`finum`, implemented under `experiments/`) produces provenance-stamped
JSONL research artifacts. A ledger node may reference one through `evidence_run` with
`evidence: numerical-directional` so future researchers can reproduce the diagnostic. The signal
is only *"this computation suggests direction X under its recorded assumptions and error
limitations."* Passing a battery changes neither logical status nor proof certification.

## Rules that keep research diagnostics separate from proof

1. A `proved` node may not inherit an unresolved dependency or `assuming` edge. For KLS this
   explicitly includes `conditional`, `heuristic`, and imported nodes marked
   `import_class: preprint-unreviewed`; conditional nodes must declare and recursively propagate
   a non-empty `assuming` contract. Imported nodes default to `import_class: published`.
2. Referenced numerical diagnostics require an existing, valid provenance-stamped JSONL and an
   explicit matching `evidence_target`. Reproducibility rests on the recorded seed, params, and
   library versions; the state of the worktree is not gated. Retired diagnostics belong in the
   dated exploration record. No numerical diagnostic validates a theorem or supplies a step in a
   proof dossier.
3. Every `kind: conjecture` node lists the obstructions it must respect (`bounded_by`); for KLS
   the checker enforces exact reverse parity with `obstructions.yaml.constrains` and requires
   clearance for both forbidden and methodological-warning mechanisms.
4. A program has exactly one ledger until explicit merge semantics are implemented; duplicate
   program ledgers and duplicate node ids fail rather than overwrite.

## Definition of done for a contribution

The four-step contract and the commands that check it are in [`../CLAUDE.md`](../CLAUDE.md).
