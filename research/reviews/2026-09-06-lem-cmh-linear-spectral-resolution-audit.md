---
verdict: revise
authors:
- prover w4p03 (Claude agent, session 2026-08-30)
reviewer: /w5/reviewer-clsr
fingerprints:
  solutions/lem-cmh-linear-spectral-resolution.md: a870f5351dae6061153ae3523bb6f5d10cbf6f62f7b6e8f2de5cead9f0556c26
  lem:cmh-linear-spectral-resolution: 1acf8cd4ee1e8840de2a9816181ad28d515e592d55c5ab6f670587c83e2ba716
  thm:regular-moment-map-compact-target: 6c5fc0b83ba7ee921113bb0cac813d6c92fd41e9b1a9dda5247df865f76eb813
  def:cmh: 5093f7f871d8362c179b6ca901822ba370d6a14237ed9bb3fe076ab964ff9722
---

# `lem:cmh-linear-spectral-resolution` — cold certification review (lens `certify`), no certification

Subject: `solutions/lem-cmh-linear-spectral-resolution.tex`, SHA-256
`85e5a77107f71ccbde028f6c49172d1513879a1491b25205d308d9e30fdfa4ce` (1124 lines; the copy at
commit `29be4d6`, unchanged in the working tree). Ledger node
`lem:cmh-linear-spectral-resolution` (`status: open`, no `proofs[]` record); manuscript
statement `modules/kls/41-cmh-normalization.tex` lines 269–291 (identical at `HEAD` and in the
working tree, which carries unrelated uncommitted additions elsewhere in the same module).
Dossier author: `prover w4p03 (Claude agent, session 2026-08-30)` (header line 18). Reviewer:
`/w5/reviewer-clsr`, run `w5r01`, concurrency key
`review:solutions/lem-cmh-linear-spectral-resolution.tex`. The author's narrative was not
available and was not used; the wave-four orchestrator record
`research/explorations/2026-08-31-orchestrator-kls-angles-wave-w4.md` and the probe record
`research/explorations/2026-08-30-kls-route-prober-cmh-anisotropic-bootstrap-w4c01.md` were
read only to fix the intended claim set (P0–P3, P6, P7), never as mathematical evidence.

This report **does not certify** the node. Every proof step of the dossier was checked line by
line and no mathematical error was found in any of them; the reason for the audit verdict is a
**statement-agreement failure** (lens item 1): the manuscript statement and the ledger summary
assert the column equation $(1-\Aop)(Ha)=(A+Q)a$ as an operator identity, and the dossier
proves — and says it proves — only its weak (closed-form) version. Three smaller items are
listed with it. Repair instructions are exact and are repeated in the handoff.

Standalone build: `cd solutions && latexmk -pdf -interaction=nonstopmode -outdir=../build
lem-cmh-linear-spectral-resolution.tex` exits 0, 11 unresolved cross-module `\ref`s (expected),
no LaTeX errors, PDF produced.

## Findings

### 1. Statement agreement (the blocking finding)

| clause of the manuscript lemma (lines 270–290) | ledger `summary` | dossier `thm:sol-clsr-main` | agreement |
|---|---|---|---|
| regular isotropic compact-target moment map; $\Aop=-\calL$, $\calL f=e^{\psi}\operatorname{div}(e^{-\psi}H^{-1}\nabla f)$ | same | Def. `def:sol-clsr-class` + part (a) | yes; log-concavity is the module's standing hypothesis (line 24 of the module) and is explicit in the dossier |
| $u_b=\partial_b\psi$ centered orthonormal eigenfunctions at the Brascamp–Lieb gap $1$ | same | part (b) | yes |
| $(1-\Aop)(Ha)=(A+Q)a$ | `(1-A_op)(Ha)=(A+Q)a` | part (c): **weak form only**, eq. `eq:sol-clsr-weak-column`, with `rem:sol-clsr-weak-vs-strong` (l. 276) and `rem:sol-clsr-gap` (l. 731) stating the strong form is *not* proved on the class | **no** |
| $(A+Q)a\perp u_b$; $\int(A+Q)\,d\eta=I$ | same | part (c) | yes |
| decomposition $Ha=a+\sum_bM_{ab}u_b+v$ and the three resolution identities | same | part (d) | yes, *provided* $\langle v,\Aop v\rangle$ is read as the form value $\sum_i\calE(v_i)$ (dossier says so explicitly; manuscript and ledger do not) |
| $\mathsf R\preceq I$, equality iff spectrally pure at the gap | same | (C1) | yes |
| $(\mathrm{AB})_{\rho,\beta}\iff$ channel inequality | same | (C2) | yes, but $(\mathrm{AB})_{\rho,\beta}$ and $Q_{\rm lin}$ are **undefined in the manuscript** (they occur only inside this lemma); the dossier defines both |
| $\mathsf R\succeq\mathsf N-nI$, $Q_{\rm lin}\le n+1$ | same | part (f) | yes |
| $\mathsf R\succeq\mathsf D$ on regular finite products | same | part (g) | yes |

Why the third row is a defect and not a reading convention. The manuscript's own conventions
(`subsec:cmh-conventions`) define $\Aop$ as *the nonnegative self-adjoint operator of the closed
form*. An identity $(1-\Aop)(Ha)=(A+Q)a$ with that $\Aop$ asserts $(Ha)_i\in\Dom(\Aop)$. The
dossier's Remark `rem:sol-clsr-gap` correctly proves this is equivalent to
$(A+Q)a\in L^2(\eta;\R^n)$ and states that the dossier establishes only $\Tr(A+Q)\in L^1(\eta)$
on the general class ($L^2$ is proved on products, `rem:sol-clsr-product-strong`). So the
dossier does not prove the clause as written; the dossier says so; and a certification would
attach a `proofs[]` record to a node whose manuscript text claims more than the artifact proves.
Under `CLAUDE.md` constraint 4 that is exactly what the reviewer exists to stop.

I checked the equivalence in `rem:sol-clsr-gap` myself: given the weak equation for all $f$ in
the core (which is dense in $\Dom(\calE)$), $(A+Q)a\in L^2$ makes the right side continuous in
the form norm, hence $\calE(f,w_i)=\langle f,w_i-((A+Q)a)_i\rangle$ for all $f\in\Dom(\calE)$
and $w_i\in\Dom(\Aop)$ by the representation theorem; conversely $w_i\in\Dom(\Aop)$ forces
$((A+Q)a)_i=w_i-\Aop w_i$ a.e. (an $L^1$ function annihilated by the core is zero), hence $L^2$.
Correct. Whether $\Tr Q\in L^2(\eta)$ actually holds on the compact-target class is not decided
by this report and I did not attempt to prove or refute it.

### 2. Barriers

The node carries no `bounded_by`. The dossier's closing audit (lines 1097–1124) walks the six
obstruction nodes and the CMH guardrails; I confirm that no localization, no stochastic
covariance bootstrap, no pointwise Loewner promotion of the cyclic square (it is used under the
trace only), no kernel transport through a noninvertible map, and no semicontinuity claim
appears. P1 (trace-upgrade cluster) is respected: no member of the cluster is touched.

### 3. Hypothesis accounting

Used: (H1) $P$ a convex body, $\mu=e^{-V}\mathbf 1_{\operatorname{int}P}dx$ with
$V\in C^\infty(\R^n)$, centered, isotropic, $D^2V\succeq0$ on $\operatorname{int}P$. Log-concavity
is load-bearing (positivity of $A$ in Lemmas `normalization`, `form-membership`, `cyclic`, and
part (g)); it is the module's standing hypothesis but is not repeated inside the lemma —
acceptable, noted. (H2) `thm:regular-moment-map-compact-target` (smoothness, diffeomorphism,
weak Stein identity with zero flux, $\E_\mu\tau=I$). (H3) Klartag's Hessian bound. (H4)
Brascamp–Lieb. (H5) CEK uniqueness (part (g) only). (H6) closability and the form core, reused
from the certified normalization dossier. Stated but unused: the ledger `depends_on` lists
`prop:cmh-bochner`; the dossier (line 1082) says no identity consumes it. Under constraint 8
this is a sharpening opportunity: drop it from `depends_on` when the record is wired.

### 4. Dependency and applicability

`depends_on`: `thm:regular-moment-map-compact-target` (proved, literature, published),
`def:cmh` (defined), `prop:cmh-bochner` (proved; unused). No open dependency. `assumes` is empty
and nothing in the proof is conditional. P2 is not engaged.

### 5. Citation debt

| source | role | classification | what I verified |
|---|---|---|---|
| Klartag, *Log-concave moment measures I*, LNM 2116 (2014), arXiv:1309.2767 | $0\prec H\preceq2R^2I$ | **published** | Read Theorem 1.1 in the arXiv text: under conditions (1) — $K$ bounded, $\rho$ $C^\infty$ with all derivatives bounded on $K$ — and barycenter at the origin, it states $\Delta\psi(x)\le2R^2(K)$ for all $x$. The dossier's Loewner form follows in one line from $H\succ0$ ($H\preceq(\Tr H)I$). The dossier's class satisfies (1) because $V\in C^\infty(\R^n)$ and $\overline P$ is compact. Line 99 says "Theorem 1.1 gives the pointwise bound $H\preceq2R^2I$"; it should say the theorem bounds $\Delta\psi$ and that the Loewner bound is the immediate consequence. Also Klartag §6 eq. (89) restates Brascamp–Lieb exactly in the form the dossier uses, with equality at $u=\nabla\psi\cdot\theta$. |
| Brascamp–Lieb 1976, JFA 22 | $\Var_\eta f\le\int\langle H^{-1}\nabla f,\nabla f\rangle d\eta$ | **published** | Primary text is paywalled (sciencedirect 403 with my tools). The statement used is verified against its restatement in the published Klartag paper above, eq. (89), for smooth $u$ with $ue^{-\psi}$ integrable, which covers every core pullback; the closure argument to $\Dom(\calE)$ is the dossier's own and is checked below. A literature-scout confirmation of Theorem 4.1 of the primary is requested for completeness; it does not change this verdict. |
| Cordero-Erausquin–Klartag 2015, JFA 268, arXiv:1304.0630 | uniqueness of the moment potential up to translation (part (g)) | **published** | Read Theorem 2 in the arXiv text: for $\mu$ finite, not supported in a hyperplane, barycenter at the origin, the essentially-continuous convex $\psi$ with moment measure $\mu$ exists and is unique up to translation. The product potential is finite and convex on $\R^n$, hence essentially continuous; the dossier's use is correct. |
| Berman–Berndtsson 2013; Fathi 2019 (Thm 2.3) | through the certified literature node `thm:regular-moment-map-compact-target` | published (node's own classification) | Not re-audited (certified dependency node). I did read Fathi's definition: a Stein kernel satisfies $\int x\cdot f\,d\mu=\int\langle\tau,\nabla f\rangle_{\HS}d\mu$ for *any smooth* $\R^d$-valued $f$; the dossier's "ambient test form" with $F\in C_c^\infty(\R^n)$ (Lemma `eigen`, line 627 ff.) is within that class. |

No unreviewed preprint is load-bearing (the trace bound $\Tr\mathsf N\le2n$ is re-derived, not
imported from Chen–Klartag). No run artifact is cited.

### 6. The steps, line by line

All checked; none failed. Where I note something it is editorial, except D2.

- **Setting and operator data** (l. 60–160). Monge–Ampère $\log\det H=-\psi+V\circ\nabla\psi$
  is the change of variables in $(\nabla\psi)_\#\eta=\mu$: correct. Form core
  $\mathscr D=\{F|_{\operatorname{int}P}:F\in\R+C_c^\infty(\R^n)\}$, closability reused from
  `solutions/thm-cmh-normalization.tex` Lemma `lem:sol-cmh-dirichlet` (certified). I
  re-derived closability on this core directly (limit of $\tau^{1/2}\nabla f_k$ tested against
  $C_c^\infty(\operatorname{int}P;\R^n)$ vanishes), fine. $\ker\Aop=\R\mathbf 1$: correct on a
  connected support. Core energy bound $n\|\nabla f\|_\infty^2$: correct.
- **(MA1)** and Lemma `symmetric-form` (l. 300–325): $\partial_iH^{ij}=\psi_bH^{bj}-V_j\circ\nabla\psi$;
  verified index by index; $\calL=e^{\psi}\partial_i(e^{-\psi}H^{ij}\partial_j\cdot)$ follows.
- **Pullback dictionary**: $\nabla_yf=H\nabla_xg$, $\calL(g\circ\nabla\psi)=(L_\mu g)\circ\nabla\psi$
  using $H^{ij}\psi_{ai}\psi_{bj}=H_{ab}$ and (MA1); correct.
- **Lemma `MA2`** (twice-differentiated Monge–Ampère): I differentiated (MA1) in $y_\ell$ and
  recovered $\calL H_{k\ell}+H_{k\ell}=A_{k\ell}+Q_{k\ell}$ with
  $Q_{k\ell}=H^{ia}H^{bj}\psi_{ijk}\psi_{ab\ell}=\Tr(H^{-1}\partial_kH\,H^{-1}\partial_\ell H)$;
  positivity of $A$ (log-concavity) and of $Q$ (HS norm of $H^{-1/2}S_cH^{-1/2}$): correct.
- **Coercivity** (l. 396–412): ray argument via the recession slope and Fubini; correct.
- **Cutoffs**: $\zeta_m=\chi_m(\psi)$, $|\nabla\zeta_m|\le2R/m$; correct.
- **Lemma `ibp`** (l. 420–437). (i) correct. (ii) **D2**: the lemma requires $X'$ supported in a
  *compact* subset of $\R$, but Lemma `cutoff` (l. 447) applies it with $X'=\chi_m$, whose support
  is $(-\infty,2m]$. The proof of (ii) only uses $\sup\operatorname{supp}X'<\infty$ (the field
  is supported in $\{\psi\le\sup\operatorname{supp}X'\}$, compact by coercivity since $\psi$ is
  bounded below), so the argument is valid; the *statement* of (ii) must be weakened to
  "$X'$ vanishing on $[t,\infty)$ for some $t$". Editorial, but it is a hypothesis not met by its
  application and must be fixed.
- **Cutoff energy** $\kappa_m\le2(n+c_VR)/m$: uses $\chi_m'\le0$, $|\langle\nabla V\circ\nabla\psi,\nabla\psi\rangle|\le c_VR$; correct.
- **Pointwise dominations** (i)–(iii): (i) is the dual-norm computation with
  $\sup_{|\zeta|=1}\|S_{H^{-1/2}\zeta}\|_{\HS}^2\le\sum_\beta\|S_{H^{-1/2}e_\beta}\|_{\HS}^2=\mathfrak g$;
  (ii) $\mathfrak g=\Tr(H^{-1}\Gamma)\ge\|H\|_{\op}^{-1}\Tr\Gamma$; (iii) two Cauchy–Schwarz. All correct.
- **Finite total column energy** (l. 500–540): the cutoff identity
  $\mathcal D_m+\mathcal T_m=\int\zeta_m^2\Tr H^2+\mathrm{Err}_m$, the bound
  $|\mathrm{Err}_m|\le\eps_m\mathcal D_m^{1/2}$, the quadratic inequality, monotone convergence
  along the nested dyadic sequence, then passage to the limit in the identity: correct. This
  is the analytic heart and it holds.
- **Normalization** $\int(A+Q)d\eta=I$: correct (monotone convergence on the nonnegative side,
  dominated on $\int\zeta_mh$, polarization; entry integrability from positivity).
- **Form membership and weak column equation** (l. 569–623): $\zeta_mf$ is a core element
  (support $\nabla\psi(\{\psi\le2m\})\Subset\operatorname{int}P$); $\calE^0(\zeta_mf-f)\to0$;
  closedness; the three limits in (iii) with the stated dominations
  ($\Tr(A+Q)+2R^2\in L^1$, product of two $L^2$ functions, $\kappa_m^{1/2}$). Correct.
- **Eigenfunctions** (l. 627–658): centering and orthonormality are direct from
  $\E X=0$, $\Cov=I$; $\ell_b\in\mathscr D$; the weak Stein identity gives
  $\calE^0(f,\ell_b)=\langle f,\ell_b\rangle$ on the core; continuity and density extend it;
  representation theorem gives $\Aop\ell_b=\ell_b$. Correct.
- **Brascamp–Lieb gap** (l. 661–680): applies to core pullbacks (finite energy), passes to
  $\Dom(\calE)$ by form-norm approximation; spectrum on $\mathbf 1^\perp$ in $[1,\infty)$;
  attained. Correct (and consistent with Klartag (89)'s equality case).
- **Orthogonality** and **third-moment tensor** (l. 690–730): integrability of $\psi_{kib}$
  via domination (ii); the cutoff integration by parts with error $\le2R^2\cdot2R/m$; total
  symmetry; $(M_a)_{ib}=(\Theta_ba)_i$. Correct.
- **Resolution (d)** (l. 756–810): $\langle w_i,\mathbf 1\rangle=a_i$; $v_i\perp\mathbf 1,u_b$;
  Pythagoras; $a^\top\mathsf Da=\sum_i\calE(w_i)$ (I verified
  $(\partial_bH)_{km}a_k=\partial_bw_m$); bilinear expansion with
  $\calE(u_b,\cdot)=\langle u_b,\cdot\rangle$; subtraction. Correct. $T_a\ge0$ by BL. Correct.
- **Anticommutator proposition**: absolute convergence, $f=w_i$ in the weak equation, symmetry
  of $\tfrac12a^\top\{H,A+Q\}a$. Correct.
- **C1–C5** (l. 826–870): spectral-measure characterization of $T_a=0$; the algebra of C2, C3
  (including $\langle v,(2\Aop-1)v\rangle\ge\|v\|^2$ and $\|M_a\|^2=a^\top\sum_b\Theta_b^2a$),
  C4, and the basis sum in C5. All correct.
- **Cyclic square** (l. 878–912): the two eigenframe expansions, the symmetrized coefficient
  $[(\lambda_p-\lambda_q)^2+(\lambda_q-\lambda_r)^2+(\lambda_r-\lambda_p)^2]/(6\lambda_p\lambda_q\lambda_r)$,
  and $\Tr(HA)\ge0$. Correct.
- **Part (f)** (l. 914–936): $\mathsf D\succeq0$; $\Tr\mathsf R\ge\Tr\mathsf D$ from the trace
  identity and the cyclic square; $\Tr\mathsf N\le2n$, $\Tr\mathsf D\le n$ from tracing
  $\mathsf N-I\preceq\mathsf D$; $\mathsf R\succeq\mathsf N-nI$; $Q_{\rm lin}\le n+1$. Correct.
- **Part (g), products** (l. 955–1000): membership of the product in the class;
  identification of the canonical potential via CEK uniqueness and translation invariance of
  all matrices; diagonalization; the exact one-dimensional identity $HQ=(\psi''')^2/\psi''$;
  $(\mathsf R-\mathsf D)_{kk}=\int V_k''(\psi_k')(\psi_k'')^3e^{-\psi_k}\ge0$. Correct.
  `rem:sol-clsr-product-strong` (boundedness of $Q_{kk}$ from the one-dimensional (MA1)) is correct.
- **Calibrations** (§9): remarks only; I spot-checked the exponential ($\mathsf N=2$,
  $\|M_a\|^2=1$, $\|v\|^2=0$) and the Laplace ($\mathsf N=5/4$ with $\tau=|x|/\sqrt2+1/2$);
  they are consistent and carry no proof weight, as the dossier says.

### 7. Defect list

- **D1 (blocking; statement agreement).** Manuscript line 275–276 and ledger line 1196 assert
  $(1-\Aop)(Ha)=(A+Q)a$ as an operator identity; the dossier proves the weak form only
  (`eq:sol-clsr-weak-column`) and states the strong form is open on the class.
- **D2 (dossier, editorial but a hypothesis mismatch).** Lemma `lem:sol-clsr-ibp`(ii), line 423:
  hypothesis "$X'$ supported in a compact subset of $\R$" is not satisfied by its application
  at line 447 ($X'=\chi_m$). Proof already covers the weaker hypothesis.
- **D3 (dossier, citation precision).** Line 99–104: Klartag's Theorem 1.1 bounds $\Delta\psi$,
  not $H$ in Loewner order; add the one-line deduction and the hypothesis match with his (1).
- **D4 (manuscript/ledger, wording).** $Q_{\rm lin}$ and $(\mathrm{AB})_{\rho,\beta}$ are used in
  the lemma (lines 286–289) but defined nowhere in `modules/`; $\langle v,\Aop v\rangle$ is a
  form value, which the manuscript and ledger do not say. Orchestrator-owned.
- **D5 (ledger, sharpening).** `prop:cmh-bochner` in `depends_on` is not used by the proof.

## Corrections

Required before a new review can certify (the dossier repairs are the `researcher`'s; the
manuscript and ledger wording are orchestrator deltas — either route for D1 is acceptable, and
the dossier must end up proving the statement that is written):

1. **D1, route (a) — repair the dossier:** prove $(A+Q)a\in L^2(\eta;\R^n)$ (equivalently
   $\Tr Q\in L^2(\eta)$, since $\Tr A$ is bounded) on the class of `def:sol-clsr-class`; then
   `rem:sol-clsr-gap` becomes the strong column equation and the manuscript display is proved
   literally. Or **route (b) — align the statement:** replace, in
   `modules/kls/41-cmh-normalization.tex` lines 275–276, "the columns $Ha=\nabla(\partial_a\psi\cdot a)$
   satisfy $(1-\mathsf A_{\rm op})(Ha)=(A+Q)a$" by "the columns $Ha=\nabla\langle a,\nabla\psi\rangle$
   lie in $\Dom(\calE)$ and satisfy the column equation in the weak form
   $\calE(f,(Ha)_i)=\langle f,(Ha)_i\rangle-\langle f,((A+Q)a)_i\rangle$ for every bounded smooth
   finite-energy $f$ (with $(A+Q)a\in L^1(\eta)$)", and make the matching change to the ledger
   `summary` at `research/program/ledger.yaml` line 1196 ("the columns satisfy the weak column
   equation E(f,Ha)=<f,Ha>-<f,(A+Q)a> for bounded smooth finite-energy f"). Under route (b) the
   dossier text needs no mathematical change; `rem:sol-clsr-weak-vs-strong` should then say the
   manuscript states the weak form and that the strong form is a separate open question.
2. **D2:** in `solutions/lem-cmh-linear-spectral-resolution.tex` line 423 replace "with $X'$
   supported in a compact subset of $\R$" by "with $X'$ vanishing on $[t,\infty)$ for some
   $t\in\R$", and in the proof (line 434–436) keep "support in the compact set
   $\{\psi\le t\}$ (Lemma `coercive`)".
3. **D3:** at lines 99–104 write: "Theorem 1.1 of [Klartag] gives $\Delta\psi\le2R(P)^2$ on
   $\R^n$ for a centered log-concave target on a bounded convex $P$ whose potential $V$ is
   smooth with all derivatives bounded on $P$ (his conditions (1), satisfied here since
   $V\in C^\infty(\R^n)$ and $\overline P$ is compact); since $H\succ0$, this yields
   $H\preceq(\Tr H)\Id\preceq2R(P)^2\Id$."
4. **D4 (orchestrator):** before the lemma in `modules/kls/41-cmh-normalization.tex`
   (after line 268) add one sentence defining, in isotropic source coordinates,
   $Q_{\rm lin}(\mu):=\lambda_{\max}(\mathsf N)=\sup_{|a|=1}\int|Ha|^2d\eta$ and
   $(\mathrm{AB})_{\rho,\beta}:\ \mathsf R\succeq\rho\mathsf N-\beta I$; and state that
   $\langle v,\mathsf A_{\rm op}v\rangle$ denotes the closed-form value $\sum_i\calE(v_i)$.
5. **D5 (orchestrator, optional):** drop `prop:cmh-bochner` from `depends_on` of the node when
   the `proofs[]` record is wired (constraint 8).

## Exclusions

Not certified by this report: any statement about $(\mathrm{AB})_{\rho,\beta}$ with universal
constants, any bound on $\CMH$, `conj:gate-zero`, `conj:gate-zero-sharp`, the probe's P4
(deficit kernel) and P5 (corrector hierarchy), the strong column equation on the general class,
`lem:linear-sector-third-moment` and `cor:gate-zero-third-moment` (uncommitted, not in scope),
and the literature nodes `thm:regular-moment-map-compact-target` and
`thm:chen-klartag-moment-hessian` (not re-audited). The manuscript/dossier/ledger wording
mismatch on the column equation is reported here under the `certify` lens as a statement
agreement failure; a `sync`-lens audit of the wider module was not performed.
