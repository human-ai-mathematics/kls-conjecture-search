---
type: exploration
date: "2026-08-27"
outcome: directional
nodes:
  - q:stein-weighted
---
# KLS Wave 3: semantic synchronization

Date: 2026-08-27

Role: orchestrator

## Scope

A read-only comparison of the Wave 1--2 promotions against the manuscript, ledger, and proof
dossiers found four semantic deltas.  This synchronization changes no KLS gate status.

## Exact target restored for `q:stein-weighted`

The manuscript asked for the weighted stopped Stein-trace inequality, whereas the ledger had
replaced that mathematical object by its proposed Jacobi--Reilly mechanism.  The question is now
stated on both planes as the actual integral inequality, with
$2\beta+64\eta^2<1$, and explicitly classified as an independent analytic ingredient extracted
from the refuted weighted package.  It has no viable KLS consumer by itself.  In particular, no
implication is asserted between `q:stein-weighted`, `q:upgrade`, and `q:alignment`.

## CMH domain and provenance repairs

The Hodge statement now specifies the closed covariance generator

$$
\mathcal A_1=-\operatorname{Div}_\mu(\Sigma\nabla\,\cdot\,),\qquad
L^2_0(\mu)=(\ker\mathcal A_1)^\perp,
$$

the source condition $h=\mathcal A g\in L^2_0(\mu)$, and the inverse domain

$$
\mathcal A_1^{-1}:L^2_0(\mu)
\longrightarrow \operatorname{Dom}(\mathcal A_1)\cap L^2_0(\mu).
$$

The corresponding dossier is being repaired separately and remains subject to a fresh
independent review before its synchronized bytes are treated as certified.

The Gamma completion now names `prop:cmh-bochner` as the direct source of its integrated
product-Gamma identity.  Conversely, the two dependencies previously attached to
`cor:cmh-linear-images` were removed: its proof is direct conditional-variance tensorization and
the linear-map chain rule, and neither dependency supplies a premise of the corollary.

## Certification wording

The stale word ``candidate'' was removed from the already reviewed Lyapunov--Stein lemma, and the
now-refuted weighted time demand is described in the past tense.  No solution hash was changed by
these two manuscript edits.

## Validation at synchronization time

- `python3 research/check_ledger.py`: 195 nodes, 675 labels, 0 errors.
- `python3 research/check_agents.py`: 0 errors.
- `git diff --check`: clean.
- Full `latexmk` manuscript build: successful, 161 pages.
