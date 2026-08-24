# CLAUDE.md — the rules an agent works under in this repo

This file is served under two names — `CLAUDE.md` and `AGENTS.md` are the same file, so
Claude Code and Codex read identical instructions. Other documents link to it as `CLAUDE.md`.

This is the single normative source for how work enters this repository. The other documents
are maps, not rules: [`research/README.md`](research/README.md) describes the control plane,
[`solutions/README.md`](solutions/README.md) the proof plane,
[`experiments/README.md`](experiments/README.md) the numerical channel, and
[`orchestration.md`](orchestration.md) how to parallelize across them. When any of them appears
to contradict this file, this file wins.

The subject is functional inequalities — the Poincaré, log-Sobolev, and transportation-cost
constants of `P ∝ e^{-U}` — across a manuscript (Parts I–III), an open-target program (A1–A5),
and an exploratory KLS proof program.

## The planes

| plane | where | what it holds |
|---|---|---|
| claims | `research/ledger.yaml`, `research/kls/routes/eldan-localization/ledger.yaml` | the machine-readable graph: status, edges, provenance pointers |
| prose | `modules/**/*.tex` | the manuscript; the `\label`s that node ids bind to |
| proofs | `solutions/*.tex` | standalone dossiers a reviewer or Lean can check |
| evidence | `research/runs/*.jsonl` | provenance-stamped `finum` artifacts |
| memory | `research/explorations/`, `research/knowledge/`, `research/reviews/` | dated attempt log, shared battery and obstructions, audit reports |

## The soundness contract

Three signals, ranked by evidentiary strength. They need not occur in a fixed sequence: an
analytic proof may bypass numerics entirely.

| signal | mechanism | what it is worth |
|---|---|---|
| **R0 — structural** | `python3 research/check_ledger.py` returns 0 errors | cheap and deterministic; **necessary, never sufficient** |
| **R1 — numerical** | a provenance-stamped `finum` artifact in `research/runs/` | rigorous refutation, or *direction*; **never** proof |
| **R2 — proof** | `solutions/<id>.tex` with `checked_by ∈ {agent, human, lean}` | the only route to `status: proved` |

**The invariant: R1 may never masquerade as R2.** An agent that "passes numerics" has produced
evidence *for* a prover, not a proof. Mechanically: `finum` never edits a ledger; uppercase
`REFUTED` is reserved for a rigorous analytic or exact lower bound (`finum/verdict.py:falsify`),
while every sampled, MCMC, FEM, or finite-grid quantity goes through `compare_directional` and
can only be *directional*. This is why **criticism is a first-class role, not QA**: never let a
prover grade its own proof.

## Definition of done

For any contribution:

1. the target is sharpened (or confirmed), or a standalone proof dossier is supplied;
2. the ledger node is updated with matching status, provenance, and edges;
3. `python3 research/check_ledger.py` returns 0 errors;
4. the attempt — **including dead ends** — is logged in
   `research/explorations/YYYY-MM-DD-slug.md`; cross-cutting findings are promoted to
   `research/knowledge/`.

A *proof* contribution has four further requirements, specified in
[`solutions/README.md`](solutions/README.md): the dossier compiles standalone with a complete
audit header, its theorem matches the `\label` it `refines` and respects every `bounded_by`
obstruction, the node carries `solution:` + `checked_by:`, and agent certification names a
distinct author and reviewer plus a persisted report under `research/reviews/`.

## Commands

```bash
python3 research/check_ledger.py                                   # R0 — after every ledger edit
python3 -m unittest discover -s research/tests -p 'test_*.py'      # checker regressions
cd experiments && uv run python -m finum selftest                  # calibration anchors
cd experiments && uv run python -m finum run --target A3           # → research/runs/<ts>-A3.jsonl
cd experiments && uv run pytest                                    # finum oracle suite
latexmk -pdf -outdir=build main.tex                                # the whole document
cd solutions && latexmk -pdf -outdir=../build <id>.tex             # one dossier, standalone
```

## Hard constraints

Specific to this repo; a naive agent swarm hits every one of these.

1. **A ledger is a single-file write-contention point.** Git-worktree isolation helps parallel
   `finum`/`solutions` work but does nothing for a shared YAML. Funnel *all* ledger edits
   through one orchestrator; squads write only to `research/targets/*.md`,
   `research/explorations/`, `research/runs/`, and (provers) `solutions/`.
2. **No private Monte Carlo.** The retraction that created `research/explorations/` is the
   cautionary tale: two agents ran ad-hoc scripts, disagreed, and a non-reproducible claim had
   to be withdrawn. Every numerical claim flows through `finum` with a provenance-stamped
   artifact, or it does not count.
3. **The battery is fixed and shared.** An agent must not mint its own happy-path instances to
   clear `numerical-strong` — that is reward-hacking the soundness gate. New instances are
   curated into `research/knowledge/instances.md` by the librarian, not minted by the refiner.
4. **`check_ledger.py` is necessary, not sufficient.** It verifies structure — labels resolve,
   the DAG is acyclic, no proved node rests on an unproved one, obstruction parity holds. It
   does **not** verify that the `.tex` prose, the ledger `statement:`, and the solution dossier
   agree semantically, nor that any proof is correct. That is a critic's responsibility, and it
   is where a green exit code stops meaning anything.
5. **Respect `bounded_by`.** A refined statement that violates a known obstruction is wrong by
   construction — e.g. any A1 bound without a tail term violates `obs:flat-direction`. Check
   this *before* spending a numerical run.
6. **Don't fan out across the trace-upgrade unification.** `q:upgrade`, the high-rank part of
   `q:stein-weighted`, and `q:alignment` are the same operator-to-trace problem in three
   coordinate systems (`rem:trace-upgrade-unification`). One team owns it, then propagates.
7. **`conditional` KLS nodes are Lean-certifiable only as conditional implications.** The
   assumption becomes a hypothesis; the node reaches unconditional `proved` only when the
   assumption is discharged.
8. **`research/explorations/` is append-only.** It exists so the next agent does not re-run a
   refuted approach. Add dated files; do not rewrite history.

## Conventions

- A node `id` **is** the LaTeX `\label` of its statement. When a statement changes, update both
  the `.tex` and the ledger.
- `depends_on` means "used in the proof" and must stay acyclic. `unlocks` is a forward pointer
  only — the checker rejects an `unlocks` edge that duplicates the target's
  `depends_on`/`assuming`/`discharged_by`.
- Reproducibility of a `finum` artifact rests on its recorded seed, params, and library
  versions. Nothing gates on the state of the worktree.
- Math in Markdown files is written in LaTeX `$…$`.
