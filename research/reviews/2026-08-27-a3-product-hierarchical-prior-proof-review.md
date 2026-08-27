---
type: proof-review
date: "2026-08-27"
verdict: pass
authors:
  - /root/a3_prior_prover
reviewer: /root/a3_prior_review
nodes:
  - thm:a3-product
  - prop:a3-hierarchical-prior
solutions:
  - solutions/a3-product-hierarchical-prior.tex
follows_up: research/reviews/2026-08-27-a3-product-hierarchical-prior-audit.md
---

# A3 product and hierarchical-prior dossier — independent proof review

This is a fresh cold review of `solutions/a3-product-hierarchical-prior.tex`, whose reviewed
SHA-256 is `5b23fc098363d58fa3691717ad680c91e4c1ca88d9708983b72923c0a51fcea6`.
The proof was reconstructed from the dossier, ledger, manuscript, and actual published sources.
The author's exploration narrative was not used as evidence, and the reviewer is distinct from
the author.

## Findings

### Repair verification

The earlier audit identified one false displayed identity: the two terms in the two-factor law of
total variance lacked their addition sign.  The current dossier has the required `+` at line 66.
As a byte-level scope check, deleting exactly that one inserted character from the current file
reproduces the earlier audited SHA-256
`c281f5f6f5d67086f3c3507d2607fda6aacb034f902740dbf6f208402dac7d18`.  Thus no other change was
introduced between the failed artifact and this repaired artifact.  The repaired identity is the
correct law of total variance, and conditional Jensen now yields the printed two-factor
Efron--Stein inequality.

### Statement agreement, dependencies, and fences

The dossier, ledger, and labeled manuscript statements agree mathematically.

- `thm:a3-product` gives exact finite-product tensorization with constant $\max_i C_i$, followed
  by the weighted Hardy consequence $4\max_i B_i$ in the diagonal product metric.
- `prop:a3-hierarchical-prior` gives the specified noncentered Gaussian/log-half-Cauchy prior,
  optimal constant $4$, and the same full pullback energy on all three planes.

The dependency closure is unconditional.  `thm:hardy-1d` and `thm:a3-student` are both
`imported` / `published`.  Muckenhoupt's 1972 weighted Hardy theorem at exponent two gives the
one-sided squared-norm upper factor $4$ used here.  Huguet's published Bernoulli theorem (2024,
DOI `10.3150/23-BEJ1670`) gives the exact generalized-Cauchy gap
$(\beta-\tfrac12)^2$ in dimension one for $\tfrac12<\beta\le\tfrac32$, hence gap $1/4$ and
Poincar\'e constant $4$ at $\beta=1$.  No preprint-unreviewed result or numerical evidence is
used.

Neither target has a formal `bounded_by` edge.  The three nearby A3 obstructions are respected:
`obs:heavy-tail-no-classical` because the claims use weighted/pullback metrics;
`obs:marginals-not-joint` because independence is explicit in the product theorem and the
hierarchical proposition treats a fully specified pushforward with all scale directions; and
`obs:flat-direction` because the latter is a prior-only statement and asserts no likelihood
curvature floor.

### Checked steps

1. The repaired two-factor total-variance identity and conditional Jensen iterate to
   Efron--Stein for every finite product.
2. Applying the factor inequalities sectionwise and using Fubini gives the upper constant
   $\max_iC_i$.  Coordinate-only tests, with approximate optimizers if needed, give the reverse
   inequality for the optimal constant.
3. Applying the published one-dimensional bound $C_i\le4B_i$ gives exactly
   $4\max_iB_i$, without a sum over coordinates.
4. The standard half-Cauchy density transforms under $y=\log s$ to the normalized density
   $q(y)=1/(\pi\cosh y)$.
5. The same $q$ is the pushforward of standard Cauchy under $\operatorname{arsinh}$.  Its
   derivative cancels the weight $1+x^2$ exactly, and the correspondence is an $L^2$ and
   Dirichlet-energy isometry.  Sharpness therefore transfers in both directions.
6. The standard Gaussian factor has optimal constant $1$.  Tensorizing $d$ Gaussian factors and
   $d+1$ log-half-Cauchy factors gives base product constant $4$, with equality witnessed by a
   log-scale near-extremizing sequence.
7. The map $T(z,u,v)=(e^{u+v_j}z_j,u,v)$ is a global diffeomorphism.  All three chain-rule
   formulas are correct.  Their squares yield the displayed pullback energy and, on expansion,
   the coefficient--local-scale, coefficient--global-scale, and distinct-coefficient cross terms
   with the printed coefficients.
8. Variance and energy are preserved by the unitary pullback.  Functions depending only on $u$
   preserve the log-scale Rayleigh quotient, proving optimality of $4$ without assuming an
   attained extremizer.

### Hypothesis accounting

The product proof uses a finite independent product, probability densities and medians, positive
measurable weights, finiteness of the Hardy quantities, and the associated closed factor/product
forms.  The hierarchical proof uses fixed finite $d\ge1$, mutually independent standard
Gaussian and standard half-Cauchy variables, and the complete joint law of $(\Theta,U,V)$ with no
likelihood.  Every used hypothesis is stated.  No stated mathematical hypothesis is unused.

### Mechanical validation

`cd solutions && latexmk -g -pdf -outdir=../build a3-product-hierarchical-prior.tex` succeeds and
produces a four-page PDF.  The repaired `+` is visibly present.  The only warnings are the expected
standalone unresolved cross-module references.

## Corrections

None.  The sole defect in the earlier audit is repaired and fully rechecked.

## Exclusions

This review does not certify likelihood-tilted posteriors, arbitrary dependent laws sharing the
same marginals, `conj:a3-dependent`, raw Euclidean half-Cauchy inequalities, or any downstream A3
question.
