---
---

# Song–Zhang: audit obligations and the summable-loss question

## Question examined

Early critique, starting from the `refute` lens: what would invalidate the informal
inference that summable losses in the polynomial/curvature loop suffice for `conj:kls`?
This is an audit preparation for the literature integration, not a proof or a refutation
of the preprint. It engages `conj:kls` and the comparison with `ap:s-occupation`; no
implication to that route's occupation target is proposed. The existing brief's
distinction between dimension-dependent estimates and completion remains binding.

The informal statement under attack is: “Replacing the iteration factor 4 by 1 while
retaining a summable error proves KLS by the same argument.” Its failure means that
there is an iteration depth at which a required premise of the unchanged argument
cannot be met by the bounded sequence of constants. This is a logical applicability
test, not the quantified negation of `conj:kls`.

## What we learned

*Observed in the source.* Theorem 5.1 requires
$R\geq2^{40}\epsilon^{-2}$. Lemma 6.4 requires $\Gamma\geq Kr^2$ and initializes
degrees below $D_r=\lceil32r^2\rceil$ separately. Its main induction estimates are
uniform above this threshold. Section 6.2 uses $\epsilon=r^{-2}$ and exponential
growth of $\Gamma_r$ to satisfy both thresholds.
[Song–Zhang v1, Sections 5–6](https://arxiv.org/html/2610.01447v1#S5).

*Established, elementary applicability obstruction; not certified.* If
$\Gamma_{r+1}\leq e^{3/r^2}\Gamma_r$ for all $r\geq r_0$, then
$\Gamma_r\leq\Gamma_{r_0}\exp(3\sum_{j\geq r_0}j^{-2})=:M<\infty$.
For $r>\sqrt{M/K}$ the first threshold fails. Also
$R_r=(1+r^{-2})\Gamma_r\leq2M$ cannot meet
$R_r\geq2^{40}r^4$ for every $r$. Increasing a finite initial constant does not
repair either obstruction. This does **not** show that a sharper theorem is false;
it shows that the proposed substitution does not instantiate the existing theorem.

Replacing 4 by any fixed $c>1$ instead leaves the upper envelope
$C c^r$. Taking depths tending to infinity therefore still gives an unbounded
estimate; it does not imply that the actual Poincaré constants diverge. A genuinely
bounded-product argument must include all initialization and admissibility costs,
not merely the displayed multiplier. Enforcing a polynomial lower threshold by
inflating the constants at each depth reintroduces an unbounded estimate.

*Established, boundary calculations; not certified.* Two one-dimensional tests can
be reconstructed independently of the preprint. Write
$c_d=\sqrt{\operatorname{Var}(A_d(X))}/d!$, with
$e^{tx}/\mathbb E e^{tX}=\sum A_d(x)t^d/d!$.
For $X\sim N(0,1)$, the product of the generating functions has expectation
$e^{ts}$, so coefficient comparison gives
$\mathbb E[A_d(X)^2]=d!$ and $c_d=1/\sqrt{d!}$.
For $X=Y-1$ with $Y$ exponential of rate one, the generating function is
$(1-t)e^{t(x+1)}$. Hence $A_d(X)=Y^d-dY^{d-1}$ for $d\geq1$.
Since $\mathbb E Y^m=m!$, its mean is zero and

$$
\mathbb E A_d(X)^2=(2d)!-2d(2d-1)!+d^2(2d-2)!
=d^2(2d-2)!.
$$

Consequently $c_d=\sqrt{(2d-2)!}/(d-1)!$. In particular $c_2=\sqrt2$,
whereas the Gaussian value is $1/\sqrt2$. These computations forbid importing
Gaussian orthogonality or Gaussian coefficient growth into a universal argument.
The exponential is a nonsmooth boundary calibration, not a regular measure to
which an inverse-operator construction may be applied without approximation.
No numerical experiment is used.

## What resists

*Audit obligations, not diagnosed defects.* For Lemma 5.4, independently reconstruct
the domain/core argument and the adjacent-swap propagation before checking the
dyadic bookkeeping. Freeze the scalar normalizer of the whole family when
permuting its slots. Test the first degrees $2$ and $4$, the earliest allowed
generation, and a zero successor. Prove the lag convolution estimate with the
whole overlapping family retained; charging every interval separately risks an
extra depth factor. Check the stopping argument through its possible exit rather
than assuming the local normalizer bound globally.

For Lemma 6.4, put the quantifiers in this order: choose universal constants and
an initial depth; then every depth, every admissible profile constant, every
dimension and measure, and every degree. Verify the small-degree initialization,
the large-degree estimate and their join. Moment convergence at each fixed degree
is enough for a pointwise limiting inequality if its constants are uniform; it
does not by itself give a uniform rate of convergence over degrees.

No explicit contradiction in these lemmas was obtained in this pass. The concrete
obstruction above concerns the suggested improvement, not the paper's stated
iteration. The Letwin input still needs a separate exact normalization/dependency
audit. Gaussian and exponential checks cannot replace any of those audits.

## Proposed next step

Before seeking a better multiplier, write one complete induction contract listing
its coefficient profile, degree range, regularity class, normalization and every
threshold as functions of depth and error. Ask whether a bounded profile constant
can satisfy that contract for arbitrarily large depth. The first discriminating
test is the low-degree initialization together with the small-loss comparison
threshold, not a numerical search for smaller constants.

Keep this as an audit objective until that contract is explicit. Do not register
an implication to `conj:mm-spectral-occupation`, CMH, or the trace-upgrade cluster:
the polynomial/curvature loop presently supplies none. No existing route changes
state and no new mathematical candidate is proposed here.
