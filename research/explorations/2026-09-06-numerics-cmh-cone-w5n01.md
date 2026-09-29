---
artifacts:
  - research/runs/2026-09-06T175558.606924Z-cmh-cone.jsonl
  - research/runs/2026-09-06T175611.501834Z-cmh-cone.jsonl
candidates:
  - id: cand:cmh-exponential-galerkin-rate
    statement: >-
      Let mu be a product of n independent centered one-sided exponentials, or any
      invertible linear image of one -- in particular the exponential cone measure
      bar mu_{K,beta} of def:exponential-cone with K = Delta_{n-1} and beta = n. For every
      integer d >= 1 the supremum of the CMH Rayleigh quotient of def:cmh over the span of
      the monomials of x of total degree 1..d equals exactly 2 + 2 cos(pi/(d+1)) =
      4 cos^2(pi/(2(d+1))), independently of n. The value increases strictly to the exact
      constant CMH(mu) = 4 of thm:cmh-1d and thm:cmh-product and is never attained, so the
      saturating endpoint of the CMH route is approached at rate 4 - pi^2/(d+1)^2 + O(d^-4)
      by polynomial test functions. Reason to believe it: on the orthonormal Laguerre basis
      of the centered exponential, tau(s) = s, L_mu L_k = -k L_k and s L_k' = k(L_k -
      L_{k-1}), so on span{L_1,...,L_d} the quotient equals 2 - 2 (sum_k w_k w_{k-1}) /
      (sum_k w_k^2) after the substitution w_k = k v_k, whose maximum is the extreme
      eigenvalue 2 cos(pi/(d+1)) of the d x d tridiagonal matrix with zero diagonal and -1
      off-diagonal; CMH and the total-degree polynomial spaces are both affine invariant,
      and thm:cmh-product transfers the one-dimensional value to the product. Reason to
      doubt it: the transfer to a product asserts that no genuinely multivariate degree-d
      polynomial beats the best univariate one, which the run confirms numerically for
      n = 2, 3, 4 and d <= 10 but which is not proved here.
  - id: cand:cone-transverse-equality-simplex
    statement: >-
      Within the exponential cone family of def:exponential-cone with base K a Cartesian
      product Delta_{k_1} x ... x Delta_{k_r} x [-1,1]^s, the normalized gate matrix
      Sigma^{-1/2} E[tau Sigma^{-1} tau] Sigma^{-1/2} satisfies conj:gate-zero-sharp with
      equality in a direction transverse to the cone axis if and only if r = 1, s = 0 and
      beta = n, i.e. if and only if the cone is a linear image of n i.i.d. centered
      exponentials, in which case the whole gate matrix equals 2 Id. For every other base
      in the family and every beta >= n, the axis value 1 + n/beta of
      prop:cone-linear-sector is the unique equality case at beta = n and every transverse
      eigenvalue is strictly below 2. Reason to believe it: exact rational arithmetic
      decides the Loewner inequality 2 Sigma - E[tau Sigma^{-1} tau] >= 0 on 264 instances
      spanning m <= 7 product bases, single simplices up to Delta_12, and beta in
      {n, n+1, 2n, 5n}, and the spectra separate exactly this way; as beta -> infinity the
      transverse block tends to the base's own gate ratio, which is 2(m+2)/(m+4) < 2 for a
      simplex base and 6/5 for a cube base. Reason to doubt it: the family is a finite
      polytopal slice of the log-concave cone, the claim quantifies over all beta and all
      block shapes, and every number is computed from eq:cone-stein-kernel, whose node
      prop:cone-moment-map was open when this was proposed and has since been proved.
---

# Exponential cones: exact gate matrices, ball quadrature, and CMH Galerkin

`numerics` run `w5n01`, identity `/w5/numerics-cone`, concurrency key `numerics-code`.
New target `cmh-cone` (`experiments/numerics/targets/kls/cmh_cone/`), profiles `standard`
and `exact-only`, plus oracle tests in `experiments/tests/test_19_cmh_cone.py`.

**No status change is implied by anything below.** Every number is computed *from*
eq:cone-stein-kernel, and its node `prop:cone-moment-map` is `open`: a disagreement would
indict the formula at least as readily as the conjecture. Gate zero is necessary for
$\mathrm{CMH}(4)$ and never sufficient, and a finite family of bases supports no universal
statement (`CLAUDE.md` constraints 2 and 3).

## What was asked

Four diagnostics on $\bar\mu_{K,\beta}$ (`subsec:cmh-cones`): the exact gate matrix of cube
cones against the closed form of `cor:cube-cone-gate-zero`; the exact gate pencil of cones
over products of simplices and intervals; the transverse gate eigenvalue of ball cones by
quadrature; and a CMH Galerkin lower bound on cube cones as the replacement for the M9
probe.

## Thresholds, fixed before the run

| channel | refutes | merely consistent |
|---|---|---|
| 1, 2 (exact) | an exact rational Rayleigh lower bound $>2$ for the pencil $(\E[\tau\Sigma^{-1}\tau],\Sigma)$ refutes `conj:gate-zero-sharp`; $>4$ refutes `conj:gate-zero` and hence $\mathrm{CMH}(4)$ | a complete LDL$^\top$ of $c\Sigma-M$ with nonnegative rational pivots, which *decides* $\lambda_{\max}\le c$ on that instance |
| 3 (quadrature) | transverse eigenvalue $>2$ is a directional break of `conj:gate-zero-sharp` worth analytic follow-up | a reported margin below 2 |
| 4 (Galerkin) | an exact rational lower bound $>4$ at $n\ge3$, stable under one degree refinement, is a refutation candidate for $\mathrm{CMH}(4)$ | a value below 4, read against the exponential-product endpoint at the same degree |

Both directions are realisable: the Loewner test returns an explicit rational negative
direction when it fails, so channels 1 and 2 can contradict, not only fail to contradict.

## What came back

**Channel 1 — cube cones, exact.** 20 instances, $n\in\{2,3,4,5,8\}$,
$\beta\in\{n,n+1,2n,5n\}$. The exact rational gate matrix equals
$(1+n/\beta)\oplus\frac{6\beta^2+11\beta+5n+4}{5\beta(\beta+1)}\mathrm{Id}_{n-1}$ entry by
entry on every instance, with the off-axis block exactly zero. `cor:cube-cone-gate-zero` is
reproduced exactly, including the $n=\beta=2$ anchor $G=2\,\mathrm{Id}_2$.

**Channel 2 — products of simplices and intervals, exact.** 244 instances: every
$\Delta_{k_1}\times\cdots\times\Delta_{k_r}\times[-1,1]^s$ with $r\le3$, $k_i\le3$,
$s\le3$, $m\le7$, plus single simplices $\Delta_k$, $k\in\{4,5,6,8,12\}$, each at
$\beta\in\{n,n+1,2n,5n\}$. **All 264 exact instances (channels 1 and 2) are decided
$\lambda_{\max}\le2$ by a complete rational LDL$^\top$; none contradicts, at 2 or at 4.**
The largest exact rational Rayleigh lower bound over the whole sweep is exactly $2$,
attained at all 66 instances with $\beta=n$.

The spectra separate cleanly. At $\beta=n$ a *single* simplex base gives the whole spectrum
$\equiv2$ (`cone-S5-n6-b6` $\to[2,2,2,2,2,2]$, the exponential product), while every genuine
product base has the axis at 2 and all transverse eigenvalues strictly below
(`cone-S2S3-n6-b6` $\to[1.6857,1.6857,1.8186,1.8186,1.8186,2]$). That is
`cand:cone-transverse-equality-simplex`.

One structural point the manuscript does not currently make: **the axis is not always the
maximizing direction.** `prop:cone-linear-sector` (ii) pins only the axis value
$1+n/\beta$; for $\beta>n$ the transverse block can exceed it, by up to $+0.588$ in this
sweep (`cone-S12-n13-b65`: $\lambda_{\max}=1.7883$ against an axis value of $6/5$). The
transverse block tends to the *base's own* gate-zero ratio as $\beta\to\infty$
— $2(m+2)/(m+4)$ for $\Delta_m$, $6/5$ for the cube — so within this family the transverse
sector is fenced by sharp gate zero for the base, and the cone construction never amplifies
it above 2.

**Channel 3 — ball cones, quadrature (directional).** The radial moment-map ODE
$\Lambda'(s)^m=\nu(B_s)$ was integrated with DOP853 at `rtol=1e-12`. Calibrations: the
$m=1$ solution is $\Lambda'=2\tanh s$ giving $\tau=(4-r^2)/2$ to $2.4\times10^{-12}$; the
traced Stein normalisation $\E\alpha+(m-1)\E\beta_\perp=\E|U|^2$ holds to $<10^{-9}$ for
every $m$; and the $m=1$ ball cone reproduces the $n=2$ cube closed form to
$3.3\times10^{-14}$. Transverse eigenvalues at $\beta=n$:

| $m$ | 1 | 2 | 3 | 5 | 10 |
|---|---|---|---|---|---|
| transverse | 2.000000 | 1.703906 | 1.547016 | 1.381613 | 1.220560 |
| margin below 2 | 0.000000 | 0.296094 | 0.452984 | 0.618387 | 0.779440 |

No directional break; the margin *widens* with dimension. The ball is a smooth,
non-polytopal, non-product base and it is strictly safer than the simplex.

**Channel 4 — CMH Galerkin, exact matrices.** Both moment matrices are exact `Fraction`
matrices; only the generalized eigenvalue is floating, and one rationalized eigenvector is
re-evaluated exactly as a certified lower bound. The Bochner identity of `prop:cmh-bochner`
holds **exactly** (residual $=0$ in `Fraction` arithmetic) on every basis function and on
every certified witness, so the polynomial span carries no boundary defect on the cone.

| instance | $d=2$ | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| exponential product ($\Delta_{n-1}$, $\beta=n$; $n=2,3,4$) | 3.000000 | 3.414214 | 3.618034 | 3.732051 | 3.801938 |
| cube cone $n=3$, $\beta=3$ | 2.776137 | 3.034515 | 3.153062 | 3.210872 | 3.244699 |
| cube cone $n=4$, $\beta=4$ | 2.637497 | 2.813867 | 2.877087 | 2.899291 | — |
| cube cone $n=3$, $\beta=4$ | 2.290068 | 2.440877 | 2.491090 | 2.507989 | — |

The exponential-product row is exactly $2+2\cos(\pi/(d+1))$ — verified to $d=10$ and
derived from the Laguerre basis; that is `cand:cmh-exponential-galerkin-rate`, and it is
now a calibration anchor of the target. The cube-cone rows sit strictly below it at every
degree and flatten faster. **Nothing exceeded 4**, and the cube cone is not a saturating
family: the transverse base directions dilute the one-dimensional exponential mechanism
rather than adding to it.

## Interpretation

Directional, consistent, no escalation. Concretely for the search:

- `conj:gate-zero-sharp` survives an exact test on 264 cone instances, and its equality
  set inside this family is exactly the exponential products. The family therefore supplies
  no counterexample and no near miss — the maximum is *attained* at 2 and never exceeded.
- The cube cones were proposed in `subsec:cmh-cones` as the natural place to test
  $\mathrm{CMH}(4)$ beyond the product endpoint of `rem:cmh-saturation-risk`. On this
  evidence they do **not** realise the perturbation `q:cmh-solenoidal-perturbation` asks
  for: at equal polynomial degree they are strictly *below* the saturating product, and
  the gap grows with $n$ and with $\beta-n$. Route C's saturation risk is not resolved,
  but this particular perturbation direction looks flat-to-downhill.
- A perturbation that could raise CMH above 4 has to move the *radial* mechanism, not the
  base: every quantity here that touches 2 or 4 is the Gamma factor's, and every base
  contribution seen so far is strictly dissipative.

## Caveats a reader must carry

- Everything is computed from eq:cone-stein-kernel; `prop:cone-moment-map` is `open`.
- Gate zero is necessary for $\mathrm{CMH}(4)$, never sufficient; a passed battery is not
  evidence for CMH or KLS.
- Channel 3 is quadrature and is `directional` by construction, whatever its residuals.
- Channel 4's certified lower bounds degrade at high degree: at $d=8$, with the whitened
  denominator conditioned at $1.9\times10^{7}$, the rationalized eigenvector certifies only
  $2.809$ where the floating eigenvalue is $3.879$. The floating value is the diagnostic;
  the exact value is the only thing with certificate status, and it is a lower bound, so
  the degradation is safe in the direction that matters.

## Proposed adversarial and calibration instances

For the `synthesizer` only (`CLAUDE.md` constraint 3); not added to
`research/instances.md` here. The existing CMH battery is one-dimensional closed forms,
Dirichlet laws, and one algebraic countermodel: it has no non-compactly-supported instance,
no instance whose *base geometry* is a free parameter, and no non-product instance that
saturates the sharp linear sector in $n\ge3$. These fill exactly that hole.

| proposed id | tier | object | oracle / adversarial property | `numerics` |
|---|---|---|---|---|
| `cal-cmh-cone-axis` | calibration | $\bar\mu_{K,\beta}$, any base | axis gate value $=1+n/\beta$ | `cmh-cone / cal-cmh-cone-axis` |
| `cal-cmh-cone-cube-closed-form` | calibration | cube cone | `cor:cube-cone-gate-zero`, exactly | `cmh-cone / cal-cmh-cone-cube-closed-form` |
| `cal-cmh-cone-simplex-product` | calibration | $K=\Delta_{n-1}$, $\beta=n$ | $M=2\Sigma$ exactly | `cmh-cone / cal-cmh-cone-simplex-product` |
| `cal-cmh-cone-galerkin-chebyshev` | calibration | exponential product | degree-$d$ CMH Galerkin $=2+2\cos(\pi/(d+1))$ | `cmh-cone / cal-cmh-cone-galerkin-chebyshev` |
| `cal-cmh-cone-ball-1d` | calibration | $m=1$ radial moment map | $\Lambda'=2\tanh s$, $\tau=(4-r^2)/2$ | `cmh-cone / cal-cmh-cone-ball-1d` |
| `stress-cmh-cube-cone` | stress | cube cone, $n\ge3$ | non-product, saturates the linear sector, unbounded support | `cmh-cone / cone-cube-n{n}-b{beta}` |
| `stress-cmh-simplex-product-cone` | stress | $\Delta_{k_1}\times\cdots$ at $\beta=n$ | saturating and non-product for $r\ge2$; separates axis from transverse equality | `cmh-cone / cone-{base}-n{n}-b{beta}` |
| `stress-cmh-ball-cone` | stress | ball cone | smooth non-polytopal base; tests the kernel away from facets | `cmh-cone / cone-ball-m{m}-b{beta}` |

## Reproduction

```bash
cd experiments && uv run pytest                       # includes tests/test_19_cmh_cone.py
cd experiments && uv run pytest -m slow               # the full standard battery, ~13 s
cd experiments && uv run python -m numerics check cmh-cone
cd experiments && uv run python -m numerics run cmh-cone --profile standard
cd experiments && uv run python -m numerics run cmh-cone --profile exact-only
```

Both artifacts record `seed=0`, `git_commit 5b772c9` with `git_dirty: true`
(`git_diff_sha256 5ce1063d…`), Python 3.13.12, numpy 2.4.6, scipy 1.18.0. The target is
deterministic and uses no Monte Carlo; determinism is not a rigor certificate.

Five earlier artifacts of this target, emitted while the sweep configuration and the
module's imports were still being fixed, were removed before the final runs: each records a
`git_diff_sha256` for a worktree state that no longer exists, so none of them is
reproducible from the repository, which is the only thing that makes an artifact worth
keeping. The two runs cited above are the complete record of this work, and their numbers
are identical to the superseded ones on every instance they share.
