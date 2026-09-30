---
verdict: pass
authors:
  - "prover w4p03 (Claude agent, session 2026-08-30)"
  - /w5/researcher-clsr-repair
reviewer: /w5/reviewer-clsr-second
fingerprints:
  solutions/lem-cmh-linear-spectral-resolution.md: 74580b1c5580b588a5d6c04ec035808e92544a722dfbfd1dc0c3e4ac520dbde5
  lem:cmh-linear-spectral-resolution: 1acf8cd4ee1e8840de2a9816181ad28d515e592d55c5ab6f670587c83e2ba716
  thm:regular-moment-map-compact-target: 6c5fc0b83ba7ee921113bb0cac813d6c92fd41e9b1a9dda5247df865f76eb813
  def:cmh: 5971e940e93fa8179ce6c80c9817d3b3a88ac7db2ffe56897f1957c02431f9e7
---

# `lem:cmh-linear-spectral-resolution` — cold certification review after repair (lens `certify`)

Subject: `solutions/lem-cmh-linear-spectral-resolution.tex`, working-tree copy, SHA-256
`afb080d21b7241da3513d74ed7b3dc5d10b686138372fae30b93312bc1dae4c9` (1148 lines; the
committed copy at `29be4d6` is the one the first audit read, and it differs from this one by
the repair diff only). Ledger node `lem:cmh-linear-spectral-resolution` (`status: open`, no
`proofs[]` record, working-tree `summary`), manuscript statement
`modules/kls/41-cmh-normalization.tex` lines 274–299 (working-tree version, with the defining
paragraph at lines 266–273). Dossier authors as written in the header (lines 18–19):
`prover w4p03 (Claude agent, session 2026-08-30)` and `/w5/researcher-clsr-repair`. Reviewer
`/w5/reviewer-clsr-second`, run `w5r05`, concurrency key
`review:solutions/lem-cmh-linear-spectral-resolution.tex`. I authored none of this work and no
checkpoint names me.

The earlier audit `research/reviews/2026-09-06-lem-cmh-linear-spectral-resolution-audit.md`
(reviewer `/w5/reviewer-clsr`) was read as a list of items to re-verify, not as evidence. The
authors' checkpoints (`research/explorations/2026-09-06-researcher-clsr-repair-w5p03.md` and the
wave-four records it cites) were not used as mathematical evidence; the repair checkpoint was
opened only to confirm that it names no reviewer identity of mine. Every proof step below was
re-derived by me from the dossier text and the sources; where I say "correct" I mean I
reproduced the computation.

Standalone build: `cd solutions && latexmk -pdf -interaction=nonstopmode -outdir=../build
lem-cmh-linear-spectral-resolution.tex` exits 0, no LaTeX errors, PDF produced; unresolved
cross-module `\ref`/`\cite` standalone as expected. `python3 scripts/check.py` reports 0 errors
on the working tree.

## Findings

### 1. Statement agreement (the item that blocked the first audit)

Clause-by-clause comparison of the manuscript lemma (working tree), the ledger `summary`
(working tree), and `thm:sol-clsr-main` (lines 170–285):

| manuscript clause | ledger `summary` | dossier | agreement |
|---|---|---|---|
| regular isotropic compact-target moment map; $\Aop=-\calL$, $\calL f=e^{\psi}\operatorname{div}(e^{-\psi}H^{-1}\nabla f)$, $H=D^2\psi$ | same | `def:sol-clsr-class` (l. 68–95) + part (a) (l. 176–187) | yes. "Regular compact-target" is the class of `thm:regular-moment-map-compact-target` (convex body, positive $C^\infty(\R^n)$ density, i.e. $V=-\log g\in C^\infty(\R^n)$); log-concavity is the module's standing hypothesis (module line 24) and explicit in the dossier; isotropy explicit in both |
| $u_b=\partial_b\psi$ centered orthonormal eigenfunctions at the Brascamp–Lieb gap $1$ | same | part (b) (l. 188–192) | yes |
| columns $Ha=\nabla\langle a,\nabla\psi\rangle$ lie in $\Dom(\calE)$ and satisfy the **weak** column equation $\calE(f,(Ha)_i)=\langle f,(Ha)_i\rangle-\langle f,((A+Q)a)_i\rangle$ for every bounded smooth finite-energy $f$, with $(A+Q)a\in L^1(\eta)$ | "columns lie in the form domain and satisfy the weak column equation … for bounded smooth finite-energy f, with (A+Q)a in L^1" | part (c) (l. 193–215): $(A+Q)a\in L^1(\eta;\R^n)$, $(Ha)_i\in\Dom(\calE)$, eq. `eq:sol-clsr-weak-column` for every $f\in C^\infty(\R^n)\cap L^\infty$ with $\int\langle H^{-1}\nabla f,\nabla f\rangle d\eta<\infty$; explicitly no $\Dom(\Aop)$ membership asserted | **yes** — this is the repaired D1, route (b). The three texts now assert the same object. "Finite energy" in the manuscript is the energy of the form $\calE$ it has just named, which in source coordinates is $\int\langle H^{-1}\nabla f,\nabla f\rangle d\eta$ by part (a); the dossier's class $\mathfrak B$ is exactly that reading |
| $(A+Q)a\perp u_b$; $\int(A+Q)\,d\eta=I$ | same | part (c), Lemmas `normalization`, `orthogonality` | yes |
| decomposition $Ha=a+\sum_bM_{ab}u_b+v$; $\mathsf N=\int H^2$, $\mathsf D=\int H^{ab}(\partial_aH)(\partial_bH)$, $\mathsf R=\mathsf N-\mathsf D$; the three resolution identities; $\langle v,\Aop v\rangle$ is the closed-form value $\calE(v,v)$ | same, "where <v,A_op v> is the closed-form value" | part (d) (l. 216–239), with $\langle v,\Aop v\rangle:=\sum_i\calE(v_i)$ named as the closed-form value written $\calE(v,v)$ in the lemma | **yes** (repaired D4 half). The manuscript's $M_{ab}$ is a compressed notation for the vector coefficient $(M_a)_{\cdot b}$; dimensions force that reading and the dossier states it |
| $\mathsf R\preceq I$, equality in a direction iff spectrally pure at the gap | same | (C1) (l. 241–244, proof l. 840–851) | yes |
| $(\mathrm{AB})_{\rho,\beta}\iff$ channel inequality for all unit $a$ | same | (C2) (l. 245–254) | yes; $(\mathrm{AB})_{\rho,\beta}:\ \mathsf R\succeq\rho\mathsf N-\beta I$ is now defined in the manuscript paragraph before the lemma (module l. 266–271), matching the dossier |
| $\mathsf R\succeq\mathsf N-nI$ unconditionally, so $Q_{\rm lin}\le n+1$ | same | part (f) (l. 265–274) | yes; $Q_{\rm lin}(\mu):=\lambda_{\max}(\mathsf N)$ is now defined in the manuscript paragraph (module l. 267), matching dossier l. 157–160 |
| $\mathsf R\succeq\mathsf D$ on every regular finite product of one-dimensional laws | same | part (g) (l. 275–284) | yes; under the lemma's isotropy hypothesis each factor is centered with variance one, which is what the dossier assumes |

One residual wording point, not a mathematical disagreement: the letters $A$ and $Q$ are not
named in the manuscript. Their sum is nevertheless pinned by the manuscript: the differentiated
Monge–Ampère identity `eq:differentiated-MA` (`modules/kls/04-family-moment-map.tex` l. 95–99)
displays $\calL H_{ij}+H_{ij}=(H\,\Hess V(\nabla\varphi)\,H)_{ij}+\varphi^{ac}\varphi^{bd}\varphi_{abi}\varphi_{cdj}$,
whose two terms are the dossier's $A$ and $Q$ (`eq:sol-clsr-AQ-def`, l. 143–147; I checked
$\varphi^{ac}\varphi^{bd}\varphi_{abi}\varphi_{cdj}=\Tr(H^{-1}\partial_iH\,H^{-1}\partial_jH)$),
and the lemma uses only the sum $A+Q=\calL H+H$. I record this as an orchestrator-side
sharpening (add "where $A=H(D^2V\circ\nabla\psi)H$ and $Q_{k\ell}=\Tr(H^{-1}\partial_kH\,H^{-1}\partial_\ell H)$
are the two terms of \eqref{eq:differentiated-MA}" before the lemma); it does not block
certification because the mathematical content of the clause is unambiguous.

The strong (operator-domain) form $(1-\Aop)(Ha)=(A+Q)a$ is no longer asserted anywhere in the
three texts. `rem:sol-clsr-weak-vs-strong` (l. 287–302) and `rem:sol-clsr-gap` (l. 748–763)
state that it is a separate open question on the class, equivalent to $\Tr Q\in L^2(\eta)$, and
`rem:sol-clsr-product-strong` (l. 1016–1024) proves it on products. The "Flagged gaps"
paragraph (l. 1109–1118) records the agreement. I re-checked the equivalence in
`rem:sol-clsr-gap` myself: (b) $\Rightarrow$ (a) by $L^2$-continuity of
$f\mapsto\langle f,w_i-((A+Q)a)_i\rangle$, density of $\mathfrak B\supset\mathscr D$ in
$\Dom(\calE)$ and the representation theorem; (a) $\Rightarrow$ (b) because
$w_i-((A+Q)a)_i-\Aop w_i\in L^1_{\rm loc}$ is annihilated by $C_c^\infty(\operatorname{int}P)$
pullbacks, hence vanishes a.e. Correct, and correctly excluded from the claim.

### 2. Barriers

The node carries no `bounded_by` and no `heuristic_barriers`. The closing audit (l. 1120–1146)
walks the six obstruction nodes and the CMH guardrails; I confirm from the proof text that no
localization, no stochastic covariance bootstrap, no pointwise Loewner promotion of the cyclic
square (Lemma `cyclic` enters only under the trace, l. 950–952), no kernel transport through a
noninvertible map, and no (semi)continuity of $Q_{\rm lin}$ or $\CMH$ appears. Program
constraint P1 is respected: no member of the trace-upgrade cluster is touched. P2 is not
engaged: `assumes` is empty and no step is conditional.

### 3. Hypothesis accounting

Used, all stated: (H1) `def:sol-clsr-class` — convex body $P$, $\mu=e^{-V}\mathbf 1_{\operatorname{int}P}dx$
with $V\in C^\infty(\R^n)$, centered, isotropic, $D^2V\succeq0$ on $\operatorname{int}P$;
log-concavity is load-bearing for $A\succeq0$ (Lemma `MA2`, Lemma `cyclic`, part (g)) and is the
module's standing hypothesis. (H2) `thm:regular-moment-map-compact-target`: smoothness and
strict convexity of $\psi$, $\nabla\psi$ a diffeomorphism onto $\operatorname{int}P$, the weak
Stein identity with zero flux (Lemma `eigen`), $\E_\mu\tau=I$ (Lemmas `normalization`,
`form-membership`(ii), the resolution). (H3) Klartag's Laplacian bound, used wherever
$\|H\|_{\rm op}\le2R^2$ appears (finiteness of $\mathsf N$, boundedness of $u_b,H_{ai}$, Lemmas
`domination`–`form-membership`, `M`, `product-strong`). (H4) Brascamp–Lieb (Lemma `BL` only).
(H5) Cordero-Erausquin–Klartag uniqueness (part (g) only). (H6) The form core
$\mathscr D=\{F|_{\operatorname{int}P}:F\in\R+C_c^\infty(\R^n)\}$ and closability, taken from
the certified `solutions/thm-cmh-normalization.tex` Lemma `lem:sol-cmh-dirichlet`; I
re-derived closability on this core directly (if core $f_k\to0$ in $L^2(\mu)$ and
$\tau^{1/2}\nabla f_k\to G$ in $L^2(\mu;\R^n)$, then testing against
$C_c^\infty(\operatorname{int}P;\R^n)$ fields, where $\rho$ and $\tau$ are smooth and bounded
below, gives $G=0$), and $\ker\Aop=\R\mathbf 1$ on the connected $\operatorname{int}P$.

Stated but unused: the ledger `depends_on` lists `prop:cmh-bochner`; the dossier (l. 1101–1105)
says no identity consumes it, and I confirm — the Bochner identity is not invoked anywhere.
Under `CLAUDE.md` constraint 8 it should be dropped when the `proofs[]` record is wired
(proposed delta below). No hypothesis is used without being stated.

### 4. Dependency and applicability

`depends_on`: `thm:regular-moment-map-compact-target` (`proved`, literature, published),
`def:cmh` (`defined`), `prop:cmh-bochner` (`proved`, unused). No open dependency. `assumes` is
empty. Nothing is conditional.

### 5. Citation debt

| source | role | classification | verified against the source |
|---|---|---|---|
| Klartag, *Logarithmically-concave moment measures I*, LNM 2116 (2014); arXiv:1309.2767 | $0\prec H\preceq2R^2I$ (`rem:sol-clsr-klartag-import`, l. 99–110) | **published** | Read in the arXiv text: conditions (1) — $K$ bounded, $\rho$ $C^\infty$ with $\rho$ and all derivatives bounded in $K$; log-concave meaning density $e^{-\rho}$ on open convex $K$ with $\rho$ convex; Theorem 1.1 — barycenter at the origin, then $\Delta\psi(x)\le2R^2(K)$ for all $x$, $R(K)=\sup_K|x|$. The dossier's class meets (1) since $V\in C^\infty(\R^n)$ and $\overline P$ is compact, is centered, and $D^2V\succeq0$ on $\operatorname{int}P$. $H\preceq(\Tr H)I\preceq2R^2I$ from $H\succ0$ is immediate. The bound is translation-invariant so it applies to the canonical $\psi$. **D3 is repaired correctly.** |
| Brascamp–Lieb 1976, JFA 22 | $\Var_\eta f\le\int\langle H^{-1}\nabla f,\nabla f\rangle d\eta$ (Lemma `BL`) | **published** | Primary is paywalled for my tools. The exact statement used — for smooth $u$ with $ue^{-\psi}$ integrable, $\int ue^{-\psi}=0\Rightarrow\int u^2e^{-\psi}\le\int\langle(\nabla^2\psi)^{-1}\nabla u,\nabla u\rangle e^{-\psi}$, with equality at $u=\nabla\psi\cdot\theta$ — is restated as eq. (89) of the published Klartag paper above, §6, in precisely this regularity setting. Every core pullback is such a $u$; the extension to $\Dom(\calE)$ is the dossier's own closure argument, checked below. A literature-scout confirmation of Theorem 4.1 of the primary remains welcome but is not needed for this verdict, since the load-bearing statement is verified in a published source. |
| Cordero-Erausquin–Klartag, *Moment measures*, JFA 268 (2015); arXiv:1304.0630 | uniqueness of the moment potential up to translation (part (g), l. 986–990) | **published** | Read Theorem 2 and Definition 2 in the arXiv text: for $\mu$ finite, not supported in a hyperplane, barycenter at the origin, the essentially-continuous convex $\psi$ with moment measure $\mu$ is unique up to translation; "any finite convex function $\psi:\R^n\to\R$ is essentially-continuous" (remark after Def. 2). The product potential is finite and convex, so the dossier's use is exact. |
| Berman–Berndtsson 2013; Fathi 2019 (Thm 2.3) | through the certified literature node `thm:regular-moment-map-compact-target` | published (node's own classification) | Not re-audited as a node. I did read Fathi arXiv:1804.04699: a Stein kernel satisfies $\int x\cdot f\,d\mu=\int\langle\tau,\nabla f\rangle_{\HS}d\mu$ "for any smooth test function $f$ taking values in $\R^d$", and the proof of Theorem 2.3 integrates by parts on the whole source space with no boundary term; the dossier's ambient test form with $F\in C_c^\infty(\R^n)$ (l. 657–666) is within that class. Independently, the identity $\int x_bF\,d\mu=\int\tau_{bj}\partial_jF\,d\mu$ follows from the dossier's own cutoff tools (source-side integration by parts of $\zeta_mF(\nabla\psi)\partial_b e^{-\psi}$, error $\le(2R/m)\|F\|_\infty$), so this step does not even depend on the exact test class of the import. |

No unreviewed preprint is load-bearing: the trace bound $\Tr\mathsf N\le2n$ is re-derived
(l. 942–962), not imported from Chen–Klartag. No run artifact is cited anywhere; the
calibration table (§9) is explicitly non-probative and I treated it as such.

### 6. The steps, line by line

Every step was re-derived. None failed.

- **Setting** (l. 68–95). $\eta$ is a probability because $(\nabla\psi)_\#\eta=\mu$ is; $R$,
  $c_V$, $c_{V''}$ finite. Correct.
- **Operator data** (l. 112–135). $L_\mu g=\Div_\mu(\tau\nabla g)=\Tr(\tau D^2g)-x\cdot\nabla g$
  from $\Div_\mu\tau=-x$; core energy $\le n\|\nabla f\|_\infty^2$ from
  $\langle\tau\xi,\xi\rangle\le(\Tr\tau)|\xi|^2$ and $\E_\mu\Tr\tau=n$; $U$ unitary. Correct.
- **(MA)/(MA1)** (l. 310–320). $\log\det H=-\psi+V\circ\nabla\psi$ is the change of variables;
  $\partial_k\log\det H=H^{ij}\psi_{ijk}$. Correct.
- **Lemma `symmetric-form`** (l. 322–343). $\partial_iH^{ij}=-H^{ia}\psi_{abi}H^{bj}$, then
  (MA1) at $k=b$; the three-term expansion of $e^{\psi}\partial_i(e^{-\psi}H^{ij}f_j)$ cancels
  the $\psi_iH^{ij}f_j$ against $\psi_bH^{bj}f_j$. Correct.
- **Lemma `pullback`** (l. 344–370). $f_{ij}=g_{ab}\psi_{ai}\psi_{bj}+g_a\psi_{aij}$,
  $H^{ij}\psi_{ai}\psi_{bj}=H_{ab}$, (MA1) on the second term, subtraction of
  $(V_i\circ\nabla\psi)g_aH_{ai}$. Correct; hence part (a).
- **Lemma `MA2`** (l. 375–401). Differentiating (MA1) in $y_\ell$ with
  $\partial_\ell H^{ij}=-H^{ia}\psi_{ab\ell}H^{bj}$; identification of
  $H^{ia}H^{bj}\psi_{ab\ell}\psi_{ijk}=\Tr(H^{-1}\partial_\ell H\,H^{-1}\partial_kH)=Q_{k\ell}$
  and $H_{ik}V_{im}H_{m\ell}=A_{k\ell}$; $c^\top Qc=\|H^{-1/2}S_cH^{-1/2}\|_{\HS}^2$. Correct.
- **Lemma `coercive`** (l. 410–424). Unbounded closed convex sublevel set contains a ray;
  the recession slope of a convex function is base-point independent, so
  $s\mapsto\psi(y+sv)$ is nonincreasing for every $y$; Fubini along $v$ gives
  $\int e^{-\psi}=\infty$. Correct.
- **Cutoffs** (l. 426–434). $\zeta_m=\chi_m(\psi)\in C_c^\infty$ by coercivity;
  $|\nabla\zeta_m|\le(2/m)|\nabla\psi|\le2R/m$. Correct.
- **Lemma `ibp`** (l. 436–456). (i) divergence theorem for the compactly supported field
  $\phi e^{-\psi}H^{-1}\nabla u$. (ii) **D2 is repaired:** the hypothesis now reads "$X'$
  vanishing on $[t,\infty)$ for some $t\in\R$" (l. 440); the field
  $e^{-\psi}H^{-1}X'(\psi)\nabla\psi$ is supported in $\{\psi\le t\}$, compact by Lemma
  `coercive`, and no lower bound is needed since $\psi\ge\min\psi$. The formula
  $\calL(X(\psi))=X''\Gamma+X'(n-\langle\nabla V\circ\nabla\psi,\nabla\psi\rangle)$ from
  $\partial_{ij}X(\psi)=X''\psi_i\psi_j+X'H_{ij}$ and (MA1)-free algebra ($H^{ij}H_{ij}=n$).
  Correct. The application in Lemma `cutoff` (l. 464) takes $X(s)=\int_0^s\chi_m$, so
  $X'=\chi_m$ vanishes on $[2m,\infty)$: the hypothesis is now met.
- **Lemma `cutoff`** (l. 457–475). $\int|\chi_m'(\psi)|\Gamma\,d\eta
  =\int\chi_m(\psi)(n-\langle\nabla V\circ\nabla\psi,\nabla\psi\rangle)d\eta\le n+c_VR$ using
  $\chi_m'\le0$; $\chi_m'^2\Gamma\le\tfrac2m|\chi_m'|\Gamma$. Correct.
- **Lemma `domination`** (l. 479–515). (i) dual-norm identity
  $\langle H^{-1}G,G\rangle=\sup_\xi(\xi\cdot G)^2/\langle H\xi,\xi\rangle$, substitution
  $\xi=H^{-1/2}\zeta$, top eigenvalue $\le$ trace of the quadratic form
  $\zeta\mapsto\|S_{H^{-1/2}\zeta}\|_{\HS}^2$, and the trace equals $\mathfrak g$. (ii)
  $\Tr(H^{-1}\Gamma)\ge\lambda_{\min}(H^{-1})\Tr\Gamma$ for PSD $\Gamma$. (iii) two
  Cauchy–Schwarz steps. All correct.
- **Lemma `D-finite`** (l. 517–556). The cutoff identity
  $\mathcal D_m+\mathcal T_m=\int\zeta_m^2\Tr H^2+\mathrm{Err}_m$ (from (i) with
  $\phi=\zeta_m^2H_{ij}$ and $-H_{ij}\calL H_{ij}=\Tr H^2-\Tr(H(A+Q))$), the bound
  $|\mathrm{Err}_m|\le2\|H\|_{\HS,\infty}\kappa_m^{1/2}\mathcal D_m^{1/2}$, the quadratic
  inequality $\mathcal D_m^{1/2}\le\eps_m/2+\sqrt{\Tr\mathsf N+\eps_m^2/4}$, monotone
  convergence along the nested dyadic sequence, $\mathrm{Err}_m\to0$, and the limit in the
  identity. Correct. This is the analytic heart and it holds.
- **Lemma `normalization`** (l. 560–583). $c^\top(A+Q)c=\calL h+h\ge0$, (i) with
  $\phi=\zeta_m$, error $\le\kappa_m^{1/2}(\int\mathfrak g)^{1/2}$ by `domination`(i),
  monotone convergence on the left, dominated on $\int\zeta_mh\to c^\top(\int H)c=1$,
  polarization, entries dominated by the trace of a PSD matrix. Correct.
- **Lemma `form-membership`** (l. 586–641). (i) $\zeta_mf$ is a core element because
  $\nabla\psi(\{\psi\le2m\})\Subset\operatorname{int}P$; $\calE^0(\zeta_mf-f)\to0$ by
  dominated convergence and $\kappa_m\to0$; the sequence is $\calE^0$-Cauchy and
  $L^2$-convergent, so closedness gives $f\in\Dom(\calE)$ with $\calE(f)=\calE^0(f)$;
  polarization on the vector space $\mathfrak B$. (ii) $\calE^0(H_{ai})\le\int\mathfrak g$,
  $\calE^0(u_b)=\int H_{bb}=1$, core pullbacks bounded with $\calE^0\le n\|\nabla g\|_\infty^2$.
  (iii) (i) with $\phi=\zeta_mf$, $u=w_i$; the three limits with the dominations
  $|\calL w_i|\le\Tr(A+Q)+2R^2\in L^1$, product of two $L^2$ functions, and
  $\|f\|_\infty\kappa_m^{1/2}\calE^0(w_i)^{1/2}$. Correct: the weak column equation holds for
  every $f\in\mathfrak B$.
- **Lemma `eigen`** (l. 644–676). Centering and orthonormality from $\E X=0$, $\Cov=I$;
  $\ell_b=x_b\chi|_{\operatorname{int}P}\in\mathscr D$; the ambient weak Stein identity gives
  $\calE^0(f,\ell_b)=\langle f,\ell_b\rangle$ on the core; form-norm continuity and density
  extend it to $\Dom(\calE)$; the representation theorem gives $\ell_b\in\Dom(\Aop)$,
  $\Aop\ell_b=\ell_b$. Consistency $\calL u_b=-u_b$ is (MA1). Correct.
- **Lemma `BL`** (l. 678–698). Applies to core pullbacks; passes to $\Dom(\calE)$ by
  form-norm approximation ($\Var$ is $L^2$-continuous); on $\mathbf 1^\perp\cap\Dom(\calE)$
  the form dominates the norm, so $\sigma(\Aop|_{\mathbf 1^\perp})\subset[1,\infty)$;
  attained at $u_b$. Correct.
- **Lemma `orthogonality`** (l. 707–721). $f=u_b$ in the weak equation against the
  form–operator pairing $\calE(u_b,w_i)=\langle\Aop u_b,w_i\rangle$. Correct.
- **Lemma `M`** (l. 722–746). $|\psi_{kib}|\le(2R^2\mathfrak g)^{1/2}\in L^2\subset L^1$;
  cutoff integration by parts of $\zeta_mH_{ki}\partial_be^{-\psi}$ with error
  $\le2R^2\cdot2R/m$; total symmetry; $(M_a)_{ib}=(\Theta_ba)_i$. Correct.
- **Resolution, part (d)** (l. 765–819). $\langle w_i,\mathbf 1\rangle=a_i$;
  $v_i\perp\mathbf 1,u_b$ by construction; Pythagoras for the first identity;
  $a^\top\mathsf Da=\sum_i\calE(w_i)$ via $\partial_bw_m=(\partial_bH)_{km}a_k$; the bilinear
  expansion with $\calE(\mathbf 1,\cdot)=0$, $\calE(u_b,u_c)=\delta_{bc}$,
  $\calE(u_b,v_i)=0$; subtraction for the third identity; $T_a\ge0$ by Lemma `BL` since each
  $v_i$ is centered; $\mathsf N-I\preceq\mathsf D$. Correct.
- **Prop. `anticommutator`** (l. 820–836). Absolute convergence
  $|\langle Ha,(A+Q)a\rangle|\le2R^2\Tr(A+Q)$; $f=w_i$ in the weak equation; symmetry. Correct.
- **C1–C5** (l. 840–890). Spectral-measure characterization of $T_a=0$ on $[1,\infty)$;
  C2 algebra and $\rho\,a^\top\mathsf Na\le1+\beta-T_a$; C3 with
  $T_a+\langle v,\Aop v\rangle=\langle v,(2\Aop-1)v\rangle\ge\|v\|^2$ and
  $\|M_a\|^2=a^\top\sum_b\Theta_b^2a$; C4; C5 basis sum and
  $\Tr\mathsf R\ge\tfrac12\Tr\mathsf N\iff\Tr\mathsf R\ge\Tr\mathsf D$. All correct.
- **Lemma `cyclic`** (l. 903–940). Eigenframe expansions
  $\Tr(HQ)=\sum\lambda_r(\lambda_p\lambda_q)^{-1}\widetilde T_{pqr}^2$ and
  $\Tr(H^{bc}\partial_bH\partial_cH)=\sum\lambda_p^{-1}\widetilde T_{pqr}^2$; symmetrized
  coefficient $[(\lambda_p-\lambda_q)^2+(\lambda_q-\lambda_r)^2+(\lambda_r-\lambda_p)^2]/(6\lambda_p\lambda_q\lambda_r)$;
  $\Tr(HA)=\Tr(H^{3/2}D^2V H^{3/2})\ge0$. Correct.
- **Part (f)** (l. 942–962). $\mathsf D\succeq0$ (Gram against $H^{-1}$);
  $\Tr\mathsf R=\int\Tr(H(A+Q))\ge\int\mathfrak g=\Tr\mathsf D$; tracing
  $\mathsf N-I\preceq\mathsf D$ gives $\Tr\mathsf N\le2n$, $\Tr\mathsf D\le n$;
  $a^\top\mathsf Da\le\Tr\mathsf D$; $\mathsf R\succeq\mathsf N-nI$; $Q_{\rm lin}\le n+1$.
  Correct.
- **Part (g)** (l. 977–1015). The product lies in the class with $P=\prod[\alpha_k,\beta_k]$,
  $D^2V=\diag(V_k'')$; the sum potential is finite, convex, satisfies (MA) and pushes
  $\otimes e^{-\psi_k}$ to $\mu$, hence is a translate of the canonical potential by CEK
  Theorem 2, and all matrices are translation-invariant; diagonalization
  $A=\diag(V_k''(\psi_k')\psi_k''^2)$, $Q=\diag(\psi_k'''^2/\psi_k''^2)$,
  $H^{bc}\partial_bH\partial_cH=\diag(\psi_k'''^2/\psi_k'')$; exact identity
  $HQ=\psi_k'''^2/\psi_k''$; $(\mathsf R-\mathsf D)_{kk}=\int V_k''(\psi_k')\psi_k''^3e^{-\psi_k}\ge0$.
  Correct. `rem:sol-clsr-product-strong` (one-dimensional (MA1) bounds
  $\psi'''/\psi''$) is correct.
- **§9 calibrations and §10 audit trail** are remarks; I spot-checked the one-sided exponential
  row ($\tau=x+1$, $\mathsf N=2$, $\|M_a\|^2=1$, $\|v\|^2=0$) and it is consistent. No proof
  weight.

### 7. The three repaired items

1. **D1 (route (b)).** Manuscript, ledger `summary`, and `thm:sol-clsr-main`(c),(d) now state
   the weak column equation with the same test class and the same $L^1$ integrability, and
   name $\langle v,\Aop v\rangle$ as the closed-form value; the dossier proves exactly that
   (Lemma `form-membership`(iii)). Verified clause by clause in §1.
2. **D2.** Lemma `ibp`(ii) hypothesis at l. 440 is "$X'$ vanishing on $[t,\infty)$ for some
   $t\in\R$"; the proof (l. 450–455) uses the compact sublevel set $\{\psi\le t\}$; the
   application at l. 464 ($X'=\chi_m$, vanishing on $[2m,\infty)$) satisfies it.
3. **D3.** `rem:sol-clsr-klartag-import` (l. 99–110) quotes Theorem 1.1 as
   $\Delta\psi\le2R(P)^2$ under conditions (1), matches them to `def:sol-clsr-class`, and
   deduces $H\preceq(\Tr H)I\preceq2R(P)^2I$ from $H\succ0$. Verified against the arXiv text.

Also verified: the header (l. 18–20) carries both author identities and the date 2026-09-06;
the audit-trail item (5) (l. 1101–1105) records `prop:cmh-bochner` as unused with the proposed
drop; no mathematical step changed relative to the audited copy except the D2 hypothesis
wording and the D3 citation wording, both re-checked above.

## Corrections

None required for certification. Two orchestrator-side wording sharpenings, not defects:

- Name $A$ and $Q$ in `modules/kls/41-cmh-normalization.tex` before the lemma as the two terms
  of `eq:differentiated-MA` (see §1).
- Optionally write the decomposition as $Ha=a+\sum_b(M_a)_{\cdot b}u_b+v$ so that
  $\|M_a\|$ visibly refers to the matrix $(M_a)_{ib}$.

## Exclusions

Not certified by this report: any statement about $(\mathrm{AB})_{\rho,\beta}$ with universal
constants; any bound on $\CMH$; `conj:gate-zero` and `conj:gate-zero-sharp`; the strong column
equation $(1-\Aop)(Ha)=(A+Q)a$ on the general compact-target class (open, equivalent to
$\Tr Q\in L^2(\eta)$, proved only on products); the probe's P4 (deficit kernel) and P5
(corrector hierarchy) named in `rem:sol-clsr-noncertified`; the calibration values of §9 for
boundary laws outside the class; the uncommitted nodes `lem:linear-sector-third-moment`,
`cor:gate-zero-third-moment`, `prop:cone-moment-map`, `prop:cone-linear-sector`,
`cor:cube-cone-gate-zero` and their dossiers; the literature nodes
`thm:regular-moment-map-compact-target` and `thm:chen-klartag-moment-hessian` (not re-audited);
and a `sync`-lens audit of the wider module.

## Proposed ledger delta (orchestrator applies)

For `research/program/ledger.yaml` node `lem:cmh-linear-spectral-resolution`:

```yaml
    status: proved
    depends_on: ['thm:regular-moment-map-compact-target', 'def:cmh']
    proofs:
      - artifact: solutions/lem-cmh-linear-spectral-resolution.tex
        mode: agent
        review: research/reviews/2026-09-06-lem-cmh-linear-spectral-resolution-proof-review.md
```

`prop:cmh-bochner` is dropped from `depends_on` because the proof does not use it
(constraint 8). `assumes` stays empty; `implies` and `refuted_by` are unchanged. The manuscript
sentence "The following candidate statement is staged in a standalone dossier pending
independent review; its ledger status is \emph{open}" (module l. 272–273) will need the
orchestrator's matching edit once the status changes; that is a `manuscript`-key edit and is
not proposed here beyond noting it.
