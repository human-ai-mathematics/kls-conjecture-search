---
type: proof-review
date: "2026-08-27"
verdict: pass
authors:
  - /root/a4_logistic_prover
reviewer: /root/a3_prior_review
nodes:
  - prop:a4-logistic-global
solutions:
  - solutions/prop-a4-logistic-global.tex
---

# A4 global logistic rigidity — independent proof review

This is a cold review of `solutions/prop-a4-logistic-global.tex`, whose reviewed SHA-256 is
`11715df143046b87387d677b7d4023e9676cafa02c3544ae09ca51c4bd3b1f69`.  The proof was
reconstructed from the dossier, ledger, manuscript, certified dependency dossiers, and review
archive.  The author's exploration narrative was not used as evidence, and the reviewer is
distinct from the author.

## Findings

### Statement agreement and dependency closure

The ledger statement, Proposition `\label{prop:a4-logistic-global}` in the A4 manuscript, and the
dossier agree mathematically.  For a finite binary-logistic posterior with prior
$N(\mu_0,\Sigma_0)$, $\Sigma_0\succ0$, and a Gaussian family $\mathcal Q$ containing
$N(a,S)$ for every $a\in\mathbb R^d$ at one fixed $S\succ0$, they assert
$$
C_{\mathrm{mean},\mathcal Q}=C_{\mathcal Q}
=C_{\mathrm{mean},\mathrm{all}}=C_{T_2}=\lambda_{\max}(\Sigma_0)
$$
in the repository convention $W_2^2\le 2C_{T_2}\operatorname{KL}$.  The dossier makes the prior
mean and admissible finite-KL domains explicit without strengthening the mathematical claim.

Both ledger dependencies are discharged.  `prop:a2-logistic-global` is proved and independently
certified, as is its dependency `prop:a2-subquadratic-global`; its exact conclusion in the same
normalization is $C_{T_2}(\pi)=\lambda_{\max}(\Sigma_0)$.  `eq:a4-mean-dual` is likewise proved
and independently certified and covers the extended-valued unrestricted mean domain.  The latter
is consistent with, but not essential to, the shorter upper-bound argument from $T_2$; this is
redundant dependency strength, not a proof gap.  No external theorem beyond these certified
repository dependencies, no preprint, and no numerical artifact enters the argument.

### Posterior tails and upper chains

For $s=x_i^T\theta$ and $y_i\in\{0,1\}$, each logistic summand is either
$\log(1+e^s)$ or $\log(1+e^{-s})$.  It is therefore nonnegative and at most
$\log 2+|s|$.  Finiteness of the design gives constants $a,b<\infty$ with
$0\le L(\theta)\le a+b\|\theta\|$.  Consequently the posterior normalizer is positive and
finite, and Gaussian domination supplies $\int e^{\varepsilon\|\theta\|^2}\,d\pi<\infty$ for
all sufficiently small $\varepsilon>0$.

Applying the entropy inequality first to truncated versions of
$\varepsilon\|\theta\|^2$ shows that every competitor with finite reverse KL has a finite second
moment.  Hence all relevant Wasserstein distances and means are well defined.  Jensen's inequality
under every coupling gives
$$
\|\mathbb E_q\theta-\mathbb E_\pi\theta\|^2\le W_2^2(q,\pi),
$$
and the certified exact $T_2$ result gives the two upper chains
$$
C_{\mathrm{mean},\mathcal Q}\le C_{\mathcal Q}\le\lambda_{\max}(\Sigma_0),
\qquad
C_{\mathrm{mean},\mathcal Q}\le C_{\mathrm{mean},\mathrm{all}}
\le\lambda_{\max}(\Sigma_0).
$$
This also checks the domain passage asserted through the unrestricted mean dual.

### Exact translation asymptotics

Put $A=\Sigma_0^{-1}$ and $q_{t,v}=N(\mu_0+tv,S)$ for fixed $v\ne0$.  The location-rich
hypothesis puts every such law in $\mathcal Q$.  Direct expansion, including every fixed term,
gives
$$
\operatorname{KL}(q_{t,v}\|\pi)
=-h(N(0,S))+\log Z
+\frac12t^2v^TAv+\frac12\operatorname{tr}(AS)
+\mathbb E_{q_{t,v}}L.
$$
The entropy, normalizer, and trace terms are independent of $t$.  If $G\sim N(0,S)$, the linear
likelihood bound gives
$$
0\le\mathbb E_{q_{t,v}}L
\le a+b\bigl(\|\mu_0+tv\|+\mathbb E\|G\|\bigr)=O(1+t).
$$
Thus the coefficient and normalization in the dossier are exact:
$$
2\operatorname{KL}(q_{t,v}\|\pi)=t^2v^T\Sigma_0^{-1}v+O(1+t).
$$
Every witness has finite KL, and positivity of $v^T\Sigma_0^{-1}v$ makes it admissible for all
sufficiently large $t$.

Writing $\bar\theta=\mathbb E_\pi\theta$ gives the separate exact expansion
$$
\|\mu_0+tv-\bar\theta\|^2=t^2\|v\|^2+O(1+t).
$$
Moreover, Jensen under any coupling gives
$W_2^2(q_{t,v},\pi)\ge\|\mu_0+tv-\bar\theta\|^2$; no equality or covariance match between
$S$ and the posterior is assumed.  Therefore
$$
\lim_{t\to\infty}
\frac{\|\mathbb E_{q_{t,v}}\theta-\mathbb E_\pi\theta\|^2}
     {2\operatorname{KL}(q_{t,v}\|\pi)}
=\frac{\|v\|^2}{v^T\Sigma_0^{-1}v}.
$$
The direction $v$ is arbitrary, and Rayleigh optimization yields
$$
\sup_{v\ne0}\frac{\|v\|^2}{v^T\Sigma_0^{-1}v}
=\lambda_{\max}(\Sigma_0).
$$
This proves the matching lower bound for both the restricted mean and restricted transport
constants.  Combining it with the first upper chain gives
$\lambda\le C_{\mathrm{mean},\mathcal Q}\le C_{\mathcal Q}\le C_{T_2}=\lambda$; combining it
with the second gives
$\lambda\le C_{\mathrm{mean},\mathcal Q}\le C_{\mathrm{mean},\mathrm{all}}
\le C_{T_2}=\lambda$.  These are the two required equality chains.

### Hypothesis accounting and fences

The proof uses $\Sigma_0\succ0$ for Gaussian tails and the positive Rayleigh denominator; finite
binary responses and finite covariates for convexity and the global linear likelihood bound; and
$S\succ0$ plus inclusion of every translation for admissible remote witnesses.  The arbitrary
prior mean is retained exactly.  The Gaussian nature of members of $\mathcal Q$ outside the one
included translation family is not used: the upper bound holds for arbitrary competitors, while
the lower bound needs only those witnesses.  This unused strength is a possible sharpening, not a
defect.

The node has no formal `bounded_by` edge.  The A4-wide fences are nevertheless respected.
`obs:flat-direction` and `obs:gaussian-tail-rigidity` are realized rather than contradicted: the
remote translations recover the prior scale, not a posterior/Fisher scale.
`obs:heavy-tail-no-classical` and `obs:restricted-not-finite` do not apply because the Gaussian
prior supplies quadratic-exponential tails and the certified global $T_2$ inequality makes the
restricted constant finite.  `obs:symmetry-vs-physical` is not invoked: there is no multimodal,
spectral, quotient, or symmetry-improvement claim.  The proposition is global and does not claim
a localized ELBO certificate or a computable KL error bar.

### Mechanical validation

`cd solutions && latexmk -g -pdf -outdir=../build prop-a4-logistic-global.tex` succeeds and
produces a two-page PDF.  The only LaTeX warnings are the expected standalone unresolved parent
references to the proposition and its two certified dependencies; there are no TeX errors or
unresolved citations.

## Corrections

None.

## Exclusions

This review does not certify localized A4 constants, posterior/Fisher-scale global improvement,
variational families lacking the stated translation witnesses, heavy-tailed targets, quadratic
or superquadratic likelihood tails, or a computable upper bound on the variational KL.  It checks
the status and exact conclusions used from the two dependency nodes but does not create a new
certification event for those already certified nodes.
