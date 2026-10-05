---
{}
---

# Chen–Klartag imports: author derivation and source audit

Author: researcher_chen_klartag, gpt-6-astra, 2026-10-01.

## Question examined

Mission `mine/prove`, one of the preprint-import certifications: determine whether the
pinned Chen–Klartag v1 source supplies the exact statements
`thm:chen-klartag-moment-hessian`, `thm:chen-klartag-thin-shell`, and
`thm:chen-klartag-third-moment`, including the last directive's convex-body and
simplex clause. Work was on branch `certify-open-results`. This is authorship,
not review or certification. No portfolio route is changed.

## What we learned

*Established (written argument, not certified).* The new dossier
`solutions/thm-chen-klartag-imports.md`, enumerator `104.%s`, derives all three
conclusions and the convex-body clause. It records the manuscript statements,
normalizations, hypothesis usage, proof bottlenecks, external inputs and exclusions.
The pinned [HTML](https://arxiv.org/html/2607.23307v1) was available and read,
including the proofs in Sections 2–4 and Appendix A. Its mathematics was readable;
a PDF fallback for that source was not needed. The source locations are Theorems
1.5, 1.1 and 1.2, respectively, and Corollary 1.3 for convex bodies.

*Established.* The regular class is a bounded open convex target with density
$e^{-V}$ inside it, where $V$ is smooth convex and $V$ and all its derivatives are
bounded. It permits nonsmooth support boundaries and uniform measures; a smooth
full-support density is not by itself in this class. This agrees with condition
(2) of Klartag's published moment-measure paper. The dossier uses source $\psi$,
which is manuscript $\varphi$, and distinguishes it from the source's dual potential.

*Established.* The energy bootstrap first proves integrability using potential
sublevel cutoffs, then obtains the global balance, then applies entrywise
Brascamp–Lieb. It never assumes the integral of a formal Laplacian vanishes.
Cyclic averaging of the fully symmetric third derivative tensor yields the
nonnegative sum of squared eigenvalue differences. The coordinate change is
constant orthogonal at the point; derivatives of moving eigenframes are absent.

*Established.* The third-moment conclusion is a full ordered-triple Hilbert–Schmidt
bound, obtained by Bessel's inequality. Thin shell follows from the Stein identity
and the published Barthe–Klartag negative-Sobolev inequality. The source's lower
semicontinuity assertion is also justified directly using a supremum of continuous
quadratic variational functionals, so it introduces no dependency on the open
Klartag–Lehec import.

*Established.* Gaussian convolution, Gaussian damping and ball truncation,
followed by centering and covariance whitening, provide regular approximants
with convergence of all mixed moments through degree four. This extends the
moment conclusions without claiming convergence of Hessian squares. The explicit
exponential moment potential calibrates the Hessian constant outside the regular
class. Independent exponential moments and the exact Gamma cone transform verify
sharpness and the regular-simplex clause. No numerical run was used.

*Observed (tooling).* The first full checker attempt failed at the MyST subprocess:
Node could not execute npm under the sandbox (`EPERM`), leading to a misleading
npm-not-found/version message and consequent missing-anchor errors. The diagnostic
was a direct `spawnSync("npm", ["--version"])`. The authorized full checker was
rerun with tool escalation and `UV_CACHE_DIR=/tmp/kls-uv-cache`; it exited zero and
listed the dossier as an uncertified draft. Its log is the temporary file
`/tmp/chen-klartag-check-final.log`. The checker was not modified. A final full
check after creation of this checkpoint is recorded in the author's handoff.

## What resists

No mathematical step is left open by the author for the stated three imports.
Independent source-proof review is still required. Published background inputs
are explicitly invoked, not newly certified: moment-measure existence, regularity,
the bounded-Hessian theorem, Brascamp–Lieb, and Barthe–Klartag Proposition 10.
The author's PDF of Klartag's moment-measure paper and the author's PDF of
Barthe–Klartag were consulted for their hypotheses and applicable statements;
links and locations are in the dossier.

The argument does not establish a directional tensor constant, a Loewner bound,
CMH, KLS, a classification of all equality cases, or an arbitrary nonsmooth
moment-Hessian-square limit theorem. None of the three nodes has a `bounded_by`
entry. The brief's trace/operator and thin-shell/KLS distinctions are respected.
There is no external-source availability blocker.

Dependencies actually used internally: the Hessian conclusion for the two
consequences, supplied in the same dossier. No open Letwin, Klartag–Lehec, CMH or
other draft is used. There are no conditional `assumes` antecedents.

## Proposed next step

Assign a fresh independent reviewer, with no author conversation history, the
`certify` lens and the following verbatim assignment:

Read `SPECIFICATION.md`, `.codex/agents/reviewer.toml`,
`solutions/thm-chen-klartag-imports.md`, this checkpoint, and the three target
directives in `modules/04-family-moment-map.md`, together with their ledger entries.
Review the exact pinned source https://arxiv.org/html/2607.23307v1, including
Section 2, Lemmas 3.1–3.7, the approximation at the end of Section 3, Section 4,
and Appendix A. Check Theorems 1.5, 1.1, 1.2 and Corollary 1.3 against the dossier
and manuscript, not just the source's theorem statements. In particular check the
expanded regular class, published regularity/Hessian inputs, cutoff construction,
Fatou-before-integration ordering, form closure, fixed orthogonal-coordinate tensor
identity, all constants, ordered-triple norm, centered derivatives required for
Barthe–Klartag Proposition 10, moment convergence after whitening, and the
exponential and simplex equality calculations. Distinguish the regular Hessian
conclusion from its general distributional consequences. Check the dependency
closure and absence of any unstated open import; no bounded_by fences are attached.
No author-known gap remains, but identify any defect found rather than inheriting
this author's conclusion. Exclude directional/Loewner improvements, CMH, KLS and
unclaimed Hessian-limit statements. Record author identity
`researcher_chen_klartag, gpt-6-astra, 2026-10-01`. Write a new independent review
under `research/reviews/` and fingerprint the actual versions read. Only the
orchestrator may apply any resulting ledger change. The author proposes no
manuscript, bibliography, ledger or other-dossier edit.
