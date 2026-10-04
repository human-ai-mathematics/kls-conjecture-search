---
---

# Wave A: two-sided target perturbations fail the admissibility gate

## Question examined

Starting lens: **refute**, extremal/boundary, for `ap:c-solenoidal-perturbation` and
`conj:cmh-second-variation`. The mission required a genuinely nontrivial target-side
perturbation, log-concave for both signs, before calculating full CMH variation.

The canonical conjecture, verbatim, is:

> Take the product moment potential $\psi_0(s,t)=\phi(s)+t^2/2$ with $\phi$ the one-sided exponential moment potential, and perturb it by $\psi_\eps=\psi_0+\eps\,a(s)b(t)$. Call the perturbation admissible if, for all sufficiently small $\abs\eps$, $\psi_\eps$ is smooth and strictly convex and its moment measure $\mu_\eps$ is log-concave and belongs to the regular moment-map class on which [](#def:cmh) is set. Then, for every admissible perturbation,
>
> $$\limsup_{\eps\to0}\frac{\CMH(\mu_\eps)+\CMH(\mu_{-\eps})-2\CMH(\mu_0)}{\eps^2}\le0,$$
>
> where $\CMH(\mu_0)=4$ by [](#cor:cmh-product-saturation).

Exact negation attacked: there exist $a,b$ and $\varepsilon_0>0$ such that for
every $|\varepsilon|<\varepsilon_0$ the specified
$\psi_\varepsilon=\phi(s)+t^2/2+\varepsilon a(s)b(t)$ is smooth and strictly
convex and its moment measure is log-concave and belongs to the regular class of
`def:cmh`, and

$$\limsup_{\varepsilon\to0}
\frac{\mathrm{CMH}(\mu_\varepsilon)+\mathrm{CMH}(\mu_{-\varepsilon})-8}
{\varepsilon^2}>0.$$

The portfolio's exponential-times-exponential target differs from the canonical
exponential-times-Gaussian source ansatz. Both saturate by `thm:cmh-product`, but
a witness for one is not automatically a witness to the other quantified claim.

## What we learned

### Established (uncertified): fixed-support target-linear rigidity

Let $\Omega$ be open and convex, $V_0$ affine, and $c\in C^2(\Omega)$.
If $V_0+\varepsilon c$ is convex for every sufficiently small signed $\varepsilon$,
then at every $x\in\Omega$ and every $v$,

$$0\le v^TD^2(V_0+\varepsilon c)(x)v
=\varepsilon v^TD^2c(x)v.$$

Both signs force $D^2c=0$ by polarization, so $c(x)=\ell\cdot x+k$.
Normalization adds only a spatial constant. Convexity inequalities give the same
conclusion without differentiability when both signed potentials are finite.

On the positive orthant, $V_0=x+y$, so the entire two-sided target-linear class is
the exponential product with rates $r_i=1+\varepsilon\ell_i>0$. After centering,
it is the law of $T(E-\mathbf1)$, where $E_i$ are independent unit exponentials
and $T=\operatorname{diag}(r_1^{-1},r_2^{-1})$. Its exact data are

$$\Sigma_\varepsilon=TT^T,\qquad
H_\varepsilon(Tz)=T\operatorname{diag}(z_1+1,z_2+1)T^T.$$

The finite-boundary normal flux vanishes, and exponential tails justify polynomial
integrations by parts. For $g_\varepsilon(Tz)=g_0(z)$,

$$L_\varepsilon g_\varepsilon(Tz)=L_0g_0(z),\qquad
\mathbb E\langle H_\varepsilon\nabla g_\varepsilon,
\Sigma_\varepsilon^{-1}H_\varepsilon\nabla g_\varepsilon\rangle
=\mathbb E|H_0\nabla g_0|^2.$$

Thus the full numerator and denominator are unchanged. In `prop:cmh-hodge`,
the covariance Poisson solution pulls back as $\psi_\varepsilon(Tz)=\psi_0(z)$;
the gradient field and solenoidal field each push forward by $T$, so their
separate energies are unchanged as well. The optimizing test is transported.
Since total-degree polynomial spaces are preserved by affine changes, their
optimized full quotients satisfy

$$Q_d(\varepsilon)=Q_d(0),\qquad Q_d''(0)=0\quad(d\ge1).$$

In particular the exact degree-one through degree-four second variations are all
zero for these directions, without assuming any formula for $Q_d(0)$.
Full CMH is identically four by affine covariance and `cor:cmh-product-saturation`.
These remain boundary-model calculations, not a nonproduct regular perturbation.

### Established (uncertified): a Gaussian spectator does not rescue a linear coupling

On $(0,\infty)\times\mathbb R$ let $V_0=x+y^2/2$. Two-sided convexity of
$V_0+\varepsilon c$ forces $c_{xx}=0$, hence $c=xA(y)+B(y)$.
The perturbed Hessian then has identically zero $xx$ entry. A positive
semidefinite matrix with a zero diagonal entry has a zero corresponding row,
so $\varepsilon A'(y)=0$ and $A$ is constant. Thus the perturbation can only
change the exponential rate and the separate Gaussian factor, subject to the
latter's own convexity and integrability constraints. Whenever these hold,
`thm:cmh-product` and `thm:cmh-1d` give full CMH exactly four.

This does **not** classify the canonical source-linear family: its induced target
potential generally has higher-order epsilon terms. No vacuity of the conjecture
is established.

### Established (uncertified): radial Gamma variation is one-sided

In orthant coordinates the interval-cone family is

$$\rho_\beta(x,y)=\frac{(x+y)^{\beta-2}e^{-(x+y)}}{\Gamma(\beta)}
\mathbf1_{x,y>0},\qquad\beta>0.$$

Indeed $s=x+y$, $u=x/(x+y)$ has Jacobian $s$, so $s$ is Gamma and $u$ uniform,
independently. Its potential has Hessian

$$D^2V_\beta=\frac{\beta-2}{(x+y)^2}
\begin{pmatrix}1&1\\1&1\end{pmatrix}.$$

Log-concavity is therefore equivalent to $\beta\ge2$.
The path $\beta=2+\varepsilon$ fails for every negative epsilon. More generally,
$V_\varepsilon=x+y+\varepsilon a(x+y)$ is two-sided convex only if $a''=0$.

The nonlinear path $\beta=2+\varepsilon^2$ escapes this obstruction: it is
log-concave for both signs, with nonzero mixed log-density derivative for
$\varepsilon\ne0$, hence is not a product in these coordinates. Its first
variation vanishes. An epsilon-second-variation calculation is a one-sided
first variation in beta, not the proposed linear-direction Hessian. This path
does not have the canonical source-linear ansatz either. The certified
`prop:cone-moment-map` supplies a possible exact boundary oracle.

### Established (uncertified): regular approximation loses the exact endpoint

The unbounded exponential and cone supports do not meet the compact-support
hypothesis of `thm:regular-moment-map-compact-target`. They are exact boundary
calibrations. A regular version of the even radial path is explicit: restrict
its density to $P_{\delta,R}=[\delta,R]^2$, $0<\delta<R<\infty$, normalize,
and center. The positive smooth density near this body extends positively and
smoothly to all space by extending its potential with a smooth cutoff.
Convexity holds on the body. The cited theorem supplies a smooth strictly convex
canonical potential, target diffeomorphism, and weak zero flux for every epsilon.
At zero this is a product of truncated exponentials, not the exact saturator.

As $\delta\downarrow0$ and $R\uparrow\infty$, dominated convergence recovers
the boundary law with moments, also uniformly for beta in a compact interval
on its admissible side. But `lem:affine-poincare-w2-liminf` and
`prop:cmh-approximation-closure` control a scalar Poincare limit, not CMH or its
derivatives. They do not identify the regular kernel with the cone kernel or
justify passing second variations to the limit. Those are still missing estimates.

### Prior evidence and fences

No numerical calculation is a premise of this checkpoint. The prior experiments
`2026-08-30-finum-cmh-ab-m9-w4c02.md` and
`2026-09-06-numerics-cmh-cone-w5n01.md` motivated this analytical gate.
The former's suggested target potential $V_0+\varepsilon c$ with convex $c$
is admissible **one-sidedly**, not for both signs unless affine.

The target has no explicit `bounded_by` entries. Substantive fences are respected:
product saturation and `thm:cmh-product` are preserved; `prop:cmh-hodge` retains
both channels and no-flux domains; no invented Stein kernel circumvents
`prop:letwin-not-gate-zero`; `cand:cmh-exponential-galerkin-rate` is not assumed;
and regular approximation is not strengthened into CMH continuity.

## What resists

There is no nonproduct two-sided target-linear direction on the fixed support of
either product model. This blocks the proposed calculation, not the source-linear
conjecture. Nonlinear paths, moving supports, and varying regular approximants
remain outside the no-go. No refuter dossier is offered.

A stable positive coefficient at fixed degree would still not suffice. If
$Q_d(\varepsilon)=4-\delta_d+a_d\varepsilon^2+R_d(\varepsilon)$ with
$\delta_d>0$, one needs an admissible epsilon for which
$a_d\varepsilon^2+R_d(\varepsilon)>\delta_d$, or a uniform joint degree/parameter
argument. Neither endpoint attainment nor differentiation through the optimizing
supremum is available merely from positive $a_d$.

## Proposed next step

Replace the impossible target-linear instruction by a precise family. An explicit
boundary test is $\rho_{2+\varepsilon^2}$: use `prop:cone-moment-map`, varying
covariance, and the full numerator and denominator to calculate the right beta
derivative of the degree-one through degree-four quotient at beta two. Identify
separately an estimate transferring any strict finite-test violation to the regular
$P_{\delta,R}$ approximants. This probes CMH(4), not automatically the canonical
source-linear conjecture. Retaining that conjecture literally instead requires
solving its source-linear admissibility gate first.

Proposed portfolio delta: keep `ap:c-solenoidal-perturbation` active and replace
its `next` by this family-and-regularity gate. Delete the inference from a stable
positive finite-degree coefficient to a candidate refutation without deficit and
remainder control. No claim-status or dependency delta.

Handoff: this checkpoint only; no runs. Outcome: analytical obstruction, with the
target negation unresolved. Next: independent examination of the fixed-support
rigidity and affine quotient transport, followed by a choice between the canonical
source-linear question and the explicit even radial boundary family.
