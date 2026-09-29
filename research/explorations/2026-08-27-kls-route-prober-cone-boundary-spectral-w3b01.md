---
---
# KLS route probe W3-B01: rounded isotropic right-cone boundary gap

Date: 2026-08-27

Role: `kls-route-prober`

Gate owner: rounded isotropic right-cone test for the unregistered
`cone-boundary-spectral` candidate

Verdict: **PROMOTE the candidate to a registered probe, not to a theorem.**

No numerical experiment was used. This report makes no statement, comparison, or transfer
concerning the trace-upgrade cluster.

## Gate, quoted verbatim

The route scout's exact kill gate is:

> Find mean-zero profiles satisfying the seam condition for which
> $\mathcal E_n(\psi,\phi)/\operatorname{Var}_{\pi_n}(\psi,\phi)\to0$, or prove a
> universal lower bound and then handle the spherical modes.

The requested closure obligation is also verbatim:

> Because $K_n$ is not smooth, a refuting profile must be transferred to $C^2$ strictly
> convex $\varepsilon_n$-roundings. A profile supported away from the apex/seam, or a
> Mosco-convergent rounding calculation, supplies that transfer. A vanishing first boundary
> eigenvalue on such roundings **rejects the route**. A positive cone calculation does not
> prove the route; it merely earns the next tests, regular simplices and product seams.

This report proves the positive alternative on the singular cones, including all spherical
modes, and gives the fixed-dimension Mosco argument that produces a diagonal family of smooth,
strictly convex, exactly isotropic roundings with the same universal gap up to a factor two.

## Disposition in one line

For the relaxed tangential form of normalized cone measure on the isotropic right cones $K_n$,

$$
  C_P(\partial K_n,\sigma_{K_n})\leq \frac{425}{12}
  \qquad(n\geq2).
  \tag{1}
$$

For each $n$ there are $C^\infty_+$ isotropic roundings $\widehat K_{n,\varepsilon}$ converging
to $K_n$ for which

$$
  C_P(\partial\widehat K_{n,\varepsilon},
      \sigma_{\widehat K_{n,\varepsilon}})
  \leq \frac{425}{6}
  \tag{2}
$$

once $\varepsilon$ is sufficiently small (depending on $n$). Thus neither dimension nor the
isotropically normalized opening degenerates this kill family. This is a model-family pass, not
a proof of the all-body boundary target.

## 1. External Hardy bridge: exact assumptions and exact use

The primary source was checked in its final arXiv source, version 2:

- A. V. Kolesnikov and E. Milman, *Remarks on the KLS Conjecture and Hardy-Type
  Inequalities*, Lecture Notes in Mathematics 2116 (2014), 273--292,
  arXiv:1405.0617v2, DOI `10.1007/978-3-319-09477-9_18`.

Its Corollary 8 (`cor:Hardy1` in the source) assumes that $\Omega$ is a smooth convex domain
whose barycenter is the origin and states

$$
 P^N_\Omega\leq C P^\infty_\Omega
 \leq C\left(\frac4nP^{\mathrm{Lin}}_\Omega
                 +2P^\infty_{\sigma_{\partial\Omega}}\right).
 \tag{3}
$$

Here $\sigma_{\partial\Omega}$ is exactly the normalized cone measure

$$
 d\sigma_{\partial\Omega}(y)
 =\frac{\langle y,\nu(y)\rangle}{n|\Omega|}
   d\mathcal H^{n-1}(y),
 \tag{4}
$$

and $P^\infty_\sigma$ tests restrictions to the boundary of smooth ambient functions, with the
ambient $L^\infty$ gradient norm. There is no curvature lower bound in Corollary 8. Smoothness,
convexity, and centering are the relevant assumptions.

If the intrinsic boundary inequality

$$
 \operatorname{Var}_{\sigma_{\partial\Omega}}g
 \leq C_\partial\int_{\partial\Omega}
       |\nabla_{\partial\Omega}g|^2d\sigma_{\partial\Omega}
 \tag{5}
$$

holds for all boundary Sobolev functions, then it applies to the restriction of every ambient
$1$-Lipschitz function and gives $P^\infty_{\sigma_{\partial\Omega}}\leq C_\partial$. For an
isotropic body $P^{\mathrm{Lin}}_\Omega=1$, so (3) gives a dimension-free interior Neumann gap.
Thus the published bridge has the measure and normalization used by the scout.

The converse is neither asserted nor used. In particular, proving only the ambient-Lipschitz
boundary estimate would recover the scout's circular weak formulation. The calculation below
controls the entire intrinsic Sobolev form and does not invoke KLS, an interior Poincare
inequality, or a thin-shell argument.

## 2. Isotropic normalization removes the opening parameter

Start with a right circular cone in $\mathbb R\times\mathbb R^{n-1}$ having apex at $t=b$,
base at $t=-a$, height $H=a+b$, and base radius $R$. Put

$$
 u=\frac{b-t}{H}.
$$

For uniform volume measure, $u$ has density $nu^{n-1}du$. Centering the axial coordinate gives
$b=na$ and $H=(n+1)a$. Moreover,

$$
 \operatorname{Var}(t)
 =H^2\frac{n}{(n+1)^2(n+2)}
 =\frac{na^2}{n+2},
$$

so axial isotropy forces

$$
 a^2=\frac{n+2}{n}.
 \tag{6}
$$

Conditionally on $u$, the transverse coordinate is uniform on the
$(n-1)$-ball of radius $Ru$. Hence

$$
 \mathbb E z_i^2
 =\frac{R^2}{n+1}\mathbb E u^2
 =\frac{R^2n}{(n+1)(n+2)},
$$

and transverse isotropy forces

$$
 R^2=\frac{(n+1)(n+2)}n.
 \tag{7}
$$

Consequently every centered right circular cone becomes, after its diagonal isotropic map and
a rotation, exactly

$$
 K_n=\{(t,z):-a_n\leq t\leq na_n,
       \ |z|\leq R_n(na_n-t)/((n+1)a_n)\},
$$

with (6)--(7). There is no residual opening parameter. Its normalized opening is

$$
 \frac{R_n}{H_n}=\frac1{\sqrt{n+1}}.
 \tag{8}
$$

Thus a purported degeneration in an independently chosen opening is removed by the very
isotropic normalization required by the target.

## 3. Exact full boundary form

Set

$$
 d=n-1,\qquad p=\frac1{n+1},\qquad q=\frac n{n+1},
$$

and

$$
 \ell_b^2=R_n^2=\frac{(n+1)(n+2)}n,
 \qquad
 \ell_\ell^2=H_n^2+R_n^2
 =\frac{(n+1)(n+2)^2}{n}.
 \tag{9}
$$

The base has cone-measure mass $p$: it is the radial pyramid of height $a_n$ inside a cone of
height $(n+1)a_n$. The lateral surface has mass $q$. On both pieces the conditional radial law is

$$
 d\beta_d(u)=d u^{d-1}du,
 \tag{10}
$$

because both surface area and the support factor in (4) are constant along each conical piece.

For $n\geq3$, write $\omega\in S^{n-2}$ and use normalized spherical measure $d\omega$. A
boundary function is a pair $(f_b,f_\ell)$ with common seam trace

$$
 f_b(1,\omega)=f_\ell(1,\omega).
 \tag{11}
$$

The exact probability and tangential energy are

$$
\begin{aligned}
 \|f\|_{L^2(\sigma_{K_n})}^2
 &=p\int|f_b|^2d\beta_d d\omega
   +q\int|f_\ell|^2d\beta_d d\omega,\\
 \mathcal E_n(f)
 &=p\int\left(\frac{|\partial_u f_b|^2}{\ell_b^2}
        +\frac{|\nabla_\omega f_b|^2}{R_n^2u^2}\right)d\beta_d d\omega\\
 &\quad+q\int\left(\frac{|\partial_u f_\ell|^2}{\ell_\ell^2}
        +\frac{|\nabla_\omega f_\ell|^2}{R_n^2u^2}\right)d\beta_d d\omega.
 \tag{12}
\end{aligned}
$$

The relaxed domain is the closure of patchwise smooth continuous functions under the norm
$\|f\|_2^2+\mathcal E_n(f)$. Equivalently, the two $H^1$ traces agree at the seam. The base center
and lateral apex impose the usual regularity of polar Sobolev functions; no artificial Dirichlet
condition is inserted there.

There are no source, damping, or stochastic error terms in this gate. The complete burden is:

1. radial oscillation on each of the two pieces;
2. transmission of the two piece means through (11);
3. non-axisymmetric spherical modes;
4. stability of (4), (11), and (12) under smooth isotropic rounding.

## 4. Axisymmetric Sturm--Liouville problem

For axisymmetric profiles $(\psi,\phi)$, the positive operator on branch
$j\in\{b,\ell\}$ is

$$
 \mathsf L_jv
 =-\frac1{\ell_j^2}u^{1-d}(u^{d-1}v')'.
 \tag{13}
$$

At $u=0$ one takes the regular solution. At the seam one has continuity and the weighted
Kirchhoff condition

$$
 \psi(1)=\phi(1),
 \qquad
 \frac p{\ell_b^2}\psi'(1)
 +\frac q{\ell_\ell^2}\phi'(1)=0.
 \tag{14}
$$

For $\lambda>0$, the regular solutions are multiples of

$$
 u^{-\nu}J_\nu(\ell_j\sqrt\lambda\,u),
 \qquad \nu=\frac{d-2}{2},
 \tag{15}
$$

and (14) is the exact scalar determinant equation. An explicit root computation is unnecessary:
the following beta estimate bounds its first nonzero root uniformly.

### 4.1 Two exact one-dimensional estimates

For $U\sim\beta_d$, set $X=-d\log U$. Then $X$ is unit exponential. If
$h(X)=v(e^{-X/d})$, the sharp exponential Poincare inequality and
$e^{2X/d}\geq1$ give

$$
 \operatorname{Var}_{\beta_d}v
 \leq4\int|h'|^2e^{-x}dx
 \leq\frac4{d^2}\int_0^1|v'(u)|^2d\beta_d(u).
 \tag{16}
$$

Writing $m_v=\int v,d\beta_d$, Fubini and Cauchy--Schwarz also give the
endpoint trace estimate

$$
\begin{aligned}
 m_v-v(1)&=-\int_0^1v'(s)s^d ds,\\
 |m_v-v(1)|^2
 &\leq\frac1{d(d+2)}\int_0^1|v'(s)|^2d\beta_d(s).
 \tag{17}
\end{aligned}
$$

Both constants are explicit and valid for every $d\geq1$.

### 4.2 Mixture variance and the seam

Let $m_b,m_\ell$ be the two branch means and let $c$ be their common seam value. The exact
mixture identity is

$$
 \operatorname{Var}_{\pi_n}(\psi,\phi)
 =p\operatorname{Var}_{\beta_d}\psi
  +q\operatorname{Var}_{\beta_d}\phi
  +pq(m_b-m_\ell)^2.
 \tag{18}
$$

Apply (16) to the first two terms, and apply
$(m_b-m_\ell)^2\leq2|m_b-c|^2+2|m_\ell-c|^2$ followed by (17) to the last.
If

$$
 E_b=\frac p{\ell_b^2}\int|\psi'|^2d\beta_d,
 \qquad
 E_\ell=\frac q{\ell_\ell^2}\int|\phi'|^2d\beta_d,
$$

then

$$
 \operatorname{Var}_{\pi_n}(\psi,\phi)
 \leq C_b(n)E_b+C_\ell(n)E_\ell,
 \tag{19}
$$

where

$$
\begin{aligned}
 C_b(n)
 &=\frac{4(n+1)(n+2)}{n(n-1)^2}
   +\frac{2(n+2)}{(n-1)(n+1)},\\
 C_\ell(n)
 &=\frac{4(n+1)(n+2)^2}{n(n-1)^2}
   +\frac{2(n+2)^2}{n(n-1)(n+1)}.
 \tag{20}
\end{aligned}
$$

For $n\geq3$ both expressions decrease with $n$, and

$$
 C_b(3)=\frac{95}{12},
 \qquad
 C_\ell(3)=\frac{425}{12}.
 \tag{21}
$$

This sharply enough bounds the axisymmetric Sturm--Liouville problem:

$$
 \lambda_{1,\mathrm{axis}}(K_n)\geq\frac{12}{425}
 \qquad(n\geq3).
 \tag{22}
$$

The cancellation behind (22) is now explicit. The lateral length is order $n$, but
$\beta_{n-1}$ lives in a layer of $u$-width order $1/n$ at the seam. Its beta gap contributes
$(n-1)^2/\ell_\ell^2\asymp1$. The small base mass also cancels the long lateral length in the
between-piece term. Neither effect was visible from diameter alone.

## 5. Every spherical mode

Let $\bar f_j(u)$ be the spherical average of $f_j(u,\cdot)$ and put
$f_j^\perp=f_j-\bar f_j$. Radial energy and $L^2$ norm split orthogonally, and the seam traces of
$\bar f_b$ and $\bar f_\ell$ agree. The degree-one eigenvalue of $S^{n-2}$ is $n-2$, so

$$
 \int_{S^{n-2}}|f_j^\perp|^2d\omega
 \leq\frac1{n-2}\int_{S^{n-2}}
                  |\nabla_\omega f_j|^2d\omega.
 \tag{23}
$$

Since $u\leq1$, the angular part of (12) therefore gives

$$
 \|f^\perp\|_{L^2(\sigma_{K_n})}^2
 \leq\frac{R_n^2}{n-2}\mathcal E_{n,\mathrm{ang}}(f)
 \leq\frac{20}{3}\mathcal E_{n,\mathrm{ang}}(f),
 \qquad n\geq3.
 \tag{24}
$$

Equivalently, a spherical harmonic of degree $k\geq1$ adds the nonnegative potential

$$
 \frac{k(k+n-3)}{R_n^2u^2}
 \tag{25}
$$

to (13). Thus the degree-zero mode is indeed the only potentially expensive sector. Combining
(19)--(24) proves

$$
 \operatorname{Var}_{\sigma_{K_n}}f
 \leq\frac{425}{12}\mathcal E_n(f),
 \qquad n\geq3.
 \tag{26}
$$

### The dimension-two endpoint

For $n=2$, (6)--(9) show that $K_2$ is an equilateral triangle: its base and each lateral edge
have length $2\sqrt6$. Since the origin is its incenter, (4) is uniform arclength on the perimeter,
whose total length is $6\sqrt6$. The relaxed boundary is a metric circle, hence

$$
 C_P(\partial K_2,\sigma_{K_2})
 =\left(\frac{6\sqrt6}{2\pi}\right)^2
 =\frac{54}{\pi^2}<\frac{425}{12}.
 \tag{27}
$$

This handles the $S^0$ sector without pretending that the spherical Poincare inequality (23)
applies there. Equations (26)--(27) prove (1).

## 6. Smooth, strictly convex, exactly isotropic roundings

The singular calculation is not silently substituted for the smooth target. Here is the closure
argument, including normalization.

### 6.1 A canonical smoothing and isotropic correction

Let $h_n$ be the support function of $K_n$. Smooth it by an axisymmetric approximate identity on
$SO(n)$ and add $\varepsilon$:

$$
 h^0_{n,\varepsilon}=\rho_\varepsilon*h_n+\varepsilon.
 \tag{28}
$$

A rotational average of support functions is a support function. In the distributional support
function identity, $\bar\nabla^2h+hI$ is positive semidefinite; the last term in (28) makes it
positive definite. Thus (28) defines a $C^\infty$ strictly convex body
$K^0_{n,\varepsilon}$, and $K^0_{n,\varepsilon}\to K_n$ in Hausdorff distance.

Let $c_{n,\varepsilon}$ and $\Sigma_{n,\varepsilon}$ be the barycenter and covariance of its
uniform law, and set

$$
 \widehat K_{n,\varepsilon}
 =\Sigma_{n,\varepsilon}^{-1/2}
   (K^0_{n,\varepsilon}-c_{n,\varepsilon}).
 \tag{29}
$$

Continuity of volume moments under Hausdorff convergence of convex bodies gives

$$
 c_{n,\varepsilon}\to0,
 \qquad
 \Sigma_{n,\varepsilon}\to I.
 \tag{30}
$$

Hence (29) is $C^\infty$, strictly convex, exactly isotropic, and still converges to $K_n$.
The affine correction is asymptotically the identity and cannot change a Rayleigh quotient by
more than $1+o_n(1)$.

### 6.2 Cone-measure normalization

For every smooth approximant, the divergence theorem gives

$$
 \int_{\partial\widehat K_{n,\varepsilon}}
 \langle y,\nu(y)\rangle d\mathcal H^{n-1}(y)
 =n|\widehat K_{n,\varepsilon}|,
 \tag{31}
$$

so (4) remains a probability measure without any renormalization error. Alternatively, cone
measure is the push-forward of uniform volume under radial projection. Hausdorff convergence,
with the origin uniformly interior for fixed $n$, gives uniform convergence of radial functions
and therefore weak convergence

$$
 \sigma_{\widehat K_{n,\varepsilon}}\Longrightarrow\sigma_{K_n}.
 \tag{32}
$$

Linear maps cause no hidden measure defect: radial projection commutes with an invertible linear
map, so $\sigma_{AK}=A_\#\sigma_K$ for bodies centered at the radial origin.

### 6.3 Why the seam does not become a bottleneck

For fixed $n$, the weighted tangential forms on
$\partial\widehat K_{n,\varepsilon}$ Mosco-converge to (12). A direct chart proof is short enough
to record the load-bearing points:

1. Away from a $\delta$-neighborhood of the seam and apex, the rounded boundary is a normal
   graph over the base or lateral patch, and its metric tensor, surface Jacobian, support factor,
   and tangential gradients converge uniformly.
2. The support factor is bounded above and below on all these bodies for fixed $n$, because a
   common inner ball and outer ball persist. The smoothing collars therefore carry no singular
   cone-measure density.
3. For the Mosco limsup, approximate a function in the relaxed domain by patchwise smooth
   functions with a shared seam trace. Continue it across the shrinking collar. The two traces
   differ by $O(\delta)$ at collar distance $\delta$, so the collar interpolation has bounded
   gradient and its weighted area tends to zero.
4. For the liminf, bounded collar energy and the one-dimensional Cauchy--Schwarz inequality on
   geodesics transverse to the collar force the two limiting seam traces to agree: a nonzero
   jump across width $\delta$ costs order $|\mathrm{jump}|^2/\delta$. Dropping the remaining
   nonnegative collar energy and passing on the two regular patches yields (12).
5. At the apex there is no extra junction condition for boundary dimension at least two; it is
   the ordinary polar Sobolev closure. In dimension two the same transverse estimate enforces
   periodic continuity at every rounded vertex.

Rellich compactness on the compact boundary and the min--max characterization then give

$$
 \lambda_1(\partial\widehat K_{n,\varepsilon},
           \sigma_{\widehat K_{n,\varepsilon}})
 \longrightarrow
 \lambda_1(\partial K_n,\sigma_{K_n})
 \qquad(\varepsilon\downarrow0)
 \tag{33}
$$

for each fixed $n$. Combining (1) and (33), choose the smoothing parameter for each $n$ below
its convergence threshold. This yields the diagonal family (2). The threshold is allowed to
depend on $n$; the resulting spectral constant does not.

This closure is exactly what a singular-cone refutation would also require. The seam collar is
high-conductance, not low-conductance, and cannot turn the positive cone calculation into a
vanishing mode.

## 7. Residue and first wall

### Established at prover-ready level

- the cone is centered and isotropic with no free opening parameter;
- the full cone-measure tangential form, including angular coefficients and seam trace;
- the exact weighted Kirchhoff Sturm--Liouville problem;
- the explicit all-mode bound $C_P\leq425/12$;
- the dimension-two endpoint;
- a canonical $C^\infty_+$ smoothing, exact isotropic correction, cone-measure normalization,
  and fixed-dimension Mosco passage yielding a uniformly gapped diagonal rounding family;
- applicability of the exact Kolesnikov--Milman Corollary 8 bridge.

### Remaining obligations

1. **Technical gap / certification only.** The Mosco chart argument above should be written as a
   standalone lemma or tied to a source with exactly the weighted convex-hypersurface hypotheses
   before receiving proof status. No adverse scaling or missing boundary condition remains.
2. **Needs new idea.** The first mathematical wall is no longer the right cone. It is a uniform
   seam-capacity estimate for many patches: regular-simplex facet means or the two components of
   the product decomposition. The two-edge trace estimate (17) uses a single common seam and
   does not by itself control a high-degree facet adjacency graph.
3. **Scope boundary.** Fixed-$n$ Mosco convergence gives a diagonal sequence of sharp roundings,
   which is the required singular-model kill test. This report does not claim a quantitative
   convergence rate uniform jointly in $n$ and $\varepsilon$, nor does it need one to establish
   (1)--(2).

The next exact product version, if the route is admitted, should demand a dimension-free
Poincare inequality for the piece-mean graph in

$$
 \sigma_{K\times L}
 =\frac d{d+m}(\sigma_K\otimes\lambda_L)
  +\frac m{d+m}(\lambda_K\otimes\sigma_L),
$$

with the codimension-one seam trace supplying the conductance. It must not infer this conductance
from weak Wasserstein closeness of the two components.

## 8. Fence-by-fence evasion

| Fence | Check for this argument |
|---|---|
| `obs:two-tail` | No localized cut, posterior covariance, or absolute-scale source appears. Isotropy fixes the cone geometry, and the proof controls the full static boundary form. |
| `obs:proj-ceiling` | Spherical harmonics and the two-piece seam are handled directly. No projection-law estimate is used to control quadratic chaos. |
| `obs:crude-insufficient` | There is no covariance trace or time integral. |
| `obs:relative-ceiling` | The boundary target is explicitly a stronger sufficient hypothesis for KLS, not a weak bootstrap sold as progress. This model test does not claim the all-body hypothesis. |
| `obs:circularity` | The proof uses only beta Poincare, spherical Poincare, seam trace, and convex smoothing. The Kolesnikov--Milman result is used only after the intrinsic estimate. No interior KLS or localized isoperimetric profile is inserted. |
| `obs:rank-one-refuted` | There is no cut or stochastic rank-one mode. |

The scout's warning is preserved: replacing the intrinsic Sobolev form by variance control only
for ambient Lipschitz restrictions would merely restate weak KLS up to constants and is not an
admissible proof of this candidate.

## 9. Route-control recommendation

**PROMOTE, with scope.** The right-cone kill test does not reject the mechanism. The candidate may
be registered as an open route question, provided its next gate is the regular-simplex/product
seam and the 2014 published bridge is imported. Nothing here advances the all-body question to
conditional or proved status.

Proposed one-line gate update for the orchestrator:

> The rounded isotropic right-cone test passes analytically:
> $\lambda_1(\partial K_n,\sigma_{K_n})\geq12/425$, with diagonally smooth isotropic
> roundings retaining at least $6/425$; the next falsifiable gate is a dimension-free
> facet-mean/seam-capacity estimate on regular simplices or products.

Proposed candidate ledger delta, only after the orchestrator admits the route (no proof status is
proposed):

```yaml
- id: lem:right-cone-boundary-gap
  kind: lemma
  status: open
  route: cone-boundary-spectral
  statement: >-
    For the isotropic right circular cone $K_n$, the relaxed normalized-cone-measure
    tangential form on $\partial K_n$ has Poincare constant at most $425/12$.
    Moreover, for every $n$ it admits smooth strictly convex exactly isotropic
    roundings whose Poincare constants are at most $425/6$.
```

No `proved`, `solution`, `checked_by`, or cross-route edge is proposed.

## Shared handoff envelope

```yaml
outcome: complete
artifacts:
  - research/explorations/2026-08-27-kls-route-prober-cone-boundary-spectral-w3b01.md
proposed_deltas:
  - Promote cone-boundary-spectral from unregistered scout candidate to an open registered probe.
  - Stage lem:right-cone-boundary-gap as open only after route admission; certify it through a prover and a distinct proof-checker.
  - Import the published Kolesnikov--Milman 2014 Hardy bridge if the route is admitted.
  - Replace the cone kill gate by the exact regular-simplex/product seam-capacity gate quoted above.
next_role: prover
next_prompt: |
  Turn Sections 2--6 of the cone-boundary spectral probe into one standalone proof
  dossier for lem:right-cone-boundary-gap. Verify the beta endpoint estimate, the
  mixture constants, every spherical mode, the n=2 perimeter case, and the weighted
  Mosco passage for support-function smoothings followed by exact isotropic correction.
  Do not claim the all-body cone-boundary target, do not edit route-control or ledger
  files, and make no trace-upgrade-cluster implication.
```
