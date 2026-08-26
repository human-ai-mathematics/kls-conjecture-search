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
| claims | `research/a-series/ledger.yaml`, `research/kls/ledger.yaml` | the machine-readable graph: status, edges, provenance pointers |
| prose | `modules/**/*.tex` | the manuscript; the `\label`s that node ids bind to |
| proofs | `solutions/*.tex` | standalone dossiers a reviewer or Lean can check |
| diagnostics | `research/runs/*.jsonl` | provenance-stamped `finum` research artifacts |
| memory | `research/explorations/`, `research/knowledge/`, program obstruction files, `research/reviews/`, `research/decisions/` | attempts, shared battery, no-go prose, audits, harness decisions |

## The soundness contract

Three signals with different roles. They are not a ladder whose lower rungs accumulate into a
proof: an analytic proof is certified independently of numerics.

| signal | mechanism | what it is worth |
|---|---|---|
| **R0 — structural** | `python3 research/check_ledger.py` returns 0 errors | cheap and deterministic; **necessary, never sufficient** |
| **R1 — numerical** | a provenance-stamped `finum` artifact in `research/runs/` | research direction, stress testing, or a candidate refutation; **never** claim or proof validation |
| **R2 — proof** | `solutions/<id>.tex` with `checked_by ∈ {agent, human, lean}` | certifies a proved claim or conditional implication; refutations point to a certified refuter |

**The invariant: R1 never validates R2.** A proof dossier and its review must stand without any
numerical run. `finum` may guide intuition, expose a likely counterexample, or help sharpen a
statement; sampled, MCMC, FEM, and finite-grid quantities remain directional. If exact arithmetic
or an analytic lower bound yields a checkable certificate (`finum/verdict.py:falsify`), that
certificate must be persisted and independently checked in the proof/refutation plane before a
logical status changes. This is why **criticism is a first-class role, not QA**: never let a prover
grade its own proof.

## Definition of done

For any mathematical or proof contribution:

1. the target is sharpened (or confirmed), or a standalone proof dossier is supplied;
2. the ledger node is updated with matching status, certification/refutation provenance, and edges;
3. `python3 research/check_ledger.py` returns 0 errors;
4. the attempt — **including dead ends** — is logged in
   `research/explorations/YYYY-MM-DD-slug.md`; cross-cutting findings are promoted to
   `research/knowledge/`.

A harness, schema, or repository-organization contribution instead records its rationale and
validation in `research/decisions/YYYY-MM-DD-slug.md`; it does not create a fictitious
mathematical attempt or require a claim-status change.

A *proof* contribution has four further requirements, specified in
[`solutions/README.md`](solutions/README.md): the dossier compiles standalone with a complete
audit header, its theorem matches the `\label` it `refines` and respects every `bounded_by`
obstruction, the node carries `solution:` + `checked_by:`, and agent certification points to a
persisted report under `research/reviews/` naming distinct author(s) and reviewer.

## Commands

```bash
python3 research/check_ledger.py                                   # R0 — after every ledger edit
python3 research/check_ledger.py status                            # derived unresolved frontier
python3 research/check_ledger.py node q:upgrade                    # one node + derived consumers
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
   through one orchestrator; squads write only to `research/a-series/targets/*.md`,
   `research/explorations/`, `research/runs/`, and (provers) `solutions/`.
2. **No private Monte Carlo.** The retraction that created `research/explorations/` is the
   cautionary tale: two agents ran ad-hoc scripts, disagreed, and a non-reproducible claim had
   to be withdrawn. Every numerical observation cited as research guidance flows through `finum`
   with a provenance-stamped artifact; none counts toward proof certification.
3. **The research battery is shared.** Use the curated instances in
   `research/knowledge/instances.md` so stress tests remain comparable and do not collapse to a
   refiner's happy path. A refiner may propose a new adversarial instance, but the librarian must
   review it before adding it to the shared registry. Passing any finite battery changes no claim
   or proof status.
4. **`check_ledger.py` is necessary, not sufficient.** It verifies structure — labels resolve,
   the DAG is acyclic, no proved node rests on an unproved one, obstruction ids resolve. It
   does **not** verify that the `.tex` prose, the ledger `statement:`, and the solution dossier
   agree semantically, nor that any proof is correct. That is a critic's responsibility, and it
   is where a green exit code stops meaning anything.
5. **Respect `bounded_by`.** A refined statement that violates a known obstruction is wrong by
   construction — e.g. any A1 bound without a tail term violates `obs:flat-direction`. Check
   this *before* spending a numerical run.
6. **Don't fan out across the trace-upgrade cluster.** `q:upgrade`, the high-rank part of
   `q:stein-weighted`, and `q:alignment` are three manifestations of the same high-rank
   occupation difficulty (`rem:trace-upgrade-unification`); their formal equivalence is not
   proved. One team owns the comparison, then propagates only what has actually been shown.
7. **`conditional` KLS nodes are Lean-certifiable only as conditional implications.** The
   assumption becomes a hypothesis; the node reaches unconditional `proved` only when the
   assumption is discharged.
8. **`research/explorations/` and `research/decisions/` are append-only.** Explorations prevent
   refuted mathematical approaches from being rerun; decisions preserve harness rationale. Add
   dated files; do not rewrite history.

## Conventions

- A new node `id` **is** the LaTeX `\label` of its statement. A stable legacy/synthetic id whose
  certified provenance cannot be renamed declares an explicit `label:` manuscript anchor; the
  checker requires that effective label to occur in the node's declared `file`. When a statement
  changes, update both the `.tex` and the ledger.
- `depends_on` means "repository claim nodes used in the proof" and must stay intra-program and
  acyclic. Manuscript equations and ordinary literature citations stay in the dossier/manuscript.
  Downstream consumers are derived by reversing `depends_on`; speculative roadmap relationships
  belong in prose, not a second graph.
- Reproducibility of a `finum` artifact rests on its recorded seed, params, and library
  versions. Nothing gates on the state of the worktree.
- Math in Markdown files is written in LaTeX `$…$`.
