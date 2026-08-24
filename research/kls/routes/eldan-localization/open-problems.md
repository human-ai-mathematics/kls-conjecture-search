# Eldan fixed-cut route — open problems (P1–P7)

Within this route, the seven targets form **one interlinked fixed-cut program**, so they are kept
together here (with the cross-references that bind them) rather than split into one file each.
They are one route within the broader KLS strategy map. Ported from the
standalone KLS program's roadmap; references re-synced to the unified `modules/kls/`.

Each entry is a **self-contained brief**:
- **Statement** — the precise target (`\ref` label + ledger id).
- **Unlocks** — what it implies (from [`../../ledger.yaml`](../../ledger.yaml)).
- **Bounded by** — obstructions any proof must respect
  ([`../../obstructions.md`](../../obstructions.md)).
- **Attack** — the suggested mechanism / available tools.
- **Prior work** — what has been tried; entry point.

Cross-check every claimed result against `research/kls/obstructions.md`, update the central
`research/kls/ledger.yaml` through the orchestrator, and run
`python3 research/check_ledger.py`.

---

## P1 · `q:upgrade` — operator-to-trace upgrade (Eldan-A headline)

**Statement** (`q:upgrade`, `modules/kls/14-open-targets.tex`; target `ass:all-cut-carleson`).
Upgrade the unconditional per-direction Carleson estimate `cor:per-direction`
($E\int s_t|G_t\theta|^2\,dt \le \theta^\top R_0\theta \le 1$, every fixed $\theta$) to the
**trace** scale uniformly over balanced cuts:
$E\int_{I\cap[0,\tau]} s_t\|G_t\|^2_{\mathrm{HS}}\,dt \le C_0|I| + C_1 E\int r_t + \alpha E\int D_t$,
$\alpha<1$. Equivalently, the source $s_t G_t^2$ must not occupy many almost-orthogonal
directions for a non-negligible set of early balanced times (noncommutative Carleson).

**Unlocks.** `ass:all-cut-carleson` ⇒ `thm:intro-all-cut` ⇒ **KLS directly**.

**Bounded by.** `obs:proj-ceiling` (projection/radial info alone caps at $\log n$; Letwin's
moment-map proof bypasses this for intrinsic QCTS, but the dynamic upgrade still needs
cut-specific structure $G_t, K_t, D_t$ and covariance occupation);
`obs:two-tail` (the inflated-posterior configuration must be shown rare, not controlled
pointwise).

**Attack.** The difficulty is purely small-time (`cor:away-from-zero`: for $t\ge t_0$,
$S_t \le 8/t^2 + D_t/2$ pathwise). Needs a probabilistic small-time non-alignment estimate
between the whitened color Hessian $H_t = A_t^{-1/2} G_t A_t^{-1/2}$ and the large spectral
windows of $A_t$ (the Euclidean source is $S_t = s_t\operatorname{Tr}(A_t H_t A_t H_t)$).

**Prior work / entry point.** Start with `prog:product-test` (P7): on products the
per-direction estimate becomes a per-coordinate **budget** (`thm:budget`) and the whole
question reduces to `q:alignment` (P6). The designated tail-union model is now implemented by
`finum run --target kls-align`; the generic `kls-loc` target remains an engine diagnostic.

---

## P2 · `q:weighted` — weighted excess propagation with rate (Eldan-B input i-w)

**Statement** (`q:weighted`; target `ass:weighted-package`). For balanced near-Cheeger $E$
($e_0(E)\le1$) and $T\le T_0$:
$E\int_0^{T\wedge\tau_\eta} e_t(E)\,(1+\|A_t\|_{\mathrm{op}})^{5/2}\,dt \le C(T e_0(E) + T^{1+\gamma})$.

**Unlocks.** Half of `ass:weighted-package`.

**Bounded by.** `obs:two-tail` calibrates the covariance power $(1+\|A\|)^{5/2}$, but not the
time rate $T^{1+\gamma}$; a weaker absolute-scale form is inert (`prop:intro-audit`) and
unprovable slice-wise. `obs:circularity` is a warning that inserting a localized profile lower
bound may restate KLS, not a theorem forbidding every direct approach.

**Attack.** The **unweighted** analogue is already resolved by the bootstrap
(`thm:bootstrap`, near-worst measures, all balanced cuts). The weighted version additionally
needs **second-moment control of the perimeter martingale against the covariance weight** —
control of $E\int e_t (1+\|A_t\|)^{5/2}$ rather than $E\int e_t$. The perimeter is a
martingale (`lem:perimeter-martingale`); the missing piece is its joint interaction with rare
covariance-inflation excursions. If the BL cap saturated deterministically, a pointwise
$E e_t\lesssim t^{5/2+\gamma}$ would be sufficient; the former $t^{3/2}$ heuristic was
dimensionally incorrect (`rem:weight-explains-rate`).

**Prior work / entry point.** `thm:bootstrap` + interface evaluation (`cor:loglog`). Connects
to `q:taming` (P4).

---

## P3 · `q:stein-weighted` — weighted stable Stein trace (Eldan-B input ii-w)

**Statement** (`q:stein-weighted`; target `ass:weighted-package`). Prove the weighted stable
Stein-trace estimate for balanced near-Cheeger cuts, damping $\beta<\tfrac12$, with the excess
term in the $(1+\|A_t\|)^{5/2}$-weighted form.

**Unlocks.** The other half of `ass:weighted-package` ⇒ (with P2) `thm:intro-weighted` ⇒ **KLS**.

**Bounded by.** `obs:two-tail` (no slice-wise shortcut).

**Attack.** The intrinsic quadratic-chaos input is now dimension-free, conditional on Letwin
v1 (`thm:letwin-qcts`). Before Reilly/Jacobi can use it, prove the foundational
`rem:almost-stability-gap`: the localized fixed near-Cheeger cut is not automatically a stable
critical minimizer; the index form has tangential Jacobi zero modes; and the global Poisson
solution leaves mixed Reilly boundary terms. A quantitative trace/almost-stability theorem,
uniform under tilt and modulo this kernel, is the next lemma. Constant-mode splitting is
downstream of that bridge, not yet the sole residual.

**Prior work / entry point.** The Stein-norm ↔ Riccati source conversion is lossless on the
fixed tight window (`lem:stein-vs-source`), provided the package includes
$2\beta+64\eta^2<1$. Then address `rem:almost-stability-gap`, followed by `q:splitting` (P5).

---

## P4 · `q:taming` — extremality tames the covariance process

**Statement** (`q:taming`). For every $\kappa\in(0,1]$, do there exist $\varepsilon>0$ and
$T_0\in(0,1/8)$ such that
every isotropic log-concave $\mu$ with $h_\mu \le (1+\varepsilon)h^*_n$ satisfies
$h_\mu(T_0^{4/3}+\Xi_{T_0}(\mu)) \le \kappa T_0$? Here
$\Xi_T = \int_0^T E(\lambda_{\max}(A_t)-1)_+\,dt$.

**Unlocks.** Absolute-scale supply $T_0e_0+C\kappa T_0$ for near-worst measures (via
`thm:bootstrap`), and
therefore the matched-time completion described in `cor:dichotomy`.

**Bounded by.** `obs:relative-ceiling` — the stronger, unweighted all-measure condition
$\Xi_{T_0}\le\kappa T_0$ at a sufficiently small universal time is already sufficient for KLS.
The $h_\mu$-weighted near-worst statement above is distinct and genuinely weaker. No converse
equivalence is proved.

**Attack.** Couple the **splitting analysis** (`modules/kls/13-jacobi-splitting.tex`) to the
**covariance SDE** (`eq:cov-sde`): covariance inflation is driven by third-moment anisotropy,
while near-worst measures are conjecturally approximately split along their dangerous
directions (where variance processes are one-dimensional and tame, `prop:products`(ii)). This
coupling has **not been attempted**; note the type mismatch in `rem:taming-type-mismatch`.

**Prior work / entry point.** The required inequality follows in the small-$h_n^*$ dimension
regime whenever $h^*_n \le c\kappa T_0/(1+\log\log n)$ (`cor:loglog`, with `hyp:KI`
discharged by the published `cor:KI-discharged`); the
unresolved regime has $h^*_n$ larger than this scale. Converting that dichotomy into a theorem
also needs the separate `hyp:absolute-geometric-completion`; see `cor:dichotomy`.

---

## P5 · `q:splitting` — quantitative splitting / boundary Obata

**Statement** (`q:splitting`). For a near-worst measure and a near-minimal balanced cut, small
constant-mode curvature $\mathfrak K_\Sigma$ forces quantitative proximity, along the normal
direction, to the split structure of `prop:exact-splitting`, with constants stable under the
localization tilt (`prop:persistent-splitting`).

**Unlocks.** The constant-mode part of `q:stein-weighted` (P3).

**Attack.** Only a sufficient flat model is proved: a global cylinder with a globally
Hessian-flat direction splits, and an already split log-affine factor has a flat orthogonal
halfspace (`prop:exact-splitting`). The converse $\mathfrak K_\Sigma=0\Rightarrow$ global
splitting is unproved and false without additional hypotheses (boundary-local flatness alone is
insufficient). First formulate and prove a valid rigidity theorem, then its stability version.
`cor:generic-degeneracy` gives small curvature at many balanced volumes under a smooth-minimizer
grant, but does not transfer that fact to the selected cut followed under localization; that
transfer is an additional open step.

---

## P6 · `q:alignment` — adapted alignment problem for products (Eldan-A residue)

**Statement** (`q:alignment`, `modules/kls/09-product-stress.tex`). For $\mu$ a product of $n$
isotropic two-sided exponentials: does there exist universal $T_0,C_0,C_1,\alpha<1$ such that
for every $n$ and every balanced cut $E$,
$$
E\int_{I\cap[0,\tau]} S_t^H\,dt
\le C_0|I| + C_1 E\int r_t + \alpha E\int D_t,
$$
where, for the high-variance coordinate projection $P_t^H$ and $P_t^L=I-P_t^H$,
$S_t^H=s_t(\|P_t^HG_tP_t^H\|_{HS}^2+2\|P_t^LG_tP_t^H\|_{HS}^2)$ counts every matrix entry
incident to a high coordinate. The obstruction-side negation asks whether a **fixed** cut can
spend $\Omega(1)$-fractions of unboundedly many per-coordinate budgets inside a common short
window, while staying balanced and underdamped.

**Unlocks.** `prog:product-test` decided positively ⇒ strong evidence for / a model of
`q:upgrade`. A negative answer (an explicit aligning cut) **refutes** `ass:all-cut-carleson`
and redirects attention to Eldan-B.

**Bounded by.** `obs:rank-one-refuted` — single-coordinate cuts cannot do it (budget $\le1$,
spikes self-extinguish); the residue is genuinely high-complexity cuts.

**Attack.** **Designated test family** (`rem:test-family`): the balanced tail union
$E_n=\{\max_i|x_i|\ge a_n\}$. It is permutation-symmetric, high-complexity, and
coordinate-selective; its complement is a product of truncated one-dimensional factors. Measure
the incident-high source $S_t^H$, together with $r,D$, balance survival, uncertainty, and
interval sweeps past the conditional $c/\log n$ window. The existing energy
shell is radial and uninformative.

**Executed diagnostic.** `finum run --target kls-align` now computes these observables with exact
tilted-Laplace moments, a filtering-path simulation, paired-grid gates, and discovery/held-out
interval scans. The 2026-08-20 run through $n=1024$ found a visible simultaneous-alignment pulse
but no sampled divergence of the required constant. This is a one-family, 16-held-out-path,
dirty-worktree diagnostic with node-only stopping, so it neither supports nor refutes the
universal node. The finite-dimensional identities and the local fixed-time boundary-Poisson
limit are proved; boundedness of the full stopped observable is conjectural. See the
[`cycle-1 synthesis`](../../../explorations/2026-08-20-kls-program-cycle-1.md),
[`asymptotic analysis`](../../../explorations/2026-08-20-kls-tail-union-asymptotics.md), and
[`final diagnostic`](../../../runs/2026-08-20-kls-align-high-n-final.jsonl).

---

## P7 · `prog:product-test` — execute/extend the product stress test

**Status.** Largely **executed** in `modules/kls/09-product-stress.tex`: coordinate budgets
(`thm:budget`), rank-one refutation (`cor:refutation`), covariance reduction (`cor:V2-implies`),
dimension-dependent covariance-window discharge (`thm:V2-window`, `cor:KI-discharged`). The
published fallback reaches $c/\log^2n$; conditional on Letwin v1 the fixed-time moment window
reaches $c/\log n$. The remaining open part is
exactly `q:alignment` (P6). The covariance-only route is heuristically expected to fail on
universal windows (`heur:V2-fails`) — so any proof must be cut-aware.

**Highest-value next step.** Prove, or refute, a stopped uniform envelope for the tail union,

$$
\sup_{n\ge1,\ 0<t<1/2}\mathbb E[1_{\{t<\tau\}}S_t^H]<\infty.
$$

If further computation is used, first test the predicted fixed-time Poisson limit at much larger
$n$, then tighten full paths and stopping; another modest-dimensional path sweep is lower value.

---

## Cross-cutting verification debt

- **Covariance-window status.** The published sup-over-time / clean $(\log^2 n)^{-1}$ form is
  `KLnotes` Thm 61 (*not* `KlartagLehec2022Polylog` Lemma 5.2). Klartag–Lehec Corollary 5.4
  gives fixed-time moments on $(C\kappa_n^2\log n)^{-1}$; Letwin v1 makes $\kappa_n$ universal
  and hence extends that moment window to $c/\log n$. Keep the latter explicitly
  preprint-conditional and do not silently upgrade the separate sup-time theorem.
- Geometric module (`13-jacobi-splitting.tex`) results are **model statements**; the
  quantitative, uniform-in-localization versions are open (`q:splitting`).
