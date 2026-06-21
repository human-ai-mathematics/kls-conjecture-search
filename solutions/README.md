# solutions/ — the Phase-2 output plane

Where agents write **proofs** of the open targets: self-contained, standalone-compilable,
human-checkable `.tex` files — **separate from the manuscript** (`../modules/`). This is the
deliverable of Phase 2 (prove), as `research/` is the workspace of Phase 1 (refine).

A solution file is the artifact a `proved` ledger node points to (via its `solution:` field),
exactly as `evidence_run:` is the artifact a `numerical-strong` node points to. The ledger
records the *claim and its state*; this directory holds the *proof a human (or Lean) can open
and check*.

## Why separate from the manuscript

- **Human review boundary.** A reviewer reads one self-contained file and its one-file PDF, not
  a diff against the whole book.
- **Clear provenance.** Agent-authored, dated, revertible; the manuscript stays human-curated
  until a human chooses to lift a checked solution in.
- **Liftable.** Each file is a `subfiles` document, so once accepted it drops into `main.tex`
  with a single `\subfile{solutions/<id>}` line — no rewrite.

## The `checked_by` ladder

A proof is only as trustworthy as its check. Every solution declares its level in the header:

| `checked_by` | meaning | may a ledger node be `proved`? |
|---|---|---|
| `none`  | drafted, unreviewed | **no** — not a proof yet |
| `human` | a human read and accepts the natural-language argument | yes (NL-certified) |
| `lean`  | a compiling Lean proof sits beside it (`<id>.lean`) | yes (machine-certified) |

Numerics never appear on this ladder: they refine and refute statements, they never prove.
(See `../research/README.md` soundness contract.)

## Writing a solution

1. Copy `TEMPLATE.tex` to `solutions/<ledger-id>.tex` (e.g. `conj-a1.tex`; replace `:` with
   `-` since `:` is awkward in filenames).
2. Fill the audit header (ledger node, `refines` label, `bounded_by`, `evidence_run`,
   `checked_by`, author/date).
3. State the **refined** theorem (the sharp form Phase 1 produced) and prove it. Use `\ref`/
   `\cite` freely — they resolve when lifted into `main.tex` and show `??` standalone (expected).
4. Compile standalone:
   ```bash
   latexmk -pdf -outdir=build solutions/<id>.tex
   ```
5. Wire the ledger node (`research/ledger.yaml` or a route ledger): add
   `solution: solutions/<id>.tex` and `checked_by: human|lean`. The node may flip to
   `status: proved` only once the file exists and `checked_by ∈ {human, lean}` — enforced by
   `research/check_ledger.py`.

## Definition of done (a Phase-2 contribution)

1. `solutions/<id>.tex` exists, compiles standalone, audit header complete.
2. The theorem matches the refined statement in the manuscript `\label` it `refines`, and
   respects every `bounded_by` obstruction.
3. The ledger node has `solution:` + `checked_by` set; `python3 research/check_ledger.py`
   returns 0 errors.
4. `checked_by: human` (a named human accepted it) or `checked_by: lean` (with `<id>.lean`).
