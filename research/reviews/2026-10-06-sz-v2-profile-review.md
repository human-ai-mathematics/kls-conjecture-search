---
verdict: pass
authors:
  - plan_sz_architecture, unknown, 2026-10-06
reviewer: reviewer, gpt-6-astra, 2026-10-06
fingerprints:
  solutions/sz-v2-small-loss.md: 10bb1729c3f61515d14cc72d24a9d3409e7972811b40da1a5a1e699259b04874
  lem:sz-v2-profile-calculus: f7da70fff133bd9fdcc1eaa51baa844a4c96599c4bfa0345900c794f35f15164
  def:sz-v2-height-profiles: 96a140c2ad0f0d237038116dad4f24466bf9d91a72ccbd9b8a62e37f7b0d9482
  lem:sz-v2-profile-refinement: a7087671a822effe51fa9fa6f245528730e97bcfac3b03bdb39e42e02fbe5a08
  def:sz-v2-common-radius: 49ae12dc3b61656251736c6d98ed212477348fbfdcfcb5ce82c490131854c2b7
  prop:sz-v2-common-radius: 2ae867703ee8d57f0b0ca660a3af2ef8c37357725d7d5d66e3670c92014d1044
  prop:sz-v2-static-coefficient-transfer: bc15d851517e3f5214ddf15d70fc42328b860a6b0d5655ba0898aa0ee1d040c0
  prop:sz-v2-height-reduction: 8b074fd671347e3be0c2e47c689462e5c590c8d5982687265fe27039d0562923
  lem:sz-v2-terminal-distortion: a9bba017a6789be19cac1518024a01c88a73b0d5cef8ee3b15bde4f73e416f83
  prop:sz-v2-finite-chain-blocks: 9f8e06931ebd02c5e2c98d41b058cececa4926b2a70382378c73ea93e7442c8a
  lem:sz-v2-propagated-joint-loss: 1d476098d11506ee2dcf0690bcd96206b11e55b9bf597aaf41975db58b108e0a
  lem:sz-v2-normalized-hierarchy: c871dbe2a0195d11acb31e90e91b361b2f1f56848b52beab30b54bb6669dd499
  prop:sz-v2-small-loss: 1b14806d5b226c659ec59b9fad8476889050fabc8bd8db3b5b32b5f4435a8c52
  solutions/sz-v2-summable-budgets.md: cb068ed2355072b088268fbaabb8b0a8abc0f26777b13ec2c5eccdcf41c3915d
  lem:sz-v2-profile-threshold: a3c3d52e2f34f4321a741ebb2e4cb51c9be024ba0ac305d4ba014a5d3f82bf56
  prop:sz-v2-summable-budgets: b53fa0c1e2dfe13bf23d91984f09c2162cd200fbc8e03059234c2e3ed9561a78
  solutions/sz-v2-kls.md: b3e292de24b9aec8059551dbc9d2694b8c7bf07fd72cb56a2ff458ea7ad3bbd2
  thm:sz-v2-kls: f5dfe05f2a9880082765a4f61d7fd0cfd36cc8e259615b54280e37b1380ee16e
  lem:sz-analytic-foundations: e3b0250c18499cbdf58b3cb609937032b0101d8aa096aac355555309e5e94d3f
---

## Findings

Independent full certify review of the three fingerprinted dossiers. This
reviewer was launched with a fresh context containing paths and an audit
mission, without the authoring conversation, and authored none of the proof
text. The author's identity and unrecorded model were confirmed by the
orchestrator. Corrections requested during examination were made by the
author/orchestrator and reread before fingerprinting.

The following conclusions each pass:

| Dossier | Canonical conclusions certified |
| --- | --- |
| `solutions/sz-v2-small-loss.md` | [](#lem:sz-v2-profile-calculus), [](#lem:sz-v2-profile-refinement), [](#prop:sz-v2-small-loss) |
| `solutions/sz-v2-summable-budgets.md` | [](#lem:sz-v2-profile-threshold), [](#prop:sz-v2-summable-budgets) |
| `solutions/sz-v2-kls.md` | [](#thm:sz-v2-kls) |

The canonical statements follow with their specified quantifiers: universal
constants are fixed before the finite chain length, margins, orders, terminal
depths, dimension, and law. The refinement lemma permits a fixed bounded offset
range, with only its additive allowance depending logarithmically on that
range. Its coefficient-cap assertion is proved, rather than assumed.

### Scalar estimates and initialization

I checked the tower thresholds, finiteness of the discrete stopping index,
integer nonexpansiveness, disappearance of the jump at three after taking
the maximum, and the forward-average derivative. The resulting Lipschitz
constants multiply under composition. Convergence toward four reaches the
constant interval in finitely many iterations, so the termination assertion
is exact, not merely asymptotic.

The fixed-power argument first bounds the unaveraged heights by a fixed
additive amount, then applies the remaining contractions; its error is
therefore proportional to $4^{-m}$. The sum/product estimates and their
constant-branch versions follow. I checked the normalized-logarithm burn-in,
including its lower bound at zero and its transfer-factor estimate. The
three-range sum is valid; the subsequent depth argument uses the stronger
explicit disjoint-range sum.

The initial prescribed-depth profile follows from the certified fixed-cost
height theorem with the least odd order above $\log(r+1)$. The common-radius
comparison supplies $\mathcal A\le\max\{1,C_P\}$, and the universal amplitude
absorbs normalization by $\varrho^2$ and the floor one. The large polynomial
starting threshold makes the chosen order and the inherited starting depth
admissible. This initialization does not require KLS or a uniform coefficient
conclusion.

### Near-unit depth induction

I checked (D1)–(D10), including the degree truncation and all first-exit
inequalities. Above the contradictory floor the finite-chain theorem supplies
one actual starting family, its retained prefix, its matched radius budget,
and the polynomial propagation bound. The actual-radius estimate gives
$\lambda\ge u/2$ because $C_P\le R+1\le z+2$ and the amplitude makes $z$
large. There is no substitution of this radius into an unrelated family's
budget.

For the low kernel, each inherited interval starts beyond its corresponding
$K_l$. Hence $\alpha_l k\ge\sqrt{C_{\rm cut}k}$; beyond the last interval
the same estimate uses $\epsilon$. Summing over disjoint degrees bounds a
single convergent series, with no factor for the number of caps. The degree
one term belongs to the initial geometric range. The high kernel tail follows
from the fixed-depth transferred coefficient cap and the choice
$k_0\ge100\xi^{-1}\log(M_0/\xi)$.

The coherent-root estimate separates degrees at
$N=\lceil D\epsilon^{-2}Q^2\rceil$. Monotonicity handles the initial segment,
the fixed polynomial growth cap handles the tail, and $Q\ge C_Q\epsilon^{-4}$
absorbs the remaining polynomial prefactor into $e^\epsilon$ after taking
the root. The extra minimum with the first height-stage coefficient bound
provides that growth cap without changing any floor.

The gap between the exponents $20\epsilon$ and $7\epsilon$ pays the fixed
constants in (D10) through $\epsilon Q$, not through a fixed multiplier at
every stage. In particular $a_Qu^Q\le p/2048$ and the retained losses justify
the initial short prefixes. Before a possible first exit the required
normalizers are at most $bu$. The delayed loss estimate gives
$P_N\le(17/56)p$ through the contradiction horizon; the matched budget at
time $m$ then has strictly positive discrepancy
$up(1-2c-cp)$ with $c=17/56$.

The chosen dyadic terminal degree satisfies the logarithmic tail requirement.
The propagated coefficient estimate contradicts the curvature inequality at
that degree. The terminal-distortion lemma and
$\log(b^4e^\xi)\le Q^{-1}\log(1+1/s)$ advance the depth. The product of all
remaining distortions is at most $e^\epsilon$ from a depth of order
$\epsilon^{-1}$. This proves the entire finite depth induction at cost
$e^{21\epsilon}$.

### Coefficient return and the two outer inductions

The profile hypothesis is uniform over the law class at each fixed depth, so
static transfer applies to it. Burn-in and the squared transfer factor fit
within the extracted cap's $e^{3\delta}$ allowance. No continuity of the
common-radius supremum is used.

I checked the low/high height split in (E3)–(E8). At low height, fixed-power
costs are paid before using Lipschitz continuity for the additive variable
$y=\log(s)/Q$. Division by $e^y$ absorbs that variable with coefficient one.
At high height the selected extraction order is at most $h$ for $y\le1$ and
at most $h(1+y)$ otherwise. The explicit iterated-height product argument
gives the stated additive $5y$, absorbed after taking cube roots because the
retained offset is at least five. The depth used for extraction is itself
admissible for the chosen order.

The next depth induction is initialized separately: the preceding outer
stage at a smaller admissible order handles high heights, while the original
retained profile handles low heights. Thus coefficient return alone is not
being mistaken for initialization. Old floors are controlled individually by
the hypothesis, the newest floor by (E7), and the initial seed floor by its
specified alternative in the one-cap case. The $\delta$ cost is paid once,
and the $\epsilon$ cost per outer round is $e^{24\epsilon}$.

For the small-loss profile, the choices
$j=\kappa(r)$ and $\epsilon=\delta/(j+1)$ permit $Q\le r$ and the required
starting-depth inequality once $r\ge C_R\delta^{-12}$. They give
$t_j(Q)\le3$, order cost at most $e^\delta$, and total round cost at most
$e^{24\delta}$. The product allowance and the constant branch turn the next
profile into precisely the required height with increment $2D4^{-m}$.
The simultaneous choice $D\ge C\log(e+D)$ is finite and universal.

For the summable profiles I checked both threshold-absorption inequalities,
the exact retained caps, the polynomial bounds on old floor arguments, and
their payment from the next offset and amplitude increments. Each old floor
is bounded by the current amplitude times $(4+S_i)^{1/3}$; their count adds
no cost. The same admissible finite order/depth choice closes the next stage.
The additive costs are at most $B2^{-i}$, the multiplicative costs at most
$e^{41\alpha_i}$, and $C_A\ge42$ suffices. The logarithmic dependence of
the remaining allowances on $B$ permits one finite universal choice before
induction. The two geometric sums give the exact canonical uniform bounds.

### Final composition, hypotheses, and dependencies

For a fixed regular law, finite termination chooses $i$ after fixing
$x=\max\{1,a^{-1}\}$, then the canonical threshold lemma controls
$r=R_i+\lceil C_*t(x)\rceil$. Burn-in and the bounded amplitudes give a
universal common-radius bound. The factor $2^{85}$ is used only once,
after all refinements. Weak approximation passes a scalar Poincare inequality
on compact smooth tests. The clipping argument bounds the means using a ball
of positive mass, proves $L^2$ integrability by monotone convergence, and then
passes variance to the limit. No supremum over degrees, depths, or cap lists
is passed through weak convergence.

The hypotheses used are: the specified scalar definitions and integer
indices; a fixed valid nondecreasing seed and coefficient majorants;
finite ordered margin chains in $(0,1/16]$; the explicit old and seed floors;
the uniform all-law initial profile; sufficiently large universal amplitude
and cutoff constants; centered regular laws with covariance at most $I$ and
positive lower curvature; and finally isotropy, log-concavity, local
Lipschitz regularity, and finite Dirichlet energy for the limiting statement.
All are stated in the canonical interfaces or their named dependencies.
There is no additional unrecorded hypothesis or needed `assumes` edge.

I compared the reconstruction directly with Section 9 of
[Song–Zhang v2](https://arxiv.org/html/2610.01447v2), using the supplied local
HTML and its parsed text, particularly Propositions 9.21–9.26 and their
displayed parameter choices and proofs. Their claimed conclusions were not
accepted as proof inputs. The analytic mechanisms delegated to earlier
certifications were checked against their canonical statements, including
static transfer, the finite-chain construction, delayed losses, terminal
distortion, the fixed-cost height theorem, and analytic approximation.

A traversal of the current dependency graph has 32 nodes and contains no
BKL node, `conj:kls`, or other already-proved KLS input. Its only open nodes
are the six conclusions certified together here. Their internal dependence
is acyclic; all external proof dependencies are proved. No proved fence is
violated and no unrelated open fence is discharged.

`UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py --impact` completed
successfully after the repairs, reporting zero changed items and no errors.
The grouped fingerprint command also completed successfully on the versions
recorded above. No numerical experiment was used as evidence.

## Corrections

None outstanding. During this review the author/orchestrator aligned the
two-ceiling definition of the retained caps, promoted the scalar calculus
and threshold bounds to explicit canonical interfaces and dependency edges,
and inlined the disjoint-degree and iterated-height product arguments.
The final dossier's additional Cheeger conclusion was removed, leaving the
exact canonical Poincare statement in this certification. All these final
versions were reread.

## Exclusions

This review does not recertify the internal proofs of already-certified
upstream dossiers, establish the whole Song–Zhang preprint, or review the
independent BKL route. It does not certify any further Cheeger comparison,
the separate canonical-target adapter, CMH or occupation assertion, or a
priority claim. No manuscript-prose sync audit is asserted.

## Proposed records

For each of the three rows in the scope table, mark its listed nodes
`proved`, preserve their existing `references` and `depends_on`, and add
the proof record with `artifact` equal to that row's dossier and `review`
equal to `research/reviews/2026-10-06-sz-v2-profile-review.md`.
No `assumes`, `bounded_by`, or `refuted_by` relation is added.
