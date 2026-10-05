---
verdict: pass
authors:
  - researcher_letwin, gpt-6-astra, 2026-10-01
reviewer: reviewer_letwin_r2, gpt-6-astra, 2026-10-01
fingerprints:
  solutions/thm-letwin-imports.md: 4b94b88237120d52dd49b004b4cdd26d2b703ae1568fa8d2a1047b8158b7341a
  thm:letwin-moment-map: fe8a88cbdf6b7c59609c16b77e7d8f8858792816ce38924fe4046b1950cc54b0
  thm:regular-moment-map-compact-target: 6c5fc0b83ba7ee921113bb0cac813d6c92fd41e9b1a9dda5247df865f76eb813
  thm:letwin-qcts: 8e2ac0819f46db553fe83a6f3034436816565262316c2e6bde7d81baead1a082
  def:qcts: 0f22746bfd781ed526102c33b699417cb07ef6d9df40f0fb4ce59158e6376b86
---

# Letwin imports: second independent certification review

## Findings

**Pass, jointly for `thm:letwin-moment-map` and `thm:letwin-qcts`.** The repaired dossier proves both canonical statements. R1 is closed by an actual examination of the cited Kolesnikov–Milman theorem. No proof or source-verification step required for these two imports remains incomplete.

Lens: `certify`. This review began in a fresh context containing the assignment and handoff, without the conversation that produced or directed the proof. Author: researcher_letwin, gpt-6-astra, 2026-10-01. Reviewer: reviewer_letwin_r2, gpt-6-astra, 2026-10-01. The earlier review is a checklist, not evidence for this verdict. I read the reviewer instructions, specification, brief, original author checkpoint, repair checkpoint, previous report, repaired dossier, canonical statements, dependency records, and the relevant boundary statements. Only this new review is written in the repository.

### Statement agreement and dependencies

Dossier lines 32–60 agree with the canonical matrix statement in `modules/04-family-moment-map.md:145` and quadratic statement in `modules/29-qcts-obstruction.md:51`: the constants are respectively 2 and 8, the matrices are arbitrary constant symmetric matrices, and the quadratic gradient coefficient is 2. The regular matrix class is isotropic density $e^{-V}\mathbf1_K$, bounded open convex $K$, with smooth convex $V$ near $\overline K$. I checked the overline in the actual Letwin PDF, Lemma A.1, p. 16; it can disappear in text extraction. The all-law quadratic conclusion removes that restriction. All dimensions $n\ge1$, singular matrices, and the zero matrix are covered. Symmetrization contracts the Hilbert–Schmidt norm and leaves the quadratic polynomial unchanged, so `def:qcts` also agrees if its supremum includes nonsymmetric matrices.

The dependency closure is the two reviewed nodes, `thm:regular-moment-map-compact-target` (proved on published references), and `def:qcts` (defined). Neither reviewed node has an `assumes` or `bounded_by` edge. The quadratic node's currently open matrix dependency is proved first in this same dossier and certified jointly here; it is not assumed. No Chen–Klartag result or other open result is a premise. The appropriate application of this verdict is to promote both nodes together, retaining their existing dependency edges and references.

### R1: actual boundary source and specialization

I read the [published Kolesnikov–Milman PDF](https://publications.hse.ru/pubs/share/direct/216903475.pdf), DOI [10.1007/s12220-016-9736-5](https://doi.org/10.1007/s12220-016-9736-5), including its geometric conventions and Theorem 1.2(1), PDF pp. 4–6. It applies to arbitrary $C^1$ tests on a compact weighted manifold with nonnegative outward second fundamental form and positive curvature tensor. At $1/N=0$, its factor is one. The word “Neumann” does not require the test itself to satisfy a Neumann condition.

I independently checked every specialization in dossier lines 166–190. The closed sublevels $M_R$ are compact and connected; positive definite $H$ makes every level above the minimum regular and its boundary smooth. With outward normal $\nabla\varphi/|\nabla\varphi|$, the tangential second fundamental form is $H/|\nabla\varphi|$, matching the source's sign convention. The conditional density has potential $\varphi+\log\nu(M_R)$, so Euclidean infinite-dimensional curvature is precisely $H$. The normalization factor in line 184 is correct. Bounded tests give convergence of the conditional means and second moments; monotone convergence applies to the unnormalized nonnegative energies, including an infinite limiting energy. For $n=1$, the boundary tangent space is zero-dimensional and the same conditions hold. Thus the entrywise Hessian tests require no additional boundary hypothesis. The explicit citation in lines 63–67 and direct link in lines 169–170 complete R1. Verification of the historical 1976 passage is no longer needed for this repaired proof.

### Primary sources actually read

I downloaded and read the actual [Letwin 2607.24164v1 PDF](https://arxiv.org/pdf/2607.24164v1), specifically the statement of Theorem 1.2, the Section 2 regularity setup and Lemmas 2.1–2.4, the entire proof of Theorem 2.5, Definition 2.6, Lemmas 2.7 and 2.9, Proposition 2.8, the entire quadratic transfer proof, and every proof in Appendix A.1–A.7. The PDF SHA-256 is `5dd9194cf36d91e2e4929a48564fe99d8d163a0a5ec7b31d80dc1f58a41778f1`. The new source proof was not inferred from either author's summary or the previous review. The dossier expands its coordinate and analytic justifications and supplies an independently verified published boundary input for Appendix A.6.

The published inputs were checked against their actual texts:

| Input | Source and application checked |
|---|---|
| Compact-target existence and regularity | [Berman–Berndtsson, Theorem 1.1, PDF p. 2](https://arxiv.org/pdf/1207.6128): centered positive smooth density on a convex body supplies a smooth potential and gradient diffeomorphism. The dossier's cutoff extension of $V$ gives the required global positive smooth density; global convexity of the extension is unnecessary. Centering and positive interior density put zero in the body's interior. The Monge–Ampère equation gives $H\succ0$. |
| Hessian bound | [Klartag, Theorem 1.1 and condition (1), PDF p. 2](https://arxiv.org/pdf/1309.2767): neighborhood smoothness on the compact closure supplies bounded derivatives of every order, and the theorem gives $\operatorname{Tr}H\le2R_K^2$. |
| Stein kernel | [Fathi, Theorem 2.3 and proof, PDF pp. 4–5](https://www.normalesup.org/~mfathi/docs/Stein%20kernels%20and%20OT,%20revised%20version.pdf): the Hessian transported by the inverse gradient is a symmetric positive Stein kernel. Ambient compactly supported tests give the distributional zero-flux interpretation. The dossier also proves the identity directly. |
| Negative Sobolev inequality | [Barthe–Klartag, equation (3), Proposition 10, PDF p. 5](https://arxiv.org/pdf/1907.01823): the dual class, square-integrability conditions and centered derivatives agree; isotropy is not required. |
| Sobolev density | Same source, Proposition 27, PDF p. 24: density is of ambient $C_c^\infty(\mathbb R^n)$ in weighted $H^1$, so tests may reach the convex support boundary. Its published status is confirmed by [Barthe's publication record](https://cv.hal.science/franckbarthe), *Bulletin of the Hellenic Mathematical Society* 64 (2020), 1–31. |

These established results are used at their verified statements and hypotheses, rather than having their entire historical proofs re-certified. No unavailable source remains a required premise.

### Independent line-by-line proof checks

**Lines 75–163: analytic domain.** The inverse-Hessian derivative and first differentiated Monge–Ampère equation give exactly the stated divergence form and drift. Compact support suffices for symmetry without tail bounds on $H^{-1}$. Ordinary Euclidean cutoffs yield $\mathbb EH=I$, with error bounded by $C\mathbb E|f|/R$. Integrability of $e^{-\varphi}$ forces bounded convex sublevels, hence coercivity. The proper function $W\ge1$ has bounded $LW$. Although $q_R$ need not be compactly supported on the entire real line, $q_R(W)$ is compactly supported in source space, which is all that is needed. Integration by parts gives the nonnegative energy estimate of line 147 and $\|L\chi_R\|_1=O(R^{-1})$. Fatou is applied before integrability of $Lf$ is asserted; dominated convergence only follows afterward. This validates the noncompact generator integration used later.

**Lines 194–274: tensor algebra.** Twice differentiating the logarithmic equation gives the displayed $A$ and $Q$ with the correct signs and inverse metrics. The product rule gives $LS=-2S+2(D_B+A_B+C_B)$. For $B\succeq0$ every source term is nonnegative. Boundedness of $S$ and the cutoff lemma therefore establish integrability of each term before separating their expectations. Under constant $y=Pz$, the covariant third tensor and contravariant $B$ give $\widetilde Q=P^TQP$; contracting the derivative-coordinate factors with the inverse metric leaves $D_B$ unchanged. I checked these cancellations independently. Normalizing at a point gives the two sums in lines 262–263, whose difference is the nonnegative square sum in line 269. This pointwise operation never transforms the global isotropic mean identity or differentiates a moving frame. Consequently $\mathbb ED_B\le\mathbb ES/2$.

**Lines 278–293: matrix conclusion.** Summing the verified boundary/exhaustion variance inequality for the entries of $B^{1/2}HB^{1/2}$ gives $\mathbb ES-\operatorname{Tr}(B^2)\le\mathbb ED_B$ and the factor 2. No inverse of $B$ is used. For indefinite $B$, the comparison in its fixed orthonormal eigenbasis increases each coefficient $b_ib_j$ to $|b_i||b_j|$; the right-hand normalization is unchanged.

**Lines 298–372: quadratic transfer.** The source-coordinate Stein identity uses bounded first derivatives of the composed test, not unproved higher-derivative bounds. Both pairings extend continuously through the published weighted $H^1$ density statement since the linear function and kernel column are in $L^2$. Approximants need not themselves retain the unit energy constraint. For invertible symmetric $M$, congruence by $P=|M|^{1/2}$ produces kernel $P\tau P$ and a centered, generally non-isotropic law. Its squared Hilbert–Schmidt norm is exactly the trace controlled by the matrix theorem. The remaining sign matrix is orthogonal, and the quadratic derivatives are centered and square integrable. Summing over its columns gives the factor $4\cdot2=8$. Adding $\delta$ only on the kernel of $M$ removes singularity by an explicit fourth-moment $L^2$ limit.

**Lines 376–409: general laws and normalization.** Gaussian convolution, convex truncation and whitening produce regular isotropic targets. Finite log-concave polynomial moments give a uniform eighth-moment bound; the displayed $\varepsilon^2$ estimate removes fourth-moment tails. Conditional moments through degree four converge, covariance tends to $I$, and continuous whitening preserves these limits. Isotropy rules out lower-dimensional support. Variance passes for each fixed matrix before the universal conclusion and supremum are taken. The final gradient identity is $\mathbb E|2MX|^2=4\operatorname{Tr}(M^2)$. No convergence of potentials, Hessians, or kernels is required.

### Hypotheses and fences

Every used hypothesis is stated or follows from the regular class: finite dimension, centered identity covariance, bounded open convex target, smooth convex potential near its closure, constant symmetric matrices, and canonical probability normalization. Full dimensionality follows from isotropy. Intermediate invertibility is explicitly removed. Log-concavity supplies the dual inequality, density, convolution stability and polynomial moments. There is no unstated symmetry of the law, uniform lower ellipticity, bounded third derivatives, isotropy after congruence, or boundary condition on the Hessian tests. No unused stated hypothesis creates a defect.

The fixed-matrix conclusion respects the proved algebraic countermodel `prop:letwin-not-gate-zero`; it does not infer a Loewner bound on $\mathbb EH^2$. The full tensor calculation avoids reliance on projection-only information. The brief's two-tail, occupation, bootstrap and moving-competitor boundaries do not supply or obstruct a step of this static proof. No cluster comparison or open antecedent is silently discharged.

## Corrections

None required for certification of these two statements. R1 is closed. The earlier report remains an unchanged `revise` record; this new verdict attaches only to the fingerprints above. Surrounding manuscript prose and the earlier-noted singular-sign shortcut are not substitutes for the dossier's correct singular limit and are outside this certify verdict.

## Build and version stabilization

Immediately before recording the verdict, `UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py` completed with exit 0, including MyST, under tool escalation for the sandbox spawn restriction. It reported 131 nodes: 4 defined, 33 open, 92 proved, 2 refuted, with no failure or MyST error. The subsequent `UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py --fingerprint solutions/thm-letwin-imports.md` also exited 0 under escalation; its exact output is the front-matter block.

SHA-256 comparisons detected a concurrent ledger change. I reread the affected dependency neighborhood: the Chen–Klartag nodes had been certified; both Letwin nodes remained open with unchanged dependencies. Final comparisons immediately before writing found no further changes in the dossier, canonical/dependency and boundary files, instructions, brief, bibliography, checkpoints, prior review or reread ledger. No concurrent work was reverted. No proof, module, ledger, bibliography, prior record, or git data was edited.

## Exclusions

This certifies neither Letwin Theorem 1.1 nor the general KLS exponent or its localization/Lichnerowicz extraction; none is a premise here. It does not certify adaptive estimates, gate zero, CMH, stochastic occupation estimates, Chen–Klartag imports, equality classifications, or downstream corollaries. Published source theorem proofs are not newly certified as standalone results. No node outside the two named imports receives a status recommendation.

## Proposed certification records and handoff

Both nodes may move from `open` to `proved` together, with their existing references and dependency relations preserved and no new `assumes`, `bounded_by`, or `refuted_by` relation. This report does not itself edit their statuses.

```yaml
files:
  - research/reviews/2026-10-01-letwin-imports-r2-review.md
deltas:
  - file: research/program/ledger.yaml
    node: thm:letwin-moment-map
    set:
      status: proved
      proofs:
        - artifact: solutions/thm-letwin-imports.md
          review: research/reviews/2026-10-01-letwin-imports-r2-review.md
    preserve:
      depends_on: [thm:regular-moment-map-compact-target]
      references: [Letwin2026QuadraticKLS]
  - file: research/program/ledger.yaml
    node: thm:letwin-qcts
    set:
      status: proved
      proofs:
        - artifact: solutions/thm-letwin-imports.md
          review: research/reviews/2026-10-01-letwin-imports-r2-review.md
    preserve:
      depends_on: [thm:letwin-moment-map, def:qcts]
      references: [Letwin2026QuadraticKLS]
```
