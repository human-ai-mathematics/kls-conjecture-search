---
---

# Song–Zhang v2 reconstructed and independently checked

## Question examined

Complete `ap:sz-v2-reconstruction`: reconstruct the source chain leading to
[](#thm:sz-v2-kls) and register a separate proof of [](#conj:kls), preserving
the BKL proof and the version-pinned SZ v1 record.

## What we learned

**Established and independently reviewed.** Twelve new dossiers reconstruct
the common coefficient radius, improved inner iteration, dimension bound,
fixed-cost repeated height reduction, finite chains retaining earlier caps,
near-unit refinement, summable budgets, universal Poincaré bound, and the
composition with the canonical target. The new layer has twenty-three
proved claims and two definitions. Independent agent reviews, distinct from
journal refereeing or human acceptance, cover the exact local statements.
The source remains Song–Zhang arXiv:2610.01447v2, not a new author or an
original proof discovered in this project.

The main certification sequence is:

- `research/reviews/2026-10-06-sz-v2-radius-review.md`;
- `research/reviews/2026-10-06-sz-v2-foundations-review.md`;
- `research/reviews/2026-10-06-sz-v2-inner-review.md`;
- `research/reviews/2026-10-06-sz-v2-blocks-review.md`;
- `research/reviews/2026-10-06-sz-v2-height-review.md`;
- `research/reviews/2026-10-06-sz-v2-profile-review.md`;
- `research/reviews/2026-10-06-sz-v2-kls-composition-review.md`.

The last profile review covers both the analytic estimates and their scalar
interfaces. It does not infer a proof from convergence of a product alone.
In particular, the actual finite family, retained coefficient caps,
admissible starting depths, coefficient return, and the order of universal
and measure-dependent choices were checked. Local transcription corrections
included the restriction $z\leq R$ in the raw local frame, exact alignment
of two integer ceilings, and explicit scalar dependencies for the final
composition. These corrections were independently reread before passing.

**Established provenance.** The dependency closure of [](#thm:sz-v2-kls)
contains no BKL node, no [](#conj:kls), and no open claim. Common earlier
analytic and polynomial results remain inputs. In particular, the final
reconstruction reuses the certified fixed-depth profile
[](#thm:sz-iterated-curvature) inside the mesoscopic estimates. This is a
broader reuse than the initial integration checkpoint's phrase “Historical
v1 baseline only”; the interface was checked in the inner review. That
fixed-depth input does not supply the new polynomial cost in depth.
The original planning checkpoint is preserved.

The unchanged [](#conj:kls) now has two proof records and both source
references. The repository's dependency graph takes the union of their
premises; it does not itself encode independence between proofs. Each
composition dossier and review instead identifies its actual inputs. The
BKL composition was checked again in full within that scope in
`research/reviews/2026-10-06-bkl-kls-second-proof-review.md`. It does not use
the new SZ theorem. Its old dossier and review remain unchanged; only the
review pointer for the KLS record was updated to cover the final dependency
union. The SZ adapter uses the new Poincaré theorem and the established
Cheeger comparison, without BKL.

**Established bibliographic distinction.** `SongZhang2026IteratedLogKLS`
continues to mean v1, and `SongZhang2026ConstantKLS` means v2. The submission
chronology and same authorship are recorded in [](#sec:sz-v2-proof). The two
source proofs have distinct closing mechanisms and share earlier spectral
foundations. Submission order is not a claim about discovery order.

**Established methodological limit.** The earlier Wave A contract correctly
separated summable-loss algebra from the missing estimates. The new proof
iterates a common radius and pays the fixed Poincaré comparison once. It
therefore does not literally establish every replacement estimate requested
by that older contract. The exact comparison is recorded in
`2026-10-06-sz-v2-contract-comparison.md`. Neither the coefficient equivalence
nor the old algebra supplied the new finite-block construction or the BKL
cumulant/suspension mechanism. No priority is claimed.

## What resists

The import objective is accomplished. This says nothing further about the
sharp CMH inequality, universal occupation estimates, adaptive trace bounds,
or all-frame fiber constructions. Their sufficient conditions cannot be
recovered by reversing implications into KLS.

The precise correspondence with the earlier startup denominator and moving
degree range remains a separate comparison problem. In particular,
`ap:sz-conditional-initialization` and `ap:sz-recovery-probe` retain their
existing states and their sharpened interface-comparison tests. The BKL
initialization consequence remains available with its own provenance, not
as an input to the independently reconstructed SZ proof.

## Proposed next step

Close `ap:sz-v2-reconstruction` as accomplished, not abandoned or refuted.
Retain every pre-existing research route's state and recorded obstruction.
Read the two source mechanisms side by side through [](#sec:sz-v2-proof)
and [](#sec:bkl-proof), and pursue any further comparison through its exact
statement and dependencies. Publication of the manuscript remains a human
act; this integration does not deploy the site.
