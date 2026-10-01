---
verdict: pass
authors:
  - claude-prover-w4p02, unknown, 2026-08-30
  - researcher_followup, gpt-6-astra, 2026-10-01
reviewer: reviewer, gpt-6-astra, 2026-10-01
fingerprints:
  solutions/prop-mm-window-occupation.md: 84396ef917be9eaa7bc45cf05f0a6f9e83424a6625d55416658d7c05c09100ed
  prop:mm-window-occupation: b13fcfb79f741c03ddd93e3c526e8022bd1a7c55efce5eac9a5126b0b1d292e1
  thm:KL-window: c8805f6f7be529a3a27f935a273c4a3253861fe59ebc6b52dc416a68cdd915f7
  thm:klartag-logn: 70dd5528111bc813bcfa6750d3afcfcdc31121dbf564fb0681db32265b576b60
  lem:mm-stopped-window-source: 295927719eb3106576e470f35a28a9aaf4b6ac8a1a7d8fb739e3249c202c8fb2
  lem:mm-restart-deweighting: ec93efcb1ac959a52ffa4388970b9434e653605ff400c9a1093346afda979f20
  lem:mm-smallgap-fourth-moment: 5efc054693b4557b794756da70c6b5a5ba03e38dc8bd743eca82855cc796d1df
  lem:mm-time-weighted-fixed-source: 661b4f05678efc9391f1738433880ef1c5188f8b10291ebbe2b7f9aa5cedeb46
  thm:letwin-qcts: 8e2ac0819f46db553fe83a6f3034436816565262316c2e6bde7d81baead1a082
---

# Occupation implication after the empty-branch clarification

## Findings

**Pass, for `prop:mm-window-occupation` only.** This review was conducted in a
fresh context, from the repository artifacts and the assignment, without the
conversation that authored the dossier. I read the specification first, the
reviewer role, the brief, both October 1 occupation checkpoints, the current
dossier and canonical statements, and the relevant companion material. The
historical joint review was context, not evidence for the present verdict.

### Statement agreement and exact scope

The two dossier theorems together imply the canonical proposition in
`modules/08-spectral-approach.md`: the same regular isotropic class, normalized
first eigenfunction, gap threshold, window, constants $34,0$, and all-law
$C_P\le C\log^2 n$ conclusion for $n\ge2$. Its source-only bound is slightly
stronger than the canonical occupation inequality, since the latter also
allows the nonnegative damping on the right. Time is nonnegative throughout;
the estimates containing inverse powers of $T$ concern $T>0$, while the
occupation statement at $T=0$ is the identity $0\le0$.

The scope correction is mathematically necessary and correct. The input
$C_P(\mu)\le K_n$ and the spectral characterization give
$\lambda=1/C_P(\mu)\ge1/K_n>3/(8K_n)$. Thus **the small-gap class is empty**.
There is no admissible eigenfunction to which this occupation implication
applies. Also $C_K\log n\le(C_K/\log2)\log^2n$ for $n\ge2$, so the
frontier conclusion already follows from the published input alone. The
separate stopped-source lemma has no gap restriction. The corrected overview,
scope bullet and uniformity remark accurately distinguish these facts.

### Steps checked

The strong-convexity exponential-moment domination gives continuous posterior
covariance paths. Compact-interval continuity makes the dense-time supremum
equal the actual maximum, so equality at the exit level is included. Isotropy
gives $A_0=I$ and hence $\tau_2>0$; $\{\tau\le T\}$ belongs to
$\mathcal F_\tau$. The restart dossier's optional-posterior identification,
innovation construction and deterministic solution map supply exactly the
forms used here. Its drift derivative is the covariance, bounded by
$\varepsilon^{-1}I$, so pathwise uniqueness identifies the planted and imported
localization laws.

Conditional Jensen gives
$v_\sigma^2\le\mathbb E[f(X)^4\mid\mathcal F_\sigma]$ on finite stopping
times. Multiplication by an $\mathcal F_\sigma$ event and the tower property
give the joint optional-projection inequality; no independence is assumed.
The tail calculation first truncates at $\delta>0$ and then uses monotone
convergence. The substitution $u=1/s$ yields exactly
$(T^{-2}+2\bar C/T+2\bar C^2)e^{-1/(\bar CT)}$.
For $T\le1$, $\bar C\ge1$, this is bounded by
$5\bar C^2T^{-2}e^{-1/(\bar CT)}$.

The derivative of $\log h$ and its zero limit at the origin show that the
defined $t_c$ is positive and universal; continuity includes the supremum
endpoint. The stopped-source dependency with $L=2$ pays $32T$. Restart,
Cauchy–Schwarz, the optional projection and the certified fourth-moment
implication pay at most $\sqrt2\,T h(T)\le\sqrt2T$. Thus
$(32+\sqrt2)T\le34T$, with no damping spent. The calculations are valid
conditional deductions even though their gap antecedent has no instance.

I also read the internal bridge argument in
`solutions/prop-spectral-sufficiency.md`; its dimension-free conditional
conclusion is not invoked. The vector filtering SDE gives the stated
$q$-identity. Here the source integral is finite and the posterior covariance
cap bounds the drift, licensing the stopped expectation passage. The crude
bounds $q\le\varepsilon^{-1}$ and $\mathbb E D\le\varepsilon^{-2}$ serve
only finiteness. Bessel gives $|g_0|^2\le1$, hence $q\le M_*$; the terminal
variance identity gives a lower bound $1/2$ at $T_*$. Posterior
Brascamp–Lieb and the fixed-test tower property give the upper bound
$\lambda/T_*$. The displayed $c_1$, $C_2$ and both branch inequalities have
the correct signs and powers of $\log n$.

The bridge's Gaussian smoothing, quadratic tilt and whitening converge in
$W_2$ at fixed dimension. Lower and upper Hessian bounds make the ground-state
Schrödinger potential confining, supplying compact resolvent. Weak convergence
passes the inequality on compact smooth tests; value truncation, spatial
cutoffs and mollification extend it to locally Lipschitz tests. The limiting
isotropic log-concave measure is full dimensional and has a density, as needed
for almost-everywhere gradient convergence. No eigenfunction limit or
dimension-uniform approximation is required.

### Inputs, hypotheses and fences

All seven ledger dependencies are proved with current records. Their canonical
statements supply the exact forms used: the supremum-in-time window; the
published $K_n$; stopped and restarted source bounds; small-gap fourth moment;
the time-weighted budget inside restart; and the all-law quadratic input with
constant eight. There is no open `depends_on` and no `assumes` edge. The Letwin
input is consumed as an already certified repository theorem, not imported
afresh from an unchecked preprint. Its source proof and the companion proofs
are not being recertified by this report.

The two direct published imports were checked against actual source texts:
[Klartag–Lehec, Theorem 61](https://arxiv.org/html/2406.01324v2) has exactly the
level-two supremum exit event and logarithmic-square window;
[Klartag, Theorem 1.2 and equations (1.4)–(1.5)](https://arxiv.org/pdf/2303.14938)
give the all-isotropic $C_P\le C\log n$ bound in the repository's convention.
The former source's Theorem 34 also supplies the Brascamp–Lieb forms used for
posterior covariance and terminal variance. No unavailable external source is
needed for the occupation assembly's certification.

Hypotheses used in the displayed assembly are $n\ge2$, smooth strong
log-concavity, centered isotropy, the regular spectral realization, a fixed
normalized first eigenfunction, the stated small-gap bound, the planted
channel with the usual observation filtration, and $0\le T\le T_0(n)$.
All are stated. The source assembly itself needs only a fixed centered
unit-variance test with fourth moment at most two; the eigenfunction and gap
hypotheses enter through that fourth-moment input and the bridge. For the
bare proposition, the published Poincaré bound already proves both its empty
implication and its weaker conclusion, so the longer chain is logically
redundant. This is a limitation, not a defect in truth.

There is no registered `bounded_by` edge. The proof neither replaces joint
expectations by products of marginals nor infers a universal-time covariance
bound. The covariance-spike obstruction is consistent with the shrinking
window: it rules out continuing this rarity mechanism to dimension-free
times, without asserting that the particular conservative window is sharp.
No projection-to-tensor promotion, relative-occupation premise, slice estimate,
moving competitor or trace-upgrade inference occurs.

### Build and fingerprints

`uv --cache-dir /tmp/kls-uv-cache run scripts/check.py` completed its MyST
check with no dossier error. Its only failure was the expected obsolete
occupation dossier fingerprint in the historical joint review. The fingerprint
block above was freshly generated with the same command and
`--fingerprint solutions/prop-mm-window-occupation.md` after the mathematical
examination. No old fingerprint was copied to stand in for that run.

## Corrections

None required for this certification. Replace only the occupation proof
record. Preserve the historical joint report and its separate stopped-source
certification.

## Exclusions

This is not a certification of any nonempty small-gap example, universal-time
occupation, `conj:mm-spectral-occupation`, KLS, an improved frontier, or a Lean
formalization. It does not renew the stopped-source record or the Letwin and
other companion records, and is not a global manuscript/brief sync audit.
No step required for the exact occupation proposition remains unverified.

## Handoff

Retain `status: proved`, the existing dependency list, and the absence of
`assumes`, `bounded_by` and `refuted_by` on the occupation node.

```yaml
files:
  - research/reviews/2026-10-01-window-occupation-empty-branch-review.md
deltas:
  - file: research/program/ledger.yaml
    node: prop:mm-window-occupation
    set:
      status: proved
      depends_on: [thm:KL-window, thm:klartag-logn, lem:mm-stopped-window-source, lem:mm-restart-deweighting, lem:mm-smallgap-fourth-moment, lem:mm-time-weighted-fixed-source, thm:letwin-qcts]
      proofs:
        - artifact: solutions/prop-mm-window-occupation.md
          review: research/reviews/2026-10-01-window-occupation-empty-branch-review.md
```
