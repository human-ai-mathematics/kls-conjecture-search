---
---
# Prover: the Route-S window chain — four candidate dossiers (stopped source, restart deweighting, small-gap fourth moment, window occupation)

Date: 2026-08-30

Role: `prover`

Run id: `w4p02`

Concurrency keys: `solution:lem-mm-stopped-window-source`,
`solution:lem-mm-restart-deweighting`, `solution:lem-mm-smallgap-fourth-moment`,
`solution:prop-mm-window-occupation` (explicitly coupled node set assigned as one prover task).

Assignment source: verbatim `next_prompt` of
`research/explorations/2026-08-30-kls-route-prober-mm-occupation-initial-layer-w4s01.md`
(Lemmas A–D, Theorem E), as forwarded by the orchestrator with the four
orchestrator-accepted candidate ids (ledger acceptance pending) and one attempt-record path.

## What was produced

Four standalone dossiers, all `checked_by: none`, all headers carrying
"candidate node, ledger acceptance pending":

1. `solutions/lem-mm-stopped-window-source.tex` — **conditional on `thm:letwin-qcts`**.
   Theorem: for every regular approximant ($V\in C^\infty$,
   $\nabla^2V\succeq\varepsilon I$), every fixed test $f\in L^2(\mu)$ with
   $\mathrm{Var}_\mu(f)=1$, every $L\ge1$, $T>0$, with
   $\tau_L=\inf\{t:\|A_t\|_{\mathrm{op}}\ge L\}$:
   $\mathbb E\int_0^{T\wedge\tau_L}\|H_t\|_{\mathrm{HS}}^2\,dt\le 8L^2T$,
   uniformly in $n$ and $\varepsilon$.  Route exactly as prescribed: pathwise whitened
   duality $\|A_t^{-1/2}H_tA_t^{-1/2}\|_{\mathrm{HS}}^2\le8v_t$ via Letwin on the
   whitened posterior, deterministic operator-norm bound strictly before $\tau_L$, and
   $\mathbb E v_t\le1$.  No independence step; no unstopped
   $\|A_t\|_{\mathrm{op}}$ moment; isotropy of $\mu$ explicitly unused (needed so the
   restart dossier can reuse it at the non-isotropic prior $\mu_\sigma$).

2. `solutions/lem-mm-restart-deweighting.tex` — **unconditional**.  Theorem: for every
   a.s. positive stopping time $\sigma$ of the usual augmentation of the observation
   filtration, a.s. on $\{\sigma<\infty\}$,
   $\mathbb E[\int_\sigma^\infty\|H_t\|^2dt\mid\mathcal F_\sigma]
   \le \mathrm{Var}_{\mu_\sigma}(f)/(\varepsilon+\sigma)\le v_\sigma/\sigma$.
   The restart construction is written in full, in seven steps: (1) pathwise posterior
   kernel, path continuity, fixed-time Bayes identification transferred to the usual
   augmentation via reverse martingale convergence; (2) optional-time posterior
   identification (dyadic optional sampling of the closed continuous posterior
   martingales; $\mu_\sigma$ is a regular conditional distribution; extension to
   nonnegative integrable tests by monotone convergence, giving $f\in L^2(\mu_\sigma)$
   a.s.); (3) $\mu_\sigma$ smooth $(\varepsilon+\sigma)$-strongly log-concave;
   (4) innovation Brownian motion by Lévy plus a complete dyadic proof of the strong
   Markov property; (5) exact restart algebra
   $\mu_{\sigma+u}=\Theta(\mu_\sigma;u,\tilde c_u)$; (6) pathwise well-posedness of the
   observation equation — the key simplification of this dossier: because the noise is
   additive, the tilt equation is a deterministic integral equation per path, solved by
   Banach fixed point with the Brascamp–Lieb Lipschitz constant
   $\varepsilon^{-1}$, so no Yamada–Watanabe or stochastic-flow machinery is needed and
   the solution map $\mathsf S_\nu$ is jointly measurable via Picard iterates;
   (7) freezing lemma via strong Markov + monotone class, evaluation of the frozen
   functional against the planted channel of the fixed prior $\nu=\mu_\sigma(\omega)$,
   and the certified `lem:mm-time-weighted-fixed-source` with
   $\kappa=\varepsilon+\sigma(\omega)$.

3. `solutions/lem-mm-smallgap-fourth-moment.tex` — **unconditional implication**;
   its instantiation uses the published import `thm:klartag-logn`
   (`Klartag2023Logarithmic`; ledger acceptance pending), cited, not proved.
   Theorem: if every isotropic log-concave law on $\mathbb R^n$ has $C_P\le K_n$, then
   every normalized first eigenfunction of a regular isotropic approximant with
   $\lambda\le3/(8K_n)$ satisfies $\mathbb E_\mu f^4\le2$.  Steps: qualitative
   $f\in L^4$ by Bakry–Émery + Gross hypercontractivity and
   $P_tf=e^{-\lambda t}f$ ($\varepsilon$-dependent, finiteness only); the identity
   $\lambda\,\mathbb Ef^4=3\,\mathbb E f^2|\nabla f|^2$ proved **as an identity in
   $[0,\infty]$** by pairing the eigenequation with truncated cubics $\varphi_k(f)$
   (Lipschitz post-composition stays in the form domain) and monotone convergence on
   both sides; Poincaré for $f^2$; bootstrap closure at coefficient $\le1/2$.  The
   probe's observation that $K=1/\lambda$ gives coefficient
   $p^2/(4(p-1))>1$ for every $p>2$ (so the external frontier is genuinely needed) is
   recorded as a remark, not a claim.

4. `solutions/prop-mm-window-occupation.tex` — **conditional on `thm:letwin-qcts`**,
   consuming (1)–(3).  Two theorems.  (a) With
   $T_0(n)=\min\{t_c,1/(\bar C\log^2 n)\}$ and WLOG $\bar C\ge1$: for every regular
   isotropic approximant ($n\ge2$), every first eigenfunction with
   $\lambda\le3/(8K_n)$, and every $T\le T_0(n)$,
   $\mathbb E\int_0^T\|H_s\|^2ds\le34\,T$; hence the occupation hypothesis of
   `conj:mm-spectral-occupation` holds on $[0,T_0(n)]$ with $C_0=34$, $C_1=0$, no damping
   consumed.  (b) Rerunning the certified `prop-spectral-sufficiency` bridge argument
   at fixed $n$ with the branch split at $3/(8K_n)$: conditional on `thm:letwin-qcts`,
   every isotropic log-concave law on $\mathbb R^n$ ($n\ge2$) has
   $C_P\le C\log^2 n$.  The dossier also proves, as its own lemmas: path continuity of
   $A_t$ and the stopping-time/positivity/exit-event facts for $\tau_2$; the law
   identification transferring the published `thm:KL-window` bound to the planted
   realization (via the deterministic solution map of dossier 2 — every realization of
   the tilt SDE has law $\mathsf S_\mu\#\mathbb W$); the optional projection
   $\mathbb E[v_\tau^2\mathbf 1_E]\le\mathbb E f^4$ (the probe's Lemma C, proved from
   dossier 2's optional-time identification plus conditional Jensen); and the tail
   integral $\mathbb E[\tau^{-2}\mathbf 1_{\tau\le T}]\le
   (T^{-2}+2\bar CT^{-1}+2\bar C^2)e^{-1/(\bar CT)}\le5\bar C^2T^{-2}e^{-1/(\bar CT)}$
   for $T\le\min\{1,t_1(n)\}$.  Scope fences are stated up front in the dossier, as
   instructed.

## Constant audit (assignment item: verify every constant)

All of the probe's constants check out; none needed correction.

- Pre-exit: $8L^2T=32T$ at $L=2$.
- Tail integral: exact computation
  $\int_0^Ts^{-3}e^{-1/(\bar Cs)}ds=(\bar C/T+\bar C^2)e^{-1/(\bar CT)}$; bracket
  $1+2\bar C+2\bar C^2\le5\bar C^2$ for $\bar C\ge1$ via $(3\bar C+1)(\bar C-1)\ge0$;
  requires $T\le1$, guaranteed by $t_c\le1/(4\bar C)<1$.  The probe's
  $5\max(\bar C^2,1)$ becomes $5\bar C^2$ under the loss-free normalization
  $\bar C\ge1$ (enlarging $\bar C$ shrinks the window and weakens the bound).
- $t_c$: $h(t)=\sqrt5\,\bar C\,t^{-2}e^{-1/(2\bar Ct)}$ is increasing on
  $(0,1/(4\bar C)]$ (log-derivative sign) and vanishes at $0^+$, so
  $t_c=\sup\{t\le1/(4\bar C):h(t)\le1\}$ is well defined, universal, and $h\le1$ on
  $(0,t_c]$.  This replaces the probe's implicit "choose $t_c$" with an explicit
  monotonicity argument; no closed form is needed since the final constant is
  unspecified-universal.
- Post-exit: $\sqrt2\cdot\sqrt5\,\bar C\,T^{-1}e^{-1/(2\bar CT)}=\sqrt2\,T\,h(T)\le\sqrt2\,T$.
- Total: $32+\sqrt2\le34$.  So $C_0=34$, $C_1=0$ confirmed.
- Bridge: $M_*=1+34t_c$; $T_*(n)=\min\{t_c,1/(\bar C\log^2n),1/(2M_*)\}\ge c_1/\log^2n$
  for $n\ge2$ with $c_1=\min\{t_c\log^22,\log^22/(2M_*),1/\bar C\}$ — this removes the
  probe's $n_0$ bookkeeping; small $n$ is absorbed into the constant on both branches
  (large-gap: $8C_K\log n/3\le(8C_K/(3\log2))\log^2n$ for $n\ge2$).

## Notable proof-engineering choices and dead ends

- **Restart route.** Two routes were available for dossier 2: (i) the prescribed
  strong-Markov restart with conditional application of the certified fixed-prior
  lemma; (ii) a direct conditional-Itô rerun of the certified proof on
  $[\sigma,\infty)$.  Route (ii) was rejected: the certified proof's $L^2$-closure
  from $C_c^\infty$ tests passes an integrated inequality through weak limits, and
  redoing that closure conditionally on $\mathcal F_\sigma$ (weak limits inside a
  conditional expectation) is genuinely awkward; route (i) needs only the *statement*
  of the certified lemma at a frozen prior.  This is why the dossier proves the full
  identification machinery instead.
- **Additive noise kills the SDE machinery.** The observation/tilt equation
  $c_u=\int_0^u\mathsf a(\nu;s,c_s)ds+w_u$ is, per path, a deterministic integral
  equation with a globally Lipschitz drift (Brascamp–Lieb constant
  $\kappa^{-1}\le\varepsilon^{-1}$).  So "weak uniqueness of the localization SDE"
  is realized in the strongest available form: a deterministic Banach-fixed-point
  solution map $\mathsf S_\nu$, pathwise uniqueness for free, and uniqueness in law as
  the push-forward $\mathsf S_\nu\#\mathbb W$.  The same map yields the law
  identification needed to apply the published `thm:KL-window` to the planted
  realization (dossier 4, its Lemma 2) — a step the probe consumed silently and which
  I flagged and proved.
- **Fourth-moment identity in $[0,\infty]$.** Proving
  $\lambda\mathbb Ef^4=3\mathbb Ef^2|\nabla f|^2$ via truncated cubics and two-sided
  monotone convergence avoids any $L^p$ bound on $|\nabla f|$ (a first draft used the
  Bakry–Émery gradient commutation to put $|\nabla f|$ in every $L^p$; unnecessary —
  discarded).  Only $f\in L^4$ (hypercontractivity) is needed, and only to license the
  final rearrangement.
- **$H_t$ zero-convention.** The tensor is defined everywhere by
  $H_t=\mathsf H(\mu_t)$ with $\mathsf H=0$ where the defining integrals fail to
  converge absolutely; this makes the restart identity
  $H_{\sigma+u}=\mathsf H(\Theta(\mu_\sigma;u,\tilde c_u))$ exact pathwise (not just
  a.e.) and is shown to affect no integral.
- **No correction to the probe's mathematics was needed.**  The one presentational
  fix: the probe's Lemma C first-moment display is unused; only the second-moment
  optional projection is proved and consumed.

## Standing summary

| dossier | standing | unresolved premises |
|---|---|---|
| `lem-mm-stopped-window-source` | conditional | `thm:letwin-qcts` (preprint-unreviewed import) |
| `lem-mm-restart-deweighting` | unconditional | none (consumes certified `lem:mm-time-weighted-fixed-source`) |
| `lem-mm-smallgap-fourth-moment` | unconditional implication | published import `thm:klartag-logn` (ledger acceptance pending) discharges its hypothesis |
| `prop-mm-window-occupation` | conditional | `thm:letwin-qcts`; plus certification of the three companion dossiers; plus ledger acceptance of `thm:klartag-logn` |

Hypotheses actually used are itemized in a closing remark of each dossier; none is
used silently.  In particular: dossier 1 does not use isotropy; dossier 2 does not use
the eigenfunction equation or Letwin; dossier 3 does not use localization or Letwin;
dossier 4's only $n$-dependent inputs are the two published windows/frontiers.

## Build results

`cd solutions && latexmk -pdf -outdir=../build <id>.tex`, all four:

- `lem-mm-stopped-window-source` — exit 0, no errors, no over/underfull boxes; 9
  unresolved cross-module `\ref`s (expected `??` standalone), 0 unresolved citations.
- `lem-mm-restart-deweighting` — exit 0, clean log; 7 unresolved `\ref`s.
- `lem-mm-smallgap-fourth-moment` — exit 0, clean log; 2 unresolved `\ref`s.
- `prop-mm-window-occupation` — exit 0, clean log; 34 unresolved `\ref`s (it cites the
  three companion theorem labels plus manuscript labels).

## Fence-by-fence check (summary; full paragraphs in each dossier)

The four candidate nodes carry no `bounded_by` edges; all registered obstructions were
checked anyway, per dossier: no cut/slice/excess estimate (`rem:two-tail-slice-bounds`,
`rem:profile-circularity`, `rem:single-coordinate-cuts`); the only tensor input is the full
symmetric-matrix Letwin bound with its conditional standing displayed
(`rem:projection-ceiling`); no crude covariance integral or relative occupation premise
(`rem:crude-insufficient`, `rem:relative-ceiling` — the frontier input produces a
strictly weaker output); `prop:covariance-spike` respected constructively (all
operator-norm usage is stopped; no beyond-window claim); the recorded
marginal-independence, moving-projector, rank-entrance, and weight-removal dead ends
are each avoided by construction and said so where relevant.  Constraint 6: only
`conj:mm-spectral-occupation` is touched; nothing crosses to `conj:trace-upgrade`,
`conj:stein-weighted`, or `conj:product-alignment`.  Scope fences (not the gate, no universal time,
no beyond-window, no frontier improvement, conditional standing) are stated up front
in dossier 4 as required.

## No applicable ledger delta

All four dossiers ship `checked_by: none`, which has no ledger value.  Deferred
artifact candidates only, for the orchestrator after independent review: the four
candidate nodes of the w4s01 proposed delta would receive
`solution: solutions/<id>.tex` plus a real `checked_by` and `review:` once each passes
a cold check; `lem:mm-restart-deweighting` and `lem:mm-smallgap-fourth-moment` could
then be `proved`-eligible (the latter once `thm:klartag-logn` is an accepted import),
while `lem:mm-stopped-window-source` and `prop:mm-window-occupation` remain at most
`conditional` on `thm:letwin-qcts` (constraint 7).  `conj:mm-spectral-occupation` is
unaffected.  No numerics were used or requested.

```yaml
outcome: complete
artifacts:
  - solutions/lem-mm-stopped-window-source.tex
  - solutions/lem-mm-restart-deweighting.tex
  - solutions/lem-mm-smallgap-fourth-moment.tex
  - solutions/prop-mm-window-occupation.tex
  - research/explorations/2026-08-30-prover-mm-window-chain-w4p02.md
proposed_deltas:
  - none (checked_by: none has no ledger value; solution/checked_by wiring is deferred until independent review passes)
next_role: proof-checker
next_prompt: |
  Cold-review the Route-S window chain: four candidate dossiers by author
  claude-prover-w4p02, all checked_by: none, reviewed as four separate reviews by
  distinct cold checkers (one per review:<dossier> key), in dependency order
  (1),(2),(3) then (4). Reconstruct every proof from repository artifacts only; do not
  consult the prover's conversation.

  (1) solutions/lem-mm-stopped-window-source.tex. Claim (CONDITIONAL on
  thm:letwin-qcts, modules/kls/14-qcts-obstruction.tex): for every smooth mu with
  Hess V >= eps I > 0, fixed f in L^2(mu) with Var_mu(f)=1, L>=1, T>0, tau_L the first
  time ||A_t||_op >= L: E int_0^{T wedge tau_L} ||H_t||_HS^2 dt <= 8 L^2 T. Check: the
  Bayes/Cameron-Martin fixed-time identification; a.e. definedness of H_t; the whitened
  duality ||A^{-1/2}HA^{-1/2}||_HS <= sqrt(8 v_t) (symmetric-matrix duality, Letwin on
  the whitened posterior); ||A_t||_op < L strictly before tau_L needing no
  stopping-time theory; E v_t <= 1 via E m_t^2 >= (E f)^2 (f is not assumed centered);
  Tonelli. Verify no independence step and no unstopped ||A_t||_op moment occurs, and
  that the conditional standing is carried in statement and header.

  (2) solutions/lem-mm-restart-deweighting.tex. Claim (UNCONDITIONAL): for every a.s.
  positive stopping time sigma of the usual augmentation of the observation filtration,
  a.s. on {sigma<infty}: E[int_sigma^infty ||H_t||^2 dt | F_sigma]
  <= Var_{mu_sigma}(f)/(eps+sigma) <= v_sigma/sigma. This is the heaviest dossier;
  audit each of the seven steps: fixed-time Bayes identification and its transfer to
  the augmented filtration (reverse martingale convergence); dyadic optional sampling
  giving the optional-time identification and the rcd property of mu_sigma; f in
  L^2(mu_sigma) a.s.; (eps+sigma)-strong log-concavity of mu_sigma; the innovation BM
  (Levy) and the dyadic strong-Markov proof; the exact restart algebra; the
  deterministic Banach-fixed-point solution map for the tilt equation (Brascamp-Lieb
  Lipschitz constant 1/kappa), its measurability via Picard iterates, and pathwise
  uniqueness; the freezing/monotone-class step; and the evaluation at a frozen prior
  via the certified lem:mm-time-weighted-fixed-source with kappa = eps+sigma
  (verify the certified statement is consumed as stated, nonnegative terms dropped
  legitimately, MCT in T). Confirm the H_t zero-convention affects no integral.

  (3) solutions/lem-mm-smallgap-fourth-moment.tex. Claim (implication; hypothesis
  discharged by the published import thm:klartag-logn, cite Klartag2023Logarithmic,
  ledger acceptance pending): if C_P <= K_n for all isotropic log-concave laws on R^n,
  then any normalized first eigenfunction of a regular isotropic approximant with
  lambda <= 3/(8 K_n) has E f^4 <= 2. Check: hypercontractive qualitative L^4 bound
  (finiteness only); the truncated-cubic pairing and the two-sided monotone
  convergence giving lambda E f^4 = 3 E f^2 |grad f|^2 in [0,infty]; the Lipschitz
  post-composition/form-domain step; Poincare for f^2 under the K_n hypothesis;
  the rearrangement needing E f^4 < infty. The 4/3-coefficient non-circularity remark
  must remain a remark, not a claim.

  (4) solutions/prop-mm-window-occupation.tex. Claims (CONDITIONAL on thm:letwin-qcts;
  also contingent on certification of (1)-(3)): (a) with Cbar >= 1 WLOG and
  T0(n) = min(t_c, 1/(Cbar log^2 n)), every regular isotropic approximant (n>=2) with
  lambda <= 3/(8K_n) satisfies E int_0^T ||H||^2 <= 34 T for all T <= T0(n), i.e. the
  conj:mm-spectral-occupation hypothesis with C0=34, C1=0, no damping consumed; (b) hence
  C_P <= C log^2 n for every isotropic log-concave law on R^n, n>=2, conditional on
  thm:letwin-qcts. Check especially: continuity of A_t, tau_2 a stopping time with
  tau_2 > 0 and {tau<=T} in F_tau; the law-identification lemma transferring
  thm:KL-window (modules/kls/15-covariance-technology.tex, [KLnotes Thm 61]) to the
  planted realization through the deterministic solution map; the optional projection
  E[v_tau^2 1_{tau<=T}] <= E f^4 (conditional Jensen at the stopping time); the tail
  integral E[tau^{-2} 1_{tau<=T}] <= (T^{-2}+2Cbar/T+2Cbar^2) e^{-1/(Cbar T)}
  <= 5 Cbar^2 T^{-2} e^{-1/(Cbar T)} for T <= min(1, t1(n)); the definition and
  well-definedness of t_c via monotonicity of h(t) = sqrt5 Cbar t^{-2} e^{-1/(2Cbar t)}
  on (0, 1/(4Cbar)]; the constant chain 32 + sqrt2 <= 34; the fixed-n rerun of the
  certified bridge (q-identity finiteness from the eps-dependent caps, Bessel,
  q <= 1+34t with no Gronwall, terminal variance >= 1/2 at T_*(n), posterior
  Brascamp-Lieb, T_*(n) >= c1/log^2 n for n>=2, the large-gap branch, and the
  certified fixed-test approximation passage at fixed n). Verify the scope fences
  stated in the dossier: not conj:mm-spectral-occupation, no universal-time or
  beyond-window claim, no frontier improvement (the output log^2 n is strictly weaker
  than the published log n input), nothing about conj:trace-upgrade/conj:stein-weighted/
  conj:product-alignment, conditional standing under constraint 7.

  For each dossier: write one review in research/reviews/ under the structured
  contract, verdict pass/revise, naming author claude-prover-w4p02 and yourself as a
  distinct reviewer. Builds: all four compile with latexmk -pdf -outdir=../build from
  solutions/, exit 0, no errors or bad boxes; cross-module refs show ?? standalone as
  expected. No ledger edit: the orchestrator wires solution/checked_by/review only
  after your verdicts, and (1) and (4) remain at most conditional under constraint 7.
```
