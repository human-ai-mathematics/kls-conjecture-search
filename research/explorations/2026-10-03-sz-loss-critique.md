---
---

# Structured recovery: sharp algebra and realizable calibrations

## Question examined

Independent early critique, starting from the `refute` lens, for
`ap:sz-recovery-probe`. Does sharp two-block recovery obstruct improving the
factor four in `thm:sz-iterated-curvature` when the tensors come from the
first-eigenfunction construction of `thm:sz-curvature-comparison`?

There was no stabilized structured inequality at the start of this pass. The
two concrete statements attacked, and their exact negations, are therefore
kept separate from any later candidate:

1. For every integer $l\ge2$ and every
   $S\in\mathbb R^2\otimes\operatorname{Sym}^l(\mathbb R^2)$,
   $\|\mathsf P_2S\|^2> (l-1)\|S\|^2/(2l)$ whenever $S\ne0$.
   Its negation is: there exist $l\ge2$ and nonzero such $S$ with the
   reverse weak inequality. This tests strict algebraic improvement only.
2. For every centered regular product law on $\mathbb R^2$ and every centered
   $F\in\operatorname{Dom}(H^{1/2})$, $Q_1DF$ is symmetric in its two slots.
   Its negation is: there exist such a law and $F$ for which $Q_1DF$ is
   not symmetric. This is the broad gradient-range shortcut proposed by
   the mining agent, not a first-eigenfunction claim.

The outcomes below are exact algebraic witnesses and analytic calibrations,
not certification and not a refutation of an eigenfunction-prefix estimate.

## What we learned

*Established, not certified: generic recovery is sharp already at one
polynomial slot.* Let $v_0=e_2\otimes e_1^{\otimes l}$, and let $v_a$, for
$1\le a\le l$, have $e_2$ in derivative slot $a$, with $e_1$ in every
other slot. These are orthonormal. Set

$$
S=v_0-\frac1l\sum_{a=1}^lv_a.
$$

This tensor is symmetric in the derivative slots. If $\tau$ interchanges the
polynomial slot with the first derivative slot, then

$$
\|S\|^2=\frac{l+1}{l},\qquad
\langle S,\tau S\rangle=-\frac{l+1}{l^2},\qquad
\frac{\|\mathsf P_2S\|^2}{\|S\|^2}=\frac{l-1}{2l}.
$$

Here $\mathsf P_2=(I+\tau)/2$. The last expression is exactly the certified
two-block coefficient for $(s,q)=(1,2)$. Also the full symmetrization of $S$
vanishes, since its coefficients sum to zero. This witnesses the first
negation. No claim is made that $S$ arises as $Q_1u^J$ for a first eigenfunction.

*Established, not certified: products miss this obstruction entirely.*
Let $\nu=\bigotimes_{i=1}^n\nu_i$ be a centered regular product law. Write
$H=\sum_iH_i$ on its product spectral basis. A first positive eigenfunction
has the form $F_0=\sum_if_i(x_i)$, with $f_i=0$ unless the first eigenvalue
of $H_i$ equals that of $H$. Indeed any product eigenfunction with two
positive-energy factors has energy strictly greater than the smallest
positive one-coordinate eigenvalue.

Inverse spectral powers preserve each one-coordinate centered subspace.
Differentiation adds only that coordinate's index. Centering and the scalar
normalization of the entire family preserve this property. Consequently
every nonvanishing generated family has the form

$$
u^J(x)=\sum_i g_{i,J}(x_i)e_i^{\otimes(J+1)}.
$$

Product Appell tensors factor across coordinates. In their inner product
against $g_{i,J}(x_i)$, any positive polynomial degree on another coordinate
has zero expectation. It follows that

$$
Q_ku^J=\sum_i t_{i,k,J}e_i^{\otimes(k+J+1)}.
$$

Thus all these tensors are fully symmetric, including across polynomial
and derivative slots. Their two-block recovery constant is one whenever
the tensor is nonzero. Orthogonal rotations preserve this conclusion.
For a Gaussian the first eigenfunction is linear, so its first centered
gradient successor is already zero.

Regular product approximants to products of centered exponentials have
the same symmetry, independently of how their one-dimensional spectra
change under approximation. The exponential boundary itself does not
satisfy the regular hypotheses and supplies no inverse-operator prefix.
These facts explain why neither product nor Gaussian tests can establish
realizability of the generic sharp tensor.

*Established, not certified: the mining agent's centered-gradient
counterexample survives independent calculation.* Choose a smooth, even,
non-Gaussian regular one-dimensional law $\rho=e^{-W}dx$, with variance
$\sigma^2$, and put $J=\mathbb E W''=\mathbb E(W')^2$.
Integration by parts gives $\mathbb E[xW']=1$; Cauchy--Schwarz gives
$\sigma^2J>1$, with equality forcing $W'$ to be linear and hence the law
to be Gaussian. For example take
$W(x)=x^2/2+\delta\cos x+\text{constant}$, $0<\delta<1$.
Rescaling permits variance at most one while preserving regularity and
strictness. Set

$$
c=\frac{1+\sigma^2J}{2\sigma^2},\qquad
g=W'-cx,\qquad h(x_1,x_2)=g(x_1)x_2.
$$

For $\rho\otimes\rho$, $\mathbb E\nabla h=0$ by parity and

$$
Q_1\nabla h=
\begin{pmatrix}
0&(1-\sigma^2J)/2\\
(\sigma^2J-1)/2&0
\end{pmatrix}.
$$

The entries follow from $\mathbb E[xg]=1-c\sigma^2$ and
$\mathbb E[g']=J-c$. For the displayed potential, $h$ and its derivatives
have polynomial growth and $Hh\in L^2$, so $h\in\operatorname{Dom}(H)$.
The centered form-domain function $F=H^{1/2}h$ satisfies
$DF=P_+\nabla h=\nabla h$. Hence $Q_1DF$ is nonzero and skew-symmetric.
This witnesses the second negation and pinpoints what fails when the
first-eigenfunction condition is replaced by mere membership in the range
of a centered gradient.

There are **two applicability blockers**: $F$ is not asserted to be a first
eigenfunction, and this tensor has only one derivative slot. The two-block
lemma at $q=2$ requires at least two derivative slots, while its dyadic
application uses $l=Lk$ with $L\ge3$. Thus this witness does not contradict
even the admissible long-block lemma for arbitrary starting functions.

*Established, not certified: optimizing the multiplier leaves the two
threshold obstructions.* The comparison demands
$R\ge2^{40}\varepsilon^{-2}$; the sharp coefficient step demands
$\Gamma_r\ge Kr^2$. With $\varepsilon=r^{-2}$ and
$R=(1+r^{-2})\Gamma_r$, a bounded sequence $\Gamma_r$ cannot meet either
condition for arbitrarily large $r$. This is the existing audit obstruction
in `2026-10-03-song-zhang-audit-targets.md`, applied without changing its
quantifiers. A better recovery inequality alone does not discharge these
premises. The certified equivalence
`prop:sz-exponential-coefficients-equivalence` likewise forbids presenting
a universal exponential coefficient bound as weaker than KLS.

## What resists

The generic sharp tensor has not been realized by the specified
first-eigenfunction iteration. Product regular laws exclude it, while the
centered-gradient witness removes essential hypotheses. No break was found
in the narrower structured setting; no positive margin or validity claim
is inferred from these calibrations.

Both engaged Song--Zhang nodes have no `bounded_by` edges. The substantive
fences are the brief's regular-class restriction, its threshold audit, and
its separation of polynomial bounds from CMH and occupation antecedents.
All are respected here. No claim about another sufficient-condition route
or a new `depends_on` edge is proposed.

## Proposed next step

First freeze a structured inequality with all of its prefix conditions and
defect weights. Then distinguish two tests. For generated symmetry alone,
one small genuinely coupled regular family is

$$
W_\delta(x)=\frac{x_1^2+2x_2^2}{2}
 +\delta\cos(x_1+x_2)+\text{constant},\qquad |\delta|<1/4.
$$

Its Hessian is bounded between positive scalar multiples of the identity;
a scalar spatial contraction enforces covariance at most the identity.
At $\delta=0$ the first eigenvalue is simple. Study the continuing first
eigenfunction and, for $k=1,L=3$, the earliest long-block tensor $Q_1u^2$
together with its normalization defects $\chi_0,\chi_1$. The Gaussian
successor vanishes, so a perturbation argument must construct the leading
nonzero normalized prefix rather than differentiate a normalizer defined
at a zero family.

This test can decide whether coupling creates the forbidden tensor
components. It is **not** a test of the small-loss stopped prefix used in
the curvature comparison: at the Gaussian base point $p_0=1$, and the
first loss stays close to one under such a perturbation, whereas that
prefix requires its cumulative loss to be tiny. A witness against a
candidate carrying that condition must satisfy it separately. Do not
promote a near-Gaussian symmetry defect to such a witness.

Keep this as calibration for `ap:sz-recovery-probe`; no route closure, node
delta, or new candidate is warranted by the present calculations. The
useful next result is an exact estimate on the actual admissible prefix,
including defects, rather than a sharper estimate for arbitrary tensors.
