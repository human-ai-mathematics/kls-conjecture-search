---
---
# Proof mining: CMH product deficits and Dirichlet aggregation surplus

Date: 2026-08-27

Role: `proof-miner`

Run id: `w3t01`

Scope: extract the exponential--Gaussian transverse-deficit calculation flagged in the Wave-1
synthesis, determine its actual generality, and recover the exact surplus hidden in Dirichlet
aggregation. This record changes no ledger, manuscript, route-control file, dossier, review, or
mathematical status. No numerical evidence is used.

## Sources and certification boundary

The certified sources mined here are:

- `solutions/thm-cmh-normalization.tex`, especially the closed Stein operator and integrated
  Bochner identity;
- `solutions/thm-cmh-dirichlet.tex`, especially the product cross-term calculation and the exact
  Gamma row completion;
- `research/reviews/2026-08-25-kls-cmh-normalization-repair-audit.md`;
- `research/reviews/2026-08-25-kls-cmh-exact-cases-repair-audit.md`;
- `modules/kls/41-cmh-normalization.tex`, including the CMH and Hodge domains; and
- `modules/kls/42-cmh-exact-cases.tex`, including product tensorization and Dirichlet
  aggregation.

At extraction time the two certified dossier hashes are

```text
093a075de109d732f711468b3879cf5e2cda2c931027e15e0464e23d92704f46  solutions/thm-cmh-dirichlet.tex
53c94a296e3efb2bce3f8bd3f3fb353c40b55c06f2748e50cbfd0457f401ead7  solutions/thm-cmh-normalization.tex
```

The identities below are deductions from those proofs. They are not separately certified nodes.
In particular, their full operator-domain formulations and the quantitative consequences stated
as candidates below still require a standalone dossier and cold review.

## Executive verdict

1. The schematic Wave-1 formula is exact. If $\lambda$ is the centered rate-one one-sided
   exponential, $\gamma_d$ is standard Gaussian, $\mathcal N$ is the CMH numerator, and
   $\mathcal D=\mathbb E(L_{\lambda}+L_{\gamma})^2$, then on the common product core
   $$
   \begin{aligned}
   4\mathcal D(g)-\mathcal N(g)
   ={}&4\mathbb E\left[Y^2\left(g_{YY}-\frac12g_Y\right)^2\right]
      +3\mathbb E(L_\gamma g)^2
      +\mathbb E\|D_z^2g\|_{\mathrm{HS}}^2\\
     &+8\mathbb E\left[Y\,\|\nabla_zg_Y\|^2\right],
   \end{aligned}
   \tag{EG}
   $$
   where $Y=X+1\sim\operatorname{Exp}(1)$.
2. Formula (EG) is a model-specific exact calibration, but its mechanism is genuinely reusable.
   The certified product proof already contains a general deficit decomposition: a factor whose
   CMH constant is strictly below the product endpoint forces a quantitative penalty on every
   near-extremizer that depends on that factor, plus a positive mixed-Hessian term.
3. The Hodge identity is not used to prove (EG). It only interprets the CMH numerator after the
   fact. Consequently (EG) is not a second-variation theorem and does not resolve
   `conj:cmh-second-variation`.
4. The displayed conditional moment in the Dirichlet aggregation remark gives the exact identity
   $d_\beta(g\circ\pi)=d_\alpha(g)+D_\pi(g)$ with $D_\pi\ge0$. Applying the certified theorem to
   the fine law yields an additional, generally strict coarse-law deficit. For symmetric integer
   parameters $\alpha_i=k$, aggregation alone improves the factor $4$ to at most
   $2(k+1)/k$, before the already-certified $s_A$ surplus is included.
5. The first real analytic bottleneck is not any of these identities. It is using their static
   coercivity under a perturbation for which the law, covariance, canonical moment-map kernel,
   operator, Hodge projection, and non-attained exponential near-extremizer all vary together.

## 1. Operator data and the declared core

Let $X=Y-1$ with $Y\sim\operatorname{Exp}(1)$ and let $Z\sim\gamma_d=N(0,I_d)$ be independent.
The centered exponential has covariance one and canonical Stein kernel $H_\lambda(X)=X+1=Y$.
In the $Y$ coordinate its nonpositive Stein generator is

$$
L_\lambda=Y\partial_{YY}+(1-Y)\partial_Y.
\tag{1.1}
$$

For the standard Gaussian,

$$
H_\gamma=I_d,
\qquad
L_\gamma=\Delta_z-z\cdot\nabla_z.
\tag{1.2}
$$

On the product, the certified product theorem gives

$$
H=Y\oplus I_d,
\qquad
\Sigma=I_{d+1},
\qquad
L=L_\lambda+L_\gamma.
\tag{1.3}
$$

All calculations below are first made on the algebraic product of factor operator cores. One
concrete choice is smooth functions with Gaussian-compact support and with compactly supported
smooth $Y$ dependence satisfying the natural Laguerre zero-flux condition
$Ye^{-Y}g_Y\to0$ at $Y=0$ and $Y=\infty$. This is the same compact-support/vanishing-flux
convention used in `solutions/thm-cmh-normalization.tex:42-49,63-75` and
`modules/kls/41-cmh-normalization.tex:407-419`.

For the closed formulation put

$$
\mathsf A_\lambda=-L_\lambda,
\qquad
\mathsf A_\gamma=-L_\gamma,
\qquad
\mathsf A=\mathsf A_\lambda\otimes I+I\otimes\mathsf A_\gamma.
\tag{1.4}
$$

The two factor operators strongly commute. Hence the joint spectral theorem gives

$$
\operatorname{Dom}(\mathsf A)
=\operatorname{Dom}(\mathsf A_\lambda\otimes I)
 \cap\operatorname{Dom}(I\otimes\mathsf A_\gamma),
\tag{1.5}
$$

and $st\le(s+t)^2/4$ shows that
$\mathsf A_\lambda^{1/2}\mathsf A_\gamma^{1/2}g\in L^2$ for every
$g\in\operatorname{Dom}(\mathsf A)$. On the smooth core its squared norm is exactly
$\mathbb E[Y\|\nabla_zg_Y\|^2]$. This is the natural closed meaning of the mixed-Hessian term.
The existing product dossier does not spell out this joint-spectral closure; a prover should do
so rather than leave the candidate only as a formal core identity.

## 2. Mined proof I: exact exponential--Gaussian deficit

### Mechanism in three lines

1. The $\alpha=1$ Gamma integration by parts completes the exponential factor deficit into the
   square $Y^2(g_{YY}-g_Y/2)^2$.
2. Gaussian Bochner writes the Gaussian factor deficit as one pure Hessian square, while leaving
   three additional copies of the Gaussian generator energy at endpoint constant four.
3. The two product integrations by parts turn the generator cross term into the positive mixed
   Hessian square, with coefficient eight after multiplying the denominator by four.

### Exact definitions

For a common-core function $g=g(Y,z)$ define

$$
\begin{aligned}
\mathcal N_\lambda(g)&=\mathbb E[Y^2g_Y^2],
&\mathcal D_\lambda(g)&=\mathbb E(L_\lambda g)^2,\\
\mathcal N_\gamma(g)&=\mathbb E|\nabla_zg|^2,
&\mathcal D_\gamma(g)&=\mathbb E(L_\gamma g)^2,\\
\mathcal X(g)&=\mathbb E[Y\|\nabla_zg_Y\|^2].
\end{aligned}
\tag{2.1}
$$

Thus the product CMH numerator and denominator are

$$
\mathcal N(g)=\mathcal N_\lambda(g)+\mathcal N_\gamma(g),
\qquad
\mathcal D(g)=\mathbb E(L_\lambda g+L_\gamma g)^2.
\tag{2.2}
$$

The proof of `lem:cmh-gamma-completion` at
`solutions/thm-cmh-dirichlet.tex:192-216` uses only the one-dimensional Gamma integration by parts

$$
\mathbb E[Y^2uu']=-\frac12\mathbb E[(2Y-Y^2)u^2]
\tag{2.3}
$$

when $\alpha=1$. With $u=g_Y$ and the other variables frozen, this gives

$$
\mathcal D_\lambda(g)-\frac14\mathcal N_\lambda(g)
=\mathbb E\left[Y^2\left(g_{YY}-\frac12g_Y\right)^2\right].
\tag{2.4}
$$

The Gaussian specialization of certified `prop:cmh-bochner`, recorded at
`solutions/thm-cmh-normalization.tex:142-145`, gives

$$
\mathcal D_\gamma(g)
=\mathcal N_\gamma(g)+\mathbb E\|D_z^2g\|_{\mathrm{HS}}^2.
\tag{2.5}
$$

Finally the certified product cross-term identity at
`solutions/thm-cmh-dirichlet.tex:108-129` specializes to

$$
\mathbb E[(L_\lambda g)(L_\gamma g)]
=\mathbb E[Y\|\nabla_zg_Y\|^2]
=\mathcal X(g).
\tag{2.6}
$$

Indeed, one Laguerre integration by parts gives
$-\mathbb E[Yg_YL_\gamma g_Y]$, and Gaussian integration by parts gives the last expression.
Combining (2.2)--(2.6) proves the exact identity

$$
\boxed{
\begin{aligned}
4\mathcal D(g)-\mathcal N(g)
={}&4\mathbb E\left[Y^2\left(g_{YY}-\frac12g_Y\right)^2\right]
 +3\mathbb E(L_\gamma g)^2
 +\mathbb E\|D_z^2g\|_{\mathrm{HS}}^2\\
&+8\mathbb E[Y\|\nabla_zg_Y\|^2].
\end{aligned}}
\tag{2.7}
$$

This fixes every constant in the Wave-1 schematic statement. In particular,

$$
4\mathcal D(g)-\mathcal N(g)
\ge3\mathbb E(L_\gamma g)^2
 +8\mathbb E[Y\|\nabla_zg_Y\|^2].
\tag{2.8}
$$

### Closure to the full product operator domain

The core identity is compatible with graph closure. For a graph-Cauchy sequence $g_n$, apply
(2.7) to $g_n-g_m$. The certified product theorem gives
$\mathcal N(g_n-g_m)\le4\mathcal D(g_n-g_m)$; (2.7) then makes every square on its right Cauchy.
Equivalently, joint spectral calculus controls the factor generators and the mixed field as in
(1.5). Thus (2.7) has a canonical extension to $\operatorname{Dom}(\mathsf A)$, with all
derivative expressions understood as the closures of their core realizations. This closure is a
proof-ready deduction, not a separately reviewed repository statement.

### Quantitative near-extremizer consequence

If $\mathcal D(g)=1$ and $\mathcal N(g)\ge4-\varepsilon$, (2.7) yields separately

$$
\begin{aligned}
\mathbb E(L_\gamma g)^2&\le\varepsilon/3,\\
\mathbb E\|D_z^2g\|_{\mathrm{HS}}^2&\le\varepsilon,\\
\mathbb E[Y\|\nabla_zg_Y\|^2]&\le\varepsilon/8,\\
\mathbb E\left[Y^2\left(g_{YY}-\tfrac12g_Y\right)^2\right]&\le\varepsilon/4.
\end{aligned}
\tag{2.9}
$$

Let $\bar g(Y)=\mathbb E_{\gamma_d}g(Y,Z)$. Gaussian Poincar\'e and (2.5) imply

$$
\|g-\bar g\|_{L^2(\lambda\otimes\gamma_d)}^2
\le\mathbb E|\nabla_zg|^2
\le\mathbb E(L_\gamma g)^2
\le\varepsilon/3.
\tag{2.10}
$$

Thus every normalized CMH near-extremizer collapses in $L^2$ onto the exponential coordinate.
This is a genuine transverse-rigidity statement, not just product tensorization.

### Hypothesis usage

| hypothesis | exact use | first failure if removed | verdict |
|---|---|---|---|
| Product independence | Gives block-diagonal $H,\Sigma$, the generator sum, commuting factor operators, and two separate integrations by parts in (2.6) | Cross terms acquire derivatives of the joint density and of off-diagonal kernel blocks, with no positive square | Essential |
| Centered exponential $X=Y-1$ | Identifies $\Sigma_\lambda=1$, $H_\lambda=Y$, and drift $1-Y$ | Without recentering the displayed CMH normalization is wrong, although translation itself is harmless | Normalization, not rigidity |
| Rate one and standard Gaussian | Makes both covariances identity and fixes the displayed coefficients | Non-unit scales insert covariance matrices | Removable by invertible factorwise affine covariance |
| $\alpha=1$ in the Gamma row | Makes $\delta=\alpha^2/(\alpha+1)^2-1/4$ vanish and places the factor exactly at endpoint four | For $\alpha>1$ an additional positive zeroth-order factor deficit appears | Essential only for endpoint equality |
| Gaussian spectator | Gives exact CMH constant one and the pure-Hessian identity (2.5) | A general spectator has only its own factor deficit, not the displayed Hessian square | Replaceable by a subcritical CMH factor in the general lemma below |
| Canonical moment-map/Stein data | Supplies the certified Bochner identity and canonical product kernel | A merely symmetric Stein kernel need not satisfy the Codazzi cancellation in Bochner | Essential for the general Bochner input |
| Smooth common core and zero flux | Justifies (2.3), (2.5), and (2.6) | Boundary terms or undefined mixed derivatives appear first | Essential on the core; then removable by graph closure |
| Log-concavity | Not used in the algebra after the two factors and their canonical data are fixed | None in (2.3)--(2.7) | Structural provenance only |
| Hodge decomposition | Not used anywhere in (2.7) | Nothing breaks | Interpretive only; it must not be listed as a proof dependency |

### True bottleneck

The identity itself has no unresolved algebraic step. Its use in
`conj:cmh-second-variation` is blocked by two facts.

First, the endpoint exponential CMH constant is approached by a sequence rather than attained by
an $L^2$ eigenfunction. Second, under an admissible nonproduct perturbation, the law, covariance,
canonical kernel, generator, numerator, denominator, and Hodge projection all change. Formula
(2.7) freezes every one of them at the product law. In addition, the mixed penalty has weight
$Y$, whereas the exponential CMH numerator has weight $Y^2$; (2.9) therefore gives no uniform
CMH-numerator or Hodge-norm control of $g-\bar g$ in the far exponential tail. This mismatch is
the first quantity that can blow up in a perturbative use.

### Hodge interpretation and guardrail

Certified `prop:cmh-hodge` splits $\mathcal N(g)$ into the affine inverse-divergence energy and a
nonnegative solenoidal energy. For $g=g(Y)$ the solenoidal field vanishes because the problem is
one-dimensional. Formula (2.10) says a product-law near-extremizer is close in ordinary $L^2$ to
such a function. It does **not** say that its solenoidal energy is small: continuity in the
weighted CMH numerator is exactly what the $Y$ versus $Y^2$ mismatch fails to provide. No
second-variation sign follows.

## 3. The reusable product-deficit lemma already inside the proof

Let $\mu_i$ be centered factors carrying canonical CMH data
$(\Sigma_i,H_i,L_i)$, and for a product-core function put

$$
\mathcal N_i(g)
=\mathbb E\langle H_i\nabla_i g,\Sigma_i^{-1}H_i\nabla_i g\rangle,
\qquad
\mathcal D_i(g)=\mathbb E(L_i g)^2,
\tag{3.1}
$$

and

$$
\mathcal X_{ij}(g)
=\mathbb E\|H_i^{1/2}D^2_{ij}gH_j^{1/2}\|_{\mathrm{HS}}^2.
\tag{3.2}
$$

The exact cross identity already proved for `thm:cmh-product` gives

$$
\mathcal D(g)
=\sum_i\mathcal D_i(g)+2\sum_{i<j}\mathcal X_{ij}(g),
\qquad
\mathcal N(g)=\sum_i\mathcal N_i(g).
\tag{3.3}
$$

Therefore, for arbitrary declared constants $c_i$ and any $C$,

$$
\boxed{
C\mathcal D-\mathcal N
=\sum_i\bigl(c_i\mathcal D_i-\mathcal N_i\bigr)
 +\sum_i(C-c_i)\mathcal D_i
 +2C\sum_{i<j}\mathcal X_{ij}.}
\tag{3.4}
$$

If every factor satisfies $\CMH(\mu_i)\le c_i\le C$, every term on the right is nonnegative.
If $c_j<C$, then

$$
C\mathcal D(g)-\mathcal N(g)
\ge(C-c_j)\mathcal D_j(g)+2C\sum_{i\ne j}\mathcal X_{ij}(g).
\tag{3.5}
$$

This is the reusable result. A factor strictly below the product endpoint is quantitatively
invisible to an endpoint near-extremizer, and all mixed Hessians incident to it are penalized.
Formula (EG) is the $C=4$, exponential plus Gaussian calibration, with both individual deficits
then expanded exactly.

The mechanism transfers to arbitrary finite block products and to nondegenerate Gaussian
covariances by factorwise affine normalization. It does **not** transfer to noninvertible images:
the certified manuscript explicitly warns that the transported Stein kernel need not be the
canonical kernel of the image.

## 4. Mined proof II: unrestricted Gamma row completion

### Mechanism in three lines

1. Expand a diagonal Hessian-row square and integrate its cross term against one Gamma density.
2. Sum rows; the first-order and full Hessian terms reconstruct the integrated Laguerre Bochner
   identity exactly.
3. The parameter restriction $\alpha_i\ge1$ is used only to make the residual coefficient
   $\delta_i$ nonnegative; neither the identity nor its proof uses degree-zero homogeneity.

For independent $Y_i\sim\Gamma(\alpha_i,1)$ and an arbitrary smooth core function $G$, define

$$
N_\Gamma(G)=\mathbb E(\mathcal L_\Gamma G)^2,
\qquad
D_i(G)=\frac1{\alpha_i}\mathbb E[Y_i^2G_i^2],
\qquad
D_\Gamma=\sum_iD_i.
\tag{4.1}
$$

The computation at `solutions/thm-cmh-dirichlet.tex:192-216` proves, without invoking Euler's
identity or homogeneity,

$$
N_\Gamma(G)-\frac14D_\Gamma(G)
=\sum_i\mathbb ER_i+\sum_i\delta_iD_i(G),
\tag{4.2}
$$

where

$$
R_i=Y_i^2\left|G_{ii}-\frac{G_i}{\alpha_i+1}\right|^2
 +\sum_{j\ne i}Y_iY_j|G_{ij}|^2,
\qquad
\delta_i=\frac{\alpha_i^2}{(\alpha_i+1)^2}-\frac14.
\tag{4.3}
$$

The identity is valid for $\alpha_i>0$ whenever the integrations are justified. The sign
$\delta_i\ge0$ is equivalent to $\alpha_i\ge1$. In particular, (4.2) proves the product-Gamma
CMH bound for arbitrary test functions when all $\alpha_i\ge1$, and for $\alpha_i=1$ it gives
the exponential square in (2.4).

### Hypothesis usage and defect

| hypothesis | exact use | verdict |
|---|---|---|
| $\alpha_i>0$ | Defines the Gamma laws and the integration-by-parts density | Needed for the identity |
| $\alpha_i\ge1$ | Only makes $\delta_i\ge0$ | Needed for the CMH(4) consequence, not the identity |
| Homogeneity of degree zero | First used later in `lem:cmh-row-min` through $\sum_jY_jG_{ij}=-G_i$ | Unused in Gamma completion |
| Smoothness/decay or closed Laguerre core | Removes endpoint flux and makes all terms finite | Needed, then closable |

There is a semantic scope mismatch in the certified surfaces. The manuscript and dossier set
$G(Y)=g(Y/S)$ before stating `lem:cmh-gamma-completion`, and the ledger explicitly states that
$G$ is homogeneous of degree zero. Yet the proof uses no homogeneity, and the immediately
following remark says the lemma alone proves $\mathrm{CMH}(4)$ for the full product-Gamma law,
which requires arbitrary test functions. The review repeats that consequence without flagging
the restricted statement. This is not a false formula; it is a hidden stronger theorem and a
statement/proof mismatch that should be repaired only through a new author/reviewer cycle.

## 5. Mined proof III: exact Dirichlet aggregation surplus

### Mechanism in three lines

1. Coordinate aggregation intertwines the fine and coarse Wright--Fisher generators exactly, so
   the CMH denominators agree.
2. Conditional Dirichlet second moments show that the fine CMH numerator is the coarse numerator
   plus an explicit positive block-refinement energy.
3. Applying the certified fine-law CMH theorem, and optionally its $s_A$ surplus, transfers that
   entire extra energy into a strict coarse-law deficit.

Let $Q\sim\operatorname{Dir}(\beta_1,\ldots,\beta_N)$ and partition the fine coordinates into
nonempty blocks $G_1,\ldots,G_m$. Set

$$
r_i=|G_i|,
\qquad
P_i=\sum_{a\in G_i}Q_a,
\qquad
\alpha_i=\sum_{a\in G_i}\beta_a,
\qquad
A=\sum_a\beta_a=\sum_i\alpha_i.
\tag{5.1}
$$

Then $P\sim\operatorname{Dir}(\alpha)$. For $Ug=g\circ\pi$ define

$$
h_i(P)=\partial_i g(P)-\sum_jP_j\partial_jg(P),
\qquad
u_i^\alpha=P_ih_i,
\qquad
u_a^\beta=Q_ah_i\quad(a\in G_i).
\tag{5.2}
$$

Direct substitution in the Wright--Fisher generators gives

$$
L_\beta Ug=U L_\alpha g,
\qquad
n_\beta(Ug)=n_\alpha(g).
\tag{5.3}
$$

Conditionally on $P$, the proportions $(Q_a/P_i)_{a\in G_i}$ have Dirichlet parameters
$(\beta_a)_{a\in G_i}$. Therefore

$$
\mathbb E\left[\left.\sum_{a\in G_i}\frac{Q_a^2}{\beta_a}\right|P\right]
=P_i^2\frac{\alpha_i+r_i}{\alpha_i(\alpha_i+1)}.
\tag{5.4}
$$

Using the definitions of $d_\alpha$ and $d_\beta$ from
`modules/kls/42-cmh-exact-cases.tex:175-185` gives the exact identity

$$
\boxed{
d_\beta(Ug)=d_\alpha(g)+D_\pi(g),
\qquad
D_\pi(g)=\mathbb E\sum_i
\frac{r_i-1}{\alpha_i(\alpha_i+1)}\bigl(u_i^\alpha(P)\bigr)^2.}
\tag{5.5}
$$

The manuscript records (5.4) and only the inequality $d_\beta\ge d_\alpha$ at
`modules/kls/42-cmh-exact-cases.tex:396-403`. The exact subtraction (5.5) is the unrecorded
surplus.

If every $\beta_a\ge1$, the certified fine-law theorem applies and yields

$$
n_\alpha(g)-\frac{A(A+1)}4d_\alpha(g)
\ge\frac{A(A+1)}4D_\pi(g).
\tag{5.6}
$$

For $A>3$, applying the certified fine-law `cor:cmh-dirichlet-surplus` gives the stronger bound

$$
n_\alpha(g)-\frac{A(A+1)}4d_\alpha(g)
\ge s_A d_\alpha(g)
 +\left(\frac{A(A+1)}4+s_A\right)D_\pi(g).
\tag{5.7}
$$

Thus the direct scalar surplus and aggregation surplus multiply rather than compete.

### Uniform aggregation gain

Put

$$
\kappa_\pi
=\inf_{\substack{u\ne0\\\sum_i u_i=0}}
\frac{\displaystyle\sum_i
 \frac{r_i-1}{\alpha_i+1}\frac{u_i^2}{\alpha_i}}
 {\displaystyle\sum_i\frac{u_i^2}{\alpha_i}}.
\tag{5.8}
$$

Since $\sum_i u_i^\alpha=0$, (5.5) gives
$D_\pi(g)\ge\kappa_\pi d_\alpha(g)$. Consequently

$$
\CMH(\operatorname{Dir}(\alpha))
\le\frac4{1+\kappa_\pi},
\tag{5.9}
$$

and for $A>3$,

$$
\CMH(\operatorname{Dir}(\alpha))
\le
\frac4{
\left(1+\frac{4s_A}{A(A+1)}\right)(1+\kappa_\pi)}.
\tag{5.10}
$$

The finite-dimensional quotient in (5.8) has the following exact qualitative behavior.

- $\kappa_\pi>0$ if and only if at most one block is a singleton.
- If all $r_i\ge2$, then
  $\kappa_\pi\ge\min_i(r_i-1)/(\alpha_i+1)$.
- If $G_j$ is the unique singleton, weighted Cauchy--Schwarz and $\sum_i u_i=0$ give
  $$
  \kappa_\pi\ge\frac{\alpha_j}{A}
  \min_{i\ne j}\frac{r_i-1}{\alpha_i+1}.
  \tag{5.11}
  $$
- With two singleton blocks, a nonzero tangent vector supported on those two blocks makes the
  quotient zero. Individual functions can still have $D_\pi(g)>0$; only a uniform gain fails.

If every $\alpha_i$ is an integer $k_i\ge1$, split block $i$ into $r_i=k_i$ fine coordinates
with all $\beta_a=1$. For the symmetric case $k_i=k$,
$\kappa_\pi=(k-1)/(k+1)$, so aggregation alone gives

$$
\CMH(\operatorname{Dir}(k,\ldots,k))\le\frac{2(k+1)}k.
\tag{5.12}
$$

For general real $\alpha_i\ge2$, the strongest elementary log-concave refinement takes
$r_i=\lfloor\alpha_i\rfloor$, with $r_i-1$ unit parameters and one remaining parameter at least
one. This maximizes the block coefficient among refinements whose fine parameters stay in the
certified range.

### Domain and hypothesis usage

The identities (5.3)--(5.5) require only $\beta_a>0$ and hold first on the polynomial core.
The pullback $U$ is an $L^2$ isometry, maps coarse polynomials to fine polynomials, and
intertwines the generators. Graph-core approximation and closedness therefore extend them to
$\operatorname{Dom}(L_\alpha)$. Invoking the certified fine CMH theorem requires
$\beta_a\ge1$; hence necessarily $\alpha_i\ge r_i$. This splittability restriction is
load-bearing.

| hypothesis | exact use | first failure if removed | verdict |
|---|---|---|---|
| Fine Dirichlet law and coordinate partition | Gives conditional Dirichlet proportions and generator intertwining | A general noninvertible linear image has neither property | Essential |
| $\beta_a>0$ | Defines both Dirichlet laws and the second moments in (5.4) | Conditional moments cease to be a probability-law identity | Essential for the identity |
| $\beta_a\ge1$ | Invokes the certified fine-law CMH and $s_A$ estimates | (5.5) survives but (5.6)--(5.10) no longer follow | Essential for the certified inequality |
| $g$ depends only on block sums | Makes fine derivatives constant within each block | Within-block derivatives create additional terms of no fixed sign | Essential |
| Polynomial/operator core | Justifies the differential intertwining, then graph closure | Arbitrary $L^2$ functions have no generator or CMH energy | Essential domain contract |
| Log-concavity of the coarse law | Automatic from $\alpha_i\ge r_i\ge1$ | No separate use after the fine theorem is invoked | Inherited, not an extra step |

### True bottleneck and scope

There is no missing algebraic step. The limitation is structural: a coarse coordinate with
$\alpha_i<2$ cannot be split nontrivially while keeping every fine parameter at least one. With
two such unsplit coordinates the aggregation quadratic form has a tangent null direction, so
this mechanism alone gives no uniform strict improvement. It also proves no general
noninvertible-image monotonicity for CMH; it succeeds only because Dirichlet aggregation preserves
the Wright--Fisher generator and has the exact conditional second moment (5.4).

Iterating a hierarchy of coordinate partitions gives an additive sum of levelwise terms
$D_{\pi_\ell}$ by repeated use of (5.5). This is a valid reuse, but it is not a new mechanism and
does not evade the splittability restriction at any level.

## 6. Parked candidate nodes, ledger-ready

Every item below is parked for later prioritization and, if admitted, must enter as
`status: open`. None is certified or promoted by this mining report.

### Candidate A: `lem:cmh-product-deficit-decomposition`

- **kind:** lemma
- **route:** `moment-map-cmh`
- **refines:** `thm:cmh-product`
- **exact statement:** For a finite product of centered factors carrying canonical CMH data, for
  every function in the common product operator domain and every constants
  $c_i\ge\CMH(\mu_i)$ and $C\ge\max_i c_i$, equations (3.3)--(3.4) hold, with mixed terms defined
  by closure from the tensor core. In particular (3.5) holds for each subcritical factor.
- **program:** prove the core identity from the already-certified two-fold integration by parts;
  use the joint spectral theorem and graph closure to fix the full domain; state the finite-factor
  induction and factorwise affine covariance.
- **proposed `depends_on`:** `[def:cmh, thm:cmh-product]`
- **proposed `bounded_by`:** `[]`

### Candidate B: `cor:cmh-exponential-gaussian-transverse-deficit`

- **kind:** corollary
- **route:** `moment-map-cmh`
- **refines:** `cor:cmh-product-saturation`
- **exact statement:** For $\lambda\otimes\gamma_d$, with the closed operators and fields fixed in
  Section 1, identity (2.7) holds on $\operatorname{Dom}(\mathsf A)$. If
  $\mathcal D(g)=1$ and $\mathcal N(g)\ge4-\varepsilon$, then (2.9)--(2.10) hold.
- **program:** combine Candidate A, the unrestricted $\alpha=1$ Gamma completion, and Gaussian
  Bochner; prove closure and the conditional Gaussian Poincar\'e consequence. Explicitly disclaim
  a perturbative or Hodge-energy conclusion.
- **proposed `depends_on`:**
  `[lem:cmh-product-deficit-decomposition, prop:cmh-bochner, lem:cmh-gamma-completion]`
- **proposed `bounded_by`:** `[]`

### Candidate C: `lem:cmh-gamma-completion-unrestricted`

- **kind:** lemma
- **route:** `moment-map-cmh`
- **refines:** `lem:cmh-gamma-completion`
- **exact statement:** For independent $Y_i\sim\Gamma(\alpha_i,1)$ with $\alpha_i>0$ and every
  function in the product Laguerre operator core, without any homogeneity assumption, (4.2)--(4.3)
  hold. If $\alpha_i\ge1$ for all $i$, all residual coefficients are nonnegative and the full
  product-Gamma law satisfies CMH(4); the identity extends to the closed product operator domain.
- **program:** reuse the written one-row integration by parts verbatim, separate identity from
  sign, and supply graph closure.
- **proposed `depends_on`:** `[def:cmh, prop:cmh-bochner]`
- **proposed `bounded_by`:** `[]`

### Candidate D: `prop:cmh-dirichlet-aggregation-deficit`

- **kind:** proposition
- **route:** `moment-map-cmh`
- **refines:** `cor:cmh-dirichlet-surplus`
- **exact statement:** Under (5.1), for $\beta_a>0$, the generator intertwining (5.3) and exact
  energy identity (5.5) hold on the polynomial core and by closure on
  $\operatorname{Dom}(L_\alpha)$. If every $\beta_a\ge1$, then (5.6), (5.8)--(5.10) hold, with
  the stated criterion and bounds for $\kappa_\pi$; include the symmetric integer calibration
  (5.12).
- **program:** prove the derivative intertwining and conditional second moment; pass through the
  polynomial graph core; derive the tangent-space Rayleigh quotient and combine with the already
  certified $s_A$ theorem.
- **proposed `depends_on`:**
  `[def:cmh, thm:cmh-dirichlet, cor:cmh-dirichlet-surplus]`
- **proposed `bounded_by`:** `[]`

## 7. Fence-by-fence check

The CMH route currently carries no formal `bounded_by` edges for these exact-case nodes. The
empty proposals above also survive every repository obstruction.

| fence | check |
|---|---|
| `rem:two-tail-slice-bounds` | Concerns fixed-cut Eldan slice weights. These are stationary CMH identities with no cut, covariance weight, or excess estimate. |
| `rem:projection-ceiling` | The product lemma keeps the full mixed Hessian and the Dirichlet lemma keeps the full tangent field and conditional block moments. Neither derives quadratic chaos from radial or projection tests. |
| `rem:crude-insufficient` | No stochastic covariance integral or bootstrap input occurs. |
| `rem:relative-ceiling` | No all-measure relative covariance bound is asserted. |
| `rem:profile-circularity` | No localized isoperimetric profile or posterior competitor family occurs. |
| `rem:single-coordinate-cuts` | No product-cut occupation claim occurs. Product structure is used only for an exact stationary operator identity. |
| CMH gate-zero guardrail | The results concern products and Dirichlet aggregations already inside certified classes. They give no universal bound on $\mathbb E[H\Sigma^{-1}H]$. |
| Hodge/perturbation guardrail | Static product transverse coercivity is not identified with the solenoidal second variation. |
| Noninvertible-image guardrail | Candidate D is explicitly Dirichlet-specific; no general canonical-CMH monotonicity under singular maps is inferred. |

## 8. Defects and omissions found

1. **`lem:cmh-gamma-completion` scope mismatch.** The ledger states degree-zero homogeneity, while
   the proof never uses it and the manuscript/dossier immediately claim an arbitrary
   product-Gamma consequence. The exact identity also holds for $\alpha_i>0$; only nonnegativity
   uses $\alpha_i\ge1$. A new proof/review cycle should either strengthen the existing node or add
   Candidate C.
2. **`thm:cmh-product` domain passage is implicit.** The certified proof establishes the
   conditional and cross identities on a smooth product core but does not print the joint-spectral
   passage to the full $\operatorname{Dom}(\mathsf A)$ used in the definition of CMH. The passage
   is recoverable by (1.5) and positivity, so no counterexample or status downgrade is proposed;
   Candidate A should persist it explicitly.
3. **The Dirichlet aggregation remainder is suppressed.** The manuscript prints the exact
   conditional moment but records only monotonicity and calls it a consistency check. Subtracting
   the coarse coefficient yields (5.5), and the certified fine theorem yields the strict
   quantitative consequences. This is missed strength, not an error in the existing theorem.
4. **Hodge is not a dependency of the transverse identity.** Treating the positive terms in
   (2.7) as the Hodge solenoidal component would be false. The Hodge field is defined by a separate
   covariance-divergence projection, and the current proof supplies no equality with the mixed
   Hessian squares.

## 9. Archived-attempt comparison

- The `rotated Gamma--Gaussian` item in
  `research/explorations/2026-08-25-kls-cmh-model-archive.md` concerns failure of a guessed
  cofactor conservation law in the older construction layer. It is unrelated to (EG), which is
  an exact normalization-layer product identity. This extraction is not a rerun of that failed
  route.
- The weak Dirichlet aggregation compatibility is already in the manuscript and was recomputed by
  the exact-case reviewer. The new content is the retained remainder, its tangent-space coercivity
  constant, and its combination with $s_A$.
- The product maximum formula is already certified. Candidate A does not re-prove tensorization;
  it records the quantitative deficit that its proof discards.

## 10. Proposed knowledge entry for the synthesizer

**CMH product deficit decomposition.** For a canonical product, the CMH denominator splits into
factor generator squares plus twice the nonnegative mixed-Hessian squares. Therefore at endpoint
$C$,

$$
C\mathcal D-\mathcal N
=\sum_i(c_i\mathcal D_i-\mathcal N_i)
 +\sum_i(C-c_i)\mathcal D_i
 +2C\sum_{i<j}\mathcal X_{ij}.
$$

**Use.** Quantitatively eliminate subcritical spectator dependence from product-law CMH
near-extremizers. The exponential--Gaussian case has the exact expansion (2.7).

**Guardrail.** This is a fixed-product identity. It is not stable under an arbitrary nonproduct
perturbation or noninvertible image, and its mixed-Hessian term is not the Hodge solenoidal term.

## Shared handoff envelope

```yaml
outcome: complete
artifacts:
  - research/explorations/2026-08-27-proof-miner-cmh-transverse-deficit-w3t01.md
proposed_deltas:
  - "Park lem:cmh-product-deficit-decomposition and cor:cmh-exponential-gaussian-transverse-deficit as proof-ready candidates for one future coupled dossier; do not promote them from this report."
  - "Park prop:cmh-dirichlet-aggregation-deficit as a separate proof-ready candidate; do not promote it from this report."
  - "Record the hidden generality of lem:cmh-gamma-completion as certification debt for a future proof/review cycle: its identity uses neither homogeneity nor alpha_i >= 1, while its nonnegative consequence does."
  - "If later prioritized, ask the singleton synthesizer to curate the CMH product deficit decomposition with the fixed-product and non-Hodge guardrails above."
next_role: orchestrator
next_prompt: |
  Keep the four candidates in Section 6 parked at status open/no-status until a later wave
  explicitly prioritizes them. If that happens, assign one prover a coupled product-deficit
  dossier and a separate prover the Dirichlet aggregation dossier, then use distinct cold
  reviewers. Preserve the full domain, splittability, non-Hodge, noninvertible-image, and
  non-perturbative guardrails from this report; do not infer a universal CMH or KLS status
  change.
```
