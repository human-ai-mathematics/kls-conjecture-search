# Literature survey: modified transport for A4 and two-well metastability for A5

Date: 2026-08-27

Role: `literature-scout`

Upstream targets: `q:a4-modified`, `conj:a5-metastable`, `q:a5-metastable`

## Exact statements searched for

Two independent, non-trace-cluster targets were selected after reading the live A-series ledger,
target briefs, manuscript statements, and every applicable `bounded_by` fence.

For A4, the desired statement in repository normalization was:

> For a named heavy-tail law $\pi$, identify an explicit cost $\alpha$, quadratic near zero and
> adapted to the tail at infinity, for which
> $$
> \mathcal T_\alpha(q,\pi)\le C_\alpha\operatorname{KL}(q\|\pi)
> $$
> holds globally or on a specified family/sublevel.  Determine what global statement remains
> possible for polynomial-tail laws.

The relevant fences are `obs:heavy-tail-no-classical` and `obs:restricted-not-finite`.  An
ordinary $T_2$ conclusion would violate the former, while finiteness of $W_2$ on individual KL
sublevels does not by itself supply a finite linear conversion constant.

For A5, the desired fixed-landscape neighbour of the posterior target was:

> For $\mu_n(dx)\propto e^{-nH(x)}dx$ with two nondegenerate equal-depth wells separated by one
> nondegenerate index-one saddle, prove the exact Euclidean Poincar\'e asymptotic, constants
> included, and in particular identify $\lim n^{-1}\log C_P(\mu_n)$.

The relevant fence is `obs:symmetry-vs-physical`.  A raw metastable spectral-gap theorem does not
by itself imply quotient improvement, and the fixed-potential two-well statement is weaker than
the random empirical, collision-controlled, multiple-orbit-network statement in
`conj:a5-metastable`.

## Found: published one-dimensional modified-transport classification

### Gozlan, Theorem 57, with Propositions 16 and 26

Source: Nathael Gozlan, *Characterization of Talagrand's Like Transportation-Cost Inequalities
on the Real Line*, Journal of Functional Analysis 250 (2007), no. 2, 400--425, DOI
[10.1016/j.jfa.2007.05.025](https://doi.org/10.1016/j.jfa.2007.05.025).

Classification: `import_class: published`.

Primary source read: [arXiv:math/0608241v1](https://arxiv.org/abs/math/0608241), submitted
10 August 2006.  I read the definitions, Proposition 16, Proposition 26, Theorem 57, and the
proof of Theorem 57, not only the abstract.  I did not read every proof in the paper.

Let $\mathcal A$ be the paper's class of even, continuous, nondecreasing, superadditive costs
$\alpha:\mathbb R\to\mathbb R_+$ with $\alpha(0)=0$ and
$\alpha(t)=t^2$ for $|t|\le1$.  Write $\operatorname{ST}_\alpha(a)$ for the strong inequality
with scaled cost $\alpha(a(x-y))$:
$$
\mathcal T_{\alpha(a\,\cdot)}(\nu,\beta)
\le \operatorname{KL}(\nu\|\mu)+\operatorname{KL}(\beta\|\mu)
\qquad\text{for all }\nu,\beta\in\mathcal P(\mathbb R).
$$
Theorem 57 states that if $\mu$ is a nonatomic, full-support log-concave probability law on
$\mathbb R$ and $\alpha\in\mathcal A$, then the following are equivalent:
$$
\exists a>0:\ \mu\text{ satisfies }\operatorname{ST}_\alpha(a),
\qquad
\exists b>0:\ \int e^{\alpha(bx)}d\mu(x)<\infty.
\tag{G}
$$
If $\alpha$ is convex, the same equivalence holds for the ordinary one-reference-measure
transport inequality, up to the scaling of the cost recorded in Proposition 16.

### Conversion to the repository normalization

For $1\le p\le2$, define the convex cost
$$
\theta_p(t)=
\begin{cases}
t^2,&|t|\le1,\\[2mm]
\dfrac{2}{p}|t|^p+1-\dfrac{2}{p},&|t|\ge1.
\end{cases}
$$
For
$$
\pi_p(dx)=Z_p^{-1}e^{-|x|^p}dx,
$$
the moment condition in (G) holds with $\alpha=\theta_p$ for every sufficiently small $b>0$,
because
$$
-|x|^p+\theta_p(bx)
=-\left(1-\frac{2b^p}{p}\right)|x|^p+O(1)
$$
in the tail.  Therefore there is $a_p>0$ such that
$$
\mathcal T_{\theta_p(a_p\,\cdot)}(q,\pi_p)
\le \operatorname{KL}(q\|\pi_p)
\qquad\text{for every }q\in\mathcal P(\mathbb R).
\tag{A4-MT}
$$
This is exactly the repository form with the cost
$\alpha_p(r)=\theta_p(a_pr)$ and $C_{\alpha_p}=1$.  Equivalently, elementary comparison of
the two scaled regimes gives a finite, non-explicit $C_p$ with
$$
\mathcal T_{\theta_p}(q,\pi_p)\le C_p\operatorname{KL}(q\|\pi_p).
$$
Thus the source realizes the A4 prediction: quadratic cost near zero and $p$-power cost at
infinity, reducing to linear tail growth at $p=1$ and ordinary quadratic transport at $p=2$.

The same source also sharpens the polynomial-tail obstruction.  Proposition 16 converts an
ordinary TCI with convex cost into a scaled strong TCI.  Proposition 26 then forces exponential
integrability of the distance-to-a-positive-mass-set cost.  Since every nonzero even convex cost
is unbounded and grows at least linearly at infinity, a polynomial-tail law such as Student-$t$
or the horseshoe cannot satisfy a global TCI with any nontrivial unbounded convex cost.  Any
positive A4 theorem for those priors must instead be weighted, weak, family-restricted, or
KL-sublevel-specific.  This is compatible with, and sharper than, the existing classical
$T_2$ fence.

### What the result does not give

- The constants $a_p$ and $C_p$ are existential, not explicit or optimal.
- The theorem is one-dimensional; strong TCIs tensorize for products, but a dependent posterior
  needs a separate coupling contract.
- It does not cover likelihood tilts, hierarchical posteriors, or a specified variational family.
- It gives no positive global convex-cost theorem for Student-$t$ or horseshoe tails; it explains
  why such a theorem is impossible.
- It does not compute a localized restricted coefficient $C_{\mathcal Q,r}$.

## Found: published fixed-potential Eyring--Kramers Poincar\'e law

### Menz--Schlichting, Corollaries 2.15 and 2.18

Source: Georg Menz and Andr\'e Schlichting, *Poincar\'e and Logarithmic Sobolev Inequalities by
Decomposition of the Energy Landscape*, Annals of Probability 42 (2014), no. 5, 1809--1884,
DOI [10.1214/14-AOP908](https://doi.org/10.1214/14-AOP908).

Classification: `import_class: published`.

Primary source read: [arXiv:1202.1510v4](https://arxiv.org/abs/1202.1510), revised 8 September
2014 and identified by arXiv as the published version.  I read Assumptions 1.4 and 1.7,
Corollaries 2.15 and 2.18, and the proof deriving the corollaries from the local and
mean-difference inputs.  I did not reread in full the long proofs of Theorems 2.9 and 2.12.

Let
$$
\mu_\varepsilon(dx)=Z_\varepsilon^{-1}e^{-H(x)/\varepsilon}dx.
$$
Assume $H\in C^3(\mathbb R^d)$ is a nonnegative Morse function satisfying the paper's Poincar\'e
growth hypotheses
$$
\liminf_{|x|\to\infty}|\nabla H(x)|>0,
\qquad
\liminf_{|x|\to\infty}
\bigl(|\nabla H(x)|^2-\Delta H(x)\bigr)>-\infty.
\tag{MS-growth}
$$
Specialize to exactly two equal-depth nondegenerate minima $m_1,m_2$ and a unique communicating
nondegenerate index-one saddle $s$.  Set
$$
\kappa_i=\sqrt{\det\nabla^2H(m_i)},
$$
and let $\lambda_-(s)<0$ be the negative eigenvalue of $\nabla^2H(s)$.

### Conversion to the repository normalization

The paper writes $\operatorname{PI}(\varrho)$ as
$$
\operatorname{Var}_{\mu_\varepsilon}(f)
\le \frac1\varrho\int|\nabla f|^2d\mu_\varepsilon.
$$
Therefore the repository's Euclidean constant is exactly $C_P=1/\varrho$; no additional
$\varepsilon$ factor is introduced in the conversion.  Corollary 2.18 gives
$$
C_P(\mu_\varepsilon)
=
\left(1+O\!\left(\sqrt\varepsilon|\log\varepsilon|^{3/2}\right)\right)
\frac{2\pi\varepsilon}{\kappa_1+\kappa_2}
\frac{\sqrt{|\det\nabla^2H(s)|}}{|\lambda_-(s)|}
\exp\!\left(\frac{H(s)-H(m_2)}{\varepsilon}\right).
\tag{A5-EK}
$$
The displayed error is the paper's multiplicative `approximately equal` convention.  Setting
$\varepsilon=1/n$ gives
$$
\frac1n\log C_P\!\left(Z_n^{-1}e^{-nH}dx\right)
\longrightarrow H(s)-H(m_2).
$$
For a two-well orbit this is the repository communication height.

### Fence check and exact limitation

The result respects `obs:symmetry-vs-physical`: it computes the raw metastable barrier and makes
no automatic quotient claim.  It supplies a deterministic two-well anchor for A5 but does not
prove `conj:a5-metastable`:

- $H$ is fixed, whereas the posterior potential is random and $n$-dependent;
- the general theorem assumes unique communicating saddles and a strictly dominant barrier,
  while a symmetric $K!$ orbit generally has repeated saddles and barriers;
- it supplies no uniform empirical derivative, saddle, or capacity comparison;
- it supplies no collision-stratum control;
- it supplies no quotient/orbifold Bernstein--von Mises theorem;
- beyond the two-well or generic unique-dominant-barrier case, it does not establish the full
  finite-network $\Gamma_{\mathrm{conn}}$ statement used by the repository.

## Related published result checked but not proposed as an import

Bolley--Villani, Corollary 2.3, in Fran\c{c}ois Bolley and C\'edric Villani,
*Weighted Csisz\'ar--Kullback--Pinsker Inequalities and Applications to Transportation
Inequalities*, Annales de la Facult\'e des Sciences de Toulouse 14 (2005), no. 3, 331--352,
DOI [10.5802/afst.1095](https://doi.org/10.5802/afst.1095), was read in the
[published source](https://www.numdam.org/item/AFST_2005_6_14_3_331_0.pdf).
It is `import_class: published`, and the existing bibliography key is `BolleyVillani2005`.

If $\mu$ has a square-exponential moment, their result gives
$$
W_2(\nu,\mu)
\le C\left[
\operatorname{KL}(\nu\|\mu)^{1/2}
+\left(\frac{\operatorname{KL}(\nu\|\mu)}2\right)^{1/4}
\right].
\tag{BV}
$$
I read Theorem 2.1, Corollary 2.3, and the corollary's proof, not only the abstract.  Formula
(BV) gives finite $W_2$ and a nonlinear KL modulus, but it does not prove a finite localized
linear coefficient $C_{\mathcal Q,r}$: squaring and dividing by KL leaves a bound deteriorating
like $\operatorname{KL}^{-1/2}$ near zero.  It therefore distinguishes a finite-radius mechanism
from the stronger linear certificate sought in `q:a4-certificate`.

## Proposed imported nodes

The first node should be anchored by a new manuscript theorem, suggested label
`thm:a4-modified-transport-1d`:

```yaml
- id: thm:a4-modified-transport-1d
  kind: theorem
  status: imported
  import_class: published
  file: modules/open-targets/A4-variational-inference.tex
  statement: "For a nonatomic full-support log-concave law mu on R and a convex admissible cost alpha that is quadratic near zero, a scaled global transport-entropy inequality T_{alpha(a·)}(nu,mu) <= KL(nu||mu) holds for some a>0 iff int exp(alpha(bx)) dmu(x)<infinity for some b>0. Consequently pi_p proportional to exp(-|x|^p), 1<=p<=2, admits the cost theta_p(t)=t^2 for |t|<=1 and theta_p(t)=(2/p)|t|^p+1-2/p for |t|>=1; polynomial-tail laws admit no nontrivial global unbounded convex-cost TCI."
  references: [Gozlan2007RealLine]
  bounded_by: [obs:heavy-tail-no-classical, obs:restricted-not-finite]
```

The second node should be anchored by a new manuscript theorem, suggested label
`thm:a5-two-well-eyring-kramers`:

```yaml
- id: thm:a5-two-well-eyring-kramers
  kind: theorem
  status: imported
  import_class: published
  file: modules/open-targets/A5-quotient-and-reparameterization.tex
  statement: "For mu_epsilon proportional to exp(-H/epsilon) with H a coercive C3 Morse potential having exactly two equal-depth nondegenerate minima m1,m2 and a unique nondegenerate index-one saddle s, C_P(mu_epsilon)=(1+O(sqrt(epsilon)|log epsilon|^(3/2))) [2 pi epsilon/(kappa1+kappa2)] [sqrt(|det Hess H(s)|)/|lambda_-(s)|] exp((H(s)-H(m2))/epsilon), where kappa_i=sqrt(det Hess H(m_i)). Hence for epsilon=1/n, n^{-1} log C_P converges to the communication height."
  references: [MenzSchlichting2014]
  bounded_by: [obs:symmetry-vs-physical]
```

The key `MenzSchlichting2014` already exists in `fi_references.bib`; no bibliography append is
needed for the A5 node.

## Proposed BibTeX append

The exact append-only proposal for the new A4 key is:

```bibtex
@article{Gozlan2007RealLine,
  author        = {Gozlan, Nathael},
  title         = {Characterization of {Talagrand}'s Like Transportation-Cost Inequalities on the Real Line},
  journal       = {Journal of Functional Analysis},
  volume        = {250},
  number        = {2},
  pages         = {400--425},
  year          = {2007},
  doi           = {10.1016/j.jfa.2007.05.025},
  eprint        = {math/0608241},
  archivePrefix = {arXiv},
  primaryClass  = {math.PR},
  url           = {https://arxiv.org/abs/math/0608241}
}
```

## Gap after the imports

For A4, the remaining statement is:

> For each named robust-Bayes posterior and variational family, determine an explicit strongest
> weighted, weak, restricted, or sublevel cost and a computable constant.  In particular, handle
> likelihood-tilted generalized-normal laws and replace global convex transport by an admissible
> non-global notion for Student-$t$ and horseshoe tails.

For A5, the remaining statement is:

> Prove, uniformly with high probability for the random empirical posterior landscape, that the
> full repeated-symmetry orbit network has raw exponent $\Gamma_{\mathrm{conn}}$, including
> collision separation, tail coercivity, and two-sided capacities with subexponential errors;
> independently prove the quotient Fisher-scale Poincar\'e limit on the stratified orbit space.

Neither imported theorem discharges these statements.

## Citation debt

- The A4 manuscript currently cites `GozlanLeonard2007` for the modified-transport toolbox, but
  the exact one-dimensional log-concave iff theorem above is in the single-author Gozlan JFA
  paper.  `GozlanLeonard2007` is adjacent theory, not the theorem-specific source.
- The A5 manuscript says Menz--Schlichting “predict” the raw rate.  That wording is honest.  The
  source must not be upgraded to a proof of the random posterior, repeated $K!$-orbit network,
  collision, or quotient lines.
- `BolleyVillani2005` supports a nonlinear $W_2$--KL modulus, not a finite linear
  $C_{\mathcal Q,r}$ under tail moments alone.

## Searched and not found

Queries used included:

- `Bolley Villani 2005 weighted Csiszar Kullback Pinsker theorem exponential moment Wp relative entropy pdf`
- `Menz Schlichting 2014 Poincare logarithmic Sobolev decomposition energy landscape theorem spectral gap Eyring Kramers pdf`
- `modified transport entropy inequality heavy tailed measures cost theorem`
- `Characterization of Talagrand's like transportation-cost inequalities on the real line pdf Gozlan`
- `transportation entropy inequality Student t distribution modified cost polynomial tails`
- `Eyring Kramers random empirical potential posterior permutation symmetry quotient spectral gap`
- `posterior label switching spectral gap Eyring Kramers permutation quotient Bernstein von Mises`

No primary source was found that directly supplies either the A5 random-posterior-plus-quotient
theorem or a global convex modified-transport inequality for polynomial-tail Student/horseshoe
laws.  The search found Berglund--Dutercq's symmetry-aware Eyring--Kramers law for finite-state
jump processes, but that is a lead for a possible orbit-network reduction, not an import for the
continuous posterior diffusion.

```yaml
outcome: complete
artifacts:
  - research/explorations/2026-08-27-literature-scout-a4-a5-imports-lit-01.md
proposed_deltas:
  - "Add imported node thm:a4-modified-transport-1d exactly as specified above, with new reference Gozlan2007RealLine."
  - "Append the Gozlan2007RealLine BibTeX entry exactly as specified above."
  - "Add imported node thm:a5-two-well-eyring-kramers exactly as specified above, using existing reference MenzSchlichting2014."
next_role: orchestrator
next_prompt: |
  Add manuscript anchors and atomically consider the two imported ledger nodes:
  (1) thm:a4-modified-transport-1d, import_class published, references
  [Gozlan2007RealLine], with the exact one-dimensional log-concave
  moment/modified-transport equivalence, generalized-normal theta_p corollary,
  and polynomial-tail global-convex-cost obstruction stated above;
  (2) thm:a5-two-well-eyring-kramers, import_class published, references
  [MenzSchlichting2014], restricted to the fixed C3 Morse two-equal-well,
  unique-saddle setting and with the exact repository-normalized prefactor
  stated above. Do not use (2) to discharge the random empirical landscape,
  repeated K!-orbit barrier network, collision-stratum, or quotient-BvM parts
  of conj:a5-metastable. Append the exact Gozlan2007RealLine BibTeX entry,
  resolve the manuscript labels, apply ledger/manuscript/bibliography changes
  atomically, and run python3 research/check_ledger.py.
```
