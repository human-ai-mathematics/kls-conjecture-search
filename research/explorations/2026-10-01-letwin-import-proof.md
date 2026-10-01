---
---

# The two Letwin imports: source proof and transfer

## Question examined

Starting lens: mine, then prove to turn the source comparison into a standalone dossier.
The mission concerns `thm:letwin-moment-map` and `thm:letwin-qcts`, two of the seven
preprint imports that were open pending certification. It prepares their certification; it does not pursue or
close a KLS route. Author: researcher_letwin, gpt-6-astra, 2026-10-01.

## What we learned

*Established, not certified.* The dossier `solutions/thm-letwin-imports.md` reconstructs
the regular-target matrix proof and the general quadratic proof from the pinned
[Letwin v1](https://arxiv.org/abs/2607.24164v1). Theorem 2.5 is the matrix source and
Theorem 1.2 the quadratic source. Its proof spells out four transfers: the contravariant
change of the fixed matrix together with the third tensor; source-coordinate cutoffs
that establish integrability before integrating the generator; congruence of the Stein
kernel on a non-isotropic law; and approximation in moments through degree four.

*Established, not certified.* The singular-matrix step requires attention in the local
explanation: `modules/04-family-moment-map.md` applies an orthogonal sign matrix without
first restricting to invertible matrices. The dossier first proves the estimate for
invertible matrices and then adds a positive multiple of the kernel projection and
passes to the limit. This repairs the explanation without changing the theorem.

*Observed from source and repository inspection.* The prescribed regular class is an
isotropic target with bounded open convex support and a convex smooth potential on a
neighborhood of its closure. The existing canonical matrix statement refers to that
class by its source, while the dossier states it explicitly. Published external inputs
are identified individually; their applications include the precise distinction between
regularity of the moment map and the separate bound on its Hessian.

*Established, not certified.* The reconstruction proves no unweighted adaptive estimate.
In particular the fixed-matrix statement does not promote to an operator bound for the
expected squared Hessian. The argument therefore leaves `prop:letwin-not-gate-zero`
and the projection/occupation boundaries intact.

## What resists

Independent certification remains outstanding. The author makes no review verdict.
The source's Theorem 1.1, and specifically the localization/Lichnerowicz extraction of
the improved general KLS exponent, is excluded from this dossier. It is not a missing
premise of either imported statement. The two estimates do not settle `conj:kls`,
`conj:gate-zero`, or any universal-time occupation estimate.

## Proposed next step

A fresh reviewer should read the pinned source, this dossier, the two canonical
statements and their dependency closure. Verify especially the invariant scalar
contractions, the cutoff argument before integration, the convex-domain
Brascamp–Lieb application, the published Barthe–Klartag hypotheses after congruence,
and the two limiting arguments. Check that the canonical source-defined regular class
matches the explicit dossier class. Record only an independent verdict; the author's
reconstruction is no substitute for it. No route or status delta is proposed here.
