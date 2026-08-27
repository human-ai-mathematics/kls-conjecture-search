# KLS route probe: uniform CMH on the certified approximants

Date: 2026-08-27

Role: `kls-route-prober`

Concurrency key: `kls-gate:ass:uniform-cmh-approximants`

Target: `ass:uniform-cmh-approximants`

This probe starts from the now-certified conditional node `q:cmh-approximation`. It does not
repeat its constant-preserving $W_2$ passage, does not assert continuity of
$C_{\mathrm{CMH}}$, and does not replace the exact centered
Gaussian-convolution/Gaussian-tilt/growing-ball family by a more convenient family.

## Gate, verbatim

> Prove a universal $C$ such that the centered Gaussian-convolution, Gaussian-tilt, and
> growing-ball regular moment-map approximants of every centered log-concave law satisfy
> $\sup_k C_{\mathrm{CMH}}(\mu_k)\le C$. The certified conditional node
> `q:cmh-approximation` then passes the affine Poincaré inequalities to the limit with no loss,
> including proper affine-support degeneration; it asserts no continuity of
> $C_{\mathrm{CMH}}$.

The ledger statement is the same: there must be one finite constant independent of the original
law, its ambient dimension, and the approximation index. The gate does not fix that constant to
$4$. Products of centered one-sided exponentials show that any such constant must be at least
$4$, while a counterexample to $\mathrm{CMH}(4)$ alone would not refute the existence of a
larger universal constant.

## Exact family and certified inputs

For $X\sim\mu$ and $G\sim N(0,I_n)$ independent, the certified dossier first forms
$\lambda_\delta=\mathcal L(X+\sqrt\delta G)$ with density $q_\delta$, then

$$
 d\widetilde\mu_{\delta,\varepsilon,R}(x)
 =Z_{\delta,\varepsilon,R}^{-1}
   \mathbf 1_{B(0,R)}(x)q_\delta(x)e^{-\varepsilon|x|^2/2}\,dx,
$$

and finally translates by its mean. It takes $\delta_k=k^{-4}$ and chooses
$0<\varepsilon_k<k^{-1}$ and $R_k>k$ so that the centered law $\mu_k$ satisfies

$$
 W_2(\mu_k,\mu)<\frac2k+\frac{\sqrt n}{k^2}.
$$

Each $\mu_k$ has covariance $\Sigma_k\succ0$, translated-ball support $P_k$, a smooth positive
interior density, and a canonical target-coordinate Hessian $H_k$. The imported published node
`thm:regular-moment-map-compact-target` gives smoothness, positivity, the global moment-map
diffeomorphism, the Stein identity
$\operatorname{Div}_{\mu_k}H_k=-x$, weak zero boundary flux, and
$\mathbb E_{\mu_k}H_k=\Sigma_k$. The dossier
`solutions/q-cmh-approximation.tex` and its independent review certify the exact closed
ambient-core Stein form and the limit passage. None of those results bounds
$C_{\mathrm{CMH}}(\mu_k)$.

The normalization inputs actually available are:

- `def:cmh`, fixing the closed generator
  $\mathsf A_k=-L_k=-\operatorname{Div}_{\mu_k}(H_k\nabla\,\cdot\,)$ and its domain;
- `prop:cmh-bochner`, the integrated Bochner identity for the genuine canonical Hessian;
- `prop:cmh-hodge`, the exact affine-gradient/solenoidal splitting;
- `thm:cmh-implies-affine-poincare`, used only after a CMH bound has been obtained;
- the exact line, product, and Dirichlet results in
  `solutions/thm-cmh-dirichlet.tex`;
- the imported Chen--Klartag trace estimate and Letwin constant-matrix estimate; and
- `prop:letwin-not-gate-zero`, which certifies the limit of those matrix-algebra inputs.

The target has no ledger `bounded_by` edge.

## Term-by-term decomposition of the demanded estimate

Fix $k$ and initially take $g$ in the certified operator core. Put

$$
 u_k=H_k\nabla g,
 \qquad
 h_k=\mathsf A_k g=-L_kg.
$$

The CMH numerator is the covariance-normalized flux energy

$$
 \mathcal N_k(g)
 =\int_{P_k}\langle H_k\nabla g,\Sigma_k^{-1}H_k\nabla g\rangle\,d\mu_k
 =\|\Sigma_k^{-1/2}u_k\|_2^2.
 \tag{1}
$$

The denominator is the squared closed-generator source

$$
 \mathcal D_k(g)=\|h_k\|_2^2=\int_{P_k}(L_kg)^2\,d\mu_k.
 \tag{2}
$$

The certified Bochner identity decomposes it with constant one as

$$
 \mathcal D_k(g)
 =\underbrace{\int\langle H_k\nabla g,\nabla g\rangle\,d\mu_k}_{\mathcal G_k(g)}
 +\underbrace{\int
   \|H_k^{1/2}D^2gH_k^{1/2}\|_{\mathrm{HS}}^2\,d\mu_k}_{\mathcal Q_k(g)}.
 \tag{3}
$$

Thus the exact analytic estimate demanded by the gate is

$$
 \boxed{
 \mathcal N_k(g)\le C\bigl(\mathcal G_k(g)+\mathcal Q_k(g)\bigr)
 \quad\text{for every }k\text{ and every }g\in\operatorname{Dom}(\mathsf A_k).
 }
 \tag{UCMH}
$$

Every term in this display is load-bearing.

- **Source.** $h_k=-L_kg$ is the only source. Uniform control is the closed second-order Riesz
  transform bound
  $\|\Sigma_k^{-1/2}H_k\nabla\mathsf A_k^{-1}h\|_2\le\sqrt C\|h\|_2$
  on the centered range.
- **First coercive term.** $\mathcal G_k$ is the canonical $H_k$-Dirichlet energy.
- **Second coercive term.** $\mathcal Q_k$ is the full Hessian square. It is the only certified
  positive reservoir sensitive to variation of the direction field $\nabla g$.
- **Derivative-of-$H_k$ errors.** They cancel exactly in `prop:cmh-bochner`, and only because
  $H_{mj}\partial_jH_{k\ell}=\varphi_{mk\ell}$ is totally symmetric for a genuine moment map.
  There is no residual Codazzi term available to discard or spend a second time.
- **Boundary.** The global Stein identity supplies weak zero normal flux on $\partial P_k$.
  The ambient restriction core and Friedrichs closure in
  `solutions/q-cmh-approximation.tex` account for the growing-ball boundary. No unsigned
  boundary contribution remains in (3).
- **Damping.** There is no stochastic-time damping in this stationary gate. The two positive
  terms in (3) are the entire coercive side.
- **Approximation error.** There is no small $k$-error to absorb. The estimate must hold before
  taking the limit, with the same $C$ for every $k$. The certified limit theorem passes only the
  affine Poincaré inequalities and gives no convergence of $H_k$, $L_k$, or their domains.

An estimate proved first on the operator core extends to the closed domain if its right-hand side
is the graph norm: applying it to core differences makes the flux in (1) Cauchy. This is the
closure mechanism already used for the Bochner terms; it is not an additional source of slack.

## Two exact reformulations

### A sufficient pointwise metric criterion

Let

$$
 M_k=\operatorname*{ess\,sup}_{P_k}
 \lambda_{\max}(\Sigma_k^{-1/2}H_k\Sigma_k^{-1/2}).
$$

Since $K_k=\Sigma_k^{-1/2}H_k\Sigma_k^{-1/2}\preceq M_kI$ implies
$K_k^2\preceq M_kK_k$, one has
$H_k\Sigma_k^{-1}H_k\preceq M_kH_k$. Hence (3) gives

$$
 C_{\mathrm{CMH}}(\mu_k)\le M_k.
 \tag{4}
$$

Therefore $\sup_kM_k<\infty$ would close the gate. The live compact-target theorem, however,
is qualitative and supplies no such relative bound. The explicit regularization parameters also
degenerate: $\varepsilon_k\downarrow0$, $R_k\uparrow\infty$, the convolution scale has
$\delta_k^{-1}=k^4$, and in an affine-support collapse
$\lambda_{\min}(\Sigma_k)\downarrow0$. Any estimate whose constant depends on
$\varepsilon_k^{-1}$, $R_k$, $\delta_k^{-1}$, or
$\lambda_{\min}(\Sigma_k)^{-1}$ therefore does not meet the gate.

Pointwise domination is also much stronger than the endpoint mechanism. For the centered
one-sided exponential the canonical one-dimensional kernel is $H(x)=x+1$, which is unbounded,
while `thm:cmh-1d` gives $C_{\mathrm{CMH}}=4$. This observation does **not** prove divergence
of $M_k$ along the certified approximants—such a claim would require precisely the unavailable
continuity of $H_k$—but it rules out treating (4) as an equivalent characterization of the
sharp endpoint.

### Exact Hodge operator content

Let
$\mathsf A_{1,k}=-\operatorname{Div}_{\mu_k}(\Sigma_k\nabla\,\cdot\,)$.
For $h=\mathsf A_kg$, let $\psi=\mathsf A_{1,k}^{-1}h$ and

$$
 w_k(h)=H_k\nabla\mathsf A_k^{-1}h-\Sigma_k\nabla\mathsf A_{1,k}^{-1}h.
$$

On the centered range, `prop:cmh-hodge` gives the orthogonal identity

$$
 \|\Sigma_k^{-1/2}H_k\nabla\mathsf A_k^{-1}h\|_2^2
 =\langle h,\mathsf A_{1,k}^{-1}h\rangle
  +\|\Sigma_k^{-1/2}w_k(h)\|_2^2.
 \tag{5}
$$

Thus (UCMH) is the positive-form estimate

$$
 \mathsf A_{1,k}^{-1}+\mathsf S_k^*\mathsf S_k\preceq CI,
 \qquad
 \mathsf S_kh=\Sigma_k^{-1/2}w_k(h),
 \tag{6}
$$

uniformly in $k$. A uniform bound $C_{\mathrm{aff}}$ on the first term and a uniform bound
$C_{\mathrm{sol}}$ on the second would give $C=C_{\mathrm{aff}}+C_{\mathrm{sol}}$. Conversely,
(6) bounds each positive channel separately. The operator norm of the first term is exactly
$C_P^{\mathrm{aff}}(\mu_k)$, so importing a universal bound for it as an input would import KLS
itself. The Hodge identity is an exact diagnosis, not an upper estimate, and the solenoidal term
cannot be discarded.

## Attack: the first unsupported step is already linear

Because CMH is affine invariant, whiten each individual approximant and write again $H_k$ for
its isotropic canonical Hessian. Then $\mathbb EH_k=I$. Test (UCMH) on
$g(x)=a\cdot x$, $|a|=1$. Here $D^2g=0$, $L_kg=-a\cdot x$, and (3) gives
$\mathcal D_k(g)=1$. Therefore any universal CMH constant must first prove

$$
 \mathbb E H_k^2\preceq CI
 \quad\text{uniformly in }k,n,\mu.
 \tag{7}
$$

The special target $C=4$ is `conj:gate-zero`. The imported inputs stop short of even an
unspecified dimension-free $C$:

- Chen--Klartag gives only
  $\operatorname{Tr}(\mathbb EH_k^2)\le2n$, hence the dimension-dependent consequence
  $\lambda_{\max}(\mathbb EH_k^2)\le2n$.
- Letwin gives, for every constant symmetric $B$,
  $\mathbb E\operatorname{Tr}(BH_kBH_k)\le2\operatorname{Tr}(B^2)$.
  With $P_a=a\otimes a$, the exact static identity is
  $$
  \mathbb E|H_ka|^2
  =\mathbb E(a^\top H_ka)^2
   +\frac12\mathbb E\|[P_a,H_k]\|_{\mathrm{HS}}^2.
  \tag{8}
  $$
  Letwin controls the first term by $2$ and gives no bound on the transverse commutator.
- `prop:letwin-not-gate-zero` constructs PSD matrix laws with $\mathbb EH=I$ satisfying the
  Letwin inequality for every symmetric $B$, but
  $\lambda_{\max}(\mathbb EH^2)\ge1+m/\sqrt{2m-1}\to\infty$. Thus positivity,
  normalization, and the full constant-matrix estimate cannot imply (7) with **any** universal
  constant by matrix algebra.

The countermodel is not a moment-map Hessian and is not evidence that (7) fails for the
approximants. Its certified force is methodological: the missing estimate must consume
differentiated Monge--Ampère/Codazzi structure to control the static commutator in (8).

This is the first step that cannot be justified. Precisely, one needs a universal $C_0$ such that

$$
 \sup_{k,\mu,n}\sup_{|a|=1}
 \mathbb E\|[a\otimes a,H_k]\|_{\mathrm{HS}}^2\le C_0,
 \tag{9}
$$

or a different genuine-moment-map argument proving (7). For the sharp value $C=4$, Letwin's
rank-one term leaves a commutator budget of $4$ in (8). No certified repository result supplies
(9). Since the linear sector fails to close, proceeding to variable $\nabla g$ would hide the
first obstruction rather than advance the gate.

This use of gate zero is only a diagnosis inside the present CMH gate. No equivalence or transfer
to `q:upgrade`, `q:stein-weighted`, or `q:alignment` is asserted, and no parallel trace-cluster
proof is opened.

## What the other CMH components actually imply

### Invariant lift

The construction archive contains a checked coordinate completion of squares at a
Schur-normal $1+2$ point. It does not certify that this tensor is the multiplier produced by the
global operator, and it has no arbitrary-dimensional split reduction. That is exactly the open
node `q:mm-invariant-lift`. Consequently it currently supplies no inequality for
$\mathcal N_k$ or the commutator in (9).

### Square-root commutator and Haar tree

The identities

$$
 Q_M=N^{1/2}K_MN^{1/2},
 \qquad
 e_M=[N^{1/2},K_M]N^{1/2}u,
$$

and the resolvent representation for $[N^{1/2},K_M]$ are formal on a common core. The Bessel
deficit, retained Letwin/Codazzi/Monge--Ampère/corrector remainder, and complete-tree spending
estimate have not been certified. The corresponding node
`q:mm-square-root-commutator` depends on the invariant lift and remains open. A formal identity
without the full Haar sum and domain estimate gives no bound on (UCMH), and the static
countermodel forbids treating its commutator as a lower-order error.

### Solenoidal channel

The certified Hodge identity gives (5), so it proves that the solenoidal channel is nonnegative
and must be paid for. It gives no upper bound on $\mathsf S_k$. In dimension one the channel
vanishes, and for products its interaction is controlled by the exact tensorization theorem;
neither fact applies to arbitrary ball-truncated approximants. The open perturbation node tests
whether the sharp constant $4$ fails, but a positive second variation would not by itself refute
the present gate's existence of some larger finite $C$.

### Exact cases and the three regularization operations

The exact-case results do not propagate through the certified family.

1. **Gaussian convolution.** No theorem states that canonical CMH is monotone under convolution.
   Although a convolution is a linear image of a product, `cor:cmh-linear-images` is deliberately
   only a Poincaré-level statement; under a noninvertible image the transported Stein kernel need
   not be the canonical moment-map kernel.
2. **Gaussian tilt.** The tilt changes the density, canonical moment potential, $H_k$, and
   $L_k$. There is no CMH comparison theorem under this reweighting. Its curvature constant
   tends to zero and therefore cannot be used as a uniform parameter.
3. **Growing-ball truncation.** The compact target supplies regularity and zero flux, not
   coercivity. Ball truncation also destroys product structure in dimension greater than one, so
   `thm:cmh-product` does not even bound the exact canonical approximants of a product input.
4. **Centering and whitening.** Centering is built into the target rather than used as a CMH
   comparison. Each full-dimensional $\mu_k$ may be whitened invertibly with no change of CMH,
   but this produces no estimate. Whitening must be undone before the singular limit, as the
   certified approximation dossier already proves.

Dirichlet laws and their Gamma lifts are exact special geometries; the regular approximants of a
general law are not Dirichlet. Passing a finite gate-zero battery on those proved classes is only
calibration.

## Exact residue

- **Needs new idea — first obstruction, genuine moment-map static commutator.** Prove (7), or
  equivalently a dimension-free replacement for (9), using differential moment-map structure.
  The matrix-algebra route is excluded by `prop:letwin-not-gate-zero`.
- **Fenced (method-level, not a ledger `bounded_by` edge) — constant multipliers alone.**
  Positivity, $\mathbb EH=I$, the Chen--Klartag trace bound, and Letwin's full constant-matrix
  estimate cannot yield a universal operator bound without additional Hessian compatibility.
- **Needs new idea — variable gradient field.** Even (7) controls only constant $\nabla g$.
  One still needs the uniform gradient-field coercivity (UCMH), preserving the correlation
  between $H_k$ and $\nabla g$ and using $\mathcal Q_k$ without discarding it.
- **Technical gap — invariant all-split lift.** Identify the target-flat multiplier generated by
  the global operator, including every coefficient, and reduce all split dimensions to named
  positive squares. Low-dimensional coordinate positivity is insufficient.
- **Technical gap / needs new idea — complete square-root commutator estimate.** Put the
  resolvent identity on one closed core and control the full Haar sum with the Bessel,
  Monge--Ampère, Codazzi, corrector, Hodge, and descendant reservoirs, with no nodewise
  positivity or duplicated slack.
- **Needs new idea — solenoidal operator.** Bound the second positive term in (5) uniformly,
  together with rather than in place of the affine channel. Assuming a universal bound on the
  first term is assuming the KLS conclusion that this route is meant to prove.
- **Technical gap if one pursues stability rather than a direct estimate.** Establish a
  canonical-CMH comparison under each of convolution, Gaussian reweighting, and ball truncation.
  None exists in the live graph, and the Poincaré-level closure cannot substitute for it.

No residue belongs to the already-certified `q:cmh-approximation` limit passage.

## Fence-by-fence evasion check

The ledger assigns no `bounded_by` obstruction to `ass:uniform-cmh-approximants`. The full
obstruction registry was nevertheless checked.

- `obs:two-tail`: no cut slice, localization source, or absolute excess estimate is used.
- `obs:proj-ceiling`: the proposed target (UCMH) is tensor- and test-field-aware. The failed
  constant/rank-one reduction is explicitly stopped rather than promoted to a proof.
- `obs:crude-insufficient`: no covariance occupation integral or logarithmic bootstrap appears.
- `obs:relative-ceiling`: no all-measure relative localization bound is inserted.
- `obs:circularity`: no localized isoperimetric profile or changing competitor family appears.
- `obs:rank-one-refuted`: no fixed product cut or stochastic incident-high witness is used.

The additional CMH guardrails are also respected: no continuity of $C_{\mathrm{CMH}}$ is
asserted; no canonical kernel is pushed through a noninvertible map; the algebraic matrix law is
not called a moment-map counterexample; CMH remains only sufficient for KLS; and no equivalence
with the trace-upgrade cluster is claimed.

## Numerical disposition

No `finum` diagnostic is proposed. The gate asserts existence of some unspecified finite
universal $C$, so no single finite observed quotient has a fixed refuting threshold. A value
above $4$ would refute only the sharp statement $\mathrm{CMH}(4)$, not this gate. Refuting the
gate numerically would first require a specified dimension-indexed analytic family and a fixed
certification rule proving its quotient diverges; no such family was established here.

## Route viability and proposed gate text

The route remains logically viable but has not advanced past its first differential
operator-to-trace obstacle. The certified approximation theorem has cleanly isolated the issue:
regularity, boundary flux, affine-support degeneration, and the limit are no longer gaps; the
entire missing input is a uniform canonical-Hessian/closed-generator estimate on the exact
approximants. Existing invariant-lift, commutator, solenoidal, and gate-zero components diagnose
the terms but do not bound them.

Proposed one-line gate update for the orchestrator:

> On the certified centered Gaussian-convolution/Gaussian-tilt/growing-ball approximants, prove
> uniformly on the closed ambient core
> $\|\Sigma_k^{-1/2}H_k\nabla g\|_2^2\le
> C\{\|H_k^{1/2}\nabla g\|_2^2+
> \|H_k^{1/2}D^2gH_k^{1/2}\|_2^2\}$, including the genuine-moment-map linear-sector bound and
> the solenoidal/complete-commutator remainder; constants depending on
> $\varepsilon_k^{-1}$, $R_k$, $\delta_k^{-1}$, or
> $\lambda_{\min}(\Sigma_k)^{-1}$ do not qualify.

## Proposed ledger delta

None. Equations (UCMH), (5), and the linear-sector necessity are exact consequences of existing
certified nodes, not new claims. No new candidate node or structural relation was established
beyond the live graph.

```yaml
outcome: blocked
artifacts:
  - research/explorations/2026-08-27-kls-route-prober-uniform-cmh-approximants-par-03.md
proposed_deltas:
  - none
next_role: orchestrator
next_prompt: |
  Review the uniform-CMH probe and, if accepting its route-control sharpening, replace the
  `ass:uniform-cmh-approximants` gate sentence by the proposed one-line coercivity statement in
  the report. Do not change the node's open status or infer any CMH continuity. The first
  unsupported step is the dimension-free genuine-moment-map linear-sector/static-commutator
  estimate; Chen--Klartag trace control and Letwin constant multipliers cannot supply any
  universal constant by matrix algebra. Do not dispatch `finum` from this report: the gate has
  no fixed finite refuting threshold. Any comparison with `q:upgrade`, high-rank
  `q:stein-weighted`, or `q:alignment` remains reserved to the trace-cluster synthesizer.
```
