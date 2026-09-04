---
type: exploration
date: "2026-08-27"
outcome: proposed
nodes:
  - prop:two-tail
---
# Prover repair: cut-oriented Lyapunov--Stein duality (wave 2, S02)

Date: 2026-08-27

Role: `/root/repair_lyapunov_stein_duality_w2`

Scope key: `solution:lem-lyapunov-stein-duality`

Artifact: `solutions/lem-lyapunov-stein-duality.tex`

Repair contract:
`research/reviews/2026-08-27-lem-lyapunov-stein-duality-proof-review.md`

## Prior audit blockers

The cold audit pinned the original dossier at SHA-256
`a66f3d93d9af8d38eba1c8ced50adcdb6a744d341af34275ab131f7a15bd69af`.  It found the
analytic argument and constants correct, but declined certification for three semantic reasons.

1. The dossier's formal lemma continued past direct-sum invariance and included the eigenbasis
   weighted-harmonic-mean identity and the exact anisotropic two-tail calibration
   $\lambda_{\rm cut}(A_\Lambda,K_\Lambda)=\Lambda$.  The labeled manuscript lemma and ledger
   statement end at direct-sum invariance, so the dossier formally asserted a wider theorem.
2. The two-tail calculation cited the proved node `prop:two-tail`, but that dependency was absent
   from the dossier header and the ledger node's `depends_on` list.
3. The ledger's abbreviated statement did not explicitly record that
   $\mathscr L_A^{-1}$ is taken on the covariance support, that the quotient defining
   $\lambda_{\rm cut}$ has domain $K\ne0$, or that $\lambda_{\rm cut}(A,0)=0$.

The prior audit remains immutable and certifies no node.

## Exact dossier repair

The formal lemma in `solutions/lem-lyapunov-stein-duality.tex` now ends immediately after
$$
\lambda_{\rm cut}(A\oplus B,K\oplus0)=\lambda_{\rm cut}(A,K),
$$
so its scope matches the labeled manuscript lemma.  The proof environment likewise ends after
the direct-sum argument.  The eigenbasis formula, its derivation from the covariance-support
Moore--Penrose formula, and the exact two-tail calculation were moved together into an explicitly
named post-proof remark, “Auxiliary eigenbasis formula and two-tail calibration.”  That remark
states that its identities are not assertions of the formal lemma.

The dossier header now declares

```text
depends_on: lem:pathwise-BL; prop:two-tail
```

because the auxiliary remark still cites `prop:two-tail`.  The repair retains the exact
$K_\Lambda=8a\varphi(a)\Lambda e_1e_1^T$ normalization and the calculation
$\mathscr L_{A_\Lambda}^{-1}K_\Lambda=K_\Lambda/\Lambda$.  It also preserves the covariance-
support inverse convention, ambient Moore--Penrose interpretation on supported matrices,
singular direct-sum blocks, the separate $K=0$ branch, the factor $4/t$, and the explicit
exclusion of any assertion at $t=0$.

The dossier remains `checked_by: none`.  No review, manuscript, ledger, route, bibliography, or
knowledge file was edited in this repair.

## Validation

The forced standalone command

```bash
cd solutions
latexmk -g -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=../build lem-lyapunov-stein-duality.tex
```

succeeded and produced a three-page PDF.  The log has no TeX error, overfull box, or underfull
box.  Its unresolved cross-manuscript references are the expected standalone-subfile behavior.
The repaired source hash is

```text
ea4680b012c611bb99af21639f885e05103e610e698139ee2f55445d5d28dc33  solutions/lem-lyapunov-stein-duality.tex
```

## Central synchronization still required

Before a fresh cold review, the orchestrator must add `prop:two-tail` to the ledger node's
`depends_on` list and make the ledger statement explicit about covariance-support inversion, the
$K\ne0$ quotient domain, and the convention $\lambda_{\rm cut}(A,0)=0$.  No enlargement of the
labeled manuscript lemma is required.  Certification metadata and a status transition remain
inapplicable until a distinct reviewer passes the repaired hash.

```yaml
outcome: complete
artifacts:
  - solutions/lem-lyapunov-stein-duality.tex
  - research/explorations/2026-08-27-prover-lyapunov-stein-duality-repair-w2s02.md
proposed_deltas:
  - add prop:two-tail to lem:lyapunov-stein-duality.depends_on
  - totalize the ledger statement's support-inverse and zero-case conventions
next_role: proof-checker
next_prompt: |
  Cold-review solutions/lem-lyapunov-stein-duality.tex at SHA-256
  ea4680b012c611bb99af21639f885e05103e610e698139ee2f55445d5d28dc33 after the orchestrator
  applies the stated ledger semantic synchronization. Verify that the formal lemma now ends
  after direct-sum invariance and agrees with the labeled manuscript lemma; treat the harmonic-
  mean formula and exact two-tail calculation only as the explicitly auxiliary post-proof
  calibration. Recheck the factor 4, covariance-support inverse, singular blocks, K=0 branch,
  direct sums, and t=0 exclusion. Rebuild standalone and persist a new review; do not amend the
  prior immutable audit.
```
