---
verdict: pass
authors:
  - plan_framework researcher, unknown, 2026-10-06
reviewer: reviewer, gpt-6-astra, 2026-10-06
fingerprints:
  solutions/bkl-cumulant-energy.md: afbb7f43de962e4df2f4febe6ba70b96333bbad3257a20aea7472ca9a8ffb764
  lem:bkl-cumulant-energy: 87709dd0dbd422d53f71e28dd3c792839dfd771ebecd1b63059b65f898b556e8
  def:bkl-tilt-cumulants: 43636c8506cef53a8ed43a8231a955e160d704cc899cc248c5e08425ab5f449c
  lem:bkl-cumulant-dynamics: c6d9d767482c117e49dea11d360003958d8b5051e2d2fd8b37c193cbacf1dfcd
---

# Independent certification of the cumulant energy inequality

## Findings

**Pass for [](#lem:bkl-cumulant-energy).** The dossier proves both the
canonical differential estimate and its infinite-time consequence with exactly
the two stated integrability hypotheses. The numerical choice $C=17$ is valid.
The mission began in a fresh context without the authoring conversation, and
the reviewer authored no dossier in this dependency chain.

The actual source read was Bizeul–Klartag–Lehec, *Presenting a proof of the
Kannan–Lovász–Simonovits conjecture*, arXiv:2610.05474v1, Section 5, Lemmas
5.1–5.2 and their complete proofs, equations (80)–(93). The local HTML copy
`/tmp/bkl-2610.05474v1.html` has SHA-256
`fb51ab0d94171ac7de2a3009efb5249e44ee66de5c9a1dc5899bdb843de29df9`.
The reconstruction agrees with the source calculation and makes explicit the
terminal subsequence needed in its final limiting sentence.

### Agreement, hypotheses and dependencies

The tensor norm, fixed-vector convention and remainder are those of
[](#def:bkl-tilt-cumulants) and [](#lem:bkl-cumulant-dynamics). The latter
was registered as proved, with its independent review, before this report.
There is no open `depends_on`, no `assumes`, and no assigned `bounded_by` fence.

The proof uses finite dimension, compactly supported isotropic log-concave
initial law, the resulting positive covariance at every finite time, an integer
order at least three, and a deterministic fixed vector. The infinite-time
claim additionally uses finiteness of both displayed integrals. These
hypotheses all appear in the statement directly or in its explicit reference
to the dynamics process. The initial unit-vector restriction is removed by
the proof's degree-two homogeneity, including the zero vector. No regularity
of the initial density or dimension-free higher-cumulant bound is assumed.

### Line-by-line calculation and limits

The covariance congruence identity for $F$ is exact. Applying it to the
directions in its first and second differentials permits normalization of
the covariance at a single fixed point; no stochastic derivative of the
normalizing matrix is introduced or omitted. The inverse expansion on each
tensor slot gives the sum of the squared slot operators plus the square of
their sum, with coefficient one half. Self-adjointness and commutation on
different slots justify each inner-product identity. This checks all four
terms in the second-order expansion, particularly the cross term with
coefficient minus two.

The deterministic direction contributes $-(m+1)$ times the energy and minus
twice its pairing with the remainder. The noise directions contribute the
next-order energy, the covariance–cumulant cross term and two nonnegative
sums. Dropping those sums and applying Young's inequality leaves one half
of the next-order energy. The third-order matrix estimate bounds the sum of
squared slot-sums by $8(m-1)^2$ times the current energy, without a dimension
factor. Thus the loss is at most $m+1+16(m-1)^2$, which is at most $17m^2$
for every permitted order. All transformations of the remainder pairing and
the sum of the squared noise tensors use the full ordered-index norm and
give the exact claimed quantities.

The dynamics result supplies deterministic finite-order bounds and a true
square-integrable martingale on bounded intervals. The expectation step is
therefore justified before taking an infinite-time limit; it does not rest
on a merely local martingale. The cross integral is absolutely bounded by
the square root of the product of the two assumed integrals, by
Cauchy–Schwarz on time times probability. Finiteness of the nonnegative
current-energy integral supplies a deterministic increasing sequence of
terminal times at which its expectation tends to zero. Such times can be
chosen in successive unit intervals since their integrals tend to zero.
Monotone convergence along that sequence proves the infinite-time bound
and, at the same time, finiteness of the next-order integral. There is no
assertion of terminal decay at all times and no prior assumption of
next-order integrability.

The full command `uv run --cache-dir /tmp/kls-plan-uv-cache scripts/check.py`
completed with exit code 0 and no MyST errors after registration of the
dynamics dependency. The front matter is the actual output of its
`--fingerprint solutions/bkl-cumulant-energy.md` invocation. The canonical
statement and dependency remained the versions checked despite concurrent
edits to surrounding exposition.

## Corrections

None. No source or proof step required within scope remains unverified.

## Exclusions

This certifies neither the all-order cumulant induction nor the tilt-average
criterion, suspension, or KLS. It makes no noncompact-process assertion.
The two integrability hypotheses remain conditions of this lemma; their
eventual inductive discharge is a separate proof. No KLS estimate, general
Poincaré bound, or higher-order dimension-free estimate is used here.

## Proposed record and handoff

```yaml
files: [research/reviews/2026-10-06-bkl-energy-review.md]
deltas:
  - file: research/program/ledger.yaml
    node: lem:bkl-cumulant-energy
    set:
      status: proved
      proofs:
        - artifact: solutions/bkl-cumulant-energy.md
          review: research/reviews/2026-10-06-bkl-energy-review.md
    preserve:
      references: [BizeulKlartagLehec2026KLS]
      depends_on: [def:bkl-tilt-cumulants, lem:bkl-cumulant-dynamics]
```
