---
verdict: pass
authors:
  - bk_powers, gpt-6-astra, 2026-10-06
  - orchestrator, gpt-6.1-sol, 2026-10-06
reviewer: reviewer, gpt-6-astra, 2026-10-06
fingerprints:
  solutions/bk-kls-composition.md: f4fbcf73fc7332342b6318a92d0468981b9a78bd838dfff0c09303b08f759f45
  conj:kls: b34221c5440f365f12cb6529324aed7a62b355236e5a037761de51f02adeab69
  thm:bkl-tilt-bound: b14ed0af1b0f660928c9d507b8567b89ff97bbbd8620a138eba3fecf5aadf82f
  thm:bkl-tilt-criterion: 050f47b3ff5487f31a0b08990786dee5bef2a5ce39b8c85bb5982ea1410ab344
  lem:bkl-analytic-foundations: 7657fb2bb9597db83ab252a2b5ba773b834bf96f7d71f6cc27377648b7e2314d
  thm:sz-v2-kls: f5dfe05f2a9880082765a4f61d7fd0cfd36cc8e259615b54280e37b1380ee16e
  thm:bk-explicit-poincare: ed29bf2fbe5c374559d511d8ce54e010095503ae0794aff0218b323e1062045a
---

# Canonical KLS: the BK composition

## Findings

**Pass** for `solutions/bk-kls-composition.md` as an additional proof of the
unchanged canonical `conj:kls`. Retain its existing `proved` status and other
proof records, subject to their separate fingerprint updates after the
collective dependency list changed. This dossier uses only the BK explicit
Poincaré theorem as its substantive theorem input, with the published Cheeger
comparison for the equivalent formulation.

This is a full `certify` review in the independent context of the BK operator
and outer reviews. The assignment supplied paths and author identities, not
the authoring conversation. I authored none of the dossier, its canonical
statement, or its inputs. The current dossier was reread after its final
editorial scope wording changed and before the fingerprint command.

### Statement and dependency agreement

The canonical target quantifies over every dimension, every isotropic
log-concave law, and every locally Lipschitz test, and asserts a universal
Poincaré constant and its equivalent uniform Cheeger lower bound. The dossier
supplies precisely these claims with $C=1+2\cdot10^{16}$. Its variance
convention gives an unambiguous extended quantity for tests outside $L^2$,
without narrowing the canonical test class.

The canonical `thm:bk-explicit-poincare` provides both the finite-energy
inequality and square integrability, for every covariance-at-most-identity
law on its affine support. Isotropic laws are a subclass. This input is now
proved by `research/reviews/2026-10-06-bk-outer-review.md`, carried across its
prose cleanup by `research/reviews/2026-10-06-bk-outer-editorial.md`. I read
the editorial note and verified that its stated scope concerns the same
input; the statement fingerprint remains the one independently checked in
the outer review. The operator and localization inputs likewise retain their
certifications with the separate input-status editorial note. No open
antecedent is accepted here.

The ledger's target dependency list is collective across its proofs. I read
the canonical statements of `thm:bkl-tilt-bound`, `thm:bkl-tilt-criterion`,
`lem:bkl-analytic-foundations`, and `thm:sz-v2-kls` and account for them in
the mandatory fingerprint union. They are already proved but are not used
by this BK composition. Their presence in this report is not a claim that
the BK proof needs either of the other KLS proofs. No such premise appears
in the dossier. The only new genuine edge is
`conj:kls -> thm:bk-explicit-poincare`, already added by the orchestrator.

### All test functions

For a positive-dimensional isotropic law, full affine dimension follows
from identity covariance; log-concavity then gives absolute continuity.
The almost-everywhere Euclidean gradient therefore defines its nonnegative
Dirichlet integral. When this integral is finite, the explicit BK theorem
applies and proves square integrability before the variance is used.

For an $L^2$ test, expansion about its mean gives the exact displayed identity
for $\int|f-c|^2$, so the infimum over finite constants equals the usual
variance. If energy is infinite, the target inequality holds in the extended
nonnegative reals. A function outside $L^2$ has infinite squared distance
from every finite constant, since otherwise
$|f|^2\le2|f-c|^2+2c^2$ would put it in $L^2$. Thus no undefined mean or
subtraction of two infinite quantities enters. The zero-dimensional point
mass case, if included in “every dimension,” is immediate from the input's
explicit point-mass convention.

These steps use only the stated finite-energy input and elementary identities.
There is no density argument silently extending the input to a larger space,
and no assumption that a locally Lipschitz function is automatically square
integrable.

### Cheeger equivalence

I checked the cited published
[Klartag 2023 source, equation (1.4), p. 3](https://arxiv.org/pdf/2303.14938),
which gives $1/4\le h^{-2}/C_P\le\pi$ in the indicated inverse-isoperimetric
normalization. I also checked the definitions and comparison statements of
[Milman 2009](https://arxiv.org/pdf/0712.4092): its Minkowski expansion
constant is the manuscript's $h$, and its spectral-gap scale is $C_P^{-1/2}$.
The exact $\pi$ used here is recorded in Klartag's published equation;
Milman supplies the general comparison and matching boundary convention.

It follows that $h\ge(\pi C)^{-1/2}$ from the BK bound. Conversely,
$h\ge b>0$ implies $C_P\le4b^{-2}$. Both directions are algebraically
correct and independent of dimension. The manuscript's structural equations
`eq:cheeger-two-sided` and `eq:hstar-def` agree with this use. No perimeter
normalization is changed by the composition.

### Hypotheses, fences, and build

The hypotheses used are exactly isotropy, log-concavity, finite dimension,
real locally Lipschitz tests, the certified explicit BK input, and the
published comparison on this log-concave class. The finite-energy versus
infinite-energy split is exhaustive. The zero test, constant tests, and
point masses create no exception. No symmetry, smooth density, positive
curvature, or bounded support is required at the conclusion. No `assumes`
or `bounded_by` relation is attached to the target; no structural inequality
beyond KLS is inferred.

`uv run scripts/check.py --fingerprint solutions/bk-kls-composition.md`
completed with exit 0 after the new dependency was registered. Its exact
output is the front matter above. A subsequent full checker run completed
the MyST build without any MyST error. It exited 1 solely on two historical
proof-record errors: the BKL and SZ composition reports do not yet fingerprint
the newly added BK dependency. Those failures concern their collective
ledger scope, not any statement, dependency truth, build step, or fingerprint
in this new BK report. Updating those earlier certifications belongs to the
orchestrator and a separate independent review; this report does not amend
their fingerprints. No other failure was reported.

## Corrections

None required for the BK composition. The two historical proof-record scope
updates just described remain separate repository maintenance and are not
silently certified here.

## Exclusions

This is not a re-review of the BKL or SZ proofs or their independence, nor a
new review of the already certified BK chain. The actual uses in this
composition are only the explicit BK theorem and the established Cheeger
comparison. No optimal constant, additional structural inequality, or claim
about the original 1995 geometric proof is established here. No mathematical
step in the assigned composition remains unverified.

## Proposed record and handoff

```yaml
files: [research/reviews/2026-10-06-bk-kls-composition-review.md]
deltas:
  - node: conj:kls
    preserve_status: proved
    preserve_existing_proofs: true
    append_proof:
      artifact: solutions/bk-kls-composition.md
      review: research/reviews/2026-10-06-bk-kls-composition-review.md
    preserve_depends_on:
      - thm:bkl-tilt-bound
      - thm:bkl-tilt-criterion
      - lem:bkl-analytic-foundations
      - thm:sz-v2-kls
      - thm:bk-explicit-poincare
    preserve_references:
      - BizeulKlartagLehec2026KLS
      - SongZhang2026ConstantKLS
      - BalasubramanianKasiviswanathan2026KLS
```
