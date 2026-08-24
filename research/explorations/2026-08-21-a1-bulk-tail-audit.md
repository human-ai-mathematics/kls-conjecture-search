# A1 — bulk--tail statement audit and a sharp separable obstruction

- **Date:** 2026-08-21
- **Nodes:** `conj:a1`, `q:a1-poincare`, `q:a1-barw`, `q:a1-tail`, `q:a1-sharp`, `q:a1-lsi`
- **Type:** analytic audit; no new `finum` run and no numerical-evidence claim
- **Sources checked:** the repository statement and code, plus Cattiaux--Guillin,
  [*On the Poincaré Constant of Log-Concave Measures*](https://arxiv.org/abs/1810.08369),
  especially their Theorem 2.5 (Milman's equivalence of the log-concave spread and Poincaré
  constants), and Veysseire,
  [*Improved spectral gap bounds on positively curved manifolds*](https://arxiv.org/abs/1105.6080).
  The latter proves a factor-one harmonic-mean bound for compact reversible diffusions; this audit
  does not assume its extension to the noncompact Euclidean posterior.
- **Certification:** “proof draft” below means an analytic argument is recorded in the manuscript;
  it is not `status: proved` until a standalone solution receives the repository-required
  independent agent, human, or Lean check.

> **Same-day follow-up.** The later exploration
> [`2026-08-21-a1-harmonic-mean-and-mode-leverage.md`](2026-08-21-a1-harmonic-mean-and-mode-leverage.md)
> supplies a separate noncompact spectral-domain proof draft of factor one under a global
> two-sided Hessian bound, and an explicit log-Hessian-Lipschitz mode-leverage certificate.  Thus
> the source-applicability warning below remains correct for arbitrary noncompact strongly
> log-concave laws and unbounded Hessians, but bounded-Hessian Gaussian-prior logistic is no longer
> left unresolved.  Independent repository certification is still pending.

> **Later certification, 2026-08-21.** Under the user-authorized independent-agent review
> protocol, `/root/cross_review` accepted `prop:a1-euclidean-harmonic`,
> `prop:a1-mode-leverage`, and `cor:a1-leverage-asymptotic`; their consolidated proof is
> `solutions/a1-harmonic-mode-leverage.tex`.  The chronology above is preserved as the state at
> the time of this audit.  In particular, `prop:a1-bulk-tail` was not part of that review and
> remains an analytic draft.

## What was tried

I separated three claims that are currently bundled together in `conj:a1`:

1. the abstract inverse-Hessian Poincaré inequality;
2. the algebraic bulk--tail split for a fixed deterministic \(\bar W\);
3. existence of a **computable** \(\bar W\) for which the resulting bound improves on the prior
   scale and has the sharp \(1/n\) asymptotics.

I then tested the logical necessity of the tail term on an exactly analyzable one-observation
separable logistic family, and compared the resulting asymptotics with A2.

## Result 1 — analytic proof draft for the displayed abstract A1 inequality

**Status: analytic proof draft, conditional on the cited log-concave spread-to-gap theorem.**

Let \(\pi\propto e^{-U}\) be log-concave with \(U\in C^2\) strictly convex and
\(H=\nabla^2U\succ0\). Set
\[
  Q:=\mathbb E_\pi\lambda_{\max}(H^{-1}).
\]
For every smooth 1-Lipschitz \(f\), Brascamp--Lieb gives
\[
  \operatorname{Var}_\pi(f)
  \le \mathbb E_\pi\langle H^{-1}\nabla f,\nabla f\rangle
  \le Q.
\]
Thus the squared spread constant
\(
S^2(\pi):=\sup_{\|f\|_{\rm Lip}\le1}\operatorname{Var}_\pi(f)
\)
satisfies \(S^2(\pi)\le Q\). Milman's equivalence for log-concave measures, in the
\((2,\infty)\)-to-\((2,2)\) form recorded by Cattiaux--Guillin Theorem 2.5, supplies a universal
\(C_M<\infty\) such that
\[
  C_P(\pi)\le C_M S^2(\pi)\le C_M Q.                 \tag{A1.1}
\]
(Their theorem is stated with a universal comparison constant, not a factor asymptotic to one.)

For any deterministic diagonal \(\bar W\succeq0\), on
\[
G_{\bar W}=\{X^TW(\theta)X\succeq X^T\bar W X\},
\qquad A_{\bar W}=\Sigma_0^{-1}+X^T\bar W X,
\]
Loewner inversion gives \(H^{-1}\preceq A_{\bar W}^{-1}\). Everywhere,
\(H^{-1}\preceq\Sigma_0\). Consequently
\[
 Q\le \lambda_{\max}(A_{\bar W}^{-1})
   +\mathbb E_\pi[\lambda_{\max}(H^{-1});G_{\bar W}^c]
 \le \lambda_{\max}(A_{\bar W}^{-1})
   +\lambda_{\max}(\Sigma_0)\pi(G_{\bar W}^c).       \tag{A1.2}
\]
Equations (A1.1)--(A1.2) prove the formal two inequalities displayed in `conj:a1`.

**What remains open.** The substantive conjecture is not (A1.1)--(A1.2), but a selection theorem:
construct \(\bar W=\bar W(X,y,\Sigma_0)\) for which (A1.2) is both certified and substantially
smaller than \(\lambda_{\max}(\Sigma_0)\). The pre-audit wording bundled the abstract lemma with
this genuinely GLM-specific target; the integrated manuscript and ledger now separate them.

## Result 2 — an analytic family makes the mode-Hessian tail-free ratio diverge

**Status: analytic counterexample draft.** This strengthens the dirty finite-run obstruction from one numerical ratio to
an unbounded family.

Take one dimension, prior \(N(0,\sigma^2)\), one positive logistic observation, and covariate
\(x=a>0\):
\[
  \pi_a(d\theta)\propto
  \exp\!\left(-\frac{\theta^2}{2\sigma^2}\right)\operatorname{sigmoid}(a\theta)\,d\theta.
\]
By symmetry,
\(\mathbb E_{N(0,\sigma^2)}\operatorname{sigmoid}(a\Theta)=1/2\). Hence the density of
\(\pi_a\) relative to the Gaussian is exactly \(2\operatorname{sigmoid}(a\theta)\). Dominated
convergence gives total-variation and second-moment convergence
\[
  \pi_a\longrightarrow N(0,\sigma^2)\mid\{\theta>0\},
  \qquad
  \operatorname{Var}_{\pi_a}(\theta)\longrightarrow
  \sigma^2\left(1-\frac2\pi\right).                  \tag{A1.3}
\]
Therefore the linear test gives
\(C_P(\pi_a)\ge\operatorname{Var}_{\pi_a}(\theta)\), bounded away from zero.

Let \(\hat\theta_a\) be the mode and \(s_a=a\hat\theta_a\). The score equation is
\[
  s_a(1+e^{s_a})=a^2\sigma^2,
\]
so \(s_a\to\infty\) (indeed \(s_a\asymp W(a^2\sigma^2)\)). With
\(w(s)=\operatorname{sigmoid}(s)(1-\operatorname{sigmoid}(s))\), the inverse mode Hessian is
\[
  B_a:=\left(\sigma^{-2}+a^2w(s_a)\right)^{-1}
      =\frac{\sigma^2}{1+s_a\operatorname{sigmoid}(s_a)}
      \longrightarrow0.                              \tag{A1.4}
\]
Combining (A1.3)--(A1.4),
\[
  \frac{C_P(\pi_a)}{B_a}\longrightarrow\infty.
\]
Thus **no universal finite \(C\)** can validate the tail-free mode-curvature claim
\(C_P\le C(\sigma^{-2}+a^2w(a\hat\theta_a))^{-1}\).

For the mode choice \(\bar w=w(s_a)\), evenness and monotonicity of \(w\) in \(|s|\) give
\[
  G_{\bar w}=\{|\theta|\le\hat\theta_a\}.
\]
Since \(\hat\theta_a=s_a/a\to0\), \(\pi_a(G_{\bar w})\to0\). The crude corrected expression
therefore tends to the prior scale \(\sigma^2\), exactly as it should. The tail term is not a
minor proof loss in this family; it carries essentially the whole bound.

This also sharpens the meaning of `obs:flat-direction`: a tail-free **prior** bound always exists
(take \(\bar W=0\)). What is impossible is a universal tail-free improvement based on the
positive mode/observed likelihood curvature.

## Result 3 — exact A1--A2 scale bookkeeping

**Status: analytic conditional implication.** Suppose along a regular fixed-dimensional sequence
there are deterministic/data-measurable \(\bar W_n\) such that
\[
  n^{-1}A_{\bar W_n}\ \xrightarrow{P}\ I(\theta_0),
  \qquad
  n\,\mathbb E_{\pi_n}[\lambda_{\max}(H_n^{-1});G_{\bar W_n}^c]
  \xrightarrow{P}0.                                  \tag{A1.5}
\]
Then (A1.1)--(A1.2) imply only
\[
  \limsup nC_P(\pi_n)\le C_M\lambda_{\max}(I(\theta_0)^{-1}). \tag{A1.6}
\]
For the crude probability correction, the sufficient tail condition is the much stronger
\(n\pi_n(G_{\bar W_n}^c)\to0\). A typical rowwise route with bounded design would take a
mode-centred radius \(r_n=M_n/\sqrt n\), with \(M_n\to\infty\), \(M_n=o(\sqrt n)\), and enough
concentration (for example \(M_n\asymp\sqrt{\log n}\)) to make the complement \(o(1/n)\).

Equation (A1.6) is rate-consistent with A2, but it does **not** recover A2's exact coefficient
unless the universal spread-to-gap loss is replaced by a \(1+o(1)\) spectral-stability argument.
That is a separate sharpness lemma; it cannot follow merely by choosing a better \(\bar W_n\).

## Global LSI/transport warning for the A1 second stage

For every finite binary-logistic likelihood and fixed Gaussian prior,
\[
  C_{\rm LS}(\pi)=C_{\rm TCI}(\pi)=\lambda_{\max}(\Sigma_0).  \tag{A1.7}
\]
This is proved in full in
[`2026-08-21-a2-strong-laplace-and-global-constants.md`](2026-08-21-a2-strong-laplace-and-global-constants.md).
In brief, the logistic loss has only linear growth, so arbitrarily large exponential tilts retain
the Gaussian prior's quadratic log-MGF coefficient. A global \(T_2(C)\) inequality forces
\(C\ge\lambda_{\max}(\Sigma_0)\), while Bakry--Émery and Otto--Villani give the reverse upper
bounds. Thus a bulk-improved global LSI/\(T_2\) is impossible for this flagship model; local,
restricted, or warm-start inequalities remain meaningful.

## Audit of the existing `finum` artifact

`research/runs/2026-06-20-A1.jsonl` is dirty and evidence-ineligible. It is useful only as a
historical diagnostic.

- The A1 code evaluates \(\bar W=W(\hat\theta)\) and the **tail-free** `bulk_bound`; it never
  computes \(G_{\bar W}\), \(\pi(G_{\bar W}^c)\), or the integrated-tail expression in
  `conj:a1`.
- `stress-logit-separable` refutes the factor-one mode bound on that finite instance
  (linear lower bound \(3.4163\) versus bulk \(2.6283\)); Result 2 above supplies the missing
  unbounded analytic family.
- `stress-wide` has `no-verdict` because its covariance lower estimate \(6.1199\) exceeded the
  proved prior bound \(5\), so the shared A1 battery did not pass.
- `consistent` in the other rows means only “not refuted by this lower bound,” never that the
  upper bound holds.

Accordingly there is no support for `numerical-strong`, and no such claim is made here.

## Refined proof and test frontier

1. Resolve whether Veysseire's compact harmonic-mean factor-one result applies directly to the
   noncompact Euclidean posterior, or retain and make explicit the universal spread-to-gap factor
   in (A1.1); then submit the resulting lemma for independent certification.
2. Restate the positive A1 target as existence of a computable \(\bar W\) with a certified
   improvement, not merely the inequality valid for every \(\bar W\).
3. For `q:a1-sharp`, prove a local spectral-stability theorem with multiplicative
   \(1+o(1)\); the universal Milman comparison cannot yield the exact A2 coefficient.
4. Extend `finum.targets.a1` to record the actual event, both tail corrections, and uncertainty
   on their estimates. Add the one-dimensional \(a\)-sweep above as an analytic calibration.
5. Redirect `q:a1-lsi` for Gaussian-prior logistic toward local/restricted constants; any global
   improvement contradicts (A1.7).
