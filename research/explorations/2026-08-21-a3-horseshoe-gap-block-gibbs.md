# A3 next cycle — exact horseshoe gap and dependence-bearing tensorization

**Date:** 2026-08-21

**Targets:** `prop:a3-horseshoe`, `thm:a3-block-gibbs`, `q:a3-horseshoe`,
`conj:a3-dependent`, `q:a3-hierarchical`

**Outcome:** an analytic proof draft gives the sharp horseshoe constant `C_HS=4`; a second
analytic proof draft isolates dependence through a block conditional-variance gap and identifies
that gap with `1-rho_max` for two blocks. Both remain unpromoted pending an independent repository
proof audit. No provenance-eligible numerical evidence is claimed.

> **Later certification update.** The independent audit summarized in Section 10 accepted both
> `prop:a3-horseshoe` and `thm:a3-block-gibbs`; they are now `proved` with standalone dossiers.
> The wording above records the state when this exploration was first written.

## 1. What was attempted

The previous A3 cycle reduced the one-dimensional horseshoe problem to exclusion of a bulk
eigenvalue below the intrinsic tail threshold `1/4`. The proposed route was:

1. prove a global upper bound for `H(a)=exp(a)E1(a)` with a valid remainder sign;
2. turn that bound into a drift inequality in `y=asinh(x)`;
3. use a positive half-line supersolution to exclude odd sub-threshold spectrum;
4. treat the logarithmic pole at `y=0` in the weighted form domain;
5. transfer the trace-zero bound to the even sector and use a mean-corrected tail cutoff for the
   reverse inequality.

The dependence target was also made quantitative: replace “some coupling bound” by the spectral
gap of the block-resampling Dirichlet form, and identify its exact two-block value.

## 2. Analytic proof draft: a global exponential-integral bound

For `a>0`, set

```text
H(a) = exp(a) E1(a) = int_0^infinity exp(-t)/(a+t) dt,
N(a) = a^2+5a+2,
Q(a) = a(a^2+6a+6).
```

The needed rational upper bound is

```text
H(a) < N(a)/Q(a).                                      (2.1)
```

This rational function is a left Gauss--Radau / Laplace-continued-fraction convergent, but no
quadrature error convention is needed. The following direct remainder identity fixes the sign.
Polynomial division gives, pointwise in `t`,

```text
N - Q/(a+t)
  = a(t-1) - t^2 + 6t - 4 + t(t^2-6t+6)/(a+t).       (2.2)
```

The first two groups integrate to zero against `exp(-t)dt`, because the first three exponential
moments are `1,1,2`. Moreover

```text
{exp(-t)t^3}'' = exp(-t)t(t^2-6t+6).
```

Consequently

```text
N-QH(a)
 = int_0^infinity {exp(-t)t^3}''/(a+t) dt
 = 2 int_0^infinity exp(-t)t^3/(a+t)^3 dt > 0.        (2.3)
```

Both integrations by parts are legitimate without a hidden endpoint term:

- at `t=0`, both `exp(-t)t^3` and its first derivative vanish;
- at infinity, the exponential factor makes both converge to zero;
- `(a+t)^-1` and its first two derivatives are bounded at zero for every fixed `a>0`.

This proves (2.1) globally with an explicit positive remainder.

## 3. Intrinsic drift inequality

Scale covariance reduces the problem to `tau=1`. Put

```text
x = sinh(y),  c = cosh(y),  a=x^2/2,
q(y) proportional c H(a),  W(y)=-log q(y).
```

The weighted `x`-Dirichlet form becomes the ordinary `y`-Dirichlet form. Since
`H'(a)=H(a)-1/a`, direct differentiation gives

```text
W'(y) = x c [1/(aH(a))-1] - x/c.                     (3.1)
```

Bound (2.1) implies

```text
1/(aH(a)) >= (a^2+6a+6)/(a^2+5a+2).                 (3.2)
```

With `c=sqrt(1+2a)`, the rational lower bound in (3.2) dominates the exact quantity needed in
(3.1):

```text
(a^2+6a+6)/(a^2+5a+2)
  >= 1 + c^-2 + [c(c+1)]^-1.                         (3.3)
```

The exact difference in (3.3) is

```text
[c^2(c-1)^2+5c^2+2c+1]
  / [c^2(c+1)(c^4+8c^2-1)] > 0.                     (3.4)
```

Substitution in (3.1) yields the global drift inequality

```text
W'(y) >= x/(c+1) = tanh(y/2),  y>0.                  (3.5)
```

The sampled drift diagnostic added in this cycle evaluates a closed positive lower residual
derived from (3.4); its role is regression protection only, not proof.

## 4. Barta/ground-state step and the logarithmic pole

On the positive half-line, let

```text
L f = f''-W'f',      g(y)=sinh(y/2).
```

Then

```text
-Lg/g = -1/4 + (1/2)W'(y)coth(y/2) >= 1/4.           (4.1)
```

For a compactly supported Dirichlet test `phi=gu`, expansion and one integration by parts gives
the exact ground-state identity

```text
int_0^infinity (|phi'|^2-phi^2/4)q dy
 = int_0^infinity g^2|u'|^2q dy
 + int_0^infinity (-Lg/g-1/4)phi^2q dy.              (4.2)
```

The origin is not silently treated as a smooth point. As `y downarrow 0`,

```text
H(sinh^2(y)/2) = -log(y^2/2)-gamma+o(1),
q(y) asymp log(1/y).
```

Hence both `q` and `1/q` are locally integrable. Finite energy therefore gives a trace at zero:

```text
|phi(y)-phi(0)|^2
 <= [int_0^y |phi'|^2q][int_0^y 1/q].
```

Odd functions have zero trace. For such a smooth function, `phi(y)=O(y)`, `g(y)~y/2`, and
`u(y)=phi(y)/g(y)=O(1)`. The boundary term suppressed in (4.2) is

```text
q(y)g(y)g'(y)u(y)^2 = O(y log(1/y)) -> 0.            (4.3)
```

Smooth compactly supported odd functions form a core: start from the defining full-line smooth
core and symmetrize. Thus form closure extends the inequality in (4.2) to the entire odd domain
(it need not extend the two terms on the right separately). The odd half-line spectral bottom is
at least `1/4`.

## 5. Direct even-sector reduction and the tail upper test

Repeated expansion of the integral defining `H` gives

```text
H(a)=a^-1-a^-2+O(a^-3),
q(y)=K exp(-y)[1+O(exp(-2y))],  y->infinity.          (5.1)
```

The odd argument controls the even sector without an essential-spectrum theorem or Sturm
interlacing. Let `f` be a half-line even-sector function with zero `q`-mean, and put
`h=f-f(0)`. Then `h` has Dirichlet trace and

```text
E(h)=E(f),
||h||_q^2=||f||_q^2+f(0)^2 int_0^infinity q >= ||f||_q^2.       (5.2)
```

Applying the trace-zero estimate from Section 4 to `h` proves that every mean-zero even function
also has Rayleigh quotient at least `1/4`. Parity decomposition is orthogonal for both variance
and energy, so the full gap is at least `1/4`.

For the reverse inequality, translate an increasingly wide smooth cutoff of `exp(y/2)` to
`[R,R+ell]`. Direct use of (5.1) gives Rayleigh quotient
`1/4+O(ell^-2)+O(exp(-2R))`. Subtracting its `q`-mean changes no energy and a negligible amount of
its norm. Sending `R` and then `ell` to infinity proves that the full gap is at most `1/4`.

Combining Sections 4 and 5 gives the analytic proof-draft conclusion

```text
lambda_HS=1/4,  C_HS(tau)=4 for every tau>0.          (5.4)
```

### Certification boundary

Equation (5.4) is not promoted in the ledger during this cycle. Independent review should check:

1. the polynomial identity (2.2) and both integrations by parts;
2. the algebra from (3.2) to (3.5);
3. closure of (4.2) in the singular weighted form domain;
4. the even-sector trace-shift reduction (5.2);
5. the explicit mean-corrected tail upper test.

If any of items 3--5 fails for the intended form domain, the repository statement must revert to
`C_HS>=4` plus the Hardy upper bracket until repaired.

## 6. Analytic proof draft: dependence through the block-Gibbs gap

Let `X=(X_1,...,X_m)` have joint law `pi`, and define

```text
gamma_blk(pi)
 = inf_{Var(f)>0} sum_i E Var(f|X_-i) / Var(f).       (6.1)
```

Suppose every conditional block law has a weighted Poincare inequality

```text
Var_i(g|x_-i) <= C_i E_i <A_i grad_i g,grad_i g>,    (6.2)
```

with deterministic finite `C_i`. Equations (6.1)--(6.2) immediately give

```text
Var_pi(f)
 <= [max_i C_i/gamma_blk]
    E_pi sum_i <A_i grad_i f,grad_i f>.               (6.3)
```

For a product law, Efron--Stein gives `gamma_blk>=1`, and a function of one nondegenerate block
gives equality.

### Exact two-block identity

For two blocks `X,Y`, work in `L^2_0(pi)` and let `P_X,P_Y` be the orthogonal conditional-
expectation projections. Then

```text
E Var(f|X)+E Var(f|Y)
 = <f,(2I-P_X-P_Y)f>.                                (6.4)
```

The HGR maximal correlation is the operator norm of `P_XP_Y` between the centered measurable
subspaces. The standard two-projections identity gives

```text
||P_X+P_Y|| = 1+rho_max.                              (6.5)
```

Since the sum of projections is positive, (6.4)--(6.5) imply exactly

```text
gamma_blk = 2-||P_X+P_Y|| = 1-rho_max.               (6.6)
```

This includes non-attainment by operator-norm approximation. If there is a nonconstant common
factor, `rho_max=1` and `gamma_blk=0`. The fixed-marginal copula obstruction is therefore not an
exception to (6.3): its dependence factor collapses while all marginal Hardy constants stay
fixed.

## 7. First posterior rungs

### 7.1 Bounded likelihood

Let `pi_0` be the log-noncentered horseshoe prior from the previous cycle, with pullback constant
`4`, and let `dpi_L=Z^-1 L dpi_0` with `0<m<=L<=M`. Then

```text
Var_piL(f) <= (M/Z) Var_pi0(f),
E_pi0 Gamma(f) <= (Z/m) E_piL Gamma(f),
```

so

```text
C_w(pi_L) <= 4M/m.                                   (7.1)
```

This is narrow but complete. Ordinary Gaussian and logistic likelihoods usually have `inf L=0`,
so (7.1) is a first rung rather than the final Bayesian theorem.

### 7.2 Horseshoe normal means

For

```text
y_j|theta_j ~ N(theta_j,sigma_j^2),
theta_j=exp(u+v_j)z_j,
```

integrating `z_j` gives, up to a constant,

```text
m_j(w)
 = (sigma_j^2+exp(2w))^-1/2
   exp[-y_j^2/{2(sigma_j^2+exp(2w))}],  w=u+v_j.
```

The scale posterior is

```text
sech(u) product_j sech(v_j)m_j(u+v_j).
```

Conditionally on `u`, the local blocks factorize. The next model-specific attempt should:

1. compute the one-sided Hardy quantities of `sech(v)m_j(u+v)` and determine whether their
   suprema are uniform in `u` and standardized `|y_j|/sigma_j` on a stated regime;
2. control `gamma_blk` for `u` versus the local block, or instead bound the covariance term in
   `d/du E[f|u]` by conditional PI and a score variance;
3. keep every dimension/data loss explicit;
4. switch parameterization or add a weighted scale metric if either conditional constants or the
   dependence factor degenerates.

The metric must be named. The finite prior result is Euclidean in `(z,u,v)` with log scales, or
equivalently uses the centered pullback metric with cross terms. Raw-scale noncentering
`(z,tau,lambda)` may still have infinite classical Poincare constant because `tau` is half-Cauchy.
The non-bi-Lipschitz map `tau <-> log tau` reconciles this with A5.

## 8. Numerical contract and stop/go rules

The added A3 diagnostic evaluates:

- the rational `H` upper bound against the exact special function on a finite grid;
- the explicit positive lower residual in the odd Barta inequality;
- scale covariance of the exact horseshoe density and Hardy/FEM diagnostics.

These are regression checks for analytic formulas. They do not promote (5.4). A future spectral
diagnostic should be parity-separated and use tail-matched Robin or shooting conditions; a
finite-box eigenvalue alone is not a two-sided spectral enclosure.

**Go on the horseshoe proof:** all five certification items after (5.4) survive independent
review.

**Revert:** a domain/parity gap is found that cannot be repaired.

**Refute `C_HS=4`:** only a stable eigenvalue below `1/4` with residual and two-sided enclosure is
decisive; failure of the particular supersolution would not be.

**Go on dependence:** conditional constants are uniform in a named regime and
`gamma_blk>0` is quantitatively verified.

**Narrow:** `gamma_blk` tends to zero with dimension/data; expose the loss rather than claiming a
dimension-free theorem.

**Stop:** a multimodal/capacity bottleneck is present but absent from the hypotheses.

## 9. Proposed promotions at the pre-review stage

At this stage the coordinator could, after independent certification:

- update `prop:a3-horseshoe` from the lower-bound draft to the sharp equality `C_HS=4`;
- add a ledger node such as `thm:a3-block-gibbs`, depending on conditional block inequalities and
  bounded by `obs:marginals-not-joint`;
- add a bounded-likelihood corollary under `prop:a3-hierarchical-prior`;
- promote the block-gap theorem and the raw-scale/log-scale metric distinction into shared
  knowledge.

None of those ledger or shared-knowledge edits was authorized or made in this cycle.

## 10. Certification outcome — later independent agent pass

Later on 2026-08-21, the independent `root/cross_review` agent audited exactly
`prop:a3-horseshoe` and `thm:a3-block-gibbs`. The audit checked the positive `E1` remainder,
drift algebra, singular trace/form closure, even-sector trace shift, mean-corrected tail test, the
conditional-variance tensorization, and the two-projections/HGR identity. No substantive error was
found. The persisted review is
[`2026-08-21-a3-independent-agent-audit.md`](../reviews/2026-08-21-a3-independent-agent-audit.md).
The two results were lifted into standalone dossiers:

- `solutions/prop-a3-horseshoe.tex`;
- `solutions/thm-a3-block-gibbs.tex`.

This addendum records the later outcome without rewriting the chronology above. The review level
is `checked_by: agent`, not human or Lean, and it creates no numerical evidence. Posterior use of
the block theorem still requires model-specific conditional constants and a quantitative positive
`gamma_blk`; likelihood-tilted horseshoe constants remain open beyond bounded density comparison.
