---
---
# Prover attempt: stopped bootstrap covariance interface

Date: 2026-08-27

Role: /root/prove_bootstrap_stopped_interface_w3

Target: thm:bootstrap-stopped-interface

## Outcome

A standalone candidate dossier was written at
solutions/thm-bootstrap-stopped-interface.tex. Its final SHA-256 is
1a8d482407819d409d2d6e8cb92da044e915ba04d79f58a62b4776a0c1a9ad56.
The dossier retains checked_by: none; it has no proof status until a distinct reviewer passes
these exact bytes.

The proved candidate statement matches the staged manuscript and ledger target:

$$
\begin{aligned}
\int_0^T \mathbb E[\bar e_t(E)\mathbf 1_{\{t<\tau_\eta\}}]\,dt
\le Te_0+h_\mu\biggl[
&\left(\frac{\varepsilon}{2}+\eta\right)T+\frac{T^2}{16\eta^2}\\
&+\left(\frac{T}{8\eta^2}+\frac14\right)
\widehat\Xi_{T,\eta}(\mu,E)\biggr].
\end{aligned}
$$

where

$$
\widehat\Xi_{T,\eta}(\mu,E)
=\int_0^T\mathbb E[X_s\mathbf 1_{\{s<\tau_\eta\}}]\,ds.
$$

For $0<T<1/8$, $\eta=T^{1/3}$, and $\varepsilon\le T^{1/3}$, the dossier checks the
specialization with the explicit universal choice $C=2$.

## Proof mechanism

At deterministic time $t$, set

$$
P_t=\mathbb P(\tau_\eta\le t),
\qquad
Z_t=\mathbb E[X_t\mathbf 1_{\{t<\tau_\eta\}}].
$$

Keeping the stopping indicator inside the whitening comparison gives

$$
\mathbb E[
h_{\mu_t}\min(p_t,q_t)\mathbf 1_{\{t<\tau_\eta\}}]
\ge h_n^\star(1/2-\eta)(1-P_t-Z_t/2).
$$

The certified bootstrap proof's sign split must still be used: multiplication by the lower
bound $h_n^\star/h_\mu\ge1-\varepsilon$ is valid only when the last bracket is nonnegative.
If it is negative, nonnegativity of the posterior Cheeger term and
$P_t/2+Z_t/4>1/2$ close the other case. This yields

$$
\mathbb E[\bar e_t\mathbf 1_{\{t<\tau_\eta\}}]
\le e_0+h_\mu\left(
\frac\varepsilon2+\eta+\frac{P_t}{2}+\frac{Z_t}{4}\right).
$$

The stopped mass martingale gives, without dropping the covariance indicator,

$$
P_t
\le \frac{1}{4\eta^2}
\left(t+\int_0^t Z_s\,ds\right).
$$

Tonelli then gives

$$
\int_0^T P_t\,dt
\le\frac{1}{4\eta^2}
\left(\frac{T^2}{2}+T\widehat\Xi_{T,\eta}\right),
$$

which produces the coefficients $1/16$, $1/8$, and $1/4$ in the target.

## Dependency and fence audit

The direct ledger dependencies are exactly:

- lem:half;
- lem:whitening; and
- lem:perimeter-martingale.

The proof also uses the repository's standard stochastic-localization setup identities
eq:qv-p, eq:B-le-A, and eq:cov-sde. For the nontrivial finite-valued case, the cut has
finite initial lower outer Minkowski perimeter; if its initial perimeter is infinite, the
theorem is automatic in the extended sense. The stopped covariance integrand is jointly
measurable and integrable because $\mathbb E X_t\le\mathbb E\operatorname{Tr}A_t\le n$.

The result is unconditional given its stated near-worst hypotheses and its already certified
dependencies. It uses no smoothness, no numerical evidence, no near-minimality of the cut, and
no unstated covariance estimate.

- rem:profile-circularity is respected: no supermartingale property or lower bound is asserted for the
  moving mass-constrained isoperimetric profile.
- rem:relative-ceiling is respected: the result does not bound
  $\widehat\Xi_{T,\eta}$ at a dimension-free relative scale and does not imply KLS. The
  dimension-dependent estimate $\widehat\Xi_{T,\eta}\le nT$ is used only to record
  integrability.

## Dead ends and corrections during the attempt

Merely integrating the already certified pointwise bootstrap inequality does not prove the
target: that inequality has already replaced the stopped covariance error by
$\mathbb E X_t$, so it can recover only $\Xi_T$. The whitening step and the stopped
quadratic-variation step both had to be repeated before either indicator was discarded.

The first two standalone compilation attempts exposed transcription-only TeX defects: one
missing backslash before \left and one form-feed character in \frac. Both were corrected;
neither affected the mathematical argument. A control-character scan is now clean.

## Validation

- cd solutions && latexmk -pdf -g -outdir=../build thm-bootstrap-stopped-interface.tex:
  exit code 0, producing a four-page PDF.
- The remaining undefined references are the expected standalone references to manuscript
  labels.
- The log has no overfull/underfull boxes, undefined control sequences, LaTeX errors, fatal
  errors, or undefined citations.
- git diff --check -- solutions/thm-bootstrap-stopped-interface.tex: exit code 0.

No step remains unclosed.

## Deferred certification

No ledger delta is applicable from this authoring attempt. If a distinct cold proof checker
passes the dossier, the deferred artifact candidate is
solution: solutions/thm-bootstrap-stopped-interface.tex; the orchestrator would then decide
the atomic manuscript/ledger certification delta.

~~~yaml
outcome: complete
artifacts:
  - solutions/thm-bootstrap-stopped-interface.tex
  - research/explorations/2026-08-27-prover-bootstrap-stopped-interface-w3p01.md
proposed_deltas:
  - none
next_role: proof-checker
next_prompt: |
  Cold-review the exact dossier solutions/thm-bootstrap-stopped-interface.tex at SHA-256
  1a8d482407819d409d2d6e8cb92da044e915ba04d79f58a62b4776a0c1a9ad56 for the open node
  thm:bootstrap-stopped-interface. Reconstruct the proof from repository artifacts, independently
  of the author conversation. Check agreement with the ledger statement and the theorem labeled
  thm:bootstrap-stopped-interface in modules/kls/25-bootstrap.tex. Verify that the whitening
  lower bound retains Z_t = E[X_t 1_{t<tau_eta}], that the two-case sign split never multiplies a
  negative bracket by rho >= 1-epsilon, and that the stopped mass quadratic variation retains
  1_{s<tau_eta}. Check Tonelli and the constants 1/16, 1/8, 1/4, as well as the T<1/8,
  eta=T^(1/3), epsilon<=T^(1/3) specialization (C=2). Audit measurability, integrability,
  infinite-perimeter handling, and exact dependence on lem:half, lem:whitening, and
  lem:perimeter-martingale. Check both fences rem:profile-circularity and rem:relative-ceiling: the
  dossier must not claim any universal bound on widehat Xi or any KLS conclusion. Compile the
  dossier standalone. Persist a structured review under research/reviews/ with author
  /root/prove_bootstrap_stopped_interface_w3 and a distinct reviewer identity. If and only if
  every check passes, propose the atomic orchestrator delta setting the node to proved with this
  solution and review; do not edit the ledger or dossier yourself.
~~~
