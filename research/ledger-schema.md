# Ledger schema

This is the field-level schema for [`kls/ledger.yaml`](kls/ledger.yaml).
[`check_ledger.py`](check_ledger.py) is the executable
validator; [`../CLAUDE.md`](../CLAUDE.md) owns the contribution rules.

## Document shape

Each production ledger has exactly two top-level keys:

```yaml
meta:
  program: kls
nodes:
  - id: ...
```

`nodes` is a list with unique `id` values. A program has one production ledger.

### Metadata

| field | program | requirement |
|---|---|---|
| `program` | required | Program id: `kls`. |
| `route_policy.allowed` | required | Closed route vocabulary used by every node's `route`. |

## Node fields

Every node requires:

| field | meaning |
|---|---|
| `id` | Stable node id, normally the exact LaTeX label. |
| `kind` | Mathematical form. |
| `status` | Logical standing in the repository. |
| `file` | Existing repository-relative manuscript file containing the effective label. |
| `statement` | Concise current statement matching the manuscript anchor. |

`label` supplies the manuscript anchor when it differs from a stable `id`; otherwise the anchor
is `id`.

### Kinds

| value | use |
|---|---|
| `theorem` | Principal truth-valued statement. |
| `proposition` | Standalone intermediate or local statement. |
| `lemma` | Supporting result. |
| `corollary` | Direct consequence. |
| `conjecture` | Precise asserted target not yet established. |
| `assumption` | Explicit premise of a conditional implication. |
| `question` | Research target posed as a question. |
| `definition` | Introduction of a mathematical object. |
| `obstruction` | Fence available to `bounded_by`. |
| `example` | Concrete construction, calibration, or counterexample statement. |

### Statuses

| value | meaning | provenance |
|---|---|---|
| `open` | Unresolved. | No proof certification. |
| `conditional` | A blocking premise or unreviewed preprint occurs in the dependency closure. | Optional certified implication; if present, both `solution` and `checked_by`. |
| `proved` | Unconditional in the repository dependency graph. | `solution` and `checked_by`; no blocking premise. |
| `imported` | Taken from named literature. | `import_class` and non-empty `references`. |
| `defined` | Non-proof state of a definition. | Valid exactly for `kind: definition`. |
| `refuted` | Independently certified false as stated. | `refuted_by` naming proved/imported refuters also present in `depends_on`. |

Numerical output never supplies proof or refutation provenance.

## Navigation and graph fields

All graph-valued fields are YAML lists.

| field | program | meaning |
|---|---|---|
| `route` | required | Owning route from `meta.route_policy.allowed`. |
| `depends_on` | both | Same-ledger claims actually used in the proof; acyclic. |
| `bounded_by` | both | Same-ledger nodes with `kind: obstruction` that constrain the claim or proof. |
| `bridges` | optional | Comparison links inside this repository, written as `program/id`; never proof dependencies. The comparison with `conj:a1-bis` in `posterior-inequalities-exploration` is prose only (`CLAUDE.md` constraint 9). |
| `refuted_by` | both | Proved/imported refuters, each also listed in `depends_on`. |

Conditional premises and downstream consumers are derived from `depends_on`. Roadmap
relationships belong in route or target prose.

## Imported results

`status: imported` requires:

- `import_class: published | preprint-unreviewed`;
- a non-empty `references` list of keys from `fi_references.bib`.

An unreviewed preprint blocks unconditional downstream proof status. A repository-certified proof
uses `status: proved` instead.

## Proof certification

Certification fields are valid only on `proved` or `conditional` nodes.

| field | requirement |
|---|---|
| `solution` | Existing `.tex` dossier under `solutions/`; required for `proved`. |
| `checked_by` | `agent`, `human`, or `lean`; required with `solution`. |
| `review` | Required for `checked_by: agent`; persisted under `research/reviews/`. |
| `accepted_by` | Required human identity for `checked_by: human`. |

`checked_by: lean` requires an adjacent `.lean` file. A certified conditional implication remains
`conditional` until its blocking premises are discharged.

## Content boundary

Ledger nodes contain current mathematical state, not workflow notes, attempt history, numerical
specifications, or roadmap edges. Put those in the manuscript, route/target briefs,
`research/explorations/`, `experiments/`, or `research/runs/` as appropriate. Proof certification
lives in `solutions/` and `research/reviews/`.

## Checker boundary

The checker validates schema, paths, labels, provenance shape, obstruction and bridge resolution,
acyclicity, and dependency-status consistency. Independent review must compare the ledger
statement, manuscript statement, dossier, and applicable obstructions mathematically.

## Verify

```bash
python3 research/check_ledger.py
python3 research/check_ledger.py status
python3 research/check_ledger.py node q:upgrade
python3 -m unittest discover -s research/tests -p 'test_*.py'
```
