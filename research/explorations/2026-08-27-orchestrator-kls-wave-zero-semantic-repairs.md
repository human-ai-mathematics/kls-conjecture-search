# Wave-zero semantic repairs

Date: 2026-08-27  
Owner: orchestrator  
Program: KLS  
Type: manuscript/ledger synchronization

## Purpose

The wave-zero proof-mining audit compared the KLS manuscript against the current standalone
dossiers and their persisted reviews.  It found four proof-presentation defects and one scope
defect.  These are repairs of already stated mathematics, not new KLS progress.  In particular,
no open gate is discharged and no mathematical status changes in this synchronization pass.

## Repairs

### `lem:stein-vs-source`

The manuscript statement now records the range $0<\eta\le 1/4$ used in the proof to keep
$s_t=p_tq_t$ uniformly away from zero on $\{t<\tau_\eta\}$.  The ledger statement now exposes
the same range and both conversion inequalities.  The underlying dossier already used this
hypothesis.

### `prop:qcts-equivalence`

The converse no longer invokes a randomized median on an auxiliary probability space.  For a
full-dimensional isotropic log-concave law and nonzero symmetric $M$, the quadratic polynomial
$x\mapsto x^TMx$ is nonconstant and its level sets are Lebesgue null.  Its law is therefore
atomless, so a deterministic median cut has mass $1/2$.  The proof then identifies the color
correlation with $\mathbb E|Y-m|$ and applies the quadratic reverse-moment inequality.  The
ledger statement has been expanded to record the exact two directions of the equivalence.

### `thm:bootstrap`

The manuscript now preserves the sign of the bracket multiplied by
$\rho=h_n^\star/h_\mu$.  When $1-P-Y/2\ge0$, near-worstness supplies the desired lower bound on
$\rho$; when it is negative, nonnegativity of the posterior perimeter term gives the target
estimate directly.  The exit estimate is also written for the stopped continuous martingale,
with the hitting event, martingale isometry, and bracket bound explicit.  The ledger statement
now includes the pointwise estimate, exit estimate, integrated consequence, and optimized
$T^{4/3}$ form.  A fresh cold review is required for semantic agreement of the repaired
manuscript with the dossier.

### `lem:inf-martingales`

The fixed-family argument now uses the noncompact statement actually available from
`lem:perimeter-martingale`: each fixed-cut perimeter is a supermartingale, with equality only
under compact support.  Conditional expectation followed by the fixed infimum still proves the
claim.  The competitor family is stated to be nonempty and countable, which supplies
measurability, a common null set, and an integrable upper bound for the infimum. An uncountable
family is covered only when a fixed countable determining subfamily is supplied; mere joint
measurability is not enough. The ledger no longer describes the inputs as martingales without
the compact-support qualification.

The dependency audit additionally makes `prop:trivial-excess` depend on
`lem:perimeter-martingale` and makes `prop:intro-audit` depend on `lem:half`; both edges are
used explicitly in their dossiers. The trivial-excess ledger statement now records isotropy,
log-concavity, half mass, and finite perimeter rather than advertising a broader theorem.

### `prop:persistent-splitting`

The manuscript and ledger now require product factorization of the effective support together
with additive factorization of the extended-valued convex potential.  Additivity only on the
interior of a non-product support would not make the localized posterior a product.  The
repaired standalone dossier states this globally with proper lower-semicontinuous factors and
positive finite normalizers; its current bytes are undergoing fresh review together with the
other five nodes sharing that artifact.

### `thm:budget`

The ledger summary now makes the balance range and the stopped process scope explicit.  The
standalone product-covariance dossier separately defines the coarse balance exit time and adds
the missing finite-moment/nontrivial-mass hypotheses to `lem:block`.  Manuscript and ledger
certification will be integrated only after a fresh cold audit of the whole coupled artifact.

The same synchronization makes the domain of `lem:block` explicit (finite second moment and a
nontrivial $J$-measurable cut), replaces the informal word “balanced” in `cor:refutation` by
$p_0\in[2/5,3/5]$, and prevents the product clause of `thm:covariance-bound` from accidentally
importing that cut-balance hypothesis when it needs only the product measure class.

The Klartag--Lehec covariance-spike attribution in the same module is corrected from two-sided
to centered one-sided exponentials, which is the family in their Proposition 65.  The separate
two-sided-exponential `q:alignment` question is left unchanged; the cited result does not supply
its answer or a persistent path event.

## Certification discipline

The edits above preserve the existing ledger statuses while the changed coupled dossiers have
`checked_by: none`.  Prior reviews remain historical evidence for the old artifact bytes; they
do not certify repaired files.  New review records must precede any restoration of
`checked_by: agent` or replacement of active `review` pointers.  The structural ledger checker
remains green after the synchronization, but that is not treated as semantic certification.

## Validation

- `python3 research/check_ledger.py`: 0 errors across 180 nodes after the repair set.
- `git diff --check`: clean at the synchronization checkpoint.

## Literature metadata

The source audit also retires citation debt without changing any mathematical status:
`KLnotes` now carries its published *Bulletin of the AMS* metadata and DOI;
`KlartagLehec2025ThinShell` records version 2 dated 23 February 2026;
`MikulincerShenfeld2021BrownianTransport` carries its 2024 *PTRF* publication metadata; and the
published Bobkov--Chistyakov sharp one-dimensional density--variance reference has been added
for the spectator argument's quantile-perimeter bound.

Two source-checked Klartag--Lehec v2 results are also imported as
`thm:kl-stopped-rank-tail` and `thm:kl-integrated-rank-covariance`.  They are deliberately left
without dependency edges to live KLS gates: rank-indexed eigenvalue occupation is genuine new
input, but it supplies no orientation of $K_t$, $H_t$, or a spectral source in the moving high
eigenspaces.  Their classification remains `preprint-unreviewed`.

The published covariance-spike node is sharpened to the fixed-time event level actually proved
for centered one-sided exponential products, and the Bobkov--Chistyakov density--variance lemma
is imported at its exact sharp constants.  The event is not described as persistent in time;
the proposed weighted-excess obstruction must integrate deterministic-time estimates by
Tonelli.

The previously undefined phrase “near-Cheeger” in `ass:weighted-package` and `q:weighted` is now
replaced by the exact additive condition $e_0\le1$ used in the certified consumption proof. A
new open target, `prop:weighted-spectator-obstruction`, records the stronger proposed negation
for arbitrarily small additive *and* relative excess. Its status remains open pending a
standalone dossier and independent review; no weighted gate is marked refuted at this stage.

## Outcome

The manuscript and ledger now expose the hypotheses and case distinctions already required by
the proof mechanisms.  No KLS conjectural gate or conditional assumption changed status.
