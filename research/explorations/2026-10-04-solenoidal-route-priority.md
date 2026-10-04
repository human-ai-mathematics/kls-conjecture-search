---
---

# The solenoidal perturbation route moves to priority 3

<!-- Orchestrator checkpoint. Changes a route's priority only; its state, its `next` and every status are unchanged. -->

## Question examined

Should `ap:c-solenoidal-perturbation` stay among the priority-2 tests of the
[strategy checkpoint](2026-10-04-strategy-after-song-zhang.md)? It was placed there as
a cheap way to refute $\mathrm{CMH}(4)$, and through it the moment-map approach.

## What we learned

*Judgment (orchestrator), on the two calibrations so far; no new mathematics.*

- In [Wave A](2026-10-04-wave-a-cmh-variation.md), the planned two-sided target-linear
  perturbations turned out to be affine tilts with zero second variation: the test was
  ill-posed and gave no signal.
- The [even radial retest](2026-10-04-cmh-even-radial-retest.md) on
  $\beta=2+\varepsilon^2$ found strictly negative optimized variations at degrees one
  through four. This is uncertified, and it gives no signal against $\mathrm{CMH}(4)$.
- The route's `next` now first asks to resolve admissibility for a source-linear
  perturbation in `conj:cmh-second-variation`. That is a third attempt, and admissibility
  must be settled before any computation. It is no longer a cheap discriminating test.

## What resists

Two negative calibrations are weak evidence, not a certification. They leave
`conj:cmh-second-variation` and $\mathrm{CMH}(4)$ open. Lowering the priority closes
nothing, and the route stays `active` with its `next`.

## Proposed next step

Keep `ap:c-gate-zero` and `ap:f-simplex-dual` as priority 2. Run
`ap:c-solenoidal-perturbation` with the other priority-3 routes, after the Song–Zhang
priority `ap:sz-conditional-initialization`.
