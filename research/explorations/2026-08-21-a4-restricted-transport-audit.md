# A4 restricted transport audit: prior-scale rigidity, entropy balls, and the tangent target

Date: 2026-08-21

Targets: `conj:a4`, `q:a4-restricted`, `q:a4-mean`, `q:a4-multimodal`, and `q:a4-elbo`.

Original status: analytic exploration under the then-current human/Lean-only gate. Results marked
**Proof** were internal proof drafts rather than ledger promotions. Statements marked
**Conjecture** or **Proposed test** are not evidence. No `numerical-strong` claim is made.

> **Later certification update.** This is the pre-review exploration record. The subsequent
> [independent-agent audit](../reviews/2026-08-21-a4-a5-independent-agent-audit.md), performed
> under the repository's owner-authorized agent-certification contract, promoted
> `eq:a4-mean-dual`, `prop:a4-mean-local`, `prop:a4-local-wellspecified`,
> `prop:a4-local-misspecified`, `prop:a4-local-excess`, `ex:a4-gaussian-local`, and
> `lem:a4-symmetrization` to `proved`. The global logistic claim `prop:a4-logistic-global` and
> the main finite-radius target remain open. The original status language below is retained as
> chronology rather than as the current ledger verdict.

## Verdict

The global family restriction does not buy a posterior-scale constant for the principal A4
example. For a Gaussian-prior logistic posterior and any Gaussian variational family containing
all translations of one fixed covariance,

$$
C_{\mathrm{mean},\mathcal Q}(\pi)
=C_{\mathcal Q}(\pi)
=C_{\mathrm{mean},\mathrm{all}}(\pi)
=C_{\mathrm{TCI}}(\pi)
=\lambda_{\max}(\Sigma_0).
$$

This remains true when the bulk covariance is of order $n^{-1}$. The likelihood is only linear
in the remote tails, so arbitrarily translated Gaussians recover the quadratic prior scale.
Only the KL-localized constant $C_{\mathcal Q,r}$ can plausibly recover the posterior scale.

There are three further corrections/refinements.

1. The unrestricted mean constant has an exact cumulant dual, stronger than the pre-audit
   manuscript's upper bound; the integrated manuscript now states the identity.
2. A KL sublevel alone does not control $W_2$ for a heavy-tailed target if the family can reweight
   remote tails. Its finiteness in the current `stress-ep-tails` model comes from the coercive,
   finite-dimensional Gaussian family as well as the KL cutoff.
3. The stored separated-mixture diagnostic did not use a reweighting witness. Its broad single
   Gaussian gave ratio $0.656<10.190$ for mode collapse while its note claimed the opposite.
   The implementation now uses actual $\varepsilon$-reweighted component mixtures and a focused
   regression, but the resulting single-separation sweep remains a diagnostic, not asymptotic
   evidence.

## 1. Exact dual for the unrestricted posterior-mean constant

Let $X\sim\pi$, $\bar X=X-\mathbb E X$, and define, with extended values allowed,

$$
K_{\mathrm{lin}}(\pi)
:=\sup_{\|u\|=1}\sup_{t\ne0}
\frac{2}{t^2}\log\mathbb E_\pi e^{t u^\top\bar X}.
$$

### Proof

The Gibbs variational formula gives

$$
\log\mathbb E_\pi e^{t u^\top\bar X}
=\sup_{q\ll\pi}
\left\{t u^\top(\mathbb E_qX-\mathbb E_\pi X)-\mathrm{KL}(q\|\pi)\right\}.
$$

If the cumulant is at most $K t^2/2$, the entropy inequality and optimization over $t$ give

$$
|u^\top(\mathbb E_qX-\mathbb E_\pi X)|^2
\le 2K\,\mathrm{KL}(q\|\pi).
$$

Taking the supremum over $u$ proves $C_{\mathrm{mean},\mathrm{all}}\le K_{\mathrm{lin}}$.
Conversely, if the mean inequality holds with constant $C$, then
$\mathrm{KL}(q\|\pi)\ge a^2/(2C)$ for
$a=u^\top(\mathbb E_qX-\mathbb E_\pi X)$. Substitution in the variational formula gives

$$
\log\mathbb E_\pi e^{t u^\top\bar X}
\le\sup_{a\in\mathbb R}\left(ta-\frac{a^2}{2C}\right)
=\frac{Ct^2}{2}.
$$

Taking optimal constants in both directions proves the exact identity

$$
\boxed{C_{\mathrm{mean},\mathrm{all}}(\pi)=K_{\mathrm{lin}}(\pi).}
$$

For a restricted family, only
$C_{\mathrm{mean},\mathcal Q}\le K_{\mathrm{lin}}$ is automatic. Equality requires that
$\mathcal Q$ contain, or asymptotically reproduce, the relevant entropy tilts.

## 2. Gaussian-prior logistic posteriors are globally prior-scale

Let

$$
\pi(d\theta)\propto
\exp\left[-\frac12\theta^\top\Sigma_0^{-1}\theta-\ell(\theta)\right]d\theta,
$$

where $\ell$ is a binary logistic negative log likelihood. It obeys

$$
0\le\ell(\theta)\le c_0+c_1\|\theta\|,
$$

because each loss is bounded above by $\log2+|x_i^\top\theta|$. Fix any $S\succ0$ and suppose
$\mathcal Q$ contains $q_m=N(m,S)$ for every $m\in\mathbb R^d$; a full mean-field Gaussian
family has this property with diagonal $S$.

### Proof

The posterior potential has Hessian at least $\Sigma_0^{-1}$. Bakry--Émery and
Otto--Villani therefore give

$$
C_{\mathrm{mean},\mathcal Q}
\le C_{\mathcal Q}
\le C_{\mathrm{TCI}}(\pi)
\le\lambda_{\max}(\Sigma_0).                                      \tag{1}
$$

Translation leaves the entropy of $q_m$ fixed. The quadratic prior and the linear-growth bounds
on $\ell$ give, as $m=tv$ and $|t|\to\infty$,

$$
2\,\mathrm{KL}(q_{tv}\|\pi)
=t^2v^\top\Sigma_0^{-1}v+O(|t|).                                 \tag{2}
$$

Moreover,

$$
W_2^2(q_{tv},\pi)
\ge\|tv-\mathbb E_\pi\theta\|^2,
$$

and the numerator in the mean constant is exactly the same squared mean displacement. Hence

$$
\liminf_{|t|\to\infty}
\frac{\|\mathbb E_{q_{tv}}\theta-\mathbb E_\pi\theta\|^2}
     {2\,\mathrm{KL}(q_{tv}\|\pi)}
\ge\frac{\|v\|^2}{v^\top\Sigma_0^{-1}v}.                       \tag{3}
$$

Optimizing (3) over $v$ gives the reverse inequality to (1), proving

$$
\boxed{
C_{\mathrm{mean},\mathcal Q}
=C_{\mathcal Q}
=C_{\mathrm{mean},\mathrm{all}}
=C_{\mathrm{TCI}}
=\lambda_{\max}(\Sigma_0).}
$$

The cumulant dual sees the same obstruction directly. Completing the Gaussian square, using
$\ell\ge0$ for the upper bound and $\ell(\theta)\le c_0+c_1\|\theta\|$ for the lower bound,
gives, for each unit $u$,

$$
\log\mathbb E_\pi e^{t u^\top(\theta-\mathbb E\theta)}
=\frac{t^2}{2}u^\top\Sigma_0u+O(|t|).
$$

Thus the optimal linear sub-Gaussian proxy is forced to the prior scale even if local Fisher
information makes $\mathrm{Cov}_\pi=O(n^{-1})$.

### Consequence for the A4 statement

The global $C_{\mathcal Q}$ part of `q:a4-restricted` cannot be posterior-scale for the usual
location-rich mean-field/Gaussian family in logistic regression. A viable theorem must be about
$C_{\mathcal Q,r}$, a bounded parameter family, or a family that excludes remote translations.

## 3. KL localization: what it does and does not guarantee

### Proof: an unrestricted entropy ball can still have infinite $W_2$ radius

Take $\pi(dx)\propto e^{-|x|^p}dx$ with $1\le p<2$ and fix $r>0$. Let
$A_R=[R,R+1]$, $p_R=\pi(A_R)$, and $\pi_R=\pi(\cdot\mid A_R)$. Define

$$
q_R=(1-\varepsilon_R)\pi+\varepsilon_R\pi_R,
\qquad
\varepsilon_R=\frac{r}{2\log(1/p_R)}.
$$

For large $R$, $0<\varepsilon_R<1$. Convexity of relative entropy in its first argument gives

$$
\mathrm{KL}(q_R\|\pi)
\le\varepsilon_R\mathrm{KL}(\pi_R\|\pi)
=\varepsilon_R\log(1/p_R)=r/2.                                  \tag{4}
$$

On the other hand $\log(1/p_R)\asymp R^p$, so

$$
\mathbb E_{q_R}X^2
\ge\varepsilon_R R^2
\asymp rR^{2-p}\longrightarrow\infty.                           \tag{5}
$$

For any coupling, Minkowski's inequality gives

$$
W_2(q_R,\pi)
\ge\left|\sqrt{\mathbb E_{q_R}X^2}-\sqrt{\mathbb E_\pi X^2}\right|.
$$

Equations (4)--(5) prove

$$
\boxed{C_{\mathrm{all},r}(\pi)=\infty\quad\text{for every }r>0.}
$$

The same construction is stronger for polynomial tails. Entropy localization controls the
second moment uniformly only under a quadratic-exponential integrability condition, or after a
family restriction that forbids these tail reweightings.

### Proof: why the current Gaussian-location stress model is finite on a sublevel

For $q_m=N(m,S)$ with fixed $S$ and the same stretched-exponential target,

$$
\mathrm{KL}(q_m\|\pi)=\mathbb E|m+S^{1/2}Z|^p+O(1)\asymp|m|^p
$$

as $|m|\to\infty$. Thus $\{m:\mathrm{KL}(q_m\|\pi)\le r\}$ is bounded. The transport ratio is
continuous away from zero KL (and is globally bounded near a coincident Gaussian target by its
$T_2$ inequality), so $C_{\mathcal Q,r}<\infty$ for this finite-dimensional family. The phrase
“KL sublevel is finite” in `stress-ep-tails` is therefore family-specific, not an unrestricted
entropy-ball principle.

## 4. The exact local/tangent problem

Assume $\pi$ has finite second moment and itself lies in a smooth finite-dimensional family
$q_\eta$ that is differentiable both in quadratic mean and in $W_2$. Let
$s_i=\partial_{\eta_i}\log q_\eta|_{\eta=0}$ and define

$$
F_{ij}=\int s_is_j\,d\pi.
$$

Assume the scores are centered, their weighted Poisson equations have finite-energy solutions,
and let $\phi_i$ solve

$$
-\nabla\!\cdot(\pi\nabla\phi_i)=s_i\pi,
\qquad
G_{ij}=\int\langle\nabla\phi_i,\nabla\phi_j\rangle\,d\pi.
$$

The KL and Wasserstein second-order expansions are

$$
2\,\mathrm{KL}(q_\eta\|\pi)=\eta^\top F\eta+o(\|\eta\|^2),
\qquad
W_2^2(q_\eta,\pi)=\eta^\top G\eta+o(\|\eta\|^2).
$$

### Proof consequence

Provided $F$ is positive definite on identifiable directions and the two displayed second-order
expansions hold uniformly by direction, the infinitesimal restricted
constant is exactly

$$
\boxed{\lambda_{\max}(F^{-1/2}GF^{-1/2}).}                       \tag{6}
$$

For the translation family $q_m=(x\mapsto x+m)_\#\pi$, $G=I$ and
$F=J_{\mathrm{loc}}(\pi)$, the Fisher information matrix for location. Hence the local
translation constant is $1/\lambda_{\min}(J_{\mathrm{loc}})$; for a Gaussian it is
$\lambda_{\max}(\Sigma)$ and agrees with the global value.

Equation (6) is a tractable posterior-scale subtarget: compute the generalized eigenvalue on the
tangent space of a well-specified Gaussian or flow family, then quantify the remainder on a
small KL ball. If the variational gap

$$
\delta_{\mathcal Q}:=\inf_{q\in\mathcal Q}\mathrm{KL}(q\|\pi)
$$

is positive, the sublevel is empty for $r<\delta_{\mathcal Q}$ and the expansion at $\pi$ does
not apply. In that case localization should be parameterized as
$r=\delta_{\mathcal Q}+\rho$, with the nonzero baseline error of the optimizer kept explicit.

## 5. An exact gap between mean and transport constants

The hierarchy in the manuscript can be strict even inside Gaussian variational families. Let
$\pi(dx)\propto e^{-|x|^p}dx$, $1\le p<2$, and take the centered scale family
$\mathcal Q=\{N(0,s^2):s>0\}$. Symmetry gives

$$
C_{\mathrm{mean},\mathcal Q}=0.
$$

But $\mathrm{KL}(N(0,s^2)\|\pi)\asymp s^p$ while
$W_2^2(N(0,s^2),\pi)\gtrsim s^2$, so

$$
C_{\mathcal Q}=\infty.
$$

This is the requested concrete case where the reported mean has a perfect certificate although
ordinary $W_2$ has no finite family-restricted conversion factor. It also shows why the choice of
allowed variational directions, not just the target tail, matters.

## 6. Separated-mixture diagnostic audit and repair

The historical artifact `research/runs/2026-06-20-A4.jsonl` is dirty and is not evidence-eligible.
Its `stress-sep-mixture` record reports

$$
R_{\mathrm{collapse}}=10.1904773,
\qquad
R_{\mathrm{reweight}}=0.6560792,
\qquad
\texttt{reweight\_larger=false},
$$

but its note says the reweighting witness dominates. Inspection explains the contradiction:
the code used $q=N(0,\Delta^2)$, a broad single Gaussian, rather than

$$
q_\varepsilon=(1/2+\varepsilon)\pi_-+(1/2-\varepsilon)\pi_+.
$$

The implementation now sweeps genuine $q_\varepsilon$. A local, uncommitted diagnostic at mode
centres $\pm3$, component standard deviation $1$, gave

$$
R_{\mathrm{collapse}}=10.1905,
\qquad
\max_{\varepsilon\in[10^{-3},0.25]}R(q_\varepsilon)=69.4816
\quad(\varepsilon=10^{-3}).
$$

This only confirms that the corrected witness exercises a different, slower mode at that fixed
separation. It does **not** establish an $e^{c\Delta^2}$ law: that requires a separation sweep,
$\varepsilon$ refinement relative to the overlap floor, and grid/quantile convergence. No run
artifact was generated from the dirty worktree.

## 7. ELBO sign correction

With the repository convention,

$$
\log Z=\mathrm{ELBO}(q)+\mathrm{KL}(q\|\pi).
$$

Therefore an upper bound on $\mathrm{KL}(q^*\|\pi)$ requires an **upper bound on $\log Z$**
together with the computed ELBO. A stronger lower bound on $\log Z$ gives a lower bound on KL,
not the error certificate requested in `q:a4-elbo`. The target notebook, ledger, and manuscript
now use this corrected sign.

## 8. Tractable next targets

### Analytic reductions (historical pre-review list)

1. Remove global $C_{\mathcal Q}$ from the posterior-scale logistic claim for any location-rich
   Gaussian family; it is exactly prior-scale.
2. Use the exact cumulant dual for unrestricted mean certificates.
3. Treat KL localization and family coercivity as separate hypotheses.
4. Use the tangent generalized eigenvalue (6) as the small-radius calibration target.

### Conjectures

1. Under an explicit family-coercivity and target-tail contract, there exists $\rho_0>0$ such
   that for $0\le\rho\le\rho_0$ the optimizer-centered sublevel
   $r=\delta_{\mathcal Q}+\rho$ admits the relevant tangent term plus explicit baseline and
   remainder terms. For misspecification, the expansion must be based at the optimizer rather than
   silently reusing the well-specified formula at $\pi$.
2. In the Gaussian mixture with centers $\pm a$ (separation $2a$), determine the sharp scaling of
   the component-reweighting and single-Gaussian family constants. The current computations are
   lower witnesses only and do not establish exponential or polynomial two-sided laws.

### Proposed tests

1. For the logistic target, optimize $C_{\mathcal Q,r}$ over means and diagonal covariances while
   sweeping $r-\delta_{\mathcal Q}$; compare with (6), not with global $C_{\mathcal Q}$.
2. For the separated mixture, sweep separation, $\varepsilon$ on both sides of the overlap floor,
   spatial resolution, and quantile cutoffs. Report reweighting and mode-collapse families
   separately.
3. For the mean constant, estimate the cumulant proxy directly and compare it with variational
   exponential tilts; remote-$t$ growth must recover $\lambda_{\max}(\Sigma_0)$ in logistic models.

## Validation

- Focused regression:
  `experiments/.venv/bin/python -m pytest -q experiments/tests/test_15_a4_reweighting.py` — passed.
- Direct call to the corrected target returned calibration passed and the fixed-separation values
  above; this was a dirty-tree diagnostic and no JSONL artifact was written.
- The historical A4 JSONL remains unchanged and non-promotable.
