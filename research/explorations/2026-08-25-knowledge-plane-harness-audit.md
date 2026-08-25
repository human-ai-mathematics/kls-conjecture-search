# Knowledge-plane harness audit

- **Date:** 2026-08-25
- **Scope:** `research/knowledge/` as the shared research-memory and instance-registry plane
- **Outcome:** preserve the curated mathematical content while tightening the R1/R2 language

## Findings

The three knowledge files have a useful separation of concerns: `lemmas.md` records reusable
analytic tools, `obstructions.md` explains the cross-target no-go statements represented in the
ledger, and `instances.md` fixes common calibration and stress cases. Their internal claim ids all
resolve to either a ledger node or a manuscript label.

Two phrases overstated the numerical contract. First, the instance-registry introduction said
that `finum` owns every registered instance, although several rows are specifications for future
backends. Second, the normalization-layer table repeated floating values from the retained
`cmh-gate-zero` artifact even though its recorded commit does not contain that target and the
artifact is explicitly not linked as current evidence. Those values were removed; the exact
formulas and future calibration requirements remain.

The obstruction file now calls its numerical material a diagnostic role rather than a numerical
demonstration. The linear-test entry likewise avoids describing richer numerical spectral
estimators as two-sided evidence without rigorous error control.

## Logical effect

No mathematical statement, ledger status or edge, proof dossier, review verdict, or numerical
artifact changed. The cleanup only makes the knowledge prose match the repository's soundness
contract. No ledger edit is required because no claim changed.

## Validation

- All internal ids mentioned in `research/knowledge/*.md` resolve to a ledger id or manuscript
  label.
- `python3 research/check_ledger.py`: clean.
- `python3 -m unittest discover -s research/tests -p 'test_*.py'`: clean.
- `cd experiments && uv run python -m finum selftest`: pass.
- `cd experiments && uv run pytest`: 90 passed.
