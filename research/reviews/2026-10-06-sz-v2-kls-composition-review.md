---
verdict: pass
authors:
  - plan_sz_architecture, unknown, 2026-10-06
reviewer: reviewer, gpt-6-astra, 2026-10-06
fingerprints:
  solutions/sz-v2-kls-composition.md: d70f79bfd4303082a4284b1ad3fa780a4f7e81d592dae5e0459116a6625d4d0a
  conj:kls: b34221c5440f365f12cb6529324aed7a62b355236e5a037761de51f02adeab69
  thm:bkl-tilt-bound: b14ed0af1b0f660928c9d507b8567b89ff97bbbd8620a138eba3fecf5aadf82f
  thm:bkl-tilt-criterion: 050f47b3ff5487f31a0b08990786dee5bef2a5ce39b8c85bb5982ea1410ab344
  lem:bkl-analytic-foundations: 7657fb2bb9597db83ab252a2b5ba773b834bf96f7d71f6cc27377648b7e2314d
  thm:sz-v2-kls: f5dfe05f2a9880082765a4f61d7fd0cfd36cc8e259615b54280e37b1380ee16e
---

## Findings

**Pass** for the proof of [](#conj:kls) in the fingerprinted composition
dossier. This is an independent full review of the adapter: the reviewer
received repository paths and a mission without the author's conversation,
and authored none of the proof. The upstream [](#thm:sz-v2-kls) has now
been certified in `research/reviews/2026-10-06-sz-v2-profile-review.md`
and registered `proved`. Its canonical finite-energy statement is exactly
the input used here.

Every step of the adapter was checked:

1. Isotropy implies full-dimensional support, and a full-dimensional
   log-concave law has a Lebesgue density. The almost-everywhere gradient
   of a locally Lipschitz function is therefore defined almost everywhere
   for the law, and its squared integral is an extended nonnegative number.
2. At finite energy, the upstream theorem applies with precisely the
   given dimension, isotropic law, and function. It supplies both square
   integrability and the bound with one universal constant. No additional
   regularity, approximation, or uniformity assumption is inserted.
3. For a square-integrable function, expansion of the square around its
   mean proves that $\inf_c\int|f-c|^2d\mu$ is ordinary variance.
   Outside $L^2$, finiteness for any finite $c$ would contradict
   $|f|^2\le2|f-c|^2+2c^2$. The extended variance is thus infinite.
   At infinite energy the inequality holds in the extended nonnegative
   reals, without subtracting an undefined mean. This makes explicit
   the canonical statement's usual interpretation; it does not replace
   its finite-energy conclusion by a weaker one.
4. The resulting common Poincare bound implies the Cheeger formulation
   through [](#eq:cheeger-two-sided). I read the actual published
   [Klartag 2023 paper, equation (1.4), page 3](https://arxiv.org/pdf/2303.14938),
   and checked that its $\psi_\mu$ is the manuscript's $h_\mu^{-1}$.
   The forward implication is $h^{-2}\le\pi C_P\le\pi C$, and
   the reverse is $C_P\le4h^{-2}\le4c^{-2}$. Both constants and
   directions are correct. This established comparison, also attributed
   to the background literature in the dossier, is the only external
   result needed beyond the certified theorem.

The conclusion therefore implies the unchanged canonical [](#conj:kls),
with its order of quantifiers and equivalent Cheeger clause. The universal
constant is selected before the dimension, law, and function. Isotropy,
log-concavity, local Lipschitz regularity, and the finite/infinite energy
split account for every hypothesis; none is unstated or unused. No
`assumes` antecedent remains. No `bounded_by` relation is attached to
the target, and no sharper structural inequality is inferred.

### Dependencies and proof provenance

The only actual theorem premise is [](#thm:sz-v2-kls). It is used as a
certified node, not as an unchecked preprint assertion. Its complete proof
and the earlier profile and analytic proofs are outside this adapter
review's scope. The current theorem statement and its registered pass
report were read. A traversal of its 32-node dependency closure contains
no open node, no BKL node, and no [](#conj:kls). Thus this composition
has neither an open dependency nor circular use of its target.

The collective target dependency list also contains
[](#thm:bkl-tilt-bound), [](#thm:bkl-tilt-criterion), and
[](#lem:bkl-analytic-foundations). Their statements were read and are
fingerprinted by the checker, but none is used by this adapter. They
belong to the other proof record. In particular, this proof uses neither
the BKL conclusion, its coefficient corollaries, nor the target's already
recorded proved status. This provenance distinction does not assert
disjointness of all upstream analytic foundations.

The full `UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py` reported
no MyST error. Its only failure was the old BKL KLS review's missing
fingerprint for the newly added collective dependency `thm:sz-v2-kls`.
That separate proof-record update is covered by
`research/reviews/2026-10-06-bkl-kls-second-proof-review.md`.
The fresh checker output from
`--fingerprint solutions/sz-v2-kls-composition.md` is recorded above.

## Corrections

None.

## Exclusions

This report certifies the canonical-target adapter only. It does not
recertify the Song–Zhang profile theorem or its proof, the BKL chain or
its composition, manuscript prose, a claim of priority, or any stronger
CMH, gate-zero, or occupation conclusion. No numerical or run artifact
is evidence.

## Proposed record

Keep [](#conj:kls) `proved`, with its current references and dependency
union. Add the following second proof record, preserving the BKL record:

```yaml
artifact: solutions/sz-v2-kls-composition.md
review: research/reviews/2026-10-06-sz-v2-kls-composition-review.md
```
