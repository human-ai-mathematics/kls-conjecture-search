---
---
# finum: the CMH anisotropic bootstrap $(\mathsf N,\mathsf D,\mathsf R)$ and the M9 probe

Date: 2026-08-30

Role: `finum`

Run id: `w4c02`

Concurrency key: `finum-code`

Artifact: [`research/runs/2026-08-30T180751.811560Z-cmh-ab.jsonl`](../runs/2026-08-30T180751.811560Z-cmh-ab.jsonl)

New target: `experiments/finum/targets/kls/cmh_ab/` (registry id `cmh-ab`), oracle suite
`experiments/tests/test_18_cmh_ab.py`. The certified `cmh_gate_zero` module was not modified; it
is imported read-only for two cross-checks.

**No status changes.** Nothing below certifies a claim, a proof step or a dossier. The exact
rational Loewner verdicts are candidates; channel 1(c) and channel 2 are quadrature on finite
grids and are directional in every case.

## 1. What was asked, and what was actually computed

Two channels from `2026-08-27-kls-route-prober-cmh-linear-recovery-w3c01.md` and the M9 task of
`2026-08-25-kls-cmh-normalization-layer.md`.

**Channel 1.** In source coordinates with source density $e^{-\psi}$, $H=D^2\psi$,
$\eta=e^{-\psi}\,dy$:

$$\mathsf N=\int H^2\,d\eta,\qquad
\mathsf D=\int H^{ab}(\partial_aH)(\partial_bH)\,d\eta,\qquad
\mathsf R=\mathsf N-\mathsf D,$$

with the probe's certified-in-probe facts $\mathsf N=\mathsf D+\mathsf R$ for
$\mathsf R=\tfrac12\int\{H,A+Q\}$ and $\mathsf N-I\preceq\mathsf D$, and the open candidate
$({\rm AB})_{\rho,\beta}$: $\mathsf R\succeq\rho\mathsf N-\beta I$, sharp form
$\mathsf R\succeq\mathsf N/2$.

**Channel 2 (M9).** Perturb the moment potential of the saturating product,
$\psi_\varepsilon(s,t)=\phi(s)+t^2/2+\varepsilon a(s)b(t)$, and compute a Galerkin lower bound
for $C_{\mathrm{CMH}}(\mu_\varepsilon)$.

### Coordinate transport, verified before coding

With $x=\nabla\psi(y)$ and $\tilde H(x)=H(y(x))$, the chain rule gives
$\partial_{y_a}H=\sum_bH_{ab}\partial_{x_b}\tilde H$, hence
$H^{ab}(\partial_aH)(\partial_bH)=\tilde H_{cd}(\partial_c\tilde H)(\partial_d\tilde H)$ and

$$v^\top\mathsf Dv=\int\sum_{c,d}\tilde H_{cd}\,
\langle(\partial_c\tilde H)v,(\partial_d\tilde H)v\rangle\,d\mu .$$

The index placement is pinned **four** independent ways, all in the oracle suite:

1. the exact one-dimensional identity $\mathsf N=2\mathsf D+\mathbb E[H^3V'']$ (below);
2. $\mathsf N$ equals $R_1$ of the certified `cmh-gate-zero` battery, law by law, exactly;
3. $\lambda_{\max}(\mathsf N,\Sigma)$ equals the certified gate-zero ratio on Dirichlet
   instances, and $\mathrm{Dir}(a,b)$ on $\Delta_1$ reproduces the standardized $\mathrm{Beta}(a,b)$
   channel exactly;
4. on the two-dimensional geometries, $\mathsf N-\mathsf D$ agrees with
   $\tfrac12\int\{H,A+Q\}$ assembled from the differentiated Monge--Ampère reservoirs through a
   disjoint code path, to relative $1.1\times10^{-13}$.

### Substitution made in channel (c), and why

The task specified a damped-Newton solve of $g(\nabla\phi)\det D^2\phi=e^{-\phi}$ for prescribed
compact targets. That was **not** done. By the Cordero-Erausquin--Klartag characterisation a
moment map is exactly a pair $(\psi,(\nabla\psi)_\#e^{-\psi})$ with $\psi$ convex and $e^{-\psi}$
a probability density, so *prescribing $\psi$ and reading off the target* enumerates the same
class with no PDE solve. All derivatives are then analytic (a truncated two-variable jet
arithmetic to total order four; no step size enters anywhere) and every integral is a
source-coordinate quadrature. The requested residual checks are still computed and reported:
$\int\nabla\psi\,d\eta=0$, $\int H\,d\eta=\Sigma$ ($\mathbb E_\mu H=\mathrm{Cov}$), and
$\mathbb E_\mu[H\nabla f]=\mathbb E_\mu[xf]$ on quadratic $f$ ($\operatorname{Div}_\mu H=-x$),
with a pre-registered abort at $10^{-6}$.

**The cost is real and is the main residue of this record.** The class covered is *perturbed
products* plus the certified Dirichlet maps, not arbitrary compact convex bodies. Prescribing the
source potential cannot produce a target prescribed in advance, and in particular cannot produce
a target-side perturbation that is guaranteed to stay log-concave (see §4).

## 2. Pre-registered thresholds, fixed before the run

Recorded in the artifact under `thresholds` and as module constants:

| threshold | value | meaning |
|---|---|---|
| exact-contradiction escalation | $\lambda_{\min}(\mathsf R-\mathsf N/2)<0$ on an exact rational Dirichlet instance | refutes the sharp candidate $\rho=1/2,\beta=0$ as a universal matrix inequality |
| directional-against (AB) | $\min_{\text{inst}}\rho^*(\beta=1)<0.05$ | — |
| directional-support (AB) | $\rho^*(\beta=0)\ge0.3$ on every instance | — |
| M9 refutation candidate | $q(\varepsilon)>4.05$, stable under one degree and one grid refinement, convexity verified | candidate refutation of $\mathrm{CMH}(4)$ |
| moment-map residual abort | $10^{-6}$ | instance contributes to no verdict |

## 3. Results

### 3.1 One dimension is exactly the wrong place to look (exact)

13 closed-form instances (Gaussian; $\Gamma(a)$, $a\in\{1,2,5,20\}$; $\mathrm{Beta}(a,b)$ for
seven parameter pairs including the uniform interval; Laplace), all in `fractions.Fraction`.

The identity $\mathsf N=2\mathsf D+\mathbb E[H^3V'']$ holds **exactly** on every one, with
$\mathbb E[H^3V'']$ the $A$-reservoir and $\mathsf D$ the $Q$-reservoir. Hence on the line

$$\mathsf R=\mathsf D+\mathbb E[H^3V''],\qquad V''\ge0\ \Rightarrow\ \mathsf R\ge\mathsf D
\ \Leftrightarrow\ \mathsf R\ge\mathsf N/2 ,$$

**always**, with equality exactly on the log-affine densities. Realised: the centred one-sided
exponential has $(\mathsf N,\mathsf D,\mathsf R)=(2,1,1)$ and the uniform interval
$(6/5,3/5,3/5)$; both saturate $\mathsf R=\mathsf N/2$ *and* $\mathsf N-I=\mathsf D$. Every
$\Gamma(a)$ has $\mathsf R=1$ exactly and $\mathsf N=1+1/a$.

So one dimension is a calibration anchor, not a test: it cannot refute the sharp candidate. This
is worth stating because the whole 1-D margin *is* the log-concavity reservoir.

### 3.2 Dirichlet: no exact contradiction, and the saturator identified (exact)

21 exact rational instances: uniform simplices $m=2\ldots8$, the requested anisotropic sweep, and
an extreme-anisotropy family. Everything is a rational question about the chart matrices, because
$\mathsf N_w=\Sigma^{-1/2}\mathcal N\Sigma^{-1/2}$ and $\mathsf D_w=\Sigma^{-1/2}\mathcal D
\Sigma^{-1/2}$ share the same congruence:

$$\mathsf R_w\succeq\mathsf N_w/2\iff \tfrac12\mathcal N-\mathcal D\succeq0,\qquad
\mathsf N_w-I\preceq\mathsf D_w\iff \mathcal D-\mathcal N+\Sigma\succeq0 .$$

Both were decided by exact symmetric-pivot $LDL^\top$, no floating eigensolver.

**Every instance satisfies the sharp candidate and Brascamp--Lieb.** The threshold for exact
escalation was not met. Realised extremes:

| instance | $\lambda_{\max}(\mathcal D,\mathcal N)$ | $\rho^*(0)$ | $\rho^*(1)$ | gate-zero $\lambda_{\max}(\mathsf N_w)$ |
|---|---|---|---|---|
| $\mathrm{Dir}(5,5,5)$ | 0.0745 | 0.9255 | 1.8630 | 1.0667 |
| $\mathrm{Dir}(1,\dots,1)$, $m=8$ | 0.4625 | 0.5375 | 1.1486 | 1.6364 |
| $\mathrm{Dir}(1,1,100)$ | 0.4881 | 0.5119 | 1.0240 | 1.9527 |
| $\mathrm{Dir}(1,1,10000)$ | 0.49988 | 0.50012 | 1.00025 | 1.99950 |

$\min\rho^*(0)=0.50012$ over the Dirichlet family and $0.5$ over the line, both far above the
$0.3$ support threshold; $\min\rho^*(1)=1.0002$, far above the $0.05$ against-threshold. So the
run is **directional support** for (AB) on its pre-registered reading, and gives no directional
evidence against it.

The structure behind the numbers is the useful part. $\mathrm{Dir}(1,\ldots,1,K)\to$ the product
of centred one-sided exponentials as $K\to\infty$, and along that family
$\lambda_{\max}(\mathcal D,\mathcal N)\uparrow1/2$ and $\lambda_{\max}(\mathsf N_w)\uparrow2$ in
lockstep (the identity $\rho^*(0)=1-\lambda_{\max}(\mathcal D,\mathcal N)$ is checked in the
oracle suite). **The saturator of the sharp candidate is exactly the saturator of
$\mathrm{CMH}(4)$: products of log-affine one-dimensional laws.** No Dirichlet instance reaches
$\lambda_{\max}(\mathsf N_w)>2$, which by the probe's own Loewner argument
($\mathsf R\succeq\mathsf N/2$ together with $\mathsf N-I\preceq\mathsf D$ forces
$\mathsf N\preceq2I$) is a second, independent route to the same non-refutation.

### 3.3 The one genuinely new directional finding: the $Q$-reservoir alone is not enough

On the 2-D geometries the two differentiated Monge--Ampère reservoirs are reported separately,
$\mathsf R=\mathsf R_A+\mathsf R_Q$ with $\mathsf R_X=\tfrac12\int\{H,X\}$. Then
$\mathsf R_A\succeq0$ *is* target log-concavity, and $\mathsf R_Q\succeq\mathsf D$ is the
anisotropic form of the Chen--Klartag cyclic square whose trace version
$\operatorname{Tr}\mathsf R_Q\ge\operatorname{Tr}\mathsf D$ is what makes the scalar bootstrap
work.

The run reproduces the certified trace inequality on every instance, and finds the Loewner form
**false** on admissible instances. Worst case:

```
instance   gauss-gauss + y-bump(c=2.5,w=1.2) x He2*exp(-t^2/4) @ eps = -0.1
lambda_min(R_Q - D)/||D||   = -1.2296e-2
Tr(R_Q - D)/Tr(D)           = +3.818e-3        (certified scalar fact, reproduced)
lambda_min(R_A)             = +0.9795          (target log-concavity, comfortable)
log-concavity bulk margin   = +0.1292          (pointwise, well-conditioned nodes)
worst moment-map residual   =  2.07e-9         (abort threshold 1e-6)
lambda_max(D, N)            =  0.01206         (the sharp candidate itself holds with huge slack)
```

The effect is seven orders of magnitude above the residual and survives on four further
`gauss-gauss` couplings. This is a genuinely log-concave, genuinely non-product, two-dimensional
moment map on which $\mathsf R_Q\succeq\mathsf D$ fails.

**Interpretation for the prover.** The probe fenced off the *pointwise* Loewner promotion of the
cyclic third-tensor square with the two-dimensional jet (13), and explicitly left open its
integrated form. This run is directional evidence that the *integrated* matrix form is false too.
Consequently any proof of $\mathsf R\succeq\mathsf N/2$, or of
$({\rm AB})_{\rho,\beta}$ with $\rho$ close to $1/2$, must genuinely spend $\mathsf R_A\succeq0$,
i.e. log-concavity of the target. It cannot run on the Monge--Ampère third-tensor algebra alone.
That is consistent with, and sharpens, the one-dimensional identity of §3.1, where the entire
margin is the $A$-reservoir.

This is directional, not exact. It is the item most worth turning into an analytic statement.

### 3.4 M9: the saturator sits on the boundary of the log-concave class

Calibration first, because it decides how much the channel can see.

* Degree-one Galerkin at $\varepsilon=0$ equals $\lambda_{\max}(\mathbb EH^2)=2$ exactly.
* On the Gaussian product, where $C_{\mathrm{CMH}}=1$ is **attained**, the Galerkin value is
  exactly $1$ at every degree. This is the only absolute anchor in the channel and it calibrates
  numerator, denominator and generator drift simultaneously.
* The pure-Laguerre ladder at the saturator is
  $q_k=2\bigl(1+\cos\frac{\pi}{k+1}\bigr)$ to $10^{-7}$: $2,\,3,\,3.4142,\,3.6180,\dots\to4$.
  That closed form is the quantitative statement that the exponential endpoint is a
  *continuous-spectrum edge*, not an eigenvalue — the certified obstruction from
  `2026-08-27-proof-miner-cmh-transverse-deficit-w3t01.md`, visible as a convergence rate.
* With the near-extremal enrichment $e^{au}$, $a\in\{0.3,0.4,0.45,0.475\}$, degree 6:
  $q(0)=3.99615$, so the probe's resolution floor is $\mathbf{0.0038}$ below $4$. A true second
  variation smaller than that is invisible to this channel.

Dictionary: 3 longitudinal $u$-bumps $\times$ 4 transverse $He_j e^{-t^2/4}$, $j=0..3$, at
$\varepsilon\in\{0,\pm0.02,\pm0.05,\pm0.1\}$, at three Gamma shapes $a\in\{1,1.5,3\}$ (36 rows).

**Result: no refutation candidate. `m9_max_admissible_q` $=q(0)=3.99615$** — no admissible
perturbation in the dictionary raises the quotient at all, and the nine admissible two-sided
pairs all have strictly negative second differences ($-0.68$ to $-5.58$).

The reason is structural and is the real content of the channel. At $a=1$ the target potential is
affine on its support, so $D^2V$ has a zero eigenvalue and $\mathsf R_A$ has a zero direction.
A moment-potential perturbation moves that eigenvalue at first order, so **for at least one sign
of $\varepsilon$, and here for both, the perturbed target leaves the log-concave class.** The
run records this instance by instance: 219 of the 342 two-dimensional instances have
`target_log_concavity = "violated"`.

A near-miss worth recording, because it is exactly the trap this channel exists to avoid. The
coupling `u-bump(c=2.5,w=1.2) x He0*exp(-t^2/4)` at $a=1$ gives

```
q(0) = 3.99615   q(+0.02) = 4.01883   q(+0.05) = 4.05212   q(+0.10) = 4.10556
refinements at +0.05:  degree 8 -> 4.05233 ;  grid (260,60) -> 4.0521174
```

stable under both refinements, and its *averaged* log-concavity test
$\lambda_{\min}\bigl(\int A\,d\eta\bigr)=+0.0057$ is **positive**. Under that test alone it met
the pre-registered refutation criterion and was emitted as a candidate. It is not one: the
*pointwise* test on well-conditioned nodes gives $\lambda_{\min}(A)/\text{scale}=-0.673$ there,
against $-5.7\times10^{-15}$ at $\varepsilon=0$ where the truth is exactly zero. The target is
definitively not log-concave. Both tests are one-sided necessary conditions; the run now applies
both, and reports both, and the candidate does not survive.

**Consequence for `q:cmh-solenoidal-perturbation`.** The M9 design as specified — perturb the
moment potential and take a two-sided second difference — is not available at the saturator,
because the admissible cone there is one-sided at best and the tried dictionary is on the wrong
side of it. An admissible M9 needs a *target-side* perturbation $V_\varepsilon=V_0+\varepsilon c$
with $c$ convex, which is the Monge--Ampère inverse problem that channel (c) deliberately
avoided. That is the honest circular obstruction and it should be recorded as such rather than
worked around.

## 4. Dead ends and things that did not work

* **Newton Monge--Ampère was not attempted.** Replaced as described. This is a real reduction of
  scope, not a neutral reformulation.
* **Uniform-factor perturbations.** Every coupling tried on the uniform moment potential
  $2\log\cosh(\sqrt3y/2)$ fails the strict-convexity gate: its Hessian vanishes at both ends of
  the interval. The `uniform` factor is used only unperturbed.
* **$s$-space bumps on an exponential factor.** $\psi_{ss}=e^s\to0$ as $s\to-\infty$ while an
  ordinary Gaussian bump has $a''(s)=O(1)$ there, so convexity dies for every $\varepsilon\ne0$.
  Only bumps in $u=e^s$ (where $a''(s)=O(u)$, the same order as the unperturbed Hessian) survive.
  63 of 342 instances still abort on convexity or residual.
* **An exponential-shear family** $\psi=e^s(1+\varepsilon b(t))-s+t^2/2$ was considered and
  rejected on paper: its determinant behaves like $e^{2s}\varepsilon[(1+\varepsilon b)b''-
  \varepsilon(b')^2]$, so convexity at large $s$ needs $b$ convex and bounded, hence affine,
  hence $b''=0$ and the determinant negative.
* **The first averaged log-concavity test was too weak** and produced a false refutation
  candidate (§3.4). Recorded because it is the failure mode a reader should expect from any
  averaged admissibility check on a class with a boundary.
* **Pointwise $D^2V$ is not computable near a degenerate Hessian.** Forming
  $D^2V=H^{-1}AH^{-1}$ amplifies roundoff by $\|H^{-1}\|^2$; on the uniform simplex that gave a
  spurious $-0.044$ where the truth is $0$. The battery assembles $A=D^2F-\Gamma$ directly and
  restricts the pointwise sign test to nodes with $\operatorname{cond}(H)<10^6$. The fix is
  validated against the closed-form Dirichlet $D^2V$ to $5.4\times10^{-12}$ relative.

## 5. Proposed adversarial instances

For the `synthesizer` only; not added to the registry here (`CLAUDE.md` constraint 3).

1. **`stress-cmh-ab-exponential-limit`** — $\mathrm{Dir}(1,1,K)$, $K\in\{10^3,10^4\}$.
   *Why the battery does not cover it:* `cmh-gate-zero` sweeps $\mathrm{Dir}(1,1,1000)$ for the
   gate-zero ratio, but nothing in the shared battery records that this family converges to the
   product of centred one-sided exponentials and therefore *simultaneously* saturates
   $\mathsf R\succeq\mathsf N/2$ and $\lambda_{\max}(\mathsf N)\le2$. It is the only exactly
   computable approach to the (AB) equality case.
2. **`stress-cmh-ab-reservoir-split`** — the perturbed Gaussian product
   `gauss-gauss + y-bump(2.5,1.2) x He2 e^{-t^2/4}` at $\varepsilon=\pm0.1$.
   *Why the battery does not cover it:* every existing CMH instance is a product, a Dirichlet law
   or an algebraic countermodel. This is the first admissible non-product moment map in the
   repository on which the integrated matrix cyclic square $\mathsf R_Q\succeq\mathsf D$ fails
   while its certified trace version holds. It separates the two reservoirs, which no registered
   instance does.
3. **`fence-cmh-m9-boundary`** — `exp-gauss + u-bump(2.5,1.2) x He0 e^{-t^2/4}` at
   $\varepsilon=+0.05$.
   *Why the battery does not cover it:* it is the explicit witness that a moment-potential
   perturbation of the $\mathrm{CMH}(4)$ saturator raises the Galerkin quotient to $4.052$ *and*
   leaves the log-concave class. Any future M9 attempt will rediscover it; it should be a fence,
   like `fence-cmh-algebraic-countermodel`.

## 6. Verdict

* **Exact channels:** consistent with $({\rm AB})_{1/2,0}$. No exact contradiction; nothing to
  escalate to a refutation dossier.
* **Directional (AB) reading:** support, on the pre-registered thresholds
  ($\min\rho^*(0)=0.500$ exact, $0.740$ on the admissible 2-D instances; $\min\rho^*(1)=1.000$).
* **Directional against a sub-statement:** the integrated matrix inequality
  $\mathsf R_Q\succeq\mathsf D$ is refuted directionally on an admissible instance, while its
  certified trace version is reproduced. This is the one result worth handing to a prover.
* **M9:** no refutation candidate for $\mathrm{CMH}(4)$; the probe is blocked at the saturator by
  the log-concave boundary rather than by numerics, and the resolution floor is $0.0038$.

Nothing here changes `conj:gate-zero`, `ass:cmh-recovery-envelope`, `thm:cmh-dirichlet`,
`q:cmh-solenoidal-perturbation`, `prog:cmh-route` or `conj:kls`.

## 7. Proposed deltas

Harness-level only; a decision record draft is included because a new target and a new registry
entry are a repository-organization change.

```text
research/decisions/2026-08-30-finum-cmh-ab-target.md  (draft, for the orchestrator)

  Decision: add the finum target `cmh-ab` next to `cmh-gate-zero`.
  Rationale: the CMH linear-recovery probe reduced its gate to one matrix inequality
    (AB): R >= rho N - beta I. That inequality is computable exactly on the two exactly
    solvable moment-map families and directionally on analytic source potentials, and the
    two Monge-Ampere reservoirs R_A, R_Q can be separated, which the existing gate-zero
    battery cannot do. M9 shares the same source-potential engine.
  Scope: `experiments/finum/targets/kls/cmh_ab/**` and `experiments/tests/test_18_cmh_ab.py`;
    `cmh_gate_zero` is imported read-only and unmodified.
  Validation: `uv run python -m finum check` green on every target; `uv run pytest -m
    "not slow"` green (34 new oracle tests). Four independent cross-checks pin the index
    placement of D; the Gaussian-product Galerkin anchor is exact and attained.
  Boundary: exact Loewner verdicts are refutation candidates; all quadrature is directional;
    no ledger, manuscript, routes, gating, bibliography or review file is touched.

experiments/README.md  (one row, orchestrator to apply)
  | `cmh-ab` | CMH anisotropic-bootstrap (N, D, R) and M9 probe | `standard`, `exact-only`, `fast` |
```

No mathematical delta is proposed. The candidate lemma worth stating analytically is in the
`next_prompt` of the handoff envelope below, and it belongs to a `prover`, not here.
