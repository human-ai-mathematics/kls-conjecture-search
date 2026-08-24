# A1 — noncompact harmonic mean and a deterministic mode-leverage certificate

- **Date:** 2026-08-21
- **Nodes:** `prop:a1-euclidean-harmonic`, `prop:a1-mode-leverage`,
  `cor:a1-leverage-asymptotic`; related frontier nodes `prop:a1-bulk-tail`, `q:a1-poincare`,
  `q:a1-barw`, `q:a1-tail`, `q:a1-sharp`, and `conj:a2`
- **Type:** analytic proof drafts plus deterministic calibration; no promotable numerical run
- **Certification:** every result called a proof draft below remains `open` until it is moved to a
  standalone solution and independently checked under the repository workflow.
- **Source boundary:** Veysseire's theorem is stated for compact weighted manifolds.  The
  Euclidean argument below is a separate spectral-domain argument; it is not an assertion that
  the compact theorem applies verbatim.

> **Later certification, 2026-08-21.** The user-authorized independent audit by
> `/root/cross_review` accepted `prop:a1-euclidean-harmonic`, `prop:a1-mode-leverage`, and
> `cor:a1-leverage-asymptotic`.  The standalone reviewed proof is
> `solutions/a1-harmonic-mode-leverage.tex`.  “Draft” and “pending” below are retained as the
> contemporaneous pre-review record; they no longer describe those three nodes.

## Executive result

Two parts of the previous A1 programme can be made substantially sharper.

1. The factor-one harmonic-mean estimate can be proved on noncompact Euclidean space under a
   concrete domain hypothesis, and that hypothesis can be verified for smooth uniformly convex
   potentials with a global upper Hessian bound.  This class contains every finite
   Gaussian-prior binary-logistic posterior.  It does **not** yet contain arbitrary uniformly
   convex potentials with unbounded Hessian, Poisson posteriors, nonsmooth losses, or merely weakly
   convex laws.
2. A log-Lipschitz condition on the likelihood curvature gives an explicit, data-computable
   posterior-tail bound in mode-Hessian coordinates.  It covers logistic and Poisson likelihoods
   and, for bounded-Hessian models such as logistic, combines with factor one to give an exact
   fixed-dimensional Poincare asymptotic under vanishing maximal leverage.

At the time of writing, these were analytic drafts rather than ledger-certified theorems; the
later certification note above records their current status.

## 1. A noncompact factor-one theorem under an explicit domain contract

Let

\[
  \mu(dx)=Z^{-1}e^{-U(x)}dx,\qquad
  A=-\Delta+\nabla U\mathbin\cdot\nabla
\]

on \(L^2(\mu)\), with Dirichlet form
\(\mathcal E(f,f)=\int|\nabla f|^2d\mu\).  Put
\(\rho(x)=\lambda_{\min}(\nabla^2U(x))\), and let
\(\lambda_1=1/C_P(\mu)\) denote the bottom of the spectrum of \(A\) on constants' orthogonal
complement.

### Abstract domain lemma

**Proof-draft statement.** Suppose that:

1. \(U\) is smooth enough for the weighted Bochner identity on \(C_c^\infty\);
2. \(\rho\ge m>0\);
3. \(A\) is the nonnegative self-adjoint operator associated with \(\mathcal E\); and
4. for every bounded spectral subspace of \(A\), its elements lie in the closed Bochner domain and
   satisfy
   \[
     \|Af\|_2^2
       =\int\|\nabla^2 f\|_{\rm HS}^2d\mu
        +\int\langle\nabla^2U\nabla f,\nabla f\rangle d\mu.       \tag{HM.1}
   \]

Then

\[
  \boxed{\quad C_P(\mu)\le\int\rho(x)^{-1}\,d\mu(x).\quad}       \tag{HM.2}
\]

The statement uses no first-eigenfunction or compact-resolvent assumption.

### Spectral-localization proof

Fix \(\varepsilon>0\).  By the definition of the bottom of the nonzero spectrum, the spectral
projection of \(A\) onto \([\lambda_1,\lambda_1+\varepsilon]\) is nonzero.  Choose a nonzero
\(f\) in its range and put \(g=|\nabla f|\).  Spectral calculus gives

\[
  \|Af\|_2^2
  \le(\lambda_1+\varepsilon)\langle f,Af\rangle
  =(\lambda_1+\varepsilon)\int g^2d\mu.             \tag{HM.3}
\]

The weak Kato inequality, justified first for
\(g_\delta=(|\nabla f|^2+\delta^2)^{1/2}\) and then by \(\delta\downarrow0\), gives
\(|\nabla g|^2\le\|\nabla^2f\|_{\rm HS}^2\) almost everywhere.  Combining (HM.1)--(HM.3),

\[
  (\lambda_1+\varepsilon)\int g^2d\mu
  \ge\int|\nabla g|^2d\mu+\int\rho g^2d\mu.          \tag{HM.4}
\]

Apply the Poincare inequality with its optimal gap \(\lambda_1\) to \(g\):

\[
  \int|\nabla g|^2d\mu
  \ge\lambda_1\left\{\int g^2d\mu-\left(\int g\,d\mu\right)^2\right\}.
\]

After substitution in (HM.4),

\[
  \int\rho g^2d\mu
  \le\lambda_1\left(\int g\,d\mu\right)^2
     +\varepsilon\int g^2d\mu.                     \tag{HM.5}
\]

Cauchy--Schwarz and \(\rho\ge m\) yield

\[
  \left(\int g\,d\mu\right)^2
       \le\left(\int\rho g^2d\mu\right)\left(\int\rho^{-1}d\mu\right),
  \qquad
  \int g^2d\mu\le m^{-1}\int\rho g^2d\mu.
\]

Since \(f\) is nonconstant, \(\int\rho g^2d\mu>0\).  Divide (HM.5) by this quantity:

\[
  1\le\lambda_1\int\rho^{-1}d\mu+\frac{\varepsilon}{m}.
\]

Letting \(\varepsilon\downarrow0\) proves (HM.2).  This is the same algebra as the compact
eigenfunction proof, but spectral localization removes the need for the infimum to be attained.

### Closing the domain contract for bounded Hessian

The abstract fourth hypothesis is not automatic merely from the phrase "strongly log-concave".
It does close under the following concrete assumptions:

\[
  U\in C^\infty(\mathbb R^d),\qquad
  mI\preceq\nabla^2U(x)\preceq MI\quad\text{for every }x.          \tag{HM.6}
\]

Indeed, under the unitary map \(f\mapsto e^{-U/2}f\), the Friedrichs realization of \(A\) is the
Schrodinger operator

\[
  -\Delta+V_U,\qquad
  V_U=\frac14|\nabla U|^2-\frac12\Delta U.            \tag{HM.7}
\]

Strong convexity gives \(|\nabla U(x)|\ge m|x|-|\nabla U(0)|\), while the upper Hessian bound gives
\(\Delta U\le dM\).  Hence \(V_U\) is bounded below and tends to infinity quadratically.  The
Friedrichs operator has `C_c^\infty` as an operator core; equivalently, its graph norm can be
localized by smooth cutoffs.  Local Rellich compactness plus the coercive tail of \(V_U\) also
shows compact resolvent, although compactness is not needed by the spectral-band proof.

For \(\phi\in C_c^\infty\), integration by parts has no boundary term and gives exactly (HM.1).
If \(\phi_k\to f\) in the graph norm of \(A\), apply (HM.1) to
\(\phi_k-\phi_l\).  Positivity of \(\nabla^2U\) makes \(\nabla^2\phi_k\) Cauchy in \(L^2\), and
the form identity makes \(\nabla\phi_k\) Cauchy in \(L^2\).  Thus (HM.1) passes to the graph
limit.  The regularized Kato inequality passes to the same limit.  This closes the cutoff,
boundary, spectral-domain, and Kato steps under (HM.6).

Every finite Gaussian-prior logistic posterior satisfies (HM.6), since

\[
 \Sigma_0^{-1}\preceq\nabla^2U(\theta)
 \preceq\Sigma_0^{-1}+\tfrac14X^TX.
\]

Consequently factor one is a complete-on-paper proof draft for that class.

### Boundary of the result

No claim is made here for all noncompact strongly log-concave measures.  The unresolved step for
an unbounded Hessian is verifying an operator core on which (HM.1) closes without losing the
nonnegative curvature term.  A naive exhaustion has boundary terms, and a naive mollification of
\(U\) requires simultaneous Mosco convergence of gaps and uniform integrability of
\(\rho^{-1}\).  Poisson curvature is unbounded, so the result above does not by itself give
factor one for Poisson GLMs.  Merely convex or nonsmooth losses are further outside (HM.6).

## 2. Log-Hessian-Lipschitz GLMs

Suppose that each likelihood curvature is positive and satisfies

\[
  |\log\ell_i''(s)-\log\ell_i''(t)|\le L_i|s-t|.       \tag{ML.1}
\]

This holds with \(L_i=1\) for binary logistic and Poisson regression and with \(L_i=0\) for a
Gaussian linear likelihood.  Let \(\hat\theta\) be the posterior mode,

\[
  \widehat H=\nabla^2U(\hat\theta),\qquad
  \alpha_i=L_i\sqrt{x_i^T\widehat H^{-1}x_i},\qquad
  \eta=\max_i\alpha_i,                               \tag{ML.2}
\]

and use mode-Hessian coordinates
\(z=\widehat H^{1/2}(\theta-\hat\theta)\), \(r=|z|\).

### Hessian and potential sandwiches

Condition (ML.1) and Cauchy--Schwarz give

\[
 e^{-\eta r}I
 \preceq \widehat H^{-1/2}\nabla^2U(\theta)\widehat H^{-1/2}
 \preceq e^{\eta r}I.                                \tag{ML.3}
\]

The fixed prior Hessian also obeys this comparison because
\(e^{-\eta r}\Sigma_0^{-1}\preceq\Sigma_0^{-1}\preceq
e^{\eta r}\Sigma_0^{-1}\).  Integrating (ML.3) twice along the segment from the mode to
\(\theta\) gives

\[
 g_-(r;\eta)\le U(\theta)-U(\hat\theta)\le g_+(r;\eta),             \tag{ML.4}
\]

where

\[
 g_-(r;\eta)=\frac{e^{-\eta r}+\eta r-1}{\eta^2},\qquad
 g_+(r;\eta)=\frac{e^{\eta r}-\eta r-1}{\eta^2},                   \tag{ML.5}
\]

with the continuous value \(g_\pm(r;0)=r^2/2\).  Notice that
\(g_-\le r^2/2\le g_+\).  The lower comparison is Gaussian near the mode and becomes linear at
radius \(r\gg1/\eta\); it therefore records rather than hides the saturating tail.

### Explicit weights and tail probability

For \(R>0\), let

\[
 E_R=\{|\widehat H^{1/2}(\theta-\hat\theta)|\le R\},\qquad
 \bar w_i(R)=e^{-\alpha_iR}\ell_i''(x_i^T\hat\theta).              \tag{ML.6}
\]

Then \(E_R\subseteq G_{\bar W(R)}\).  Define the one-dimensional radial integrals

\[
 D_d(\eta)=\int_0^\infty r^{d-1}e^{-g_+(r;\eta)}dr,
 \qquad
 N_d(R,\eta)=\int_R^\infty r^{d-1}e^{-g_-(r;\eta)}dr.              \tag{ML.7}
\]

The common sphere area and the whitening Jacobian cancel, so (ML.4) proves the fully computable
bound

\[
 \pi(G_{\bar W(R)}^c)\le\pi(E_R^c)
 \le\varepsilon_d(R,\eta):=\min\left\{1,\frac{N_d(R,\eta)}{D_d(\eta)}\right\}.   \tag{ML.8}
\]

Together with `prop:a1-bulk-tail`, this is already a non-oracle A1 certificate with universal
factor \(C_M\).  It applies to Poisson as well as logistic, because the tail calculation does not
use the bounded-Hessian hypothesis needed by the factor-one proof.

### Direct factor-one certificate for bounded-Hessian models

Inequality (ML.3) also gives

\[
 \lambda_{\max}(H(\theta)^{-1})
 \le e^{\eta r}\lambda_{\max}(\widehat H^{-1}).                    \tag{ML.9}
\]

For \(0\le\eta<1\), set

\[
 K_d(\eta)=
 \frac{\displaystyle\int_0^\infty r^{d-1}
                 e^{\eta r-g_-(r;\eta)}dr}
      {\displaystyle D_d(\eta)}.                                  \tag{ML.10}
\]

The numerator is finite exactly in the regime certified by this radial majorant: its remote-tail
exponent has slope \(\eta-1/\eta<0\).  Combining (HM.2), (ML.4), and (ML.9), every
bounded-Hessian posterior satisfying (ML.1) obeys the analytic proof-draft bound

\[
  \boxed{\quad C_P(\pi)\le K_d(\eta)\lambda_{\max}(\widehat H^{-1}),
             \qquad 0\le\eta<1.\quad}                              \tag{ML.11}
\]

This is not the false tail-free inverse-mode-Hessian formula: the multiplier is finite only after
the leverage condition controls the remote likelihood flattening.  When \(\eta\ge1\), (ML.10)
deliberately emits no finite certificate; (ML.8) and the prior-scale fallback remain valid.

## 3. Exact fixed-dimensional asymptotics

For fixed \(d\), \(K_d(\eta)\to1\) as \(\eta\downarrow0\).  This follows by dominated
convergence: \(g_\pm(r;\eta)\to r^2/2\) pointwise; for
\(0\le\eta\le\eta_0<1\), the numerator is dominated by
\(r^{d-1}e^{\eta_0r-g_-(r;\eta_0)}\), which is integrable, and
\(e^{-g_+}\le e^{-r^2/2}\).

The same argument applied to the actual whitened density shows convergence in total variation
and of every fixed polynomial moment to \(N(0,I_d)\).  In particular,

\[
 \operatorname{Cov}_{\pi_n}
 =\widehat H_n^{-1/2}(I_d+o(1))\widehat H_n^{-1/2}.                 \tag{ML.12}
\]

The linear lower test, (ML.11), and (ML.12) therefore prove the deterministic implication

\[
 \eta_n\to0
 \quad\Longrightarrow\quad
 C_P(\pi_n)=(1+o(1))\lambda_{\max}(\widehat H_n^{-1})              \tag{ML.13}
\]

for fixed-dimensional bounded-Hessian log-curvature-Lipschitz posteriors.  If the inputs are
random and \(\eta_n\to0\), \(\widehat H_n/n\to I(\theta_0)\) in probability, the deterministic
subsequence argument gives

\[
 nC_P(\pi_n)\ \longrightarrow\ \lambda_{\max}(I(\theta_0)^{-1})
 \quad\text{in probability}.                                      \tag{ML.14}
\]

Thus ordinary regular logistic regression has an A2 route that requires neither finite global PL
nor global bounded oscillation relative to the BvM Gaussian.  For fixed dimension, a transparent
minimal structural condition is the absence of a dominant observation, \(\eta_n\to0\).

No growing-dimensional theorem is claimed.  The local Taylor remainder is of order
\(\eta r^3\), and a Gaussian radius is of order \(\sqrt d\), suggesting the stronger scale
\(\eta d^{3/2}\to0\) for density comparison; turning that heuristic into a uniform spectral
statement is a separate `q:a2-highdim` problem.

## 4. High-leverage failure is correctly exposed

For the one-observation family

\[
 \pi_a(d\theta)\propto e^{-\theta^2/(2\sigma^2)}\operatorname{sigmoid}(a\theta)d\theta,
\]

the previous audit showed that the inverse mode Hessian tends to zero although the variance stays
bounded below.  Here

\[
 \eta_a^2=\frac{a^2}{\sigma^{-2}+a^2w(a\hat\theta_a)}\longrightarrow\infty.
\]

Hence (ML.11) rejects precisely this false tail-free regime.  In a wide design, data-null
directions remain in \(\widehat H^{-1}\) at the prior scale, so even small row leverage cannot
manufacture improvement in unidentified directions.

## 5. Deterministic calibration added

`experiments/finum/targets/a1.py` now contains stable implementations of \(g_\pm\),
\(\varepsilon_d\), \(K_d\), logistic row leverage, the rowwise weight floor, and the complete
factor-one split expression.  The focused tests check:

- \(g_-\le r^2/2\le g_+\);
- the \(\eta=0\) radial tail equals the exact chi-law survival probability and \(K_d(0)=1\);
- \(K_d(\eta)\to1\) numerically as \(\eta\downarrow0\), while \(\eta\ge1\) triggers the explicit
  failure gate; and
- the rowwise weights in (ML.6) are valid on the mode ellipsoid;
- the one-observation separable family has increasing \(\eta>1\), whereas replicated separable
  intercept data have decreasing row leverage (at the slower \(1/\sqrt{\log n}\) scale).

These are deterministic algebra/calibration checks.  They do not constitute `numerical-strong`
evidence and do not justify a ledger promotion.

## Recommended certification and ledger follow-up (historical)

After independent review, the repository can consider separate nodes for:

1. the bounded-Hessian Euclidean harmonic-mean proposition (HM.2);
2. the mode-leverage certificate (ML.8)--(ML.11); and
3. the exact vanishing-leverage Poincare asymptotic (ML.13)--(ML.14).

At that stage all three remained analytic proof drafts; they have since passed the review named at
the top of this note.  The existing general `prop:a1-bulk-tail` remains useful for
unbounded-Hessian GLMs and weaker regularity, with its universal Milman factor, but it was outside
that review and remains open.
