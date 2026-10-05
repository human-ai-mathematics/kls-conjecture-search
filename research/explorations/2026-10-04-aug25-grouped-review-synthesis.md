---
---

# August-25 grouped review: seventeen refreshed certifications

## Question examined

Complete the user's requested fresh grouped review of the three August-25
core dossiers, motivated by the previously repaired survival gap. The precise
[launch scope](2026-10-04-aug25-grouped-review-launch.md) contains seventeen
current consumers: sixteen still used the two August-25 reports, while
`thm:bootstrap` used a later report on the same bootstrap dossier.

The user also requested a correctly admissible retest of
`ap:c-solenoidal-perturbation` on the even radial path. That parallel mission
has its own [checkpoint](2026-10-04-cmh-even-radial-retest.md), script and
provenance-bearing output.

## What we learned

### Independent grouped review and repair

*Established by independent certification.* The first fresh reviewer read
all three dossiers and all seventeen canonical interfaces, without retaining
the old cross-review conclusions. It issued:

- [Pass](../reviews/2026-10-04-aug25-grouped-pass.md) for the five current
  consumers of `solutions/kls-qcts-stein-boundary-core.md`:
  `prop:qcts-equivalence`, `prop:stein-rep`, `lem:stein-vs-source`,
  `lem:boundary-rep`, and `prop:two-tail`.
- [Revise](../reviews/2026-10-04-aug25-grouped-revise.md) for the Riccati
  and bootstrap dossiers, with localized repairs rather than a claim that
  their twelve conclusions were false.

The repairs, written by a separate researcher and documented in
[the repair checkpoint](2026-10-04-aug25-grouped-repair.md), were:

1. Before tight-window absorption, use the per-direction budget to establish
   finite source, terminal and dissipation integrals. Remove auxiliary local
   stops before applying the deterministic-prefix Carleson premise.
2. Remove the obsolete shared survival proof and its incorrect general
   reduced-boundary justification. The shared dossier now owns six claims
   and explicitly consumes the independently certified standalone survival
   bridge; its local identities use the original posterior and moment stops.
3. Replace the false assertion that every log-concave isoperimetric profile
   tends to zero at the left endpoint. Interior concavity and nonnegativity
   prove `lem:half` without endpoint continuity, including in dimension one.
4. Preserve the ceiling's quantitative all-measure sufficient implication
   while delimiting its discussion of the particular bootstrap upper
   certificate. No converse or general propagation impossibility is claimed.

A second fresh-context reviewer independently examined both repaired dossiers
and all twelve current consumers. Its
[grouped pass](../reviews/2026-10-04-aug25-repaired-review.md) covers:

| Dossier | Certified current nodes |
|---|---|
| `solutions/kls-localization-riccati-core.md` | `lem:matrix-riccati`, `thm:scalar-riccati`, `cor:per-direction`, `cor:tight-window-consumption`, `lem:pathwise-BL`, `cor:away-from-zero` |
| `solutions/kls-bootstrap-interface.md` | `lem:half`, `lem:whitening`, `thm:bootstrap`, `lem:crude`, `cor:loglog`, `prop:ceiling` |

The ledger now points all seventeen consumers to these two new passing
reports. Their statuses remain `proved`. Two dependency edges were added to
record actual proof use: `cor:tight-window-consumption` uses
`cor:per-direction`, and the certificate discussion in `prop:ceiling` uses
`thm:bootstrap`. All historical reviews, including the fresh revise, remain
unchanged. No canonical statement was weakened or refuted.

### What the ceiling actually says

*Established by the review.* `prop:ceiling` proves that an all-measure bound
on the covariance interface at a sufficiently small universal time implies
KLS. It does not prove the reverse implication, impossibility of that bound,
or impossibility of other propagation arguments. The brief's former
"restatement" language and the manuscript's "equivalent-strength" reading
were corrected. A researcher could legitimately pursue that sufficient
condition, provided the proof is independent of the desired KLS conclusion.

The atlas's list of four negative results does not actually include
`prop:ceiling`; the reviewer verified this and requested no change to those
four bullets. Their other mathematical claims were outside this audit.

### Parallel even radial test

*Established analytically but uncertified as a node:* the path
$\beta=2+\varepsilon^2$ defines full-dimensional log-concave boundary laws for
both signs, and explicit compact restrictions are regular. The boundary
calculation does not automatically transfer to those restrictions and does
not instantiate the source-linear exponential–Gaussian ansatz of
`conj:cmh-second-variation`.

*Observed exact symbolic evidence, not a new certification:* the optimized
right-beta derivatives at two for total degrees one through four are

$$
-\frac12,\qquad -\frac{133}{120},\qquad
-\frac{227}{280}-\frac{403\sqrt2}{840},\qquad
-\frac{559}{504}-\frac{1373\sqrt5}{5040}.
$$

The epsilon second derivatives are twice these values. Both parity branches,
the multiple endpoint maximizers, covariance and denominator variation are
accounted for. The full numerator is used; the solenoidal energy contributes
only at order $\varepsilon^4$ in the written projection-distance argument.
The exact table and its supporting analytical reductions remain subject to
independent examination if a future proof uses them as premises. This is a
negative low-degree boundary calibration, not a theorem about full CMH.

`ap:c-solenoidal-perturbation` remains active, with its next test returned to
the canonical source-linear admissibility question; this completed radial
calibration should not be repeated. No route state changed in this session.

## What resists

The review recertifies exactly the seventeen named consumers. It does not
recertify every other August-25 dossier, every downstream proof, or the full
source proofs behind its already certified inputs. No universal survival,
trace-upgrade, CMH or KLS premise was discharged.

For the radial path, regular-kernel convergence and variation transfer remain
unproved. Moment convergence alone is insufficient. The calculation at four
fixed degrees proves neither a full CMH upper bound nor the canonical
second-variation conjecture, and yields no counterexample.

## Proposed next step

The grouped review and its repair cycle are complete. The full checker passed
after integrating all seventeen certification records. Canonical statement
snapshots before and after the writer's corrections agree exactly. The
writer updated the half-profile proof and ceiling explanation; the
orchestrator updated the brief, dependency edges and CMH next test.

Resume the portfolio's mathematical tests using the repaired backbone and the
ceiling's one-way scope. Any future use of the symbolic radial identities as
proved premises needs its own analytic dossier and independent examination;
the present calibration supplies no such certification.
