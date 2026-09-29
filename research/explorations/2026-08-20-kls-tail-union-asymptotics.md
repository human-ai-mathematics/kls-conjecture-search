---
---
# Tail-union alignment at high dimension

Date: 2026-08-20

Status: analytical exploration. Sections 2 and 3 contain proved finite-dimensional identities.
Proposition 4.1 proves only local, fixed-time point-process convergence on bounded boundary
windows. The passage from that point process to the full source observable, the small-time
formulas in Section 6, and every assertion involving the pathwise stopping time are explicitly
labelled formal or conjectural. The Monte Carlo calculation in Section 9 is a model diagnostic,
not proof.

## 1. Outcome

The rise of the measured stopped occupation

\[
\mathbb E\int_0^{0.5\wedge\tau}S_t^H\,dt
\]

from roughly (10^{-2}) at (n=16) to roughly (5\times10^{-1}) at (n=1024) is consistent
with a slow crossover to a finite rare-event Poisson limit. It is not currently evidence for
growth to infinity.

The mechanism is unusually explicit. Write \(\beta=\sqrt2\) for the rate of the isotropic
Laplace marginal and (L=\log 2). At each fixed (0<t<1/2), the observations relevant to one
side of the tail boundary have the form

\[
c=\beta+t a_n+\sqrt t\,z,
\]

and the two signed boundary clouds have limiting intensity

\[
\rho_t(z)\,dz
=kL\exp(-k^2/2-kz)\,dz,
\qquad k=\frac{\beta}{\sqrt t}.
\tag{1.1}
\]

At such a point the posterior tail probability and the two hazard derivatives converge to

\[
\lambda(z)=\Phi(z),\qquad
d(z)=\frac{\eta(z)}{\sqrt t},\qquad
h(z)=\frac{\eta(z)(\eta(z)-z)}{t},
\qquad
\eta(z)=\frac{\phi(z)}{\Phi(-z)}.
\tag{1.2}
\]

The limiting posterior covariance is (1/t>2), so these are precisely high coordinates. The
intensity has infinite mass at \(-\infty\), but all source-relevant weighted sums are finite.
The identity

\[
\int_{\mathbb R}\rho_t(z)\Phi(z)\,dz=L
\tag{1.3}
\]

also shows why the global tail-union mass remains nondegenerate.

A formal small-(t) evaluation of this cloud gives

\[
\begin{aligned}
\mathbb E r_t
&\sim C_*t^{-3/2}e^{-1/(2t)},\\
\mathbb E D_t
&\sim 2C_*t^{-5/2}e^{-1/(2t)},\\
\mathbb E S_t^H
&\sim C_*t^{-5/2}\left(\frac1{2t}+\frac12\right)e^{-1/(2t)},
\qquad
C_*=\frac{L\beta}{2\sqrt\pi}.
\end{aligned}
\tag{1.4}
\]

Thus

\[
\frac{\mathbb E S_t^H}{\mathbb E D_t}
\sim \frac1{4t}+\frac14.
\tag{1.5}
\]

Damping does **not** absorb the narrow early source pulse pointwise: near the formal source peak
(t=(\sqrt{14}-3)/5\simeq0.1483), the ratio in (1.5) is about (1.94). On the other hand, the
source density itself tends to zero super-exponentially as (t\downarrow0), and its formal peak
is finite, about (4.34). The most plausible conclusion is therefore neither “damping absorbs
everything” nor “the required (C_0) diverges,” but rather:

> The tail union produces a bounded (O(1)) source pulse. Damping and (r) reduce its broad-time
> occupation, while the absolute (C_0|I|) term must pay for a finite residual on short windows.

Turning this into a theorem requires a uniform-in-(n,t) envelope and a path-space treatment of
the balance stopping time. Those steps are not proved here.

## 2. Exact finite-(n) product formulas

Let the one-dimensional posterior at localization state ((c_i,t)) be

\[
\nu_i(dx)\propto
\exp\left(c_ix-\frac t2x^2\right)\frac\beta2e^{-\beta|x|}\,dx,
\qquad \beta=\sqrt2.
\]

Put

\[
F_i=\{|X_i|<a_n\},\qquad
z_i=\nu_i(F_i),qquad
u_i=\mathbb E_i[X_i\mid F_i],\qquad
w_i=\operatorname{Var}_i(X_i\mid F_i),
\]

and let (m_i,A_i) be the full posterior mean and variance. Define

\[
d_i=m_i-u_i,qquad h_i=A_i-w_i,qquad
q=\prod_{i=1}^nz_i,qquad p=1-q,qquad s=pq.
\tag{2.1}
\]

Here (q) is the posterior mass of the product complement
(F=\bigcap_iF_i), while (p) is the posterior mass of the tail union (E=F^c).

### Lemma 2.1 (mixture reconstruction; proved)

If

\[
\delta=\mathbb E[X\mid E]-\mathbb E[X\mid F],
\qquad
G=\operatorname{Cov}(X\mid E)-\operatorname{Cov}(X\mid F),
\]

then

\[
\delta_i=\frac{d_i}{p},
\qquad
G=\operatorname{diag}\left(\frac{h_i}{p}\right)-\frac{q}{p^2}dd^T.
\tag{2.2}
\]

#### Proof

Conditioning on (F) preserves the product structure, so its mean is (u=(u_i)) and its
covariance is (W=\operatorname{diag}(w_i)). The mean mixture identity gives
(m=p\mathbb E[X\mid E]+qu), hence (m-u=p\delta=d). The covariance mixture identity is

\[
A=p\operatorname{Cov}(X\mid E)+qW+pq\delta\delta^T.
\]

Subtract (W), divide by (p), and use (A-W=\operatorname{diag}(h_i)). \(\square\)

For a high set (H=\{i:A_i\ge2\}), put

\[
R=\sum_i d_i^2,quad R_H=\sum_{i\in H}d_i^2,quad
K_H=\sum_{i\in H}h_i^2,quad J_H=\sum_{i\in H}h_id_i^2.
\tag{2.3}
\]

### Lemma 2.2 (exact observables; proved)

The information, damping, and incident-high source are

\[
r=\frac qpR,
\tag{2.4}
\]

\[
D=\frac{2q}{p}\sum_iA_id_i^2-\left(\frac qp\right)^2R^2,
\tag{2.5}
\]

and

\[
S^H=pq\left[
\frac{K_H}{p^2}-\frac{2qJ_H}{p^3}
+\frac{q^2}{p^4}\left(2R_HR-R_H^2\right)
\right].
\tag{2.6}
\]

#### Proof

Equations (2.4) and (2.5) follow by substituting (delta=d/p) in

\[
r=s|\delta|^2,qquad D=2s\delta^TA\delta-r^2.
\]

For (2.6), square the diagonal entries
(G_{ii}=h_i/p-qd_i^2/p^2), add all off-diagonal squares incident to (H), and note that

\[
\sum_{i,j:\ i\in H\text{ or }j\in H}d_i^2d_j^2
=2R_HR-R_H^2.
\]

Multiplication by (s=pq) gives the result. \(\square\)

These formulas are implemented, without dense matrices, in
`experiments/finum/localization/tail_union.py`.

## 3. Exact hazard identities

Let

\[
\ell_i(c_i,t)=-\log z_i(c_i,t).
\]

### Lemma 3.1 (log-survival derivatives; proved)

At fixed (t),

\[
\partial_{c_i}\ell_i=d_i,
\qquad
\partial_{c_i}^2\ell_i=h_i.
\tag{3.1}
\]

#### Proof

Exponential-family differentiation gives

\[
\partial_{c_i}\log z_i=u_i-m_i=-d_i.
\]

Differentiating once more and using
(partial_{c_i}u_i=w_i), (partial_{c_i}m_i=A_i), gives
(partial_{c_i}^2\log z_i=w_i-A_i=-h_i). \(\square\)

There is also a useful exact mixture form. If (arepsilon_i=1-z_i), and (v_i,b_i) are the
mean and variance conditional on (F_i^c), then

\[
d_i=\varepsilon_i(v_i-u_i),
\qquad
h_i=\varepsilon_i(b_i-w_i)+z_i\varepsilon_i(v_i-u_i)^2.
\tag{3.2}
\]

This identifies (d_i,h_i) as first and second derivatives of a one-coordinate tail hazard; it
also shows that squared source terms are governed by second moments of rare posterior hazards,
up to polynomial tail-displacement factors.

The balanced radius is exact:

\[
e^{-\beta a_n}=1-2^{-1/n},
\qquad
n e^{-\beta a_n}\longrightarrow L=\log2,
\qquad
a_n=\frac{\log n-\log L+o(1)}{\beta}.
\tag{3.3}
\]

## 4. A proved fixed-time boundary point process

Use the filtering representation

\[
C_i(t)=tX_i+B_i(t),
\]

where (X_i) are independent isotropic Laplace variables and (B_i) are independent Brownian
motions. It has exactly the same one-time localization-state law as the drifted tilt process.

The density of (C_i(t)) admits the exact decomposition

\[
g_t(c)=\frac{\beta}{2t}e^{\beta^2/(2t)}\left[
e^{-\beta c/t}\Phi\left(\frac{c-\beta}{\sqrt t}\right)
+e^{\beta c/t}\Phi\left(\frac{-c-\beta}{\sqrt t}\right)
\right].
\tag{4.1}
\]

This follows by completing the square separately on the positive and negative half-lines.

### Proposition 4.1 (bounded-window Poisson convergence; proved)

Fix (t>0). For each sign (sigma\in\{-1,1\}), center a signed observation by

\[
Z_{i,\sigma}^{(n)}=
\frac{\sigma C_i(t)-\beta-ta_n}{\sqrt t}.
\]

On every bounded collection of (z)-intervals, the combined point counts from the two signs
converge jointly to those of a Poisson point process with intensity (1.1).

#### Proof

For bounded (z), substitute (c=\beta+ta_n+\sqrt t,z) in (4.1). The first Gaussian CDF tends
to one uniformly on bounded (z)-sets, and the second term is negligible. Using (3.3),

\[
2n\,g_t(\beta+ta_n+\sqrt t,z)\sqrt t
\longrightarrow
\frac{\beta}{\sqrt t}L
e^{-\beta^2/(2t)-\beta z/\sqrt t}
=\rho_t(z).
\]

The factor two accounts for the positive and negative boundaries. A single coordinate cannot
hit bounded windows at both boundaries once (n) is large. Counts in disjoint windows are
therefore multinomial rare-event counts with cell probabilities (O(1/n)), and the elementary
Poisson limit for multinomials gives joint convergence. \(\square\)

### Lemma 4.2 (posterior boundary moments; proved pointwise)

At (c=\beta+ta_n+\sqrt t,z), for fixed (t>0,z\in\mathbb R), the standardized posterior
variable (U=\sqrt t(X-a_n)) converges in moments to (N(z,1)). Consequently the one-sided tail
probability, (d_i), (h_i), and (A_i) converge to (1.2) and

\[
A_i\longrightarrow\frac1t.
\tag{4.2}
\]

#### Proof

On the positive half-line the posterior is a (N((c-\beta)/t,1/t)) density truncated at zero.
Its untruncated mean is (a_n+z/\sqrt t), whose distance from zero in posterior standard
deviations tends to infinity. The negative half-line has vanishing posterior mass. Thus
(U\Rightarrow N(z,1)), with Gaussian domination giving moment convergence. Conditioning on
(X<a_n) becomes conditioning (U<0). For (U\sim N(z,1)),

\[
\mathbb E[U\mid U<0]=z-\eta(z),qquad
\operatorname{Var}(U\mid U<0)=1+z\eta(z)-\eta(z)^2,
\]

which gives (1.2) and (4.2). The negative boundary is identical after reflection. \(\square\)

In particular, every boundary point is high in the limit when (t<1/2). The endpoint (t=1/2)
is singular for the hard threshold (A_i\ge2): the limiting covariance equals exactly two, while
finite-state Brascamp--Lieb gives (A_i\le1/t). This endpoint has zero time measure but should not
be used for a pointwise convergence claim about the indicator.

## 5. What the point process does and does not prove

The limiting intensity has infinite total mass because it grows at \(-\infty\). Nevertheless,

\[
\int_{\mathbb R}\rho_t(z)\Phi(z)\,dz=L.
\tag{5.1}
\]

Indeed, for (k>0), integration by parts gives

\[
\int_{\mathbb R}e^{-kz}\Phi(z)\,dz=\frac{e^{k^2/2}}{k}.
\]

Therefore the Poisson product

\[
q_\infty=\prod_j\Phi(-Z_j)
\]

is well-defined, and its Poisson Laplace functional gives

\[
\mathbb E q_\infty
=\exp\left(-\int\rho_t(z)\Phi(z)\,dz\right)
=e^{-L}=\frac12.
\tag{5.2}
\]

For every fixed (t>0), the weighted integrals associated with (d^2,h^2), and (hd^2) are
finite: Gaussian decay wins at \(-\infty\), while the factor (e^{-kz}) wins at (+\infty\).
This makes a finite fixed-time limiting source highly plausible.

What is **not** proved by Proposition 4.1 is:

1. uniform integrability of the full rational observable (2.6), including rare small-(p)
   states;
2. negligibility of all coordinates outside bounded boundary windows, uniformly in (n);
3. convergence jointly as a process in (t);
4. convergence after multiplication by (1_{\{t<\tau\}}), where \(\tau\) is the first exit of
   (p_t) from ([1/3,2/3]).

On the stopped set the denominators in (2.4)--(2.6) are harmless, since (p,q\in[1/3,2/3]).
The unresolved issue is a uniform envelope and path-space tightness, not an algebraic
singularity on the stopped interval.

## 6. Formal small-time asymptotics of the Poisson cloud

This section is a formal Laplace calculation, not a proved interchange of the limits
(n\to\infty), (t\downarrow0), expectation, and stopping.

Let (k=\beta/\sqrt t\). When (t\downarrow0), the cloud contains very many points with very
small hazards. Equation (5.1) and the decay of the second hazard moment suggest

\[
p_\infty,q_\infty\longrightarrow\frac12
\quad\text{in probability}.
\tag{6.1}
\]

At the saddle relevant to squared moments, (z\sim-k/2\), so

\[
\eta(z)\sim\phi(z),qquad
d^2\sim\frac{\phi(z)^2}{t},qquad
h^2\sim\frac{z^2\phi(z)^2}{t^2}.
\]

The two Gaussian integrals are exact:

\[
\begin{aligned}
\int_{\mathbb R}e^{-kz}\phi(z)^2\,dz
&=\frac{e^{k^2/4}}{2\sqrt\pi},\\
\int_{\mathbb R}z^2e^{-kz}\phi(z)^2\,dz
&=\frac{e^{k^2/4}}{2\sqrt\pi}
\left(\frac{k^2}{4}+\frac12\right).
\end{aligned}
\tag{6.2}
\]

Inserting (6.2) into (2.4)--(2.6), replacing (p,q) by (1/2), and observing that the rank-one
corrections and the (r^2) term are lower at this exponential scale yields (1.4). In particular,

\[
\mathbb E S_t^H=O\left(t^{-7/2}e^{-1/(2t)}\right)\longrightarrow0.
\tag{6.3}
\]

The full expression displayed in (1.4) has its maximum at

\[
t_S=\frac{\sqrt{14}-3}{5}=0.148331\ldots,
\qquad
S_{\rm formal}(t_S)=4.34034\ldots.
\tag{6.4}
\]

The leading damping and information profiles peak at (t_D=1/5) and (t_r=1/3), respectively.
This separation explains why damping looks more effective on broad intervals than at the source
peak. It does not imply that (alpha D) with (alpha<1) absorbs the source on every broad
interval.

For orientation only, integrating the three formal profiles over ([0,0.5]) gives

\[
\int S_{\rm formal}=1.0813,qquad
\int D_{\rm formal}=0.7935,qquad
\int r_{\rm formal}=0.1090.
\tag{6.5}
\]

The small-(t) approximation is not quantitatively controlled near (t=0.5), and (6.5) is
unstopped. It should not be compared to a stopped finite-(n) run as though it were a prediction
with error bars.

## 7. Shrinking times and the remaining uniformity gap

The only way the interval quotient

\[
\frac{1}{|I_n|}\mathbb E\int_{I_n\cap[0,\tau]}
\left(S_t^H-C_1r_t-\alpha D_t\right)dt
\tag{7.1}
\]

could diverge while every fixed-time limit remains finite is through intervals (I_n) moving
toward zero or through failure of uniform integrability. The natural crossover scale is
(t=\kappa/a_n\asymp1/\log n).

Here is the relevant logarithmic-scale calculation. Set (a=a_n), (t=\kappa/a), scale a
positive latent coordinate as (x=ay), and keep the observation (c) of order one. The joint
large-deviation cost per (a) is

\[
\beta y+\frac{(c-\kappa y)^2}{2\kappa},\qquad y\ge0.
\]

The marginal observation rate is therefore

\[
I_\kappa(c)=
\begin{cases}
c^2/(2\kappa),&c\le\beta,\\
\beta c/\kappa-\beta^2/(2\kappa),&c\ge\beta,
\end{cases}
\tag{7.2}
\]

while the posterior tail probability has exponential rate

\[
J_\kappa(c)=
\begin{cases}
\beta+\kappa/2-c,&c\le\beta,\\
(\beta+\kappa-c)^2/(2\kappa),&\beta\le c\le\beta+\kappa,\\
0,&c\ge\beta+\kappa.
\end{cases}
\tag{7.3}
\]

Minimizing (I_\kappa+2J_\kappa-\beta) gives

\[
c_\kappa=
\begin{cases}
\beta-\kappa,&0<\kappa\le\beta/2,\\
\beta^2/(4\kappa),&\kappa\ge\beta/2,
\end{cases}
\qquad c_\kappa>0.
\tag{7.4}
\]

Thus the Laplace principle predicts, at the exponential scale,

\[
n\,\mathbb E[\lambda_i(t)^2]
=\exp(-a_nc_\kappa+o(a_n)).
\tag{7.5}
\]

Polynomial factors in (a_n), such as the tail-displacement factors in (3.2), cannot defeat
(7.5). Hence the (t=\kappa/a_n) regime should have vanishing, not exploding, source density.

Equations (7.2)--(7.5) are a checked Laplace-principle derivation, but this note does **not** claim
a finite-(n), uniform theorem from them. Such a theorem still needs uniform remainder estimates,
control outside compact (c)-sets, and insertion into the rational global formula (2.6).

The two formal regimes cover every proposed sequence (t_n\downarrow0):

- if (a_nt_n=O(1)), (7.5) predicts exponential decay in (a_n);
- if (a_nt_n\to\infty), the boundary saddle is separated from the Laplace cusp and (6.3)
  predicts polynomial-in-(1/t_n) times (e^{-1/(2t_n)}).

This is strong evidence against a shrinking-window blowup, but the uniform bridge between the two
regimes is the exact missing proof.

## 8. Interpretation of the current dimension trend

A power-law fit to (n=16,\ldots,1024) is misleading because these dimensions straddle the
Laplace-cusp crossover. At the squared-source saddle (z=-k/2), the untruncated posterior mean is

\[
x_*(t,n)=a_n-\frac{\beta}{2t}.
\tag{8.1}
\]

The Gaussian boundary approximation starts turning on when (x_*\gtrsim0), equivalently

\[
t\gtrsim\frac{\beta}{2a_n}\sim\frac1{\log n}.
\tag{8.2}
\]

At the limiting source peak (t\simeq0.1483), the crossover occurs near (a_n\simeq4.77), or
(n\simeq6\times10^2). Dimensions (512) and (1024) are therefore exactly where a sharp rise
should appear. True convergence is much slower: the relevant distance from the cusp in posterior
standard deviations is

\[
\chi_n(t)=a_n\sqrt t-\frac{\beta}{2\sqrt t},
\tag{8.3}
\]

and one needs (chi_n(t)\gg1), not merely (chi_n(t)>0), for the half-line truncation to be
negligible. This explains why the finite-(n) source density near (1.3) at (n=512) can still
be far below the Poisson-cloud value near (4.5).

Consequently, the plausible asymptotic scaling is

\[
\mathbb E\int_0^{0.5\wedge\tau}S_t^Hdt=O(1)
\quad\text{with a slow crossover in }a_n\asymp\log n,
\tag{8.4}
\]

not (n^\gamma) or a positive power of (log n). Equation (8.4) is a conjectural conclusion,
not a proved bound.

For (7.1), the prediction is correspondingly precise:

- no interval should force divergence for fixed (C_1\ge0) and (0\le\alpha<1);
- short intervals near (t\simeq0.15) can retain a positive (O(1)) residual even for
  (alpha) close to one, because (S^H/D>1) there;
- a universal absolute term (C_0|I|), rather than damping alone, is expected to cover that
  residual.

## 9. Reproducible cutoff-PPP calculation

The following script samples the limiting Poisson cloud above a cutoff (z_0). The very dense
lower cloud is replaced by its deterministic Campbell mean in the additive statistics
(\log q,\sum d^2,\sum h^2,\sum hd^2). This replacement is accurate when its fluctuations are
small, but it is another approximation. The second triple in each output row is additionally
masked by the **current** condition (p\in[1/3,2/3]); it is not first-exit stopping.

Run from the repository root with `experiments/.venv/bin/python`:

```python
import numpy as np
from scipy.integrate import quad
from scipy.special import log_ndtr

BETA = np.sqrt(2.0)
L = np.log(2.0)
LOG_2PI = np.log(2.0 * np.pi)
rng = np.random.default_rng(20260820)


def run(t, z0, reps=3000):
    k = BETA / np.sqrt(t)
    log_C = np.log(k * L) - k * k / 2.0
    mean_count = L * np.exp(-k * k / 2.0 - k * z0)

    def fields(z):
        log_Q = log_ndtr(-z)
        eta = np.exp(-z * z / 2.0 - LOG_2PI / 2.0 - log_Q)
        d2 = eta * eta / t
        h = eta * (eta - z) / t
        return log_Q, d2, h * h, h * d2

    background = [
        quad(
            lambda z, j=j: np.exp(log_C - k * z) * fields(z)[j],
            -14.0,
            z0,
            epsabs=1e-9,
            limit=100,
        )[0]
        for j in range(4)
    ]

    values = []
    for _ in range(reps):
        z = z0 + rng.exponential(1.0 / k, rng.poisson(mean_count))
        log_Q = log_ndtr(-z)
        eta = np.exp(-z * z / 2.0 - LOG_2PI / 2.0 - log_Q)
        d2 = eta * eta / t
        h = eta * (eta - z) / t

        q = np.exp(background[0] + log_Q.sum())
        p = 1.0 - q
        s = p * q
        R = background[1] + d2.sum()
        K = background[2] + np.dot(h, h)
        J = background[3] + np.dot(h, d2)

        norm_G2 = K / p**2 - 2.0 * q * J / p**3 + q * q * R * R / p**4
        source = s * norm_G2
        information = s * R / p**2
        damping = 2.0 * s * R / (t * p**2) - information**2
        values.append((source, information, damping, p))

    values = np.asarray(values)
    balanced = (values[:, 3] >= 1.0 / 3.0) & (values[:, 3] <= 2.0 / 3.0)
    mean = values[:, :3].mean(axis=0)
    masked = (values[:, :3] * balanced[:, None]).mean(axis=0)
    return mean_count, mean, masked, balanced.mean()


for t, z0 in [
    (0.05, -4.5),
    (0.10, -4.0),
    (0.15, -4.0),
    (0.20, -4.0),
    (0.30, -4.0),
    (0.40, -4.0),
    (0.49, -4.0),
]:
    count, mean, masked, balance = run(t, z0)
    print(
        f"{t:.2f} {count:.0f} "
        + " ".join(f"{x:.3f}" for x in mean)
        + " | "
        + " ".join(f"{x:.3f}" for x in masked)
        + f" | {balance:.3f}"
    )
```

The seeded output on the current environment is

```text
# t  mean simulated count   mean(S,r,D)       current-balance-masked(S,r,D)  P(balance)
0.05 3275 0.234 0.001 0.043 | 0.234 0.001 0.043 | 1.000
0.10 1848 3.272 0.061 1.203 | 3.266 0.060 1.181 | 0.999
0.15 1944 4.493 0.178 2.311 | 4.463 0.170 2.225 | 0.994
0.20 1455 4.056 0.263 2.529 | 3.994 0.246 2.378 | 0.983
0.30  756 2.638 0.359 2.228 | 2.441 0.298 1.866 | 0.901
0.40  436 1.686 0.369 1.683 | 1.386 0.284 1.299 | 0.775
0.49  291 1.160 0.368 1.343 | 0.844 0.249 0.911 | 0.666
```

Changing (z_0) among (-3.5,-4,-4.5) changes the reported source means at
(t=0.10,0.15,0.20) by about two percent in a 1500-replicate check. This is a cutoff diagnostic,
not a rigorous error estimate.

## 10. Decisive numerical runs

The next computation should separate fixed-time convergence from first-exit stopping.

### 10.1 Fixed-time sweep first

Use independent one-time filtering states, without path simulation, at

\[
n=2^{10},2^{12},2^{14},2^{16},2^{18}
\]

and

\[
t=0.05,0.075,0.10,0.125,0.15,0.175,0.20,0.25,0.35,0.45.
\]

Report unmasked means and means masked by current balance for (S^H,S,r,D,p), with at least
256 states at the smaller dimensions and enough states at larger (n) to put a useful confidence
interval on (S^H-\alpha D-C_1r). Also report the crossover coordinate (\chi_n(t)) from (8.3).
Compare directly with the cutoff-PPP calculation. This is much cheaper and more diagnostic than
increasing full-path dimension first.

If resources permit, include (2^{20}) in the fixed-time sweep. The normal boundary limit is slow;
dimensions only through (2^{14}) may still look like growth rather than saturation.

### 10.2 Full stopped paths

After the fixed-time limit is visible, run full filtering paths at

\[
n=2^{10},2^{12},2^{14},2^{16}
\]

with horizon (0.5), at least 128--256 paths, (dt\le0.0025), and a paired refinement at
(dt/2). Concentrate deterministic windows around the predicted pulse:

\[
|I|=0.005,0.01,0.02,0.05,0.10,0.20,0.50,
\]

with starts on a (0.005) grid over (t\in[0.05,0.30]). Record both the separately averaged
terms and the directly paired path variable

\[
\int_{I\cap[0,\tau]}(S^H-\alpha D-C_1r)dt.
\]

The paired variable is essential because source and damping are strongly correlated.

### 10.3 Explicit shrinking-time falsification sweep

To test the only remaining divergence mechanism, include windows centered at

\[
t=\frac{\kappa}{a_n},
\qquad
\kappa\in\left\{\frac\beta4,\frac\beta2,\beta,2\beta,4\beta\right\},
\]

with widths (0.1t,0.25t,0.5t). Plot the source density against (a_n), and compare its logarithm
to the rate (c_\kappa a_n) in (7.4). Also include fixed-(t) windows near (0.15); otherwise a
shrinking-time sweep alone can miss the actual (O(1)) pulse.

## 11. Proof target suggested by the analysis

The clean model theorem would be a stopped uniform envelope:

> **Conjecture.** There is a universal (C) such that, for every (n) and every
> (0<t<1/2),
> \[
> \mathbb E[1_{\{t<\tau\}}S_t^H]\le C.
> \]

This immediately rules out an unbounded interval quotient, independently of (C_1\ge0) and
(0\le\alpha<1), because (r,D\ge0). A sharper result could compare source and damping away
from the finite pulse, but damping-only absorption is not the correct first target.

A plausible proof decomposition is:

1. use balance to remove all powers of (p^{-1}) in (2.6);
2. reduce to one-coordinate expectations of (h_i^2,h_id_i^2,d_i^2) via independence before
   stopping and an appropriate stopped/change-of-measure argument;
3. prove a uniform two-regime hazard bound, using the (t\asymp1/a_n) Laplace estimate in
   Section 7 and the separated-boundary Gaussian estimate in Section 6;
4. bridge the compact transition region (a_nt\asymp1) with the exact half-line formulas already
   implemented in the experiment.

Until that envelope or an actual divergent interval is proved, the high-(n) tail-union data is a
valuable stress signal but not a route refutation.
