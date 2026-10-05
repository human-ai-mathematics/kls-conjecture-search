---
---

# Conditional implications: finiteness before Carleson absorption

## Question examined

Starting from the mine lens, examine the four fixed-cut implications that
were still open for lack of a dossier, then write their proofs after authorization.
The nodes are `thm:centroid-implies-kls`, `thm:carleson-implies-centroid`,
`thm:intro-all-cut`, and `thm:intro-weighted`. No portfolio route is changed;
this is certification preparation for the existing fixed-cut architecture.

## What we learned

*Established, not certified.* The all-cut assumption concerns deterministic
intervals intersected with its specified exit time. Applying it after adding
an arbitrary localizing stop is not justified. Instead, tracing
`cor:per-direction` gives a finite total source budget for each fixed
dimension. Localize the scalar Riccati identity, take expectations, and use
Fatou for the nonnegative terminal and damping terms and monotone convergence
for the source. This proves finiteness before the all-cut assumption is
invoked. Its deterministic prefixes then give the desired universal Gronwall
bound. This argument is written in `solutions/thm-carleson-implies-centroid.md`.

*Established, not certified.* The stopped-centroid implication is a bounded
mass-martingale maximal estimate followed by `lem:survival-implies-kls`.
The all-cut-to-KLS implication follows directly from the existing certified
`cor:tight-window-consumption`, at the coarse-window endpoint. Both are
written in `solutions/thm-centroid-implies-kls.md`.

*Established, not certified, subject to a positive horizon.* The weighted
package gives the tight-window source premise by its Stein conversion and
error bound on near-minimizing half-mass cuts. Its absorption margin already
places its fixed window inside the allowed range. This is written in
`solutions/thm-intro-weighted.md`; the proof does not use the package's
refutation to obtain a vacuous implication.

*Observed from the text.* The existing localization-core dossier's
tight-window consumption proof invokes localization and Fatou without
displaying the finiteness step before absorption. The argument above provides
a way to make that step explicit. This observation does not itself change
the existing certification or certify a repair.

## What resists

No Carleson or centroid antecedent is discharged. The weighted antecedent is
recorded as refuted. Its literal wording must require a positive horizon
before the constructive dossier can match the intended implication. Changing
that wording changes a fingerprint of its existing refutation and therefore
requires an independent review of the affected certification. All new
dossiers require independent review before any status transition.

## Proposed next step

Stabilize the positive-horizon wording and proof-dependency metadata. Review
the new dossiers independently, concentrating on the order of localization,
finiteness, and absorption, and check that only the stated deterministic
Carleson premise is consumed. Separately examine the corresponding
finiteness justification in the already certified tight-window dossier.
