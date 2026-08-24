# A2 — strong-Laplace proof, exact logistic global constants, and source audit

- **Date:** 2026-08-21
- **Nodes:** `conj:a2`, `thm:a2-target`, `q:a2-poincare`, `q:a2-lsi`
- **Type:** analytic audit; no new `finum` run and no numerical-evidence claim
- **Primary sources checked:** Chewi--Stromme,
  [*The Ballistic Limit of the Log-Sobolev Constant Equals the Polyak--Łojasiewicz Constant*](https://arxiv.org/abs/2411.11415),
  and Cattiaux--Guillin,
  [*On the Poincaré Constant of Log-Concave Measures*](https://arxiv.org/abs/1810.08369).
- **Original certification status:** the derivations below were analytic proof drafts under the
  then-current human/Lean-only gate. The later certification update records the reviewed subset;
  all other claims remain outside `proved` until they pass the current independent-review gate.

> **Same-day follow-up.** The later exploration
> [`2026-08-21-a2-subquadratic-tail-rigidity.md`](2026-08-21-a2-subquadratic-tail-rigidity.md)
> extends the linear-growth logistic identity to a directional Gaussian-average subquadratic
> class and records the shrinking-prior tradeoff.  The A1 mode-leverage follow-up also supplies a
> model-specific exact Poincare draft for bounded-Hessian logistic.  All remain open pending
> independent certification.

> **Later certification, 2026-08-21.** The user-authorized audit by `/root/cross_review`
> accepted the finite-logistic result `prop:a2-logistic-global` through the stronger audited node
> `prop:a2-subquadratic-global`; see `solutions/a2-subquadratic-tail-rigidity.tex`.  It also
> accepted the A1 vanishing-leverage result recorded in its own solution dossier.  The historical
> wording above is preserved, while `thm:a2-target` remains outside the audit and remains open.

## What was tried

I checked the proof obligations in `thm:a2-target`, audited the assumptions attributed to
Chewi--Stromme, and tested the claimed Fisher-scale LSI/transport conclusion against the actual
tails of the flagship Gaussian-prior logistic posterior.

## Result 1 — analytic proof draft for `thm:a2-target`

**Status: analytic proof draft.** Beyond independent certification, the open work is verifying its global oscillation hypothesis in a useful
model class, not proving the implication.

Let \(H\succ0\), \(T(z)=\hat\theta+H^{-1/2}z\), and suppose
\[
  \mu(dz)=q(z)\gamma(dz),\qquad
  q(z)=\frac{e^{-r(z)}}{\int e^{-r}\,d\gamma},\qquad
  \delta:=\operatorname{osc}(r)<\infty,
\]
where \(\gamma=N(0,I_d)\), and let \(\pi=T_\#\mu\). Then
\[
  e^{-\delta}\le q\le e^\delta.                       \tag{A2.1}
\]
Holley--Stroock and Lipschitz pushforward give
\[
  C_P(\pi),\ C_{\rm LS}(\pi),\ C_{\rm TCI}(\pi)
  \le e^\delta\lambda_{\max}(H^{-1}),                 \tag{A2.2}
\]
where the transport upper bound may be obtained from LSI and Otto--Villani.

Moreover, (A2.1) gives, for \(Z\sim\gamma\),
\[
 \|\mathbb E_\mu z\|\le(e^\delta-1)\mathbb E\|Z\|,
 \qquad
 \|\mathbb E_\mu zz^T-I\|_{\rm op}
 \le(e^\delta-1)\mathbb E\|Z\|^2.
\]
Hence \(\|\operatorname{Cov}_\mu-I\|_{\rm op}=o(1)\) as \(\delta\to0\), and
\[
  \lambda_{\max}(\operatorname{Cov}_\pi)
  =(1+o(1))\lambda_{\max}(H^{-1}).                    \tag{A2.3}
\]
The covariance lower bound applies not only to \(C_P\): under the repository normalization,
\(T_2(C)\) implies the linear sub-Gaussian bound and therefore
\(C_{\rm TCI}\ge\lambda_{\max}(\operatorname{Cov})\). Also
\(C_{\rm LS}\ge C_P\ge\lambda_{\max}(\operatorname{Cov})\). Combining (A2.2)--(A2.3),
\[
 C_P(\pi),\ C_{\rm LS}(\pi),\ C_{\rm TCI}(\pi)
 =(1+o(1))\lambda_{\max}(H^{-1}).                     \tag{A2.4}
\]
This deterministic sandwich applied on events where
\(\delta_n=o_P(1)\) and \(H_n/n\to I(\theta_0)\) proves all conclusions of
`thm:a2-target`.

Two wording corrections follow.

- A generic “tail/no-bottleneck condition” is not **equivalent** to global
  \(\operatorname{osc}(r_n)=o_P(1)\). It can be an alternative hypothesis for the Poincaré
  limit only after a separate stability theorem is proved.
- The lower bound for \(T_2\) is not the Poincaré `lem:linear-test-lower`; it is the distinct
  lemma \(T_2(C)\Rightarrow\operatorname{Cov}\preceq CI\).

## Result 2 — exact global LSI and transport constants for Gaussian-prior logistic

**Status: analytic proof draft.** This is an exact obstruction, for every sample size, to a global
posterior-scale LSI or \(T_2\) in the flagship model.

Let
\[
 \pi(d\theta)=Z^{-1}\exp\!\left[-\frac12(\theta-m)^T\Sigma_0^{-1}(\theta-m)
                                  -L(\theta)\right]d\theta,
\]
where \(\Sigma_0\succ0\) and \(L\) is any finite binary-logistic negative log-likelihood.
Each observation loss satisfies
\[
 0\le \log(1+e^s)-ys\le\log2+|s|,\qquad y\in\{0,1\},
\]
so, for finite design, there are \(a,b<\infty\) with
\[
 0\le L(\theta)\le a+b\|\theta\|.                    \tag{A2.5}
\]

Fix \(u\in\mathbb R^d\). Completing the Gaussian square yields
\[
\begin{aligned}
 \log\mathbb E_\pi e^{t u^T\theta}
 &=\frac{t^2}{2}u^T\Sigma_0u+t u^Tm+O(1)\\
 &\quad+\log\mathbb E_{Y_t}e^{-L(Y_t)},
 \qquad Y_t\sim N(m+t\Sigma_0u,\Sigma_0).
\end{aligned}
\]
By (A2.5), \(\log\mathbb E e^{-L(Y_t)}\le0\), while Jensen gives
\[
 \log\mathbb E e^{-L(Y_t)}\ge-\mathbb E L(Y_t)\ge-O(1+|t|).
\]
Therefore, after centering (which changes only the linear term),
\[
 \lim_{t\to\infty}\frac{2}{t^2}
 \log\mathbb E_\pi e^{t u^T(\theta-\mathbb E\theta)}
 =u^T\Sigma_0u.                                      \tag{A2.6}
\]

Now check the constant convention directly. The repository defines
\(T_2(C)\) by \(W_2^2(q,\pi)\le2C\operatorname{KL}(q\|\pi)\). Since
\(W_1\le W_2\), this implies \(T_1(C)\). The entropy variational formula (equivalently the
Bobkov--Götze argument) then gives, for every Lipschitz \(f\),
\[
 \log\mathbb E_\pi e^{t(f-\mathbb Ef)}
 \le\frac{C t^2\|f\|_{\rm Lip}^2}{2}.                \tag{A2.7}
\]
Apply (A2.7) to \(f(\theta)=u^T\theta\) and compare with (A2.6):
\[
 C_{\rm TCI}(\pi)\ge\frac{u^T\Sigma_0u}{\|u\|^2}.
\]
Taking the top eigenvector gives
\[
 C_{\rm TCI}(\pi)\ge\lambda_{\max}(\Sigma_0).       \tag{A2.8}
\]
On the other hand, convexity of the likelihood gives
\(\nabla^2U\succeq\Sigma_0^{-1}\), so Bakry--Émery and Otto--Villani yield
\[
 C_{\rm TCI}(\pi)\le C_{\rm LS}(\pi)
 \le\lambda_{\max}(\Sigma_0).                       \tag{A2.9}
\]
Equations (A2.8)--(A2.9) prove the exact identity
\[
 \boxed{C_{\rm TCI}(\pi)=C_{\rm LS}(\pi)=\lambda_{\max}(\Sigma_0).} \tag{A2.10}
\]

This applies to every \(n\), every finite design, separable or not. In particular, with a fixed
Gaussian prior,
\[
 nC_{\rm LS}(\pi_n)=nC_{\rm TCI}(\pi_n)
 =n\lambda_{\max}(\Sigma_0)\longrightarrow\infty,     \tag{A2.11}
\]
even in regular fixed-dimensional logistic models for which the Poincaré constant is expected
to have the Fisher \(1/n\) scale.

There is no conflict with Result 1: for Gaussian-prior logistic the global oscillation of the
local Gaussian remainder is not small; in fact it is generally infinite. The local Gaussian has
\(O(n)\) quadratic precision, whereas arbitrarily far out the logistic likelihood is only linear
and the posterior returns to the fixed prior's quadratic tail.

The same proof shows a useful generalization: whenever a convex likelihood perturbation is
nonnegative and at most linear at infinity, the Gaussian tail covariance fixes the optimal global
LSI and \(T_2\) constants exactly. For an \(n\)-dependent Gaussian prior covariance
\(\Sigma_{0,n}\), both constants equal \(\lambda_{\max}(\Sigma_{0,n})\), not automatically the
local Fisher constant.

## Result 3 — Chewi--Stromme assumptions were understated

**Status: primary-source audit.** Their Theorem 2 does prove
\[
 \lim_{t\downarrow0}\frac{C_P(e^{-f/t})}{t}
 =\lambda_{\min}(\nabla^2f(x_*))^{-1},
\]
but not from a unique nondegenerate minimizer alone. The theorem assumes:

1. a unique global minimizer;
2. finite global PL constant in their inverse convention,
   \(f-f_*\le(C_{\rm PL}/2)\|\nabla f\|^2\);
3. a growth bound \(\Delta f\le L(1+\|\nabla f\|^2)\); and
4. normalizability of \(e^{-f/t}\).

Their LSI theorem has the same global character and gives
\(\lim C_{\rm LS}(e^{-f/t})/t=C_{\rm PL}(f)=1/\mu_{\rm PL}\) in the repository's rate
notation. Thus the reciprocal in the A2 manuscript is correct, but its Poincaré citation drops
essential hypotheses.

A natural statistical example exposes the distinction. For intercept-only Bernoulli likelihood
with success probability \(p\in(0,1)\),
\[
 f_p(\theta)=\log(1+e^\theta)-p\theta
\]
has a unique nondegenerate minimizer and Fisher curvature \(p(1-p)>0\), but
\(f_p(\theta)\sim(1-p)\theta\) and \(f_p'(\theta)\to1-p\) as \(\theta\to+\infty\). Hence its
global PL rate is zero (\(C_{\rm PL}=\infty\)). The unregularized low-temperature law has
exponential tails and no classical LSI; adding a fixed Gaussian prior makes LSI finite but, by
(A2.10), exactly prior-scale.

So “global log-concavity” alone is not a sufficient discriminator for a Fisher-local LSI limit.
Under the Chewi--Stromme hypotheses the exact discriminator is
\[
 C_{\rm PL}(f)=\lambda_{\min}(\nabla^2f(x_*))^{-1}
 \quad\text{or, equivalently,}\quad
 \mu_{\rm PL}(f)=\lambda_{\min}(\nabla^2f(x_*)).
\]

## A1--A2 consistency verdict

- The **Poincaré** lines are scale-compatible: if an A1 recipe makes
  \(A_{\bar W_n}/n\to I\) and its integrated tail \(o(1/n)\), the A1 theorem gives the right
  \(1/n\) scale. Its fixed universal Milman factor does not give A2's exact coefficient; a
  separate \(1+o(1)\) spectral-stability theorem is required.
- The **global LSI/transport** lines split: they are Fisher-local under the very strong global
  Gaussian-comparison hypothesis, but exactly prior-scale for ordinary fixed-Gaussian-prior
  logistic posteriors. A1 and A2 should state this dichotomy explicitly rather than treating
  logistic as a likely Fisher-local example.

## Audit of the existing `finum` artifact

`research/runs/2026-06-20-A2.jsonl` is dirty and evidence-ineligible.

- The Gaussian-linear calibration correctly checks scalar \(n\)-normalization, although it uses
  \(\operatorname{Cov}=(n\Sigma_x)^{-1}\) (no fixed-prior correction), so it is an algebraic
  calibration rather than a finite-\(n\) Gaussian-prior posterior identity.
- The contamination rows are an analytic refutation of TV-only transfer and remain useful as an
  obstruction diagnostic.
- The logistic sweep uses one data set/chain per \(n\), despite the target's convergence-in-
  probability/repeated-draw requirement. The reported sequence is
  \(12.596,10.718,7.004,7.649\) against target \(6.603\): closer overall but non-monotone.
- The artifact-producing code defined `trend_up = last > first`, although this run approaches
  the target mainly by decreasing, and its note said “increases toward target.” That flag was not
  a meaningful convergence diagnostic. The 2026-08-21 implementation now records absolute
  endpoint errors and does not impose monotonicity; this repairs the diagnostic, not the missing
  repeated-draw/convergence gates.
- `stress-non-fisher-local` is explicitly deferred. Result 2 supplies an exact logistic
  discriminator that requires no LSI estimator.

There is consequently no basis for `numerical-strong`, and none is claimed here.

## Refined proof and test frontier

1. Treat the global-oscillation implication `thm:a2-target` as proved; move the open payload to
   model-specific verification or to a weaker Poincaré-only stability theorem.
2. Correct the Chewi--Stromme assumptions before using their result as the deterministic anchor
   for `q:a2-poincare`.
3. Split `q:a2-lsi` into global-tail classes. For fixed-Gaussian-prior logistic, record the exact
   prior-scale theorem (A2.10); reserve the Fisher limit for globally Gaussian-comparable,
   bounded-parameter, or suitably quadratic-tail models.
4. Add the covariance lower lemma for \(T_2\) separately from `lem:linear-test-lower`.
5. Complete the A2 numerical sweep repair: the error-to-target statistic now replaces
   `trend_up`; repeated data draws and a two-chain/ESS gate are still needed for a convergence-in-
   probability diagnostic.
