---
numbering:
  enumerator: "0.%s"
---

(sec:overview)=
# The Kannan–Lovász–Simonovits frontier

+++ {"part": "abstract"}

The Kannan–Lovász–Simonovits conjecture asks for a dimension-free Poincaré constant, $C_{\mathrm P}\le K\lambda_{\max}(\mathrm{Cov})$, for every log-concave measure; it has been open since 1995. A single logarithm now separates the best available bound from the conjecture, and by July 2026 the sharp radial and homogeneous-quadratic cases had removed every quadratic obstruction to closing it. What survives is not a quadratic-form problem but a uniformity problem: each method controls a fixed object, or an average, where KLS needs control of an object that adapts to the measure or to the extremizing function — and the covariance spike of a product of centered exponentials proves that the most direct repair, a uniform operator-norm covariance bound, is false. This manuscript states that residue precisely, surveys the five strategy families of the literature against it, and develops four live routes that respond to it: fixed-cut and fixed-eigenfunction stochastic localization, a deterministic moment-map programme, and inverse-variance conditional-fiber frames. Each route is given the same entrance — mechanism, bridge to KLS, established inputs, main advance, exact bottleneck, refuted variants, and what would close or reopen it — so that its state can be read without its machinery. Nothing here proves KLS. Every claim is a node of this repository's ledger, whose status — not the prose — says what is established, what is conditional, what rests on an unreviewed preprint, and what is merely hoped for.

+++

(sec:reading-paths)=
## How to read this document

This manuscript is long because it is a research record as well as an exposition. It is meant to be entered at several depths, and only the first of the paths below is meant to be read in full by everyone.

**A twenty-minute overview.** Part I, then the atlas in Section [](#sec:frontier-atlas). That is the conjecture, the frontier, the obstruction that shapes every attempt, and one table per live route giving its advance and its exact blocker. Nothing else is needed to say accurately what this project has and has not done.

**The methods of the literature.** Part II, Sections [](#sec:family-needles) through [](#sec:family-transport), five families in a common format. Each closes by naming the live route it feeds, so the survey can be read either on its own or as the approach to Parts III and IV.

**The stochastic-localization routes.** The prelude, Section [](#sec:localization-prelude), then Route E from Section [](#sec:introduction) or Route S from Section [](#sec:spectral-route). The prelude replaces the full apparatus with what a reader needs to follow the argument; the apparatus itself is Appendices [](#sec:notation)–[](#sec:models), linked where used.

**The deterministic moment-map route.** Section [](#sec:moment-map-cmh) for the programme, Section [](#sec:cmh-normalization) for the endpoint and the proof that it dominates the affine Poincaré constant, Section [](#sec:cmh-exact-cases) for the cases where it is computed exactly. No stochastic localization is used anywhere in it.

**The open bottlenecks, as a list.** Section [](#sec:open) for Route E, Section [](#subsec:spectral-headline) for Route S, and Section [](#sec:kls-synthesis) for the four cross-route targets, each mapped to the ledger node that carries it.

**The complete technical development.** Front to back, with the appendices read at the point they are first linked rather than in advance.

**Reading the status of a statement.** Every theorem, lemma, proposition, corollary, conjecture, assumption and definition below is a node of `research/program/ledger.yaml`, which records its status — proved, open, refuted or defined — and what it rests on; the prose does not, so a statement's typography never outruns its evidence. An open question is stated as a conjecture, in the direction the search tries to establish. Two distinctions the ledger preserves are easy to lose and matter throughout: an unreviewed preprint is recorded as *open* however plausible it is, and a *proved* implication whose antecedent is still open is proved but not progress on the conjecture.

(sec:kls-orientation)=
## The conjecture and why it matters

Part I is the entry point to this document, and it is meant to be readable on its own. This section states the Kannan–Lovász–Simonovits conjecture in the forms used below and fixes the normalizations that make quoted exponents comparable; Section [](#sec:kls-known) records what is known and how the current best bound is built; Section [](#sec:kls-remaining) isolates what is left over, which is the thing every route in Parts III and IV is a response to.

Nothing in Parts I and II is a repository result. Both are exposition of the published and preprint literature, written so that Parts III–V — which *are* repository work — can be read without leaving the document. Imported statements are attributed individually, and version-1 preprints are marked as such wherever they are used.

The conjecture is a statement about *expansion*. A log-concave measure cannot be cut in two without paying for the cut, and KLS asserts that in the right normalization the price does not decay as the dimension grows. Equivalently, in its analytic form, the measure has a spectral gap bounded below independently of $n$: no function of many variables can have large variance and small gradient energy at the same time. Both readings are made precise in the next few pages, and the two-sided comparison [](#eq:cheeger-two-sided) is what allows them to be used interchangeably.

(subsec:kls-conjecture)=
### The conjecture

Let $\mu$ be a log-concave probability measure on $\R^n$. Write $\mu^+(A)$ for the Minkowski boundary measure of a Borel set $A$, and define the Cheeger constant and its reciprocal, the inverse Cheeger scale,

$$
h_\mu=\inf_{A}\frac{\mu^+(A)}{\min\{\mu(A),1-\mu(A)\}},
\qquad
\PsiKLS_\mu=h_\mu^{-1}.
$$

The Poincaré constant $\CP(\mu)$ is the least constant with

$$
\Var_\mu(f)\le\CP(\mu)\int_{\R^n}|\nabla f|^2\dd\mu
$$

for every locally Lipschitz $f$.

:::{warning} The $\psi$ convention
:label: rem:psi-convention
Part of the literature calls $h_\mu$ “the KLS constant” and part calls $h_\mu^{-1}$ by the same name, both writing $\psi_\mu$. This document always writes $h$ for the expansion constant and $\PsiKLS=h^{-1}$ for the inverse scale, and never uses the bare symbol $\psi$ for either. Combined with $\CP\asymp\PsiKLS^2$ below, the convention accounts for most apparent contradictions between quoted exponents: a bound $\PsiKLS_n\lesssim(\log n)^{a}$ is the same statement as $\CP\lesssim(\log n)^{2a}$, so the same theorem is quoted with two different exponents depending on which constant the source names.
:::

For log-concave measures the Cheeger and reverse Cheeger (Buser–Ledoux) inequalities give the two-sided comparison

```{math}
:label: eq:cheeger-two-sided
\tfrac14\le\frac{\PsiKLS_\mu^2}{\CP(\mu)}\le\pi ,
```

so $\CP\asymp\PsiKLS^2$ with universal constants; the explicit constants are recorded in [@Klartag2023Logarithmic; @Milman2009Isoperimetric]. The lower bound is Cheeger's inequality in the normalization $\CP(\mu)\le4h_\mu^{-2}$ used throughout.

:::{prf:conjecture} KLS
:label: conj:kls
There is a universal constant $C<\infty$ such that, for every dimension, every isotropic log-concave $\mu$, and every locally Lipschitz $f$,

$$
\Var_\mu(f)\le C\int_{\R^n}|\nabla f|^2\dd\mu.
$$

Equivalently up to universal constants, the Cheeger constants of all such measures are bounded below uniformly in the dimension.
:::

Write

```{math}
:label: eq:hstar-def
\hstar_n=\inf\bigl\{h_\nu:\ \nu\ \text{isotropic log-concave on }\R^n\bigr\}.
```

Thus [](#conj:kls) is equivalently $\inf_n\hstar_n>0$, up to the comparison [](#eq:cheeger-two-sided).

Three formulations are used interchangeably below.

(a) **Isotropic form.** For isotropic $\mu$ (that is, $\E_\mu X=0$ and $\Cov_\mu(X)=I_n$),

$$
\CP(\mu)=O(1),\qquad \PsiKLS_\mu=O(1),\qquad h_\mu=\Omega(1).
$$

(b) **Affine form.** For every log-concave $\mu$,

```{math}
:label: eq:kls-affine
\CP(\mu)\le C\norm{\Cov\mu}_\op .
```

The reverse inequality $\CP(\mu)\ge\norm{\Cov\mu}_\op$ is automatic: testing the Poincaré inequality on the linear function $f(x)=\inner{x}{v}$ with $v$ a top eigenvector of $\Cov\mu$ gives $\Var_\mu f=\inner{\Cov\mu\,v}{v}$ and $\int|\nabla f|^2\dd\mu=|v|^2$. So [](#eq:kls-affine) says exactly this: *up to a universal constant, linear functions already detect the slowest mode of every log-concave measure.*

(c) **Geometric form.** The least-expanding arbitrary cut of a convex body is, up to a universal factor, no worse than the least-expanding hyperplane cut [@KannanLovaszSimonovits1995].

Applying Poincaré to $f(x)=|x|^2$ in isotropic position gives

```{math}
:label: eq:kls-implies-thin-shell
\Var(|X|^2)\le4n\,\CP(\mu),
```

the implication “KLS $\Rightarrow$ thin shell” discussed in Section [](#subsec:kls-solved-neighbours). There is no known dimension-free converse from this one radial estimate to KLS. It is therefore accurate to say that thin-shell control alone does not currently prove KLS, but not that such a converse has been disproved within the log-concave class.

Finally, no family is known that forces the ratio in [](#eq:kls-affine) to grow with $n$. The entire gap is in the upper bound; it is not a gap between competing upper and lower power laws.

(sec:kls-known)=
## What is known

Where the problem actually stands: the quantitative frontier, the two neighbouring conjectures that have been settled and why settling them did not settle KLS, the architecture of the argument that produces the current best bound, and the exact place the surviving logarithm enters.

(subsec:kls-status)=
### Status as of 24 August 2026

Set

$$
\PsiKLS_n=\sup_\mu\PsiKLS_\mu,
\qquad
C_{\mathrm P,n}=\sup_\mu\CP(\mu),
$$

the suprema over isotropic log-concave measures on $\R^n$. The full conjecture is open. The status distinction that matters for this repository is between the best *published* bound and the best *current preprint* claim.

|  | Bound | Source and status |
|---|---|---|
| Best published | $\PsiKLS_n\lesssim\sqrt{\log n}$, $C_{\mathrm P,n}\lesssim\log n$ | Klartag's improved Lichnerowicz argument [@Klartag2023Logarithmic]. Published; the benchmark this repository treats as certified literature. |
| Best current preprint | $\PsiKLS_n\lesssim(\log n)^{1/4}$, $C_{\mathrm P,n}\lesssim\sqrt{\log n}$ | Letwin, arXiv version 1 of 27 July 2026 [@Letwin2026QuadraticKLS]. Not peer reviewed; see the audit in Section [](#subsec:mm-audit). |

The quantitative history is the following. Exponents are given for $\PsiKLS_n$ and for $C_{\mathrm P,n}$ side by side, precisely because of [](#rem:psi-convention).

| Date | $\PsiKLS_n$ | $C_{\mathrm P,n}$ | Main development |
|---|---|---|---|
| 1995 | $O(n^{1/2})$ | $O(n)$ | The localization lemma [@KannanLovaszSimonovits1995]. |
| 1995–2011 | down to $O(n^{5/12})$ | — | Bobkov's radial inequality fed by successively better thin-shell bounds; the last notable pre-localization record [@GuedonMilman2011]. |
| 2012/13 | $O(n^{1/3}\sqrt{\log n})$ | $O(n^{2/3}\log n)$ | Stochastic localization [@Eldan2013ThinShell]. |
| 2016; 2024 | $O(n^{1/4})$ | $O(n^{1/2})$ | Fixed Gaussian tilt and the $\Tr(A_t^2)$ stopping argument [@LeeVempala2018; @LeeVempala2024]. |
| 2020/21 | $\exp O(\sqrt{\log n\log\log n})$ | same class | Iterated high-Schatten potentials and affine preconditioning [@Chen2021]. |
| 2022 | $O(\log^5 n)$ | $O(\log^{10}n)$ | First polylogarithmic bound; heat flow, spectral projections, $H^{-1}$ [@KlartagLehec2022Polylog]. |
| 2022 | $O(\log^{3.2226}n)$ | $O(\log^{6.4452}n)$ | Two localization representations and spiked-spectrum estimates [@JambulapatiLeeVempala2022KLS]. |
| 2023 | $O(\sqrt{\log n})$ | $O(\log n)$ | Improved Lichnerowicz plus short-time covariance control [@Klartag2023Logarithmic]. |
| July 2026, v1 | $O((\log n)^{1/4})$ | $O(\sqrt{\log n})$ | Sharp quadratic Poincaré inequality, giving $\kappa_n=O(1)$ [@Letwin2026QuadraticKLS]. |

:::{prf:remark} Reading the table
:label: rem:history-table-caveats
Two entries deserve care. The 2016/2024 row is one result: the Lee–Vempala preprint of 2016 appeared in final form in the Annals in 2024, and the repository bibliography records both. The $O(n^{5/12})$ entry summarizes a sequence of thin-shell improvements rather than a single paper, and is quoted here only to mark the pre-localization ceiling. Separately, the bibliography contains [@vempala2016kls], a 2016 announcement of a proof of the full conjecture; it is not a milestone in this table, and it is listed in the bibliography for completeness of the record only.
:::

(subsec:kls-solved-neighbours)=
### Solved neighbours that are not KLS

The classical implication structure is

```{math}
:label: eq:kls-implication-chain
\mathrm{KLS}\ \Longrightarrow\ \text{thin shell}\ \Longrightarrow\ \text{slicing},
```

and no reverse implication is known in a dimension-free form. Both of the weaker conjectures have now moved decisively. Neither resolution proves KLS, and it is worth being precise about why.

**Slicing.** Bourgain's slicing conjecture asks whether the isotropic constants $L_n$ are universally bounded. Guan proved $L_n\lesssim\log\log n$ and, in the process, obtained the stochastic-localization trace estimate that turned out to be decisive [@Guan2024]. Klartag and Lehec combined that estimate with $M$-ellipsoids and Shannon–Stam stability to prove $\sup_nL_n<\infty$, published in 2025 [@KlartagLehec2025Slicing]; Bizeul subsequently gave an alternative proof through small-ball estimates [@Bizeul2025SmallBallSlicing]. This is a genuine resolution, but slicing controls determinant and volume information, not the bottom of the full spectrum.

**Thin shell.** For isotropic log-concave $X$ the thin-shell conjecture asks for $\Var(|X|^2)\le Cn$, equivalently $\E(|X|-\sqrt n)^2\le C$. Klartag and Lehec proved it via parallel couplings of exponential tilts, nonlinear filtering, optimal transport, $H^{-1}$ estimates, and Guan-type covariance control [@KlartagLehec2025ThinShell]. A July 2026 version-1 preprint of Chen and Klartag sharpened it to the optimal $\Var(|X|^2)\le8n$, with equality for products of centered exponentials, together with a sharp third-moment-tensor bound [@ChenKlartag2026SharpThinShell]; both statements are recorded as [](#thm:chen-klartag-thin-shell) and [](#thm:chen-klartag-third-moment).

**Why this does not close the gap.** Eldan's reverse estimate bounds the inverse Cheeger scale by a weighted average of thin-shell parameters $\sigma_k$ [@Eldan2013ThinShell],

```{math}
:label: eq:eldan-reverse
\PsiKLS_n\le C\sqrt{(\log n)\sum_{k=1}^n\frac{\sigma_k^2}{k}} .
```

Even with the thin-shell conjecture in hand — that is, with $\sigma_k=O(1)$ — the harmonic sum contributes a $\log n$ and [](#eq:eldan-reverse) yields only $\PsiKLS_n\lesssim\log n$, not $O(1)$. Radial concentration constrains one observable; KLS quantifies over every function and every measurable cut. The same asymmetry recurs, in sharper form, for Letwin's theorem: it eliminates every *quadratic* witness, and the first eigenfunction of a general log-concave diffusion need not be quadratic.

(subsec:kls-architecture)=
### The present proof architecture

Modern progress on KLS is a hybrid argument with four ingredients, no one of which replaces another. Figure [](#fig:kls-architecture) is the shape of the current best bound.

- **Stochastic localization creates Gaussian curvature.** The tilt $e^{-t|x|^2/2}$ makes the localized measure $t$-strongly log-concave (Section [](#sec:family-sl)).

- **Matrix martingale estimates control how much covariance survives.** The covariance process $A_t$ obeys an exact Riccati SDE whose noise is the third-moment tensor.

- **Bochner/Lichnerowicz converts curvature plus covariance into a spectral gap.** Klartag's improved comparison $\CP\le\sqrt{\norm{\Cov}_\op/t}$ ([](#thm:improved-lichnerowicz)) is what makes short-time curvature usable.

- **Letwin's preprint supplies the previously missing sharp third-moment estimate**, through moment maps, Monge–Ampère, Stein kernels, and $H^{-1}$ (Section [](#sec:family-moment-map)).

::::{figure}
:label: fig:kls-architecture

```{mermaid}
flowchart LR
  sl["Stochastic localization"] --> curv["Gaussian curvature t"]
  sl --> cov["Covariance process A_t"]
  cov --> pot["Third moments, matrix potentials"]
  mm["Moment map and Monge–Ampère"]:::new --> qp["Sharp quadratic Poincaré"]:::new
  qp --> kap["κ_n = O(1)"]:::new
  kap --> pot
  curv --> il["Improved Lichnerowicz"]
  pot --> il
  il --> cp["C_P ≲ √(log n)"]:::res
  cp --> psi["Ψ_KLS ≲ (log n)^(1/4)"]:::res
  classDef new fill:#eef2fb,stroke:#1f3a73,stroke-width:2px
  classDef res fill:#f2f2f2
```

The architecture of the current best bound. Boxed in colour: the July 2026 preprint contribution. It does not replace stochastic localization; it discharges a crucial input to the localization–Lichnerowicz pipeline.
::::

**The exact bridge, and where the logarithm lives.** Define the directional third-moment parameter

```{math}
:label: eq:kappa-def
\kappa_n=\sup_{\mu,\theta}\bigl\lVert\E_\mu[\inner{X}{\theta}X\otimes X]\bigr\rVert_{\HS},
```

the supremum over isotropic log-concave $\mu$ on $\R^n$ and $\theta\in S^{n-1}$. The localization–Lichnerowicz pipeline delivers

```{math}
:label: eq:kls-bridge
\boxed{\ C_{\mathrm P,n}\lesssim\kappa_n\sqrt{\log n}\ }
```

(Section [](#subsec:sl-where-the-log-lives)), and Letwin's $\kappa_n\le2\sqrt2$ ([](#prop:letwin-kappa)) is what turns [](#eq:kls-bridge) into the current record.

The point to retain is *where the surviving $\sqrt{\log n}$ comes from*. It is not hidden in the moment-map calculation. Klartag–Lehec smooth the maximum covariance eigenvalue by log-trace-exp,

$$
\Phi_t=\frac1\beta\log\Tr\bigl(e^{\beta A_t}\bigr),
\qquad
\norm{A_t}_\op\le\Phi_t\le\norm{A_t}_\op+\frac{\log n}\beta ,
$$

and approximating $\lmax$ to within a constant forces $\beta\asymp\log n$. The Itô drift is then of size $O(\kappa_n^2\log n)$, so covariance control survives only until $t_*\asymp1/(\kappa_n^2\log n)$, and improved Lichnerowicz converts that time into $\CP\lesssim t_*^{-1/2}\lesssim\kappa_n\sqrt{\log n}$. The logarithm is the *entropy cost of replacing a matrix maximum by a soft maximum over $n$ directions*. That diagnosis is what makes target 3 of Section [](#sec:kls-synthesis) concrete.

(sec:kls-remaining)=
## The shape of the remaining problem

The July 2026 preprints changed the shape of the problem, and it is worth stating the change precisely rather than as a mood: *the remaining difficulty is no longer quadratic forms or third moments*. Conditional on [@Letwin2026QuadraticKLS], $\kappa_n=O(1)$ and every quadratic witness is eliminated. What survives is a difficulty of a different type, and this section states it in the two forms every route below must answer.

(subsec:kls-adaptive-residue)=
### Fixed and averaged, against adaptive and uniform

Every method surveyed in Part II controls something. Needles control one-dimensional conditional measures sharply; stochastic localization controls short-time covariance and, conditionally, third moments; heat-flow and $H^{-1}$ arguments control coordinate and quadratic spectral mass; moment maps control fixed deterministic matrix energies $\E\Tr(BHBH)$; parallel coupling controls linear exponential tilts; Brownian transport controls averaged derivatives to within a polylogarithm. Section [](#subsec:synthesis-table) tabulates these one by one.

What none of them controls is the same object when it is allowed to *adapt*. In every row of that table the estimate holds for a fixed matrix, a fixed direction, a fixed tilt, or on average along a path, and KLS needs it uniformly, for an object that may depend on the measure or on the extremizing function. The gap is not a constant to be improved; it is a quantifier in the wrong place. A reader who remembers one sentence from Part I should remember this one, because it is the sentence each of the four routes of Parts III and IV proposes a different way around.

(subsec:kls-spike-obstruction)=
### The covariance spike, and why the direct repair is false

The most natural repair — bound $\norm{A_t}_\op$ better — cannot work, and this is not a guess about difficulty but a proved fact.

:::{prf:proposition} Covariance spikes are compatible with KLS
:label: prop:covariance-spike
Let $\mu$ be the law of $n$ independent centered one-sided exponential coordinates and let $G$ be a standard Gaussian independent of $X\sim\mu$. Then $\CP(\mu)=O(1)$ by tensorization, yet

$$
\Prob\!\left(
\bigl\lVert\Cov(X\mid X+\sqrt sG)\bigr\rVert_\op\ge c_{\rm sp}s
\right)
\ge1-\left(1-\tfrac12e^{-s}\right)^n
$$

for a universal $c_{\rm sp}>0$. Consequently, for $s\le\log n$,

$$
\E\bigl\lVert\Cov(X\mid X+\sqrt sG)\bigr\rVert_\op\gtrsim s
\qquad\text{and}\qquad
\Prob\!\left(
\bigl\lVert\Cov(X\mid X+\sqrt sG)\bigr\rVert_\op\ge c_{\rm sp}s
\right)\ge1-e^{-1/2}.
$$
:::

This is worked out in Section 8.1 and Proposition 65 of Klartag–Lehec [@KLnotes]; it is imported here, not proved.

The consequence is structural, and it is worth stating flatly: *uniform operator-norm control of the conditional covariance at every scale is false, even for a measure that satisfies KLS.* Any argument whose only use of the localization path is a pathwise bound on $\norm{A_t}_\op$ is therefore attempting to prove something stronger than KLS, and something that is not true. A successful potential must exploit eigenvalue profiles, averaging, tensorization, or the particular extremizing function — not better pointwise bounds.

There is a second consequence, and it cuts the other way. Rare covariance spikes can be *harmless*: the measure above satisfies KLS with a universal constant while spiking. A potential that charges the full largest eigenvalue whenever a spike occurs is therefore overcharging, and overcharging in a way that is easy to detect.

(subsec:kls-tensorization-test)=
### The tensorization test

That gives a cheap and surprisingly discriminating test, which any proposal — including every route below — should be made to pass before it is developed.

> *Evaluate the proposed potential on a product of $n$ independent copies of a one-dimensional measure. A quantity that is not tensorization-aware will charge $n$ independent coordinates $n$ times for a phenomenon that costs $O(1)$.*

The test is not a formality. Section [](#sec:product-stress) applies it to the all-cut Carleson estimate of Route E and it is where the rank-one candidate is refuted; the same computation is what identifies the surviving adapted alignment problem. A proposal that fails it is not merely inefficient, it is false at scale, and the failure is usually visible in a page.

Every live route of this repository is a response to the two constraints of this section:

- Route E (Section [](#sec:introduction)) retains the two-color covariance of one fixed candidate cut, rather than the full spectrum of $A_t$.

- Route S (Section [](#sec:spectral-route)) retains the covariance tensor of one fixed first eigenfunction.

- Route C (Section [](#sec:moment-map-cmh)) abandons stochastic localization altogether and works in deterministic moment-map coordinates.

- Route F (Section [](#sec:conditional-fiber-frame)) replaces Euclidean directions by one test-independent isotropic frame of inverse-variance-normalized conditional line resamplings.

Section [](#sec:frontier-atlas) compares them side by side, with the advance and the exact blocker of each; the chapters of Parts III and IV then develop them at their natural lengths.
