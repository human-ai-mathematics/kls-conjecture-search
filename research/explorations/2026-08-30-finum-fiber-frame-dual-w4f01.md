# finum: fiber-frame-dual — all-frame simplex min-max library for `conditional-fiber-frame`

Date: 2026-08-30

Role: `finum`

Run id: `w4f01`

Gate served: `q:conditional-fiber-frame` (research/kls/gating.md). Quoting the gate: "A
root-frame-only argument or a floating finite computation does not decide the all-frame gate."
**Nothing below changes any logical status.** Every number is directional research evidence;
every exact rational certificate is a *candidate* requiring a prover and an independent
proof-checker before it has logical force.

Write scope: `experiments/finum/targets/kls/fiber_frame_dual/` (new target, registry row,
oracle tests `experiments/tests/test_18_fiber_frame_dual.py`, README row), two tool-emitted
artifacts under `research/runs/`, and this append-only exploration.

## What was asked

For the isotropic uniform simplex ($X=R_m(P-\tfrac1m\mathbf1)$, $P\sim\mathrm{Dir}(1,\dots,1)$,
$d=m-1$, $R_m=\sqrt{m(m+1)}$), probe the all-frame degree-$k$ min–max of probe `w1f01` (eq. 43)

$$\Lambda_{m,k}=\sup_{\rho\ \text{admissible}}\ \lambda_{\min}\Big(d\int B_{m,k}(\theta)\,d\rho(\theta),\ G_{m,k}\Big)$$

on the quotient $V_{m,k}$. Channels: (A) exact root-frame gaps $\lambda^{\mathrm{root}}_{m,k}$,
$k=2,3$; (B) frame-library lower bounds (root, vertex, admissible mixtures, uniform spherical
frame); (C) exact cap-descent proxies $f_j=P_1^j$ centered, $j=2..k$; (D) optimized rational
mixture with exact re-verification.

## Pre-registered thresholds (fixed before running; stamped into both artifacts' config)

- **Directional against the route:** gap_lib$(m,2)$ decreases monotonically from $m=4$ to the
  top computed $m$ by a total factor $\ge 3$ AND is $<0.1$ at the top $m$.
- **Constructive lead:** some single frame family keeps its degree-2 gap $\ge 0.2$ for all
  computed $m$.
- **Exact-certificate escalation:** only an exact rational witness proving
  $\Lambda_{m,2}\ge c$ for all computed $m$, or an exact dual certificate proving
  $\Lambda_{m,2}\le\varepsilon_m\downarrow$, is a prover-escalable candidate — never a status
  change.

## What ran

Artifacts (tool-emitted, never hand-edited):

- `research/runs/2026-08-30T172853.262299Z-fiber-frame-dual.jsonl` — profile `standard`,
  seed `20260830`.
- `research/runs/2026-08-30T173244.394413Z-fiber-frame-dual.jsonl` — profile `deep`,
  seed `20260830` (superset ranges; 40k spherical samples/seed).

Environment as recorded: Python 3.13.12, numpy 2.4.6, scipy 1.18.0, Linux 6.17;
`git_commit: cd4a894a` **plus the uncommitted `fiber-frame-dual` worktree diff** delivered
together with this exploration (the orchestrator harvests the diff; the artifact configs record
the exact battery).

Discipline: `uv run python -m finum check` green before and after the code change
(baseline and 7 new target checks); `uv run pytest -m "not slow"`: 115 passed. Exact channels
are deterministic and reproduced identically across the two artifacts on their overlap.

Method summary (all exact channels in `fractions.Fraction`, no floating input):

- Basis of $V_{m,k}$: monomials in $p_1..p_{m-1}$, degrees $1..k$. $G$ from exact Dirichlet
  moments (probe eq. 30). Root pencil from the closed Dirichlet-neutrality formula
  (probe eqs. 28–29, 31).
- Vertex orbit ($\theta_i\propto e_i-\tfrac1m\mathbf1$, an admissible tight frame): the chord
  conditional law is uniform; along a vertex chord the argmin over the other coordinates is
  chord-constant, so the simplex splits into $m-1$ polyhedral chambers; the chamber
  $\{\arg\min_{\ell\ge2}p_\ell=2\}$ maps unimodularly onto a weighted simplex where monomial
  moments are exact factorials. One chamber matrix is computed on the full $m$-variable
  monomial list; all other (direction, chamber) pairs follow by exchangeability relabeling.
- Certification: for each exactly assembled frame pencil, an exact rational Rayleigh quotient
  (upper bound on $\lambda_{\min}$) and an exact integer Bareiss/Sylvester positive-definiteness
  test of $K-\lambda G$ (certified lower bound). $G\succ0$ certified per $(m,k)$ the same way.
  Since a library member lower-bounds the sup, each certified $\lambda_{\mathrm{lo}}$ is a
  **certified rational lower bound on $\Lambda_{m,k}$**.
- Mixtures $\alpha\,\rho_{\mathrm{root}}+(1-\alpha)\rho_{\mathrm{vertex}}$: admissible for all
  $\alpha\in[0,1]$ (the frame constraint is linear); concave $\lambda_{\min}(\alpha)$ scanned,
  refined, rationalized, re-certified exactly (channel D).
- Spherical frame: seeded double MC over $(\theta,p)$ with per-sample exact Gauss–Legendre chord
  moments; two-seed agreement gate and the exact linear-block anchor. **Directional only.**

Calibration anchors (run aborts on failure; all passed, exactly):

1. closed root formula == independent chord/chamber machinery, entrywise Fraction equality
   ($m=3,4$ at $k=2$; $m=3$ at $k=3$);
2. linear sector quotient $\equiv1$: $K_{\mathrm{lin}}=G_{\mathrm{lin}}$ exactly for root and
   vertex at every computed $(m,k)$;
3. radial quadratic root quotient $=(m+2)(m+3)/(5m^2)$ exactly at every computed $(m,k)$;
4. per-direction radial energy $=\tfrac{4}{5}R_m^{-4}$ exactly (probe eq. 35), $m=3,4$;
5. vertex frame == root frame at $m=2$ exactly; vertex machinery independently cross-checked
   against a seeded MC direction estimator at $m=3$ (5% tol) in the oracle suite;
6. spherical MC linear block vs exact Gram: max rel. dev. 0.6%–1.8%, all two-seed converged.

## Numbers

$k=2$ (float $\lambda_{\min}$; exact certified enclosures in the artifacts; every exact frame
value below is bracketed by certified rationals to $\le10^{-7}$ relative):

| $m$ | root (exact) | vertex (exact) | best mixture $\alpha^*$ | spherical (directional) | certified $\Lambda_{m,2}\ge$ |
|---|---|---|---|---|---|
| 3 | 2/3 | 0.763573 | 0 (=vertex) | 0.7523 | 20946790/27432587 ≈ 0.763573 |
| 4 | 21/40 | 0.617488 | 0 | 0.6629 | ≈ 0.617488 |
| 5 | 56/125 | 0.533861 | 0 | 0.6115 | ≈ 0.533861 |
| 6 | 2/5 | 0.481046 | 0 | 0.5793 | ≈ 0.481046 |
| 7 | 18/49 | 0.444905 | 0 | 0.5509 | ≈ 0.444905 |
| 8 | 11/32 | 0.418683 | 0 | 0.5337 | ≈ 0.418683 |
| 9 | 44/135 | 0.398813 | 0 | 0.5179 | ≈ 0.398813 |
| 10 | 39/125 | 0.383246 | 0 | 0.5054 | ≈ 0.383246 |
| 11 | 182/605 | 0.370726 | 0 | — | ≈ 0.370726 |
| 12 | 7/24 | 0.360441 | 0 | 0.4814 | ≈ 0.360441 |
| 13 | 48/169 | 0.351842 | 0 | — | ≈ 0.351842 |
| 14 | 68/245 | 0.344548 | 0 | 0.4681 | 30383793/88184617 ≈ 0.344548 |
| 15 | 34/125 | — | — | — | 7998123/29404864 ≈ 0.272000 |

$k=3$:

| $m$ | root | vertex | $\alpha^*$ | spherical (directional) | certified $\Lambda_{m,3}\ge$ |
|---|---|---|---|---|---|
| 3 | 0.571736 | 0.761488 | 0 | 0.7521 | 9948137/13064070 ≈ 0.761488 |
| 4 | 0.402708 | 0.608712 | 0 | 0.6587 | ≈ 0.608712 |
| 5 | 0.315776 | 0.504905 | 0 | 0.6063 | ≈ 0.504905 |
| 6 | 0.263863 | 0.432571 | 0 | 0.5725 | ≈ 0.432571 |
| 7 | 0.229739 | 0.380592 | 0 | 0.5428 | 33271711/87420976 ≈ 0.380592 |
| 8 | 0.205762 | 0.342115 | 0 | — | 33432429/97722661 ≈ 0.342115 |

Cap-descent proxies (exact; root frame, the worst family — full per-frame values in the
artifacts): quotient of centered $P_1^2$: $16/21\ (m{=}3)\to 272/675\approx0.403\ (m{=}15)$;
quotient of centered $P_1^3$: $0.694\ (m{=}3)\to 0.346\ (m{=}8)$. Successive decrements shrink
(final $\lambda m$ products *increase* with $m$), i.e. decay is slower than $1/m$ over the
computed range for every proxy and frame; no proxy shows a vanishing trend.

## Key observations

1. **An exact pattern in channel A.** At every $m=3..15$ the exact rational Rayleigh upper
   bound for the root pencil at $k=2$ equals $(m+2)(m+3)/(5m^2)$ **exactly** — the radial
   quadratic value of probe eq. 36 — and the certified lower bound sits within $10^{-7}$ below
   it. So on this whole range the radial quadratic $F=|X|^2-d$ *is* the degree-2 root
   minimizer, and $\lambda^{\mathrm{root}}_{m,2}=(m+2)(m+3)/(5m^2)\to 1/5$. This is an exact
   analytic **candidate identity** (finite-$m$ certificates only; the all-$m$ statement is a
   conjecture with a plausible $S_m$-isotypic proof). Consequence *if proved for all $m$*:
   $\Lambda_{m,2}\ge\lambda^{\mathrm{root}}_{m,2}\ge 1/5-o(1)$, so **no degree-2 dual
   certificate can refute the route**; any fixed-degree refuter needs $k\ge3$.
2. **The vertex frame strictly beats the root frame** at both degrees and every computed $m$,
   and the optimal root/vertex mixture is always the pure vertex frame ($\alpha^*=0$; the
   concave mixture scan never found an interior optimum). This is coherent with the analytic
   story: the root frame's $L^2$ killer is a vertex cap, and vertex-to-opposite-face directions
   are exactly what the root orbit lacks.
3. **The rotation-invariant spherical frame beats both** for $m\ge4$ (directional): degree-2
   gap $\approx0.47$ at $m=14$ and degree-3 gap $\approx0.54$ at $m=7$, decaying slowly.
   Spherical $k=3$ values essentially equal the $k=2$ values at the same $m$, suggesting its
   low sector is quadratic.
4. **Certified floors on the min–max:** exact rational witnesses give
   $\Lambda_{m,2}\ge0.3445$ for all computed $m\le14$ (vertex certificates) and
   $\Lambda_{m,3}\ge0.3421$ for $m\le8$. These are finite-$m$ facts, not route decisions.
5. **Cap descent does not appear at fixed degree.** All polynomial cap proxies decay slower
   than $1/m$ and appear to level off well above zero. The known $O(m^{-2})$ vertex-cap
   refutation of the root frame does not descend to degree $\le3$ on the computed range.

## Pre-registered threshold outcomes

- **Directional-against: NOT met.** gap_lib decayed by total factor 1.42 (deep; threshold 3)
  and ends at 0.468 (threshold 0.1). The recorded `monotone_decreasing: false` is a *coverage
  artifact*: the spherical channel was not computed at $m\in\{11,13\}$, so gap_lib dips to the
  vertex value there; each individual family is monotone decreasing in $m$.
- **Constructive lead: MET** by root, vertex, and spherical at $k=2$ (all stay $\ge0.2$; root
  exactly at $(m+2)(m+3)/(5m^2)\ge0.272$ up to $m=15$).
- **Escalation:** no route-deciding exact certificate in either direction. The candidate exact
  identity of observation 1 is the only prover-grade item, and it *supports* rather than
  refutes the route at degree 2.

Overall reading: **directionally pro-route at fixed degree** on the computed range. The
finite-degree min–max shows no sign of collapse; the library keeps uniform-looking gaps, with
frames that weight long vertex directions doing better — consistent with the analytic
prediction that only non-polynomial (cap-type) tests can kill specific frames. This does not
decide the gate (a slow decay to 0 beyond the computed range, or at higher degree, is not
excluded).

## Dead ends and honest limitations

- **Normalization trap (implementation dead end, caught by the linear anchor):** the fiber
  quotient must be normalized by the variance of the *isotropic arc-length* coordinate
  $T=\langle X,\theta\rangle$, not of an arbitrary affine chord parameter; the exact conversion
  factors are $(dT/dw)^2 = 2m(m+1)$ (root chord) and $m^2(m+1)/(m-1)$ (vertex chord). The
  first assembly omitted them and failed the exact linear anchor immediately — keep the anchor.
- The "midpoint" orbit ($e_i+e_j-2e_l$ directions, channel (iv)) was **not** implemented: its
  $O(m^3)$ orbit does not collapse to a single chamber computation under the basis used, and
  cost was spent on the exact vertex orbit + spherical channel instead. Honest gap; the
  spherical frame dominates the computed library anyway.
- Only root+vertex orbits enter the exact mixture optimization, so channel D is a 1-parameter
  concave problem; a richer orbit union could only raise the certified floors.
- The $k=3$ root trend ($0.572\to0.206$ over $m=3..8$) is undecided between a positive limit
  and slow decay; larger $m$ at $k=3$ is the natural next exact run (cost: the $n=119$ pencil
  at $m=8$ was the practical ceiling for this wave).
- Spherical values are Monte Carlo (20k/40k samples per seed, two seeds, agreement $\le2\%$);
  they are directional and never enter a certificate.
- The gap_lib monotonicity flag conflates library coverage with mathematics (see above); read
  per-family columns.

## Proposed adversarial instance (for the synthesizer; registry is not edited here)

| id | route | adversarial property | `finum` |
|---|---|---|---|
| `stress-fiber-frame-simplex-pencil` | conditional-fiber-frame | fixed-degree all-frame min–max $\Lambda_{m,k}$ on the isotropic uniform simplex; exact rational frame-pencil certificates plus directional spherical frame | `fiber-frame-dual` (`standard`, `deep`) |

Why the battery does not already cover it: the existing KLS registry rows are moment-map/CMH
instances; nothing exercises conditional-fiber (chord-variance-normalized) forms or all-frame
pencils.

## Explicitly

No ledger, manuscript, gating, routes, knowledge, solutions, or reviews file was touched. No
status change is implied by these runs. An exact certificate emitted here remains a candidate
until independently proved and reviewed.
