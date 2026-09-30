---
verdict: pass
authors:
  - /root/prove_cmh_recovery
reviewer: /root/review_cmh_recovery_w0
fingerprints:
  solutions/lem-affine-poincare-w2-liminf.md: 5afb3e3e3dc73100386f977a871b50a4595288d0ab1ab55a27ba2abcabf1557b
  lem:affine-poincare-w2-liminf: 9b3e2cf72b9adab7eb84ee54baff7e3ebe92d5341b02734938f2285f5a45cc3e
  thm:regular-moment-map-compact-target: 6c5fc0b83ba7ee921113bb0cac813d6c92fd41e9b1a9dda5247df865f76eb813
  cor:cmh-recovery-sequence-suffices: f9b55a151c8c485807235a4f7498fe1932a00d6544b4657d670989ae2c35845b
  def:cmh: 5093f7f871d8362c179b6ca901822ba370d6a14237ed9bb3fe076ab964ff9722
  thm:cmh-implies-affine-poincare: 434bde8b4ccac59502b5c71180a4f20df98e1abc02f85826578bba9321480559
  ass:cmh-recovery-envelope: 97413c87f6cb04227066c5ba42930acffd8f0f977af2603e5529125ff4c2bcc4
---

# Affine-Poincaré $W_2$ lower semicontinuity and one-sequence CMH recovery

This is a cold review of `solutions/lem-affine-poincare-w2-liminf.tex`, whose reviewed
pre-certification SHA-256 is
`929482e5360db8782d1defd95a27547cc54fcaca957e529dadde8a34e56f4e22`. The proof was
reconstructed from the dossier, the manuscript and ledger statements, the certified dependency
dossier and review, and the actual published sources. The prover's exploration narrative was not
used as evidence. The author and reviewer identities are distinct, and the exploration record
names only `/root/prove_cmh_recovery` as the prover.

## Findings

### Statement agreement and exact logical status

The current ledger and manuscript statements agree. Lemma
`lem:affine-poincare-w2-liminf` asks for centered, full-dimensional, compactly supported regular
moment-map approximants $\mu_k$ of every centered log-concave $\mu$, with convergence in the
original ambient $W_2$ metric and

$$
 C_{\mathrm P}^{\mathrm{aff}}(\mu)
 \le \liminf_k C_{\mathrm P}^{\mathrm{aff}}(\mu_k),
$$

including degeneration to a proper affine support and without asserting continuity of
$C_{\mathrm{CMH}}$. Part (i) of the dossier theorem is exactly this statement. Part (ii) proves
the strictly stronger fact that the same lower-semicontinuity inequality holds for every centered
log-concave sequence $\nu_k\to\mu$ in ambient $W_2$.

Corollary `cor:cmh-recovery-sequence-suffices` agrees across all three planes: under
`ass:cmh-recovery-envelope`, one regular recovery sequence satisfying
$\liminf_k C_{\mathrm{CMH}}(\mu_k)\le C$ implies
$C_{\mathrm P}^{\mathrm{aff}}(\mu)\le C$ for every centered log-concave law, with the same
constant through affine-support collapse, and hence implies KLS. The dossier does not replace the
existential recovery-envelope assumption by a bound over all regularizations.

The lemma has only a published imported premise and may become `proved`. The corollary has a
complete certified implication, but `ass:cmh-recovery-envelope` remains `open`; repository
constraint 7 therefore requires the corollary to remain `conditional`.

### The covariance form and its common ambient core

For a centered log-concave $\mu$, the dossier correctly identifies its affine hull with
$S=\operatorname{Ran}\Sigma$. The covariance is positive definite on $S$ when
$d=\dim S>0$. On the relative interior of the convex support, the intrinsic log-concave density
is positive and locally bounded above and below. This makes the local distributional-gradient
argument valid: convergence to zero in $L^2(\mu)$ together with convergence of
$\Sigma_S^{1/2}\nabla_S f_j$ forces the limiting gradient field to vanish. Thus the covariance
pre-form is closable, and the kernel of its closure consists exactly of constants because the
relative interior is connected.

The claimed form core is proved rather than assumed. Value truncation converges in value and
energy; growing spatial cutoffs have a vanishing tail-gradient term and an $O(R^{-2})$ cutoff
term; and intrinsic mollification converges in the form norm by absolute continuity and dominated
convergence. Hence $\mathbb R+C_c^\infty(S)$ is a core.

This intrinsic core is exactly the restriction of the fixed ambient class
$\mathbb R+C_c^\infty(\mathbb R^n)$. The extension
$F(s+t)=\phi(s)\eta(t)$ is compactly supported and smooth, and two extensions agreeing on $S$
have gradient difference in $S^\perp$. Both

$$
 \Sigma=P_S\Sigma_SP_S,
 \qquad
 \Sigma^+=P_S\Sigma_S^{-1}P_S
$$

annihilate that normal difference. The covariance energy is therefore intrinsic and independent
of extension. At rank zero, centeredness gives $\mu=\delta_0$ and the stated convention
$C_{\mathrm P}^{\mathrm{aff}}(\mu)=0$ is coherent.

### Gaussian smoothing, tilt, truncation, and recentering

For $X\sim\mu$ and an independent standard Gaussian $G$, the displayed coupling with
$X+\sqrt\delta G$ proves

$$
 W_2^2(\lambda_\delta,\mu)\le n\delta,
 \qquad
 \mathbb E\lambda_\delta=0,
 \qquad
 \operatorname{Cov}(\lambda_\delta)=\Sigma+\delta I.
$$

The Gaussian convolution has a positive smooth log-concave density. For fixed $\delta$, the
Gaussian-tilted, ball-truncated density relative to $\lambda_\delta$ converges pointwise to one
as $\varepsilon\downarrow0$ and $R\uparrow\infty$; its normalizer tends to one and the density
ratio is eventually bounded by two. Dominated convergence applies both to bounded continuous
tests and to $|x|^2$, so the weak-plus-second-moment characterization gives the asserted fixed-
$\delta$ $W_2$ convergence.

With $\delta_k=k^{-4}$, the simultaneous choice of $\varepsilon_k,R_k$ and the comparison-of-
means inequality give $|m_k|<k^{-1}$. Translation and the triangle inequality then give the
checked ambient estimate

$$
 W_2(\mu_k,\mu)<\frac{2}{k}+\frac{\sqrt n}{k^2}.
$$

The recentered support is the ball with center $-m_k$ and radius $R_k$. Its density is the
restriction of a positive smooth ambient function, is log-concave, and is full-dimensional and
centered. The origin lies in its interior (also directly from $|m_k|<k^{-1}<R_k$). Thus the
compact-target barycenter and regularity hypotheses are all met. Whether $B(0,R)$ denotes the
open ball or its closure is measure-theoretically immaterial; the convex body used by the
published theorem is its closure.

### Published compact-target theorem and Stein normalization

All non-elementary external inputs used by the dossier are published; no unreviewed preprint
enters the dependency closure.

- Brascamp--Lieb, *Journal of Functional Analysis* 22 (1976),
  [DOI 10.1016/0022-1236(76)90004-5](https://doi.org/10.1016/0022-1236(76)90004-5), proves the
  Prékopa marginal theorem used to preserve log-concavity under Gaussian convolution.
- Berman--Berndtsson, Theorem 1.1, *Annales de la Faculté des Sciences de Toulouse* 22
  (2013), [DOI 10.5802/afst.1386](https://doi.org/10.5802/afst.1386), gives a smooth convex
  solution and a global gradient diffeomorphism $\mathbb R^n\to\operatorname{int}P$ for a
  positive smooth target density exactly under its zero-barycenter condition. A smooth convex
  potential whose gradient is a diffeomorphism has positive-definite Hessian and is strictly
  convex.
- Fathi, Theorem 2.3, *Annals of Probability* 47 (2019),
  [DOI 10.1214/18-AOP1305](https://doi.org/10.1214/18-AOP1305), identifies
  $D^2\varphi((\nabla\varphi)^{-1})$ as a positive symmetric Stein kernel when the moment
  potential is $C^2$ on all of $\mathbb R^n$. The source explicitly covers a compact convex
  target whose density is bounded above and below; the dossier's positive smooth ambient density
  has those bounds on the compact target.
- The affine-hull density fact is the classical published Borell characterization of
  log-concave measures (C. Borell, *Periodica Mathematica Hungarica* 6 (1975),
  [DOI 10.1007/BF02018814](https://doi.org/10.1007/BF02018814)). The $W_2$/moment
  characterization is Theorem 6.9 in the published monograph `Villani2008`.

Fathi's global ambient test identity is exactly
$\operatorname{Div}_{\mu_k}H_k=-x$ with no boundary distribution, hence it supplies the weak
zero-normal-flux convention. Testing with an ambient cutoff equal to the coordinate function on
a neighborhood of the bounded target gives

$$
 \mathbb E_{\mu_k}H_k
 =\mathbb E_{\mu_k}[X\otimes X]
 =\operatorname{Cov}(\mu_k).
$$

The construction therefore satisfies every hypothesis of the published imported node
`thm:regular-moment-map-compact-target`.

### Lower semicontinuity along every centered log-concave $W_2$ sequence

For an arbitrary centered log-concave $\nu_k\to\mu$ in $W_2$, quadratic Wasserstein convergence
gives convergence of every covariance entry and hence $\Sigma_k^\nu\to\Sigma$ in operator norm.
For one fixed ambient-core test $F$, bounded continuity gives variance convergence, while

$$
 \left|\int\!\langle\Sigma_k^\nu\nabla F,\nabla F\rangle\,d\nu_k
       -\int\!\langle\Sigma\nabla F,\nabla F\rangle\,d\mu\right|
$$

is bounded by the operator-norm covariance error times $\|\nabla F\|_\infty^2$ plus weak
convergence of the bounded continuous integrand
$\langle\Sigma\nabla F,\nabla F\rangle$. Thus both sides of the affine Poincaré inequality
converge on the same ambient core.

If $L=\liminf_k C_{\mathrm P}^{\mathrm{aff}}(\nu_k)<\infty$, the proof selects one subsequence
on which the constants converge to $L$ before choosing any test function. Along that fixed
subsequence, the inequality passes to the limit for every ambient-core test. Intrinsic core
density then extends it to the whole closed covariance-form domain. This proves

$$
 C_{\mathrm P}^{\mathrm{aff}}(\mu)
 \le \liminf_k C_{\mathrm P}^{\mathrm{aff}}(\nu_k).
$$

The case $L=\infty$ is immediate, and the rank-zero limit was handled separately. No inverse is
taken in a collapsing direction, and no whitening precedes the limit. The order of quantifiers,
the fixed subsequence, covariance convergence, and the singular-support convention are all
correct.

### Closed Stein form and the regular CMH endpoint

For each regular compact-target law, the ambient-restriction class
$\mathscr D=\{F|_P:F\in\mathbb R+C_c^\infty(\mathbb R^n)\}$ is dense in $L^2(\nu)$. The exact
normalization $\mathbb E_\nu H=\Sigma_\nu$ makes every core energy finite.

If $f_j\to0$ in $L^2(\nu)$ and $H^{1/2}\nabla f_j\to u$, then on each compact subset of
$\operatorname{int}P$ the density is equivalent to Lebesgue measure and $H^{\pm1/2}$ are bounded.
Therefore $f_j\to0$ and $\nabla f_j\to H^{-1/2}u$ locally in ordinary $L^2$; closedness of
distributional differentiation forces $u=0$. The same argument for a zero-energy element of the
closure gives zero distributional gradient on the connected target interior, so the closed-form
kernel is exactly the constants.

The global weak Stein identity identifies the nonnegative self-adjoint Friedrichs operator of
this form with the closed Stein generator used in `def:cmh`; no maximal-domain convention or
boundary distribution is inserted. The already proved and independently agent-certified
dependency `thm:cmh-implies-affine-poincare` is therefore applicable and gives, for every member
of a regular recovery sequence,

$$
 C_{\mathrm P}^{\mathrm{aff}}(\nu)\le C_{\mathrm{CMH}}(\nu).
$$

Combining this pointwise comparison with the stronger lower-semicontinuity theorem and the one
sequence supplied by `ass:cmh-recovery-envelope` gives the valid extended-real liminf chain

$$
 C_{\mathrm P}^{\mathrm{aff}}(\mu)
 \le\liminf_k C_{\mathrm P}^{\mathrm{aff}}(\mu_k)
 \le\liminf_k C_{\mathrm{CMH}}(\mu_k)
 \le C.
$$

### Hypothesis accounting and dependency closure

The lemma uses centeredness, log-concavity, finite-dimensionality, and the published imported
compact-target theorem. For the stronger sequential statement, centeredness of every $\nu_k$
is used in turning second-moment convergence into covariance convergence, while log-concavity is
used for each intrinsic affine-support form and common-core identification. The corollary also
uses the defined node `def:cmh`, the proved and agent-certified regular endpoint
`thm:cmh-implies-affine-poincare`, and the unresolved assumption
`ass:cmh-recovery-envelope`.

No used hypothesis is unstated and no theorem hypothesis is unused. The Gaussian tilt is a
permissible strengthening of the constructed target density rather than an extra premise; the
observation that log-concavity is closed under $W_2$ limits is true but not needed once the limit
$\mu$ is assumed log-concave.

The lemma's dependency closure contains only the published imported node
`thm:regular-moment-map-compact-target`. The corollary's closure contains that published input,
the defined CMH constant, the proved regular endpoint, and exactly one blocking open premise,
`ass:cmh-recovery-envelope`. There is no numerical premise or preprint-unreviewed dependency.

### Fences

Neither reviewed node has a `bounded_by` edge. The proof invokes no localization occupation
estimate, no fixed-cut or evolving-competitor assertion, no projection-ceiling estimate, and no
operator-to-trace upgrade. The ball truncation is only a measure approximation and the spatial
cutoff is only a form-core density argument; neither is a fixed-cut localization claim. The
orthogonal projection $P_S$ records intrinsic versus normal directions and is not a
projection-only KLS estimate. Canonical moment-map kernels are used only on the full-dimensional
approximants and are never transported through a noninvertible map.

### Mechanical validation

From `solutions/`,

```text
latexmk -pdf -outdir=../build lem-affine-poincare-w2-liminf.tex
```

completed successfully and produced a five-page PDF. There is no TeX error. The unresolved
cross-manuscript references are the expected standalone behavior allowed by `solutions/README.md`;
all three citations resolve. Before this report was added, `python3 research/check_ledger.py`
reported 2 ledgers, 184 nodes, 651 labels, and 0 errors.

## Corrections

None. The open-ball/closed-convex-body notation is immaterial to the measure and has been checked
against the source theorem; it does not require a proof repair.

## Exclusions

This review does not discharge `ass:cmh-recovery-envelope`, prove any universal bound on
$C_{\mathrm{CMH}}$, or prove lower semicontinuity or continuity of $C_{\mathrm{CMH}}$. It does
not transport a canonical moment-map kernel through a noninvertible map, identify the declared
closed forms with unnamed maximal Sobolev or Neumann domains, recertify the upstream CMH
normalization dossier beyond checking its active certification and applicability, or certify any
localization, fixed-cut, projection, trace-upgrade, or numerical claim. KLS is obtained only
conditionally on the explicitly unresolved recovery-envelope assumption.

Updating the dossier provenance header, the shared ledger, or the manuscript is outside this
reviewer's write surface.
