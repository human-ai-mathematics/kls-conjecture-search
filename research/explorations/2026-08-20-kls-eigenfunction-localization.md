# KLS eigenfunctions under stochastic localization

Date: 2026-08-20

Status: analytical exploration. The stochastic identities and conditional implications below are
proved. Statements explicitly labelled **Conjecture** are open. Every use of Letwin's quadratic
Poincare inequality is conditional on the correctness of arXiv:2607.24164v1, submitted 27 July
2026; it is a recent version-1 preprint and is not yet peer reviewed.

## 1. Outcome

There is a clean fixed-function localization system. If \(f\) is fixed and

\[
g_t=\operatorname{Cov}_{\mu_t}(f,X),\qquad
H_t=\mathbb E_{\mu_t}\!\left[(f-m_t)(X-a_t)\otimes(X-a_t)\right],
\]

where \(m_t=\mathbb E_{\mu_t}f\), then

\[
d g_t=H_t\,dW_t-A_tg_t\,dt.
\]

Consequently, “learning” the fixed function is driven by the Euclidean source
\(\|H_t\|_{\mathrm{HS}}^2\) and damped by \(2g_t^TA_tg_t\). Letwin's result controls the
whitened tensor exactly:

\[
\left\|A_t^{-1/2}H_tA_t^{-1/2}\right\|_{\mathrm{HS}}^2
\le 8\operatorname{Var}_{\mu_t}(f).
\]

The unresolved step is entirely the unwhitening

\[
\|H_t\|_{\mathrm{HS}}^2
=\operatorname{Tr}(A_t\widehat H_tA_t\widehat H_t),
\qquad \widehat H_t=A_t^{-1/2}H_tA_t^{-1/2},
\]

integrated for a universal amount of localization time. A fixed-time or unweighted covariance
estimate is not enough: the conditional variance of \(f\), the large eigenspaces of \(A_t\), and
the matrix energy of \(\widehat H_t\) may be correlated.

The clean dynamic headline is an absorptive Carleson estimate for this source: if its time integral
is bounded by an absolute term, the covariance information \(\int|g_t|^2dt\), and strictly less
than the full damping \(2\int g_t^TA_tg_tdt\), then Ito and Gronwall force a universal spectral
gap. A still weaker one-horizon criterion only asks for a strict deficit in the exact
source-minus-damping occupation.

A tempting shortcut is false. Even in dimension one, and even for the actual first nonconstant
eigenfunction of a compactly supported log-concave measure, there is no universal \(C\) such that

\[
\mathbb E\langle\tau\nabla f,\nabla f\rangle
\le C\left(\mathbb E|\nabla f|^2+\mathbb E\|\nabla^2f\|_{\mathrm{HS}}^2\right)
\tag{1.1}
\]

for the positive moment-map Stein kernel \(\tau\). Section 8 gives an explicit truncated-exponential
counterexample and checks its boundary conditions and isotropic rescaling.

## 2. Setup and regularity fence

Let \(\mu\) initially be a compactly supported, full-dimensional log-concave probability measure.
Eldan localization has the form

\[
d\mu_t(x)=Z_t^{-1}\exp\left(\langle c_t,x\rangle-\frac t2|x|^2\right)d\mu(x),
\]

and, for every fixed integrable test function \(\varphi\),

\[
d\mathbb E_t\varphi
=\operatorname{Cov}_t(\varphi,X)\cdot dW_t.
\tag{2.1}
\]

Here and below \(\mathbb E_t\), \(\operatorname{Var}_t\), and \(\operatorname{Cov}_t\) mean expectation,
variance, and covariance under \(\mu_t\), and

\[
a_t=\mathbb E_tX,\qquad A_t=\operatorname{Cov}_t(X).
\]

Compact support makes all martingales below true martingales on bounded time intervals. The usual
restriction, smoothing, and limiting argument may subsequently be used, but every proposed
estimate must be uniform through that approximation. For the spectral statements, one may first
work with smooth strongly log-concave approximants having a first eigenfunction. The explicit
counterexample in Section 8 is already a legitimate log-concave measure and does not require a
smooth-approximation claim to refute (1.1).

Fix a sufficiently regular deterministic function \(f\), not an evolving function, and define

\[
\begin{aligned}
m_t&=\mathbb E_t f, &
v_t&=\operatorname{Var}_t(f), &
e_t&=\mathbb E_t|\nabla f|^2,\\
g_t&=\mathbb E_t[(f-m_t)(X-a_t)],&&&
H_t&=\mathbb E_t[(f-m_t)(X-a_t)\otimes(X-a_t)],\\
k_t&=\mathbb E_t[(f-m_t)^2(X-a_t)].
\end{aligned}
\tag{2.2}
\]

Thus \(g_t\in\mathbb R^n\), \(H_t\) is symmetric, and \(k_t\in\mathbb R^n\).

## 3. The fixed-\(f\) stochastic system

### Lemma 3.1 (fixed-function SDEs; proved)

Under the setup above,

\[
\begin{aligned}
d m_t&=g_t\cdot dW_t,\\
d v_t&=k_t\cdot dW_t-|g_t|^2dt,\\
d e_t&=\operatorname{Cov}_t(|\nabla f|^2,X)\cdot dW_t,\\
d g_t&=H_t\,dW_t-A_tg_t\,dt.
\end{aligned}
\tag{3.1}
\]

In particular,

\[
\mathbb E v_T=v_0-\mathbb E\int_0^T|g_t|^2dt,
\qquad
\mathbb E e_T=e_0.
\tag{3.2}
\]

#### Proof

The equations for \(m_t\) and \(e_t\) are (2.1) applied to \(f\) and \(|\nabla f|^2\). Since
\(v_t=\mathbb E_tf^2-m_t^2\), Ito's formula gives

\[
dv_t=\bigl(\operatorname{Cov}_t(f^2,X)-2m_tg_t\bigr)\cdot dW_t-|g_t|^2dt.
\]

Expanding \(f=m_t+(f-m_t)\) shows that the stochastic coefficient is \(k_t\).

For the last equation, write \(g_t=\mathbb E_t(fX)-m_ta_t\). Equation (2.1), the mean SDE
\(da_t=A_t\,dW_t\), and

\[
d[m,a]_t=A_tg_t\,dt
\]

show that the drift is \(-A_tg_tdt\). In components, the remaining stochastic coefficient is

\[
\operatorname{Cov}_t(fX_i,X_j)-a_{t,i}g_{t,j}-m_tA_{t,ij}
=\mathbb E_t[(f-m_t)(X_i-a_{t,i})(X_j-a_{t,j})],
\]

which is \(H_{t,ij}\). Taking expectations gives (3.2). \(\square\)

### Lemma 3.2 (source-damping identity; proved)

Put

\[
S_t^f=\|H_t\|_{\mathrm{HS}}^2,
\qquad
D_t^f=g_t^TA_tg_t\ge0,
\qquad
I_T(f)=\mathbb E\int_0^T|g_t|^2dt.
\]

Then

\[
d|g_t|^2=2\langle g_t,H_t\,dW_t\rangle
+(S_t^f-2D_t^f)dt
\tag{3.3}
\]

and hence

\[
I_T(f)
=T|g_0|^2+
\mathbb E\int_0^T(T-t)(S_t^f-2D_t^f)dt.
\tag{3.4}
\]

#### Proof

Equation (3.3) is Ito's formula applied to the final equation of (3.1). Integrate its expectation
first to time \(s\), and then integrate \(s\in[0,T]\); Fubini produces the kernel \(T-t\).
\(\square\)

### Lemma 3.3 (Gaussian-channel form; proved)

The localization can be realized as the posterior channel

\[
Y_t=tX+B_t,
\qquad
\mu_t=\operatorname{Law}(X\mid Y_s,\ s\le t),
\]

with innovations Brownian motion \(W_t=Y_t-\int_0^ta_sds\). If

\[
M(t,c)=
\frac{\int f(x)e^{\langle c,x\rangle-t|x|^2/2}d\mu(x)}
     {\int e^{\langle c,x\rangle-t|x|^2/2}d\mu(x)},
\]

then at \(c=c_t\),

\[
\nabla_cM=g_t,
\qquad
\nabla_c^2M=H_t.
\tag{3.5}
\]

Moreover, if \(a(t,c)=\nabla_c\log Z(t,c)\), then

\[
\partial_tM+\frac12\Delta_cM+a(t,c)\cdot\nabla_cM=0.
\tag{3.6}
\]

#### Proof

Bayes' formula gives the displayed posterior density. Differentiating the ratio once and twice in
\(c\) gives (3.5). Its numerator and denominator separately solve the backward Euclidean heat
equation \(\partial_tF=-\Delta_cF/2\); the quotient rule gives (3.6). Since
\(dc_t=a_tdt+dW_t\), Ito's formula recovers the martingale and gradient equations above.
\(\square\)

This is the sense in which the averaged targets below are “heat averaged”; they are not ordinary
Langevin-semigroup averages of \(f\) under the fixed measure.

### Gaussian sign check

For \(\mu=N(0,I)\) and \(f(x)=x_1\), the posterior covariance is
\(A_t=(1+t)^{-1}I\). Hence

\[
v_t=(1+t)^{-1},\qquad
g_t=(1+t)^{-1}e_1,\qquad H_t=0.
\]

Equations (3.1) and (3.3) reduce to

\[
v_t'=-|g_t|^2=-(1+t)^{-2},
\qquad
\frac d{dt}|g_t|^2=-2g_t^TA_tg_t=-2(1+t)^{-3},
\]

which checks both the sign and the factor \(2\) in the damping.

## 4. First eigenfunction and conditional KLS theorems

Suppose now that \(d\mu=e^{-V}dx\) is isotropic and sufficiently regular, and let

\[
-Lf=\lambda f,
\qquad L=\Delta-\nabla V\cdot\nabla,
\qquad \mathbb E_\mu f=0,
\qquad \mathbb E_\mu f^2=1
\tag{4.1}
\]

be a first nonconstant eigenfunction. Then

\[
e_0=\mathbb E|\nabla f|^2=\lambda,
\qquad \lambda\le1,
\qquad |g_0|=|\mathbb E(fX)|\le1.
\tag{4.2}
\]

The upper bound \(\lambda\le1\) follows by testing the Rayleigh quotient with an isotropic linear
function. The last bound follows by testing \(g_0\) in its own direction and using isotropy. If
\(b=\mathbb E\nabla f\), integration by parts against the coordinate functions also gives

\[
b=\lambda g_0.
\tag{4.3}
\]

For smooth full support, Bochner gives

\[
\mathbb E\|\nabla^2f\|_{\mathrm{HS}}^2
+\mathbb E\langle\nabla^2V\nabla f,\nabla f\rangle
=\lambda^2,
\tag{4.4}
\]

so the Hessian energy is at most \(\lambda^2\).

### Lemma 4.1 (terminal strong-convexity estimate; proved)

For every \(T>0\),

\[
\mathbb E v_T\le\frac{\lambda}{T},
\qquad
I_T(f)\ge1-\frac{\lambda}{T}.
\tag{4.5}
\]

#### Proof

The posterior \(\mu_T\) is \(T\)-uniformly log-concave. Brascamp--Lieb therefore gives, pathwise,

\[
v_T=\operatorname{Var}_{\mu_T}(f)
\le\frac1T\mathbb E_T|\nabla f|^2=\frac{e_T}{T}.
\]

Take expectations and use the fixed-integrand density martingale
\(\mathbb Ee_T=e_0=\lambda\). The second inequality follows from
\(\mathbb Ev_T=1-I_T(f)\). \(\square\)

### Theorem 4.2 (absorptive dynamic criterion; proved)

Assume there are universal constants \(T_0,C_0,C_1>0\) and \(\alpha<1\) such that, for every
regular isotropic log-concave \(\mu\), its normalized first eigenfunction, and every \(t\le T_0\),

\[
\mathbb E\int_0^tS_s^f\,ds
\le C_0t+C_1\mathbb E\int_0^t|g_s|^2ds
+\alpha\,\mathbb E\int_0^t2D_s^f\,ds.
\tag{4.6}
\]

Then there is a universal \(c>0\) such that \(\lambda\ge c\). If (4.6) is uniform under the
standard regularization passage, it proves KLS.

#### Proof

Let \(q(t)=\mathbb E|g_t|^2\). Taking expectations in (3.3) and applying (4.6) gives

\[
\begin{aligned}
q(t)
&=|g_0|^2+\mathbb E\int_0^t(S_s^f-2D_s^f)ds\\
&\le1+C_0t+C_1\int_0^tq(s)ds
-(1-\alpha)\mathbb E\int_0^t2D_s^f\,ds\\
&\le1+C_0t+C_1\int_0^tq(s)ds.
\end{aligned}
\]

Gronwall yields, for \(t\le T_0\),

\[
q(t)\le(1+C_0t)e^{C_1t}.
\tag{4.7}
\]

Choose a universal \(T\le T_0\) so small that

\[
T(1+C_0T)e^{C_1T}\le\frac12.
\]

Then \(I_T(f)\le1/2\), and (3.2) gives \(\mathbb Ev_T\ge1/2\). Lemma 4.1 gives
\(\mathbb Ev_T\le\lambda/T\), hence \(\lambda\ge T/2\). \(\square\)

The strict inequality \(\alpha<1\) is what makes (4.6) absorptive. The proof uses neither a
pointwise covariance bound nor a claim that the source itself is \(O(\lambda)\).

### Theorem 4.3 (one-horizon occupation criterion; proved)

Assume that there are universal \(T\in(0,1)\) and \(\rho<1-T\) such that

\[
\mathbb E\int_0^T(T-t)(S_t^f-2D_t^f)dt\le\rho.
\tag{4.8}
\]

Then

\[
\lambda\ge T(1-T-\rho).
\tag{4.9}
\]

The same conclusion holds under the stronger source-only hypothesis

\[
\mathbb E\int_0^T(T-t)S_t^fdt\le\rho.
\tag{4.10}
\]

#### Proof

Combine Lemma 4.1, (3.4), and \(|g_0|^2\le1\):

\[
1-\frac\lambda T
\le I_T(f)
\le T+\rho.
\]

Rearranging gives (4.9). Since \(D_t^f\ge0\), (4.10) implies (4.8). \(\square\)

This criterion is deliberately not \(I_T(f)\lesssim\lambda\). A universal strict deficit below
one suffices. In particular, the possibly order-one initial value \(g_0\) costs only
\(T|g_0|^2\le T\).

## 5. Letwin's whitened \(H_t\) estimate and the exact gap

The input used here is the following claimed theorem from Letwin's version-1 preprint:
for isotropic log-concave \(Y\) and every symmetric \(B\),

\[
\operatorname{Var}(Y^TBY)\le8\|B\|_{\mathrm{HS}}^2.
\tag{5.1}
\]

### Lemma 5.1 (whitened fixed-\(f\) bound by Hilbert--Schmidt duality; proved conditional on (5.1))

For every \(t\), on the support of \(A_t\), put

\[
\widehat H_t=A_t^{-1/2}H_tA_t^{-1/2}.
\]

Then

\[
\|\widehat H_t\|_{\mathrm{HS}}^2\le8v_t.
\tag{5.2}
\]

#### Proof

Condition on the localization filtration and let

\[
Y=A_t^{-1/2}(X-a_t).
\]

Its law is isotropic and log-concave. For every symmetric \(B\),

\[
\begin{aligned}
\langle B,\widehat H_t\rangle_{\mathrm{HS}}
&=\mathbb E_t[(f-m_t)Y^TBY]\\
&=\operatorname{Cov}_t(f,Y^TBY).
\end{aligned}
\]

Cauchy--Schwarz and (5.1) imply

\[
|\langle B,\widehat H_t\rangle_{\mathrm{HS}}|
\le\sqrt{8v_t}\,\|B\|_{\mathrm{HS}}.
\]

Taking the Hilbert--Schmidt dual supremum proves (5.2). \(\square\)

### Corollary 5.2 (unwhitening; proved conditional on (5.1))

One has the exact identity and crude consequence

\[
S_t^f
=\operatorname{Tr}(A_t\widehat H_tA_t\widehat H_t)
\le8v_t\|A_t\|_{\mathrm{op}}^2.
\tag{5.3}
\]

Consequently, Theorem 4.3 would follow if, for some universal \(T\in(0,1)\) and
\(\rho<1-T\),

\[
8\,\mathbb E\int_0^T(T-t)v_t\|A_t\|_{\mathrm{op}}^2dt\le\rho.
\tag{5.4}
\]

#### Proof

Since \(H_t=A_t^{1/2}\widehat H_tA_t^{1/2}\), cyclicity of trace gives the identity in (5.3).
The inequality follows from (5.2) and

\[
\operatorname{Tr}(A\widehat HA\widehat H)
\le\|A\|_{\mathrm{op}}^2\|\widehat H\|_{\mathrm{HS}}^2.
\]

Insert this in (4.10). \(\square\)

### What remains open

Equation (5.2) is an intrinsic, dimension-free static estimate. Equations (4.6), (4.8), and
(5.4) are joint, function-aware occupation estimates. The following gaps must not be conflated:

1. The pathwise Brascamp--Lieb cap \(A_t\preceq t^{-1}I\) makes the right side of (5.4) behave
   like \(v_t/t^2\) near zero and is not integrable by itself.
2. Conditional on Letwin v1, known fixed-time moments of \(\|A_t\|_{\mathrm{op}}\) are universal
   only on \(t\lesssim1/\log n\), not on a universal interval.
3. Even a marginal estimate on \(\mathbb E\|A_t\|_{\mathrm{op}}^2\) does not control
   \(\mathbb E[v_t\|A_t\|_{\mathrm{op}}^2]\): \(v_t\) and covariance inflation may be strongly
   correlated.
4. Replacing the exact contraction by \(\|A_t\|_{\mathrm{op}}^2\) discards the orientation and
   effective rank of \(\widehat H_t\). This is precisely the same operator-to-trace loss that
   appears in the fixed-cut localization route, now for a first eigenfunction.
5. The negative term \(2D_t^f\) is genuine damping. The absorptive criterion only needs control
   of the source modulo a strict fraction of that damping; a source-only proof may be
   unnecessarily strong.

Thus Letwin's theorem closes the whitened static problem, but not the unwhitened, universal-time
occupation problem.

## 6. Random-horizon heat-scale averaging

A fixed terminal time is not essential. Let \(\mathsf T\), independent of the localization, have
law \(\pi\) supported in \([T_-,T_+]\) with \(T_->0\), and define

\[
K_\pi(t)=\mathbb P(\mathsf T\ge t),
\qquad
J_\pi(t)=\mathbb E(\mathsf T-t)_+
=\int_t^\infty K_\pi(s)ds.
\tag{6.1}
\]

Useful identities are

\[
\int_0^\infty K_\pi(t)dt=\mathbb E\mathsf T,
\qquad
\int_0^\infty J_\pi(t)dt=\frac12\mathbb E\mathsf T^2.
\tag{6.2}
\]

### Theorem 6.1 (random-horizon conditional KLS implication; proved)

For every normalized first eigenfunction,

\[
1\le
\lambda\,\mathbb E\frac1{\mathsf T}
+|g_0|^2\mathbb E\mathsf T
+\mathbb E\int_0^\infty
J_\pi(t)(S_t^f-2D_t^f)dt.
\tag{6.3}
\]

Hence, if there are universal \(\pi\) and \(\delta>0\) such that

\[
\mathbb E\mathsf T+
\mathbb E\int_0^\infty J_\pi(t)(S_t^f-2D_t^f)dt
\le1-\delta,
\tag{6.4}
\]

then

\[
\lambda\ge
\frac{\delta}{\mathbb E(1/\mathsf T)}.
\tag{6.5}
\]

The source-only version obtained by deleting \(-2D_t^f\) is sufficient as well.

#### Proof

Average the deterministic inequality

\[
1\le\frac\lambda T+\int_0^T\mathbb E|g_t|^2dt
\]

over \(T\sim\pi\). Fubini turns the last term into
\(\int K_\pi(t)\mathbb E|g_t|^2dt\). Integrating (3.3) in expectation and applying Fubini once
more gives

\[
\int_0^\infty K_\pi(t)\mathbb E|g_t|^2dt
=|g_0|^2\mathbb E\mathsf T
+\mathbb E\int_0^\infty J_\pi(t)(S_t^f-2D_t^f)dt.
\]

This proves (6.3); use \(|g_0|^2\le1\) to obtain (6.5). \(\square\)

### Conjecture 6.2 (net heat-channel source; open, weakest direct target)

There exist a universal horizon law \(\pi\) and \(\delta>0\) such that (6.4) holds for every
regular isotropic log-concave measure and its normalized first eigenfunction.

This is exactly KLS-sufficient and retains the damping. It makes no pointwise demand on \(A_t\).
Theorem 4.2 is a stronger local-in-time package that would imply the needed lower bound on
\(\mathbb Ev_T\) by Gronwall.

To state a Letwin-compatible source-only target, define, when \(\widehat H_t\ne0\),

\[
\Lambda_t(f)^2
=\frac{\operatorname{Tr}(A_t\widehat H_tA_t\widehat H_t)}
       {\|\widehat H_t\|_{\mathrm{HS}}^2},
\qquad
\Lambda_t(f)=0\quad\text{if }\widehat H_t=0.
\tag{6.6}
\]

It is the covariance scale actually seen by the whitened \(f\)-Hessian. In an eigenbasis
\(A_t=\operatorname{diag}(\alpha_1,\ldots,\alpha_n)\),

\[
\Lambda_t(f)^2
=\frac{\sum_{i,j}\alpha_i\alpha_j(\widehat H_t)_{ij}^2}
       {\sum_{i,j}(\widehat H_t)_{ij}^2}
\le\|A_t\|_{\mathrm{op}}^2.
\tag{6.7}
\]

### Conjecture 6.3 (exact heat-averaged alignment; open)

There exist universal \(\pi\) and \(\delta>0\) such that

\[
\mathbb E\mathsf T
+8\mathbb E\int_0^\infty
J_\pi(t)v_t\Lambda_t(f)^2dt
\le1-\delta.
\tag{6.8}
\]

Conditional on Letwin v1, this implies KLS: (5.2) and (6.6) give

\[
S_t^f
=\|\widehat H_t\|_{\mathrm{HS}}^2\Lambda_t(f)^2
\le8v_t\Lambda_t(f)^2,
\]

so (6.8) implies the source-only version of Theorem 6.1.

Conjecture 6.3 is strictly more targeted than (5.4). It permits a large
\(\|A_t\|_{\mathrm{op}}\) when \(\widehat H_t\) does not occupy the corresponding eigenspaces,
and it only asks for an averaged estimate with the exact kernel consumed by the proof.

## 7. Effective-rank and spectral-incidence relaxations

The exact \(\Lambda_t(f)\) is the correct object, but two coarser sufficient bounds may be more
tractable.

### Lemma 7.1 (effective-rank bounds; proved)

For a nonzero symmetric matrix \(B\), define its stable rank

\[
r_{\mathrm{st}}(B)=\frac{\|B\|_{\mathrm{HS}}^2}{\|B\|_{\mathrm{op}}^2}.
\]

Use the convention \(r_{\mathrm{st}}(0)=+\infty\), so the effective-rank integrand below is zero
when \(\widehat H_t=0\).

Then

\[
\Lambda_t(f)^2
\le\min\left\{
\|A_t\|_{\mathrm{op}}^2,
\frac{\operatorname{Tr}(A_t^2)}{r_{\mathrm{st}}(\widehat H_t)}
\right\}.
\tag{7.1}
\]

Equivalently, with

\[
r_2(A)=\frac{\operatorname{Tr}(A^2)}{\|A\|_{\mathrm{op}}^2},
\]

the second term is
\(\|A_t\|_{\mathrm{op}}^2r_2(A_t)/r_{\mathrm{st}}(\widehat H_t)\).

#### Proof

The first bound is (6.7). Schatten Holder with exponents \(4,\infty,4\) gives

\[
\|A^{1/2}BA^{1/2}\|_{\mathrm{HS}}^2
\le\|B\|_{\mathrm{op}}^2\operatorname{Tr}(A^2).
\]

Divide by \(\|B\|_{\mathrm{HS}}^2\) and take \(B=\widehat H_t\). \(\square\)

### Conjecture 7.2 (heat-averaged effective rank; open)

There exist universal \(\pi,\delta>0\) such that

\[
\mathbb E\mathsf T+8\mathbb E\int_0^\infty J_\pi(t)v_t
\min\left\{
\|A_t\|_{\mathrm{op}}^2,
\frac{\operatorname{Tr}(A_t^2)}{r_{\mathrm{st}}(\widehat H_t)}
\right\}dt
\le1-\delta.
\tag{7.2}
\]

Conditional on Letwin v1, this implies Conjecture 6.3 and hence KLS. It is only a sufficient
surrogate: when \(A_t\simeq I\), the exact value \(\Lambda_t^2\simeq1\) is much sharper than a
poor stable-rank bound. Its potential gain is specifically the regime where \(A_t\) is spiky and
\(\widehat H_t\) has greater effective rank than the spiky covariance sector.

There is a more geometric high-eigenspace version. For \(L>0\), let

\[
P_t^H=\mathbf1_{(L,\infty)}(A_t),
\qquad P_t^L=I-P_t^H,
\]

and define the fraction of whitened \(H_t\)-energy incident to the high covariance space by

\[
\eta_{t,L}(f)=
\frac{
\|P_t^H\widehat H_tP_t^H\|_{\mathrm{HS}}^2
+2\|P_t^H\widehat H_tP_t^L\|_{\mathrm{HS}}^2}
{\|\widehat H_t\|_{\mathrm{HS}}^2},
\tag{7.3}
\]

with value zero when \(\widehat H_t=0\).

### Lemma 7.3 (spectral-incidence split; proved)

For every \(L>0\),

\[
\Lambda_t(f)^2
\le L^2+\|A_t\|_{\mathrm{op}}^2\eta_{t,L}(f).
\tag{7.4}
\]

#### Proof

Use an eigenbasis of \(A_t\). Entries of \(\widehat H_t\) with both indices in the low space are
weighted by \(\alpha_i\alpha_j\le L^2\); every entry incident to the high space is weighted by at
most \(\|A_t\|_{\mathrm{op}}^2\). Divide the resulting estimate by
\(\|\widehat H_t\|_{\mathrm{HS}}^2\). \(\square\)

Since \(\mathbb Ev_t\le v_0=1\), (6.2) and (7.4) give

\[
\mathbb E\int_0^\infty J_\pi(t)v_t\Lambda_t(f)^2dt
\le \frac{L^2}{2}\mathbb E\mathsf T^2
+\mathbb E\int_0^\infty J_\pi(t)v_t
\|A_t\|_{\mathrm{op}}^2\eta_{t,L}(f)dt.
\tag{7.5}
\]

### Conjecture 7.4 (high-space non-alignment; open)

There exist universal \(\pi,L,\delta>0\) such that

\[
\mathbb E\mathsf T
+4L^2\mathbb E\mathsf T^2
+8\mathbb E\int_0^\infty J_\pi(t)v_t
\|A_t\|_{\mathrm{op}}^2\eta_{t,L}(f)dt
\le1-\delta.
\tag{7.6}
\]

The coefficient \(4L^2\mathbb E\mathsf T^2\) is exactly \(8\) times the first term on the
right of (7.5). Conditional on Letwin v1, (7.6) implies KLS. This target asks only that a first
eigenfunction's whitened quadratic tensor not spend too much averaged energy in the randomly
inflated covariance subspace. It is the fixed-eigenfunction analogue of the incident-high
alignment problem in the fixed-cut route.

The logical hierarchy is

\[
\text{(7.6) or (7.2)}
\Longrightarrow \text{(6.8)}
\Longrightarrow \text{source-only (6.4)}
\Longrightarrow \text{KLS},
\]

conditional only at the arrows using Letwin's preprint. The net-source Conjecture 6.2 is weaker
than all source-only versions because it retains damping.

## 8. Counterexample to naive Stein unweighting

Fathi's moment-map construction gives a positive symmetric Stein kernel and the weighted
Poincare inequality

\[
\operatorname{Var}_\mu(f)
\le\mathbb E_\mu\langle\tau_\mu\nabla f,\nabla f\rangle.
\tag{8.1}
\]

The weight cannot be removed by adding only an unweighted Hessian energy.

### Proposition 8.1 (truncated-exponential first-eigenfunction counterexample; proved)

There is no universal constant \(C\) for (1.1), even in dimension one, even after isotropic
normalization, and even when \(f\) is the first nonconstant Neumann eigenfunction.

This directly refutes a statement quantified over all log-concave measures, the scope of KLS.
If (1.1) were instead postulated only for everywhere-positive, uniformly log-concave densities,
transferring this example would additionally require a uniform spectral/Mosco convergence
argument for smooth approximants; no such transfer is claimed here. The compact hard-boundary
example itself is exact.

#### Step 1: measure and Stein kernel

For \(R>0\), let

\[
d\mu_R(x)=\frac{e^{-x}}{1-e^{-R}}\mathbf1_{[0,R]}(x)dx.
\]

Its mean is

\[
m_R=\frac{1-(R+1)e^{-R}}{1-e^{-R}}
=1-\frac{R}{e^R-1},
\tag{8.2}
\]

and

\[
\sigma_R^2
=\frac{2-(R^2+2R+2)e^{-R}}{1-e^{-R}}-m_R^2
\longrightarrow1.
\]

In dimension one the Stein kernel is unique. The centered kernel is

\[
\begin{aligned}
\tau_R(x)
&=\frac{1}{e^{-x}}\int_x^R(y-m_R)e^{-y}dy\\
&=x+1-m_R-(R+1-m_R)e^{x-R}.
\end{aligned}
\tag{8.3}
\]

It has the correct endpoint behavior:

\[
\tau_R(R)=0,
\qquad
\tau_R(0)=1-m_R-(R+1-m_R)e^{-R}=0.
\]

Moreover,

\[
(\tau_R e^{-x})'=-(x-m_R)e^{-x},
\]

so integration by parts proves the Stein identity without boundary terms.

#### Step 2: first eigenfunction and boundary conditions

The self-adjoint generator is

\[
L_Rh=h''-h',
\qquad h'(0)=h'(R)=0.
\]

Writing \(h=e^{x/2}u\) gives

\[
-L_Rh=e^{x/2}\left(-u''+\frac14u\right),
\qquad
u'+\frac12u=0\quad\text{at }0,R.
\tag{8.4}
\]

Besides the constant eigenfunction at eigenvalue zero, the eigenvalues are

\[
\lambda_{j,R}=\frac14+\frac{j^2\pi^2}{R^2},\qquad j\ge1.
\]

Indeed, if \(k^2=\lambda-1/4>0\), the boundary condition at zero gives

\[
u(x)=C\left(\cos(kx)-\frac1{2k}\sin(kx)\right),
\]

and the boundary condition at \(R\) reduces to \(\sin(kR)=0\). For
\(\lambda<1/4\), the same hyperbolic calculation has only the ground state
\(u=e^{-x/2}\), \(\lambda=0\). Thus the \(j=1\) mode below is the first nonconstant one.

For \(k=\pi/R\), an unnormalized first eigenfunction is

\[
f_R(x)=e^{x/2}\left(\cos(kx)-\frac1{2k}\sin(kx)\right).
\tag{8.5}
\]

Its derivative is

\[
f_R'(x)=-e^{x/2}\left(k+\frac1{4k}\right)\sin(kx),
\tag{8.6}
\]

so \(f_R'(0)=f_R'(R)=0\), and

\[
-L_Rf_R=\lambda_Rf_R,
\qquad \lambda_R=\frac14+\frac{\pi^2}{R^2}.
\]

Self-adjointness, or integration of the eigenvalue equation using the Neumann conditions, gives
\(\mathbb E_{\mu_R}f_R=0\). Normalize henceforth so that
\(\mathbb E_{\mu_R}f_R^2=1\). Then

\[
\mathbb E_{\mu_R}(f_R')^2=\lambda_R.
\tag{8.7}
\]

Also \(f_R''=f_R'-\lambda_Rf_R\). Since

\[
f_R(R)^2e^{-R}=f_R(0)^2,
\]

integration by parts yields

\[
\mathbb E_{\mu_R}(f_Rf_R')
=\frac12\mathbb E_{\mu_R}f_R^2.
\]

After the stated normalization this is \(1/2\). Consequently,

\[
\mathbb E_{\mu_R}(f_R'')^2
=\lambda_R-2\lambda_R\left(\frac12\right)+\lambda_R^2
=\lambda_R^2.
\tag{8.8}
\]

#### Step 3: divergence of the Stein energy

Equation (8.6) cancels the exponential density, so

\[
\frac{\mathbb E_{\mu_R}[\tau_R(f_R')^2]}
     {\mathbb E_{\mu_R}(f_R')^2}
=\frac{\int_0^R\tau_R(x)\sin^2(\pi x/R)dx}
       {\int_0^R\sin^2(\pi x/R)dx}.
\tag{8.9}
\]

By symmetry,

\[
\int_0^Rx\sin^2(\pi x/R)dx=\frac{R^2}{4},
\qquad
\int_0^R\sin^2(\pi x/R)dx=\frac R2.
\]

For the final term in (8.3), put \(s=R-x\) and use
\(\sin(\pi s/R)\le\pi s/R\):

\[
\int_0^Re^{x-R}\sin^2(\pi x/R)dx
\le\frac{\pi^2}{R^2}\int_0^\infty s^2e^{-s}ds
=\frac{2\pi^2}{R^2}.
\]

Since \(R+1-m_R=O(R)\), (8.9) becomes

\[
\frac{\mathbb E_{\mu_R}[\tau_R(f_R')^2]}
     {\mathbb E_{\mu_R}(f_R')^2}
=\frac R2+O(1).
\tag{8.10}
\]

Therefore

\[
\mathbb E_{\mu_R}[\tau_R(f_R')^2]
=\lambda_R\left(\frac R2+O(1)\right),
\]

whereas (8.7)--(8.8) give

\[
\mathbb E_{\mu_R}(f_R')^2+
\mathbb E_{\mu_R}(f_R'')^2
=\lambda_R+\lambda_R^2=O(1).
\]

This disproves (1.1) before isotropization.

#### Step 4: isotropization

Let

\[
Y=\frac{X-m_R}{\sigma_R},
\qquad F_R(y)=f_R(m_R+\sigma_Ry).
\]

The transformed law is isotropic and log-concave. Its Stein kernel is

\[
\widetilde\tau_R(y)=\frac1{\sigma_R^2}\tau_R(m_R+\sigma_Ry).
\]

Since \(F_R'=\sigma_Rf_R'\) and \(F_R''=\sigma_R^2f_R''\),

\[
\mathbb E[\widetilde\tau_R(F_R')^2]
=\mathbb E_{\mu_R}[\tau_R(f_R')^2],
\]

while

\[
\mathbb E(F_R')^2+\mathbb E(F_R'')^2
=\sigma_R^2\lambda_R+\sigma_R^4\lambda_R^2=O(1),
\]

because \(\sigma_R^2\to1\). The transformed generator is
\(\widetilde Lh=h''-\sigma_Rh'\), and
\(-\widetilde L F_R=\sigma_R^2\lambda_RF_R\), with Neumann boundary conditions. Thus \(F_R\)
remains the first nonconstant eigenfunction after isotropization. This proves the proposition.
\(\square\)

### Numerical sanity check

A dependency-free trapezoidal quadrature with \(200{,}000\) subintervals gave:

| \(R\) | \(\sigma_R^2\) | \(\lambda_R\) | numerical \(\mathbb E(f_R')^2\) | \(\mathbb E[\tau_R(f_R')^2]/\mathbb E(f_R')^2\) |
|---:|---:|---:|---:|---:|
| 10 | 0.99545959 | 0.34869604 | 0.34869604 | 4.7174108 |
| 20 | 0.99999918 | 0.27467401 | 0.27467401 | 9.9101699 |
| 40 | 1.00000000 | 0.25616850 | 0.25616850 | 19.975920 |

The normalized mean was below \(1.2\times10^{-10}\) in these runs, and the computed Hessian
energy agreed with \(\lambda_R^2\). The last column approaches \(R/2\), as predicted.

### Heat-flow fence

Ordinary Langevin heat averaging cannot repair (1.1). For the semigroup \(P_s=e^{sL_R}\),

\[
P_sf_R=e^{-\lambda_Rs}f_R.
\]

Thus the Stein energy, gradient energy, and Hessian energy all acquire the same factor
\(e^{-2\lambda_Rs}\). Integrating them against any common nonnegative heat-time weight leaves the
diverging ratio unchanged. Any useful heat averaging must instead exploit the evolving posterior
geometry of Sections 3 and 6, or another mechanism that changes the Stein/covariance weight.

## 9. Comparison with the \(H^{-1}\) residual route

Barthe--Klartag prove that, when all coordinate derivatives of \(h\) have mean zero,

\[
\operatorname{Var}_\mu(h)
\le\sum_i\|\partial_i h\|_{H^{-1}(\mu)}^2.
\tag{9.1}
\]

The repository's proposed first-eigenfunction residual is

\[
\sum_i\|\partial_i f-b_i\|_{H^{-1}(\mu)}^2\le C\lambda,
\qquad b=\mathbb E\nabla f.
\tag{9.2}
\]

After the preferred-direction split recorded in
research/kls/routes/moment-map-spectral/README.md, (9.2) is KLS-sufficient. The subsequent model
audit in
[`2026-08-20-kls-hminus1-models.md`](2026-08-20-kls-hminus1-models.md) proves more precisely
that it is quantitatively KLS-equivalent on the regular class; either direction still needs a
uniform regularization or approximate-minimizer passage for arbitrary log-concave measures.

The truncated-exponential example does not refute (9.2). In general, duality gives

\[
\|h\|_{H^{-1}(\mu)}^2
\le C_P(\mu)\mathbb E_\mu h^2
\tag{9.3}
\]

for centered \(h\). The one-dimensional measures above have uniformly bounded Poincare constants,
so their \(H^{-1}\) norm does not acquire the \(R\)-sized spatial multiplier present in the Stein
energy. This is why (9.2) is better calibrated than (1.1).

Letwin's proof controls \(H^{-1}\) norms when the differentiated data become linear after a fixed
linear change of variables. For a general eigenfunction, the fields
\(\partial_i f-b_i\) are nonlinear. Extending the \(H^{-1}\) mechanism to these residuals is a
genuine new theorem; it does not follow by inserting the random matrix \(\nabla^2f(X)\) into
Letwin's fixed-matrix estimate.

## 10. Research verdict

The fixed-eigenfunction localization strand has a rigorous backbone but no unconditional KLS
advance yet:

- **Proved:** the SDEs (3.1), source-damping identity (3.4), absorptive and one-horizon
  conditional KLS implications, the random-horizon version, and the Hilbert--Schmidt dual
  derivation of the whitened \(H_t\) estimate conditional on Letwin v1.
- **Best dynamic headline:** the absorptive estimate (4.6). It is non-tautological, consumes the
  exact damping with \(\alpha<1\), and closes by Ito, Gronwall, the density martingale, and
  posterior Brascamp--Lieb.
- **Weakest exact residual:** control the averaged net source in Conjecture 6.2, or,
  source-only, the exact covariance scale \(\Lambda_t(f)\) in Conjecture 6.3.
- **Structured sufficient targets:** effective-rank Conjecture 7.2 and high-space non-alignment
  Conjecture 7.4. They allow covariance inflation, provided the first eigenfunction's whitened
  quadratic tensor does not align with it for too much heat-scale time.
- **Refuted shortcut:** a universal unweighting of Fathi's positive Stein form by first and second
  Euclidean derivatives, even restricted to first eigenfunctions.
- **Parallel route retained:** the first-eigenfunction \(H^{-1}\) residual (9.2), which avoids the
  pointwise Stein multiplier and is not touched by the counterexample.

The best next analytical calculation is to exploit the eigenfunction equation inside the posterior
channel to relate the damping \(D_t^f\) or the high-space incidence \(\eta_{t,L}(f)\) to the fixed
initial energies \(\lambda\) and \(\mathbb E\|\nabla^2f\|_{\mathrm{HS}}^2\le\lambda^2\). A bound only
on \(\|A_t\|_{\mathrm{op}}\) discards exactly the structure that makes this strand distinct.

## Primary sources

- B. Letwin, *The KLS constant is \(O(\log^{1/4}n)\)*,
  [arXiv:2607.24164v1](https://arxiv.org/abs/2607.24164).
- M. Fathi, *Stein kernels and moment maps*,
  [arXiv:1804.04699](https://arxiv.org/abs/1804.04699), especially the moment-map weighted
  Poincare inequality in Section 4.
- F. Barthe and B. Klartag, *Spectral gaps, symmetries and log-concave perturbations*,
  [arXiv:1907.01823](https://arxiv.org/abs/1907.01823), Proposition 10 for (9.1).
- R. Eldan, *Thin shell implies spectral gap up to polylog via stochastic localization*,
  [arXiv:1203.0893](https://arxiv.org/abs/1203.0893).
- B. Klartag, *Logarithmic bounds for isoperimetry and slices of convex sets*,
  [arXiv:2303.14938](https://arxiv.org/abs/2303.14938), for the current first-eigenfunction and
  improved-Lichnerowicz framework.
