---
verdict: revise
authors:
  - researcher_letwin, gpt-6-astra, 2026-10-01
reviewer: reviewer_letwin, gpt-6-astra, 2026-10-01
fingerprints:
  solutions/thm-letwin-imports.md: 15c555d4dc060828994f22698206cc846b3e58592c43964b5db585a90ddb7acf
  thm:letwin-moment-map: fe8a88cbdf6b7c59609c16b77e7d8f8858792816ce38924fe4046b1950cc54b0
  thm:regular-moment-map-compact-target: 6c5fc0b83ba7ee921113bb0cac813d6c92fd41e9b1a9dda5247df865f76eb813
  thm:letwin-qcts: 8e2ac0819f46db553fe83a6f3034436816565262316c2e6bde7d81baead1a082
  def:qcts: 0f22746bfd781ed526102c33b699417cb07ef6d9df40f0fb4ce59158e6376b86
---

# Letwin imports: independent certification review

## Findings

**Revise: one source-verification reservation, not a discovered counterexample or algebraic gap.** The tensor argument, noncompact integrations, quadratic transfer and approximation check out. The dossier's cited 1976 Brascamp–Lieb text was unavailable to this reviewer. The precise boundary inequality is independently supported by an accessible published theorem identified below, but the dossier should explicitly anchor that application to it, or the original cited passage must be made available and checked. Under the invocation's unavailable-source rule, this report does not certify either node.

Lens: `certify`. This is a fresh context, with no author conversation. The author handoff read was `research/explorations/2026-10-01-letwin-import-proof.md`. Only this new report was written in the repository.

### Statements and dependency closure

The canonical matrix statement in `modules/04-family-moment-map.md`, at `thm:letwin-moment-map`, asserts

$$
\mathbb E_\nu\operatorname{Tr}(BHBH)\le2\operatorname{Tr}(B^2)
$$

for every constant symmetric matrix under the source's regular moment-map assumptions. The explicit regular class in dossier lines 32–40 agrees: isotropic $e^{-V}\mathbf1_Kdx$, bounded open convex $K$, and smooth convex $V$ on a neighborhood of $\overline K$. No estimate for Hessians of arbitrary nonsmooth target laws is silently imported.

The canonical `thm:letwin-qcts` in `modules/29-qcts-obstruction.md` asserts, for every isotropic log-concave $X$ and symmetric $M$,

$$
\operatorname{Var}(X^TMX)\le2\mathbb E|\nabla(X^TMX)|^2
=8\|M\|_{\mathrm{HS}}^2,
\qquad \mathcal Q(\mu)\le8.
$$

Dossier lines 43–60 agree, including the order of quantifiers and constants. The matrix dimension can be one; zero matrices cause no exception. In `def:qcts`, allowing all real matrices rather than just symmetric matrices changes nothing: the antisymmetric part contributes zero and orthogonal symmetrization contracts the Hilbert–Schmidt norm.

The dependency closure consists of these two nodes, `thm:regular-moment-map-compact-target`, and `def:qcts`. The regularity node is `proved` on published references; the definition is `defined`. Both imported nodes are currently `open`; neither has `assumes` or `bounded_by`. The quadratic proof actually proves its open matrix dependency earlier in the same dossier, so this is a joint certification request, not an assumption of an unproved matrix result. Until a passing joint review, the quadratic node must not be promoted independently. No other open result is used.

### Source examination and external inputs

I read the actual [Letwin v1 HTML](https://arxiv.org/html/2607.24164v1): the regularity setup, Lemmas 2.1–2.4, the full proof of Theorem 2.5, Definition 2.6, Lemmas 2.7 and 2.9, Proposition 2.8, the proof of Theorem 1.2, and the proofs of Appendix A.1–A.7. The dossier follows those steps and expands the pointwise coordinate transformation. The source's statement that its integrated identity is invariant is read as invariance of the contractions used in its pointwise comparison; the dossier correctly avoids transforming the isotropic global mean identity along with a point-dependent normalization. No inaccessible part of the Letwin preprint itself remains in scope.

Published inputs were checked as follows:

| Input | Actual source examined and application |
|---|---|
| Compact-target regularity | [Berman–Berndtsson, Theorem 1.1, PDF p. 2](https://arxiv.org/pdf/1207.6128). A positive smooth extension of the density and a centered convex body give the global smooth potential and gradient diffeomorphism. Centering with positive interior density places the origin in the body's interior. Positivity of the Monge–Ampère determinant upgrades the convex Hessian to positive definiteness. |
| Bounded Hessian | [Klartag, Theorem 1.1, PDF p. 2](https://arxiv.org/pdf/1309.2767). Its regularity condition (1) requires bounded $K$ and bounded derivatives of the target potential; the dossier's neighborhood smoothness supplies these. The theorem bounds $\Delta\varphi$ by $2R_K^2$, precisely the stronger trace bound used in line 86. |
| Moment-map Stein kernel | [Fathi, Theorem 2.3 and its proof, PDF pp. 4–5](https://www.normalesup.org/~mfathi/docs/Stein%20kernels%20and%20OT,%20revised%20version.pdf). The dossier also derives the needed weak identity directly. Distributional zero boundary flux means the identity holds for ambient compactly supported tests, without requiring those tests to vanish on the target boundary. |
| Negative Sobolev estimate and density | [Barthe–Klartag, equation (3), Proposition 10, and Proposition 27](https://arxiv.org/pdf/1907.01823), PDF pp. 5 and 24. The dual class and the centered-derivative condition agree. Isotropy is not a hypothesis. Density is of ambient $C_c^\infty(\mathbb R^n)$, not tests supported away from the boundary of the convex support. The publication is *Bulletin of the Hellenic Mathematical Society* 64 (2020), 1–31; see the [author's publication record](https://cv.hal.science/franckbarthe). |
| Brascamp–Lieb on convex sublevels | The cited [1976 article](https://www.sciencedirect.com/science/article/pii/0022123676900045) did not yield its full text: the PDF endpoint returned 403, and the [Springer reprint](https://link.springer.com/chapter/10.1007/978-3-642-55925-9_36) exposed only subscription metadata. I did read the applicable boundary theorem in the published [Kolesnikov–Milman paper, Theorem 1.2(1), equivalently 3.1(1)](https://publications.hse.ru/pubs/share/direct/216903475.pdf). It gives exactly the required inequality at $1/N=0$, with Euclidean metric and weight $e^{-\varphi}$. This verifies the mathematical boundary step through a different primary source; it does not establish what the unavailable original passage says. |

### Independent analytic and coordinate checks

**Regularity and integration, lines 74–171.** Extending $V$ smoothly with a cutoff and exponentiating gives a globally positive smooth density agreeing near $\overline K$; global convexity of that extension is unnecessary for the regularity theorem. Boundedness of $H$ follows from the trace estimate and $H\succ0$. Neither $H^{-1}$ nor third derivatives are assumed globally bounded.

The divergence identity follows by substituting
$\partial_aH^{ab}=-H^{bi}\partial_i\log\det H$
and the first differentiated Monge–Ampère equation. Its drift is exactly $-V_b$, with the correct sign. Ordinary Euclidean cutoffs have error at most $C\mathbb E|f|/R$, giving $\mathbb EH=\mathbb E\nabla\varphi\otimes\nabla\varphi=I$ without a Hessian-metric tail assumption.

The coercivity argument is valid: an unbounded convex sublevel with interior contains cones of arbitrarily large volume, contradicting integrability. Any problematic lower sublevel is contained in a higher one with interior. Hence $W\ge1$ is proper. Although $q_R$ need not have compact support as a function on the whole real line, $q_R(W)$ does, which is exactly what the proof needs. The identity

$$
R^{-2}\int w(W/R)\Gamma(W)\,d\nu=\int q_R(W)LW\,d\nu
$$

uses a compactly supported test and gives the asserted $O(R^{-1})$ bound. Fatou is applied to the nonnegative quantity $\chi_R(Lf+cf)$ before any unproved integrability is invoked. Only then does dominated convergence give $\int Lf=0$. This closes the noncompact generator step.

For the convex-domain variance inequality, each closed sublevel above the minimum is compact with smooth boundary, positive definite Hessian and nonnegative second fundamental form. Taking the Euclidean $N=\infty$ case of the accessible boundary theorem gives curvature $D^2\varphi$ and precisely the integrand $\Gamma(u)$. No boundary condition is imposed on $u$. The conditional-probability denominators tend to one; monotone convergence applies to the unnormalized nonnegative energy integrals. This confirms the exhaustion argument mathematically, subject to the citation repair below.

**Tensor identity and comparison, lines 175–255.** Differentiating twice yields $LH+H=A+Q$ with the displayed indices; the inverse-Hessian derivative contributes the positive $Q$ on the right. $Q$ is a Gram matrix. For positive semidefinite $B$, all three source terms in $LS+2S$ are nonnegative. Thus the cutoff lemma makes their expectations finite before they are separated.

I independently contracted the transformed tensors. Under constant $y=Pz$, $\widetilde H=P^THP$, $\widetilde B=P^{-1}BP^{-T}$ and the three covariant factors in $\widetilde T$ cancel the two inverse metrics to give $\widetilde Q=P^TQP$. The derivative-coordinate factors cancel against $\widetilde H^{-1}$ in $D_B$. Consequently both compared scalars are invariant. At $H=I$ and diagonal $B$, the two contractions are

$$
D_B=\sum_{ijk}b_ib_jT_{ijk}^2,\qquad
C_B=\sum_{ijk}b_i^2T_{ijk}^2.
$$

Full third-derivative symmetry gives their difference as $\frac12\sum_{ijk}(b_i-b_j)^2T_{ijk}^2$. There is no derivative of a moving frame and no assumption that the original $B,H$ commute. The integrated identity therefore gives $\mathbb ED_B\le\mathbb ES/2$.

**Matrix conclusion, lines 259–274.** Summing entrywise variance inequalities for $B^{1/2}HB^{1/2}$ produces exactly $\mathbb ES-\operatorname{Tr}(B^2)$ on the left and $\mathbb ED_B$ on the right. The factor two follows. Singular positive matrices need no inverse. In an orthonormal eigenbasis of an indefinite $B$, replacing each $b_ib_j$ by $|b_i||b_j|$ increases the trace expression termwise; $\operatorname{Tr}(|B|^2)=\operatorname{Tr}(B^2)$. This proves the full symmetric-matrix assertion once the cited variance input is anchored.

**Stein, duality and congruence, lines 279–352.** Only first derivatives of $g\circ\nabla\varphi$ are required and are bounded. The resulting Stein identity extends in weighted $H^1$ because its two factors $v\cdot Z$ and $\tau v$ are square integrable. Approximants need not retain energy at most one: the identity first extends by continuity, and Cauchy–Schwarz is then applied to the limiting admissible test.

For invertible symmetric $M$, $P=|M|^{1/2}$ is invertible and $J=M|M|^{-1}$ is symmetric orthogonal. The transformed kernel is $P\tau P$, not a similarity transform. Its squared Hilbert–Schmidt norm is the controlled trace $\operatorname{Tr}(|M|H|M|H)$. The law of $Z$ is centered and log-concave, and the quadratic polynomial and its centered derivatives meet Proposition 10's integrability hypotheses. Summing against the orthonormal columns of $J$ produces $4\mathbb E\|P\tau P\|_{\mathrm{HS}}^2\le8\operatorname{Tr}(M^2)$ without a commutator estimate. Adding $\delta P_0$ only on the kernel of $M$ makes it invertible; fourth moments give the stated $L^2$ limit. In particular the zero matrix is covered.

**All isotropic log-concave laws, lines 357–390.** Gaussian convolution is positive, smooth and log-concave; restriction to an open ball and invertible affine normalization preserve log-concavity. The normalized potential is smooth on a neighborhood of the closed ellipsoid. The uniform eighth-moment bound and the displayed $\varepsilon^2$ tail estimate imply convergence of every moment of degree at most four. The conditional covariance tends to $I$, so whitening is continuous and introduces no limiting degeneracy. A lower-dimensional law cannot be isotropic in the ambient dimension. The proof consequently covers all laws in the canonical statement, including nonsmooth densities, bounded supports, and unbounded supports. It requires no convergence of potentials, Hessians or Stein kernels. The variance passes for each fixed $M$, and only afterward is the universal conclusion and the supremum defining $\mathcal Q$ taken. Isotropy gives the final factor $4$ in the gradient energy.

### Hypotheses and fences

Every substantive hypothesis used is stated or follows from the regular class: fixed finite dimension; centered covariance $I$; bounded open convex target; smooth convex potential near its closure; constant symmetric test matrices; and the canonical probability normalization. Strict positivity of $H$ and its upper bound come from the checked published inputs. Intermediate invertibility is explicitly removed. Log-concavity supplies convolution stability and finite polynomial moments. Full dimensionality follows from isotropy and is preserved by the invertible congruence. There is no assumption of symmetry of the law, uniform lower ellipticity, uniform bounds on third derivatives, or isotropy of the congruence-transformed law. No unused hypothesis is a certification defect; the quadratic conclusion indeed removes the initial smooth compact-target restrictions.

I read the brief and the dossier's cited fences. The proved `prop:letwin-not-gate-zero` is respected: controlling $\mathbb E\operatorname{Tr}(BHBH)$ does not control $\mathbb EH^2$ in Loewner order. The projection ceiling is avoided by the full third-order tensor comparison. The two-tail scaling, occupation, bootstrap, single-coordinate-cut and moving-competitor boundaries do not intervene in this static argument. The brief's monotone scalar cutoffs concern its retained localization cutoffs; they do not prohibit the decreasing spatial exhaustion cutoff $\eta$ here. Neither P1's cluster comparisons nor P2's open antecedents are invoked or discharged.

## Corrections

**R1 — source-verification closure, dossier lines 63–67 and 165–171.** The 1976 reference could not be read in full. Do not characterize this as a refutation of Brascamp–Lieb or a failure of the tensor proof. There are two sufficient repairs:

1. Supply a readable copy of the cited original result and identify the precise passage supporting the convex-domain form, including any required reduction from its stated formulation. A fresh reviewer must read that passage and check the reduction; bibliographic metadata alone is insufficient.
2. Preferably, add an explicit primary-source citation or direct link in the dossier to Kolesnikov–Milman, *Brascamp–Lieb-Type Inequalities on Weighted Riemannian Manifolds with Boundary*, Theorem 1.2(1), DOI `10.1007/s12220-016-9736-5`, using the accessible PDF linked above. State its specialization: $M=\overline{\{\varphi<R\}}$ with Euclidean metric, probability weight proportional to $e^{-\varphi}$, $1/N=0$, $\operatorname{Ric}_{\mu,\infty}=D^2\varphi\succ0$, and nonnegative second fundamental form. The theorem is for arbitrary $C^1$ test functions; do not impose an unnecessary Neumann condition on the entries of $B^{1/2}HB^{1/2}$. Retain the conditional-normalization and exhaustion argument. A direct link suffices within the researcher's write surface; if a BibTeX entry is desired, propose it to the orchestrator rather than editing `references.bib`.

This is the complete repair list for the two statements in scope. No further mathematical defect was found in the audited dossier. No certification delta is proposed.

## Build and stabilization

Immediately before recording this report, `UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py` completed with exit 0 under tool escalation, including MyST, with 131 nodes (4 defined, 36 open, 89 proved, 2 refuted). The initial sandbox run failed in the MyST startup path; escalation resolved it without a code change. The fingerprint command was then run under the same environment and exited 0; its output is copied verbatim into the front matter.

The dossier and audited manuscript files were reread or compared against their recorded hashes before fingerprinting. Concurrent changes were detected in the ledger; its relevant records and diff were reread. Those changes certified unrelated conditional bridges and did not change either Letwin statement, their dependency closure or their open statuses. No other agent's work was reverted.

## Exclusions

This review does not certify Letwin Theorem 1.1, the general KLS exponent or its localization/Lichnerowicz bridge. Those results are not premises of these two imports. It does not certify the Chen–Klartag preprint, gate zero, CMH, adaptive matrix choices, stochastic occupation bounds, equality classifications, or downstream manuscript corollaries. Published inputs were checked for their applicable statements and hypotheses; their full historical proofs were not re-certified. The author's noted singular-sign shortcut in surrounding manuscript prose is outside this certify review; the dossier already handles singular matrices correctly.

```yaml
files:
  - research/reviews/2026-10-01-letwin-imports-review.md
next: |
  Researcher: close R1 in solutions/thm-letwin-imports.md, lines 63–67 and
  165–171. Either supply the original Brascamp–Lieb passage and its
  convex-domain reduction for source verification, or explicitly cite/link
  Kolesnikov–Milman Theorem 1.2(1), DOI 10.1007/s12220-016-9736-5, and spell
  out its Euclidean N=infinity specialization on the smooth convex closed
  sublevels, positive Hessian, nonnegative boundary second fundamental form,
  arbitrary C1 tests, conditional normalization and exhaustion limit.
  Do not alter the two canonical statements or the tensor/congruence proof.
  Use a direct link or propose any bibliography addition to the orchestrator.
  Record the repair in a new dated checkpoint, then request a fresh certify
  review of both imports together with a new full check and fingerprints.
  Leave both ledger nodes open until that review passes; append a new report
  rather than overwriting this one. No other repair is requested by this audit.
```
