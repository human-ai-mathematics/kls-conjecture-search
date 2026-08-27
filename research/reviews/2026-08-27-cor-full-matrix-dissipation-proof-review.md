---
type: audit
date: "2026-08-27"
---

# Full matrix dissipation — cold W2 audit

This is an independent review of
`solutions/cor-full-matrix-dissipation.tex`, SHA-256
`5164913efaa6a4059c0d8f8f69f32ebc329a18b39601a150feb6ac84d7b1548c`, for
`cor:full-matrix-dissipation`.  The author is
`/root/prove_full_matrix_dissipation_w2` and the reviewer is
`/root/review_full_matrix_dissipation_w2`.  The author's exploration narrative was not used as
proof evidence.

This report does not certify the dossier.  The proof of the ledger target is mathematically sound
for its actual deterministic initial matrix $R_0$, but the abstract lemma invoked by the theorem
omits that initial-value hypothesis and is false or ill-typed at its printed level of generality.
The repair is small, but a fresh review of the repaired bytes is required.

## Findings

### Statement agreement, fences, and dependency closure

The manuscript statement at `modules/kls/12-riccati.tex:121`--`130` and the ledger statement ask
for

$$
\mathbb E\int_0^\infty (R_t^2+s_tG_t^2)\,dt\preceq R_0,
$$

with the explicit warning that taking a trace can cost the dimension.  The dossier states this
same conclusion under the standing isotropic log-concave, fixed nontrivial cut setup and proves the
stronger finite-horizon inequality

$$
\mathbb E R_T+\mathbb E\int_0^T(R_t^2+s_tG_t^2)\,dt\preceq R_0.
$$

Thus there is no mathematical disagreement among the target statements.  The target has no
formal `bounded_by` edge.  The nearby operator-to-trace obstruction is nevertheless an applicable
semantic fence, and the dossier respects it: it derives only
$\mathbb E\int_0^\infty(\|R_t\|_{\mathrm{HS}}^2+s_t\|G_t\|_{\mathrm{HS}}^2)dt
\leq\operatorname{Tr}R_0\leq n$ and explicitly disclaims a dimension-free trace upgrade.  It does
not assert an implication for `q:upgrade`, `q:stein-weighted`, `q:alignment`, or any other member
of the trace-upgrade cluster.

The only declared mathematical dependency, `lem:matrix-riccati`, is `proved` and is covered by
the passing agent review `research/reviews/2026-08-25-kls-core-r2-audit.md`, whose front matter
contains both that node and `solutions/kls-localization-riccati-core.tex` with distinct author and
reviewer.  Its certified conclusion is exactly

$$
dR_t=d\widetilde N_t-(R_t^2+s_tG_t^2)\,dt.
$$

There is no open, conditional, imported-preprint, or numerical premise in the target's dependency
closure.  The target dossier cites no external result.  The Gaussian computation used as an
illustration was rederived directly, so it creates no citation debt.

### Defect: the abstract lemma omits its initial-value hypothesis

At `solutions/cor-full-matrix-dissipation.tex:61`--`78`, the abstract lemma starts with an arbitrary
continuous adapted positive-semidefinite matrix process.  It does not say that $X_0$ is
deterministic or even integrable, but concludes

$$
\mathbb E X_T+\mathbb E\int_0^TQ_t\,dt\preceq X_0
$$

and its optional-sampling calculation at lines 96--106 replaces
$\mathbb E x_0^\theta$ by $x_0^\theta$.  That step uses determinism of $X_0$ without stating it.

This is not valid for the printed generality.  In dimension one, let $X_t=X_0$ for all $t$, where
$X_0$ is a nonconstant nonnegative integrable random variable, and take $N=0$, $Q=0$.  All printed
assumptions hold.  The conclusion becomes $\mathbb E X_0\leq X_0$ if read almost surely, which
fails, for example, when $X_0$ is Bernoulli; if the right side is not read pointwise, the comparison
between a deterministic expectation and an unaveraged random matrix is simply ill-typed.

The actual application has no such problem: the initial law and cut are fixed, hence $R_0$ is a
deterministic finite matrix.  The printed proof establishes precisely that specialization.  But the
requested abstract lemma is an asserted intermediate result in the dossier, and the deterministic
initial-value condition is a used but unstated hypothesis.  It must be made explicit before the
dossier can be certified.  The expectation display at line 111 also contains the adjacent typo
`E a_T^\theta` in place of `\E a_T^\theta`; its surrounding argument is unambiguous, but it should
be corrected in the same repair.

### Checked stochastic and matrix steps

Subject to the missing deterministic-$X_0$ clause, the abstract argument was checked line by line.

1. For each deterministic $\theta$, scalarization gives a nonnegative process
   $x_t^\theta$, an increasing occupation $a_t^\theta$, and a scalar local martingale
   $M_t^\theta$ satisfying $x_t^\theta+a_t^\theta=x_0^\theta+M_t^\theta$.
2. A localizing sequence can be chosen so that each stopped scalar local martingale is a true
   martingale.  Optional sampling at the bounded time $T\wedge\sigma_k$ is legitimate.  With
   deterministic finite $x_0^\theta$, the stopped nonnegative sum is integrable and has expectation
   $x_0^\theta$.
3. Since $\sigma_k\uparrow\infty$ almost surely, continuity of $X$ and pathwise local
   integrability of $Q$ give convergence at every fixed $T$.  Fatou applied to the nonnegative sum
   yields
   $\mathbb E x_T^\theta+\mathbb E a_T^\theta\leq x_0^\theta$ without uniform
   integrability of the unstopped martingale.
4. Testing coordinate vectors makes the diagonal entries of $X_T$ and
   $H_T=\int_0^TQ_tdt$ integrable.  Positivity gives
   $|X_{ij}|\leq(X_{ii}+X_{jj})/2$ and
   $\int|Q_{ij}|\leq(H_{ii}+H_{jj})/2$, which proves absolute entrywise integrability.  Testing all
   deterministic $\theta$ then reconstructs the finite-horizon Loewner inequality.
5. Monotone convergence for each nonnegative quadratic-form occupation gives the infinite-time
   directional bound.  Applying it to coordinate vectors and using the same positive-semidefinite
   entry estimate proves almost-sure absolute convergence and $L^1$ integrability of every matrix
   entry, after which polarization gives the infinite-horizon Loewner inequality.
6. In the localization application, covariance decomposition gives $R_t\succeq0$; symmetry of
   $R_t,G_t$ and $s_t\geq0$ give
   $Q_t=R_t^2+s_tG_t^2\succeq0$.  The certified semimartingale identity supplies the required
   continuous local martingale and locally integrable drift.  The preceding argument therefore
   proves the finite inequality including $\mathbb E R_T$ and its infinite-time consequence.

No stochastic or matrix step other than the overbroad initial-value statement remains unverified.

### Hypothesis accounting and the Gaussian trace example

The target application uses: a fixed initial probability law and fixed measurable cut; finite
second moments; $0<\mu(E)<1$ and strict positivity of the finite-time likelihood so that both
conditional covariances remain defined; the certified continuous matrix Riccati identity;
covariance decomposition; and symmetry/nonnegativity of the matrix drift.  Isotropy is used only
for $A_0=I_n$ and hence $R_0=A_0-B_0\preceq I_n$.  The estimate with right side $R_0$ does not use
isotropy.  Log-concavity belongs to the standing localization setup but is not separately spent by
the positive-drift argument.  No balance, stopping window, cut-boundary regularity, compact
support, fourth moment, or endpoint uniform-integrability assumption is used.

For the standard Gaussian, completing the square in the localization density gives a product
Gaussian posterior with mean $c_t/(1+t)$ and covariance $(1+t)^{-1}I_n$.  Conditioning on
$E=\{x_1\leq0\}$ changes only the first coordinate.  Therefore, pathwise for every $j\geq2$,

$$
G_te_j=0,\qquad R_te_j=(1+t)^{-1}e_j,
\qquad \int_0^\infty|R_te_j|^2dt=1.
$$

The retained $R_t^2$ term is thus genuine and its spectator directions contribute exactly $n-1$
to the traced occupation.  This verifies both the example and the claimed dimension cost without
using numerical evidence.

### Standalone build and structural context

A forced standalone rebuild from `solutions/`,

```text
latexmk -g -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=../build cor-full-matrix-dissipation.tex
```

returned exit code zero and produced a visually inspected three-page PDF.  There is no TeX error,
fatal warning, overfull box, or underfull box.  The three unresolved parent labels are expected in
standalone subfile mode.

Before this report was added, `python3 research/check_ledger.py` reported one unrelated structural
error: `ass:weighted-package.refuted_by` names `prop:weighted-spectator-obstruction` without the
required matching `depends_on` edge.  That concurrent ledger condition is outside this reviewer's
write surface and is unrelated to `cor:full-matrix-dissipation`.

## Corrections required before a new review

1. At `solutions/cor-full-matrix-dissipation.tex:61`--`68`, state explicitly that the abstract
   process has a deterministic initial matrix $X_0$.  This is the minimal repair matching the
   application.  An alternative, more general repair is to assume entrywise integrability of a
   random $X_0$ and replace every right side $X_0$ or $x_0^\theta$ after expectation by
   $\mathbb E X_0$ or $\mathbb E x_0^\theta$, respectively.
2. At `solutions/cor-full-matrix-dissipation.tex:111`, replace `E a_T^\theta` by
   `\E a_T^\theta`.
3. Keep the dossier at `checked_by: none`, make no certification change to the ledger, and submit
   the repaired dossier bytes to a new independent proof review.  This audit proposes no
   certification delta.

## Exclusions

This audit does not recertify the upstream Riccati dossier beyond checking its active passing
certification and exact applicability.  It does not certify `cor:per-direction`, any
operator-to-trace upgrade, any all-cut Carleson statement, any trace-upgrade-cluster implication,
or any numerical artifact.  The Gaussian halfspace calculation is checked only as the dossier's
sharpness illustration, not as a separate ledger claim.  No solution, manuscript, ledger,
bibliography, exploration, knowledge, route-control, or prior-review file was changed.
