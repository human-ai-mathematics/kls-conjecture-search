---
verdict: pass
authors:
  - claude-prover-w4p02
reviewer: proof-checker-w4r04
fingerprints:
  solutions/prop-mm-window-occupation.md: 01607a7c457415d67a748b284d3af9c8fe1bed33b5e5ffbf144eb1176920df6e
  prop:mm-window-occupation: bbd631e99eaca03ead444b48a8cc8a2f931eac2296797ef35aa65437c11aeab7
  thm:KL-window: c8805f6f7be529a3a27f935a273c4a3253861fe59ebc6b52dc416a68cdd915f7
  thm:klartag-logn: 70dd5528111bc813bcfa6750d3afcfcdc31121dbf564fb0681db32265b576b60
  lem:mm-stopped-window-source: c405064bb67767843b0c86c8266cc60e9693dc13df3968410792d1a5b3f6b5e1
  lem:mm-restart-deweighting: ec93efcb1ac959a52ffa4388970b9434e653605ff400c9a1093346afda979f20
  lem:mm-smallgap-fourth-moment: 5efc054693b4557b794756da70c6b5a5ba03e38dc8bd743eca82855cc796d1df
  lem:mm-time-weighted-fixed-source: 661b4f05678efc9391f1738433880ef1c5188f8b10291ebbe2b7f9aa5cedeb46
  thm:letwin-qcts: 8e2ac0819f46db553fe83a6f3034436816565262316c2e6bde7d81baead1a082
---

# Window occupation and Route-S polylog reproduction — independent proof review

Cold review of `solutions/prop-mm-window-occupation.tex` (reviewed SHA-256
`dcde8acc03b27565e4a811cec5a0b79e9f74fccedd502a269129a6dde16ff7b8`), reconstructed from
repository artifacts only: the dossier, `research/kls/ledger.yaml` (node at line 950),
`modules/kls/30-spectral-route.tex` (`\label{prop:mm-window-occupation}`),
`modules/kls/15-covariance-technology.tex` (`thm:KL-window`, `thm:klartag-logn`,
`rem:kl-window-verified`), `modules/kls/14-qcts-obstruction.tex` (`thm:letwin-qcts`),
`modules/kls/02-family-stochastic-localization.tex` (`subsec:sl-process`,
`eq:sl-density`), the three companion candidate dossiers, and the two certified
dependency dossiers with their persisted passing reviews
(`2026-08-27-lem-mm-time-weighted-fixed-source-proof-review.md`,
`2026-08-27-prop-spectral-sufficiency-proof-review.md`). The prover's session narrative
was not consulted as evidence. Author `claude-prover-w4p02` and reviewer
`proof-checker-w4r04` are distinct; the exploration record
`research/explorations/2026-08-30-prover-mm-window-chain-w4p02.md` names only the prover
as author.

## Scope of this certification (read before wiring)

This review certifies the **assembly**: the exit-time bookkeeping, the law
identification, the optional projection, the tail integral, the constant chain
$32+\sqrt2\le34$, and the fixed-$n$ rerun of the certified bridge. The certified result
is a **conditional implication** (repository constraint 7): everything is conditional on
the unreviewed preprint import `thm:letwin-qcts`, and this pass is additionally
**contingent on independent certification of the three companion candidate dossiers**,
whose statements are consumed as inputs here and which are under separate review:

| companion input | version consumed (SHA-256) |
|---|---|
| `solutions/lem-mm-stopped-window-source.tex` (conditional on Letwin) | `a559c44fc9288c76be10be2d75a650c7f74524ef3ed5562490867f51a16a7e82` |
| `solutions/lem-mm-restart-deweighting.tex` (unconditional) | `8511c90a222f86aea8c4dbc9d48a1b955d2ff6245e2dfe7143692d7d3034c2d2` |
| `solutions/lem-mm-smallgap-fourth-moment.tex` (uses `thm:klartag-logn`) | `3a722083c961595dbaf8ed3e6b610b5dfe189f3d726c675479224bbaaabdd2a1` |

The assembly consumes, beyond the restart companion's headline display, four of its
**internal artifacts**: the optional-time identification (its Step 2,
`eq:sol-rdw-optional`), the innovation Brownian motion (Step 4), the exact restart
algebra (Step 5), and the deterministic solution map with pathwise uniqueness and its
Step 7(a) identification (Steps 6, 7(a)), all declared in the assembly's input (I5). A
certifying review of `lem-mm-restart-deweighting` necessarily checks these steps as part
of its proof; the contingency above therefore covers them, but the orchestrator must not
wire this node before all three companion reviews pass **at the hashed versions above**
(or re-review if the texts change).

## Findings

### 1. Statement agreement

The dossier's two theorems, the ledger `statement:` of `prop:mm-window-occupation`, and
the manuscript proposition at `\label{prop:mm-window-occupation}`
(`modules/kls/30-spectral-route.tex:231`–`240`) agree mathematically: conditional on
`thm:letwin-qcts`, with $T_0(n)=\min\{t_c,1/(\bar C\log^2n)\}$ from `thm:KL-window`, the
occupation hypothesis `eq:spectral-occupation` holds on $[0,T_0(n)]$ with $C_0=34$,
$C_1=0$ for every normalized first eigenfunction of a regular isotropic approximant with
$\lambda\le3/(8K_n)$, with no damping consumed; and, combined with the certified bridge
argument rerun at fixed $n$ and the trivial large-gap branch,
$\CP\le C\log^2n$ for every isotropic log-concave law, conditional on `thm:letwin-qcts`.

One wording observation, not a defect: the dossier states $n\ge2$ explicitly; the
manuscript proposition and ledger statement leave $n\ge2$ implicit through
$K_n=C_K\log n$, which is only defined by `thm:klartag-logn` for $n\ge2$ (its manuscript
and ledger statements both carry $n\ge2$). Read with that definitional frame the three
surfaces agree; the orchestrator may optionally add "$n\ge2$" to the manuscript
proposition and ledger statement for self-containedness (at $n=1$ the display
$\CP\le C\log^2n$ would be vacuously false and is not claimed by the dossier).

### 2. Inputs and their exact standing (dependency closure)

- `thm:letwin-qcts` — imported, `preprint-unreviewed`
  (`Letwin2026QuadraticKLS`, v1). Enters only through the stopped-window companion,
  where it is an explicit hypothesis. **Keeps the node `conditional` at best.**
- `thm:KL-window` — imported, `published` (`[KLnotes Thm. 61]`). The manuscript's
  `rem:kl-window-verified` records verification of the statement number, sup-over-time
  form, threshold $2$, and window $1/(C\log^2n)$ against arXiv:2406.01324v2 (matching
  the published Bull. AMS 62 (2025) article). The dossier uses the registered statement
  verbatim, including the loss-free WLOG $\bar C\ge1$ (checked: enlarging $\bar C$
  shrinks the window and weakens the exponential bound, so the statement with $C$
  implies the statement with $\max\{C,1\}$).
- `thm:klartag-logn` — imported, `published` (`Klartag2023Logarithmic`), registered in
  the ledger (line 535) despite the dossier header's stale "ledger acceptance pending"
  comment. Used as branch-splitting input and inside the fourth-moment companion; the
  pipeline output $O(\log^2n)$ is strictly weaker than this input, so no circularity.
- Three companion candidate dossiers — statements consumed as inputs; **not certified
  here** (see contingency above).
- `lem:mm-time-weighted-fixed-source` — `proved`, certified 2026-08-27; consumed only
  inside the restart companion, not directly here.
- `solutions/prop-spectral-sufficiency.tex` — certified 2026-08-27. Its **theorem is
  not usable as a black box** (its hypothesis demands dimension-free constants, and
  $T_0(n)\to0$ here); the assembly instead reruns its internal steps at fixed $n$. I
  re-verified against the certified dossier's text that every rerun step ($q$-identity
  with stopped Itô passage, Bessel, terminal-variance identity, posterior
  Brascamp–Lieb, approximant construction, fixed-test passage) is proved measure-by-
  measure at fixed $n$ and nowhere uses dimension-freeness; the only place the certified
  proof used the universal hypothesis is where the rerun substitutes
  Theorem `thm:sol-prop-mm-window-occupation` at the same fixed $n$. The rerun is
  legitimate. (The ledger `depends_on` of the node omits `prop:spectral-sufficiency`;
  defensible, since the node's theorem is not a premise — only its certified argument is
  re-executed — and this review checks the re-executed steps.)

### 3. Steps checked (all verified)

**Lemma `lem:sol-mwo-exit` (path regularity, stopping).** Continuity of $t\mapsto A_t$:
entries are ratios of $\mu$-integrals of $(x_ix_j,x_i,1)\,e^{c_t\cdot x-t|x|^2/2}$; on
$[0,U]$, $R=\sup_{s\le U}|c_s|<\infty$ pathwise, domination by
$(1+|x|^2)e^{R|x|}\in L^1(\mu)$ ($\varepsilon$-strong log-concavity gives all
exponential moments), denominator positive and continuous; DCT gives continuity.
(i) $\{\tau_L\le t\}$ equals the sup-over-dense-set event by continuity (the inf is
attained at the closed level set: if $\tau_L\le t$ then $\|A_{\tau_L}\|_\op\ge2$ by
continuity along approximating times), and each $\|A_s\|_\op$ is $\F_s$-measurable, so
$\{\tau_L\le t\}\in\F_t$ (usual augmentation absorbs the null continuity defect).
(ii) $A_0=I$ by isotropy, $\|A_0\|_\op=1<2$, continuity forces $\tau_2>0$.
(iii)–(iv) elementary and correct; $\{\tau\le T\}\cap\{\tau\le t\}=\{\tau\le T\wedge t\}
\in\F_t$ is exactly $\F_\tau$-membership.

**Lemma `lem:sol-mwo-law` (law identification — the step the probe consumed silently;
here proved).** For the $\varepsilon$-strongly log-concave $\mu$, the drift
$z\mapsto\mathsf a(\mu;t,z)$ has $\nabla_z\mathsf a=\Cov(\Theta(\mu;t,z))\preceq
(\varepsilon+t)^{-1}I\preceq\varepsilon^{-1}I$ (Brascamp–Lieb), so it is globally
Lipschitz uniformly in $t$; the restart companion's Step 6 gives a deterministic
solution map $\mathsf S_\mu$ with pathwise uniqueness for
$\gamma_u=\int_0^u\mathsf a(\mu;s,\gamma_s)\dd s+w_u$. Hence **any** realization of the
manuscript localization (`subsec:sl-process`: tilt density `eq:sl-density`,
$\dd c_t=a_t\dd t+\dd W_t$, $c_0=0$, $W$ a standard BM, $a_t=\mathsf a(\mu;t,c_t)$) has
tilt-path law $\mathsf S_\mu\#\mathbb W$. The planted channel satisfies the same
equation with the innovation BM (companion Steps 4, 5, 7(a) at the stopping time
$\sigma=0$, which needs no positivity), so its tilt path has the same law
$\mathsf S_\mu\#\mathbb W$. Since $A_s=\Cov(\Theta(\mu;s,c_s))$ is a fixed measurable
functional of $(s,c_s)$ and $\sup_{s\le t}\|A_s\|_\op$ is path-measurable by continuity,
the probability in `thm:KL-window` is realization-independent, and with exit-lemma (iii)
gives $\Prob(\tau\le t)\le e^{-1/(\bar Ct)}$ for $t\le t_1(n)$. Sound.

**Lemma `lem:sol-mwo-optional-projection`.** Optional-time identification (companion
Step 2, valid for measurable $\phi\ge0$ as an identity in $[0,\infty]$) applied to $f^2$
and $f^4$; pathwise $0\le v_\sigma\le\int f^2\dd\mu_\sigma$; conditional Jensen
(conditional Cauchy–Schwarz) $(\E[f^2(X)\mid\F_\sigma])^2\le\E[f^4(X)\mid\F_\sigma]$;
multiply by $\one_E$, $E\in\F_\sigma$, $E\subseteq\{\sigma<\infty\}$; tower. Gives
$\E[v_\sigma^2\one_E]\le\E[f^4(X)\one_E]\le\E_\mu f^4$. Correct.

**Lemma `lem:sol-mwo-tail`.** The identity
$\tau^{-2}=T^{-2}+2\int_\tau^Ts^{-3}\dd s$ on $\{\delta<\tau\le T\}$ is exact
($\int_\tau^T s^{-3}\dd s=(\tau^{-2}-T^{-2})/2$); the $\delta>0$ regularization makes
the expectation split legitimate, Tonelli converts the second term to
$2\int_\delta^Ts^{-3}\Prob(\delta<\tau\le s)\dd s$, monotone convergence as
$\delta\downarrow0$ (using $\tau>0$ a.s.). Substitution $u=1/s$:
$\int_0^Ts^{-3}e^{-1/(\bar Cs)}\dd s=\int_{1/T}^\infty ue^{-u/\bar C}\dd u
=(\bar C/T+\bar C^2)e^{-1/(\bar CT)}$ — the antiderivative
$\int_a^\infty ue^{-u/\bar C}\dd u=(a\bar C+\bar C^2)e^{-a/\bar C}$ is correct. For
$T\le1$, $\bar C\ge1$: $1+2\bar C+2\bar C^2\le5\bar C^2$ iff
$(3\bar C+1)(\bar C-1)\ge0$. All verified.

**Definition of $t_c$.** $h(t)=\sqrt5\,\bar C\,t^{-2}e^{-1/(2\bar Ct)}\to0$ as
$t\downarrow0$; $\frac{\dd}{\dd t}\log h=-2/t+1/(2\bar Ct^2)=t^{-1}(1/(2\bar Ct)-2)>0$
for $t<1/(4\bar C)$. The sublevel set $\{h\le1\}\cap(0,1/(4\bar C)]$ is a nonempty
interval $(0,t_c]$ (continuity at $t_c$), $0<t_c\le1/(4\bar C)\le1/4<1$, and $t_c$
depends only on $\bar C$. Well defined and universal.

**Main theorem (constants).** Pathwise split
$\int_0^TS\le\int_0^{T\wedge\tau}S+\one_{\{\tau\le T\}}\int_\tau^\infty S$ (checked at
the edge $\tau=T$). Pre-exit: companion (I4) at $L=2$ gives $32T$ (hypotheses match:
regular approximant, unit-variance $f$, $L\ge1$, $T>0$). Post-exit: tower with
$\{\tau\le T\}\in\F_\tau$, restart (I5) at $\sigma=\tau$ (a.s. positive stopping time,
by the exit lemma), Cauchy–Schwarz, $\E f^4\le2$ from (I6) on the small-gap branch
($K_n>0$ needs $n\ge2$), the tail lemma (applicable since
$T\le T_0(n)\le\min\{1,t_1(n)\}$, using $t_c<1$), and
$\sqrt2\cdot\sqrt5\,\bar C\,T^{-1}e^{-1/(2\bar CT)}=\sqrt2\,T\,h(T)\le\sqrt2\,T$ for
$T\le t_c$. Total $(32+\sqrt2)T\le34T$. The a-fortiori occupation form with $C_0=34$,
$C_1=0$ uses only $q\ge0$, $D_t=g_t^TA_tg_t\ge0$ ($A_t\succeq0$). All constants
re-derived independently; no correction needed.

**Fixed-$n$ bridge rerun.** $M_*=1+34t_c\ge(1+34T_0(n))e^0$, so the certified Grönwall
constant is dominated; with $C_1=0$ no Grönwall step is needed and
$q(t)\le|g_0|^2+\E\int_0^tS\le1+34t\le M_*$ on $[0,T_0(n)]$. Finiteness for the
$q$-identity's stopped Itô passage: $\E\int_0^tS\le34t$ (Theorem 1),
$q(s)\le\E[v_s/(\varepsilon+s)]\le\varepsilon^{-1}$, and
$\E D_s\le\varepsilon^{-2}$ — I re-derived both caps:
$A_s\preceq(\varepsilon+s)^{-1}I$ (posterior Brascamp–Lieb) and
$|g_s|^2\le v_s\|A_s\|_\op$ (Cauchy–Schwarz on $u\cdot g_s=\Cov_{\mu_s}(f,u\cdot X)$),
whence $(\varepsilon+s)|g_s|^2\le v_s$; these are finiteness-only and enter no final
constant. Bessel $|g_0|^2\le1$ (centered isotropic coordinates orthonormal). Terminal
variance $\E\Var_{\mu_{T_*}}(f)=1-\int_0^{T_*}q\ge1-T_*M_*\ge1/2$ at
$T_*(n)=\min\{T_0(n),1/(2M_*)\}$; upper bound $\lambda/T_*$ by posterior Brascamp–Lieb
($\nabla^2V_t\succeq tI$) plus the fixed-test tower property; hence
$\lambda\ge T_*(n)/2$. Large-gap branch: $\lambda>3/(8K_n)$ gives
$\CP=1/\lambda<(8C_K/3)\log n\le(8C_K/(3\log2))\log^2n$ for $n\ge2$. Window floor:
$T_*(n)\ge c_1/\log^2n$ with $c_1=\min\{t_c\log^22,\log^22/(2M_*),1/\bar C\}$ — each of
the three terms checked using $\log^2n\ge\log^22>0$. The approximation passage reuses
the certified construction (Gaussian convolution, Gaussian tilt, isotropization; compact
resolvent via the ground-state Schrödinger potential; passage on $C_c^\infty$ then
locally Lipschitz tests by truncation/cutoff/mollification/lower semicontinuity, no
eigenfunction convergence) at fixed $n$ with the $j$-independent constant
$C_2\log^2n$, $C_2=\max\{8C_K/(3\log2),2/c_1\}$. All verified.

### 4. Fences (constraint 5) and constraint 6

The ledger node carries no `bounded_by` edge; the dossier nevertheless checks the
registered fences and I confirm: no cut/slice/excess estimate (`obs:two-tail`,
`obs:circularity`, `obs:rank-one-refuted`); the only tensor input is the full
symmetric-matrix Letwin bound inside the companion, with conditional standing displayed
(`obs:proj-ceiling`); no crude covariance integral $\Xi_T$ or bootstrap
(`obs:crude-insufficient`); the a-priori input is the published frontier and the output
strictly weaker (`obs:relative-ceiling`). `prop:covariance-spike` is respected
constructively: no assertion for $t>T_0(n)$, and the dossier says so up front. Recorded
dead ends respected: the post-exit charge is a joint Cauchy–Schwarz through the optional
projection, not a product of marginals; no unstopped $\|A_t\|_\op$ moment. Constraint 6:
no statement touches `q:upgrade`, `q:stein-weighted`, or `q:alignment`.

### 5. Hypothesis accounting

Used and stated: regularity class (smooth, $\varepsilon$-strongly log-concave, centered,
isotropic, compact resolvent — isotropy for $A_0=I$, `thm:KL-window`, $K_n$, and Bessel;
$\varepsilon$ only for exponential moments, the solution map's Lipschitz constant, and
finiteness caps, entering no final constant); normalized first eigenfunction (used as a
unit-variance test in Theorem 1, as an eigenfunction only through (I6) and the bridge);
$\lambda\le3/(8K_n)$; $n\ge2$; $T\le T_0(n)$; the declared imports and companions. Used
but only implicitly stated in the manuscript/ledger: $n\ge2$ (see Finding 1). Stated but
unused: none of substance; sharpening opportunities only ($34$ could be $32+\sqrt2$;
$t_c$ is not optimized). No hidden hypothesis found.

### 6. Citation debt

No new external citation is introduced: all imports enter through registered ledger
import nodes whose statements the dossier reproduces verbatim. `thm:letwin-qcts` remains
`preprint-unreviewed` — this is the declared conditionality, and by constraint 7 the
node stays `conditional` even after this review. `thm:KL-window` and `thm:klartag-logn`
are `published` imports; the KL-window attribution debt was previously resolved and is
recorded in `rem:kl-window-verified` (verified against arXiv:2406.01324v2). I did not
re-open the external PDFs in this environment; this review certifies that the dossier's
use matches the registered import statements exactly, and the dossier's own request
(remark (iv)) that the reviewer confirm Thm. 61 concerns the tilt process of
`subsec:sl-process` is answered affirmatively at the level of the repository's
registered convention and verification remark, on which the law-identification lemma's
transfer argument is then a complete proof.

### 7. Standalone build

`cd solutions && latexmk -C && latexmk -pdf -outdir=../build
prop-mm-window-occupation.tex` from a clean state: compiles, 7-page PDF, unresolved
`\ref`/`\cite` shown as `??`/`[?]` as expected for a `subfiles` standalone.

## Corrections

None. No mathematical step required repair. (Cosmetic, for wiring time, not blocking:
the dossier header comments still say "candidate node, ledger acceptance pending" for
`prop:mm-window-occupation` and for `thm:klartag-logn`, though both nodes now exist in
`research/kls/ledger.yaml`; and the header `checked_by`/`reviewer`/`review` fields await
the standard post-review update.)

## Exclusions

- The three companion dossiers are **not** certified by this review; each requires its
  own passing proof review at the hashed versions above before this node is wired.
- `q:mm-spectral-occupation` itself remains open: $T_0(n)\to0$, so nothing universal is
  certified, and no claim for $t>T_0(n)$ exists.
- No unconditional statement of any kind: everything is conditional on
  `thm:letwin-qcts`, and the frontier reproduction $\CP\le C\log^2n$ is strictly weaker
  than the published unconditional $\CP\le C_K\log n$ input — a route-health
  certificate only, no frontier improvement.
- Nothing about the trace-upgrade cluster, the CMH route, or any other Route-S node.
- The internal correctness of `lem:mm-time-weighted-fixed-source` and
  `prop:spectral-sufficiency` rests on their 2026-08-27 certifications; I re-verified
  only the fixed-$n$ applicability of the bridge's internal steps, not their original
  derivations from scratch.

## Addendum (same session, before handoff): companion contingency discharged

While this review was in progress, the three companion reviews landed and were wired
by the orchestrator:
`2026-08-30-lem-mm-stopped-window-source-proof-review.md` (pass, reviewer
`proof-checker-w4r03`), `2026-08-30-lem-mm-restart-deweighting-proof-review.md` (pass,
reviewer `proof-checker-w4r02`; its Findings verify Steps 2, 4, 5, 6, 7 — the internal
artifacts consumed by this assembly), and
`2026-08-30-lem-mm-smallgap-fourth-moment-proof-review.md` (pass, reviewer
`proof-checker-w4r03`); all reviewers are distinct from author `claude-prover-w4p02`.
I verified against git that the certified companion texts are exactly the versions
hashed above at the prover commit `e4ae256`, and that every subsequent edit to the three
`.tex` files (through commit `bbf4a43`) touches `%`-comment header lines only (zero
non-comment diff lines): the mathematical statements and proofs certified by those
reviews are byte-identical to the versions this review consumed. The companion
contingency of this certification is therefore **discharged**; the sole remaining gate
on the proposed ledger delta is the permanent one, conditionality on `thm:letwin-qcts`
(the node stays `conditional`, per constraint 7).
