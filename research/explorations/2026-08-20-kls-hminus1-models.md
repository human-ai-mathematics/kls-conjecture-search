---
---
# KLS first-eigenfunction \(H^{-1}\) residual: model cases and the heat-time split

Date: 2026-08-20

Status: exploratory note. “New” below means new information for this repository's route triage,
not a claim of priority in the literature.

## Verdict

The proposed estimate in the
[moment-map/spectral route brief](../kls/routes/moment-map-spectral/README.md),

\[
  R(f):=\sum_{i=1}^n\|\partial_i f-b_i\|_{H^{-1}(\mu)}^2
  \le C\lambda,
  \qquad b=\int \nabla f\,d\mu,
\]

is not an easier intermediate lemma: uniformly over isotropic log-concave measures admitting a
first eigenfunction, it is quantitatively equivalent to KLS. There is, however, an elementary and
exactly located weaker statement:

\[
  \int_0^T\sum_i\langle h_i,P_t h_i\rangle\,dt
  \le T(\lambda-|b|^2)\le T\lambda,
  \qquad h_i=\partial_i f-b_i.
\]

In particular the short-time part, with \(T=1\), already has the desired \(O(\lambda)\) scale.
The unresolved part is precisely the long-time, low-spectrum tail. An unconditional
\(O(\lambda)\) estimate on that tail would recover the full residual estimate and hence KLS.

The model cases do not supply a new way to control this tail:

- In one dimension the target follows immediately from the already-known one-dimensional KLS
  bound; using it here imports the conclusion.
- For products, the coordinate \(H^{-1}\) norm and the residual tensorize with equality. Thus a
  proof based on one-dimensional Poincaré constants merely imports known product KLS.
- For a Gaussian, the first eigenfunctions are linear and the residual is identically zero.
- For a truncated one-sided exponential, the standardized gap tends to \(1/4\), the residual
  tends to \(1\), and \(R/\lambda\to4\). Hence any universal constant in the proposed estimate is
  at least \(4\). Moreover, asymptotically all of the residual lies in the first eigendirection
  itself. This is a rank-one low-frequency obstruction, not an effective-rank loss.
- The limiting shifted exponential has gap \(1/4\), but the positive spectral bottom is not an
  eigenvalue. It therefore makes the regularization/approximate-minimizer issue literal.

The most amenable rigorous subproblem exposed here is not the full trace estimate. It is to find
additional log-concave structure that excludes or controls the low-spectrum projection of
\(\nabla f-b\). Neither short-time smoothing, product reduction, nor effective rank does that by
itself.

## 1. Setup and two exact bounds

Let \(\mu\) be centered and isotropic. Work first in a regular setting in which

\[
  A=-L=-\Delta+\nabla V\cdot\nabla
\]

is nonnegative and self-adjoint, with first nonzero eigenvalue \(\lambda\) and normalized first
eigenfunction

\[
  Af=\lambda f,\qquad \int f\,d\mu=0,\qquad \int f^2\,d\mu=1.
\]

The same calculations hold for a log-concave density on a convex interval/domain with reflecting
(Neumann) boundary conditions. For centered \(h\), use

\[
 \|h\|_{H^{-1}(\mu)}^2
 =\sup_u\left\{2\int hu\,d\mu-\int|\nabla u|^2\,d\mu\right\}
 =\langle h,A^{-1}h\rangle.
\]

The last equality is spectral/variational and is understood on the orthogonal complement of the
constants. The derivative inequality used below is Proposition 10 of
[Barthe--Klartag](https://arxiv.org/abs/1907.01823): if all derivative means vanish, then

\[
  \operatorname{Var}_\mu(u)
  \le \sum_i\|\partial_i u\|_{H^{-1}(\mu)}^2.
\]

Put \(h_i=\partial_i f-b_i\), where \(b=\int\nabla f\,d\mu\). The eigenfunction identities give

\[
 \int|\nabla f|^2\,d\mu=\lambda,
 \qquad
 \sum_i\int h_i^2\,d\mu=\lambda-|b|^2.                 \tag{1}
\]

Testing \(Af=\lambda f\) against \(x_i\) gives

\[
  b=\lambda\int xf\,d\mu,
  \qquad |b|^2\le\lambda^2,                             \tag{2}
\]

where the second assertion is Cauchy--Schwarz and isotropy. The linear Rayleigh test also gives
\(\lambda\le1\).

Now set \(g=f-\langle b,x\rangle\). Its derivative means vanish, so Barthe--Klartag and (2) give

\[
 \begin{aligned}
  R(f)&\ge \operatorname{Var}_\mu(g)\\
      &=1+|b|^2-2|b|^2/\lambda.                         \tag{3}
 \end{aligned}
\]

In the other direction, the dual Poincaré inequality
\(\|h\|_{H^{-1}}^2\le\lambda^{-1}\|h\|_2^2\), followed by (1), gives

\[
  R(f)\le \frac{\lambda-|b|^2}{\lambda}
       =1-\frac{|b|^2}{\lambda}.                        \tag{4}
\]

Thus there is a useful universal sandwich:

\[
 \boxed{
  1+|b|^2-2|b|^2/\lambda
  \ \le R(f)\le\
  1-|b|^2/\lambda.}
                                                               \tag{5}
\]

The upper bound \(R\le1\) is dimension-free and genuine, but it is one factor \(\lambda\) short
of the proposed target.

### Why the full estimate is KLS-equivalent

If \(|b|^2\ge\lambda/4\), then (2) implies \(\lambda\ge1/4\). If
\(|b|^2<\lambda/4\), then (3) implies \(R(f)>1/2\). Consequently

\[
  R(f)\le C\lambda\quad\Longrightarrow\quad
  \lambda\ge \min\{1/4,1/(2C)\}.                       \tag{6}
\]

Conversely, a uniform KLS bound \(\lambda\ge c\), combined with (4), gives
\(R(f)\le1\le\lambda/c\). Therefore the two uniform assertions are quantitatively equivalent
on the regular class. Passing either assertion to all log-concave measures still requires the
regularization/approximate-minimizer step.

## 2. The exact heat representation and the provable weaker theorem

Let \(P_t=e^{-tA}\). Spectral calculus gives, for every centered \(h\),

\[
 \|h\|_{H^{-1}}^2
 =\int_0^\infty\langle h,P_t h\rangle\,dt
 =\int_0^\infty\|P_{t/2}h\|_2^2\,dt.                  \tag{7}
\]

Hence

\[
 R(f)=\int_0^\infty S(t)\,dt,
 \qquad
 S(t):=\sum_i\langle h_i,P_t h_i\rangle.              \tag{8}
\]

For \(T>0\), \(L^2\)-contraction and (1) prove the short-time theorem

\[
 \boxed{
 R_{[0,T]}(f):=\int_0^T S(t)\,dt
 \le T(\lambda-|b|^2)\le T\lambda.}                  \tag{9}
\]

No log-concavity beyond the symmetric diffusion setup is used in (9). At \(T=1\), the complete
short-time part satisfies exactly the desired scaling, with constant one.

The gap only yields

\[
  R_{[T,\infty)}(f)
  \le e^{-\lambda T}\frac{\lambda-|b|^2}{\lambda}
  \le e^{-\lambda T}.                                  \tag{10}
\]

This displays the problem rather than solving it. In the nonlinear branch
\(|b|^2<\lambda/4\), equations (3) and (9) also give the lower obstruction

\[
  R_{[T,\infty)}(f)
  \ge \frac12-T\lambda.                                \tag{11}
\]

Thus, if arbitrarily small gaps existed, every fixed heat time would leave an order-one tail.
Making the generic upper bound (10) of order \(\lambda\) requires
\(T\gtrsim\lambda^{-1}\log(1/\lambda)\); equation (11) shows that at least
\(T=\Omega(\lambda^{-1})\) is necessary in the hard branch. A time depending on the unknown gap
cannot produce a uniform gap proof.

There are equivalent regularized formulations. For every \(\tau,\rho>0\),

\[
 \begin{aligned}
  \sum_i\langle h_i,(A+\tau)^{-1}h_i\rangle
    &\le \frac{\lambda-|b|^2}{\tau}\le\frac\lambda\tau,       \tag{12}\\
  R_{[\rho,\infty)}^{\rm spec}
    &:=\sum_i\int_{[\rho,\infty)}\frac1\nu\,
                  d\langle h_i,E_A(\nu)h_i\rangle
      \le\frac{\lambda-|b|^2}{\rho}\le\frac\lambda\rho.    \tag{13}
 \end{aligned}
\]

In particular, all spectral frequencies \(\nu\ge1\) already cost at most \(\lambda\). The only
unresolved piece is the low-frequency projection \(0<\nu<1\). An unconditional
\(O(\lambda)\) estimate for that piece, for all isotropic log-concave measures, would combine
with (13) to give the original target and hence KLS. This is the precise sense in which the
long-time tail is “exactly the gap.”

### A visible first-mode leakage

Define

\[
  c_i=\langle h_i,f\rangle=\int f\,\partial_i f\,d\mu.
\]

The first eigenspace component alone gives the exact orthogonal decomposition

\[
  R(f)=\frac{|c|^2}{\lambda}
       +\sum_i\|h_i-c_i f\|_{H^{-1}}^2.                \tag{14}
\]

Thus the target necessarily requires \(|c|^2\lesssim\lambda^2\), as well as control of the
remaining low modes. The elementary estimate is only \(|c|^2\le\lambda\). For a smooth
full-space density, integration by parts rewrites

\[
  c=\frac12\int f^2\nabla V\,d\mu,                    \tag{15}
\]

with the appropriate boundary term on a finite interval. The exponential computation below
shows that (14) can asymptotically account for the entire residual.

## 3. One dimension: exact \(H^{-1}\) formula, but no new KLS mechanism

Let \(d\mu=p(x)\,dx\) on an interval \(I=(a,d)\), and let \(h\) be centered. Define

\[
  H(x)=\int_a^x h(s)p(s)\,ds.
\]

Then

\[
  \boxed{\|h\|_{H^{-1}(\mu)}^2
    =\int_I\frac{H(x)^2}{p(x)}\,dx.}                  \tag{16}
\]

Indeed \(H(a)=H(d)=0\), so
\(\int h u\,d\mu=-\int H u'\,dx\). Weighted Cauchy--Schwarz gives one inequality, and the
choice \(u'=-H/p\), by approximation if necessary, gives equality. Formula (16) is convenient
for checking concrete examples without solving a Poisson equation numerically.

For an isotropic log-concave law on the line, the desired residual bound is already automatic.
[Bobkov, Corollary 4.3](https://doi.org/10.1214/aop/1022874820) gives

\[
  \frac1{12\operatorname{Var}(X)}\le\lambda_1
  \le\frac1{\operatorname{Var}(X)}.
\]

Consequently (4) yields \(R(f)\le1\le12\lambda\) in the isotropic case. This is a valid model
bound, but it merely feeds the known one-dimensional spectral gap into the residual. It does not
provide an independent proof mechanism for high-dimensional KLS. Also, for exponential-tail
laws the spectral bottom need not be attained, so a literal first eigenfunction may be absent.

## 4. Products: exact tensorization and why it does not advance KLS

Let \(\mu=\bigotimes_{j=1}^m\mu_j\), with factor generators \(A_j\) and
\(A=\sum_j A_j\). If \(q=q(x_j)\) is centered and depends only on the \(j\)-th block, then

\[
  \boxed{\|q\|_{H^{-1}(\mu)}=\|q\|_{H^{-1}(\mu_j)}.}   \tag{17}
\]

For the lower bound, restrict the variational test functions to functions of \(x_j\). For the
upper bound, replace any test function \(U(x)\) by its conditional average
\(\bar U(x_j)=\int U(x)\,d\mu_{-j}\). The pairing with \(q\) is unchanged, while Jensen gives

\[
  \int|\nabla_j\bar U|^2\,d\mu_j
  \le\int|\nabla U|^2\,d\mu.
\]

This proves (17) directly, without assuming a discrete spectrum.

When the factors do have discrete spectra, let
\(\lambda=\min_j\lambda_j\) and \(J=\{j:\lambda_j=\lambda\}\). A product first
eigenfunction is a sum of factor first eigenfunctions,

\[
  f(x)=\sum_{j\in J}\alpha_j f_j(x_j),
  \qquad \sum_{j\in J}\alpha_j^2=1,
\]

allowing the evident extra index if a factor first eigenspace is not simple. Applying (17) to each
block gives exact residual tensorization:

\[
  \boxed{R_\mu(f)=\sum_{j\in J}\alpha_j^2R_{\mu_j}(f_j).}       \tag{18}
\]

There is no dimension or multiplicity loss. In particular, proving the factor bounds by their
one-dimensional Poincaré constants and then invoking (18) is just the standard tensorization of
known product KLS, expressed in \(H^{-1}\) language.

This also rules out effective rank as the missing generic gain. For identical one-dimensional
factors define the residual Gram matrix

\[
  M_{ij}=\langle h_i,A^{-1}h_j\rangle.
\]

For \(f=\sum_i\alpha_i f_0(x_i)\), coordinate orthogonality gives

\[
  M=R_{\mu_0}(f_0)\,\operatorname{diag}(\alpha_1^2,\ldots,\alpha_n^2),
  \quad \operatorname{tr}M=R_{\mu_0}(f_0).             \tag{19}
\]

Its effective rank \(\operatorname{tr}M/\|M\|_{\rm op}=1/\max_i\alpha_i^2\) can range from
\(1\) to \(n\), while the trace and the ratio \(R/\lambda\) do not change. The trace is already
dimension-free by (4); what is missing is a factor \(\lambda\), not a rank estimate.

## 5. Gaussian model: a degenerate success

For the standard Gaussian \(\gamma_n\), \(A\) is the Ornstein--Uhlenbeck number operator,
\(\lambda=1\), and every normalized first eigenfunction has the form

\[
  f(x)=\langle u,x\rangle,\qquad |u|=1.
\]

Then \(b=u\), every \(h_i=0\), and

\[
  R(f)=0.                                                \tag{20}
\]

This checks normalization and the preferred-linear branch, but says nothing about the nonlinear
branch where (3) forces an order-one residual.

## 6. Truncated exponential: exact spectrum and a rank-one obstruction

Let \(\mu_L\) have density

\[
  p_L(x)=\frac{e^{-x}}{Z_L}\mathbf 1_{[0,L]}(x),
  \qquad Z_L=1-e^{-L},
\]

with reflecting boundary conditions. Its raw generator is

\[
  A=-\frac{d^2}{dx^2}+\frac d{dx}.
\]

Under \(f=e^{x/2}u\), this becomes

\[
  Af=e^{x/2}\left(-u''+\frac14u\right),
  \qquad u'+\tfrac12u=0\quad\text{at }0,L.
\]

Besides the constant eigenfunction at zero, the spectrum is

\[
  \nu_m=\frac14+\left(\frac{m\pi}{L}\right)^2,
  \qquad m=1,2,\ldots.                                  \tag{21}
\]

Indeed the Robin condition at zero selects
\(u_m(x)=\cos(k_mx)-(2k_m)^{-1}\sin(k_mx)\), and the condition at \(L\) reduces to
\(\sin(k_mL)=0\). Let

\[
 \begin{aligned}
  k_m&=m\pi/L,\\
  f_m(x)&=N_m^{-1}e^{x/2}
       \left(\cos(k_mx)-\frac1{2k_m}\sin(k_mx)\right),\\
  N_m^2&=\frac{L}{2Z_L}\left(1+\frac1{4k_m^2}\right).
                                                               \tag{22}
 \end{aligned}
\]

These are normalized in \(L^2(\mu_L)\). The mean and variance of \(\mu_L\) are

\[
 \begin{aligned}
  m_L&=\frac{1-(L+1)e^{-L}}{Z_L},\\
  \sigma_L^2
    &=\frac{2-(L^2+2L+2)e^{-L}}{Z_L}-m_L^2.             \tag{23}
 \end{aligned}
\]

After the affine standardization \(y=(x-m_L)/\sigma_L\), the first gap is

\[
  \lambda_L=\sigma_L^2\nu_1.                           \tag{24}
\]

The residual \(R\) is invariant under this affine standardization: the derivative is multiplied
by \(\sigma_L\), while the generator is multiplied by \(\sigma_L^2\).

For the first eigenfunction, direct integration gives

\[
  b_{\rm raw}=\int f_1'\,d\mu_L
  =-\frac{1+e^{-L/2}}{N_1Z_L}.                         \tag{25}
\]

The standardized derivative mean is \(\sigma_Lb_{\rm raw}\), so the dimensionless ratio
\(|b|^2/\lambda\) is still \(b_{\rm raw}^2/\nu_1\).

### Exact residual series

Write \(h=f_1'-b_{\rm raw}\). Since every \(f_m\), \(m\ge1\), is centered, the constant
subtraction does not affect its nonconstant spectral coefficients. Orthogonality of sines and
cosines in (22) gives

\[
 a_m:=\langle h,f_m\rangle
 =\begin{cases}
    \tfrac12, &m=1,\\[2mm]
    \displaystyle
    \frac{4m\sqrt{\nu_1}}{L\sqrt{\nu_m}(m^2-1)},
       &m\ge2\text{ even},\\[3mm]
    0,&m>1\text{ odd}.
   \end{cases}                                          \tag{26}
\]

For example, \(a_1=1/2\) also follows from

\[
 \int f_1f_1'p_L
 =\frac12[f_1^2p_L]_0^L+\frac12\int f_1^2p_L
 =\frac12,
\]

because \(f_1(L)^2p_L(L)=f_1(0)^2p_L(0)\). Therefore

\[
 \boxed{
 R_L=\frac1{4\nu_1}
   +\sum_{\substack{m\ge2\\m\ {\rm even}}}
      \frac{16m^2\nu_1}
      {L^2\nu_m^2(m^2-1)^2}.}                         \tag{27}
\]

The first summand in (27) is exactly the self-leakage term \(|c|^2/\lambda\) from (14).

As \(L\to\infty\),

\[
 \sigma_L^2\to1,
 \quad \lambda_L\to\frac14,
 \quad N_1^2\sim\frac{L^3}{8\pi^2},
 \quad \frac{b_{\rm raw}^2}{\nu_1}\sim\frac{32\pi^2}{L^3}.  \tag{28}
\]

The first term in (27) tends to one, while the universal upper bound (4) tends to one. By
squeezing,

\[
  R_L\longrightarrow1,
  \qquad \frac{R_L}{\lambda_L}\longrightarrow4.        \tag{29}
\]

Thus \(C\ge4\) is necessary in any universal residual estimate. More sharply,

\[
  \frac{(4\nu_1)^{-1}}{R_L}\longrightarrow1,           \tag{30}
\]

so the obstruction becomes rank one in spectral space.

The same calculation gives a lower bound for the long-time tail after standardization:

\[
  R_{[T,\infty)}(f_1)
  \ge \frac{e^{-\lambda_LT}}{4\nu_1}
  \longrightarrow e^{-T/4}.                            \tag{31}
\]

Every fixed heat time therefore leaves a nonzero first-mode contribution in this model.

### Small reproducible computation

Equation (27) is rapidly convergent (the summands are \(O(m^{-6})\) for fixed \(L\)). This
snippet uses only the displayed formulas:

```python
import numpy as np

for L in [4., 8., 16., 32., 64., 128.]:
    Z = 1. - np.exp(-L)
    mean = (1. - (L + 1.) * np.exp(-L)) / Z
    second = (2. - (L * L + 2. * L + 2.) * np.exp(-L)) / Z
    variance = second - mean * mean

    nu1 = .25 + (np.pi / L) ** 2
    m = np.arange(2., 100000., 2.)
    num = .25 + (m * np.pi / L) ** 2
    terms = 16. * m**2 * nu1 / (L**2 * num**2 * (m**2 - 1.)**2)
    residual = 1. / (4. * nu1) + terms.sum()
    gap_iso = variance * nu1
    first_fraction = (1. / (4. * nu1)) / residual
    print(L, gap_iso, residual, residual / gap_iso, first_fraction)
```

| \(L\) | \(\lambda_L\) | \(R_L\) | \(R_L/\lambda_L\) | first-mode fraction |
|---:|---:|---:|---:|---:|
| 4 | 0.603252 | 0.341239 | 0.565666 | 0.845156 |
| 8 | 0.395528 | 0.679340 | 1.717550 | 0.910423 |
| 16 | 0.288545 | 0.917410 | 3.179437 | 0.944388 |
| 32 | 0.259638 | 0.986768 | 3.800550 | 0.975789 |
| 64 | 0.252410 | 0.998233 | 3.954814 | 0.992207 |
| 128 | 0.250602 | 0.999775 | 3.989489 | 0.997820 |

### The limiting eigenfunction is absent

For the untruncated exponential law \(e^{-x}\mathbf1_{[0,\infty)}dx\), the same unitary
conjugation gives the half-line Schrödinger operator

\[
  -\frac{d^2}{dx^2}+\frac14,
  \qquad u'(0)+\tfrac12u(0)=0.
\]

It has the zero bound state \(u=e^{-x/2}\), corresponding to constants, and continuous spectrum
\([1/4,\infty)\). The threshold \(1/4\) is not an \(L^2\) eigenvalue. After shifting by one, this
law is centered, isotropic, and has spectral gap \(1/4\), but no first nonconstant eigenfunction.
The truncated eigenfunctions constitute a concrete approximation to this nonattained spectral
edge.

Products of identical truncated exponentials have an \(n\)-dimensional first eigenspace, but (18)
shows that every normalized combination has the same \(R_L\). In the untruncated limit, the
positive spectral edge again ceases to be an eigenvalue.

The truncated law has a hard boundary and is not one of the smooth, strongly log-concave
full-support approximants stipulated in the route brief. This note does not prove spectral
convergence for a particular smoothing of the wall. Accordingly, (29)--(31) are rigorous model
diagnostics and a regularization warning, not a counterexample inside the stipulated smooth
class.

## 7. What succeeded, what is tautological, and what failed

### Rigorous information added by the model analysis

1. The universal sandwich (5), including the simple but useful upper bound \(R\le1\).
2. The exact heat identity (7) and short-time bound (9): every fixed short-time window has the
   desired \(O(\lambda)\) scale.
3. The matching obstruction (11): in the nonlinear/small-gap branch, a fixed-time truncation must
   leave an order-one tail.
4. The resolvent and high-frequency bounds (12)--(13), which isolate low-frequency leakage as the
   only missing part.
5. Exact product tensorization (17)--(18), with no multiplicity loss.
6. The exact truncated-exponential spectrum and residual series (21)--(27), the lower bound
   \(C\ge4\), and the asymptotically rank-one nature of its residual.
7. A concrete nonattainment example showing why an approximate-minimizer formulation is not
   optional.

### Statements that do not constitute progress toward KLS

- The full unconditional estimate \(R\lesssim\lambda\) is KLS-equivalent by (4)--(6).
- The one-dimensional estimate \(R\le12\lambda\) uses the known one-dimensional gap.
- Its product extension uses exact tensorization of that known gap.
- The Gaussian check has zero residual because the eigenfunction is already linear.
- The dimension-free trace bound \(R\le1\) follows from the Poincaré constant \(1/\lambda\) of the
  same measure and loses exactly the needed factor.

### Failed or blocked targets

- **Close the full bound from \(L^2\) energy.** Equation (1) plus dual Poincaré gives only (4).
  Improving the inverse-operator cost from \(1/\lambda\) to \(O(1)\) on all residuals is precisely
  the low-spectrum assertion and hence KLS-strength.
- **Close by finite heat time.** Equation (9) succeeds for the short-time part, but (11) and the
  explicit lower bound (31) show why the tail cannot be discarded.
- **Close by effective rank or first-eigenspace multiplicity.** Equation (19) lets effective rank
  vary from \(1\) to \(n\) without changing the residual. The exponential obstruction itself is
  asymptotically rank one.
- **Close by differentiating the eigenfunction equation using only convexity.** The commutator
  identity
  \[
    A\nabla f=\lambda\nabla f-\nabla^2V\,\nabla f
  \]
  and Bochner's identity do imply
  \[
    \int\|\nabla^2f\|_{\rm HS}^2\,d\mu
    +\int\langle\nabla^2V\nabla f,\nabla f\rangle\,d\mu
    =\lambda^2.
  \]
  Mere convexity controls the sign of the second term, but gives no upper control on the forcing
  or on the low spectral projection in (14). The exponential calculation shows substantial
  first-mode leakage even though \(V''=0\) in the interior; the tail/boundary geometry carries the
  obstruction.

## 8. Route recommendation

The full residual trace should remain classified as a KLS-equivalent endpoint, not as a likely
stand-alone preliminary lemma. The tractable, honest reduction is:

\[
 \text{short time/high spectrum: proved by (9), (13)}
 \quad+\quad
 \text{long time/low spectrum: completely open and KLS-strength}.
\]

A next useful lemma would need a new quantity, controlled independently of KLS, that bounds the
low-spectrum component of \(h=\nabla f-b\). The decomposition (14) suggests separating the
self-leakage vector \(c=\int f\nabla f\,d\mu\) from the orthogonal low modes. Model-case work on
Gaussian, one-dimensional, or product measures alone is unlikely to supply the missing input:
those cases respectively kill the residual, import a known gap, or tensorize it exactly.
