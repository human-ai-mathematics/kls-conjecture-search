---
---
# Archived CMH construction regression models

This is the preserved 2026-08-25 model inventory formerly maintained as
`research/kls/routes/moment-map-cmh/models.md`. The curated shared battery in
`research/knowledge/instances.md` and the numerical channel in `experiments/README.md` are
authoritative for current work.

These are fixed adversarial models, not a menu from which a prover may choose a convenient
subset. They are registered in the shared battery at
[`../knowledge/instances.md`](../knowledge/instances.md).

Since 25 August 2026 the route has a `finum` target, **`cmh-gate-zero`**
(`experiments/finum/targets/cmh_gate_zero.py`), covering the normalization layer only. It
computes the gate-zero ratio
$\lambda_{\max}(\Sigma^{-1/2}\mathbb E[H\Sigma^{-1}H]\Sigma^{-1/2})$ from exact moment
matrices, with floating eigenvalue estimates treated as directional and rational Rayleigh
witnesses checked exactly. It also regression-tests the Dirichlet surplus directionally and the
countermodel sector identities analytically. The construction-layer rows below still have
analytic/reporting status only.

| model | evidence level | detects | does not decide |
|---|---|---|---|
| Gaussian moment map | exact calibration | signs, adjoints, square-root normalization; all commutators vanish | noncommutative shape control |
| aligned product moment maps | analytic calibration | tensorization and commuting multipliers | eigenframe rotation |
| rotated product exponentials | reported; dossier pending | negative individual Haar nodes in the originating calculation | failure of the globally summed inequality |
| Gamma/Laguerre near-extremizers | reported; dossier pending | near-exhaustion of descendant and leaf slack | the exact universal constant in the global bound |
| localized high-frequency product exponential | reported; dossier pending | wrong leading sign for conformal-only reservoir allocation | the coupled conformal/traceless/corrector estimate |
| $45^\circ$ two-exponential projection with one-dimensional child | structural calibration under boundary decay | conditional/scalar channel; the scalar Stein equation forces $S=K$ | Airy mismatch, because $\mathsf D=0$ structurally |
| rotated Gamma--Gaussian | reported; dossier pending | failure of the guessed conservation of $\mathbb E[\operatorname{cof}(T)a\mid z]$ | full tensor Hodge estimate |
| three-exponential projection | exact density/kernel compatibility audit | a genuine canonical-versus-inherited Stein mismatch | universal CMH without reconstructing $K$ |
| **uniform simplex / symmetric Dirichlet** | **exact algebra; theorem** | **the first nonproduct class where CMH is computable; gate-zero anchor $2(m+1)/(m+3)$** | **universal CMH — the family is strictly inside the bound** |
| **asymmetric log-concave Dirichlet $\alpha_i\ge1$** | **exact algebra; theorem** | **whether unequal parameters break the Gamma-row completion (they do not)** | **the nonproduct saturating direction, which is not in this family** |
| **product of one-sided exponentials** | **exact; saturating** | **the endpoint: $C_{\mathrm{CMH}}=4$ with zero slack** | **whether a perturbation raises it — that is `q:cmh-solenoidal-perturbation`** |
| **algebraic $O(m)$ countermodel ($m\ge18$)** | **exact finite-dimensional algebra** | **that Letwin's constant-matrix bound does not imply gate zero; the static commutator is unconstrained by matrix moments** | **anything about genuine moment maps — it satisfies no Monge--Ampère condition** |

## Three-exponential projection

Let $Y_1,Y_2,Y_3$ be independent standard exponentials and

$$
\xi_1=Y_1-Y_3,\qquad \xi_2=Y_2-Y_3,
\qquad m(\xi)=\max(0,-\xi_1,-\xi_2).
$$

The reported density and inherited Stein kernel are

$$
\rho(\xi)=\frac13e^{-\xi_1-\xi_2-3m(\xi)},
$$

$$
S(\xi)=
\begin{pmatrix}
\xi_1+2m+2/3&m+1/3\\
m+1/3&\xi_2+2m+2/3
\end{pmatrix}.
$$

On the positive cone, the exploration reports that $S^{-1}$ fails the Hessian compatibility
equations, so the inherited kernel is not the canonical moment-map kernel: $S-K\not\equiv0$.
The next exact model calculation is to solve for an Airy potential in

$$
K_\lambda=S-\rho^{-1}R^\top D^2\lambda R
$$

under the requirement that $K_\lambda^{-1}$ be a Hessian, with positive-definiteness, global
convexity, interface, boundary, and integrability conditions across the three cones. This is the
preferred nontrivial Hodge regression.

## The normalization-layer models

### Dirichlet and the uniform simplex

For $P\sim\mathrm{Dir}(\alpha)$ with $A=\sum_i\alpha_i$ the moment-map data are exact:
$H=C(p)/A$ with $C(p)=\operatorname{diag}(p)-pp^\top$, and $\Sigma$ as in
`eq:cmh-dirichlet-data`. Every observable is a finite combination of Dirichlet moments
$\mathbb E\prod_iP_i^{k_i}=\prod_i(\alpha_i)_{k_i}/(A)_{\sum k_i}$, so the matrix entries admit
exact rational evaluation. A generalized eigenvalue computed in floating point is still
directional; an uppercase refutation additionally requires an exact rational Rayleigh witness or
an interval-certified lower bound above the claimed ceiling.

**Calibration anchor.** For the uniform simplex $\alpha=(1,\dots,1)$ on $\Delta_{m-1}$
(ambient dimension $n=m-1$), the whitened second moment is
$\mathbb EH^2=\frac{2(m+1)}{m+3}I$, so the gate-zero ratio is $2(m+1)/(m+3)<2$. At $m=2$ this is
the uniform interval and gives exactly $1.2$, which must agree with the one-dimensional channel.
An implementation that misses this anchor has the tangent-space normalization or the
pseudo-inverse convention wrong.

**What it detects.** Whether a nonproduct family can push the gate-zero ratio toward $4$. So far
it cannot: all computed Dirichlet instances sit near $2$, and the theorem shows the whole family
is strictly inside $\mathrm{CMH}(4)$ with surplus $s_A$.

**What it cannot decide.** Universal CMH. The Dirichlet family is *not* where the constant is
attained — by the product formula the saturating direction is products of one-sided exponentials.
A good Dirichlet number is therefore a calibration, not positive evidence, exactly as the gate
discipline below requires.

### The algebraic countermodel

The $O(m)$-invariant family of §13 of
[`2026-08-25-kls-cmh-construction-claim-archive.md`](2026-08-25-kls-cmh-construction-claim-archive.md).
Verified exactly through the
three-sector decomposition rather than by sampling $z$: the vector coefficient is $1+d/m$, the
traceless coefficient is $1+(m-2)/((2m-1)(m+2))$, both below the comparison value, and the scalar
deficit is the perfect square $(a-dt)^2$. This is the route's only *negative* exact model, and
its role is to stop any future argument from treating $[B,H]$ as a lower-order correction.

It is a **fence, not a counterexample to gate zero**: it imposes no Hessian compatibility.
Reporting it as evidence against `conj:gate-zero` would be a category error.

## Gate discipline

- A model that is too commutative to activate a term is a calibration, not positive evidence.
- A negative node does not refute a full-tree statement.
- A model inside the proved classes (line, product, Dirichlet) can no longer *support* the
  headline; it can only detect an implementation error. Positive evidence must come from outside
  those classes.
- A sampled quantity can be directional only unless `finum` supplies the repository-prescribed
  provenance and verdict gates.
- A rigorous analytic model can refute a precise universal form, but the calculation must be
  persisted; a consolidated summary alone is not the dossier.
