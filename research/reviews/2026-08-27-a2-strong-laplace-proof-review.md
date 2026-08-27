---
type: proof-review
date: "2026-08-27"
verdict: pass
authors:
  - /root/a3_prior_prover
reviewer: /root/a3_prior_review
nodes:
  - thm:a2-target
solutions:
  - solutions/thm-a2-target.tex
---

# A2 strong-Laplace transfer — independent proof review

This is a cold review of `solutions/thm-a2-target.tex`, whose reviewed SHA-256 is
`d6deec5171f867218de151cd2a696c06f3b103ba60d9897664f60101e96bf3a7`.  The proof was
reconstructed from the dossier, ledger, manuscript, certified obstruction, and actual published
sources.  The author's exploration narrative was not used as evidence, and the reviewer is
distinct from the author.

## Findings

### Statement agreement and status

The ledger, manuscript theorem at `\label{thm:a2-target}`, and dossier agree mathematically.  In
fixed dimension they assume $H_n/n\to I(\theta_0)\succ0$ in probability and a global whitened
density representation
$$
\frac{d\bar\pi_n}{d\gamma}=\frac{e^{-r_n}}{\int e^{-r_n}\,d\gamma},
\qquad \operatorname{osc}(r_n)=o_P(1),
$$
and conclude that $C_{\rm P}$, $C_{\rm LS}$, and $C_{\rm TCI}$ are all
$(1+o_P(1))\lambda_{\max}(H_n^{-1})$, hence their products by $n$ converge to
$\lambda_{\max}(I(\theta_0)^{-1})$.  The dossier's relative-limit formulation makes the meaning
of the random multiplicative error precise and is equivalent to the manuscript statement.

The node has no unresolved ledger dependency.  The two external mechanisms actually used are
published: Holley--Stroock, *Journal of Statistical Physics* 46 (1987), DOI
`10.1007/BF01011161`, and Otto--Villani, *Journal of Functional Analysis* 173 (2000), DOI
`10.1006/jfan.1999.3557`.  Their conventions match the repository statements.  Gaussian
calibration and LSI linearization are also proved in the manuscript toolkit.  No
preprint-unreviewed result or numerical observation enters the proof.

### Normalized density ratio and bounded perturbation

For $a_n=\operatorname*{ess\,inf}r_n$, $b_n=\operatorname*{ess\,sup}r_n$, and
$\delta_n=b_n-a_n$, probability normalization gives
$e^{-b_n}\le\mathcal Z_n\le e^{-a_n}$.  Therefore
$$
e^{-\delta_n}\le q_n\le e^{\delta_n},
\qquad \|q_n-1\|_\infty\le e^{\delta_n}-1.
$$
The second inequality uses both sides correctly, since
$1-e^{-\delta}\le e^\delta-1$.  After the affine unwhitening, the perturbing potential remains
$r_n\circ T_n^{-1}$ and has oscillation exactly $\delta_n$.

In the repository normalization
$\operatorname{Ent}(f^2)\le2C_{\rm LS}\int|\nabla f|^2$,
Holley--Stroock costs the density ratio $\sup q/\inf q=e^{\delta_n}$, equivalently one
oscillation of the unnormalized potential.  It does not cost $e^{2\delta_n}$.  Thus both
$C_{\rm P}$ and $C_{\rm LS}$ are at most $e^{\delta_n}\lambda_n$ for
$\lambda_n=\lambda_{\max}(H_n^{-1})$.  Otto--Villani under
$W_2^2\le2C_{\rm TCI}\operatorname{KL}$ gives
$C_{\rm TCI}\le C_{\rm LS}$ with no further factor.

### Covariance and transportation lower bounds

Writing $\eta_n=e^{\delta_n}-1$, the first-moment estimate
$\|m_n\|\le\eta_n\sqrt d$ and the quadratic-form estimate
$\|M_n-I_d\|_{\rm op}\le\eta_n$ are exact.  Hence
$$
\|\operatorname{Cov}_{\bar\pi_n}-I_d\|_{\rm op}
\le\eta_n+d\eta_n^2=:\varepsilon_n=o_P(1),
$$
where fixed dimension is used.  Congruence by $H_n^{-1/2}$ preserves the entire anisotropic
Loewner comparison:
$$
(1-\varepsilon_n)H_n^{-1}
\preceq\operatorname{Cov}_{\pi_n}
\preceq(1+\varepsilon_n)H_n^{-1}.
$$
In particular its largest eigenvalue is at least
$(1-\varepsilon_n)\lambda_n$; no isotropic replacement or condition-number loss is introduced.

Linear tests give $C_{\rm P}\ge\lambda_{\max}(\operatorname{Cov})$, and LSI linearization gives
$C_{\rm LS}\ge C_{\rm P}$.  The $T_2$ lower bound is checked separately, as required.  The
entropy variational formula, $W_1\le W_2$, and the repository $T_2(C)$ convention give
$$
\log\mathbb E e^{t(v^TX-\mathbb Ev^TX)}
\le\sup_{k\ge0}\{|t|\|v\|\sqrt{2Ck}-k\}
=\frac{Ct^2\|v\|^2}{2}.
$$
Differentiation at zero yields
$\operatorname{Cov}\preceq CI$, hence
$C_{\rm TCI}\ge\lambda_{\max}(\operatorname{Cov})$.  The bounded Gaussian density comparison
supplies all linear exponential moments needed for this argument.

Combining these bounds gives, simultaneously for all three constants,
$$
1-\varepsilon_n\le \frac{C_n}{\lambda_n}\le e^{\delta_n}.
$$
Both endpoints converge to one in probability.

### Probabilistic quantifiers and Fisher limit

All inequalities are first deterministic on the data-realization event where $H_n\succ0$ and the
global representation holds.  That event has probability tending to one, and the dossier
explicitly permits arbitrary definitions on its complement.  Thus every displayed $o_P(1)$ and
ratio conclusion has a complete quantifier interpretation.

Setting $B_n=H_n/n$ gives the exact identity $nH_n^{-1}=B_n^{-1}$.  Since
$B_n\to J=I(\theta_0)\succ0$ in operator norm in probability, positivity holds with probability
tending to one and continuity of inversion gives $B_n^{-1}\to J^{-1}$.  Continuity of
$\lambda_{\max}$ and Slutsky's theorem then give the three claimed Fisher limits.

### Hypothesis accounting and fence

The analytic transfer uses exactly: fixed $d$; $H_n/n\to_P I(\theta_0)\succ0$; the global
Gaussian density-ratio representation after mode-Hessian whitening; and
$\operatorname{osc}(r_n)=o_P(1)$.  The mode location is used only as a translation.  Interiority,
local prior positivity/smoothness, and model regularity are stated statistical context intended to
produce the analytic hypotheses, but are not separately consumed after those hypotheses are
assumed.  This is harmless unused strength and a possible future sharpening, not a gap.

The formal fence `obs:tv-insufficient` is respected.  The proof never reasons from total-variation
convergence: it uses global $L^\infty$ density-ratio control, which controls second moments and
excludes the certified remote-contamination example.  The theorem also does not extend to the
ordinary fixed-Gaussian-prior logistic setting fenced by Gaussian-tail rigidity.

### Mechanical validation

`cd solutions && latexmk -g -pdf -outdir=../build thm-a2-target.tex` succeeds and produces a
four-page PDF.  Its only warning is the expected standalone unresolved reference to
`thm:a2-target`.

## Corrections

None.

## Exclusions

This review does not certify the broader conjecture `conj:a2`, total-variation BvM as a sufficient
hypothesis, verification of the global oscillation assumption for any particular statistical
model, growing dimension, or the neighboring logistic/global-tail claims.
