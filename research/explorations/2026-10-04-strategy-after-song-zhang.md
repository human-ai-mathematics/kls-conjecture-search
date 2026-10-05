---
---

# Strategy after Song–Zhang: one main line, decisive tests, the rest on hold

<!-- Orchestrator checkpoint. Decisions on routes only; no node, statement or status changes. -->

## Question examined

How should the search for `conj:kls` spend its next agent calls, now that
`thm:song-zhang-kls` is certified and every route has a `next` test
([the triage checkpoint](2026-10-04-portfolio-triage-after-song-zhang.md))? Eleven routes
were active at once. The manuscript names the loss of the polynomial–curvature iteration
as the most immediate question (`subsec:atlas-assessment`, `subsec:synthesis-assessment`),
yet the portfolio carried it only as the unadmitted probe `ap:sz-recovery-probe`.

## What we learned

*Judgment (orchestrator), on the records below; no new mathematics.*

1. **The portfolio followed the history of the search, not its priorities.** Six open
   routes served the moment map and one the fixed eigenfunction, which the atlas calls the
   best structurally motivated. Several routes cannot move before a test elsewhere is
   decided: by its own `next`, `ap:c-recovery-envelope` reduces to `conj:gate-zero` at its
   linear stage, and so does `ap:c-anisotropic-bootstrap`.
2. **The Song–Zhang line gets a route, but not as a fifth approach.** The admission
   criteria of [the zoom-recovery checkpoint](2026-10-03-sz-zoom-recovery.md) — a precise
   intermediate estimate, a mechanism, a comparison with the obstructions, a discriminating
   test — are not met. What is missing first is the precise estimate, and
   [the audit-targets checkpoint](2026-10-03-song-zhang-audit-targets.md) says how to get
   it: write the complete induction contract and ask whether a bounded profile constant
   can meet its thresholds at every depth. That is the objective of the new route
   `ap:sz-induction-contract`. Either outcome is a result: an incompatibility is an
   obstruction for every bounded-multiplier improvement of this proof; a compatible
   contract is the estimate admission requires. `ap:sz-recovery-probe` becomes its
   sub-route.
3. **Each approach has a test that can close it or relaunch it, and none has run.**
   - Moment map: `ap:c-solenoidal-perturbation` (a stable positive second variation is a
     candidate refutation of `conj:cmh-second-variation`, hence of CMH(4), which would
     close every C route) and `ap:c-gate-zero` (`cand:cone-transverse-equality-simplex` by
     exact algebra).
   - Conditional fibers: `ap:f-simplex-dual` (exact $\Lambda_{m,3}$, preregistered decay
     criterion).
   - Fixed cut: not a route but a review. Its bridge `lem:survival-implies-kls` rests on
     `research/reviews/2026-08-25-kls-core-r2-audit.md`, whose author
     (`kls_core_author`) and reviewer (`kls_bootstrap_author`) certified each other's
     work the same day (see also `2026-08-25-kls-excess-bootstrap-r2-audit.md`). Before
     more effort goes into the E routes, a fresh `reviewer` should certify the bridge
     again. This questions the independence of that review, not the mathematics.

## What resists

The order of priority is a judgment on motivation and cost, not on difficulty. No route is
closed by this checkpoint, and nothing here says that a priority-3 route is less likely to
succeed. The portfolio has no priority field: the order of its entries and their section
comments carry it.

## Proposed next step

The portfolio now reads, in order:

- **Priority 1:** `ap:sz-induction-contract`, then its sub-route `ap:sz-recovery-probe`.
- **Priority 2:** `ap:c-solenoidal-perturbation`, `ap:c-gate-zero`, `ap:f-simplex-dual`,
  and the review of `lem:survival-implies-kls`.
- **Priority 3, still active:** `ap:s-occupation` (its `next` adds a comparison of
  `thm:sz-curvature-comparison` with the stochastic source, once the contract exists),
  `ap:e-trace-upgrade`, `ap:e-screened-supply`, `ap:e-taming-splitting`,
  `ap:f-frame-construction`.
- **Blocked:** `ap:c-recovery-envelope` and `ap:c-anisotropic-bootstrap` on
  `conj:gate-zero` (a refutation of `conj:gate-zero` would close them, not reopen them),
  together with the routes already blocked.

Launch priorities 1 and 2 as one wave: four `researcher` missions and one fresh `reviewer`.
Then write a synthesis checkpoint, close or promote routes on what the wave decides, and
launch a `writer` only if a status changes.
