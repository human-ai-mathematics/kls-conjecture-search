---
verdict: pass
authors:
  - /root/prove_posterior_defect_par_06
reviewer: /root/review_posterior_defect_cold_08
fingerprints:
  solutions/lem-mm-posterior-defect.md: c76f3bfde5369eb94682bc89a61bd9f2e31c170944d9492482a39356c2849e59
  lem:mm-posterior-defect: 355e6dc85e241fe8049eab66d9647ed41cb8b0f48e9ce3292c439935a75acecd
---

# Posterior eigenfunction-defect calculus — independent proof review

This is a cold review of `solutions/lem-mm-posterior-defect.tex`, whose reviewed SHA-256 is
`44288f5a817859cee3f535ae6b8da902cb72dfef504d4f3c2c4c34697d6db70f`.  The proof was
reconstructed from the dossier, ledger, manuscript, route controls, and obstruction registry;
the prover's narrative was not used as evidence.  The author and reviewer identities are
distinct.

## Findings

### Statement agreement and logical closure

The dossier theorem, the ledger statement for `lem:mm-posterior-defect`, and the manuscript lemma
at `\label{lem:mm-posterior-defect}` agree mathematically.  The manuscript's regular setting is a
smooth strongly log-concave isotropic probability, with a normalized first nonconstant
eigenfunction of $-L$; the dossier merely spells out centeredness, the normalization
$\mathbb E_\mu f=0$, $\mathbb E_\mu f^2=1$, the Friedrichs realization, and
$\nabla^2V\succeq\varepsilon I$.  Its definitions of $m_t,g_t,H_t,b_t,C_t,u_t,K_t,R_t$ and
$\rho_t$ have the same centering and tensor orientation as the manuscript.  All six conclusions,
including $\mathbb E_tR_t=\lambda m_t$ and the averaged gradient-defect estimate, occur with the
same constants and quantifiers in all three locations.

The node has no `depends_on`, `references`, or `bounded_by` field.  No external premise enters the
proof, so dependency closure is unconditional and the node may become `proved` after the
certification pointers are applied.

### Hypothesis accounting

The proof uses the following hypotheses.

1. The smooth density and Friedrichs generator give local elliptic regularity and the closed
   Dirichlet form $\mathcal E(h,k)=\mathbb E_\mu\nabla h\cdot\nabla k$.
2. Convexity of $V$ supplies the nonnegative curvature term in the weighted Bochner identity;
   strong convexity supplies Gaussian tails, hence all polynomial moments for $\mu$ and every
   posterior $\mu_t$.
3. The generator-domain eigenfunction relation $-Lf=\lambda f$, its positive eigenvalue,
   $\mathbb E_\mu f=0$, and $\mathbb E_\mu f^2=1$ supply respectively the defect equation,
   $m_0=0$, the gradient energy $\mathbb E_\mu|\nabla f|^2=\lambda$, and
   $\mathbb E_\mu(Lf)^2=\lambda^2$.
4. Independence of $X$ and $B^{\mathrm{obs}}$, together with the Brownian mean and covariance,
   supplies the planted second-moment and gradient calculations.

No used hypothesis is unstated.  Centered isotropy and the fact that $\lambda$ is specifically the
first positive eigenvalue are not used by the identities: after the stated domain and tail
conditions are imposed, the argument works for any normalized positive-eigenvalue eigenfunction.
That is harmless route-context slack and a possible later sharpening, not a defect.

### Posterior density, innovation, and filtering

For fixed $x$, the likelihood of the observation path $dc_s=x\,ds+dB_s^{\mathrm{obs}}$ is
$\exp(c_t\cdot x-t|x|^2/2)$.  Bayes' formula therefore gives exactly the displayed posterior
density.  With
$$
W_t=c_t-\int_0^t a_s\,ds,
$$
the observation-filtration drift has conditional mean zero and
$[W^i,W^j]_t=\delta_{ij}t$; Levy's characterization consequently gives an innovation Brownian
motion.  Normalizing the likelihood and applying Ito's formula cancels its drift and yields
$$
d\mu_t(x)=\mu_t(x)(x-a_t)\cdot dW_t,
\qquad
d\mathbb E_t\phi=\operatorname{Cov}_t(\phi,X)\cdot dW_t.
$$
Bounded truncation followed by stopping proves this first for bounded tests.  Conditional
expectation is an $L^2$ contraction, so it extends to $f$ and every component of $\nabla f$ with
the asserted stochastic-integral coefficients.

### Friedrichs domains and spatial cutoffs

There is no hidden boundary assumption at infinity.  For $t>0$, the posterior likelihood ratio
and that ratio multiplied by any fixed polynomial are bounded because of
$\exp(c_t\cdot x-t|x|^2/2)$.  Thus $f,\nabla f$, and
$(c_t-tx)\cdot\nabla f$ have the required posterior $L^2$ integrability; at $t=0$ these facts are
the original Friedrichs-domain and energy assumptions.  Hence $f$ is in the posterior form domain,
the distributional relation
$$
L_tf=Lf+(c_t-tx)\cdot\nabla f
$$
has an $L^2(\mu_t)$ right-hand side, and the defining representation of the Friedrichs operator
places $f$ in $D(L_t)$.  This justifies pairing against the constant and against global form-domain
tests.

Strong convexity of
$V_t=V-c_t\cdot x+t|x|^2/2$ gives every polynomial moment.  Standard compact cutoffs of a
coordinate and of a centered quadratic therefore converge to those tests in $W^{1,2}(\mu_t)$.
Closedness of the form passes the integration-by-parts identity to the limit.  Only derivatives of
the tests occur, so no upper-growth assumption on $\nabla V$ and no boundary trace is being
inserted.

The final weighted Bochner passage is also valid for the Friedrichs eigenfunction without an
unstated growth hypothesis.  One may multiply the pointwise local Bochner identity by
$\chi_R^2$, where $\chi_R$ is a compact cutoff with $|\nabla\chi_R|\lesssim R^{-1}$.  Using
$Lf=-\lambda f$ gives
$$
\int\chi_R^2\bigl(\|\nabla^2f\|_{\mathrm{HS}}^2
 +\langle\nabla^2V\nabla f,\nabla f\rangle\bigr)\,d\mu
=\lambda\int\chi_R^2|\nabla f|^2\,d\mu
-2\int\chi_R\nabla^2f(\nabla\chi_R,\nabla f)\,d\mu.
$$
Convexity and absorption first give global $L^2$ control of $\nabla^2f$; the last term then tends
to zero by Cauchy--Schwarz and the $L^2$ tail of $\nabla f$.  This proves the integrated identity
and
$$
\mathbb E_\mu\|\nabla^2f\|_{\mathrm{HS}}^2
\le \mathbb E_\mu(Lf)^2=\lambda^2.
$$

### Generator sign and the three posterior identities

The posterior generator is
$L_t=L+(c_t-tx)\cdot\nabla$, so the sign is exactly
$$
-L_tf=\lambda f-R_t.
$$
Pairing with $1$ gives $\mathbb E_tR_t=\lambda m_t$.  Pairing with
$x_i-a_{t,i}$ gives
$$
(b_t)_i=\mathbb E_t[(-L_tf)(X_i-a_{t,i})]
=(\lambda g_t-u_t)_i,
$$
and hence $\lambda g_t=b_t+u_t$.

For symmetric $D$, the centered test
$Q_D=(x-a_t)^TD(x-a_t)-\operatorname{Tr}(DA_t)$ has gradient
$2D(x-a_t)$.  With
$$
(C_t)_{ij}=\mathbb E_t[(X_i-a_{t,i})\partial_jf],
$$
the form pairing is
$2\langle D,\operatorname{sym}C_t\rangle_{\mathrm{HS}}$, whereas the defect side is
$\langle D,\lambda H_t-K_t\rangle_{\mathrm{HS}}$.  Since $H_t$ and $K_t$ are symmetric and $D$
is arbitrary, this proves
$\lambda H_t=2\operatorname{sym}C_t+K_t$.  The auxiliary $A_t$ here is the posterior covariance
already fixed by the manuscript setup; equivalently its sole occurrence is just the scalar
centering $\mathbb E_t[(X-a_t)^TD(X-a_t)]$.

### Planted cancellation and the two stochastic budgets

At the planted point,
$$
R_t(X)=(tX+B_t^{\mathrm{obs}}-tX)\cdot\nabla f(X)
=B_t^{\mathrm{obs}}\cdot\nabla f(X).
$$
The conditional-law identity and independence then give
$\mathbb E\mathbb E_tR_t^2=t\mathbb E_\mu|\nabla f|^2=t\lambda$.

Filtering $f$ gives $dm_t=g_t\cdot dW_t$.  The stopped Ito isometry and
$m_t=\mathbb E[f(X)\mid\mathcal F_t^{\mathrm{obs}}]$ imply, after $L^2$ removal of the stops,
$$
\mathbb Em_t^2=\int_0^t\mathbb E|g_s|^2\,ds.
$$
Subtracting the squared conditional mean
$(\mathbb E_tR_t)^2=\lambda^2m_t^2$ from the planted second moment proves the exact
centered-defect budget.

For $b_t=\mathbb E_t\nabla f$, the displayed orientation of $C_t$ gives componentwise
$$
db_{t,j}=\sum_i(C_t)_{ij}\,dW_{t,i},
\qquad db_t=C_t^T\,dW_t.
$$
The stopped vector Ito isometry and the $L^2$-closed martingale property give
$$
\mathbb E\int_0^t\|C_s\|_{\mathrm{HS}}^2\,ds
=\mathbb E|b_t|^2-|b_0|^2.
$$
Conditional Jensen bounds the first term by $\lambda$.  Since $R_0=\rho_0=u_0=0$, the already
proved coordinate identity gives $b_0=\lambda g_0$, producing precisely
$\lambda-\lambda^2|g_0|^2$.  In both isometries, localization brackets increase monotonically and
the stopped martingales converge in $L^2$ to conditional expectations, so no inequality is lost
when the stops are removed.

### Spatial gradient budget

Direct differentiation, including the derivative of $-tx$, gives
$$
\nabla R_t(x)=\nabla^2f(x)(c_t-tx)-t\nabla f(x).
$$
At $x=X$, the first factor is $B_t^{\mathrm{obs}}$.  Its centering makes the cross term vanish and
its covariance $tI$ gives
$$
\mathbb E\mathbb E_t|\nabla R_t|^2
=t\mathbb E_\mu\|\nabla^2f\|_{\mathrm{HS}}^2
 +t^2\mathbb E_\mu|\nabla f|^2.
$$
The checked weighted Bochner and gradient-energy identities therefore give the claimed
$t\lambda^2+t^2\lambda$ bound.

### Fences and excluded claims

Although this node has no formal `bounded_by` edge, every live route fence was checked.

- No cut or slice estimate, localized isoperimetric profile, product-cut counterexample, or crude
  covariance integral is used.  Thus `rem:two-tail-slice-bounds`, `rem:profile-circularity`,
  `rem:single-coordinate-cuts`, `rem:crude-insufficient`, and `rem:relative-ceiling` are not crossed.
- The arbitrary symmetric-matrix identity is exact integration by parts, not a dimension-free
  quadratic-chaos theorem inferred from radial or projection tests, so `rem:projection-ceiling` is
  respected.
- No posterior covariance operator norm is bounded.  No tensor is unwhitened, and no
  high-incidence occupation estimate is proved.  This respects `prop:covariance-spike` and the
  moment-map spectral route's orientation-preserving unwhitening fence.
- The false truncated-exponential variable-weight Stein shortcut is not invoked.  Neither a
  transport nor a needle mechanism is used.
- The dossier does not use `thm:letwin-qcts`, does not pass to arbitrary log-concave measures, and
  does not prove or claim `conj:mm-spectral-occupation`, `prop:spectral-sufficiency`, or KLS.

### Citation debt and mechanical validation

The dossier contains no citation and invokes no imported ledger node.  Levy characterization,
Ito isometry, the Friedrichs form representation, and weighted Bochner are standard analytic
steps and were reconstructed above rather than accepted as external premises.  There is therefore
no published/preprint classification debt and no numerical evidence.

From `solutions/`,

```text
latexmk -g -pdf -outdir=../build lem-mm-posterior-defect.tex
```

completed successfully and produced a four-page PDF.  The only TeX warnings are the two expected
standalone unresolved references to the manuscript label `lem:mm-posterior-defect`; there are no
citations.  Before this report was added, `python3 research/check_ledger.py` reported 0 errors.

## Corrections

None.

## Exclusions

This review certifies only the six posterior-defect identities and budgets in the regular setting
of the theorem.  It certifies no whitened quadratic estimate, unwhitening argument,
high-incidence occupation bound, operator-norm covariance estimate, approximation theorem for
arbitrary log-concave measures, spectral-sufficiency bridge, or KLS implication.  It neither uses
nor reviews `thm:letwin-qcts`, and it certifies no numerical artifact.  Updating the dossier
header, ledger, or manuscript status is control-plane work outside this reviewer's write surface.
