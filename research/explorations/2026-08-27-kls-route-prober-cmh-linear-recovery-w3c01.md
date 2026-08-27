# KLS route probe: linear CMH recovery and the anisotropic Hessian bootstrap

Date: 2026-08-27

Role: `kls-route-prober`

Concurrency key: `kls-gate:ass:cmh-recovery-envelope`

Target: the linear-test quotient inside `ass:cmh-recovery-envelope`

This probe starts after the certification of `prop:cmh-recovery-calculus`. It treats only the
first necessary linear sector of the existential recovery gate. It does not attempt the
variable-gradient CMH inequality, does not discard the Hodge solenoidal channel, and does not
open a parallel comparison with any stochastic trace-upgrade node.

## Gate, verbatim

The live gate is:

> Construct, for every centered log-concave law, at least one regular compact-target moment-map
> recovery sequence with a universal bound on $\liminf C_{\mathrm{CMH}}$. The unconditional affine
> Poincar\'e lower-semicontinuity lemma and the regular CMH endpoint then pass the bound to the
> limit. This is the preferred approximation gate; it does not demand control of every
> regularization choice.

The exact ledger statement is:

> There is a universal $C$ such that every centered log-concave law has at least one regular
> recovery sequence $\mu_k$ with ambient $W_2$ convergence and
> $\liminf_k C_{\mathrm{CMH}}(\mu_k)\le C$; no bound over every regularization choice is
> required.

The first necessary test on any proposed sequence is the following. For a centered,
full-dimensional regular law $\nu$, with covariance $\Sigma\succ0$ and canonical target-coordinate
moment Hessian $H$, set

$$
 Q_{\mathrm{lin}}(\nu)
 :=\sup_{a\ne0}
 \frac{\mathbb E_\nu\langle Ha,\Sigma^{-1}Ha\rangle}
      {a^T\Sigma a}
 =\lambda_{\max}\!\left(
  \Sigma^{-1/2}\mathbb E_\nu[H\Sigma^{-1}H]\Sigma^{-1/2}
 \right).
 \tag{1}
$$

Indeed, for $g_a(x)=a\cdot x$, the weak Stein identity gives
$L_\nu g_a=-a\cdot x$, so the denominator of the CMH quotient is $a^T\Sigma a$ and its numerator
is the numerator of (1). Thus

$$
 1\le Q_{\mathrm{lin}}(\nu)\le C_{\mathrm{CMH}}(\nu).
 \tag{2}
$$

The lower bound is Jensen together with $\mathbb EH=\Sigma$. Consequently the first unresolved
subgate is:

$$
 \boxed{
 \text{For every centered log-concave $\mu$ and every $\varepsilon>0$, find regular $\nu$ with}
 \quad W_2(\nu,\mu)<\varepsilon,
 \quad Q_{\mathrm{lin}}(\nu)\le C_{\mathrm{lin}}.
 }
 \tag{LR}
$$

Here $C_{\mathrm{lin}}$ must be independent of dimension, target, and accuracy. A diagonal
selection turns (LR) into a recovery sequence with bounded limsup. Conversely, a recovery with
bounded liminf has a good subsequence satisfying (LR), up to an arbitrarily small additive error.
Hence (LR) is exactly the linear part of the existential gate, not merely a test of the stronger
canonical approximation family.

Even a proof of (LR) would not discharge `ass:cmh-recovery-envelope`: nonconstant $\nabla g$ and
the solenoidal term of `prop:cmh-hodge` would remain.

## Certified starting point

The following repository facts are now available and were read with their dossiers and passing
reviews.

1. `thm:regular-moment-map-compact-target` gives the smooth canonical potential, positive
   Hessian, global gradient diffeomorphism, Stein identity, zero-flux convention, and
   $\mathbb EH=\Sigma$ for every regular compact-target law.
2. `lem:affine-poincare-w2-liminf` gives regular compact-target recovery in ambient $W_2$ and
   the affine-Poincar\'e liminf passage. It gives no canonical-Hessian convergence.
3. `def:cmh`, `prop:cmh-bochner`, and `prop:cmh-hodge` fix the full operator quotient, its two
   Bochner squares, and the nonnegative solenoidal channel.
4. `thm:cmh-1d`, `thm:cmh-product`, and `thm:cmh-dirichlet` give exact or bounded CMH on the
   line, on products, and on log-concave Dirichlet laws.
5. The newly certified `prop:cmh-recovery-calculus` proves invertible affine invariance,
   singular-square monotonicity of the recovery envelope, finite-product closure, and harmless
   normal collapse. It deliberately proves no rectangular projection theorem.
6. The imported Chen--Klartag estimate controls only
   $\operatorname{Tr}\mathbb E\bar H^2\le2n$ after whitening. The imported Letwin estimate
   controls $\mathbb E\operatorname{Tr}(B\bar H B\bar H)$ for constant symmetric $B$.
   `prop:letwin-not-gate-zero` proves that these matrix-algebra data do not control
   $\lambda_{\max}(\mathbb E\bar H^2)$ by any universal constant without genuine Hessian
   structure.

The target has no ledger `bounded_by` edge. The route guardrails are nevertheless load-bearing:
the finite-stage Hessian must be canonical; no Hessian continuity may be assumed; a rectangular
projection may not inherit its parent kernel; and the full CMH solenoidal channel may not be
dropped after the linear sector.

## Term-by-term decomposition of the linear quotient

Whiten one finite-stage law by an invertible map. Affine covariance of the canonical data leaves
(1) unchanged, so from now on

$$
 \Sigma=I,
 \qquad \mathbb EH=I,
 \qquad Q_{\mathrm{lin}}(\nu)=\lambda_{\max}(\mathbb EH^2).
 \tag{3}
$$

Every part of (3) matters.

- **Canonical column energy.** For a unit vector $a$, the quantity is
  $\mathbb E|Ha|^2$, not the scalar Rayleigh moment
  $\mathbb E(a^THa)^2$.
- **Longitudinal/transverse split.** With $P_a=a\otimes a$,
  $$
   |Ha|^2=(a^THa)^2+rac12\|[P_a,H]\|_{\mathrm{HS}}^2.
   \tag{4}
  $$
  Letwin controls the first term. The second is the static transverse column energy.
- **Source coordinates.** If $d\eta(y)=e^{-\psi(y)}dy$ and
  $(\nabla\psi)_\#\eta=\nu$, then $H=D^2\psi$ and
  $$
   \mathbb E_\nu|H(x)a|^2
   =\int_{\mathbb R^n}|D^2\psi(y)a|^2e^{-\psi(y)}dy.
   \tag{5}
  $$
  Thus (LR) is an $L^2$ column estimate for a genuine Hessian, not a moment bound for an
  arbitrary positive matrix field.
- **Approximation quantifier.** Only one well-chosen regular law at each accuracy is needed. No
  convergence of $H_k$ to a limiting Hessian is required if the estimate is proved directly at
  each finite stage.
- **Boundary.** Compact targets are used through their global source representation and cutoff
  integration by parts. No boundary term can be assigned a favorable sign and omitted.
- **Downstream terms.** For non-linear $g$, the certified Bochner denominator contains both
  $\mathbb E\langle H\nabla g,\nabla g\rangle$ and the full Hessian square. Nothing in the
  present linear calculation pays either the variable-field correlation or the Hodge
  solenoidal operator.

The published directional bound of Klartag,

$$
 \left(\mathbb E|a^THa|^p\right)^{1/p}
 \le4p^2|a|^2,
 \tag{6}
$$

and Letwin's sharper $p=2$ constant-matrix estimate both land on the first term of (4). Summing
polarized scalar estimates over an orthonormal basis costs a factor of order $n$ and does not
bound (5).

## A proof-ready reduction: the anisotropic Chen--Klartag bootstrap

The trace proof can be lifted to a matrix identity up to one exact missing Loewner estimate.
This is the most useful reduction produced by the probe.

Let the isotropic regular target have density proportional to $e^{-V}$ on its compact convex
support. In source coordinates define the symmetric diffusion

$$
 \mathcal Lf=H^{ij}f_{ij}-(V_i\circ\nabla\psi)f_i,
 \qquad (H^{ij})=H^{-1}.
$$

Differentiated Monge--Amp\`ere gives

$$
 \mathcal LH+H=A+Q,
 \qquad
 A=H(D^2V\circ\nabla\psi)H\succeq0,
 \qquad
 Q_{ij}=\operatorname{Tr}(H^{-1}\partial_iH\,H^{-1}\partial_jH)\succeq0.
 \tag{7}
$$

Define the following constant symmetric matrices:

$$
 \begin{aligned}
  \mathsf N&:=\int H^2\,d\eta,\\
  \mathsf D&:=\int H^{ab}(\partial_aH)(\partial_bH)\,d\eta,\\
  \mathsf R&:=\frac12\int\bigl(H(A+Q)+(A+Q)H\bigr)\,d\eta.
 \end{aligned}
 \tag{8}
$$

The matrix $\mathsf D$ is positive semidefinite: for every $v$,

$$
 v^T\mathsf Dv
 =\int H^{ab}\langle(\partial_aH)v,(\partial_bH)v\rangle\,d\eta\ge0.
$$

The anticommutator defining $\mathsf R$ is symmetric, but positivity of $H,A,Q$ does not make it
positive semidefinite.

### Exact identity

The diffusion product rule gives

$$
 \mathcal L(H^2)
 =(\mathcal LH)H+H(\mathcal LH)
   +2H^{ab}(\partial_aH)(\partial_bH).
$$

The standard compact-target cutoff argument gives $\int\mathcal L(H^2)d\eta=0$. Substitution of
(7) therefore yields the exact matrix identity

$$
 \boxed{\mathsf N=\mathsf D+\mathsf R.}
 \tag{9}
$$

### Exact one-sided inequality

Apply the sharp Brascamp--Lieb inequality for $e^{-\psi}$ separately to the components of the
vector field $Ha$. Since $\int Ha\,d\eta=a$,

$$
 \begin{aligned}
  a^T(\mathsf N-I)a
  &=\int|Ha-a|^2d\eta\\
  &\le\int H^{bc}\langle(\partial_bH)a,(\partial_cH)a\rangle d\eta
   =a^T\mathsf Da.
 \end{aligned}
$$

Hence

$$
 \boxed{\mathsf N-I\preceq\mathsf D.}
 \tag{10}
$$

Both (9) and (10) are finite-stage canonical-Hessian statements. They use no limiting Hessian,
no rectangular image, and no unproved CMH estimate.

### The one missing inequality

Suppose there are universal $\rho>0$ and $\beta\ge0$ such that, on one selected regular
recovery sequence,

$$
 \boxed{\mathsf R\succeq\rho\mathsf N-\beta I.}
 \tag{AB}_{\rho,\beta}
$$

Then (9) gives
$\mathsf D\preceq(1-\rho)\mathsf N+\beta I$. Combining with (10),

$$
 \rho\mathsf N\preceq(1+\beta)I,
 \qquad
 Q_{\mathrm{lin}}(\nu)=\lambda_{\max}(\mathsf N)le\frac{1+\beta}{\rho}.
 \tag{11}
$$

Thus (LR) is discharged if, for every target and accuracy, one can choose a regular approximant
satisfying the same $({\rm AB})_{\rho,\beta}$. This is a single exact new inequality. It is
strictly more structural than restating $\mathsf N\preceq CI$: it names the differentiated
Monge--Amp\`ere reservoirs which must retain a fixed fraction of the column energy.

The sharp trace analogue has $\rho=1/2$ and $\beta=0$. Indeed, tracing (9) gives the
Chen--Klartag quantities

$$
 N_2=D_2+A_2+Q_2,
$$

and cyclic symmetry of the full third tensor gives $Q_2\ge D_2$, while $A_2\ge0$. Hence
$\operatorname{Tr}\mathsf R\ge\operatorname{Tr}\mathsf D$, or
$\operatorname{Tr}\mathsf R\ge\tfrac12\operatorname{Tr}\mathsf N$. Tracing (10) then gives
$\operatorname{Tr}\mathsf N\le2n$.

The desired operator statement is precisely the missing anisotropic retention of this scalar
bootstrap. The strongest natural form is

$$
 \mathsf R\succeq\mathsf D,
 \tag{12}
$$

which is equivalent through (9) to
$\mathsf R\succeq\mathsf N/2$ and gives $Q_{\mathrm{lin}}\le2$. A weaker
$({\rm AB})_{\rho,\beta}$ would already give the unspecified finite constant required by the
recovery gate.

### Why the trace proof does not polarize pointwise

The scalar inequality $q_2\ge d_2$ is obtained only after summing and cyclically averaging all
three indices of the symmetric tensor $D^3\psi$. There is no pointwise Loewner version.

For an explicit two-dimensional jet, take

$$
 H=\operatorname{diag}(\lambda,\mu),
 \qquad 0<\lambda<\mu,
$$

and let the only nonzero entries of the symmetric third tensor be the permutations of
$\psi_{112}=t$. With $A=0$, direct substitution into (7)--(8) gives

$$
 Q=\operatorname{diag}\!\left(\frac{2t^2}{\lambda\mu},
                               \frac{t^2}{\lambda^2}\right),
$$

$$
 D_{\rm point}
 =\operatorname{diag}\!\left(
 t^2\left(\frac1\lambda+\frac1\mu\right),
 \frac{t^2}{\lambda}
 \right).
$$

Therefore the first diagonal entry of
$\tfrac12(HQ+QH)-D_{\rm point}$ is

$$
 t^2\left(\frac1\mu-\frac1\lambda\right)<0.
 \tag{13}
$$

This is a local algebraic obstruction to a pointwise proof, not a global moment-map
counterexample. Any valid proof of (12), or of the weaker recovery form
$({\rm AB})_{\rho,\beta}$, must use integration, a corrector, or a nonlocal structural
argument. It cannot promote the cyclic trace square term by term to matrix order.

## Approximation mechanisms tested

### 1. Growing-ball truncation

For a compact target $K$, Klartag's published pointwise estimate gives
$0\preceq H\preceq2R(K)^2I$. After whitening,

$$
 Q_{\mathrm{lin}}\le2R(\Sigma^{-1/2}K)^2.
 \tag{14}
$$

This proves finiteness for a fixed compact target, but the whitened radius of the certified
growing-ball sequence is uncontrolled and its support radius tends to infinity. Equation (14)
therefore gives no universal recovery constant.

Published common-compact-support stability of moment potentials gives local uniform convergence
of normalized source potentials and gradient convergence at common differentiability points.
It gives no $D^2\psi_k$ convergence or uniform integrability of (5). Growing supports are even
outside its common-compact hypothesis.

This derivative gap is real at the level of convex compactness. For example,

$$
 f_k(x)=\frac{x^2}{2}+\epsilon_k\sqrt{x^2+\delta_k^2},
 \qquad \delta_k=\epsilon_k^3\downarrow0,
$$

converges locally uniformly to $x^2/2$, and its gradients converge away from the origin, while
the squared $L^2$ mass of the additional Hessian is of order
$\epsilon_k^2/\delta_k=\epsilon_k^{-1}$. This is not asserted to be a sequence of canonical
moment potentials of admissible targets; it shows exactly why potential/gradient compactness
alone cannot justify the quadratic-Hessian passage.

**Verdict:** regularity mechanism only. A proof must establish (LR) or
$({\rm AB})_{\rho,\beta}$ before the support expands; potential convergence cannot replace it.

### 2. Gaussian smoothing

The certified family begins with $\mu*\gamma_\delta$. As a measure this is the rectangular
linear image of the product $\mu\otimes\gamma_\delta$ under $(x,z)\mapsto x+z$. Product CMH and
product $Q_{\mathrm{lin}}$ do not descend to the canonical Hessian of that image. Conditioning
an inherited Stein kernel produces a valid Stein kernel of the convolution, but not the
canonical moment-map kernel demanded by (1).

Padding the sum map does not evade the obstruction. The square singular map

$$
 (x,z)\longmapsto(x+z,0)
$$

can control an ambient recovery of the embedded convolution in $\mathbb R^{2n}$. Returning to
the intrinsic $n$-dimensional convolution would require reversing the certified affine-support
extension inequality, which is exactly the unavailable rectangular projection theorem.

Moment-measure-specific stability improves ordinary fixed-source transport stability, but the
verified literature still stops at source Gibbs densities, potentials, or almost-everywhere
gradients. It supplies no Hessian convergence and no semicontinuity of $Q_{\mathrm{lin}}$.

**Verdict:** no canonical comparison. Gaussian smoothing can be retained as a regularity step
only if the finite-stage anisotropic estimate is proved independently.

### 3. Gaussian tilt

Fathi's published contraction theorem gives a genuine positive result on the relatively
strongly log-concave subclass. If

$$
 D^2V\succeq\varepsilon\Sigma^{-1},
$$

then the whitened canonical Hessian satisfies
$0\preceq\bar H\preceq\varepsilon^{-1}I$, and hence

$$
 Q_{\mathrm{lin}}\le\varepsilon^{-1}.
 \tag{15}
$$

For the certified approximation, the absolute tilt is
$D^2V_k\succeq\varepsilon_k I$. Relative to covariance this yields at best

$$
 Q_{\mathrm{lin}}(\mu_k)
 \le\bigl(\varepsilon_k\lambda_{\min}(\Sigma_k)\bigr)^{-1}.
 \tag{16}
$$

The tilt must be removed, so $\varepsilon_k\downarrow0$; under affine-support degeneration the
smallest covariance eigenvalue also tends to zero. Thus (16) diverges even before the
growing-ball parameter is considered. Whitening does not change this relative curvature
parameter.

**Verdict:** proves (LR) on a fixed relatively strongly log-concave subclass, but degenerates
along recovery of a general law.

### 4. Products, invertible maps, and affine collapse

At the linear level the exact calculus is especially transparent. For regular factors,
$Q_{\mathrm{lin}}$ of a product is the maximum of the factor quotients because $H$, $\Sigma$,
and $\mathbb E[H\Sigma^{-1}H]$ are block diagonal. Invertible maps preserve the quotient because
linear tests pull back bijectively. Defining

$$
 \mathfrak R_{\mathrm{lin},n}(\mu)
 :=\inf_{(\mu_k)\in\operatorname{Rec}_n(\mu)}
   \liminf_kQ_{\mathrm{lin}}(\mu_k),
 \tag{17}
$$

the diagonal arguments already certified for `prop:cmh-recovery-calculus` give:

$$
 \begin{aligned}
  \mathfrak R_{\mathrm{lin},n}(T_\#\mu)
   &=\mathfrak R_{\mathrm{lin},n}(\mu) &&(T\text{ invertible}),\\
  \mathfrak R_{\mathrm{lin},n}(T_\#\mu)
   &\le\mathfrak R_{\mathrm{lin},n}(\mu) &&(T\text{ square, possibly singular}),\\
  \mathfrak R_{\mathrm{lin}}(\mu_1\otimes\cdots\otimes\mu_m)
   &\le\max_i\mathfrak R_{\mathrm{lin}}(\mu_i),\\
  \mathfrak R_{\mathrm{lin},n}(\iota_\#\mu)
   &\le\max\{\mathfrak R_{\mathrm{lin},d}(\mu),1\}
     &&(\iota:\mathbb R^d\hookrightarrow\mathbb R^n).
 \end{aligned}
 \tag{18}
$$

The proofs use invertible maps at every finite stage, simultaneous good-member selection for
finite products, and vanishing truncated-Gaussian normal factors. No Hessian limit is used.
Since $Q_{\mathrm{lin}}\le C_{\mathrm{CMH}}$, the certified full recovery calculus already
implies bounded linear recovery for its Gaussian, one-dimensional-product, and
uniform-simplex-generated model classes.

What (18) does not give is density of those classes among all log-concave laws. Ball truncation
destroys product structure, and every dimension-lowering product/simplex lift again meets the
rectangular canonical-kernel barrier.

**Verdict:** exact and proof-ready closure calculus, but no general density theorem.

## Literature boundary

The companion primary-source audit is
`research/explorations/2026-08-27-literature-scout-cmh-hessian-recovery-w3l01.md`. Its verified
boundary is sharp for this probe.

- Klartag's published compact-support stability reaches normalized potentials, local uniform
  convergence, and gradients at differentiability points, but not Hessians.
- Klartag's published directional Hessian moments control $a^THa$, not $|Ha|$.
- Fathi's published contraction gives (15), with the degenerating constant in (16).
- Bonnet--Rubinstein and Machado--Ramos prove source-density or source-measure stability in
  unreviewed 2026 preprints, but neither controls $D^2\psi$ or (1). Machado--Ramos also show that
  a source-$W_2$ stability constant degenerates through affine-support collapse.
- Delalande--Farinelli's regularized moment measure changes the source log-density without
  changing the pushforward map accordingly, so its stable Hessian is not the canonical Hessian
  in (1).

No reviewed source found by that audit proves canonical-Hessian convergence,
$Q_{\mathrm{lin}}$ semicontinuity, a rectangular projection comparison, or universal linear
recovery.

## What is established

The following statements are ready for a prover to formalize.

1. **Linear recovery calculus.** Definition (17) has the floor one and all four closure
   properties in (18). This is a strict linear-sector analogue of the already certified full
   recovery calculus.
2. **Anisotropic bootstrap reduction.** For every isotropic regular compact-target moment map,
   the matrices in (8) satisfy (9)--(10). Any universal
   $({\rm AB})_{\rho,\beta}$ on one recovery sequence gives the explicit bound (11).
3. **Pointwise method obstruction.** The two-dimensional jet (13) refutes a pointwise Loewner
   promotion of the cyclic third-tensor inequality. This does not refute its integrated or
   recovery-selected form.

No general bound or counterexample to (LR) is established.

## Exact residue

- **Needs new idea — anisotropic source retention.** Prove
  $({\rm AB})_{\rho,\beta}$ with universal $\rho>0$, $\beta<\infty$ on at least one regular
  compact-target recovery of every centered log-concave target. The natural sharp candidate is
  the integrated inequality $\mathsf R\succeq\mathsf D$.
- **Fenced — pointwise cyclic-square promotion.** Equation (13) shows that the scalar
  $q_2-d_2$ sum of squares does not have the required pointwise matrix sign. Any proof must use
  an integrated corrector, nonlocal coercivity, or a different genuine-Hessian mechanism.
- **Technical gap with no current theorem — Hessian compactness.** Potential, source-density,
  source-measure, and almost-everywhere gradient stability do not control the quadratic Hessian
  energy. A stability-based proof needs a new uniform-integrability or Hessian-semicontinuity
  theorem at exactly the norm in (5).
- **Fenced — rectangular descent.** Product and simplex lifts may be projected only after a
  canonical comparison theorem is proved. Padding a rectangular map by zero normal coordinates
  does not reverse the direction of affine-support extension.
- **Needs new idea — genuine class density.** Absent rectangular descent, prove that the
  product/affine/singular-square closure of bounded-linear-recovery blocks is intrinsically
  $W_2$-dense in all log-concave laws, or identify a larger tensor-stable exact class.
- **Downstream and deliberately not attacked.** After (LR), upgrade linear columns to variable
  $\nabla g$ while retaining the Bochner Hessian square and the Hodge solenoidal channel. The
  present report supplies no implication to that second gate.

## Fence-by-fence evasion check

The ledger gives `ass:cmh-recovery-envelope` no `bounded_by` edge. The full obstruction registry
was nevertheless checked.

- `obs:two-tail`: no cut, boundary slice, excess, or covariance-weighted localization estimate
  is used.
- `obs:proj-ceiling`: the live quantity is the full column energy $|Ha|^2$. Scalar projection
  bounds are explicitly stopped at (4) and (6).
- `obs:crude-insufficient`: no stochastic covariance integral or logarithmic bootstrap occurs.
- `obs:relative-ceiling`: no all-measure relative localization bound is inserted.
- `obs:circularity`: no localized isoperimetric profile or evolving competitor family occurs.
- `obs:rank-one-refuted`: products are used only through exact stationary tensorization, not
  through a fixed product cut.

The CMH-specific fences are also respected.

- No canonical kernel is transported through a noninvertible or rectangular map.
- No continuity, lower semicontinuity, or upper semicontinuity of $Q_{\mathrm{lin}}$ or
  $C_{\mathrm{CMH}}$ is asserted.
- The algebraic PSD matrix countermodel and the local jet (13) are method obstructions, not
  genuine moment-map counterexamples.
- The solenoidal channel is retained as a downstream obligation.
- The analysis of $\mathbb EH^2$ is confined to the linear recovery gate. No equivalence or
  implication is asserted with `q:upgrade`, high-rank `q:stein-weighted`, or `q:alignment`.

## Numerical disposition

No `finum` run is proposed. The gate asks for some unspecified finite universal constant. A
finite quotient above $4$ would refute only the sharp CMH(4) endpoint, not universal bounded
linear recovery. No analytic dimension-indexed genuine moment-map family with a proved divergent
threshold was found.

## Route viability and proposed gate update

The linear recovery gate remains viable and unrefuted. The certified recovery calculus closes
all tensor-generated model classes and removes affine-support collapse from the hard part, but
the general law is blocked before any variable-field analysis. The sharpest current formulation
is not generic “Hessian continuity”; it is the integrated anisotropic retention of the two
positive differentiated Monge--Amp\`ere sources after their anticommutator with $H$.

Proposed one-line gate update for the orchestrator:

> First discharge the linear recovery subgate. In source coordinates, prove on one regular
> compact-target recovery of every target that the integrated differentiated-Monge--Amp\`ere
> source matrix $\mathsf R=\frac12\int\{H,A+Q\}$ retains
> $\rho\mathsf N-\beta I$, where $\mathsf N=\int H^2$, for universal $\rho>0,\beta<\infty$;
> the exact identities $\mathsf N=\mathsf D+\mathsf R$ and
> $\mathsf N-I\preceq\mathsf D$ then give
> $Q_{\rm lin}\le(1+\beta)/\rho$. The trace cyclic square has no pointwise Loewner upgrade,
> and potential/gradient stability or rectangular inherited kernels do not qualify.

## Proposed ledger delta

Only the following candidate structural lemma is proposed. It carries no certifying status and
does not change the recovery assumption.

```yaml
- id: lem:cmh-linear-bootstrap-reduction
  kind: lemma
  status: open
  route: moment-map-cmh
  file: modules/kls/41-cmh-normalization.tex
  statement: "For an isotropic regular compact-target moment map with source potential psi, H=D2 psi, differentiated-Monge-Ampere sources A and Q, and matrices N=E H^2, D=E[H^{-1}_{ab}(partial_a H)(partial_b H)], R=(1/2)E[H(A+Q)+(A+Q)H], one has N=D+R and N-I <= D in Loewner order. Consequently, any bound R >= rho N-beta I with rho>0 along a regular recovery sequence implies Q_lin <= (1+beta)/rho on that sequence."
  depends_on: [thm:regular-moment-map-compact-target, def:cmh]
```

The notation `H^{-1}_{ab}` in the proposed plain-text statement means the $(a,b)$ entry of
$H^{-1}$, not the inverse of one scalar entry. The manuscript version should use $H^{ab}$ to
avoid ambiguity.

No `proved`, `refuted`, `solution`, `checked_by`, recovery-assumption status, or cross-route edge
is proposed.

```yaml
outcome: blocked
artifacts:
  - research/explorations/2026-08-27-kls-route-prober-cmh-linear-recovery-w3c01.md
proposed_deltas:
  - "Optionally stage open lem:cmh-linear-bootstrap-reduction with the exact matrix definitions and conditional constant (1+beta)/rho; do not change ass:cmh-recovery-envelope."
  - "Sharpen the CMH recovery gate by the proposed anisotropic source-retention sentence; record that the trace cyclic square has no pointwise Loewner promotion."
next_role: prover
next_prompt: |
  Write a standalone dossier for candidate `lem:cmh-linear-bootstrap-reduction`. Work on one
  isotropic regular compact-target moment map in source coordinates. Define the symmetric
  diffusion L, the differentiated Monge--Ampere sources A and Q, and the constant matrices
  N, D, and R exactly as in the probe. Prove by the matrix diffusion product rule and cutoff
  integration that N=D+R. Apply sharp Brascamp--Lieb componentwise to Ha, using EH=I, to prove
  N-I <= D in Loewner order. Deduce that R >= rho N-beta I implies
  Q_lin<= (1+beta)/rho, and record the sharp specialization R>=D => Q_lin<=2. Include the
  explicit two-dimensional H=diag(lambda,mu), psi_112=t jet showing that
  sym(HQ)-D need not be pointwise PSD when lambda<mu; label it only a method obstruction, not
  a global moment-map counterexample. Audit all domains, cutoff integrations, index placement,
  and affine whitening. State explicitly that the lemma is a conditional reduction: it proves
  neither the anisotropic-retention premise, universal linear recovery, the full CMH quotient,
  nor KLS. Do not edit the ledger, manuscript, routes, gating, bibliography, or reviews.
```
