---
---

# Klartag–Lehec stopped-rank import reconstruction

Author: researcher_kl_rank, gpt-6-astra, 2026-10-01.

## Question examined

Mission lens: mine/prove. Reconstruct `thm:kl-stopped-rank-tail` and
`thm:kl-integrated-rank-covariance` exactly as used in
`modules/30-covariance-technology.md`, from the actual pinned
[Klartag–Lehec v2 HTML](https://arxiv.org/html/2507.15495v2) and
[PDF](https://arxiv.org/pdf/2507.15495v2), including their proof dependencies.
This is an import-certification preparation task on `certify-open-results`,
not a new portfolio route and not an attempt to infer KLS from thin shell.
The resulting author dossier is `solutions/thm-kl-rank-imports.md`, enumerator
`105.%s`. The two manuscript statement bodies are reproduced there verbatim.

## What we learned

- *Established (written argument, uncertified):* the dossier reconstructs the
  chain from the covariance SDE through source Lemmas 5.2–5.5 and Proposition
  5.1 to Corollary 6.1 and Theorem 6.2. The dependency map records printed PDF
  pages and source equation numbers. Both pinned representations were available.
  The one non-elementary geometric estimate accepted as an established input is
  `thm:improved-lichnerowicz`, not a 2026 preprint consequence.
- *Established (written argument, uncertified):* the stopped Itô identity is
  sufficient in its absolutely continuous/a.e. form. The source's notation
  asserting a derivative at every fixed time should not be repeated literally
  for arbitrary stopping times. The growth inequality is integrated over positive
  time intervals and requires only the a.e. identity.
- *Established (written argument, uncertified):* a positive polynomial
  interpolation supplies the exponential/quadratic potential with coefficient
  `64` instead of the source's `12`. Endpoint values and two derivatives match;
  the derivative bound is explicit. This removes reliance on the source's final
  “elementary exercise” in Lemma 5.5 without altering either target statement.
- *Established (written argument, uncertified):* bounded tilt moments give a
  direct exponential-martingale proof of the qualitative initial exit estimate.
  Its constants may depend on the fixed law and dimension. They occur only in
  the vanishing terminal remainder, so the final tail constant is universal.
  No uniform initial operator-norm window is needed.
- *Established (written argument, uncertified):* the rank first-hit event gives
  the factor `n/k`; layer cake gives the logarithmic inverse second moment,
  including `k=n` and an infinite hitting time. A pathwise split at the first hit
  bounds the time integral, and the decreasing integrable rank profile sums to
  a universal multiple of `n`. Eigenvalue crossings cause no ambiguity because
  the rank is reordered at every time.
- *Observed (source/structure, not numerical evidence):* Theorem 6.2's reference
  to Corollary 4.10 imports notation only. Its proof does not depend on the
  parallel-coupling transport or negative-Sobolev arguments. The thin-shell
  theorem is downstream of the integrated estimate, not an ancestor.

The mechanism and bottleneck for each target, and the hypothesis-usage table,
are in the dossier. Compact support is used for the ODE and stochastic
integrability as well as the terminal limit. Log-concavity supplies the tensor
bound and covariance cap; isotropy fixes the initial thresholds. All stopping
is relative to the Brownian filtration. There is no extension to anticipative
times, noncompact laws, arbitrary initial covariance, or oriented sources.

## What resists

No source-access gap remained for the sections used. The source's sharper
auxiliary interpolation coefficient `12` is not proved by the replacement
construction; the dossier explicitly records this exclusion in a `prf:remark`.
The pointwise derivative wording is also addressed in a `prf:remark`.
Neither excluded auxiliary assertion is needed by the written target arguments.
The published improved Lichnerowicz and standard Prékopa–Leindler inequalities
remain external inputs. This is not a claim that their proofs were newly
certified in this mission.

Independent mathematical review remains necessary, especially for the
nonsmooth projected-measure approximation, spectral Hessian at collisions,
three-index accounting in the growth estimate, replacement interpolation, and
universal-constant bookkeeping through the terminal limit. The author assigns
no verdict and makes no ledger transition. Neither target had a `bounded_by`,
`depends_on`, or `assumes` edge in the ledger read for the task. The manuscript's
orientation warning and the brief's thin-shell/KLS distinction remain intact;
none of `conj:trace-upgrade`, `conj:mm-spectral-occupation`, or
`conj:stein-weighted` is discharged.

## Proposed next step

Pass the following assignment to a fresh independent reviewer; no subagents
were used in this author session:

> Read `SPECIFICATION.md`, the researcher identity above, the two target
> directives in `modules/30-covariance-technology.md`, and
> `solutions/thm-kl-rank-imports.md`. Check the complete pinned-v2 proof chain
> against Proposition 5.1, Corollary 6.1 and Theorem 6.2, following every row of
> the dossier's source dependency map. Check the established improved
> Lichnerowicz input and its nonsmooth projected-class application; the stopped
> covariance SDE and spectral Hessian including collisions; all index regions
> in Lemma 5.4; the explicit polynomial cutoff replacing Lemma 5.5; a.e.
> Gronwall; the fixed-law terminal limit and dimension-independent surviving
> constants; and the hitting-time, layer-cake and rank-integration endpoints.
> Preserve the exact compact isotropic log-concave class, Brownian filtration,
> threshold 3, exponent 1/8, inverse-moment power 16 and integration interval
> [0,1]. The two targets have no explicit ledger fences; exclude all orientation
> and KLS conclusions. Assess the author's two auxiliary-source qualifications
> rather than assuming the source's availability establishes validity. Run the
> full checker and fingerprint the stabilized dossier and relevant statements
> before recording an independent review. Do not treat this checkpoint or a
> successful structural check as certification.

The full checker was run as requested with
`UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py`. Its sandboxed run failed
at Node startup and consequently could not load manuscript anchors. The tool
escalation rerun completed successfully after the dossier was written and listed
it as an uncertified draft. The checker was not changed. This checkpoint adds
no numerical run, candidate, portfolio transition, or proposed status delta.

```yaml
files:
  - solutions/thm-kl-rank-imports.md
  - research/explorations/2026-10-01-kl-rank-imports.md
deltas: []
next: |
  Perform the independent review specified above and in the dossier's closing
  handoff. The author has not certified either target.
```

Final-check addendum: after this checkpoint was added, the escalated full checker
completed with one error outside this mission's write surface:

```text
FAIL prop:weighted-spectator-obstruction.proofs[0]: the statement of 'ass:weighted-package' changed since research/reviews/2026-08-27-prop-weighted-spectator-obstruction-repair-proof-review.md fingerprinted it; it needs a new review
```

The earlier successful check and this later failure are distinct runs on the
shared working tree. No affected manuscript statement, review, or fingerprint
was edited by this author. The final run reported no error on the new dossier,
which remained listed as a draft. A direct comparison also confirmed that both
new theorem bodies exactly match their manuscript bodies. Resolving the unrelated
fingerprint failure belongs to the orchestrator and an independent reviewer;
this author has not altered their files or tried to refresh their fingerprints.
