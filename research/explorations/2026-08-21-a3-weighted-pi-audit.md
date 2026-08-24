# A3 audit — tail floors, horseshoe scale covariance, and the dependence gap

**Date:** 2026-08-21
**Target:** `conj:a3`, `prop:a3-horseshoe`, `q:a3-*`
**Outcome:** the product/one-dimensional programme is sound after qualification, but the current
joint-posterior conjecture is false as stated. This note separates proved calculations,
counterexamples, conjectures, and non-promotable diagnostics.

Here “proved” denotes an internal analytic derivation or a cited imported theorem, not a new ledger
promotion. At the time of this audit, new derivations remained proof drafts under the then-current
standalone-solution and human/Lean gate.

> **Later certification update.** Section 11 records the subsequent independent-agent audit that
> promoted `prop:a3-horseshoe` and `thm:a3-block-gibbs`. Product, hierarchical-prior,
> fixed-marginal, and bounded-likelihood drafts were outside that review and remain unpromoted.

## 1. Repository and evidence scope

Read in full: `research/README.md`, `research/explorations/README.md`, `orchestration.md`, the A3
target notebook and manuscript, the A3 ledger nodes, all three shared knowledge documents,
`experiments/finum/targets/a3.py`, and `research/runs/2026-06-20-A3.jsonl`.

The stored run has `git_dirty: true`. It is historical obstruction diagnostics only, not evidence
for a positive conjecture. The computations below are deterministic audit diagnostics and are
also **not** provenance-eligible evidence. The proof-draft/refuted conclusions were subsequently
integrated into the ledger, manuscript, target notebook, and shared knowledge during this cycle.

## 2. Proved: what one-dimensional regular variation actually gives

Let `mu(dx)=p(x)dx` on the line, with median zero for simplicity, and consider

`Var_mu(f) <= C_w int a(x)|f'(x)|^2 mu(dx)`.

The correct one-sided Hardy quantity is

`B_+ = sup_{x>0} mu([x,infinity)) int_0^x dt/(a(t)p(t))`,

and `B_+ <= C_opt <= 4 B_+` in the symmetric case.

Assume on the positive tail

`p(x) ~ c x^(-1-alpha)L(x)`, `a(x) ~ kappa x^2`, `alpha>0`,

with `L` slowly varying. Karamata's theorem gives

```
mu([x,infinity)) ~ (c/alpha) x^(-alpha)L(x),
int^x dt/(a(t)p(t)) ~ x^alpha/(kappa c alpha L(x)),
```

and hence the proved tail limit

`mu([x,infinity)) int_0^x dt/(a(t)p(t)) -> 1/(kappa alpha^2)`.

Consequences:

- the tail forces `B_+ >= 1/(kappa alpha^2)`;
- it does **not** upper-bound the full supremum, which may be dominated by a finite-location
  bottleneck;
- `C_w asymp alpha^-2` is defensible as `alpha -> 0` only for a family whose bulk Hardy
  contribution is uniformly controlled by `O(alpha^-2)`.

Thus the former ledger/manuscript claim `C_w asymp max_j alpha_j^-2` had no globally valid meaning
without a regime and uniform body assumptions; the integrated statement now includes those
qualifications.

### Intrinsic coordinate and the sharper tail floor

For `a(x)=1+x^2`, put `y=asinh(x)` and `g(y)=f(sinh y)`. Then exactly

```
int (1+x^2)|f'(x)|^2 mu(dx) = int |g'(y)|^2 q(y)dy,
q(y) = p(sinh y) cosh y.
```

Regular variation turns into `q(y) ~ c' exp(-alpha y)L(exp(y))`. Under the usual smooth tail
regularity, translated approximate eigenfunctions
`g(y)=exp(alpha y/2) phi((y-R)/ell)` give Rayleigh quotients tending to `alpha^2/4`. Therefore

`C_w >= 4/alpha^2`.

For a pure Cauchy-type tail this is the bottom of the tail continuum; an additional bulk
eigenmode can only make `C_w` larger.

## 3. Proved: exact generalized-Cauchy and Student rescaling

For `mu_beta(dx) proportional (1+|x|^2)^(-beta)dx`, put `alpha=2 beta-d`. The exact Huguet
spectral gap translates to

```
d=1:
  lambda = alpha^2/4,                  0<alpha<=2,
  lambda = alpha-1,                    alpha>=2.

d>=2:
  lambda = alpha^2/4,                  0<alpha<=4,
  lambda = 2 alpha-4,                  4<=alpha<=d+2,
  lambda = alpha+d-2,                  alpha>=d+2.
```

Hence `C_w=4/alpha^2` is exact only in the near-integrability branch. In one dimension, for
example, the lighter-tail branch is `C_w=1/(alpha-1)`, not `Theta(alpha^-2)`.

For `X` with multivariate Student `t_nu(0,Sigma)`, write
`X=sqrt(nu) Sigma^(1/2)Y` and `beta=(nu+d)/2`. The sharp radial statement is

```
lambda_{beta,d} Var(f(X))
 <= E[(nu+X^T Sigma^-1 X) grad f(X)^T Sigma grad f(X)].
```

Equivalently, with normalized radial metric
`(1+X^T Sigma^-1 X/nu)Sigma`, the constant is `nu/lambda_{beta,d}`. This is not the same law or
metric as a product of independent Student coordinates; the latter tensorizes the one-dimensional
constants.

### Citation audit

The formula in the manuscript agrees with Theorem 1.1 of
[Huguet, arXiv:2302.02684v2](https://arxiv.org/abs/2302.02684). The repository bibliography entry
previously named a different title and gave `2403.07393`; that identifier is
[an unrelated gravimetry paper](https://arxiv.org/abs/2403.07393). The coordinator corrected the
shared bibliography during integration.

## 4. Proved: weighted LSI is a distinct statement

[Bobkov--Ledoux (2009)](https://doi.org/10.1214/08-AOP407), Theorem 3.4, prove for generalized
Cauchy `nu_beta` on `R^d`, under `beta >= (d+1)/2` and `beta>1`,

`Ent_{nu_beta}(g^2) <= (beta-1)^-1 int |grad g|^2(1+|x|^2)^2 dnu_beta`.

This needs a **quartic** Dirichlet weight. It is not an entropy version of A3 in the same
quadratic metric, and in one dimension it does not cover the Cauchy/horseshoe boundary
`alpha=1`. The three sampler statements should remain separate:

- quadratic weighted PI for the preconditioned diffusion;
- weak PI for raw Euclidean dynamics;
- quartic weighted LSI where its additional parameter conditions hold.

## 5. Proved: product tensorization, and why weak PI is not dimension-free

If each factor satisfies
`Var_{mu_j}(h) <= C_j int a_j |h'|^2 dmu_j`, conditional variance decomposition gives

`Var_{tensor mu_j}(f) <= max_j C_j int sum_j a_j(x_j)|partial_j f|^2 dmu`.

Combining this with Hardy gives the fully safe A3 theorem

`C_product <= 4 max_j B_j`.

This is dimension-free in the weighted metric.

For weak PI, suppose a factor obeys

`Var(f) <= beta_1(s) int |f'|^2 dmu + s Osc(f)^2`.

Applying the factor inequality with `s/d` in each conditional-variance term gives
`beta_d(s) <= beta_1(s/d)`. Therefore a regularly varying rate
`beta_1(s) asymp s^(-2/alpha)` yields the product upper rate
`d^(2/alpha)s^(-2/alpha)`. Smoothed indicators of
`{max_j |X_j|>R}` give the matching order for iid regularly varying factors. The manuscript's
weak rate exponent is plausible in one dimension, consistently with
[Cattiaux--Gozlan--Guillin--Roberto (2010)](https://doi.org/10.1214/EJP.v15-754), but it must not
inherit the weighted theorem's dimension-free slogan.

## 6. Refuted: coordinate marginals do not control a dependent joint law

This is a statement-level counterexample, not a numerical objection.

It is enough to fix the standard Cauchy density `p(x)=1/[pi(1+x^2)]`, with CDF `F`. Put
`A=(0,1/2)` and `D=(1/2,1)`. On `(0,1)^3`, define the positive-a.e., piecewise-smooth copula
density

`c_epsilon=(1-epsilon)4[1_{A^3}+1_{D^3}]+epsilon`.

Every one-dimensional marginal is uniform. Therefore

`pi_epsilon(x)=prod_j p(x_j) c_epsilon(F(x_1),F(x_2),F(x_3))`

has exactly the same marginal `p` in all three coordinates for every `epsilon in (0,1)`.

Translate the common corner `o=(1/2,1/2,1/2)` to the origin. Choose a smooth odd angular function
`g` on `S^2` that is `+1` on the all-negative octant, `-1` on the all-positive octant, and changes
only through mixed-sign octants. Then
`phi(u)=g((u-o)/|u-o|)` belongs to `H^1((0,1)^3)`: its gradient is `O(|u-o|^-1)`, whose square is
locally integrable in three dimensions. Its gradient is supported where the copula density is
`epsilon`, while the two high-density cubes give variance at least `1-3 epsilon/4`.

Under `u_j=F(x_j)`, the diagonal Cauchy-weight energy has coefficient
`(1+x_j^2)p(x_j)^2 <= 1/pi^2`. Thus the energy is at most
`epsilon pi^-2 int |grad phi|^2`, and smooth-test approximation in this bounded coefficient gives
the same Rayleigh conclusion. Hence the joint constant is at least `c/epsilon` while every
marginal and marginal Hardy quantity is fixed. This argument claims piecewise-smooth joint
densities and smooth admissible tests; it deliberately does not claim an unproved smoothing of
the copula density that preserves the exact marginals and energy estimate.

So `conj:a3` is false for a generic “posterior whose coordinates have polynomial tails.” It needs
product structure, a quantitative dependence assumption, or a specified two-scale theorem.

A second formal problem occurs if `pi` is the joint coefficient/scale posterior: the displayed
energy differentiates only with respect to `theta`. Any nonconstant `f(lambda,tau)` then has
positive variance and zero right-hand side.

## 7. Proved horseshoe corrections

### 7.1 Exact density and hierarchy

The standard hierarchy is

`theta | lambda,tau ~ N(0,tau^2 lambda^2)`, `lambda ~ C+(0,1)`.

The pre-audit manuscript wrote `lambda|tau ~ C+(0,tau)` while also retaining `tau` in the
conditional Gaussian, double-counting the scale; this is now corrected. Direct integration (also displayed in the
appendix of [Carvalho--Polson--Scott (2010)](https://doi.org/10.1093/biomet/asq017)) gives

```
h_tau(x) = 1/[pi sqrt(2pi) tau] exp(a) E1(a),
a = x^2/(2 tau^2).
```

Thus the density has an exact special-function form. Its origin and tail expansions are

```
h_tau(x) ~ [pi sqrt(2pi) tau]^-1[-gamma-log(x^2/(2tau^2))], x -> 0,
h_tau(x) ~ 2 tau/[pi sqrt(2pi) x^2],                         |x| -> infinity.
```

The historical `finum` law `p proportional log(1+tau^2/x^2)` has the right two asymptotic shapes
but is only a proxy.

### 7.2 Exact scale covariance

Because `h_tau(x)=tau^-1 h_1(x/tau)`, substitution `x=tau y` proves

```
Var_{h_tau}(f)
 <= C int (tau^2+x^2)|f'(x)|^2 h_tau(x)dx
```

if and only if the corresponding `tau=1` inequality holds with the same `C`. The same
substitution in Hardy's functional proves `B_HS(tau)=B_HS(1)`. Hence the open target cannot be a
“sharp rate in tau”: the rate is exactly constant.

### 7.3 The Hardy tail convention

For a symmetric law Hardy uses `P(X>=r)`, not `P(|X|>=r)`. If
`B_abs= sup P(|X|>=r) I(r)=2B_+`, the theorem reads

`B_abs/2 <= C_opt <= 2 B_abs`,

not `B_abs <= C_opt <= 4B_abs`. The pre-audit manuscript mixed these conventions; the integrated
version now uses the one-sided tail consistently.

### 7.4 A sharper horseshoe target

The intrinsic coordinate `y=asinh(x/tau)` turns the weighted problem into an ordinary PI whose
density has two-sided exponential tail `q(y) asymp exp(-|y|)`. The tail approximate-eigenfunction
calculation of Section 2 proves

`C_HS >= 4`.

The exact remaining question is whether a bulk eigenvalue lies below the tail threshold `1/4`.
The crisp conjecture is:

> **Conjecture:** for the standard horseshoe marginal and weight `tau^2+x^2`, `C_HS=4`.

This is much sharper than “close a factor-four gap,” and is scale-free.

## 8. Proved hierarchical-prior lemma in the correct metric

There is a useful solved result before adding data. Let

`theta_j=exp(u+v_j)z_j`,

where the `z_j` are independent standard Gaussians and `u,v_j` are independent log-half-Cauchy
variables. A log-half-Cauchy has density `1/(pi cosh u)`. It is the `asinh` image of a standard
Cauchy, so Huguet's `beta=1` result gives its exact classical Poincaré constant `4`.

The base product law of `(z,u,v)` therefore has constant `4`. For a smooth function in centered
coordinates, the chain rule gives

```
partial_{z_j} F = exp(u+v_j) partial_{theta_j}f,
partial_{v_j} F = partial_{v_j}f + theta_j partial_{theta_j}f,
partial_u F     = partial_u f + sum_j theta_j partial_{theta_j}f.
```

Tensorization proves, with optimal constant `4`, the joint prior inequality with energy

```
sum_j exp(2u+2v_j)|partial_{theta_j}f|^2
+ sum_j |partial_{v_j}f+theta_j partial_{theta_j}f|^2
+ |partial_u f+sum_j theta_j partial_{theta_j}f|^2.
```

This exposes why diagonal coefficient weights are insufficient: cross terms are the pullback of
the product geometry. For a likelihood ratio bounded between positive constants, Holley--Stroock
transfers this inequality with factor `exp(osc(log L))`. Ordinary logistic/Gaussian likelihoods
generally do not have finite log-oscillation, and coupled or multimodal posteriors remain the real
frontier.

## 9. Numerical diagnostics only

The old stored values differed between `tau=.5` and `tau=1` because `x_max=400` and the pole
cutoff `1e-6` were absolute. Re-running the proxy on the scale-covariant grid
`[-400 tau,400 tau]` gives identically, up to roundoff,

`B_grid=0.9065112879`, `C_FEM=2.4458755664`

for `tau=.25,.5,1,2,4`.

For the true exponential-integral density, adaptive one-sided quadrature (including the infinite
tail) gave

`B_HS(1) approximately 1.01244403028`, attained near `x=11.3827`.

The finite-domain spectral solve is severely downward biased. In the intrinsic `asinh`
coordinate, the FEM sequence was

| half-width `Y` | 10 | 20 | 40 | 80 | 120 |
|---:|---:|---:|---:|---:|---:|
| `C_FEM(Y)` | 3.1948 | 3.7168 | 3.9158 | 3.9772 | 3.9897 |

This is directional support for `C_HS=4`, not a proof and not `numerical-strong` evidence.

The A3 target code was changed to the exact density, a standardized grid and relative pole
cutoff, with a focused scale-covariance regression. No new run artifact was created.

## 10. Recommended frontier

1. Correct the Huguet citation and record the full `(d,nu,Sigma)` calibration table.
2. Replace the broad conjecture by the product Hardy proof draft (then certify it) plus an
   explicitly hypothesis-bearing dependent theorem.
3. Attack the sharp one-dimensional statement `C_HS=4` by excluding sub-threshold eigenvalues in
   the `asinh` coordinate.
4. State regular-variation results as “tail floor plus bulk Hardy control,” not tail-index-only
   constants.
5. Treat weak-PI dimension dependence explicitly.
6. Submit the exact non-centered hierarchical-prior pullback lemma for independent certification;
   reserve “posterior” for a theorem with a stated likelihood perturbation/dependence contract.

## 11. Later certification outcome

A subsequent same-day proof cycle closed two items that were still prospective in this audit.
The independent `root/cross_review` agent found no substantive defect in the sharp horseshoe
argument, including the logarithmic-pole form closure and the direct even-sector trace shift, and
also verified the abstract block-Gibbs/HGR theorem developed in the follow-up note. Standalone
agent-reviewed dossiers now live at `solutions/prop-a3-horseshoe.tex` and
`solutions/thm-a3-block-gibbs.tex`; the review is persisted at
[`2026-08-21-a3-independent-agent-audit.md`](../reviews/2026-08-21-a3-independent-agent-audit.md).
This does not retroactively promote the product, hierarchical-prior, fixed-marginal, or
bounded-likelihood drafts. The recorded review level is independent agent; no human or Lean check
is claimed.

## 12. 2026-08-22 fixed-marginal review update

A later independent audit certified the fixed-Cauchy-marginal counterexample separately; see
[`2026-08-22-a3-marginals-independent-audit.md`](../reviews/2026-08-22-a3-marginals-independent-audit.md)
and `solutions/obs-marginals-not-joint.tex`. This does not change the historical scope of the
2026-08-21 A3 review or promote the product, hierarchical-prior, or bounded-likelihood drafts.
