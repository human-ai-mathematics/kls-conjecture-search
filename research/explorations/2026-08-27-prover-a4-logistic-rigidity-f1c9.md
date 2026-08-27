# A4 global logistic rigidity proof consolidation

**Date:** 2026-08-27
**Role:** `prover` (`/root/a4_logistic_prover`)
**Target:** `prop:a4-logistic-global`
**Outcome:** an unconditional standalone candidate dossier proves the current ledger and
manuscript statement. It remains unreviewed (`checked_by: none`) and therefore has no ledger
value.

## What was attempted

The manuscript's analytic draft was expanded into a self-contained proof of

$$
C_{\mathrm{mean},\mathcal Q}=C_{\mathcal Q}
=C_{\mathrm{mean},\mathrm{all}}=C_{\mathrm{TCI}}
=\lambda_{\max}(\Sigma_0)
$$

for every Gaussian variational family containing all translations of one fixed covariance. The
audit focused on the exact reverse-KL expansion, the mean lower bound for $W_2$, all nonzero
translation directions, the final generalized Rayleigh optimization, and the two equality
chains. No numerical work was run or used.

## Dependencies, status, and fences

- `prop:a2-logistic-global` is proved and supplies the exact upper endpoint
  $C_{\mathrm{TCI}}(\pi)=\lambda_{\max}(\Sigma_0)$.
- `eq:a4-mean-dual` is proved and identifies the unrestricted mean inequality, including its
  extended-value domain, with the centered directional log-MGF envelope. The Gaussian-prior
  posterior has the required first moment (indeed a small quadratic exponential moment).
- The dependency closure contains no unresolved premise, so the candidate result is
  unconditional.
- The target has no formal `bounded_by` edge. The full A4 guardrail audit is nevertheless clean:
  the conclusion realizes `obs:flat-direction` and `obs:gaussian-tail-rigidity` at prior scale;
  Gaussian quadratic tails and the global $T_2$ inequality avoid
  `obs:heavy-tail-no-classical` and `obs:restricted-not-finite`; and no multimodal or quotient
  claim engages `obs:symmetry-vs-physical`. The result is not a localized ELBO certificate, so it
  makes no approximation/optimization-error or computable-$\log Z$ assertion.

## Analytic derivation

Write $A=\Sigma_0^{-1}$ and

$$
\pi(d\theta)=Z^{-1}\exp\left[-\frac12(\theta-\mu_0)^T
A(\theta-\mu_0)-L(\theta)\right]d\theta.
$$

For a finite binary-logistic design,
$0\le L(\theta)\le a+b\|\theta\|$. Fix arbitrary $v\ne0$ and use the family members
$q_{t,v}=N(\mu_0+tv,S)$, where $S\succ0$ is fixed. The entropy of $q_{t,v}$ and its covariance
contribution to the prior energy are independent of $t$, while

$$
\frac12\mathbb E_{q_{t,v}}
[(\theta-\mu_0)^TA(\theta-\mu_0)]
=\frac12t^2v^TAv+\frac12\operatorname{tr}(AS),
\qquad
\mathbb E_{q_{t,v}}L=O(1+t).
$$

Consequently,

$$
2\operatorname{KL}(q_{t,v}\|\pi)=t^2v^T\Sigma_0^{-1}v+O(1+t),
$$

whereas, with $\bar\theta=\mathbb E_\pi\theta$,

$$
\|\mathbb E_{q_{t,v}}\theta-\bar\theta\|^2
=\|\mu_0+tv-\bar\theta\|^2=t^2\|v\|^2+O(1+t).
$$

Thus the exact directional limit is

$$
\lim_{t\to\infty}
\frac{\|\mathbb E_{q_{t,v}}\theta-\mathbb E_\pi\theta\|^2}
{2\operatorname{KL}(q_{t,v}\|\pi)}
=\frac{\|v\|^2}{v^T\Sigma_0^{-1}v}.
$$

For any coupling, Jensen gives
$W_2^2(q_{t,v},\pi)\ge\|\mathbb E_{q_{t,v}}\theta-\mathbb E_\pi\theta\|^2$.
Optimizing the last display over all $v\ne0$ gives

$$
\sup_{v\ne0}\frac{\|v\|^2}{v^T\Sigma_0^{-1}v}
=\lambda_{\max}(\Sigma_0),
$$

attained in any top eigendirection. The certified $T_2$ bound supplies every upper bound, so the
proof closes through

$$
\lambda\le C_{\mathrm{mean},\mathcal Q}\le C_{\mathcal Q}
\le C_{\mathrm{TCI}}=\lambda,
\qquad
\lambda\le C_{\mathrm{mean},\mathcal Q}\le C_{\mathrm{mean},\mathrm{all}}
\le C_{\mathrm{TCI}}=\lambda.
$$

Along a top eigendirection the mean lower bound and pointwise $T_2(\lambda)$ upper bound also
squeeze the transport ratio of the same remote Gaussian translations to $\lambda$.

## Dead ends and corrections retained

1. The manuscript shorthand $2\operatorname{KL}=t^2v^T\Sigma_0^{-1}v+O(|t|)$ hides why the
   fixed covariance does not change the leading coefficient. The dossier separates the Gaussian
   entropy, the trace term $\operatorname{tr}(\Sigma_0^{-1}S)$, the normalizer, and the
   at-most-linear likelihood expectation.
2. No closed formula for $W_2(N(\mu_0+tv,S),\pi)$ is available because $\pi$ is generally
   non-Gaussian. Attempting to compute it is unnecessary: the coupling mean bound supplies the
   lower estimate and the certified global $T_2$ inequality supplies the matching upper estimate
   in a top direction.
3. Checking only a preselected top direction would conceal the optimization step. The dossier
   proves the limit for every $v\ne0$ and then performs the exact Rayleigh optimization.
4. The covariance $S$ need not match either the prior or posterior covariance. Its only roles are
   positive definiteness, absolute continuity, and constancy along the translation ray.

## Hypotheses and unclosed steps

The proof uses exactly: a finite binary-logistic data set with finite covariates; a positive
definite Gaussian prior covariance; a Gaussian variational family containing every mean
translation of one fixed $S\succ0$; and the two proved dependencies above. The prior mean is
arbitrary, and no design-rank, identifiability, asymptotic, localization, or covariance-matching
hypothesis is used. There are no unclosed analytic steps and no unstated hypothesis known to the
author.

## Artifact, validation, and certification boundary

Candidate dossier: `solutions/prop-a4-logistic-global.tex`.

The dossier records `checked_by: none`; no ledger, manuscript, review, bibliography, or knowledge
file was edited. There is no applicable ledger delta at this stage. Only after a distinct
reviewer passes the dossier may the orchestrator atomically add the deferred candidate
`solution: solutions/prop-a4-logistic-global.tex` together with real review provenance.

The required standalone command
`cd solutions && latexmk -pdf -outdir=../build prop-a4-logistic-global.tex` succeeds and produces
`build/prop-a4-logistic-global.pdf`. The final log has no TeX errors or box warnings; its only
warnings are the expected standalone unresolved cross-module references to
`prop:a4-logistic-global`, `prop:a2-logistic-global`, and `thm:a4-mean-dual`.
