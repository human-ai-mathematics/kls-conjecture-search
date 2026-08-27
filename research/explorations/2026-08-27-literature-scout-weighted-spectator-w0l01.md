# Literature scout: weighted-spectator inputs

Date: 2026-08-27

Role: literature-scout

Run id: `w0l01`

Scope: source verification for the proposed exponential-spectator obstruction to `q:weighted`.
This record imports no refutation and changes no mathematical status.

## Exact statements sought

The proposed obstruction needs two external statements in the repository's normalization.

1. For the product of $N$ centered one-sided exponentials under the repository's simplified
   stochastic localization, a fixed-time event of probability bounded below on which
   $\lVert A_t\rVert_{\mathrm{op}}\gtrsim t^{-1}$, down to $t\asymp1/\log N$.  The event-level
   statement is needed: an expectation bound alone does not justify multiplying by the excess.
2. For every one-dimensional log-concave posterior density $f$ of variance $v>0$, the upper
   bound
   $$
   f(q_p)\leq\lVert f\rVert_\infty\leq C v^{-1/2}
   $$
   at every $p$-quantile $q_p$.  The direction is critical: a high-variance spectator must
   provide a low-perimeter competing half-line for the posterior profile.

The stronger neighbours searched for were a pathwise spike persisting on a time interval, and a
source proving that a cylinder over a near-minimizing base cut remains near-Cheeger after adding
arbitrarily many exponential spectators.

## Found

### Klartag--Lehec exponential covariance spike

**Citation and class.** Bo'az Klartag and Joseph Lehec, *Isoperimetric inequalities in
high-dimensional convex sets*, *Bulletin of the American Mathematical Society* **62** (2025),
no. 4, 575--642, DOI `10.1090/bull/1869`.  `import_class: published`.

I read the full proof of Proposition 65 and its preliminary Lemma 66 in
[arXiv:2406.01324v2](https://arxiv.org/html/2406.01324v2), last revised 29 November 2024.  The
publisher metadata establishes the subsequent peer-reviewed publication.  The accessible v2
source numbers the result Proposition 65; I did not obtain the publisher-typeset PDF to verify
whether that numbering was retained there.

Let $Y_i=1+X_i$ be independent exponential random variables of rate one and let $G_i$ be
independent standard Gaussians.  For Gaussian-channel noise variance $s$, the source proves
$$
 \operatorname{Var}(X_i\mid X_i+\sqrt{s}G_i)
 =s\,v\!\left(\sqrt{s}-\frac{Y_i}{\sqrt{s}}-G_i\right),
 \qquad
 v(u)=\operatorname{Var}(G\mid G\geq u).
$$
On the event
$$
 \{Y_i\geq s,\ G_i\geq0\},
 \qquad
 \mathbb P(Y_i\geq s,G_i\geq0)=\frac12e^{-s},
$$
the argument of $v$ is nonpositive.  Hence, for the universal constant
$$
 c_{\mathrm{sp}}:=\inf_{u\leq0}\operatorname{Var}(G\mid G\geq u)>0,
$$
the conditional variance is at least $c_{\mathrm{sp}}s$.  Independence across coordinates gives
the exact event estimate
$$
 \mathbb P\!\left(
  \left\lVert\operatorname{Cov}(X\mid X+\sqrt{s}G)\right\rVert_{\mathrm{op}}
  \geq c_{\mathrm{sp}}s
 \right)
 \geq1-\left(1-\frac12e^{-s}\right)^N. \tag{1}
$$
Consequently, when $s\leq\log N$,
$$
 \mathbb P\!\left(
  \left\lVert\operatorname{Cov}(X\mid X+\sqrt{s}G)\right\rVert_{\mathrm{op}}
  \geq c_{\mathrm{sp}}s
 \right)
 \geq1-e^{-1/2}. \tag{2}
$$
The source states the threshold with an unspecified universal $c$ rather than a numerical
constant.  Its displayed line after (1) prints only a constant lower bound on the expectation;
this is a typographical loss of the factor $s$.  The event at threshold $c_{\mathrm{sp}}s$ and
the proposition's own statement imply
$$
 \mathbb E\left\lVert\operatorname{Cov}(X\mid X+\sqrt{s}G)\right\rVert_{\mathrm{op}}
 \geq c_{\mathrm{sp}}(1-e^{-1/2})s.
$$

#### Exact conversion to repository time

For an observed value $z$ in the Gaussian channel,
$$
 \mathcal L(X\mid X+\sqrt{s}G=z)(dx)
 \propto
 \exp\!\left(\frac zs\cdot x-\frac{|x|^2}{2s}\right)\mu(dx).
$$
The repository writes
$$
 \mu_t(dx)\propto
 \exp\!\left(c_t\cdot x-\frac t2|x|^2\right)\mu(dx)
$$
and uses the planted realization $c_t=tX+B_t$, with $B_t\sim N(0,tI)$.  Therefore the exact
identification is
$$
 t=\frac1s,
 \qquad
 c_t=\frac zs=tX+\sqrt t\,G.
$$
There is no factor-two or square-root discrepancy.  Equations (1)--(2) become
$$
 \mathbb P\!\left(\lVert A_t\rVert_{\mathrm{op}}\geq\frac{c_{\mathrm{sp}}}{t}\right)
 \geq1-\left(1-\frac12e^{-1/t}\right)^N, \tag{3}
$$
and, for $t\geq1/\log N$,
$$
 \mathbb P\!\left(\lVert A_t\rVert_{\mathrm{op}}\geq\frac{c_{\mathrm{sp}}}{t}\right)
 \geq1-e^{-1/2}. \tag{4}
$$
Thus, to use every deterministic $t\in[T/2,T]$, it suffices to take
$\log N\geq2/T$.

This result does **not** give one event on which the spike persists throughout $[T/2,T]$.
It is a fixed-time estimate.  Fixed-time estimates can still be integrated by Tonelli if the
rest of the proposed lower bound is proved at each deterministic time; no pathwise persistence
may be quoted from Proposition 65.

### Sharp one-dimensional density--variance bound

**Citation and class.** Sergey G. Bobkov and Gennadiy P. Chistyakov, *On concentration functions
of random variables*, *Journal of Theoretical Probability* **28** (2015), no. 3, 976--988,
DOI `10.1007/s10959-013-0504-1`.  `import_class: published`.

I read Proposition 2.1 and its proof in the authors' 2 June 2013 revision corresponding to the
published article.  If a real random variable has log-concave density $f$, variance $v$, and
$M=\operatorname*{ess\,sup}f$, the exact sharp statement is
$$
 \frac1{12}\leq vM^2\leq1. \tag{5}
$$
The upper equality is attained by a one-sided exponential density.  In particular,
$$
 f(q_p)\leq M\leq\frac1{\sqrt v} \tag{6}
$$
for every $p\in(0,1)$ and every quantile where the density is evaluated.  Balancedness is not
needed for this upper bound.

The proof normalizes $M=1$, writes
$I(u)=f(F^{-1}(u))$, uses the concavity of $I$, and compares it to the triangular profile with
the same maximum.  Integrating the inverse-quantile representation of the variance gives
$v\leq1$.  Thus (6) has the **upper** direction required by the spectator proposal.  On the
event that a spectator posterior coordinate has variance $v\geq c_{\mathrm{sp}}/t$, a half-line
in that coordinate of any prescribed mass $p$ has perimeter at most
$$
 \frac1{\sqrt v}\leq\sqrt{\frac{t}{c_{\mathrm{sp}}}}. \tag{7}
$$

The Klartag--Lehec notes also use the weaker comparison
$\lVert f\rVert_\infty^2\operatorname{Var}(f)\asymp1$ in the proof of Lemma 66, but
Bobkov--Chistyakov is the direct sharp primary source for (5).

## Collision and mismatch audit

The two source inputs are valid, but they do not by themselves prove the proposed refutation of
`q:weighted`.

1. **One-sided, not two-sided.** Proposition 65 uses $X_i=Y_i-1$ with $Y_i$ a one-sided
   exponential.  The description at `modules/kls/00-orientation.tex` is correct.  The sentence
   at `modules/kls/22-product-stress.tex` that attributes the same endpoint to a product of
   *two-sided* exponentials is not supported by Proposition 65 and should not cite it for that
   model.
2. **Fixed time, not a path window.** Equations (3)--(4) are marginal-in-time statements.  A
   proof using one persistent spike event on $[T/2,T]$ would exceed the source.  A Tonelli proof
   may instead use (4) separately at every $t$.
3. **The density inequality is an upper bound.** It upper-bounds a competing spectator
   half-line perimeter and hence the posterior profile.  It supplies no lower bound on the
   perimeter $P_t(E)$ of the tracked cylinder cut.
4. **The cut still has to qualify, but the companion probe has an internal argument.** No
   external source found proves tensor-stability of a cylinder's near-Cheeger qualification.
   The companion `q:weighted` prober reports the following additive-excess resolution: put
   $h_\infty=\lim_n h_n^\star$, choose a fixed base dimension $m$, law $\nu$, and balanced cut
   $E$ with $P_0(E)\leq h_\infty/2+\delta$; then for every number $N$ of spectators,
   $I_{\nu\otimes\mathrm{Exp}^{\otimes N}}(1/2)\geq h_{m+N}^\star/2\geq h_\infty/2$, so the
   cylinder has $e_0\leq\delta$ uniformly in $N$.  This is repository-internal work, not a
   literature import, and must be checked from the prober's persisted record.  The wording
   `near-Cheeger` remains quantitatively undefined: the argument addresses the additive-excess
   reading, not every possible relative reading.
5. **The joint lower bound is internal work.** One must prove
   on a base event that $t<\tau_\eta$ and $P_t(E)$ stays bounded below.  Product localization
   makes the base filtration independent of the spectator filtration, so (4) can then be
   multiplied by that base event.  The companion prober reports a proof from small-tilt
   continuity of finite perimeter and factor independence; neither external source proves this
   base stability, and the persisted internal argument still needs the normal proof workflow.

Subject to independent checking of the companion probe's internal items 4--5, the literature
scaling is exactly the proposed one: (4), (7), and a base perimeter bounded below give
$e_t(E)\gtrsim1$ and weight $\gtrsim t^{-5/2}$ at each deterministic $t\in[T/2,T]$, producing
an integral of order $T^{-3/2}$.  The primary sources therefore do not kill the proposed
mechanism.  It remains a candidate analytic refutation, not a certified refutation.

## Proposed ledger delta

The event-level refinement has an existing manuscript anchor and is useful independently of the
spectator proposal:

```yaml
- id: prop:covariance-spike
  kind: proposition
  status: imported
  import_class: published
  references: [KLnotes]
  route: shared
  file: modules/kls/00-orientation.tex
  statement: "For N independent centered one-sided exponentials under simplified stochastic localization, P(||A_t||_op >= c/t) >= 1-(1-e^(-1/t)/2)^N; hence this probability is at least 1-e^(-1/2) whenever t >= 1/log N. Equivalently, in Gaussian-channel noise variance s=1/t, the spike has size cs for s<=log N."
```

If the density estimate is to be used as a dependency in a refutation dossier rather than cited
inline, add a manuscript anchor and the following imported node:

```yaml
- id: lem:one-dimensional-density-variance
  kind: lemma
  status: imported
  import_class: published
  references: [BobkovChistyakov2015Concentration]
  route: shared
  file: modules/kls/27-eldan-open-targets.tex
  statement: "For every one-dimensional log-concave probability density f of variance v>0, 1/12 <= v ||f||_infty^2 <= 1. In particular every p-quantile half-line has boundary density at most v^(-1/2)."
```

No dependency edge to `q:weighted` or refutation status is justified until the companion
prober's additive near-Cheeger and base-stability arguments are persisted, authored as a
standalone dossier, and independently reviewed.

## Bibliography delta

The key `KLnotes` already exists.  Its current `@misc` record should be replaced atomically by
the published metadata:

```bibtex
@article{KLnotes,
  author        = {Klartag, Bo'az and Lehec, Joseph},
  title         = {Isoperimetric Inequalities in High-Dimensional Convex Sets},
  journal       = {Bulletin of the American Mathematical Society},
  volume        = {62},
  number        = {4},
  pages         = {575--642},
  year          = {2025},
  doi           = {10.1090/bull/1869},
  eprint        = {2406.01324},
  archivePrefix = {arXiv},
  primaryClass  = {math.FA}
}
```

Add the following new key if the density--variance node or citation is accepted:

```bibtex
@article{BobkovChistyakov2015Concentration,
  author  = {Bobkov, Sergey G. and Chistyakov, Gennadiy P.},
  title   = {On Concentration Functions of Random Variables},
  journal = {Journal of Theoretical Probability},
  volume  = {28},
  number  = {3},
  pages   = {976--988},
  year    = {2015},
  doi     = {10.1007/s10959-013-0504-1}
}
```

## Citation debt

- `KLnotes` is already treated in the repository as published, but its BibTeX type and fields do
  not yet record the journal, volume, issue, pages, or DOI.
- `solutions/kls-excess-audit.tex` cites `Bobkov1999LogConcave` for
  $\lVert f\rVert_\infty\leq1$ in variance-one normalization.  The direct sharp statement and
  proof are Proposition 2.1 of Bobkov--Chistyakov.  The dossier citation should be changed or
  supplemented when its current repair cycle is merged.
- The displayed expectation line in the accessible Klartag--Lehec v2 proof loses the factor
  $s$ typographically; use the event estimate or Proposition 65's statement, not that line in
  isolation.

## Searched and not found

Queries and source searches included:

- `Klartag Lehec Proposition 65 exponential localization covariance`;
- `2406.01324 Proposition 65 one-sided exponential conditional covariance`;
- `log-concave density sup norm variance sharp inequality`;
- `Bobkov Chistyakov concentration functions variance maximum density`;
- searches within the repository for `spectator`, `half-line perimeter`, `near-Cheeger`, and the
  existing uses of `KLnotes` and `Bobkov1999LogConcave`.

I found no primary source providing a persistent-in-time version of the exponential spike, no
source making the spike example two-sided exponential, and no source proving that the proposed
cylinder remains near-Cheeger after addition of arbitrarily many spectators.  The companion
probe's reported additive-excess resolution is internal mathematics, not a literature import.

```yaml
outcome: complete
artifacts:
  - research/explorations/2026-08-27-literature-scout-weighted-spectator-w0l01.md
proposed_deltas:
  - "Import the event-level prop:covariance-spike with import_class published and reference KLnotes."
  - "Optionally import lem:one-dimensional-density-variance with import_class published and reference BobkovChistyakov2015Concentration when a manuscript anchor is added."
  - "Replace the KLnotes bibliography metadata and append BobkovChistyakov2015Concentration exactly as displayed above."
  - "Correct the unsupported two-sided-exponential attribution in modules/kls/22-product-stress.tex; Proposition 65 is one-sided."
next_role: orchestrator
next_prompt: |
  Apply no q:weighted status change from this literature report alone. Import the event-level
  centered-one-sided-exponential covariance-spike node and the sharp density-variance lemma only
  if their manuscript anchors and bibliography entries are added atomically with the displayed
  published provenance. Reconcile this report with the q:weighted prober's persisted additive
  near-Cheeger and base-stability arguments, and sharpen the undefined term `near-Cheeger` before
  assigning a refutation dossier. Require that dossier to use fixed-time Tonelli plus
  product-filtration independence, not an unsupported persistent spike event, and to correct
  every two-sided/one-sided attribution. Only a distinct cold review may then justify a
  refutation node or q:weighted status change.
```
