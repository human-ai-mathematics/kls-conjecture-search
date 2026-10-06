---
---

# Continuing a search after its target is proved

## Question examined

Can the framework retain routes towards alternative proofs or stronger statements after
the target, in this program `conj:kls`, becomes proved? This is a framework change, not a
claim that KLS or any announced proof has been certified here.

## What we learned

- **Established (contract change).** A proved target may retain active routes. Their
  objectives and next tests must identify the remaining work. A proof of the target
  does not refute a route's sufficient condition or establish that route's impossibility.
- **Established (contract change).** A refuted target still rejects active proof routes;
  a corrected statement needs a different target. Closing an accomplished objective,
  abandoning an objective, and proving an obstruction remain distinct reasons to record.
- **Established (implementation).** Only the target-level restriction in the search
  checker changes. Proved and refuted blocker nodes still require reassessment, and
  missing blockers and closed candidates are still rejected. No field, state, or YAML
  schema was added.
- **Established (contract clarification).** The shared statement-level dependency DAG
  is not evidence of independence between proof records. A dossier and its review must
  specify actual inputs and claimed exclusions. A lemma derived from the target cannot
  provide an independent proof of that target. Genuine edges cannot be erased to bypass
  cycles.
- **Observed (regression checks).** The focused search suite passes 13 tests, including
  the proved-target acceptance, refuted-target rejection, and unchanged blocker rules.
  The unchanged ledger suite passes 10 tests and the proof suite passes 34 tests. Commands:
  `.venv/bin/python -m unittest discover -s scripts/tests -p test_search.py`, and the same
  command with `test_ledger.py` and `test_proofs.py`. These checks validate the framework,
  not mathematical correctness or independence.

## What resists

The ledger still represents dependencies per statement, not per proof. If future
alternative proofs require incompatible acyclic representations, that calls for a
separate design and migration. This change does not solve that future representation
problem and does not weaken any certification or fingerprint rule.

## Proposed next step

Reassess the portfolio after actual mathematical certifications, recording what each
continuing route would add. A resolved blocker must be handled even if the main target
also becomes proved. No mathematical status or existing route is changed by this patch.

### Proposal for the upstream template

**Title:** Allow alternative proof routes after a target is proved.

**Problem and behavior:** Previously the checker rejected every active route whenever
the brief's target was proved or refuted. Restrict this rejection to refuted targets.
After a proof, routes may remain active for an explicitly described alternative proof
or stronger result. Keep blocker validation, the node-level DAG, certification, and
fingerprints unchanged. Clarify that the shared DAG does not certify proof independence.

**Patch surface:** The search checker and its tests; the portfolio and stopping rules
in the specification; the portfolio, node, and solution templates; explanatory comments
in the refuted worked example's portfolio. No schema migration is required.

**Validation:** Accept an active alternative-proof route with a proved target; reject
an active route with a refuted target; continue rejecting resolved, absent, and closed
candidate blockers. Run the search, ledger, and proof unit suites and the upstream
repository's full check before merging there. This is a local proposal only: no external
template repository or publication was modified.
