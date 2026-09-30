---
verdict: pass
authors:
  - /root/prove_mm_weighted_source
reviewer: /root/review_mm_weighted_source_w0
fingerprints:
  solutions/lem-mm-time-weighted-fixed-source.md: 50465a9ec4e4cbe3fabcf21230d2277a454b28ad44fa888fee2605ae7d414b20
  lem:mm-time-weighted-fixed-source: 661b4f05678efc9391f1738433880ef1c5188f8b10291ebbe2b7f9aa5cedeb46
---

# Time-weighted fixed-function source budget — independent proof review

This is a cold review of `solutions/lem-mm-time-weighted-fixed-source.tex`, whose reviewed
SHA-256 is `ad701ce42c7154ab803ca0a74a376bda6c41fc2e33132eb2f7689aebeeadaddc`.
The proof was reconstructed from the dossier, manuscript, ledger, route controls, obstruction
registry, and primary literature; the prover's narrative was not used as mathematical evidence.
The author and reviewer identities are distinct.

## Findings

### Statement agreement and dependency closure

The dossier theorem, the ledger statement for `lem:mm-time-weighted-fixed-source`, and the
manuscript lemma at `\label{lem:mm-time-weighted-fixed-source}` agree mathematically.  They have
the same curvature hypothesis $\nabla^2V\succeq\kappa I$ with $\kappa\ge0$, the same fixed-test
posterior quantities $g_t,H_t,A_t$, the same quantifier $T>0$, and exactly the same constants and
signs in

$$
\mathbb E\int_0^T(\kappa+t)\|H_t\|_{\mathrm{HS}}^2\,dt
+2\mathbb E\int_0^T
\bigl(|g_t|^2-(\kappa+t)g_t^TA_tg_t\bigr)\,dt
\le \operatorname{Var}_\mu(f)-\kappa|g_0|^2.
$$

All three surfaces also retain precisely one time weight in the $\kappa=0$ infinite-horizon
consequence and disclaim an unweighted initial-layer estimate.  Writing the probability as
$e^{-V}dx$ in the manuscript and as $Z^{-1}e^{-V}dx$ in the dossier differs only by an additive
normalization of $V$.  The manuscript's phrase "for which the posterior identities are
justified" and the ledger's word "admissible" are made precise, rather than narrowed, by the
dossier's proof that every $f\in L^2(\mu)$ is allowed.  The dossier's weighted-$L^2$ membership
and nonnegativity assertions are consequences of the same estimate and covariance cap.

The node is currently `open` and has no `depends_on`, `bounded_by`, `references`, `solution`,
`checked_by`, or `review` field.  It also has no incoming formal edge.  Thus its dependency
closure is empty: no open assumption, conditional node, imported preprint, or numerical artifact
enters the proof.  Subject to this certification, the node may become unconditionally `proved`.

### Hypothesis accounting

The proof uses the following hypotheses.

1. The smooth density and $\nabla^2V\succeq\kappa I$, $\kappa\ge0$, give a convex initial
   potential and posterior curvature $\nabla^2V+tI\succeq(\kappa+t)I$.
2. The planted observation is $c_t=tX+B_t^{\mathrm{obs}}$, with $B^{\mathrm{obs}}$ independent
   of $X$; this supplies the Bayes likelihood, innovation Brownian motion, and filtering
   martingales.
3. The test $f$ is fixed before observing the channel and belongs to $L^2(\mu)$.  Its fixedness
   prevents any adapted-test correction, while square integrability supplies the martingale
   closure and terminal variance budget.
4. The finite horizon $T>0$ makes the weighted Hilbert space finite-measure and permits bounded
   localization before taking expectations.
5. Finite fourth moment of the fixed law is used only to identify $H$ under the
   $C_c^\infty\to L^2$ approximation.  A full-dimensional log-concave probability has
   exponential tails, hence this moment is finite.  Here this fact needs no additional premise:
   integrability of the positive log-concave density makes a sufficiently high convex sublevel
   of $V$ bounded, and convexity along rays then gives $V(x)\ge c|x|-C$ for some $c>0$.

No centering, isotropy, eigenfunction equation, Letwin input, cut hypothesis, or approximation of
the measure is used.  Smoothness is stronger than the minimal regularity one could likely impose,
and the word log-concave is redundant once the displayed Hessian lower bound with
$\kappa\ge0$ is assumed.  These are harmless sharpening opportunities, not proof defects.  No
used hypothesis is unstated.

### Posterior, innovation, and the fixed-function SDE

For the signal model $dc_t=X\,dt+dB_t^{\mathrm{obs}}$, the likelihood at a fixed signal value
$x$ is
$\exp(c_t\cdot x-t|x|^2/2)$.  Bayes' formula therefore gives the displayed posterior density with
the correct signs.  With $a_t=\mathbb E[X\mid\mathcal F_t^{\mathrm{obs}}]$,

$$
W_t=c_t-\int_0^t a_s\,ds
$$

is an observation-filtration continuous local martingale with
$[W^i,W^j]_t=\delta_{ij}t$; Levy characterization makes it Brownian.  Applying Ito to the
normalized likelihood cancels the drift and yields, first for bounded tests and then by the
stated $L^2$ closure,

$$
d\mathbb E_t\phi=\operatorname{Cov}_{\mu_t}(\phi,X)\cdot dW_t.
$$

Every use on the compact smooth core is in this domain: $f$ and $fX$ are bounded, while $X$ is
square-integrable.  The later use for an $L^2$ difference is justified by martingale closure.

The tensor orientation also checks.  Componentwise,

$$
\operatorname{Cov}_t(fX,X)=H_t+m_tA_t+a_t\otimes g_t.
$$

Since $g_t=\mathbb E_t(fX)-m_ta_t$, the stochastic terms $m_tA_t$ and
$a_t\otimes g_t$ cancel under the product rule, while

$$
d[m,a]_t=A_tg_t\,dt.
$$

Consequently

$$
dg_t=H_t\,dW_t-A_tg_t\,dt,
$$

with neither a transpose nor a factor missing.

### Weighted Ito identity

Put $w_t=\kappa+t$.  From the checked SDE,

$$
d|g_t|^2
=2g_t^TH_t\,dW_t+
\bigl(\|H_t\|_{\mathrm{HS}}^2-2g_t^TA_tg_t\bigr)dt.
$$

Since $dw_t=dt$ has finite variation, the product rule gives

$$
d(w_t|g_t|^2)
=2w_tg_t^TH_t\,dW_t+
\left(w_t\|H_t\|_{\mathrm{HS}}^2
+|g_t|^2-2w_tg_t^TA_tg_t\right)dt.
$$

For
$\mathcal R_t=|g_t|^2-w_tg_t^TA_tg_t$, the drift is exactly
$w_t\|H_t\|_{\mathrm{HS}}^2+2\mathcal R_t-|g_t|^2$, as claimed.  The coefficient two, the
damping sign, and the deterministic-weight contribution are all correct.

### Brascamp--Lieb remainder and terminal cap

The posterior potential has Hessian at least $w_tI$.  Brascamp--Lieb applied to every linear
test gives

$$
w_tA_t\preceq I.
$$

When $w_t=0$ this is simply the trivial positive-semidefinite inequality; otherwise it follows
with constant one from the inverse-Hessian variance bound.  Hence

$$
\mathcal R_t=g_t^T(I-w_tA_t)g_t\ge0.
$$

The second use of the cap is distinct.  For $u_t=g_t/|g_t|$ when $g_t\ne0$, conditional
Cauchy--Schwarz gives

$$
|g_t|^2
=\operatorname{Cov}_t(f,u_t\cdot X)^2
\le v_t\,u_t^TA_tu_t
\le \frac{v_t}{w_t},
$$

and therefore $w_t|g_t|^2\le v_t$, including the zero cases by continuity/convention.  This is
valid at bounded random stopping times because the posterior coefficients have continuous
versions and the inequality is pathwise.

The named external input has no preprint debt.  Brascamp and Lieb's inverse-Hessian variance
inequality is a published 1976 *Journal of Functional Analysis* result, DOI
`10.1016/0022-1236(76)90004-5`, recorded as `BrascampLieb1976` in the repository.  Its exact form
was also checked in the published primary paper of Carlen--Cordero-Erausquin--Lieb,
*Ann. Inst. H. Poincare Probab. Statist.* 49 (2013), DOI `10.1214/11-AIHP462`, equation (1.3).
For a linear test and $\nabla^2V_t\succeq w_tI$, it gives exactly the displayed matrix cap.  The
dossier has no unreviewed external or numerical input.

### Stopping and the posterior variance budget

On the compact smooth core, log-concave exponential tails near time zero and the Gaussian factor
for positive time make all displayed posterior moments finite and continuous on compact time
intervals.  Thus the stochastic integral

$$
L_t=\int_0^t2w_sg_s^TH_s\,dW_s
$$

is a continuous local martingale with locally finite quadratic variation.  One may stop its
bracket and the absolute finite-variation integrals simultaneously.  The resulting increasing
stops make $L$ square-integrable and converge past any fixed $T$.  At
$\theta_N=T\wedge\tau_N$, expectation of the weighted Ito identity is therefore legitimate and
has exactly the dossier's signs:

$$
\mathbb E\int_0^{\theta_N}
\bigl(w_t\|H_t\|_{\mathrm{HS}}^2+2\mathcal R_t\bigr)dt
=\mathbb E[w_{\theta_N}|g_{\theta_N}|^2]
-\kappa|g_0|^2
+\mathbb E\int_0^{\theta_N}|g_t|^2dt.
$$

For compactly supported $f$, $m_t=\mathbb E[f(X)\mid\mathcal F_t^{\mathrm{obs}}]$ is a bounded
martingale and $dm_t=g_t\cdot dW_t$.  Optional isometry at the bounded stopping time and the
conditional-law identity for $\mu_{\theta_N}$ give

$$
\mathbb E m_{\theta_N}^2-m_0^2
=\mathbb E\int_0^{\theta_N}|g_t|^2dt,
\qquad
\mathbb E v_{\theta_N}=\mathbb E_\mu f^2-\mathbb E m_{\theta_N}^2.
$$

Their sum is the exact budget

$$
\mathbb E v_{\theta_N}
+\mathbb E\int_0^{\theta_N}|g_t|^2dt
=\operatorname{Var}_\mu(f).
$$

The terminal cap absorbs the stopped endpoint, yielding the claimed deterministic right-hand
side.  Since both remaining integrands are nonnegative and $\theta_N\uparrow T$, monotone
convergence removes the stopping.  No expectation of the unstopped local martingale and no
terminal uniform-integrability assertion is used.  The same terminal cap at time zero also shows
$\kappa|g_0|^2\le\operatorname{Var}_\mu(f)$, so the right-hand side is nonnegative.

### Closure from $C_c^\infty$ to $L^2(\mu)$

Smooth compactly supported functions are dense in $L^2(\mu)$ by truncation and mollification
against the positive smooth density.  For
$\delta_j=f_j-f$ and $M_t^j=\mathbb E_t\delta_j$, martingale isometry gives

$$
\mathbb E\int_0^T|g_t^j-g_t|^2dt
=\mathbb E|M_T^j-M_0^j|^2
\le\|\delta_j\|_{L^2(\mu)}^2.
$$

Thus $g^j\to g$ strongly in $L^2$.  With
$Q_t=I-w_tA_t$ satisfying $0\preceq Q_t\preceq I$,

$$
|(g_t^j)^TQ_tg_t^j-g_t^TQ_tg_t|
\le |g_t^j-g_t|\,(|g_t^j|+|g_t|),
$$

so the remainder integrals converge in $L^1$ by Cauchy--Schwarz.

The tensor identification uses no hidden moment of $f$.  Since
$a_t=\mathbb E[X\mid\mathcal F_t^{\mathrm{obs}}]$, conditional Jensen and
$(r+s)^4\le8(r^4+s^4)$ give

$$
\mathbb E|X-a_t|^4
\le8\bigl(\mathbb E|X|^4+\mathbb E|a_t|^4\bigr)
\le16\mathbb E|X|^4.
$$

Moreover,

$$
H_t^j-H_t
=\mathbb E_t[(\delta_j-\mathbb E_t\delta_j)(X-a_t)^{\otimes2}].
$$

The first centered term is bounded after taking expectation by
$\|\delta_j\|_2(\mathbb E|X-a_t|^4)^{1/2}$.  For the second, outer
Cauchy--Schwarz, conditional Jensen, and the tower property give the same bound.  Hence
$H^j\to H$ strongly in $L^1(\mathbb P\,dt)$, uniformly on each finite time horizon.

The compact-core inequality and remainder nonnegativity bound $H^j$ in
$L^2(w_t\,d\mathbb P\,dt)$.  To make the standard subsequence step explicit, choose a subsequence
realizing the liminf of the weighted norms and then a weakly convergent subsubsequence.  Because
$w_t\le\kappa+T$, the preceding convergence is also strong in
$L^1(w_t\,d\mathbb P\,dt)$; testing against bounded functions identifies the weak limit with the
displayed posterior tensor $H$.  This remains valid when $\kappa=0$, since $w_t=t>0$ for almost
every $t\in(0,T)$.  Weak lower semicontinuity, convergence of the remainder, and

$$
\operatorname{Var}_\mu(f_j)-\kappa|g_0^j|^2
\longrightarrow
\operatorname{Var}_\mu(f)-\kappa|g_0|^2
$$

then give the complete finite-horizon estimate.  Here $g_0^j\to g_0$ follows from
$X\in L^2(\mu)$.  This simultaneously proves the asserted weighted-$L^2$ membership of $H$.

### The $\kappa=0$ infinite-horizon consequence

At $\kappa=0$, remainder nonnegativity permits only the claimed weighted estimate

$$
\mathbb E\int_0^T t\|H_t\|_{\mathrm{HS}}^2dt
\le\operatorname{Var}_\mu(f).
$$

The integrand is nonnegative, so monotone convergence as $T\uparrow\infty$ proves the displayed
infinite-horizon consequence.  No step removes the factor $t$, and no conclusion about
$\int_0^\varepsilon\|H_t\|_{\mathrm{HS}}^2dt$ is inferred.

### Fences and excluded route claims

There is no formal `bounded_by` edge.  The moment-map spectral route's main fence is nevertheless
respected: the proof does not unwhiten $H_t$, replace its covariance orientation by a global
operator norm, or close the initial high-incidence occupation problem.  It retains exactly the
vanishing time weight that separates this lemma from `conj:mm-spectral-occupation`.

The six recorded KLS obstruction shapes are also untouched.

- `rem:two-tail-slice-bounds`: no cut, slice-wise excess, or absolute-scale Stein estimate occurs.
- `rem:projection-ceiling`: no radial or projection-only estimate is promoted to tensor control.
- `rem:crude-insufficient`: no crude $\Xi_T$ estimate is used as a bootstrap input.
- `rem:relative-ceiling`: no universal relative-scale covariance occupation bound is asserted.
- `rem:profile-circularity`: no localized isoperimetric profile or moving competitor family is inserted.
- `rem:single-coordinate-cuts`: no product-cut witness or adaptive alignment assertion is made.

The dossier proves neither the unweighted source estimate in `conj:mm-spectral-occupation` nor the
conditional bridge `prop:spectral-sufficiency`.  It proves no covariance occupation theorem,
regularization-uniform result for nonsmooth or lower-dimensional laws, spectral gap, Cheeger
bound, or KLS conclusion.

### Standalone build and archive validation

From `solutions/`,

```text
latexmk -g -pdf -outdir=../build lem-mm-time-weighted-fixed-source.tex
```

completed successfully and produced a four-page PDF.  The only TeX warnings are the expected
standalone unresolved manuscript references to `lem:mm-time-weighted-fixed-source` (twice) and
`conj:mm-spectral-occupation`; all dossier-internal references resolve.  Before this report was
added, `python3 research/check_ledger.py` reported 0 errors across 180 nodes.

## Corrections

None.  A future editorial pass may add a direct `\cite{BrascampLieb1976}` in the dossier and may
replace "admissible" by "arbitrary $L^2$" in the accepted statement, but the source was checked
above and neither wording point changes the proved claim.

## Exclusions

This review certifies only `lem:mm-time-weighted-fixed-source` in the immutable dossier scope
named in the front matter.  It does not certify a generic filtering identity for tests outside the
square-integrable instances actually used.  It certifies no unweighted initial-layer estimate,
no route-S occupation gate, no spectral-sufficiency implication, no approximation of the measure,
no nonsmooth or affine-support-degenerate extension, no KLS theorem, and no numerical artifact.
Updating the dossier header, manuscript, ledger, route control, bibliography, or exploration log
is outside this reviewer's write surface.
