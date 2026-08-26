# Target briefs

This directory is the mutable staging area for the five A-series research streams. Each file is
a short handoff brief for an analyst or refiner, not a source of mathematical truth and not an
attempt log.

## Ownership

| information | canonical location |
|---|---|
| claim, status, dependencies, obstructions, certification/refutation pointers | `../ledger.yaml` |
| exact accepted statement and exposition | `../../../modules/open-targets/` |
| proposed refinement awaiting promotion | this directory |
| dated attempts, including dead ends | `../../explorations/` |
| A-series obstruction prose | `../obstructions.md` |
| reusable lemmas and shared stress instances | `../../knowledge/` |
| numerical implementation and artifacts | `../../../experiments/finum/`, `../../runs/` |
| proof and independent certification | `../../../solutions/`, `../../reviews/` |

The ledger and manuscript win if a brief drifts. Do not copy proof histories, numerical logs, or
manual status summaries into these files.

## Workflow

1. The orchestrator assigns a ledger node and remains the only ledger writer.
2. A refiner reads the ledger node, manuscript statement, target brief, and every listed
   `bounded_by` obstruction.
3. The refiner records the attempt in a dated exploration and stages only the proposed statement
   delta or numerical specification under **Candidate refinement**.
4. The orchestrator promotes an accepted change to the manuscript and ledger, runs the checker,
   and clears or replaces the staged candidate.

One file covers one A-series stream. Do not create per-node files or nested target directories;
the ledger already supplies node-level organization.

| stream | headline node | brief |
|---|---|---|
| A1 | `conj:a1` | [`A1-data-informed-glm.md`](A1-data-informed-glm.md) |
| A2 | `conj:a2` | [`A2-bernstein-von-mises.md`](A2-bernstein-von-mises.md) |
| A3 | `conj:a3-dependent` | [`A3-heavy-tailed-posteriors.md`](A3-heavy-tailed-posteriors.md) |
| A4 | `q:a4-certificate` | [`A4-variational-inference.md`](A4-variational-inference.md) |
| A5 | `conj:a5-metastable` | [`A5-quotient-and-reparameterization.md`](A5-quotient-and-reparameterization.md) |

## Brief outline

```markdown
# A<n> — <title>

> Mutable refinement brief. The ledger and manuscript are authoritative;
> dated history belongs in `research/explorations/`.

## Entry points

- Headline node: `<node-id>`
- Manuscript: `<path>` (`<label>`)
- Numerical target: `<finum-id>`, if applicable
- Baseline: `<node-id>`, if applicable

## Target-specific guardrails

- `<obstruction-id>` — <concrete consequence for this target>.

## Active handoff

| node | requested deliverable |
|---|---|
| `<node-id>` | <one concrete outcome> |

## Candidate refinement

<Exact proposed statement or concise delta, or “None currently.”>

## Context

- [Latest relevant exploration](...)
- [Relevant solution or review](...)
```

Keep a brief compact enough to scan in one sitting. Read dependencies from the ledger rather
than copying its graph here. Markdown structure and navigation are intentionally not
machine-validated.
