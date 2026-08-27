# A4 — Transport constants for variational inference

## Entry points

- Headline node: `q:a4-certificate`
- Manuscript: [`modules/open-targets/A4-variational-inference.tex`](../../../modules/open-targets/A4-variational-inference.tex) (`q:a4-certificate`)
- Numerical target: [`finum/targets/a_series/a4.py`](../../../experiments/finum/targets/a_series/a4.py), `finum run A4`
- Baselines: `thm:glm-fi`, `prop:a4-logistic-global`

## Target-specific guardrails

- `obs:restricted-not-finite` — a KL cutoff alone need not give finite $W_2$ radius; state
  family coercivity, compactness, or quadratic-exponential tail control.
- `obs:flat-direction` and `obs:gaussian-tail-rigidity` — global location-rich logistic constants
  remain prior-scale, so posterior-scale claims must be localized.
- `obs:symmetry-vs-physical` — multimodal lower bounds depend on the variational family and should
  be compared with the appropriate quotient problem.
- Keep raw approximation error separate from optimizer-centered excess-KL geometry, and treat an
  upper bound on $\log Z$ as a separate requirement for an end-to-end certificate.

## Active handoff

| node | requested deliverable |
|---|---|
| `q:a4-certificate` | State and prove a finite-radius posterior-scale certificate with explicit coercivity and remainder terms. |
| `q:a4-restricted` | Compute localized raw and optimizer-centered constants for a specified posterior/family pair. |
| `q:a4-mean` | Characterize family-restricted mean constants using the proved cumulant duals. |
| `q:a4-modified` | Match robust-prior tail classes with defensible modified transport costs. |
| `q:a4-multimodal` | Turn component-reweighting and mode-collapse witnesses into family-dependent bounds. |
| `q:a4-elbo` | Pair the localized constant with a computable upper KL certificate. |

## Candidate refinement

### Exact replacement for `q:a4-modified`

For $1\le p\le2$, let
$\theta_p(t)=t^2$ for $|t|\le1$ and
$\theta_p(t)=\frac2p|t|^p+1-\frac2p$ for $|t|\ge1$.  The global one-dimensional
generalized-normal branch is closed by `thm:a4-modified-transport-1d`: for
$\pi_p(dx)\propto e^{-|x|^p}dx$ there is $a_p>0$ such that
$\mathcal T_{\theta_p(a_p\,\cdot)}(q,\pi_p)\le\KL(q\|\pi_p)$ for every $q$.  The same theorem
rules out a global transport--entropy inequality with any nonzero unbounded convex cost for a
polynomial-tail Student or horseshoe law.  Neither conclusion is an open deliverable of this
node.

The first residual target is the one-dimensional Student-logistic posterior and fixed-scale
Gaussian location family
$$
 \pi_{\nu,n}(dx)=Z_{\nu,n}^{-1}
 \left(1+\frac{x^2}{\nu}\right)^{-(\nu+1)/2}\operatorname{sigmoid}(x)^n\,dx,
 \qquad \nu>2,\quad n\in\mathbb N,\ n\ge1,
 \qquad
 \mathcal Q_s=\{q_m=N(m,s^2):m\in\mathbb R\},\quad s>0.
$$
Writing $K(m)=\KL(q_m\|\pi_{\nu,n})$ and
$\delta=\min_m K(m)$, first prove that $K$ is continuous and coercive, that $\delta>0$, and that every complete
sublevel $M_\rho=\{m:K(m)\le\delta+\rho\}$ is nonempty and compact.  Then determine explicit
matching upper and lower bounds, including the sharp large-$\rho$ order, for
$$
 C_{\nu,n,s}(\rho)
 :=\sup_{m\in M_\rho}
 \frac{W_2^2(q_m,\pi_{\nu,n})}{2K(m)},
 \qquad \rho\ge0.
$$
Finiteness must be deduced from this named family's coercive compact sublevel and the
$\mathcal P_2$ moment condition $\nu>2$; a KL cutoff alone is not a finiteness hypothesis.
Any finite bound here improves the global baseline $+\infty$ only on this family and sublevel.
For horseshoe posteriors, a later target must first specify a weighted, weak, bounded, or
otherwise finite cost and its family coercivity contract; no global unbounded-convex-cost claim
is retained.
