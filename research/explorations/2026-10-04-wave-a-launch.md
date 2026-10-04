---
---

# Wave A: assignments and corrected decision gates

## Question examined

Launch the priorities proposed in
[the strategy checkpoint](2026-10-04-strategy-after-song-zhang.md), with the user's
authorization on 2026-10-04. Four researcher missions and one fresh reviewer examine
the Song–Zhang contract, CMH perturbations, product-base cones, conditional fibers,
and `lem:survival-implies-kls`. This record corrects the scope of the earlier decision
gates; it does not assert a new mathematical result.

## What we learned

*Observed (repository state).* The portfolio at launch contains ten active routes,
six blocked routes and six closed routes, counting sub-routes. Priority ordering
reduces concurrent work, not the number of entries marked active to seven.

*Established (logical scope, not a new certified claim).* The missions use these
decision gates:

1. `ap:sz-induction-contract`, **mine**, then **construct**: write the complete
   quantified induction contract and trace each depth-dependent threshold to the
   step that requires it. State the replacement estimates needed for bounded
   profiles. Failure with unchanged thresholds is an applicability obstruction
   for that proof, not impossibility for every improvement that also changes the
   thresholds. A compatible proposed contract is not a proof of its estimates.
2. `ap:c-solenoidal-perturbation`, **refute**: first establish admissibility of the
   proposed family, including both parameter signs and approximation conventions.
   Then examine the full quotient at degrees one through four. For
   $Q_d(\varepsilon)=4-\delta_d+a_d\varepsilon^2+\rho_d(\varepsilon)$,
   a positive coefficient is insufficient: a witness must satisfy
   $a_d\varepsilon^2+\rho_d(\varepsilon)>\delta_d$ at an admissible parameter,
   or a uniform argument must justify a joint degree/parameter limit.
3. `ap:c-gate-zero`, **prove**: decide the algebraic product-base cone candidate
   `cand:cone-transverse-equality-simplex` uniformly in its parameters. Separate a
   proof, additional equality cases, and violation of the sharp bound two.
   A violation of two alone does not refute `conj:gate-zero` at four.
4. `ap:f-simplex-dual`, **construct**: first specify and justify the exact all-frame
   min–max problem, then seek certified values or rigorous brackets for
   $\Lambda_{m,3}$, $3\le m\le8$. Retain the predeclared directional criterion
   (monotone decrease by a factor at least three and final value below $0.1$).
   A seeded optimization is not a certificate of global optimality; values for
   finitely many dimensions imply neither asymptotic decay nor a degree-four
   necessity if they do not decrease.
5. `lem:survival-implies-kls`, **certify**, fresh reviewer context: reconstruct
   posterior isoperimetry, perimeter expectation, balanced-cut reduction and
   all regularization/limit steps from the proof and actual sources. Earlier
   certification supplies provenance, not an argument to defer to.

*Observed (execution).* The Song–Zhang researcher, CMH researcher and independent
survival reviewer were launched first. The cone and fiber researchers follow as
slots become available. Every agent reads the repository contract and its role;
each owns a distinct new record. Shared program files remain the orchestrator's.

## What resists

No mission is promised a proof or refutation. An exact obstruction, a useful
reduction, or a precise unclosed step is a valid outcome. Research findings remain
uncertified until the independent review channel is completed. The recovery probe
and the occupation comparison are not part of these five initial assignments.

## Proposed next step

Complete all five assignments, integrate their exact handoffs, and record a wave
synthesis with updated route tests. If a review finds a defect, preserve its report
and send every defect to a researcher for repair before a fresh re-review. Use the
full checker before any status transition, and the writer workflow if a manuscript
milestone is reached. Preserve earlier checkpoints unchanged.
