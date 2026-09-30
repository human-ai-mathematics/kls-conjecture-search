---
verdict: pass
authors:
  - prover-w4p01
reviewer: proof-checker-w4r01
fingerprints:
  solutions/prop-split-screened-supply.md: c9aa1a2a9298eb01d649225f5613f4411284015d09de3438403c92983f723fe4
  prop:split-screened-supply: 2978c26605b7f1f0d555277fa000ad70a7d8ac1b45813c18547fe73d3a519684
  prop:stein-rep: 809545792ca08860114a8276ff5b61febda2930cfd2b8b0f3a1a5ca1a0d00e6a
  lem:stein-vs-source: 6bd84bc399d194fcb26d5a831feb198bcda29c1beaa21a9d1ebe64320eca30b5
  lem:block: 8a8c2e99fae755f4beed8f10c667b71bc1b5067bbf1fbe5ca6cfaed191e1555e
  cor:per-direction: 41aeb34aa0f748e931a100d435bb6cbba97772f149ce25c2e089fc77974c1e43
  thm:scalar-riccati: 83fdb94d00721fdfab219b0a417b1ac815c170925d051a187929c3635241286d
  lem:lyapunov-stein-duality: 053e29d7fe7f570d943da7b4c27630eed5d4519a07957ef9b8374692fd518213
  prop:products: 85b9ec9b7b81c783e52dce9f3edce41396f581da4f7a425bd3df9031860a6c8c
  lem:perimeter-martingale: c0e1c3539694fe07c6ebe7c767bafeeadef66ac4778e02f7d217b6c9d3ad3daa
---

# Split-class screened weighted supply — independent proof review

Cold review of `solutions/prop-split-screened-supply.tex` (reviewed SHA-256
`c3d36e34b6bb217d20a25528d31595cd6c07db66d186290d4805f987c01a3909`), reconstructed from
repository artifacts only: the dossier, `research/kls/ledger.yaml`,
`modules/kls/27-eldan-open-targets.tex`, the certified dependency dossiers
(`solutions/kls-qcts-stein-boundary-core.tex`, `solutions/kls-product-covariance.tex`,
`solutions/kls-localization-riccati-core.tex`, `solutions/kls-excess-audit.tex`,
`solutions/kls-geometry-models.tex`, `solutions/lem-lyapunov-stein-duality.tex`), their
persisted reviews, and the probe record
`research/explorations/2026-08-30-kls-route-prober-weighted-screened-interface-w4w01.md`.
The prover's session and narrative were not consulted as evidence. Author `prover-w4p01`
and reviewer `proof-checker-w4r01` are distinct.

**Scope of this certification.** This review certifies the theorem the dossier actually
states and proves: the screened weighted supply in *total-budget* form on the
**compact-smooth product-preserving regular split class (convention (M2))**, together with
the clearly separated auxiliary Lemma `lem:sol-constant-supply-consumption` (a conditional
implication with explicit hypotheses, attached to no ledger node). It does **not** certify
the general (non-regular) split-class statement; see Findings 1 and the Exclusions.

## Findings

### 1. Statement agreement (with one scope caveat the orchestrator must resolve)

The dossier theorem `thm:sol-split-screened-supply`, the ledger `statement:` of
`prop:split-screened-supply` (`research/kls/ledger.yaml`, node at line 826), and the
manuscript statement at `\label{prop:split-screened-supply}`
(`modules/kls/27-eldan-open-targets.tex:120`–`133`) agree verbatim in the inequality, the
quantifier order (for every admissible $(\mu,E,J,k)$, every $\eta\in(0,1/4]$, every
$\kappa>0$, every $T>0$), the constant $(2k+64\eta^2(1+k))/\kappa$, the screened set
$\{Q_t\ge\kappa e_tW_{\rm cut}\}$ with $Q_t=s_t\|K_t\|_{\rm HS}^2$ and
$W_{\rm cut}=(1+\lambda_{\rm cut}(A_t,K_t))^{5/2}$ under the certified
$\lambda_{\rm cut}(A,0)=0$ convention, the uniformity in $T$, the ambient dimension, and
the spectators, and the explicit total-budget (not $C(k)T$) shape.

**Caveat.** The dossier theorem carries the restriction "in the regular split class (M2)"
(compactly supported smooth isotropic one-dimensional factors; $E_J$ with $C^2$ relative
boundary, tubular neighborhood over the support, $P_0(E)<\infty$). Neither the current
ledger statement nor the manuscript proposition carries that restriction. The dossier is
internally honest about this ("restricted per convention (M2)", and
`rem:sol-general-class` flags the general-class gap), but as currently worded the ledger
and manuscript claim strictly more than this dossier proves. The general-class version is
confined by `rem:sol-general-class` to a defined-on-approximants convention, with the
screened-indicator limit interchange explicitly open (the indicator
$\one_{\mathcal A_{\kappa,t}}$ does not converge monotonically along the certified
approximation scheme, so Fatou does not transfer the bound to rough limiting data). This
matches Section 5(5) of the w4w01 probe exactly. Consequently: **this certification may be
wired to the node only together with a statement amendment** (ledger and manuscript in the
same edit) adding the regular-class restriction and the approximant remark. Without that
amendment the node must stay `open` and this review must not be used as its active
certification. The exact proposed text is in the reviewer's handoff, mirrored below.

The dossier header's parenthetical "no manuscript `\label` yet" is stale (the label now
exists at `modules/kls/27-eldan-open-targets.tex:121`); provenance shows the label was
added after the dossier was authored. Non-blocking; fix at wiring time.

### 2. Step-by-step verification of the main proof

Preliminaries checked: product persistence and diagonal $A_t$ are `prop:products`(i)
(certified, `solutions/kls-geometry-models.tex:336`–`353`); $0<p_t<1$ at all finite times
from $0<p_0<1$ and strict positivity of the finite-time likelihood matches the certified
Riccati-core setup; $\tau_\eta$ is a stopping time for the augmented right-continuous
filtration because $p$ has continuous paths; the $|p_0-1/2|>\eta$ edge case gives
$\tau_\eta=0$ and a trivially true statement; all interchanges are Tonelli for nonnegative
progressively measurable integrands (conventions (M3)–(M4)), needing no a priori
integrability.

- **Step 1 (pathwise domination).** $e_t\ge0$ uses only that $E$ itself, with
  $\mu_t$-mass $p_t$ and perimeter $P_t(E)$, is a competitor in the infimum defining
  $I_{\mu_t}(p_t)$ — the upper-bound direction of the profile only. On
  $\mathcal A_{\kappa,t}$ the defining inequality divided by $\kappa>0$ gives
  $e_tW_{\rm cut}\le Q_t/\kappa$; off the set the left side vanishes and $Q_t\ge0$. The
  $K_t=0$ degenerate state is handled exactly by the certified conventions of
  `lem:lyapunov-stein-duality` ($\lambda_{\rm cut}(A,0)=0$, $W_{\rm cut}=1$; membership
  forces $e_t=0$, both sides vanish). Verified with no case gap.
- **Step 2 (conversion).** On $\{t<\tau_\eta\}$, $|p_t-1/2|\le\eta\le1/4$ gives
  $s_t\ge1/4-\eta^2\ge3/16>1/8$. The second inequality of the certified
  `lem:stein-vs-source` (`solutions/kls-qcts-stein-boundary-core.tex:183`–`205`; I
  re-derived it: $K=G+(q-p)\delta\delta^T$, $s\|K\|^2\le2S+2(q-p)^2r^2/s\le
  2S+64\eta^2r^2\le2S+64\eta^2D$ using $|q-p|\le2\eta$, $1/s<8$, $r^2\le D$) applies with
  identical notation ($D=2s\delta^TA\delta-r^2$). The identification
  $Q_t=\calS_{\mu_t}(E)/s_t$ is the certified `prop:stein-rep`
  ($\calS_\nu(E)=s^2\|K\|_{\rm HS}^2$; finite fourth moments hold at $t=0$ by compact
  support and at $t>0$ by the Gaussian factor). The endpoint $t=\tau_\eta$ is
  Lebesgue-null in the time integral. Verified.
- **Step 3 (source budget under $0<p_0<1$ only).** The inline reproduction of
  `thm:budget`(i) is verified line by line against primitives, independently of the
  packaged theorem: `lem:block` (certified with the finite-second-moment and
  $0<\nu(E)<1$ hypotheses, both satisfied by $(\mu_t,E)$ pathwise) gives $G_t$ supported
  on $J\times J$, so $S_t=\sum_{i\in J}s_t|G_te_i|^2$; the unconditional
  `cor:per-direction` gives $\E\int_0^Ts_t|G_te_i|^2\,dt\le(R_0)_{ii}$ for every $T$;
  $R_0=A_0-B_0\preceq A_0=I_n$ by isotropy, so $(R_0)_{ii}\le1$; summing over $J$ and
  monotone convergence in $T$ give $\E\int_0^\infty S_t\,dt\le k$. The certified product
  dossier's dependency-audit paragraph (`solutions/kls-product-covariance.tex:296`–`298`)
  independently records that part (i) needs only $0<p_0<1$; my check does not rely on
  that paragraph but confirms it. The coarse balance window $p_0\in[2/5,3/5]$ is nowhere
  used. Verified.
- **Step 4 (dissipation budget).** `thm:scalar-riccati` gives
  $dr=dM+(S-D)\,dt$ with $D\ge r^2\ge0$. In the regular class the localizing bounded
  stopping times $(\sigma_m)$ with true stopped martingales and integrable stopped
  coefficients are exactly those of the certified Riccati and product dossiers; optional
  stopping at the bounded time $T\wedge\tau_\eta\wedge\sigma_m$ is legitimate, the
  identity rearranges because all stopped terms are finite, $\E r\ge0$ is discarded, the
  $S$-integral is enlarged to $[0,\infty)$ (nonnegative), and monotone convergence in $m$
  (with $\sigma_m\uparrow\infty$, $D\ge0$) yields
  $\E\int_0^{T\wedge\tau_\eta}D_t\,dt\le r_0+k$. $r_0\le1$: $B_0=s_0\delta_0\delta_0^T$
  has rank $\le1$ and $B_0\preceq A_0=I_n$, so its trace is its only nonzero eigenvalue.
  Verified.
- **Step 5 (combination).** $\E\int Q\le 2k+64\eta^2(1+k)$; divide by $\kappa$. Constant
  arithmetic re-checked; every ingredient is independent of $T$, $n$, and the spectators.
  Verified.

### 3. Auxiliary Lemma `lem:sol-constant-supply-consumption`

Verified in full as a self-contained conditional implication; it covers no ledger node.
It is the certified `cor:tight-window-consumption` proof
(`solutions/kls-localization-riccati-core.tex`, Section 4) with the single Gronwall input
changed from $1+C_0T$ to $1+c+C_0T$. Checks: $u(T)=\E r_{T\wedge\tau_\eta}$ bounded and
measurable in the regular class; Fatou/monotone-convergence removal of the localizing
times; insertion of the constant-supply Carleson hypothesis; the discard of
$(\alpha-1)\E\int D\le0$ is exactly where $\alpha<1$ and the *explicit* a priori
finiteness hypothesis (automatic in the regular class: $D$ is bounded on bounded
intervals by the support diameter) are used; Gronwall with nondecreasing inhomogeneity
gives $u(T)\le(1+c+C_0T)e^{C_1T}\le C_*=(1+c+C_0T_0)e^{C_1T_0}$; for $\eta\le1/6$,
$s\ge2/9$ gives $|\delta|^2\le\tfrac92r$; Doob $L^2$ on the bounded stopped mass
martingale with $s\le1/4$ gives $\Prob(\tau_\eta\le T)\le9C_*T/(8\eta^2)$
(recomputed: $\tfrac{4}{\eta^2}\cdot\tfrac1{16}\cdot\tfrac92C_*T$); the stated
$T_*\le\min(T_0,\,4\eta^2/(9C_*))$ makes this $\le1/2$; on survival
$\min(p_{T_*},q_{T_*})\ge1/2-\eta\ge1/3$; the boundary consequence is the certified
`lem:survival-implies-kls` with $(T_*,1/2,1/3)$. The constants match the review target
exactly. The lemma claims no screened trace companion and draws no KLS conclusion from
the main theorem (`rem:sol-no-companion`), and the main proposition does not use the
lemma. Verified.

### 4. Measurability conventions (M1)–(M4)

(M1)–(M4) match Section 5, items 1–4, of the w4w01 probe record, and item 5 is carried by
`rem:sol-general-class`. (M3)'s realization of $P_t$ as the increasing limit
$Y_{n,t}\uparrow P_t(E)$ of infima over the fixed countable rational boundary-layer
family of bounded continuous mass martingales is exactly the certified construction in
`solutions/kls-excess-audit.tex` (Lemma `lem:perimeter-martingale`,
`eq:sol-boundary-layer-limit`); countable infima and monotone limits of continuous
adapted processes are progressively measurable. The joint measurability of
$I_{\mu_t}(p_t)$ via a fixed countable regular competitor family is adopted as a
*measurability convention only*, consistent with the certified `lem:excess-identity`
practice; no supermartingale or martingale property of the moving profile infimum is
asserted, preserving the `lem:inf-martingales` caveat
(`solutions/kls-excess-audit.tex:272`–`316`). (M4)'s Borel property of
$(A,K)\mapsto\lambda_{\rm cut}$ on supported pairs via fixed-rank strata and the
eigenbasis Moore–Penrose formula `eq:sol-lyapunov-pseudoinverse` is sound (the
pseudo-inverse is continuous on each fixed-rank stratum; the $K=0$ convention is a Borel
patch). The weight and the screened indicator appear **only** inside nonnegative
Lebesgue-time integrals handled by Tonelli; I confirmed no Itô differential is taken of
$W_{\rm cut}$, of the indicator, or of any function of $\lambda_{\rm cut}$ anywhere in
the dossier.

### 5. Dependency closure and citation debt

Every dependency is `status: proved` with an active agent certification in
`research/kls/ledger.yaml`:

| input | use | solution / review |
|---|---|---|
| `prop:stein-rep` | $Q_t=\calS_{\mu_t}(E)/s_t$ | `kls-qcts-stein-boundary-core.tex` / 2026-08-25-kls-core-r2-audit.md |
| `lem:stein-vs-source` | Step 2 conversion | same |
| `prop:two-tail` | fence calibration only (via Lyapunov dossier remark) | same |
| `lem:block` | Step 3 support | `kls-product-covariance.tex` / 2026-08-27-kls-product-covariance-proof-review.md |
| `cor:per-direction` | Step 3 per-direction budget | `kls-localization-riccati-core.tex` / 2026-08-25-kls-core-r2-audit.md |
| `thm:scalar-riccati` | Step 4; $D\ge r^2$ | same |
| `lem:survival-implies-kls` | auxiliary lemma only | same |
| `lem:lyapunov-stein-duality` | $\lambda_{\rm cut}$ definition, $K=0$ convention, pseudoinverse formula, harmonic-mean and two-tail calibrations | `lem-lyapunov-stein-duality.tex` / 2026-08-27-lem-lyapunov-stein-duality-repair-proof-review.md |
| `prop:products` | product persistence, diagonal $A_t$ | `kls-geometry-models.tex` / 2026-08-27-kls-geometry-models-repair-proof-review.md |
| `lem:perimeter-martingale` | (M3) measurable realization of $P_t$ | `kls-excess-audit.tex` / 2026-08-27-kls-excess-repair-w0r2-proof-review.md |

No `conditional` or `preprint-unreviewed` input enters: the conditional Letwin QCTS
window and the Klartag–Lehec import (`thm:KL-window`, `cor:KI-discharged`) are outside
this dossier's dependency cone. The dossier itself cites no external literature directly;
all published inputs (Brascamp–Lieb, Bobkov, Doob, Gronwall, Carbery–Wright) enter only
through the already-certified dependency dossiers, so no new citation debt arises.

Provenance note (out of my write scope, recorded for the orchestrator): the passing
review of `solutions/kls-product-covariance.tex` declares reviewed SHA-256
`2173a912…350e`, while the committed bytes hash to `79b6a07e…ebec` (both entered the
repository in commit `cd4a894`); the dossier also retains a stale scope sentence "The
current bytes are an unreviewed repair". The discrepancy is consistent with post-review
header wiring. It does not affect this review — I re-verified every product-dossier fact
used here (Lemma `lem:block`, `cor:per-direction` consumption pattern, and the part-(i)
argument) directly against the current bytes — but the janitor may want to reconcile it.

### 6. Fences

- **`rem:two-tail-slice-bounds`.** The theorem is a time-integrated expectation bound, not a
  slice-wise absolute-scale Stein estimate; it retains the calibrated weight power $5/2$
  (two-tail calibration $\lambda_{\rm cut}(A_\Lambda,K_\Lambda)=\Lambda$, certified
  `eq:sol-cut-two-tail`); the two-tail initial laws $N(0,\diag(\Lambda,1,\dots,1))$,
  $\Lambda>1$, are outside the isotropic-factor hypothesis class; dynamically reached
  two-tail-type states remain chargeable and are paid through $Q_t/\kappa$. Respected.
- **`rem:profile-circularity`.** The only profile information used anywhere is the upper-bound
  direction $I_{\mu_t}(p_t)\le P_t(E)$ (Step 1, $e_t\ge0$); no lower bound on the moving
  profile enters, and the fenced excess-identity refinement is not used. Respected.

### 7. Repository constraint 6

The dossier proves a supply estimate on the `conj:weighted-excess-rate` screened-interface gate. Its
Scope paragraph and `rem:sol-shape` explicitly assert nothing about `conj:trace-upgrade`, the
high-rank part of `conj:stein-weighted`, or `conj:product-alignment`, and I confirmed no occupation
estimate, equivalence, or comparison across that cluster is proved or implied by any
step. The disclaimer is present and respected.

### 8. Hypothesis accounting

Used: product structure with isotropic (mean-zero, variance-one) one-dimensional
log-concave factors; regular class (M2) (measurability, localizing times, finiteness);
$J$-measurability of $E$ (Step 3 support); $0<p_0<1$ (definedness of two-color
quantities); $\eta\le1/4$ (conversion window); $\kappa>0$; $T>0$. Used but stated only
inside (M2): $P_0(E)<\infty$, $C^2$ relative boundary. Stated but not needed by the main
proof (sharpening opportunities, not defects): the full perimeter-martingale *identity*
of the regular class — the main theorem needs only progressive measurability of $e_t$ and
$e_t\ge0$; and no balance hypothesis on $p_0$ is needed, as correctly advertised. The
auxiliary lemma uses each of its stated hypotheses ($\eta\le1/6$, $|p_0-1/2|\le\eta/2$,
$\alpha<1$, a priori finiteness, $c,C_0,C_1\ge0$, $T_0$).

### 9. Build

`cd solutions && latexmk -gg -pdf -outdir=../build prop-split-screened-supply.tex`
succeeds (exit 0, 6 pages); unresolved cross-module `\ref`/`\cite` display as `??`/`[?]`
standalone, as expected for a `subfiles` dossier.

### 10. Dependency-edge comparison (flag for the orchestrator, not a defect)

The ledger node's current `depends_on`
`[lem:stein-vs-source, thm:budget, lem:block, thm:scalar-riccati,
lem:lyapunov-stein-duality, prop:trivial-excess]` does **not** match the actual proof:
`prop:trivial-excess` is used nowhere in the dossier, and `thm:budget` is not invoked as
a statement (its packaged balance hypothesis $p_0\in[2/5,3/5]$ is unavailable here; the
dossier instead reproduces part (i) from primitives). The edge set matching the actual
proof is the dossier header's:
`[prop:stein-rep, lem:stein-vs-source, lem:block, cor:per-direction, thm:scalar-riccati,
lem:lyapunov-stein-duality, prop:products]`, plus `lem:perimeter-martingale` for the
(M3) measurability construction, with `lem:survival-implies-kls` consumed by the
auxiliary lemma only.

## Corrections

None required to the mathematics; no step was repaired. Two non-blocking editorial items
to fix at wiring time (header comments only, no proof content): the stale
"no manuscript `\label` yet" parenthetical, and the empty `reviewer:`/`review:` header
fields, which should point to this report when the orchestrator wires the node.

## Exclusions

Not certified by this review:

- The **general (non-regular) split-class statement**, including the current unrestricted
  wording of the ledger node and manuscript proposition; the defined-on-approximants
  convention and the open screened-indicator limit interchange of
  `rem:sol-general-class` are recorded, not proved.
- Any fixed-time expected-source estimate or $C(k)\,T$-form upgrade (explicitly open).
- The screened trace companion ((C)/(22) of the probe record), the general aligned
  initial-layer occupation candidate, and any KLS-type conclusion.
- Anything in the trace-upgrade cluster (`conj:trace-upgrade`, high-rank `conj:stein-weighted`,
  `conj:product-alignment`).
- The interpretive `rem:sol-harmonic-mean` (checked for plausibility against the
  certified harmonic-mean identity, but it is used nowhere and carries no claim weight).
- The status or content of any dependency dossier beyond the specific statements
  consumed here; the SHA discrepancy noted in Findings 5 is flagged, not adjudicated.
