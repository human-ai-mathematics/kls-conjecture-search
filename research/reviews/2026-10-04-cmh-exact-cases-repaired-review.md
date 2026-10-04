---
verdict: pass
authors:
  - kls-cmh-normalization, unknown, 2026-08-25
  - kls_ledger_audit, unknown, 2026-08-25
  - repair_cmh_hodge_domain_w3, unknown, 2026-08-27
  - cmh_1d_domain_repair, gpt-6-astra, 2026-10-04
reviewer: reviewer, gpt-6-astra, 2026-10-04
fingerprints:
  solutions/thm-cmh-dirichlet.md: b877827d30bcedd42ba209d4dc4802b03fb1c536728c354fa23808336c324361
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

Fresh full independent `certify` review of `solutions/thm-cmh-dirichlet.md`
and all ten of its current ledger consumers. No authoring conversation was
provided. The previous revise report and the repair checkpoint were read as
repository records; neither their conclusions nor the August passing audit
were retained without checking the current arguments. Authorship is recorded
from those records. The repair author confirmed the dossier frozen. The
writer's replacement proof following [](#thm:cmh-1d) was subsequently read
before the final fingerprint command; it agrees with the repaired argument
and changes no canonical statement.

**Pass for the complete dossier and each of its ten claims.** The earlier
inverse-domain defect is repaired without narrowing the canonical quantifier.

| Node | Conclusion checked against the canonical statement |
| --- | --- |
| `thm:cmh-1d` | Exact identity, including infinite constants; log-concave constant four and exponential sharpness. |
| `thm:cmh-product` | Block maximum formula, unrestricted scalar specialization, invertible affine invariance. |
| `cor:cmh-linear-images` | Affine Poincare tensorization and every linear image, including singular maps and sums. |
| `lem:cmh-gamma-completion` | Exact ordered-row completion and nonnegative surplus terms. |
| `lem:cmh-row-min` | Pointwise constrained minimum for the homogeneous lift. |
| `lem:cmh-angular-coefficient` | Both scalar minimization branches and their constants. |
| `thm:cmh-dirichlet` | Every m at least two and every parameter at least one, with the stated no-flux closure. |
| `cor:cmh-dirichlet-surplus` | The quantitative coefficient and strict inequality for A greater than three. |
| `cor:cmh-dirichlet-poincare` | Constant-four Poincare bound and the listed independent closures. |
| `cor:cmh-product-saturation` | Exact exponential-product saturation and the Hodge splitting for every admissible test. |

### The repaired general one-dimensional argument

The natural scalar domain is the maximal weighted Sobolev domain, with the
adjoint carrying no-flux boundary conditions. This is compatible with the
canonical differential-operator setup: its locally regular positive density
and connected interval interior suffice. No new log-concavity, tail,
endpoint smoothness, or spectral-gap hypothesis is inserted into the general
identity. Finite nonzero variance is already needed to define the covariance
normalization. In particular, the proof applies to the smooth heavy-tail
example in the revise report.

Writing p=tau rho, centering gives p positive on the interior. Compact flux
fields phi/rho are dense in L2(mu): their fluxes are dense in L2(dx/rho),
by localization and the interior bounds on rho and its reciprocal. Testing
the adjoint relation against phi identifies B0* with the maximal derivative
D, including its entire domain; hence the closure of B0 is D*. This proves
graph-core density, not merely L2 density. The kernel of D is precisely the
constants on the connected interval.

For each such phi, its displayed primitive against 1/p is bounded and has
finite weighted energy, since its derivative has compact interior support.
The integration-by-parts identity holds against every weighted-form test,
and -phi'/rho belongs to L2(mu). The representation theorem for the closed
form therefore places this primitive in Dom(A) with exactly the claimed
image. This is an actual family of CMH tests, and no enlargement of Ran(A)
has occurred.

If M=Var(mu) CMH(mu) is finite, the resulting adjoint coercivity passes in
the graph norm to Dom(D*). A Cauchy sequence of images then has Cauchy
preimages, so the closedness of D* makes its range closed. Its range closure
is the orthogonal complement of ker(D), hence exactly centered L2. Solving
D*u=v for a centered v in Dom(D) and using the adjoint pairing proves
CP at most M. This implication alone proves that infinite CP forces
infinite CMH. It neither requires nor concludes a spectral gap for A.

For finite CP and h=A f, constants in ker(A) imply that h is centered.
Poincare bounds the functional on Ran(D); constants do not affect its
definition. Riesz on the closure of this range gives the displayed w and
norm bound. Every bounded primitive of a smooth interior test belongs to
both form domains. Comparing its two weak pairings identifies tau f'=w
as distributions and hence almost everywhere. Local integrability of the
initial flux follows from weighted Cauchy--Schwarz on compact subintervals.
Its global square integrability is a conclusion, not an assumption.
Taking the supremum over the actual Dom(A) proves the upper bound. This
settles both extended-constant cases without any unbounded inverse.

The exponential test has second moment (1-2a)^(-1), mean (1-a)^(-1)
and derivative energy a^2/(1-2a); its quotient is exactly (1-a)^(-2).
Together with the cited upper bound it proves sharpness.

### Products and affine images

The canonical kernel and covariance are block diagonal. On the tensor
core the two integrations by parts give the nonnegative squared mixed
Hessian norm, with the stated ordering of the block matrices. The block
nonnegative generators strongly commute. Their joint spectral variables
therefore give sum_i ||A_i g||^2 at most ||sum_i A_i g||^2 throughout
the sum operator domain. Conditional factor inequalities and graph
approximation then control the closed flux norm there. Single-block
tests give the reverse inequality, including an infinite factor constant.
The repaired scalar identity supplies the unrestricted scalar specialization.

For ordinary affine Poincare, conditional variance followed by Jensen for
the conditional gradient proves tensorization with the maximum factor
constant. Pullback through T gives covariance T Sigma T-transpose and
exactly the energy in the dossier. This uses no inverse of T. The stronger
CMH affine statement is restricted to invertible maps, as required by the
canonical conventions.

### Gamma, Dirichlet, and boundary checks

The softmax derivative is C(p)/A. Its Jacobian transforms exp(-varphi)
to the Dirichlet density: the source factor is the product of p_i to
the alpha_i powers and the inverse Jacobian removes one power of each
p_i. The tangent pseudoinverse calculation gives A(A+1) times the
sum of v_i squared divided by alpha_i. Thus the CMH quotient is exactly
A(A+1)d_alpha/n_alpha, with no ambient normal contribution.

The centered Gamma zero-flux kernel is Y_i, so the imported Bochner
statement supplies precisely the first-order row Y_i G_i squared and
the full ordered Hessian sum. The Gamma integration by parts gives the
cross term in the dossier with its negative sign; expansion leaves
-alpha_i/(alpha_i+1)^2 times E[Y_i^2 G_i^2]. In units D_i this is
-alpha_i^2/(alpha_i+1)^2. Subtracting one quarter D_Gamma gives exactly
delta_i, nonnegative for alpha_i at least one.

Differentiated Euler homogeneity gives sum_j Y_j G_ij=-G_i. The reciprocal
weights in the constrained square minimum sum to S/Y_i, proving the row
bound including its factor (1+Y_i/(alpha_i+1)) squared. The Gamma-to-simplex
change of variables factors its density, proving independence of S and P.
The inverse radial moments are 1/(A-1) and 1/((A-1)(A-2)); substituting
them gives exactly the three integrated row terms and F_A.

For z at most four, the constrained minimum in p is at one, and all
remaining positive terms increase with a. At a=1 this is A-1+z/4.
For z at least four the interior branch is increasing in a/(a+1), with
minimum A-2+sqrt(z) at a=1; the boundary branch is increasing and
joins it at the interface. Both formulas agree at z=4. A at least three
gives z at least two, so the stated s_A is nonnegative, and strictly
positive for A greater than three. The identity z/4+A-1/2=A(A+1)/4
then proves both the main inequality and the surplus. The sole remaining
parameter region is m=2, A<3; the log-concave scalar result applies there
and uses no inverse second radial moment.

The closure paragraph is valid also at alpha_i=1 and A=3. For a polynomial
g on the compact simplex, the first two derivatives of its homogeneous
lift are bounded by constants times S^(-1), S^(-2). A smooth cutoff at
S of order epsilon has squared-generator and weighted-Hessian errors
bounded by a constant times epsilon^(A-2), which tends to zero in the
Gamma branch. The weighted first-order errors are smaller. The cutoff
identities are passed to the limit before applying exact homogeneity;
the cutoff itself need not satisfy Euler's identity. Coordinate-face
fluxes vanish with Y_i^(alpha_i) or a higher power, including alpha_i=1;
exponential tails justify removal of an upper radial cutoff.

Polynomials are indeed a simplex operator core: L_alpha preserves degree
spaces, is symmetric under the Dirichlet no-flux integration by parts,
and acts as -k(k+A-1) on the component of degree k orthogonal to lower
degrees. Its top-degree action gives this scalar; symmetry eliminates the
lower-degree remainder. Density of polynomials on the compact simplex
and spectral truncation give the graph core. The established inequality
then closes the flux in that graph norm. These arguments justify the
claimed operator-domain extension rather than only the formal lift.

The Poincare consequence uses the certified CMH implication with the same
normalization and the linear-image corollary. Products of exponentials have
finite CMH equal to four, so every admissible operator test has finite
numerator. Thus the finite-flux hypothesis of the certified Hodge statement
is satisfied for every test in the saturation corollary. No perturbative
conclusion is inferred.

### Sources, hypotheses, dependencies, and verification

The exact input CP at most four times variance appears in
[Cattiaux--Guillin v1, equation (2.25)](https://arxiv.org/pdf/1810.08369)
and in [their revised manuscript, equation (2.13)](https://perso.math.univ-toulouse.fr/cattiaux/files/2013/11/cattiaux-guillin-GAFA-revised21.pdf).
The [author's publication list](https://perso.math.univ-toulouse.fr/cattiaux/publications-2/)
identifies its publication in LNM 2256 (2020), pages 171--217. The
[original KLS paper](https://www.renyi.hu/~miki/KannanLovSimIso.pdf) was
also retrieved; the precise Poincare normalization used here is supplied
explicitly by the Cattiaux--Guillin display and its KLS attribution.
This is an established published input, not an unchecked new preprint.
[Kolesnikov--Milman, section 1.2](https://arxiv.org/pdf/1610.06336)
supports the stated prior-art pointer through the simplex and conservative
Gamma references; it contributes no step to this proof.

Every hypothesis used is visible in the statement or its operator setup:
centering, connected interval support and positive locally regular density,
finite nonzero variance, natural closed no-flux domains for the line;
independence and canonical factor data for products; log-concavity only
for the constant-four scalar input; m at least two and alpha_i at least
one for Dirichlet; degree-zero homogeneity for row minimization; A>2
for inverse second radial moments; A at least three for the angular
lemma, with the remaining scalar branch separately treated. No stated
hypothesis is silently strengthened. The line identity itself does not
need log-concavity. No unused hypothesis causes a defect.

The required `def:cmh`, `prop:cmh-bochner`,
`thm:cmh-implies-affine-poincare`, and `prop:cmh-hodge` statements were
read and supply exactly the normalization, identity, implication, and
finite-flux decomposition used. The latter three retain their independent
normalization-dossier certification. The ten nodes have no open
`depends_on`, `assumes`, or `bounded_by` edge. The proof DAG is acyclic;
there is no use of the Dirichlet Poincare consequence to prove Dirichlet
CMH. The projection ceiling is respected by the full Hessian-row argument,
which makes no quadratic-chaos conclusion.

Full `uv run scripts/check.py` completed with no MyST error and exactly
ten stale-certification errors, all for the old records of this dossier.
The final `--fingerprint solutions/thm-cmh-dirichlet.md` succeeded after
the synchronized manuscript proof was read and gave the block above.
No numerical output was used as mathematical evidence. No step within
the certified scope remains unverified.

## Corrections

None required. Replace the ten old proof-record review paths by this report,
retaining `status: proved` and all existing relations. The earlier revise
report remains a valid historical record of the repaired inverse-domain
defect; it is not edited or erased.

## Exclusions

This review does not recertify the normalization dossier, cone formulas,
the Bessel formula in the nearby sharpness remark, fiber-floor proofs,
universal CMH, KLS, gate zero, regular recovery, or perturbative claims.
Fingerprinting dependency statements certifies their agreement with this
proof's use, not new proofs of those dependencies. The writer's local
synchronization was checked; this is not a full manuscript `sync` audit.

## Handoff

```yaml
files:
  - research/reviews/2026-10-04-cmh-exact-cases-repaired-review.md
deltas:
  - path: research/program/ledger.yaml
    nodes:
      - thm:cmh-1d
      - thm:cmh-product
      - cor:cmh-linear-images
      - lem:cmh-gamma-completion
      - lem:cmh-row-min
      - lem:cmh-angular-coefficient
      - thm:cmh-dirichlet
      - cor:cmh-dirichlet-surplus
      - cor:cmh-dirichlet-poincare
      - cor:cmh-product-saturation
    replace_proofs_for_each:
      - artifact: solutions/thm-cmh-dirichlet.md
        review: research/reviews/2026-10-04-cmh-exact-cases-repaired-review.md
    status_for_each: proved
    relations: retain all current depends_on; no new assumes, bounded_by, or refuted_by
```
