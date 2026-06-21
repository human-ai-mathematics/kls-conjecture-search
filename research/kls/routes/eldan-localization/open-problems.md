# Open problems — the live KLS frontier (P1–P7)

The KLS analogue of `../targets/*.md`. KLS is **one interlinked proof program**, not seven
independent targets, so its open problems are kept together here (with the cross-references
that bind them) rather than split into one file each. Ported from the
standalone KLS program's roadmap; references re-synced to the unified `modules/kls/`.

Each entry is a **self-contained brief**:
- **Statement** — the precise target (`\ref` label + ledger id).
- **Unlocks** — what it implies (from `ledger.yaml`).
- **Bounded by** — obstructions any proof must respect (`obstructions.md`).
- **Attack** — the suggested mechanism / available tools.
- **Prior work** — what has been tried; entry point.

Cross-check every claimed result against `obstructions.md`, update `ledger.yaml`, and run
`python3 research/check_ledger.py`.

---

## P1 · `q:upgrade` — operator-to-trace upgrade (Route A headline)

**Statement** (`q:upgrade`, `modules/kls/14-open-targets.tex`; target `ass:all-cut-carleson`).
Upgrade the unconditional per-direction Carleson estimate `cor:per-direction`
($E\int s_t|G_t\theta|^2\,dt \le \theta^\top R_0\theta \le 1$, every fixed $\theta$) to the
**trace** scale uniformly over balanced cuts:
$E\int_{I\cap[0,\tau]} s_t\|G_t\|^2_{\mathrm{HS}}\,dt \le C_0|I| + C_1 E\int r_t + \alpha E\int D_t$,
$\alpha<1$. Equivalently, the source $s_t G_t^2$ must not occupy many almost-orthogonal
directions for a non-negligible set of early balanced times (noncommutative Carleson).

**Unlocks.** `ass:all-cut-carleson` ⇒ `thm:intro-all-cut` ⇒ **KLS directly**.

**Bounded by.** `obs:proj-ceiling` (projection/radial info caps at $\log n$ — the upgrade
*must* use cut-specific structure $G_t, K_t, D_t$, not spectral control of $A_t$);
`obs:two-tail` (the inflated-posterior configuration must be shown rare, not controlled
pointwise).

**Attack.** The difficulty is purely small-time (`cor:away-from-zero`: for $t\ge t_0$,
$S_t \le 8/t^2 + D_t/2$ pathwise). Needs a probabilistic small-time non-alignment estimate
between the whitened color Hessian $H_t = A_t^{-1/2} G_t A_t^{-1/2}$ and the large spectral
windows of $A_t$ (the Euclidean source is $S_t = s_t\operatorname{Tr}(A_t H_t A_t H_t)$).

**Prior work / entry point.** Start with `prog:product-test` (P7): on products the
per-direction estimate becomes a per-coordinate **budget** (`thm:budget`) and the whole
question reduces to `q:alignment` (P6). Settle the model first. **Numerics:** `finum run --target kls-loc` (finum.localization).

---

## P2 · `q:weighted` — weighted excess propagation with rate (Route B input i-w)

**Statement** (`q:weighted`; target `ass:weighted-package`). For balanced near-Cheeger $E$
($e_0(E)\le1$) and $T\le T_0$:
$E\int_0^{T\wedge\tau_\eta} e_t(E)\,(1+\|A_t\|_{\mathrm{op}})^{5/2}\,dt \le C(T e_0(E) + T^{1+\gamma})$.

**Unlocks.** Half of `ass:weighted-package`.

**Bounded by.** `obs:two-tail` — the weight $(1+\|A\|)^{5/2}$ and rate $T^{1+\gamma}$ are
*calibrated* on the two-tail example (`prop:two-tail`); a weaker absolute-scale form is inert
(`prop:intro-audit`) and unprovable slice-wise. `obs:circularity` — do **not** attack
directly; route through the bootstrap.

**Attack.** The **unweighted** analogue is already resolved by the bootstrap
(`thm:bootstrap`, near-worst measures, all balanced cuts). The weighted version additionally
needs **second-moment control of the perimeter martingale against the covariance weight** —
control of $E\int e_t (1+\|A_t\|)^{5/2}$ rather than $E\int e_t$. The perimeter is a
martingale (`lem:perimeter-martingale`); the missing piece is its interaction with rare
covariance-inflation excursions (heuristic $E e_t \lesssim t^{3/2}$ where the BL cap
saturates, `rem:weight-explains-rate`).

**Prior work / entry point.** `thm:bootstrap` + interface evaluation (`cor:loglog`). Connects
to `q:taming` (P4).

---

## P3 · `q:stein-weighted` — weighted stable Stein trace (Route B input ii-w)

**Statement** (`q:stein-weighted`; target `ass:weighted-package`). Prove the weighted stable
Stein-trace estimate for balanced near-Cheeger cuts, damping $\beta<\tfrac12$, with the excess
term in the $(1+\|A_t\|)^{5/2}$-weighted form.

**Unlocks.** The other half of `ass:weighted-package` ⇒ (with P2) `thm:intro-weighted` ⇒ **KLS**.

**Bounded by.** `obs:two-tail` (no slice-wise shortcut).

**Attack.** Mechanism in `modules/kls/13-jacobi-splitting.tex` (`rem:dirichlet-trace`): via the
boundary representation (`lem:boundary-rep`) and the weighted Reilly identity (`prop:reilly`),
reduce to (a) quadratic-chaos control of the interior Dirichlet quantity (available up to the
log ceiling, `obs:proj-ceiling`); (b) stability control of mean-zero boundary modes
(`prop:second-variation`); (c) the **constant mode** via the Schur energy $J^\sharp$ or
splitting. (c) is the residual — the same constant-mode obstruction as `q:upgrade` in geometric
coordinates.

**Prior work / entry point.** Constant mode needs `q:splitting` (P5). The Stein-norm ↔ Riccati
source conversion is lossless on the tight window (`lem:stein-vs-source`).

---

## P4 · `q:taming` — extremality tames the covariance process

**Statement** (`q:taming`). For every $\kappa>0$, do there exist $\varepsilon,T_0>0$ such that
every isotropic log-concave $\mu$ with $h_\mu \le (1+\varepsilon)h^*_n$ satisfies
$h_\mu\,\Xi_{T_0}(\mu) \le \kappa T_0$? Here $\Xi_T = \int_0^T E(\lambda_{\max}(A_t)-1)_+\,dt$.

**Unlocks.** Relative-scale excess propagation for near-worst measures (via `thm:bootstrap`).

**Bounded by.** `obs:relative-ceiling` — the same statement **without** near-worstness is
KLS-equivalent, so the near-worstness hypothesis is essential and legitimate.

**Attack.** Couple the **splitting analysis** (`modules/kls/13-jacobi-splitting.tex`) to the
**covariance SDE** (`eq:cov-sde`): covariance inflation is driven by third-moment anisotropy,
while near-worst measures are conjecturally approximately split along their dangerous
directions (where variance processes are one-dimensional and tame, `prop:products`(ii)). This
coupling has **not been attempted**; note the type mismatch in `rem:taming-type-mismatch`.

**Prior work / entry point.** Already settled affirmatively (under `hyp:KI`, discharged by
`thm:KL-window`) whenever $h^*_n \le c\kappa T_0/\log\log n$ (`cor:loglog`); the only obstructed
regime is $h^*_n$ decaying slower than $1/\log\log n$. See `cor:dichotomy`.

---

## P5 · `q:splitting` — quantitative splitting / boundary Obata

**Statement** (`q:splitting`). For a near-worst measure and a near-minimal balanced cut, small
constant-mode curvature $\mathfrak K_\Sigma$ forces quantitative proximity, along the normal
direction, to the split structure of `prop:exact-splitting`, with constants stable under the
localization tilt (`prop:persistent-splitting`).

**Unlocks.** The constant-mode part of `q:stein-weighted` (P3).

**Attack.** The equality case is proved (`prop:exact-splitting`: $\mathfrak K_\Sigma = 0$ ⇔
product with a log-affine factor). Need the *stability* (Obata-type rigidity) version. Note
`cor:generic-degeneracy`: in a small-Cheeger counterexample the splitting branch is **generic**,
not exceptional — so this is central.

---

## P6 · `q:alignment` — adapted alignment problem for products (Route A residue)

**Statement** (`q:alignment`, `modules/kls/09-product-stress.tex`). For $\mu$ a product of $n$
isotropic two-sided exponentials: does there exist universal $T_0,C_0,C_1,\alpha<1$ such that
for every $n$ and every balanced cut $E$,
$E\int_{I\cap[0,\tau]} \sum_{i:\,A_t^{(i)}\ge2} s_t|G_t e_i|^2\,dt \le C_0|I| + C_1 E\int r_t + \alpha E\int D_t$?
Equivalently: can a **fixed** cut spend $\Omega(1)$-fractions of unboundedly many per-coordinate
budgets inside a common short window, while staying balanced and underdamped?

**Unlocks.** `prog:product-test` decided positively ⇒ strong evidence for / a model of
`q:upgrade`. A negative answer (an explicit aligning cut) **refutes** `ass:all-cut-carleson`
and forces Route B.

**Bounded by.** `obs:rank-one-refuted` — single-coordinate cuts cannot do it (budget $\le1$,
spikes self-extinguish); the residue is genuinely high-complexity cuts.

**Attack.** **Designated test family** (`rem:test-family`): permutation-symmetric thin-shell
sets $E = \{x : \sum_i \psi(x_i) \ge \theta\}$, $\psi$ even. Compute $E\int_0^T S_t\,dt$ using
1D log-concave estimates, independence, and the explicit variance dynamics (`prop:products`).
**Finite-dimensional in difficulty** and the single most informative computation now open on
Route A. **Numerics:** `finum run --target kls-loc` thin-shell run; the live danger is past $t_1(n)=c/(\log n)^2$ and
non-radial coordinate-selective cuts — see the 2026-06-18 thin-shell-alignment exploration.

---

## P7 · `prog:product-test` — execute/extend the product stress test

**Status.** Largely **executed** in `modules/kls/09-product-stress.tex`: coordinate budgets
(`thm:budget`), rank-one refutation (`cor:refutation`), covariance reduction (`cor:V2-implies`),
polylog-window discharge (`thm:V2-window`, `cor:KI-discharged`). The remaining open part is
exactly `q:alignment` (P6). The covariance-only route is heuristically expected to fail on
universal windows (`heur:V2-fails`) — so any proof must be cut-aware.

**Highest-value next step.** The thin-shell-family computation of P6.

---

## Cross-cutting verification debt

- **`thm:KL-window` / `hyp:KI` citation — DISCHARGED (2026-06-14 sweep).** The
  "unconditional on the polylog window" claims (`thm:V2-window`, `cor:KI-discharged`, hence
  `cor:loglog`, `cor:dichotomy`) rest on the Klartag–Lehec covariance bound in its
  **exponential-tail** form. Resolved: the sup-over-time / clean $(\log^2 n)^{-1}$-window form is
  `KLnotes` Thm 61 (*not* `KlartagLehec2022Polylog` Lemma 5.2); the second moment $E X_t^2$ is
  `KlartagLehec2022Polylog` Cor 5.4. See `rem:kl-window-verified`. Residual: confirm statement
  numbering against local arXiv copies (version-dependent).
- Geometric module (`13-jacobi-splitting.tex`) results are **model statements**; the
  quantitative, uniform-in-localization versions are open (`q:splitting`).
