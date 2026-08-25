# Shared tools — reusable across targets

Lemmas, identities, and numerical primitives used by more than one open target. Math in LaTeX
(`$…$`); the canonical formal statement is the manuscript `\label` named under each entry —
this file links and explains. Keep target-specific tricks in the target `.md`.

---

## lem:linear-test-lower — the universal sound refuter
$C_P(\pi) = \sup_f \mathrm{Var}_\pi(f)/\mathbb E_\pi\|\nabla f\|^2$, so **every** test function
gives a certified lower bound $R[f] \le C_P$. The linear test $f(\theta)=\langle v,\theta\rangle$
gives $R[f] = v^\top\mathrm{Cov}_\pi v / \|v\|^2$, maximised at **$C_P \ge \lambda_{\max}(\mathrm{Cov}_\pi)$**
(`rem:rayleigh-lower-only`).

- **Why it matters:** the one tool that *soundly* refutes an upper-bound conjecture — if a claimed
  $C_P \le B$ has the exact $\lambda_{\max}(\mathrm{Cov}_\pi) > B$, the conjecture is false.
  A sampled covariance needs explicit confidence/mixing and numerical-error control before it can
  carry that verdict.
- **finum:** `constants.poincare_lower(samples) = ` $\lambda_{\max}$(empirical cov), a directional
  estimate unless the preceding controls are supplied; richer test-function bases (quadratic,
  RBF) and spectral estimators can give tighter directional estimates.
- **Used by:** A1 (`q:a1-sharp`), A2 (`conj:a2`, the contamination falsification), A4 (`q:a4-mean`),
  A5 (`q:a5-detect`).

---

## thm:hardy-1d — the 1D weighted Hardy/Muckenhoupt criterion
A weighted Poincaré $\mathrm{Var}_\mu(f) \le C \int a\,|f'|^2\,d\mu$ on $\mathbb R$ holds iff the
Hardy quantities $B_\pm = \sup_{x \gtrless m} \mu(\text{tail}) \int_m^x dt/(a(t)p(t))$ are finite,
pinning the optimal constant up to factor 4: $\max(B_+,B_-) \le C_{\mathrm{opt}} \le 4\max(B_+,B_-)$.

- **Why it matters:** turns "does a tail-index-dependent constant exist, and what is it" into a
  single explicit supremum — closed form for Student-$t$, analytically solved for the horseshoe,
  and numerically directional for other mixtures. Use one-sided tails; replacing
  $\mu([x,\infty))$ by $\mu(|X|\ge x)$ doubles the
  symmetric Hardy quantity and changes the bracket accordingly.
- **finum:** evaluate the Hardy supremum numerically for any 1D marginal; combine with
  tensorization for product priors.
- **Used by:** A3 (`conj:a3-dependent`, `prop:a3-horseshoe`, `q:a3-catalogue`); the original
  `conj:a3` is retained only as a refuted tombstone.

---

## Holley–Stroock $e^{\mathrm{osc}}$ transfer
If $\pi = e^{-W}\nu/Z$ with $\mathrm{osc}(W) \le A$, then $C_P(\pi) \le e^A C_P(\nu)$ (same for
$C_{\mathrm{LS}}$). With $\mathrm{osc}\to0$ the constants transfer *exactly*.

- **Why it matters:** the clean device behind A2's "BvM Gaussian computes the constants": if the
  rescaled posterior is an $o_P(1)$-oscillation reweighting of its Gaussian, the Gaussian constants
  transfer with factor $1+o_P(1)$.
- **Used by:** A2 (`thm:a2-target`), A1-bis.
- **Caveat:** global $o(1)$ oscillation is a sufficient density-ratio comparison, not equivalent
  to a generic tail/no-bottleneck hypothesis.

---

## Tensorization (weighted and unweighted)
For a product $\mu = \bigotimes_i \mu_i$, $C_P(\mu) = \max_i C_P(\mu_i)$ (weighted analogue:
$\mathrm{Var}_\mu(f) \le (\max_i C_i) \int \sum_i a_i\,|\partial_i f|^2\,d\mu$). Dimension-free.

- **Used by:** A3 (product priors, `eq:a3-tensor`), A5 (Neal funnel non-centered law).
- **Caveat:** hierarchical posteriors are **not** products — tensorization is the easy half; the
  conditional-variance decomposition with unbounded conditional scales is the hard half
  (`q:a3-hierarchical`).

---

## $T_2$ implies the covariance lower constraint

With the convention $W_2^2(\nu,\pi)\le2C\,\mathrm{KL}(\nu\|\pi)$, the $T_2(C)$ inequality
implies the centered sub-Gaussian bound
$\log\mathbb E_\pi e^{t\langle u,X-\mathbb EX\rangle}\le Ct^2\|u\|^2/2$. Differentiating at
$t=0$ gives
$$
  \operatorname{Cov}_\pi(X)\preceq C I,
  \qquad C_{\mathrm{TCI}}(\pi)\ge\lambda_{\max}(\operatorname{Cov}_\pi).
$$

- **Used by:** A2 (strong-Laplace lower sandwich and logistic tail rigidity), A4 (mean/transport
  lower witnesses).
- **Caveat:** this is a lower constraint on a claimed $T_2$ constant, not an upper bound or a
  numerical estimator of the optimal constant.

---

## lem:a5-lipschitz — Lipschitz transport of all three constants
$T_\#\nu = \mu$ with $T$ globally $L$-Lipschitz $\Rightarrow C_P(\mu) \le L^2 C_P(\nu)$ (same for
$C_{\mathrm{LS}}$, $C_{\mathrm{TCI}}$).

- **Why it matters:** makes "non-centering improves the constant" precise — it is a statement about
  *which metric the sampler sees*. A funnel is where the centered$\leftrightarrow$non-centered map
  fails to be bi-Lipschitz. For Neal's map neither direction is globally Lipschitz, so this lemma
  supplies no global comparison in either direction.
- **Used by:** A5 (`q:a5-reparam`, `ex:a5-neal`).

---

## lem:a5-pi-exp-tail — Poincaré forces a small Lipschitz exponential moment

If a Euclidean law has finite Poincaré constant $C$, every real $1$-Lipschitz $f\in L^2$ obeys
$$
 \mathbb E e^{c|f-\operatorname{med}f|}<\infty
 \qquad\text{for }0<c<\frac{\log2}{2\sqrt C}.
$$
Apply Poincaré to a ramp of height $2\sqrt C$ above successive median-centered levels. The
independent-copy variance formula gives a factor-$1/2$ tail contraction at each step; iteration
and tail integration give the exponential moment. This independently agent-certified lemma is
the decisive obstruction for lognormal-type funnel coordinates.

- **Used by:** A5 (`ex:a5-neal`, `prop:a5-partial-funnel`).

---

## prop:a1-bulk-tail — Brascamp–Lieb + log-concave self-improvement
For strictly convex $U$: $\mathrm{Var}_\pi(f) \le \mathbb E_\pi\langle H(\theta)^{-1}\nabla f,\nabla f\rangle$.
This is *not yet* a Poincaré inequality (curvature and gradient stay coupled); the
Milman log-concave spread-to-gap comparison (as recorded by Cattiaux–Guillin) gives the proof-draft
bound $C_P \le C_M\mathbb E_\pi \lambda_{\max}(H(\theta)^{-1})$ with a universal factor $C_M$.
Veysseire proves a factor-one harmonic-mean result for compact reversible diffusions; extending
that route verbatim is not asserted. A separate independently agent-certified proof gives factor one on
$\mathbb R^d$ under smooth $U$ and $mI\preceq\nabla^2U\preceq MI$:
$$
  C_P(\pi)\le \mathbb E_\pi\lambda_{\max}((\nabla^2U)^{-1}).
$$
It uses spectral localization, integrated Bochner, weak Kato, and graph-norm closure after the
Schrödinger conjugation. This covers finite Gaussian-prior logistic posteriors; unbounded-Hessian
Poisson and minimal regularity remain open.

- **Why it matters:** the skeleton of A1 (`eq:a1-cfg`) and the bulk constant of A4.
- **Note:** the operative quantity is $\mathbb E_\pi \lambda_{\max}(H^{-1})$ (average *inverse*
  curvature), not $\lambda_{\max}((\mathbb E_\pi H)^{-1})$ — matrix inversion is operator-convex, so
  the tail of $W(\theta)$ is structurally part of the problem (ties back to `obs:flat-direction`).
- **Used by:** A1 (`q:a1-poincare`), A4 (`q:a4-restricted`).

---

## prop:a1-mode-leverage — deterministic mode-to-tail geometry

If each positive likelihood curvature has log-Lipschitz constant $L_i$, put
$\alpha_i=L_i\sqrt{x_i^T\widehat H^{-1}x_i}$ and $\eta=\max_i\alpha_i$. In mode-Hessian radius
$r$, the certified theorem gives
$$
 e^{-\eta r}\widehat H\preceq H(\theta)\preceq e^{\eta r}\widehat H,
 \qquad
 g_-(r;\eta)\le U(\theta)-U(\hat\theta)\le g_+(r;\eta),
$$
with $g_\pm(r;\eta)=(e^{\pm\eta r}\mp\eta r-1)/\eta^2$. This yields explicit rowwise bulk
weights, a radial one-dimensional-quadrature tail bound, and—when the factor-one domain theorem
applies and $\eta<1$—$C_P\le K_d(\eta)\lambda_{\max}(\widehat H^{-1})$ with
$K_d(\eta)\to1$.

- **Why it matters:** this is the first fully data-computable A1 certificate and gives the A2
  Fisher coefficient in fixed-dimensional logistic sequences with vanishing maximal leverage.
- **Guardrail:** $\eta\ge1$ rejects this direct majorant; it does not say that the posterior lacks
  a Poincaré inequality. The prior/bulk-tail certificate remains available.
- **Used by:** A1 (`q:a1-barw`, `q:a1-tail`, `q:a1-sharp`), A2 (`q:a2-poincare`).

---

## Exact dual for unrestricted posterior-mean transport

For $X\sim\pi$,
$$
C_{\mathrm{mean},\mathrm{all}}(\pi)
=\sup_{\|u\|=1}\sup_{t\ne0}\frac{2}{t^2}
  \log\mathbb E e^{t u^\top(X-\mathbb EX)}.
$$
The manuscript and standalone agent-certified solution prove this exact equivalence from the
Gibbs variational formula. It is not merely a
sub-Gaussian upper bound. For a restricted family $\mathcal Q$, only
$C_{\mathrm{mean},\mathcal Q}\le C_{\mathrm{mean},\mathrm{all}}$ is automatic.

- **Used by:** A4 (`q:a4-mean`, `prop:a4-logistic-global`).
- **Caveat:** covariance does not lower-bound a restricted mean constant; the family must contain
  the corresponding entropy tilt or another explicit witness.

---

## Local VI calculus — three constants, not one

For a smooth variational family, local KL supplies a Fisher matrix $F$ and local $W_2$ supplies a
tangent Gram matrix $G$. The generalized eigenvalue
$\lambda_{\max}(F^{-1/2}GF^{-1/2})$ is the certified limit only in the well-specified case, or
for the optimizer-centred excess ratio
$$
 \frac{W_2^2(q,q_*)}{2\{\mathrm{KL}(q\|\pi)-\delta_{\mathcal Q}\}}.
$$
For a misspecified raw sublevel, the leading value is instead the approximation baseline
$W_2^2(q_*,\pi)/(2\delta_{\mathcal Q})$, generically followed by a $\sqrt\rho$ term. A fixed-
covariance Gaussian location family calibrates all three formulas exactly.

The unrestricted entropy-localized mean constant also has the exact tilt formula
$$
 \sup_{\|u\|=1}\sup_{0<r_u(t)\le r}
 \frac{\psi_u'(t)^2}{2r_u(t)},\qquad r_u(t)=t\psi_u'(t)-\psi_u(t),
$$
and is $\lambda_{\max}(\operatorname{Cov}\pi)+O(\sqrt r)$ under a common exponential-moment
contract.

- **Used by:** A4 (`prop:a4-mean-local`, `prop:a4-local-wellspecified`,
  `prop:a4-local-misspecified`, `prop:a4-local-excess`).
- **Guardrail:** an optimizer-centred excess constant measures optimization error around $q_*$;
  it is not by itself an approximation certificate for $q_*$ against $\pi$.

---

## thm:a3-product — product Hardy certificate

Writing $B_j=\max(B_{j,+},B_{j,-})$, the analytic tensorization draft gives
$$
\operatorname{Var}_{\otimes_j\mu_j}(f)
\le4\max_j B_j\int\sum_j a_j(x_j)|\partial_jf|^2\,d\mu.
$$
This is dimension-free in the weighted product metric. It does **not** extend from fixed
marginals to an arbitrary dependent joint law (`obs:marginals-not-joint`), and weak Poincaré
tensorization instead incurs a $d^{2/\alpha}$ loss for iid power tails.

---

## thm:a3-block-gibbs — the explicit dependence factor

Define
$$
 \gamma_{\rm blk}=\inf_f
 \frac{\sum_i\mathbb E\operatorname{Var}(f\mid X_{-i})}{\operatorname{Var}(f)}.
$$
Uniform conditional weighted Poincaré constants $C_i$ give the agent-certified bound
$C_{\rm joint}\le\max_iC_i/\gamma_{\rm blk}$. Products have $\gamma_{\rm blk}=1$; for two blocks,
the two-projections identity gives the exact value
$\gamma_{\rm blk}=1-\rho_{\max}(X,Y)$, with $\rho_{\max}$ the HGR maximal correlation.

- **Why it matters:** this turns A3's vague “dependence penalty” into a measurable spectral
  target and explains exactly how the fixed-marginal copula obstruction collapses the joint gap.
- **Used by:** A3 (`conj:a3-dependent`, `q:a3-hierarchical`).

---

## Symmetry averaging and block stability

For a finite isometric group and invariant target, $\bar q=|G|^{-1}\sum_g g_\#q$ preserves every
invariant observable while convexity gives
$\mathrm{KL}(\bar q\|\pi)\le\mathrm{KL}(q\|\pi)$ and
$W_2^2(\bar q,\pi)\le W_2^2(q,\pi)$. The ratio of those two decreasing quantities is not ordered,
and a variational family must admit the average.

For invariant measures with
$\operatorname{osc}\log(d\widetilde\pi/d\pi)\le\varepsilon$, direct density comparison changes
each invariant/non-invariant restricted Poincaré gap by at most $e^{\pm\varepsilon}$. Hence a
block ordering with log-margin greater than $2\varepsilon$ is stable.

- **Used by:** A4 (`lem:a4-symmetrization`), A5 (`prop:a5-block-stability`, `q:a5-detect`).
