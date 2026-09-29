---
verdict: pass
authors:
  - /root/prove_conditional_fiber_structure_w3
reviewer: /root/review_conditional_fiber_structure_w3
fingerprints:
  solutions/conditional-fiber-frame-structure.md: 6c960a309afee30be04a30c3f4c6bf3a5b5de8b526771b18e7333ab5b60947a6
  lem:conditional-fiber-form: 165238918db5e698e1b4b0515048915581b3d87aeb43c4b46bcdd41f468e878b
  thm:cmh-1d: 20ca97481f8d3f33bab114618adc59596740cec2d34e37ad9c5c8ec1b9fa9904
  prop:conditional-fiber-root-obstruction: e0a5f377615350c463031a1921a94c7ec6000a2e4e456454a91ede6be4f239e0
---

# Conditional-fiber form structure and simplex root obstruction — independent review

## Scope and immutable dossier

This is a cold line-by-line review of
`solutions/conditional-fiber-frame-structure.tex` at SHA-256
`4a2adf954edf5b51f80e4f61787a5fd57c374e04144de598003635fab21c69b8`.
The certifying scope is exactly `lem:conditional-fiber-form` and
`prop:conditional-fiber-root-obstruction`.

## Findings

### Statement agreement and hypotheses

The pinned dossier, the current ledger statements, and the statements at
`lem:conditional-fiber-form` and `prop:conditional-fiber-root-obstruction` in
`modules/kls/45-conditional-fiber-frame.tex` agree mathematically. In particular:

- the structural construction assumes a full-dimensional probability with a Borel density and
  finite second moment;
- the tight-frame identity is $d\int\theta\theta^T\,d\rho=I_d$;
- log-concavity is assumed only for the factor-$4$ gradient comparison;
- $\mathcal D_{\mu,\rho}(a\cdot x)=|a|^2$ holds before isotropy, while the corresponding
  Rayleigh quotient equals one only when $\operatorname{Cov}(\mu)=I_d$;
- the Gaussian and product conclusions assert a form gap of one, not merely an upper or lower
  estimate; and
- the root proposition concerns only the fixed even $A_{m-1}$ root frame.

The hypotheses actually used are the density and finite second moment for the canonical line
disintegration and linear $L^2$ calibration; the tight-frame identity for the linear and
gradient identities; log-concavity for the one-dimensional factor-$4$ input; isotropy for the
linear Rayleigh quotient; Gaussianity for the chaos argument; independence, centering, unit
variance, and densities for the standardized-product calibration; and the flat Dirichlet law
and fixed root frame for the simplex calculation. Evenness is part of the route's admissible-frame
definition but is not needed in the structural proof once the tight-frame identity is assumed.
Likewise, under the stated ambient-density hypothesis, “full-dimensional” is redundant but
harmless. These are sharpening opportunities, not defects.

Neither certified node has a `bounded_by` edge. Thus there is no obstruction premise to
discharge. The proof nevertheless respects the route fence: the factor-$4$ inequality runs from
the conditional-fiber form to the gradient form, so a lower form gap is sufficient for KLS but
is not claimed to follow from or be equivalent to KLS.

### Disintegration, versions, and the maximal form

The incidence bundle is Borel. Countably many Borel orthonormal-frame charts on the sphere give
a measurable kernel of Lebesgue measures on $\theta^\perp$, and parameterized Tonelli applied to
$(\theta,z,t)\mapsto r(z+t\theta)$ gives jointly measurable normalizers and moment numerators.
For the signed first moment, the printed truncation sentence is read through the positive and
negative parts; finite second moment makes both parts finite on almost every relevant fiber.

For every fixed $\theta$,

$$
 \int_{\theta^\perp}\int_{\mathbb R}t^2r(z+t\theta)\,dt\,dz
 =\int (x\cdot\theta)^2\,d\mu(x)<\infty.
$$

Hence the nonnormalizable or nonfinite-moment fibers are null for $\bar\mu_\theta$. A good
conditional law has a Lebesgue density and cannot have zero variance. The zero-weight fallback
therefore changes no energy while making all versions total and measurable.

If two ambient density representatives agree Lebesgue almost everywhere, orthogonal Fubini
shows that their fiber data agree for $\bar\mu_\theta$-almost every $z$, for every fixed
$\theta$; integrating in $\rho$ proves density-version independence. The same disintegration
applied to the disagreement set of two representatives of $f\in L^2(\mu)$ proves that the form
depends only on the $L^2(\mu)$ class. Thus the maximal domain is well defined.

### Closed Dirichlet form and generator

For fixed $\theta$, conditional expectation $P_\theta$ is the orthogonal projection onto
functions measurable with respect to $P_{\theta^\perp}X$. The inverse conditional variance
$w_\theta$ is measurable with respect to that same sigma-field, so it commutes with
$P_\theta$. Therefore the directional energy is

$$
 \|w_\theta^{1/2}(I-P_\theta)f\|_2^2.
$$

The multiplication operator is closed, and composition with the bounded projection
$I-P_\theta$ remains closed by the convergence argument printed in the dossier. Joint
measurability then defines the direct-integral operator
$Tf(\theta,x)=\sqrt d\,w_\theta^{1/2}(I-P_\theta)f(x)$. If $f_n\to f$ and $Tf_n\to G$, a
subsequence converges in the fiber $L^2(\mu)$ space for almost every $\theta$; directional
closedness identifies $G=Tf$. This verifies closedness on the stated maximal domain.

For a globally Lipschitz $f$, the independent-copy identity on each fiber gives

$$
 \operatorname{Var}(f(z+T\theta))
 \le \operatorname{Lip}(f)^2\operatorname{Var}(T).
$$

Thus $C_c^\infty(\mathbb R^d)$ lies in the domain and is dense in $L^2(\mu)$. Polarization gives
the symmetric pair-jump representation with the printed factor $d/2$; Cauchy--Schwarz makes
the bilinear integral absolutely convergent. Normal contractions reduce every pairwise
difference, proving the Markov property. Constants have zero energy, so the associated
self-adjoint Markov semigroup is conservative and reversible.

On the stated sufficient Bochner domain, set
$h_\theta=w_\theta(I-P_\theta)f$. Truncating $w_\theta$, commuting the truncations through
$P_\theta$, and passing in $L^2$ proves $P_\theta h_\theta=0$. Consequently, for every form-domain
$g$,

$$
 \langle w_\theta^{1/2}(I-P_\theta)f,
          w_\theta^{1/2}(I-P_\theta)g\rangle
 =\langle h_\theta,g\rangle.
$$

Strong measurability and $\int\|h_\theta\|_2\,d\rho<\infty$ justify the Bochner integral and
identify $A_{\mu,\rho}f=d\int h_\theta\,d\rho$. The same bound implies joint $L^1$ integrability,
so Fubini gives the displayed pointwise signed-update formula almost everywhere. No step
integrates the raw total rate $d\int w_\theta(x)\,d\rho(\theta)$, which may indeed be infinite.
The dossier correctly makes no claim about the full operator domain or a literal finite-rate
jump process.

### Factor-$4$ bridge and calibrations

Every good fiber of a log-concave density is a one-dimensional log-concave probability. The
certified dependency `thm:cmh-1d` supplies

$$
 \operatorname{Var}_{\mu_{\theta,z}}(g)
 \le 4\sigma_\theta^2(z)\int |g'|^2\,d\mu_{\theta,z}.
$$

This dependency is currently `proved` with an independent passing proof review; no open or
preprint-unreviewed premise enters the present nodes. Applying it to line restrictions and using
the tight-frame identity gives exactly
$\mathcal D_{\mu,\rho}[f]\le4\int|\nabla f|^2\,d\mu$. Hence a form-gap constant $C$ yields
$C_P(\mu)\le4C$ with the correct direction.

For $f_a(x)=a\cdot x$, the conditional variance on a good fiber is
$(a\cdot\theta)^2\sigma_\theta^2$, so tight-frame averaging gives
$\mathcal D[f_a]=|a|^2$. Only under isotropy does this also equal $\operatorname{Var}(f_a)$.

For the standard Gaussian, conditional expectation on the $r$th Wiener chaos is
$Q_\theta^{\otimes r}$ with $Q_\theta=I-\theta\theta^T$. Since its range is contained in the
range of $Q_\theta\otimes I^{\otimes(r-1)}$, the loss dominates the first-leg projection. The
tight-frame average of that projection is the identity, so every nonconstant chaos has energy at
least its variance. The energy is at most $d$ times the variance, so the full form domain is
$L^2$; a linear chaos attains quotient one. Thus every admissible Gaussian frame has gap exactly
one.

For independent centered variance-one density factors, the coordinate frame reduces the form
to the sum of the coordinate conditional variances. Martingale variance tensorization
(equivalently Efron--Stein) gives $\operatorname{Var}(f)\le\mathcal D(f)$, and nonconstant linear
tests attain equality. The product gap is therefore exactly one.

### Simplex root constants and cap test

For $P\sim\operatorname{Dir}(1,\ldots,1)$,
$\operatorname{Cov}(P)=[m(m+1)]^{-1}P_{\mathbf1^\perp}$, so
$X=\sqrt{m(m+1)}(P-m^{-1}\mathbf1)$ is isotropic on the $(m-1)$-dimensional space
$H_0$. The identity

$$
 \sum_{i<j}(e_i-e_j)(e_i-e_j)^T=mP_{H_0}
$$

and the two orientations of every root give
$(m-1)\int\theta\theta^T\,d\rho_{\rm root}=I_{H_0}$.

Conditioning on all coordinates outside $(i,j)$ and on $s=P_i+P_j$, Dirichlet neutrality makes
$P_i/s$ uniform on $[0,1]$. The isotropically scaled root coordinate is uniform on
$[-R_ms/\sqrt2,R_ms/\sqrt2]$, with variance $R_m^2s^2/6$. Combining its reciprocal with the
outer factor $m-1$ and total unordered-root mass $2/[m(m-1)]$ gives exactly

$$
 \mathcal D_{\rm root}[f]
 =\frac{12}{m^2(m+1)}\sum_{i<j}
   \mathbb E\frac{\operatorname{Var}_{ij}(f)}{(P_i+P_j)^2}
 =\frac{12}{m+1}\sum_{i<j}
   \mathbb E\frac{\operatorname{Var}_{ij}(f)}{(\eta_i+\eta_j)^2}.
$$

The marginal $P_1\sim\operatorname{Beta}(1,m-1)$ gives
$p_{m,\varepsilon}=(\varepsilon/m)^{m-1}$. Only the $m-1$ pairs incident to coordinate $1$
can change the cap indicator. For such a pair, with
$S_{1j}=\eta_1+\eta_j$ and $q_{1j}=\mathbb P(A\mid\mathcal F_{1j})$,
$\operatorname{Var}_{1j}(\mathbf1_A)\le q_{1j}$. Truncating the possibly singular
$S_{1j}^{-2}$ before applying the tower property gives

$$
 \mathbb E[S_{1j}^{-2}\operatorname{Var}_{1j}(\mathbf1_A)]
 \le \mathbb E[S_{1j}^{-2}\mathbf1_A]
 \le \frac{p_{m,\varepsilon}}{(m-\varepsilon)^2}.
$$

This proves finite energy and hence membership of the centered indicator in the maximal domain.
Division by $p_{m,\varepsilon}(1-p_{m,\varepsilon})$ gives exactly the manuscript and ledger
Rayleigh bound. Letting $\varepsilon\downarrow0$ yields

$$
 \operatorname{gap}(\mathcal D_{\rm root})
 \le\frac{12(m-1)}{m^2(m+1)}\le\frac{12}{m^2}.
$$

The endpoint $m=2$ is consistent: the single unoriented root resamples the full one-dimensional
simplex and the limiting bound is one.

## Corrections

During review, the ledger wording for `lem:conditional-fiber-form` was found to omit the
log-concavity qualifier on the factor-$4$ comparison. The orchestrator corrected that single
central statement. I rechecked the resulting ledger statement against the unchanged manuscript
and pinned dossier. No dossier correction was needed, and its SHA-256 remains the value recorded
above.

## Mechanical checks

- Forced standalone build:
  `cd solutions && latexmk -g -pdf -interaction=nonstopmode -halt-on-error -outdir=../build conditional-fiber-frame-structure.tex`.
  It succeeds and produces the six-page PDF. The three unresolved cross-file references are the
  expected standalone behavior allowed by `solutions/README.md`; there is no TeX error.
- `python3 research/check_ledger.py` reports 195 nodes, 675 labels, and 0 errors before the
  certification delta.
- The pinned dossier hash was recomputed after the build and is unchanged.

## Exclusions

This review does not certify `q:conditional-fiber-frame`, which remains open. In particular it
does not prove an all-frame simplex obstruction, root-frame optimality, a failure of every
permutation-invariant frame, an equivalence with KLS, or KLS itself. It does not review the
imported Sasada proposition or its normalization. It certifies the closed-form generator and the
stated sufficient Bochner-domain formula, not a characterization of the full generator domain or
a finite-rate pathwise jump construction. No numerical artifact or novelty claim is in scope.
