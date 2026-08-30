# Proof-checker: cold review of the split-class screened supply dossier

Date: 2026-08-30

Role: `proof-checker`

Run id: `w4r01`

Concurrency key: `review:prop-split-screened-supply`

Reviewer identity: `proof-checker-w4r01` (distinct from the author `prover-w4p01`; the
prover's exploration record was opened only to confirm authorship, not used as evidence).

## What was done

Cold review of `solutions/prop-split-screened-supply.tex` (SHA-256
`c3d36e34b6bb217d20a25528d31595cd6c07db66d186290d4805f987c01a3909`) for the open node
`prop:split-screened-supply`, reconstructed entirely from repository artifacts. Persisted
report: `research/reviews/2026-08-30-prop-split-screened-supply-proof-review.md`
(`type: proof-review`, `verdict: pass`, with an explicit wiring contingency).

Checked and verified (details in the report):

1. Step 1 pathwise domination $e_tW_{\rm cut}\one_{\mathcal A_{\kappa,t}}\le Q_t/\kappa$,
   including $e_t\ge0$ via the profile-infimum upper bound only and the $K_t=0$ case
   under the certified $\lambda_{\rm cut}(A,0)=0$ convention.
2. Step 2 conversion via the second inequality of the certified `lem:stein-vs-source`
   (re-derived: constants $2$ and $64\eta^2$ correct on $\{t<\tau_\eta\}$, $\eta\le1/4$,
   $s_t\ge3/16>1/8$), and $Q_t=\calS_{\mu_t}(E)/s_t$ via `prop:stein-rep`.
3. Step 3 inline reproduction of `thm:budget`(i) under only $0<p_0<1$, verified from
   primitives (`prop:products` + `lem:block` + `cor:per-direction` + isotropy + monotone
   convergence), independently of the product dossier's audit paragraph, which it
   confirms.
4. Step 4 dissipation budget $\le1+k$: localizing times, optional stopping at bounded
   times, $r_0\le1$ (rank-one $B_0\preceq I$), monotone convergence.
5. Conventions (M1)–(M4) match Section 5 of the w4w01 probe and the certified
   perimeter-martingale construction; weight and indicator appear only inside
   nonnegative Lebesgue-time integrals (Tonelli); no Itô calculus on the weight.
6. `rem:sol-general-class` honestly confines the general split class to the
   defined-on-approximants convention and flags the screened-indicator limit interchange
   as open.
7. Auxiliary Lemma `lem:sol-constant-supply-consumption`: one-line Gronwall change from
   the certified `cor:tight-window-consumption`, explicit a priori finiteness hypothesis,
   constants $C_*=(1+c+C_0T_0)e^{C_1T_0}$ and $T_*\le\min(T_0,4\eta^2/(9C_*))$
   recomputed and correct; no companion claimed, no KLS conclusion drawn.
8. Fences `obs:two-tail` and `obs:circularity` respected; constraint-6 disclaimer
   present and respected.
9. Dependency closure: every input `proved` with active agent certification; no
   conditional or preprint-unreviewed input in the cone; no new external citations.
10. Standalone build: clean, 6 pages, expected `??` cross-refs.

## Findings that gate the wiring

- **Statement scope caveat.** The dossier proves the theorem on the compact-smooth
  product-preserving regular split class (M2); the current ledger statement and the
  manuscript proposition at `modules/kls/27-eldan-open-targets.tex:121` are unrestricted.
  The certification may be wired **only together with** a statement amendment (ledger and
  manuscript in the same edit) adding the regular-class restriction and the approximant
  remark; otherwise the node stays `open` and the review is not to be used as active
  certification.
- **Edge-set flag (task item 9, not a defect).** The actual proof matches the dossier
  header's edges `[prop:stein-rep, lem:stein-vs-source, lem:block, cor:per-direction,
  thm:scalar-riccati, lem:lyapunov-stein-duality, prop:products]` plus
  `lem:perimeter-martingale` (measurability construction), with
  `lem:survival-implies-kls` consumed by the auxiliary lemma only. The ledger's current
  `depends_on` lists `thm:budget` (not invoked as a statement; its balance hypothesis is
  unavailable and part (i) is reproduced from primitives) and `prop:trivial-excess`
  (unused).
- **Provenance blemish outside my scope.** The 2026-08-27 product-covariance review
  declares a SHA that does not match the committed dossier bytes, and that dossier
  retains a stale "unreviewed repair" scope sentence; consistent with post-review header
  wiring. All product-dossier facts used here were re-verified against current bytes.
  Janitor-level reconciliation suggested.
- Non-blocking editorial items in the dossier header (stale "no manuscript label yet"
  note; empty reviewer/review fields) to be fixed at wiring.

## Dead ends

None mathematical: every step of the main proof and the auxiliary lemma verified on
first reconstruction. The one deliberation was whether the statement-scope caveat forces
an `audit` instead of a pass; precedent (the 2026-08-27 weighted-spectator repair review,
which passed with proposed ledger statement text) supports a pass whose delta makes the
statement alignment part of the same atomic ledger edit, and the report's scope section
makes the restriction explicit and machine-visible.

```yaml
outcome: complete
artifacts:
  - research/reviews/2026-08-30-prop-split-screened-supply-proof-review.md
  - research/explorations/2026-08-30-proof-checker-split-screened-supply-w4r01.md
proposed_deltas:
  - "Atomically, for prop:split-screened-supply in research/kls/ledger.yaml: amend statement to: 'For a product of isotropic one-dimensional log-concave laws in the compact-smooth product-preserving regular class, a J-measurable cut with C^2 relative boundary, |J|=k and 0<p_0<1, every eta in (0,1/4], kappa>0, and every T>0, the screened weighted excess satisfies E int_0^{T wedge tau_eta} e_t (1+lambda_cut(A_t,K_t))^(5/2) 1{Q_t >= kappa e_t W_cut} dt <= (2k+64 eta^2 (1+k))/kappa, uniformly in the ambient dimension and in every spectator coordinate. Total-budget form, not proportional to T. General split laws and cuts are covered only in the defined-on-approximants convention; the screened-indicator limit interchange is open.'; set depends_on: [prop:stein-rep, lem:stein-vs-source, lem:block, cor:per-direction, thm:scalar-riccati, lem:lyapunov-stein-duality, prop:products, lem:perimeter-martingale]; keep bounded_by: [obs:two-tail, obs:circularity]; set solution: solutions/prop-split-screened-supply.tex, checked_by: agent, review: research/reviews/2026-08-30-prop-split-screened-supply-proof-review.md, status: proved."
  - "In the same change set, amend the manuscript proposition at modules/kls/27-eldan-open-targets.tex \\label{prop:split-screened-supply} to carry the same regular-class restriction and an approximant sentence for the general split class."
  - "Update the dossier header of solutions/prop-split-screened-supply.tex at wiring: reviewer proof-checker-w4r01, review path above, refresh the stale 'no manuscript label yet' note. If the statement amendment is declined, wire nothing and keep the node open."
  - "Optional janitor item: reconcile the SHA declared in research/reviews/2026-08-27-kls-product-covariance-proof-review.md with the committed bytes of solutions/kls-product-covariance.tex and its stale 'unreviewed repair' scope sentence."
next_role: orchestrator
next_prompt: |
  The cold review of solutions/prop-split-screened-supply.tex passed:
  research/reviews/2026-08-30-prop-split-screened-supply-proof-review.md (reviewer
  proof-checker-w4r01, author prover-w4p01). Apply the proposed deltas above atomically:
  the certification is valid only for the regular-class (M2) statement, so the ledger
  statement of prop:split-screened-supply and the manuscript proposition at
  modules/kls/27-eldan-open-targets.tex:121 must be amended to carry the regular-class
  restriction (and the approximant remark for general split laws) in the same edit that
  sets solution/checked_by/review/status. Also correct depends_on to the verified edge
  set (drop thm:budget and prop:trivial-excess; add prop:stein-rep, cor:per-direction,
  prop:products, lem:perimeter-martingale). Run python3 research/check_ledger.py after
  the edit. If you decline the statement amendment, wire nothing: the node stays open and
  the review must not be referenced as its active certification. The auxiliary lemma in
  the dossier certifies a conditional implication only and adds no node. The janitor
  reconciliation of the product-covariance review SHA is optional housekeeping.
```
