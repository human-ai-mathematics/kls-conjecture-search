# A5 next cycle: orbit connectivity, block stability, and partial noncentring

Date: 2026-08-21

Reviewed nodes: `prop:a5-ratio`, `prop:a5-block-stability`, `ex:a5-gaussian-crossover`,
`prop:a5-partial-gaussian`, `lem:a5-pi-exp-tail`, `ex:a5-neal`, and
`prop:a5-partial-funnel`. Broader targets: `conj:a5-metastable`, `q:a5-qbvm`, `q:a5-detect`,
and `q:a5-reparam`.

Original status: analytic exploration submitted for review. The subsequent independent
certification outcome is recorded at the end. General posterior metastability and quotient BvM
remain conjectural.

## Verdict

Five conclusions survive a sharpness audit.

1. For more than two symmetry wells, the Poincaré exponent is governed by the height at which the
   **whole orbit graph becomes connected**, equivalently the worst-cut bottleneck. The easiest
   pairwise transition can be irrelevant to the slowest global cut.
2. A bounded density-ratio oscillation preserves the invariant and non-invariant gaps block by
   block with the sharp comparison factor $e^{\pm\varepsilon}$.
3. In a scalar Gaussian hierarchy, both $C_P$ and the Gaussian condition number are minimized by
   the exact partial noncentring coefficient $\alpha_*=1/(1+rB)$.
4. The prior-only nonlinear Neal funnel has a singular global-$C_P$ phase: every partial
   coordinate short of full noncentring still has infinite $C_P$.
5. A $\mathbb Z_2$ Gaussian-orbit sequence realizes the raw exponential scale and quotient Fisher
   scale simultaneously. A global density-ratio comparison turns it into a conditional statistical
   bridge, but ordinary BvM or total variation does not.

## 1. Correct barrier: orbit-connectivity height

Let $\mathcal W=G\theta_*$ be a finite orbit of equal-depth population-risk minima and set
$R_*=R(\theta_*)$. For $w\ne w'$ define

$$
H(w,w')=\inf_{\gamma:w\to w'}\max_t\{R(\gamma(t))-R_*\}.        \tag{1}
$$

For $h\ge0$, let $\mathcal G_h$ be the graph on $\mathcal W$ whose edge $ww'$ is present when
$H(w,w')\le h$. Define

$$
\boxed{
\Gamma_{\rm conn}=\inf\{h:\mathcal G_h\text{ is connected}\}. \tag{2}
$$

### Finite-graph proof (subsequently independently checked)

For a nontrivial cut $A\subsetneq\mathcal W$, write

$$
B(A)=\min_{w\in A,w'\notin A}H(w,w').                          \tag{3}
$$

If $\mathcal G_h$ is connected, it crosses every cut, so $B(A)\le h$ for all $A$. Taking the
connectivity threshold gives $\max_A B(A)\le\Gamma_{\rm conn}$. Conversely, for every
$h<\Gamma_{\rm conn}$, choose a connected component $A$ of $\mathcal G_h$. No crossing edge has
height at most $h$, hence $B(A)>h$. Letting $h\uparrow\Gamma_{\rm conn}$ yields

$$
\boxed{
\Gamma_{\rm conn}
=\max_{\varnothing\ne A\subsetneq\mathcal W}
  \min_{w\in A,w'\notin A}H(w,w').}                            \tag{4}
$$

This is also the maximum edge height in a minimum-bottleneck spanning tree.

The previous formula $\min_{w\ne w'}H(w,w')$ only finds the first edge that appears. It equals
(2) precisely when the graph made from minimum-height edges is already connected. For a group
orbit, this says that the minimum-height group moves generate a connected Cayley graph.

### Counterexample

Take four wells indexed by $\mathbb Z_4$. Suppose the step-two transitions $0\leftrightarrow2$
and $1\leftrightarrow3$ have height $1$, while step-one transitions have height $2$. The minimum
pair height is $1$, but at height $1$ the orbit graph has two components. It becomes connected
only at height $2$, so $\Gamma_{\rm conn}=2$.

For $\mathbb Z_2$ there is only one nontrivial edge/cut, so pairwise and connectivity heights
coincide.

### What remains conjectural

Equation (4) is finite-graph algebra. The posterior assertion

$$
\frac1n\log C_P(\pi_n)\to^{\mathbb P}\Gamma_{\rm conn}         \tag{5}
$$

still needs all of the metastability hypotheses: fixed finite orbit, equal-depth free Morse wells,
coercive tails, a quantitative collision-stratum gap, uniform empirical-landscape convergence,
and matching upper/lower capacities with subexponential error. The graph identity corrects the
candidate exponent; it does not prove (5).

## 2. Blockwise density-ratio stability

Let $\pi$ and $\widetilde\pi$ be invariant under the same finite isometry group and use the same
metric carré du champ, with energy obtained by integrating it against the relevant law. Suppose

$$
\operatorname{osc}\log h\le\varepsilon,
\qquad h=\frac{d\widetilde\pi}{d\pi}.                           \tag{6}
$$

Let $m=\operatorname*{ess\,inf}h$ and $M=\operatorname*{ess\,sup}h$. Then $M/m\le e^\varepsilon$.

### Proof (subsequently independently agent-certified)

For every test function,

$$
m\,\operatorname{Var}_\pi(f)
\le\operatorname{Var}_{\widetilde\pi}(f)
\le M\,\operatorname{Var}_\pi(f),                              \tag{7}
$$

because variance is the infimum of $\int(f-c)^2$ over constants. Likewise

$$
m\mathcal E_\pi(f)\le\mathcal E_{\widetilde\pi}(f)
\le M\mathcal E_\pi(f).                                       \tag{8}
$$

The pointwise group average $P_G=|G|^{-1}\sum_g f\circ g$ is the orthogonal projection for both
invariant measures. Hence the invariant sector and $\ker P_G$ are the same function spaces for
both Rayleigh problems. Combining (7)--(8) *before* normalizing $h$ gives the sharper factor
$M/m$, not the wasteful product of two separate $e^{\pm\varepsilon}$ bounds:

$$
\boxed{
e^{-\varepsilon}\lambda_b(\pi)
\le\lambda_b(\widetilde\pi)
\le e^\varepsilon\lambda_b(\pi),
\quad b\in\{\mathrm{inv},\mathrm{noninv}\}.}                   \tag{9}
$$

Thus

$$
\lambda_{\rm noninv}(\pi)<e^{-2\varepsilon}\lambda_{\rm inv}(\pi)
\quad\Longrightarrow\quad
\lambda_{\rm noninv}(\widetilde\pi)<\lambda_{\rm inv}(\widetilde\pi). \tag{10}
$$

The log-ordering margin is $2\varepsilon$. Equation (9) also compares the quotient and raw gaps,
but it does **not** stabilize individual eigenvectors. Davis--Kahan-type projector control needs
an isolated eigenvalue and an operator-norm comparison in a common Hilbert space.

## 3. Exact scalar partial noncentring

Consider

$$
u\sim N(0,A),\qquad \theta\mid u\sim N(u,B),\qquad
L_y(\theta)\propto e^{-r(\theta-y)^2/2},qquad A,B>0, r\ge0.   \tag{11}
$$

For $z_\alpha=\theta-\alpha u$, the quadratic posterior precision in $(u,z_\alpha)$ is

$$
H_\alpha=
\begin{pmatrix}
A^{-1}+(1-\alpha)^2B^{-1}+r\alpha^2&-(1-\alpha)B^{-1}+r\alpha\\
-(1-\alpha)B^{-1}+r\alpha&B^{-1}+r
\end{pmatrix}.                                                  \tag{12}
$$

### Proof (subsequently independently agent-certified)

The coordinate change is a determinant-one shear, so $\det H_\alpha$ is constant in $\alpha$.
For a $2\times2$ positive-definite matrix at fixed determinant, the smaller eigenvalue decreases
and the condition number increases with the trace. Direct expansion gives

$$
\operatorname{tr}H_\alpha
=\text{constant}+(B^{-1}+r)\alpha^2-2B^{-1}\alpha.             \tag{13}
$$

Therefore both $C_P=1/\lambda_{\min}(H_\alpha)$ and
$\kappa_P=\operatorname{cond}(H_\alpha)$ have the unique minimizer

$$
\boxed{\alpha_*=\frac{B^{-1}}{B^{-1}+r}=\frac{1}{1+rB}.}       \tag{14}
$$

At $r=0$, full noncentring is optimal; as $rB\to\infty$, the optimum tends to centring. The prior
variance $A$ affects the achieved eigenvalues but cancels from (14). In the unit model, the two
endpoints tie at $r=1$, but the partial optimum is then $\alpha_*=1/2$ and is strictly better than
either endpoint.

This is exact finite-dimensional Gaussian algebra. It is not evidence that a nonlinear funnel
has a smooth partial-$C_P$ optimum.

## 4. Nonlinear partial Neal funnel

For the prior-only canonical funnel,

$$
s>0,\qquad u\sim N(0,s^2),\qquad z\sim N(0,1),\qquad \theta=e^u z. \tag{15}
$$

Define

$$
z_\alpha=e^{-\alpha u}\theta=e^{(1-\alpha)u}z,
\qquad 0\le\alpha\le1.                                        \tag{16}
$$

### Proof (subsequently independently second-audited)

For $\beta=1-\alpha>0$, conditioning on $|z|\ge1$ shows

$$
\mathbb E\exp(c|z_\alpha|)
\ge \mathbb P(|z|\ge1)\,
\mathbb E\left[e^{c e^{\beta u}}\mathbf 1_{\{u>0\}}\right]
=\infty
\quad(c>0).                                                     \tag{17}
$$

In the Euclidean $(u,z_\alpha)$ coordinates, $z_\alpha$ is itself a one-Lipschitz observable.
It lies in $L^2$, since $\mathbb E z_\alpha^2=e^{2(1-\alpha)^2s^2}$, while the exponential
integral diverges because $ce^{(1-\alpha)u}-u^2/(2s^2)\to+\infty$.
A truncation argument now supplies the missing implication: for a one-Lipschitz $f$ and median
$m$, apply Poincaré to
$g=\min\{(f-m-t)_+,2\sqrt{C_P}\}$. The independent-copy variance identity shows that increasing
$t$ by $2\sqrt{C_P}$ halves the upper tail; applying the same argument to $-f$ gives a two-sided
exponential moment. Thus a finite Poincaré inequality would give some exponential integrability
for the centred coordinate, contradicting (17). Consequently

$$
C_P(u,z_\alpha)=\infty\quad(0\le\alpha<1),qquad
C_P(u,z_1)=\max\{s^2,1\}.                                      \tag{18}
$$

The prior-only global-$C_P$ phase is therefore singular: there is no finite interior objective
to optimize. The potential in partial coordinates also has unbounded Hessian for $\alpha<1$, so
$L_VC_P$ does not repair the objective.

Adding data multiplies the density by $L(y\mid e^{\alpha u}z_\alpha)$. This can alter (17), but
the result depends on likelihood tail coercivity. A local or high-probability bi-Lipschitz bound
cannot prove a global Poincaré inequality. A data-dependent partial-funnel theorem must first pass
an exponential-moment test, then supply a global Lyapunov/capacity argument.

## 5. Exact $\mathbb Z_2$ bridge

Fix $a,\sigma>0$ and set

$$
\mu_n=\tfrac12N(-a,\sigma^2/n)+\tfrac12N(a,\sigma^2/n),
\qquad \bar\mu_n=|\cdot|_\#\mu_n.                              \tag{19}
$$

The folded-well Hardy calculation at within-well standard deviation $s_n=\sigma/\sqrt n$ gives

$$
\log\frac{C_P(\mu_n)}{\sigma^2/n}
=\frac{na^2}{2\sigma^2}+O\!\left(\log\left(1+\frac{a\sqrt n}{\sigma}\right)\right). \tag{20}
$$

Hence

$$
\frac1n\log C_P(\mu_n)\longrightarrow\frac{a^2}{2\sigma^2}.  \tag{21}
$$

On the quotient,

$$
\bar\mu_n=\operatorname{Law}|a+\sigma Z/\sqrt n|.
$$

The map from $Z$ is $\sigma/\sqrt n$-Lipschitz, so
$C_P(\bar\mu_n)\le\sigma^2/n$. The quotient-coordinate variance tends to the same scale, giving

$$
nC_P(\bar\mu_n)\longrightarrow\sigma^2.                        \tag{22}
$$

The limiting risk $R(x)=(|x|-a)^2/(2\sigma^2)$ has two wells and
$\Gamma_{\rm conn}=a^2/(2\sigma^2)$, so (21)--(22) realize both A5 scales exactly in a canonical
Gaussian-orbit sequence.

### Conditional statistical transfer

Let $\widetilde\mu_n$ be a genuine $\mathbb Z_2$-invariant posterior satisfying the **global**
comparison

$$
\varepsilon_n=\operatorname{osc}\log\frac{d\widetilde\mu_n}{d\mu_n}.
$$

Equation (9) implies:

- if $\varepsilon_n=o(n)$, the raw logarithmic exponent (21) transfers;
- if $\varepsilon_n=o(1)$, the quotient leading constant (22) transfers.

This is a conditional analytic proof draft under a strong hypothesis. Total-variation BvM does
not supply that hypothesis, and a local density ratio on a high-probability set is insufficient
without a tail extension. Thus the example is not a proof of general quotient BvM.

## 6. Symmetrization link to A4

For any $q\ll\pi$ with invariant target $\pi$, define
$\bar q=|G|^{-1}\sum_g g_\#q$. Convexity of KL and averaging isometric couplings give

$$
\mathrm{KL}(\bar q\|\pi)\le\mathrm{KL}(q\|\pi),
\qquad W_2^2(\bar q,\pi)\le W_2^2(q,\pi).                       \tag{23}
$$

Every invariant observable is preserved. This identifies the correct VI reduction for scientific
quantities on the quotient, subject to the important caveat that the chosen variational family
must contain $\bar q$. It does not compare the transport/KL ratio because both terms decrease.

## 7. Computations and stop/go criteria

### Near-term go

1. Unit-test (14) against a dense $\alpha$ grid for unequal $A,B,r$ and check both $C_P$ and
   condition number.
2. Unit-test (2)--(4) on a four-node barrier matrix where the easiest edge fails to connect the
   orbit.
3. Use (9) for a global oscillation comparison in an exact finite-state or Gaussian-orbit model.
4. For a real $\mathbb Z_2$ posterior, attempt a global density-ratio proof after quotient
   rescaling; explicitly split the main chamber from tails and collision regions.

### Stop

1. Stop a metastable exponent calculation if it uses the minimum pair barrier without checking
   connectivity of the minimum-height orbit graph.
2. Stop a block-ordering claim if the observed margin is at most the comparison uncertainty
   $2\varepsilon$ or if only one fitted eigenvector was classified.
3. Stop optimizing global $C_P$ over nonlinear partial funnel coordinates until finite
   exponential moments have been established.
4. Stop a quotient-BvM constant claim based only on total variation or local weak convergence.

## Certification outcome (independent review, 2026-08-21)

The independent audit `/root/review_a4_a5` accepted:

- `prop:a5-ratio` and `prop:a5-block-stability`;
- `ex:a5-gaussian-crossover`; and
- `prop:a5-partial-gaussian` / `eq:a5-partial-optimum`.

The finite worst-cut/connectivity identity was also checked, but it is only an algebraic component
of the still-open `conj:a5-metastable`; it does not promote that conjecture.

The audit supplied the missing truncation proof behind the Neal-funnel exponential-integrability
step. A separate second audit by `/root/cross_review` then accepted `lem:a5-pi-exp-tail`,
`ex:a5-neal`, and `prop:a5-partial-funnel` after the necessary $s>0$ hypothesis and all
integrability steps were made explicit. Their dossiers now record `checked_by: agent` and the
second-review path.
`ex:a5-folding` and `ex:a5-z2-bridge` remain unpromoted because the raw Hardy asymptotic was not
independently closed. General metastability and quotient BvM remain open. Ledger and
shared-knowledge updates were subsequently applied while this dated note was retained as the
analytic record.
