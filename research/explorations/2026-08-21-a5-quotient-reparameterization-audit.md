# A5 quotient and reparameterization audit: exact folding, representation tests, and condition numbers

Date: 2026-08-21

Targets: `prop:a5-ratio`, `conj:a5-metastable`, `q:a5-qbvm`, `q:a5-detect`, and
`q:a5-reparam`.

Original status: analytic exploration under the then-current human/Lean-only gate. Results marked
**Proof** below were internal proof drafts rather than ledger promotions. Conjectures and proposed
tests are explicitly labeled, and no numerical evidence status is promoted.

> **Later certification update.** This is the pre-review exploration record. The subsequent
> [A4/A5 independent-agent audit](../reviews/2026-08-21-a4-a5-independent-agent-audit.md)
> promoted `prop:a5-ratio`, `prop:a5-block-stability`, `ex:a5-gaussian-crossover`, and
> `prop:a5-partial-gaussian`; a separate
> [second-agent audit](../reviews/2026-08-21-a5-funnel-second-agent-audit.md) promoted
> `lem:a5-pi-exp-tail`, `ex:a5-neal`, and `prop:a5-partial-funnel`. Folding, the proposed
> $\mathbb Z_2$ bridge, and the metastability conjecture remain open. The original status
> language below is retained as chronology rather than as the current ledger verdict.

## Verdict

The Poincaré quotient mechanism is exact, but its operational statement needs two refinements.

1. Strict improvement occurs exactly when
   $\lambda_{\mathrm{noninv}}<\lambda_{\mathrm{inv}}$. If the gaps are equal, the first
   eigenspace may contain both representation types but the quotient constant does not improve.
   Therefore a sample diagnostic should estimate the two restricted gaps, not assign a type to
   an arbitrary “first eigenfunction.”
2. The folded Gaussian double well admits a one-line sharp upper bound omitted from the pre-audit
   target and now integrated: it is a $\sigma$-Lipschitz image of a standard Gaussian, so its quotient Poincaré,
   LSI, and $T_2$ constants are all at most $\sigma^2$, uniformly in the separation. The
   Poincaré bound tends to equality as the wells separate.

For reparameterization, minimizing a raw functional-inequality constant is ill-posed: a coordinate
dilation by $a$ multiplies every constant by $a^2$. A meaningful Euclidean algorithmic target is
scale-normalized, for example

$$
\kappa_P(\mu)=L_V C_P(\mu),
\qquad L_V=\sup_x\|\nabla^2V(x)\|_{\mathrm{op}},
$$

or the bi-Lipschitz distortion of the coordinate map. On a Gaussian this is exactly the covariance
condition number. A two-dimensional Gaussian hierarchy gives a complete finite-sample
centered/non-centered crossover: non-centering wins below unit data precision and centering wins
above it, for both $C_P$ and the scale-invariant condition number under the stated normalization.

## 1. Quotient gaps and the group projection

Let

$$
P_Gf=\frac1{|G|}\sum_{g\in G}f\circ g.
$$

Because the action preserves $\pi$ and the Dirichlet form, $P_G$ is the orthogonal projection
onto the invariant subspace in $L^2(\pi)$ and commutes with the generator. For every mean-zero
$f$, put $f_{\mathrm{inv}}=P_Gf$ and $f_\perp=(I-P_G)f$.

### Proof: exact variance and energy decomposition

Orthogonality and commutation give

$$
\mathrm{Var}_\pi(f)
=\mathrm{Var}_\pi(f_{\mathrm{inv}})+\mathrm{Var}_\pi(f_\perp),
$$

$$
\mathcal E_\pi(f)
=\mathcal E_\pi(f_{\mathrm{inv}})+\mathcal E_\pi(f_\perp).       \tag{1}
$$

With the restricted gaps interpreted in $[0,\infty]$ and reciprocal constants in the extended
sense, consequently

$$
C_P(\pi/G)=\lambda_{\mathrm{inv}}^{-1},
\qquad
C_P(\pi)=\min(\lambda_{\mathrm{inv}},\lambda_{\mathrm{noninv}})^{-1},
$$

and, whenever $0<\lambda_{\mathrm{inv}}<\infty$, the improvement ratio is well-defined:

$$
\frac{C_P(\pi)}{C_P(\pi/G)}
=\frac{\lambda_{\mathrm{inv}}}
       {\min(\lambda_{\mathrm{inv}},\lambda_{\mathrm{noninv}})}.
$$

In particular,

$$
\boxed{C_P(\pi/G)<C_P(\pi)
\iff\lambda_{\mathrm{noninv}}<\lambda_{\mathrm{inv}}.}          \tag{2}
$$

If equality holds between the restricted gaps, invariant and non-invariant minimizing directions
may coexist but the quotient does not improve the constant. This is the precise version of
“quotient helps iff the slow mode is non-invariant.”

If $\lambda_{\mathrm{inv}}=0$, both the quotient constant and the raw constant are infinite and a
formal ratio would be $\infty/\infty$; no ratio is asserted. Empty spectral sectors are assigned
gap $+\infty$.

### Consequence for detection from samples

If the first eigenvalue is simple, commutation implies its eigenfunction is either invariant or
has zero group average. If the eigenvalue is degenerate, an arbitrary fitted eigenfunction can
mix invariant and non-invariant vectors in the same eigenspace; its representation “type” is not
well-defined.

For any learned test function, (1) provides two sound Rayleigh witnesses,

$$
R_{\mathrm{inv}}(f)
=\frac{\mathrm{Var}(P_Gf)}{\mathcal E(P_Gf)},
\qquad
R_{\mathrm{noninv}}(f)
=\frac{\mathrm{Var}((I-P_G)f)}{\mathcal E((I-P_G)f)}.            \tag{3}
$$

They are lower bounds for the two restricted Poincaré constants. Lower bounds alone do not
certify which restricted gap is smaller. A rigorous classifier additionally needs spectral
residual bounds/two-sided eigenvalue estimates, or an isolated-gap assumption. A practical
Ritz--Galerkin version should use a basis closed under the group action, split its generalized
eigenproblem by $P_G$, and report both restricted spectra and their uncertainty.

## 2. The folded Gaussian well has a sharp quotient bound

Let

$$
\mu_a=\tfrac12N(-a,\sigma^2)+\tfrac12N(a,\sigma^2),
\qquad \bar\mu_a=|\cdot|_\#\mu_a.
$$

### Proof

If $Z\sim N(0,1)$, symmetry gives

$$
\bar\mu_a=\operatorname{Law}|a+\sigma Z|.
$$

The map $T(z)=|a+\sigma z|$ is globally $\sigma$-Lipschitz. The Lipschitz transport lemma
therefore yields the uniform bounds

$$
\boxed{
C_P(\bar\mu_a)\le\sigma^2,
\quad C_{\mathrm{LS}}(\bar\mu_a)\le\sigma^2,
\quad C_{\mathrm{TCI}}(\bar\mu_a)\le\sigma^2.}                    \tag{4}
$$

The linear test on the quotient coordinate gives
$C_P(\bar\mu_a)\ge\mathrm{Var}|a+\sigma Z|$. Here

$$
\mathbb E|a+\sigma Z|
=\sigma\sqrt{\frac2\pi}e^{-a^2/(2\sigma^2)}
+a\left(1-2\Phi(-a/\sigma)\right),
$$

and $\mathbb E|a+\sigma Z|^2=a^2+\sigma^2$. Hence

$$
\mathrm{Var}|a+\sigma Z|\longrightarrow\sigma^2
\quad\text{as }a/\sigma\to\infty.
$$

Combining with (4) proves

$$
\boxed{C_P(\bar\mu_a)\to\sigma^2.}                              \tag{5}
$$

Thus the `stress-folded-well` quotient claim is analytic, uniform, and asymptotically sharp; its
finite-element values near $1$ for $a=2,3$ and $\sigma=1$ are only a consistency check.

The raw law also has a polynomial prefactor that must not be dropped. Its density is

$$
p_a(x)=\frac{1}{\sqrt{2\pi}\sigma}
e^{-(x^2+a^2)/(2\sigma^2)}\cosh(ax/\sigma^2).
$$

Applying the one-dimensional Hardy criterion at median zero and rescaling the bottleneck layer
$x=(\sigma^2/a)s$ shows, after splitting off the two Gaussian tails,

$$
B_+(\mu_a)=\Theta\!\left(\frac{\sigma^3}{a}
e^{a^2/(2\sigma^2)}\right).
$$

Since $B_+\le C_P\le4B_+$,

$$
C_P(\mu_a)=\Theta\!\left(\frac{\sigma^3}{a}
e^{a^2/(2\sigma^2)}\right),
\qquad
\log\!\left(\frac{C_P(\mu_a)}{\sigma^2}\right)
=\frac{a^2}{2\sigma^2}+O(\log(a/\sigma)).                     \tag{5a}
$$

Thus the exponential rate is correct, but a uniform lower bound with no polynomial prefactor is
not.

## 3. Making the metastable conjecture well-posed

The pre-audit form

$$
C_P(\pi_\Theta)\asymp e^{n\Gamma_{\rm conn}}\operatorname{poly}(n)
$$

mixes the robust logarithmic barrier with an unspecified prefactor. A first tractable theorem is
the logarithmic asymptotic

$$
\boxed{\frac1n\log C_P(\pi_\Theta)\longrightarrow\Gamma_{\rm conn}
\quad\text{in }\mathbb P_{\theta_*}\text{-probability},}         \tag{6}
$$

for fixed $K$ and a free $S_K$-orbit $\mathcal W$ of nondegenerate minima. Writing $\ell$ for the
population negative log likelihood, let $H(w,w')$ be the pairwise communication height. The
spectral exponent is the orbit-connectivity height

$$
\Gamma_{\rm conn}
=\inf\{h:(\mathcal W,\{ww':H(w,w')\le h\})\text{ is connected}\}
=\max_{\varnothing\ne A\subsetneq\mathcal W}
\min_{w\in A,w'\notin A}H(w,w').
$$

This corrects the earlier easiest-pair formula: the minimum pair height is sufficient only when
the minimum-height orbit graph is already connected. It is automatic for two wells but can
underestimate the slowest cut for a larger orbit.

The theorem must also assume exponentially quantitative uniform empirical-risk control near the
relevant paths, capacity bounds, negligible tail escape, and negligible mass near collision
strata. Polynomial/Eyring--Kramers prefactors
should be a second target. If $K$ grows with $n$, orbit entropy and the number of saddles enter
and (6) needs a different statement.

The quotient line also needs stronger hypotheses than ordinary BvM convergence. Total variation
does not control Poincaré constants (`obs:tv-insufficient`). A viable proof package should include:

1. a fixed, identifiable orbit whose stabilizer is trivial and whose distance from collision
   strata is positive;
2. a fundamental chamber with the quotient/reflection Dirichlet form;
3. an $o_P(1)$ oscillation comparison of the rescaled quotient density with its Fisher Gaussian
   on the main region;
4. a tail/Lyapunov or capacity estimate excluding remote invariant bottlenecks; and
5. a quantitative “no physical multimodality” hypothesis, equivalently an invariant gap of order
   $n$ after rescaling.

Under these conditions the local quotient map is an isometry near the orbit, so the Fisher
matrix is the ordinary identifiable Fisher matrix. The open work is global control of the chamber,
not the local covariance calculation.

**Conjecture.** Establish (6) first in a
finite-dimensional smooth multiwell model with an exact
finite group action and no singular mass. Separately prove
$nC_P(\pi_{\Theta/G})\to\lambda_{\max}(I^{-1})$ under oscillation-plus-tail hypotheses. Combining
the two through the pre-existing ratio identity then gives the desired raw/quotient separation
without hiding assumptions in `poly(n)`.

## 4. Bi-Lipschitz comparison and the scale defect

Let $T$ be a bijection with $T_\#\nu=\mu$, $\mathrm{Lip}(T)=L$, and
$\mathrm{Lip}(T^{-1})=M$. Applying the Lipschitz transport lemma in both directions proves, for
each $C\in\{C_P,C_{\mathrm{LS}},C_{\mathrm{TCI}}\}$,

$$
\boxed{M^{-2}C(\nu)\le C(\mu)\le L^2C(\nu).}                    \tag{7}
$$

The scale-free uncertainty in this comparison is governed by
$L^2M^2$, the squared bi-Lipschitz condition number.

### Proof: minimizing a raw constant is ill-posed

For the dilation $D_a(x)=ax$, both bounds in (7) coincide, so

$$
C(D_a{}_\#\mu)=a^2C(\mu).                                       \tag{8}
$$

Taking $a\downarrow0$ makes the displayed constant arbitrarily small without changing the
abstract law or an intrinsic sampling problem. Any optimization over reparameterizations must
fix a physical metric/normalization or use a scale-invariant objective.

For a smooth target $d\mu\propto e^{-V}dx$ with globally Lipschitz gradient, define

$$
\kappa_P(\mu):=L_VC_P(\mu),
\qquad
L_V:=\sup_x\|\nabla^2V(x)\|_{\mathrm{op}}.                     \tag{9}
$$

Under a scalar dilation, $L_V$ is divided by $a^2$ while $C_P$ is multiplied by $a^2$, so
$\kappa_P$ is invariant. It is the natural Poincaré analogue of the smoothness/strong-convexity
condition number controlling Euclidean Langevin discretizations.

For $N(0,\Sigma)$,

$$
\kappa_P
=\lambda_{\max}(\Sigma)\lambda_{\max}(\Sigma^{-1})
=\operatorname{cond}(\Sigma).                                  \tag{10}
$$

After an invertible affine map $A$, this becomes
$\operatorname{cond}(A\Sigma A^\top)$, whose minimum is $1$, attained exactly by whitening up to
an orthogonal map and scalar dilation. This is a fully solved calibration problem for any proposed
reparameterization objective.

## 5. Exact finite-data centered/non-centered phase diagram

Consider the normalized Gaussian hierarchy

$$
u\sim N(0,1),\qquad z\sim N(0,1),\qquad \theta=u+z,
\qquad y\mid\theta\sim N(\theta,r^{-1}),\qquad r\ge0.
$$

The observation value changes only the posterior mean. In centered coordinates $(u,\theta)$ and
non-centered coordinates $(u,z)$, the posterior precision matrices are

$$
H_{\mathrm c}(r)=
\begin{pmatrix}2&-1\\-1&1+r\end{pmatrix},
\qquad
H_{\mathrm{nc}}(r)=
\begin{pmatrix}1+r&r\\r&1+r\end{pmatrix}.                       \tag{11}
$$

### Proof: exact constants and crossover

For a Gaussian with precision $H$, $C_P=1/\lambda_{\min}(H)$ and
$\kappa_P=\operatorname{cond}(H)$. The non-centered eigenvalues are $1$ and $1+2r$, so

$$
C_P^{\mathrm{nc}}=1,
\qquad
\kappa_P^{\mathrm{nc}}=1+2r.                                  \tag{12}
$$

The centered eigenvalues are

$$
\lambda_\pm(r)=
\frac{3+r\pm\sqrt{(1-r)^2+4}}2,                                \tag{13}
$$

so $C_P^{\mathrm c}=1/\lambda_-$ and
$\kappa_P^{\mathrm c}=\lambda_+/\lambda_-$. Direct algebra gives

$$
\begin{array}{c|c|c}
&0\le r<1&r>1\\ \hline
C_P& C_P^{\mathrm{nc}}<C_P^{\mathrm c}
    & C_P^{\mathrm c}<C_P^{\mathrm{nc}}\\
\kappa_P&\kappa_P^{\mathrm{nc}}<\kappa_P^{\mathrm c}
    &\kappa_P^{\mathrm c}<\kappa_P^{\mathrm{nc}}.
\end{array}                                                     \tag{14}
$$

Both pairs are equal at $r=1$. Thus non-centering wins in the weak-data regime and centering wins
in the strong-data regime in an exact finite-sample model. The threshold is meaningful because
the prior coordinates were normalized to unit scale; equation (8) explains why that normalization
must be stated.

This model is the clean entry subtarget for `q:a5-reparam`. General variances give explicit
$2\times2$ matrices, and partial non-centering becomes a one-parameter matrix condition-number
optimization before tackling nonlinear funnels.

## 6. Neal-funnel audit

For the canonical map

$$
T(u,z)=(u,e^uz),
$$

neither $T$ nor $T^{-1}(u,\theta)=(u,e^{-u}\theta)$ is globally Lipschitz: both Jacobians are
unbounded. The historical `stress-neal-funnel` note calls this “one-way Lipschitz,” which is
incorrect. The Lipschitz lemma supplies no global comparison in either direction.

The analytic conclusion $C_P^{\mathrm{cen}}=\infty$ is nevertheless valid. The centered
coordinate $\theta=e^u z$ is a Euclidean 1-Lipschitz observable of $(u,\theta)$ and has no finite
exponential moment, whereas a finite Poincaré inequality forces some exponential integrability
for centered Lipschitz observables. The non-centered product Gaussian has
$C_P=\max\{s^2,1\}$.

The dirty historical run only records the finite linear-test lower bound

$$
C_P^{\mathrm{cen}}\ge\mathrm{Var}(\theta)=e^{2s^2}
$$

at $s=1.5,2$. That lower bound refutes the particular finite comparison tested there but does not
numerically establish infinity for either fixed $s$; infinity comes from the analytic tail
argument. The historical record is also tagged with `obs:symmetry-vs-physical`, although its
mechanism is reparameterization/tail geometry rather than group symmetry; the current diagnostic
uses `obs:heavy-tail-no-classical` instead.

## 7. Tractable next targets

### Analytic reductions/calibrations (historical pre-review list)

1. Use the strict gap condition (2), including the equality/degeneracy case.
2. Use the now-integrated analytic folded-well bound (4)--(5) as the numerical calibration.
3. Replace raw-constant optimization by a fixed normalization, $\kappa_P$, or bi-Lipschitz
   distortion.
4. Use the Gaussian hierarchy (11)--(14) as the exact centered/non-centered calibration.

### Conjectures

1. Prove the raw log-barrier asymptotic (6) before attempting an Eyring--Kramers prefactor.
2. Prove quotient BvM constants under oscillation comparison plus global tail/capacity control,
   not TV convergence alone.
3. For nonlinear partial non-centering, combine a bi-Lipschitz comparison on a high-probability
   regular region with an explicit Lyapunov/tail penalty. A high-probability Lipschitz statement
   alone cannot control a global functional-inequality constant.

### Proposed tests

1. Fit invariant and non-invariant Ritz blocks separately; report restricted eigenvalues,
   residuals, degeneracy, and uncertainty rather than a binary label for one learned eigenvector.
2. Extend the exact Gaussian hierarchy to unequal prior/noise scales and optimize partial
   non-centering analytically; any numerical method must reproduce the $r=1$ normalized crossover.
3. For funnels, report both $C_P$ lower witnesses and a scale-normalized algorithmic objective.
   Separate failure of global Lipschitz comparison from failure caused by genuinely heavy-tailed
   hyperpriors.

## Validation

All displayed A5 results are analytic. The existing dirty A5 JSONL was inspected but not modified
or promoted. No new run artifact was generated.
