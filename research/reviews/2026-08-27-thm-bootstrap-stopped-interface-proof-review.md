---
verdict: pass
authors:
  - prove_bootstrap_stopped_interface_w3, unknown, 2026-08-27
reviewer: review_bootstrap_stopped_interface_w3, unknown, 2026-08-27
fingerprints:
  solutions/thm-bootstrap-stopped-interface.md: 7c7dcc9e96daa718b359532f193e319f0cb8759fe20140a3b6d89ebdf0fd922a
  thm:bootstrap-stopped-interface: 79e7d5d20e15142a7f56585b648283171f5c63a721accf1eedd14b7072d9efe8
  lem:half: 1d4daf2283e1a1022580a067533d1cc3aae4194fa319d223aa00e4112d031a2f
  lem:whitening: 3df7fc9dc6144b5c2ca23c0e9d21fc7a2132c0d494e03c75213cdc7ad7f72573
  lem:perimeter-martingale: c0e1c3539694fe07c6ebe7c767bafeeadef66ac4778e02f7d217b6c9d3ad3daa
---

# Stopped bootstrap interface — cold proof review

This review was reconstructed from repository artifacts without the prover's conversation
history.  The reviewer is distinct from the dossier author, and no exploration log names this
reviewer as an author.

## Frozen review boundary

| Artifact | SHA-256 at review time |
|---|---|
| `solutions/thm-bootstrap-stopped-interface.tex` | `1a8d482407819d409d2d6e8cb92da044e915ba04d79f58a62b4776a0c1a9ad56` |
| `modules/kls/25-bootstrap.tex` | `eb08372878c85e29db253d06d4c673f0af607df96032a45421a83e47d6b291ba` |
| `research/kls/ledger.yaml` | `5bb0812e52070aca34ce3fb74cdfe267ec0a87c06ee8a05b829b09a1c58bd0d0` |

The first hash is the pinned dossier hash supplied for review.  The manuscript and ledger hashes
record the synchronized statement snapshot against which it was checked; unrelated append-only or
single-writer changes to those shared files do not alter the frozen dossier scope.

## Findings

### Statement agreement

The dossier theorem at `solutions/thm-bootstrap-stopped-interface.tex:66`, the manuscript theorem
at `modules/kls/25-bootstrap.tex:152`, and the ledger node at
`research/kls/ledger.yaml:503` agree mathematically.  Their shared hypotheses are $n\ge2$,
$\varepsilon\in(0,1]$, an isotropic log-concave $\mu$ satisfying
$h_\mu\le(1+\varepsilon)h_n^\star$, an arbitrary balanced measurable cut $E$, and
$\eta\in(0,1/2)$.  For every $T>0$ they use the same cut-stopped interface
$$
\widehat\Xi_{T,\eta}(\mu,E)
=\int_0^T\mathbb E[X_s\mathbf1_{\{s<\tau_\eta\}}],ds
$$
and assert the same integrated bound, including the coefficients $1/16$, $1/8$, and $1/4$.
They also have the same specialization $0<T<1/8$, $\eta=T^{1/3}$, and
$\varepsilon\le T^{1/3}$.  The dossier strengthens the unspecified universal constant in the
manuscript and ledger to the compatible explicit choice $C=2$.

### Setup, integrability, and stopping conventions

The mass process $p_t=\mu_t(E)$ is the bounded continuous localization martingale.  With
$s_t=p_t(1-p_t)$, $\delta_t=m_t^E-m_t^{E^c}$, and
$r_t=s_t|\delta_t|^2$, its bracket is
$$
d[p]_t=s_tr_t,dt.
$$
The covariance decomposition gives
$s_t\delta_t\delta_t^T\preceq A_t$; this rank-one matrix has nonzero eigenvalue $r_t$.
Consequently $r_t\le\lambda_{\max}(A_t)$ and, since $s_t\le1/4$,
$$
s_tr_t\le\frac14\lambda_{\max}(A_t)
\le\frac14(1+X_t).
$$
Thus the quadratic-variation identity and both constants in the displayed setup bound are
correct.

Taking traces in $dA_t=\Theta_t\,dW_t-A_t^2dt$, first after localization and then using Fatou,
gives $\mathbb E\operatorname{Tr}A_t\le n$.  Hence
$Z_t:=\mathbb E[X_t\mathbf1_{\{t<\tau_\eta\}}]\le n$, which is enough for every finite-time
Tonelli and martingale-isometry use below.  If the initial lower Minkowski perimeter is infinite,
then $e_0=+\infty$ and the theorem is automatic as an extended-real inequality.  In the only
nontrivial case, finite initial perimeter, the certified fixed-cut perimeter lemma supplies an
integrable nonnegative supermartingale.

The strict-exit convention
$\tau_\eta=\inf\{t:|p_t-1/2|>\eta\}$ is handled correctly.  Continuity implies that on
$\{\tau_\eta\le t\}$ the stopped path reaches $|p_{\tau_\eta}-1/2|=\eta$.  Replacing
$\mathbf1_{\{s\le\tau_\eta\}}$ by $\mathbf1_{\{s<\tau_\eta\}}$ in a Lebesgue-time bracket
integral changes at most one time point on each path.

### Deterministic-time excess comparison

Fix $t>0$, write
$\mathcal A_t=\{t<\tau_\eta\}$,
$P_t=\mathbb P(\tau_\eta\le t)$,
$Z_t=\mathbb E[X_t\mathbf1_{\mathcal A_t}]$, and
$a=1/2-\eta$.  The perimeter input is used only at this deterministic time:
$$
\mathbb E[\mu_t^+(E)\mathbf1_{\mathcal A_t}]
\le\mathbb E\mu_t^+(E)
\le\mu^+(E)=h_\mu/2+e_0.
$$
The last equality follows from balance and `lem:half`; no perimeter optional-stopping assertion is
used.

The finite-time posterior covariance is nondegenerate because the localization tilt is strictly
positive on the full-dimensional initial support.  On $\mathcal A_t$ one has
$\min(p_t,1-p_t)\ge a$.  The certified whitening comparison and the valid tangent inequality
$$
\lambda^{-1/2}\ge1-\tfrac12(\lambda-1)_+\qquad(\lambda>0)
$$
therefore give exactly
$$
\mathbb E[h_{\mu_t}\min(p_t,1-p_t)\mathbf1_{\mathcal A_t}]
\ge h_n^\star a(1-P_t-Z_t/2).
$$
In particular, the error is the stopped expectation $Z_t$, not the larger unstopped
$\mathbb E X_t$.

The proof retains the required sign split.  Put
$\rho=h_n^\star/h_\mu$ and $B_t=1-P_t-Z_t/2$.  Isotropy and near-worstness give
$1/(1+\varepsilon)\le\rho\le1$ and hence $\rho\ge1-\varepsilon$.

- If $B_t\ge0$, multiplying by the lower bound for $\rho$ preserves the direction, and
  $$
  \frac12-(1-\varepsilon)aB_t
  =\frac12-a(1-P_t)+\frac{aZ_t}{2}+\varepsilon aB_t
  \le\eta+\frac{P_t}{2}+\frac{Z_t}{4}+\frac\varepsilon2.
  $$
  Here $a\le1/2$ and $0\le B_t\le1$ justify each coefficient.

- If $B_t<0$, the argument does not multiply a negative quantity by the lower bound for $\rho$.
  It discards the nonnegative posterior Cheeger term.  Since this case is exactly
  $P_t/2+Z_t/4>1/2$, the desired right side is strictly larger than the remaining $h_\mu/2$.

Both cases prove
$$
\mathbb E[\bar e_t(E)\mathbf1_{\{t<\tau_\eta\}}]
\le e_0+h_\mu\left(\frac\varepsilon2+\eta+\frac{P_t}{2}+\frac{Z_t}{4}\right).
$$

### Stopped exit probability and integrated constants

The process $M_u=p_{u\wedge\tau_\eta}-1/2$ is bounded, continuous, and square-integrable.
Doob's weak $L^2$ maximal inequality, followed by martingale isometry for the bounded stopped
martingale and the checked bracket bound, gives
$$
\begin{aligned}
P_t
&\le\eta^{-2}\mathbb E M_t^2
=\eta^{-2}\mathbb E[p]_{t\wedge\tau_\eta}\\
&\le\frac1{4\eta^2}\int_0^t
\mathbb E[\mathbf1_{\{s<\tau_\eta\}}(1+X_s)],ds\\
&\le\frac1{4\eta^2}\left(t+\int_0^t Z_s,ds\right).
\end{aligned}
$$
No unbounded optional-stopping theorem occurs.  Nonnegativity permits Tonelli, so
$$
\int_0^T P_t,dt
\le\frac1{4\eta^2}\left(\frac{T^2}{2}
+\int_0^T(T-s)Z_s,ds\right)
\le\frac1{4\eta^2}\left(\frac{T^2}{2}+T\widehat\Xi_{T,\eta}\right).
$$
The $P_t/2$ term therefore contributes exactly $T^2/(16\eta^2)$ and
$T\widehat\Xi_{T,\eta}/(8\eta^2)$, while the $Z_t/4$ term contributes exactly
$\widehat\Xi_{T,\eta}/4$.  These are the three constants asserted in every statement plane.

For $\eta=T^{1/3}$ and $\varepsilon\le T^{1/3}$,
$$
(\varepsilon/2+\eta)T\le\tfrac32T^{4/3},\qquad
\frac{T^2}{16\eta^2}=\frac1{16}T^{4/3},
$$
and $T<1/8$ gives both $\eta<1/2$ and
$$
\frac{T}{8\eta^2}+\frac14
=\frac{T^{1/3}}8+\frac14<\frac5{16}.
$$
Thus the full bracket is bounded by
$2(T^{4/3}+\widehat\Xi_{T,\eta})$, and $C=2$ is valid.

### Hypotheses, dependencies, citations, and fences

The argument uses: balance of $E$; log-concavity and isotropy of $\mu$; the stated near-worst
comparison; $0<\eta<1/2$; finite initial perimeter in the nontrivial case; `lem:half`;
`lem:whitening`; `lem:perimeter-martingale`; and the standard localization mass-bracket,
two-color covariance-decomposition, and covariance-SDE identities.  The clean form additionally
uses exactly $0<T<1/8$, $\eta=T^{1/3}$, and $\varepsilon\le T^{1/3}$.  No regularity of the cut,
near-minimality of the cut, or covariance occupation estimate is used.  The restrictions $n\ge2$
and $\varepsilon\le1$ are stronger than the displayed algebra needs, but are harmless unused
scope restrictions rather than defects.

All three declared ledger dependencies are currently `proved` with agent-certified dossiers and
passing review pointers.  The only external isoperimetric input enters through those already
certified dependencies; the reviewed dossier itself has no external citation and no
`preprint-unreviewed`, conditional, open, or numerical premise.  This review checked the exact
deterministic consequences consumed here but does not recertify the dependency dossiers.

Both `bounded_by` fences are respected:

- `rem:profile-circularity`: the proof never assigns supermartingale behavior to the random
  mass-constrained profile.  It uses the external worst-case constant $h_n^\star$ through
  whitening and the explicit near-worst hypothesis at time zero.
- `rem:relative-ceiling`: the cut-dependent stopped interface remains on the right-hand side.
  The proof supplies no dimension-free or relative-scale upper bound for it; the preliminary
  $\widehat\Xi_{T,\eta}\le nT$ bound is dimension dependent.  No KLS conclusion, converse, or
  equivalence is inferred.

## Corrections

None.  Every stopping indicator, whitening step, sign-sensitive inequality, bracket identity,
constant, and specialization in the pinned dossier is correct.

## Validation

- `cd solutions && latexmk -pdf -outdir=../build thm-bootstrap-stopped-interface.tex`: exit code
  0.
- A forced rebuild with `latexmk -pdf -g -outdir=../build
  thm-bootstrap-stopped-interface.tex` also exited 0 and produced the four-page standalone PDF.
  The only warnings are the expected unresolved references to manuscript labels when a subfile is
  compiled alone; the dossier has no citations.

## Proposed ledger delta

Every premise is discharged.  The node may take `status: proved` with the following certification
fields, while preserving its current statement, route, file, dependencies, and fences:

```yaml
status: proved
solution: solutions/thm-bootstrap-stopped-interface.tex
checked_by: agent
review: research/reviews/2026-08-27-thm-bootstrap-stopped-interface-proof-review.md
```

## Exclusions

This review does not certify a universal estimate for
$\widehat\Xi_{T,\eta}(\mu,E)$, an unstopped covariance-interface estimate, excess propagation at
relative scale, the nearby pathwise feature remark, KLS, or any manuscript or ledger node other
than the one listed in the front matter.  It does not re-review the full certified bootstrap,
perimeter, half-balance, or whitening dossiers, and it does not certify any numerical artifact.

```yaml
outcome: complete
artifacts:
  - research/reviews/2026-08-27-thm-bootstrap-stopped-interface-proof-review.md
proposed_deltas:
  - "For thm:bootstrap-stopped-interface, set status: proved, solution: solutions/thm-bootstrap-stopped-interface.tex, checked_by: agent, and review: research/reviews/2026-08-27-thm-bootstrap-stopped-interface-proof-review.md; preserve its statement, route, file, depends_on, and bounded_by fields."
next_role: orchestrator
next_prompt: |
  Atomically certify thm:bootstrap-stopped-interface with status: proved,
  solution: solutions/thm-bootstrap-stopped-interface.tex, checked_by: agent, and review:
  research/reviews/2026-08-27-thm-bootstrap-stopped-interface-proof-review.md.  Preserve its
  statement, route, file, depends_on, and bounded_by fields, and run
  python3 research/check_ledger.py after the single-writer ledger update.
```
