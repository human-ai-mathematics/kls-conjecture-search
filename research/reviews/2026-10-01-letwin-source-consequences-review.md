---
verdict: pass
authors:
  - researcher_consequences, gpt-6-astra, 2026-10-01
reviewer: reviewer_consequences, gpt-6-astra, 2026-10-01
fingerprints:
  solutions/letwin-source-consequences.md: 497d91f85365df9cf56c3c3ec88930902cdd5428908f9f6e683d655eebb0ea0c
  cor:qcts-source: 756c3ea163d568cfa1fd2d20f541f3c22fce1309ceffa9425dd0dfb2273dbf80
  thm:letwin-qcts: 8e2ac0819f46db553fe83a6f3034436816565262316c2e6bde7d81baead1a082
  prop:stein-rep: 809545792ca08860114a8276ff5b61febda2930cfd2b8b0f3a1a5ca1a0d00e6a
  thm:covariance-bound: 2e75251b1b26d1b59f51189995e4451c1aca795f438da0e9ddb5b4afc87f136a
  lem:product-qcts: 93f2e2a3230253762243cd991c55f11de59b986c8daf848ecd044256ef2302eb
  cor:V2-implies: d872e6355975f6888991dfea6e2d77384f18c164aa95b21a2369b98214e6a3d0
---

# Source consequences: certification review

## Findings

**Pass, jointly for `cor:qcts-source`, `thm:covariance-bound` and `cor:V2-implies`.** The deductions prove their canonical statements. At final inspection the upstream `thm:letwin-qcts` and `thm:letwin-moment-map` are both `proved`, with valid records naming `research/reviews/2026-10-01-letwin-imports-r2-review.md`. This verdict does not anticipate an unfinished source review or certify the source theorem itself.

Lens: `certify`, fresh context without the author's conversation. Identities are supplied by the assignment. Only the two requested reports were written. No proof, ledger, manuscript or bibliography was edited.

### Statements and dependencies

| Node | Canonical location | Dossier lines | Agreement |
|---|---|---|---|
| `cor:qcts-source` | `modules/29-qcts-obstruction.md:70` | 26–81 | Positive-definite covariance, all nontrivial masses, constants 8 and 17, and exact-balance case agree. |
| `thm:covariance-bound` | `modules/16-product-stress.md:94` | 84–134 | General conditional branch and independent product branch agree. |
| `cor:V2-implies` | `modules/16-product-stress.md:112` | 137–171 | Same deterministic-interval premise, measure-by-measure horizon, constants, and independent variance-process assertion. |

The source statement, `prop:stein-rep` and `lem:product-qcts` were read against their uses. The latter two are already `proved`, with valid certifications under the full check. The source's dependency closure through `def:qcts`, `thm:letwin-moment-map` and `thm:regular-moment-map-compact-target` is discharged; their statements and the newly recorded upstream review were read. This audit uses that certification, not a new proof of Letwin.

The remaining open statuses within this dossier belong to the three results proved here, in the acyclic order `cor:qcts-source`, `thm:covariance-bound`, `cor:V2-implies`. Promote them together or in that order; none is used as an unproved external premise. Preserve `thm:letwin-qcts` in `assumes` for the last two, because their canonical statements remain explicit implications even now that their antecedent has been proved.

### Line-by-line mathematical checks

**Lines 28–64: color, whitening and duality.** Invertible whitening preserves log-concavity and cut mass and transforms conditional covariance by congruence. The normalized color has mean zero and second moment one. Dividing the certified color identity by the square root of the mass product gives exactly the dossier's contraction. Polynomial moments are finite. Cauchy–Schwarz and the quadratic input give constant 8; symmetric Hilbert–Schmidt duality uses the contrast itself as test, with the zero case separated. Left and right multiplication by the covariance square root produce exactly the squared operator-covariance loss after squaring. No dimensional or trace factor is lost.

**Lines 66–81: coarse balance.** Covariance decomposition gives the rank-one matrix $B=s\delta\delta^T\preceq A$, hence $r=\operatorname{Tr}B\le\|A\|_{\mathrm{op}}$. The correction coefficient $2(q-p)^2/s$ is at most one on $[1/3,2/3]$. Thus the constant is $16+1=17$. At exact balance the correction vanishes before estimating, leaving 8.

**Lines 99–115: posterior domain.** An isotropic law has full affine support. At every finite positive time, its Gaussian tilt has positive likelihood, finite normalization and all polynomial moments, and is equivalent to the original law. Full affine support therefore persists and covariance is positive definite. At zero it is identity. Centering preserves the contrasts. The deterministic static estimate applies to every admissible posterior, avoiding an uncountable intersection of fixed-time exceptional events. Replacing covariance norm by $1+X_t$ yields constant 34. No singular inverse or infinite-time posterior is used.

**Lines 117–134 and 166–171: product branch.** The likelihood factors coordinatewise and remains a product after centering. The anisotropic product quadratic estimate gives $s\|K\|^2\le C_*\|A\|^2$ and then source constant $2C_*+1$, or $2(2C_*+1)$ in excess form. The cut need not be a product. Coordinate tilt drifts depend only on their coordinate and time; strong uniqueness of the one-dimensional localization equations and independent Brownian coordinates give independent coordinate variance processes. The covariance norm is their maximum. These arguments use no Letwin input.

**Lines 139–165: integration.** Nonnegative measurable integrands permit Tonelli before finiteness is asserted. The (V2) premise then supplies the finite bound on each deterministic interval for this measure. Balance holds before the coarse exit; the single exit endpoint has zero time measure. The bound is uniform in the fixed cut and gives exactly $C_0=C(1+K)$, $C_1=\alpha=0$. No random-interval assertion or cut chosen after observing localization is introduced.

### Hypotheses, sources and fences

Used hypotheses are centered log-concavity and positive-definite covariance for the static statement, nontrivial cut mass, coarse balance for its correction, isotropy and finite times for localization, product factors for the independent branch, and finite $T_0,K$ with the stated every-interval (V2) premise. All are present or supplied by manuscript notation; no extra smoothness is needed. The localization tilt equation and strong-solution setup match [Klartag–Lehec v2, Section 2, equations (18)–(19)](https://arxiv.org/html/2203.15551v2#S2). Other substantive inputs are the certified repository statements just identified.

None of the three nodes has a `bounded_by` edge. The covariance-square loss is retained. A bound for one measure on its specified horizon is never asserted on a universal positive horizon over all dimensions. In particular this is not a certification of `ass:all-cut-carleson`.

## Corrections

None. No analytic step remains unverified within the stated scope. The upstream dependency was open during the initial audit, but its passing repair review and ledger transition were both read before this verdict.

## Verification and concurrency

The final full command `UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py` completed its MyST build without a dossier error, but exited 1 on one unrelated concurrent certification mismatch: `prop:weighted-spectator-obstruction` records an older fingerprint of `ass:weighted-package`. This does not touch any statement or dependency in these two dossiers; no repair of that separate certification is proposed here. The initial sandboxed build failed at Node/npm spawning; escalation resolved it. Both required fingerprint commands were run afterward; the block above is the exact output for this dossier.

The last change check detected concurrent edits to the ledger and `modules/14-eldan-statements.md`. I reread the changed file and affected ledger neighborhoods, including the upstream proof records, and read the new upstream review. Checks and fingerprints were regenerated on that tree. Final byte comparisons cover the dossiers, modules, ledger, brief, specification and new upstream review. Concurrent edits were preserved.

## Exclusions

This does not recertify Letwin's source or boundary repair, KLS, a universal-horizon Carleson estimate, singular-covariance whitening, sharpness, or downstream geometric inputs. Surrounding manuscript status prose is outside the certify lens.

## Proposed certification records and handoff

Apply the following in dependency order; preserve every existing relation. This report itself changes no ledger status. Its records precede application of the companion covariance-windows report.

```yaml
files:
  - research/reviews/2026-10-01-letwin-source-consequences-review.md
deltas:
  - file: research/program/ledger.yaml
    node: cor:qcts-source
    set:
      status: proved
      proofs:
        - artifact: solutions/letwin-source-consequences.md
          review: research/reviews/2026-10-01-letwin-source-consequences-review.md
    preserve:
      depends_on: [thm:letwin-qcts, prop:stein-rep]
  - file: research/program/ledger.yaml
    node: thm:covariance-bound
    set:
      status: proved
      proofs:
        - artifact: solutions/letwin-source-consequences.md
          review: research/reviews/2026-10-01-letwin-source-consequences-review.md
    preserve:
      depends_on: [cor:qcts-source, lem:product-qcts]
      assumes: [thm:letwin-qcts]
  - file: research/program/ledger.yaml
    node: cor:V2-implies
    set:
      status: proved
      proofs:
        - artifact: solutions/letwin-source-consequences.md
          review: research/reviews/2026-10-01-letwin-source-consequences-review.md
    preserve:
      depends_on: [thm:covariance-bound]
      assumes: [thm:letwin-qcts]
```
