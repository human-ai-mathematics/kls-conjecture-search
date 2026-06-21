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
  $C_P \le B$ has $\lambda_{\max}(\mathrm{Cov}_\pi) > B$, the conjecture is false (mod. numerical error).
- **finum:** `constants.poincare_lower(samples) = ` $\lambda_{\max}$(empirical cov); richer
  test-function bases (quadratic, RBF) and the Pillaud-Vivien estimator give a tighter two-sided
  $\hat C_P$.
- **Used by:** A1 (`q:a1-sharp`), A2 (`conj:a2`, the contamination falsification), A4 (`q:a4-mean`),
  A5 (`q:a5-detect`).

---

## thm:hardy-1d — the 1D weighted Hardy/Muckenhoupt criterion
A weighted Poincaré $\mathrm{Var}_\mu(f) \le C \int a\,|f'|^2\,d\mu$ on $\mathbb R$ holds iff the
Hardy quantities $B_\pm = \sup_{x \gtrless m} \mu(\text{tail}) \int_m^x dt/(a(t)p(t))$ are finite,
pinning the optimal constant up to factor 4: $\max(B_+,B_-) \le C_{\mathrm{opt}} \le 4\max(B_+,B_-)$.

- **Why it matters:** turns "does a tail-index-dependent constant exist, and what is it" into a
  single explicit supremum — closed form for Student-$t$/horseshoe, numeric otherwise.
- **finum:** evaluate the Hardy supremum numerically for any 1D marginal; combine with
  tensorization for product priors.
- **Used by:** A3 (`conj:a3`, `prop:a3-horseshoe`, `q:a3-catalogue`).

---

## Holley–Stroock $e^{\mathrm{osc}}$ transfer
If $\pi = e^{-W}\nu/Z$ with $\mathrm{osc}(W) \le A$, then $C_P(\pi) \le e^A C_P(\nu)$ (same for
$C_{\mathrm{LS}}$). With $\mathrm{osc}\to0$ the constants transfer *exactly*.

- **Why it matters:** the clean device behind A2's "BvM Gaussian computes the constants": if the
  rescaled posterior is an $o_P(1)$-oscillation reweighting of its Gaussian, the Gaussian constants
  transfer with factor $1+o_P(1)$.
- **Used by:** A2 (`thm:a2-target`), A1-bis.

---

## Tensorization (weighted and unweighted)
For a product $\mu = \bigotimes_i \mu_i$, $C_P(\mu) = \max_i C_P(\mu_i)$ (weighted analogue:
$\mathrm{Var}_\mu(f) \le (\max_i C_i) \int \sum_i a_i\,|\partial_i f|^2\,d\mu$). Dimension-free.

- **Used by:** A3 (product priors, `eq:a3-tensor`), A5 (Neal funnel non-centered law).
- **Caveat:** hierarchical posteriors are **not** products — tensorization is the easy half; the
  conditional-variance decomposition with unbounded conditional scales is the hard half
  (`q:a3-hierarchical`).

---

## lem:a5-lipschitz — Lipschitz transport of all three constants
$T_\#\nu = \mu$ with $T$ globally $L$-Lipschitz $\Rightarrow C_P(\mu) \le L^2 C_P(\nu)$ (same for
$C_{\mathrm{LS}}$, $C_{\mathrm{TCI}}$).

- **Why it matters:** makes "non-centering improves the constant" precise — it is a statement about
  *which metric the sampler sees*. A funnel is where the centered$\leftrightarrow$non-centered map
  fails to be bi-Lipschitz, so the lemma applies only one way and the constants genuinely differ.
- **Used by:** A5 (`q:a5-reparam`, `ex:a5-neal`).

---

## Brascamp–Lieb + log-concave self-improvement
For strictly convex $U$: $\mathrm{Var}_\pi(f) \le \mathbb E_\pi\langle H(\theta)^{-1}\nabla f,\nabla f\rangle$.
This is *not yet* a Poincaré inequality (curvature and gradient stay coupled); the
Milman/Veysseire log-concave self-improvement (Cattiaux–Guillin) promotes it to
$C_P \lesssim \mathbb E_\pi \lambda_{\max}(H(\theta)^{-1})$.

- **Why it matters:** the skeleton of A1 (`eq:a1-cfg`) and the bulk constant of A4.
- **Note:** the operative quantity is $\mathbb E_\pi \lambda_{\max}(H^{-1})$ (average *inverse*
  curvature), not $\lambda_{\max}((\mathbb E_\pi H)^{-1})$ — matrix inversion is operator-convex, so
  the tail of $W(\theta)$ is structurally part of the problem (ties back to `obs:flat-direction`).
- **Used by:** A1 (`q:a1-poincare`), A4 (`q:a4-restricted`).
