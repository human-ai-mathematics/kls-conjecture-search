---
verdict: pass
authors:
  - plan_framework researcher, unknown, 2026-10-06
reviewer: reviewer, gpt-6-astra, 2026-10-06
fingerprints:
  solutions/bkl-cumulant-bound.md: c9a6b0955d620422b892b61e7922409ea163e728e1317982b1e31150d0d151b2
  thm:bkl-cumulant-bound: f494b6a9fe460588d0b885054be670483c49ffb759e6239e6f9b3651303ce275
  def:bkl-tilt-cumulants: 43636c8506cef53a8ed43a8231a955e160d704cc899cc248c5e08425ab5f449c
  lem:bkl-cumulant-dynamics: c6d9d767482c117e49dea11d360003958d8b5051e2d2fd8b37c193cbacf1dfcd
  lem:bkl-cumulant-energy: 87709dd0dbd422d53f71e28dd3c792839dfd771ebecd1b63059b65f898b556e8
---

# Independent certification of the all-order cumulant bound

## Findings

**Pass for [](#thm:bkl-cumulant-bound).** The dossier proves the canonical
statement for all dimensions, all isotropic log-concave probability measures,
all integer orders at least two and all vectors, with one universal constant.
The constant can in particular be chosen as $153$ using the certified energy
calculation's $C=17$. This is not a sharpness claim.

This certify mission began in a fresh context containing repository paths and
an assignment, without the authoring conversation. No reviewed dossier was
authored by this reviewer. The source actually read was Bizeul–Klartag–Lehec,
*Presenting a proof of the Kannan–Lovász–Simonovits conjecture*,
arXiv:2610.05474v1, Theorem 4.1 and its complete Section 6 proof,
equations (94)–(106), together with the Section 4–5 arguments covered by the
preceding dynamics and energy reports. The HTML copy
`/tmp/bkl-2610.05474v1.html` has SHA-256
`fb51ab0d94171ac7de2a3009efb5249e44ee66de5c9a1dc5899bdb843de29df9`.
The dossier gives the same coupled induction and expands the source's final
approximation sentence into a moment-convergence proof.

### Agreement, dependencies and hypotheses

The order of quantifiers is essential and agrees exactly: the constant is
chosen before dimension, measure, cumulant order and vector. The tensor norm
is the full ordered-index Hilbert–Schmidt norm specified by
[](#def:bkl-tilt-cumulants); its squared directional contraction is exactly the
canonical matrix quadratic form. The factorial is the square of $(m-1)!$
and the constant's exponent is $m-1$, as in the manuscript and source.

Both [](#lem:bkl-cumulant-dynamics) and [](#lem:bkl-cumulant-energy) were
registered as proved with their reports before this verdict. All direct
dependencies are proved or defined, with no open dependency, `assumes` or
`bounded_by` edge. The dynamics proof's use of [](#prop:letwin-kappa) has its
antecedent discharged by [](#thm:letwin-qcts); this proof does not silently
remove a conditional premise.

All used hypotheses are stated: finite positive dimension, log-concavity,
isotropy, integer order at least two and a deterministic vector. Compact
support and unit norm are temporary proof restrictions, both removed in the
dossier. No density regularity, curvature lower bound, or preliminary KLS
bound is required. The earlier dimension-dependent constants justify analytic
operations only and do not occur in the recurrence.

### Steps checked

**Lines 36–65: simultaneous induction.** Fixing dimension causes no loss of
uniformity because the constant is numerical. The induction is over all
compactly supported isotropic laws and all unit vectors simultaneously.
At order two its left side is at most $1+8/2=5$, so $K\ge5$ proves the
base case including the integrated third-order bound. The induction hypothesis
has two distinct valid consequences: the integrated next-order estimate for
the current process, and the static estimate for every law in the class.
The latter applies to each whitened posterior because that posterior belongs
to the same class. It does not require an induction statement about a random
initial law or a new expectation interchange. In particular the required
current-order time integral is controlled at the previous induction level.

**Lines 68–95: the split contraction.** For a subset of size $a$, its range
is $2\le a\le m-2$. After fixing the indices on the distinguished-vector
side, the remaining contraction is precisely the directional cumulant of
order $m-a+1$ at vector $A^{-1}z$. Its squared weighted norm is at most
$b_{m-a+1}\langle z,A^{-1}z\rangle$. The identity resolving that quadratic
form into the final whitened coordinate sum has no missing metric factor.
Summing the fixed indices gives the $(a+1)$st energy, whose time integral
is supplied by the induction at order $a$. Both orders invoked are strictly
below $m$; no desired current-order static estimate has been used. These
operations sum actual squared components and introduce no dimension factor.

**Lines 96–127: summation and closure.** There are exactly
$\binom{m-1}{a-1}$ subsets of each size containing the distinguished index.
They permute only the other slots, so their weighted norms agree. Whitening
realizes all of them in one ordinary tensor-valued Hilbert space over time
and probability; the triangle inequality therefore applies even though the
metric is random. The factorial identity on lines 110–112 is exact, with
power $K^{(m-1)/2}$. There are $m-3$ sizes, including an empty sum at $m=3$.
This proves the remainder integral is finite before invoking the energy
lemma. Together with the preceding current-energy integral it discharges
both hypotheses of that lemma without circularity.

Substitution gives the two terms in parentheses on lines 122–123. The first
is bounded by one half when $K\ge9C$, since $m/(m-1)\le3/2$; the second
is bounded by one half when $K\ge64$, since $(m-3)/(m-1)\le1$.
Thus the same numerical $K\ge\max\{5,9C,64\}$ works at every order and
in every dimension. The nonnegative static part of the stronger inductive
conclusion yields the requested static cumulant estimate.

**Lines 132–153: removal of compact support.** Conditioning on sufficiently
large convex balls preserves log-concavity and full affine dimension.
All fixed moments of the original law are finite by the one-dimensional
log-concave tail argument established in the dynamics dossier. Dominated
convergence for truncated moments and the normalizing probabilities proves
convergence of every mixed moment; in particular the conditional covariance
converges to the identity and is eventually invertible. Recentring and
whitening preserve compact support and log-concavity and give isotropic laws.
Each fixed moment after this affine transformation is a finite polynomial in
convergent entries and moments. The moment–cumulant formula gives entrywise
cumulant convergence. At fixed dimension and order, the finite tensor norm
therefore converges and passes the bound with the same universal constant.
Homogeneity gives all vectors, with zero treated directly. No localization
process for a noncompact initial law is assumed.

The full command `uv run --cache-dir /tmp/kls-plan-uv-cache scripts/check.py`
completed with exit code 0 and no MyST errors after both dynamics and energy
were registered. The fingerprints above are the actual output of
`--fingerprint solutions/bkl-cumulant-bound.md`. The canonical statement and
its direct dependencies were read again at final inspection; surrounding
editorial changes do not alter the reviewed statements.

## Corrections

None. No source, limit, contraction, or inductive step required within this
scope remains unverified.

## Exclusions

This report certifies the all-order static cumulant theorem only. It does not
certify suspension, tilt bounds, the tilt criterion, uniform conditional
initialization or KLS. It makes no claim that the cumulant theorem alone
implies any of these. No KLS estimate, suspension, tilt criterion or
Song–Zhang polynomial variance bound is used in this dependency chain.
Existing upstream Letwin certification is relied on at its stated scope;
that source proof is not recertified here. No sharp value of $K$ is asserted.

## Proposed record and handoff

```yaml
files: [research/reviews/2026-10-06-bkl-cumulants-review.md]
deltas:
  - file: research/program/ledger.yaml
    node: thm:bkl-cumulant-bound
    set:
      status: proved
      proofs:
        - artifact: solutions/bkl-cumulant-bound.md
          review: research/reviews/2026-10-06-bkl-cumulants-review.md
    preserve:
      references: [BizeulKlartagLehec2026KLS]
      depends_on: [def:bkl-tilt-cumulants, lem:bkl-cumulant-dynamics, lem:bkl-cumulant-energy]
```
