# Lean (L2) channel — design and Mathlib gap

This is the **Lean channel's design document**, the machine-certified counterpart of the
numerical channel (`finum`, `experiments/`). Where `finum` *refines and refutes* statements (and
never promotes a node to proved), the Lean channel is one of the two ways a ledger node may
legitimately reach `status: proved` — the **machine-checked** one.

It answers a single, architecture-shaped question:

> *What must Mathlib provide before a `solutions/<id>.lean` can exist for a given ledger node?*

The gap below is therefore scoped to the **minimal formal spine** the project would formalize
first — the imported toolkit of
[`modules/02-results-toolkit.tex`](modules/02-results-toolkit.tex):

> **Gaussian Poincaré → tensorization → Bakry–Émery.**

a handful of classical theorems, not the whole theory. Status as of mid-2026 mathlib4
(`leanprover-community/mathlib4`); module paths are the real ones to start from. Verdicts:
**present** / **partial** / **absent**. Sources are listed at the bottom; everything below was
checked against the mathlib4 docs, not recalled.

---

## 0. Where the Lean channel sits in the architecture

The repo runs a two-phase, soundness-first pipeline (`research/README.md`):

```
open .tex statement → Phase 1 (refine + finum stress-test) → conjectured / evidence: numerical-strong
                    → Phase 2 (prove) → proved
```

Phase 2's output plane is `solutions/`, gated by the `checked_by` ladder
(`solutions/README.md`):

| `checked_by` | meaning | promotes node to `proved`? |
|---|---|---|
| `none` | drafted, unreviewed | **no** |
| `agent` | a distinct agent reviews the dossier and persists a report | yes (agent-certified) |
| `human` | a human accepts the natural-language argument | yes (NL-certified) |
| `lean` | a compiling `<id>.lean` sits beside `<id>.tex` | **yes (machine-certified)** |

`research/check_ledger.py` enforces that a node flips to `proved` only with
`checked_by ∈ {agent, human, lean}` and the matching solution/review metadata required by that
level. **Numerics never appear on this
ladder** — the soundness contract (`finum`'s only sound verdict is REFUTED) means the Lean
channel, not `finum`, is the upper end of the evidence hierarchy: any numerical corroboration
reward is capped strictly below what a checked Lean proof (the **L2 reward**) grants.

So this document is the substrate-gap half of the Lean channel: the deliverable is not just
"contribute to Mathlib," it is "close enough of the gap that the *proved* nodes of
`research/ledger.yaml` and `research/kls/ledger.yaml` can each acquire a `solutions/*.lean`
with `checked_by: lean`." §5 names those first targets explicitly.

---

## 1. Executive summary

| Building block | Mathlib status | Module (entry point) |
|---|---|---|
| Real Gaussian `gaussianReal` (1D) | **present** | `Probability.Distributions.Gaussian.Real` |
| General `IsGaussian` (Banach/Hilbert/finite-dim, via char. functions) | **present** (recent) | `Probability.Distributions.Gaussian.Basic` |
| Multivariate Gaussian as `N(0,Σ)` with covariance **matrix** + `‖Σ‖_op` | **partial** (no matrix-level covariance API) | — |
| `variance`; variance of a sum over a product measure | **present** | `Probability.Moments.Variance` (`variance_sum_pi`) |
| Finite product measures; independence | **present** | `MeasureTheory.Constructions.Pi`, `Probability.Independence.Basic` |
| KL divergence `klDiv`, log-likelihood ratio `llr` | **present** | `InformationTheory.KullbackLeibler.Basic` |
| Entropy functional `Ent_μ(g)=∫ g log(g/∫g) dμ` (LSI form) | **absent** (buildable from `llr`+`Real.log`) | — |
| Dirichlet energy `∫‖∇f‖² dμ` as a packaged form | **absent** (components exist: `fderiv`, `∫`) | — |
| Convexity `ConvexOn`, inner-product spaces, `iteratedFDeriv`/Hessian | **present** | `Analysis.Convex.Function`, `Analysis.InnerProductSpace.*` |
| `m`-strong convexity ⇔ `∇²U ⪰ mI` (packaged) | **absent** | — |
| **Poincaré inequality** (statement + Gaussian instance) | **absent** | — |
| **Log-Sobolev inequality** | **absent** | — |
| Bakry–Émery Γ / Γ₂ carré-du-champ, curvature criterion | **absent** | — |
| Brascamp–Lieb inequality | **absent in Mathlib** (Numina has a ~8k-line formalization) | — |
| `W₂` Wasserstein metric / optimal transport, Otto–Villani `⇒ T₂` | **absent / very partial** | — |
| Ornstein–Uhlenbeck semigroup, Hermite polynomials | **absent** | — |
| Brownian motion / SL flow | **early** (late-2025 preprint formalization) | (arXiv:2511.20118) |

**Headline.** The *measure-theoretic substrate* is in good shape (Gaussians, products,
variance, independence, KL). The *functional-inequality layer itself* — Poincaré, LSI, the
entropy and Dirichlet functionals, Bakry–Émery, Otto–Villani — is essentially **greenfield**.
The first deliverable is therefore to define the FI vocabulary and prove the three spine
theorems, contributing the reusable definitions upstream. Each spine node certifies a named
manuscript `\label` / ledger node (the cross-reference column in §2–§3, summarized in §5).

---

## 2. Gaussian Poincaré

**Certifies.** `fam:gaussian-covariance` (Part I Tier 1, `modules/03-tier1-gaussian.tex`) and the
Gaussian half of `thm:glm-fi`.

**Target.** `Var_{N(0,Σ)}(f) ≤ ‖Σ‖_op · ∫ ‖∇f‖² dN(0,Σ)`; in particular `C_P = ‖Σ‖_op`,
sharp (linear `f`).

**Present.**
- `gaussianReal μ v` (1D) and the general `IsGaussian` predicate with closure under linear
  maps, convolution, products, and the characteristic-function characterization
  (`charFunDual`). Enough to *talk about* `N(0,Σ)` abstractly.
- `ProbabilityTheory.variance` and integration (`MeasureTheory.integral`).
- `fderiv` / `gradient` for the `∫‖∇f‖²` right-hand side.

**Missing.**
- A **finite-dimensional `N(0,Σ)` with an explicit covariance matrix** and the operator
  norm `‖Σ‖_op`. `IsGaussian` is abstract (Banach, via dual char. functions); there is no
  API exposing `Σ : Matrix` / `‖Σ‖_op` for the constant.
- The **Dirichlet energy** `∫‖∇f‖² dμ` as a named quantity (assemble from `gradient`+`∫`).
- The **Poincaré inequality statement** itself (a `Prop` `HasPoincaré μ C`), plus the
  Gaussian **instance** and its sharpness witness (the manuscript's `rem:rayleigh-lower-only`,
  numerically the `finum` linear-test refuter `lem:linear-test-lower`).
- Cleanest route to the proof — the **Ornstein–Uhlenbeck semigroup** + spectral
  gap, or **Hermite** expansion — neither is in Mathlib.

**Effort.** Medium. The definitions are small; the proof either ports a self-contained
1D + tensorization argument (needs §3) or builds a minimal OU semigroup. Recommended:
prove **1D standard Gaussian Poincaré** first, then lift to `N(0,Σ)` by linear change of
variables + §3 tensorization.

---

## 3. Tensorization

**Certifies.** `thm:tensorization` (`modules/02-results-toolkit.tex`) — the toolkit lemma that
makes the whole Part I difficulty gradation compositional.

**Target.** For a product `μ = ⊗_i μ_i`, `C_P(μ) = max_i C_P(μ_i)` (and the same for LSI).

**Present (the key building block already exists).**
- `MeasureTheory.Measure.pi` (finite products) and `Probability.Independence.Basic`.
- **`variance_sum_pi`**: `variance (∑ i, X i ∘ proj i) (Measure.pi μ) = ∑ i, variance (X i) (μ i)`
  and `IndepFun.variance_sum`. This is exactly the additivity that powers the tensorization
  of the Dirichlet form.

**Missing.**
- The **conditional-variance / Efron–Stein decomposition** `Var_μ(f) ≤ ∑_i E[Var_i(f)]`
  for a general (non-linear) `f` on a product — the actual engine of FI tensorization
  (`variance_sum_pi` only covers separable sums `∑_i X_i`).
- The **tensorization theorem** for the Poincaré (and LSI) *constant*, i.e. the inequality
  `C_P(⊗μ_i) ≤ max_i C_P(μ_i)`, which needs §2's `HasPoincaré` predicate plus the
  conditional decomposition.
- Entropy subadditivity (`Ent_{⊗μ}(f) ≤ ∑_i E[Ent_i(f)]`) for the LSI version — needs the
  entropy functional (absent — see the entropy row of §1).

**Effort.** Medium, and it is the **highest-leverage** node: once `HasPoincaré`/`HasLSI`
predicates and the conditional decomposition exist, tensorization is the lemma that makes
the whole spine compositional. Depends on §2 for the predicate.

---

## 4. Bakry–Émery (and Holley–Stroock, Otto–Villani)

**Certifies.** `thm:bakry-emery`, `thm:holley-stroock`, `thm:otto-villani`
(`modules/02-results-toolkit.tex`) and the flagship Part I baseline `thm:glm-fi`
(`modules/05-tier3-glm.tex`): Gaussian prior ⇒ `C_P ≤ C_LS ≤ λmax(Σ₀)`.

**Target.** `∇²U ⪰ mI` (`m>0`) ⇒ `μ ∝ e^{-U}` satisfies Poincaré and LSI with
`C_P ≤ C_LS ≤ 1/m`; and (Otto–Villani) LSI ⇒ `T₂` with `C_TCI ≤ C_LS`.

**Present.**
- `ConvexOn`, `StrictConvexOn`; inner-product spaces; `iteratedFDeriv` / second derivatives;
  positive-definiteness of matrices (`Matrix.PosDef`). The ingredients of "`∇²U ⪰ mI`".
- `klDiv` / `llr` for the relative-entropy side of `T₂`.

**Missing.**
- The packaged equivalence **`m`-strong convexity ⇔ `∇²U ⪰ mI`** for `C²` potentials on
  `ℝⁿ` (Mathlib has convexity and Hessians but not this bridge as a reusable lemma).
- The **carré-du-champ** `Γ(f) = ½(L f² − 2fLf)` and **`Γ₂`**, the generator `L` of the
  weighted diffusion, and the **`CD(m,∞)` curvature criterion** — none of the Bakry–Émery
  Γ-calculus exists in Mathlib.
- **Otto–Villani** and the whole transport side: there is **no general `W₂` Wasserstein
  metric / optimal-transport** development in Mathlib (only partial Kantorovich-duality
  pieces), so `T₂` and `LSI ⇒ T₂` are out of reach without building optimal transport
  first.

**Effort.** High for the full criterion via Γ-calculus. **Pragmatic shortcut:** for the
*statistically relevant* case the project actually needs (`thm:glm-fi`: Gaussian prior ⇒
`∇²U ⪰ Σ_0^{-1} ⪰ ‖Σ_0‖_op^{-1} I`), one only needs **strong-convexity ⇒ Poincaré/LSI**,
which can be obtained from §2 (Gaussian) + a Holley–Stroock (`thm:holley-stroock`) /
Brascamp–Lieb (`thm:brascamp-lieb`) comparison rather than the full CD criterion. Defer
Otto–Villani / `T₂` until optimal transport lands.

---

## 5. First Lean targets — the gap mapped to *proved* nodes

You can only Lean-certify a node that already has a crisp statement and a Phase-2 (or
imported/proved) argument. The **formalization-ready nodes today** — `status ∈
{proved, imported}` in `research/ledger.yaml` — and the spine prerequisites that gate each
`solutions/<id>.lean`:

| Ledger node (`\label`) | Statement | Gated by | First-target effort |
|---|---|---|---|
| `lem:linear-test-lower` | `C_P(π) ≥ λmax(Cov_π)` (the universal sound refuter; mirrors `finum.constants.poincare_lower`) | §2 vocabulary (`HasPoincaré`, Dirichlet energy) only | **low** — pure variational lower bound, no Gaussian machinery |
| `thm:glm-fi` | Gaussian prior ⇒ `C_P ≤ C_LS ≤ λmax(Σ₀)`, `C_TCI ≤ λmax(Σ₀)` | §2 + §4 strong-convexity shortcut (`+ thm:holley-stroock`) | medium |
| `thm:a5-monotone` | quotient constants never worse: `C_P(π/G) ≤ C_P(π)` | §2 vocabulary + Lipschitz-transport contraction | medium |
| `prop:a5-ratio` | quotient improvement ratio `= λ_inv / min(λ_inv, λ_noninv)` | `thm:a5-monotone` | medium |
| `lem:a5-lipschitz` | `T_#ν = μ`, `T` `L`-Lipschitz ⇒ `C_P(μ) ≤ L² C_P(ν)` (same for LS, TCI) | §2 vocabulary; change-of-variables on the Dirichlet form | **low** |
| `thm:hardy-1d` *(imported)* | 1D weighted Hardy/Muckenhoupt criterion (constant up to factor 4) | 1D measure theory; no FI vocabulary needed | medium (self-contained) |
| `thm:a3-student` *(imported)* | sharp weighted Poincaré for generalized Cauchy / Student-t | `thm:hardy-1d` + radial reduction | high |

**Recommended first PR:** `lem:linear-test-lower` and `lem:a5-lipschitz` — both need only the §2
vocabulary (`HasPoincaré μ C`, the Dirichlet energy) and elementary arguments, so they pay for
the foundational definitions while producing two `checked_by: lean` nodes. `thm:glm-fi` (the
manuscript flagship) is the headline target and the natural §4 deliverable.

Recommended **upstreaming order** (each builds on the previous), independent of which node it
certifies:

1. **FI vocabulary** — `HasPoincaré μ C`, `HasLSI μ C`, the entropy functional `Ent_μ`, the
   Dirichlet energy. Small, foundational, reusable. *(prereq for everything; unblocks
   `lem:linear-test-lower`, `lem:a5-lipschitz`)*
2. **1D Gaussian Poincaré** (and LSI), with the sharp constant. *(needs 1; OU or direct)*
3. **Tensorization** of `C_P` / `C_LS` over products. *(needs 1–2 + conditional decomposition;
   certifies `thm:tensorization`)*
4. **`N(0,Σ)` Poincaré** `C_P = ‖Σ‖_op` by change of variables + 3. *(needs covariance-matrix
   API; certifies `fam:gaussian-covariance`)*
5. **Strong-convexity ⇒ Poincaré/LSI** in the form `thm:glm-fi` needs (`∇²U ⪰ mI ⇒ 1/m`),
   via Gaussian comparison — *not* the full Γ-calculus. *(needs 2–4; certifies `thm:glm-fi`)*

Explicitly **deferred** (do not promise; keep these nodes off the `checked_by: lean` ladder
until the prerequisites land): the full Bakry–Émery Γ₂ / `CD(m,∞)` criterion; Otto–Villani /
`T₂` (blocked on optimal transport); Brascamp–Lieb (`thm:brascamp-lieb` — integrate Numina's
formalization rather than re-prove); and the KLS-only primitives of §6.

This staircase is the honest minimal spine: steps 1–5 are a realistic 12–18-month
upstream-contribution target; the deferred list is where the Lean-agent track should be
*scoped out*, not promised.

---

## 6. KLS-backbone primitives (Part III)

Part III (`modules/kls/`, ledger `research/kls/ledger.yaml`,
`program: kls`) is a route-spanning **proof program**. Its Eldan stochastic-localization
backbone is in the proof phase, while the deterministic CMH route has only open internal nodes.
The 41 legacy nodes marked `proved` predate the current standalone-dossier metadata contract and
carry an explicit certification debt. Lean certification is a *separate, heavier* front: beyond
the FI spine above it needs stochastic calculus, geometric measure theory, and
Brascamp–Lieb. Below, the primitives are derived from the **actual proved/imported ledger nodes**
(not an external blueprint), with the Mathlib status of each.

| Primitive (Mathlib need) | KLS ledger nodes that need it | Status |
|---|---|---|
| Itô calculus, **matrix-valued** SDEs, quadratic variation (the localization SDE) | `lem:matrix-riccati`, `thm:scalar-riccati`, `cor:per-direction` | **absent** (Brownian motion only, late-2025 preprint) |
| Martingales, supermartingales, optional stopping, Gronwall on stopped processes | `lem:perimeter-martingale`, `lem:inf-martingales`, `thm:carleson-implies-centroid`, `ass:stopped-centroid` | **partial** (martingale basics present) |
| PSD / Loewner order, `λmax`, spectral theorem, whitening | `cor:per-direction`, `lem:whitening`, `prop:gaussian-model` (pervasive) | **present**, scattered (`Matrix.PosDef`, `Analysis.InnerProductSpace.Spectrum`) |
| Hilbert–Schmidt / Frobenius norm, trace (Stein-trace estimates) | `prop:stein-rep`, `lem:stein-vs-source`, `prop:intro-audit` | **present** |
| Brascamp–Lieb (pathwise source bound) | `lem:pathwise-BL`, `cor:away-from-zero` | **absent in Mathlib** (Numina ~8k-line formalization → integration target; = `thm:brascamp-lieb`) |
| Bakry–Émery / curvature criterion | shared with the FI spine (§4) | **absent** (= §4) |
| Carbery–Wright anti-concentration | `def:qcts`, `prop:qcts-equivalence` | **absent** |
| Isoperimetric profile of log-concave measures + concavity; weighted Reilly; boundary representation | `lem:half`, `lem:profile-bound`, `prop:reilly`, `lem:boundary-rep`, `prop:second-variation` | **absent** |
| Finite-perimeter sets, coarea, divergence theorem on weighted manifolds (GMT) | `prop:reilly`, `lem:perimeter-martingale`, `lem:boundary-rep` | **mostly absent** (geometric-measure-theory gap) |
| Klartag–Lehec covariance window | `thm:KL-window`, `hyp:KI`, `rem:kl-window-verified`, `cor:KI-discharged`, `thm:V2-window` | **absent** (literature import) |

The KLS backbone and the FI spine **share** the PSD/trace primitives and the
`IsGaussian`/product substrate; they **diverge** in that KLS additionally needs stochastic
calculus (the Riccati SDE), GMT (the Reilly/boundary machinery), and Brascamp–Lieb. The single
most reusable cross-cutting contribution is therefore the **FI vocabulary itself**
(`HasPoincaré`, `HasLSI`, the entropy and Dirichlet functionals) — it underpins both fronts, and
it is the same vocabulary that backs the Part II ↔ Part III bridge `ab/conj:a1-bis →
kls/conj:kls` (the `C_P ≤ K·λmax(Cov)` shadow of KLS; `research/kls/shared/target.md`).

Note the epistemic asymmetry: many headline KLS nodes are `conditional` (e.g.
`thm:intro-all-cut`, `thm:centroid-implies-kls`), resting on `open` assumptions
(`ass:all-cut-carleson`, `ass:stopped-centroid`). A `conditional` theorem can be Lean-certified
*as a conditional implication* (the hypothesis becomes a Lean argument), but the node only
reaches unconditional `proved` once its assumption is discharged — a distinction `check_ledger.py`
already enforces (`no proved-on-open`).

---

## Sources

- [Mathlib.Probability.Distributions.Gaussian.Basic](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Distributions/Gaussian/Basic.html) · [.Real](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Distributions/Gaussian/Real.html)
- [Mathlib.Probability.Moments.Variance](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Moments/Variance.html) (`variance_sum_pi`)
- [Mathlib.MeasureTheory.Constructions.Pi](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Constructions/Pi.html) · [Mathlib.Probability.Independence.Basic](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Independence/Basic.html)
- [Mathlib.InformationTheory.KullbackLeibler.Basic](https://leanprover-community.github.io/mathlib4_docs/Mathlib/InformationTheory/KullbackLeibler/Basic.html)
- [Mathlib.Analysis.Convex.Function](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Convex/Function.html) · [Mathlib.Analysis.InnerProductSpace.Defs](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/Defs.html)
- [Basic probability in Mathlib (community blog)](https://leanprover-community.github.io/blog/posts/basic-probability-in-mathlib/)
- [Formalization of Brownian motion in Lean (arXiv:2511.20118)](https://arxiv.org/html/2511.20118v1)

---

*Companion documents: [`research/README.md`](research/README.md) (the two-phase control plane),
[`solutions/README.md`](solutions/README.md) (the `checked_by` proof ladder),
[`experiments/README.md`](experiments/README.md) (the `finum` numerical channel).*
