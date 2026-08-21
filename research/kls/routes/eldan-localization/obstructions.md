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
**Forces.** The covariance weight $(1+\|A\|_{\mathrm{op}})^{5/2}$ on any slice-wise excess term
(power-matching $\Lambda^2$ against $\Lambda^{-1/2}$). It does **not** determine the time rate
$T^{1+\gamma}$; that remains a stronger open demand requiring a joint rare-event estimate. Any proof must instead show such inflated
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
**Update (2026-08-20).** Letwin's version-1 preprint proves quadratic-chaos thin shell by a
moment-map/Stein-kernel argument, bypassing rather than contradicting this method-specific no-go.
**Regime.** Static, all dimensions. Constrains: `q:upgrade`, `prop:qcts-equivalence`.

### `obs:crude-insufficient` — Klartag's own bound defeats the naive bootstrap
**Statement.** `lem:crude` + `rem:insufficiency` (`modules/kls/12-bootstrap.tex`). The crude
evaluation $\Xi_T \lesssim \log n$ would need $h_\mu \le CT/\log n$ to certify an $O(T)$
excess bound; but even the published $h_\mu \ge h^*_n \ge c(\log n)^{-1/2}$ (Klartag 2023),
and a fortiori Letwin's version-1 $c(\log n)^{-1/4}$ claim, exceeds that for all
large $n$.
**Kills.** Using the crude interface evaluation as the bootstrap input. The best known KLS
lower bound is itself the obstruction. Any useful evaluation of $\Xi_T$ must beat $\log n$
(the polylog technology gives $\log\log n$, `cor:loglog`).
**Regime.** High dimension. Constrains: any bootstrap route relying on `lem:crude`.

### `obs:relative-ceiling` — relative scale for all measures is already KLS-sufficient
**Statement.** `prop:ceiling` (`modules/kls/12-bootstrap.tex`). If
$9(1+\kappa)T_0\le1/2$ and $\Xi_{T_0}(\mu) \le \kappa T_0$ held for **every** isotropic
log-concave $\mu$, KLS would follow directly. Within `thm:bootstrap`, certifying a
relative-scale propagation bound $\int E\,\bar e_t \le \kappa h_\mu T$ would demand this
unweighted scale of control on $\Xi_T$.
**Kills.** Treating the all-measure bound $\Xi_T\le\kappa T$ as a weaker input to this
localization route. The target `q:taming` is different: it is both near-worst-specific and
$h_\mu$-weighted, and supplies absolute-scale excess.
**Regime.** All measures vs near-worst. Constrains: `ass:all-cut-carleson`, `q:taming`.

### `obs:circularity` — direct profile propagation risks circularity
**Statement.** `lem:excess-identity` + `lem:inf-martingales` + `rem:circularity`
(`modules/kls/11-excess-propagation.tex`). $E e_t = e_0 + [I_\mu(p_0) - E\,I_{\mu_t}(p_t)]$;
any quantitative lower bound on $E\,I_{\mu_t}(p_t)$ is a Cheeger-type bound for the random
measure $\mu_t$. The infimum over a **fixed** set family is a supermartingale, but the family
eligible at balanced $\mu_t$-mass is random and time-dependent, so that lemma gives no
supermartingale property for the localized profile.
**Warning.** An argument that merely inserts a lower profile bound may restate the desired
phenomenon. This is not a formal no-go: additional structure could control the moving infimum.
The external worst-case constant $h^*_n$ is one sound anchor, used by `thm:bootstrap`, but is not
proved to be the only possible anchor.
**Regime.** All. Constrains: `q:weighted` as a proof-design warning only; it forbids no mechanism
in `obstructions.yaml`.

### `obs:rank-one-refuted` — on products, a fixed single-coordinate cut cannot ride inflation
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

Route A's operator-to-trace upgrade is the full occupation trace; the product alignment problem
isolates its incident-high masked residue and is a model reduction, not an equivalent theorem.
Weighted excess and the proposed Jacobi/Reilly route face related
high-covariance/high-rank phenomena, but no equivalence with the boundary constant mode is
proved. The missing almost-stability trace bridge is recorded in `rem:almost-stability-gap`.
