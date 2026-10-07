---
verdict: pass
authors:
  - plan_sz_architecture, unknown, 2026-10-06
  - sz_v2_height, gpt-6-astra, 2026-10-06
reviewer: reviewer, gpt-6-astra, 2026-10-06
fingerprints:
  solutions/sz-v2-block-foundations.md: eeec9ebdc985d8e16213bf897af9da6e175816f96a0f2528ac16127df65d9947
  lem:sz-v2-orbit-green-restart: 9895497ca11d1b97f40ed5b61a9eb4a8a7c428b93df875da3750d32a1e439900
  lem:sz-analytic-foundations: e3b0250c18499cbdf58b3cb609937032b0101d8aa096aac355555309e5e94d3f
  lem:sz-v2-normalized-hierarchy: c871dbe2a0195d11acb31e90e91b361b2f1f56848b52beab30b54bb6669dd499
  lem:sz-v2-skew-credit: e9510673a1e46fd5d998b3b77b212371ad779546264a1b2f0db5a68e585ea5c3
  lem:sz-v2-block-extension: bd4af255cd408a4f0dc48be3fc4bef8630d5237a50b24f5f3da600d42d7d569e
  lem:sz-v2-operator-block-primitives: bb09229db057bba3a2bdf944fb2c6fd59ee16aaba488b607a84e62a2bdc42a7e
  lem:sz-v2-block-propagation: 8099f09f88ce91637389d0074c60ab6b76f8081d494dc38ab7cc71818e6fdccf
  solutions/sz-v2-joint-loss.md: c1004fbe3a49b9fe7388066a37d27e547bcb338dc17ed851d90f9c4b2b40c94e
  lem:sz-v2-raw-joint-frame: 73908a712b09b92a0d81866a0dca7318e0087f1da0c377c7fa8316f748c01bc7
  def:sz-v2-common-radius: 49ae12dc3b61656251736c6d98ed212477348fbfdcfcb5ce82c490131854c2b7
  lem:sz-v2-joint-frame: aaf5c36182ce8cdc5e342504d9f86ea34e8ed764bf63b01f6b3ad29edbb1bc2d
  prop:sz-v2-common-radius: 2ae867703ee8d57f0b0ca660a3af2ef8c37357725d7d5d66e3670c92014d1044
  lem:sz-v2-propagated-joint-loss: 1d476098d11506ee2dcf0690bcd96206b11e55b9bf597aaf41975db58b108e0a
  solutions/sz-v2-chain-blocks.md: f634bfa6a6b2d1a6837dd342537db924efd5a20605badab108f0830b3fc16ed4
  prop:sz-v2-finite-chain-blocks: 9f8e06931ebd02c5e2c98d41b058cececa4926b2a70382378c73ea93e7442c8a
  thm:sz-polynomial-variance: ffd52798e616ccd22bb3e4c78d5c382fd5657d3b598e6e4ec3c9afc4f696da8e
  thm:letwin-qcts: 8e2ac0819f46db553fe83a6f3034436816565262316c2e6bde7d81baead1a082
  lem:sz-v2-mesoscopic-powers: e01550a65203ed00238ab57cafdde06aac331b358c0e36fcf4406fc897d33f7f
---

## Findings

Independent full certification in a fresh reviewer context, with repository
paths and an assignment but no authoring conversation. The author identities
above are those supplied by the assignment. This grouped report passes all
three fingerprinted dossiers and all six of their canonical claims. The
finite-chain statement is checked for its stated $N\ge1$ and odd $Q\ge3$.

The source comparison used the supplied full text of Song–Zhang,
arXiv:2610.01447v2, especially Lemmas 8.11–8.13, the local-frame and
two-block calculation around (235)–(237), Lemmas 9.3–9.5, and Proposition
9.23 and its proof. These source arguments were checked, rather than treating
their assertions as established imports. The proof inputs from earlier
repository certifications were checked against their canonical statements;
their complete proofs are outside this review's scope.

**Green estimate and restart.** Both finite block telescopes are valid,
including the second-block terminal estimate from $b_{2m}\le1$. The
Dirichlet Green kernel gives $1-b_q$ with the stated sign. Reindexing the
convolution costs its first moment as well as its mass. Absorption gives
the upper orbit bound before it is used to control the window weights.
The shifted Green kernel is dominated by the triangular window count,
which gives the lower bound. Replacing the full triangular count by the
$J$-window count preserves its Lipschitz constant and yields the asserted
$C/z+C\gamma Jm$ estimate.

The restart has $S_0=S_1$ and decreasing $S_k$, so $U$ is one unit family
with energy at most $u$. Dirichlet orthogonality of skew linear fields to
the genuine gradient $U$ gives the claimed skew credit; its Dirichlet
projection has squared norm $\beta^{-1}-e^{-1}$. This proves positivity
and the stated successor-energy bound. The successor direction is exactly
$B^{1/2}\mathcal T^2\mathcal W$. Its successive loss fractions are the
same family's $C_k/(zS_{k+1}+C_k)$, with $S_{k+1}\ge m/4$ on the required
prefix. The two length and coherent-smallness assumptions give the stated
$C\kappa u^p$ bounds. At every later nonzero index,
$v_{j+1}/e_j=zS_{j+3}/S_{j+2}\le z$; this establishes the actual
$z$-matched budget, including the absorbing-zero convention. No substitution
of $z$ into a generic $R$ budget is made.

**Extension and propagation.** The delayed term at a putative first exit
only requires the earlier prefix. The inequality
$(1-2C_\theta u)P_N\le K_qu^q/4$ gives $P_N\le p_*/3$, and includes
the stated short-prefix hypothesis. Thus normalizers are not assumed to
remain valid indefinitely. The conversion to powers uses the exact loss
fractions and $\eta_j\ge\lambda$, followed by the Bochner/Cauchy–Schwarz
ratio recurrence. Its lower ratio is positive under the stated thresholds.
For propagation, greedy division leaves a remainder shorter than $m_0$;
the geometric decrement tail bounds each nonzero digit's logarithmic cost
by $2\eta$. Counting only levels with $m_l\le h$ proves the stated
logarithmic envelope, also for $s=0$ and $h=0$.

**Joint frames.** Iterated Appell testing with full symmetrization proves
(B3) with the factorial and $z$ powers shown. The first $k$ slots are
symmetrized; the next $3k$ slots are the remaining derivative slots.
All fresh defect indices are at least one since $k\le d/2$ and
$j\ge2d-1$. Adjacent sorting, the joint-frame weight $C_Fk^2$, and
Cauchy–Schwarz give exactly the upper coefficient $108C_Fk^5$.
Global, local, and polynomial propagation charge the whole string of
older-slot maps. The corrected local variant uses $R/z\ge1$.

For normalized losses, repeated testing retains the scalar normalizers of
the complete original family. Expansion of the Dirichlet square gives
$\|\nabla z^i\|^2=\chi_i/\beta_{i+1}$, hence the fresh swap bound.
The convolution mass and $(3k+1)^{2\alpha}\le16k^2$ give
$5184C_FE^2k^8$. A prefix $j<N$ uses defects only through $N-3$.
Each nonterminal dyadic degree is used at most $2k$ times, and the first
$J$ losses remain actual losses. This proves the delay and startup terms
of (B2), including the terminal and short-prefix cases.

**Finite chains.** The intervals in the degree-sum proof are disjoint;
each finite interval starts beyond its own $K_i$. Its damping is bounded
by a single summable $k^M e^{-b\sqrt{Lk}}$ series, with no sum of constants
over the bands. The cutoffs $\Xi_i$ are nondecreasing and dominate
$K_{i+1}$. For every tested degree, the cap $G(X^X)$ applies because
$d_p,e_p,J_p\le Cp^{3/2}\le X$. The raw kernel has the claimed mass and
first moment; the early coherent term has its additional $k^6$ weight.
The exceptional quadratic coefficient is uniformly bounded: whitening
the certified quadratic inequality gives $c_2^2\le2$ for covariance
contractions. The degree-two identity also supplies the omitted $j=2$
raw estimate and the first symmetric restart loss.

At first exit, the hierarchy inequality bounds all needed normalizers by
$u/[(1-a_qu^q)(1-p_*)]\le\beta u$. Apply (B2) with
$d_0=d=e_q$; its retained prefix is contained in $J_q=4e_q$, so no
additional startup term is lost. The absolute gap implies
$\lambda\ge1/(R+1)\ge u/2$. The earlier coefficient bands have margins
at least the current margin, and the last band uses the explicit
$1+\epsilon$ radius margin. This verifies (F2). Substitution in the
terminal term gives (F3), including the cancellation of the positive
power of $F$. The analogous two initialization expressions have the
displayed powers, and their exponential decay dominates the residual
polynomials uniformly in the chosen band. The fixed-degree base $Q=3$
is covered separately; no large-degree estimate is used at that base.

The order induction first obtains its lower radius from the common-radius
maximum, or from the old decrement tail and current bridge when
$R\ge2\mathcal A$. It then obtains the new decrement ratio and length
growth. Mixed-radix propagation therefore precedes the new Green argument.
Its finite-prefix global factor controls an upward radius step and gives
the length comparison needed by restart. Rounding is harmless because
the real lengths are at least $F^24^{q-1}$. The branch below the floor
asserts only the radius, as required. All thresholds can be fixed before
the finite number of retained floors is chosen.

**Hypotheses, dependencies, and build.** The arguments use the stated
regular centered covariance-contraction class, ordered finite families,
the actual hierarchy, its spectral gap and absorbing-zero convention;
the sequence lemma uses its explicit nonnegative sequences, finite delay
kernel, endpoint/shift conditions, and smallness assumptions. Extension
uses its delayed estimate through first exit. Propagation uses the exact
finite-block norms. Joint losses use the specified power envelope and
normalizer bound; the local raw variant additionally uses $0<z\le R$.
The chain uses the fixed seed bounds and threshold, majorant ordering,
monotonicity, ordered margins, cutoff definitions, and above-floor branch.
No extra hypothesis is needed. The abstract sequence and propagation
lemmas do not need the analytic hypotheses; oddness of the order is not
needed by the abstract restart or extension calculation, but is retained
for their application. These are harmless possible strengthenings.

All dependencies outside this group are already certified. Within the
group, the chain uses the other five proved implications, in an acyclic
order. There are no open external dependencies or assumptions. No
`bounded_by` edge is attached to these nodes; the arguments respect the
actual-family and matched-budget restrictions. The full
`UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py` exited zero,
with no MyST error. The fingerprints above are the output of the grouped
`--fingerprint` invocation after the correction was reread.

## Corrections

During this review, the local raw-frame variant at
`solutions/sz-v2-joint-loss.md:37` and its canonical statement were
restricted to $0<z\le R$. The proof at line 94 now explicitly uses
$R/z\ge1$ before bounding every shorter propagation by the longest one.
I checked the corrected statement and proof, and the unchanged global and
polynomial variants. The unrestricted local variant was not proved and
is not certified. No other correction is required.

## Exclusions

This certifies the six named block claims only. It does not certify the
height-reduction, small-loss, summable-budget, or KLS conclusions, the
surrounding manuscript's global status assertions, or every statement of
the cited preprint. Previously certified analytic, polynomial, quadratic,
radius, tensor-frame, and mesoscopic-power proofs are used at their checked
interfaces, not recertified here. No numerical or run artifact is evidence.
BKL, KLS, and coefficient bounds derived from either are not inputs.

## Proposed certification records

Set the following nodes to `proved`, retain their existing relations and
references, and add the indicated artifact with
`review: research/reviews/2026-10-06-sz-v2-blocks-review.md`:

| Node | `proofs[].artifact` |
|---|---|
| `lem:sz-v2-orbit-green-restart` | `solutions/sz-v2-block-foundations.md` |
| `lem:sz-v2-block-extension` | `solutions/sz-v2-block-foundations.md` |
| `lem:sz-v2-block-propagation` | `solutions/sz-v2-block-foundations.md` |
| `lem:sz-v2-raw-joint-frame` | `solutions/sz-v2-joint-loss.md` |
| `lem:sz-v2-propagated-joint-loss` | `solutions/sz-v2-joint-loss.md` |
| `prop:sz-v2-finite-chain-blocks` | `solutions/sz-v2-chain-blocks.md` |
