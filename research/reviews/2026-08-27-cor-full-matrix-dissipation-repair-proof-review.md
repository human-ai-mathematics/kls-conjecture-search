---
verdict: pass
authors:
  - /root/prove_full_matrix_dissipation_w2
  - /root/repair_full_matrix_dissipation_w2
reviewer: /root/review_full_matrix_dissipation_w2
fingerprints:
  solutions/cor-full-matrix-dissipation.md: ea87bfa39c766f4f0df537ed4d3bc944eee4c6049db04b401861e652963a2357
  cor:full-matrix-dissipation: 67207edd4c5c4e8e6674ab24f20583a4a51374e514582fd7032b1120e7b0f0ce
  lem:matrix-riccati: b529c0f736b4dce32a7843e81f8edb6569491781941e3b8aecdc1be0ddf7a023
---

*Follows up* `research/reviews/2026-08-27-cor-full-matrix-dissipation-proof-review.md`.

# Full matrix dissipation repair — independent proof review

This is a fresh review of `solutions/cor-full-matrix-dissipation.tex`, SHA-256
`fd202cc8b71e9cbc576859de720339dcf37ab6bc93ab520cf1ff055626700dc7`.
The original author, repair author, and reviewer are pairwise distinct.  The historical audit named
in `follows_up` remains unchanged and was used only to identify the requested repairs, not as
mathematical evidence for the current proof.  The proof was reconstructed from the current
dossier, manuscript and ledger statements, standing two-color setup, and certified dependency.

## Findings

### The two audited defects are repaired

The abstract positive-matrix-drift lemma now assumes at
`solutions/cor-full-matrix-dissipation.tex:61`--`62` that its initial matrix $X_0$ is
deterministic.  Consequently $x_0^\theta=\theta^TX_0\theta$ is deterministic and finite, so the
stopped expectation identity at lines 96--106 has the stated right side.  The former
random-initial-value counterexample is outside the repaired hypotheses.  The display at line 111
now correctly reads

$$
\mathbb E x_T^\theta+\mathbb E a_T^\theta\leq x_0^\theta.
$$

Both requested changes are complete, and no unrelated mathematical line changed.

### Three-way statement agreement and fences

The ledger statement at `research/kls/ledger.yaml:136`--`142` and the manuscript corollary at
`modules/kls/12-riccati.tex:121`--`130` assert

$$
\mathbb E\int_0^\infty (R_t^2+s_tG_t^2)\,dt\preceq R_0,
$$

that discarding $R_t^2$ recovers the source-only per-direction estimate, and that taking a trace
can cost the dimension.  Under the same standing isotropic log-concave, fixed nontrivial cut
setup, the dossier proves the stronger finite-horizon statement

$$
\mathbb E R_T+
\mathbb E\int_0^T(R_t^2+s_tG_t^2)\,dt\preceq R_0
$$

and states the ledger/manuscript inequality as its infinite-horizon consequence.  Thus the three
statements agree mathematically, with the dossier supplying a valid strengthening rather than a
different target.

The node has no formal `bounded_by` edge.  The nearby operator-to-trace obstruction is nonetheless
respected: the proof derives only

$$
\mathbb E\int_0^\infty
\bigl(\|R_t\|_{\mathrm{HS}}^2+s_t\|G_t\|_{\mathrm{HS}}^2\bigr)\,dt
\leq\operatorname{Tr}R_0\leq n.
$$

It explicitly disclaims any dimension-free trace upgrade and asserts no implication among
`q:upgrade`, the high-rank part of `q:stein-weighted`, `q:alignment`, or any other member of the
trace-upgrade cluster.

### Dependency closure and citation debt

The only declared dependency is `lem:matrix-riccati`.  It is `proved`, points to
`solutions/kls-localization-riccati-core.tex`, and is covered by the active passing report
`research/reviews/2026-08-25-kls-core-r2-audit.md`.  That certified dependency gives exactly

$$
dR_t=d\widetilde N_t-(R_t^2+s_tG_t^2)\,dt
$$

for the continuous Brownian-driven matrix local martingale arising in the standing two-color
localization setup.  Its drift is locally integrable.  No open, conditional, imported,
`preprint-unreviewed`, or numerical premise occurs in the dependency closure.

The present dossier has no external citation.  Its only additional example is an elementary
Gaussian completion-of-the-square computation, independently checked below, so there is no new
citation debt.

### Positive matrix drift, optional sampling, and Fatou

Fix a deterministic $\theta\in\mathbb R^n$ and put

$$
x_t^\theta=\theta^TX_t\theta,
\qquad
a_t^\theta=\int_0^t\theta^TQ_u\theta\,du,
\qquad
M_t^\theta=\theta^TN_t\theta.
$$

Positivity of $X_t,Q_t$ makes $x_t^\theta,a_t^\theta$ nonnegative and $a_t^\theta$
increasing, while the assumed decomposition gives
$x_t^\theta+a_t^\theta=x_0^\theta+M_t^\theta$.  A scalar localizing sequence can be
chosen so that each stopped $M^\theta$ is a true martingale.  Optional sampling at the bounded
time $T\wedge\sigma_k$ is therefore legitimate.  Since $x_0^\theta$ is now deterministic and
finite, the stopped nonnegative sum is integrable and has expectation $x_0^\theta$.

For fixed $T$, $T\wedge\sigma_k\to T$ almost surely.  Continuity of $X$ and pathwise local
integrability of $Q$ give almost-sure convergence of the stopped sum to
$x_T^\theta+a_T^\theta$.  Fatou's lemma then yields the corrected finite-horizon directional
inequality without any uniform-integrability assumption on the unstopped local martingale or
terminal process.

### Entrywise integrability, Loewner reconstruction, and infinite time

Testing the finite-horizon estimate at each coordinate vector proves integrability of the diagonal
entries of $X_T$ and $H_T=\int_0^TQ_tdt$.  For every positive-semidefinite matrix $C$,
$|C_{ij}|\leq(C_{ii}+C_{jj})/2$; applying this pointwise to $X_T$ and $Q_t$ gives

$$
\mathbb E |(X_T)_{ij}|<\infty,
\qquad
\mathbb E\int_0^T|(Q_t)_{ij}|dt<\infty.
$$

Thus both matrix expectations are well defined entrywise.  The directional inequality for every
deterministic $\theta$ is exactly the asserted finite-horizon Loewner inequality.

For each $\theta$, $a_T^\theta\uparrow a_\infty^\theta$ as $T\uparrow\infty$, so monotone
convergence gives $\mathbb E a_\infty^\theta\leq x_0^\theta$.  Coordinate testing makes every
diagonal occupation finite almost surely and in $L^1$; the same positive-semidefinite entry bound
then gives absolute almost-sure and $L^1$ convergence of every off-diagonal integral.
Polarization reconstructs the matrix expectation and its infinite-horizon Loewner bound.  No
limit interchange remains unjustified.

### Application, hypotheses, and isotropy

In the localization application, strict positivity of the finite-time likelihood preserves
$p_t,q_t>0$ from the stated $0<\mu(E)<1$, so both conditional covariance matrices are defined.
Covariance decomposition gives

$$
R_t=p_t\Sigma_t^E+q_t\Sigma_t^{E^c}\succeq0.
$$

The matrices $R_t,G_t$ are symmetric and $s_t\geq0$, hence
$Q_t=R_t^2+s_tG_t^2\succeq0$.  The certified Riccati identity supplies exactly the abstract
decomposition, including continuity, adaptedness, progressivity, and local drift integrability.
The initial law and cut are fixed, so $R_0$ is deterministic.  The abstract lemma therefore gives
the finite inequality including $\mathbb E R_T$ and, by the checked infinite-time argument, the
target inequality.

The hypotheses actually used are: a fixed initial law with finite second moments, a fixed
measurable nontrivial cut, the standing finite-time two-color localization processes, the certified
matrix Riccati identity, and positivity/symmetry from covariance decomposition.  Isotropy is used
only at the final normalization
$R_0=A_0-B_0\preceq A_0=I_n$.  The estimate with right side $R_0$ does not use isotropy.
Log-concavity belongs to the standing setup but is not separately used by the abstract drift
argument.  No balance, stopping window, boundary regularity, compact support, fourth moment, or
endpoint uniform-integrability hypothesis is used.  No used hypothesis is unstated.

### Gaussian halfspace and the genuine trace cost

For the standard Gaussian initial law, completing the square in the localization density shows
that, pathwise at time $t$, the posterior is Gaussian with mean $c_t/(1+t)$ and covariance
$(1+t)^{-1}I_n$.  It factors across the coordinate axes.  Conditioning on
$E=\{x_1\leq0\}$ affects only the first coordinate, so for every spectator direction $j\geq2$,

$$
G_te_j=0,
\qquad
R_te_j=(1+t)^{-1}e_j,
\qquad
\int_0^\infty|R_te_j|^2dt=1.
$$

Thus the retained $R_t^2$ term spends an exact unit budget in each of $n-1$ spectator directions,
while the source-only term vanishes there.  This analytically verifies that the strengthening is
genuine and that its traced occupation can already cost $n-1$.  No sampled or numerical output is
used.

### Standalone build and validation

The forced standalone command

```text
cd solutions && latexmk -g -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=../build cor-full-matrix-dissipation.tex
```

returned exit code zero and produced a visually inspected three-page PDF.  There is no TeX error,
fatal warning, overfull box, or underfull box.  The three unresolved parent labels are the expected
standalone-subfile behavior.  After the mathematical review and before this report was written,
`python3 research/check_ledger.py` reported 0 errors for 189 nodes and 660 labels.

## Corrections

None.  The repaired dossier needs no further mathematical change.  Updating its provenance-only
header and the orchestrator-owned ledger to point to this report is the post-certification delta,
not a proof repair.

## Exclusions

This review does not recertify the upstream Riccati dossier beyond checking its active
certification and exact applicability.  It does not certify `cor:per-direction`, an
operator-to-trace upgrade, an all-cut Carleson estimate, any trace-upgrade-cluster implication, or
any numerical artifact.  The Gaussian halfspace calculation is checked only as this dossier's
sharpness illustration, not as a separate ledger claim.  No solution, manuscript, ledger,
bibliography, exploration, knowledge, route-control, or prior-review file was changed by this
reviewer.
