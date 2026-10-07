---
title: 'BK: covariance-normalized localization and moving Appell variance'
ledger-node: [lem:bk-localization-covariance, lem:bk-moving-appell-variance]
numbering:
  enumerator: "154.%s"
---

*Part of the Balasubramanian–Kasiviswanathan proof, Chapter [](#sec:bk-proof); the reading order is on the [full proofs](#sec:proofs-bk) page.*

**Overview.** We reconstruct Sections 6 and Appendix D of
[@BalasubramanianKasiviswanathan2026KLS] at commit
`4837c33649ba2271f43c9684e9350ecbdd725f95`. Quadratic variance bounds control
third moments, prevent finite-time explosion, and control ordered products of
covariance matrices. A finite formal-series calculation then compares the
Appell variance before and after localization.

**Dependencies.** The only inequality input is [](#thm:letwin-qcts).
The Appell normalization [](#def:bk-uniform-appell-coefficients) is stated explicitly below. Standard finite-dimensional
Itô calculus and local existence for smooth SDE coefficients are used.
No KLS, BKL, SZ v2, or all-degree coefficient estimate is an input.

:::{prf:theorem} Global localization and ordered covariance bounds
:label: thm:sol-bk-localization
Let $\mu_0$ be any compactly supported isotropic log-concave law on
$\mathbb R^n$. Write
$$
 \mu_{\theta,\Lambda}(dx)=Z(\theta,\Lambda)^{-1}
 e^{\theta\cdot x-x^T\Lambda x/2}\mu_0(dx),
$$
and let $m(\theta,\Lambda)$ and $A(\theta,\Lambda)$ be its mean and covariance.
The SDE, started at $(0,0)$,
$$
 d\theta_t=A_t^{-1/2}dB_t+A_t^{-1}m_tdt,
 \qquad d\Lambda_t=A_t^{-1}dt,
 \qquad \mu_t=\mu_{\theta_t,\Lambda_t},
$$
has a global solution with $A_t\succ0$. Every bounded Borel test has
$\int f\,d\mu_t$ a true martingale. On the full ordered tensor spaces,
for every integer $k\ge1$, $0\le s\le t$, every integer $d\ge1$, and
$s_1,\ldots,s_d\in[0,t]$,
$$
 \mathbb E[A_t^{\otimes k}\mid\mathcal F_s]
 \preceq e^{4k^2(t-s)}A_s^{\otimes k},\qquad
 \mathbb E[A_{s_1}\otimes\cdots\otimes A_{s_d}]
 \preceq e^{4d^2t}I.
$$
For $t>0$, $0\le q\le d$ and $\delta\ge0$,
$$
 \mathbb E[(A_t+\delta\Lambda_t^{-1})^{\otimes q}
       \otimes A_t^{\otimes(d-q)}]
 \preceq (1+\delta/t)^q e^{4d^2t}I.
$$
This proves [](#lem:bk-localization-covariance).
:::

:::{prf:proof}
Suppose the support lies in $B_R$. All tilt moments are smooth in the finite
parameters and $A$ is positive definite: tilt densities are strictly positive
relative to the original full-dimensional law. Local existence therefore holds.
Put $\xi_t=A_t^{-1/2}(x-m_t)$. Differentiating the normalization gives
$$
 d\log Z_t=m_t^TA_t^{-1/2}dB_t+\tfrac12m_t^TA_t^{-1}m_tdt,
 \qquad d\rho_t(x)=\rho_t(x)\xi_t(x)\cdot dB_t,
$$
where $\rho_t=d\mu_t/d\mu_0$. Consequently, initially up to localization,
$$
 dE_tf=E_t[(f-E_tf)\xi_t]\cdot dB_t.
$$
These formulas follow by Itô from the smooth tilt integral also for bounded
Borel $f$, since compact support permits parameter differentiation.

For any isotropic log-concave $Y$, set $S_i=E[Y_iYY^T]$ and
$S(v)=\sum_i v_iS_i$. By [](#thm:letwin-qcts) and Cauchy--Schwarz,
$$
 |\langle S(v),H\rangle|\le |v|\sqrt{\operatorname{Var}(Y^THY)}
 \le\sqrt8|v|\|H\|_{\rm HS}.
$$
Thus $\|S(v)\|_{\rm HS}^2\le8|v|^2$. Symmetry of all three tensor indices
identifies this squared norm with $v^T(\sum_i S_i^2)v$. Also
$$
 0\preceq\sum_i(S_i\otimes I-I\otimes S_i)^2
 =\sum_i S_i^2\otimes I+I\otimes\sum_i S_i^2-2\sum_iS_i\otimes S_i.
$$
Hence $\sum_iS_i^2\preceq8I$ and $\sum_iS_i\otimes S_i\preceq8I$.
Apply these pointwise to the posterior $\xi_t$ and put
$U_{i,t}=A_t^{1/2}S_{i,t}A_t^{1/2}$. Differentiating its first two moments gives
$$
 dm_t=A_t^{1/2}dB_t,\qquad
 dA_t=\sum_iU_{i,t}dB_{i,t}-A_tdt,\qquad
 \sum_iU_{i,t}\otimes U_{i,t}\preceq8A_t\otimes A_t.
$$

To prove nonexplosion, let $\zeta$ be the maximal lifetime. Matrix Itô gives
$$
 d\log\det A_t=\sum_i\operatorname{Tr}(S_{i,t})dB_{i,t}
 -\left(n+\tfrac12\sum_i\operatorname{Tr}(S_{i,t}^2)\right)dt.
$$
The drift rate lies in $[-5n,-n]$ and the martingale quadratic variation rate
is at most $8n^2$. Extend the martingale integrand by zero beyond $\zeta$;
it defines a continuous square-integrable martingale on every finite interval.
On $\{\zeta\le T\}$ the log determinant therefore has a finite limit and is
bounded below before $\zeta$. Since $A_t\preceq R^2I$, its least eigenvalue
is at least $\det A_t/R^{2(n-1)}$, with a positive pathwise lower bound.
Consequently $A_t^{-1}$ is pathwise bounded up to $\zeta$, as is $m_t$.
The drift integrals for $\theta,\Lambda$ have finite limits. Stopping the
martingale in $\theta$ when $\|A_t^{-1}\|$ exceeds an integer gives continuous
extensions with bounded quadratic variation; on each such path one of these
stops is never reached. Thus $\theta,\Lambda$ have finite limits at $\zeta$.
At their limit $A$ is positive definite and local smooth-coefficient existence
extends the SDE, a contradiction. Since $T$ was arbitrary, $\zeta=\infty$.
The bounded local martingale $E_tf$ is now a true martingale by bounded
convergence along its localizing sequence, also conditionally.

The drift of $A_t^{\otimes k}$ has $k$ linear terms and one quadratic-variation
term for each pair of slots. Tensoring the preceding two-slot bound with the
positive remaining factors gives a drift at most
$$
 [-k+8\tbinom k2]A_t^{\otimes k}\preceq4k^2A_t^{\otimes k}.
$$
The stochastic terms are true martingales: $A_t\preceq R^2I$ and
$\sum_i\|U_{i,t}\|_{\rm HS}^2\le8nR^4$ bound their squared scalar integrands
for each fixed tensor test by $8nk^2R^{4k}|z|^4$. Multiplication by
$e^{-4k^2t}$ and conditional expectation prove the first bound, initially
for rational test vectors and then simultaneously by continuity.

For mixed times, permute slots into increasing time order. If the latest time
$u$ occurs $k$ times and $v$ is the next earlier time (or zero), condition on
$\mathcal F_v$. All other factors form a positive $\mathcal F_v$-measurable
operator. The conditional bound replaces $A_u^{\otimes k}$ by
$e^{4k^2(u-v)}A_v^{\otimes k}$. Repeat after merging equal times.
The successive intervals are disjoint and contained in $[0,t]$, and $k\le d$;
the accumulated factor is at most $e^{4d^2t}$, with all final factors equal
to $A_0=I$. Undo the slot permutation.

Finally integrate the positive block matrices
$\left(\begin{smallmatrix}A_s&I\\I&A_s^{-1}\end{smallmatrix}\right)$.
Their Schur complement yields
$\Lambda_t^{-1}\preceq t^{-2}\int_0^t A_sds$.
Insert this comparison in each of any $j$ selected tensor slots, expand the
integrals, and use the mixed-time estimate. This gives an upper bound
$t^{-j}e^{4d^2t}I$ for the corresponding expectation with $\Lambda_t^{-1}$
in those slots and $A_t$ in the others. Boundedness of $A_s$ justifies all
integrations entrywise. Expanding the first $q$ factors of
$(A_t+\delta\Lambda_t^{-1})$ now sums to $(1+\delta/t)^q$.
:::

For any law with all moments define $P_d^\mu[T]=\langle T,\mathcal A_d^\mu\rangle$
by the formal identity
$$
 \frac{e^{z\cdot x}}{E_\mu e^{z\cdot X}}
 =\sum_{d\ge0}\frac{\langle\mathcal A_d^\mu(x),z^{\otimes d}\rangle}{d!},
 \qquad c_d(\mu)=\frac1{d!}\sup_{\|T\|=1}\|P_d^\mu[T]\|_2.
$$
All tensors use the ordered-index Hilbert--Schmidt norm. In particular,
$D_vP_d[T]=dP_{d-1}[T(v,\cdot)]$, and all expected derivatives of order
less than $d$ vanish. If $X=m+BY$, coefficient comparison gives
$P_d^{\mathcal L(X)}[T](m+By)=P_d^{\mathcal L(Y)}[(B^T)^{\otimes d}T](y)$.

:::{prf:theorem} Moving variance with lower-degree error
:label: thm:sol-bk-moving-appell
Fix $d\ge2$ and finite constants $C_k\ge0$ such that $c_k(\nu)\le C_k$
for every isotropic log-concave law in every dimension and $1\le k<d$.
Set $\Sigma_d=\sum_{k=2}^{d-1}(d-k+1)C_kC_{d-k+1}$, with an empty sum zero.
For the localization above, fixed $T\in\operatorname{Sym}^d\mathbb R^n$,
$p_t=P_d^{\mu_t}[T]$ and $V(t)=\mathbb E E_tp_t^2$, one has, for all $t\ge0$,
$$
 \sqrt{V(0)}\le e^{(d+1)t}\sqrt{V(t)}
       +d!\Sigma_dt\,e^{(2d^2+d+1)t}\|T\|.
$$
This proves [](#lem:bk-moving-appell-variance).
:::

:::{prf:proof}
At a fixed time put $\Psi(z)=\log E e^{z\cdot X}$, $\Gamma_j=D^j\Psi(0)$,
and define finite-on-polynomials constant-coefficient operators
$$
 C_i=\sum_{k\ge1}\frac1{k!}\langle A^{-1/2}e_i,\Gamma_{k+1}[D^k]\rangle,
 \qquad R_i=\xi_i-C_i.
$$
Their symbols are $u_i(z)=[A^{-1/2}(\nabla\Psi(z)-m)]_i$.
The moment-series SDE is $dZ=Z\sum_i u_i dB_i$. Applying Itô to $Z^{-1}$
and comparing finitely many formal coefficients gives
$$
 dp_t=-\sum_iC_ip_t,dB_i+\sum_iC_i^2p_t,dt.
$$
No derivative of a time-varying operator is taken in this formula: each
symbol is evaluated at that time. Combining the square differential with
$d\rho=\rho\xi\cdot dB$ gives the variance drift
$$
 D_t=\sum_i\|C_ip_t\|_2^2-2\langle p_t,\sum_iR_iC_ip_t\rangle_2.
$$
Differentiating the generating function in $z$ along $A^{-1/2}e_i$ gives
$$
 R_iP_j[S]=P_{j+1}[\operatorname{Sym}(A^{-1/2}e_i\otimes S)].
$$
Another coefficient comparison, in
$E[Xe^{z\cdot X}]/Ee^{z\cdot X}=\nabla\Psi(z)$, gives
$$
 \Gamma_{k+1}[U]=E[(X-m)P_k[U]].
$$
For an isotropic law Bessel's inequality for its orthonormal coordinate
functions implies
$\|\Gamma_{k+1}:\operatorname{Sym}^k\to\mathbb R^n\|\le k!c_k$.

Whiten at this fixed time: $y=A^{-1/2}(x-m)$,
$\widetilde T=(A^{1/2})^{\otimes d}T$ and
$\bar p=P_d^{\mathcal L(\xi)}[\widetilde T]$.
The chain rule and cumulant transformation show that $C_i$ becomes
$\sum_{k\ge1}(k!)^{-1}(\Gamma_{k+1}^{\xi}[D_y^k])_i$ and $R_i$ becomes
$y_i-C_i$. These are only identities for evaluating the already-computed drift.
In $\sum_i R_i C_i\bar p$, the $k=1$ contribution is $d\bar p$:
$\Gamma_2^\xi=I$ and the raising formula reconstructs each of its $d$ slots.
The $k=d$ contribution is $\langle E_t[p_t\xi_t],\xi_t\rangle$;
its pairing with $p_t$ is $|E_t[p_t\xi_t]|^2\le E_tp_t^2$.

For $2\le k\le d-1$, put $j=d-k+1$ and contract $k$ ordered slots of
$\widetilde T$ with $\Gamma_{k+1}^\xi$, producing
$W_k\in\mathbb R^n\otimes\operatorname{Sym}^{d-k}\mathbb R^n$.
Applying the cumulant norm bound to each fixed remaining-index slice gives
$\|W_k\|\le k!C_k\|\widetilde T\|$.
Differentiation and raising give precisely
$$
 \frac{d!}{k!(d-k)!}P_j^{\mathcal L(\xi)}[\operatorname{Sym}W_k].
$$
Since symmetrization is an orthogonal projection, its norm is at most
$d!jC_kC_j\|\widetilde T\|$. Dropping the nonnegative square term in the
drift and writing $v_t=E_tp_t^2$ therefore gives
$$
 D_t\ge-2(d+1)v_t-2d!\Sigma_d\sqrt{v_t}\|\widetilde T_t\|.
$$

It remains to justify expectation without an inverse-covariance bound in mean.
Every posterior moment through order $2d$ is bounded deterministically by
compact support. Its diffusion coefficient satisfies
$|E_t[f\xi_t]|^2\le E_tf^2\le\sup_{B_R}|f|^2$ by Bessel.
The variance $v_t$ is a fixed polynomial in these finitely many moments:
formal inversion uses only addition and multiplication since the constant
moment is one. Its Itô drift and diffusion thus have deterministic bounds.
Stopping on bounded tilt parameters and removing the stops gives convergence
of stochastic integrals in $L^2$ and drifts in $L^1$. Hence $V$ is locally
absolutely continuous and $V'=\mathbb ED_t$ almost everywhere. Cauchy--Schwarz
and the equal-time covariance estimate give
$$
 V'(t)\ge-2(d+1)V(t)
       -2d!\Sigma_d\sqrt{V(t)}e^{2d^2t}\|T\|.
$$
For $T\ne0$, the leading polynomial is nonzero and a full-dimensional
log-concave law cannot be supported on its zero set; thus $V(t)>0$.
Continuity gives a positive minimum on each compact time interval. Divide
by $2\sqrt V$, multiply by $e^{(d+1)t}$ and integrate to obtain
$$
 \sqrt{V(0)}\le e^{(d+1)t}\sqrt{V(t)}
 +d!\Sigma_d\|T\|\int_0^t e^{(2d^2+d+1)s}ds.
$$
Bounding the integral by its endpoint times $t$ proves the result.
For $T=0$ it is immediate.
:::

**Fences respected.** These new nodes have no assigned `bounded_by` edges.
The brief's projection ceiling is avoided by a full tensor estimate, not
projection estimates. No adaptive cut, scalar covariance ceiling, uniform
all-degree bound, sharp gate-zero claim, or open antecedent is used.
Compact support is used only here; its later removal belongs to reverse transfer.

**Reviewer handoff.** Check the two-slot Loewner inequality on the full tensor
space, the log-determinant continuation argument, mixed-time conditioning,
the $k=d$ Bessel endpoint, and the moment-polynomial justification of expectation.
The lower-degree bounds in the second theorem are quantified antecedents,
not asserted uniform coefficient theorems. The covariance and moving-variance statements use the inputs specified above; their certifications are recorded separately.
