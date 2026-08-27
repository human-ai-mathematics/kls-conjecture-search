# A3 product and hierarchical-prior proof consolidation

**Date:** 2026-08-27
**Role:** `prover` (`/root/a3_prior_prover`)
**Targets:** `thm:a3-product`, `prop:a3-hierarchical-prior`
**Outcome:** one unconditional, standalone candidate dossier proves both current manuscript
statements. It remains unreviewed (`checked_by: none`) and therefore has no ledger value.

## What was attempted

The goal was to convert the two short analytic drafts in
`modules/open-targets/A3-heavy-tailed-posteriors.tex` into a self-contained proof dossier while
auditing four points that the manuscript proof compresses:

1. the exact normalization and transformation law of a log-half-Cauchy variable;
2. the dimension-free product tensorization constant before and after the Hardy factor-four
   estimate;
3. the entire chain-rule pullback energy, including every structural cross term;
4. sharpness of the constant $4$ without assuming the gap has an attained eigenfunction.

No numerical experiment was run or used.

## Dependency and fence audit

- `thm:a3-product` has the single dependency `thm:hardy-1d`, an imported published node. The
  weighted Hardy/Muckenhoupt statement gives $C_i^{\rm opt}\le 4B_i$. The product part itself is
  proved directly from conditional-variance tensorization.
- `prop:a3-hierarchical-prior` has the single dependency `thm:a3-student`, also an imported
  published node. Its $d=1$, $\beta=1$ branch supplies the exact standard-Cauchy weighted constant
  $4$.
- Neither target has a `bounded_by` edge. The proof nevertheless checks the nearby A3
  obstructions: it asserts a weighted/product result rather than a classical heavy-tail gap;
  independence is explicit in the product theorem; the hierarchical law is a specified
  pushforward, not an arbitrary law inferred from its marginals; and its energy includes scale
  derivatives and all pullback cross terms. No likelihood or posterior-curvature statement is
  made.

Both dependency closures terminate at imported published nodes. No unresolved premise is used,
so both candidate results are unconditional.

## Analytic derivation

### Product certificate

For a finite product $\mu=\bigotimes_i\mu_i$, Efron--Stein gives

\[
 \operatorname{Var}_\mu(f)
 \le \sum_i \mathbb E_{\mu_{-i}}
       \operatorname{Var}_{\mu_i}(f(x_{-i},\cdot)).
\]

Inserting the coordinate weighted inequalities yields the product upper constant
$\max_i C_i$, not $\sum_iC_i$. Testing functions of a single coordinate gives the reverse
inequality for optimal constants, including by approximate extremizers if no optimizer exists.
Thus the exact product constant is $\max_iC_i$. Applying the imported one-dimensional bound
$C_i\le4B_i$ proves the ledger statement $C_{\rm product}\le4\max_iB_i$.

### Log-half-Cauchy normalization and sharp constant

If $S\sim C^+(0,1)$, then

\[
 q(u)=\frac{2e^u}{\pi(1+e^{2u})}=\frac1{\pi\cosh u}
\]

is the density of $U=\log S$. Separately, if $X$ is standard Cauchy, then
$Y=\operatorname{arsinh}X$ has the same density because
$(1+\sinh^2u)^{-1}\cosh u=(\cosh u)^{-1}$. The equality needed by the proof is equality in
law, not a pathwise identity between the two original variables.

At $d=1$, $\beta=1$, `thm:a3-student` gives the exact Cauchy weighted constant $4$ for weight
$1+x^2$. Under $u=\operatorname{arsinh}x$, this weighted energy becomes
$\int|h'(u)|^2q(u)\,du$ exactly. The transformation is an isometry of form domains, so the
classical Poincaré constant of $q$ is exactly $4$, not merely at most $4$.

### Base product and pullback

The standard Gaussian constant is $1$ (proved in the dossier by the Ornstein--Uhlenbeck
variance-dissipation identity). Conditional-variance tensorization therefore makes the Euclidean
constant of the independent base vector $(Z,U,V)$ equal to $4$.

For $T(z,u,v)=(\theta,u,v)$ with $\theta_j=e^{u+v_j}z_j$, the full chain rule is

\[
 \partial_{z_j}(f\circ T)=e^{u+v_j}f_{\theta_j},\qquad
 \partial_{v_j}(f\circ T)=f_{v_j}+\theta_jf_{\theta_j},\qquad
 \partial_u(f\circ T)=f_u+\sum_j\theta_jf_{\theta_j}.
\]

Squaring and summing gives exactly the manuscript energy. Its expanded form also contains

- $2\theta_j f_{v_j}f_{\theta_j}$ coefficient--local-scale terms;
- $2\theta_j f_uf_{\theta_j}$ coefficient--global-scale terms;
- $2\theta_j\theta_k f_{\theta_j}f_{\theta_k}$ terms for every $j<k$;
- two copies of each $\theta_j^2f_{\theta_j}^2$, one from the local-scale square and one from
  the global-scale square.

The pushforward identity transfers the base constant $4$ to this pullback form.

For sharpness, one must use a sequence $h_k(U)$ whose one-dimensional variance/energy ratios
tend to $4$. This gives joint test functions depending on $U$ alone with the same ratios.
It does not assume that a one-dimensional extremizer is attained.

## Dead ends and corrections retained

1. The manuscript shorthand “transform through $u=\operatorname{arsinh}x$” can be misread as
   saying that the logarithm of a half-Cauchy variable is pathwise the `arsinh` of that same
   variable. That is false. The repaired proof computes both pushforward densities and uses their
   equality in law.
2. The simple test $f=u$ does not prove optimality $4$: its Rayleigh ratio is
   $\operatorname{Var}_q(U)=\pi^2/4<4$. The correct lower-bound argument uses the
   near-extremizing sequence inherited from the sharp Cauchy inequality.
3. Keeping only diagonal coefficient terms after noncentring is not the pullback of the base
   Euclidean form. Expanding the three chain-rule squares exposes the missing coefficient--scale
   and inter-coefficient terms. The dossier records both the compact square form and its full
   expansion.
4. A raw-scale Euclidean Poincaré claim was not pursued: half-Cauchy scales are heavy-tailed and
   the log map is non-bi-Lipschitz. The proved statement is exactly the log-scale/pullback-metric
   proposition in the manuscript.

## Artifact and certification boundary

Candidate dossier:
`solutions/a3-product-hierarchical-prior.tex`.

The dossier intentionally records `checked_by: none`. No ledger, manuscript, review, knowledge,
or bibliography file was edited. The future atomic ledger candidate, only after an independent
passing review, is to point both target nodes at this shared dossier with that review's real
`checked_by` provenance.

## Validation

- `cd solutions && latexmk -pdf -outdir=../build a3-product-hierarchical-prior.tex` succeeds and
  produces `build/a3-product-hierarchical-prior.pdf` (four pages).
- The final log has no TeX errors and no overfull or underfull boxes. Its only warnings are the
  expected standalone `??` references to the four cross-module labels `thm:a3-product`,
  `prop:a3-hierarchical-prior`, `thm:hardy-1d`, and `thm:a3-student`.
- `python3 research/check_ledger.py` reports two ledgers, 174 nodes, 636 labels, and 0 errors.
