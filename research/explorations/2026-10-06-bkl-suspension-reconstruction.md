---
---

# Suspension reconstruction and the initialization consequence

## Question examined

Starting lens: **prove**. Reconstruct BKL Section 7 for
[](#prop:bkl-suspension), [](#thm:bkl-tilt-bound), and [](#conj:kls), then
compare the resulting coefficient estimate with
`cand:sz-uniform-conditional-initialization` on route
`ap:sz-conditional-initialization`. The source is
[BKL v1, Section 7](https://arxiv.org/html/2610.05474v1#S7).
The source HTML was provided locally at `/tmp/bkl-2610.05474v1.html`.
Author: Codex (GPT-6), researcher agent `/root/bkl_suspension_author`.

## What we learned

*Established as written arguments, not certified.*
`solutions/bkl-suspension-kls.md` supplies the replicated suspension proof.
The key cancellation is exact: each block has coefficient
$1/\sqrt N$, while the squared Hilbert–Schmidt norm sums $N$ disjoint
blocks. The curvature cost is still $1/\sqrt N$, so choosing a new $N$
for every Laplace noise parameter allows the noise variance to disappear
without taking a limit of measures in changing dimension.

*Established as written arguments, not certified.* Smooth compact tests,
after subtracting their affine projections and normalizing, are dense in
the affine-orthogonal unit sphere. At a fixed measure and degree the Taylor
map is continuous because its coordinates are integrations against fixed
polynomials. The linear component is controlled by the same cumulant
hypothesis; orthogonality then explains the factor two in the squared bound.

*Established as written arguments, not certified.* The full coefficient
bound extends to nonregular isotropic measures by testing the dual Appell
polynomials and passing finitely many moments. Whitening on the range of
the covariance and applying the tensor power of a contraction handles all
centered covariance contractions, including singular ones. This extension
occurs before the spectral criterion and does not use KLS.

*Established as written arguments, not certified.*
`solutions/cor-bkl-uniform-conditional-initialization.md` proves the startup
estimate in every positive degree, with $G=4A$, $r_0=2$, from $c_d\le A^d$.
Its proof uses neither the premise $\mathcal H_r(\Gamma)$ nor KLS. Thus it
would settle the candidate's conclusion if the coefficient chain receives
independent certification. No candidate is closed in this checkpoint.

## What resists

The upstream analytic, cumulant, and tilt-criterion interfaces must be
independently reviewed with this chain. This checkpoint is not a
certification or an applicable ledger-status delta. The initialization
argument does not discharge other bounded-loss iteration contracts.

## Proposed next step

Review the suspension dossier cold against the three canonical statements,
checking the all-dimension cumulant quantifier, bounded-Hessian density,
ordered-index block orthogonality, moment convergence, and singular
covariance contraction. Review the startup corollary against the exact
candidate quantifiers and then, only if its dependency chain is certified,
promote/close the candidate and close the accomplished startup route.
