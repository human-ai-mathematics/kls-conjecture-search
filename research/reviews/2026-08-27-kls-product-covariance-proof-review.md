---
verdict: pass
authors:
  - /root/kls_proof_audit
  - /root/repair_product_dossier
reviewer: /root/review_product_w0
fingerprints:
  solutions/kls-product-covariance.md: 5c6ad1f7a7977833526828aadc086cd693b693db7e0c84f914761d930a8733c5
  lem:block: 8a8c2e99fae755f4beed8f10c667b71bc1b5067bbf1fbe5ca6cfaed191e1555e
  thm:budget: 747881527155d39703c8dbb3a198afcd2c3686e5258ead72eb805f874e1bc196
  cor:per-direction: 41aeb34aa0f748e931a100d435bb6cbba97772f149ce25c2e089fc77974c1e43
  thm:scalar-riccati: 83fdb94d00721fdfab219b0a417b1ac815c170925d051a187929c3635241286d
  prop:products: 85b9ec9b7b81c783e52dce9f3edce41396f581da4f7a425bd3df9031860a6c8c
  cor:refutation: 50f836a8a6885da08f837ec667d19b41a722b0e356f8c44acf5bd11b745a8a67
  lem:product-qcts: 93f2e2a3230253762243cd991c55f11de59b986c8daf848ecd044256ef2302eb
  cor:KI-discharged: 2411e9c586f6ecbbb44f141b7f0b3a7733942614025262b49fcebc385b3f58d5
  thm:KL-window: c8805f6f7be529a3a27f935a273c4a3253861fe59ebc6b52dc416a68cdd915f7
---

# Product coordinate budgets and covariance window — independent proof review

This is a cold review of `solutions/kls-product-covariance.tex`, whose reviewed SHA-256 is
`2173a912189b560ff4d34ed7ff1950a16f508521973b853b8cd285523896350e`. The proof was
reconstructed from the current dossier, manuscript, ledger, certified dependencies, obstruction
registry, and primary literature. The 2026-08-25 review predates these bytes and was not used as
evidence. The original author, repair author, and reviewer identities are pairwise distinct.

## Findings

### Statement agreement

The current dossier, ledger summaries, and manuscript anchors agree mathematically for all five
nodes.

- `lem:block` now assumes a finite-second-moment product law and a nontrivial
  $J$-measurable cut in all three places. They assert that $delta$ vanishes off $J$ and that
  $G,K$ are supported on $J\times J$.
- `thm:budget` assumes a product of isotropic one-dimensional log-concave factors, a fixed
  $J$-measurable cut with $|J|=k$, and $p_0\in[2/5,3/5]$. The dossier explicitly defines
  $\tau=\inf\{t:p_t\notin[1/3,2/3]\}$, matching the manuscript's coarse balanced exit time,
  and all three sources record the exact source budget, the stopped information-rate bound, and
  the boundary lower bound.
- `cor:refutation` retains $p_0\in[2/5,3/5]$, a cut and one coordinate fixed before
  localization, and a deterministic threshold. Its boundary, total-budget, and deterministic-level
  occupation conclusions match the manuscript; the ledger is a faithful concise statement of the
  refutation scope and explicitly excludes path-adaptive choices.
- `lem:product-qcts` has the same centered product, one-dimensional log-concavity, covariance
  $A$, symmetric-matrix, and weighted Hilbert--Schmidt conclusion in the dossier and manuscript.
  The ledger's pathwise phrase is the immediate application to the centered product posterior
  recorded at the end of the proof.
- `cor:KI-discharged` states precisely that the published sup-over-time covariance window and
  the Brascamp--Lieb cap discharge `hyp:KI` with $C_2=2$. The dossier makes the inherited
  range $n\ge3$ explicit; the manuscript anchor inherits exactly that range from `hyp:KI`.

The recent source synchronization is therefore complete. No current theorem is being certified
against the older, weaker statement bytes.

### Hypothesis accounting

Every hypothesis used in the five proofs is stated.

1. For `lem:block`, product independence and $J$-measurability are used for conditional
   factorization, $0<\nu(E)<1$ defines both colors, and finite second moment makes all conditional
   means and covariances finite.
2. For `thm:budget`, product structure supplies pathwise factorization, isotropy gives $A_0=I$,
   one-dimensional log-concavity supplies finite moments and posterior strong log-concavity, the
   fixed $J$ supplies a deterministic set of columns to sum, and the nested balance interval gives
   the survival margin. Part (i) is indeed stronger than the packaged theorem and needs only a
   nontrivial cut, but the full theorem uses the displayed balance hypothesis in part (iii).
3. For `cor:refutation`, the one-coordinate set and cut are fixed before the Brownian path and
   $L>0$ is deterministic. The balance hypothesis is inherited explicitly from the budget theorem.
4. For `lem:product-qcts`, centering kills every mixed covariance, independence factors the
   surviving moments, log-concavity supplies the fourth-moment bound, and symmetry of $M$ combines
   each unordered off-diagonal pair.
5. For `cor:KI-discharged`, the initial law is isotropic and log-concave, $n\ge3$, and the proof
   uses only the published Klartag--Lehec event and the posterior Brascamp--Lieb cap.

There is harmless slack but no defect: the source-budget subpart of `thm:budget` does not need the
nested balance interval, while the packaged boundary conclusion does. No used hypothesis is
unstated, and no unstated smoothness, compact-support, finite-perimeter, or Letwin premise remains.

### Block support and finite-time applicability

Write $X=(X_J,X_{J^c})$. Product structure makes $X_{J^c}$ independent of the pair
$(X_J,\mathbf 1_E)$. Conditioning on either $E$ or $E^c$ therefore leaves the entire outside
joint law unchanged and preserves its independence from $X_J$. Consequently the two conditional
outside means agree, every conditional inside--outside covariance is zero, and the two outside
covariance blocks agree. Thus $\delta_i=0$ off $J$ and $G$ is supported on $J\times J$; the same
then holds for $K=G+(q-p)\delta\delta^T$.

If $0<\nu(E)<1$, conditional second moments are bounded by the unconditional second moment divided
by the corresponding color mass. Hence the two added hypotheses are sufficient for every quantity
in the statement. Along localization, the likelihood is strictly positive and finite relative to
the initial product law at every finite time. The initial nontrivial cut therefore satisfies
$0<p_t<1$, and the Gaussian factor gives finite posterior moments. The block lemma is legitimately
available at each time.

### Product persistence and the exact source budget

For each realized localization parameter $c_t$, the posterior density multiplier factorizes as

$$
\exp\left(c_t\cdot x-\frac t2|x|^2\right)
=\prod_i\exp\left(c_{t,i}x_i-\frac t2x_i^2\right).
$$

Thus the posterior remains a product pathwise even though the random coordinates of $c_t$ need not
be independent as processes. The fixed event remains $J$-measurable. Since $G_t$ is supported on
$J\times J$,

$$
S_t=s_t\|G_t\|_{\mathrm{HS}}^2
=\sum_{i\in J}s_t|G_te_i|^2.
$$

The certified per-direction estimate applies to each deterministic $e_i$ and gives, for every
$T$,

$$
\mathbb E\int_0^T s_t|G_te_i|^2\,dt\le e_i^TR_0e_i=(R_0)_{ii}.
$$

There is no operator-norm substitution and no random-direction summation. Summing the fixed
$k$ columns and using monotone convergence yields

$$
\mathbb E\int_0^\infty S_t\,dt
\le\sum_{i\in J}(R_0)_{ii}\le k,
$$

because $0\preceq R_0=A_0-B_0\preceq A_0=I$.

### Bounded localization, Fatou removal, and $r_0\le1$

The certified scalar Riccati identity is

$$
dr_t=dM_t+(S_t-D_t)dt,
\qquad D_t\ge0.
$$

At $t\wedge\tau\wedge\sigma_m$, where the increasing bounded sequence $(\sigma_m)$ localizes
the martingale and coefficients, expectation and deletion of $D$ give

$$
\mathbb E r_{t\wedge\tau\wedge\sigma_m}
\le r_0+\mathbb E\int_0^{t\wedge\tau\wedge\sigma_m}S_u\,du.
$$

The terminal values are nonnegative and converge to $r_{t\wedge\tau}$, so Fatou has the required
direction. The stopped integration domains increase, so monotone convergence applies to the
nonnegative source. This proves

$$
\mathbb E r_{t\wedge\tau}
\le r_0+\mathbb E\int_0^{t\wedge\tau}S_u\,du\le r_0+k.
$$

Covariance decomposition gives $0\preceq B_0\preceq A_0=I$. Since
$B_0=s_0\delta_0\delta_0^T$ has rank at most one, its only possible nonzero eigenvalue is
$\operatorname{Tr}B_0=r_0$. Hence $r_0\le1$ and the claimed $1+k$ constant is exact. No
unstopped local martingale is assigned expectation zero.

### Quadratic variation, survival, and the perimeter passage

The mass martingale satisfies

$$
[p]_{T\wedge\tau}=\int_0^{T\wedge\tau}s_tr_t\,dt.
$$

Since $s_t\le1/4$ and
$\mathbf1_{\{t<\tau\}}r_t\le r_{t\wedge\tau}$,

$$
\mathbb E[p]_{T\wedge\tau}
\le\frac14\int_0^T\mathbb E r_{t\wedge\tau}\,dt
\le\frac{(1+k)T}{4}.
$$

The distance from any $p_0\in[2/5,3/5]$ to the complement of $[1/3,2/3]$ is at least
$1/15$. Continuity implies that $\{\tau\le T\}$ forces a stopped fluctuation of at least
$1/15$. Doob's $L^2$ maximal inequality for the bounded stopped mass martingale therefore gives

$$
\mathbb P(\tau\le T)
\le 15^2\,\mathbb E[p]_{T\wedge\tau}
\le\frac{225}{4}(1+k)T.
$$

Thus the dossier's universal $C_0$ may be taken as $225/4$. At
$T_k=[2C_0(1+k)]^{-1}$ the path survives with probability at least $1/2$, and survival gives
$\min(p_{T_k},q_{T_k})\ge1/3$.

The posterior potential has Hessian at least $T_kI$, so the standard published
Bakry--Emery/Bobkov isoperimetric consequence gives

$$
\mu_{T_k}^+(E)\ge c\sqrt{T_k}\min(p_{T_k},q_{T_k}).
$$

The fixed-set perimeter direction also holds without compact support. To see it directly for
Minkowski perimeter, choose a deterministic sequence $\varepsilon_m\downarrow0$ realizing the
initial liminf and put

$$
Q_m(t)=\frac{\mu_t(E_{\varepsilon_m})-\mu_t(E)}{\varepsilon_m}\ge0.
$$

Both fixed-set masses are bounded martingales, so $\mathbb E Q_m(t)=Q_m(0)$. Moreover
$\mu_t^+(E)\le\liminf_mQ_m(t)$. Fatou therefore yields

$$
\mathbb E\mu_t^+(E)
\le\liminf_m\mathbb E Q_m(t)=\mu^+(E).
$$

This justifies the exact direction used in the dossier for arbitrary fixed Borel $E$; if the
initial perimeter is infinite, the conclusion is immediate. Combining the survival event with
posterior isoperimetry and this fixed-set inequality gives

$$
\mu^+(E)\ge\frac{c'}{\sqrt{1+k}}
\ge\frac{c'}{\sqrt{1+k}}\min(p_0,q_0).
$$

The occupation and Riccati arguments already consume dependencies certified for general
log-concave laws, so the dossier's product-preserving approximation paragraph is not a hidden
premise. Bounded stochastic localization, positive-time posterior moments, Fatou for nonnegative
occupation, and the direct outer-neighborhood argument close the general-law passage.

### Fixed-coordinate refutation

Setting $k=1$ gives the total source budget and boundary estimate. For every deterministic
$L>0$,

$$
\mathbf1_{\{S_t\ge L^2/2\}}\le\frac{2S_t}{L^2}.
$$

Tonelli and the total budget therefore give

$$
\mathbb E\bigl|\{t\ge0:S_t\ge L^2/2\}\bigr|
\le\frac2{L^2}.
$$

The quantifiers are in the correct order: the cut, its coordinate, and the level are selected
before observing the path. The proof gives a total occupation bound, not the literal
interval-by-interval all-cut Carleson estimate, and makes no assertion about a coordinate, cut, or
threshold selected after localization.

### Quadratic-chaos covariance calculation

For centered independent factors and symmetric $M$,

$$
Y^TMY=\sum_iM_{ii}Y_i^2+2\sum_{i<j}M_{ij}Y_iY_j.
$$

Every covariance between different displayed summands vanishes. Distinct diagonal terms are
independent; a diagonal/off-diagonal pair contains a centered singleton; two off-diagonal pairs
are independent when disjoint and contain one or two centered singleton factors when they share
exactly one index. Thus

$$
\operatorname{Var}(Y^TMY)
=\sum_iM_{ii}^2\operatorname{Var}(Y_i^2)
+4\sum_{i<j}M_{ij}^2\sigma_i^2\sigma_j^2.
$$

The published one-dimensional reverse H\"older bound gives
$\mathbb EY_i^4\le C_4\sigma_i^4$ after scaling a nondegenerate factor to variance one; a
zero-variance factor is trivial. Hence
$\operatorname{Var}(Y_i^2)\le(C_4-1)\sigma_i^4$. Since

$$
\|A^{1/2}MA^{1/2}\|_{\mathrm{HS}}^2
=\sum_iM_{ii}^2\sigma_i^4
+2\sum_{i<j}M_{ij}^2\sigma_i^2\sigma_j^2,
$$

the optimal coefficient produced by this calculation is exactly
$C_*=\max(C_4-1,2)$. The proof remains valid for the centered product posterior at every finite
time.

### Published covariance window and citation debt

The load-bearing source statement was checked against the accepted author version corresponding
to the published Klartag--Lehec article. Its Theorem 61 states, for the same stochastic
localization covariance process,

$$
\mathbb P\!\left(\exists s\le t:\|A_s\|_{\mathrm{op}}\ge2\right)
\le\exp\!\left(-\frac1{Ct}\right),
\qquad t\le\frac1{C\log^2n}.
$$

This is a supremum-over-time event, not the weaker fixed-time event. The article is published in
*Bulletin of the American Mathematical Society* 62 (2025), 575--642, DOI
`10.1090/bull/1869`; the ledger classification `published` is correct. Corollary 5 in the same
published source gives the one-dimensional reverse H\"older input used above. Brascamp--Lieb's
inverse-Hessian variance inequality is a published 1976 *Journal of Functional Analysis* result,
DOI `10.1016/0022-1236(76)90004-5`, and gives $A_t\preceq t^{-1}I$ for $t>0$. The posterior
strong-convexity isoperimetry used in the budget theorem is likewise covered by the published
Bakry--Gentil--Ledoux, Bobkov, and Milman sources already cited by the certified survival lemma.
There is no unreviewed-preprint premise in any of these five proofs.

On the good sup-time event, $\|A_t\|_{\mathrm{op}}<2$; on its complement the
Brascamp--Lieb cap gives $\|A_t\|_{\mathrm{op}}\le t^{-1}$. Therefore

$$
\mathbb E\|A_t\|_{\mathrm{op}}
\le2+t^{-1}e^{-1/(Ct)}.
$$

With $u=(Ct)^{-1}$, the second term is $Cu e^{-u}\le C/e$, uniformly over $t>0$.
At $t=0$, $A_0=I$. Choosing $c_0\le C^{-1}$ proves `hyp:KI` on
$0\le t\le c_0(\log n)^{-2}$ for every $n\ge3$, exactly with exponent $C_2=2$.
No Letwin theorem, version-1 preprint, quadratic Poincar\'e inequality, or $c/\log n$ window is
used.

### Dependency closure, consumers, and fences

The dependency closure is unconditional.

- `thm:budget` uses `lem:block` together with `cor:per-direction`,
  `thm:scalar-riccati`, and `prop:products`. The latter three are proved, agent-certified nodes;
  the Riccati nodes have the passing core review and `prop:products` has the passing geometry
  review. Their required statements were also rechecked here at the points of use.
- `cor:refutation` depends only on `thm:budget`; the coupled certification is acyclic because the
  budget proof does not use the corollary.
- `cor:KI-discharged` depends only on the published imported node `thm:KL-window`.
- `lem:block` has no dependency. `lem:product-qcts` has no ledger dependency; its only external
  moment input is published and source-checked above.

No dependency is open, conditional, `preprint-unreviewed`, numerical, or supported by a run
artifact. All five nodes may remain `proved` once their active review pointer is replaced by this
report.

Every consumer named in the repair exploration was checked against the repaired hypotheses.

- The fixed-coordinate corollary explicitly inherits $p_0\in[2/5,3/5]$.
- The residual prose and `q:alignment` quantify over fixed balanced cuts and leave the
  high-complexity, high-rank incident-occupation problem open.
- The trace-upgrade comparison says only that summing deterministic coordinate budgets gives the
  naive $\operatorname{Tr}R_0\le n$ bound. It expressly proves no equivalence across the
  trace-upgrade cluster.
- The product clause of `thm:covariance-bound` now imports only the initial product-measure class.
  Its proof uses `lem:product-qcts` and the coarse posterior balance window, not `thm:budget` or
  its initial balance hypothesis.
- `obs:rank-one-refuted` records exactly the fixed balanced one-coordinate obstruction, while
  `q:alignment` is formally bounded by it and asks about high-complexity fixed cuts.
- `thm:covariance-bound` consumes `lem:product-qcts`, and `cor:loglog` consumes the published
  $C_2=2$ discharge without importing the separate Letwin sharpening.

None of the five reviewed nodes has a formal `bounded_by` edge. The nearby rank-one obstruction is
downstream of `cor:refutation`, and its fixed-cut scope is respected. No reviewed result asserts
an adaptive choice, a high-rank occupation refutation, an all-cut Carleson estimate, or an
equivalence among `q:upgrade`, the high-rank part of `q:stein-weighted`, and `q:alignment`.

### Standalone build and structural validation

From `solutions/`,

```text
latexmk -pdf -outdir=../build kls-product-covariance.tex
```

completed with exit code 0 and produced a four-page PDF. The warnings are the expected standalone
unresolved cross-manuscript references and citation-link destination; there is no TeX error.
Before this report was added, `python3 research/check_ledger.py` reported 0 errors.

## Corrections

None.

## Exclusions

This review certifies only the five nodes and the dossier named in the front matter. It inspected
the exact dependency statements needed for closure but does not recertify the rest of
`solutions/kls-localization-riccati-core.tex` or `solutions/kls-geometry-models.tex`. It does not
certify `thm:covariance-bound`, `thm:V2-window`, `cor:loglog`, `q:alignment`, any heuristic
covariance-sharpness claim, either new Klartag--Lehec rank-tail import in module 15, or any other
consumer merely checked for scope compatibility. It certifies no Letwin-dependent result, no
adaptive or high-rank occupation claim, no all-cut Carleson estimate, no KLS conclusion, and no
numerical artifact. Updating the dossier header, ledger, manuscript, routes, bibliography, or
explorations is outside this reviewer's write surface.
