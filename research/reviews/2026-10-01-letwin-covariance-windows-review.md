---
verdict: pass
authors:
  - researcher_consequences, gpt-6-astra, 2026-10-01
reviewer: reviewer_consequences, gpt-6-astra, 2026-10-01
fingerprints:
  solutions/letwin-covariance-windows.md: e8ec8b28b10554d2112023e4daa00f27cad26f91a1f7fff69823a12b3e64b47f
  prop:letwin-kappa: 95b731e551b7d7bc79b4aa8f98b04c61ecbd81f2e93797788409e25124ad2187
  thm:letwin-qcts: 8e2ac0819f46db553fe83a6f3034436816565262316c2e6bde7d81baead1a082
  cor:letwin-window: e10c2dd5189699a298ec6c3cbca5a7bc3b7aca0a1a0cae354bd58c5c2d4ed211
  cor:KI-letwin: 579b447dcfd2b604059e840dbdad5378c9daf5f4d1369b1bf6a30652414f335c
  thm:V2-window: 989d2a3691b5d3f5a22772603a3ba508912268992bb373396cc0ef3aca5bf64c
  thm:KL-window: c8805f6f7be529a3a27f935a273c4a3253861fe59ebc6b52dc416a68cdd915f7
  cor:V2-implies: d872e6355975f6888991dfea6e2d77384f18c164aa95b21a2369b98214e6a3d0
---

# Covariance windows: certification review

## Findings

**Pass, jointly for `prop:letwin-kappa`, `cor:letwin-window`, `cor:KI-letwin` and `thm:V2-window`, in the dependency-ordered certification batch described below.** Every local deduction, external application and limit step checks out. The upstream Letwin nodes are now `proved` on `research/reviews/2026-10-01-letwin-imports-r2-review.md`; the source dependency is discharged before this verdict. The source-reduction prerequisites are proved and certified by the companion report written in this same audit, and their records must be applied first.

Lens: `certify`, fresh context without the authoring conversation. The assignment supplies the identities. Only the two requested reports were written.

### Statements and dependency closure

| Node | Canonical location | Dossier lines | Agreement |
|---|---|---|---|
| `prop:letwin-kappa` | `modules/30-covariance-technology.md:78` | 30–60 | Same conditional bound and normalization, including dimension one. |
| `cor:letwin-window` | `modules/30-covariance-technology.md:106` | 63–129 | Same unconditional moments for $n\ge2$; the dossier makes explicit the stronger uniform choice of time constant in $p$. |
| `cor:KI-letwin` | `modules/30-covariance-technology.md:135` | 132–158 | Same conditional exponent-one window for $n\ge3$ and interface integration. |
| `thm:V2-window` | `modules/16-product-stress.md:141` | 161–203 | Same conditional longer window and independent shorter fallback, with unconditional all-cut fallback only for products. |

The source, third-moment, covariance-window, (V2)-reduction and published `thm:KL-window` statements were read against every use. The auxiliary `ass:KI`, `cor:loglog`, interface definition and all-cut statement were checked to ensure that no additional conclusion or universal horizon is substituted. Upstream regularity and moment-map statements were read to locate the boundary of reliance on the separate source certification.

The external Letwin source and its moment-map dependency have valid `proved` records at final inspection; `thm:KL-window` is established on references. Open statuses among the seven consequences are the claims proved in this joint audit, not unproved premises: the companion report establishes the three source-reduction nodes first, this dossier establishes the third-moment implication and unconditional window next, and then the two interface statements. No open external dependency remains. Apply the records in that order or as one dependency-closed batch; never promote `thm:V2-window` alone while leaving `cor:V2-implies` open.

Retain Letwin in `assumes` for the three explicitly conditional statements. For the unconditional moment corollary, invoking the third-moment implication is legitimate because its antecedent is now actually discharged, not erased.

### Primary sources checked

I read [Klartag–Lehec, arXiv:2203.15551v2](https://arxiv.org/html/2203.15551v2): equation (23), Lemma 2.2 and proof, Lemmas 5.1–5.3 and Corollary 5.4 with proofs. Its Schatten two-norm matches Hilbert–Schmidt. The log-trace-exponential calculation, eigenvalue-collision continuity, stopped drift and quadratic variation estimates establish the fixed-time tail with $\beta=2\log n$ for $n\ge2$. Its covariance cap then gives the moment estimate. Lemma 2.2 identifies the observation tilt law. The time constant is independent of the real exponent.

I also read [Klartag–Lehec notes, arXiv:2406.01324v2, Theorem 61 and proof](https://arxiv.org/html/2406.01324v2#S7). The theorem controls a time-supremum event for arbitrary isotropic log-concave laws. Its stopped proxy has drift of order $t^{-1/2}\log n$ below the covariance threshold and bounded quadratic variation; the maximal martingale tail yields the shorter squared-logarithm window without Letwin. No requested primary source was unavailable.

### Mathematical checks

**Lines 32–60: third moments.** The symmetric matrix $M$ is finite. Centering cancels the trace term and isotropy makes the linear factor have second moment one. The contraction is exactly $\|M\|_{\mathrm{HS}}^2$. Cauchy–Schwarz gives $\|M\|^4\le8\|M\|^2$; treating zero separately before division yields $2\sqrt2$. Neither supremum introduces a dimensional factor.

**Lines 65–90,125–129: constants and dimensions.** Maximizing $y^pe^{-y/C}$ at $y=Cp$ works for every real $p\ge1$, with only the moment constant depending on $p$. Substitution of $\kappa_n^2\le8$ gives one $c=1/(8C)$ for all exponents. The window is restricted to $n\ge2$, so $\log n$ is positive. Time zero is handled separately. This checks the precise quantifier order rather than interpreting a constant depending on $p$ as universal.

**Lines 94–123: nonsmooth initial laws.** The coupling $X_\varepsilon=(X+\varepsilon G)/\sqrt{1+\varepsilon^2}$ preserves isotropy and log-concavity and supplies smooth positive laws. For fixed positive $t$, the coupled observation parameters converge almost surely. Gaussian Bayes likelihood identifies the covariance law of localization. For a convergent parameter sequence, likelihood-weighted polynomials through degree two are uniformly bounded and have uniformly vanishing tails; on compact sets their parameter dependence is uniformly continuous. Weak convergence therefore passes the normalization and first two moment integrals. The limiting normalizer is positive, so posterior covariances and their operator norms converge almost surely. Fatou transfers every nonnegative real moment bound with the same constants. No uniform integrability or whole-path convergence is assumed. At zero covariance is identity.

**Lines 134–158: KI and interface.** The $p=1$ specialization supplies exactly the claimed KI exponent in its $n\ge3$ domain. Reducing $c_0$ to at most $\log3$ ensures $t_1\le1$. The early constant bound and later Brascamp–Lieb cap integrate to $C_1t_1+\log(T/t_1)$ for $t_1\le T\le1$, hence the stated logarithmic-logarithmic bound. No near-worstness, cut or geometric premise of the downstream `cor:loglog` is removed.

**Lines 163–203: V2 and independent fallback.** Taking $p=2$ and integrating proves (V2) on every deterministic subinterval. The general all-cut application still uses the explicit Letwin antecedent; its product implication is independent. The fallback uses containment of the fixed-time threshold event in the published supremum event. Splitting there and applying the covariance cap gives $1+t^{-2}e^{-1/(Ct)}$. The latter term has maximum $4C^2e^{-2}$, establishing the asserted uniform second-moment constant. At zero $X_0=0$. Taking the smaller time constant and larger bound makes both windows simultaneous. This does not promote fixed-time moments to a moment of a time supremum.

### Hypotheses and fences

All used hypotheses are present: isotropic log-concavity, finite-time localization, unit directions, real $p\ge1$, $n\ge2$ for the logarithmic windows, $n\ge3$ for KI, and the displayed interval for $T$. Product structure is needed only for the independent all-cut consequence. Positive likelihood preserves full affine support, hence positive-definite posterior covariance, at finite times. No singular covariance is inverted. None of the four nodes has `bounded_by`. The source reduction retains its covariance-square loss; both time horizons still shrink with dimension, and the interface retains its logarithmic loss. No universal-horizon Carleson assertion follows.

## Corrections

None. No step remains unverified within scope. The formerly open upstream dependency was resolved by its separate passing review and ledger record before this verdict; this dossier does not certify that theorem itself.

## Verification and concurrency

The final `UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py` completed MyST without a dossier error after escalation for the sandbox spawn failure. It exited 1 on an unrelated concurrent mismatch: `prop:weighted-spectator-obstruction` records an older fingerprint of `ass:weighted-package`. That node and statement are outside this dependency closure; they are not certified by this review. Both fingerprint commands succeeded afterward. The front matter reproduces this dossier's output exactly.

A concurrent change to the ledger and `modules/14-eldan-statements.md` was detected before report creation. I reread the changed module and affected ledger neighborhoods, including both new upstream proof records, and the new upstream review. The full check and fingerprints were rerun. Final byte comparisons cover both dossiers, modules, ledger, brief, specification and the new upstream review. No concurrent edits were reverted.

## Exclusions

No recertification of Letwin's source or boundary repair, no sharp $\kappa_n\le2$, no supremum moment bound, no dimension-free horizon, no KLS or universal all-cut Carleson theorem, and no removal of downstream geometric premises. Previously certified inputs are used at their recorded scope. Surrounding manuscript status prose is outside the certify lens.

## Proposed certification records and handoff

Apply the companion source-consequence records first, then the records below in order, preserving all existing edges. Together the two reports certify the seven-node dependency-closed batch; neither report itself edits the ledger.

```yaml
files:
  - research/reviews/2026-10-01-letwin-covariance-windows-review.md
deltas:
  - file: research/program/ledger.yaml
    node: prop:letwin-kappa
    set:
      status: proved
      proofs:
        - artifact: solutions/letwin-covariance-windows.md
          review: research/reviews/2026-10-01-letwin-covariance-windows-review.md
    preserve:
      assumes: [thm:letwin-qcts]
  - file: research/program/ledger.yaml
    node: cor:letwin-window
    set:
      status: proved
      proofs:
        - artifact: solutions/letwin-covariance-windows.md
          review: research/reviews/2026-10-01-letwin-covariance-windows-review.md
    preserve:
      depends_on: [prop:letwin-kappa, thm:letwin-qcts]
  - file: research/program/ledger.yaml
    node: cor:KI-letwin
    set:
      status: proved
      proofs:
        - artifact: solutions/letwin-covariance-windows.md
          review: research/reviews/2026-10-01-letwin-covariance-windows-review.md
    preserve:
      depends_on: [cor:letwin-window]
      assumes: [thm:letwin-qcts]
  - file: research/program/ledger.yaml
    node: thm:V2-window
    set:
      status: proved
      proofs:
        - artifact: solutions/letwin-covariance-windows.md
          review: research/reviews/2026-10-01-letwin-covariance-windows-review.md
    preserve:
      depends_on: [cor:letwin-window, thm:KL-window, cor:V2-implies]
      assumes: [thm:letwin-qcts]
```
