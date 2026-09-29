---
---
# Prover: time-weighted fixed-function source budget (wave 0, S02)

Date: 2026-08-27

Role: `/root/prove_mm_weighted_source`

Scope key: `solution:lem-mm-time-weighted-fixed-source`

## Contract and target audit

The accepted ledger node is `lem:mm-time-weighted-fixed-source`, with manuscript anchor
`lem:mm-time-weighted-fixed-source` in `modules/kls/30-spectral-route.tex`. The node is `open`,
has no `depends_on` edge, and has no `bounded_by` edge. Its exact finite-horizon target is
$$
\mathbb E\int_0^T(\kappa+t)\|H_t\|_{\mathrm{HS}}^2\,dt
+2\mathbb E\int_0^T
\left(|g_t|^2-(\kappa+t)g_t^TA_tg_t\right)dt
\le \operatorname{Var}_\mu(f)-\kappa|g_0|^2.
$$
The stated consequence at $\kappa=0$ is
$$
\mathbb E\int_0^\infty t\|H_t\|_{\mathrm{HS}}^2\,dt
\le \operatorname{Var}_\mu(f),
$$
with no unweighted initial-layer conclusion.

The dossier proves this for every $f\in L^2(\mu)$ when
$d\mu=Z^{-1}e^{-V}dx$, $V\in C^\infty(\mathbb R^n)$, and
$\nabla^2V\succeq\kappa I_n$ with $\kappa\ge0$. It does not require centering, isotropy, an
eigenfunction equation, or a preprint input. This makes the manuscript's phrase “for which the
posterior identities are justified” precise by proving the necessary $L^2$ closure.

## Proof mechanism

Use the planted observation channel $c_t=tX+B_t^{\mathrm{obs}}$ and its innovation Brownian
motion. With $w_t=\kappa+t$, posterior Brascamp--Lieb gives
$$
w_tA_t\preceq I.
$$
It has two separate consequences:

1. the remainder
   $$
   \mathcal R_t=|g_t|^2-w_tg_t^TA_tg_t
   =g_t^T(I-w_tA_t)g_t
   $$
   is nonnegative;
2. conditional Cauchy--Schwarz gives the terminal cap
   $$
   w_t|g_t|^2\le v_t,
   \qquad v_t=\operatorname{Var}_{\mu_t}(f).
   $$

For a compactly supported smooth test, the filtering identities and Itô's product rule give the
exact fixed-function equation
$$
dg_t=H_t\,dW_t-A_tg_t\,dt.
$$
The cross-variation $d[m,a]_t=A_tg_tdt$ is retained; omitting it would lose the damping term.
Multiplication by $w_t$ gives
$$
d(w_t|g_t|^2)
=2w_tg_t^TH_t\,dW_t
+\left(w_t\|H_t\|_{\mathrm{HS}}^2+2\mathcal R_t-|g_t|^2\right)dt.
$$

On a fixed horizon, stop both the local martingale and all finite-variation terms. At the bounded
stopping time $\theta$, the conditional variance identity is exact:
$$
\mathbb Ev_\theta
+\mathbb E\int_0^\theta|g_t|^2dt
=\operatorname{Var}_\mu(f).
$$
The terminal cap then proves the stopped target. Since the two target integrands are
nonnegative, monotone convergence removes the stopping without requiring convergence of a
terminal local-martingale term.

## Admissible-class closure

For arbitrary $f\in L^2(\mu)$, take $f_j\in C_c^\infty$ converging in $L^2(\mu)$. The filtering
martingale isometry gives the strong convergence
$$
\mathbb E\int_0^T|g_t^j-g_t|^2dt
\le\|f_j-f\|_{L^2(\mu)}^2.
$$
Since $0\preceq I-w_tA_t\preceq I$, the nonnegative remainder integrals converge in $L^1$.

For the tensor, a smooth log-concave probability has finite fourth moment and conditional Jensen
gives
$$
\sup_{t\ge0}\mathbb E|X-a_t|^4\le16\mathbb E|X|^4.
$$
Consequently
$$
\sup_{t\ge0}\mathbb E\|H_t^j-H_t\|_{\mathrm{HS}}
\le C_\mu\|f_j-f\|_{L^2(\mu)}.
$$
The compact-core estimate bounds $H^j$ in
$L^2((\kappa+t)d\mathbb Pdt)$; weak compactness, the preceding strong $L^1$ identification, and
weak lower semicontinuity pass the complete inequality to $f$. This also establishes the
weighted $L^2$ membership that makes every term of the theorem well-defined.

For $\kappa=0$, discard the nonnegative remainder and send $T$ to infinity by monotone
convergence.

## Dead ends and exclusions

- A direct expectation of the unstopped local martingale was rejected. The proof uses a bounded
  stopping time, the exact stopped variance budget, and monotone stopping removal.
- A formal Itô calculation for a general $L^2$ test was not treated as a domain argument. The
  proof starts on $C_c^\infty$ and records the strong/weak closure needed for $g$ and $H$.
- The linear time weight cannot be discarded near zero. Finiteness of
  $\int_0^1tF(t)dt$ for $F\ge0$ does not imply finiteness of $\int_0^1F(t)dt$; no deweighting or
  unweighted occupation estimate is claimed.
- The result does not approximate the measure, cover singular/lower-dimensional limits, or
  discharge `q:mm-spectral-occupation`.

## Fence check

There is no formal `bounded_by` edge. The proof uses no cut, slice, radial, projection,
near-extremal, or covariance-occupation argument, so it does not engage `obs:two-tail`,
`obs:proj-ceiling`, `obs:crude-insufficient`, `obs:relative-ceiling`, `obs:circularity`, or
`obs:rank-one-refuted`. The covariance cap is used only with the retained factor $\kappa+t$.

## Validation and status

The standalone command

```bash
cd solutions && latexmk -pdf -outdir=../build lem-mm-time-weighted-fixed-source.tex
```

succeeded and produced `build/lem-mm-time-weighted-fixed-source.pdf`. The log contains only the
expected unresolved cross-module references to `lem:mm-time-weighted-fixed-source` and
`q:mm-spectral-occupation`; there are no internal undefined references, TeX errors, or box
warnings. `python3 research/check_ledger.py` reports 0 errors across 180 nodes.

The dossier remains `checked_by: none`. It is an unconditional candidate proof of this lemma,
with no unclosed analytic step and no unresolved hypothesis. There is no applicable ledger delta
before independent review. The deferred candidate value is
`solution: solutions/lem-mm-time-weighted-fixed-source.tex`.

```yaml
outcome: complete
artifacts:
  - solutions/lem-mm-time-weighted-fixed-source.tex
  - research/explorations/2026-08-27-prover-mm-time-weighted-source-w0s02.md
proposed_deltas:
  - none; checked_by remains none and the solution path is deferred until independent certification
next_role: proof-checker
next_prompt: |
  Cold-review `solutions/lem-mm-time-weighted-fixed-source.tex` for ledger node
  `lem:mm-time-weighted-fixed-source`, without using the prover's conversation history. The
  theorem is unconditional: for every smooth probability
  `dmu=Z^{-1} exp(-V) dx` with `Hess V >= kappa I`, `kappa >= 0`, and every fixed
  `f in L^2(mu)`, it claims
  `E int_0^T (kappa+t)||H_t||_HS^2 dt + 2 E int_0^T
  (|g_t|^2-(kappa+t)g_t^T A_t g_t) dt <= Var_mu(f)-kappa|g_0|^2`,
  with both integrands nonnegative, and hence at `kappa=0`,
  `E int_0^infinity t||H_t||_HS^2 dt <= Var_mu(f)`. It expressly makes no
  unweighted initial-layer claim. Audit the planted posterior and innovation identities; the
  orientation and cross-variation in `dg=H dW-Ag dt`; the weighted Ito identity; the two
  distinct uses of posterior Brascamp--Lieb (nonnegative remainder and terminal covariance
  cap); the random-stopping conditional-variance budget; localization and monotone stopping
  removal; and the full `C_c^infinity -> L^2(mu)` passage, including strong `g` convergence,
  convergence of the remainder, fourth-moment `L^1` identification of `H`, weighted weak
  compactness, and lower semicontinuity. Verify that smooth log-concavity supplies every moment
  used, that no hidden centering/isotropy/eigenfunction/Letwin/numerical assumption occurs, and
  that the `kappa=0` infinite-horizon limit is only weighted. The node has no `depends_on` or
  `bounded_by` edge; check the dossier's fence paragraph against all route fences. Recompile
  standalone. If and only if every step passes, persist a distinct-author proof review and
  propose the atomic certification delta to the orchestrator; otherwise return a verbatim
  repair contract covering every defect.
```
