---
---

# BK: certified compatible integration and third KLS proof

## Question examined

Complete `ap:bk-reconstruction`: reconstruct the pinned BK source, certify its
explicit constant, compose it into `conj:kls`, and preserve the two existing
proofs and the independent objectives of the alternative mechanisms.

## What we learned

*Established and independently certified.* Twelve source assertions now have
passing reviews, with two definitions recording compatible tensor calculus and
the uniform Appell convention. The nine dossiers cover approximation, Hodge,
integration, powers, localization and moving variance, reverse transfer, degree
induction, the scalar bounds, and the final composition. The source version
and PDF SHA-256 are recorded in `2026-10-06-bk-integration.md`.

The certificates are:

- `2026-10-06-bk-operators-review.md`: `lem:bk-compatible-hodge`,
  `prop:bk-integration-calculus`, `lem:bk-uniform-power-bound`,
  `cor:bk-integration-powers`, `cor:bk-quadratic-seed`.
- `2026-10-06-bk-localization-review.md`: `lem:bk-regular-approximation`,
  `lem:bk-localization-covariance`, `lem:bk-moving-appell-variance`,
  `prop:bk-reverse-transfer`.
- `2026-10-06-bk-outer-review.md`: `thm:bk-appell-bound`,
  `thm:bk-explicit-poincare`, `cor:bk-cheeger`.
- `2026-10-06-bk-kls-composition-review.md`: a third proof record on `conj:kls`.

All reports are under `research/reviews/`. The outer and input-status editorial
notes preserve the certifications after removing obsolete draft-status prose.
The reviewers verified the pre-edit normalized hashes rather than changing
old reports. No mathematical repair was required by the proof reviews.

The quantitative conclusion is $C_P\le1+2\cdot10^{16}$. The inverse Cheeger
bound is $\sqrt{\pi(1+2\cdot10^{16})}$ in the existing normalization; the
numerical comparison is attributed to the published Klartag equation, with
Milman supplying the underlying equivalence. The older exponential criterion
also gives a qualitative consequence, but does not supply this BK constant.

*Established by separate review.* Adding `thm:bk-explicit-poincare` to the
collective dependency list of `conj:kls` required extending the two previous
composition certifications. `2026-10-06-kls-proof-dependency-extension-review.md`
verified their historical baseline and unchanged actual premises. Their
proof records now name that report; earlier reports remain unmodified.
Neither old proof uses BK, and BK uses neither old KLS proof nor its conclusion.
The shared Letwin/Appell inputs remain explicitly attributed.

*Observed.* The complete checker passed after registering all three proof
records and the extension review: 192 nodes, including 162 proved, 9 defined,
19 open and 2 refuted. Comparing statement snapshots before and after the first
writer pass preserved all 178 preexisting statements. The sole later precision
in a new statement specified fixed degree, leading tensor and derivative order
in `lem:bk-regular-approximation` before its certification.

*Decision.* Close the accomplished reconstruction route. Keep all existing
alternative routes in their previous states. Insert `sec:bk-proof` after the
SZ v2 technical chapter and before `sec:kls-synthesis`; shift subsequent chapter
numbers while preserving stable labels. The final writer pass and sync audit
will align the public prose with the completed certifications.

*Methodological assessment.* The search had identified the exponential end
point, but had not discovered this way of attaining it. Existing CMH work
already used Hodge decomposition; the new mechanism is the compatible-tensor
estimate uniform in rank, coupled to one prefactor for all integration powers
and a direct degree induction. No priority claim follows from this reconstruction.

## What resists

This certifies a reconstruction through independent agent reviews, not journal
refereeing. No implication settling CMH, eigenfunction occupation or the
conditional-fiber mechanism has been proved here. The large explicit constant
is not an optimality claim. The source's radial blog example was not used as
proof evidence, and no claim is made about sessions outside the visible agent
tree or about first public availability of the preprint.

## Proposed next step

Finish the verdict-driven prose pass and independent sync audit. Human reading
of the BK chapter, comparison and final composition remains necessary before
manual publication. No publication or merge is performed in this integration.
