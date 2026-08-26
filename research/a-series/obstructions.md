# A-series obstructions

These cross-target fences constrain admissible statements through ledger `bounded_by` edges.
Each heading names a ledger node with `kind: obstruction`; the ledger owns its logical status
and manuscript source. This file states only the operational consequence.

## `obs:flat-direction` — saturating links lose remote curvature

**Source:** `prop:flat-prior-nonintegrable`.
**Applies to:** A1, A3, A4.

For logistic and other saturating links, likelihood curvature can vanish in remote predictor
directions. The one-observation family
$\pi_a(d\theta)\propto e^{-\theta^2/(2\sigma^2)}\operatorname{sigmoid}(a\theta)d\theta$
rules out a universal constant-times inverse-mode-Hessian bound. A valid posterior-scale result
must add tail control, a stronger model hypothesis, or a different data-informed statistic.

## `obs:gaussian-tail-rigidity` — global logistic LSI and $T_2$ stay at prior scale

**Source:** `prop:a2-logistic-global`.
**Applies to:** A1, A2, A4.

For a finite binary-logistic likelihood with Gaussian prior covariance $\Sigma_0$,
$C_{\mathrm{LS}}(\pi)=C_{\mathrm{TCI}}(\pi)=\lambda_{\max}(\Sigma_0)$. Fisher-scale entropy or
transport claims therefore require localization, restriction, shrinking priors, or stronger
tail growth. The Poincaré constant is not ruled out from improving.

## `obs:heavy-tail-no-classical` — classical inequalities fail for heavy tails

**Source:** `thm:heavy-tail-no-lsi`.
**Applies to:** A3, A4, A5.

Polynomial or merely exponential tails do not support classical LSI or $T_2$; sufficiently heavy
tails also fail classical Poincaré. Use a weighted or weak inequality, or prove an explicit
model-specific tail regularization. For the Neal funnel, incomplete noncentring has infinite
Euclidean $C_P$ unless the likelihood supplies such regularization.

## `obs:marginals-not-joint` — marginal constants do not control dependence

**Source:** `prop:a3-marginals-not-joint`.
**Applies to:** A3.

Fixed one-dimensional marginals can coexist with an arbitrarily severe joint bottleneck.
Hierarchical results must therefore include a quantitative dependence contract. Their Dirichlet
form must also include scale derivatives and the pullback cross terms created by noncentring.

## `obs:tv-insufficient` — total variation does not transfer constants

**Source:** `warn:a2-tv-fails`.
**Applies to:** A2.

Total-variation convergence to a Gaussian does not control functional-inequality constants.
Vanishing remote contamination can preserve TV convergence while making $C_P$ diverge. A BvM
transfer theorem needs spectral stability, tail control, or another quantitatively stronger
comparison.

## `obs:symmetry-vs-physical` — quotienting removes only symmetry modes

**Source:** `prop:a5-ratio`.
**Applies to:** A2, A4, A5.

A quotient strictly improves $C_P$ exactly when
$\lambda_{\mathrm{noninv}}<\lambda_{\mathrm{inv}}$. Physical invariant slow modes survive,
and equality gives no strict improvement. Multimodal claims must compare the invariant and
non-invariant spectral blocks; one arbitrary first eigenfunction is insufficient. For multiple
wells, the relevant barrier is the worst-cut connectivity height, not the smallest pairwise
transition height.

## `obs:restricted-not-finite` — restricted transport may still be infinite

**Source:** `warn:a4-heavytail`.
**Applies to:** A3, A4.

A variational restriction or KL cutoff does not by itself make a $W_2$ transport constant finite.
For $\pi\propto e^{-|x|^p}$ with $1\le p<2$, Gaussian translations satisfy
$W_2^2/\mathrm{KL}\asymp |m|^{2-p}\to\infty$. A finite certificate must state a coercive family,
bounded sublevel, quadratic-exponential target tail, or modified cost.
