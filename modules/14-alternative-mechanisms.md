---
numbering:
  enumerator: "14.%s"
---

(sec:frontier-atlas)=
# Alternative mechanisms after KLS

The three proofs of KLS (Chapter [](#sec:kls-synthesis)) obtain a universal constant through estimates on polynomials of every degree. This part develops three further mechanisms, each through a sufficient condition of its own: the moment-Hessian inequality, an occupation estimate for one eigenfunction, a gap for resampling along lines. Each condition implies KLS, and no converse is known. Proved, each would give a further proof together with something the three proofs do not provide: a constant, an object followed, or a kind of argument. A fourth method, the fixed cut, is kept as an archive for what its obstructions teach. This chapter compares the four; the obstacles they face are explained in Section [](#sec:kls-remaining).

(subsec:atlas-approaches)=
## The mechanisms, side by side

**What each would add.** The moment map has an implication towards KLS that loses no constant, exact values on the line and on products, and the sharp bound $4$ on Dirichlet laws; it would give a deterministic proof, with no stochastic localization, and the constant $4$, which the exponential on the line attains (Section [](#subsec:after-constant-question)). The fixed eigenfunction would give a localization mechanism that ignores covariance spikes in directions the eigenfunction does not use. Conditional fibers would give an elementary mechanism whose only analytic input is one-dimensional. The order is that of what each has established; it is not a forecast.

| Mechanism | Object retained | The idea in one line | What it would add to the three proofs | Chapter |
|---|---|---|---|---|
| Moment map | Hessian metric of the moment map, Haar fields, Schur fibers | Prove one deterministic inequality for the moment-map Hessian, $\mathrm{CMH}(4)$, which bounds the affine Poincaré constant with no loss ([](#thm:cmh-implies-affine-poincare)) | A deterministic proof with the constant $4$; its linear test has a sharp form with constant $2$, [](#conj:gate-zero-sharp) | [](#sec:moment-map-cmh) |
| Fixed eigenfunction | Covariance tensor of a first spectral mode | Follow a first eigenfunction through stochastic localization; one occupation estimate, [](#conj:mm-spectral-occupation), then gives KLS ([](#prop:spectral-sufficiency)) | A localization mechanism blind to covariance spikes that the eigenfunction does not see | [](#sec:spectral-approach) |
| Conditional fibers | One isotropic frame of line resamplings, chosen from the measure before the test function | A dimension-free gap for the resampling form, [](#conj:conditional-fiber-frame), gives KLS with constant $4C$ ([](#lem:conditional-fiber-form)) | A mechanism using only one-dimensional log-concave inequalities and a choice of directions | [](#sec:conditional-fiber-frame) |
| Fixed cut (archive) | Mass and two-color covariance of one prospective bottleneck set | Follow one balanced set through stochastic localization; KLS follows if it cannot be identified before a universal time ([](#lem:survival-implies-kls)) | Kept for its results, which are obstructions and a ceiling | [](#sec:introduction) |

(subsec:synthesis-constraint)=
## The constraint every mechanism must meet

The covariance spike ([](#prop:covariance-spike), explained in Section [](#subsec:kls-spike-obstruction)) cuts in two directions. A direct “bound $\norm{A_t}_\op$ better” approach cannot work, since the statement it needs is false; and rare spikes can be harmless, so a successful potential must recognize them rather than charge the full top eigenvalue whenever one occurs. The working criterion is the tensorization test of Section [](#subsec:kls-tensorization-test): evaluate the proposed quantity on a product of independent copies, and reject it if it charges $n$ independent coordinates $n$ times. It is the first thing to check on each direction below.

(subsec:atlas-state)=
## What each mechanism gives, and what blocks it

The table above says what each mechanism *tries*; this one says where each has got to. The middle column is the mechanism's own contribution, the right column the statement whose absence stops it; the full account of both is the opening summary of each entry chapter.

| Mechanism | What it gives | What blocks it |
|---|---|---|
| Moment map | The target inequality given precise operator data ([](#def:cmh)) and compared with the affine Poincaré constant ([](#thm:cmh-implies-affine-poincare)); exact values on the line and on products, and the bound $4$, sharp over the family, on every log-concave Dirichlet law; the linear sector resolved into a directional third moment ([](#lem:linear-sector-third-moment)), with the exponential cones as its first non-product equality set | Constructing the proof: the invariant multiplier lift ([](#conj:mm-invariant-lift)) — how a multiplier defined on one block of a Schur split acts on the whole space — and the global square-root commutator ([](#conj:mm-square-root-commutator)). Testing it: the linear test ([](#conj:gate-zero), sharp form [](#conj:gate-zero-sharp)) and the second variation at the product ([](#conj:cmh-second-variation)) |
| Fixed eigenfunction | The exact fixed-function equation and the stopped source estimate [](#lem:mm-stopped-window-source) | Source occupation on a universal time interval, [](#conj:mm-spectral-occupation); the small-gap implication [](#prop:mm-window-occupation) applies to no measure (Section [](#subsec:spectral-window-chain)) |
| Conditional fibers | The resampling form, closed and compared with the gradient ([](#lem:conditional-fiber-form)); the natural simplex frame ruled out ([](#prop:conditional-fiber-root-obstruction)) | A universal form gap, [](#conj:conditional-fiber-frame), or a decision on the all-frame simplex problem using growing-degree or nonpolynomial tests; every fixed polynomial degree has a uniform positive floor ([](#lem:fiber-polynomial-floor)) |
| Fixed cut (archive) | The bootstrap comparison and its interface functional ([](#thm:bootstrap)), the insufficiency of the crude evaluation ([](#rem:crude-insufficient)) and the ceiling [](#prop:ceiling); the coordinate budgets of the product stress test (Chapter [](#sec:product-stress)) | For the all-cut variant, the operator-to-trace upgrade [](#conj:trace-upgrade); for the near-Cheeger variant, a tensor-stable replacement for the weighted package that [](#prop:weighted-spectator-obstruction) rules out |

(subsec:atlas-moment-map-direction)=
## The moment map: from fixed matrices to a nonlinear estimate

Brascamp–Lieb in moment-map coordinates already gives [](#eq:mm-brascamp-lieb), so KLS would follow from

```{math}
:label: eq:nonlinear-moment-map
\E\inner{\tau_\mu\nabla f}{\nabla f}\lesssim\E\abs{\nabla f}^2 .
```

The identity $\E\tau_\mu=I$ is insufficient, because $\tau_\mu(X)$ may correlate with $\nabla f(X)$. Letwin's fixed-matrix inequality controls a deterministic matrix $B$; an extension of this kind would need to handle an $X$-dependent direction or matrix field.

The moment-map chapters (Chapter [](#sec:moment-map-cmh)) pursue a precise form of this idea: the inequality $\mathrm{CMH}(4)$ ([](#def:cmh)), which bounds the affine Poincaré constant by [](#thm:cmh-implies-affine-poincare). Two facts developed there change how the extension should be read. $\mathrm{CMH}(4)$ also charges a solenoidal excess, so it is a sufficient condition rather than a known reformulation of [](#eq:nonlinear-moment-map) (Chapter [](#sec:moment-map-cmh)). And its cheapest necessary consequence, the linear test of Section [](#subsec:gate-zero) ([](#conj:gate-zero)), is itself an average-versus-uniform statement, which [](#prop:letwin-not-gate-zero) shows no fixed-matrix argument supplies: the moment map relocates the difficulty rather than escaping it. How hard even the linear test is, [](#cor:gate-zero-third-moment) calibrates: its sharp form implies $\kappa_n\le2$, so proving it is at least as hard as a sharp directional third-moment bound.

% Agent note: Route C is tracked by the `ap:c-…` approaches of research/program/portfolio.yaml.

(subsec:atlas-function-adapted)=
## The fixed eigenfunction: localization adapted to one function

For a fixed test function set $M_t(f)=\E_{p_t}f$, so that

```{math}
:label: eq:function-adapted-sde
\dd M_t(f)=\Cov_{p_t}(X,f)\cdot\dd W_t .
```

A covariance-based estimate bounds the integrand by the worst case,

```{math}
:label: eq:worst-case-step
\abs{\Cov_{p_t}(X,f)}^2\le\norm{A_t}_\op\Var_{p_t}f ,
```

which discards essentially all information about $f$. A direct estimate of

```{math}
:label: eq:function-adapted-occupation
\int\frac{\abs{\Cov_{p_t}(X,f)}^2}{\Var_{p_t}f}\dd t
```

for a near-extremizing eigenfunction would avoid the top-eigenvalue entropy cost of [](#eq:logtraceexp) and would respect tensorization, since [](#eq:function-adapted-occupation) factorizes over independent blocks in a way that $\norm{A_t}_\op$ does not.

This is exactly [](#conj:mm-spectral-occupation), the central problem of the fixed-eigenfunction chapter (Chapter [](#sec:spectral-approach)). Its analogue for a fixed cut is [](#conj:trace-upgrade), the operator-to-trace upgrade of Chapter [](#sec:open).

(subsec:atlas-coupling-beyond-tilts)=
## A further direction: parallel coupling beyond linear tilts

Parallel coupling, the tool behind the thin-shell theorem, controls the finite-dimensional family of exponential tilts $e^{\inner\theta x}\mu(\dd x)$ (Chapter [](#sec:family-coupling)). A coupling for perturbations $(1+\eps f)\mu$, with cost controlled by $\int\abs{\nabla f}^2\dd\mu$, would address arbitrary spectral directions directly rather than one linear family. No statement of this manuscript formulates such an extension, and none of the mechanisms above carries it.

% Agent note: this direction has no ledger node and no portfolio approach.

(subsec:atlas-barriers)=
## What is already ruled out

Negative results are the most reusable part of a search, and four of them constrain everything above. Each is stated and explained in its own section; they are collected here so that a reader does not rediscover a dead variant.

- **No uniform operator-norm covariance bound.** [](#prop:covariance-spike): the statement a direct “bound $\norm{A_t}_\op$ better” approach would need is false, for a measure that satisfies KLS (Section [](#subsec:kls-spike-obstruction)).

- **Independent spectators and global covariance weights.** [](#prop:weighted-spectator-obstruction) supplies the product-cylinder witnesses relevant to [](#ass:weighted-package) and [](#conj:weighted-excess-rate).

- **No matrix-moment argument supplies the linear test** (Section [](#subsec:gate-zero)). [](#prop:letwin-not-gate-zero): the fixed-matrix estimate does not supply it, so the moment-map mechanism relocates the average-versus-uniform difficulty rather than escaping it.

- **The natural conditional-fiber root frame fails.** The most obvious implementation of the conditional-fiber mechanism is ruled out by [](#prop:conditional-fiber-root-obstruction), which is why the question is stated for all frames, [](#conj:conditional-fiber-frame).

Two further cautions are advisory rather than established: the two-tail obstruction ([](#rem:two-tail-slice-bounds)) and the circularity warning of Section [](#sec:excess). They are recorded as remarks for exactly that reason: they guide work, but no statement here is excluded on their strength.

(subsec:atlas-assessment)=
## What the three proofs contribute to each mechanism

For each mechanism, the table records what the three proofs contribute towards its sufficient condition, and what remains to be proved.

| Mechanism | What the three proofs contribute | What remains to be proved |
|---|---|---|
| Moment map | KLS with a universal constant, evaluated explicitly by Balasubramanian–Kasiviswanathan ([](#thm:bk-explicit-poincare)); no corresponding bound on the moment-map Hessian | The value $4$: universal $\mathrm{CMH}(4)$, its sharp linear test [](#conj:gate-zero-sharp), and the commutator [](#conj:mm-square-root-commutator) |
| Fixed eigenfunction | A first eigenfunction followed through deterministic spectral comparisons, with polynomial control of centering losses instead of a source estimate along localization | [](#conj:mm-spectral-occupation): the polynomial comparisons do not estimate the stochastic source |
| Conditional fibers | An all-function comparison through polynomial tensors | [](#conj:conditional-fiber-frame): the polynomial comparison constructs no frame, and the root-frame obstruction still applies |

For the archived fixed cut, what remains is [](#conj:trace-upgrade), or a replacement for the weighted package that independent coordinates leave unchanged; [](#prop:weighted-spectator-obstruction) still applies.

(subsec:synthesis-caution)=
## Scope of the quadratic input

Several mechanisms start from Letwin's quadratic estimate [](#thm:letwin-qcts) and its directional consequence [](#prop:letwin-kappa) (sources in Section [](#subsec:mm-audit)). Their limits are precise. The covariance consequence [](#cor:letwin-window) bounds fixed-time moments only up to time $c/\log n$, and Letwin's general bound [](#thm:letwin-kls) depends on the dimension (Chapter [](#sec:family-moment-map)). Neither supplies a universal-time occupation bound, control of orientation, an adaptive matrix estimate or the linear test, and the implications [](#thm:carleson-implies-centroid), [](#thm:centroid-implies-kls) and [](#thm:intro-all-cut) keep their Carleson or centroid hypotheses. The three proofs of KLS use the same input through conversions on polynomials; they do not supply the moment-Hessian inequality, its sharp linear test or the occupation estimate either (Section [](#subsec:atlas-assessment)).

% Agent note: source versions describe provenance; badges and proof links carry verification status. Preserve explicit antecedents and dimension-dependent windows when updating this section. Theorem 1.1 has its own proof link; its time-restricted bridge is separate from the matrix, quadratic, and covariance imports.

(subsec:atlas-external-reading)=
## Suggested external reading order

For a reader coming to the subject rather than to this manuscript: [@KannanLovaszSimonovits1995] for the conjecture and deterministic localization; [@Eldan2013ThinShell] for stochastic localization and the third-moment parameter; [@LeeVempala2018; @LeeVempala2024] for the cleanest entry to the covariance SDE and the set-transfer argument; [@KLnotes] for the best conceptual exposition of localization, filtering, Bochner, and the operator-norm obstruction; [@KlartagLehec2022Polylog] for heat flow, spectral measures, and $H^{-1}$; [@Klartag2023Logarithmic] for improved Lichnerowicz and the published bound; [@Letwin2026QuadraticKLS] for the quadratic input and its localization consequences; [@SongZhang2026IteratedLogKLS] for Song and Zhang's polynomial–curvature iteration, developed in Chapter [](#sec:polynomial-curvature); [@SongZhang2026ConstantKLS] for its second version, by repeated refinement, in Chapter [](#sec:sz-v2-proof); [@BizeulKlartagLehec2026KLS] for cumulants and suspension in Chapter [](#sec:bkl-proof); [@BalasubramanianKasiviswanathan2026KLS] for compatible integration in Chapter [](#sec:bk-proof); and [@KlartagLehec2025ThinShell; @ChenKlartag2026SharpThinShell] for the strongest related tools and the clearest illustration of the quadratic-to-all-functions gap.
