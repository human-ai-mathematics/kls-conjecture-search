---
---

# Song–Zhang v2: fixed-cost height blocks reconstructed

## Question examined

Complete the Section 8 reconstruction on `ap:sz-v2-reconstruction`, targeting
`prop:sz-v2-height-reduction`, after the common-radius interface was reviewed.
The starting lens is prove. The independent raw-frame interfaces are
`lem:sz-v2-raw-joint-frame` and `lem:sz-v2-propagated-joint-loss`.

## What we learned

- *Established, not certified:* `solutions/sz-v2-joint-loss.md` reconstructs
  the raw joint frame, its local and polynomial-envelope variants, and the
  normalized delayed-loss estimate. It uses the joint partial
  symmetrization theorem, the operator/hierarchy primitives, and exact
  Appell testing. It assumes its stated power envelopes and normalizer
  bounds; it does not construct them.
- *Established, not certified:* `solutions/sz-v2-height-blocks.md` constructs
  the fixed-cost blocks at every finite odd order, then proves the complete
  profile and the repeated-height assertion of
  `prop:sz-v2-height-reduction`. The proof uses a larger fixed radius floor
  than the source's near-unit construction. This is sufficient for Section
  8, whose constants may have a fixed multiplicative loss. It makes successive
  lengths grow by at least a fixed factor and permits the separately
  reconstructed greedy propagation lemma.
- *Established, not certified:* the order of construction is explicit.
  Previously constructed blocks provide the envelope needed for extension;
  the new radius is first kept above its floor; its exact block norm and
  earlier decrements give the next envelope; only then is the local Green
  argument used to initialize its actual family. Its matched energy budget
  comes from the decreasing sliding-window masses, not from a substitution
  in the generic restricted-radius budget.
- *Established, not certified:* the longer retained prefix, static
  coefficient remainder, and logarithmic-distortion burn-in are all checked
  before the depth recurrence. The original seed caps every improved seed,
  keeping constants independent of the outer height stage. The final cost
  still grows with the number of stages and proves no uniform KLS bound.
- *Review repair:* the independent block reviewer identified that the local
  raw-frame variant needed the explicit restriction $z\le R$. Without it,
  replacing a shorter propagation power by the longest power can reverse
  the inequality. The statement and proof in the joint-loss dossier now
  impose $0<z\le R$. All height-block uses have
  $z=\|\mathcal T^m\|^{2/m}\le R$ and are within that restriction.

## What resists

No analytic step is left marked as a gap in the completed height-block
draft. Its correctness and the exact canonical implication still require
independent review. This checkpoint records a completed argument, not a
certification. The separate near-unit-floor construction and retained-chain
estimates required in Section 9 are outside this fixed-cost theorem.

## Proposed next step

Review `prop:sz-v2-height-reduction` against
`solutions/sz-v2-height-blocks.md` with cold context. Check especially the
finite-radius induction, the initial coherent smallness estimates, the
power-envelope chronology, the remainder coefficient bound, and the
stage-independent starting depths.

The theorem uses `def:sz-v2-common-radius`, `def:sz-v2-height-profiles`,
`thm:sz-v2-iterated-curvature`,
`prop:sz-v2-static-coefficient-transfer`, `prop:sz-v2-common-radius`,
`lem:sz-v2-operator-block-primitives`, `lem:sz-v2-normalized-hierarchy`,
`lem:sz-v2-mesoscopic-powers`, `lem:sz-v2-raw-joint-frame`,
`lem:sz-v2-propagated-joint-loss`, `lem:sz-v2-orbit-green-restart`,
`lem:sz-v2-block-extension`, and `lem:sz-v2-block-propagation`.
The generic Green/restart and extension nodes have their own independent
proofs and do not depend on any small-loss or height profile; this avoids a
cycle with the later Section 9 reconstruction.

There are no new `bounded_by` edges. No BKL theorem, consequence of BKL,
or KLS theorem is an input. The brief's coefficient-equivalence and uniform
admissibility warnings are addressed by keeping the finite radius,
all-degree coefficient premise, actual block family, and depth threshold
distinct. There is no applicable proved-status delta before review.

The full repository check and whitespace check completed successfully
after the dossiers and canonical interfaces were integrated. These checks
validate structure and rendering, not the proof.
