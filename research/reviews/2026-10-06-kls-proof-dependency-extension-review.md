---
verdict: pass
authors:
  - bkl_suspension_author, gpt-6-astra, 2026-10-06
  - plan_sz_architecture, unknown, 2026-10-06
  - orchestrator, gpt-6.1-sol, 2026-10-06
reviewer: reviewer, gpt-6-astra, 2026-10-06
fingerprints:
  solutions/bkl-suspension-kls.md: dc4bcc0cfacfcb4a77548af89df6247179cc497ee2f7fb32ed398eb6f2d02b99
  prop:bkl-suspension: e63452cb08c1c930757ec5b8733c971f652626daf45e0ccbc3c9fbe292be084e
  def:bkl-tilt-cumulants: 43636c8506cef53a8ed43a8231a955e160d704cc899cc248c5e08425ab5f449c
  thm:bkl-tilt-bound: b14ed0af1b0f660928c9d507b8567b89ff97bbbd8620a138eba3fecf5aadf82f
  thm:bkl-cumulant-bound: f494b6a9fe460588d0b885054be670483c49ffb759e6239e6f9b3651303ce275
  lem:bkl-analytic-foundations: 7657fb2bb9597db83ab252a2b5ba773b834bf96f7d71f6cc27377648b7e2314d
  prop:bkl-tilt-appell-duality: 200cfcdd5bc5aed9562b945189b1ccd942730024ac955f0988db40841d86755e
  conj:kls: b34221c5440f365f12cb6529324aed7a62b355236e5a037761de51f02adeab69
  thm:bkl-tilt-criterion: 050f47b3ff5487f31a0b08990786dee5bef2a5ce39b8c85bb5982ea1410ab344
  thm:sz-v2-kls: f5dfe05f2a9880082765a4f61d7fd0cfd36cc8e259615b54280e37b1380ee16e
  thm:bk-explicit-poincare: ed29bf2fbe5c374559d511d8ce54e010095503ae0794aff0218b323e1062045a
  solutions/sz-v2-kls-composition.md: d70f79bfd4303082a4284b1ad3fa780a4f7e81d592dae5e0459116a6625d4d0a
---

## Findings

Re-review of `research/reviews/2026-10-06-bkl-kls-second-proof-review.md`
and `research/reviews/2026-10-06-sz-v2-kls-composition-review.md`, restricted
to their certifications of [](#conj:kls). **Pass for each of the two
composition dossiers.** This reviewer has no authoring history for either
proof and received only repository paths and the dependency-extension
assignment. Earlier independent conclusions are retained only after the
baseline and scope checks below.

### Verified baseline and complete change

The candidate revision `4fe3bd1200cfbc9863e4754f181328f4048b0691` added both
prior reports. I created an isolated worktree at
`/tmp/kls-bk-review-baseline`, built its historical manuscript there, and ran
the fingerprint command for both dossiers. Every dossier and statement
fingerprint in both prior reports matched the historical output exactly.
No historical manuscript was built in the current tree. The checkout used
the same pinned MyST installation; the package manifests have no diff.

The current two dossiers have empty Git diffs against that baseline.
Current checker-generated fingerprints also match every old dossier and
statement fingerprint. The only additional required statement is
[](#thm:bk-explicit-poincare). The target's collective `depends_on` list
adds that node and its `references` adds the BK bibliography key; the
canonical target and all actual premises of these two proofs are unchanged.
The current `--diff` output confirms zero changed fingerprinted items and
exactly two errors: each old KLS record lacks the newly required BK statement
fingerprint. Thus the consequence of this graph edit can be delimited.

### Actual proof interfaces and unaffected conclusions

I read the final BKL composition and the Song–Zhang adapter, along with the
current canonical target and their direct input statements. The BKL
composition still selects one universal $K\ge1$ from
[](#thm:bkl-tilt-bound), uses $R=\sqrt{2K}$ in
[](#thm:bkl-tilt-criterion), obtains $C_P\le2CK$ on regular isotropic laws,
then uses [](#lem:bkl-analytic-foundations) for isotropic approximation and
scalar stability. The constants remain uniform before dimension, measure,
degree and test are selected. Its mathematical premises are those three
nodes, not the BK or Song–Zhang endpoint.

The Song–Zhang adapter still uses only [](#thm:sz-v2-kls) for the
finite-energy conclusion, including $L^2$ integrability. Its extended
variance is ordinary variance on $L^2$ and infinite otherwise, and the
infinite-energy inequality is interpreted in the extended nonnegative
reals. The constant is selected uniformly before dimension, measure and
function. Its proof uses neither a BKL nor a BK conclusion.

The earlier checks of approximation, finite-energy domains, extended
variance and the two-sided Cheeger comparison are retained: the relevant
steps and statements are unchanged and the new collective edge enters
none of them. In particular the previously source-checked comparison
$h^{-2}\le\pi C_P$ and $C_P\le4h^{-2}$ continues to give exactly the
target's equivalence, without any new source result being invoked.
No hypothesis or constant has been strengthened, removed or newly supplied.
Neither proof has an open `assumes` antecedent or a `bounded_by` edge.

A traversal of the actual BKL inputs' dependency closure has 17 nodes;
the Song–Zhang input's closure has 32. Both contain only proved/defined
nodes, no BK node, and no [](#conj:kls). Thus the new collective edge
creates no dependence of these proofs on their target or the BK proof.
This says nothing about disjointness of their other analytic foundations.

I also checked the added canonical [](#thm:bk-explicit-poincare): it
asserts the uniform constant $1+2\cdot10^{16}$ for covariance at most
identity, finite-energy locally Lipschitz tests, their $L^2$ integrability,
and intrinsic affine-support gradients. Its statement fingerprint matches
`research/reviews/2026-10-06-bk-outer-review.md`, with the dossier's
subsequent status-only cleanup carried by
`research/reviews/2026-10-06-bk-outer-editorial.md`. The ledger now records
it as proved. It is included here solely because the graph uses a
collective dependency union; it is not a premise of either proof under
review. Its internal proof is not recertified here.

The current full-build `uv run scripts/check.py --diff` reported no MyST
error and failed only for the two expected missing fingerprints noted
above. The final fingerprint command for both dossiers succeeded and its
output is recorded verbatim in the front matter. The original reviews
remain unchanged.

## Corrections

None to the proofs or canonical statements. Keep [](#conj:kls) `proved`,
with its current collective references and dependencies. In that node
only, replace the review pointers for these two existing records:

```yaml
- artifact: solutions/bkl-suspension-kls.md
  review: research/reviews/2026-10-06-kls-proof-dependency-extension-review.md
- artifact: solutions/sz-v2-kls-composition.md
  review: research/reviews/2026-10-06-kls-proof-dependency-extension-review.md
```

Keep all other records, including records for other nodes in the multi-node
BKL dossier, unchanged. The separate BK KLS composition requires its own
independent review and is not covered by these proposed records.

## Exclusions

Only the two existing canonical-target compositions are certified by this
re-review. The checker fingerprints other claims associated with the
multi-node BKL dossier, but this report grants them no new certification.
Upstream BKL, Song–Zhang and BK proofs, the new BK KLS composition,
manuscript prose, attribution and priority, and stronger structural
inequalities are outside scope. No numerical artifact is proof evidence.
