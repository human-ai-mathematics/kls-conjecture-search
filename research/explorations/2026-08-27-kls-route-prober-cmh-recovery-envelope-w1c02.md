---
---
# KLS route probe: the existential CMH recovery envelope

Date: 2026-08-27

Role: `kls-route-prober`

Concurrency key: `kls-gate:ass:cmh-recovery-envelope`

Target: `ass:cmh-recovery-envelope`

This probe treats only the weaker existential recovery gate. It does not try to control the
specific Gaussian-convolution/Gaussian-tilt/growing-ball family of
`ass:uniform-cmh-approximants`, does not assert continuity of $C_{\mathrm{CMH}}$, and does not
transport a canonical moment-map kernel through a noninvertible map.

## Gate, verbatim

The current gate is:

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

The word **one** and the `liminf` are load-bearing. After extracting a subsequence, the gate is
equivalent to asking that for every centered log-concave $\mu$ there are regular compact-target
laws $\nu_j$ with

$$
 W_2(\nu_j,\mu)<j^{-1},
 \qquad
 C_{\mathrm{CMH}}(\nu_j)\le C+j^{-1}.
 \tag{1}
$$

Thus this gate asks for $W_2$-density of a universally bounded-CMH regular class. It is strictly
weaker than controlling every member of the certified canonical family, but it still asks for
a new CMH estimate, not merely an approximation theorem.

## Dependency and certification audit

The following pieces are already certified.

1. `thm:regular-moment-map-compact-target` is a published import. A centered target
   $g\mathbf 1_{\operatorname{int}P}$ with $P$ a convex body and $g$ positive smooth has a smooth
   strictly convex canonical moment potential, a global gradient diffeomorphism, a smooth
   positive canonical Hessian kernel $H$, weak zero flux,
   $\operatorname{Div}_\mu H=-x$, and $\mathbb E_\mu H=\operatorname{Cov}(\mu)$.
2. `lem:affine-poincare-w2-liminf` constructs such regular approximants for every centered
   log-concave law and proves, along every centered log-concave ambient-$W_2$ sequence,
   $$
   C_P^{\mathrm{aff}}(\mu)
   \le \liminf_k C_P^{\mathrm{aff}}(\mu_k),
   \tag{2}
   $$
   including proper affine-support degeneration.
3. `thm:cmh-implies-affine-poincare` proves on each regular member
   $$
   C_P^{\mathrm{aff}}(\mu_k)\le C_{\mathrm{CMH}}(\mu_k).
   \tag{3}
   $$
4. `cor:cmh-recovery-sequence-suffices` combines (2)--(3) with the present assumption and
   proves KLS with the same constant. It is correctly `conditional` because the present node is
   open.
5. `prop:cmh-bochner`, `prop:cmh-hodge`, `thm:cmh-1d`, `thm:cmh-product`, and
   `thm:cmh-dirichlet` give the exact operator decomposition and the model classes used below.

The certification artifacts read for these claims were
`solutions/lem-affine-poincare-w2-liminf.tex` and
`research/reviews/2026-08-27-lem-affine-poincare-w2-liminf-proof-review.md`,
`solutions/q-cmh-approximation.tex` and
`research/reviews/2026-08-27-q-cmh-approximation-proof-review.md`,
`solutions/thm-cmh-normalization.tex` with
`research/reviews/2026-08-25-kls-cmh-normalization-repair-audit.md`, and
`solutions/thm-cmh-dirichlet.tex` with
`research/reviews/2026-08-25-kls-cmh-exact-cases-repair-audit.md`. The
earlier approximation probe, literature harness, uniform-approximant probe, and both prover
explorations were also checked; none supplies the missing bound in (4).

The recovery assumption has no ledger `bounded_by` edge. The CMH route nevertheless has three
explicit guardrails: for centered envelopes the canonical kernel is transported directly only
by invertible linear maps (equivalently, by affine maps followed by recentering); the
Hodge solenoidal channel is nonnegative and cannot be discarded; and constant-matrix moment
estimates do not control the static transverse commutator.

## Term-by-term decomposition of the demanded object

For one regular approximant $\nu$, write

$$
 \Sigma_\nu=\operatorname{Cov}(\nu),
 \qquad
 L_\nu g=\operatorname{Div}_\nu(H_\nu\nabla g),
 \qquad
 \mathsf A_\nu=-L_\nu.
$$

The demanded constant is

$$
 C_{\mathrm{CMH}}(\nu)
 =\sup_{g\in\operatorname{Dom}(\mathsf A_\nu)\setminus\ker\mathsf A_\nu}
 \frac{
  \mathbb E_\nu\langle H_\nu\nabla g,
  \Sigma_\nu^{-1}H_\nu\nabla g\rangle
 }{
  \mathbb E_\nu(L_\nu g)^2
 }.
 \tag{4}
$$

Every part of (4) matters.

- **Canonical metric.** $H_\nu$ is the target-coordinate Hessian of the canonical moment
  potential, not an arbitrary Stein kernel and not a kernel inherited through a projection.
- **Covariance normalization.** $\Sigma_\nu^{-1}$ is an ordinary inverse on each
  full-dimensional approximant. At a singular limit only the covariance Dirichlet form is
  passed; no inverse is taken in a collapsing direction.
- **Flux numerator.** With $u=H_\nu\nabla g$, the numerator is
  $\|\Sigma_\nu^{-1/2}u\|_2^2$.
- **Source.** The denominator is the squared divergence source
  $\|h\|_2^2$ for $h=-\operatorname{Div}_\nu u=-L_\nu g$.
- **Coercive terms.** The certified Bochner identity is
  $$
  \mathbb E_\nu(L_\nu g)^2
  =\mathbb E_\nu\langle H_\nu\nabla g,\nabla g\rangle
   +\mathbb E_\nu
    \|H_\nu^{1/2}D^2gH_\nu^{1/2}\|_{\mathrm{HS}}^2.
  \tag{5}
  $$
  The differentiated-$H$ terms have already cancelled by the genuine moment-map Codazzi
  symmetry. There is no unused remainder to spend again.
- **Solenoidal channel.** Write
  $\mathsf A_{1,\nu}=-\operatorname{Div}_\nu(\Sigma_\nu\nabla\,\cdot\,)$. If
  $-\operatorname{Div}_\nu(\Sigma_\nu\nabla\psi)=h$ and
  $w=u-\Sigma_\nu\nabla\psi$, then
  $$
  \|\Sigma_\nu^{-1/2}u\|_2^2
  =\langle h,\mathsf A_{1,\nu}^{-1}h\rangle
   +\|\Sigma_\nu^{-1/2}w\|_2^2.
  \tag{6}
  $$
  The first channel has operator norm exactly $C_P^{\mathrm{aff}}(\nu)$; the second is
  nonnegative and has no general upper bound.
- **Boundary and domain.** Each compact-target member must carry the global weak Stein identity,
  zero boundary flux, the closed ambient-restriction form, and constant kernel. These points are
  already certified for the recovery construction; they supply no CMH bound.
- **Damping.** There is no time parameter and no Riccati damping in this stationary gate. The
  two terms in (5) are the entire coercive side.
- **Approximation error.** Ambient $W_2$ controls covariances and the affine Poincar\'e limit. It
  gives no convergence of $H_\nu$, $L_\nu$, their domains, or (4). The gate avoids needing such
  convergence by asking for a bounded `liminf` before applying (2)--(3).
- **Quantifiers.** The universal $C$ is independent of the dimension and the target law. The
  recovery sequence, and the good subsequence extracted from its `liminf`, may depend on the
  target; after extraction, that good subsequence is itself relabelled as the recovery sequence
  in (1).

## A useful exact object: the recovery envelope

For a centered log-concave law $\mu$ on $\mathbb R^n$, define

$$
 \mathfrak R_n(\mu)
 =\inf_{(\mu_k)\in\operatorname{Rec}_n(\mu)}
   \liminf_{k\to\infty}C_{\mathrm{CMH}}(\mu_k),
 \tag{7}
$$

where $\operatorname{Rec}_n(\mu)$ is the class of centered, full-dimensional, log-concave,
compact-target regular moment-map sequences converging to $\mu$ in ambient $W_2$. The certified
regular-approximation lemma makes this class nonempty, although it supplies no finite uniform
upper bound on (7).

Equation (1) shows that the present gate is exactly

$$
 \sup_{n\ge1}\ \sup_{\mu\ \mathrm{centered\ log\mbox{-}concave\ on}\ \mathbb R^n}
 \mathfrak R_n(\mu)<\infty.
 \tag{8}
$$

The certified liminf bridge gives the unconditional lower bound

$$
 C_P^{\mathrm{aff}}(\mu)\le\mathfrak R_n(\mu).
 \tag{9}
$$

Thus a universal estimate in (8) is already KLS-hard at the affine Hodge channel. The recovery
envelope may be strictly larger because of the solenoidal term in (6); no equality with
$C_P^{\mathrm{aff}}$ is known.

## Established recovery calculus

The existential formulation does buy something that the stronger canonical-family gate does
not: exact tensor-stable approximants can be chosen for tensor-stable model classes.
Whenever an envelope on the right-hand side below is infinite the asserted upper bound is
vacuous; the diagonal selections are made only in the finite case.

### 1. Universal floor

Every full-dimensional regular law satisfies

$$
 C_{\mathrm{CMH}}(\nu)\ge1.
 \tag{10}
$$

Indeed, for $g(x)=a\cdot x$ the denominator in (4) is $a^\top\Sigma_\nu a$, while Jensen and
$\mathbb E H_\nu=\Sigma_\nu$ give

$$
 \mathbb E\|\Sigma_\nu^{-1/2}H_\nu a\|^2
 \ge
 \|\Sigma_\nu^{-1/2}\mathbb E H_\nu a\|^2
 =a^\top\Sigma_\nu a.
$$

This floor will make collapsing Gaussian normal factors cost exactly one in the limit.

### 2. Invertible linear invariance

If $T:\mathbb R^n\to\mathbb R^n$ is invertible, then

$$
 \mathfrak R_n(T_\#\mu)=\mathfrak R_n(\mu).
 \tag{11}
$$

Push a recovery sequence through $T$. Regular compact targets and ambient $W_2$ convergence are
preserved, and the certified affine covariance
$H_{T_\#\nu}(Tx)=TH_\nu(x)T^\top$ leaves (4) unchanged. Apply the same argument to $T^{-1}$
for the reverse inequality.

There is also a one-way statement for a singular **square** linear image:

$$
 \mathfrak R_n(T_\#\mu)\le\mathfrak R_n(\mu)
 \qquad(T:\mathbb R^n\to\mathbb R^n\text{ linear, possibly singular}).
 \tag{12a}
$$

This does not transport a kernel through $T$. For each $j$, choose a recovery sequence with
`liminf` at most $\mathfrak R_n(\mu)+(2j)^{-1}$ and then a sufficiently far good member
$\nu_j$ with $W_2(\nu_j,\mu)<j^{-1}$ and
$C_{\mathrm{CMH}}(\nu_j)\le\mathfrak R_n(\mu)+j^{-1}$. Choose invertible $T_j\to T$.
Each $(T_j)_\#\nu_j$ has exactly the same CMH constant as $\nu_j$. If
$X_j\sim\nu_j$ and $X\sim\mu$ are coupled in $L^2$, then

$$
 \mathbb E|T_jX_j-TX|^2
 \le2\|T_j\|_{\mathrm{op}}^2\mathbb E|X_j-X|^2
   +2\mathbb E|(T_j-T)X|^2\longrightarrow0.
$$

Only invertible linear covariance is used at finite $j$; no canonical kernel is asserted to
converge under the singular limiting map.

This argument is dimension-preserving. A genuinely rectangular projection from a
higher-dimensional exact product or simplex lift to a lower-dimensional target remains outside
it: the projected finite-$j$ kernels are not canonical, and an ambient recovery in the larger
space does not by itself produce a regular recovery in the smaller declared ambient space.

### 3. Product upper bound

For finitely many centered log-concave factors,

$$
 \mathfrak R_{n_1+\cdots+n_m}
   \left(\bigotimes_{i=1}^m\mu_i\right)
 \le\max_i\mathfrak R_{n_i}(\mu_i).
 \tag{12}
$$

For each factor and each $j$, first choose a recovery sequence whose `liminf` is below
$\mathfrak R_{n_i}(\mu_i)+(2j)^{-1}$, then select a sufficiently far good member whose $W_2$
error is below $j^{-1}$ and whose CMH constant is below
$\mathfrak R_{n_i}(\mu_i)+j^{-1}$. This simultaneous diagonal selection is legitimate because
only finitely many factors occur and the definition uses a `liminf`. Products of compact regular
moment maps are compact regular moment maps: their source potentials add, their canonical
Hessians and covariances are block diagonal, and their target bodies multiply. Product
couplings give

$$
 W_2^2\!\left(\bigotimes_i\nu_{i,j},\bigotimes_i\mu_i\right)
 \le\sum_iW_2^2(\nu_{i,j},\mu_i),
$$

while the certified product formula gives
$C_{\mathrm{CMH}}(\bigotimes_i\nu_{i,j})=\max_iC_{\mathrm{CMH}}(\nu_{i,j})$.

### 4. Affine-support collapse costs only the floor one

Let $S\subset\mathbb R^n$ be a linear subspace of dimension $d$, and regard a centered law
$\mu$ on $S$ as an ambient law via the inclusion $\iota:S\hookrightarrow\mathbb R^n$. Then

$$
 \mathfrak R_n(\iota_\#\mu)
 \le\max\{\mathfrak R_d(\mu),1\}.
 \tag{13}
$$

To prove it, for each $j$ choose an intrinsic recovery sequence within $(2j)^{-1}$ of the
envelope and extract a good member $\nu_j$ with $W_2$ error below $j^{-1}$ and CMH constant
below $\mathfrak R_d(\mu)+j^{-1}$. Let $\zeta_R$ be the standard Gaussian conditioned to
$[-R,R]$. It is centered,
log-concave, and a positive-smooth compact-target regular law. The one-dimensional identity and
the Neumann Bakry--\'Emery/Brascamp--Lieb inequality on the convex interval give

$$
 1\le C_{\mathrm{CMH}}(\zeta_R)
 =\frac{C_P(\zeta_R)}{\operatorname{Var}(\zeta_R)}
 \le\frac1{\operatorname{Var}(\zeta_R)}
 \longrightarrow1.
 \tag{14}
$$

For a dossier, the interval inequality can be obtained by smooth convex barriers outside
$[-R,R]$ followed by monotone form convergence; this avoids silently applying a full-space
Brascamp--Lieb statement across the hard boundary.

Choose $R_j\to\infty$ and $\varepsilon_j\downarrow0$, and on the orthogonal splitting
$\mathbb R^n=S\oplus S^\perp$ set

$$
 \widehat\nu_j
 =\nu_j\otimes
   \bigl((x\mapsto\varepsilon_jx)_\#\zeta_{R_j}\bigr)^{\otimes(n-d)}.
 \tag{15}
$$

Every $\widehat\nu_j$ is centered, full-dimensional, compact-target regular. Orthogonal product
couplings give

$$
 W_2^2(\widehat\nu_j,\iota_\#\mu)
 \le W_2^2(\nu_j,\mu)
   +(n-d)\varepsilon_j^2\operatorname{Var}(\zeta_{R_j})\longrightarrow0.
$$

Scaling does not change CMH, and the product theorem plus (14) yields (13). Hence singular
covariance is not the hard part of the existential gate: once the intrinsic sequence is found,
compact Gaussian normal factors restore full dimension without increasing any constant
$C\ge1$. Equivalently, one may tensor with Gaussian normal factors and then use (12a) to
collapse the normal directions through invertible maps approaching the singular projection.
For every nontrivial intrinsic law, (9) and the linear test give
$\mathfrak R_d(\mu)\ge C_P^{\mathrm{aff}}(\mu)\ge1$, so (13) is simply
$\mathfrak R_n(\iota_\#\mu)\le\mathfrak R_d(\mu)$. The point mass has ambient envelope $1$.

## Exact analytic calibrations

### Gaussian laws

For the standard Gaussian on $\mathbb R^n$, use
$\zeta_R^{\otimes n}$. Product $W_2$ convergence gives the Gaussian limit, while (14) and the
product formula give $C_{\mathrm{CMH}}\to1$. Invertible linear invariance handles every
nondegenerate centered Gaussian, and (13) handles singular Gaussians. The lower bound (10)
applies to every full-dimensional recovery member. Consequently

$$
 \mathfrak R_n(\gamma)=1
 \tag{16}
$$

for every centered Gaussian law, including the point mass at zero under the ambient recovery
convention.

### Products of one-dimensional log-concave laws

Apply the certified compact-target construction in one dimension to each nondegenerate centered
factor. Every approximant is one-dimensional and log-concave, so the exact identity and sharp
one-dimensional KLS inequality give

$$
 C_{\mathrm{CMH}}(\nu_{i,j})
 =\frac{C_P(\nu_{i,j})}{\operatorname{Var}(\nu_{i,j})}\le4.
$$

Then (12), (11), and (13) show:

$$
 \mathfrak R_n(\mu)\le4
 \tag{17}
$$

for every invertible linear image, and every affine-support embedding, of a finite product of
one-dimensional centered log-concave factors. Unlike growing-ball truncation, this tailored
coordinatewise recovery preserves the exact product structure.

This bound is sharp on the centered one-sided exponential $\lambda$. The certified
one-dimensional identity gives $C_P^{\mathrm{aff}}(\lambda)=4$, so (9) yields
$\mathfrak R_1(\lambda)\ge4$, while the preceding construction gives the reverse inequality.
Thus $\mathfrak R_1(\lambda)=4$. For a finite product of one-dimensional log-concave factors,
variance tensorization gives the upper affine-Poincar\'e bound by the maximum of the factor
constants, and coordinate tests give the reverse inequality. Hence if one factor is a centered
one-sided exponential, that product has affine Poincar\'e constant $4$ and recovery envelope
exactly $4$. No claim is made after adjoining an arbitrary higher-dimensional cofactor whose
own envelope might exceed $4$.

### The uniform simplex

The centered uniform law on a full-dimensional simplex is already a compact-target regular
moment-map law: its target density is constant and positive smooth, and the compact-target
theorem supplies the canonical data. It is the Dirichlet law with all $\alpha_i=1$, so the
certified Dirichlet theorem gives $C_{\mathrm{CMH}}\le4$. The constant sequence is therefore an
intrinsic recovery. Equations (11)--(13) give (17) for every invertible linear image, every
finite product of uniform-simplex blocks and one-dimensional factors, and every embedding of
such a law into a larger ambient affine space.

More precisely, if $U_m$ is the uniform law on the $(m-1)$-simplex, then
$C_{\mathrm{CMH}}(U_2)=12/\pi^2$. For $m=3$ the main Dirichlet proof gives the following
formula with $s_3=0$, and for $m>3$ the certified surplus gives it with $s_m>0$:

$$
 \mathfrak R_{m-1}(U_m)
 \le4\left(1+\frac{4s_m}{m(m+1)}\right)^{-1}\le4,
$$

with $s_m$ exactly as in `cor:cmh-dirichlet-surplus`. No claim that this upper bound is the
exact envelope is needed.

The exact theorem also gives $C_{\mathrm{CMH}}\le4$ for every log-concave Dirichlet law
$\alpha_i\ge1$. For $\alpha_i>1$ its density vanishes on a face, so it is not literally the
positive ambient-smooth target class used in the certified approximation lemma. Its explicit
softmax moment potential and Wright--Fisher zero-flux core supply the operative CMH data, but a
future dossier should fix whether the phrase “regular recovery sequence as in the lemma” admits
such directly verified regular members before using a constant Dirichlet sequence. The uniform
simplex has no such semantic issue.

Under the strict positive-ambient-density interpretation, let $\widetilde\nu_\varepsilon$ be the
Dirichlet law conditioned on the inner simplex $p_i\ge\varepsilon$, let $m_\varepsilon$ be its
mean, and set
$\nu_\varepsilon=(p\mapsto p-m_\varepsilon)_\#\widetilde\nu_\varepsilon$. Its density
is positive smooth on a neighborhood of its compact support and may be extended to a globally
positive $C^\infty$ function; it converges in $W_2$ to the centered Dirichlet law. The
first missing estimate is then exactly

$$
 \liminf_{\varepsilon\downarrow0}
 C_{\mathrm{CMH}}(\nu_\varepsilon)\le4.
$$

The Gamma/Wright--Fisher proof does not survive this truncation: the canonical Hessian is no
longer $C(p)/A$, the generator changes, and new no-flux faces appear. This is a genuine CMH
boundary-stability gap, not a $W_2$ approximation gap.

## Attack on a general target and the first missing estimate

The certified Gaussian-convolution/Gaussian-tilt/growing-ball construction gives regular
$\mu_k\to\mu$, but no estimate on (4). Allowing a different sequence removes the need to bound
every parameter choice; it does not create a CMH comparison principle.

For a regular $\nu$, put

$$
 Q_{\mathrm{lin}}(\nu)
 :=\lambda_{\max}\!\left(
  \Sigma_\nu^{-1/2}
  \mathbb E_\nu[H_\nu\Sigma_\nu^{-1}H_\nu]
  \Sigma_\nu^{-1/2}
 \right).
$$

Already the linear tests in (4) require a single constant $C_{\mathrm{lin}}<\infty$, independent
of $n$, $\mu$, and the requested approximation accuracy, such that along some
$W_2$-approximating sequence,

$$
 \liminf_k
 \lambda_{\max}\!\left(
  \Sigma_k^{-1/2}
  \mathbb E[H_k\Sigma_k^{-1}H_k]
  \Sigma_k^{-1/2}
 \right)\le C_{\mathrm{lin}}.
 \tag{18}
$$

No certified result constructs a sequence satisfying (18). In isotropic coordinates the
existing trace estimate controls only $\operatorname{Tr}\mathbb E H_k^2\le2n$, and the Letwin
constant-matrix estimate controls $\mathbb E\operatorname{Tr}(BH_kBH_k)$ rather than
$\mathbb E\operatorname{Tr}(B^2H_k^2)$. Their difference is the static commutator. The certified
algebraic countermodel proves that positivity, $\mathbb EH_k=I$, and Letwin's
all-symmetric-$B$ constant-matrix estimate cannot supply a dimension-free version of (18) by
matrix algebra. The countermodel is
not a genuine moment map and therefore does not refute (18); it identifies the first missing
genuine-Hessian estimate.

This probe does not open a parallel proof of `conj:gate-zero` or transfer anything to the
trace-upgrade cluster. Equation (18) is recorded only as a necessary test on the one sequence
owned by the present recovery gate.

Even a proof of (18) would not close the gate. For variable $\nabla g$ one still needs, along
the same chosen sequence,

$$
 \|\Sigma_k^{-1/2}H_k\nabla g\|_2^2
 \le C\left\{
  \|H_k^{1/2}\nabla g\|_2^2
  +\|H_k^{1/2}D^2gH_k^{1/2}\|_2^2
 \right\},
 \tag{19}
$$

including the solenoidal channel in (6). Controlling only the affine term in (6) by assuming a
universal Poincar\'e bound would insert KLS itself.

### Why the obvious construction operations stop here

There is one exact but nonuniform comparison worth isolating. If
$H_\nu(x)\preceq M\Sigma_\nu$ almost everywhere, then
$C_{\mathrm{CMH}}(\nu)\le M$. Indeed, for
$K=\Sigma_\nu^{-1/2}H_\nu\Sigma_\nu^{-1/2}\preceq MI$ one has
$K^2\preceq MK$, hence
$H_\nu\Sigma_\nu^{-1}H_\nu\preceq MH_\nu$; the numerator in (4) is bounded by $M$ times the
first Bochner term in (5).

1. **Strong-convexity bounds degenerate.** The Gaussian tilt has curvature
   $\varepsilon_kI$ with $\varepsilon_k\downarrow0$. Even if one grants the favorable
   pointwise bound $H_k\preceq\varepsilon_k^{-1}I$ furnished, where its hypotheses apply, by
   the moment-map contraction principle, the direct criterion
   above costs the uncontrolled scale
   $(\varepsilon_k\lambda_{\min}\Sigma_k)^{-1}$. Linear invariance cannot remove this relative
   scale. Thus pointwise ellipticity discards the second Bochner term that is essential at
   one-dimensional exponential-type limits, where the true CMH constant stays at most $4$.
2. **Growing compact targets give regularity, not coercivity.** Bounds that grow with
   $R_k$, $\varepsilon_k^{-1}$, the convolution scale $\delta_k^{-1}$, or
   $\lambda_{\min}(\Sigma_k)^{-1}$ are nonuniform along the recovery.
3. **Convolution has no canonical-CMH monotonicity.** A convolution is a noninvertible linear
   image of a product. It inherits a Stein kernel, but that kernel need not be the canonical
   moment-map kernel of the image. The certified arbitrary-linear-image theorem is only at the
   affine Poincar\'e level.
4. **Simplex or product lifts do not descend.** A polytope can be represented through a
   higher-dimensional simplex and a general log-concave law can be represented through
   auxiliary-variable convex lifts, but the projection is noninvertible. The product/Dirichlet
   CMH theorem therefore does not pass to the desired marginal.
5. **Triangulation and mixtures are not a comparison theorem.** Mixtures of exact simplex
   pieces need not remain log-concave, and $C_{\mathrm{CMH}}$ has no proved convexity under
   mixing.
6. **Nonlinear transport is not affine covariance.** Knothe/Brenier maps from product models
   can approximate or represent general targets, but nonlinear pushforward changes the
   canonical moment potential, its Hessian, and the generator. No CMH stability theorem is
   available.
7. **Minimizing over regularizations is only the definition.** Compactness of measures gives no
   compactness of canonical Hessians or closed generators, and no upper semicontinuity of (4).
   Choosing a minimizing sequence for (7) gives a finite universal value only after assuming
   exactly the gate.

The first unjustified step is therefore precise:

> **Needs new idea — bounded-CMH density, already in the linear sector.** Given a general
> full-dimensional centered log-concave $\mu$ and $\epsilon>0$, construct a regular
> compact-target $\nu$ such that $W_2(\nu,\mu)<\epsilon$ and
> $Q_{\mathrm{lin}}(\nu)\le C_{\mathrm{lin}}+\epsilon$, where one
> $C_{\mathrm{lin}}<\infty$ is independent of $n$, $\mu$, and $\epsilon$. Equivalently, construct
> a recovery sequence satisfying (18). No current regularization, comparison, exact-case
> density theorem, or genuine-Hessian commutator estimate supplies such a constant.

The downstream residue is:

> **Needs new idea — variable-field/solenoidal coercivity.** On the same selected sequence,
> upgrade the linear bound to (19), retaining the Bochner Hessian square and paying the Hodge
> solenoidal term. A universal bound on the affine Hodge channel cannot be taken as an input,
> because it is the KLS conclusion.

- **Technical gap (model-boundary semantics).** For nonuniform log-concave Dirichlet targets,
  either declare the directly verified softmax/Wright--Fisher class admissible as “regular,” or
  prove the displayed $\varepsilon$-inner-simplex CMH liminf. This does not affect the uniform
  simplex calibration.
- **Fenced construction operation.** Rectangular dimension-lowering projection of an exact
  product/simplex lift has no canonical-CMH recovery theorem. Singular-square monotonicity
  avoids kernel transport by using invertible maps at every finite stage, but it does not prove
  this rectangular descent.

There is no remaining technical gap in ambient $W_2$ convergence, existence of some regular
compact-target approximants, closed affine-Poincar\'e passage, or affine-support degeneration
once an intrinsic bounded-CMH recovery is supplied.

## Fence-by-fence check

The ledger assigns no `bounded_by` edge to `ass:cmh-recovery-envelope`. The complete obstruction
registry was nevertheless checked.

- `obs:two-tail`: no fixed cut, boundary slice, excess, or covariance-weighted localization
  estimate is used.
- `obs:proj-ceiling`: the failed reduction is stopped at a full canonical-Hessian matrix and a
  variable gradient field; no projection-only quadratic-chaos estimate is promoted.
- `obs:crude-insufficient`: no stochastic covariance occupation integral or logarithmic
  bootstrap appears.
- `obs:relative-ceiling`: no all-measure relative localization estimate is inserted.
- `obs:circularity`: no localized profile or evolving competitor family occurs.
- `obs:rank-one-refuted`: product structure is used only for the exact stationary CMH product
  formula, not for a stochastic product cut.

The route-specific fences are also respected.

- No canonical moment-map kernel is transported through a noninvertible image. The
  singular-square envelope inequality uses invertible maps at every finite stage and asserts no
  kernel limit. Rectangular projections and direct arbitrary-linear CMH transfer are stopped;
  arbitrary linear images are otherwise used only for certified Poincar\'e consequences.
- No convergence, lower semicontinuity, or upper semicontinuity of $C_{\mathrm{CMH}}$ is
  asserted.
- The algebraic PSD matrix law is used only as a method fence, never as a moment-map
  counterexample.
- The solenoidal channel is retained.
- Equation (18) is not claimed equivalent to `conj:gate-zero`, `q:upgrade`, high-rank
  `q:stein-weighted`, or `q:alignment`; no trace-cluster implication is asserted.

## Numerical disposition

No `finum` diagnostic is proposed. The gate asks for some unspecified finite universal
constant. A finite quotient above $4$ would only challenge the sharp endpoint, not refute the
existence of a larger recovery-envelope constant. A meaningful refutation diagnostic would
first need an analytic dimension-indexed target family and a fixed divergence threshold; this
probe establishes neither.

## Route viability and proposed gate text

The existential gate remains logically viable and is strictly better targeted than uniform
control of the canonical approximation family. It closes on tensor-generated exact classes,
and affine-support degeneration is now separated from the hard part by (13). It does not yet
advance a general law past the necessary linear canonical-Hessian estimate.

Proposed one-line gate update for the orchestrator:

> Work intrinsically on the affine hull: prove $W_2$-density, up to $o(1)$ in the constant, of
> regular compact-target laws with universally bounded full CMH quotient; vanishing compact
> Gaussian normal factors then give ambient recovery at cost $\max\{C,1\}$. A candidate sequence
> must first pass the genuine-moment-map linear quotient (18) and then the variable-field/
> solenoidal estimate (19); direct rectangular product or simplex projections with inherited,
> noncanonical kernels do not qualify.

## Proposed ledger delta

The following is a candidate structural node only. It must go through a standalone dossier and
a distinct proof-checker before any certifying status or solution metadata is proposed.

```yaml
- id: prop:cmh-recovery-calculus
  kind: proposition
  status: open
  route: moment-map-cmh
  file: modules/kls/41-cmh-normalization.tex
  statement: "The CMH recovery envelope dominates C_P^aff, is invariant under invertible linear maps, is nonincreasing under singular square linear limits in the same declared ambient dimension, is at most the maximum of the factor envelopes on finite products, and an intrinsic recovery on an affine support extends to an ambient full-dimensional recovery at cost max(C,1) by tensoring vanishing compact Gaussian normal factors. Consequently the envelope equals 1 for centered Gaussian laws, equals 4 for finite products of one-dimensional log-concave laws containing a centered one-sided exponential factor, and is at most 4 for invertible linear images, same-ambient singular square linear images, and affine-support embeddings of finite products of one-dimensional log-concave laws and uniform-simplex blocks."
  depends_on: [def:cmh, lem:affine-poincare-w2-liminf, thm:cmh-implies-affine-poincare, thm:regular-moment-map-compact-target, thm:cmh-1d, thm:cmh-product, thm:cmh-dirichlet]
```

No `proved`, `refuted`, `solution`, `checked_by`, or general-gate status delta is proposed.

```yaml
outcome: blocked
artifacts:
  - research/explorations/2026-08-27-kls-route-prober-cmh-recovery-envelope-w1c02.md
proposed_deltas:
  - "Add candidate prop:cmh-recovery-calculus only after a prover and distinct proof-checker certify the exact envelope, product, normal-collapse, Gaussian, product-law, and uniform-simplex statements; do not change ass:cmh-recovery-envelope."
  - "Sharpen the gate by the displayed intrinsic bounded-CMH-density formulation and record that affine-support collapse costs max(C,1)."
next_role: prover
next_prompt: |
  Write a standalone dossier for candidate `prop:cmh-recovery-calculus`. Define the recovery
  envelope as the infimum over liminf CMH constants of ambient-W2 regular compact-target
  sequences. Prove its lower bound by the certified affine-Poincare liminf lemma and regular CMH
  endpoint; prove invertible linear invariance and singular-square monotonicity via invertible
  maps converging to the singular map; prove the finite-product max upper bound with explicit
  simultaneous good-subsequence selection; and prove affine-support extension by
  tensoring scaled symmetric truncated-Gaussian normal factors whose one-dimensional CMH
  constants tend to 1. Deduce that every centered Gaussian has envelope exactly 1, that a
  centered one-sided exponential and any finite product of one-dimensional log-concave factors
  containing one have envelope exactly 4, and that invertible linear images, same-ambient
  singular square images, and affine-support embeddings of finite products of one-dimensional
  log-concave laws and uniform-simplex blocks have envelope at most 4. Check the compact-target regularity,
  W2 product couplings, centering, full dimensionality, boundary/core convention, and the
  universal lower bound CMH>=1. Treat nonuniform Dirichlet boundary regularity as excluded unless
  its membership in the declared recovery class is separately proved. State explicitly that the
  proposition does not discharge `ass:cmh-recovery-envelope`, prove CMH continuity, or transport
  a canonical kernel through a noninvertible map. Do not edit the ledger, manuscript, route
  files, or reviews.
```
