# A4 next cycle: three local VI theorems and exact entropy-tilt calibration

Date: 2026-08-21

Reviewed nodes: `eq:a4-mean-dual`, `prop:a4-mean-local`,
`prop:a4-local-wellspecified`, `prop:a4-local-misspecified`, `prop:a4-local-excess`,
`ex:a4-gaussian-local`, and `lem:a4-symmetrization`. Broader targets:
`q:a4-restricted`, `q:a4-mean`, and `conj:a4`.

Original status: analytic exploration submitted for review. The subsequent independent
certification outcome is recorded at the end of this note.

## Verdict

There is no single “local VI constant.” Three inequivalent objects have to be separated.

1. In a well-specified family, both numerator and KL vanish at the posterior, and the local
   constant is a generalized eigenvalue.
2. In a misspecified family, the ordinary ratio retains the approximation baselines
   $D_*=W_2^2(q_*,\pi)$ and $2\delta_Q$ and can have a $\sqrt\rho$ correction.
3. If numerator and denominator are instead centred at the VI optimizer, the generalized
   eigenvalue describes **optimization error around $q_*$**, not approximation error to $\pi$.

The unrestricted localized mean constant has an exact entropy-tilt representation. It sees the
posterior covariance as the entropy radius tends to zero, even when the global mean constant is
forced to prior scale by remote tilts. A fixed-covariance Gaussian family calibrates all three
regimes in closed form.

## 1. Local setup and the coercivity contract

Let $q_\eta$, $\eta\in\mathbb R^p$, be an identifiable $\mathcal P_2$ family and put

$$
K(\eta)=\mathrm{KL}(q_\eta\|\pi),\qquad
D(\eta)=W_2^2(q_\eta,\pi),\qquad
M(\eta)=\|\mathbb E_{q_\eta}\theta-\mathbb E_\pi\theta\|^2.
$$

The local calculations below are valid for the *full family supremum* only under the following
isolation clause.

> **Local-sublevel contract.** There is a radius $\rho_0>0$ such that the complete family
> sublevel $\{\eta:K(\eta)\le\delta_Q+\rho_0\}$ lies in one compact identifiable chart around
> the stated optimizer. The function $K$ is continuous on that chart, the optimizer is unique,
> and $K$ is separated above $\delta_Q$ off every neighborhood of it. In that chart the Taylor
> remainders below are uniform, and $F\succ0$.

Without this clause, Taylor expansion in one chart gives only a directional lower witness: a
remote component of the same KL sublevel may dominate the supremum. Multiple minimizers require
an envelope over their charts; a boundary minimizer requires a tangent-cone expansion and may
retain a KL-linear term.

For the GLM program, this finite-dimensional clause should eventually be derived from a concrete
coercivity/tail package: covariance eigenvalues bounded away from zero and infinity on the KL
sublevel, bounded means, and uniform $\mathcal P_2$ integrability. It is not a consequence of a
KL cutoff over an unrestricted family.

## 2. Well-specified theorem

Assume $q_0=\pi$ and, uniformly as $h\to0$,

$$
2K(h)=h^\top Fh+O(\|h\|^3),
\quad D(h)=h^\top Gh+O(\|h\|^3),
\quad \mathbb E_{q_h}\theta-\mathbb E_\pi\theta=Bh+O(\|h\|^2).       \tag{1}
$$

A sufficient Wasserstein tangent construction is:

- the scores $s_i=\partial_i\log q_\eta|_0$ are centred in
  $L^2(\pi)\cap H^{-1}(\pi)$;
- the weak Poisson problems
  $-\nabla\cdot(\pi\nabla\phi_i)=s_i\pi$ have finite-energy solutions;
- $F_{ij}=\int s_i s_j\,d\pi$ is finite and positive definite; and
- $G_{ij}=\int\nabla\phi_i\cdot\nabla\phi_j\,d\pi$.

### Proof (subsequently independently agent-certified)

The local-sublevel contract and $F\succ0$ imply $\|h\|=O(\sqrt\rho)$ whenever $K(h)\le\rho$.
Dividing (1) gives, uniformly on the punctured sublevel,

$$
\frac{D(h)}{2K(h)}
=\frac{h^\top Gh}{h^\top Fh}+O(\sqrt\rho).
$$

The upper bound is the largest generalized Rayleigh quotient plus the uniform error. Arbitrarily
small multiples of a top generalized eigenvector remain in every positive sublevel and give the
matching lower limit. Hence

$$
C_{Q,\rho}=\lambda_{\max}(F^{-1/2}GF^{-1/2})+O(\sqrt\rho),       \tag{2}
$$

and, since $M(h)=h^\top B^\top Bh+O(\|h\|^3)$,

$$
C_{\mathrm{mean},Q,\rho}
=\lambda_{\max}(F^{-1/2}B^\top BF^{-1/2})+O(\sqrt\rho).         \tag{3}
$$

The cubic remainder is stronger than is needed for convergence, but it makes the stated rate
transparent.

## 3. Misspecified ordinary ratio

Let $\eta_*$ be a unique interior minimizer, $\delta=K(\eta_*)>0$, and write

$$
2K(\eta_*+h)=2\delta+h^\top F_*h+O(\|h\|^3),\qquad F_*\succ0,  \tag{4}
$$

$$
D(\eta_*+h)=D_*+b_D^\top h+O(\|h\|^2),
\quad
M(\eta_*+h)=M_*+b_M^\top h+O(\|h\|^2).                         \tag{5}
$$

### Proof (subsequently independently agent-certified)

Up to an $O(\rho)$ radial perturbation, the KL sublevel is
$h^\top F_*h\le2\rho$. The denominator has no linear variation at an interior optimizer, while
the numerator generally does. Expanding the ratio and maximizing the linear form on this
ellipsoid gives

$$
C_{Q,\delta+\rho}
=\frac{D_*}{2\delta}
+\frac{\sqrt{2\rho}}{2\delta}\|F_*^{-1/2}b_D\|+O(\rho),          \tag{6}
$$

$$
C_{\mathrm{mean},Q,\delta+\rho}
=\frac{M_*}{2\delta}
+\frac{\sqrt{2\rho}}{2\delta}\|F_*^{-1/2}b_M\|+O(\rho).        \tag{7}
$$

If $b_D=0$ or $b_M=0$, the corresponding first correction is $O(\rho)$. Equations (6)--(7), not
(2)--(3), are the ordinary localized constants for a misspecified family. In particular, a
posterior-scale tangent matrix cannot erase a nonzero approximation baseline.

## 4. Optimizer-centred excess KL

Define

$$
C^{\mathrm{ex}}_{Q,\rho}(q_*)
=\sup_{0<K(\eta)-\delta\le\rho}
\frac{W_2^2(q_\eta,q_*)}{2\{K(\eta)-\delta\}},                 \tag{8}
$$

and define the mean version by replacing the numerator with
$\|\mathbb E_{q_\eta}\theta-\mathbb E_{q_*}\theta\|^2$.
If

$$
W_2^2(q_{\eta_*+h},q_*)=h^\top G_*h+O(\|h\|^3),
\qquad
\mathbb E_{q_{\eta_*+h}}\theta-\mathbb E_{q_*}\theta
=B_*h+O(\|h\|^2),                                               \tag{9}
$$

then subtracting $\delta$ from (4) puts (8) in the well-specified algebra. Thus

$$
C^{\mathrm{ex}}_{Q,\rho}(q_*)
=\lambda_{\max}(F_*^{-1/2}G_*F_*^{-1/2})+O(\sqrt\rho),         \tag{10}
$$

$$
C^{\mathrm{ex}}_{\mathrm{mean},Q,\rho}(q_*)
=\lambda_{\max}(F_*^{-1/2}B_*^\top B_*F_*^{-1/2})+O(\sqrt\rho).
                                                                        \tag{11}
$$

These constants control an approximate optimizer $q$ relative to $q_*$; they do not certify
$q_*$ relative to $\pi$. A safe decomposition is

$$
W_2(q,\pi)\le W_2(q,q_*)+W_2(q_*,\pi).
$$

The second term is approximation error and still needs the raw baseline or another argument.

## 5. Exact localized unrestricted mean dual

For a unit vector $u$, set

$$
X_u=u^\top(\theta-\mathbb E_\pi\theta),\qquad
\psi_u(t)=\log\mathbb E_\pi e^{tX_u},\qquad
r_u(t)=t\psi_u'(t)-\psi_u(t).                                  \tag{12}
$$

Assume each nonconstant directional cumulant is Legendre on the interior of its effective domain,
with boundary mean values approximable by derivatives. The Gibbs variational formula implies

$$
\mathrm{KL}(q\|\pi)\ge \psi_u^*(\mathbb E_qX_u).               \tag{13}
$$

The exponential tilt

$$
\frac{dq_{u,t}}{d\pi}=e^{tX_u-\psi_u(t)}                       \tag{14}
$$

attains equality, with mean $\psi_u'(t)$ and entropy $r_u(t)$. Minimizing entropy at a fixed
projected mean before maximizing the ratio proves the exact identity

$$
\boxed{
C_{\mathrm{mean},\mathrm{all},r}
=\sup_{\|u\|=1}\sup_{0<r_u(t)\le r}
\frac{\psi_u'(t)^2}{2r_u(t)}.}                                 \tag{15}
$$

The supremum includes endpoint limits; a constant direction contributes zero. This is the
localized counterpart of `eq:a4-mean-dual`.

If $\mathbb E e^{\tau\|\theta\|}<\infty$ for some $\tau>0$ and
$\operatorname{Cov}(\theta)\succ0$, directional third cumulants are uniformly bounded near zero.
Writing $v_u=u^\top\operatorname{Cov}(\theta)u$ gives

$$
\psi_u(t)=\tfrac12v_ut^2+O(|t|^3),\quad
\psi_u'(t)=v_ut+O(t^2),\quad
r_u(t)=\tfrac12v_ut^2+O(|t|^3).                                \tag{16}
$$

Since $r_u$ increases with $|t|$ on each side of zero and $v_u$ is uniformly positive, the
constraint $r_u(t)\le r$ forces $|t|=O(\sqrt r)$. Therefore

$$
C_{\mathrm{mean},\mathrm{all},r}
=\lambda_{\max}(\operatorname{Cov}_\pi\theta)+O(\sqrt r).      \tag{17}
$$

This local statement and the global logistic rigidity coexist: remote tilts recover the prior
quadratic tail, while a shrinking entropy ball only sees local cumulants.

## 6. Exact Gaussian calibration

Let $\pi=N(\mu,\Sigma)$, and fix $S\succ0$ in the location family
$Q_S=\{N(\mu+m,S):m\in\mathbb R^d\}$. Define

$$
\delta_S=\frac12\left\{\operatorname{tr}(\Sigma^{-1}S)-d
+\log\frac{\det\Sigma}{\det S}\right\},                       \tag{18}
$$

$$
D_S=\operatorname{tr}\left[S+\Sigma
-2(\Sigma^{1/2}S\Sigma^{1/2})^{1/2}\right],
\qquad \lambda=\lambda_{\max}(\Sigma).                         \tag{19}
$$

Then exactly

$$
2\mathrm{KL}(q_m\|\pi)=2\delta_S+m^\top\Sigma^{-1}m,qquad
W_2^2(q_m,\pi)=D_S+\|m\|^2.                                   \tag{20}
$$

At fixed $s=m^\top\Sigma^{-1}m$, the largest $\|m\|^2$ is $\lambda s$. Since the sublevel is
$0\le s\le2\rho$, a one-variable endpoint maximization gives, for $S\ne\Sigma$,

$$
\boxed{
C_{Q_S,\delta_S+\rho}
=\max\left\{\frac{D_S}{2\delta_S},
\frac{D_S+2\rho\lambda}{2(\delta_S+\rho)}\right\},}          \tag{21}
$$

$$
\boxed{
C_{\mathrm{mean},Q_S,\delta_S+\rho}
=\lambda\frac{\rho}{\delta_S+\rho}.}                         \tag{22}
$$

Both optimizer-centred excess constants are exactly $\lambda$ for every $\rho>0$. If $S=\Sigma$,
then $\delta_S=D_S=0$ and both ordinary localized constants are also exactly $\lambda$ for every
$\rho>0$. This simultaneously checks (2), (6), and (10): the misspecified raw transport constant
starts at $D_S/(2\delta_S)$, the raw mean constant starts at zero, and the optimizer-centred
geometry is already $\lambda$.

For unrestricted Gaussian means, $\psi_u(t)=t^2u^\top\Sigma u/2$, so (15) also equals $\lambda$
at every positive entropy radius.

## 7. Symmetrization bridge to A5

If a finite isometry group $G$ leaves $\pi$ invariant and
$\bar q=|G|^{-1}\sum_g g_\#q$, convexity gives

$$
\mathrm{KL}(\bar q\|\pi)\le\mathrm{KL}(q\|\pi),
\qquad
W_2^2(\bar q,\pi)\le W_2^2(q,\pi).                             \tag{23}
$$

The Wasserstein inequality follows by averaging the isometric images of an optimal coupling.
Every invariant observable has the same expectation under $q$ and $\bar q$. This is useful for
label-invariant VI only if the family is closed under averaging; a single-Gaussian family usually
is not. Also, (23) does not compare the ratio because numerator and denominator both decrease.

## 8. Stop/go criteria

### Near-term go

1. Verify (21)--(22) numerically for noncommuting $S$ and $\Sigma$; this is an exact regression,
   not evidence for the GLM conjecture.
2. For a Gaussian or mean-field GLM family, prove the local-sublevel contract and the uniform
   expansions before estimating a generalized eigenvalue.
3. Report raw misspecified ratios and optimizer-centred excess ratios separately.

### Stop

1. Stop a posterior-scale claim if a remote parameter sequence stays in the asserted KL sublevel.
2. Stop using (2) for a misspecified raw ratio if $D_*>0$ or $\delta_Q>0$.
3. Stop treating a grid maximum as an upper bound on any family supremum.

## Certification outcome (independent review, 2026-08-21)

The independent audit `/root/review_a4_a5` accepted the following nodes after the compact-chart
contract was strengthened to require continuity, uniqueness, and quantitative separation:

- `eq:a4-mean-dual` and `prop:a4-mean-local`;
- `prop:a4-local-wellspecified`, `prop:a4-local-misspecified`, and `prop:a4-local-excess`;
- `ex:a4-gaussian-local`; and
- `lem:a4-symmetrization`.

Standalone dossiers are stored under `solutions/` with `checked_by: agent` and a link to the
persisted independent review. The broader GLM theorem `conj:a4`, the restricted-family questions,
and `prop:a4-logistic-global` were not discharged by this audit. The ledger and shared-knowledge
updates were subsequently applied while this dated note was retained as the analytic record.
