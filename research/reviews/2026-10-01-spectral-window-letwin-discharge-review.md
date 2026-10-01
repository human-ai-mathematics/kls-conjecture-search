---
verdict: pass
authors:
  - claude-prover-w4p02, unknown, 2026-08-30
  - researcher_followup, gpt-6-astra, 2026-10-01
reviewer: reviewer, gpt-6-astra, 2026-10-01
fingerprints:
  solutions/lem-mm-stopped-window-source.md: c93760397e864b2c3effa15b98b3360622365fb2971122f420e6b4fc156107ea
  lem:mm-stopped-window-source: 295927719eb3106576e470f35a28a9aaf4b6ac8a1a7d8fb739e3249c202c8fb2
  thm:letwin-qcts: 8e2ac0819f46db553fe83a6f3034436816565262316c2e6bde7d81baead1a082
  solutions/prop-mm-window-occupation.md: ea97284b9a34f7149536096b8e1af6bba054ad44da0d5ca68178a4c67ffb0f5f
  prop:mm-window-occupation: b13fcfb79f741c03ddd93e3c526e8022bd1a7c55efce5eac9a5126b0b1d292e1
  thm:KL-window: c8805f6f7be529a3a27f935a273c4a3253861fe59ebc6b52dc416a68cdd915f7
  thm:klartag-logn: 70dd5528111bc813bcfa6750d3afcfcdc31121dbf564fb0681db32265b576b60
  lem:mm-restart-deweighting: ec93efcb1ac959a52ffa4388970b9434e653605ff400c9a1093346afda979f20
  lem:mm-smallgap-fourth-moment: 5efc054693b4557b794756da70c6b5a5ba03e38dc8bd743eca82855cc796d1df
  lem:mm-time-weighted-fixed-source: 661b4f05678efc9391f1738433880ef1c5188f8b10291ebbe2b7f9aa5cedeb46
---

# Independent joint review of the spectral window consequences

## Findings

**Pass for the two named statements, with the vacuity limitation below.** Lens:
`certify`. This reviewer began without the conversation that authored or directed
the dossiers. Only the assignment, repository artifacts and primary mathematical
texts were used. The specification and reviewer instructions were read first.
Authorship is confirmed by the supplied checkpoint and the historical reports.
Neither historical review is modified or used as a substitute for checking the
revised argument.

### Statements, dependencies and the discharged input

The stopped-source theorem agrees with `modules/08-spectral-approach.md:221`:
every regular approximant, fixed unit-variance square-integrable test, $L\ge1$,
$T>0$, constant $8L^2$, and the covariance exit stop. The dossier additionally
proves the whitened estimate without stopping and does not require isotropy of
the initial law. This is a valid strengthening.

The two occupation theorems agree with the proposition at line 243, read with
the regular setting and the definition of $K_n$ for $n\ge2$: constants
$C_0=34,C_1=0$, the small-gap restriction, the shrinking window, and the
$C\log^2n$ consequence for every isotropic log-concave law at fixed dimension.
The time interval is $0\le T\le T_0(n)$; the proof treats $T>0$, and $T=0$ is
immediate. No negative time is part of the statement.

`thm:letwin-qcts` is proved with the current R2 certification. I read its canonical
statement, the full `solutions/thm-letwin-imports.md` and its R2 report. Its
quadratic conclusion covers every isotropic log-concave law, every dimension,
and every symmetric matrix, with constant eight. Its compact regular target
class belongs only to the intermediate moment-map assertion. The explicit
fourth-moment approximation removes that restriction before the quadratic
conclusion. The stopped posterior therefore needs no bounded-support hypothesis.
This review consumes the certified node, rather than issuing a second
certification of that import or of its external analytic foundations.

Both reviewed nodes have `thm:letwin-qcts` in `depends_on` and no `assumes`.
All other listed dependencies are proved; the stopped-source result is certified
jointly here before its use in the occupation result. The open
`conj:mm-spectral-occupation` is not a premise. The final conditional theorem of
`prop:spectral-sufficiency` is not invoked: its internal identities and
approximation are re-executed with the dimension fixed. No missing edge to that
conditional theorem is needed. Neither reviewed node has `bounded_by`.

### A material limitation: the small-gap branch is empty

With the actual definition of $K_n$, the published input already implies
$C_P(\mu)\le K_n$ for each regular isotropic approximant. Its first nonconstant
eigenvalue consequently satisfies

$$
\lambda=1/C_P(\mu)\ge1/K_n>3/(8K_n).
$$

Thus no measure satisfies the small-gap hypothesis of the occupation assertion
or of the fourth-moment companion with this $K_n$. Their implications are true,
but provide no nonempty subclass on which the occupation conjecture has been
established. All actual laws lie on the large-gap branch, and the reproduced
$O(\log^2n)$ bound follows already from the stronger input. This is not a
counterexample to either quantified statement and does not invalidate the
calculations checked below. It does rule out interpreting this certification as
new occupation progress. The stopped-source lemma itself has no such restriction
and is nonvacuous.

### Stopped-source proof

I checked Steps 0–4 of `solutions/lem-mm-stopped-window-source.md` in full.
The constant-drift Gaussian likelihood has the displayed sign and factor $1/2$.
For example, its product over any Brownian increment partition telescopes to
$\exp(x\cdot c_t-t|x|^2/2)$, and cylinder generation gives the stated path
likelihood. Bayes then gives the conditional kernel. Strong convexity guarantees
normalization, all posterior polynomial moments and an everywhere positive
density, hence positive definite covariance. The ratios defining the moments
are jointly measurable.

For $f\in L^2$, conditional integrability holds at each deterministic time;
Tonelli makes the exceptional set negligible for product time-probability
measure. Conditional Cauchy–Schwarz with the posterior fourth moment makes
the tensor integral absolutely convergent there. The zero convention therefore
does not affect the conclusion.

Centering and whitening give an isotropic log-concave vector at each admissible
pair $(t,\omega)$. The covariance pairing with every symmetric $M$ is bounded
by $\sqrt{8v_t}\|M\|_{HS}$; the symmetric Hilbert–Schmidt dual recovers the full
norm of the symmetric tensor. No measurable choice of maximizing $M$ is needed.
Unwhitening costs exactly $\|A_t\|_{op}^2$ in the squared bound, replaced by
$L^2$ only on $t<\tau_L$. The endpoint has zero time measure, including the
case $\tau_L=0$. The total-variance budget gives $\mathbb E v_t\le1$ and
Tonelli yields $8L^2T$. No factorization of dependent quantities occurs.

Used hypotheses: the planted channel, smooth strong log-concavity, the fixed
$L^2$ test with variance one, finite positive time and the stated level. Initial
centering, isotropy, spectral discreteness and the eigenfunction equation are
unused; smoothness and $L\ge1$ are stronger than the elementary stopped argument
strictly needs. These are sharpening opportunities, not defects.

### Occupation proof and companion checks

I read all three companion dossiers (restart, fourth moment, time-weighted
source) and all internal steps of the spectral-sufficiency dossier used here.

* Restart: dominated convergence gives continuous posterior moments for bounded
  tests and coordinate polynomials. Reverse martingale convergence transfers to
  the usual filtration; downward dyadic approximation identifies the posterior
  at stopping times. The innovation is a continuous martingale with bracket
  $tI$; the increment/dyadic argument supplies the required conditional Brownian
  law. Restart of the tilt is exact algebra. The derivative of the drift is its
  covariance, bounded by $(\varepsilon+u)^{-1}I$. The weighted sup norm gives the
  claimed contraction factor $1/2$, and Picard iteration is measurable. Freezing
  the prior uses the conditional Brownian law and a monotone-class argument,
  not independence of the posterior variance and exit event.
* Time-weighted source: the product rule has drift
  $(\kappa+t)\|H\|^2+2\mathcal R-|g|^2$, with $\mathcal R\ge0$.
  The terminal cap and stopped variance identity pay for it with the correct
  sign. Increasing stops remove by monotone convergence. The $L^2$ test closure
  controls $g$ strongly and $H$ in $L^1$ by the fourth moment; weak weighted
  lower semicontinuity passes the source. For zero curvature the weight vanishes
  only at the negligible initial endpoint. At restart the positive curvature
  $\varepsilon+\sigma$ yields exactly $v_\sigma/(\varepsilon+\sigma)$.
* Fourth moment: qualitative hypercontractivity gives $f\in L^4$ before any
  subtraction. The truncated cubic is an admissible form test; both sides
  increase to $\lambda\mathbb E f^4=3\mathbb E f^2|\nabla f|^2$.
  Applying the imported Poincaré inequality to $f^2$ yields coefficient
  $4K_n\lambda/3\le1/2$. The algebra is sound, subject to the vacuity noted above.

In the occupation dossier, continuity of $A_t$ makes $\tau_2$ a stopping time
and isotropy makes it strictly positive. The dense-time supremum correctly
includes equality at the exit level. The event $\{\tau\le T\}$ is
$\mathcal F_\tau$-measurable. Uniqueness of the deterministic drift equation
identifies the planted and imported localization laws.

Optional projection is correctly applied to $f^2$ and $f^4$:
$v_\sigma^2\le\mathbb E[f^4(X)\mid\mathcal F_\sigma]$. The tail integral,
regularized first at $\delta>0$, is

$$
\mathbb E[\tau^{-2}\mathbf1_{\tau\le T}]
\le(T^{-2}+2\bar C/T+2\bar C^2)e^{-1/(\bar CT)}
\le5\bar C^2T^{-2}e^{-1/(\bar CT)}.
$$

I checked the substitution, boundary term and $T\le1,\bar C\ge1$ conditions.
The positive universal cap $t_c$ exists by the limit and derivative of $h$;
continuity includes its supremum endpoint. The pre-exit charge is $32T$;
Cauchy–Schwarz and the joint optional projection give post-exit charge at most
$\sqrt2\,T h(T)\le\sqrt2T$. Thus $32T+\sqrt2T\le34T$, with no damping spent.

In the fixed-dimensional bridge, the covariance caps give the claimed
$\varepsilon$-dependent finiteness bounds only. The $q$ identity follows from
the vector SDE; square-integrable source and bounded drift permit its expectation
passage. Bessel gives $|g_0|^2\le1$. The terminal martingale variance identity
and posterior Brascamp–Lieb give $1/2\le\lambda/T_*$. The lower bound
$T_*\ge c_1/\log^2n$ and both branch constants are correct for $n\ge2$.
Gaussian smoothing, quadratic tilting and whitening converge in $W_2$ at fixed
dimension. The approximants have positive lower and finite upper Hessian bounds,
so the ground-state potential is confining. Fixed compact smooth tests pass by
weak convergence; bounded value truncations, spatial cutoffs and mollification
then pass to locally Lipschitz tests. Full-dimensional log-concave laws have
densities, so the almost-everywhere gradient limits used here are legitimate.
There is no eigenfunction limit and no uniform-in-dimension approximation step.

The occupation argument uses the regular isotropic spectral class, normalized
first eigenfunction, $n\ge2$, its stated gap restriction, and
$0\le T\le T_0(n)$. Strong convexity supplies the integrability and restart
regularity but enters no final constant. No unstated spectral hypothesis was found.

### External texts checked

The two published imports were checked against their actual texts, rather than
the old reviews. [Klartag–Lehec, Theorem 61 and Sections 6.1–6.2](https://arxiv.org/html/2406.01324v2)
give exactly the supremum-in-time exit probability, level two and logarithmic
window, for the same tilt equation. The same source's Theorem 34 verifies the
Brascamp–Lieb covariance and fixed-test forms used above, with the stronger
posterior curvature substituted. [Klartag, Theorem 1.2 and (1.4)–(1.5)](https://arxiv.org/pdf/2303.14938)
give $C_P\le C\log n$ for the full isotropic class, with the stated convention.

For the companion's qualitative integrability, I checked the actual book text
of Bakry–Gentil–Ledoux, Corollary 5.7.2, Theorem 5.2.3 and Section 5.3
([full-text reproduction](https://dokumen.pub/analysis-and-geometry-of-markov-diffusion-operators-9783319002262-9783319002279.html),
[publisher](https://doi.org/10.1007/978-3-319-00227-9)):
strong convexity implies log-Sobolev, hypercontractivity sends $L^2$ to every
finite $L^p$ at a suitable finite time, and the eigenfunction identity yields
the asserted finiteness. The author's short public PDF contains only front
matter; it was not mistaken for the chapter. The necessary chapter text was
available in the full reproduction.

The [Letwin source Theorem 1.2](https://arxiv.org/html/2607.24164v1) also matches
the certified quadratic node's all-law quantifiers and factor eight. Its proof
is consumed through the existing certified repository node and the read R2
dossier, not imported afresh by this review. No unavailable source is a remaining
premise of this certification.

### Fences and build

The covariance stop is essential in the first argument. The second uses a joint
rare-event charge, not a product of marginals or an unstopped operator-norm
moment. Neither extends the shrinking window to a universal one. The exponential
product covariance-spike statement is compatible with this restriction. There
are no slice, moving-competitor, projection-only or relative-occupation steps,
and no inference concerning the trace-upgrade cluster.

`uv --cache-dir /tmp/kls-uv-cache run scripts/check.py` was run with authorized
sandbox escalation for the Node subprocess. MyST completed without a dossier
error. The only five failures were the obsolete dossier/statement fingerprints
in the two historical proof records being replaced here; no other dependency
certification was lifted. An earlier sandboxed run failed before MyST because
its Node subprocess could not execute properly; no toolchain was changed.
The front matter is the output of the same checker with `--fingerprint` and both
dossier paths, run after the mathematical examination. The brief's changed
table was reread before final recording.

## Corrections

No correction is required to the two mathematical statements or proofs for this
verdict. The reviewer does not certify the surrounding prose as synchronized:
`modules/08-spectral-approach.md:28,34,73,217` still describe the discharged
Letwin antecedent as conditional. That is an editorial synchronization defect,
reported to the orchestrator for its planned writer pass. The brief table has
already been corrected. In particular, the introductory claim that the window
chain settles a nonempty initial-layer portion needs the vacuity qualification
above. Suggested replacement prose is included in the handoff.

## Exclusions

Only `lem:mm-stopped-window-source` and `prop:mm-window-occupation` receive new
certification records. This does not certify a nonempty small-gap subclass,
universal-time occupation, `conj:mm-spectral-occupation`, KLS, a better frontier,
any trace-upgrade assertion, or a Lean proof. Existing companion certifications
are not replaced. No new review of the entire Letwin source or its general KLS
theorem is issued. A global prose/ledger synchronization audit is outside this
certify lens. No proof step needed for the two exact conclusions remains unverified.

## Handoff

Apply both proof-record replacements together, retain `status: proved` and the
current dependency lists, and retain the absence of `assumes`, `bounded_by` and
`refuted_by`. All historical review files remain unchanged.

```yaml
files:
  - research/reviews/2026-10-01-spectral-window-letwin-discharge-review.md
deltas:
  - file: research/program/ledger.yaml
    node: lem:mm-stopped-window-source
    set:
      status: proved
      depends_on: [thm:letwin-qcts]
      proofs:
        - artifact: solutions/lem-mm-stopped-window-source.md
          review: research/reviews/2026-10-01-spectral-window-letwin-discharge-review.md
  - file: research/program/ledger.yaml
    node: prop:mm-window-occupation
    set:
      status: proved
      depends_on: [thm:KL-window, thm:klartag-logn, lem:mm-stopped-window-source, lem:mm-restart-deweighting, lem:mm-smallgap-fourth-moment, lem:mm-time-weighted-fixed-source, thm:letwin-qcts]
      proofs:
        - artifact: solutions/prop-mm-window-occupation.md
          review: research/reviews/2026-10-01-spectral-window-letwin-discharge-review.md
  - file: modules/08-spectral-approach.md
    owner: writer
    location: "after prop:mm-window-occupation, replacing the paragraph currently at line 248"
    replacement: >-
      The scope of [](#prop:mm-window-occupation) is limited further by its gap
      hypothesis. Since [](#thm:klartag-logn) gives $C_P(\mu)\le K_n$, every
      first nonconstant eigenvalue satisfies $\lambda\ge1/K_n>3/(8K_n)$.
      Its small-gap occupation implication therefore has no admissible measure
      with this choice of $K_n$. The stopped estimate
      [](#lem:mm-stopped-window-source) applies without that restriction.
      The reproduced $C\log^2 n$ bound is weaker than the published input,
      and supplies no nonempty case of [](#conj:mm-spectral-occupation).
```
