---
verdict: revise
authors:
  - kls_core_author, unknown, 2026-08-25
  - kls_bootstrap_author, unknown, 2026-08-25
  - kls_bootstrap_author, unknown, 2026-08-27
reviewer: reviewer, gpt-6-astra, 2026-10-04
fingerprints:
  solutions/kls-localization-riccati-core.md: 1bb625d625802df0ca05a338d3038a48ff8a0d2ca112f2fe1a2a4d9877690dff
  lem:survival-implies-kls: fcc0ff284f00b4f7d903900409e37db884463ad15f1f7cbb2c48ecb254e4cc64
  lem:matrix-riccati: b529c0f736b4dce32a7843e81f8edb6569491781941e3b8aecdc1be0ddf7a023
  thm:scalar-riccati: 83fdb94d00721fdfab219b0a417b1ac815c170925d051a187929c3635241286d
  cor:per-direction: 41aeb34aa0f748e931a100d435bb6cbba97772f149ce25c2e089fc77974c1e43
  cor:tight-window-consumption: 7d0f9e5dce52482fc3b8f93155bb46e66596d3aac7d92a63f7e508bc25b59946
  lem:pathwise-BL: 5b8de97a90772764778ad79fc4a9f56642c732304f4792a95b6cc493c7a95d6a
  prop:stein-rep: 809545792ca08860114a8276ff5b61febda2930cfd2b8b0f3a1a5ca1a0d00e6a
  cor:away-from-zero: d15055503849fa299724c5cb1640fab8f4b60ebc491621b6ffb1d34480e0dd95
  lem:stein-vs-source: 6bd84bc399d194fcb26d5a831feb198bcda29c1beaa21a9d1ebe64320eca30b5
  solutions/kls-bootstrap-interface.md: 3cd7b179f5f35c14c8b4ac27d4f868313e2d10522c340c31cff70c6ea07ab83d
  lem:half: 1d4daf2283e1a1022580a067533d1cc3aae4194fa319d223aa00e4112d031a2f
  lem:whitening: 3df7fc9dc6144b5c2ca23c0e9d21fc7a2132c0d494e03c75213cdc7ad7f72573
  thm:bootstrap: c63a5b4f893d86e70e67812caeccaa0015e754febda8a6a832909f82b015492b
  lem:perimeter-martingale: c0e1c3539694fe07c6ebe7c767bafeeadef66ac4778e02f7d217b6c9d3ad3daa
  lem:crude: 4596fedb12dae4093deded196b84f7f3f624d96f97cc69158a7eca583e997a6f
  cor:loglog: 993fe5733752c06b378ba37d27e4cfb44bd644aaf9810493cb1328bfd4bf7bc7
  ass:KI: 19c8922790211e205d6eda530efc90f61707e276482b5179d2254928e394f7c4
  cor:KI-discharged: 5ddd85d0e5ca16534f2e52aadb8a2a8b139979e5b19edb727c861d88a43243b7
  prop:ceiling: 0f7675a8caf88da1824c1bd76c2d2534a0d0ced9821774be7418b340413e1a20
---

# Fresh grouped examination: Riccati consumption and bootstrap interface

## Findings

**Revise the two dossiers as written.** The corrections concern the explicit
finiteness/dependency justification in tight-window consumption, an incorrect
profile endpoint assertion, and clear separation of the superseded survival
proof and the ceiling's one-way implication. No canonical quantified theorem
is refuted. Most of the mathematics checks; this report distinguishes those
checked conclusions from the localized defects rather than declaring the whole
backbone false.

This is a full fresh-context examination of all three assigned dossiers,
without retaining any prior review verdict as mathematical evidence. The
August-25 reports and provenance checkpoint identify the authors; the August-27
bootstrap report was consulted for the additional author identity only.
There are seventeen current consumers of these three dossiers, sixteen of
which still name August-25 reviews. The five nodes in the QCTS/Stein/boundary
dossier receive a separate new pass report:
`research/reviews/2026-10-04-aug25-grouped-pass.md`.

Under the grouped-review rule, this revise report supplies no new proof record
for either of its dossiers. The table records exactly which conclusions were
verified and which argument needs correction; a row marked checked is not a
hidden pass record. The localized findings do not invalidate the existing
proofs of unaffected nodes merely because they share a file.

| Current consumer | Examination result |
|---|---|
| `lem:matrix-riccati` | Identities checked, including all Ito cross terms; no defect found. |
| `thm:scalar-riccati` | Trace identity and D>=r-squared checked; no defect found. |
| `cor:per-direction` | Stopping, nonnegative terminal value, Fatou, and infinite-horizon monotone limit checked. |
| `cor:tight-window-consumption` | Correct consumption mechanism, but finiteness before absorption and the actual source-budget dependency must be recorded; obsolete internal survival proof must be bypassed explicitly. |
| `lem:pathwise-BL` | Quadratic form-domain calculation and both constants checked. |
| `cor:away-from-zero` | Constants 8 and one half, eta choice, and integration away from zero checked. |
| `lem:half` | Exact conclusion follows from the cited profile result, but the written universal assertion I(0+)=0 is false and its endpoint argument needs correction. |
| `lem:whitening` | Lipschitz-image perimeter comparison and dimensional monotonicity checked. |
| `thm:bootstrap` | All coefficients and the two-case argument checked; relies on `lem:half`, whose proof paragraph needs correction. |
| `lem:crude` | Trace-supermartingale argument, BL cap, and split integral checked. |
| `cor:loglog` | Input statement and integration checked; inherits the bootstrap dependency only for its excess conclusion. |
| `prop:ceiling` | The quantitative sufficient implication into KLS is correct. No converse, refutation, or general prohibition of propagation arguments is proved. |

### Riccati algebra, local domains, and stopping

In `solutions/kls-localization-riccati-core.md`, lines 37–118 fix the usual
posterior and the two conditional covariance decompositions. All conditional
moments exist: log-concavity gives finite moments initially, and at positive
time the Gaussian likelihood gives every polynomial moment. Positive finite
likelihood keeps a nontrivial initial cut nontrivial at every finite time.
The local Ito calculations involve posterior moments, not derivatives of the
cut indicator. Thus they apply to a fixed measurable cut without a smooth
boundary. Near time zero, exponential integrability of a full-dimensional
log-concave law gives local moment bounds; at positive time Gaussian damping
supplies them. The displayed local identities therefore do not require an
unjustified limiting identity from a smoothed cut.

Lines 181–235: the product rule for p times a contributes exactly A v dt.
The conditional second-moment contrast is sK. In B=vv-transpose/s, the
cross-variation term is minus alpha(KB+BK), while the inverse-s drift has both
terms displayed. Substituting K=G+alpha B/s cancels the linear terms and the
quadratic coefficients 1+1-2. B-squared=rB then gives the within-color drift
minus(R-squared+sG-squared). No commutation of A and B was assumed.

Lines 249–262: tracing gives S-D, and B<=A gives D>=r-squared. Isotropy is
unnecessary for these identities; it supplies A0=I for the later budgets.
Lines 281–289: stopping at increasing coefficient/martingale levels, taking
expectation, and discarding the nonnegative terminal quadratic form is valid.
Fatou removes these stops. Monotone convergence in the deterministic horizon
gives the infinite-time Loewner bound. Testing deterministic directions is
sufficient, and no infinite-time martingale equality or random-direction
interchange is used. The dossier says 'Consequently', correctly: the weaker
source-only Loewner estimate is not logically equivalent to retaining the
R-squared dissipation, despite the canonical statement's informal 'Equivalently'.
Both asserted bounds themselves are proved.

### Tight-window defect and its exact size

Lines 321–325 pass directly from a localized identity to absorption of the
Carleson bound and then to Gronwall. Fatou by itself does not justify
subtracting two possibly infinite occupation terms or applying Gronwall to a
possibly non-locally-integrable expectation. Nor is a deterministic-prefix
Carleson premise automatically valid with an additional arbitrary localizing
stop. The manuscript proof currently includes the missing safeguard, but the
standalone dossier does not identify or spell it out.

The necessary input is already available in the immediately preceding
per-direction theorem: summing over a fixed orthonormal basis gives
E integral S <= Tr R0 <= n, with no Carleson assumption. This finite source
budget permits removal of the auxiliary stops before invoking the premise.
The terminal r and integrated D then have a finite bound 1+n; consequently u
is locally integrable. Only after this step can absorption give the claimed
dimension-free Gronwall bound. This is a short completeness/dependency repair,
not a new open estimate and not a counterexample. The dimension n is used
only to establish finiteness and disappears from the final constants.

Once that point is made, lines 328–353 check: the stopped terminal variable
dominates the un-stopped integrand before exit; s>=2/9; the initial displacement
to the outer window is at least eta/2; the weak L2 maximal bound has factor
4/eta-squared; and s<=1/4 gives 9 C-star T/(8 eta-squared). This is the maximal
probability inequality for the square submartingale, not the strong L2 norm
inequality with its extra factor 4. Continuous exit defined using a strict
inequality still reaches the boundary, so the displacement argument is valid.
Signed C0 or C1 in the canonical statement may harmlessly be increased to
their nonnegative parts, matching the dossier's formulation. Alpha<1 is used
only in absorption.

The ledger currently omits `cor:per-direction` from this node's dependencies.
The source-budget proof uses it. The needed relation proposal is
`depends_on: [thm:scalar-riccati, cor:per-direction, lem:survival-implies-kls]`.
This addition is acyclic and introduces no open dependency.

### Superseded survival and the valid replacement

The old shared dossier still advertises seven active results in lines 5,
16, 18 and 26 and proves survival internally in lines 120–155. Its line 33
identifies general outer Minkowski content with a reduced-boundary integral,
which is not valid for arbitrary measurable sets. That defect is already
recorded in `research/reviews/2026-10-04-wave-a-survival-independent.md` and is
not counted here as another active failed certification.

The active ledger record instead names `solutions/lem-survival-implies-kls.md`
and its independent repair review. The canonical antecedent and conclusion
were checked against the corrected bridge: survival at a deterministic
positive time with b0=1/3 and c0=1/2 is precisely sufficient. The bridge does
not assume a Riccati, source, or covariance-occupation estimate, so there is
no circularity. Tight-window line 317 must explicitly consume that active
canonical lemma rather than direct the reader to the obsolete internal proof.
The bootstrap ceiling already references the canonical node, so its bridge
has not failed after the replacement. This review does not recertify the
standalone repair or reintroduce the old Section 2 record.

### BL source and away-from-zero estimates

Lines 368–392 use the normalized color of L2 norm one, a centered quadratic,
and the exact identity sqrt(s) times the K/M pairing. The gradient is
2M(x-a), so its energy is 4 Tr(MAM), and duality yields exactly
4 lambda-max(A)/t. The Gaussian factor supplies the required quadratic L2
and gradient L2 norms; smooth truncations converge in the form norm. The
second inequality is the covariance cap. Applying the same cap to a linear
function checks its normalization.

The smooth variance input was verified in the actual published rederivation
[Nguyen, JFA 266 (2014), equation (1.9) and Section 4, author manuscript]
(https://arxiv.org/pdf/1302.4589): the coefficient is the inverse Hessian,
so Hessian at least tI gives exactly 1/t. The required constant can also be
checked from the gradient contraction (2.5) in the accessible original
[Bakry–Ledoux paper](https://www.math.univ-toulouse.fr/~ledoux/LevyGromov.pdf).
For a nonsmooth convex potential with convex support, the usual convex
Moreau-envelope smoothing preserves the t quadratic term; an affine lower
bound gives a common Gaussian majorant. The inequality first passes for
compact smooth tests by dominated convergence, then to these polynomials by
form closure. This verifies the precise extension used, independently of the
shared dossier's misleading general perimeter-approximation sentence. No
unavailable source is necessary for this variance input; no claim is made
that the original 1976 article itself was retrieved.

Lines 413–421: the error is `2(q-p)^2 r^2/s`, bounded by
`(128/3) eta^2 D` for eta<=1/4. The proposed eta0=min(1/4,sqrt(3)/16) makes
this at most D/2. Tonelli then gives the interval estimate for t0>0, including
unbounded nonnegative values if necessary. There is no estimate at t0=0.
The Stein representation and conversion dependencies are safe; the dossier
rederives the needed algebra, so some recorded edges are redundant, not
missing hypotheses or cycles.

### Bootstrap profile error, remaining calculations, and domains

In `solutions/kls-bootstrap-interface.md`, line 74 explicitly asserts
`I_nu(0+)=0` for every log-concave law. This is false, even for a full-dimensional
one-dimensional uniform law on an interval: the interior profile equals the
reciprocal interval length, so its right endpoint limit is positive. Assigning
I(0)=0 is not asserting I(0+)=0. The same false sentence appears in the
manuscript proof following `lem:half`.

The exact desired identity is nevertheless supported by
[Milman, Theorem 1.8, Corollaries 6.5 and 6.12]
(https://arxiv.org/pdf/0712.4092), published in Inventiones Mathematicae 177
(2009). The source gives interior concavity and symmetry at the required
nonsmooth log-concave scope, including dimension one; nonnegativity suffices
for interpolation from an interior epsilon, followed by epsilon tending to
zero. The correction is to the proof's false auxiliary assertion, not the
canonical equality h=2I(1/2). No profile minimizer or endpoint continuity is
needed. Proper-affine-support measures are handled in their affine hull;
the Dirac case has no nontrivial-mass competitors.

Lines 95–112: the affine image inclusion and lower-liminf scaling have the
correct direction. Covariance nondegeneracy is essential for whitening and
holds along finite-time posteriors of an isotropic law. Cylinder competitors
in a product with a Gaussian give the claimed nonincreasing worst-dimensional
constant. There is no assumption of Cheeger tensorization in this step.

Lines 158–255: the corrected perimeter dependency `lem:perimeter-martingale`
has the actual fixed-Borel-set lower-Minkowski statement needed at deterministic
time. If the initial perimeter is infinite, the upper bound is trivial.
For a completed-measurable actual cut with finite perimeter, its closure has
the same mass and neighborhoods, since positive closure mass excess would
force infinite content. Equivalent posteriors preserve that mass equality.
Thus this use reduces to the Borel case without changing the perimeter.
No optional stopping of the perimeter is required.

The lower bound for the profile can be negative, and the two-case argument
correctly avoids multiplying a negative bracket by a lower bound for rho.
Near-worstness and the definition of h-star give
1/(1+epsilon)<=rho<=1. The resulting coefficients epsilon/2, eta, P/2, Y/4
are correct in both cases. The bounded stopped mass martingale has quadratic
variation at most one quarter of the integrated top covariance. The maximal
probability bound, its integration, and Tonelli give exactly 1/16, 1/8, 1/4
in the integrated expression. Eta=T^(1/3), epsilon<=T^(1/3), T<1/8 give the
clean estimate. Its correctness depends on the half-mass identity, not on the
false endpoint assertion as a mathematical fact. Correct that proof paragraph
rather than weakening the theorem.

Lines 270–289: the nonnegative trace with nonpositive drift is a
supermartingale after localizing and applying Fatou. Thus E X<=n; the BL cap
also gives X<=1/t. Splitting at 1/n proves the exact logarithmic expression
for 1/n<=T<=1, including its endpoints. It supplies an upper bound only,
not a lower bound on the actual interface.

Lines 297–322: `ass:KI` supplies E||A||<=C1 through the stated t1, and
`cor:KI-discharged` supplies its proved published-window discharge. These
canonical dependency statements were checked; their full external proofs
are outside this review. Integration on [0,t1] and [t1,T] yields the asserted
bound, and substitution into the clean bootstrap gives the excess conclusion.
The assumption is stated for n>=3; any separate n=2 convention uses the
finite-dimensional trace bound and changes only an absolute constant. The
quantities involving log n are not claims at n=1. No preprint result is imported
or used as an unproved dependency in this argument.

### The ceiling: exact direction and unsupported readings

Lines 329–360 prove the quantified implication

> A uniform all-measure bound Xi(T0)<=kappa T0 at a universal positive time
> with 9(1+kappa)T0<=1/2 implies KLS.

Indeed, the integrated top eigenvalue is at most (1+kappa)T0. From a half-mass
cut, exit from [1/3,2/3] costs displacement 1/6. The square-submartingale
maximal inequality has coefficient 36; quadratic variation contributes 1/4,
leaving exactly 9. Survival probability at least one half then meets the
current canonical survival bridge. This part uses neither the bootstrap,
near-worstness, profile endpoint continuity, nor the obsolete survival proof.

Lines 336 and 362 delimit the methodological claim to making the *particular
upper certificate* C h(T^(4/3)+Xi) small term by term. That calculation is
valid when distinguished from necessity for the actual excess: a large upper
bound does not imply that the bounded quantity is large. The canonical final
sentence can and should retain this stated certificate-specific reading.
No change to its quantified sufficient implication is required. Because the
final certificate discussion also uses `thm:bootstrap`, its full-node ledger
relation should record `depends_on: [lem:survival-implies-kls, thm:bootstrap]`
if that discussion remains part of the proposition's claimed consequence.
This does not change the independence of the first, quantitative implication.

Neither KLS implies this covariance bound nor the bound is false has been
proved here. A route proving the covariance bound is a legitimate sufficient-
condition route, not automatically a circular argument. The broad phrases
'equivalent-strength statement' and 'restatement' in the current prose are
unsupported. Failure of this particular sufficient condition would not refute
KLS. No target negation or `refuted_by` transition follows from `prop:ceiling`.

### Relations, fences, and downstream impact

All recorded dependencies of the twelve nodes are currently proved; none has
an open `depends_on`, `assumes`, or `bounded_by` edge. `ass:KI` is proved,
despite its prefix. The source-budget edge above and the bootstrap edge for
the ceiling's certificate discussion are the relation corrections. The
projection, crude-input, and relative-input remarks are methodological
constraints, not additional proved fences. No run artifact enters a proof.

The current direct `depends_on` consumers of `cor:tight-window-consumption`
are `thm:intro-all-cut`, `thm:intro-weighted`, and `prop:intro-audit`; there are
no further transitive dependents in this ledger. The repair is needed to
refresh this node's standalone certification and should be carried through
those uses. Their whole dossiers were not reviewed here.

The current direct consumers of `lem:half` are `thm:intro-weighted`,
`prop:intro-audit`, `thm:bootstrap`, `thm:bootstrap-stopped-interface`,
`prop:weighted-spectator-obstruction`, `prop:spectator-excess-rate-obstruction`,
and `cor:dichotomy`. The additional transitive consumer is `cor:loglog`.
This is the dependency footprint of the proof correction, not evidence that
any of those conclusions is false. In particular no certified refutation is
reversed by the endpoint counterexample, which is a counterexample only to
the unused claimed endpoint continuity.

`prop:ceiling` has no current direct or transitive `depends_on` consumers.
Its visible effect is explanatory prose in the brief, bootstrap section,
overview, and fixed-cut discussion. Its main quantitative implication remains
valid; correcting the negative/equivalence reading has no theorem refutation
or graph-status consequence. Adding the proposed bootstrap relation makes
the full proposition an additional dependent of `lem:half` for its
certificate discussion only.

## Corrections

The following is the exhaustive required repair handoff on the versions read.
Line references identify locations, not authority to change canonical claims.

1. `solutions/kls-localization-riccati-core.md:321`: before using the Carleson
   premise, explicitly invoke `cor:per-direction`, sum in a fixed basis, and
   establish finite source budget <=n. Remove auxiliary stops using this
   integrable source, Fatou for terminal r and integrated D, and monotone
   convergence for source. Record the resulting <=1+n bound and local
   integrability of u. Apply the original deterministic-prefix premise only
   after removing those stops. The current manuscript proof of
   `cor:tight-window-consumption` already spells out this safeguard and can
   guide the repair. Add the ledger edge proposed above; do not assume that
   the premise survives arbitrary added stops or subtract extended infinities.
2. `solutions/kls-localization-riccati-core.md:5`, `:16`, `:18`, `:26`,
   `:120`, `:317`, `:424`: remove the claim to provide the active survival proof
   and replace the obsolete Section 2 argument with a clearly labelled pointer
   to `lem:survival-implies-kls` and its standalone active dossier. Preserve
   history in the append-only earlier reports. In the current dossier do not
   retain line 33 as a general reduced-boundary proof. State that the remaining
   six claims use the exact original posterior and appropriate local moment
   stops; rough cut smoothing is not needed for their local identities.
3. `solutions/kls-bootstrap-interface.md:74` and the proof after `lem:half`
   at `modules/20-bootstrap.md:23`: replace the assertion I(0+)=0 with the
   precise interior-concavity/nonnegativity argument, citing Milman Corollaries
   6.5 and 6.12. Explicitly distinguish the assigned value I(0)=0 from its
   potentially positive one-sided limit. The canonical identity is unchanged.
   Have the responsible manuscript writer edit the proof prose.
4. `solutions/kls-bootstrap-interface.md:336` and `:362`: keep the quantitative
   sufficient implication and the certificate-specific limitation explicit;
   clarify that no converse, general propagation impossibility, or automatic
   circularity follows. No new proof of such a converse is requested. Record
   the bootstrap dependency if the certificate consequence is retained in the
   node. The current numerical proof needs no change.
5. `modules/20-bootstrap.md:211`, replacement prose:
   'By [](#prop:ceiling), a bound $\Xi_{T_0}(\mu)\le\kappa T_0$ for every
   isotropic log-concave measure at a sufficiently small universal time is
   sufficient for KLS. No converse is established here. The proposition
   explains the strength of that particular covariance input; it does not
   rule out proving it or obtaining propagation by another argument.
   [](#conj:taming) instead asks for a near-worst, $h_\mu$-weighted bound.'
6. `research/program/brief.md:119`, replace trap 2 (through line 122) with:
   '2. **A KLS-sufficient covariance input** (`rem:relative-ceiling`, from
   `prop:ceiling`). A universal all-measure $\Xi_{T_0}\le\kappa T_0$ bound
   at sufficiently small fixed time implies KLS. No converse or equivalence
   is established. Proving this bound would be a sufficient-condition route;
   its failure would not refute KLS. Distinguish it from near-worst weighted
   propagation and from the actual excess controlled by the bootstrap.'
7. `modules/00-overview.md:359`: retain the paragraph through the published
   covariance estimate; replace the three concluding sentences beginning
   'But [](#prop:ceiling)' by:
   '[](#prop:ceiling) proves that an all-measure bound
   $\Xi_{T_0}(\mu)\le\kappa T_0$ at a sufficiently small universal time is
   itself sufficient for KLS. This identifies the strength of one input that
   would make the clean bootstrap certificate small. It establishes neither
   a converse nor a prohibition on other propagation arguments.'

The current atlas paragraph at `modules/07-frontier-atlas.md:59` lists four
negative results, but its four bullets do not include `prop:ceiling`.
Accordingly this review proposes no ceiling-related correction to that list.
The fixed-cut table there simply names the ceiling and does not assert its
converse. Other negative-result claims in that list were outside this mission.

After the dossier corrections, obtain a fresh independent re-review; do not
merely update fingerprints. Do not change any target to `refuted`. This report
provides no new certification delta. If proof records are temporarily removed,
apply the ledger's proved-dependency rule to the listed affected nodes rather
than silently leaving a proved node dependent on an open one; a coordinated
repair and re-review is preferable to treating these local repairs as theorem
counterexamples.

## Exclusions and build

The superseded shared survival proof is not an active certification in scope;
its standalone replacement remains the current bridge. The external
covariance-window theorems, other downstream dossiers, CMH work, and other
barrier claims are not newly certified. The exact algebra and constants listed
as checked above must not be confused with blanket approval of the two files.
No inaccessible source is being used as proof evidence; the variance input
was checked in an accessible published rederivation, and the other imported
steps and source limits were identified explicitly.

The full `UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py` completed with
exit code zero and no MyST error. The final two-dossier fingerprint command
also completed successfully. Its exact output is recorded above. The stale
survival header causes the command to include the canonical survival statement;
that entry identifies the version read, not a certification of the old proof.
All other extra statement fingerprints are checked dependency interfaces.
The checks used the approved execution path because sandboxed Node subprocesses
cannot perform the build. A successful checker does not cure the mathematical
proof-paragraph or dependency defects.

## Handoff

```yaml
files:
  - research/reviews/2026-10-04-aug25-grouped-revise.md
next: |
  Assign a researcher the dossier corrections 1–4, including the explicit
  tight-window finiteness argument, superseded-survival pointer, endpoint
  correction, and precise ceiling scope. Preserve all other agents' edits.
  Have the orchestrator record the two proposed dependency corrections and
  the brief edit, and have the manuscript writer apply corrections 3 and 5–7
  without changing canonical statements. Then run a fresh independent
  re-review of the repaired dossiers and their changed dependency scope.
```
