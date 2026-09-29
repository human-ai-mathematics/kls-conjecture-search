---
---

# Synthesizer: the reusable-facts registry, preserved at the harness migration

*The migration retires `research/knowledge/lemmas.md`. The new root contract says a finding
reusable enough to be cited elsewhere earns a ledger node and a manuscript statement, "not a
second home in a side registry", so the registry itself cannot survive. Its content is preserved
here verbatim, because a checkpoint is durable memory and deleting the text would lose work that
no node yet carries.*

## Disposition

Each entry below is one of three things, and none of them is a claim this record asserts:

- **already owned by a node** — `prop:letwin-not-gate-zero` is in the ledger; the entry's value is
  its guardrail, which now also appears in the problem brief's traps section;
- **a guardrail or audit test** — these have moved to `research/program/brief.md`, sections
  *Edge cases and audit tests* and *Traps and circular reductions*; the cut-local scale
  instability, the screened-absorption preconditions and the tensorization caveat are all there;
- **a candidate for promotion** — the cut-oriented Lyapunov dual scale is the strongest case for a
  future `kind: definition` node, since the wave-four screened interface depends on it. Promoting
  it needs a manuscript definition environment and is deliberately left as future work rather than
  done here by a harness migration, which changes no mathematical status.

Nothing below is certified by this record, and no status changes because of it.

## Preserved content

This file is a compact index of reusable facts. The cited manuscript or ledger label owns the
formal statement; proof dossiers own full arguments and certification. Entries here record only
the fact, its common use, and the main guardrail.

## Holley--Stroock perturbation

**Source.** Holley--Stroock bounded perturbation principle.

**Fact.** If $d\pi=e^{-W}d\nu/Z$ and $\operatorname{osc}(W)\le A$, then
$C_P(\pi)\le e^A C_P(\nu)$, with the analogous log-Sobolev bound.

**Use.** Transfer constants through a uniform density-ratio comparison.

**Guardrail.** Total variation convergence alone does not provide this comparison.

## Tensorization

**Fact.** For $\mu=\bigotimes_i\mu_i$,
$C_P(\mu)=\max_i C_P(\mu_i)$. If coordinate $i$ has weighted constant $C_i$ with weight $a_i$,
then the product has constant $\max_i C_i$ for the form
$\int\sum_i a_i|\partial_i f|^2d\mu$.

**Use.** Lift one-dimensional estimates to product measures.

**Guardrail.** A hierarchical or otherwise dependent law is not a product.

## $T_2$ covariance constraint

**Fact.** Under the convention
$W_2^2(\nu,\pi)\le2C\,\mathrm{KL}(\nu\|\pi)$,
$$
\operatorname{Cov}_\pi(X)\preceq CI,
\qquad
C_{\mathrm{TCI}}(\pi)\ge\lambda_{\max}(\operatorname{Cov}_\pi(X)).
$$

**Use.** Supply a necessary lower constraint for transportation-cost constants.

**Guardrail.** This is not an upper bound or an estimator of the optimal constant.

## Covariance-threshold block extraction

**Source.** The common algebra isolated in
`research/explorations/2026-08-27-kls-route-prober-upgrade-par-01.md` and
`research/explorations/2026-08-27-kls-route-prober-mm-spectral-occupation-par-02.md`.

**Fact.** Let $A\succeq0$, let $X=X^T=A^{1/2}ZA^{1/2}$, and for $L>0$ put
$P=\mathbf 1_{(L,\infty)}(A)$ and $Q=I-P$. Then
$$
\|X\|_{\mathrm{HS}}^2
=\|QXQ\|_{\mathrm{HS}}^2+\|PXP\|_{\mathrm{HS}}^2
+2\|PXQ\|_{\mathrm{HS}}^2,
$$
and
$$
\|QXQ\|_{\mathrm{HS}}^2\le L^2\|QZQ\|_{\mathrm{HS}}^2
\le L^2\|Z\|_{\mathrm{HS}}^2.
$$

**Use.** Convert an intrinsic or whitened Hilbert--Schmidt estimate into a bounded low-covariance
block while retaining every entry incident to the high-covariance space as one explicit residue.

**Guardrail.** This is algebra at a fixed state only. It gives no occupation estimate for the
high-incidence residue, and differentiating the random projector creates additional terms. The
factorization and the bound on $Z$ must be justified in the application; in the two KLS probes
the latter uses the unreviewed Letwin quadratic-Poincar\'e preprint. The identity does not relate
the cut tensor to the eigenfunction tensor.

## `prop:letwin-not-gate-zero` — static commutator split

**Fact.** For symmetric matrices $B,H$,
$$
\operatorname{Tr}(B^2H^2)
=\operatorname{Tr}(BHBH)+\frac12\|[B,H]\|_{\mathrm{HS}}^2.
$$

**Use.** Separate the constant-matrix channel controlled by the Letwin inequality from the
transverse term required by the CMH linear sector. For $B=a\otimes a$, it reads
$|Ha|^2=(a^THa)^2+\|[a\otimes a,H]\|_{\mathrm{HS}}^2/2$.

**Guardrail.** The algebraic countermodel certifies only that positivity, $\mathbb EH=I$, and
constant-matrix control do not bound the transverse term. It is not a moment-map counterexample.
This static commutator is not the stochastic high-incidence block, a moving spectral-projector
It\^o residue, or the square-root/Haar commutator of `q:mm-square-root-commutator`.

## Cut-oriented Lyapunov dual scale

**Source.** Dualization of the agent-certified `lem:pathwise-BL` in
`solutions/kls-localization-riccati-core.tex`; the direct-sum and two-tail calibrations are
recorded in
`research/explorations/2026-08-27-synthesizer-kls-wave-one.md`.

**Fact.** For $A\succ0$ define the Lyapunov operator on symmetric matrices by
$$
\mathscr L_A(M)=\frac{AM+MA}{2}.
$$
The anisotropic form of the certified pathwise Brascamp--Lieb calculation is
$$
s\langle K,M\rangle^2
\le \frac4t\langle M,\mathscr L_A M\rangle
\qquad(M=M^T),
$$
and Hilbert-space duality therefore gives
$$
s\langle K,\mathscr L_A^{-1}K\rangle\le\frac4t.
$$
For $K\ne0$ put
$$
\lambda_{\mathrm{cut}}(A,K)
=\frac{\|K\|_{\mathrm{HS}}^2}
{\langle K,\mathscr L_A^{-1}K\rangle},
$$
and set it to zero for $K=0$. Then
$$
s\|K\|_{\mathrm{HS}}^2\le\frac{4\lambda_{\mathrm{cut}}(A,K)}t.
$$
In an $A$-eigenbasis, $\lambda_{\mathrm{cut}}$ is the $K_{ij}^2$-weighted harmonic mean of
$(\lambda_i+\lambda_j)/2$. It is invariant under irrelevant direct sums:
$\lambda_{\mathrm{cut}}(A\oplus B,K\oplus0)=\lambda_{\mathrm{cut}}(A,K)$, and on the certified
anisotropic two-tail example it equals the inflated variance $\Lambda$.

**Use.** Separate covariance directions incident to a fixed cut tensor from independent
spectator spikes. It is a calibrated candidate scale for a tensor-stable replacement of the
global operator norm in the weighted-excess route.

**Guardrail.** This is a repackaging of a positive-time static inequality, not an occupation or
excess-propagation theorem. The factor $t^{-1}$ is singular at the initial endpoint, and no
bound for an integral weighted by $\lambda_{\mathrm{cut}}$ follows. The scale depends on the
cut tensor and cannot replace a cut-free covariance functional. For singular $A$, restrict the
operator to the covariance support (or state the corresponding Moore--Penrose convention)
before using the formula.

## Screened absorption preconditions

**Source.** Section 1 of
`research/explorations/2026-08-30-kls-route-prober-weighted-screened-interface-w4w01.md`
(consumer algebra of the screened `q:weighted` interface), audited and routed through
`research/explorations/2026-08-30-synthesizer-screened-kernel-comparison-w4y01.md`. Certified
inputs: `lem:stein-vs-source`, `cor:per-direction`, `thm:scalar-riccati`,
`cor:tight-window-consumption`.

**Fact.** For the screened pair
(S) $\mathbb E\int e_tW_{\rm cut}\mathbf 1_{\mathcal A_{\kappa,t}}\,dt\le C_ET$ and
(C) $\mathbb E\int Q_t\,dt\le C_0T+C_1\mathbb E\int r_t+\beta\mathbb E\int D_t
+C_2\mathbb E\int e_tW_{\rm cut}\mathbf 1_{\mathcal A_{\kappa,t}}
+\theta\mathbb E\int Q_t\mathbf 1_{\mathcal A_{\kappa,t}^c}$ on $[0,T\wedge\tau_\eta]$:

1. Absorbing the $\theta$-term requires the a priori finiteness
   $\mathbb E\int Q_t\,dt<\infty$ **before** subtraction. It holds with the dimension-dependent
   certified chain $Q_t\le2S_t+64\eta^2D_t$,
   $\mathbb E\int S_t\,dt\le\operatorname{Tr}R_0\le n$,
   $\mathbb E\int D_t\,dt\le1+n$, so
   $\mathbb E\int Q_t\,dt\le2n+64\eta^2(1+n)$. Dimension dependence is harmless here.
2. Feeding `cor:tight-window-consumption` demands the damping coefficient
   $\alpha=2\beta/(1-\theta)+64\eta^2<1$. Since $64\eta^2<1$ forces $\eta<1/8$, the admissible
   window is $\eta\in(0,1/8)$ with $\beta<(1-\theta)(1-64\eta^2)/2$; there is no admissible
   choice with $\eta\ge1/8$.
3. A constant supply $\mathbb E\int e_tW_{\rm cut}\mathbf 1_{\mathcal A}\,dt\le c_E$ (not
   $\propto T$) also suffices: Gronwall reads
   $u(T)\le(1+2C_2c_E/(1-\theta)+C_0'T)e^{C_1'T}$ and the survival time shrinks with $c_E$.
4. At $\theta=0$ the condition degenerates to the $2\beta+64\eta^2<1$ arithmetic of
   `ass:weighted-package`/`q:stein-weighted`; the screened algebra strictly generalizes it.

**Use.** Preconditions for any consumer-side (absorption/consumption) argument on the screened
Eldan interface; prevents wasted probes at $\eta\in[1/8,1/6]$ and silent subtraction of a
possibly infinite term.

**Guardrail.** Sketch-level: no dossier certifies the assembled chain, and item 3 is an
uncertified one-line Gronwall restatement of `cor:tight-window-consumption` (technical gap,
listed in the `w4w01` handoff). The constants $2$ and $64\eta^2$ are the certified
`lem:stein-vs-source` values; any $\varepsilon$-weighted refinement of the conversion is
uncertified, so the boxed coefficient is the current gate arithmetic. Nothing here bounds the
supply or companion themselves; both remain open.

## Aligned screen: initial-layer reduction and pathwise pin

**Source.** Sections 3.2–3.3 and 4 of
`research/explorations/2026-08-30-kls-route-prober-weighted-screened-interface-w4w01.md`;
comparison verdict in
`research/explorations/2026-08-30-synthesizer-screened-kernel-comparison-w4y01.md`. Certified
inputs: `lem:lyapunov-stein-duality`, `lem:pathwise-BL`, `prop:trivial-excess`,
`prop:two-tail`.

**Fact.** With $Q_t=s_t\|K_t\|_{\rm HS}^2$,
$W_{\rm cut}=(1+\lambda_{\rm cut}(A_t,K_t))^{5/2}$ (convention
$\lambda_{\rm cut}(A,0)=0$), and screen
$\mathcal A_{\kappa,t}=\{Q_t\ge\kappa e_tW_{\rm cut}\}$:

1. *Reduction (proved at certified-domination level).* For every $t_*>0$,
   $$
   \mathbb E\int_0^{T\wedge\tau_\eta}e_tW_{\rm cut}\mathbf 1_{\mathcal A_{\kappa,t}}\,dt
   \le\Bigl(1+\tfrac1{t_*}\Bigr)^{5/2}(1+e_0)\,T
   +\frac1\kappa\,\mathbb E\int_0^{t_*\wedge T\wedge\tau_\eta}
   Q_t\mathbf 1_{\mathcal A_{\kappa,t}}\,dt ,
   $$
   so the screened supply reduces, modulo a universal $O(T)$ layer, to the aligned
   initial-layer occupation estimate (AIK).
2. *Pathwise pin.* On $\mathcal A_{\kappa,t}$,
   $\kappa e_tW_{\rm cut}\le Q_t\le4\lambda_{\rm cut}/t$, hence
   $e_t\le4/(\kappa t(1+\lambda_{\rm cut})^{3/2})$: two-tail-calibrated states
   ($e\asymp\lambda^{-1/2}$) can be aligned only for $t\lesssim4/(\kappa\lambda)$.
3. *Chargeability threshold.* With $a=\Phi^{-1}(3/4)$,
   $\kappa_{\rm TT}=2^{-5/2}\cdot16a^2\varphi(a)^2/(2\varphi(a)-\varphi(0))\approx0.5492$;
   every fixed $\kappa<\kappa_{\rm TT}$ keeps all certified two-tail states in
   $\mathcal A_{\kappa,t}$ for all $\Lambda\ge1$.
4. *Spectator inertness.* Independent spectator blocks change neither $Q_t$ nor $W_{\rm cut}$
   (certified direct-sum invariance) and can only inflate $e_t$, i.e. shrink the charge set;
   the screen excludes the certified weighted-spectator and leakage witnesses, worst states
   first.

**Use.** Standard time-splitting and calibration facts for any attack on the screened supply;
cite this entry instead of re-deriving the reduction.

**Guardrail.** Item 1 uses `prop:trivial-excess`, which requires $\mu(E)=1/2$; keep the
balanced-start hypothesis. For singular $A_t$ use the covariance-support/Moore–Penrose
convention of `lem:lyapunov-stein-duality`. For general laws the screened statement is defined
on the certified product-preserving approximants; the screened indicator does not pass to
limits monotonically. Choosing $\kappa\ge\kappa_{\rm TT}$ silently discards the certified
two-tail obstruction and is not admissible calibration. AIK itself is open
(needs-new-idea), and it is **formally incomparable** with `ass:tight-prefix-carleson`: the
tight-prefix estimate implies only the constant-relaxed form AIK$^{+}$ (additive constant
$(2\alpha+64\eta^2)/(1-\alpha)$), the screen excludes excess-inflated states the prefix
estimate must count, the missing $r$/$D$ budgets cut the other way, and the zero-damping
two-tail family lies in both charges. No equivalence or ledger edge exists; trace-cluster
comparisons involving this object stay with the single synthesizer owner (CLAUDE.md
constraint 6).

## Appendix: the retired notation glossary

*`shared/notation.md` is retired with the `shared/` directory. It was written when this
repository still held Parts I and II, which the A-series split removed, and nothing live
referenced it; the authoritative Part III notation is `modules/kls/10-notation.tex` and the
macros are `preamble.tex`. Preserved verbatim below.*

> # Notation glossary
> 
> Symbols used throughout `modules/` (Parts I--II) and `modules/kls/` (Part III). The authoritative
> definitions for Part I are in `modules/01-definitions.tex`; the LaTeX macros are in
> `shared/preamble.tex`. The fixed normalization below must not be silently changed.
> 
> ## Measures and potentials
> 
> | Symbol | Meaning |
> |---|---|
> | `P` | target probability measure on `ℝ^D`, `P(dx) ∝ e^{-U(x)} dx` |
> | `U` | potential (`= -log` density up to a constant) |
> | `L` | reversible generator `Δ − ∇U·∇` of the overdamped Langevin diffusion |
> | `Hess U` | Hessian `∇²U`; `m`-strong convexity means `Hess U ⪰ m I_D` (`m>0`) |
> | `Σ`, `Σ_0` | a covariance; `Σ_0` is the Gaussian-prior covariance in the GLM spine |
> | `‖Σ‖_op`, `λmax(Σ)` | operator norm = largest eigenvalue of a symmetric PSD matrix |
> 
> ## The three constants (fixed normalization)
> 
> | Symbol | Definition |
> |---|---|
> | `C_P` | Poincaré: `Var_P(f) ≤ C_P · E_P|∇f|²`. `C_P^{-1}` is the spectral gap of `L`. |
> | `C_LS` | log-Sobolev: `Ent_P(f²) ≤ 2 C_LS · E_P|∇f|²`. |
> | `C_TCI` | transportation-cost (Talagrand `T₂`): `W₂²(Q,P) ≤ 2 C_TCI · KL(Q‖P)`, all `Q ≪ P`. |
> 
> Consequences of this normalization (proved in `modules/01-definitions.tex`):
> `C_P ≤ C_LS` (linearize LSI around constants) and `C_TCI ≤ C_LS` (Otto–Villani).
> 
> ## Imported proof mechanisms (Part I toolkit, `modules/02`)
> 
> | Label | Mechanism | One-line content |
> |---|---|---|
> | `thm:bakry-emery` | Bakry–Émery | `Hess U ⪰ m I ⇒ C_P ≤ C_LS ≤ 1/m` |
> | `thm:brascamp-lieb` | Brascamp–Lieb | `Var_P(f) ≤ E_P⟨(Hess U)^{-1}∇f, ∇f⟩` (varying curvature) |
> | `thm:holley-stroock` | Holley–Stroock | bounded perturbation `e^{-W}`: constants `× e^{osc(W)}` |
> | `thm:tensorization` | tensorization | `C_P(⊗_i μ_i) = max_i C_P(μ_i)` |
> | `thm:otto-villani` | Otto–Villani | LSI `⇒` `T₂`, `C_TCI ≤ C_LS` |
> | `thm:hardy-1d` | Hardy/Muckenhoupt | sharp two-sided `C_P` in 1D and 1D reductions |
> | `cor:ccnw-mixture-lsi` | Chen–Chewi–Niles-Weed | bounded-`χ²` mixtures have dimension-free LSI |
> 
> ## The tier curriculum (Part I)
> 
> | Section | Tier | Family |
> |---|---|---|
> | `sec:tier1` | 1 | Gaussian, strongly log-concave, Bayesian linear regression (exact) |
> | `sec:tier2` | 2 | bounded perturbations (Holley–Stroock), products (tensorization) |
> | `sec:tier3` | 3 | Gaussian-prior GLM posterior — flagship `thm:glm-fi` |
> | `sec:tier4` | 4 | heavy-tailed priors; LSI/`T₂` obstruction `thm:heavy-tail-no-lsi` |
> | `sec:tier5` | 5 | mixtures, label-switching, hierarchical funnels |
> | `sec:agenda` | — | open research agenda; bridge to KLS |
> 
> ## Part III (KLS) — key symbols
> 
> | Symbol | Meaning |
> |---|---|
> | `h*_n` | worst-case Cheeger constant over isotropic log-concave measures on `ℝ^n` |
> | `p_t = μ_t(E)` | mass martingale of a fixed cut `E` under Eldan stochastic localization |
> | `A_t` | covariance process of the localization, `dA_t = Θ_t dW_t − A_t² dt` |
> | `Ξ_T` | interface functional `∫_0^T E (λmax(A_t) − 1)_+ dt` |
> | `H=D²φ` | stationary moment-map Hessian metric (CMH route; never the stochastic `H_t`) |
> | `N`, `K_M` | moment-map elliptic operator and compressed multiplier in the CMH route |
> 
> The KLS macros (`\hstar`, `\PsiKLS`, `\Per`, `\HS`, `\cal*`, …) live in `shared/preamble.tex`.
> 
> ## Conventions
> 
> - `‖M‖_op = λmax(M)` for symmetric PSD `M`; `A ⪰ B` is the Loewner order.
> - `φ`, `Φ` are the standard Gaussian density and CDF.
> - Dimension is `D` (Part I, statistics convention) or `n` (Part III); `n` in Part I is the
>   number of data points.
> - The dimension-free Poincaré bound for *arbitrary* isotropic log-concave measures is the
>   KLS conjecture — the Tier-∞ boundary of Part I, and the subject of Part III.
