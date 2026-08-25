# Independent reviews

This directory holds persisted review provenance. Reports have one of two explicit types:

| `type` | purpose | may certify `checked_by: agent`? |
|---|---|---|
| `proof-review` | Independent review of one or more standalone proof dossiers | yes |
| `audit` | Historical, diagnostic, editorial, literature, or control-plane review | no |

The distinction is structural. A sentence such as “pass” inside an `audit` has no proof value.

## Proof-review front matter

Every certifying report starts with YAML front matter:

```yaml
---
type: proof-review
date: "YYYY-MM-DD"
verdict: pass
authors:
  - /root/proof_author
reviewer: /root/independent_reviewer
nodes:
  - thm:example
solutions:
  - solutions/thm-example.tex
---
```

`date` is quoted and matches the filename prefix. `verdict` is exactly `pass`; partial, held, or
failed work is an `audit` until a new follow-up proof review passes. `authors`, `nodes`, and
`solutions` are non-empty lists without duplicates. One report has one reviewer, but it may cover
multiple authors, nodes, and dossiers.

The front matter declares exact scope, not search terms. Across all ledger nodes pointing to the
report:

- `nodes` exactly matches their ids;
- `authors` exactly matches their distinct `authored_by` values;
- `reviewer` exactly matches their common `reviewed_by` value;
- `solutions` exactly matches their distinct `solution` paths.

The checker rejects missing and extra entries, proof reviews not wired into a ledger, reports
outside this directory, and attempts to use an `audit` as proof provenance.

A repaired proof may add the optional repo-relative pointer:

```yaml
follows_up: research/reviews/YYYY-MM-DD-earlier-audit.md
```

Never rewrite an earlier verdict after a repair. Preserve it and write a new report.

## Audit front matter

A non-certifying report uses only:

```yaml
---
type: audit
date: "YYYY-MM-DD"
---
```

Its outcome, participants, and scope remain ordinary prose because they have no mechanical R2
effect.

## Report body

The mathematical body is intentionally free-form. Prefer the smallest useful structure:

1. **Findings** — the independent mathematical checks and reasoning.
2. **Corrections** — changes required and rechecked, or “None.”
3. **Exclusions** — nearby claims not certified.

Do not repeat the machine-readable node list in a verdict sentence merely for validation. Review
reports are proof provenance, never numerical evidence; computation may expose a defect but cannot
certify an analytic step.

Validate the archive and its exact ledger parity with:

```bash
python3 research/check_ledger.py
```
