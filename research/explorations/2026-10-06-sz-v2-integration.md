---
---

# Song–Zhang v2: reconstruction scope and versioned interfaces

## Question examined

Route `ap:sz-v2-reconstruction`: reconstruct and independently check the second
Song–Zhang version as a separate proof of [](#conj:kls), without using the BKL
proof or consequences of the already established target.

## What we learned

**Observed in the version histories.** Song–Zhang v1 was submitted on
1 October 2026 at 10:43:04 UTC. BKL v1 was submitted on 4 October at
19:30:34 UTC; Song–Zhang v2 followed at 21:21:03 UTC. The latter is a
140-page revision by the same authors, entitled *An O(1) Bound for the KLS
Constant*. Submission order does not establish discovery order.

Sources: [SZ history](https://arxiv.org/abs/2610.01447v2),
[BKL history](https://arxiv.org/abs/2610.05474v1),
[SZ v2 text](https://arxiv.org/html/2610.01447v2).

**Established organizational decision.** Preserve `SongZhang2026IteratedLogKLS`
and every v1 dossier and review; cite v2 as `SongZhang2026ConstantKLS`.
Six new reconstruction blocks cover Section 6, Section 7, Section 8,
Section 9 small-loss refinement, its finite-chain budget closure, and its
universal conclusion. A new preprint citation does not certify any block.

| Existing interface | Intended reuse | Required check |
| --- | --- | --- |
| `lem:sz-analytic-foundations` | Regular operators and approximation | Domains, covariance normalization, limiting class |
| `thm:sz-polynomial-variance` | Initial Appell bounds | Ordered-index norm and factorial convention |
| `thm:sz-curvature-comparison` | Polynomial-to-spectral comparison | Exact radius and degree admissibility |
| `thm:sz-curvature-transfer` | Section 7 dimension bound | Universal profile and admissible curvature |
| `thm:sz-iterated-curvature` | Historical v1 baseline only | Does not supply the new polynomial depth cost |

**Established exclusion.** No new SZ proof may use `conj:kls`, a BKL node,
or a consequence proved using either. Acyclicity alone does not establish
this independence; authors and reviewers must identify the actual inputs.
Shared older analytic and polynomial results are permitted after interface checks.

## What resists

The v1 certification does not cover the new blocks of Section 6 or the
common-radius and finite-chain arguments in Sections 8–9. The summability
calculation in the 4 October Wave A checkpoint proves neither of its missing
analytic replacement estimates. Exact correspondence with v2 remains to be
established. No priority claim follows from this correspondence.

## Proposed next step

Write the six dossiers with explicit interfaces, reconstruct the source estimates,
and submit stable blocks to fresh independent reviewers. Keep new results
uncertified until those reviews pass. If an estimate cannot be justified,
record the exact obstruction rather than replacing it with a citation or with
the known BKL conclusion. Reassess the two continuing SZ routes only against
their exact objectives; retain the other research routes and all historical records.
