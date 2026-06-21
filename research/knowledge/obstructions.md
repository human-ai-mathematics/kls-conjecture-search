# Obstructions — the shared no-go knowledge

Cross-cutting barriers and known-false statement forms. Each obstruction constrains the
*shape* a valid theorem may take; a conjecture that violates one is wrong by construction.
The machine-readable nodes live in `../ledger.yaml` (`kind: obstruction`); the prose, the
*why*, and the **numerical demonstration** live here. Targets reference these via `bounded_by`.

Math is written in LaTeX (`$…$`); the canonical *formal* statement of each barrier is the
manuscript `\label` named under "Source" — this file links and explains, it does not restate
formally. (Part III/KLS keeps its own, machine-enforced no-go set in `../kls/obstructions.md`.)

> When you discover a new barrier useful to more than one target, add it here AND as an `obs:`
> node in the ledger. Single-target subtleties stay in that target's `.md`.

---

## obs:flat-direction — no global data-curvature floor
**Used by:** A1 (bulk tail term), A3 (tail), A5 (funnel). **Source:** `prop:flat-prior-nonintegrable`.

GLM likelihood curvature $\ell''(x_i^\top\theta)$ vanishes where $|x_i^\top\theta|\to\infty$
(logistic: $\sigma(1-\sigma)\to0$), so the global Hessian floor $\inf_\theta\lambda_{\min}(\nabla^2 U)$
is set by the **prior alone** ($\Sigma_0^{-1}$). Consequence: **any data-informed bound must
carry a tail/penalty term** — there is no $C_P \le \text{bulk}$ with no tail. The same
vanishing-curvature directions reappear as A3's surviving tail and A5's funnel flat mode.

**Numerical demonstration.** Separable / near-separable logistic: $\lambda_{\max}(\mathrm{Cov}_\pi)$
(a sound $C_P$ lower bound, see `lemmas.md`) inflates with the separation, while the bulk term
$\lambda_{\max}(A_{\bar W}^{-1})$ stays small $\Rightarrow$ a tail-free bound is *falsified*.
Lives in `instances.md` as `stress-logit-separable`.

---

## obs:heavy-tail-no-classical — no classical LSI/$T_2$ (and no classical Poincaré) for heavy tails
**Used by:** A3, A4. **Source:** `thm:heavy-tail-no-lsi`, Tier 4.

Polynomial/exponential tails admit no classical LSI and no $T_2$ (an LSI forces sub-Gaussian
concentration); for the heaviest tails even the classical Poincaré fails. The correct object is
a **weighted** (or weak) inequality with a tail-growing weight $a(x) \asymp 1+\|x\|^2$.

**Numerical demonstration.** Generalized Cauchy $\mu_\beta \propto (1+\|x\|^2)^{-\beta}$: the
unweighted 1D Hardy functional $\asymp x^2 \to \infty$ (so $C_P=\infty$); reweighting the
Dirichlet form by $(1+x^2)$ brings it to $O(1)$. The Student-$t$ closed-form gaps
$\lambda_{\beta,d}$ (`thm:a3-student`) are the calibration anchor.

---

## obs:tv-insufficient — TV-BvM does not control the constants
**Used by:** A2. **Source:** `warn:a2-tv-fails`.

Total-variation convergence to the BvM Gaussian says nothing about constants — they see tails
and remote mass that TV does not. A "BvM $\Rightarrow$ constants" claim is **false** as stated.

**Numerical demonstration (the canonical A2 trap).**
$\mu_n = (1-\varepsilon_n)N(0,1) + \varepsilon_n N(a_n,1)$ with $\varepsilon_n \to 0$,
$\varepsilon_n a_n^2 \to \infty$: $\|\mu_n - N(0,1)\|_{\mathrm{TV}} \le \varepsilon_n \to 0$ yet
the linear test gives $C_P(\mu_n) \ge \mathrm{Var}_{\mu_n}(x) \to \infty$. The reward harness
must FALSIFY any "BvM $\Rightarrow$ $n\,C_P \to \lambda_{\max}(I^{-1})$" claim here.

---

## obs:symmetry-vs-physical — symmetry-induced vs physical multimodality
**Used by:** A2 (`q:a2-multimodal`), A4 (`q:a4-multimodal`), A5. **Source:** `prop:a5-ratio`.

Quotienting by a symmetry group $G$ helps **iff the slowest eigenfunction is non-invariant**
(label switching): then $\lambda_{\mathrm{noninv}} \ll \lambda_{\mathrm{inv}}$ and $C_P$ drops
dramatically. If the slow mode is invariant (a genuine physical alternative after relabeling),
quotienting does nothing. Importing a global metastability bound without checking the
representation type is the error.

**Numerical demonstration.** Folded double well $\mu_a = \tfrac12 N(-a,\sigma^2)+\tfrac12 N(a,\sigma^2)$
(`ex:a5-folding`): the odd test function gives $C_P(\mu_a) \gtrsim e^{a^2/2\sigma^2}$ (raw) but
$C_P(\bar\mu_a) = O(\sigma^2)$ (quotient).

---

## obs:restricted-not-finite — family-restricted transport constants can be infinite
**Used by:** A4, A3. **Source:** `warn:a4-heavytail`.

$C_{\mathcal Q} \le C_{\mathrm{TCI}}$, and $C_{\mathcal Q}$ can be *much* smaller — but it is
**not automatically finite**, even for a Gaussian location family. Finiteness needs at least one
of: bounded $\mathcal Q$, restriction to a KL sublevel $C_{\mathcal Q,r}$, Gaussian-like tails
of $\pi$ along the explored directions, or a modified cost.

**Numerical demonstration.** $\pi \propto e^{-|x|^p}$, $1 \le p < 2$, and $q_m = N(m,\sigma^2)$:
$W_2^2(q_m,\pi) \asymp m^2$ while $\mathrm{KL}(q_m\|\pi) \asymp |m|^p$, so
$W_2^2/\mathrm{KL} \asymp |m|^{2-p} \to \infty$. Hence $C_{\mathcal Q}=\infty$ already at
mean-field Gaussian level for $p<2$.

---

### Note: the heavy KLS-style obstruction machinery is deferred (for the A-series)
The KLS program (`../kls/obstructions.yaml`) enforces a controlled vocabulary of forbidden
*proof mechanisms* (slice-wise, circular, …) via `check_ledger`. That guards *proofs*, so it
belongs to Phase 2. For A1–A5 Phase-1 refinement, obstructions are constraints on the
*statement form* (above), which numerics can demonstrate directly. Add mechanism enforcement to
the A-series only when proving starts.
