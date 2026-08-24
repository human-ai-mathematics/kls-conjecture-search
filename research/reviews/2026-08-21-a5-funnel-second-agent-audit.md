# A5 funnel second independent-agent audit

- **Date:** 2026-08-21
- **Original proof author:** `/root/a4_a5`
- **Proof-gap completion:** `/root/review_a4_a5`
- **Independent second reviewer:** `/root/cross_review`
- **Certification:** `checked_by: agent`
- **Verdict:** pass for the three nodes below

## Certified scope

1. `lem:a5-pi-exp-tail` — a finite Euclidean Poincaré constant forces a small exponential moment
   for every real $1$-Lipschitz $L^2$ observable.
2. `ex:a5-neal` — infinite centered Euclidean Poincaré constant, exact noncentered product
   constant $\max\{s^2,1\}$, and failure of global Lipschitz comparison in both directions.
3. `prop:a5-partial-funnel` — for $s>0$, every partial coordinate with $0\le\alpha<1$ has
   infinite Euclidean Poincaré constant, whereas $\alpha=1$ has constant $\max\{s^2,1\}$.

The lemma is proved in both reviewed artifacts,
[`solutions/ex-a5-neal.tex`](../../solutions/ex-a5-neal.tex) and
[`solutions/prop-a5-partial-funnel.tex`](../../solutions/prop-a5-partial-funnel.tex).

## Checks performed

The audit checked the independent-copy variance lower bound for the truncated ramp, its energy
bound, the resulting half-tail contraction with step $2\sqrt C$, two-sided iteration, and the
small exponential moment forced by a finite Euclidean Poincaré inequality. It then checked the
exact second moments, divergence of every positive lognormal exponential moment, the median
translation, the coordinate-wise Lipschitz witnesses in each declared Euclidean metric, Gaussian
product tensorization, and the unbounded Jacobians of both coordinate maps.

The first review had identified the missing Poincaré-to-exponential-integrability step. That step
was supplied by `/root/review_a4_a5` and therefore was not self-certified: `/root/cross_review`
performed this second audit. The final statements explicitly assume $s>0$; without that
hypothesis the partial-funnel claim would fail at the degenerate endpoint $s=0$. Both dossiers
compile standalone with clean final logs.

## Explicit exclusions

The statements concern the prior-only/weak-data Neal law. A likelihood can change the tail
integrability, and no likelihood-dependent interior partial-noncentering phase is certified here.
