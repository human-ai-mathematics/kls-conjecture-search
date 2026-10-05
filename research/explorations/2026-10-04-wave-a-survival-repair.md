---
---

# Wave A standalone survival repair

## Question examined

Prove lens: repair [](#lem:survival-implies-kls) at its canonical arbitrary
measurable-set scope, retaining all four corrections in
`research/reviews/2026-10-04-wave-a-survival-independent.md`. This is maintenance
of the fixed-cut bridge toward [](#conj:kls), not a new portfolio route.
The shared Riccati dossier is unchanged. The new draft is
`solutions/lem-survival-implies-kls.md`, numbering prefix `126`.

The canonical statement reproduced in the new theorem is:

> Let $\mu$ be isotropic log-concave and $E$ measurable. If, for some $T_0,c_0,b_0>0$,
> $\mathbb P(\min(p_{T_0},q_{T_0})\ge b_0)\ge c_0$,
> then $\mu^+(E)\ge c\,c_0b_0\sqrt{T_0}$. Consequently, if $T_0,c_0,b_0$ are universal and the event holds for every balanced cut of every isotropic log-concave measure, KLS follows.

Here the cut is deterministic, time is positive and finite, and the posterior
is the usual stochastic localization. The universal survival premise remains
an antecedent, not a result supplied by this repair.

## What we learned

*Established, with an argument written out but not certified:* each reported
repair item has an explicit replacement in the standalone proof.

1. Actual lower outer Minkowski content is used throughout. Conditional-law
   realization of localization makes each fixed indicator mass a bounded
   martingale. Nonnegative neighborhood increments and Fatou along a
   deterministic sequence realizing the initial liminf give the perimeter
   expectation inequality. Rational radii prove measurability. Infinite
   initial content is automatic. Completed-measurable sets retain their
   actual neighborhoods, while posterior integrals use Borel representatives.
   No reduced-boundary identification is asserted.
2. A Moreau-envelope and centered-mollifier approximation of an
   extended-valued convex potential retains its quadratic curvature.
   An affine lower bound provides an integrable Gaussian majorant and hence
   total-variation convergence. Pass a bounded-Lipschitz functional inequality
   through that limit, then use distance cutoffs for the actual set. This
   handles arbitrary convex supports and nonsmooth potentials, and is
   applied to each original posterior; the survival event is never
   approximated.
3. The balanced-profile argument explicitly gives $h_\mu\ge2I_\mu(1/2)$.
   Interpolation between an interior epsilon and one half, followed by
   epsilon tending to zero, uses no endpoint continuity in dimension one.
   Borel and completed-measurable profile infima agree by Borel subsets of
   equal mass and inclusion of neighborhoods.
4. The accessible curvature input is Bakry–Ledoux (1996), Corollary 2.2,
   equation (2.10), with the Minkowski convention at (2.11):
   https://www.math.univ-toulouse.fr/~ledoux/LevyGromov.pdf . The profile input
   is Milman (2009), Corollaries 6.12 and 6.5, with Theorem 1.8 and Section 6:
   https://arxiv.org/pdf/0712.4092 . Both PDFs were retrieved and the specified
   passages examined during this repair. The BGL book is not used.

*Established, uncertified scope accounting:* isotropy supplies full
dimensionality and the class for the final KLS consequence. The individual
boundary estimate only uses a full-dimensional log-concave probability with
finite first moment, a deterministic measurable cut, finite positive time,
and the stated event. No extra smoothness, compact support, regular boundary,
occupation estimate, or infinite-time uniform integrability is assumed.

*Observed structural validation:* `uv run scripts/check.py` completed with
exit code zero using the approved escalated execution path, including the
new dossier's MyST build. This is no mathematical certification.

## What resists

The repair supplies an argument for every correction; no unclosed analytic
step has been identified by its author. Its validity at the claimed scope
still requires a fresh independent review. Uniform posterior survival is
not proved, so this repair makes no claim to settle [](#conj:kls).

The node currently has no `depends_on`, `assumes`, or `bounded_by` edges; its
closure and fence list are empty. The proof imports the two established
classical theorems identified above, and otherwise proves its ingredients
inside the new artifact. No ledger, manuscript, or portfolio delta is
applicable on the basis of this uncertified draft.

## Proposed next step

Assign a fresh independent reviewer the new standalone artifact, the canonical
node [](#lem:survival-implies-kls), and the prior revise report. Audit all four
corrections, especially the rational-radius liminf, completed-set convention,
Moreau/mollification domination, functional-to-set limit, and endpoint-free
profile interpolation. Determine whether the artifact proves the canonical
statement without inheriting the shared Riccati dossier's scope.

Author identity for that review: `wave_a_survival_repair, gpt-6-astra,
2026-10-04`. No mathematical edits to the shared core dossier, program,
manuscript, bibliography, or reviews were made by this author.

```yaml
files:
  - solutions/lem-survival-implies-kls.md
  - research/explorations/2026-10-04-wave-a-survival-repair.md
next: |
  Independently review the standalone survival theorem at its full canonical
  scope and all four items in the fresh revise report. The artifact has no
  repository-node proof dependencies, antecedent nodes, or bounded_by fences.
  Its explicit survival premise is retained. Do not register a new proof
  record until the independent review determines the result.
```
