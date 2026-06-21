# Obstructions — the KLS search-space fence

Hard-won negative results that bound what any proof of KLS through this program can look
like. Before proposing an approach, check it here; after producing a result, check it does
not contradict one. Each obstruction has a stable `obs:` id used by `ledger.yaml`
(`bounded_by:` edges).

Ported from the standalone KLS program's roadmap; `\label`/module references re-synced to
the unified `modules/kls/`.

> **Machine-readable mirror:** [`obstructions.yaml`](obstructions.yaml) carries the closed
> `mechanism` vocabulary and what each obstruction `forbids`. `../check_ledger.py` enforces
> it: a KLS-ledger node whose proof declares a forbidden `mechanism` tag must clear the
> obstruction (`bounded_by` + a `clearance` note) or the check fails. The `obs:` ids here
> stay in parity with the YAML (the checker verifies this).

---

### `obs:two-tail` — no slice-wise absolute-scale Stein estimate; weight is forced
**Statement.** `prop:two-tail` (`modules/kls/05-obstruction.tex`). For
$\nu_\Lambda = N(0, \operatorname{diag}(\Lambda,1,\dots,1))$ and the two-tail cut
$E_\Lambda = \{|x_1| \ge a\sqrt\Lambda\}$ at mass $\tfrac12$: $\delta=0$, $r=D=0$, while
$S/s \asymp \Lambda^2$ and excess $e \asymp \Lambda^{-1/2} \to 0$.
**Kills.** Any inequality of the form $S_\nu(E)/s \le C_0 + C_1 r + \beta D + C_2\, e(E)$
with measure-independent constants — i.e. any **slice-wise (pointwise-in-time)** proof of
the stable Stein-trace estimate with an **absolute-scale** excess term.
**Forces.** The covariance weight $(1+\|A\|_{\mathrm{op}})^{5/2}$ on the excess term
(power-matching $\Lambda^2$ against $\Lambda^{-1/2}$), and explains the rate $T^{1+\gamma}$
as the shadow of the Brascamp–Lieb cap. Any proof must instead show such inflated
configurations carry negligible **expected occupation** — a Carleson-type statement.
**Regime.** Anisotropic posteriors $\mu_t$ with $\lambda_{\max}(A_t)=\Lambda\gg1$; cannot
occur at $t=0$ (isotropic). Constrains: `ass:weighted-package`, `q:weighted`, `q:stein-weighted`.

### `obs:proj-ceiling` — projection/radial tests cap at $\log n$
**Statement.** `modules/kls/05-obstruction.tex`. There is a positive operator $T$ on
symmetric matrices with $\langle P,TP\rangle \le C\cdot\operatorname{rank}(P)$ for every
projection $P$ while $\|T\|_{\mathrm{op}} \asymp \log n$ (explicit diagonal construction
with harmonic weights). Separately, projection thin-shell gives only
$\operatorname{Var}(X^\top M X) \lesssim \log n \cdot \|M\|^2$.
**Kills.** Any proof of quadratic-chaos thin shell (hence of the two-color source bound)
that uses **only radial information or projection tests**. The logarithm is intrinsic to
projection-only information, not an artifact of integration.
**Regime.** Static, all dimensions. Constrains: `q:upgrade`, `prop:qcts-equivalence`.

### `obs:crude-insufficient` — Klartag's own bound defeats the naive bootstrap
**Statement.** `lem:crude` + `rem:insufficiency` (`modules/kls/12-bootstrap.tex`). The crude
evaluation $\Xi_T \lesssim \log n$ would need $h_\mu \le CT/\log n$ to certify an $O(T)$
excess bound; but $h_\mu \ge h^*_n \ge c(\log n)^{-1/2}$ (Klartag 2023) exceeds that for all
large $n$.
**Kills.** Using the crude interface evaluation as the bootstrap input. The best known KLS
lower bound is itself the obstruction. Any useful evaluation of $\Xi_T$ must beat $\log n$
(the polylog technology gives $\log\log n$, `cor:loglog`).
**Regime.** High dimension. Constrains: any bootstrap route relying on `lem:crude`.

### `obs:relative-ceiling` — relative scale is KLS-equivalent, not an intermediate target
**Statement.** `prop:ceiling` (`modules/kls/12-bootstrap.tex`). If $\Xi_{T_0}(\mu) \le \kappa
T_0$ held for **every** isotropic log-concave $\mu$, KLS would follow directly. Hence a
relative-scale propagation bound $\int E\,\bar e_t \le \kappa h_\mu T$ would require
$\Xi_T \le c\kappa T$, an input already implying the whole conjecture.
**Kills.** Treating relative-scale excess propagation **for all measures** as a legitimate
stepping stone. It is only legitimate **with a near-worstness hypothesis** (that is exactly
`q:taming`).
**Regime.** All measures vs near-worst. Constrains: `ass:all-cut-carleson`, `q:taming`.

### `obs:circularity` — direct excess propagation is circular
**Statement.** `lem:excess-identity` + `lem:inf-martingales` + `rem:circularity`
(`modules/kls/11-excess-propagation.tex`). $E e_t = e_0 + [I_\mu(p_0) - E\,I_{\mu_t}(p_t)]$;
the localized profile is an infimum of perimeter martingales (a supermartingale), and any
quantitative lower bound on $E\,I_{\mu_t}(p_t)$ **is** a Cheeger lower bound for the random
measure $\mu_t$ — a localized KLS statement.
**Kills.** Any **direct** attack on excess propagation that does not introduce an external
anchor: it presupposes the kind of estimate the program is trying to produce.
**Escape.** The only non-circular anchor is the worst-case constant $h^*_n$ of the dimension,
legitimate in a proof by contradiction — this is the bootstrap (`thm:bootstrap`), valid for
near-worst measures only.
**Regime.** All. Constrains: any `q:weighted` attempt not routed through the bootstrap.

### `obs:rank-one-refuted` — a counterexample cannot ride a single inflated coordinate
**Statement.** `cor:refutation` (`modules/kls/09-product-stress.tex`). For a product measure
and any balanced cut depending on a **single** coordinate, the total source budget is
$E\int_0^\infty S_t \le 1$, so a source spike of height $\Lambda^2$ has expected occupation
$\lesssim \Lambda^{-2}$ — it is **self-extinguishing**. $\mu^+(E) \ge c\cdot\min(p,q)$.
**Kills.** The originally-proposed counterexample to Route A ("a cut adapted to the
dynamically large coordinate"). A counterexample, like a proof, must be genuinely
high-dimensional and cut-aware.
**Regime.** Product measures. Constrains: `q:alignment` (the residue is high-complexity cuts,
not single-coordinate ones).

---

## How obstructions interlock

The same residual difficulty appears in three coordinates: **operator-to-trace upgrade**
(`obs:proj-ceiling`, Route A), **weighted excess / two-tail occupation** (`obs:two-tail`,
Route B), and **constant-mode curvature** (`modules/kls/13-jacobi-splitting.tex`). The static
obstructions (`obs:two-tail`, `obs:proj-ceiling`) say cut-free / slice-wise information
saturates at a logarithm; the dynamical escape in every case is an **expected-occupation
(Carleson) estimate** that uses the cut.
