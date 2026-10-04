---
---

# A route for the conditional initialization of the Song–Zhang iteration

<!-- Orchestrator checkpoint. Admits one route; no node, statement or status changes. -->

## Question examined

After Wave A, which route should carry the Song–Zhang line? The
[contract](2026-10-04-wave-a-sz-contract.md) closed `ap:sz-induction-contract` and
proposed `cand:sz-uniform-conditional-initialization` as the first missing ingredient,
but no active route carried it. Priority 1 was held only by `ap:sz-recovery-probe`, which
calibrates a secondary question: the recovery multiplier.

## What we learned

*Judgment (orchestrator), on the Wave A records; no new mathematics.*

- The contract shows that bounded profiles cannot meet the proof's unchanged thresholds,
  and that the degree-one term of the positive lag majorant already has a growing cost.
  So a smaller recovery multiplier alone cannot give a bounded profile. Low-degree
  initialization conditional on the current curvature profile comes first.
- That is the content of `cand:sz-uniform-conditional-initialization`. The new route
  `ap:sz-conditional-initialization` proves or refutes it over the whole moving range
  $d<\lceil32r^2\rceil$, uniformly in $r$. It then has to combine it with a uniform
  comparison satisfying (R1)–(R2) of the contract. Its `next` is the first test proposed
  in the contract's *Proposed next step*.
- `ap:sz-recovery-probe` becomes its sub-route. It is still useful: once the
  initialization is settled, the multiplier is the next loss to pay.

## What resists

Admitting this route admits no fifth dimension-free approach. The admission criteria of
[the zoom-recovery checkpoint](2026-10-03-sz-zoom-recovery.md) are still unmet: a proof of
the candidate would be the precise intermediate estimate they require, but not yet the
uniform comparison.

## Proposed next step

Launch one `researcher` on `ap:sz-conditional-initialization`, starting from the `prove`
lens and with its `next` as the mission. Report failure of the particular bound tried
as a local obstruction, not as a refutation of the candidate.
