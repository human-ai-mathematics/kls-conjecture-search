---
verdict: pass
authors:
  - /w5/researcher-cone-lift
  - /w5/researcher-cone-lift-repair
reviewer: /w5/reviewer-cone-lift-second
fingerprints:
  solutions/prop-cone-moment-map.md: 56977ada78f78799ee00f7b102aa8c55d15aa1eea4b18a9e5800acabfd7ff828
  prop:cone-moment-map: 17a61295e07885d64d8d19a3ec6d3f93071bf610cd532bc7f3f5f9ca4463b2ed
  thm:regular-moment-map-compact-target: 6c5fc0b83ba7ee921113bb0cac813d6c92fd41e9b1a9dda5247df865f76eb813
  prop:cone-linear-sector: bc33a40d8941c7c53233e874964ad29d13a1bf894ca15c94a734d449c475c942
  cor:cube-cone-gate-zero: ed76f4e4e5e1d9438fd8c5529ee537ce4b8f3e08cc6982531753f726dace3637
---

# Exponential-cone dossier — second cold certification review

Reviewer `/w5/reviewer-cone-lift-second`, run id `w5r06`, lens `certify`, concurrency key
`review:solutions/prop-cone-moment-map.tex`. Authors under review: `/w5/researcher-cone-lift`
(run `w5p01`) and `/w5/researcher-cone-lift-repair` (run `w5p04`), both distinct from the
reviewer and from the first reviewer `/w5/reviewer-cone-lift` (run `w5r04`). The review was
launched without either author's conversation. The two researcher checkpoints were opened only
to confirm the author identities in their front matter; nothing in them, nor in the first audit,
was treated as evidence. The first audit was used as a list of steps to re-verify; every step
of the dossier was re-derived here independently, and then the repaired diff was checked
against the audit's repair instructions.

## Subject

- Dossier: `solutions/prop-cone-moment-map.tex`, 911 lines, untracked in the working tree at
  HEAD `5b772c9`. SHA-256:

  ```
  799082f3bade3c80277b001f0ea6199aa160a72a3ccefa99d02d89eefff3278a
  ```

- Nodes: `prop:cone-moment-map` (dossier Theorem A, `thm:sol-cone-A`),
  `prop:cone-linear-sector` (Theorem B, `thm:sol-cone-B`), `cor:cube-cone-gate-zero`
  (Theorem C, `thm:sol-cone-C`). All three are `status: open`, `provenance: internal`, no
  `assumes`, no `bounded_by`, no `heuristic_barriers` in the working-tree
  `research/program/ledger.yaml`; `depends_on` is `[thm:regular-moment-map-compact-target]`,
  `[prop:cone-moment-map]`, `[prop:cone-moment-map]` respectively.
- Manuscript statements: `modules/kls/42-cmh-exact-cases.tex`, `\label{subsec:cmh-cones}`:
  `def:exponential-cone` (l. 371), `prop:cone-moment-map` (l. 395),
  `prop:cone-linear-sector` (l. 416), `cor:cube-cone-gate-zero` (l. 455).
- Standalone build: `cd solutions && latexmk -pdf -interaction=nonstopmode -outdir=../build
  prop-cone-moment-map.tex` exits 0. Every undefined reference is a cross-module label that
  exists in `modules/`: `cor:cube-cone-gate-zero`, `def:cmh`, `def:exponential-cone`,
  `eq:cmh-1d-stein`, `eq:cmh-constant`, `eq:cone-covariance`, `eq:gate-zero-sharp`, `eq:MA`,
  `eq:moment-measure`, `eq:stein-generator`, `eq:stein-identity`, `eq:stein-kernel-def`,
  `lem:linear-sector-third-moment`, `prop:cmh-hodge`, `prop:cone-linear-sector`,
  `prop:cone-moment-map`, `subsec:cmh-conventions`, `subsec:cmh-hodge`,
  `thm:cmh-implies-affine-poincare`, `thm:regular-moment-map-compact-target`.
- The dossier cites no run artifact and no numerics. No step leans on computation. (The
  numerics checkpoint `2026-09-06-numerics-cmh-cone-w5n01.md` exists in the tree; it was not
  opened and plays no role here.)

## Findings

### 1. Statement agreement

Dossier Theorems A, B, C, the three ledger `summary:` texts, and the three manuscript
statements agree mathematically. The dossier restates and adds; every addition is listed in
its Scope paragraph and §5. Specifically:

- **Theorem A / `prop:cone-moment-map`.** Manuscript: with $\lambda$ *the* moment potential of
  $\mathrm{Unif}(\beta K)$, the moment potential of $\bar\mu_{K,\beta}$ is
  $\varphi=\exp(y_1+\lambda(y')/\beta)-\beta y_1+\log\Gamma(\beta)$, $\nabla\varphi$ is a
  diffeomorphism onto $C_K-\beta e_1$, and the canonical kernel is
  $x_1\begin{psmallmatrix}1&u^\top\\u&uu^\top+\beta\tau_K(u)\end{psmallmatrix}$ with first
  column $x$. Dossier: the same, plus $D^2\varphi\succ0$, the explicit gradient and Hessian,
  and $\E\tau=\Sigma$. "The moment potential" in the manuscript is the essentially unique
  potential of `eq:moment-measure`, i.e. the essentially-continuous potential of
  Cordero-Erausquin–Klartag, and the dossier's §0 definition is now exactly that class
  (Finding 7). The manuscript obtains $\lambda$'s regularity by applying
  `thm:regular-moment-map-compact-target` to $\mathrm{Unif}(\beta K)$ directly; the dossier
  applies it to $\mathrm{Unif}(K)$ and rescales (Lemma `lem:sol-cone-base`). Both are
  legitimate and give the same object.
- **Theorem B / `prop:cone-linear-sector`.** (i) agrees; the dossier makes "zero boundary
  flux" precise as the weak identity $\E\inner x{\nabla f}=\E[\bar x_1f]$ for all
  $f\in\mathscr P(\R^n)$ (test functions not vanishing on $\partial C_K$) and for all
  $f\in\Dom(\calE_\Sigma)$, and makes "no solenoidal part in the sense of `prop:cmh-hodge`"
  precise as $w=x-\Sigma\nabla\Aop_1^{-1}\bar x_1=0$, computed directly without invoking the
  proposition. The supremum "over $f$ of finite covariance energy" is read as
  $\Dom(\calE_\Sigma)\setminus\R$; the dossier proves the same value and attainment also over
  nonconstant $f\in\mathscr P$. (ii) agrees verbatim, with the Rayleigh quotient of
  `eq:cmh-constant` evaluated at an admissible $g=x_1\in\Dom(\Aop)\setminus\ker\Aop$ under
  the manuscript's closure convention (Finding 6, Lemma domains). (iii) agrees; "$v_{e_1}=0$
  of Lemma `lem:linear-sector-third-moment`" is read as the residual
  $\tau_Ze_1-e_1-\tfrac12T_3(e_1)Z$, which is what that lemma's display defines as $v_a$,
  vanishing identically; the lemma is not invoked and its integrability hypothesis is not
  needed for the pointwise identity (Remark `rem:sol-cone-third`). Ledger summary agrees
  under the same readings.
- **Theorem C / `cor:cube-cone-gate-zero`.** Agrees; the dossier adds finiteness of
  $\E[\tau\Sigma^{-1}\tau]$ for the cube and the explicit map $A$. The manuscript's "the
  measure is a product of two centered exponentials" at $n=\beta=2$ is proved in the form: in
  the orthonormal frame $(e_1\pm e_2)/\sqrt2$ the coordinates of $\bar x$ are
  $\sqrt2(c_1-1),\sqrt2(c_2-1)$ with $c_1,c_2$ i.i.d. standard exponential. That is a product
  of two centered exponential laws in an orthonormal frame, which is what the manuscript
  sentence asserts.

### 2. Barriers

No `bounded_by` and no `heuristic_barriers` on any of the three nodes. The dossier claims
nothing universal: `eq:gate-zero-sharp` for cube cones only (Theorem C) and for the axis
direction of a general cone only (Theorem B), and nothing about $\CMH$ itself ("Obstructions
respected", l. 905–910).

### 3. Hypothesis accounting

Used: $n\ge2$; $K\subset\R^{n-1}$ a convex body (compactness gives $|K|<\infty$ and
$c_K<\infty$; nonempty interior gives $\Cov(U)\succ0$ and "not supported in a hyperplane")
with barycenter at the origin (gives $\E U=0$, the block-diagonal $\Sigma$, the vanishing odd
moments, and the centering hypothesis of both external theorems); $\beta\ge n$. The last
enters only through log-concavity (Lemma structure (b), where $\beta-n\ge0$ makes
$-(\beta-n)\log x_1$ convex) and the two inequalities $1+n/\beta\le2$ and $G'\le2$ (Theorems B(ii),
C); every identity is proved for $\beta>0$. Remark `rem:sol-cone-hypotheses`(1)–(3) states
exactly this accounting. No hypothesis is used but unstated; none is stated but unused. That
the identities hold for all $\beta>0$ is a sharpening opportunity, not a defect, and the
dossier already records it.

### 4. Dependencies and applicability

- `thm:regular-moment-map-compact-target`: `status: proved`, `provenance: literature`,
  `import_class: published`. Applied once, in dimension $m=n-1$, to $\mathrm{Unif}(K)$
  ($P=K$, $g\equiv|K|^{-1}$, which is in $C^\infty(\R^m)$ and positive; centered). The
  manuscript statement (`04-family-moment-map.tex` l. 56–71) delivers exactly what Lemma
  base takes from it: the canonical potential is smooth and strictly convex, its gradient is a
  diffeomorphism onto $\operatorname{int}P$, and $\E_\mu\tau_\mu=\Cov(\mu)$. Its literature
  classification is the ledger's and was not re-derived.
- No other ledger node is used. `prop:cmh-hodge` and `lem:linear-sector-third-moment` (both
  `proved` in the working tree) are not invoked; `def:cmh` supplies only the definition of
  the Rayleigh quotient, and the dossier's $\Aop$ is the operator of the closure from the
  same core as `def:cmh`'s `eq:stein-dirichlet-form` (Finding 6, Lemma domains).
- Theorem C no longer cites Theorem B(ii) for $1+n/\beta\le2$; the inequality is proved inline
  (l. 785–787). Theorem C's proof references Theorem B(ii) only as an "in agreement with"
  cross-check of the top-left entry, which Theorem C computes independently. Hence **no
  `depends_on` edge from `cor:cube-cone-gate-zero` to `prop:cone-linear-sector` is needed**,
  and the existing edges are correct: Theorem B and Theorem C each use Theorem A
  (`prop:cone-moment-map`), and Theorem A uses `thm:regular-moment-map-compact-target`
  through Lemma base.
- No `assumes` on any node; nothing conditional is claimed.

### 5. Citation debt

The only external result outside the ledger is `thm:sol-cone-cek` (l. 52–58). Verified
against the source with the declared tools (ar5iv rendering of arXiv:1304.0630; a probe of
`arxiv.org/abs/1304.0630v2` returns 404, so `v1` is the only arXiv text):

- **Definition 1** there: for convex $\psi:\R^n\to\R\cup\{+\infty\}$ with
  $0<\int e^{-\psi}<\infty$, the moment measure is the push-forward of $e^{-\psi}\dd x$ under
  $\nabla\psi$ — unnormalized, so a probability moment measure forces $\int e^{-\psi}=1$, as
  the dossier says at l. 66–68.
- **Definition 2** there: $\psi$ is essentially-continuous if it is lower semi-continuous and
  its set of discontinuity points has zero $\mathcal H^{n-1}$-measure; the text adds that in
  dimension one this is equivalent to continuity, and that any finite convex $\psi:\R^n\to\R$
  is essentially-continuous. Both facts are used by the dossier (l. 37–50 and Remark
  `rem:sol-cone-hypotheses`(4)) and both are stated in the source.
- **Theorem 2** there: for a Borel measure $\mu$ with $0<\mu(\R^n)<\infty$, not supported in a
  lower-dimensional subspace, barycenter at the origin, there exists an essentially-continuous
  convex $\psi$ whose moment measure is $\mu$, unique up to translation. The dossier's
  specialization to a probability measure (l. 60–70) is exact.

Classification: **published** (J. Funct. Anal. 268 (2015) 3834–3866, bib key
`CorderoErausquinKlartag2015MomentMeasures`). The dossier cites the arXiv text's theorem
number and says so; the journal label is left as a verification remark at l. 69–70 and
`rem:sol-cone-open`(a), consistent with the literature-scout checkpoint `w5l01`, which also
did not verify the journal numbering. This is a label question, not a content risk, and does
not block certification. No other external input: the Gamma moments are computed in Lemma
structure (c).

### 6. Steps checked

Every step below was re-derived by the reviewer; all are correct.

- **§0.** Kernel invariance under translation: $(\nabla\tilde\psi)^{-1}(x)=(\nabla\psi)^{-1}(x)-a$
  and $D^2\tilde\psi(y)=D^2\psi(y+a)$ compose to the same matrix. Lemma closable: on a compact
  $Q\subset\Omega$, $\rho$ is bounded above and below and $M^{\pm1/2}$ bounded, so
  $L^2(\eta)$-convergence is $L^2(Q,\dd x)$-convergence; the distributional argument gives
  $M^{-1/2}v=0$ a.e. on $\operatorname{int}Q$; exhaustion gives $v=0$. Kernel = constants on
  connected $\Omega$; Kato's representation theorem for the operator. $\mathscr C$ has finite
  pre-form since $\E\Tr M<\infty$.
- **Lemma structure.** Jacobian $\det\begin{psmallmatrix}1&0\\u&s\Id_m\end{psmallmatrix}=s^m$;
  $\int_0^\infty s^{\beta-n+m}e^{-s}\dd s=\Gamma(\beta)$; density
  $\gamma_\beta(s)|K|^{-1}s^{-m}=\rho$; log-concavity from $\beta-n\ge0$ on the convex cone;
  $\E S^k=\Gamma(\beta+k)/\Gamma(\beta)$; $\E(S-\beta)^3=(\beta^3+3\beta^2+2\beta)-3\beta^3-3\beta^2+3\beta^3-\beta^3=2\beta$;
  $\E[(S-\beta)S^2]=\beta(\beta+1)(\beta+2-\beta)=2\beta(\beta+1)$; $\Sigma$ block-diagonal
  with $\E[(S-\beta)SU]=0$ and $\E S^2UU^\top=\beta(\beta+1)\Cov U$.
- **Lemma base.** Compact-target theorem gives the canonical $\lambda_K^0$; CEK makes any
  (essentially-continuous) $\lambda_K$ a translate; translation preserves every listed
  property. $D^2\lambda_K$ invertible as the Jacobian of a diffeomorphism, PSD by convexity,
  hence PD. Rescaling: $\int e^{-\lambda}=\beta^m\beta^{-m}\int e^{-\lambda_K}=1$;
  $e^{-\lambda}\dd y'$ is the law of $Y_0/\beta$; $\nabla\lambda(Y_0/\beta)=\beta\nabla\lambda_K(Y_0)\sim\mathrm{Unif}(\beta K)$;
  $\lambda$ finite, so CEK applies to $\mathrm{Unif}(\beta K)$ (centered, compactly supported,
  open support); $(\nabla\lambda)^{-1}(z)=\beta^{-1}(\nabla\lambda_K)^{-1}(z/\beta)$ and
  $\tau_{\beta K}(z)=\beta^2\tau_K(z/\beta)$.
- **Theorem A.** (i) $\nabla\varphi=e^g\nabla g-\beta e_1$, $D^2\varphi=e^g(\nabla g\nabla g^\top+D^2g)$
  with $\nabla g=(1,u)$, $D^2g=0\oplus D^2\lambda/\beta$; $v^\top D^2\varphi v=E[(v_1+\inner u{v'})^2+v'^\top D^2\lambda v'/\beta]$
  vanishes only at $v=0$. (ii) $\Theta$ has the explicit smooth inverse
  $(x_1,u)\mapsto(\log x_1-\lambda(y')/\beta,y')$, $y'=(\nabla\lambda)^{-1}(\beta u)$;
  $\nabla\varphi=\Psi\circ\Theta-\beta e_1$. (iii) with $x_1=e^{y_1}\Phi(y')$,
  $e^{\beta y_1}=x_1^\beta\Phi^{-\beta}$, $\Phi^{-\beta}=e^{-\lambda}$, so
  $e^{-\varphi}\dd y_1=e^{-\lambda(y')}\gamma_\beta(x_1)\dd x_1$ exactly; Tonelli; the map
  $y'\mapsto u(y')=\nabla\lambda/\beta$ pushes $e^{-\lambda}\dd y'$ to $\mathrm{Unif}(K)$;
  hence `eq:sol-cone-pushforward` reads $\E F(S,U)$ with $S\perp U$; $F\equiv1$ and $F=G\circ\Psi$ give
  normalization and pushforward; $\varphi$ finite smooth convex, $\bar\mu$ centered with
  finite first moment and open support, so CEK gives uniqueness up to translation.
  (iv) $D^2\lambda(y')=\tau_{\beta K}(\beta u)=\beta^2\tau_K(u)$, so $D^2\lambda/\beta=\beta\tau_K(u)$;
  first column $x_1(1,u)=x$; $\E\tau=\beta e_1e_1^\top\oplus\beta(\Cov U+\beta\Cov U)=\Sigma$.
- **Lemma Stein.** (a) each entry of the bracket is bounded by $1+c_K^2+\beta\Tr\tau_K(u)$
  since $|u|\le c_K$ and $|(\tau_K)_{ij}|\le\Tr\tau_K$ for PSD; independence and
  $\E\Tr\tau_K(U)=\Tr\Cov U$; $|x|\le c_Kx_1$. (b) chain rule
  $\partial_iF=\sum_j\partial_jf\,\varphi_{ij}=\sum_j\partial_jf\,\tau_{ij}$ in source
  coordinates; three absolutely convergent integrals; cutoff integration by parts with the
  correct sign $\int\partial_i\varphi\,F\chi_Re^{-\varphi}=\int e^{-\varphi}\partial_i(F\chi_R)$;
  dominated convergence; remainder $\le\|\nabla\chi\|_\infty R^{-1}\E|f|$. (c) $i=1$ with
  $\tau e_1=x$, and $f\mapsto f(\cdot-\beta e_1)$ preserves $\mathscr P$.
- **Lemma domains.** (a) $\chi_Rf\in C_c^\infty\subset\mathscr C$; $\chi_Rf\to f$ in $L^2(\mu)$;
  form-norm bound via $\inner{Mv}v\le\Tr M|v|^2$, both expectations finite by Lemma Stein (a)
  (for $M=\tau$) and all moments (for $M=\Sigma$); dominated convergence and $O(R^{-2})$.
  (b) $\calE_\Sigma(\psi,f)=\E\inner x{\nabla f}=\E[\bar x_1f]$ on $\mathscr C$ by
  `eq:sol-cone-radial`; both sides form-norm continuous; density of $\mathscr C$; Kato.
  (c) the same with $\tau e_1=x$; $\Aop g=\bar x_1\ne0$ so $g\notin\ker\Aop$.
- **Lemma affine.** $\nabla\phi_T=T\nabla\phi(T^\top\cdot)$, $D^2\phi_T=TD^2\phi(T^\top\cdot)T^\top$;
  $W=(T^\top)^{-1}Y_0$ has density $e^{-\phi(T^\top y)}|\det T|=e^{-\phi_T(y)}$;
  $\nabla\phi_T(W)=T\nabla\phi(Y_0)$; $(\nabla\phi_T)^{-1}(Tx)=(T^\top)^{-1}(\nabla\phi)^{-1}(x)$;
  kernel transforms by $T\,\cdot\,T^\top$. $T_\#\eta$ inherits CEK's hypotheses under an
  invertible linear map.
- **Theorem B.** (i) $\nabla\log\rho=((\beta-n)/x_1-1)e_1$, $\Div x=n$, total
  $\beta-x_1=-\bar x_1$; $\Aop_1$ injective on $\Dom(\Aop_1)\cap L^2_0$ (if $\Aop_1f=0$ then
  $\calE_\Sigma(f)=0$, so $f$ constant, so $f=0$ if centered); $\Aop_1^{-1}\bar x_1=\psi-\E\psi$;
  $w=0$. Cauchy–Schwarz for the closed form and for the pointwise
  $\inner{\Sigma^{-1/2}x}{\Sigma^{1/2}\nabla f}$ on $\mathscr P$; $\calE_\Sigma(f)>0$ for
  $f$ nonconstant on $C_K$; value $\E x_1^2/\beta+\E x_1^2\,\Tr(\Cov(U)^{-1}\Cov U)/(\beta(\beta+1))=(\beta+1)+m=\beta+n$.
  (ii) $e_1^\top\tau\Sigma^{-1}\tau e_1=x^\top\Sigma^{-1}x$ by symmetry; ratio $(\beta+n)/\beta$;
  $\le2\iff n\le\beta$, equality iff $\beta=n$; Rayleigh quotient at $g=x_1$: numerator
  $\E x^\top\Sigma^{-1}x=\beta+n$, denominator $\E\bar x_1^2=\beta$.
  (iii) $\tau_Ze_1=\beta^{-1/2}\Sigma^{-1/2}(\bar x+\beta e_1)=\beta^{-1/2}Z+e_1$;
  $\E Z_1^3=\beta^{-3/2}\cdot2\beta$; $\E[Z_1^2Z']=0$ by $\E U=0$;
  $\E[Z_1Z'Z'^\top]=\beta^{-1/2}(\beta(\beta+1))^{-1}\cdot2\beta(\beta+1)\Id_m$; so
  $T_3(e_1)=2\beta^{-1/2}\Id_n$, $\|T_3(e_1)\|_{\HS}^2=4n/\beta$, residual $\equiv0$.
- **Lemma 1D.** Substitution $t=\lambda_1'(y)$ in the pushforward identity;
  $h\circ\lambda_1'$ exhausts bounded measurable functions because $\lambda_1'$ is a
  homeomorphism $\R\to(-1,1)$; continuity gives $\lambda_1''=2e^{-\lambda_1}$ everywhere;
  $\frac{\dd}{\dd y}[(\lambda_1')^2+4e^{-\lambda_1}]=2\lambda_1'(\lambda_1''-2e^{-\lambda_1})=0$;
  $c=1$ from $\lambda_1'\to1$ and $\lambda_1\to\infty$ at $+\infty$; $\tau_1(t)=\tfrac12(1-t^2)$,
  which equals $-\rho^{-1}\int_{-1}^tv\rho\,\dd v$ for $\rho\equiv\tfrac12$ (`eq:cmh-1d-stein`).
- **Lemma product.** $\Lambda=\sum_j\lambda_1(y_j)$ finite, smooth, strictly convex,
  normalized, pushes the product measure to $\mathrm{Unif}([-1,1]^m)$, gradient a
  diffeomorphism onto $(-1,1)^m$; CEK identifies it with the canonical potential;
  $\tau_K(u)=\diag(\tau_1(u_j))$; $\Cov U=\tfrac13\Id_m$.
- **Theorem C.** Block product
  $\tau\Sigma^{-1}\tau=x_1^2\begin{psmallmatrix}1/\beta+|u|^2/\sigma^2&u^\top/\beta+u^\top B/\sigma^2\\u/\beta+Bu/\sigma^2&uu^\top/\beta+B^2/\sigma^2\end{psmallmatrix}$
  re-multiplied; entries bounded by a constant times $x_1^2$; top-left
  $\beta(\beta+1)(1/\beta+(m/3)\cdot3/(\beta(\beta+1)))=\beta+n$; off-diagonal block zero by
  oddness in $u_j$ (each term of $(u^\top B)_j=|u|^2u_j+\tfrac\beta2u_j(1-u_j^2)$ is odd);
  $B^2=|u|^2uu^\top+\tfrac\beta2(uu^\top D+Duu^\top)+\tfrac{\beta^2}4D^2$ with $(j,k)$ entry
  $|u|^2u_ju_k+\tfrac\beta2u_ju_k(2-u_j^2-u_k^2)+\tfrac{\beta^2}4(1-u_j^2)^2\delta_{jk}$;
  $\gamma=\tfrac15+\tfrac{m-1}9+\tfrac{2\beta}{15}+\tfrac{2\beta^2}{15}$ from $\E u_j^4=\tfrac15$,
  $\E[u_j^2-u_j^4]=\tfrac2{15}$, $\E(1-u_j^2)^2=\tfrac8{15}$; $9\gamma=(6\beta^2+6\beta+5m+4)/5=(6\beta^2+6\beta+5n-1)/5$;
  lower block $[(\beta+1)/3+3\gamma]\Id_m$; normalized
  $G'=1/\beta+9\gamma/(\beta(\beta+1))=(6\beta^2+11\beta+5n+4)/(5\beta(\beta+1))$.
  Inequalities: $1+n/\beta\le2\iff n\le\beta$, proved inline with equality iff $\beta=n$;
  $G'\le2\iff4\beta^2-\beta-5n-4\ge0$; with $n\le\beta$ then $\beta\ge2$,
  $4\beta^2-\beta-5n-4\ge4\beta^2-6\beta-4=2(2\beta+1)(\beta-2)\ge0$; equality forces $n=\beta$
  and $\beta=2$; $G'(2,2)=60/30=2$. Product structure at $n=\beta=2$: $\rho=\tfrac12e^{-x_1}$
  on $\{x_1>|x_2|\}$; $A(c_1,c_2)=(c_1+c_2,c_1-c_2)$, $|\det A|=2$, maps $(0,\infty)^2$ onto
  $C_K$ (inverse $c_1=(x_1+x_2)/2$, $c_2=(x_1-x_2)/2$), $e^{-c_1-c_2}/2=\rho$; $A(1,1)=2e_1$;
  $A=\sqrt2R$ with $R=\begin{psmallmatrix}1&1\\1&-1\end{psmallmatrix}/\sqrt2$ orthogonal,
  $\det R=-1$ (a reflection, as the dossier now says at l. 810–815); $R\sigma$ with the
  coordinate swap $\sigma$ has $\det=+1$ and the i.i.d. law is swap-invariant, so the
  statement's "$\sqrt2$ times an orthogonal map" (l. 714) and the parenthetical rotation
  form are both correct.
- **§5 remarks.** Remark `rem:sol-cone-hypotheses`(4): the witness $\psi_c$ ($c>1$,
  $T_c=\tfrac2{\sqrt c}\operatorname{artanh}(1/\sqrt c)$) was checked:
  $\psi_c'=\sqrt c\tanh(\sqrt c\,y/2)$ equals $\pm1$ at $\pm T_c$;
  $\psi_c''=\tfrac c2\operatorname{sech}^2(\sqrt c\,y/2)=2e^{-\psi_c}$;
  $\int e^{-\psi_c}=\tfrac12[\psi_c']_{-T_c}^{T_c}=1$; pushforward density
  $e^{-\psi_c}/\psi_c''=\tfrac12$ on $(-1,1)$; $\psi_c$ is convex, lower semi-continuous
  (finite at $\pm T_c$, $+\infty$ beyond), discontinuous at $\pm T_c$, hence not essentially
  continuous in dimension one, and not a translate of any finite potential. This confirms that
  the restriction to essentially-continuous potentials in §0 is necessary. The remark is not a
  proof step of any node. Remarks `rem:sol-cone-conventions`, `rem:sol-cone-hodge`,
  `rem:sol-cone-third`, `rem:sol-cone-open` are accurate descriptions of what is and is not
  proved.

### 7. The repaired diff against the first audit's Defect D1

The first audit (`2026-09-06-prop-cone-moment-map-audit.md`, Finding 7) found that the
dossier's §0 defined "moment potential" over all convex $\psi$ with $\int e^{-\psi}=1$, a
class in which uniqueness up to translation is false, while several statements quantified
over that class. The repair chosen is the audit's recommended (R1):

1. **l. 37–50.** "Moment potential" is now an essentially-continuous convex
   $\psi:\R^d\to\R\cup\{+\infty\}$ (CEK Definition 2, quoted correctly) with $\int e^{-\psi}=1$
   and moment measure $\eta$, and the sentence "a finite convex function on $\R^d$ is
   continuous, hence essentially continuous" is present and correct (and is stated in the
   source itself). Each constructed potential — $\varphi$, the rescaled $\lambda$, $\Lambda$,
   $\phi_T$ — is finite, so each is a moment potential in this sense.
2. Under this definition, every sentence the audit listed is now a correct consequence of
   `thm:sol-cone-cek`, checked one by one: l. 219 (Lemma base: "Let $\lambda_K$ be a moment
   potential" — any such is a translate of the canonical one); l. 229–230 ("every moment
   potential of that law is a translate of it"); l. 246–247 (its proof, via the canonical
   $\lambda_K^0$ and translation invariance); l. 267–268 ("any one; all are translates");
   l. 291–292 (Theorem A(iii) statement); l. 343–346 (its proof); l. 653 (Lemma 1D: "a moment
   potential $\lambda_1$ is smooth", via Lemma base in dimension one).
3. **l. 52–70.** The citation is now "Theorem 2 of the arXiv version 1304.0630v1", with the
   specialization to probability measures spelled out and the journal numbering deferred to
   `rem:sol-cone-open`(a) — consistent with Finding 5.
4. **l. 240–250.** Lemma base's proof now goes: compact-target theorem $\Rightarrow$ canonical
   $\lambda_K^0$; CEK $\Rightarrow$ the given $\lambda_K$ is a translate; translation
   preserves smoothness, strict convexity, gradient image and kernel. Correct.
5. **l. 785–787.** $1+n/\beta\le2$ proved inline; Theorem B(ii) no longer a logical input to
   Theorem C (Finding 4).
6. **l. 714, 810–815.** Reflection/rotation wording fixed (Finding 6).
7. **l. 831–847.** Remark (4) reworded with the explicit witness (Finding 6).
8. **Header l. 14.** Second author line added; date 2026-09-06.

No line of the mathematical argument outside these places changed in substance, and every
line of the argument was re-checked regardless (Finding 6).

## Corrections

None required. Two wording observations, recorded for the researcher's discretion and
requiring no new review:

- Theorem B(i), last sentence: "nonconstant $f\in\mathscr P(\R^n)$" means nonconstant on
  $C_K$ (i.e. $\mu$-a.e. nonconstant), matching $\Dom(\calE_\Sigma)\setminus\R$; for an $f$
  constant on $C_K$ the quotient is $0/0$ and is excluded. The proof's argument is for that
  reading.
- Theorem B(ii) and the manuscript write $e_1^\top\E[\tau\Sigma^{-1}\tau]e_1$; for a general
  base only that $(1,1)$ entry is shown finite, which is all the statement uses. The dossier
  says this in `rem:sol-cone-third`.

## Exclusions

- Not certified here: any node other than the three named. In particular the literature
  classification of `thm:regular-moment-map-compact-target` is taken from the ledger, and
  `prop:cmh-hodge`, `lem:linear-sector-third-moment`, `conj:gate-zero-sharp` are untouched.
- Not checked: the manuscript prose surrounding the three statements — the sentence after
  `def:exponential-cone` on square bases not being affine images of products
  (`rem:sol-cone-open`(b)), the attribution to Chen–Klartag Lemma 4.2, and the sentence after
  `lem:linear-sector-third-moment` (l. 332–333 of `41-cmh-normalization.tex`) asserting the
  lemma's integrability hypothesis for every exponential cone. The dossier verifies that
  hypothesis only for the cube. That is a `sync`-lens item for the manuscript, not a defect of
  the nodes under review, and the first audit already recorded it.
- Not decided: the theorem number of CEK's uniqueness theorem in the journal version. The
  dossier cites the arXiv text, which was verified; the journal label remains a
  `literature-scout` item and blocks nothing.
- No `depends_on` edge is added or removed.
