---
candidates:
  - id: cand:directional-h-minus-one-two
    statement: >-
      For every dimension n, every isotropic log-concave probability measure mu on R^n, and
      every theta in S^{n-1}, the linear function ell_theta(x) = <x,theta> satisfies
      ||ell_theta||^2_{H^{-1}(mu)} <= 2, where ||f||_{H^{-1}(mu)} = sup{ int f g dmu : g in
      C_c^infty, int |grad g|^2 dmu <= 1 }. Equality holds for a product of standard centered
      exponential coordinates in any coordinate direction. This is the directional (Loewner)
      form of the summed bound sum_i ||x_i||^2_{H^{-1}(mu)} <= 2n proved as Theorem 1.4 of
      arXiv:2607.23307v1; it is implied by conj:gate-zero-sharp through the Stein-kernel
      comparison ||ell_v||^2_{H^{-1}(mu)} <= E|tau_mu(X) v|^2 of eq:stein-hminus1, and is
      strictly weaker than conj:gate-zero-sharp because it discards the solenoidal channel of
      prop:cmh-hodge.
  - id: cand:letwin-rank-one-second-moment
    statement: >-
      For every isotropic log-concave mu in the regular moment-map class of
      thm:regular-moment-map-compact-target, with canonical Stein kernel tau, and every unit
      vector v in R^n, E_mu[(v^T tau v)^2] <= 2, with equality when mu is a product of standard
      centered exponentials and v is a coordinate direction. This is the rank-one case
      B = v v^T of thm:letwin-moment-map; at p = 2 it sharpens the constant 16 obtainable from
      Proposition 6.1 of Klartag, "Logarithmically-concave moment measures I", to the sharp
      constant 2. It bounds only the scalar Rayleigh quotient v^T tau v and therefore says
      nothing about the column energy E|tau v|^2 that conj:gate-zero-sharp controls.
---

# Literature sweep for the cone lift and the sharp linear sector

Role: `literature-scout`. Identity `/w5/literature-cone`, run id `w5l01`.
Scope: the operator (Loewner) form of the Chen--Klartag moment-Hessian estimate, the
directional third moment, the moment map of cone measures, the $H^{-1}$ norm of linear
functions, and the exact hypotheses of the moment-measure existence/uniqueness theorem.

The dispatch asked for `outcome: directional`. The sweep threw off two statements that have no
other home under `CLAUDE.md` constraint 7, and `scripts/check.py` requires `outcome: candidate`
whenever a `candidates:` list is non-empty, so the front matter says `candidate`. Nothing else
about the record changes: no node's status moved and no route closed.

Everything below was read in the source. Where a full proof was read this is said; where only
the statement was read this is said. No result is imported on the strength of a citation
chain or an abstract.

## 0. Exact statements searched for, in this repository's normalization

Throughout, $\mu$ is isotropic log-concave on $\R^n$, $\varphi$ is its source moment
potential with $(\nabla\varphi)_\#\nu=\mu$, $\dd\nu=e^{-\varphi}\dd y$,
$H=D^2\varphi$, and $\tau_\mu(x)=H((\nabla\varphi)^{-1}x)$ is the canonical Stein kernel
`eq:stein-kernel-def`. $T_3(a)=\E_\mu[\langle X,a\rangle X\otimes X]$.

| # | target | weaker neighbour | stronger neighbour |
|---|---|---|---|
| S1 | $\E_\nu H^2\preceq2\,\mathrm{Id}$ (`conj:gate-zero-sharp`) | $\E_\nu\Tr H^2\le2n$ | $\E_\nu H^2\preceq2\,\mathrm{Id}$ for all centered log-concave, in $\Sigma$-form |
| S2 | $\lVert T_3(\theta)\rVert_{\HS}\le2$ for all unit $\theta$ | $\lVert T\rVert_{\HS}^2\le4n$; $\kappa_n\le2\sqrt2$ | S1 (implies S2 by `cor:gate-zero-third-moment`) |
| S3 | $\lVert\ell_\theta\rVert^2_{H^{-1}(\mu)}\le C$ uniformly | $\sum_i\lVert x_i\rVert^2_{H^{-1}(\mu)}\le Cn$ | S1 |
| S4 | moment potential and Stein kernel of the cone measure $\mu_{K,\beta}$ (`prop:cone-moment-map`) | the $\beta=n$ cone as an ambient construction | the general-$\beta$ family with its kernel |
| S5 | $\E_\nu[\partial_{ijk}\varphi]=\tfrac12\E_\mu[X_iX_jX_k]$ and the column decomposition (`lem:linear-sector-third-moment`) | the summed Bessel bound | the exact Parseval form with the named remainder |

A **notational clash** governs every quotation below and must be carried into the cone dossier.
Klartag (2014) and Chen--Klartag (2026) write $\psi$ for the source potential and
$\varphi=\psi^*$ for its Legendre transform; Letwin (2026) and this repository write
$\varphi$ for the source potential. So Klartag's $\nabla^2\psi$ and Chen--Klartag's $H$ are
this repository's $H=D^2\varphi$, and Klartag's $(\nabla^2\varphi)^{-1}$ is this repository's
$\tau_\mu$.

## 1. Chen--Klartag, arXiv:2607.23307v1 (25 July 2026), `ChenKlartag2026SharpThinShell`

`import_class: preprint-unreviewed`. Source: <https://arxiv.org/abs/2607.23307>,
full text <https://arxiv.org/html/2607.23307v1>. **Only v1 exists** as of 2026-09-06.
Sections 1--4 and Appendix A were read in full, including all proofs cited below.

### 1.1 What it does state

- **Theorem 1.1.** For isotropic log-concave $X$ in $\R^n$, $\E(|X|^2-n)^2\le8n$, with
  equality for i.i.d. standard centered exponential coordinates (density
  $e^{-x-1}\1_{\{x\ge-1\}}$).
- **Theorem 1.2.** $\lVert T\rVert^2_{\HS}\le4n$ for $T=(\E X_iX_jX_k)$, equality for
  independent centered exponentials.
- **Corollary 1.3.** For $X$ uniform on a convex body in $\R^n$,
  $\Var(|X|^2)\le\frac{4n(n+1)^2}{(n+3)(n+4)}$ and
  $\lVert T\rVert^2_{\HS}\le\frac{4n(n-1)(n+2)}{(n+3)^2}$, both sharp at the regular simplex
  in isotropic position.
- **Theorem 1.4.** $\sum_{i=1}^n\lVert x_i\rVert^2_{H^{-1}(\mu)}\le2n$, equality for
  independent centered exponentials, where
  $\lVert f\rVert_{H^{-1}(\mu)}=\sup\{\int fg\dd\mu:g\in C_c^\infty,\int|\nabla g|^2\dd\mu\le1\}$.
- **Theorem 1.5.** Under the regularity assumptions of Klartag (2014) --- $\mu$ supported in a
  bounded open convex $K$, density $\rho$ with $V=-\log\rho$ smooth convex with all partial
  derivatives of all orders bounded --- $\int_{\R^n}|H|^2\dd\nu\le2n$ with $|A|^2=\lVert A\rVert_{\HS}^2$.
- **Lemma 3.1.** $LH+H=A+Q$ with $A=H(\nabla^2V\circ\nabla\psi)H$ and
  $Q_{ij}=\Tr(H^{-1}(\partial_iH)H^{-1}(\partial_jH))$, both positive semidefinite. This is
  the identity the repository records inside `eq:differentiated-MA`.
- **Lemma 3.5.** $q_2-d_2=\tfrac16\sum_{a,i,j}\frac{\psi_{aij}^2}{\lambda_a\lambda_i\lambda_j}
  [(\lambda_a-\lambda_i)^2+(\lambda_i-\lambda_j)^2+(\lambda_j-\lambda_a)^2]\ge0$, hence
  $Q_2\ge D_2$. This is the third-derivative comparison the manuscript sketches at
  `eq:third-derivative-comparison`.
- **Example 3.6.** In dimension one for the standard centered exponential,
  $\psi(t)=e^t-t$, $\dd\nu=e^{-e^t+t}\dd t$, $H(t)=e^t$, $\int H^2\dd\nu=2$.
- **Remark 4.1.** Under the regularity assumptions $\tau$ is the moment-map Stein kernel, as
  observed by Fathi.
- Equation (10): $\Tr H(x)\le2R(K)^2$, quoted from Klartag (2014) Theorem 1.1.

### 1.2 The two prior-art collisions with statements added this session

**(a) `lem:linear-sector-third-moment`'s identity is Chen--Klartag Lemma 3.7.**
Their Lemma 3.7 reads, verbatim in their notation, for all $i,j,k$:
$$T_{ijk}=2\int_{\R^n}\psi_{ijk}\,\dd\nu=2\int_{\R^n}(H_{ij}-\delta_{ij})\psi_k\,\dd\nu.$$
The first equality **is** the manuscript's "the gap-mode coefficient tensor is one half of the
third-moment tensor", $\E_\nu[\partial_{ijk}\varphi]=\tfrac12\E_\mu[X_iX_jX_k]$. I read the
proof: it is the integration by parts $\int\psi_i\psi_j\psi_k\dd\nu=2\int\psi_{ijk}\dd\nu$
justified by their Appendix Lemma, plus $(\nabla\psi)_\#\nu=\mu$.

The second equality, combined with the fact used in their proof of Theorem 1.2 that
$\psi_1,\dots,\psi_n$ are **orthonormal in $L^2(\nu)$**, is the same decomposition the
repository states as $\tau a=a+\tfrac12T_3(a)X+v_a$. Chen--Klartag then apply Bessel:
$$\sum_k\Bigl(\int(H_{ij}-\delta_{ij})\psi_k\dd\nu\Bigr)^2\le\int(H_{ij}-\delta_{ij})^2\dd\nu,$$
summed over $i,j$ to give $\lVert T\rVert^2_{\HS}\le4\int\lVert H-\mathrm{Id}\rVert^2_{\HS}\dd\nu
=4(N_2-n)\le4n$.

What is **not** in the source: the exact (Parseval) form with the orthogonal remainder $v_a$
named and $\E|v_a|^2$ isolated, and the statement column by column rather than summed. That
is what `lem:linear-sector-third-moment` adds, and it is a repackaging of their Lemma 3.7 plus
their Bessel step, not an independent discovery.

Letwin's AI-disclosure paragraph records the same observation independently and without a
numbered statement: "the author noticed that the expected third moment tensor of an isotropic
log-concave random vector in $\R^n$ could be written in terms of the expected third derivative
of the associated moment map."

**(b) `cor:gate-zero-third-moment`'s summed form is the displayed chain in their proof of
Theorem 1.2**, namely $\lVert T\rVert^2_{\HS}\le4(N_2-n)$. The repository's directional
refinement $\lVert T_3(a)\rVert^2_{\HS}\le4(a^\top\E[\tau^2]a-1)$ is **not** in the source;
summing it over an orthonormal basis reproduces theirs exactly.

### 1.3 The cone: Lemma 4.2, and what it does and does not contain

Their **Lemma 4.2** (proof read in full) is the repository's `def:exponential-cone` at
$\beta=\dim$. For $X$ isotropic uniform in a convex body $K\subseteq\R^n$, $k=n+1$, $G$
independent with density $s^{k-1}e^{-s}/(k-1)!$ on $s>0$, and
$$Y=\Bigl(\tfrac{GX}{\sqrt{k(k+1)}},\tfrac{G-k}{\sqrt k}\Bigr)\in\R^k,$$
$Y$ is isotropic and log-concave. The proof shows $(GX,G)$ has density
$\frac{e^{-s}}{n!\,\Vol_n(K)}\1_{\mathcal C}(z,s)$ on the cone
$\mathcal C=\{(sx,s):x\in K,\ s>0\}$. In the repository's normalization this is exactly
$\mu_{K,\beta}$ on $\R^{k}$ with $\beta=k=\dim$, i.e. radial exponent $\beta-\dim=0$ and
density $\propto e^{-x_1}$ on $C_K$ --- the equality case $\beta=n$ of `def:exponential-cone`.

They compute, for $1\le i,j,\ell\le k-1$:
$$T(Y)_{ij\ell}=\tfrac{k+2}{\sqrt{k(k+1)}}T(X)_{ij\ell},\quad
T(Y)_{ij\,k}=\tfrac{2}{\sqrt k}\delta_{ij},\quad
T(Y)_{i\,k\,k}=0,\quad T(Y)_{k\,k\,k}=\tfrac{2}{\sqrt k}.$$
Reading off the axis contraction, $\E[Y_k\,Y\otimes Y]=\tfrac{2}{\sqrt k}\,\mathrm{Id}_k$,
so $\lVert T_3(e_{\rm axis})\rVert_{\HS}=2$. **This is `prop:cone-linear-sector`(iii) at
$\beta=\dim$**, with their axis index $k$ playing the role of the repository's $e_1$ and their
$k$ the repository's $\beta$: $2\beta^{-1/2}\mathrm{Id}$ with $\beta=k$. Also their (26) and
(27) are the second- and third-moment transfer formulas of the same lift.

Their proof of Corollary 1.3 shows that when $K$ is a simplex the lifted $Y$ is an
**orthogonal image of a product of standard centered exponentials**, which is the manuscript's
parenthetical in `def:exponential-cone`.

They attribute the "standard cone construction" and its "underlying conical integration
formula" to Klartag, *Isotropic constants and Mahler volumes*, Adv. Math. 330 (2018), 74--108,
Lemma 2.1. That reference is **not** in `references.bib`; a BibTeX entry is proposed below.
I did not read that source, so this is a lead for the underlying formula, not an import.

What is **not** in Chen--Klartag: any moment potential, Legendre transform, or Stein kernel of
a cone measure; any $\beta\neq\dim$; any base other than a uniform measure on a convex body.
The string "cone" occurs exactly four times in the paper, all in Lemma 4.2 and its two
mentions in the introduction. `prop:cone-moment-map` was not found in this source.

### 1.4 No operator form anywhere

I grepped the full text for `preceq`, "operator", "eigenvalue", "sense of symmetric",
"theta", "unit vector", "direction". The only Loewner-order statement in the whole paper is
$LH+H\ge0$ (their (12), quoted from Klartag (2014) Lemma 5.2) and the positive
semidefiniteness of $A$ and $Q$ in Lemma 3.1. **There is no operator/Loewner form of the
moment-Hessian estimate**, no bound on $\E H^2$ as a matrix, and no directional third-moment
statement. Every displayed estimate of the paper is a trace or a summed quantity.

Consequently `conj:gate-zero-sharp` is not in this source in any form, and the manuscript's
sentence that its trace "is exactly Theorem `thm:chen-klartag-moment-hessian`" is accurate:
their Theorem 1.5 is exactly the trace of the conjectured Loewner inequality.

## 2. Letwin, arXiv:2607.24164v1 (27 July 2026), `Letwin2026QuadraticKLS`

`import_class: preprint-unreviewed`. Source <https://arxiv.org/abs/2607.24164>, full text
<https://arxiv.org/html/2607.24164v1>. **Only v1 exists** as of 2026-09-06. Sections 1 and 2
read in full; Appendix A statements read, proofs skimmed.

- **Theorem 1.2.** $\Var(\langle MX,X\rangle)\le2\,\E|\nabla\langle MX,X\rangle|^2$ for every
  symmetric $M$ and every isotropic log-concave $X$; with $\E|\nabla\langle MX,X\rangle|^2
  =4\Tr(M^2)$ this is $\Var\le8\lVert M\rVert^2_{\HS}$, exactly `thm:letwin-qcts`. He states
  that the constant $2$ is sharp, attained by an isotropic exponential vector at $M=\mathrm{Id}$.
- **$\kappa_n\le2\sqrt2$ is confirmed**, with the repository's definition verbatim:
  $\kappa_n=\sup_\mu\sup_{\theta\in S^{n-1}}\lVert\E[\langle X,\theta\rangle X\otimes X]\rVert_{\HS}$.
  *Citation detail that matters*: this is **not a numbered statement**. It appears inside the
  proof of his Theorem 1.1, by exactly the argument `prop:letwin-kappa` reproduces
  ($\lVert M\rVert^4_{\HS}\le\Var\langle X,\theta\rangle\cdot\Var\langle MX,X\rangle\le8\lVert M\rVert^2_{\HS}$).
  A citation should read "in the proof of [Letwin, Thm. 1.1]", not a theorem number.
- **Theorem 2.5.** $\E_\nu\Tr(B\,\nabla^2\varphi\,B\,\nabla^2\varphi)\le2\Tr(B^2)$ for every
  symmetric $B$, which is `thm:letwin-moment-map`. Proof read.
- **Lemma 2.9.** For centered full-dimensional log-concave $\lambda$ with a symmetric Stein
  kernel of finite $\E\lVert\tau\rVert^2_{\HS}$, and every $v\in\R^n$,
  $\lVert x\mapsto\langle x,v\rangle\rVert^2_{H^{-1}(\lambda)}\le\E|\tau_\lambda(W)v|^2$.
  Proof read. **This is the repository's `eq:stein-hminus1`**, and it is the exact conversion
  from the gate matrix to the directional $H^{-1}$ norm: `conj:gate-zero-sharp` implies
  $\lVert\ell_\theta\rVert^2_{H^{-1}(\mu)}\le2$ for every unit $\theta$, with the loss being
  precisely the solenoidal channel of `prop:cmh-hodge`.
- **Lemma 2.7** is Fathi Theorem 2.3; **Lemma 2.1** is Cordero-Erausquin--Klartag Theorem 2;
  **Lemma 2.2** is Klartag (2014). He quotes Klartag as
  $0\preceq\nabla^2\varphi(y)\preceq2\sup_{x\in K}|x|^2\,\mathrm{Id}$, citing "[46, Theorem 1]".

**No sharper directional statement and no operator-form Hessian statement appear.** Grepped for
"operator norm", "largest eigenvalue", "cone", "simplex", "third-moment": zero hits outside the
$\kappa_n$ passage. The paper contains no cone or simplex analysis at all.

One specialization worth recording (candidate `cand:letwin-rank-one-second-moment`): taking
$B=vv^\top$ with $|v|=1$ in Theorem 2.5 gives $\Tr(BHBH)=(v^\top Hv)^2$ and $\Tr(B^2)=1$,
hence $\E_\nu(v^\top Hv)^2\le2$. This is sharp (product of centered exponentials) and improves
the constant $16$ that Klartag's Proposition 6.1 gives at $p=2$. It controls only the scalar
Rayleigh quotient; the column energy $\E|Hv|^2$ that gate zero needs is exactly what
`prop:letwin-not-gate-zero` shows matrix moments cannot supply.

## 3. Cordero-Erausquin--Klartag and Klartag: the citations the cone dossier needs

### 3.1 `CorderoErausquinKlartag2015MomentMeasures` --- existence and uniqueness

`import_class: published` (J. Funct. Anal. 268(12) (2015) 3834--3866). Read at
<https://arxiv.org/html/1304.0630v1>, arXiv v1, submitted 2 April 2013; **only v1 exists**.
Statements read in full; the uniqueness proof (Section 4) read; the existence proof skimmed.

- **Definition 1.** For convex $\psi:\R^n\to\R\cup\{+\infty\}$ with
  $0<\int e^{-\psi}<\infty$, the moment measure of $\psi$ is $(\nabla\psi)_\#(e^{-\psi}\dd x)$.
- **Definition 2.** $\psi$ is *essentially-continuous* if it is lower semi-continuous and its
  set of discontinuity points has zero $\mathcal H^{n-1}$-measure.
- **Proposition 1** (necessity). If $\psi$ is essentially-continuous convex with
  $0<\int e^{-\psi}<+\infty$, its moment measure is not supported in a hyperplane and has
  barycenter at the origin.
- **Theorem 2** (the statement to cite). Let $\mu$ be a Borel measure on $\R^n$ with
  (i) $0<\mu(\R^n)<+\infty$; (ii) $\mu$ not supported in a lower-dimensional subspace;
  (iii) barycenter at the origin (in particular $\mu$ has finite first moments). *Then there
  exists an essentially-continuous convex $\psi:\R^n\to\R\cup\{+\infty\}$ whose moment measure
  is $\mu$. Moreover, such $\psi$ is uniquely determined up to translation.*

So the exact citation for the cone dossier is **Theorem 2** of the arXiv version, the same
number Letwin cites as "[21, Theorem 2]". *Citation debt*: the theorem numbering of the
**published** JFA version was not verified here; if the dossier cites the journal, the number
must be re-checked against the journal text.

The hypotheses are stated over $\R^n$ with *linear span* full, not over an affine subspace:
$\bar\mu_{K,\beta}$ is centered, has finite moments of all orders, and spans $\R^n$, so
Theorem 2 applies to it and pins its moment potential up to translation. That is exactly what
`prop:cone-moment-map` needs to be a statement about *the* moment potential.

### 3.2 Scaling relation and cone/homogeneous examples --- **not found**

Neither paper states $\lambda_{\beta K}(y)=\lambda_K(\beta y)+\mathrm{const}$ as a numbered
result. The closest is an unnumbered remark in Cordero-Erausquin--Klartag just after their
cube example (5): "By linear invariance, we may express the uniform probability measure on a
centered parallelepiped in $\R^n$ as the moment measure of $x\to\psi(T(x))+C$ for some linear
map $T$ and $C\in\R$."

The general form follows in one line from their Definition 1 by change of variables: if $\mu$
is the moment measure of $\psi$, then for invertible linear $S$ the moment measure of
$y\mapsto\psi(Sy)-\log|\det S|$ is $(S^\top)_\#\mu$. Specializing to $S=\beta\,\mathrm{Id}$ on
$\R^{m}$ gives $\lambda_{\beta K}(y)=\lambda_K(\beta y)-m\log\beta$, i.e. the repository's
relation with the constant made explicit. **The dossier should prove this line rather than
cite it**; there is no numbered statement to cite.

The explicit examples in Cordero-Erausquin--Klartag are: $|x|^2/2\mapsto$ Gaussian;
$|x|\mapsto$ uniform on $S^{n-1}$; $\sum_i2\log\cosh(x_i/2)\mapsto$ uniform on $[-1,1]^n$;
$(n+1)\log\sum_{i=0}^n\exp(x\cdot v_i/(n+1))\mapsto$ uniform on the simplex with vertices
$v_i$. **No cone example.** Their Section 5 does discuss "cones", but in the sense of the
*cone volume measure* of the logarithmic Minkowski problem --- a measure on $\partial K^\circ$
obtained from a radial $\psi(x)=f(\lVert x\rVert_K)$. That is a different object from a
measure supported on a convex cone, and it does not give `prop:cone-moment-map`.

Klartag (2014) contains no cone, no simplex, and no scaling relation: grepped for "cone",
"simplex", "scal", "homogeneous", "linear invarian" --- zero relevant hits.

### 3.3 `Klartag2013MomentMeasures` --- the compact-target Hessian bound, re-confirmed with a correction

`import_class: published` (Geometric Aspects of Functional Analysis, LNM 2116, Springer, 2014).
Read at <https://arxiv.org/html/1309.2767v1>. This re-confirms
`research/explorations/2026-08-27-literature-scout-cmh-hessian-recovery-w3l01.md` with one
correction of record.

- **Theorem 1.1** (the numbered statement) is the **Laplacian** form: for a log-concave
  probability $\mu$ with barycenter at the origin satisfying the regularity conditions (1),
  $\Delta\psi(x)\le2R^2(K)$ for every $x$, where $R(K)=\sup_{x\in K}|x|$.
- The **Loewner** form the repository uses is stated in Section 6 as unnumbered text
  immediately before Proposition 6.1: "Theorem 1.1 states that $\Delta\Psi(x)\le2R^2(K)$
  everywhere in $\R^n$. A weak conclusion is that $\nabla^2\psi(x)\le2R^2(K)\cdot Id$, or
  rather, that $(\nabla^2\varphi(x))^{-1}\le2R^2(K)\cdot Id$." It is then used to derive
  $\Var_\mu(f)\le2R^2(K)\int|\nabla f|^2\dd\mu$.
  Since $\nabla^2\psi\succ0$, "$\Delta\psi\le2R^2$" and "$\nabla^2\psi\preceq2R^2\,\mathrm{Id}$"
  are equivalent up to the trivial direction; the repository's
  $0\prec D^2\varphi\preceq2R^2\,\mathrm{Id}$ is correct, but a citation should name
  **Theorem 1.1** and note that the Loewner reading is the paper's own immediate consequence.
  Chen--Klartag quote the same result as $\Tr H(x)\le2R(K)^2$, their (10). Letwin quotes it as
  $0\preceq\nabla^2\varphi(y)\preceq2\sup_{x\in K}|x|^2\,\mathrm{Id}$, his "[46, Theorem 1]".
- **Proposition 6.1** (verified, proof read): for fixed $\theta\in S^{n-1}$ and
  $V=\int(x\cdot\theta)^2\dd\mu$, for every $p\ge1$,
  $\bigl(\int_K|((\nabla^2\varphi)^{-1}\theta\cdot\theta)/V|^p\dd\mu\bigr)^{1/p}\le4p^2$.
  In this repository's notation $(\nabla^2\varphi)^{-1}=\tau_\mu$, so this is a scalar
  Rayleigh-quotient moment bound, not a column-energy bound --- exactly as w3l01 recorded.
  At $p=2$ it is superseded by `cand:letwin-rank-one-second-moment` above.
- Klartag's **Lemma 5.2**, quoted by Chen--Klartag as $LH+H\ge0$ in the Loewner order, is the
  ancestor of `eq:differentiated-MA`.

## 4. The $H^{-1}$ norm of linear functions: what is known, and with which constants

| statement | source | constant | class |
|---|---|---|---|
| $\Var_\lambda(f)\le\sum_i\lVert\partial_if\rVert^2_{H^{-1}(\lambda)}$ for locally Lipschitz $f$ with $\E\partial_if=0$ | Barthe--Klartag, Prop. 10, quoted as Letwin Prop. 2.8 | $1$ | log-concave $\lambda$, not necessarily isotropic |
| $\lVert\ell_v\rVert^2_{H^{-1}(\lambda)}\le\E\lvert\tau_\lambda(W)v\rvert^2$ | Letwin Lemma 2.9 | exact comparison | log-concave with symmetric $L^2$ Stein kernel |
| $\sum_i\lVert x_i\rVert^2_{H^{-1}(\mu)}\le Cn$, $C$ not explicit | Klartag--Lehec, arXiv:2507.15495v2, Thm. 1.4 | universal, unspecified | isotropic log-concave |
| $\sum_i\lVert x_i\rVert^2_{H^{-1}(\mu)}\le2n$, sharp | Chen--Klartag, arXiv:2607.23307v1, Thm. 1.4 | $2n$, equality for products of centered exponentials | isotropic log-concave |
| $\lVert\ell_v\rVert_{H^{-1}(\mu)}\le\limsup_{\eps\to0^+}W_2(\mu,\mu_{\eps v})/\eps$ | Klartag--Lehec 2507.15495v2, Lemma 4.4 | exact comparison | centered compactly supported |
| $\limsup_\eps W_2(\mu,\mu_{\eps v})/\eps\le(\E|M_tv|^2)^{1/2}/t$ | Klartag--Lehec 2507.15495v2, Cor. 4.3 | exact, all $t>0$, all $v$ | log-concave |
| $\sum_i\lVert x_i\rVert^2_{H^{-1}(\mu)}\le t^{-2}\E|M_t|^2$ | Klartag--Lehec 2507.15495v2, Cor. 4.5 | exact | centered compactly supported log-concave |
| $\E\sum_i\exp(2\int_0^1\lambda_i(t)\dd t)\le Cn$ | Klartag--Lehec 2507.15495v2, Thm. 6.2 | universal, unspecified | isotropic compactly supported |

**The directional statement S3 was not found with any constant.** The sharpest thing in the
literature is the trace form at the sharp constant $2n$ (Chen--Klartag Theorem 1.4), whose
directional strengthening --- $\lVert\ell_\theta\rVert^2_{H^{-1}(\mu)}\le2$ for every unit
$\theta$, recorded here as `cand:directional-h-minus-one-two` --- is open. Klartag--Lehec's
machinery is instructive: their Lemma 4.4 and Corollary 4.3 *are* directional, so the
directional bound $\lVert\ell_v\rVert^2_{H^{-1}(\mu)}\le t^{-2}\E|M_tv|^2$ holds for every
$v$; but their terminal estimate, Theorem 6.2, is a sum over the eigenvalues of the
stochastic-localization covariance process, and an operator upgrade would require controlling
$\E\exp(2\int_0^1\lambda_1)$ for the *top* eigenvalue alone. That is the same operator-to-trace
shape as `rem:gate-zero-trace-upgrade`, reached by an entirely different route.

**Negatives for the four sources named in the task.** Full texts were converted and grepped.

- Klartag--Lehec, *Bourgain's slicing problem and KLS isoperimetry up to polylog*
  (arXiv:2203.15551v2), `KlartagLehec2022Polylog`: defines
  $\kappa_n^2=\sup_X\sup_{\theta\in S^{n-1}}\lVert\E\langle X,\theta\rangle(X\otimes X)\rVert_2^2$
  --- the repository's `eq:kappa-def` --- and the relation
  $\psi_n^2\le C\log n\cdot\kappa_n^2\le\tilde C\log^2n\cdot\sigma_n^2$ attributed to Eldan.
  Zero occurrences of "$H^{-1}$", "Stein", "moment map", "moment measure", "cone".
- Klartag, *Logarithmic bounds for isoperimetry and slices of convex sets* (arXiv:2303.14938v2),
  `Klartag2023Logarithmic`: $\kappa_n$ appears only in the remark around (3.13)--(3.14), with
  $\kappa_n^2\le4\sup_XC_P(X)\le C\psi_n^2$. Zero occurrences of "$H^{-1}$", "Stein",
  "moment map", "moment measure", "cone".
- Klartag--Lehec, Bulletin AMS survey (arXiv:2406.01324v2), `KLnotes`: zero occurrences of
  "$H^{-1}$", "moment map", "moment measure", "$\kappa_n$" in the sense above. It is not a
  source for any statement in this sweep.
- Fathi, *Stein kernels and moment maps* (arXiv:1804.04699v3), `Fathi2019SteinMomentMaps`:
  **Theorem 2.3** (proof read) --- if $\mu$ has a density and the moment potential $\varphi$
  is $C^2$ with full support, then $\Hess\varphi\circ\nabla\varphi^*$ is a Stein kernel for
  $\mu$, and $S(\mu)^2\le\int|\Hess\varphi-\mathrm{Id}|^2_{\HS}e^{-\varphi}\dd x$;
  **Corollary 2.4** --- if $\dd\mu=e^{-V}\dd x$ with $\Hess V\succeq\eps\,\mathrm{Id}$ then
  there is a positive symmetric Stein kernel with $\lVert\tau\rVert_{\op}\le\eps^{-1}$.
  No second-moment operator bound, no directional $H^{-1}$ statement, no cone.

### 4.1 The closest operator-form result found, and why it is not gate zero

Tianle Liu, *Stein Kernels and Normal Approximation for Log-Concave Bilinear Forms*,
arXiv:2608.27657v2, 1 September 2026 (v1 27 August 2026). `import_class: preprint-unreviewed`.
Statements read; proofs of Lemma 3.1 and Proposition 3.2 read; the rest skimmed.

Working in the same regular moment-map model, with $f_A=\Tr(AH)$, $q_A=Y^\top AY$,
$T_A=\E(AY)^\top H(AY)$, $U_A=\E\Tr(AHAH)$, he proves the exact identity
$\Var(f_A)=\Var(q_A)-3T_A+U_A$ (Lemma 3.1), polarizes it to
$\Gamma_{\rm tr}=\tfrac14\Gamma_{\rm quad}+\mathsf U-\tfrac34\mathsf D$ with
$\mathsf D=4\mathsf T-\Gamma_{\rm quad}\succeq0$ by the weighted Poincaré inequality
(Proposition 3.2), and concludes (Theorem 3.3, Corollaries 3.4--3.5), **subject to Letwin's
Theorems 1.2 and 2.5**:
$$0\preceq\Gamma_{\rm tr}\preceq4\,I_{\mathsf S_n},\qquad
\Gamma_{\rm tr}(A,B)=\Cov(\Tr(AH),\Tr(BH)),$$
together with $\Tr_{\mathsf S_n}\Gamma_{\rm tr}=\E\lVert H-\mathrm{Id}\rVert^2_{\HS}\le n$.

This **is** an operator-to-trace upgrade in this circle of ideas, and it is obtained for free
from Letwin's all-$B$ theorem --- but on the wrong space. $\Gamma_{\rm tr}$ acts on symmetric
matrices, whereas `conj:gate-zero-sharp` is a statement about the $n\times n$ matrix
$\E[H^2]$ acting on $\R^n$. Writing $\E|(H-\mathrm{Id})a|^2$ in a Hilbert--Schmidt orthonormal
family and applying his Corollary 3.5 yields only $\E|(H-\mathrm{Id})a|^2\le n$, which is the
unconditional bound `lem:cmh-linear-spectral-resolution` already records as
$Q_{\rm lin}\le n+1$. **It does not give gate zero, sharp or otherwise.** Per `CLAUDE.md` P1,
this comparison is reported and not acted on: no partial result is transferred across the
trace-upgrade cluster here.

## 5. Collisions with repository fences

None. `conj:gate-zero-sharp` carries no `bounded_by`; `prop:letwin-not-gate-zero` fences only
the deduction of gate zero from constant-matrix moments, and every literature result verified
here is a trace or summed statement that lands on the weak side of that fence. Chen--Klartag
Theorem 1.4 at the sharp constant $2n$ is consistent with `prop:cone-linear-sector`(ii): the
$\beta=n$ cone attains $1+n/\beta=2$ in its axis direction, and the trace bound permits exactly
one saturating direction per unit of budget.

## 6. Proposed ledger delta

No node's *logical status* changes. Two provenance/reference deltas and one new import are
proposed; all are for the orchestrator to apply, and I wrote neither `ledger.yaml` nor
`references.bib`.

### 6.1 Reference and attribution deltas on nodes added this session

```yaml
# lem:linear-sector-third-moment -- keep provenance: internal, keep status: open,
# but the identity half of it is prior art. Add:
    references: [ChenKlartag2026SharpThinShell]
# and add to the manuscript, immediately after the lemma:
#   "The identity E_nu[d_ijk phi] = (1/2) E_mu[X_i X_j X_k] is Lemma 3.7 of
#    \cite{ChenKlartag2026SharpThinShell}; the orthogonal decomposition above is the
#    exact form of the Bessel step in their proof of Theorem 1.2."

# cor:gate-zero-third-moment -- keep provenance: internal, keep status: open. Add:
    references: [ChenKlartag2026SharpThinShell]
# manuscript note: summing the displayed directional bound over an orthonormal basis
# recovers ||T||_HS^2 <= 4 (N_2 - n) <= 4n, the chain in their proof of Theorem 1.2.

# prop:cone-linear-sector -- keep provenance: internal, keep status: open. Add:
    references: [ChenKlartag2026SharpThinShell]
# manuscript note on part (iii): at beta = n this is the third-moment computation in
# Lemma 4.2 of \cite{ChenKlartag2026SharpThinShell}.

# def:exponential-cone -- keep provenance: internal, keep status: defined. Add:
    references: [ChenKlartag2026SharpThinShell, Klartag2018IsotropicMahler]
# manuscript note: the beta = n case is the cone construction of their Lemma 4.2, whose
# conical integration formula they attribute to \cite[Lemma 2.1]{Klartag2018IsotropicMahler}.

# prop:cone-moment-map, conj:gate-zero-sharp -- no change. Nothing in the sweep is prior
# art for either; both remain internal and open.
```

### 6.2 Optional literature node

Only if the orchestrator wants the directional $H^{-1}$ machinery cited in the manuscript:

```yaml
- id: thm:kl-parallel-coupling-directional-h-minus-one
  kind: theorem
  status: open           # unreviewed preprint
  provenance: literature
  import_class: preprint-unreviewed
  file: modules/kls/04-family-moment-map.tex   # anchor must be added first
  summary: >-
    Klartag-Lehec parallel coupling, directional form. For centered compactly supported
    log-concave mu with stochastic-localization derivative process M_t, every v in R^n and
    every t > 0 satisfy ||<x,v>||^2_{H^{-1}(mu)} <= t^{-2} E|M_t v|^2 (Lemma 4.4 with
    Corollary 4.3). Summing over an orthonormal basis and applying their Theorem 6.2 gives
    sum_i ||x_i||^2_{H^{-1}(mu)} <= C n (their Theorem 1.4); the operator form would need
    control of the top eigenvalue of the covariance process alone.
  references: [KlartagLehec2025ThinShell]
```

### 6.3 Exact append-only BibTeX

`Klartag2018IsotropicMahler` is needed by the `def:exponential-cone` attribution above;
`Liu2026BilinearSteinKernels` only if the orchestrator wants section 4.1 cited.

```bibtex
@article{Klartag2018IsotropicMahler,
  author  = {Klartag, Bo'az},
  title   = {Isotropic Constants and {Mahler} Volumes},
  journal = {Advances in Mathematics},
  volume  = {330},
  pages   = {74--108},
  year    = {2018},
  doi     = {10.1016/j.aim.2018.03.008}
}

@misc{Liu2026BilinearSteinKernels,
  author        = {Liu, Tianle},
  title         = {Stein Kernels and Normal Approximation for Log-Concave Bilinear Forms},
  year          = {2026},
  eprint        = {2608.27657},
  archivePrefix = {arXiv},
  primaryClass  = {math.PR},
  note          = {Version 2, 1 September 2026; preprint}
}
```

The BibTeX entry for `Klartag2018IsotropicMahler` records bibliographic data taken from
Chen--Klartag's reference list, not from the article itself; its DOI was not verified at the
publisher and must be checked before the entry is relied on.

## 7. Gap

After every import above, the following remain open, verbatim:

1. **`conj:gate-zero-sharp`.** For every isotropic log-concave moment measure,
   $\E_\nu H^2\preceq2\,\mathrm{Id}$. The literature proves exactly its trace,
   $\E_\nu\Tr H^2\le2n$ (Chen--Klartag Thm. 1.5), and a different operator upgrade on the
   space of symmetric matrices that does not imply it (section 4.1).
2. **`cand:directional-h-minus-one-two`.** For every isotropic log-concave $\mu$ and unit
   $\theta$, $\lVert\ell_\theta\rVert^2_{H^{-1}(\mu)}\le2$. The literature proves exactly its
   trace, $\sum_i\lVert x_i\rVert^2_{H^{-1}(\mu)}\le2n$ (Chen--Klartag Thm. 1.4).
3. **The directional third moment at the sharp constant.** $\lVert T_3(\theta)\rVert_{\HS}\le2$
   for every unit $\theta$. The literature proves $\lVert T\rVert^2_{\HS}\le4n$ (Chen--Klartag
   Thm. 1.2) and $\kappa_n\le2\sqrt2$ (Letwin, in the proof of his Thm. 1.1). The gap between
   $2\sqrt2$ and the conjectured $2$ is exactly a factor $\sqrt2$, and the cones of
   `prop:cone-linear-sector` attain $2$, so no constant below $2$ is available.
4. **`prop:cone-moment-map`.** No source computes the moment potential or Stein kernel of a
   cone measure at any $\beta$, and no source treats $\beta\neq\dim$. It stands as internal
   work needing an internal proof and an independent review.

## 8. Citation debt

- `prop:letwin-kappa`: $\kappa_n\le2\sqrt2$ is not a numbered statement in
  `Letwin2026QuadraticKLS`; it is derived inside the proof of his Theorem 1.1. The manuscript
  and any dossier should cite "in the proof of [Letwin, Thm. 1.1]".
- `modules/kls/15-covariance-technology.tex` line 87 says "Both results are imported from
  version 2 of an unreviewed preprint". Letwin's preprint has **only v1** on arXiv as of
  2026-09-06; `KlartagLehec2025ThinShell` is the one with a v2 (23 February 2026, confirmed
  against the arXiv submission history). A `reviewer` on the `sync` lens should confirm which
  preprint that sentence's "both results" refers to.
- `CorderoErausquinKlartag2015MomentMeasures`: verified as **Theorem 2** in arXiv v1 only.
  The published J. Funct. Anal. numbering was not checked. Any dossier citing the journal must
  re-verify the number.
- `Klartag2013MomentMeasures`: the repository's Loewner reading
  $0\prec D^2\varphi\preceq2R^2\,\mathrm{Id}$ is correct but is *not* the numbered statement;
  Theorem 1.1 is $\Delta\psi\le2R^2(K)$, and the Loewner form is an unnumbered consequence
  drawn in his Section 6. Cite Theorem 1.1 and say "equivalently, since $D^2\varphi\succ0$".
  Note also the $\psi/\varphi$ notational inversion between that paper and this repository.
- `Klartag2018IsotropicMahler` (proposed): bibliographic data taken from a reference list, not
  verified at the source; Lemma 2.1 of that paper was **not** read, so the conical integration
  formula is a lead, not an import.
- The scaling relation $\lambda_{\beta K}(y)=\lambda_K(\beta y)+\mathrm{const}$ has **no**
  numbered citation in either moment-measure paper. Prove it in the dossier from
  Cordero-Erausquin--Klartag Definition 1; the constant is $-m\log\beta$ in dimension $m$.

## 9. Searched and not found

Queries run, and what they failed to produce.

- Full-text greps of arXiv:2607.23307v1 for `preceq`, "operator", "operator norm",
  "eigenvalue", "sense of symmetric", "theta", "unit vector", "direction", "moment potential",
  "Legendre": **no** operator/Loewner form of the moment-Hessian estimate, **no** directional
  third-moment statement, **no** moment potential of a cone.
- Full-text greps of arXiv:2607.24164v1 for "cone", "simplex", "operator norm", "largest
  eigenvalue", "third-moment", "sharp": **no** cone or simplex analysis, **no** operator-form
  Hessian statement, **no** directional statement sharper than $\kappa_n\le2\sqrt2$.
- Full-text greps of arXiv:1304.0630v1 and arXiv:1309.2767v1 for "cone", "simplex",
  "homogeneous", "scal", "linear invarian", "Gamma", "exponential": **no** numbered scaling
  relation, **no** cone-supported moment measure. The only "cone" in
  Cordero-Erausquin--Klartag is the cone *volume* measure of the logarithmic Minkowski problem.
- Full-text greps of arXiv:2303.14938v2, arXiv:2203.15551v2, arXiv:2406.01324v2 and
  arXiv:1804.04699v3 for "$H^{-1}$", "Stein", "moment map", "moment measure", "cone", "third
  moment": as tabulated in section 4; none contains S1, S2, S3 or S4.
- Web searches: "moment measure of a cone measure log-concave moment potential Gamma radial
  explicit"; "\"moment map\" log-concave \"Stein kernel\" operator inequality \"E[tau^2]\"
  isotropic bound 2 identity"; "arXiv 2026 sharp thin-shell moment measure operator form
  \"E H^2\" Loewner isotropic log-concave follow-up Chen Klartag"; "\"moment map\" OR \"moment
  potential\" of measure on a cone over convex body Gamma radial \"log-concave\" explicit
  Legendre exp"; "\"third moment\" directional bound isotropic log-concave \"E[<X,theta> X
  otimes X]\" Hilbert-Schmidt norm at most 2 sharp exponential". These surfaced
  arXiv:2608.27657 (section 4.1) and arXiv:2608.20816 (*Thin-Shell implies small-ball deviation
  via Gaussian tilts*, checked and irrelevant: no moment map, no $H^{-1}$, no cone), and
  nothing containing S1, S3 or S4.

## 10. Handoff

```yaml
outcome: complete
artifacts:
  - research/explorations/2026-09-06-literature-scout-cone-lift-w5l01.md
proposed_deltas:
  - "Add references: [ChenKlartag2026SharpThinShell] to lem:linear-sector-third-moment,
     cor:gate-zero-third-moment and prop:cone-linear-sector; add
     references: [ChenKlartag2026SharpThinShell, Klartag2018IsotropicMahler] to
     def:exponential-cone. All four keep provenance: internal and their current status."
  - "Append the Klartag2018IsotropicMahler BibTeX entry of section 6.3 to references.bib."
  - "Add the three attribution sentences of section 6.1 to modules/kls/41-cmh-normalization.tex
     and modules/kls/42-cmh-exact-cases.tex."
portfolio_delta:
  - "ap:cmh-gate-zero: stays queued. The literature sweep found no operator-form statement to
     import and no obstruction; the route's first target conj:gate-zero-sharp is confirmed
     open, with its trace proved in the literature at the sharp constant."
next_role: orchestrator
next_prompt: |
  Apply the following, atomically, and re-run python3 scripts/check.py.

  (1) references.bib -- append exactly:

  @article{Klartag2018IsotropicMahler,
    author  = {Klartag, Bo'az},
    title   = {Isotropic Constants and {Mahler} Volumes},
    journal = {Advances in Mathematics},
    volume  = {330},
    pages   = {74--108},
    year    = {2018},
    doi     = {10.1016/j.aim.2018.03.008}
  }

  Do not add Liu2026BilinearSteinKernels unless you also add a manuscript sentence citing it.

  (2) ledger.yaml -- add a references field to four existing nodes, changing nothing else,
  in particular not their status and not their provenance (they stay internal):
    lem:linear-sector-third-moment  references: [ChenKlartag2026SharpThinShell]
    cor:gate-zero-third-moment      references: [ChenKlartag2026SharpThinShell]
    prop:cone-linear-sector         references: [ChenKlartag2026SharpThinShell]
    def:exponential-cone            references: [ChenKlartag2026SharpThinShell, Klartag2018IsotropicMahler]

  (3) modules/kls/41-cmh-normalization.tex -- after lem:linear-sector-third-moment add:
  "The identity $\E_\nu[\partial_{ijk}\varphi]=\tfrac12\E_\mu[X_iX_jX_k]$ is Lemma~3.7 of
  \cite{ChenKlartag2026SharpThinShell}, and the orthogonal decomposition above is the exact
  form of the Bessel step in the proof of their Theorem~1.2; what is added here is the
  directional statement with the remainder $v_a$ named."
  After cor:gate-zero-third-moment add: "Summing over an orthonormal basis recovers
  $\norm{T}_{\HS}^2\le4(N_2-n)\le4n$, the chain in the proof of Theorem~1.2 of
  \cite{ChenKlartag2026SharpThinShell}."

  (4) modules/kls/42-cmh-exact-cases.tex -- after def:exponential-cone add: "The case
  $\beta=n$ is the cone construction of Lemma~4.2 of \cite{ChenKlartag2026SharpThinShell},
  whose conical integration formula they attribute to
  \cite[Lem.~2.1]{Klartag2018IsotropicMahler}; the general $\beta\ge n$ family and its moment
  map are not treated there." After prop:cone-linear-sector add: "At $\beta=n$, part (iii)
  is the third-moment computation of that lemma, which gives
  $T(Y)_{ijk}=2\delta_{ij}/\sqrt k$, $T(Y)_{ikk}=0$, $T(Y)_{kkk}=2/\sqrt k$ with $k=\beta$."

  (5) Do NOT change the status or provenance of conj:gate-zero-sharp or prop:cone-moment-map.
  The sweep found no prior art for either: no source states any operator or Loewner form of the
  moment-Hessian estimate, and no source computes the moment potential or Stein kernel of a
  cone measure at any beta.

  (6) Two candidates are live in this checkpoint and are not to be promoted here:
  cand:directional-h-minus-one-two and cand:letwin-rank-one-second-moment.

  (7) Route to a reviewer on the sync lens: modules/kls/15-covariance-technology.tex says
  "Both results are imported from version 2 of an unreviewed preprint", but
  Letwin2026QuadraticKLS has only v1 on arXiv as of 2026-09-06; KlartagLehec2025ThinShell is
  the one with a v2 (23 February 2026). Confirm the antecedent of that sentence.
  Also: prop:letwin-kappa's kappa_n <= 2 sqrt 2 is not a numbered statement in the preprint --
  it is derived inside the proof of Letwin's Theorem 1.1 -- and Klartag2013MomentMeasures's
  numbered Theorem 1.1 is the Laplacian form Delta psi <= 2 R^2(K), the Loewner reading being
  an unnumbered consequence in his Section 6.
```
