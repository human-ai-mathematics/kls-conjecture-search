---
verdict: pass
authors:
  - bkl_suspension_author, gpt-6-astra, 2026-10-06
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
---

## Findings

Re-review of `research/reviews/2026-10-06-bkl-suspension-kls-review.md`,
restricted to its certification of [](#conj:kls). **Pass**, following a
full scoped check of the KLS composition in the dossier's final theorem
and proof. This reviewer received no BKL authoring conversation and
authored none of the proof. The new report changes no earlier report.

No matching Git historical revision is available: the BKL dossier and
earlier report are untracked in this working tree. Therefore this is not
a limited diff review based on a claimed historical commit. Before the
dependency change, the checker's output matched every dossier and
statement fingerprint in the old report. A pre-change snapshot was also
preserved at `/tmp/kls-bkl-pre-secondproof-baseline`. The current raw
SHA-256 values of the dossier and old report are respectively
`0bc7bdb2d008edc7868606a7e0bb74d0ab97cef683bf4ffc3d4873a5205f72a4`
and `25dc82dced004ec72a1d996359bf2968cec8b30d75503a3bf3013740ec2f7567`,
matching that snapshot. The final checker output above still matches all
old certified fingerprints; its sole added statement is [](#thm:sz-v2-kls).

The change is to the target's collective dependency list and references:
the separately certified Song–Zhang theorem now accompanies the three
BKL inputs. Neither the canonical KLS statement nor the BKL argument has
changed. A shared dependency list is not a declaration that every proof
uses every listed node.

### Full check of the composition

1. The actual quantitative input is [](#thm:bkl-tilt-bound): a single
   universal $K\ge1$ gives the Taylor bound $(2K)^{d/2}$ simultaneously
   for every degree and test. Restricting its all-law statement to regular
   isotropic laws satisfies the hypotheses of [](#thm:bkl-tilt-criterion).
   In that criterion take $R=\sqrt{2K}\ge1$. Its conclusion is exactly
   $C_P\le CR^2=2CK$, with both constants chosen independently of the law
   and dimension. There is no exchange of quantifiers over degrees.
2. The approximation clause of [](#lem:bkl-analytic-foundations) supplies
   isotropic BKL-regular approximants for each isotropic log-concave law.
   The common bound $2CK$ applies to every approximant. For a fixed compact
   smooth $q$, the functions $q,q^2,|\nabla q|^2$ are bounded continuous,
   so weak convergence passes both sides of the scalar inequality.
   The certified scalar stability clause extends it to locally Lipschitz
   finite-energy functions, including their $L^2$ integrability.
3. The canonical statement's unrestricted function notation has the usual
   extended interpretation when energy is infinite. Precisely, use
   $\inf_{c\in\mathbb R}\int|f-c|^2d\mu$ for extended variance. It is
   ordinary variance on $L^2$, and is infinite outside $L^2$, because
   $|f|^2\le2|f-c|^2+2c^2$. Thus infinite energy imposes no additional
   finite upper bound and causes no undefined subtraction of a mean.
   Isotropy makes a log-concave law full-dimensional, so its Lebesgue
   density also makes the locally Lipschitz gradient well-defined almost
   everywhere for this integral.
4. The target's Cheeger equivalence follows from the established
   comparison [](#eq:cheeger-two-sided). I checked it directly against
   the published [Klartag 2023 paper, equation (1.4), page 3](https://arxiv.org/pdf/2303.14938),
   including its reciprocal-isoperimetric convention. It gives
   $h^{-2}\le\pi C_P$ and $C_P\le4h^{-2}$. Therefore a universal
   Poincare bound gives a uniform positive Cheeger bound and conversely.
   This comparison asserts no universal KLS estimate by itself.

The actual source composition, the proof of Theorem 1.1 in
[BKL v1, Section 7](https://arxiv.org/html/2610.05474v1#S7), was checked
in the supplied full local source. It uses the same base $\sqrt{2K}$
and obtains $2CK$. The local dossier explicitly supplies the approximation
step. The suspension and uniform-coefficient conclusions retain their
existing independent certification, and the criterion and foundations
retain theirs; their internal proofs are not imported afresh from the
preprint or recertified by this report.

The hypotheses used are isotropy, log-concavity, finite dimension and
local Lipschitz regularity, with finite Dirichlet energy for the substantive
inequality. Regularity is a temporary restriction removed by the certified
approximation. The all-degree/all-test coefficient bound and uniformity
of its constant are needed and supplied. No additional hypothesis,
unfulfilled antecedent, or open proof dependency remains. These nodes have
no `bounded_by` relation; no sharper structural conclusion is inferred.

### Separate provenance and validation

The actual BKL premises are exactly [](#thm:bkl-tilt-bound),
[](#thm:bkl-tilt-criterion), and [](#lem:bkl-analytic-foundations).
[](#thm:sz-v2-kls) is fingerprinted because it now belongs to the target's
collective graph, but it is not a premise of this proof. Its current
canonical statement and independent pass report
`research/reviews/2026-10-06-sz-v2-profile-review.md` were checked for that
graph change. Traversal of each BKL input's dependencies finds neither
the target nor the Song–Zhang v2 endpoint, and no open node. This does not
claim that the two approaches share no analytic foundations.

The full `UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py` built
without MyST errors. Its sole failure was the expected missing
`thm:sz-v2-kls` fingerprint in the old review still attached to the KLS
record. The fresh `--fingerprint solutions/bkl-suspension-kls.md` output
is recorded verbatim above. Registration of this report repairs that
proof-record mismatch; the orchestrator should then validate the tree.

## Corrections

None to the proof or canonical statement. Replace only the KLS proof
record's review pointer as below. Do not edit the old report's fingerprints.

## Exclusions

This report certifies only the BKL composition for [](#conj:kls).
It does not newly certify [](#prop:bkl-suspension) or
[](#thm:bkl-tilt-bound), despite their inclusion in the checker-generated
fingerprints of this multi-node dossier. Their existing proof records
remain attached to the old review. Nor does this report recertify upstream
BKL proofs, the Song–Zhang theorem, its profile proof, the separate adapter,
manuscript prose, a priority claim, or any stronger structural inequality.
No run artifact is mathematical evidence.

## Proposed record

Keep [](#conj:kls) `proved`, with its current references and dependency
union. In that node only, set its existing BKL record to:

```yaml
artifact: solutions/bkl-suspension-kls.md
review: research/reviews/2026-10-06-bkl-kls-second-proof-review.md
```

Leave every other record naming the old review unchanged.
