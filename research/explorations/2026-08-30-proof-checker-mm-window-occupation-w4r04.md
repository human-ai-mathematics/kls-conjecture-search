---
---
# Cold proof review: prop:mm-window-occupation assembly dossier (w4r04)

- **Role / identity:** `proof-checker` `proof-checker-w4r04` (distinct from author
  `claude-prover-w4p02`; launched without the prover's conversation history).
- **Scope:** exactly one dossier, `solutions/prop-mm-window-occupation.tex`
  (SHA-256 `dcde8acc03b27565e4a811cec5a0b79e9f74fccedd502a269129a6dde16ff7b8`),
  ledger node `prop:mm-window-occupation` (`research/kls/ledger.yaml:950`, currently
  `open`), manuscript `modules/kls/30-spectral-route.tex`. Companion dossiers
  `lem-mm-stopped-window-source` / `lem-mm-restart-deweighting` /
  `lem-mm-smallgap-fourth-moment` are under separate review; their statements were
  treated as inputs.
- **Output:** `research/reviews/2026-08-30-prop-mm-window-occupation-proof-review.md`
  (`type: proof-review`, `verdict: pass`, explicitly contingent as below).

## What was reconstructed and checked

Full artifact-only reconstruction: dossier, ledger, manuscript statements
(`prop:mm-window-occupation`, `q:mm-spectral-occupation`, `eq:spectral-occupation`,
`thm:KL-window`, `thm:klartag-logn`, `thm:letwin-qcts`, `subsec:sl-process`,
`eq:sl-density`, `prop:covariance-spike`), the three companion candidate dossiers (as
statement inputs, versions hashed in the review), and the certified dependency dossiers
`lem-mm-time-weighted-fixed-source.tex` and `prop-spectral-sufficiency.tex` with their
2026-08-27 passing reviews.

Steps verified line by line (details in the review):

1. Continuity of $t\mapsto A_t$ (DCT with $(1+|x|^2)e^{R|x|}$ domination); $\tau_L$ a
   stopping time; $\tau_2>0$ a.s.; $\{\tau_2\le T\}\in\F_{\tau_2}$.
2. The law-identification lemma: Lipschitz drift via Brascamp–Lieb
   ($\nabla_z\mathsf a\preceq\varepsilon^{-1}I$), deterministic solution map
   $\mathsf S_\mu$ with pathwise uniqueness, planted channel as
   $\mathsf S_\mu(W^{\mathrm{innov}})$ at $\sigma=0$, both realizations' tilt laws equal
   $\mathsf S_\mu\#\mathbb W$, hence `thm:KL-window` transfers. This is the step the
   2026-08-30 probe consumed silently; the dossier proves it and the proof is sound.
3. Optional projection $\E[v_\tau^2\one_{\tau\le T}]\le\E_\mu f^4$ (optional-time
   identification for $\phi\ge0$, conditional Jensen at the stopping time, tower).
4. Tail integral: exact identity $\tau^{-2}=T^{-2}+2\int_\tau^Ts^{-3}\dd s$,
   $\delta$-regularized Tonelli, substitution
   $\int_{1/T}^\infty ue^{-u/\bar C}\dd u=(\bar C/T+\bar C^2)e^{-1/(\bar CT)}$, and
   $1+2\bar C+2\bar C^2\le5\bar C^2$ via $(3\bar C+1)(\bar C-1)\ge0$ for $\bar C\ge1$,
   $T\le1$. WLOG $\bar C\ge1$ is loss-free.
5. $t_c$ well defined: $h$ increasing on $(0,1/(4\bar C)]$
   ($\dd\log h/\dd t=t^{-1}(1/(2\bar Ct)-2)$), $h\to0$ at $0^+$, sublevel set a
   nonempty interval, $t_c\le1/4<1$, universal.
6. Constant chain: $8L^2T=32T$ at $L=2$; post-exit
   $\sqrt2\,T\,h(T)\le\sqrt2\,T$ on $(0,t_c]$; $32+\sqrt2\le34$; $C_0=34$, $C_1=0$, no
   damping consumed.
7. Fixed-$n$ bridge rerun against the certified `prop-spectral-sufficiency.tex` text:
   $q$-identity finiteness from $\E\int S\le34t$, $q\le\varepsilon^{-1}$,
   $\E D\le\varepsilon^{-2}$ (both caps re-derived); Bessel; $q\le1+34t\le M_*=1+34t_c$
   with no Grönwall; terminal variance $\ge1/2$ at $T_*(n)$; posterior Brascamp–Lieb
   upper bound $\lambda/T_*$; $T_*(n)\ge c_1/\log^2n$ for $n\ge2$; large-gap branch via
   `thm:klartag-logn`; certified fixed-test approximation passage at fixed $n$ with
   $j$-independent constant $C_2\log^2n$. Confirmed no rerun step uses
   dimension-freeness.
8. Scope fences: not `q:mm-spectral-occupation` itself; no beyond-window claim
   (`prop:covariance-spike` respected); output strictly weaker than the published
   $\log n$ input (route-health certificate only); nothing on the trace-upgrade cluster
   (constraint 6); conditional standing per constraint 7 carried in statement and
   header.
9. Standalone build from clean state: 7-page PDF, `??` refs as expected.
   `python3 research/check_ledger.py`: 0 errors (read-only run).

## Verdict and contingency

**Pass**, as a certification of the assembly only, with the ledger effect gated on:
(a) conditionality on `thm:letwin-qcts` (preprint-unreviewed) — node at most
`conditional`; (b) passing independent proof reviews of the three companion dossiers at
the SHA-256 versions recorded in the review (the restart companion's certification must
cover its internal Steps 2, 4, 5, 6, 7(a), which the assembly cites directly and which
any full review of that dossier checks as part of its proof).

Steps *not* verified here: the companions' own proofs (separate reviews); the original
derivations inside the two 2026-08-27-certified dossiers (their reviews stand); the
external PDFs of KLnotes/Klartag2023/Letwin were not re-opened — use matches the
registered import statements, and the KL-window source verification rests on the
manuscript's `rem:kl-window-verified` (arXiv:2406.01324v2).

Findings for the orchestrator beyond the verdict: stale "ledger acceptance pending"
header comments in the dossier (nodes now exist); manuscript/ledger statements leave
$n\ge2$ implicit via $K_n$ (optional wording tightening).

## Contingency discharged in-session

Before handoff, the three companion reviews landed and were wired (passes by
`proof-checker-w4r02` and `proof-checker-w4r03`, commits `935c6b7` and `bbf4a43`). Git
verification: the certified companion texts equal the hashed versions I consumed
(prover commit `e4ae256`); all later edits to the three `.tex` files are
`%`-comment header wiring only (zero non-comment diff lines). The restart review
explicitly verifies Steps 2, 4, 5, 6, 7 — the internal artifacts this assembly cites.
See the addendum in my review report. The delta below is therefore applicable now.

## Proposed ledger delta (applicable now)

On `prop:mm-window-occupation` in `research/kls/ledger.yaml`:

```yaml
status: conditional        # thm:letwin-qcts undischarged (constraint 7)
solution: solutions/prop-mm-window-occupation.tex
checked_by: agent
review: research/reviews/2026-08-30-prop-mm-window-occupation-proof-review.md
```

No `bounded_by` addition proposed. No manuscript statement change required (optional:
add "$n\ge2$" to the proposition and ledger statement).

---

```yaml
outcome: complete
artifacts:
  - research/reviews/2026-08-30-prop-mm-window-occupation-proof-review.md
  - research/explorations/2026-08-30-proof-checker-mm-window-occupation-w4r04.md
proposed_deltas:
  - "research/kls/ledger.yaml node prop:mm-window-occupation: set status: conditional, solution: solutions/prop-mm-window-occupation.tex, checked_by: agent, review: research/reviews/2026-08-30-prop-mm-window-occupation-proof-review.md. The companion contingency is discharged (see review addendum: all three companion reviews passed on the exact consumed versions, later edits comment-only); the node stays conditional while thm:letwin-qcts is preprint-unreviewed (constraint 7)."
  - "dossier header refresh at wiring: in solutions/prop-mm-window-occupation.tex update the stale 'candidate node, ledger acceptance pending' comments (nodes now exist), and set checked_by: agent, reviewer: proof-checker-w4r04, review: research/reviews/2026-08-30-prop-mm-window-occupation-proof-review.md."
  - "optional: add 'n>=2' to the manuscript statement at modules/kls/30-spectral-route.tex \\label{prop:mm-window-occupation} and to the ledger statement of prop:mm-window-occupation (currently implicit via K_n from thm:klartag-logn); run check_ledger after."
next_role: orchestrator
next_prompt: |
  The assembly dossier solutions/prop-mm-window-occupation.tex passed cold review
  (research/reviews/2026-08-30-prop-mm-window-occupation-proof-review.md, reviewer
  proof-checker-w4r04, author claude-prover-w4p02). The review's companion contingency
  is already discharged: all three companion reviews (w4r02/w4r03) passed on exactly
  the consumed versions (git-verified, later edits comment-only; see review addendum).
  Apply the proposed ledger delta now: on prop:mm-window-occupation set
  status: conditional, solution, checked_by: agent, review as listed. Keep the node
  conditional while thm:letwin-qcts remains preprint-unreviewed (constraint 7). Refresh
  the assembly dossier's stale header comments and checked_by/reviewer/review fields at
  wiring, consider the optional 'n>=2' wording tightening in the manuscript and ledger
  statements, and run python3 research/check_ledger.py to 0 errors.
```
