---
---

# Migration to the template's proof provenance

This checkpoint records a harness change. It changes no mathematical status: the ledger
holds the same 131 nodes with the same statuses (86 proved, 39 open, 4 defined,
2 refuted), and every certification still holds.

## Question examined

How to show a reader who certified each proved statement, and when, and to tell an
agent's review from a human's. Until now the site showed *Proved* alone, the same for a
proof reviewed here and for a result imported from the literature.

## What changed

The template (branch `proof-provenance` of conjecture-search-template) now:

- shows a certification next to *Proved*: *agent review (model, date)* or *reviewed by* a
  human, linked to the report on GitHub, or *accepted by* a human. A node proved on
  `references` alone shows *Established in the literature*;
- requires `reviewer`, every `authors` entry and `accepted_by` to be identities
  `<who>, <model or human>, <YYYY-MM-DD>`, which `scripts/checks/proofs.py` validates.

`scripts/status.mjs`, `scripts/checks/proofs.py`, the two test files, `SPECIFICATION.md`,
`proofs.md` and both reviewer roles were copied from it unchanged.

## The 39 review reports were rewritten once

`research/reviews/` is append-only. This migration makes a single exception: it rewrote the
`reviewer` and `authors` lines of all 39 reports, and nothing else. No verdict, fingerprint
or body changed. These fields are not fingerprinted, so no certification lapsed.

Every reviewer and author here was an AI agent. Rules applied:

- `<who>` is the last segment of the old value, with no `/root/` or `/w5/` prefix.
- `<model>` is `unknown` unless the old value named it. Only one did: "Claude Fable 5"
  became `claude-fable-5`.
- The date is the report's filename date. Two exceptions, both prover agents of wave four:
  - `prover w4p03` keeps the 2026-08-30 its old value gave.
  - `prover w4p04` is given 2026-08-30 too. This is inferred from the wave, not recorded.

| Report | reviewer | authors |
|---|---|---|
| `2026-08-25-kls-cmh-exact-cases-repair-audit.md` | `/root/cmh_exact_reviewer` → `cmh_exact_reviewer, unknown, 2026-08-25` | `/root/kls_ledger_audit` → `kls_ledger_audit, unknown, 2026-08-25` |
| `2026-08-25-kls-cmh-normalization-repair-audit.md` | `/root/kls_evidence_audit` → `kls_evidence_audit, unknown, 2026-08-25` | `/root/kls_proof_audit` → `kls_proof_audit, unknown, 2026-08-25` |
| `2026-08-25-kls-core-r2-audit.md` | `/root/kls_bootstrap_author` → `kls_bootstrap_author, unknown, 2026-08-25` | `/root/kls_core_author` → `kls_core_author, unknown, 2026-08-25` |
| `2026-08-25-kls-excess-bootstrap-r2-audit.md` | `/root/kls_core_author` → `kls_core_author, unknown, 2026-08-25` | `/root/kls_bootstrap_author` → `kls_bootstrap_author, unknown, 2026-08-25` |
| `2026-08-25-kls-geometry-product-r2-audit.md` | `/root/kls_bootstrap_author` → `kls_bootstrap_author, unknown, 2026-08-25` | `/root/kls_proof_audit` → `kls_proof_audit, unknown, 2026-08-25` |
| `2026-08-27-conditional-fiber-frame-structure-proof-review.md` | `/root/review_conditional_fiber_structure_w3` → `review_conditional_fiber_structure_w3, unknown, 2026-08-27` | `/root/prove_conditional_fiber_structure_w3` → `prove_conditional_fiber_structure_w3, unknown, 2026-08-27` |
| `2026-08-27-cor-full-matrix-dissipation-proof-review.md` | `/root/review_full_matrix_dissipation_w2` → `review_full_matrix_dissipation_w2, unknown, 2026-08-27` | `/root/prove_full_matrix_dissipation_w2` → `prove_full_matrix_dissipation_w2, unknown, 2026-08-27` |
| `2026-08-27-cor-full-matrix-dissipation-repair-proof-review.md` | `/root/review_full_matrix_dissipation_w2` → `review_full_matrix_dissipation_w2, unknown, 2026-08-27` | `/root/prove_full_matrix_dissipation_w2` → `prove_full_matrix_dissipation_w2, unknown, 2026-08-27`; `/root/repair_full_matrix_dissipation_w2` → `repair_full_matrix_dissipation_w2, unknown, 2026-08-27` |
| `2026-08-27-kls-excess-repair-w0-audit.md` | `/root/review_excess_w0` → `review_excess_w0, unknown, 2026-08-27` | `/root/kls_bootstrap_author` → `kls_bootstrap_author, unknown, 2026-08-27`; `/root/repair_excess_dossier` → `repair_excess_dossier, unknown, 2026-08-27` |
| `2026-08-27-kls-excess-repair-w0r2-proof-review.md` | `/root/review_excess_repair_w0r2` → `review_excess_repair_w0r2, unknown, 2026-08-27` | `/root/kls_bootstrap_author` → `kls_bootstrap_author, unknown, 2026-08-27`; `/root/repair_excess_dossier` → `repair_excess_dossier, unknown, 2026-08-27` |
| `2026-08-27-kls-geometry-models-repair-proof-review.md` | `/root/review_splitting_w0` → `review_splitting_w0, unknown, 2026-08-27` | `/root/kls_proof_audit` → `kls_proof_audit, unknown, 2026-08-27`; `/root/repair_splitting_dossier` → `repair_splitting_dossier, unknown, 2026-08-27` |
| `2026-08-27-kls-product-covariance-proof-review.md` | `/root/review_product_w0` → `review_product_w0, unknown, 2026-08-27` | `/root/kls_proof_audit` → `kls_proof_audit, unknown, 2026-08-27`; `/root/repair_product_dossier` → `repair_product_dossier, unknown, 2026-08-27` |
| `2026-08-27-lem-affine-poincare-w2-liminf-proof-review.md` | `/root/review_cmh_recovery_w0` → `review_cmh_recovery_w0, unknown, 2026-08-27` | `/root/prove_cmh_recovery` → `prove_cmh_recovery, unknown, 2026-08-27` |
| `2026-08-27-lem-cmh-gamma-bochner-repair-proof-review.md` | `/root/review_cmh_gamma_dependency_w3` → `review_cmh_gamma_dependency_w3, unknown, 2026-08-27` | `/root/kls_ledger_audit` → `kls_ledger_audit, unknown, 2026-08-27`; `/root/repair_cmh_hodge_domain_w3` → `repair_cmh_hodge_domain_w3, unknown, 2026-08-27` |
| `2026-08-27-lem-lyapunov-stein-duality-proof-review.md` | `/root/review_lyapunov_stein_duality_w2` → `review_lyapunov_stein_duality_w2, unknown, 2026-08-27` | `/root/prove_lyapunov_stein_duality_w2` → `prove_lyapunov_stein_duality_w2, unknown, 2026-08-27` |
| `2026-08-27-lem-lyapunov-stein-duality-repair-proof-review.md` | `/root/review_lyapunov_stein_duality_w2` → `review_lyapunov_stein_duality_w2, unknown, 2026-08-27` | `/root/prove_lyapunov_stein_duality_w2` → `prove_lyapunov_stein_duality_w2, unknown, 2026-08-27`; `/root/repair_lyapunov_stein_duality_w2` → `repair_lyapunov_stein_duality_w2, unknown, 2026-08-27` |
| `2026-08-27-lem-mm-posterior-defect-proof-review.md` | `/root/review_posterior_defect_cold_08` → `review_posterior_defect_cold_08, unknown, 2026-08-27` | `/root/prove_posterior_defect_par_06` → `prove_posterior_defect_par_06, unknown, 2026-08-27` |
| `2026-08-27-lem-mm-time-weighted-fixed-source-proof-review.md` | `/root/review_mm_weighted_source_w0` → `review_mm_weighted_source_w0, unknown, 2026-08-27` | `/root/prove_mm_weighted_source` → `prove_mm_weighted_source, unknown, 2026-08-27` |
| `2026-08-27-lem-time-weighted-source-proof-review.md` | `/root/review_time_weighted_cold_07` → `review_time_weighted_cold_07, unknown, 2026-08-27` | `/root/prove_time_weighted_par_05` → `prove_time_weighted_par_05, unknown, 2026-08-27` |
| `2026-08-27-prop-cmh-approximation-closure-proof-review.md` | `/root/review_cmh_approximation` → `review_cmh_approximation, unknown, 2026-08-27` | `/root/prove_cmh_approximation` → `prove_cmh_approximation, unknown, 2026-08-27` |
| `2026-08-27-prop-cmh-hodge-domain-repair-proof-review.md` | `/root/review_cmh_hodge_domain_w3` → `review_cmh_hodge_domain_w3, unknown, 2026-08-27` | `/root/kls_proof_audit` → `kls_proof_audit, unknown, 2026-08-27`; `/root/repair_cmh_hodge_domain_w3` → `repair_cmh_hodge_domain_w3, unknown, 2026-08-27` |
| `2026-08-27-prop-cmh-recovery-calculus-proof-review.md` | `/root/review_cmh_recovery_calculus_w2` → `review_cmh_recovery_calculus_w2, unknown, 2026-08-27` | `/root/prove_cmh_recovery_calculus_w2` → `prove_cmh_recovery_calculus_w2, unknown, 2026-08-27` |
| `2026-08-27-prop-spectator-excess-rate-obstruction-proof-review.md` | `/root/review_spectator_excess_rate_w2` → `review_spectator_excess_rate_w2, unknown, 2026-08-27` | `/root/prove_spectator_excess_rate_w2` → `prove_spectator_excess_rate_w2, unknown, 2026-08-27` |
| `2026-08-27-prop-spectral-sufficiency-proof-review.md` | `/root/review_spectral_sufficiency_w0` → `review_spectral_sufficiency_w0, unknown, 2026-08-27` | `/root/prove_spectral_sufficiency` → `prove_spectral_sufficiency, unknown, 2026-08-27` |
| `2026-08-27-prop-weighted-spectator-obstruction-proof-review.md` | `/root/review_weighted_spectator_w0` → `review_weighted_spectator_w0, unknown, 2026-08-27` | `/root/prove_weighted_spectator_obstruction` → `prove_weighted_spectator_obstruction, unknown, 2026-08-27` |
| `2026-08-27-prop-weighted-spectator-obstruction-repair-proof-review.md` | `/root/review_weighted_spectator_w0r2` → `review_weighted_spectator_w0r2, unknown, 2026-08-27` | `/root/prove_weighted_spectator_obstruction` → `prove_weighted_spectator_obstruction, unknown, 2026-08-27`; `/root/repair_weighted_spectator_w0r2` → `repair_weighted_spectator_w0r2, unknown, 2026-08-27` |
| `2026-08-27-thm-bootstrap-semantic-repair-proof-review.md` | `/root/review_bootstrap_sync_w0` → `review_bootstrap_sync_w0, unknown, 2026-08-27` | `/root/kls_bootstrap_author` → `kls_bootstrap_author, unknown, 2026-08-27` |
| `2026-08-27-thm-bootstrap-stopped-interface-proof-review.md` | `/root/review_bootstrap_stopped_interface_w3` → `review_bootstrap_stopped_interface_w3, unknown, 2026-08-27` | `/root/prove_bootstrap_stopped_interface_w3` → `prove_bootstrap_stopped_interface_w3, unknown, 2026-08-27` |
| `2026-08-30-lem-mm-restart-deweighting-proof-review.md` | `proof-checker-w4r02` → `proof-checker-w4r02, unknown, 2026-08-30` | `claude-prover-w4p02` → `claude-prover-w4p02, unknown, 2026-08-30` |
| `2026-08-30-lem-mm-smallgap-fourth-moment-proof-review.md` | `proof-checker-w4r03` → `proof-checker-w4r03, unknown, 2026-08-30` | `claude-prover-w4p02` → `claude-prover-w4p02, unknown, 2026-08-30` |
| `2026-08-30-lem-mm-stopped-window-source-proof-review.md` | `proof-checker-w4r03` → `proof-checker-w4r03, unknown, 2026-08-30` | `claude-prover-w4p02` → `claude-prover-w4p02, unknown, 2026-08-30` |
| `2026-08-30-prop-mm-window-occupation-proof-review.md` | `proof-checker-w4r04` → `proof-checker-w4r04, unknown, 2026-08-30` | `claude-prover-w4p02` → `claude-prover-w4p02, unknown, 2026-08-30` |
| `2026-08-30-prop-split-screened-supply-proof-review.md` | `proof-checker-w4r01` → `proof-checker-w4r01, unknown, 2026-08-30` | `prover-w4p01` → `prover-w4p01, unknown, 2026-08-30` |
| `2026-09-06-lem-cmh-linear-spectral-resolution-audit.md` | `/w5/reviewer-clsr` → `reviewer-clsr, unknown, 2026-09-06` | `prover w4p03 (Claude agent, session 2026-08-30)` → `prover w4p03, unknown, 2026-08-30` |
| `2026-09-06-lem-cmh-linear-spectral-resolution-proof-review.md` | `/w5/reviewer-clsr-second` → `reviewer-clsr-second, unknown, 2026-09-06` | `prover w4p03 (Claude agent, session 2026-08-30)` → `prover w4p03, unknown, 2026-08-30`; `/w5/researcher-clsr-repair` → `researcher-clsr-repair, unknown, 2026-09-06` |
| `2026-09-06-lem-fiber-root-degree-two-proof-review.md` | `/w5/reviewer-fiber-root` → `reviewer-fiber-root, unknown, 2026-09-06` | `prover agent (Claude Fable 5), run id w4p04` → `prover w4p04, claude-fable-5, 2026-08-30` |
| `2026-09-06-lem-linear-sector-third-moment-proof-review.md` | `/w5/reviewer-third-moment` → `reviewer-third-moment, unknown, 2026-09-06` | `/w5/researcher-third-moment` → `researcher-third-moment, unknown, 2026-09-06` |
| `2026-09-06-prop-cone-moment-map-audit.md` | `/w5/reviewer-cone-lift` → `reviewer-cone-lift, unknown, 2026-09-06` | `/w5/researcher-cone-lift` → `researcher-cone-lift, unknown, 2026-09-06` |
| `2026-09-06-prop-cone-moment-map-proof-review.md` | `/w5/reviewer-cone-lift-second` → `reviewer-cone-lift-second, unknown, 2026-09-06` | `/w5/researcher-cone-lift` → `researcher-cone-lift, unknown, 2026-09-06`; `/w5/researcher-cone-lift-repair` → `researcher-cone-lift-repair, unknown, 2026-09-06` |
