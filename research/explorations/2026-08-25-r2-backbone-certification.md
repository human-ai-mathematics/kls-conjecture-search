# R2 backbone certification and removal of the historical exception

Date: 2026-08-25

## Trigger and scope

The repository still described 41 KLS entries as `proved` without standalone proof dossiers,
and five A-series entries used inline-proof provenance instead of R2.  The requested endpoint was
stricter: no historical or legacy authorization path, and every node left at `status: proved`
must satisfy the ordinary R2 contract.

This pass audits and certifies the elementary KLS backbone.  It does **not** prove KLS, a
universal covariance ceiling, the weighted-excess package, universal CMH(4), or any other open
route target.

## Triage of the 41 KLS entries

The apparent debt mixed proof claims with objects that should never have been marked proved.
The final classification is:

- 34 theorem, lemma, proposition, and corollary nodes: retained as `proved` after standalone
  dossiers and independent review;
- `def:qcts`: reclassified as `defined`;
- `prop:second-variation` and `prop:reilly`: reclassified as published imports after exact-source
  checks against Rosales (2014) and Ma--Du (2010), respectively;
- `rem:kl-window-verified`: reclassified as a published import;
- `rem:almost-stability-gap`: reclassified as open; and
- `rem:trace-upgrade-unification` and `rem:taming-type-mismatch`: reclassified as heuristic.

Thus no proof status was retained merely because an inline manuscript argument existed.  The
five analogous A-series nodes were also moved to ordinary R2 rather than grandfathered.

## Proof dossiers and independent review

The 34 KLS proof claims are grouped by shared notation and dependency interface in six dossiers:

- `solutions/kls-localization-riccati-core.tex`;
- `solutions/kls-qcts-stein-boundary-core.tex`;
- `solutions/kls-excess-audit.tex`;
- `solutions/kls-bootstrap-interface.tex`;
- `solutions/kls-geometry-models.tex`; and
- `solutions/kls-product-covariance.tex`.

They were checked by distinct author/reviewer assignments and persisted in three reports:

- `research/reviews/2026-08-25-kls-core-r2-audit.md` certifies 12 nodes, authored by
  `/root/kls_core_author` and reviewed by `/root/kls_bootstrap_author`;
- `research/reviews/2026-08-25-kls-excess-bootstrap-r2-audit.md` certifies 11 nodes, authored by
  `/root/kls_bootstrap_author` and reviewed by `/root/kls_core_author`; and
- `research/reviews/2026-08-25-kls-geometry-product-r2-audit.md` certifies 11 nodes, authored by
  `/root/kls_proof_audit` and reviewed by `/root/kls_bootstrap_author`.

The five A-series proof claims are grouped in
`solutions/glm-linear-baselines.tex`, `solutions/obs-tv-insufficient.tex`, and
`solutions/a5-lipschitz-quotient.tex`.  They were authored by `/root/ab_legacy_author`, reviewed
by `/root/kls_core_author`, and certified in
`research/reviews/2026-08-25-ab-inline-r2-audit.md`.

Each certified ledger row now has `solution`, `checked_by: agent`, distinct `authored_by` and
`reviewed_by` identities, and a persisted unqualified-pass report.

## Corrections found by proof review

The review was not a metadata-only exercise.  It found and repaired several semantic gaps:

- `lem:excess-identity` now records its compact-support hypothesis in the ledger;
- the Stein/source identity is asserted as an equality only at balance, with the off-balance
  relation stated as a conversion rather than an identity;
- the bootstrap dossier includes the missing sign split needed before multiplying by the
  near-worst Cheeger ratio;
- the noncompact perimeter argument states the full conditional supermartingale conclusion;
- persistent splitting concludes rank **at most** one, including the zero case;
- the coordinate-budget refutation is explicitly limited to a cut and coordinate fixed before
  localization, with no pathwise adaptive selection;
- the imported Reilly formula was corrected from an inner-normal to an outer-normal convention;
  and
- the total-variation example now claims only the proved Poincare divergence, not unsupported
  log-Sobolev or transportation-cost divergence.

The reviews also checked the geometric second-variation signs and domains, the stopping and
localization steps, QCTS regularization, product quadratic-chaos constants, and the exact scope
of the published Klartag--Lehec covariance input.

## Control-plane change

The transitional debt manifests were removed from both ledgers.  `research/check_ledger.py` now
rejects both obsolete field names and has no allowlist or historical fallback.  Every
`status: proved` node must have a certified solution dossier.  Free-text `proof_provenance` is
narrative only.  KLS `status: defined` is accepted only for `kind: definition`; marking a
definition `proved` would still require R2.

Regression tests cover rejection of both obsolete metadata fields and the ordinary R2 checks.
The active dossiers were also renamed from `kls-legacy-*` to neutral backbone names so that
"legacy" survives only in historical records describing the retired debt.

## Validation

- `python3 research/check_ledger.py`: 2 ledgers, 172 nodes, 632 labels, 0 errors, 0 warnings;
- `python3 -m unittest discover -s research/tests -p 'test_*.py'`: 21 passed;
- an independent consistency query found 80 proved nodes, 29 distinct referenced dossiers, and
  zero incomplete or same-author/reviewer R2 rows;
- all 29 ledger-referenced dossiers compiled standalone with `latexmk` in fresh directories
  outside the repository;
- the full `main.tex` build passed at 149 pages with no undefined references or citations;
- `python3 -m py_compile research/check_ledger.py`: passed; and
- `git diff --check`: passed.

## Result

The repository has no active legacy R2 category.  Thirty-nine previously inline-only proof
claims (34 KLS and five A-series) now satisfy the same dossier-and-independent-review contract as
all other proved nodes.  Seven former KLS `proved` entries that were definitions, imports, open
questions, or heuristics have been classified accordingly.  The open KLS route boundaries are
unchanged.
