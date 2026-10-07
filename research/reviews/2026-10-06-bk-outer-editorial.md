---
verdict: editorial
amends:
  - research/reviews/2026-10-06-bk-outer-review.md
authors:
  - bk_powers, gpt-6-astra, 2026-10-06
reviewer: reviewer, gpt-6-astra, 2026-10-06
changes:
  solutions/thm-bk-appell-bound.md: {from: 005e053559713854bfc9112c01c93937dd2e8581041f8718d72d465ae5ee9f14, to: e667fd9ec1b3be81a41f6996e4027a6d6d57ec063eff4699cb1b155b23afcf7a}
  solutions/thm-bk-explicit-poincare.md: {from: 096fcce29cbaa6ba7ab7f1cd6ffc0b3534a9d39b0e49af09c44c4b83f702a54c, to: 48d85790f5674c6c63f029402bae71207adecdfc8eaa8070b0bca1e512444a1b}
---

# Editorial note on `research/reviews/2026-10-06-bk-outer-review.md`

This independent editorial examination read the diffs, not a fresh proof of
the outer theorems. The authoring conversation was not supplied. The checker
`uv run scripts/check.py --diff` identified exactly these two changed dossiers
and reported that neither historical dossier baseline could be found in Git.
I therefore used the supplied pre-cleanup snapshots
`/tmp/bk-appell-pre-cleanup.md` and `/tmp/bk-poincare-pre-cleanup.md`, computed
their normalized hashes with `checks.common.text_digest`, and verified exact
agreement with the two original report fingerprints. This verification, not
the author's description of the edits, establishes the comparison baseline.

The current `--fingerprint` command for both dossiers produced the `to`
values above. Every canonical statement and dependency fingerprint in that
output is identical to its value in the original report. The following are
the complete differences from the verified baselines.

## `solutions/thm-bk-appell-bound.md`

```diff
-This gives [](#thm:bk-appell-bound) once the stated inputs are established.
+This gives [](#thm:bk-appell-bound) using the stated inputs.
```

Why the mathematics is unchanged: both sentences identify the same
conclusion obtained from the same stated inputs; the edit updates their
verification status without removing any mathematical hypothesis.

```diff
-:::{prf:remark} Unresolved input status
-The scalar induction above is conditional on the stated integration calculus
-and reverse-transfer estimates. Their analytic construction, regularity,
-stopping, and approximation steps are separate proofs. This draft provides
-no certification of those inputs and no unconditional coefficient conclusion
-while they remain unestablished.
+:::{prf:remark} Dependencies and scope
+The scalar induction uses the separately proved integration calculus and
+reverse-transfer estimates. Their analytic construction, regularity,
+stopping, and approximation steps belong to those proofs. This dossier
+supplies the degree induction from those inputs; it does not replace their
+proofs or independent reviews.
 :::
```

Why the mathematics is unchanged: only a draft-status explanation becomes
an explanation of the same proof's scope after the independent operator and
localization certifications; no formula, quantifier, constant, hypothesis,
proof step or additional mathematical conclusion is inserted.

## `solutions/thm-bk-explicit-poincare.md`

```diff
-:::{prf:remark} Upstream scope
-This composition is conditional on the stated BK coefficient, integration,
-and approximation results. It does not supply their independent review, and
-cannot make the final conclusion unconditional before those inputs have
-been established.
+:::{prf:remark} Dependencies and scope
+This composition uses the separately proved BK coefficient, integration,
+and approximation results. It supplies the scalar conclusion from those
+inputs; it does not replace their proofs or independent reviews.
 :::
```

Why the mathematics is unchanged: the same three inputs and the same scalar
composition remain; the paragraph now records their certified status rather
than pending status. The coefficient input is certified in the amended
outer report, and the integration and approximation inputs have the separate
operator and localization reports. No dependency is silently discharged or
deleted by this wording.

This note carries the existing certification over precisely these editorial
edits. It certifies no new proof, source assertion or change outside the
listed diffs, and does not modify the earlier report.
