---
verdict: pass
authors:
  - prove_spectral_sufficiency, unknown, 2026-08-27
reviewer: review_spectral_sufficiency_w0, unknown, 2026-08-27
fingerprints:
  solutions/prop-spectral-sufficiency.md: 207df18978ce55cabb78bce26fbd9f5350791aab99cab8e6a7031217750c67bd
  prop:spectral-sufficiency: ea0691f496347072983c1a888e0c8ecc4f03b28db8e8d27dcbb8ff0c486c1c0e
  conj:mm-spectral-occupation: faf6c8299eb2e6ec3ac6c1489b1b6541ae018312780e3afe1fd47b43d0448ee3
---

# Full-damping spectral sufficiency — independent proof review

This is a cold review of `solutions/prop-spectral-sufficiency.tex`, whose reviewed SHA-256 is
`9d391d19134dfb8d08f205d9a241600978662e4470dbaeb54fb708840c839cb9`.  The proof was
reconstructed from the dossier, current manuscript, current ledger, route controls, obstruction
registry, and the actual published sources named below.  The prover's exploration narrative was
not used as mathematical evidence.  The author and reviewer identities are distinct, and the
exploration record names only the prover as author.

## Findings

### Statement agreement and dependency closure

The dossier theorem, the ledger statement for `prop:spectral-sufficiency`, and the manuscript
question at `\label{prop:spectral-sufficiency}` agree mathematically.  The manuscript asks whether
the universal full-damping estimate in `conj:mm-spectral-occupation`, uniform through regularization,
implies a universal spectral gap.  The ledger spells out the intended fixed-function SDE,
posterior Brascamp--Lieb step, regularization limit, and the fact that no strict damping surplus is
needed.  The dossier proves this implication and adds the explicit quantitative values
$$
M_*=(1+C_0T_0)e^{C_1T_0},
\qquad
T_* = \min\{T_0,(2M_*)^{-1}\},
\qquad
C_{\mathrm P}\le \frac{2}{T_*}.
$$
Its occupation premise has exactly the manuscript coefficient one in front of the complete exact
damping term $\mathbb E\int_0^t2g_s^TA_sg_s\,ds$; it assumes neither a strict surplus nor a
dimension- or regularization-dependent constant.

The current ledger has exactly one `depends_on` edge,
`conj:mm-spectral-occupation`, and no `bounded_by`, `references`, or imported-result edge.  That
dependency is still open and occurs verbatim as the dossier's displayed hypothesis.  The proof
discharges every other step internally.  Certification therefore permits `status: conditional`
only; it does not permit `proved`, does not discharge `conj:mm-spectral-occupation`, and does not
change `conj:kls` unconditionally.

### Hypothesis accounting

The proof uses exactly the following hypotheses.

1. Universal $T_0,C_0,C_1>0$ give the full-damping occupation estimate for every normalized first
   eigenfunction on every centered isotropic member of the stated smooth strongly log-concave
   regular class, uniformly in dimension and regularization.
2. Smoothness and the Friedrichs realization supply elliptic regularity and the closed Dirichlet
   form.  Strong convexity supplies Gaussian tails, hypercontractive integrability of the
   eigenfunction, and a discrete first positive eigenvalue in the stated regular class.  Ordinary
   convexity is what is used in the terminal posterior Brascamp--Lieb step.
3. Centered isotropy makes the coordinate functions an orthonormal family in $L^2(\mu)$.
   Normalization $\mathbb E_\mu f=0$, $\mathbb E_\mu f^2=1$ fixes the initial martingale and total
   variance.  The fact that $f$ is a first positive eigenfunction is used only when the lower bound
   on its eigenvalue is identified with the Poincar\'e constant.
4. The planted signal $X$ and observation Brownian motion are independent.  This supplies the
   posterior likelihood, innovation process, and filtering martingales.
5. In the final approximation step, the limiting law is isotropic and log-concave.  Isotropy
   implies full-dimensionality and finite second moment; log-concavity is preserved by Gaussian
   convolution, Gaussian tilt, translation, and invertible affine normalization.

No used hypothesis is unstated.  The explicit finiteness clause on the occupation integrals is not
an extra KLS-strength premise: for a fixed regular law with $\nabla^2V\succeq\kappa I$, posterior
Brascamp--Lieb gives $A_t\preceq(\kappa+t)^{-1}I$, while the $L^2$ filtering martingale gives
$\int_0^T\mathbb E|g_t|^2dt\le1$.  Thus the damping integral is finite on bounded intervals, and
the asserted occupation inequality makes the source integral finite.  The explicit mean-zero
condition is automatic for a positive-eigenvalue eigenfunction but is used in the computation; it
is harmless normalization rather than a hidden premise.

### Planted posterior and fixed-function filtering

For a static signal value $x$, the likelihood of the path
$dc_s=x\,ds+dB_s^{\mathrm{obs}}$ through time $t$ is
$\exp(c_t\cdot x-t|x|^2/2)$.  Bayes' formula therefore gives exactly
$$
d\mu_t(x)=
\frac{\exp(c_t\cdot x-t|x|^2/2)}
{\int\exp(c_t\cdot y-t|y|^2/2)d\mu(y)}\,d\mu(x).
$$
The process $W_t=c_t-\int_0^ta_sds$ is a continuous observation-filtration local martingale with
quadratic covariation $[W^i,W^j]_t=\delta_{ij}t$; L\'evy's characterization makes it the innovation
Brownian motion.  Normalizing the likelihood and applying It\^o gives, for every fixed admissible
test $\phi$,
$$
d\mathbb E_t\phi=\operatorname{Cov}_{\mu_t}(\phi,X)\cdot dW_t.
$$
In particular, $dm_t=g_t\cdot dW_t$ and $da_t=A_t\,dW_t$.  This is a fixed-integrand formula:
$f$ is the original eigenfunction and is not replaced by a posterior eigenfunction.

For $r_t=\mathbb E_t(fX)$, product It\^o gives the drift
$d[m,a]_t=A_tg_t\,dt$.  Componentwise, the remaining stochastic coefficient is
$$
\operatorname{Cov}_t(fX_i,X_j)-m_t(A_t)_{ij}-a_{t,i}(g_t)_j
=\mathbb E_t[(f-m_t)(X_i-a_{t,i})(X_j-a_{t,j})]
=(H_t)_{ij}.
$$
Hence the tensor orientation, sign, and drift coefficient in the dossier are exact:
$$
dg_t=H_t\,dW_t-A_tg_t\,dt.
$$

The unbounded-test passage is justified in the stated regular class.  Strong convexity gives all
coordinate moments.  The Bakry--\'Emery hypercontractive estimate, together with
$P_sf=e^{-\lambda s}f$, puts $f$ in every finite $L^p(\mu)$, so $f$ multiplied by each coordinate
polynomial used above has the necessary $L^2$ integrability.  Bounded truncation and stopping
therefore give the filtering identities first on a bounded core.  The assumed finite source
quadratic variation and nonnegative dissipative drift allow removal of the stops.  More
explicitly, BDG applied to the stopped equation bounds
$\mathbb E\sup_{s\le t}|g_s|^2$ by a constant times
$|g_0|^2+\mathbb E\int_0^t\|H_s\|_{\mathrm{HS}}^2ds$; this makes the stochastic term a true
martingale and preserves the energy equality rather than only a one-sided limit.

### Exact damping cancellation and constants

It\^o's formula applied to the checked SDE gives
$$
q(t)=|g_0|^2+
\mathbb E\int_0^t\bigl(\|H_s\|_{\mathrm{HS}}^2-2g_s^TA_sg_s\bigr)ds,
\qquad q(t)=\mathbb E|g_t|^2.
$$
Centered isotropy makes $X_1,\ldots,X_n$ orthonormal in $L^2(\mu)$, and Bessel's inequality gives
$|g_0|^2=\sum_i|\langle f,X_i\rangle|^2\le1$.  Substitution of the occupation hypothesis cancels
the entire damping integral with coefficient one and leaves exactly
$$
q(t)\le1+C_0t+C_1\int_0^tq(s)ds.
$$
There is no discarded negative remainder and no hidden requirement that the damping coefficient
be strictly smaller than one.

For the nondecreasing function $a(t)=1+C_0t$, integral Gronwall gives
$$
q(t)\le a(t)+C_1\int_0^te^{C_1(t-s)}a(s)ds
\le a(t)e^{C_1t}
\le(1+C_0T_0)e^{C_1T_0}=M_*
$$
on $[0,T_0]$.  Thus the dossier's stated constant is valid (slightly nonoptimal but explicit) and
has the required quantifier order.

### Terminal variance and Brascamp--Lieb

Because $m_t=\mathbb E[f(X)\mid\mathcal F_t^{\mathrm{obs}}]$ is an $L^2$ martingale with
$dm_t=g_t\cdot dW_t$, It\^o isometry and total variance give
$$
\mathbb E\operatorname{Var}_{\mu_t}(f)
=1-\mathbb Em_t^2
=1-\int_0^tq(s)ds.
$$
The definition of $T_*$ therefore yields
$\mathbb E\operatorname{Var}_{\mu_{T_*}}(f)\ge1-T_*M_*\ge1/2$.

The posterior potential is $V_t=V-c_t\cdot x+t|x|^2/2$, so
$\nabla^2V_t\succeq tI$.  Brascamp--Lieb, extended from compactly supported smooth tests to the
posterior form domain, gives
$$
\operatorname{Var}_{\mu_t}(f)\le t^{-1}\mathbb E_t|\nabla f|^2.
$$
The test is again the fixed original $f$.  The conditional-law tower property gives
$\mathbb E\mathbb E_t|\nabla f|^2=\mathbb E_\mu|\nabla f|^2$, and the Friedrichs form identity
gives $\mathbb E_\mu|\nabla f|^2=\langle f,-Lf\rangle=\lambda$.  Consequently
$1/2\le\lambda/T_*$ and $\lambda\ge T_*/2$.  Compact resolvent and connected positive density
identify the first positive eigenvalue with $C_{\mathrm P}(\mu)^{-1}$, proving the regular-law
bound $C_{\mathrm P}(\mu)\le2/T_*$.

### Smooth strongly convex approximation

Let $\nu$ be an arbitrary isotropic log-concave law.  Gaussian convolution
$\rho_\varepsilon\,dx=\nu*N(0,\varepsilon I)$ is positive, smooth, and log-concave, and the
coupling $X\leftrightarrow X+\sqrt\varepsilon G$ gives
$W_2(\nu*\gamma_\varepsilon,\nu)\le\sqrt{n\varepsilon}$.

For fixed $\varepsilon$, the tilted law with density proportional to
$e^{-\delta|x|^2/2}\rho_\varepsilon(x)$ converges to $\rho_\varepsilon(x)dx$ in $W_2$ as
$\delta\downarrow0$.  This does not rest on weak convergence alone: dominated convergence gives
weighted total-variation convergence with weight $1+|x|^2$; coupling the common mass identically
and the two residual masses independently makes the residual quadratic transport cost tend to
zero.  The stated diagonal choice therefore produces $\widetilde\nu_j\to\nu$ in $W_2$.

Gaussian differentiation has the checked sign and scale
$$
\nabla^2(-\log\rho_\varepsilon)(y)
=\varepsilon^{-1}I-\varepsilon^{-2}
\operatorname{Cov}(X\mid X+\sqrt\varepsilon G=y).
$$
Log-concavity makes the left side positive semidefinite, while positivity of conditional
covariance gives its upper bound by $\varepsilon^{-1}I$.  Hence the tilted potential is smooth,
$\delta$-strongly convex, and has bounded Hessian.

The compact-resolvent claim is also valid.  Under the ground-state transform, $-L$ becomes
$-\Delta+Q$ with
$$
Q=\frac14|\nabla U|^2-\frac12\Delta U.
$$
Strong convexity gives $|\nabla U(x)|\ge\delta|x|-|\nabla U(0)|$, and the upper Hessian bound keeps
$\Delta U$ bounded above.  Thus $Q(x)\to+\infty$.  After adding a harmless constant to the form,
bounded form-energy makes the $L^2$ mass uniformly small outside a large ball, while Rellich
compactness applies inside the ball; the form-domain embedding is compact, so the Friedrichs
resolvent is compact.  This directly verifies the spectral criterion used by the dossier.

$W_2$ convergence implies convergence of means and covariance matrices, so
$b_j\to0$ and $\Sigma_j\to I$.  Translation and whitening by $\Sigma_j^{-1/2}$ preserve smooth
strong convexity and the upper Hessian bound; repeating the preceding confining-potential argument
gives compact resolvent after whitening.  Coupling the pre-whitened variables with the limit and
using $\Sigma_j^{-1/2}\to I$ proves $\nu_j\to\nu$ in $W_2$.  Thus every $\nu_j$ belongs to the
regular isotropic class in the premise.

The premise is applied separately to a first eigenfunction of each $\nu_j$, yielding the same
Poincar\'e inequality
$$
\operatorname{Var}_{\nu_j}(h)
\le\frac2{T_*}\int|\nabla h|^2d\nu_j
$$
for every $j$.  No eigenfunction is selected for convergence.  For each fixed
$h\in C_c^\infty(\mathbb R^n)$, the three functions $h,h^2,|\nabla h|^2$ are bounded continuous,
so weak convergence passes this uniform inequality directly to $\nu$.

The final domain closure is sound.  For a locally Lipschitz $h$ of finite energy, first apply value
truncation $T_Mh$, then multiply by spatial cutoffs $\chi_R$ with
$|\nabla\chi_R|=O(R^{-1})$, and finally mollify the compactly supported Lipschitz function.  The
value truncation decreases the gradient almost everywhere.  For fixed $M$, the cutoff energy is
the original truncated energy plus a term $O(M^2R^{-2})$ and a cross term tending to zero by
Cauchy--Schwarz.  Absolute continuity of a full-dimensional log-concave law and bounded gradients
justify dominated convergence under mollification.  Finally, the double-integral identity
$\operatorname{Var}(u)=\frac12\iint(u(x)-u(y))^2d\nu(x)d\nu(y)$ and Fatou pass from $T_Mh$ to $h$
even before its variance is known finite.  Infinite gradient energy is vacuous.  This proves the
claimed Poincar\'e inequality on the full locally Lipschitz domain.

### KLS fences

The ledger node has no formal `bounded_by` edge.  Every registered obstruction and every adjacent
spectral-route warning was nevertheless checked.

- `rem:two-tail-slice-bounds`: no cut, slice, excess, or slice-wise Stein estimate occurs.  The proof uses the
  explicitly assumed function-aware occupation estimate.
- `rem:projection-ceiling`: no tensor estimate is inferred from radial or projection-only tests.  The
  full oriented tensors $H_t$ and $A_t$ enter only through the assumed occupation inequality and
  the exact SDE.
- `rem:crude-insufficient`: no crude covariance integral $\Xi_T$ or logarithmic bootstrap is used.
- `rem:relative-ceiling`: no all-measure relative covariance occupation bound is inserted as a
  supposedly weaker premise.
- `rem:profile-circularity`: no localized isoperimetric profile, changing balanced competitor family, or
  Cheeger lower bound is used in the spectral argument.
- `rem:single-coordinate-cuts`: no product-cut counterexample or fixed-coordinate source-budget claim is
  made.
- The spectral route's main unwhitening fence is respected: the proof does not derive the
  occupation estimate by multiplying a whitened tensor estimate by covariance norms.  It consumes
  the exact oriented damping $g_t^TA_tg_t$ and leaves `conj:mm-spectral-occupation` open.
- `prop:covariance-spike` is not contradicted.  No pathwise or expected operator-norm control of
  $A_t$ on a universal interval is claimed; terminal Brascamp--Lieb is applied only to the fixed
  eigenfunction and with its sharp $t^{-1}$ scale.
- The false truncated-exponential direct-unweighting shortcut is not used.  Neither a universal
  Lipschitz Gaussian transport nor a covariance-preserving needle reduction appears.
- No implication among `conj:trace-upgrade`, the high-rank part of `conj:stein-weighted`, `conj:product-alignment`, or
  CMH gate zero is asserted.  The deterministic CMH route is outside the proof.
- The dossier does not invoke the unreviewed Letwin QCTS preprint, any Klartag--Lehec preprint
  window, or any numerical artifact.

### Citation debt and mechanical validation

The non-elementary named analytic inputs were checked against published sources.

- The inverse-Hessian variance inequality is Brascamp--Lieb, *Journal of Functional Analysis* 22
  (1976), DOI `10.1016/0022-1236(76)90004-5`, a published source already represented by
  `BrascampLieb1976`.  The exact constant-one form used here is also stated as equation (1.3) in
  the published Carlen--Cordero-Erausquin--Lieb paper, *Ann. Inst. H. Poincar\'e Probab. Statist.*
  49 (2013), DOI `10.1214/11-AIHP462`.
- The curvature-to-hypercontractivity step is Bakry--\'Emery, *S\'eminaire de Probabilit\'es XIX*
  (1985), pp. 177--206, a published Springer Lecture Notes contribution represented by
  `BakryEmery1985`.  Its $\Gamma_2$ criterion and hypercontractive conclusion give the only fact
  needed here: a strongly log-concave eigenfunction lies in every finite $L^p$.
- Preservation of log-concavity under Gaussian convolution is the published
  Pr\'ekopa--Brascamp--Lieb theorem.  The $W_2$ and compact-resolvent passages were reconstructed
  directly above, so no unreviewed source is being used as a premise.

There is no preprint dependency or numerical evidence.

From `solutions/`,

```text
latexmk -g -pdf -outdir=../build prop-spectral-sufficiency.tex
```

completed successfully and produced a four-page PDF.  The TeX log has only the five expected
standalone unresolved manuscript references (`conj:mm-spectral-occupation`,
`prop:spectral-sufficiency`, `subsec:spectral-sde`, and `conj:kls`, with the first occurring
twice); there are no TeX errors, overfull boxes, underfull boxes, or package warnings.  Forced
Biber execution reports only that the dossier contains no citations.  Before this review was
added, `python3 research/check_ledger.py` reported 0 errors.

## Corrections

None.

## Exclusions

This review certifies only the conditional full-damping sufficiency bridge and its explicit
constant.  It does not prove or review `conj:mm-spectral-occupation`, a whitened tensor estimate, an
unwhitening or high-incidence occupation mechanism, any Letwin or Klartag--Lehec preprint result,
an operator-norm covariance bound, a trace-upgrade-cluster implication, a CMH statement, or an
unconditional proof of KLS.  It certifies no convergence of eigenfunctions and no numerical
artifact.  Updating the dossier header, ledger status, certification pointers, manuscript prose,
or route controls is outside this reviewer's write surface.
