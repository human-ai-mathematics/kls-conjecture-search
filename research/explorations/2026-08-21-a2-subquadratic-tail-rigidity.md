# A2 — subquadratic Gaussian-tail rigidity and the shrinking-prior tradeoff

- **Date:** 2026-08-21
- **Nodes:** `prop:a2-subquadratic-global`, `prop:a2-logistic-global`, `q:a2-lsi`, `conj:a2`
- **Type:** analytic proof drafts plus deterministic algebraic calibration
- **Certification:** complete-on-paper arguments below remain open pending a standalone solution
  and independent repository review.

> **Later certification, 2026-08-21.** The user-authorized independent audit by
> `/root/cross_review` accepted `prop:a2-subquadratic-global` and its finite-logistic corollary
> `prop:a2-logistic-global`.  Their consolidated standalone proof is
> `solutions/a2-subquadratic-tail-rigidity.tex`.  Pre-review “draft/open” language below is retained
> to preserve the chronology of this exploration.

## Result

The exact logistic identity does not rely on linear growth specifically.  It is enough that the
convex likelihood perturbation is subquadratic in Gaussian average along one top prior-covariance
direction.

## Directional theorem

Let \(\Sigma\succ0\), let \(m\in\mathbb R^d\), and let \(L:\mathbb R^d\to\mathbb R\) be a
finite \(C^2\) convex function.  Consider

\[
 \pi(d\theta)\propto
 \exp\!\left[-\frac12(\theta-m)^T\Sigma^{-1}(\theta-m)-L(\theta)\right]d\theta.
\]

Let \(u\) be a unit eigenvector of \(\Sigma\) with
\(u^T\Sigma u=\lambda_{\max}(\Sigma)\), and put

\[
 Y_t\sim N(m+t\Sigma u,\Sigma).
\]

**Proof-draft hypothesis:**

\[
 \mathbb E L(Y_t)=o(t^2)\qquad(t\to+\infty).          \tag{SQ.1}
\]

Then

\[
 \boxed{\quad C_{\rm LS}(\pi)=C_{T_2}(\pi)=\lambda_{\max}(\Sigma).\quad}  \tag{SQ.2}
\]

Only one top eigendirection is needed for the lower bound.  A uniform subquadratic growth
condition is a convenient sufficient assumption, not the minimal statement.

## Proof and centering check

Completing the Gaussian square gives the exact identity

\[
 \log\mathbb E_\pi e^{t u^T\theta}
 =t u^Tm+\frac{t^2}{2}u^T\Sigma u
  +\log\mathbb E e^{-L(Y_t)}-\log\mathbb E e^{-L(Y_0)}.             \tag{SQ.3}
\]

Convexity supplies a global affine lower support \(L(y)\ge a+b^Ty\), hence

\[
 \log\mathbb E e^{-L(Y_t)}\le O(1+t).                              \tag{SQ.4}
\]

Jensen supplies the other direction,

\[
 \log\mathbb E e^{-L(Y_t)}\ge-\mathbb E L(Y_t)=o(t^2).             \tag{SQ.5}
\]

Equations (SQ.4)--(SQ.5) show that the correction in (SQ.3) is \(o(t^2)\), so

\[
 \lim_{t\to\infty}\frac{2}{t^2}
 \log\mathbb E_\pi e^{t u^T(\theta-\mathbb E_\pi\theta)}
 =u^T\Sigma u=\lambda_{\max}(\Sigma).                             \tag{SQ.6}
\]

The centering is essential for the standard sub-Gaussian formulation but harmless for the
quadratic coefficient: it subtracts only \(t u^T\mathbb E_\pi\theta\).  Gaussian domination by
the affine lower support of \(L\) guarantees the required posterior moments.  The transport lower
bound actually needs only a one-directional limsup of this centered quadratic coefficient;
(SQ.1) is a convenient Gaussian-tube contract that proves the stronger full limit (SQ.6), not a
claim of logical minimality.

Under the repository normalization, \(T_2(C)\) implies

\[
 \log\mathbb E_\pi e^{t u^T(\theta-\mathbb E\theta)}\le Ct^2/2.
\]

Comparison with (SQ.6) gives \(C_{T_2}\ge\lambda_{\max}(\Sigma)\).  Convexity of \(L\) gives
\(\nabla^2U\succeq\Sigma^{-1}\), so Bakry--Emery and Otto--Villani give

\[
 C_{T_2}\le C_{\rm LS}\le\lambda_{\max}(\Sigma).
\]

This proves (SQ.2) on paper.

## Checkable sufficient conditions

Condition (SQ.1) follows from any of the following.

1. \(L(x)\le a+b\|x\|^p\) for some \(a\in\mathbb R\), \(b\ge0\), and \(0\le p<2\). Gaussian moments give
   \(\mathbb E L(Y_t)=O(1+t^p)\), while convexity's affine lower support prevents a negative
   quadratic contribution.
2. Uniform subquadratic growth, \(L(x)=o(\|x\|^2)\).  For every \(\delta>0\), an affine lower
   support and uniform upper growth give
   \(-O(1+\|x\|)\le L(x)\le\delta\|x\|^2+C_\delta\); take Gaussian
   expectations, divide by \(t^2\), and let \(\delta\downarrow0\).
3. The original finite binary-logistic likelihood, for which
   \(0\le L(x)\le a+b\|x\|\).

The directional Gaussian-average condition is intentionally stronger than a pointwise statement
along the deterministic ray alone: completing the square samples an entire fixed-covariance
Gaussian tube around that ray.  A raywise estimate without control in this tube is not enough for
the Jensen bound used above.

## Shrinking Gaussian priors cannot preserve both targets

For a sequence of finite logistic likelihoods and Gaussian prior covariances \(\Sigma_n\), (SQ.2)
holds separately for every \(n\):

\[
 C_{\rm LS}(\pi_n)=C_{T_2}(\pi_n)=\lambda_{\max}(\Sigma_n).         \tag{SQ.7}
\]

Suppose the prior precision is negligible compared with an order-\(n\) likelihood Hessian in the
strong operator sense

\[
 \frac{\|\Sigma_n^{-1}\|_{\rm op}}{n}\longrightarrow0.            \tag{SQ.8}
\]

Then

\[
 n\lambda_{\max}(\Sigma_n)
 \ge n\lambda_{\min}(\Sigma_n)
 =\frac{n}{\|\Sigma_n^{-1}\|_{\rm op}}\longrightarrow\infty.      \tag{SQ.9}
\]

Thus a Gaussian prior negligible enough to preserve the ordinary Fisher BvM target cannot make
the global LSI or \(T_2\) constant Fisher-scale.

Conversely, if \(n\lambda_{\max}(\Sigma_n)\le C\), then

\[
 \frac1n\Sigma_n^{-1}\succeq C^{-1}I,                             \tag{SQ.10}
\]

so the prior contributes order-\(n\) local curvature and changes the local information matrix.
This is a sharp scale tradeoff, not merely a failure of one proof technique.  It does not rule out
localized inequalities, non-Gaussian priors with different tail geometry, or a deliberately
penalized asymptotic target.

Condition (SQ.8) is only curvature/information negligibility. If the Gaussian prior mean $m_n$
moves, full local prior negligibility also requires
$\|\Sigma_n^{-1}(\theta_0-m_n)\|/\sqrt n\to0$ (or a model-adapted score condition). The no-go
conclusion is unchanged because (SQ.8) is already necessary to preserve the unmodified local
information matrix.

## Boundaries and falsification programme

- If (SQ.1) fails because the likelihood has a genuine quadratic tail, the prior quadratic
  coefficient need not survive; the appropriate tail precision must be computed separately.
- If \(L\) is nonconvex, the Bakry--Emery upper bound in (SQ.2) is unavailable even if the MGF
  lower bound survives.
- The theorem identifies global LSI and \(T_2\), not \(C_P\).  Regular logistic Poincare
  asymptotics are instead addressed by the A1 mode-leverage theorem.
- A useful future discriminator is a convex perturbation with an explicit asymptotic quadratic
  form: its large-tilt MGF gives a tail lower bound, but equality requires a matching global
  curvature upper route.

`experiments/finum/targets/a2.py` now includes a deterministic scaling diagnostic for (SQ.8)--
(SQ.10).  The focused test contrasts \(\Sigma_n=n^{-1/2}I\), which is locally negligible but has
\(nC_{\rm global}=\sqrt n\), with \(\Sigma_n=n^{-1}I\), which has an order-one rescaled global
constant but order-\(n\) prior precision.  This algebraic calibration is not numerical evidence.

## Suggested repository follow-up

After independent review, add a dedicated subquadratic-tail proposition node and make the existing
logistic rigidity node its corollary.  Record the prior-scaling tradeoff under `q:a2-lsi`.  Until
that review occurs, all statuses should remain open and no evidence level should be promoted.
