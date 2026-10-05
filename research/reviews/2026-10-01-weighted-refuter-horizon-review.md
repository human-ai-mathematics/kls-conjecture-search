---
verdict: pass
authors:
  - prove_weighted_spectator_obstruction, unknown, 2026-08-27
  - repair_weighted_spectator_w0r2, unknown, 2026-08-27
reviewer: reviewer_weighted, gpt-6-astra, 2026-10-01
fingerprints:
  solutions/prop-weighted-spectator-obstruction.md: 9e52a87391e5b6b51bbf3b57657604d3a9cf802c0920c0b6de5a65dcd819b5b9
  prop:weighted-spectator-obstruction: 3a65960d47cdc44c6a81fe7559223a79b7b491d7389ceb61251cc675cd573288
  prop:covariance-spike: 161bf636e00b06d616360d86e08e775faacc85e3ebd8f62c91289807a22bfbb5
  lem:one-dimensional-density-variance: d815a2b4dd127f6904303d7af11bdff816a4ca70c21541afd80ebd41506343a6
  prop:products: 85b9ec9b7b81c783e52dce9f3edce41396f581da4f7a425bd3df9031860a6c8c
  lem:half: 1d4daf2283e1a1022580a067533d1cc3aae4194fa319d223aa00e4112d031a2f
  ass:weighted-package: 814ad484d39e72ce4ede9dacf954dd637418c82ecf409d0271330c484d8aaab0
  conj:weighted-excess-rate: 34c18fad26ca581aa69fa02ded48e117e33bff3828b6cf73516bf22ba755363a
---

# Weighted refuter after horizon clarification — certify review

## Findings

**Pass.** This is a complete fresh-context mathematical re-review of the current Markdown dossier and canonical proposition against both current targets. The reviewer has no authoring conversation in context and is distinct from both assigned authors. SPECIFICATION.md, the program brief, all four dependency statements, their ledger records, and the entire dossier were read. The earlier repair review was read as historical context; its old paths and handoff are not the authority for this verdict and it is left unchanged.

### Exact targets and negations

Write $L_{\mu,E,\eta}(T)=\mathbb E\int_0^{T\wedge\tau_\eta}e_t(E)(1+\|A_t\|_{\rm op})^{5/2}\,dt$ and $R_\gamma(E,T)=Te_0(E)+T^{1+\gamma}$.

The canonical `conj:weighted-excess-rate` says: “There exist universal $C,T_0,\gamma>0$ and $\eta\in(0,1/4]$” such that every isotropic log-concave law and every balanced finite-perimeter cut with $e_0\le1$ satisfies $L(T)\le C R_\gamma(E,T)$ at all positive times up to $T_0$. Its negation is

$$
\forall C,T_0,\gamma>0\ \forall\eta\in(0,1/4]\
\exists d,\mu,E,\ 0<T\le T_0:
\quad \mu(E)=1/2,\ e_0(E)\le1,\ L(T)>C R_\gamma(E,T),
$$

with the same isotropic log-concave and finite-perimeter restrictions. The proposition supplies this and the stronger arbitrarily small additive and relative excess conditions.

The clarified canonical `ass:weighted-package` says: “There are universal constants $T_0>0$, $C_0,C_1,C_2\ge0$, $0\le\beta<\tfrac12$, $\gamma>0$, and $\eta\in(0,\tfrac14]$” with $2\beta+64\eta^2<1$, such that every eligible initial cut satisfies both clauses (i-w) and (ii-w) on that fixed window. Clause (i-w) is exactly $L(T)\le C_2R_\gamma(E,T)$. Clause (ii-w) bounds the integrated Stein norm by $C_0T+C_1\mathbb E\int r+\beta\mathbb E\int D+C_2L(T)$. The negation is: for every admissible tuple of these constants, some eligible law, cut and positive time at most $T_0$ violates at least one clause.

For any such tuple apply the refuter with $C=\max\{1,C_2\}$, the supplied $T_0,\gamma,\eta$, and $\delta\le1$. Its strict inequality gives $L(T)>C R_\gamma(E,T)\ge C_2R_\gamma(E,T)$, including when $C_2=0$. The positive horizon permits the small positive witness time. The absorption restriction only narrows the allowed windows, all covered by the refuter's $\eta\in(0,1/2)$. Half-mass witnesses belong to either initial-mass reading of the package. Neither $C_0,C_1$ nor $\beta$ can rescue a failed clause (i-w).

This is a certified family indexed by every proposed universal tuple, not one numerical witness offered against a uniform constant. The clarification preserves the already refuted package; it supplies neither a salvaging variant nor grounds to reopen `ap:e-weighted-excess`.

### Complete proof audit

The canonical proposition and dossier theorem agree; the dossier additionally makes $e_0\le1$ explicit. Centering the rate-one exponential gives an isotropic log-concave factor. All perimeters use the outer Minkowski convention.

The regularization lemma starts from an outer-Minkowski near-competitor, whose relative weighted BV perimeter is no larger. Compact truncation, smoothing in interior and support charts, and coarea give regular approximants with convergent mass and relative perimeter. For the selected finite approximant, an interior boundary patch corrects mass by a smooth flow with positive mass derivative and arbitrarily small perimeter cost. The positive density and $0<p<1$ permit such an interface. The relative tube formula counts the interior interface; support facets supply no additional first-order perimeter. The selected compact regular approximation justifies multiplying the surface density by $F_{u,t}$ whenever its normalizer is positive and finite. This verifies the exact density-change identity used later without approximating the exponential probability law by a different law.

Cylinder extension preserves both mass and Minkowski perimeter, hence $a_m=I_{\lambda^{\otimes m}}(1/2)$ decreases. The certified product Cheeger bound and half-mass identity give $a_m\ge a_*>0$. Choosing $M$ and then a regular exact-half-mass $E_0$ gives $a_*\le P_0\le a_\infty+\varepsilon$. For every later $N$, the cylinder therefore has $0\le e_0\le\varepsilon$ and relative excess at most $\varepsilon/a_*$. The displayed choice $2\varepsilon\le\min(\delta,1,\delta a_*)$ suffices with slack. No choice of $N$ can spoil initial near-minimality.

In the planted Gaussian channel $c_t=tX+B_t$, the likelihood and prior factorize. The base posterior process, cylinder mass, perimeter, and exit time depend only on the base latent and Brownian variables; all spectator posterior processes are independent of them. The channel endpoint is sufficient for the posterior, so this realizes the localization law required by the statements.

Local exponential integrability gives the uniform $L^1$ convergence of $F_{u,t}$ at $(0,0)$ by dominated convergence, including its normalizer. Choosing a compact perimeter patch carrying at least $P_0/2$, then shrinking $a,\bar T$, gives the displayed density lower bound $1/4$. The reflection-principle union bound is $4M\exp[-a^2/(8MT_b)]\le1/2$. Independence of the latent bound and Brownian bound gives $\mathbb P(G_b)\ge1/4$. On this single base event, $|c_s^0|\le a$, the mass remains strictly inside the fixed window, and $P_s\ge P_0/8$ throughout $[0,T_b]$. Continuity handles the exit-time endpoint. Both $G_b$ and $T_b$ are chosen before $N$.

For a deterministic $t>0$, the observation $c_t/t$ has noise variance $s=1/t$. Thus the covariance-spike event has probability at least $1-(1-\tfrac12e^{-1/t})^N$. When $\log N\ge2/T$ and $t\in[T/2,T]$, this is at least $h_{\rm sp}=1-e^{-1/2}$. Only marginal-in-time events are used. On a spike, a quantile halfline in a high-variance spectator has exactly the actual mass $p_t$ and perimeter at most $v_{i,t}^{-1/2}\le\sqrt{t/c_{\rm sp}}$. It is an upper competitor for the posterior profile, so no moving-profile lower bound is assumed.

The choice $T\le c_{\rm sp}P_0^2/256$ gives $e_t\ge P_0/16$ on $G_b\cap H_t$. Block diagonality gives weight at least $c_{\rm sp}^{5/2}t^{-5/2}$; independence gives event probability at least $h_{\rm sp}/4$. The parameterized surface integral, posterior moments, and profile are measurable; the latter can be obtained from a countable dense regular competitor class with shrinking mass windows. Nonnegative Tonelli consequently applies even without a finite a priori upper bound for the integral. In particular,

$$
L(T)\ge\frac{P_0h_{\rm sp}c_{\rm sp}^{5/2}}{64}
\int_{T/2}^Tt^{-5/2}\,dt
=\frac{h_{\rm sp}c_{\rm sp}^{5/2}}{96}(2^{3/2}-1)P_0T^{-3/2}.
$$

Both final strict small-time inequalities are feasible because all their constants are fixed and positive. They separately bound $CTP_0$ and $CT^{1+\gamma}$ by half of this lower bound. Since $e_0\le P_0$, the required strict violation follows. The checked order is constants and tolerance, then base and $T_b$, then $T$, then finite $N$. Every displayed constant and power in this chain agrees.

### Dependencies, sources, hypotheses and fences

All four declared dependencies are proved, with no open `depends_on` or extra antecedent. `prop:products` supplies its time-zero product bound; `lem:half` supplies its exact profile identity. Their certified statements are accepted inputs, not newly certified transitive dossiers. The factorization is also derived directly here.

The actual source of `prop:covariance-spike` was checked: [Klartag–Lehec, Proposition 65 and its proof, equation (48)](https://arxiv.org/html/2406.01324v2#S8.SS1). Completing the square yields $s\operatorname{Var}(G\mid G\ge\sqrt s-Y/\sqrt s-G_1)$. The independent event $Y\ge s$, $G_1\ge0$ has probability $e^{-s}/2$ and forces a nonpositive truncation threshold, with variance bounded below uniformly. Independent coordinates give exactly the event bound used in the dossier. Only this part of the source is needed.

For `lem:one-dimensional-density-variance`, [Bobkov–Chistyakov, Proposition 2.1, pages 979–980](https://www-users.cse.umn.edu/~bobko001/papers/2015_JOTP_BC_Conc.functions.authors.03.07.2013.pdf) states $1/12\le v\|f\|_\infty^2\le1$. Its upper bound gives precisely the quantile-density estimate used. These are published inputs; neither is an unreviewed preprint imported as a new theorem by this dossier.

All theorem hypotheses are accounted for. The positive constants and tolerance enter their corresponding choices; log-concavity gives the profile and density bounds; the finite product gives exponential moments and independent blocks. The stated $\gamma>0$ is stronger than the final power comparison needs. There is no used unstated hypothesis and no numerical proof step. Standard smoothing, the Gaussian likelihood, Brownian reflection and nonnegative Tonelli are used in their ordinary finite-dimensional domains.

The refuter has no formal `bounded_by` edge. The target's contextual two-tail and circularity fences are respected: the exponent remains $5/2$ and an explicit upper profile competitor is used. Nothing about equivalence within the trace-upgrade cluster is asserted.

### Build and versions

Immediately before writing these reports, the escalated `UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py` completed with exactly one error and exit 1: the old review's fingerprint for `ass:weighted-package` is stale. No MyST error or other check defect was reported. Both exact dossier fingerprint commands then exited zero; this report reproduces the refuter command's output, including both targets. The dossier and canonical input files remained unchanged through these checks, verified by file hashes before writing.

The global check is not yet zero because it still selects the historical proof record. This actual new pass authorizes replacing that record. It does not authorize editing the historical review or presenting the old certification as current.

## Corrections

None to the proof. No unchecked proof step remains within scope. Replace only the selected certification record as proposed below; the original review remains append-only history.

## Exclusions

This certifies `prop:weighted-spectator-obstruction` and its logical contradiction of the two pinned targets. It does not certify the separate unweighted obstruction, the package's trace clause, a cut-local replacement, a near-worst-measure variant, or KLS. The witness measures themselves satisfy dimension-free KLS. No proof repair, status transition, portfolio change, or edit to another author's work is performed by this review.

## Proposed certification and handoff

Replace `prop:weighted-spectator-obstruction.proofs[0]` by:

```yaml
artifact: solutions/prop-weighted-spectator-obstruction.md
review: research/reviews/2026-10-01-weighted-refuter-horizon-review.md
```

Retain its `status: proved` and `depends_on: [prop:covariance-spike, lem:one-dimensional-density-variance, prop:products, lem:half]`. Retain `status: refuted` and `refuted_by: [prop:weighted-spectator-obstruction]` on both `conj:weighted-excess-rate` and `ass:weighted-package`; the refuter does not become a proof dependency of either target. Keep `ap:e-weighted-excess` closed. Run the full check after this record replacement, obtaining zero before any subsequent new status transition, including the companion implication certification.

```yaml
files:
  - research/reviews/2026-10-01-weighted-refuter-horizon-review.md
deltas:
  - "Replace only prop:weighted-spectator-obstruction.proofs[0] with the displayed artifact/review pair; retain its proved status and four dependencies. Preserve the historical review."
  - "Retain both targets as refuted by prop:weighted-spectator-obstruction, and retain ap:e-weighted-excess as closed. Run the full check to zero after the record replacement, before subsequent new status transitions."
```
