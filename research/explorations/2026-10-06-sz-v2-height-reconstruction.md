---
---

# Song–Zhang v2: the common radius and the remaining block construction

## Question examined

On `ap:sz-v2-reconstruction`, reconstruct Section 8 of the pinned
arXiv:2610.01447v2 without using BKL, `conj:kls`, or a consequence of either.
The first completed proof draft concerns `prop:sz-v2-common-radius`, using
`def:sz-v2-common-radius`, `lem:sz-analytic-foundations`,
`thm:sz-polynomial-variance` and `thm:sz-curvature-comparison`.
The remaining mission is the higher-order block construction and repeated
height reduction of source Propositions 8.21–8.25 and 8.1.

## What we learned

- *Established, not certified:* `solutions/sz-v2-height-reduction.md` gives
  the common-radius argument independently of the new inner iteration.
  Form integration by parts identifies the adjoint Appell testing recurrence;
  exact finite iteration yields the comparison with every finite block.
  Finiteness is pointwise in the regular measure, so there is no assumption
  of a uniform coefficient bound.
- *Established, not certified:* the restricted operator satisfies the exact
  identity $\mathcal T^*\mathcal T=H^{-1}-L^*L$, where
  $Lf=\mathbb E[Xf]$. The covariance hypothesis gives $\|L\|\le1$ and
  hence $C_P-1\le\|\mathcal T\|^2\le C_P$. This is stronger bookkeeping
  than merely knowing the restricted radius is finite.
- *Established, not certified:* the existing v1 curvature comparison covers
  the final conversion $C_P\le2^{85}\mathcal A$ exactly. Fix the measure
  and its positive curvature first, then let the finite dyadic degree tend
  to infinity. This pays the conversion constant once.
- *Observed in the source dependency structure:* source Lemma 8.19 uses
  the new joint partial symmetrization theorem 6.15, not merely the
  two-block recovery already present in the v1 comparison. The higher-order
  startup uses the compensated restart in Lemma 6.6. A source citation to
  either result is not a replacement for its independent reconstruction.
- *Observed in the source dependency structure:* Proposition 8.3 needs the
  generic static coefficient transfer of Proposition 6.27. The inner
  refinement author is reconstructing this as
  `prop:sz-v2-static-coefficient-transfer`, with a coefficient-cap premise
  that does not depend on continuity of the radius assignment.

## What resists

The common-radius dossier does not yet prove the actual high-order starting
family, its retained prefix losses, or the propagation envelope needed by
Proposition 8.22. Nor does it prove Proposition 8.24's full depth induction.
These are unfinished reconstruction tasks, not a discovered gap in the
preprint. The obstruction in the older checkpoint about uniform
admissibility remains relevant until these estimates are reconstructed.

In particular, a product of summable scalar losses does not prove that the
same admissible actual family exists through each required block. A proof
must retain the precise floor, length, order, and energy-budget constraints.

## Proposed next step

Have a fresh reviewer check `prop:sz-v2-common-radius` against its canonical
statement and the dossier, including the tensor normalization, finite output
amplification, covariance hypothesis, and order of the degree limit.
No `bounded_by` node is attached to this interface; the proof asserts no
uniform bound on its radius and uses no target-derived premise.

Continue Section 8 in a separate dossier
`solutions/sz-v2-height-blocks.md` with numbering prefix 143, keeping the
common-radius dossier stable during review. The next exact chain is:

1. Reconstruct the capped-kernel moment estimate of Lemma 8.15 and the
   raw joint frame, using the explicitly reconstructed Theorem 6.15.
2. Prove Lemma 8.19's two-block defect telescope, discrete Green upper and
   lower orbit bounds, and sliding-window loss estimate. The hypothesis
   $\gamma m^2/z\le c_0$ must precede any uniform orbit bound.
3. Construct the single averaged starting family in Lemma 8.20, then extend
   it via Lemma 8.16 and the finite odd-order induction of Proposition 8.21.
   Check the next radius remains above its floor before using the geometric
   decrement estimate. Preserve the original full-family normalizers.
4. Prove Proposition 8.22 with its longer retained prefix, then the
   logarithmic-distortion lemma and Proposition 8.24. Only after that may
   the original seed and capped improved seeds yield Propositions 8.25/8.1.

The first full repository check was run while the orchestrator was adding
the new manuscript anchors; it failed on those temporarily unresolved new
anchors, not on the common-radius proof syntax. Repeat after integration.
