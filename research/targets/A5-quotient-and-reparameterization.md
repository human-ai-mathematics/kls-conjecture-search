# A5 — Quotient and reparameterization constants

- **Ledger:** `thm:a5-monotone` (proved), seven independently agent-certified spectral/
  reparameterization refinements, `conj:a5-metastable` (+ `q:a5-*`, open) · **Manuscript:**
  `A5-quotient-and-reparameterization.tex` (`sec:a5`)
- **Status:** mixed: monotonicity and seven spectral/reparameterization nodes are certified;
  metastability remains open · **Evidence:** none
- **Review records:** [`../reviews/2026-08-21-a4-a5-independent-agent-audit.md`](../reviews/2026-08-21-a4-a5-independent-agent-audit.md), [`../reviews/2026-08-21-a5-funnel-second-agent-audit.md`](../reviews/2026-08-21-a5-funnel-second-agent-audit.md)
- The escape hatch the other targets invoke (separates symmetry artifacts from physical structure).

## Goal (current best statements)

**R2-certified anchor:** monotonicity `C_P(π/G) ≤ C_P(π)` (`thm:a5-monotone`).

**Independently agent-certified:** with extended reciprocals,
`C_P(π/G)=1/λ_inv` and
`C_P(π)=1/min(λ_inv,λ_noninv)`; only when `0<λ_inv<∞` is the ordinary ratio
`C_P(π)/C_P(π/G) = λ_inv/min(λ_inv,λ_noninv)` invoked (`prop:a5-ratio`; solution
[`prop-a5-ratio.tex`](../../solutions/prop-a5-ratio.tex)).

All symmetry claims assume that **both prior and likelihood** are `G`-invariant. An exchangeable
prior alone does not make the posterior invariant.

**Open (`conj:a5-metastable`):**
```
n⁻¹ log C_P(π_Θ) →ᴾ Γ_conn                        (raw — connectivity-barrier law)
C_P(π_{Θ/S_K}) = (1+o_P(1))/n · λmax(I(θ_*)⁻¹)    (quotient — A2 re-emerges)
```

## Obstruction it must respect

- `obs:symmetry-vs-physical` — when `0<λ_inv<∞`, strict gain holds iff
  `λ_noninv < λ_inv`; equality/degeneracy gives no strict improvement even when non-invariant
  first eigenfunctions exist. At `λ_inv=0`, both quotient and raw constants are infinite and an
  ordinary ratio is not defined.
- `obs:heavy-tail-no-classical` — the centered Neal funnel and genuinely heavy-tailed scale priors
  can have no finite Euclidean Poincaré constant; this is a tail/reparameterization obstruction,
  not a symmetry obstruction.

## Analytic refinement (2026-08-21)

See
[`2026-08-21-a5-quotient-reparameterization-audit.md`](../explorations/2026-08-21-a5-quotient-reparameterization-audit.md)
and the next-cycle analysis
[`2026-08-21-a5-connectivity-partial-next-cycle.md`](../explorations/2026-08-21-a5-connectivity-partial-next-cycle.md).

**Quotient-gap identity (independently agent-certified):** the manuscript decomposition
argument gives that, when
`0<λ_inv<∞`, strict improvement occurs exactly when
$\lambda_{\mathrm{noninv}}<\lambda_{\mathrm{inv}}$. At equality, both representation types may
occur in the first eigenspace but the quotient constant is unchanged. Detection should therefore
estimate the two restricted gaps by group-projecting a symmetry-closed Ritz basis; classifying a
single fitted eigenfunction is ill-posed under degeneracy. See
[`prop-a5-ratio.tex`](../../solutions/prop-a5-ratio.tex).

**Invariant-block stability (independently agent-certified):** if two $G$-invariant laws
$\pi,\widetilde\pi$ obey
$\operatorname{osc}\log(d\widetilde\pi/d\pi)\le\varepsilon$, then for
$b\in\{\mathrm{inv},\mathrm{noninv}\}$,

$$
e^{-\varepsilon}\lambda_b(\pi)
\le\lambda_b(\widetilde\pi)
\le e^{\varepsilon}\lambda_b(\pi).
$$

The group-average projection defines the same two function spaces for both invariant measures.
A block ordering is stable when its log-gap margin exceeds $2\varepsilon$; stability of individual
eigenvectors still needs an isolated eigenvalue (`prop:a5-block-stability`; solution
[`prop-a5-block-stability.tex`](../../solutions/prop-a5-block-stability.tex)).

**Folded-well analytic proof draft (pending repository certification):** if
$\bar\mu_a=|\cdot|_\#[\tfrac12N(-a,\sigma^2)+\tfrac12N(a,\sigma^2)]$, then
$\bar\mu_a=\operatorname{Law}|a+\sigma Z|$ is a $\sigma$-Lipschitz Gaussian image. Hence

$$
C_P(\bar\mu_a),\ C_{\mathrm{LS}}(\bar\mu_a),\ C_{\mathrm{TCI}}(\bar\mu_a)\le\sigma^2,
\qquad C_P(\bar\mu_a)\to\sigma^2
$$

as $a/\sigma\to\infty$.
For the raw mixture, the dimensionless logarithmic statement is

$$
\log\!\frac{C_P(\mu_a)}{\sigma^2}
=\frac{a^2}{2\sigma^2}+O\!\left(\log\!\left(1+\frac a\sigma\right)\right).
$$

The error term keeps the polynomial prefactor visible; the current finite-element sweep does not
identify that prefactor.

**Reparameterization well-posedness:** a dilation by $a$ multiplies each raw constant by $a^2$,
so minimizing $C_P$ over coordinates is meaningless without normalization. Track the
scale-invariant objective $\kappa_P=L_VC_P$ (when $\nabla V$ is globally $L_V$-Lipschitz) and/or
bi-Lipschitz distortion. For a Gaussian, $\kappa_P=\operatorname{cond}(\Sigma)$ and whitening is
optimal.

**Exact entry model (independently agent-certified):** in the unit
Gaussian hierarchy
$u,z\sim N(0,1)$, $\theta=u+z$, $y\mid\theta\sim N(\theta,r^{-1})$, the centered and non-centered
posterior precisions are

$$
H_c=\begin{pmatrix}2&-1\\-1&1+r\end{pmatrix},\qquad
H_{nc}=\begin{pmatrix}1+r&r\\r&1+r\end{pmatrix}.
$$

Direct diagonalization predicts that both $C_P$ and $\kappa_P$ favor non-centering for $r<1$, are
equal at $r=1$, and favor centering for $r>1$. This phase diagram should precede nonlinear funnel
bounds; see
[`ex-a5-gaussian-crossover.tex`](../../solutions/ex-a5-gaussian-crossover.tex).

**Optimal scalar partial noncentring (independently agent-certified):** for
$u\sim N(0,A)$, $\theta\mid u\sim N(u,B)$ and Gaussian likelihood precision $r$, the coordinate
$z_\alpha=\theta-\alpha u$ has a $2\times2$ precision of constant determinant. Minimizing its
trace therefore minimizes both $C_P$ and $\kappa_P$, with the unique solution

$$
\alpha_*=\frac{1}{1+rB}.
$$

The prior variance $A$ changes the attained objective but not the optimizer
(`prop:a5-partial-gaussian`; solution
[`prop-a5-partial-gaussian.tex`](../../solutions/prop-a5-partial-gaussian.tex)).

**Funnel and partial-funnel results (independently second-audited):** for the canonical model with
$s>0$, the Neal map and its inverse are both non-Lipschitz globally. The retired diagnostic's
“one-way Lipschitz” note was incorrect; the correction is preserved in the
[`2026-08-21 A5 audit`](../explorations/2026-08-21-a5-quotient-reparameterization-audit.md). Its finite variance lower bounds do not
numerically prove $C_P=\infty$ for fixed $s$; infinity follows analytically from the absence of
exponential moments in the centered coordinate together with an explicit truncation proof that
Poincaré implies a small exponential moment. In particular,
`Var(θ_j)=exp(2s²)` is finite for every fixed `s`; it is only a finite lower witness.

For partial Neal coordinates $z_\alpha=e^{-\alpha u}\theta=e^{(1-\alpha)u}z$,
every $0\le\alpha<1$ still has a lognormal-type coordinate with no exponential moment, hence
$C_P=\infty$ in the prior-only Euclidean law. Only $\alpha=1$ is the finite product Gaussian.
This singular phase does not automatically persist after adding a likelihood; that case needs a
separate model-specific tail/Lyapunov proof and remains open.
The independently agent-certified dossiers
[`ex-a5-neal.tex`](../../solutions/ex-a5-neal.tex) and
[`prop-a5-partial-funnel.tex`](../../solutions/prop-a5-partial-funnel.tex) record the complete
arguments and their separate second-audit provenance.

**Exact $\mathbb Z_2$ bridge (analytic proof draft pending certification):** for
$\mu_n=\tfrac12N(-a,\sigma^2/n)+\tfrac12N(a,\sigma^2/n)$,

$$
\frac1n\log C_P(\mu_n)\to\frac{a^2}{2\sigma^2},
\qquad nC_P(|\cdot|_\#\mu_n)\to\sigma^2.
$$

This is a calibration, not a general quotient BvM theorem. Block density-ratio stability transfers
the raw rate under a global oscillation error $o(n)$ and the quotient leading constant under
$o(1)$ (`ex:a5-z2-bridge`).

## Quantitative metastability contract

Let `R(θ)=−E_{θ*} log p_θ(Y)`, `R*=R(θ*)`, and let `W=Gθ*` be a free orbit of nondegenerate
minima. For wells $w,w'$, let $H(w,w')$ be their pairwise communication height. Define

$$
\Gamma_{\rm conn}
=\inf\{h:\ (W,\{ww':H(w,w')\le h\})\text{ is connected}\}
=\max_{\varnothing\ne A\subsetneq W}\min_{w\in A,w'\notin A}H(w,w').
$$

This worst-cut/connectivity height reduces to the easiest pairwise barrier only when the graph of
minimum-height orbit moves is connected (automatically for $\mathbb Z_2$, not for a general
orbit). The finite-graph identity is independently checked; it does not discharge the posterior
metastability conjecture.

The conjecture assumes `Γ_conn>0`, a collision gap
`inf_{dist(θ,C)≤δ}(R(θ)−R*)≥c_col>0`, coercive population tails, a prior with `o(n)` log-density
on the relevant landscape, uniform empirical risk/derivative control implying
`Γ_conn,n→Γ_conn` in `P_{θ*}`-probability, and two-sided capacity bounds with subexponential error. Both the
raw logarithmic law and the quotient Fisher-scale law are convergence-in-probability statements;
polynomial/Eyring–Kramers prefactors are a later target.

## Sub-questions (ledger)

| node | what | difficulty |
|------|------|-----------|
| `q:a5-qbvm` | prove the quotient line (A2 on the orbit space) | bridge to A2 |
| `q:a5-metastable` | first prove `n⁻¹ log C_P → Γ_conn`; prefactor second | hard |
| `q:a5-detect` | from samples, test whether the slow mode is invariant or not | numeric |
| `q:a5-stratified` | `C_LS`/`C_TCI` on stratified/orbifold quotient spaces | hard |
| `q:a5-reparam` | normalized/scale-free centered, non-centered, partial comparison | medium |

## Numerical plan (finum)

1. `stress-folded-well`: estimate raw vs folded `C_P`; inspect
   `log(C_P(raw)/σ²)−a²/(2σ²)` against a possible `O(log(1+a/σ))` correction and check the folded
   estimate against the analytic `≤σ²` bound. Do not compare to a pure exponential prefactor.
2. `q:a5-detect`: estimate the invariant and non-invariant restricted gaps separately by applying
   the group projection to a symmetry-closed test basis. Include residual/two-sided control before
   treating either block as the slower working hypothesis; a single eigenfunction is insufficient
   under degeneracy.
3. `stress-neal-funnel`: report `exp(2s²)` only as the finite linear-test lower witness for the
   centered law, and `max{s²,1}` as the exact non-centered calibration. The centered `C_P=∞`
   conclusion is analytic, not a numerical variance estimate. Separate a half-Cauchy heavy-tail
   obstruction from the canonical Gaussian-log-scale funnel geometry.
4. Reparameterization calibration: reproduce the exact Gaussian-hierarchy crossover at normalized
   data precision `r=1`, then check $\alpha_*=1/(1+rB)$ numerically for unequal scales before
   moving to nonlinear funnels. Report both `C_P` and `κ_P=L_V C_P`.
5. Sanity/calibration: estimated quotient `C_P ≤ raw C_P`; folded-well estimates must also obey
   the analytic proof-draft upper bound `C_P ≤ σ²`.

**Research use only:** separation and resolution sweeps, polynomial-correction checks, and
two-block spectral diagnostics are directional tools for refining the conjectured logarithmic rate
and finding possible failure modes. They do not validate or certify the rate or any proof, even
when error-controlled; finite lower witnesses remain research diagnostics. Rigorous refutation
still requires an analytic argument or exact lower bound.

## Numerical research log

_(none yet)_

## Cross-links

- `conj:a5-metastable` quotient line = `conj:a2` `eq:a2-target`; supplies the escape for A2
  `q:a2-multimodal` and A4 `q:a4-multimodal`. The funnel half is bounded by
  `obs:heavy-tail-no-classical` and shares A3's tail-integrability concerns.
