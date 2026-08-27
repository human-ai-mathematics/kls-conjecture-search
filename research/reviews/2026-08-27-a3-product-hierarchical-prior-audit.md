---
type: audit
date: "2026-08-27"
---

# A3 product and hierarchical-prior dossier — independent audit

This is a cold review by `/root/a3_prior_review` of
`solutions/a3-product-hierarchical-prior.tex`, authored by `/root/a3_prior_prover`.  The
reviewed file has SHA-256
`c281f5f6f5d67086f3c3507d2607fda6aacb034f902740dbf6f208402dac7d18`.  The proof was
reconstructed from the dossier, ledger, manuscript, and actual published dependency sources;
the prover's exploration narrative was not used as evidence.  The reviewer is distinct from the
author.

## Findings

### Verdict

Revision is required.  The mathematical route and all substantive constants check out, but the
current dossier prints a false total-variance identity at lines 64--66: the addition sign between
the conditional-variance term and the variance-of-the-conditional-mean term is missing.  Since
that displayed identity is the dossier's stated derivation of finite-product Efron--Stein, the
artifact cannot receive proof certification as written.  This audit carries no certification or
ledger delta; a repaired dossier requires a new independent review report.

### Statement agreement

The theorem and proposition otherwise agree mathematically across all three planes.

- For `thm:a3-product`, the ledger states the $4\max_i B_i$ weighted product bound, the
  manuscript states both exact tensorization with $\max_i C_i$ and that Hardy consequence, and
  the dossier states and proves those same finite-product claims in the diagonal metric.
- For `prop:a3-hierarchical-prior`, all three state the noncentered Gaussian/log-half-Cauchy
  prior, optimal constant $4$, and the same pullback energy with coefficient--scale cross terms.
  The dossier merely makes the standard half-Cauchy variables and the finite dimension explicit.

Neither target has a formal `bounded_by` edge.  The nearby fences are nevertheless respected:

- `obs:heavy-tail-no-classical`: neither claim gives a raw Euclidean gap in centered heavy-tail
  coordinates; the product theorem is weighted, and the hierarchical result uses the pullback of
  Euclidean noncentered coordinates.
- `obs:marginals-not-joint`: the first theorem assumes an independent product.  The proposition
  treats one fully specified dependent pushforward and keeps every scale direction and structural
  cross term; it does not infer a joint gap from marginals.
- `obs:flat-direction`: the proposition is prior-only and makes no claim that a saturating
  likelihood supplies a posterior curvature floor.

### Dependencies and source debt

Both dependencies are discharged published results; no unreviewed preprint enters the argument.

- `thm:hardy-1d` is classified `imported` / `published`.  Muckenhoupt, *Studia Mathematica* 44
  (1972), Theorem 1, gives for $p=2$ the one-sided weighted Hardy norm constant between $B^{1/2}$
  and $2B^{1/2}$.  Squaring, applying the two half-line inequalities about a median, and using
  $\operatorname{Var}(g)\le\int|g-g(m)|^2\,d\mu$ gives exactly
  $C_i\le4\max(B_{i,+},B_{i,-})$, with no dimension-dependent loss.
- `thm:a3-student` is classified `imported` / `published`.  Huguet, *Bernoulli* 30 (2024),
  Theorem 1.1, DOI `10.3150/23-BEJ1670`, gives the optimal one-dimensional generalized-Cauchy
  gap $(\beta-\tfrac12)^2$ for $\tfrac12<\beta\le\tfrac32$.  At $\beta=1$ this is $1/4$ for
  density $\{\pi(1+x^2)\}^{-1}$ and energy $\int(1+x^2)|g'|^2\,d\mathsf C$, exactly the
  constant used.  The source also supplies near-extremizers in the low-parameter branch, though
  their existence already follows from optimality of the variational constant.  The earlier
  published Bonnefont--Joulin--Ma paper cited by the node is consistent with this one-dimensional
  calibration.

### Checked proof steps

1. Conditional-variance tensorization, once the missing `+` is restored, gives the upper product
   constant $\max_i C_i$ for every finite product.  Coordinate-only tests (or an approximating
   sequence when a factor gap is unattained) give the matching lower bound, so the tensorized
   constant is exactly $\max_i C_i$.
2. Inserting the published one-dimensional estimates $C_i\le4B_i$ gives precisely
   $4\max_iB_i$, not $4\sum_iB_i$.
3. A standard half-Cauchy has density $2/\{\pi(1+s^2)\}$ on $(0,\infty)$.  Under $y=\log s$
   its normalized density is
   $2e^y/\{\pi(1+e^{2y})\}=1/(\pi\cosh y)$.
4. If $X$ is standard Cauchy, $\operatorname{arsinh}X$ has that same density.  For
   $g(x)=h(\operatorname{arsinh}x)$, the factor
   $g'(x)=h'(\operatorname{arsinh}x)/\sqrt{1+x^2}$ cancels the Cauchy weight exactly.  The map is
   unitary in $L^2$ and isometric for the two Dirichlet energies, so the sharp constant $4$
   transfers in both directions.
5. The dossier's Ornstein--Uhlenbeck calculation proves the standard Gaussian constant $1$.
   Tensorization of $d$ Gaussian factors and $d+1$ log-half-Cauchy factors therefore gives base
   product constant $4$; a function of one log-scale coordinate and a near-extremizing sequence
   show equality.
6. The map $T(z,u,v)=(e^{u+v_j}z_j,u,v)$ is a global smooth bijection with the printed inverse.
   Its three derivative formulas are complete.  Squaring them gives exactly the pullback energy.
   Expanding verifies the coefficients $e^{2u+2v_j}+2\theta_j^2$ and all three cross-term classes:
   coefficient--local-scale, coefficient--global-scale, and distinct coefficients.
7. Pushforward preserves variance and the chain rule preserves energy.  The unitary pullback
   defines the closed form without a boundary issue.  Pulling a log-scale near-extremizing sequence
   back as $f_k(\theta,u,v)=h_k(u)$ leaves energy $|h_k'(u)|^2$, proving optimality of $4$ without
   assuming an attained extremizer.

### Hypothesis accounting

The product argument uses finiteness of the product, independence, probability normalization,
the coordinate densities and medians defining $B_{i,\pm}$, positive measurable weights, and
finiteness of every $B_i$.  The exact tensorization clause uses the factor optimal constants and
the associated closed product form.  The hierarchical argument uses finite $d\ge1$, mutually
independent standard Gaussian and standard half-Cauchy variables, and the full joint law of
$(\Theta,U,V)$ with no likelihood tilt.  These hypotheses are stated.  No stated mathematical
hypothesis is unused, and no numerical observation is used.

### Step not verified

Only the displayed equality at `solutions/a3-product-hierarchical-prior.tex:64` is not verified:
as typeset it multiplies (by juxtaposition) the two scalar variance terms instead of adding them.
The correct law of total variance is
$$
\operatorname{Var}_{\mu_1\otimes\mu_2}(f)
=\int\operatorname{Var}_{\mu_1}(f(\cdot,x_2))\,d\mu_2(x_2)
 +\operatorname{Var}_{\mu_2}\!\left(\int f(x_1,\cdot)\,d\mu_1(x_1)\right).
$$
All remaining steps listed above were checked.

### Mechanical validation

The required command

```text
cd solutions && latexmk -g -pdf -outdir=../build a3-product-hierarchical-prior.tex
```

succeeds and produces a four-page PDF.  The only LaTeX warnings are the expected unresolved
standalone cross-module references to `thm:a3-product`, `prop:a3-hierarchical-prior`,
`thm:hardy-1d`, and `thm:a3-student`.  The successful build also confirms that the missing `+`
is not a parser failure: the false juxtaposition is visibly present in the generated PDF.

## Corrections required

In `solutions/a3-product-hierarchical-prior.tex:65-66`, insert `+` before the second
`\Var_{\mu_2}` term in the displayed two-factor law of total variance.  Rebuild the standalone
PDF.  Do not change the theorem statements, constants, pullback metric, dependency claims, or
ledger in response to this audit.  Submit the repaired dossier for a fresh cold proof review;
this append-only audit must remain unchanged.

## Exclusions

This audit does not certify either target, any posterior obtained by adding a likelihood, the open
dependence target `conj:a3-dependent`, arbitrary dependent laws with the same marginals, raw
Euclidean inequalities for half-Cauchy scales, or any downstream A3 question.  It proposes no
`solution`, `checked_by`, `review`, or status ledger delta.
