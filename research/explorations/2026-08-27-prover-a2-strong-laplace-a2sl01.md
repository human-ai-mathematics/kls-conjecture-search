# A2 strong-Laplace transfer proof consolidation

**Date:** 2026-08-27
**Role:** prover (/root/a3_prior_prover)
**Target:** thm:a2-target
**Outcome:** an unconditional candidate proof of the current strong-Laplace implication was
written as a standalone dossier. It remains unreviewed (checked_by: none) and has no ledger value.

## What was attempted

The short manuscript proof was expanded into a deterministic comparison lemma applied
realization-by-realization to the random posterior. The audit focused on:

1. normalization of the density $e^{-r_n}$ and the bounds implied by
   $\delta_n=\operatorname{osc}(r_n)$;
2. the exact Holley--Stroock factor under the repository normalization;
3. covariance convergence in whitened coordinates and relative Loewner control after
   anisotropic unwhitening;
4. distinct covariance lower bounds for Poincaré, LSI, and $T_2$;
5. the meaning of every $o_P(1)$ statement and the inverse-matrix/eigenvalue limit.

No numerical work was run or used.

## Ledger closure and fences

The node thm:a2-target has no depends_on edge. It refines conj:a2 and has the single formal fence
obs:tv-insufficient. The proof uses the accepted manuscript toolkit (Gaussian calibration,
Holley--Stroock, LSI implies Poincaré, and Otto--Villani), but no unresolved ledger premise.

The formal fence is respected because the hypothesis gives a global $L^\infty$ density-ratio
comparison, not total-variation convergence. The neighboring proved obstruction
obs:gaussian-tail-rigidity is also respected: the conclusion is asserted only for a posterior
globally comparable, with vanishing oscillation, to its mode Gaussian. Ordinary fixed-prior
logistic posteriors are not asserted to satisfy that hypothesis.

## Deterministic comparison on one data realization

Let $\gamma=N(0,I_d)$ and

\[
 q(z)=\frac{e^{-r(z)}}{\mathcal Z},\qquad
 \mathcal Z=\int e^{-r}\,d\gamma,\qquad
 \delta=\operatorname{ess\,sup}r-\operatorname{ess\,inf}r.
\]

If $a=\operatorname{ess\,inf}r$ and $b=\operatorname{ess\,sup}r$, then
$e^{-b}\le\mathcal Z\le e^{-a}$. Hence

\[
 e^{-\delta}\le q\le e^\delta,\qquad
 \|q-1\|_\infty\le\eta:=e^\delta-1.
\]

The first line is the normalized density-ratio audit. It is used for moments. For the
functional-inequality upper bounds, Holley--Stroock is applied to the unnormalized perturbing
potential $r$, whose oscillation is $\delta$. It therefore gives the factor $e^\delta$, not
$e^{2\delta}$.

Let $T(z)=\hat\theta+H^{-1/2}z$ and
$G=T_\#\gamma=N(\hat\theta,H^{-1})$. Since
$C_P(G)=C_{\rm LS}(G)=\lambda_{\max}(H^{-1})$, Holley--Stroock and Otto--Villani give

\[
 C_P(\pi),\ C_{\rm LS}(\pi),\ C_{\rm TCI}(\pi)
 \le e^\delta\lambda_{\max}(H^{-1}).
\]

## Covariance convergence and unwhitening

For the whitened law, put

\[
 m=\int zq\,d\gamma,\qquad
 M=\int zz^\top q\,d\gamma,\qquad
 \Sigma=M-mm^\top.
\]

The uniform ratio bound gives

\[
 \|m\|\le\eta\sqrt d,\qquad
 \|M-I_d\|_{\rm op}\le\eta,\qquad
 \|\Sigma-I_d\|_{\rm op}\le\eta+d\eta^2=:\varepsilon.
\]

Thus, when $\varepsilon<1$,

\[
 (1-\varepsilon)I_d\preceq\Sigma\preceq(1+\varepsilon)I_d.
\]

Congruence by $H^{-1/2}$ gives the relative, anisotropy-preserving statement

\[
 (1-\varepsilon)H^{-1}
 \preceq\operatorname{Cov}_\pi
 \preceq(1+\varepsilon)H^{-1}.
\]

This is stronger and cleaner than trying to control an absolute covariance error before
unwhitening.

## Three lower bounds

For linear tests, the Poincaré Rayleigh quotient yields

\[
 C_P(\pi)\ge\lambda_{\max}(\operatorname{Cov}_\pi),
\]

and LSI linearization gives $C_{\rm LS}\ge C_P$.

There is no general ordering that would give the transport lower bound from Poincaré. It is
proved separately under the repository convention
$W_2^2(\nu,\mu)\le2C\operatorname{KL}(\nu\|\mu)$. The entropy variational formula and
$W_1\le W_2$ imply for $f_v(x)=v^\top x$ that

\[
 \log\mathbb E_\mu e^{t(f_v-\mathbb E_\mu f_v)}
 \le \sup_{k\ge0}\{|t|\|v\|\sqrt{2Ck}-k\}
 =\frac{Ct^2\|v\|^2}{2}.
\]

Expansion at zero gives
$v^\top\operatorname{Cov}_\mu v\le C\|v\|^2$, hence

\[
 C_{\rm TCI}(\mu)\ge\lambda_{\max}(\operatorname{Cov}_\mu).
\]

All three constants consequently obey

\[
 1-\varepsilon
 \le
 \frac{C(\pi)}{\lambda_{\max}(H^{-1})}
 \le e^\delta.
\]

## Probabilistic quantifiers and matrix limit

All deterministic estimates are applied conditionally on the data. Fixed dimension and
$\delta_n=o_P(1)$ imply

\[
 \eta_n=e^{\delta_n}-1=o_P(1),\qquad
 \varepsilon_n=\eta_n+d\eta_n^2=o_P(1).
\]

The sandwich therefore proves, separately for $C_P$, $C_{\rm LS}$, and $C_{\rm TCI}$,

\[
 \frac{C(\pi_n)}{\lambda_{\max}(H_n^{-1})}
 \xrightarrow{P_{\theta_0}}1.
\]

Writing $B_n=H_n/n$, the hypothesis $B_n\to I(\theta_0)\succ0$ in operator norm in probability
puts $B_n$ in the positive-definite cone with probability tending to one. Continuity of inversion
gives the matrix limit

\[
 nH_n^{-1}=B_n^{-1}
 \xrightarrow{P_{\theta_0}}I(\theta_0)^{-1}.
\]

Continuity of $\lambda_{\max}$ and Slutsky then give the stated $n$-scaled limits for all three
constants.

## Hypothesis audit

- Fixed $d$ is used in $\varepsilon_n=\eta_n+d\eta_n^2=o_P(1)$.
- $H_n/n\to I(\theta_0)\succ0$ provides high-probability positive definiteness and the final
  inverse-matrix limit.
- The global density representation and $\operatorname{osc}(r_n)=o_P(1)$ provide every upper
  bound and moment comparison.
- The mode $\hat\theta_n$ is only a translation.
- Once the two analytic inputs above are assumed, interiority of $\theta_0$, smooth positivity of
  the prior near $\theta_0$, and general model regularity are not separately used in the transfer
  proof. They are the statistical context intended to produce those inputs.

The implication is therefore unconditional under its explicit hypotheses. Verifying global
vanishing oscillation in a useful model, or replacing it by weaker spectral stability, remains a
different open problem.

## Dead ends and corrections retained

1. Combining the loose normalized bounds $e^{-\delta}\le q\le e^\delta$ by a naive
   maximum/minimum comparison can obscure the sharp perturbation factor. Holley--Stroock must be
   applied to $r$ itself and gives $e^{\operatorname{osc}(r)}$.
2. Total variation or local Laplace convergence was not substituted for global comparison; the
   certified contamination obstruction shows why that route fails.
3. The $T_2$ lower bound was not inferred from $C_P\le C_{\rm LS}$, because no such ordering with
   $T_2$ exists. The separate entropy-dual covariance argument closes it.
4. An absolute estimate on
   $H^{-1/2}(\Sigma-I)H^{-1/2}$ hides the relevant matrix scale. The relative Loewner sandwich
   gives the correct multiplicative eigenvalue bound directly.
5. The shorthand $H_n^{-1}\sim n^{-1}I(\theta_0)^{-1}$ was replaced by the explicit
   high-probability positive-definiteness, continuous-inversion, and eigenvalue argument.

## Artifact and certification boundary

Candidate dossier: solutions/thm-a2-target.tex.

The dossier records checked_by: none. No manuscript, ledger, review, knowledge, bibliography, or
numerical file was edited. A future solution field may point to this path only atomically with a
real independent certification.

## Validation

- Running
  $\,\texttt{cd solutions \&\& latexmk -pdf -outdir=../build thm-a2-target.tex}\,$ succeeds and
  produces build/thm-a2-target.pdf (four pages).
- The final log has no TeX errors and no overfull or underfull boxes. Its only warning is the
  expected standalone unresolved reference to the cross-module label thm:a2-target.
- Running $\,\texttt{python3 research/check\_ledger.py}\,$ after the final source audit reports
  2 ledgers, 174 nodes, 636 labels, and 0 errors.
