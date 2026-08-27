# Full matrix dissipation proof attempt

Date: 2026-08-27

Role: `/root/prove_full_matrix_dissipation_w2`

Run: `w2r01`

Target: `cor:full-matrix-dissipation`

## Exact target and dependency audit

The manuscript and ledger ask for

$$
\mathbb E\int_0^\infty (R_t^2+s_tG_t^2)\,dt\preceq R_0,
$$

with the explicit warning that taking a trace can still cost the dimension. The only declared
dependency is `lem:matrix-riccati`, which is `proved` and agent-certified by
`solutions/kls-localization-riccati-core.tex` and
`research/reviews/2026-08-25-kls-core-r2-audit.md`. Its exact input is

$$
dR_t=d\widetilde N_t-(R_t^2+s_tG_t^2)\,dt,
$$

where $\widetilde N$ is a matrix local martingale. The target has no `bounded_by` edge. The
nearby manuscript obstruction is nevertheless respected: the proof obtains only a Loewner
bound, whose trace is at most $\operatorname{Tr}R_0\le n$.

## Proof mechanism

The expectation step cannot simply delete the local martingale. For each deterministic vector
$\theta$, scalarize the matrix identity:

$$
x_t^\theta+a_t^\theta=x_0^\theta+M_t^\theta,
\qquad
x_t^\theta=\theta^TR_t\theta\ge0,
$$

$$
a_t^\theta=\int_0^t\theta^T(R_u^2+s_uG_u^2)\theta\,du\ge0.
$$

At a localizing sequence for $M^\theta$, optional sampling gives equality of expectations.
Fatou's lemma for the nonnegative stopped sum gives the finite-horizon estimate including the
terminal $\mathbb ER_T$ term. Applying it to coordinate vectors yields entrywise integrability;
positivity bounds off-diagonal entries by the corresponding diagonal entries. Polarization then
reconstructs the Loewner inequality. Monotone convergence of each nonnegative quadratic-form
occupation gives the infinite-time estimate. This uses no uniform integrability at the infinite
endpoint.

## Strict content and remaining limitation

The full result retains the nonnegative $R_t^2$ damping that is absent from the source-only
Loewner display in `cor:per-direction`. For a standard Gaussian and the cut
$E=\{x_1\le0\}$, every spectator direction $e_j$, $j\ge2$, has $G_te_j=0$ but
$R_te_j=(1+t)^{-1}e_j$, so its retained damping integral is exactly $1$. Thus the new term is
genuine. The same example contributes $n-1$ to the traced $R^2$ occupation, making clear why the
matrix estimate does not close the dimension-free trace gate.

## Hypotheses actually used

- The fixed cut is nontrivial, $0<\mu(E)<1$, so its conditional covariances are defined.
- The certified matrix Riccati identity holds in the standing stochastic-localization setup.
- Covariance decomposition gives $R_t\succeq0$.
- Symmetry of $R_t,G_t$ and $s_t\ge0$ give $R_t^2+s_tG_t^2\succeq0$.
- Isotropy is used only for the final normalization $R_0\preceq I_n$; the bound by $R_0$ does
  not use it.

No balance, cut regularity, compact support, stopping window, fourth-moment assumption, or
unstopped-martingale uniform integrability is used. There are no unclosed proof steps.

## Artifact and status

Candidate dossier: `solutions/cor-full-matrix-dissipation.tex`.

The dossier intentionally has `checked_by: none`. No ledger delta applies until a distinct cold
proof-checker certifies the current bytes. The future candidate ledger metadata is
`solution: solutions/cor-full-matrix-dissipation.tex` together with the eventual certifying
review and `checked_by: agent`.

Standalone compilation succeeded:

```text
cd solutions
latexmk -pdf -interaction=nonstopmode -halt-on-error \\
  -outdir=../build cor-full-matrix-dissipation.tex
```

The command returned exit code `0` and produced
`build/cor-full-matrix-dissipation.pdf` (three pages). The remaining unresolved references are
the expected cross-manuscript labels in a standalone subfile.

Final dossier SHA256:

```text
5164913efaa6a4059c0d8f8f69f32ebc329a18b39601a150feb6ac84d7b1548c
```
