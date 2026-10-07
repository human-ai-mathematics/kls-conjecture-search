---
---

# Song–Zhang v2: inner curvature refinement and dimension transfer

## Question examined

Route `ap:sz-v2-reconstruction`, targets `thm:sz-v2-iterated-curvature`
and `thm:sz-v2-dimension-bound`. Starting lens: **prove**. Reconstruct
Sections 6–7 of the pinned v2 source without using BKL or the already
proved KLS endpoint. The question is whether a single amplitude sequence
has squared growth at most a universal constant times $(r+1)^{1/3}$.

## What we learned

**Established, awaiting independent review.** The new foundations dossier
`solutions/sz-v2-inner-foundations.md` writes out the accumulated-covariance
coefficient transfer, joint dyadic partial-symmetrization frame, and skew
normalization credit. The coefficient transfer starts directly at degree
two. Its depth threshold is independent of the amplitude and dimension.
Its premise is a uniform regular coefficient cap, not KLS.

**Established, awaiting independent review.** The operator reconstruction
`solutions/sz-v2-inner-refinement.md` writes out the restricted inverse
operator, compensated restart, mesoscopic powers, averaged startup,
static coefficient radius, delayed loss comparison and amplitude induction.
The main induction is on a radius with $C_P\le Z+2$; the additive two is
paid once after the induction, rather than at every depth. The coefficient
seed can be obtained from the already certified v1 profile at one fixed
depth followed by the new static transfer, avoiding a second proof of the
source's earlier general coefficient-transfer proposition.

**Established, awaiting independent review.** The dimension implication in
`solutions/sz-v2-dimension-bound.md` follows from the exact existing interface
`thm:sz-curvature-transfer`. Its profile hypothesis is satisfied by the
new curvature theorem if that theorem's reconstruction is certified. The
choice of depth is finite and the rescaling constant is independent of
both depth and dimension.

## What resists

No unclosed mathematical step is intentionally hidden in these drafts.
This is an author's account of written arguments, not a correctness verdict.
The long operator and frame arguments need cold independent scrutiny.
In particular, a budget using a block scale $z$ must not silently replace
the restricted operator scale $R$: the unconditional hierarchy bound is
$v_{N+1}\le R e_N$. For a common scale $z\ge R$ its weakened version is
valid; for a mesoscopic block scale $z\le R$ it is not supplied by that
operator inequality. The inner reconstruction retains $R$ in this budget.

No BKL theorem, KLS conclusion, CMH premise or occupation assertion enters
any of these arguments. New foundations and operator interfaces must be
registered and reviewed before downstream proofs rely on them.

## Proposed next step

Independently audit the three foundations, then the operator primitives and
complete inner curvature proof, followed by the dimension implication.
Check the exact canonical interfaces against the dossier statements, the
finite first-exit arguments, the surviving powers of inverse radius in
the coherent/error sums, and the one-time conversion from radius to
Poincaré constant. No applicable proved-status delta is proposed by the
author; all new dossiers remain drafts pending review.
