# Shared ledger schema

This is the single field-level schema reference for
[`a-series/ledger.yaml`](a-series/ledger.yaml) and [`kls/ledger.yaml`](kls/ledger.yaml).
Contribution rules remain normative in [`../CLAUDE.md`](../CLAUDE.md), and
[`check_ledger.py`](check_ledger.py) is the executable structural validator. Unknown fields and
unknown enum values are rejected.

## Document shape

Each ledger has exactly two top-level keys:

```yaml
meta:
  program: ab | kls
nodes:
  - id: ...
```

`nodes` is a list with unique `id` values. A program has exactly one production ledger.

### Metadata

| field | program | requirement | meaning |
|---|---|---|---|
| `program` | both | required | Stable machine id: `ab` for A-series or `kls` for KLS. Program identity exists only here, never as a node `kind`. |
| `scope` | A-series | required in production | Human-readable boundary of the A-series graph. |
| `route_policy.allowed` | KLS | required in production | Closed list of route names accepted by each node's `route`. |

## Required node fields

| field | requirement | meaning |
|---|---|---|
| `id` | required non-empty string | Stable node id, normally the exact LaTeX label of the statement. |
| `kind` | required enum | Mathematical form; see [Kinds](#kinds). |
| `status` | required enum | Logical standing in the repository; see [Statuses](#statuses). |
| `file` | required existing repo-relative path | Manuscript file containing the effective LaTeX label. |
| `statement` | required non-empty string | Concise statement matching the manuscript anchor semantically. |

The effective manuscript label is `label` when that exceptional field is present and `id`
otherwise. It must occur in `file`. A stable legacy or synthetic id may use `label`; new nodes
normally make `id` and the LaTeX label identical.

## Kinds

Both programs use exactly the same kinds:

| `kind` | use |
|---|---|
| `theorem` | Principal truth-valued mathematical statement. |
| `proposition` | Standalone mathematical statement of intermediate or local scope. |
| `lemma` | Supporting result used primarily to prove another result. |
| `corollary` | Direct consequence of earlier results. |
| `conjecture` | Precise truth-valued statement proposed but not established. |
| `assumption` | Explicit premise consumed by a conditional implication; this also covers material formerly called a hypothesis. |
| `question` | Research target posed as a question rather than an asserted conclusion. |
| `definition` | Introduction of a mathematical object; it uses `status: defined`. |
| `obstruction` | Statement constraining an admissible target or proof shape and available to `bounded_by`. |
| `example` | Concrete construction, calibration, or counterexample statement. |

`program` is metadata only. Expository remarks and speculative discussion remain in manuscript or
exploration prose; a ledger-backed observation uses its precise mathematical kind.

## Statuses

Both programs use exactly the same statuses:

| `status` | meaning | required provenance |
|---|---|---|
| `open` | Unresolved. | No proof-certification metadata. |
| `conditional` | The dependency closure contains a blocking premise (`open`, `conditional`, or `refuted`) or an unreviewed preprint. The implication itself may be certified. | If any proof-certification field is present, both `solution` and `checked_by` are required. |
| `proved` | Unconditional in the repository dependency graph. | Certified `solution` and `checked_by`; no inherited blocking premise or unreviewed preprint. |
| `imported` | Taken from named literature rather than proved in the repository. | `import_class` and non-empty `references`. |
| `defined` | Non-proof state of a definition. | Valid if and only if `kind: definition`; no proof-certification metadata. |
| `refuted` | Independently certified false as stated. | Non-empty `refuted_by` naming proved/imported refuters that also occur in `depends_on`. |

Status and kind are orthogonal except for the reciprocal `definition`/`defined` rule. Numerical
output never supplies proof or refutation provenance.

## Identity and navigation fields

| field | program | meaning |
|---|---|---|
| `label` | both | Exceptional manuscript anchor when the stable `id` is not the LaTeX label. |
| `refines` | A-series | One LaTeX label genuinely sharpened by this node; not a location field. |
| `route` | KLS | Route owning the node; required when `meta.route_policy` is declared and constrained by its `allowed` list. |

## Logical graph fields

All list-valued graph fields must be YAML lists.

| field | meaning |
|---|---|
| `depends_on` | Same-ledger claim nodes actually used by the proof. This is the sole stored dependency direction and must be acyclic. |
| `bounded_by` | Declared obstruction ids constraining the statement or proof. Applicability and semantic clearance remain critic responsibilities. |
| `bridges` | Explicit cross-program comparison links written as `program/id`; never proof dependencies. |
| `refuted_by` | Proved/imported refuters for a refuted node; each must also occur in `depends_on`. |

Conditional premises and downstream consumers are derived from the transitive `depends_on` graph.
Non-logical roadmap relationships stay in program prose; do not add parallel `related`, `unlocks`,
`assuming`, or `discharged_by` graphs.

## Imported-result provenance

| field | requirement |
|---|---|
| `import_class` | Required only for `status: imported`; `published` or `preprint-unreviewed`. |
| `references` | Required non-empty list of BibTeX keys in `fi_references.bib`, only for imported nodes. |

An unreviewed preprint is an unresolved dependency risk: downstream implications may be
`conditional` but not `proved`. If the repository supplies and certifies its own proof, classify
the node as `proved` rather than `imported`.

## Proof-certification fields

Proof-certification fields are valid only on `proved` or `conditional` nodes.

| field | requirement |
|---|---|
| `solution` | Existing repo-relative `.tex` dossier under `solutions/`; required for `proved`. |
| `checked_by` | `agent`, `human`, or `lean`; required with a certified solution. |
| `review` | Required only for `checked_by: agent`; points to a persisted report under `research/reviews/`. |
| `accepted_by` | Required non-empty human identity only for `checked_by: human`. |

`checked_by: lean` requires an adjacent `.lean` file. `checked_by: none` is valid only inside an
unwired draft dossier header, never in a ledger. A certified conditional implication remains
`conditional` until every blocking premise is discharged.

## Deliberately excluded material

Claim nodes do not store workflow history, narrative notes, numerical specifications, or numerical
evidence. In particular, retired fields such as `note`, `numerics`, `evidence*`, `mechanism`,
`clearance`, `related`, and `unlocks` are rejected. Use:

- manuscript and route/target prose for active exposition and navigation;
- `research/a-series/targets/README.md` for the A1--A5 brief index;
- `research/explorations/` for dated mathematical attempts;
- `research/runs/` for immutable numerical artifacts;
- `experiments/` for numerical implementations; and
- `research/reviews/` plus `solutions/` for proof certification.

## What the checker does not establish

The checker verifies schema, paths, labels, provenance shape, obstruction resolution, bridge
resolution, acyclicity, and dependency-status consistency. It does not establish that the ledger
`statement`, manuscript theorem, dossier, and applicable obstructions agree mathematically. That
semantic audit belongs to an independent critic.

## Verify

```bash
python3 research/check_ledger.py
python3 research/check_ledger.py status
python3 research/check_ledger.py node q:upgrade
python3 -m unittest discover -s research/tests -p 'test_*.py'
```
