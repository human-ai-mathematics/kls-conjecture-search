---
type: audit
date: "2026-09-06"
---

# Exponential-cone dossier — cold certification audit (no certification)

Reviewer `/w5/reviewer-cone-lift`, run id `w5r04`, lens `certify`, concurrency key
`review:solutions/prop-cone-moment-map.tex`. Author under review: `/w5/researcher-cone-lift`
(run `w5p01`), a distinct identity. The review was launched without the author's
conversation and reconstructs the argument from repository artifacts only. The author's
checkpoint `research/explorations/2026-09-06-researcher-cone-lift-w5p01.md` was opened solely
to confirm the author identity in its front matter; nothing in it was treated as evidence.
No literature-scout checkpoint `2026-09-06-literature-scout-cone-lift-w5l01.md` existed when
this review reached the citation step, so the source was read directly (Finding 5).

This report is an `audit`: it certifies nothing. It finds one genuine quantifier defect in the
dossier's stated results and asks for a small, exactly specified repair, after which a new
proof review must run. Every other step of the argument was checked and found correct; the
list is below so that the re-review can concentrate on the diff.

## Subject

- Dossier: `solutions/prop-cone-moment-map.tex`, 875 lines, untracked in the working tree at
  HEAD `5b772c9`. SHA-256:

  ```
  b11f9a1fcda6f07f066e741f8888babe7d95bba1d1bf08d7019afb9193cd1e0a
  ```

- Nodes claimed: `prop:cone-moment-map` (dossier Theorem A), `prop:cone-linear-sector`
  (Theorem B), `cor:cube-cone-gate-zero` (Theorem C); all three `status: open` in
  `research/program/ledger.yaml` (working-tree copy), `provenance: internal`, no `assumes`,
  no `bounded_by`, no `heuristic_barriers`.
- Manuscript statements: `modules/kls/42-cmh-exact-cases.tex`, `\label{subsec:cmh-cones}`
  (lines 360–478 of the working-tree copy): `def:exponential-cone` (l. 371),
  `prop:cone-moment-map` (l. 395), `prop:cone-linear-sector` (l. 416),
  `cor:cube-cone-gate-zero` (l. 455).
- Standalone build: `cd solutions && latexmk -pdf -interaction=nonstopmode -outdir=../build
  prop-cone-moment-map.tex` exits 0. Every undefined reference is a cross-module label that
  exists in `modules/` (`eq:moment-measure`, `eq:MA`, `eq:stein-kernel-def`,
  `eq:stein-identity`, `eq:stein-generator`, `eq:cmh-constant`, `eq:gate-zero-sharp`,
  `eq:cmh-1d-stein`, `eq:cone-covariance`, `def:cmh`, `def:exponential-cone`,
  `prop:cmh-hodge`, `lem:linear-sector-third-moment`, `subsec:cmh-conventions`,
  `subsec:cmh-hodge`, `thm:cmh-implies-affine-poincare`, `thm:regular-moment-map-compact-target`,
  and the three node labels).
- The dossier cites no run artifact and no numerics; no step leans on computation.

## Findings

### 1. Statement agreement

Dossier Theorems A, B, C, the three ledger `summary:` texts, and the three manuscript
statements agree mathematically. The dossier restates rather than copies; the differences are
additions, all listed in its Scope paragraph and Remarks §5:

- Theorem A adds $D^2\varphi\succ0$, the explicit gradient/Hessian, and $\E\tau=\Sigma$.
- Theorem B(i) adds that the weak identity holds on $\mathscr P(\R^n)$ and on
  $\Dom(\calE_\Sigma)$ and that the supremum may be taken over either class; B(ii) adds the
  membership $g=x_1\in\Dom(\Aop)\setminus\ker\Aop$; B(iii) is verbatim in content.
- Theorem C adds finiteness of $\E[\tau\Sigma^{-1}\tau]$ and the explicit map $A$.
- The manuscript's "no solenoidal part in the sense of Proposition `prop:cmh-hodge`" is read
  as $w=x-\Sigma\nabla\Aop_1^{-1}\bar x_1=0$, computed directly; the proposition is not
  invoked (Remark `rem:sol-cone-hodge`). The manuscript's "$v_{e_1}=0$ of Lemma
  `lem:linear-sector-third-moment`" is read as the residual
  $\tau_Ze_1-e_1-\tfrac12T_3(e_1)Z\equiv0$, again computed directly (Remark
  `rem:sol-cone-third`). Both readings are the only ones under which the open nodes
  `prop:cmh-hodge`'s hypotheses and the open lemma are not needed, and they match what the
  manuscript sentences assert.

### 2. Barriers

None of the three nodes carries `bounded_by` or `heuristic_barriers`. The dossier claims
nothing universal: Theorem C asserts `eq:gate-zero-sharp` for cube cones only, Theorem B for
the axis direction of a general cone only, and nothing about $\CMH$ itself ("Obstructions
respected", l. 869–874).

### 3. Hypothesis accounting

Used: $n\ge2$; $K\subset\R^{n-1}$ a convex body with barycenter at the origin; $\beta\ge n$.
$\beta\ge n$ enters only through log-concavity (Lemma structure (b)) and the two inequalities
$1+n/\beta\le2$, $G'\le2$; every identity is proved for $\beta>0$. The barycenter condition
gives $\E U=0$ and places $\mathrm{Unif}(K)$, $\mathrm{Unif}(\beta K)$ and $\bar\mu$ in the
hypotheses of the two external theorems. No hypothesis is used but unstated; none is stated
but unused. Remark `rem:sol-cone-hypotheses` matches this accounting.

### 4. Dependencies and applicability

- `thm:regular-moment-map-compact-target`: `status: proved`, `provenance: literature`,
  `import_class: published` (Berman–Berndtsson 2013, Fathi 2019). Applied only in dimension
  $m=n-1$ to $\mathrm{Unif}(K)$ (density $|K|^{-1}$, smooth and positive) and, through the
  rescaling lemma, to $\mathrm{Unif}(\beta K)$. Its literature classification is the
  ledger's and was not re-derived here.
- No other internal node is used. `prop:cmh-hodge` and `lem:linear-sector-third-moment` are
  not invoked; `def:cmh` supplies only the definition of the Rayleigh quotient.
- Ledger edge remark (not a mathematical defect): the proof of Theorem C cites
  Theorem B(ii) for "$1+n/\beta\le2$ with equality iff $\beta=n$" (l. 757). Either
  `cor:cube-cone-gate-zero.depends_on` should also list `prop:cone-linear-sector`, or the
  dossier should prove that one-line inequality inline in Theorem C. The re-review should
  record whichever the researcher chooses.

### 5. Citation debt

The only external result outside the ledger is the uniqueness-up-to-translation part of
Cordero-Erausquin–Klartag, quoted as `thm:sol-cone-cek` (l. 42–49) without a source theorem
number. Verified against the source with the declared tools: the ar5iv rendering of
arXiv:1304.0630 (the arXiv text of *Moment measures*, J. Funct. Anal. 268 (2015) 3834–3866,
bib key `CorderoErausquinKlartag2015MomentMeasures`) states

> **Theorem 2.** Let $\mu$ be a Borel measure on $\R^n$ such that (i) $0<\mu(\R^n)<+\infty$;
> (ii) $\mu$ is not supported in a lower-dimensional subspace; (iii) the barycenter of $\mu$
> lies at the origin (in particular $\mu$ has finite first moments). Then there exists an
> essentially-continuous convex $\psi:\R^n\to\R\cup\{+\infty\}$ whose moment measure is
> $\mu$, and such $\psi$ is uniquely determined up to translation.

with Definition 2 there: $\psi$ is *essentially-continuous* if it is lower semi-continuous and
its set of discontinuity points has $\mathcal H^{n-1}$-measure zero; the paper notes that a
convex function is automatically continuous off $\partial\{\psi<\infty\}$. This matches the
content of `thm:sol-cone-cek` (probability normalization, finite first moment, barycenter
$0$, not in a hyperplane). Classification: **published**. What remains for
`literature-scout` (run `w5l01`) is only to confirm that the journal version keeps the label
"Theorem 2"; the dossier should then cite it as such. This is a numbering confirmation, not a
content risk, and it does not by itself block certification. The same content was already
recorded as Theorem 2 by `research/reviews/2026-09-06-lem-cmh-linear-spectral-resolution-audit.md`
(its table row on CEK), which agrees with the reading above.

### 6. Steps checked (all correct unless stated)

Point numbers follow the prover's handoff.

- Lemma structure (a)–(d): Jacobian $s^m$ of $(s,u)\mapsto(s,su)$; normalization
  $\Gamma(\beta)|K|$; density; log-concavity from $\beta-n\ge0$ on the convex cone; Gamma
  moments; $\E(S-\beta)^3=2\beta$ and $\E[(S-\beta)S^2]=2\beta(\beta+1)$ (point 6); the
  block-diagonal $\Sigma$ and its inverse and square roots.
- Lemma closability/kernel/operator: closability by the local argument on compacts
  exhausting $\Omega$ ($\rho$ bounded below, $M^{\pm1/2}$ bounded on compacts); kernel equals
  constants on the connected open $\Omega$; Kato's representation for the operator domain.
- **Point 2**, Lemma base: $\int e^{-\lambda}=1$ with $\lambda(y')=\lambda_K(\beta y')-m\log\beta$
  (sign correct: $e^{-\lambda}=\beta^m e^{-\lambda_K(\beta y')}$ is the density of
  $Y_0/\beta$); pushforward under $\nabla\lambda=\beta\nabla\lambda_K(\beta\,\cdot)$ is
  $\mathrm{Unif}(\beta K)$; $(\nabla\lambda)^{-1}(z)=\beta^{-1}(\nabla\lambda_K)^{-1}(z/\beta)$
  and $\tau_{\beta K}(z)=\beta^2\tau_K(z/\beta)$, consistent with
  $\E\tau_{\beta K}=\beta^2\Cov(U)$. See Finding 7 for the one sentence of this lemma that
  is not proved.
- **Point 1**, Theorem A: (i) gradient and Hessian of $e^{g}-\beta y_1$; positive
  definiteness; (ii) $\Theta$ and its explicit smooth inverse; (iii) the substitution
  $x_1=e^{y_1}\Phi(y')$ gives $e^{-\varphi}\dd y_1=e^{-\lambda(y')}\gamma_\beta(x_1)\dd x_1$
  exactly ($e^{\beta y_1}=x_1^\beta\Phi^{-\beta}$, $\Phi^{-\beta}=e^{-\lambda}$), Tonelli, and
  the pushforward of $e^{-\lambda}\dd y'$ under $\nabla\lambda/\beta$ is $\mathrm{Unif}(K)$
  because under $\nabla\lambda$ it is $\mathrm{Unif}(\beta K)$; product structure gives
  $\E F(S,U)$ with $S\perp U$; (iv) $D^2\lambda(y')=\tau_{\beta K}(\beta u)=\beta^2\tau_K(u)$,
  the kernel formula, first column $x$, and $\E\tau=\Sigma$ via $\E\tau_K(U)=\Cov(U)$.
- **Point 3**, Lemma Stein: (a) $|(\tau_K)_{ij}|\le\Tr\tau_K$ for PSD, $|u|\le c_K$,
  $\E[x_1^{q}|\tau_{ij}|]\le\E x_1^{q+1}\,(1+c_K^2+\beta\Tr\Cov U)$; (b) the chain rule
  $\partial_iF=\sum_j\partial_jf\,\tau_{ij}$ in source coordinates, absolute convergence of all
  three integrals, the cutoff $\chi_R$ integration by parts on $\R^n$ (no boundary: $F\chi_R$
  compactly supported), dominated convergence, and the $O(R^{-1})$ remainder; (c) the
  $i=1$ case. The direct radial proof in `rem:sol-cone-radial` also checks:
  $(s\gamma_\beta)'=(\beta-s)\gamma_\beta$ with vanishing boundary terms at $0$ and $\infty$.
- **Point 4**, Lemma domains and the convention: the core $\mathscr C=\R+C_c^\infty(\R^n)$
  restricted to the open cone is the same core as in the certified
  `solutions/thm-cmh-normalization.tex` (l. 156: "restrictions to $\operatorname{supp}\mu$ of
  $\R+C_c^\infty(\R^n)$") and as the manuscript's proof sketch of
  `thm:cmh-implies-affine-poincare` (l. 119 of `41-cmh-normalization.tex`), i.e. the no-flux
  reading of `subsec:cmh-conventions`. So the dossier's convention is the manuscript's.
  Under it: (a) polynomials lie in both closed domains with classical gradient (form-norm
  Cauchy via $\chi_Rf$, using $\inner{Mv}{v}\le\Tr M|v|^2$ and Lemma Stein (a)); (b)
  $\psi\in\Dom(\Aop_1)$, $\Aop_1\psi=\bar x_1$ by the radial identity on $\mathscr C$,
  continuity of both sides in the form norm, density of $\mathscr C$, and Kato; (c) the same
  for $g=x_1$ with $\tau e_1=x$; $g\notin\ker\Aop$ since $\ker$ is the constants.
- Lemma affine covariance: $\nabla\phi_T=T\circ\nabla\phi\circ T^\top$,
  $D^2\phi_T=TD^2\phi(T^\top\cdot)T^\top$, the density of $(T^\top)^{-1}Y_0$, and
  $\tau_{T_\#\eta}(Tx)=T\tau_\eta(x)T^\top$.
- **Point 5**, Theorem B(i): $\Div_\mu x=n+(\beta-n)-x_1=-\bar x_1$; $\ker\Aop_1=\R$ so
  $\Aop_1$ is injective on centered functions and $\Aop_1^{-1}\bar x_1=\psi-\E\psi$, $w=0$;
  Cauchy–Schwarz for the closed form gives the supremum $\calE_\Sigma(\psi)$ over
  $\Dom(\calE_\Sigma)\setminus\R$, attained at $\psi$; the value
  $\E x_1^2/\beta+\E x_1^2\,\Tr(\Cov(U)^{-1}\Cov(U))/(\beta(\beta+1))=(\beta+1)+m=\beta+n$.
- Theorem B(ii): $e_1^\top\tau\Sigma^{-1}\tau e_1=x^\top\Sigma^{-1}x$ by symmetry; ratio
  $(\beta+n)/\beta$; Rayleigh quotient at $g=x_1$: numerator $\beta+n$, denominator
  $\E\bar x_1^2=\beta$.
- **Point 6**, Theorem B(iii): $T=\Sigma^{-1/2}$ in the affine lemma;
  $\tau_Ze_1=\beta^{-1/2}\Sigma^{-1/2}(\bar x+\beta e_1)=e_1+\beta^{-1/2}Z$;
  $\E Z_1^3=2\beta^{-1/2}$, $\E[Z_1^2Z']=0$, $\E[Z_1Z'Z'^\top]=2\beta^{-1/2}\Id_m$; hence
  $T_3(e_1)=2\beta^{-1/2}\Id_n$, $\|T_3(e_1)\|_{\HS}^2=4n/\beta$, residual $\equiv0$.
- **Point 7**, Lemma 1D: $\lambda_1''=2e^{-\lambda_1}$ from the pushforward identity (the
  substitution $t=\lambda_1'(y)$ and the fact that $h\circ\lambda_1'$ exhausts bounded
  measurable functions on $\R$); first integral $(\lambda_1')^2+4e^{-\lambda_1}\equiv c$;
  $c=1$ from $\lambda_1'\to1$ and $\lambda_1\to\infty$ as $y\to+\infty$ (convexity with
  $\lambda_1'(y_0)>0$); $\tau_1(t)=\tfrac12(1-t^2)$, agreeing with `eq:cmh-1d-stein`. Lemma
  product: the product potential $\Lambda$ is finite, smooth, strictly convex, normalized, and
  pushes to $\mathrm{Unif}([-1,1]^m)$; $\Cov(U)=\tfrac13\Id_m$.
- Point 7, Theorem C: the block product $\tau\Sigma^{-1}\tau$; top-left $\beta+n$;
  off-diagonal block zero by oddness; $B^2$ expansion and its $(j,k)$ entry; diagonal
  $\gamma=\tfrac15+\tfrac{m-1}9+\tfrac{2\beta}{15}+\tfrac{2\beta^2}{15}$ from
  $\E u_j^4=\tfrac15$, $\E[u_j^2-u_j^4]=\tfrac2{15}$, $\E(1-u_j^2)^2=\tfrac8{15}$;
  $9\gamma=(6\beta^2+6\beta+5n-1)/5$; lower block $[(\beta+1)/3+3\gamma]\Id_m$;
  $G'=\tfrac1\beta+\tfrac{9\gamma}{\beta(\beta+1)}=(6\beta^2+11\beta+5n+4)/(5\beta(\beta+1))$;
  $G'\le2\iff4\beta^2-\beta-5n-4\ge0$; $4\beta^2-\beta-5n-4\ge4\beta^2-6\beta-4=2(2\beta+1)(\beta-2)$
  using $n\le\beta$, then $\beta\ge2$; equality iff $n=\beta=2$; $G'(2,2)=60/30=2$; the map
  $A(c_1,c_2)=(c_1+c_2,c_1-c_2)$ with $|\det A|=2$, $A((0,\infty)^2)=C_K=\{x_1>|x_2|\}$,
  $A(1,1)=2e_1$; $A=\sqrt2R$ with $R$ orthogonal. (The proof's $R$, columns
  $(e_1\pm e_2)/\sqrt2$, has determinant $-1$ and is correctly called a rotation-reflection at
  l. 789; the statement's "a rotation" at l. 694 is also true after composing with the
  coordinate swap, under which the i.i.d. product law is invariant. Optional wording only.)

A finite-precision guard of the rational identities ($G'$ at six $(\beta,n)$ pairs, the
$\beta=n=2$ value) agreed with the hand derivation; this is a guard against reviewer slips,
not evidence, and nothing above depends on it.

### 7. Defect D1 — the class in which "moment potential" is defined is larger than the class in which uniqueness holds

Section 0, l. 37–40, defines: a *moment potential* of $\eta$ is a convex
$\psi:\R^d\to\R\cup\{+\infty\}$ with $\int e^{-\psi}=1$ whose moment measure is $\eta$. No
essential continuity is required. `thm:sol-cone-cek` (l. 42–49), correctly, asserts
uniqueness only among *essentially-continuous* such $\psi$. The dossier then makes statements
quantified over *every* moment potential in the broad sense, and proves them by citing
`thm:sol-cone-cek`:

- l. 205: "Let $\lambda_K$ be a moment potential of the uniform probability on $K$. Then
  $\lambda_K$ is smooth and strictly convex, …" — the cited
  `thm:regular-moment-map-compact-target` describes the *canonical* potential, not an
  arbitrary one in the broad class;
- l. 215–216 (statement of Lemma base): "every moment potential of that law is a translate of
  it", and l. 242–243 (its proof), and l. 233–234 (parenthetical "independent of which moment
  potential $\lambda_K$ is used");
- l. 253–254: "$\lambda$ denotes a moment potential of the uniform probability on $\beta K$
  (any one; all are translates of `eq:sol-cone-rescaled`)";
- l. 277–278 (statement of Theorem A(iii)): "every moment potential of $\bar\mu$ is a
  translate of $\varphi$", and l. 329–332 (its proof);
- l. 633–634 (Lemma 1D): "a moment potential $\lambda_1$ is smooth, …".

These sentences are false, not merely unproved, under the dossier's definition. Explicit
witness for Lemma base with $m=1$, $K=[-1,1]$: for any $c>1$ let
$T_c=\tfrac2{\sqrt c}\operatorname{artanh}(1/\sqrt c)<\infty$ and
\[
  \psi_c(y)=\log\tfrac4c+2\log\cosh\bigl(\tfrac{\sqrt c\,y}2\bigr)\ \text{on }[-T_c,T_c],
  \qquad \psi_c=+\infty\ \text{off }[-T_c,T_c].
\]
Then $\psi_c$ is convex and lower semi-continuous, finite at $\pm T_c$ (so *not*
essentially continuous: in dimension one essential continuity is continuity, CEK Definition 2),
$\psi_c'=\sqrt c\tanh(\sqrt c\,y/2)$ increases from $-1$ to $1$ on $[-T_c,T_c]$,
$\psi_c''=2e^{-\psi_c}$ holds identically, $\int e^{-\psi_c}=\int_{-1}^{1}\tfrac12\dd t=1$, and
the pushforward of $e^{-\psi_c}\dd y$ under $\psi_c'$ has density
$e^{-\psi_c}/\psi_c''=\tfrac12$ on $(-1,1)$: it is $\mathrm{Unif}[-1,1]$. So $\psi_c$ is a
moment potential of $\mathrm{Unif}[-1,1]$ in the sense of l. 37–40, its effective domain is
bounded, and it is not a translate of the finite canonical potential
$\lambda_1(y)=\log4+2\log\cosh(y/2)$ (the $c\to1$ limit). Its "kernel"
$\psi_c''\circ(\psi_c')^{-1}(t)=\tfrac12(c-t^2)$ differs from $\tau_1$. Rescaling by
$\beta$ as in `eq:sol-cone-rescaled` gives the same failure for $\mathrm{Unif}[-\beta,\beta]$.
(A numerical quadrature at $c=4$ returned mass $1.000$, second moment $0.3333$, fourth moment
$0.2000$ for the pushforward, and $\psi_4(T_4)=0.288<\infty$; guard only.)

What the defect does and does not touch. The manuscript statements use "the moment
potential" in the sense of `eq:moment-measure`, i.e. the essentially-continuous potential of
CEK, unique up to translation; the canonical Stein kernel `eq:stein-kernel-def` is built from
that potential. For *that* claim the dossier's argument is complete: $\varphi$, the rescaled
$\lambda$, the product $\Lambda$ and $\phi_T$ are finite convex functions on $\R^d$, hence
continuous, hence essentially continuous (the dossier says so at l. 53–55), and CEK
Theorem 2 identifies each with the canonical potential up to translation. The kernel
invariance paragraph (l. 58–70) is likewise correct as written because it presupposes
$\psi\in C^\infty(\R^d)$. The defect is confined to the definition at l. 37–40 and the
sentences listed above that quantify over the broad class; those sentences appear in the
statements of Lemma base and Theorem A(iii), which is why this review cannot pass the
dossier as written: a `proof-review` certifies the dossier's stated theorems, and one of them
contains a false clause under the dossier's own definitions.

Required repair (one of the two; the first is recommended):

(R1) At l. 37–40 define a moment potential as an **essentially-continuous** convex
$\psi:\R^d\to\R\cup\{+\infty\}$ (CEK Definition 2: lower semi-continuous, discontinuity set
of zero $\mathcal H^{d-1}$-measure) with $\int e^{-\psi}=1$ and moment measure $\eta$, and
add the one-line remark that a finite convex function on $\R^d$ is continuous, hence in this
class. Then every listed sentence becomes a correct consequence of `thm:sol-cone-cek`, and
l. 205 becomes correct because an essentially-continuous potential of $\mathrm{Unif}(K)$ is a
translate of the canonical one and translation preserves smoothness, strict convexity, the
diffeomorphism property and the kernel. No other line of the dossier changes. Update
l. 53–55 and Remark `rem:sol-cone-hypotheses` (4), l. 806–811, to match.

(R2) Alternatively keep the broad definition and insert "essentially-continuous" (or
"finite") before "moment potential" at each of l. 205, 215, 233, 243, 253, 277, 329–332, 633.

Also, while editing: cite the source as "Theorem 2 of
`\cite{CorderoErausquinKlartag2015MomentMeasures}` (arXiv:1304.0630)" in `thm:sol-cone-cek`
and drop the "flagged for verification" sentence at l. 55–56 and Remark
`rem:sol-cone-open`(a), l. 857–861, once `literature-scout` confirms the journal numbering.

## Corrections

None applied: the reviewer does not write `solutions/`. The repair above (D1) is required
before any certification; the dependency-edge item in Finding 4 and the wording items are
recorded for the researcher's discretion and the orchestrator's ledger delta.

## Exclusions

- Not certified: any of the three nodes. No `proofs[]` record is proposed.
- Out of scope and not checked: the literature classification of
  `thm:regular-moment-map-compact-target` itself (taken from the ledger as `proved`,
  `published`); `prop:cmh-hodge` and `lem:linear-sector-third-moment` (not used); the
  manuscript prose after `def:exponential-cone` on square bases not being affine images of
  products (Remark `rem:sol-cone-open`(b)); and the manuscript prose after
  `lem:linear-sector-third-moment` (l. 332–333 of `41-cmh-normalization.tex`) asserting that
  every exponential cone measure satisfies that lemma's integrability hypothesis
  $\E_\nu\|D^2\varphi\|_{\HS}^2<\infty$. The dossier verifies that hypothesis only for the cube
  (bounded base kernel); for a general base it would need $\E\|\tau_K(U)\|_{\HS}^2<\infty$,
  which the dossier neither uses nor proves. That is a manuscript-prose sync item for the
  orchestrator, not a defect of the nodes under review.
- Not decided: the journal numbering of CEK's theorem (content confirmed against the arXiv
  text; label confirmation requested from `literature-scout`).
