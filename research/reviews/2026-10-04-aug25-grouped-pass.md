---
verdict: pass
authors:
  - kls_core_author, unknown, 2026-08-25
reviewer: reviewer, gpt-6-astra, 2026-10-04
fingerprints:
  solutions/kls-qcts-stein-boundary-core.md: 679acb07ec69b0741d4a515f40693de4100d0a3ef092e586bb53ff2d2bc5f630
  prop:qcts-equivalence: a2120cd5d1d4968432ea232d734c8f07c4542570f23684fd94a105e065fe246e
  def:qcts: 0f22746bfd781ed526102c33b699417cb07ef6d9df40f0fb4ce59158e6376b86
  prop:stein-rep: 809545792ca08860114a8276ff5b61febda2930cfd2b8b0f3a1a5ca1a0d00e6a
  lem:stein-vs-source: 6bd84bc399d194fcb26d5a831feb198bcda29c1beaa21a9d1ebe64320eca30b5
  thm:scalar-riccati: 83fdb94d00721fdfab219b0a417b1ac815c170925d051a187929c3635241286d
  lem:boundary-rep: ec5bb90e57459669bbd919a3edcac5720f3f22bda24693a1dbca6463219f6756
  prop:two-tail: 85de1f26b16a82f85696ec5a655749365c0f036976c11265cee235f780c44d7b
---

# Fresh grouped examination: quadratic-chaos, Stein, boundary, and two-tail claims

## Findings

**Pass for all five active nodes of `solutions/kls-qcts-stein-boundary-core.md`.**
This is a new full examination in a fresh reviewer context, not a re-review
retaining any historical verdict. The August-25 report and checkpoint supplied
author provenance only. The three assigned dossiers were read completely and
their seventeen current ledger consumers checked against canonical statements.
Sixteen consumers still name August-25 reviews; `thm:bootstrap`, the seventeenth,
names an August-27 review of the same dossier. The other two dossiers receive
separate findings in `research/reviews/2026-10-04-aug25-grouped-revise.md`.

| Certified node | Statement agreement and conclusion |
|---|---|
| `prop:stein-rep` | Pass: exact covariance identity and squared Hilbert–Schmidt dual norm, at every mass strictly between zero and one. |
| `prop:qcts-equivalence` | Pass: the entire family of balanced measurable cuts is equivalent, up to numerical constants, to quadratic variance control. |
| `lem:stein-vs-source` | Pass: both conversions have coefficient 2 and error at most 64 eta-squared times D. |
| `lem:boundary-rep` | Pass in the stated smooth bounded weighted Neumann setting, with the inner-normal minus sign and relative interface. |
| `prop:two-tail` | Pass: all four exact Gaussian formulas and the uniform-constant obstruction. |

### Algebra and quantifiers

Lines 26–92: conditioning gives `mE-a=q delta`, `mF-a=-p delta`, and
`A=p SigmaE+q SigmaF+s delta delta^T`. Substitution gives the coefficient
`pq(q-p)` without a missing factor of p or q. Since K is symmetric, dualizing
over symmetric matrices gives exactly `s^2 ||K||HS^2`; allowing arbitrary
matrices does not enlarge the supremum because their skew parts pair to zero.
The stated fourth-moment hypothesis is sufficient; the identity and norm alone
only need second moments. No log-concavity, isotropy, PDE, or localization is
used in this algebraic node.

Lines 96–168: isotropy makes the support full-dimensional. A nonzero symmetric
M defines a nonconstant quadratic, whose level sets are Lebesgue null. Thus the
median cut has exactly half the mass without external randomization. The
identity with the sign of Y-m gives its centered absolute first moment.
Cauchy–Schwarz proves the forward implication, while the reverse moment
inequality proves the converse uniformly in dimension and M. A nonsymmetric
M in the canonical definition can be replaced by its symmetric part, whose
Hilbert–Schmidt norm cannot increase. This establishes agreement with
`def:qcts`, despite the dossier explicitly writing M symmetric.

The actual source checked is [Carbery–Wright, Theorem 7, author PDF p. 13]
(https://webhomes.maths.ed.ac.uk/~carbery/analysis/papers/cw-dim_final.pdf).
Its parameters q=2d, r=d yield the stated degree-two L2/L1 comparison. The
source explicitly allows log-concave probability measures, rather than just
uniform convex-body measures. The PDF text encoding is corrupt, so the page
was downloaded and rendered for direct visual examination. This is the
published Mathematical Research Letters 8 (2001) result, not a new preprint
import. The dossier uses no numerical artifact.

Lines 172–206: B<=A implies D>=r^2 directly by testing against delta.
The squared triangle inequality gives the error `2(q-p)^2 r^2/s` in either
direction. On the stated window, `|q-p|<=2 eta` and `s>=3/16>1/8`, so the
error is bounded by `64 eta^2 D`. The definitions and inequality used from
`thm:scalar-riccati` were also checked directly in the companion dossier:
the scalar trace and the coercivity calculation are valid. The companion
report's tight-window defect is downstream of this identity and does not
invalidate this dependency. In fact the present conversion rederives the
needed coercivity without using any stochastic expectation argument.

### Operator and boundary audit

Lines 210–255 use the Neumann realization of L on the smooth bounded connected
domain, not a whole-space inverse or a Dirichlet solution. The density is
bounded above and below by positive constants on the closure. On mean-zero
H1, the weighted Dirichlet form is coercive by the ordinary bounded-domain
Poincare inequality; its weak equation has right side minus the integral of
(f-fbar) times the test function. Compatibility holds by centering. This
checks existence and uniqueness modulo constants and the sign convention in
the displayed PDE. Smooth data up to the boundary give the normal traces
used in the proof. This is the customary meaning of the smooth-data setting
here; the assertion is not a theorem for arbitrary singular data near the
support boundary.

On the interior interface the outward normal of E is minus n; on the support
boundary the flux is zero by the Neumann condition. Applying weighted
divergence gives precisely the asserted covariance. Cauchy–Schwarz uses the
weighted relative surface measure; for the stated smooth relative domains its
total mass is the relative Minkowski perimeter. The contact set of the two
boundary pieces contributes no additional codimension-one flux. Convexity of
V and K is stronger than this integration-by-parts calculation requires;
smooth bounded connected support and positive smooth weight suffice. No rough
BV/Minkowski identification or approximation of an arbitrary measurable cut
is used here. That distinguishes this node from the superseded survival proof.

### Gaussian obstruction

Lines 257–349: the mass is one half, both conditional means vanish, and only
the first variance changes. Gaussian integration by parts gives conditional
variances `1+4a phi(a)` and `1-4a phi(a)`, hence the exact contrast and source
coefficient. Each of the two boundary hyperplanes contributes
`phi(a)/sqrt(Lambda)`.

The external Gaussian isoperimetric input was checked in
[Bakry–Ledoux, Corollary 2.2 and equations (2.11)–(2.12), pp. 267–268]
(https://www.math.univ-toulouse.fr/~ledoux/LevyGromov.pdf).
The Ornstein–Uhlenbeck specialization gives the standard Gaussian profile;
the halfspace computes equality. The Lipschitz image inclusion in the dossier
has the correct direction and factor `||T||op=sqrt(Lambda)`. Thus the long-axis
halfspace attains the anisotropic midpoint profile. Subtraction and division
give the stated excess and relative excess. The exact expressions, rather
than the manuscript's approximate decimals, are the proof evidence.

The negative assertion has the form: there exist finite constants, independent
of the law, for which the displayed slice inequality holds for every
log-concave law and every half-mass set. Its negation is: for every such fixed
choice of constants there is a law and a half-mass set violating it. The
certified family Lambda tending to infinity supplies this negation: its left
side is a positive constant times Lambda squared, while the right side is
`C0+C2 O(Lambda^(-1/2))`, because r=D=0. A single fixed Lambda would not suffice.
This is not a refutation of an isotropic-only or time-integrated assertion.
The auxiliary power calibration alpha>=5/2 is consistent with the same exact
scaling and is not a sufficient dynamic estimate.

### Dependencies, hypotheses, fences, and build

The ledger edges supply the statements used: `def:qcts` and `prop:stein-rep`
for the equivalence; `prop:stein-rep` and `thm:scalar-riccati` for conversion;
`prop:stein-rep` for the two-tail source. The boundary proof redoes the elementary
centering identity and does not need a separate Stein dependency for its main
flux statement. None of these nodes has an open dependency, an `assumes` edge,
or a `bounded_by` fence. The projection-only and two-tail methodological remarks
are respected: the converse uses all balanced cuts, and the obstruction is
static. The cross-dossier links are acyclic at node level: Stein representation
is elementary; matrix Riccati does not use pathwise BL or Stein conversion;
scalar Riccati supplies coercivity; later BL/conversion consumers do not feed
back into either identity.

The full `UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py` finished with
exit code zero and no MyST error. The final scoped fingerprint command also
finished successfully. The fingerprint block is its exact output. It includes
`thm:scalar-riccati` and `def:qcts` as checked dependencies, not newly certified
claims. No unexamined dossier is fingerprinted in this pass report.

## Corrections

None required for these five certifications. The companion report records the
tight-window bookkeeping and bootstrap endpoint corrections outside this
passing dossier.

## Exclusions

No certification of the other two dossiers is conveyed here. In particular,
this report does not certify the obsolete Section 2 survival argument, the
standalone survival repair, the external covariance-window results, any
geometric stability estimate, KLS, or a dynamic occupation inequality.
The inherited truth of a required certified dependency is not a new review of
its whole proof portfolio; its statement and use were checked as described.
No ledger or manuscript file was edited.

## Handoff

For each of the following five nodes, retain `status: proved` and the current
relations, and replace its historical proof record with:

```yaml
artifact: solutions/kls-qcts-stein-boundary-core.md
review: research/reviews/2026-10-04-aug25-grouped-pass.md
```

The nodes are `prop:qcts-equivalence`, `prop:stein-rep`, `lem:stein-vs-source`,
`lem:boundary-rep`, and `prop:two-tail`. There is no target-status transition:
`prop:two-tail` is itself the proved obstruction, not a new `refuted_by` edge.

```yaml
files:
  - research/reviews/2026-10-04-aug25-grouped-pass.md
deltas:
  - path: research/program/ledger.yaml
    nodes: [prop:qcts-equivalence, prop:stein-rep, lem:stein-vs-source, lem:boundary-rep, prop:two-tail]
    proofs:
      - artifact: solutions/kls-qcts-stein-boundary-core.md
        review: research/reviews/2026-10-04-aug25-grouped-pass.md
    status: proved
    relations: retain current relations
```
