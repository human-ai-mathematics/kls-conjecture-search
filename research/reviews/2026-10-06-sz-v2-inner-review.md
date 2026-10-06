---
verdict: pass
authors:
  - sz_v2_inner, gpt-6-astra, 2026-10-06
  - sz_v2_height, gpt-6-astra, 2026-10-06
reviewer: reviewer, gpt-6-astra, 2026-10-06
fingerprints:
  solutions/sz-v2-inner-refinement.md: d3e2fd111c48fb5a56740285bd18b1676741f8cb4b9b85b3b0eb4d40a3c9cda2
  thm:sz-v2-iterated-curvature: a374bf920166e028978e9ada8311b0dadd8cfb1b4ef8850c846069900630a6ef
  lem:sz-analytic-foundations: e3b0250c18499cbdf58b3cb609937032b0101d8aa096aac355555309e5e94d3f
  thm:sz-polynomial-variance: ffd52798e616ccd22bb3e4c78d5c382fd5657d3b598e6e4ec3c9afc4f696da8e
  thm:sz-curvature-comparison: 9baf9221ded7767fc4a904b4a582b9804ab1d424bb87914745aaaa6dd0242787
  thm:sz-iterated-curvature: e1c597ce3da1e94ebc6e1fbde16ce86114991cd711e6eb3f7a9550bb161fdef8
  prop:sz-v2-static-coefficient-transfer: bc15d851517e3f5214ddf15d70fc42328b860a6b0d5655ba0898aa0ee1d040c0
  lem:sz-v2-joint-frame: aaf5c36182ce8cdc5e342504d9f86ea34e8ed764bf63b01f6b3ad29edbb1bc2d
  lem:sz-v2-skew-credit: e9510673a1e46fd5d998b3b77b212371ad779546264a1b2f0db5a68e585ea5c3
  lem:sz-v2-operator-block-primitives: bb09229db057bba3a2bdf944fb2c6fd59ee16aaba488b607a84e62a2bdc42a7e
  lem:sz-v2-normalized-hierarchy: c871dbe2a0195d11acb31e90e91b361b2f1f56848b52beab30b54bb6669dd499
  lem:sz-v2-mesoscopic-powers: e01550a65203ed00238ab57cafdde06aac331b358c0e36fcf4406fc897d33f7f
  thm:letwin-qcts: 8e2ac0819f46db553fe83a6f3034436816565262316c2e6bde7d81baead1a082
  def:sz-v2-common-radius: 49ae12dc3b61656251736c6d98ed212477348fbfdcfcb5ce82c490131854c2b7
  solutions/sz-v2-dimension-bound.md: 244c3c5dd16a41df107b171fedc4ed28618661ade64b6dd7205fdbcb9acd0479
  thm:sz-v2-dimension-bound: 47411afac9d888dc919ab146a93088b4321a9f51b193a3335c3941f2628afb2d
  thm:sz-curvature-transfer: c65a989b9e3b583ef639f2c95d7a8b60a3c0355b8434b57685bef57c626f41a9
---

## Findings

Independent full certification: **pass** for both dossiers and all five nodes
listed below. The review began in a fresh context containing the mission and
repository paths, without the conversation that authored or directed these
proofs. Neither dossier was authored by this reviewer.

| Dossier | Canonical claim | Result |
| --- | --- | --- |
| `solutions/sz-v2-inner-refinement.md` | `lem:sz-v2-operator-block-primitives` | pass |
| `solutions/sz-v2-inner-refinement.md` | `lem:sz-v2-normalized-hierarchy` | pass |
| `solutions/sz-v2-inner-refinement.md` | `lem:sz-v2-mesoscopic-powers` | pass |
| `solutions/sz-v2-inner-refinement.md` | `thm:sz-v2-iterated-curvature` | pass |
| `solutions/sz-v2-dimension-bound.md` | `thm:sz-v2-dimension-bound` | pass |

The operator, hierarchy and mesoscopic assertions agree with their canonical
statements. The curvature theorem retains every regularity, covariance,
curvature, dimension and depth quantifier; its constant is uniform in depth.
The dimension dossier states its curvature input explicitly. That input is
proved in the other dossier certified here, so their composition proves the
unconditional canonical dimension theorem. Its additional inverse-Cheeger
conclusion is also justified.

I checked the actual proofs in the supplied local rendering and extraction
of [arXiv:2610.01447v2](https://arxiv.org/html/2610.01447v2),
`/tmp/kls-sz-v2.html` and `/tmp/sz-v2.txt`: Lemmas 6.4–6.8,
6.16–6.24, the final proof of Proposition 6.1, and the dimension deduction
in Section 7. The source's proof, not just its theorem statements, was
compared with the reconstruction. The three foundations are used through
`research/reviews/2026-10-06-sz-v2-foundations-review.md`, whose certified
statements supply exactly the frame, skew credit and static transfer used
here. The existing analytic, polynomial, curvature-comparison and
fixed-depth results retain their independent certifications.

### Restricted operator, domains and normalization

The map $A=LH^{1/2}$ has bounded adjoint
$A^*z=H^{1/2}(z\cdot X)$, with $AA^*=I$ by the Dirichlet identity.
Thus $E=I-A^*A$ is a projection, $D^*D=E$, and the restricted Rayleigh
quotient becomes $\|EBE\|$. The factorization with $B^{1/2}E$ proves
$\mathcal T^*\mathcal T=B-L^*L$ and its norm identity. The positive
block estimate uses $ABA^*=\Sigma\preceq I$ and gives $C_P\le R+1$.
The centered space is infinite dimensional; removing finitely many
coordinate directions leaves a nonzero restricted space. Compactness
therefore supplies a positive top eigenvalue and a genuine extremizer.
Coordinate functions belong to $\operatorname{Dom}H$ under the regular
Hessian bounds. Taking gradient means and then a form pairing proves
both constraints on this extremizer. The affine term is retained in the
Bochner identity, giving the stated low-energy gradient.

The hierarchy uses the same scalar normalizer across each full family.
Spectral Cauchy–Schwarz makes $\chi_j$ nonnegative; centering gives the
exact mass decrement. Bochner and inverse normalization give the energy
recurrence. If a successor vanishes, Bochner still gives the claimed
inequality at that step and the specified zero continuation is valid.
The bounds on $\beta_j$ use the positive mass $v_j$, not a claim about
individual components. All inverses act on centered functions, every
successive raw gradient is in the form domain, and the weak derivatives
used for adjacent swaps commute. There is no unbounded differentiation
of an old defect: later propagation is by $\sqrt\beta\mathcal T$.

The sharper budget follows from $v_{N+1}\le Re_N$, so its reference
energy is precisely $R^{-1}$. The orbit-window loss formula follows
from $F_k$ being a scalar multiple of $B^{1/2}\mathcal T^kY$ and
$\mathcal T^*\mathcal T=B-L^*L$; its denominators and index shifts agree.
The compensation proof of (4) actually needs only symmetry of the mean
gradient, as in the canonical primitive, rather than the stronger genuine
gradient hypothesis stated for that local lemma: the proof uses the
certified skew-credit inequality and no pointwise curl condition.

### Compensated start and mesoscopic powers

The quadratic test has no affine correction because the Appell quadratic
has mean-zero gradient. Letwin's certified sharp quadratic estimate extends
by whitening and covariance contraction to $K_2\le8$. The three-slot frame
has least eigenvalue $1-\sqrt3/2>1/8$; keeping inherited slots as output
indices is legitimate. I checked the distinct initial defect
$\chi_{\rm pre}$, the subsequent defects in (5), the normalizer ratios,
and the three bounds $32,128/3,160/3$ times $\sigma^2$.
Their rescaled sum is below $160\lambda^2$ for $R\ge16$.

The degree-three block recovery used here is the proved internal lemma of
`solutions/thm-sz-curvature-comparison.md`, already covered by its independent
review. I also checked its specialization directly: $s=1,l=q=3$ gives
coefficient $1/9$, hence recovery constants $3$ and $4$. The coherent term
and two swap errors then give (7) with the stated $A_0,B_0$.
The universal bound on $c_3$ follows from the fixed-depth v1 profile and
static transfer; it does not come from BKL or a KLS endpoint.

In the mesoscopic first-exit argument, every normalizer needed by $P_N$
uses a mass before the possible exiting prefix; its successor is still
positive. Summing the two delayed defects uses $X_{N-2}$, and the
$R^{-1}$ energy budget gives $3\sigma^3+\sigma P_N$.
The choices $R_0\ge4B_0$ and $K=512+4A_0$ yield the displayed strict
no-exit margin. The representation $F_j=s_jB^{1/2}W_{j+2}$ correctly
identifies the loss fractions. Bochner gives
$\mathcal T\mathcal T^*\preceq B$ on the appropriate output family;
Cauchy–Schwarz against $W_{k-1}$ then gives the ratio recurrence.
The first compensated ratio and the cumulative loss bound prove (6),
including every $1\le m\le\lfloor R\rfloor+2$.

### Averaging and the static radius

A top right singular vector exists because the finite power is compact
and nonzero. Its normalized orbit has $b_0=b_m=1$. The bounds on
$R/z$ control all required indices through $m+9$; no positive lower
bound after $m$ is assumed. Expanding the form norm of $(B-zI)w_j$
gives (8), with the correct sign of the linear loss. Summation leaves
only the two stated boundary differences. The three-slot and degree-three
estimates control full linear moments, not only their symmetric parts.
Absorption gives the two bounds in (14).

The averaged family $U$ is centered, unit, and columnwise a genuine
gradient. Its quadratic symmetric moment is $O(z^{-2})$. The second
normalized successor is exactly the compensated restart; the loss
fractions with indices $2$ through $8$ are the seven restart fractions.
Each denominator has a window containing sufficiently many positive
interior terms, proving the cubic startup bound. The starting excess
above $R^{-1}$ is $O(z^{-3})$, with the discrepancy between $z$ and $R$
explicitly included. Splitting powers into whole blocks and a remainder
proves (11), with the block constant paid once per propagation.

Appell testing is valid on full ordered-index direct sums. Nested
symmetrizations allow iteration of the testing identity through a whole
block, giving $c_d\le z^{m/2}c_{d-m}$ with the exact factorial
normalization. The fixed logarithmic seed initializes every remainder
degree, including degree one. The bounded-radius case uses ordinary
Poincaré on Appell derivatives. Thus one static $Z$ controls every degree,
$C_P\le Z+2$, and $Z\le\max(H_0,C_P)$. No regularity or continuity
of $Z$ as a function of the law is used in transfer.

### Joint losses, first exit and depth recurrence

The joint frame is applied to a single tensor $T_j$, so its coherent
projections are compatible. At available dyadic degree $d$, the largest
error block has $4k\le2d$ slots and all defect indices are nonnegative.
Sorting the $3k$ derivative slots and the finite convolution estimate give
exactly $324C_FC_{\rm blk}^2k^6$ in (17). Every defect index in $P_N$
is at most $N-3$, hence the delay is $X_{\max(N-2,0)}$.
The first seven actual losses pay for startup, and the $2k$ uses of
intermediate degree $k$ give the stated coherent sum.

The finite comparison uses $\sigma=R^{-1}$ throughout. At the first
possible exit the required normalizers are bounded by $\nu/(1-p)$,
and the successor remains positive. The short prefixes are covered by
$p_0+p_1\le\Delta$. The ceiling defining $m$ gives the claimed horizon
bound since $a\le D_0+\sigma p$. Absorption gives $c=17/56$; the final
strict contradiction follows from $D_0\le\sigma$ and $p\le1/8$.
This argument never substitutes the block radius for the restricted
one-step radius in the energy budget and never takes an infinite hierarchy
limit.

For the depth induction I checked both coefficient bounds used in (19),
the uniform domination of $\log(e+k_0)$ by $s^{1/6}$, and both low-degree
series. Their bounds retain the essential factors $u$ and $u^3$.
The displayed integral estimates bound the integer exponential tails;
$e^{-\delta k_0/2}\le(\delta/M_0)^{32}$ makes their contributions at
most $u$ and $p/512$. The restrictions on the single universal $G$ are
compatible. In particular the low-degree contribution to the comparison
budget is at most $p/256$, leaving the required margin below $p/64$.
The delayed comparison consequently yields (21) without an extra factor
$u$. The dyadic degree choice gives the terminal exponential contradiction.

Logarithmic elasticity is at most $2^{-r}$ and supplies $\zeta_r$.
The factor $b^4e^\delta$ is bounded by
$((r+2)/(r+1))^{1/3}$, while the product of
$(1+r^{-2})^2\zeta_r^2$ converges. A single fixed-depth v1 profile
initializes the induction for $Z$. The bounded-radius and $a\ge1$
cases are covered before the large-radius argument. Every later coefficient
premise has already been proved at the preceding finite depth. The additive
two in $C_P\le Z+2$ is absorbed only after this induction.

### Dimension transfer and hypotheses

The certified curvature transfer applies to the current input for every
admissible lower curvature bound. Its constants do not depend on the
selected finite depth. Concavity gives $g(Dx)\le Dg(x)$ and induction
gives the same argument-rescaling factor at all depths. The stopping-depth
argument checks the cases $m=0,1$ and the ordinary-logarithm comparison
before the first iterate at most four. It gives a finite
$r\le\log^*(n+2)$ and $\ell_r(\log(en))\le5$.
The existing transfer supplies nonsmooth measures and the finite-energy
formulation; no new approximation interchange is made here.

The inverse-Cheeger constant used by the dimension dossier satisfies
$\psi_\mu^2\le\pi C_P(\mu)$ in this convention. I checked the precise
constant against Corollary 21 and its following display in the
[published Klartag–Lehec notes](https://arxiv.org/html/2406.01324v2#S2.SS3).
The subsequent supremum over isotropic laws preserves the dimension estimate.

Hypotheses used are finite dimension; a centered smooth probability density;
positive lower and finite upper Hessian bounds in the operator argument;
covariance at most the identity; centered finite form-domain families;
the symmetry condition in the compensation step; and positive dyadic integer
degrees where required. Large-radius thresholds and large-depth thresholds
are explicitly imposed before use, and smaller cases are covered separately.
The final transfer uses isotropic log-concavity, integer $n,r\ge1$, and
a uniform curvature profile. All are stated. No extra symmetry of the law,
commutation of covariance with another matrix, uniform curvature lower bound
over laws, or continuity of the static radius is assumed. No stated hypothesis
is unused in a way that affects the conclusions.

The five claims form an acyclic chain of certifications in this report;
all inputs outside that chain are already proved or defined. No open
external dependency or `assumes` antecedent remains. There is no applicable
`bounded_by` edge; none of the CMH, occupation or trace antecedents is
asserted. The full `UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py`
completed with exit zero and no MyST errors. Final fingerprints were generated
from the versions reread after the corrections below.

## Corrections

Resolved before certification: the mesoscopic claim was added to the
inner dossier's front matter; its fixed-depth/static-transfer dependencies
and the sharp Letwin input were made explicit in the ledger, and the
curvature claim names its mesoscopic input. The hierarchy proof's phrase
“Dirichlet norm” was corrected to “squared $L^2$ norm” for
$\nabla H^{-1/2}F_j$. I checked the corrected identity and its unchanged
mass/energy consequences. These are the versions fingerprinted above.
No mathematical repair remains within the reviewed scope.

## Exclusions

This report does not certify the longer Green-window construction,
finite block extension for the outer iteration, block propagation,
height reduction, prescribed-depth small-loss refinement, retained bounds,
summable budgets, or the SZ v2 universal KLS conclusion. It does not
re-certify the entire existing v1 or foundations dossiers, and it is not
a global manuscript/status synchronization audit. No BKL theorem,
BKL coefficient consequence or already-proved KLS endpoint is used.
No numerical run is a proof input. No step of the assigned five claims
remains unverified.

## Proposed proof records

Set the four inner claims in the table to `status: proved` and add to each:

```yaml
proofs:
  - artifact: solutions/sz-v2-inner-refinement.md
    review: research/reviews/2026-10-06-sz-v2-inner-review.md
```

Set `thm:sz-v2-dimension-bound` to `status: proved` and add:

```yaml
proofs:
  - artifact: solutions/sz-v2-dimension-bound.md
    review: research/reviews/2026-10-06-sz-v2-inner-review.md
```

Retain the current `references` and corrected `depends_on` edges. These are
unconditional proved claims; no `assumes`, `bounded_by` or `refuted_by`
relation is warranted. Apply the chain in dependency order: primitives,
hierarchy, mesoscopic powers, curvature, then dimension.
