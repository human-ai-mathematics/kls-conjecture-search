# Proof-checker: cold review of two Route-S window-chain dossiers (stopped source, small-gap fourth moment)

Date: 2026-08-30

Role: `proof-checker`

Run id: `w4r03`

Reviewer identity: `proof-checker-w4r03` (distinct from author `claude-prover-w4p02`;
authorship confirmed from the dossier headers and
`research/explorations/2026-08-30-prover-mm-window-chain-w4p02.md`, which was consulted
for authorship only, not as mathematical evidence).

Concurrency keys: `review:lem-mm-stopped-window-source`,
`review:lem-mm-smallgap-fourth-moment`,
`exploration:research/explorations/2026-08-30-proof-checker-mm-window-lemmas-w4r03.md`.

## Scope and method

Two separate cold reviews, reconstructed from repository artifacts only (dossiers,
`modules/kls/30-spectral-route.tex`, `modules/kls/02-family-stochastic-localization.tex`,
`modules/kls/14-qcts-obstruction.tex`, `modules/kls/15-covariance-technology.tex`,
`modules/kls/00-orientation.tex`, `research/kls/ledger.yaml`, `fi_references.bib`, prior
certified reviews for the shared channel convention). No numerical artifact was used as
evidence for any step. Both dossiers rebuilt standalone
(`latexmk -g -pdf -outdir=../build`, exit 0, only expected `??` cross-module refs).
`python3 research/check_ledger.py` reported 0 errors (202 nodes) before the reports were
added. Reviewed SHA-256:

- `solutions/lem-mm-stopped-window-source.tex`
  `a559c44fc9288c76be10be2d75a650c7f74524ef3ed5562490867f51a16a7e82`
- `solutions/lem-mm-smallgap-fourth-moment.tex`
  `3a722083c961595dbaf8ed3e6b610b5dfe189f3d726c675479224bbaaabdd2a1`

## Outcome A — `lem:mm-stopped-window-source`: pass (conditional)

Report: `research/reviews/2026-08-30-lem-mm-stopped-window-source-proof-review.md`
(`type: proof-review`, `verdict: pass`).

Every step checked: Cameron–Martin/Bayes fixed-time identification; a.e. definedness of
$H_t$ via Tonelli and conditional Cauchy–Schwarz; whitened symmetric-matrix duality
$\norm{A_t^{-1/2}H_tA_t^{-1/2}}_{\HS}^2\le8v_t$ with the Letwin hypothesis applied to the
genuinely isotropic log-concave whitened posterior; deterministic unwhitening strictly
before $\tau_L$ (inf-implication only); $\E v_t\le1$ via Jensen (correct without
centering of $f$); Tonelli assembly to $8L^2T$. Verified negatively: no independence
step, no unstopped $\norm{A_t}_\op$ moment, no engagement of the marginal-independence
fallacy; `prop:covariance-spike` and the registered obstruction shapes respected;
conditional standing carried in statement, hypothesis environment, and header
(constraint 7). Statement agreement across dossier/ledger/manuscript holds; the dossier
proves slightly more (no isotropy used), a recorded refinement.

Reviewer-verified routine completion (recorded in the report, no repair needed):
measurability of $\{t<\tau_L\}$, needed for the statement's expectation and the Tonelli
step, follows from pathwise continuity of $t\mapsto A_t$ (dominated convergence with
Gaussian-tail domination from $\nabla^2V\succeq\varepsilon I$), giving
$\{\tau_L>t\}=\{\sup_{([0,t]\cap\mathbb Q)\cup\{t\}}\norm{A_s}_\op<L\}$. This is plain
measurability, not stopping-time theory, so the dossier's disclaimer stands. Dead end
checked and closed: without path continuity, the debut of the jointly measurable set
$\{\norm{A_t}_\op\ge L\}$ would need completed-filtration projection arguments; the
continuity route avoids that entirely.

Sharpening noted (not a defect): the stated hypothesis $L\ge1$ is unused — the proof is
valid for every $L>0$.

## Outcome B — `lem:mm-smallgap-fourth-moment`: pass (proved-eligible)

Report: `research/reviews/2026-08-30-lem-mm-smallgap-fourth-moment-proof-review.md`
(`type: proof-review`, `verdict: pass`).

Every step checked: Bakry–Émery + Gross hypercontractive qualitative $L^4$ bound
($\varepsilon$-dependent, finiteness only); the truncated-cubic $C^1$ matching, normal
contraction/form-domain step, and the form pairing; two-sided monotone convergence
(monotonicity in $k$ verified by differentiation) giving
$\lambda\E f^4=3\E f^2|\nabla f|^2$ as an identity in $[0,\infty]$; Poincaré for $f^2$
under the $K_n$ hypothesis (the only use of isotropy/centering); the rearrangement to
$\E f^4\le2$ licensed exactly by the $L^4$ finiteness; constant chain
$\tfrac{4K_n}3\cdot\tfrac3{8K_n}=\tfrac12$ exact. The $4/3$-coefficient non-circularity
observation and the large-gap branch remain remarks deriving no claim. Citation debt
clean: sole formal dependency `thm:klartag-logn` is a published import
(`Klartag2023Logarithmic`, Ars Inveniendi Analytica 2023:4), consumed as stated;
Bakry–Émery and BGL are published classics; no preprint-unreviewed input anywhere.

## Stale-header note (both dossiers, editorial)

Both headers still say "candidate node, ledger acceptance pending"; the nodes (and the
Klartag import) now exist in `research/kls/ledger.yaml`. The created statements are the
reviewed ones; no semantic mismatch. Flagged for a future editorial pass, not a repair
condition.

## Proposed ledger deltas (for the orchestrator; both reviews are passing proof-reviews)

- `lem:mm-stopped-window-source` (kls ledger): add
  `solution: solutions/lem-mm-stopped-window-source.tex`, `checked_by: agent`,
  `review: research/reviews/2026-08-30-lem-mm-stopped-window-source-proof-review.md`;
  status may move `open` → `conditional` (on `thm:letwin-qcts`,
  preprint-unreviewed; constraint 7 forbids `proved`). `depends_on: [thm:letwin-qcts]`
  already present; no `bounded_by` edge proposed.
- `lem:mm-smallgap-fourth-moment` (kls ledger): add
  `solution: solutions/lem-mm-smallgap-fourth-moment.tex`, `checked_by: agent`,
  `review: research/reviews/2026-08-30-lem-mm-smallgap-fourth-moment-proof-review.md`;
  status may move `open` → `proved` (sole dependency `thm:klartag-logn` is an accepted
  published import; no unresolved premise remains) — final status call is the
  orchestrator's. `depends_on: [thm:klartag-logn]` already present.

## Not checked here

The companion dossiers `lem-mm-restart-deweighting` and `prop-mm-window-occupation`
(separate `review:` keys, other cold checkers); the Letwin preprint itself; the Klartag
paper beyond its accepted import statement; `q:mm-spectral-occupation` and any
occupation, universal-time, or unstopped claim; the pipeline non-circularity claim in
dossier B's remark.

```yaml
outcome: complete
artifacts:
  - research/reviews/2026-08-30-lem-mm-stopped-window-source-proof-review.md
  - research/reviews/2026-08-30-lem-mm-smallgap-fourth-moment-proof-review.md
  - research/explorations/2026-08-30-proof-checker-mm-window-lemmas-w4r03.md
proposed_deltas:
  - "kls ledger, lem:mm-stopped-window-source: solution: solutions/lem-mm-stopped-window-source.tex; checked_by: agent; review: research/reviews/2026-08-30-lem-mm-stopped-window-source-proof-review.md; status open -> conditional (premise thm:letwin-qcts, preprint-unreviewed)"
  - "kls ledger, lem:mm-smallgap-fourth-moment: solution: solutions/lem-mm-smallgap-fourth-moment.tex; checked_by: agent; review: research/reviews/2026-08-30-lem-mm-smallgap-fourth-moment-proof-review.md; status open -> proved (sole dependency thm:klartag-logn is an accepted published import)"
next_role: orchestrator
next_prompt: |
  Both cold reviews passed as type: proof-review, verdict: pass. Apply the two proposed
  ledger deltas above atomically to research/kls/ledger.yaml, then run
  python3 research/check_ledger.py and confirm 0 errors. Constraint 7:
  lem:mm-stopped-window-source stays conditional on thm:letwin-qcts; do not mark it
  proved. lem:mm-smallgap-fourth-moment may be proved since thm:klartag-logn is an
  accepted published import. Optional editorial follow-ups (no review invalidation):
  refresh the stale "candidate node, ledger acceptance pending" header comments in both
  dossiers and fill their reviewer/review header fields; a future prover pass may also
  add one sentence on pathwise continuity of A_t (measurability of {t < tau_L}) in
  lem-mm-stopped-window-source and may relax L >= 1 to L > 0. The companion dossiers
  lem-mm-restart-deweighting and prop-mm-window-occupation remain unreviewed and need
  their own cold checkers under their own review:<dossier> keys.
```
