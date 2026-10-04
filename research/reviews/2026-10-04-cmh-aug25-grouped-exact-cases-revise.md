---
verdict: revise
authors:
  - kls-cmh-normalization, unknown, 2026-08-25
  - kls_ledger_audit, unknown, 2026-08-25
  - repair_cmh_hodge_domain_w3, unknown, 2026-08-27
reviewer: reviewer, gpt-6-astra, 2026-10-04
fingerprints:
  solutions/thm-cmh-dirichlet.md: 9d15b1206907f46fc2e0cc4496ba15120fb39271dcd255fe66ed37223a1e9734
  thm:cmh-1d: 20ca97481f8d3f33bab114618adc59596740cec2d34e37ad9c5c8ec1b9fa9904
  def:cmh: 5971e940e93fa8179ce6c80c9817d3b3a88ac7db2ffe56897f1957c02431f9e7
  thm:cmh-product: 93367af0f91020a7189581ccf6821eafd93c5bb734d06bfb114187be354d08a7
  cor:cmh-linear-images: 4a8e460a9f137e2c3bfcd012669e8a658f242d5dcd19ba480849ffc13abef452
  lem:cmh-gamma-completion: 322e41a5312dc60bb984ccaa9e90cf3ba7598ef853f353546520666f45aa8a33
  prop:cmh-bochner: 237164772a03afb3fb5bfb7a896dbd45f8487332637efa548b827454d8f8ea6c
  lem:cmh-row-min: 3747422f61e31d367dbc910511a078a463c6440ae445f61324e00e45f812e05f
  lem:cmh-angular-coefficient: b2dd0851b76505e3182d0b1472b8d5102a420f78b16abdb8ae23fde0456de475
  thm:cmh-dirichlet: 0950144e400e4a077e8ae82686d149d0a736b6ec651e7c588e4e867146a8db94
  cor:cmh-dirichlet-surplus: fdd4f0dcfccd11cb61eceeec922bc50c8ed87bb4a9faa496901201eef7ea9424
  cor:cmh-dirichlet-poincare: 0295ebca6004666831c2db752ae739c062b86f6097e7b9f5152902d1765820c6
  thm:cmh-implies-affine-poincare: 9210ad8934e1f76e3f1f621274c0be2dc1c9e5fa106146b66584871844acd5e0
  cor:cmh-product-saturation: 2a3ba80b8cfea460f74c0dbcf122eeafdcf31576b42e60cf7d5507106f2332af
  prop:cmh-hodge: e53f8f0d21ff4afad0be69fb034e09db1f7daaa882338a1d927af40c3117410e
---

## Findings

Fresh full independent `certify` examination of the complete exact-cases dossier
and its canonical statements. This is not a re-review retaining August conclusions.
The grouped mission concerns twelve primary nodes and three additional current
consumers, fifteen in total. This report covers nine primary nodes and the
additional Gamma-completion node. The companion normalization report covers the
other five nodes. No authoring conversation was provided; author identities were
reconstructed from the historical reports and repair checkpoints.

**The dossier requires revision for the unrestricted one-dimensional theorem's
inverse-domain step.** This is a defect in the proof as written, not a
counterexample to its conclusion, and not a defect in the constant-four
log-concave Dirichlet estimate.

### Exact defect and witness

The canonical `thm:cmh-1d` quantifies over every centered one-dimensional law
for which the stated operators are defined; it is not restricted to log-concave
laws or to finite ordinary Poincare constant. At
`solutions/thm-cmh-dirichlet.md:42`, the proof sets
v=(D_mu^* D)^(-1)h for h=A f. At line 50 it then takes a supremum over all
centered h. Neither membership in the inverse domain nor the range/density
passage is supplied in the infinite-Poincare case. A pseudoinverse convention
does not make an unbounded inverse defined everywhere.

This is a real domain issue. Let rho(x)=c(1+x^2)^(-3) on the real line,
with c the probability normalization. It is smooth, strictly positive, centered,
and has finite nonzero variance. Its zero-flux Stein kernel is
tau(x)=(1+x^2)/4, since (tau rho)'=-x rho. The closed no-flux weighted
operator is well-defined. The function f(x)=x is in its operator domain and
A f=x: its form energy is finite, and the weak identity follows first on
compactly supported tests and then by form density. Thus h=x is an admissible
centered element of Ran(A). The zero-flux solution of D_mu^*u=h is u=tau,
which even belongs to ordinary L2(rho). But any solution of
(D_mu^*D)v=h must have

$$
v'(x)=\frac{1+x^2}{4},\qquad
v(x)=\frac{x}{4}+\frac{x^3}{12}+\text{constant}.
$$

This v is not in L2(rho): its squared cubic term times rho tends to a
positive constant at infinity. Hence h is not in the domain of the operator
inverse used at line 42. Both generators exist; the failure is not an
undefined density or zero-variance degeneracy. The example is outside
log-concavity, which is exactly why it does not affect the later log-concave uses.

For finite ordinary Poincare constant the inverse is bounded on centered L2.
The zero-flux uniqueness argument then identifies u with Dv, and the dense
range of A suffices for taking the norm of the continuous inverse quadratic
form. These facts justify the log-concave branch of the existing argument.
They do not justify its larger quantifier when the inverse is unbounded.

### Per-node conclusions

“Checked” below identifies unaffected arguments; it is not a separate proof
record or a passing certification of this failing dossier.

| Node | Mathematical conclusion of this examination |
| --- | --- |
| `thm:cmh-1d` | Revise for the general-law/infinite-Poincare branch. Finite-Poincare identity, log-concave bound and exponential sharpness checked. |
| `thm:cmh-product` | Product CMH formula checked. Its unrestricted one-dimensional restatement inherits the preceding gap; its log-concave consequences do not. |
| `cor:cmh-linear-images` | Checked: ordinary Poincare tensorization and linear pullback, including singular maps. |
| `lem:cmh-gamma-completion` | Checked: canonical Gamma kernel, ordered Bochner rows, square completion, and signs. |
| `lem:cmh-row-min` | Checked: differentiated Euler constraint and weighted Cauchy–Schwarz minimum. |
| `lem:cmh-angular-coefficient` | Checked: both minimization branches, their common endpoint and nonnegative surplus. |
| `thm:cmh-dirichlet` | Checked in every stated parameter case, with boundary/core closure as detailed below. |
| `cor:cmh-dirichlet-surplus` | Checked: strictly positive surplus for A>3 with the stated coefficient. |
| `cor:cmh-dirichlet-poincare` | Checked: the finite-Poincare one-dimensional branch suffices; the general-law gap does not enter. |
| `cor:cmh-product-saturation` | Checked: exponential sharpness, product maximum and finite-numerator Hodge splitting. |

### Products, Gamma lift, and closures checked

For products the block generators strongly commute. The nonnegative cross terms
are the squared mixed Hessian norm on the smooth tensor core. Equivalently their
joint spectral variables are nonnegative, so the sum-of-squares bound extends to
the sum generator's domain. The conditional factor estimate controls the flux
operator there; testing a single block gives the opposite inequality, including
an infinite factor constant. Ordinary affine Poincare tensorization used by the
linear-image corollary follows from conditional variance and gradient Jensen;
the covariance transforms as T Sigma T-transpose with no inverse of T.

The softmax potential has the claimed Hessian; its Jacobian changes the source
density into the Dirichlet density. The tangent pseudoinverse calculation
removes the normal ambiguity, giving the factor A(A+1), with no ambient
dimension error. Independent centered Gammas have canonical kernel diag(Y_i):
each one-dimensional zero-flux kernel is Y_i. The Bochner identity therefore has
the ordered sum over i,j, counting each off-diagonal Hessian entry twice.

The Gamma integration by parts yields the coefficient
-alpha_i/(alpha_i+1)^2 in the row completion. Multiplication by alpha_i
in D_i gives exactly delta_i=alpha_i^2/(alpha_i+1)^2-1/4. Differentiating
degree-zero homogeneity yields the row constraint. The reciprocal row weights
sum to S/Y_i, giving precisely the displayed minimum. Independence of S and P
then supplies the two inverse Gamma moments; no inverse moment is used at A=2.

In the angular minimization p_*=(a+1)/sqrt(z). For z<=4 the constrained
minimum is p=1 and then a=1; for z>=4 the interior formula is increasing
in a/(a+1), and its a=1 minimum lies in the allowable region. The boundary
region joins continuously and cannot be smaller. The branches agree at z=4.
At A=3 the surplus is zero, and at A>3 it is strictly positive. Finally
z/4+A-1/2=A(A+1)/4, establishing the exact coefficient.

The short closure paragraph is valid; it does not conceal a divergent cutoff
error. For polynomial g, derivatives of its homogeneous lift of orders one and
two are bounded by constants times S^(-1) and S^(-2). For a smooth radial
cutoff changing on S of order epsilon, the squared generator and weighted
Hessian errors integrate to O(epsilon^(A-2)); the first-order errors are
smaller. Thus A>=3 suffices. One first passes to the uncut homogeneous lift
in the Gamma identities and only then uses its Euler relation; a cutoff lift
itself need not be homogeneous. At each coordinate face the Gamma flux has
a factor Y_i^(alpha_i), which vanishes even when alpha_i=1. Exponential
tails remove the boundary at infinity.

For the simplex operator, polynomial degree spaces are invariant and symmetry
with the no-flux Dirichlet density holds at all faces. On the orthogonal
degree-k component, -L_alpha has eigenvalue k(k+A-1): its top-degree action
has that coefficient, and symmetry removes the lower-degree remainder.
Polynomials are dense on the compact simplex, so these finite-dimensional
components exhaust L2 and give the asserted operator core by spectral truncation.
The established inequality then closes the flux norm in the operator graph norm.
For m=2,A<3 only the finite-Poincare, log-concave one-dimensional case is used.
This completes the boundary and spectral check of the stated Dirichlet result.

### Hypotheses, sources, dependencies and downstream impact

The general line identity needs the nondegenerate centered interval law,
the closed operators and no-flux domains; it does not state finite Poincare,
which is the omitted distinction above. The constant-four conclusion uses
log-concavity. Products need independent blocks and their canonical block
kernels; only the scalar specialization uses one-dimensional factors.
Dirichlet needs m>=2 and alpha_i>=1. Homogeneity is essential to the row
constraint, A>2 to the inverse second radial moment, and A>=3 to the angular
bound; the residual scalar case is treated separately. No extra curvature,
uniform approximation, or universal CMH hypothesis is used.

The cited [Cattiaux–Guillin v1 equation (2.25)](https://arxiv.org/pdf/1810.08369)
really states the bound giving CP<=4 Var on the line. It is equation (2.13)
in the [revised author manuscript](https://perso.math.univ-toulouse.fr/cattiaux/files/2013/11/cattiaux-guillin-GAFA-revised21.pdf),
published in LNM 2256 (2020), pp. 171–217. The original KLS paper was retrieved
as well; the dossier's precise normalization is supported by the former display.
No recent-preprint proof is imported. The
[Kolesnikov–Milman introduction, section 1.2](https://arxiv.org/pdf/1610.06336)
does identify prior simplex and conservative-spin results, as the dossier says;
it is only a prior-art pointer, not an input to the proof or a priority certificate.

The current ledger has no open `depends_on` on these nodes, and no `assumes`
or `bounded_by` edges. The problem is inside a currently certified proof, not
an illicit use of an explicitly open premise. The proof DAG is acyclic:
Gamma completion uses Bochner, row minimization uses its defined row expression,
and Dirichlet uses these plus the scalar case and angular lemma. No step feeds
the Dirichlet Poincare consequence back into its proof. The projection ceiling
is respected because the full Hessian rows are used.

The affected unrestricted identity propagates to the corresponding unrestricted
sentence in the product theorem. It does not propagate mathematically to the
Dirichlet Poincare result, exponential saturation, or the normalization dossier's
log-concave Hodge comparison. In particular the inspected use at
`solutions/lem-fiber-polynomial-floor.md` is solely the constant-four Poincare
bound for an isotropic uniform simplex. That use remains justified, with
12/A_k times gradient energy giving 3/A_k times variance and A_3=240 giving
1/80. This review does not recertify the rest of the fiber dossier.

Full `uv run scripts/check.py` succeeded with no MyST error. The single-dossier
fingerprint output above records the unchanged tree examined. No numerical
agreement is used as evidence.

## Corrections

Required repair: `solutions/thm-cmh-dirichlet.md:42` and `:50`. Preserve the
canonical general-law statement and prove both directions with correct operator
domains, explicitly including infinite ordinary Poincare constant. Specify where
an operator inverse, inverse quadratic form, or spectral truncation is used.
Justify the supremum over attainable h=A f rather than replacing it silently by
all centered L2. Show how the no-flux identity and the relevant closures survive
the approximations. The heavy-tail example above must be covered without
asserting that its h belongs to the ordinary operator inverse domain.

Consequential verification: `solutions/thm-cmh-dirichlet.md:79` and `:100`
must follow for the full one-dimensional factor class, including infinite
constants. Preserve the already valid log-concave/exponential branch at lines
52–62 and its uses in the residual Dirichlet branch and saturation corollary.
The mirrored manuscript proof at `modules/12-cmh-exact-cases.md:45` also uses
the unrestricted inverse; after the researcher supplies the corrected argument,
its responsible writer should synchronize that proof without weakening the
canonical statement. No repair is required to the Gamma algebra, cutoff power,
Dirichlet constants, or fiber-floor constants.

## Exclusions

No new certification is issued for this dossier or any of its nodes by this
report. Universal CMH, gate zero, KLS, approximation closure, perturbative claims,
unrelated cone spectra and the complete fiber-floor proof are outside scope.
The theorem is not refuted: the witness refutes the asserted inverse-domain
step, not equality of the two possibly infinite constants.

## Handoff

```yaml
files:
  - research/reviews/2026-10-04-cmh-aug25-grouped-exact-cases-revise.md
next: |
  Repair the general one-dimensional inverse-domain and range argument in
  solutions/thm-cmh-dirichlet.md:42–50, retaining the canonical quantifier and
  treating infinite CP explicitly. Verify its product specialization at :79
  and :100. Keep the finite-CP/log-concave and all Gamma/Dirichlet results intact.
  Record the corrected operator-domain argument and request fresh independent
  certification of the complete dossier. Have the responsible manuscript writer
  synchronize its mirrored proof after the repair; do not change the statement.
```
