---
---
# Literature audit: regular moment-map approximants for CMH closure

Date: 2026-08-27

Role: `literature-scout`

Upstream target: `q:cmh-approximation`

## Exact statement searched for

The desired input, in the repository's normalization, was the following.

> Let $\mu(dx)=Z^{-1}e^{-V(x)}dx$ be centered and full-dimensional, with $V\in C^\infty$
> and $aI\preceq D^2V\preceq bI$.  Does its canonical moment potential $\varphi$ satisfy
> $(\nabla\varphi)_\#(e^{-\varphi}dy)=\mu$, with $\varphi$ smooth and strictly convex and
> $\nabla\varphi$ a global diffeomorphism, and does
> $$
> H(x)=D^2\varphi((\nabla\varphi)^{-1}(x))
> $$
> give all of the Stein identity, zero boundary flux, and closed-form data used by
> `thm:cmh-implies-affine-poincare`?

A sufficient stronger neighbour was also searched for: the same conclusion for a target
$\mu(dx)=g(x)\mathbf 1_{\operatorname{int}P}(x)dx$, where $P$ is a convex body and
$g\in C^\infty(\mathbb R^n)$ is positive.  This stronger class is enough if an arbitrary
centered log-concave law, including one on a proper affine subspace, has centered
$W_2$-convergent approximants in it.

The target has no `bounded_by` edge.  None of the fixed-cut Eldan obstructions is implicated.

## Found: published regularity theorem for compact targets

### Berman--Berndtsson, Theorem 1.1

Source: Robert J. Berman and Bo Berndtsson, *Real Monge--Amp\`ere equations and
K\"ahler--Ricci solitons on toric log Fano varieties*, Annales de la Facult\'e des Sciences de
Toulouse 22 (2013), no. 4, 649--711, DOI
[10.5802/afst.1386](https://doi.org/10.5802/afst.1386).  The published result is
`import_class: published`.  I read [Theorem 1.1 and its proof, including the regularity step in
Section 2.9](https://arxiv.org/html/1207.6128v1#S2.SS9), not only the abstract.

Theorem 1.1 says: if $P$ is a convex body containing $0$ in its interior and $g$ is a positive
smooth function, there is a smooth convex $\varphi$ satisfying
$$
g(\nabla\varphi(y))\det D^2\varphi(y)=e^{-\varphi(y)},
\qquad
\nabla\varphi:\mathbb R^n\longrightarrow\operatorname{int}P
$$
with $\nabla\varphi$ a diffeomorphism if and only if $0$ is the barycenter of $g(x)dx$ on
$P$.  The proof constructs the weak solution variationally, obtains local smoothness through
Caffarelli/Evans--Krylov regularity, and proves the global gradient-image statement.

#### Conversion to the repository normalization

Take
$$
d\mu(x)=g(x)\mathbf 1_{\operatorname{int}P}(x)dx,
\qquad
g(x)=Z^{-1}e^{-V(x)},
\qquad
\int_P g=1,\qquad \int_P xg(x)dx=0.
$$
The Monge--Amp\`ere equation and the diffeomorphism give, without an extra constant,
$$
(\nabla\varphi)_\#(e^{-\varphi(y)}dy)=\mu,
\qquad
\int_{\mathbb R^n}e^{-\varphi}=\int_Pg=1.
$$
Because $D(\nabla\varphi)=D^2\varphi$ is invertible everywhere and $\varphi$ is convex,
$D^2\varphi\succ0$ everywhere; hence $\varphi$ is strictly convex.  Thus the theorem supplies
the exact smooth moment potential and global target-coordinate map required by the regular CMH
endpoint.  No dimension-dependent or approximation constant occurs.

This theorem does **not** cover the original untruncated full-support Gaussian-tilt family: its
target is a bounded convex body.

## Found: published canonical Stein identity and zero flux

### Fathi, Theorem 2.3

Source: Max Fathi, *Stein Kernels and Moment Maps*, Annals of Probability 47 (2019), no. 4,
2172--2185, DOI [10.1214/18-AOP1305](https://doi.org/10.1214/18-AOP1305).  The result is
`import_class: published`.  I read [Theorem 2.3 and its proof in arXiv v3, 7 June
2023](https://arxiv.org/html/1804.04699v3#S2.SS2), whose version note says that v3 corrects a
sentence without changing results or proofs.

Under a $C^2$ entire moment potential, Theorem 2.3 proves that
$$
H(x)=D^2\varphi((\nabla\varphi)^{-1}(x))
$$
is a positive symmetric Stein kernel.  In the repository's scalar-test normalization, for every
$f\in C_c^\infty(\mathbb R^n)$,
$$
\int x_i f(x)d\mu(x)=\int\sum_jH_{ij}(x)\partial_jf(x)d\mu(x).
\tag{S}
$$
Fathi's proof integrates on the source $\mathbb R^n$ and explicitly notes that no boundary term
remains because the convex integrable $\varphi$ grows at least linearly.  After the global
diffeomorphism change of variables this is exactly the target-coordinate identity.

For the compact target above, (S) has the following exact local consequences:

- $H\in C^\infty(\operatorname{int}P;\operatorname{Sym}_n^{++})$;
- $\operatorname{Div}_\mu H=-x$ distributionally on ambient $\mathbb R^n$;
- because the distributional identity has no boundary measure on $\partial P$, it includes the
  zero normal trace of $gH$ at the boundary in the weak sense needed by the ambient smooth core;
- testing with a cutoff equal to the coordinate function on the bounded set $P$ gives
  $\mathbb E_\mu H=\mathbb E_\mu[X\otimes X]=\Sigma$.

Thus Berman--Berndtsson Theorem 1.1 plus Fathi Theorem 2.3 supply all non-elementary
regularity and boundary input used by `thm:cmh-implies-affine-poincare`.

### Closed-form point not stated as a literature theorem

None of the sources packages the repository's exact Friedrichs-form convention.  It follows
directly for this class.  On the ambient restriction core
$\mathscr C=\mathbb R+C_c^\infty(\mathbb R^n)|_P$, set
$$
\mathcal E_H(f,f)=\int_P\langle H\nabla f,\nabla f\rangle d\mu.
$$
The core has finite energy because $\mathbb E\operatorname{Tr}H=\operatorname{Tr}\Sigma$.
If $f_k\to0$ in $L^2(\mu)$ and the gradients are Cauchy in the $H$-metric, local smoothness and
positive definiteness make the form uniformly elliptic on each compact subset of
$\operatorname{int}P$.  Distributional differentiation there forces the gradient limit to be
zero; exhaustion of $P$ proves closability.  The same local argument shows that the kernel of
the closed form consists of constants because $P$ is connected.  Its nonnegative self-adjoint
operator is therefore the closed Stein generator used in the dossier.

If the manuscript instead intends a separately specified maximal Neumann domain with a
classical normal trace at every boundary point, that equality is **not** supplied by these
sources.  The certified endpoint only uses the closed ambient-core convention, for which the
weak zero-flux identity and the preceding closability argument suffice.

## The original proposed family versus an adjusted family

### Original full-support family: only a lead for the required regularity

The exploration proposed
$$
d\nu_\varepsilon(x)\propto
q_\varepsilon(x)e^{-\varepsilon|x|^2/2}dx,
\qquad
q_\varepsilon=\frac{d(\mu*\gamma_\varepsilon)}{dx}.
$$
Its potential is smooth and obeys
$$
\varepsilon I\preceq
D^2\left(-\log q_\varepsilon+\frac\varepsilon2|x|^2\right)
\preceq(\varepsilon^{-1}+\varepsilon)I.
$$
The family is centered after translation and does converge to $\mu$ in $W_2$, as the upstream
exploration proves.

However, the published sources checked here do not prove that this **unbounded-target** family
has a smooth entire canonical moment potential with a global diffeomorphism.  Cordero-Erausquin--
Klartag Theorem 2 gives existence of an essentially-continuous convex potential, not the needed
regularity.  Fathi Corollary 2.4 states a bounded positive moment-map Stein kernel for uniformly
log-concave laws, but its short proof invokes the moment-map construction and a Klartag Hessian
estimate without supplying the missing full-support regularity theorem.  The Klartag paper cited
there works under its bounded-support regularity condition (1).  Therefore Corollary 2.4 is a
lead for this exact issue, not a source-verified import of the full CMH regular class.

### Adjusted centered family: add a growing-ball truncation

Let $X\sim\mu$, possibly supported on a proper linear subspace, and let
$Y_\delta=X+\sqrt\delta G$, $G\sim N(0,I_n)$.  For parameters
$\delta,\varepsilon>0$ and $R<\infty$, define
$$
d\widetilde\mu_{\delta,\varepsilon,R}(x)
\propto
\mathbf1_{B(0,R)}(x)
e^{-\varepsilon|x|^2/2}q_\delta(x)dx,
\qquad
\mu_{\delta,\varepsilon,R}
=(x\mapsto x-m_{\delta,\varepsilon,R})_\#
\widetilde\mu_{\delta,\varepsilon,R}.
\tag{A}
$$
For each fixed triple, (A) is centered and full-dimensional, its support is a translated convex
body, and its interior density is the restriction of a positive $C^\infty$ function on all of
$\mathbb R^n$.  Its potential is convex and satisfies
$$
\varepsilon I\preceq D^2V_{\delta,\varepsilon,R}
\preceq(\delta^{-1}+\varepsilon)I
$$
in the support interior.  Thus it meets Berman--Berndtsson Theorem 1.1 exactly.

The family can be chosen to converge in ambient $W_2$ through affine-support degeneration.
Indeed,
$$
W_2(\mathcal L(Y_\delta),\mu)^2\le n\delta.
$$
For fixed $\delta$, first let $R\to\infty$ and $\varepsilon\downarrow0$.  The density ratio in
(A) tends to one, and dominated convergence passes both the weak limit and second moments, so
the uncentered laws converge in $W_2$ to $\mathcal L(Y_\delta)$.  Choose a diagonal
$\varepsilon(\delta)\downarrow0$, $R(\delta)\uparrow\infty$ making this $W_2$ error tend to
zero.  The means then tend to $0$, so centering changes the $W_2$ distance by a vanishing
translation.  Consequently
$$
W_2(\mu_{\delta,\varepsilon(\delta),R(\delta)},\mu)\to0,
\qquad
\operatorname{Cov}(\mu_{\delta,\varepsilon(\delta),R(\delta)})\to\Sigma,
$$
even when $\Sigma$ is singular.  No whitening is performed before this limit.

This is the exact extra truncation used, in slightly different parameterizations, in the two
2026 preprints.  It repairs the source gap of the original family without changing the
constant-preserving closure argument.

## Exact 2026 preprint audit

### Letwin, arXiv:2607.24164v1, 27 July 2026

Classification: `preprint-unreviewed`.

- Lemma A.1 constructs, from an isotropic full-dimensional target, Gaussian-convolution plus
  ball-conditioned regular measures and proves convergence of polynomial moments through degree
  four after affine normalization.
- Lemma 2.2 states the exact regularity consequence for this class: the canonical potential is
  finite and smooth, has positive-definite Hessian, and its gradient is a diffeomorphism
  $\mathbb R^n\to K$ satisfying Monge--Amp\`ere.
- Lemma 2.7, citing Fathi Theorem 2.3, identifies the target-coordinate Hessian as the positive
  symmetric Stein kernel.
- Lemma A.3 gives an explicit noncompact source integration-by-parts statement with its four
  $L^1$ hypotheses.

The appendix does not state ambient $W_2$ convergence through singular covariance, because its
purpose is an isotropic fourth-moment theorem.  Using its whitening step at a singular limit
would be invalid; the unwhitened diagonal argument above is the required adaptation.

### Chen--Klartag, arXiv:2607.23307v1, 25 July 2026

Classification: `preprint-unreviewed`.

The regularity-removal construction is **not in Appendix A**.  It is an unnumbered paragraph in
the proof of Theorem 1.2, at the end of Section 3: the density is proportional to
$$
\mathbf1_{B(0,R)}e^{-\varepsilon|x|^2/2}
\frac{d(\mu*\gamma_\delta)}{dx},
$$
followed by centering and invertible isotropic normalization, and a diagonal choice gives moment
convergence through order four.  Appendix A instead justifies integrations by parts using cutoff
functions.  Lemma A.1 constructs cutoffs and proves membership in the closed source Dirichlet
form for bounded smooth functions of finite energy; Lemmas A.2--A.3 justify the specific
noncompact integrations used in the paper.  Equation (23), in the proof of Theorem 1.4, is the
target Stein identity, and its cutoff error is shown to vanish using boundedness of $K$ and $H$.

These facts support the adjusted family and source integration by parts, but their preprint class
would block an unconditional downstream proof if they were the only dependencies.  They are not
needed as imports here because the regularity and Stein facts are already supplied by the two
published sources above; the $W_2$ diagonal is elementary.

## Proposed imported node

The natural imported statement is deliberately narrower than the full approximation gate:

```yaml
- id: thm:regular-moment-map-compact-target
  kind: theorem
  status: imported
  file: modules/kls/04-family-moment-map.tex
  statement: >-
    If P is a convex body and mu(dx)=g(x)1_int(P)(x)dx is a centered probability with
    g in C-infinity(R^n) positive, then the canonical moment potential phi is
    smooth and strictly convex on R^n, grad(phi):R^n->int(P) is a diffeomorphism, and
    H(x)=D2phi((grad phi)^(-1)(x)) is a smooth positive symmetric Stein kernel satisfying
    Div_mu H=-x and E_mu H=Cov(mu).
  import_class: published
  references:
    - BermanBerndtsson2013RealMA
    - Fathi2019SteinMomentMaps
```

The orchestrator would need to add the matching manuscript anchor before accepting this node.
The $W_2$ closure theorem and the closed-form construction are repository arguments, not imported
claims.

## Proposed bibliography delta

Add the missing published source:

```bibtex
@article{BermanBerndtsson2013RealMA,
  author  = {Berman, Robert J. and Berndtsson, Bo},
  title   = {Real {Monge--Amp\`ere} Equations and {K\"ahler--Ricci} Solitons on Toric Log {Fano} Varieties},
  journal = {Annales de la Facult\'e des Sciences de Toulouse. Math\'ematiques},
  series  = {6},
  volume  = {22},
  number  = {4},
  pages   = {649--711},
  year    = {2013},
  doi     = {10.5802/afst.1386},
  eprint  = {1207.6128},
  archivePrefix = {arXiv},
  primaryClass  = {math.DG}
}
```

Correct the two existing publication-class entries while preserving their keys:

```bibtex
@article{CorderoErausquinKlartag2015MomentMeasures,
  author  = {Cordero-Erausquin, Dario and Klartag, Bo'az},
  title   = {Moment Measures},
  journal = {Journal of Functional Analysis},
  volume  = {268},
  number  = {12},
  pages   = {3834--3866},
  year    = {2015},
  doi     = {10.1016/j.jfa.2015.04.001},
  eprint  = {1304.0630},
  archivePrefix = {arXiv},
  primaryClass  = {math.FA}
}

@incollection{Klartag2013MomentMeasures,
  author    = {Klartag, Bo'az},
  title     = {Logarithmically-Concave Moment Measures {I}},
  booktitle = {Geometric Aspects of Functional Analysis},
  series    = {Lecture Notes in Mathematics},
  volume    = {2116},
  pages     = {231--260},
  publisher = {Springer},
  address   = {Cham},
  year      = {2014},
  doi       = {10.1007/978-3-319-09477-9_16},
  eprint    = {1309.2767},
  archivePrefix = {arXiv},
  primaryClass  = {math.AP}
}
```

`Fathi2019SteinMomentMaps`, `Letwin2026QuadraticKLS`, and
`ChenKlartag2026SharpThinShell` already have the correct publication/preprint classification in
the bibliography.

## Gap after the import

For the intrinsic closed-form convention selected by the upstream probe, there is no remaining
external regularity or boundary gap: use the adjusted family (A), Berman--Berndtsson Theorem 1.1,
Fathi Theorem 2.3, the elementary closability argument above, and the upstream common-core
$W_2$ passage.

The two remaining choices are internal:

1. turn the closure theorem and adjusted approximation into a dossier and have it independently
   reviewed; and
2. state whether the limiting $H^1_\Sigma(\mu)$ means the closed relaxation used by the probe or
   a separately defined maximal distributional space.  Equality with an unnamed maximal space
   is not an imported consequence.

The original untruncated family remains only a lead for full-support moment-potential regularity;
it should be replaced by (A) rather than cited as covered.

## Citation debt

- `modules/kls/04-family-moment-map.tex` says that a preprint appendix addresses approximation.
  This is exact for Letwin Appendix A.  In Chen--Klartag, approximation is an unnumbered paragraph
  in the proof of Theorem 1.2; Appendix A handles cutoff integration by parts.
- Fathi Corollary 2.4 should not be used by itself to certify smooth global moment-map regularity
  for the full-support strongly log-concave family.  Its cited Klartag input is proved in the
  bounded-support regular class.
- The existing Cordero-Erausquin--Klartag and Klartag BibTeX records are formatted as preprints
  despite published versions; exact corrections are proposed above.

## Searched and not found

Queries and source checks included:

- `moment measures smooth strictly convex gradient diffeomorphism strongly log-concave full support`;
- `Cordero-Erausquin Klartag moment measure regularity diffeomorphism`;
- `Klartag logarithmically-concave moment measures uniformly convex unbounded support`;
- `Fathi Stein kernels moment maps Theorem 2.3 Corollary 2.4 regularity`;
- `Berman Berndtsson Real Monge-Ampere smooth gradient diffeomorphism theorem`;
- the full HTML/PDF text of arXiv:1304.0630v1, 1309.2767v1, 1804.04699v3,
  1207.6128v1, 2607.24164v1, and 2607.23307v1.

No published theorem was found that, under only
$aI\preceq D^2V\preceq bI$ on an unbounded target, explicitly provides all of smoothness of the
canonical self-moment potential, global diffeomorphism, Stein zero flux, and the repository's
closed operator domain.  The compact-target adjustment avoids needing such a theorem.

```yaml
outcome: complete
artifacts:
  - research/explorations/2026-08-27-literature-scout-cmh-regular-approximation-harness-01.md
proposed_deltas:
  - add candidate imported node thm:regular-moment-map-compact-target after adding its manuscript anchor
  - add BermanBerndtsson2013RealMA and correct the two published moment-measure bibliography records
next_role: orchestrator
next_prompt: |
  Accept the source-verified compact-target replacement for the unresolved regularity input of
  `q:cmh-approximation`. Add a manuscript anchor and imported node
  `thm:regular-moment-map-compact-target` with `import_class: published` and references
  `BermanBerndtsson2013RealMA` and `Fathi2019SteinMomentMaps`, using the exact statement in this
  exploration. Add the proposed Berman--Berndtsson BibTeX record and correct the existing
  Cordero-Erausquin--Klartag and Klartag records. Then dispatch a prover to write a standalone
  dossier for `q:cmh-approximation`: replace the untruncated approximants by the centered
  Gaussian-convolution/Gaussian-tilt/growing-ball family (A); prove its ambient W2 convergence
  without whitening, including singular covariance; establish closability on the ambient
  smooth restriction core; invoke the imported regularity and Stein theorem; and combine this
  with the constant-preserving common-core passage already written in
  `research/explorations/2026-08-27-kls-route-prober-cmh-approximation-harness-01.md`. Keep the
  limiting Sobolev space explicitly equal to the intrinsic closed covariance-form relaxation.
```
