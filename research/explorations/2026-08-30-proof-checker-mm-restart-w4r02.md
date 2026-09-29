---
---
# Proof-checker: cold review of the restart-deweighting dossier (w4r02)

Date: 2026-08-30
Role: `proof-checker`
Run id: `w4r02`
Reviewer identity: `proof-checker-w4r02` (distinct from author `claude-prover-w4p02`)
Scope: exactly one dossier, `solutions/lem-mm-restart-deweighting.tex`, node
`lem:mm-restart-deweighting` (`research/kls/ledger.yaml`, manuscript label in
`modules/kls/30-spectral-route.tex`).

## What was done

Reconstructed the proof from repository artifacts only (dossier, manuscript module, ledger,
obstruction registry, certified dependency dossier and its 2026-08-27 review, bibliography). The
prover's exploration record was consulted solely to confirm authorship. Built the dossier
standalone (`latexmk -pdf -outdir=../build`, exit 0). Ran `python3 research/check_ledger.py`
(0 errors, unchanged). Wrote the certifying report
`research/reviews/2026-08-30-lem-mm-restart-deweighting-proof-review.md`
(`type: proof-review`, `verdict: pass`).

## Checks performed (all passed)

1. Statement agreement across dossier theorem, ledger `statement:`, and manuscript
   `\label{lem:mm-restart-deweighting}`; the dossier's two refinements (augmented-filtration
   stopping times; no isotropy/centering) strictly cover the manuscript claim, and the
   augmented-filtration bound implies the raw-filtration reading by the tower property since the
   right-hand side is $(\sigma,c_\sigma)$-measurable.
2. Step 1: Cameron–Martin likelihood, admissible-test domination, Bayes identification on the
   raw filtration, and its transfer to the usual augmentation via
   $\bigcap_k\sigma(\mathcal F^0_{u_k}\cup\mathcal N)=\mathcal F_t$ and reverse martingale
   convergence (both inclusions verified).
3. Step 2: dyadic optional sampling of the closed bounded martingale, including the
   $\{\sigma_k=\infty\}$ piece; $\bigcap_k\mathcal F_{\sigma_k}=\mathcal F_\sigma$; the RCD
   property (no simultaneous-null-set gap because $\mu_\sigma$ is already a kernel and the RCD
   definition is per Borel set); $f\in L^2(\mu_\sigma)$ a.s. via $\phi=f^2$ in $[0,\infty]$.
4. Step 3: exact potential algebra, $(\varepsilon+\sigma)$-strong log-concavity, admissibility
   for the certified lemma.
5. Step 4: independence of Brownian increments from $\mathcal G_{s+}$, the augmentation lemma
   $\bigcap_{u>s}\sigma(\mathcal F^0_u\cup\mathcal N)=\sigma(\mathcal F^0_{s+}\cup\mathcal N)$
   (verified by the limsup-of-representatives argument — the one tersely stated step), the
   conditional-Fubini drift cancellation, the finite-variation bracket argument, Lévy, and the
   dyadic strong-Markov identity with its $\pi$-system/monotone-class upgrade.
6. Step 5: the pathwise-exact restart algebra (no null set involved).
7. Step 6: the deterministic Banach fixed-point solution map — Brascamp–Lieb Jacobian cap
   $\kappa^{-1}$, contraction constant recomputed
   ($\kappa^{-1}\int_0^ue^{2s/\kappa}ds\le\tfrac12e^{2u/\kappa}$), pathwise uniqueness in the
   full class of continuous paths with no side condition (the legitimate Yamada–Watanabe
   replacement, since the noise is additive and drift globally Lipschitz), and measurability via
   Picard iterates.
8. Step 7: pathwise identity, freezing via the two-finite-measures $\pi$-$\lambda$ argument,
   evaluation at a frozen prior with $W'\sim\mathbb W$, exact consumption of the certified
   `lem:mm-time-weighted-fixed-source` with $\kappa=\varepsilon+\sigma$ (nonnegative-term drops
   are those certified nonnegative), monotone convergence in $T$, and the final
   $\varepsilon+\sigma\ge\sigma>0$ chain.
9. $\mathsf H$ zero-convention affects no integral (verified directly: a.e.-$t$ absolute
   convergence from $f\in L^2(\mu_t)$ plus finite fourth moments, Tonelli).
10. Standing: unconditional, correctly claimed; the only dependency is `status: proved` and
    agent-certified; single external citation `BrascampLieb1976` classified **published**
    against the bibliography record (J. Funct. Anal. 1976, DOI matched); no citation debt.
11. Fences: all six registered obstructions plus `prop:covariance-spike` and the weight-removal
    no-go named and checked against the actual argument; none engaged or violated.
12. Hypothesis accounting: no hypothesis used but unstated; unused isotropy/centering and the
    unused positivity of $\sigma$ for the first inequality are already recorded in the dossier.

## Dead ends / near-defects examined and resolved

- The augmentation-commutes-with-intersection step in Step 4 is stated in one clause; it is a
  true standard lemma and I verified it independently, so it is an expository terseness, not a
  gap.
- The header still carries "candidate node, ledger acceptance pending" although the node now
  exists (status `open`); mechanical staleness only, to be refreshed during the orchestrator's
  post-certification header/ledger wiring. Not a ground for `revise`.

## Handoff

```yaml
outcome: complete
artifacts:
  - research/reviews/2026-08-30-lem-mm-restart-deweighting-proof-review.md
  - research/explorations/2026-08-30-proof-checker-mm-restart-w4r02.md
proposed_deltas:
  - "research/kls/ledger.yaml node lem:mm-restart-deweighting: add solution: solutions/lem-mm-restart-deweighting.tex; checked_by: agent; review: research/reviews/2026-08-30-lem-mm-restart-deweighting-proof-review.md; status may move open -> proved (claim is unconditional and its unique dependency lem:mm-time-weighted-fixed-source is proved and agent-certified; no unresolved premise)."
  - "solutions/lem-mm-restart-deweighting.tex header (mechanical, during wiring): set checked_by: agent, reviewer: proof-checker-w4r02, review: research/reviews/2026-08-30-lem-mm-restart-deweighting-proof-review.md; refresh the stale 'candidate node, ledger acceptance pending' annotations."
next_role: orchestrator
next_prompt: |
  The cold review of solutions/lem-mm-restart-deweighting.tex passed
  (research/reviews/2026-08-30-lem-mm-restart-deweighting-proof-review.md, type: proof-review,
  verdict: pass, author claude-prover-w4p02, reviewer proof-checker-w4r02). Apply the ledger
  delta for lem:mm-restart-deweighting (solution, checked_by: agent, review as listed;
  status: proved is permitted since the node is unconditional and its unique dependency
  lem:mm-time-weighted-fixed-source is proved and certified), refresh the dossier header's
  checked_by/reviewer/review fields and stale candidate annotations, and rerun
  python3 research/check_ledger.py to 0 errors. The remaining window-chain dossiers
  (lem-mm-stopped-window-source, lem-mm-smallgap-fourth-moment, prop-mm-window-occupation)
  are outside this review's scope and still need their own cold reviews.
```
