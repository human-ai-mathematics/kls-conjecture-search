# Prover: conditional-fiber form structure and simplex root obstruction

Date: 2026-08-27

Role: `prover`

Run id: `w3p01`

Owned dossier: `solutions/conditional-fiber-frame-structure.tex`

Covered nodes: `lem:conditional-fiber-form`, `prop:conditional-fiber-root-obstruction`

No numerical evidence is used. No ledger, manuscript, gating, route-control, bibliography,
review, knowledge, or numerical file is changed.

## Outcome

A coupled standalone dossier was completed. Its SHA-256 is

`4a2adf954edf5b51f80e4f61787a5fd57c374e04144de598003635fab21c69b8`.

The dossier has `checked_by: none`; it has no ledger value until a distinct cold proof-checker
audits this exact hash.

## Refined structural theorem

Let $\mu$ be a full-dimensional probability on $\mathbb R^d$ with Borel density and finite
second moment, and let $\rho$ be an even Borel probability satisfying

$$
d\int\theta\theta^T\,d\rho(\theta)=I_d.
$$

Using the canonical density disintegration along lines parallel to $\theta$, with null and
zero-variance fibers assigned weight zero, define

$$
\mathcal D_{\mu,\rho}[f]
=d\int\!\int
\frac{\operatorname{Var}_{\mu_{\theta,z}}(f(z+T\theta))}
{\operatorname{Var}_{\mu_{\theta,z}}(T)}
\,d\bar\mu_\theta(z)d\rho(\theta)
$$

on its maximal finite-energy domain. The dossier proves:

- the fiber laws, conditional means, conditional variances, conditional expectations, and form
  integrand have jointly measurable versions, independent of both the $L^2$ representative of
  $f$ and the Lebesgue-a.e. representative of the density;
- the form is densely defined, closed, symmetric, Markovian, conservative, and reversible;
- its pair-jump representation holds on the whole form domain;
- the associated nonnegative self-adjoint generator exists in form sense;
- on the explicit sufficient Bochner domain
  $h_\theta=w_\theta(I-P_\theta)f\in L^2$,
  $\int\|h_\theta\|_2d\rho<\infty$, with strong measurability,
  $$
  A_{\mu,\rho}f=d\int h_\theta\,d\rho(\theta),
  \qquad
  \mathcal L_{\mu,\rho}f
  =d\int w_\theta(P_\theta f-f)\,d\rho(\theta)
  $$
  in $L^2$ and pointwise almost everywhere, even when the raw total rate
  $d\int w_\theta(x)d\rho(\theta)$ is infinite;
- for log-concave $\mu$,
  $$
  \mathcal D_{\mu,\rho}[f]\le4\int|\nabla f|^2d\mu,
  $$
  so a form gap $C$ implies $C_P(\mu)\le4C$;
- for every linear $f_a(x)=a\cdot x$,
  $\mathcal D_{\mu,\rho}[f_a]=|a|^2$, and therefore the Rayleigh quotient is one in isotropic
  position;
- every admissible frame has gap one for the standard Gaussian; and
- the coordinate frame has gap one for every product of centered variance-one density factors.

The only dependency is proved `thm:cmh-1d`, used for the sharp one-dimensional log-concave
Poincare inequality $C_P(\nu)\le4\operatorname{Var}_\nu(T)$. Thus the result is unconditional
under its explicit hypotheses.

## Measure-theoretic and operator audit

The density disintegration is built on the Borel incidence bundle
$\{(\theta,z):z\in\theta^\perp\}$ using countably many Borel orthonormal-frame charts. This
prevents an uncountable family of unrelated conditional-probability versions. Orthogonal Fubini
shows that bad fibers are null under the finite-second-moment hypothesis and that changing a
density or test-function representative changes no integrated energy.

Writing $P_\theta=\mathbb E[\cdot\mid P_{\theta^\perp}X]$ and
$w_\theta=\sigma_\theta^{-2}$, the single-direction energy is

$$
\|w_\theta^{1/2}(I-P_\theta)f\|_2^2.
$$

The multiplier is fiber-measurable and commutes with $P_\theta$. Each single-direction operator
is closed, and a subsequence argument proves closedness of their jointly measurable direct
integral. Ambient $C_c^\infty(\mathbb R^d)$ functions are in the domain because
$\operatorname{Var}(g(T))\le\operatorname{Lip}(g)^2\operatorname{Var}(T)$, and they are dense
in $L^2(\mu)$ even when the convex support is not open.

For the generator, the proof explicitly truncates $w_\theta$ to justify
$P_\theta[w_\theta(I-P_\theta)f]=0$ and then passes in $L^2$. No literal jump-process
realization and no characterization of the full operator domain is claimed.

## Calibration audit

For the Gaussian, $P_\theta$ is second quantization of
$Q_\theta=I-\theta\theta^T$. On the $r$th chaos,

$$
I-Q_\theta^{\otimes r}
\succeq (\theta\theta^T)\otimes I^{\otimes(r-1)}.
$$

Tight-frame averaging gives $\mathcal D\ge\operatorname{Var}$, while conditional-variance
contraction gives $\mathcal D\le d\operatorname{Var}$. Linear tests attain equality.

For a standardized product and the coordinate frame, the form is exactly

$$
\sum_i\mathbb E\operatorname{Var}(f\mid X_j,\ j\ne i),
$$

so Efron--Stein and linear equality give gap one.

## Exact simplex root theorem

For $P\sim\operatorname{Dir}(1,\ldots,1)$, let
$X=\sqrt{m(m+1)}(P-m^{-1}\mathbf1)$ on $H_0=\mathbf1^\perp$ and let
$\rho_{\rm root}$ be the uniform even $A_{m-1}$ root frame. The dossier proves

$$
\mathcal D_{\rm root}[f]
=\frac{12}{m^2(m+1)}\sum_{i<j}
\mathbb E\frac{\operatorname{Var}_{ij}(f)}{(P_i+P_j)^2}
=\frac{12}{m+1}\sum_{i<j}
\mathbb E\frac{\operatorname{Var}_{ij}(f)}{(\eta_i+\eta_j)^2},
\qquad \eta_i=mP_i.
$$

For $A_{m,\varepsilon}=\{\eta_1>m-\varepsilon\}$,

$$
p_{m,\varepsilon}=\mathbb P(A_{m,\varepsilon})
=\left(\frac\varepsilon m\right)^{m-1}.
$$

Only the $m-1$ pairs incident to coordinate $1$ contribute. A truncated weighted tower identity
proves finite form energy and the exact manuscript bound

$$
\frac{\mathcal D_{\rm root}(\mathbf1_A)}{\operatorname{Var}(\mathbf1_A)}
\le
\frac{12(m-1)}{(m+1)(m-\varepsilon)^2
\left(1-(\varepsilon/m)^{m-1}\right)}.
$$

Letting $\varepsilon\downarrow0$ gives the stronger explicit consequence

$$
\operatorname{gap}(\mathcal D_{\rm root})
\le\frac{12(m-1)}{m^2(m+1)}\le\frac{12}{m^2}.
$$

At $m=2$ the first bound is one and the single root update indeed resamples the whole simplex.

## Fence, hypothesis, and status audit

Neither node has a `bounded_by` edge. All hypotheses actually used are stated: Borel density and
finite second moment for the structural setup and linear $L^2$ calibration; the tight-frame
identity; log-concavity only for the factor-$4$ gradient comparison; isotropy only for the linear
Rayleigh quotient; Gaussianity only for the Fock calculation; independence, centering, unit
variance, and density for the product calibration; and the flat Dirichlet law plus the fixed
uniform root frame for the cap calculation.

The cap refutes only $\rho_{\rm root}$. It neither controls frames using non-root directions nor
settles the all-frame supremum. No root optimality, equivalence with KLS, KLS counterexample, or
all-frame simplex conclusion is claimed.

There are no unclosed analytic steps in the dossier. The author subaudit identified one central
semantic mismatch: the manuscript/ledger context initially omitted the finite-second-moment
hypothesis and did not qualify the linear Rayleigh quotient by isotropy. The orchestrator applied
that synchronization before this handoff. The current dossier, manuscript, and ledger now all
state $\mathcal D(a\cdot x)=|a|^2$, with quotient one only in isotropic position.

## Build

Command:

```bash
cd solutions && latexmk -pdf -outdir=../build conditional-fiber-frame-structure.tex
```

Result: success, six pages. The log has no TeX error, undefined control sequence, overfull box,
or underfull box. The only warnings are the expected standalone unresolved external references
to `thm:cmh-1d` and `q:conditional-fiber-frame`.

```yaml
outcome: complete
artifacts:
  - solutions/conditional-fiber-frame-structure.tex
  - research/explorations/2026-08-27-prover-conditional-fiber-frame-structure-w3p01.md
proposed_deltas:
  - none
next_role: proof-checker
next_prompt: |
  Cold-review `solutions/conditional-fiber-frame-structure.tex` at SHA-256
  `4a2adf954edf5b51f80e4f61787a5fd57c374e04144de598003635fab21c69b8`
  for both `lem:conditional-fiber-form` and
  `prop:conditional-fiber-root-obstruction`. Verify the density disintegration and joint
  measurability, null/zero-variance fiber conventions, direct-integral closedness, pair-jump
  Markov property, form-sense generator and the sufficient Bochner-domain pointwise formula,
  the use of proved `thm:cmh-1d` in the factor-4 comparison, the isotropic linear calibration,
  the arbitrary-frame Gaussian Fock argument, the coordinate-product Efron--Stein argument,
  and every simplex-root/cap constant including domain membership and epsilon-to-zero limit.
  Confirm that the result is unconditional under its stated finite-second-moment hypotheses,
  has no `bounded_by` edge, and refutes only the root frame, not the existential all-frame
  question or KLS. Check the orchestrator's synchronized manuscript/ledger wording before any
  certification delta. Keep reviewer identity distinct from the author.
```
