---
verdict: pass
authors:
  - researcher_letwin, gpt-6-astra, 2026-10-01
reviewer: reviewer, gpt-6-astra, 2026-10-01
fingerprints:
  solutions/thm-letwin-kls.md: 42d88e3c443168ffa915a21ccf32c1e7e5c58d5eb6c8503e1dcc862bd6ef910e
  thm:letwin-kls: a80dda9a9d19fdac6e98011d9225919ac646b8c343af0c6b1f8509b2e73f49ad
  prop:letwin-kappa: 95b731e551b7d7bc79b4aa8f98b04c61ecbd81f2e93797788409e25124ad2187
  thm:letwin-qcts: 8e2ac0819f46db553fe83a6f3034436816565262316c2e6bde7d81baead1a082
  thm:improved-lichnerowicz: e95e127c46fbf098fb23cb186b9d7312b213063339704596555ab33696f2968f
---

# Independent certification of Letwin's general KLS bound

## Findings

**Pass for `thm:letwin-kls`.** Lens: `certify`. This review started without the conversation that authored or directed the dossier. The checkpoint identifies the author as researcher_letwin, gpt-6-astra, 2026-10-01. The repository specification and reviewer instructions were read first. The reviewed artifact is `solutions/thm-letwin-kls.md`; no mathematical artifact was edited.

### Statement and dependencies

Dossier lines 47–58 agree with `modules/04-family-moment-map.md:270`: one universal constant works for both suprema over every isotropic log-concave probability law in each integer dimension $n\ge2$, with exponents $1/2$ for the Poincaré constant and $1/4$ for inverse Cheeger. The canonical normalizations in module 00 were checked.

All three direct dependencies are proved. The directional Hilbert–Schmidt parameter in `prop:letwin-kappa` is exactly the one used here. Its antecedent is discharged by the separately certified all-law, all-symmetric-matrix `thm:letwin-qcts`; that premise is explicitly a direct dependency of the present node. `thm:improved-lichnerowicz` has the required covariance operator norm and curvature parameter. No open dependency or remaining assumption is used. The quadratic import's proof is not being re-certified in this review; it is an existing certified node, whose statement and active proof record were checked.

### Sources checked

- [Letwin 2607.24164v1](https://arxiv.org/html/2607.24164v1), Theorem 1.1 and its complete introductory proof: the source reduces its claim to its quadratic theorem through the third-moment parameter and a cited spectral bridge. I checked that proof, including its matrix identity and Cauchy–Schwarz step. The present dossier supplies the intervening bridge explicitly.
- [Klartag–Lehec 2203.15551v2](https://arxiv.org/html/2203.15551v2), Section 5 parameter definition and Corollary 5.4 with its proof: the Schatten two-norm is Hilbert–Schmidt, and the $p=1$ conclusion is precisely the required fixed-time expectation bound on the stated window. This is the established GAFA 32 (2022) paper.
- [Klartag 2303.14938v2](https://arxiv.org/pdf/2303.14938v2), Theorem 1.3, Lemma 2.1, its appendix proof, equations (1.4), (3.1)–(3.5), Lemma 3.1 and Corollary 3.2: the posterior representation, regular class, approximation direction, covariance comparison, and time restriction agree. This is the published version linked by the dossier's DOI. The lemma's auxiliary $t$ may be fixed at 1 when only approximation with $\delta<1$ is needed; its optional curvature-preservation clause is unused.
- [Milman](https://arxiv.org/pdf/0712.4092), definitions of $D_{\rm Poin}$ and $D_{\rm FM}$ and Theorem 1.5, published in Inventiones 177 (2009): $D_{\rm Poin}=C_P^{-1/2}$ and the reciprocal first-moment constant is the supremum of centered absolute first moments of 1-Lipschitz tests. Equivalence and Cauchy–Schwarz give $C_P\le C\sup\operatorname{Var}f$. Thus the comparison used in the dossier has the correct direction. It also appears explicitly as (3.10) in Klartag.
- [Bobkov's actual published PDF](https://www-users.cse.umn.edu/~bobko001/papers/1999_AOP_Isop.pdf), Theorem 1.2 and (1.8), Annals of Probability 27 (1999): these ensure finite Poincaré constant for full-dimensional log-concave laws with finite second moment. Only finiteness is used.

No required source was unavailable. Established theorems are used at their checked statements; their entire historical proofs are not newly certified.

### Independent checks of the argument

**Lines 62–79.** Expectation precedes the matrix norm. Rotations justify choosing the first coordinate in equivalent definitions. For independent centered exponentials, off-diagonal and other diagonal tensor entries vanish, while the $(1,1)$ entry equals 2. Hence $2\le\kappa_n\le2\sqrt2$, including every dimension under consideration.

**Lines 81–114.** Coordinate tests and strong convexity make $P$ positive and finite before choosing time. Bayes' formula has exactly the likelihood $\exp(\langle y,x\rangle-t|x|^2/2)$. Its positive normalizer is finite, and the posterior remains regular. Curvature gives the covariance cap by linear tests. All posterior applications take place on the full space, with no boundary condition on a test function.

**Lines 116–175.** Linear growth of a Lipschitz test and Gaussian damping justify parameter differentiation locally uniformly in $y$. Pairing the covariance vector with each unit direction proves the operator-norm gradient estimate without a trace loss. Conditional variance in the independent variables and Jensen give $C_P(Y)\le t+t^2P$. The displayed $L^2$ and energy bounds put $F$ in its domain; smooth cutoff approximation extends the inequality. Adding the residual conditional variance produces exactly $2+tP$. Posterior Poincaré and the Lipschitz-variance comparison are applied in the appropriate directions. The inequality holds for each fixed deterministic time and each test before taking the supremum.

**Lines 177–203.** Both choices in $t=\min(T,P^{-1})$ are strictly positive. The covariance theorem applies at this deterministic time; Jensen is used in the concave square-root direction. The two branches imply respectively $P\le K/\sqrt T$ and $P\le K^2$, with equality of times harmless. The stated $D$ absorbs the constant branch because $\kappa_n\sqrt{\log n}\ge2\sqrt{\log2}$. Constants are independent of the measure and its regularization. No prior quantitative bound for $P$ or dimensionwise extremizer is assumed.

**Lines 205–247.** Identity covariance rules out lower-dimensional support. Whitening the approximants preserves their regularity by an invertible affine change. Pulling back their Poincaré inequalities multiplies the bound by at most $\|S_\delta\|_{\rm op}$, not its reciprocal. The inequalities bound the original $C_P$ from below by $C_P(\mu)-\delta$ and from above by $(1+\delta)D\kappa_n\sqrt{\log n}$. Letting $\delta$ decrease gives the all-law result without continuity of eigenfunctions or localization paths. The final reverse-Cheeger direction is $\Psi_\mu^2\le\pi C_P(\mu)$, and the displayed maximum defines a single constant for both conclusions. The usual relaxed boundary convention for log-concave densities agrees with the canonical Minkowski Cheeger constant. General locally Lipschitz tests are covered because the comparison bounds the full Poincaré constant.

### Hypotheses and fences

Used hypotheses: finite dimension $n\ge2$, probability normalization, centering and identity covariance, log-concavity, constant Euclidean metric, and the stated quadratic and curvature inputs. Smoothness, strict positive curvature, derivative growth and positive full-space density are temporary regular-class hypotheses, all removed by approximation. Independence of the Gaussian is explicitly stated. There is no unstated symmetry, compact support, uniform regularization parameter, or assumed spectral bound. No unused final hypothesis requires a sharpening note.

The node has no registered `bounded_by`. The argument respects the relevant program restrictions: no supremum over time, no substitution of a trace for an operator norm, no matrix gate-zero inference, and no dimension-free conclusion. Open conjectures are not used as barriers or premises.

## Corrections

None required.

## Exclusions

This verdict does not certify KLS with a dimension-free constant, a time-uniform covariance event, adaptive-matrix estimates, gate zero, CMH, equality cases, other new literature imports, or the concurrently revised moment-map occupation dossiers. It is not a manuscript-wide synchronization audit. No numerical run enters the proof.

## Build and fingerprints

The first full check reported five stale fingerprint errors confined to the two concurrent occupation dossiers. After their separate review records were renewed, I reran `uv --cache-dir /tmp/kls-uv-cache run scripts/check.py` with the required subprocess permissions. It exited 0, with no MyST error or other failure: 132 nodes, comprising 4 defined, 22 open, 104 proved and 2 refuted. I then freshly ran `--fingerprint solutions/thm-letwin-kls.md`; it also exited 0, and its exact output is recorded above.

File hashes confirm that the reviewed dossier, canonical and dependency modules, normalization module and bibliography did not change during final verification. The concurrent ledger changes were reread: the occupation proof records were renewed, while this node remains open with its reviewed dependencies. No part of those independent proofs is implicitly certified here.

## Proposed certification record and handoff

Promote only `thm:letwin-kls` to `proved`, preserve its three direct dependencies and existing references, and add the proof record below. There are no new assumptions, fences or refutation relations. This review itself changes no ledger status.

```yaml
files:
  - research/reviews/2026-10-01-letwin-kls-review.md
deltas:
  - file: research/program/ledger.yaml
    node: thm:letwin-kls
    set:
      status: proved
      proofs:
        - artifact: solutions/thm-letwin-kls.md
          review: research/reviews/2026-10-01-letwin-kls-review.md
    preserve:
      depends_on: [prop:letwin-kappa, thm:letwin-qcts, thm:improved-lichnerowicz]
      references: [Letwin2026QuadraticKLS, Klartag2023Logarithmic, KlartagLehec2022Polylog, Milman2009Isoperimetric, Bobkov1999LogConcave]
```
