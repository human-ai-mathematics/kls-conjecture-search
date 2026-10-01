---
verdict: pass
authors:
  - kls_proof_audit, unknown, 2026-08-25
reviewer: kls_bootstrap_author, unknown, 2026-08-25
fingerprints:
  solutions/kls-geometry-models.md: 51f2adca44f986ee352d1f7e98544442cdd4993adff9977847a5d5f268fcc811
  lem:profile-bound: edaf5f0b76adaf78959e02db87ee943f5ff1a7a8b54831c0aa33bdfcf4d293d6
  cor:generic-degeneracy: 1103100221b4bf047150e63ccddaa04ec4c2ec9fefad01135905132ef7d93252
  prop:exact-splitting: 2e90beabe3769b62e46a73812a05ba17384dbd68c12acca434c8c621dac71b0d
  prop:persistent-splitting: 5aa02982b1ba2c12bcd728b05e39ff5096e0bec02d5b22114480ba116cc2346c
  prop:gaussian-model: 835dc58ac9d4cb324aea55003c87af159fe2427ee351779bf982b348abd92fa8
  prop:products: 85b9ec9b7b81c783e52dce9f3edce41396f581da4f7a425bd3df9031860a6c8c
  solutions/kls-product-covariance.md: a288e98ce106b7998a88685c6da2c20f161c9ba5387e88242337bffecb1723a4
  lem:block: 8a8c2e99fae755f4beed8f10c667b71bc1b5067bbf1fbe5ca6cfaed191e1555e
  thm:budget: 747881527155d39703c8dbb3a198afcd2c3686e5258ead72eb805f874e1bc196
  cor:per-direction: 41aeb34aa0f748e931a100d435bb6cbba97772f149ce25c2e089fc77974c1e43
  thm:scalar-riccati: 83fdb94d00721fdfab219b0a417b1ac815c170925d051a187929c3635241286d
  cor:single-coordinate-cuts: 2bcff88762d7f2da4e2f52f0181f2fbdc0c5ded77931063daf7352b5bab575ae
  lem:product-qcts: 93f2e2a3230253762243cd991c55f11de59b986c8daf848ecd044256ef2302eb
  cor:KI-discharged: 5ddd85d0e5ca16534f2e52aadb8a2a8b139979e5b19edb727c861d88a43243b7
  thm:KL-window: c8805f6f7be529a3a27f935a273c4a3253861fe59ebc6b52dc416a68cdd915f7
---

# KLS geometry, product, and covariance models — independent R2 audit

## Certified scope

This report certifies exactly the following eleven KLS ledger nodes:

1. `lem:profile-bound`
2. `cor:generic-degeneracy`
3. `prop:exact-splitting`
4. `prop:persistent-splitting`
5. `prop:gaussian-model`
6. `prop:products`
7. `lem:block`
8. `thm:budget`
9. `cor:single-coordinate-cuts`
10. `lem:product-qcts`
11. `cor:KI-discharged`

For every node I compared the dossier statement with its exact manuscript statement and the
current statement and dependency metadata in `research/kls/ledger.yaml`.  The scopes agree,
the headers identify the author and pending independent certification correctly, and none of
the proofs uses numerical evidence.

## Profile curvature and splitting checks

For `lem:profile-bound`, I checked the smooth, volume-constrained minimizing-branch and
twice-differentiable-profile hypotheses explicitly.  Under the manuscript's smooth
free-boundary convention, unit normal variation gives

$$
 v'(0)=P,\qquad P'(0)=\lambda P,\qquad
 P''(0)=-\mathfrak K_{\Sigma_p}+\lambda^2P,\qquad v''(0)=\lambda P.
$$

The second-order chain rule for the volume-parametrized competitor therefore cancels both
mean-curvature terms and gives
$\Psi''(p)=-\mathfrak K_{\Sigma_p}/P^2$.  Since the competitor profile is an upper barrier
tangent to $I$ at $p$, the direction $I''(p)\leq\Psi''(p)$ is correct.  All support-boundary
terms are included in $\mathfrak K=-\mathcal I(1,1)$; the proof does not silently replace a
free-boundary index form by its full-support version.

For `cor:generic-degeneracy`, symmetry and concavity give
$h_\nu=2I(1/2)$ and $\sup_{[1/3,2/3]}I\leq h_\nu/2$.  Writing
$-I''_{\mathrm{dist}}$ for the nonnegative curvature measure, the endpoint slopes satisfy

$$
 (-I''_{\mathrm{dist}})((1/3,2/3))
 \leq I'_+(1/3)-I'_-(2/3)\leq 3h_\nu.
$$

The almost-everywhere classical second derivative is the density of the absolutely continuous
part of this measure.  Integrating the pointwise profile bound consequently gives the sharper
displayed constant $3h_\nu^3/4$.  The dossier retains the manuscript's smooth-minimizer grant,
states that the conclusion concerns averaged minimizing branches, and does not transfer it to a
fixed cut followed under localization.

For `prop:exact-splitting`, the global identities
$\partial_z\nabla V=0$ and $\partial_{y_j}\partial_zV=0$ force
$V(y,z)=V_1(y)+cz$.  Tonelli factorizes the normalizing integral.  The dossier correctly rules
out $J=\mathbb R$ and, for an unbounded interval, requires a half-line, nonzero $c$, and the
decaying orientation.  In the converse direction it assumes the global split law rather than
inferring it from boundary-local curvature.  For an interior orthogonal cut, both the hypersurface
and weighted-Hessian terms vanish, while the lateral cylinder has zero support-boundary curvature
in the split direction.

For `prop:persistent-splitting`, the localization tilt separates pathwise in the two orthogonal
blocks, so the posterior remains a product and $A_t$ is block diagonal.  Conditioning an
orthogonal halfspace changes only the one-dimensional factor; hence
$\delta_t\parallel\theta$, $G_t$ is supported on
$\mathbb R\theta\otimes\mathbb R\theta$, and
$K_t=\kappa_t\theta\theta^T$.  The dossier uses the exact conclusion “rank at most one”; it
does not assert rank exactly one when $\kappa_t=0$.

## Gaussian and product-model checks

For `prop:gaussian-model`, completing the square gives
$A_t=(1+t)^{-1}I$ exactly.  For any initially balanced cut,
$B_t\preceq A_t$ and $s_t\leq1/4$ give expected stopped mass quadratic variation at most
$T/4$.  The displacement from $1/2$ to the coarse-window boundary is $1/6$, so the maximal
bound is $36(T/4)=9T$ and survival has probability at least $1/2$ for $T\leq1/18$.
Gaussian halfspaces have zero excess at every posterior.  Direct truncated-normal moments give
$r=\sigma^2\varphi(\alpha)^2/s$, and
$\varphi(\alpha)^2\leq(2/\pi)\Phi(\alpha)\Phi(-\alpha)$ yields

$$
 r\leq(2/\pi)\sigma^2,\qquad
 D=r(2\sigma^2-r)\geq(2-2/\pi)\sigma^2r>0
$$

for every nontrivial Gaussian halfspace.

For `prop:products`, the localized density factorizes for every realized tilt.  The
coordinate-variance SDE has drift $-(A_t^{(i)})^2$, so each nonnegative coordinate variance is
a supermartingale and its maximal probability is bounded by $1/\lambda$.  Tensorization,
the affine one-dimensional log-concave Poincaré bound, and the reverse Cheeger–Poincaré
comparison give
$h_{\mu_t}\geq c\lambda_{\max}(A_t)^{-1/2}$.  This proves product KLS without using the
bootstrap or any covariance-operator ceiling.

## Coordinate budget and fixed-cut scope

For `lem:block`, conditional independence proves that the mean difference vanishes outside the
coordinates on which the event depends, and both conditional covariance matrices agree outside
the corresponding block.  Thus both $G$ and $K$ have exactly the asserted block support.

For `thm:budget`, block support turns the source into a sum over only the $k$ fixed coordinate
columns.  Summing the separately certified per-direction occupation estimate gives
$\mathbb E\int_0^\infty S_tdt\leq k$.  Stopping the scalar Riccati identity first at bounded
localizers and at $t\wedge\tau$, dropping $D\geq0$, and then using Fatou gives
$\mathbb E r_{t\wedge\tau}\leq1+k$; no expectation of an unlocalized local martingale is set
to zero.  Since $d[p]_t=s_tr_tdt$, $s_t\leq1/4$, and the nested-window displacement is
$1/15$, the exit probability is at most $C_0(1+k)T$.  Taking
$T_k=[2C_0(1+k)]^{-1}$ and using the deterministic-time perimeter supermartingale yields the
claimed $c(1+k)^{-1/2}\min(p_0,q_0)$ boundary bound.  The truncation, smoothing, and perimeter
lower-semicontinuity passage preserves product and fixed-coordinate structure.

For `cor:single-coordinate-cuts`, setting $k=1$ gives the total source budget and boundary conclusion.
The pointwise indicator bound at a deterministic level gives expected occupation at most
$2/L^2$.  The dossier explicitly restricts the result to a cut and coordinate chosen before
localization.  It neither permits a pathwise adaptive choice nor claims the literal
interval-by-interval all-cut Carleson estimate.

## Product quadratic chaos and the published covariance input

For `lem:product-qcts`, centering and independence make every cross-covariance in the diagonal
and unordered off-diagonal expansion vanish.  Consequently

$$
 \operatorname{Var}(Y^TMY)
 =\sum_iM_{ii}^2\operatorname{Var}(Y_i^2)
  +4\sum_{i<j}M_{ij}^2\sigma_i^2\sigma_j^2.
$$

The one-dimensional fourth-moment estimate gives
$\operatorname{Var}(Y_i^2)\leq(C_4-1)\sigma_i^4$.  Since the weighted Hilbert–Schmidt norm has
off-diagonal coefficient two when written over unordered pairs, the exact universal choice is
$C_*=\max\{C_4-1,2\}$.  Scaling each coordinate shows that the same proof applies to every
centered product posterior.

For `cor:KI-discharged`, I checked the cited primary input against
Klartag–Lehec, arXiv:2406.01324v2, Theorem 61.  It is exactly the sup-over-time estimate

$$
 \mathbb P\!\left(\sup_{0\leq s\leq t}\|A_s\|_{\mathrm{op}}\geq2\right)
 \leq e^{-1/(Ct)},\qquad t\leq(C\log^2n)^{-1}.
$$

At fixed time the bad event is contained in this sup event, and the Brascamp–Lieb cap is
$\|A_t\|_{\mathrm{op}}\leq t^{-1}$.  Therefore
$\mathbb E\|A_t\|_{\mathrm{op}}\leq2+t^{-1}e^{-1/(Ct)}$; with
$u=(Ct)^{-1}$ the second term is $Cu e^{-u}\leq C/e$.  Together with $A_0=I$ and the harmless
bounded-dimension adjustment, this is precisely `ass:KI` with exponent $C_2=2$.  No fixed-time
substitute and no conditional Letwin input is used.

## Compilation and exclusions

Both dossiers compile standalone with
`latexmk -pdf -interaction=nonstopmode -halt-on-error` from `solutions/`:

- `/tmp/kls-geometry-audit/kls-geometry-models.pdf`
- `/tmp/kls-product-audit/kls-product-covariance.pdf`

Both commands returned exit code 0.  The remaining undefined references are the expected links
to labels in other manuscript subfiles.

This audit certifies only the eleven nodes enumerated above.  It does not certify an inverse
zero-curvature-to-splitting theorem, control of the dynamically tracked cut by the averaged
profile branch, adaptive single-coordinate refutations, the universal all-cut Carleson estimate,
or the conditional $1/\log n$ covariance window.
