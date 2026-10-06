---
verdict: pass
authors:
  - sz_v2_height, gpt-6-astra, 2026-10-06
reviewer: reviewer, gpt-6-astra, 2026-10-06
fingerprints:
  solutions/sz-v2-height-blocks.md: ee0440032d75af7bd25303befb5bd98deb1b8de1283615c3214b5495a0a4451c
  prop:sz-v2-height-reduction: 8b074fd671347e3be0c2e47c689462e5c590c8d5982687265fe27039d0562923
  def:sz-v2-common-radius: 49ae12dc3b61656251736c6d98ed212477348fbfdcfcb5ce82c490131854c2b7
  def:sz-v2-height-profiles: 96a140c2ad0f0d237038116dad4f24466bf9d91a72ccbd9b8a62e37f7b0d9482
  thm:sz-v2-iterated-curvature: a374bf920166e028978e9ada8311b0dadd8cfb1b4ef8850c846069900630a6ef
  prop:sz-v2-static-coefficient-transfer: bc15d851517e3f5214ddf15d70fc42328b860a6b0d5655ba0898aa0ee1d040c0
  prop:sz-v2-common-radius: 2ae867703ee8d57f0b0ca660a3af2ef8c37357725d7d5d66e3670c92014d1044
  lem:sz-v2-operator-block-primitives: bb09229db057bba3a2bdf944fb2c6fd59ee16aaba488b607a84e62a2bdc42a7e
  lem:sz-v2-normalized-hierarchy: c871dbe2a0195d11acb31e90e91b361b2f1f56848b52beab30b54bb6669dd499
  lem:sz-v2-mesoscopic-powers: e01550a65203ed00238ab57cafdde06aac331b358c0e36fcf4406fc897d33f7f
  lem:sz-v2-raw-joint-frame: 73908a712b09b92a0d81866a0dca7318e0087f1da0c377c7fa8316f748c01bc7
  lem:sz-v2-propagated-joint-loss: 1d476098d11506ee2dcf0690bcd96206b11e55b9bf597aaf41975db58b108e0a
  lem:sz-v2-orbit-green-restart: 9895497ca11d1b97f40ed5b61a9eb4a8a7c428b93df875da3750d32a1e439900
  lem:sz-v2-block-extension: bd4af255cd408a4f0dc48be3fc4bef8630d5237a50b24f5f3da600d42d7d569e
  lem:sz-v2-block-propagation: 8099f09f88ce91637389d0074c60ab6b76f8081d494dc38ab7cc71818e6fdccf
  lem:sz-v2-terminal-distortion: a9bba017a6789be19cac1518024a01c88a73b0d5cef8ee3b15bde4f73e416f83
---

## Findings

Independent full certification in a fresh context containing only the mission
and repository paths, without the conversation that produced the proof.
The author's identity is supplied by the assignment. This report passes
both canonical claims named by the dossier: terminal-degree distortion
and fixed-cost repeated height reduction. The latter has the required
quantifiers in dimension, measure, height stage, odd block order, and
inner depth; its coefficient conclusion includes nonsmooth measures and
singular covariance. The dossier's stronger requirement $r_*\ge2$
implies the canonical $r_*\ge1$ statement.

I checked the relevant proofs in the supplied full text of Song–Zhang,
arXiv:2610.01447v2, Section 8: the seed and scalar estimates, local orbit
and initialization mechanism, coefficient-majorant blocks, distortion,
full profile, and repeated height reduction. In particular, I read the
proofs of Lemmas 8.2, 8.14–8.15, 8.19–8.20, 8.23 and Propositions
8.22–8.25 and 8.1, rather than treating their assertions as imports.
The local proof uses an enlarged fixed floor in place of the near-unit
floor; I checked that adapted construction directly. Generic Green,
restart, extension, propagation and joint-loss interfaces are certified
in `research/reviews/2026-10-06-sz-v2-blocks-review.md`; their applications,
not a duplicate certification of their full proofs, are checked here.

**Seeds and moments.** Repeated Poincaré on Appell derivatives and the
certified static transfer give the original cap after $O(t(d))$ steps;
the perturbed logarithm remains in $[0,5]$ after burn-in. The threshold
spacing proves integer-shift stability through every height composition.
Product, fixed-power and self-power estimates give (B4)–(B5). Both
branches of the minimum satisfy the same comparison, so taking their
minimum preserves it uniformly in the amplitude and height stage.
With $y=\log(s)/Q$, the cutoff estimate reduces to boundedness of
$(1+y)^{1/3}e^{-y}$. The moment calculation for (B7) leaves only
constant-to-the-$Q$ factors, including bounded $Q^{2/Q}$.
Splitting the capped moment sum at $F^3$ gives a convergent geometric
part and the stated exponentially small tail, uniformly as $L$ grows.

**Actual initialization and extension.** The local raw frame is used
only with $z\le R$. Its delay ranges are $k,\ldots,4k-2$, all positive.
The separate quadratic frame supplies index two; its least standard
representation eigenvalue is $1-\sqrt3/2>1/8$. The original cap bounds
both kernel moments by $C/z$ and the weighted early coherent sum by
$C/z$. The terminal coherent term is exactly $\gamma b_{j-d+1}$.
Thus the Green lemma applies with one universal $K$. Its first-block
telescope also gives the first estimate in (B9), as can be seen by
absorbing $(K/z)D_1$ in the displayed first telescope of its proof.
The symmetric quadratic testing bound and (B10) supply every hypothesis
of actual restart. In particular, the resulting family retains its own
$z$-matched budget at every later index.

In extension, the retained prefix includes $2d-1<32q$. Consequently
(B2) has no intermediate coherent term. The first-exit normalizer is
bounded by $(1+1/64)u$ before it is used. The cap gives the uniform
kernel constant; $C_P\le z+3$ gives $\lambda\ge u/2$.
In the terminal estimate the apparent positive factor $F^6$ is canceled
using $F^6\rho^{d-1}=G(d)^6\rho^{d-4}$. The remaining geometric factor
with $d\ge8q$ dominates the polynomial. These are the hypotheses of
the certified block-extension lemma, with constants independent of $q$.

**Finite odd-order construction.** The base length $\lfloor R\rfloor$
has radius at least $R-C/R$ and a global factor at most two. Its
degree-sixteen initialization has the separately stated powers of $z$.
For subsequent orders, direct substitution of the length bounds gives
the exact powers in (B17)–(B18); $d\ge4p$ and the fixed seed ratio
$\rho\le C_3^{-2}$ control them uniformly in $p$. The same estimates
control the longer prefix and ensure $m\ge2d$.

At each step the existing decrement tail proves the new lower radius
before the new decrement ratio is bounded. Their geometric decrease
therefore is not assumed circularly. Lengths grow by more than four,
and the propagation costs are bounded by $C/F^4$. Greedy propagation
gives the envelope before the next initialization. Applying that old
envelope to the new exact length controls an upward radius change;
together with (B20) and rounding it gives the two-sided comparison
of length with its own new radius. Thus the next actual family exists.
Finally $m_Q\le R^Q$ and (B5) bound the static remainder by $z_Q$,
so the common-radius maximum supplies every coefficient degree at once.
The below-floor branch needs no family and satisfies all asserted
static comparisons. All choices precede the inner-depth induction.

**Distortion and full profile.** The first logarithm costs at most
$\log M$, and subsequent differences obey $F(v)=\log(1+\eta v)$.
Above two, $F(v)\le\log v$; below two, $F(v)\le\eta v$.
The burn-in bound therefore holds also for $1\le M\le e$.
For the terminal multiplier, the chosen $r_Q$ makes
$1+\log^*M\le r/2$ uniformly in $Q$. The resulting geometric error
and the $r^{-2}$ errors have a universally bounded product. This
proves the canonical terminal-distortion claim without analytic premises.

At any established depth the scalar static profile supplies the exact
coefficient-transfer premise; continuity of the block assignment is
unnecessary. Under (B27), the floor is excluded and the same actual
family is available. The cutoff splits the kernel into a geometric
seed part and an exponentially damped profile part. The latter is
small at the prescribed $k_0$, and (B7) controls the coherent root.
Every $Q$th root in (B31) is at most a fixed multiple of $M_Q$, so
one $A$ meets all the inequalities simultaneously.

I checked the finite comparison (B33), including the ceiling. If its
reverse holds, $(m+1)\tau\le p/4$ follows from
$a\le D_0+up$ and $a\ge12(u+D_0/p)\tau$. First-exit control gives
$P_N\le17p/56$, while all successor normalizers remain positive.
At time $m$, the lower bound on $aV_m$ contradicts the matched budget;
the difference is at least $up(1-2c-cp)>0$. No generic $R$ budget
is substituted. The terminal dyadic choice makes
$\log(24C_Fd/a)\le\delta d$, producing the strict contradiction.
For $a\ge1$ the certified curvature bound covers the floor branch.
The scalar increment is absorbed by $(r+1)^{1/Q}$, and the distortion
product closes finite induction at every depth.

**Height repetition and hypotheses.** The first profile starts from
the certified inner-curvature amplitude at $r_Q=O(t(Q))$. At stage $j$,
choosing $r=O(t(d))$ and the least eligible odd $k$ gives $k\le t(d)$,
$r_k\le r$, and $(r+1)^{1/k}\le e$ above one fixed threshold.
The exceptional bounded-height range uses the original cap, uniformly
in $j$. Static transfer yields the asserted coefficient estimate with
one $C_e$, for the full stated class. The next capped seed retains
all uniform comparisons. Its initial profile at the same $r_Q$ follows
from the preceding stage at order $k$; bounded $t(Q)$ uses order three.
Thus one fixed $C_*$ works for every height stage, with no stage-dependent
depth threshold.

The hypotheses used are centering, covariance contraction, smooth
uniform upper and positive lower curvature for the operator argument,
ordered finite families, the actual hierarchy and its zero convention,
nondecreasing capped coefficient majorants and their stated comparisons,
and the displayed block, normalizer, and smallness conditions. The
coefficient-transfer conclusion extends to all centered log-concave
covariance contractions. No additional hypothesis is required. Oddness
is used by the order induction; it is unnecessary for the isolated scalar
distortion estimate, a harmless strengthening opportunity. All external
dependencies are certified; terminal distortion is proved before its
use in the same dossier. No open dependency or assumption remains.
There is no attached `bounded_by` fence; the proof respects the brief's
uniform-admissibility restriction and makes no summable-loss conclusion.

The full `UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py` exited
zero, with no MyST error. The subsequent dossier `--fingerprint` command
produced the block above on the versions read.

## Corrections

None.

## Exclusions

This review does not certify Section 9 small-loss or summable-budget
profiles, the SZ KLS theorem, any limit in the height stage, or global
manuscript status prose. It does not recertify previously certified
analytic, polynomial, transfer, radius, block, or joint-frame proofs.
No BKL/KLS conclusion or coefficient bound derived from either is used;
the remaining factor $C_*^{j-1}$ is not asserted to stay bounded.
No numerical computation or run artifact is proof evidence.

## Proposed certification records

Set `lem:sz-v2-terminal-distortion` and `prop:sz-v2-height-reduction`
to `proved`, retaining their current dependencies and references, and
add to each:

```yaml
proofs:
  - artifact: solutions/sz-v2-height-blocks.md
    review: research/reviews/2026-10-06-sz-v2-height-review.md
```
