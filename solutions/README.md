# solutions/ — the proof output plane

Where agents write **proofs** of the open targets: self-contained, standalone-compilable,
human-checkable `.tex` files — **separate from the manuscript** (`../modules/`). This is the
analytic-proof channel paired with the refinement and stress-testing work in `research/`.

A solution file is the artifact a newly `proved` ledger node points to (via its `solution:` field),
exactly as `evidence_run:` is the artifact a `numerical-strong` node points to. The ledger
records the *claim and its state*; this directory holds the *proof an independent reviewer or
Lean can check*. A small set of elementary inline results predating this plane is explicitly
marked with `proof_provenance:` in the ledger; that legacy exception is not available to new
promotions.

## Why separate from the manuscript

- **Human review boundary.** A reviewer reads one self-contained file and its one-file PDF, not
  a diff against the whole book.
- **Clear provenance.** Agent-authored, dated, revertible; lifting a checked solution into the
  manuscript remains an explicit project-owner decision.
- **Liftable.** Each file is a `subfiles` document, so once accepted it drops into `main.tex`
  with a single `\subfile{solutions/<id>}` line — no rewrite.

## The `checked_by` ladder

A proof is only as trustworthy as its check. Every solution declares its level in the header:

| `checked_by` | meaning | may a ledger node be `proved`? |
|---|---|---|
| `none`  | drafted, unreviewed | **no** — not a proof yet |
| `agent` | a distinct agent audited the complete natural-language proof and left a persisted report | yes (agent-certified) |
| `human` | a human read and accepts the natural-language argument | yes (human-certified) |
| `lean`  | a compiling Lean proof sits beside it (`<id>.lean`) | yes (machine-certified) |

Agent certification is deliberately explicit rather than being recorded as human review. It
requires `authored_by`, a distinct `reviewed_by`, and a repo-local `review:` report. The report
must state its exact scope and any exclusions. This gate was enabled by the project owner on
2026-08-21 for independently audited results.

Numerics never appear on this ladder: they refine and refute statements, they never prove
(the R1/R2 contract in [`../CLAUDE.md`](../CLAUDE.md)).

## Writing a solution

1. Copy `TEMPLATE.tex` to `solutions/<ledger-id>.tex` (replace `:` with `-`). Closely coupled
   nodes may share one target-level dossier if its header and theorem labels enumerate every
   covered ledger id explicitly.
2. Fill the audit header (ledger node, `refines` label, `bounded_by`, `evidence_run`,
   `checked_by`, separate author/reviewer identities, review path, and date).
3. State the **refined** theorem and prove it. Use `\ref`/
   `\cite` freely — they resolve when lifted into `main.tex` and show `??` standalone (expected).
4. Compile standalone:
   ```bash
   cd solutions
   latexmk -pdf -outdir=../build <id>.tex
   ```
5. Wire the ledger node (`research/ledger.yaml` or a route ledger): add
   `solution: solutions/<id>.tex` and `checked_by: agent|human|lean`. For an agent audit, also
   add `authored_by`, a distinct `reviewed_by`, and `review`. The node may flip to
   `status: proved` only once these artifacts exist — enforced by `research/check_ledger.py`.

## Definition of done (a proof contribution)

1. `solutions/<id>.tex` exists, compiles standalone, audit header complete.
2. The theorem matches the refined statement in the manuscript `\label` it `refines`, and
   respects every `bounded_by` obstruction.
3. The ledger node has `solution:` + `checked_by` set; `python3 research/check_ledger.py`
   returns 0 errors.
4. `checked_by: agent` (independent named agent plus persisted report), `checked_by: human`
   (a named human accepted it), or `checked_by: lean` (with `<id>.lean`).
