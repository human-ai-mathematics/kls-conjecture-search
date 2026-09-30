---
---
# KLS route probe: the tight-prefix soft-projector injection

Date: 2026-08-27

Role: `kls-route-prober`

Concurrency key: singleton `kls-gate:q:upgrade` ownership for this wave

Target: `conj:trace-upgrade`, and only `conj:trace-upgrade`

Artifact ownership: this file only. No ledger, manuscript, route-control, bibliography,
solution, review, knowledge, or numerical file is changed.

## Outcome

The prefix It\^o identity and the arithmetic of the implication to
`ass:tight-prefix-carleson` are correct, subject to two qualifications that must remain
explicit:

1. the cutoff has to be nondecreasing and take values in $[0,1]$, not merely have the two
   displayed plateau values; and
2. the low-block estimate currently uses the unreviewed Letwin version-1 quadratic-chaos
   import.

The exact next estimate staged by the orchestrator is nevertheless **false**. The raw sum of
the $D^2\chi$ curvature and $D\chi$ cross-variation contractions is not cut-local or
tensor-stable. Take a Gaussian coordinate carrying a halfspace cut and append arbitrarily many
independent centered one-sided-exponential spectators. The cut source, information, and damping
remain entirely in the Gaussian coordinate. Every spectator instead has $B=G=0$, $R=A$, and
$\Gamma=\Theta$. Its contribution to the proposed injection is exactly the It\^o injection of
$\operatorname{Tr}(A\chi(A))$ and satisfies

$$
\mathfrak J_{\chi,\mathrm{spect}}^0(h)
=\mathbb E\operatorname{Tr}(A_h\chi(A_h))
+\mathbb E\int_0^h
\operatorname{Tr}\!\left(\chi(A_t)A_t^2+A_t^3\chi'(A_t)\right)dt
\ge \mathbb E\operatorname{Tr}(A_h\chi(A_h)).
\tag{S1}
$$

The published covariance-spike input makes the last expectation strictly positive for each
one-dimensional exponential spectator at every sufficiently small fixed time. Contributions
therefore grow linearly with the number of spectators, whereas the proposed right side remains
unchanged. This refutes the raw prefix-injection estimate for every legitimate fixed cutoff.

It does **not** refute `ass:tight-prefix-carleson`, `conj:trace-upgrade`, or KLS. In the same product the
spectator source is zero, and the positive injection in (S1) cancels exactly against the terminal
and deterministic terms that the proposed reduction discarded. The route remains viable only
after replacing the raw contraction bound by a spectator-cancelling, cut-relative estimate.

No equivalence or transfer involving high-rank `conj:stein-weighted` or `conj:product-alignment` is asserted or
analyzed here.

## Gate, quoted verbatim

The live `conj:trace-upgrade` gate in `research/kls/gating.md` is:

> Produce the tight-prefix absorptive trace estimate `ass:tight-prefix-carleson`, with every source
> and damping term matched to `thm:scalar-riccati`. For one fixed cutoff $\chi=0$ on
> $(-\infty,3]$ and $\chi=1$ on $[4,\infty)$, the next exact gate is the prefix soft-projector
> injection estimate: control its two cut-dependent $D^2\chi$ curvature and $D\chi$
> cross-variation contractions by $C_0T+C_1\mathbb E\int r_t+\gamma\mathbb E\int D_t$ with
> $\gamma<1/8$. The time-zero prefix removes the interval-boundary decrement. Rank tails alone do
> not control either surviving contraction.

The exact staged estimate is, with $H=T\wedge\tau_\eta$,

$$
\begin{aligned}
\mathfrak J_\chi^0(T)
&=\frac12\mathbb E\int_0^H\sum_k
\operatorname{Tr}\!\left(
D^2\chi(A_t)[\Theta_{t,k},\Theta_{t,k}]R_t
\right)dt\\
&\quad+\mathbb E\int_0^H\sum_k
\operatorname{Tr}\!\left(
D\chi(A_t)[\Theta_{t,k}]\Gamma_{t,k}
\right)dt
\end{aligned}
\tag{G1}
$$

and the requested upper bound is

$$
\mathfrak J_\chi^0(T)
\le C_\chi T+C_r\mathbb E\int_0^H r_tdt
+\gamma\mathbb E\int_0^H D_tdt,
\qquad \gamma<\frac18.
\tag{G2}
$$

The phrase “cut-dependent” in the gate is not true term by term: $R$ and $\Gamma$ retain an
entire cut-free spectator block whenever the cut is cylindrical. That is the defect exploited
below.

## Exact objects and certified inputs

Use the standing two-color notation

$$
B_t=s_t\delta_t\delta_t^T,
\qquad
R_t=A_t-B_t\succeq0,
\qquad
S_t=s_t\|G_t\|_{\mathrm{HS}}^2,
$$

$$
D_t=2s_t\delta_t^TA_t\delta_t-r_t^2,
\qquad r_t=\operatorname{Tr}B_t.
$$

The certified Riccati dossier `solutions/kls-localization-riccati-core.tex` gives

$$
dA_t=\sum_k\Theta_{t,k}\,dW_{t,k}-A_t^2dt,
\qquad
dR_t=\sum_k\Gamma_{t,k}\,dW_{t,k}
-(R_t^2+s_tG_t^2)dt.
\tag{2.1}
$$

The full-matrix refinement `solutions/cor-full-matrix-dissipation.tex`, with its passing repair
review, gives

$$
\mathbb ER_T+\mathbb E\int_0^T(R_t^2+s_tG_t^2)dt\preceq R_0.
\tag{2.2}
$$

It deliberately gives no trace upgrade. Its certified Gaussian-halfspace example already shows
that independent spectator directions can spend order $n$ in the traced $R_t^2$ term. The same
spectator geometry is visible more sharply in (G1).

For completeness, if $\alpha_t=q_t-p_t$, direct differentiation of
$B_t=v_tv_t^T/s_t$, $v_t=s_t\delta_t$, gives

$$
\Gamma_{t,k}=\Theta_{t,k}-\mathcal N_{t,k},
\tag{2.3}
$$

where

$$
\mathcal N_{t,k}
=s_t\left((K_te_k)\delta_t^T+\delta_t(K_te_k)^T\right)
-\alpha_t(\delta_t)_kB_t.
\tag{2.4}
$$

An equivalent decomposition, useful for seeing what is and is not controlled by log-concavity,
is

$$
\Gamma_{t,k}
=p_tT^E_{t,k}+q_tT^{E^c}_{t,k}+s_t(\delta_t)_kG_t,
\tag{2.5}
$$

where $T^E_{t,k}$ and $T^{E^c}_{t,k}$ are the third central-moment matrices of the two
conditional laws. To verify (2.5), expand $X-a_t$ as
$X-m_t^E+q_t\delta_t$ on $E$ and as
$X-m_t^{E^c}-p_t\delta_t$ on $E^c$, then subtract (2.4). This identity supplies no general
bound: conditioning an arbitrary fixed cut need not preserve log-concavity.

The low-block step uses the conditional imported estimate

$$
s_t\|A_t^{-1/2}K_tA_t^{-1/2}\|_{\mathrm{HS}}^2\le8,
\tag{2.6}
$$

which comes from `thm:letwin-qcts`. That node is an unreviewed preprint import, so every
implication using (2.6) remains conditional on it.

## Independent audit of the prefix It\^o identity

### Cutoff hypotheses

For the reduction advertised in the gate, one needs a fixed $C^2$ function
$\chi:\mathbb R\to[0,1]$ such that

$$
\chi=0\text{ on }(-\infty,3],
\qquad
\chi=1\text{ on }[4,\infty),
\qquad
\chi'\ge0.
\tag{3.1}
$$

The range and monotonicity occur in the rank-orientation probe but are omitted from the short
live-gate sentence. They are load-bearing: $F=\chi(A)\succeq0$, $F\succeq
\mathbf1_{[4,\infty)}(A)$, and $A^2\chi'(A)\succeq0$ are all used below. A nonmonotone cutoff
would not retain the claimed favorable signs and would not establish the advertised implication.

Put

$$
F_t=\chi(A_t),
\qquad
Y_t=\operatorname{Tr}(F_tR_t)\ge0.
$$

On a compact regularization, or up to the usual bounded coefficient stopping, the finite-
dimensional Daleckii--Krein It\^o formula gives

$$
\begin{aligned}
dF_t
&=\sum_kD\chi(A_t)[\Theta_{t,k}]dW_{t,k}
-A_t^2\chi'(A_t)dt\\
&\quad+\frac12\sum_k
D^2\chi(A_t)[\Theta_{t,k},\Theta_{t,k}]dt.
\end{aligned}
\tag{3.2}
$$

The drift identity is exact because $-A_t^2$ commutes with $A_t$. Applying the product rule to
$\operatorname{Tr}(F_tR_t)$ gives the quadratic covariation with coefficient one:

$$
\begin{aligned}
dY_t
&=dM_t-\operatorname{Tr}(F_tR_t^2)dt
-s_t\operatorname{Tr}(F_tG_t^2)dt
-\operatorname{Tr}(A_t^2\chi'(A_t)R_t)dt\\
&\quad+\frac12\sum_k\operatorname{Tr}\!\left(
D^2\chi(A_t)[\Theta_{t,k},\Theta_{t,k}]R_t
\right)dt\\
&\quad+\sum_k\operatorname{Tr}\!\left(
D\chi(A_t)[\Theta_{t,k}]\Gamma_{t,k}
\right)dt.
\end{aligned}
\tag{3.3}
$$

Stopping at $H=T\wedge\tau_\eta$, taking expectations first under bounded localization, and
then removing the auxiliary stop yields

$$
\begin{aligned}
\mathbb E\int_0^H s_t\operatorname{Tr}(F_tG_t^2)dt
&=Y_0-\mathbb EY_H
-\mathbb E\int_0^H\operatorname{Tr}(F_tR_t^2)dt\\
&\quad-\mathbb E\int_0^H
\operatorname{Tr}(A_t^2\chi'(A_t)R_t)dt
+\mathfrak J_\chi^0(T).
\end{aligned}
\tag{3.4}
$$

All three discarded terms have the claimed sign. For positive semidefinite $F,R$,
$\operatorname{Tr}(FR^2)=\operatorname{Tr}(RFR)\ge0$; similarly
$\operatorname{Tr}(A^2\chi'(A)R)\ge0$. Isotropy gives $A_0=I$, hence $F_0=0$ and $Y_0=0$.
Thus (3.4) implies

$$
\mathbb E\int_0^H s_t\operatorname{Tr}(F_tG_t^2)dt
\le\mathfrak J_\chi^0(T).
\tag{3.5}
$$

There is no stopping local-time term: $Y$ is first formed as a continuous semimartingale and
then stopped. At eigenvalue collisions the $C^2$ spectral map is interpreted through repeated
divided differences, not a differentiable eigenbasis. Compact support makes all coefficients
bounded on the tight mass window. For general log-concave laws, the same identity is first used
under bounded coefficient stopping; only inequalities with controlled nonnegative terms may be
passed through the repository's regularization convention. This is enough for the implication
audit and for the explicit product below.

## Independent audit of (G2) $\Rightarrow$ the tight-prefix estimate

Let

$$
P_t=\mathbf1_{[4,\infty)}(A_t),
\qquad Q_t=I-P_t.
$$

Since $F_t\succeq P_t$, symmetry of $G_t$ gives

$$
s_t\left(\|P_tG_tP_t\|_{\mathrm{HS}}^2
+2\|P_tG_tQ_t\|_{\mathrm{HS}}^2\right)
\le2s_t\operatorname{Tr}(F_tG_t^2).
\tag{4.1}
$$

The factor two on the right is necessary: $\operatorname{Tr}(FG^2)$ counts a high--low entry
from its high row once, whereas the full symmetric Hilbert--Schmidt energy counts both
orientations.

On the tight window, $|q_t-p_t|\le2\eta$, $s_t\ge1/4-\eta^2$, and
$G_t=K_t-(q_t-p_t)\delta_t\delta_t^T$. Young's inequality with parameter $2$ gives

$$
\begin{aligned}
s_t\|Q_tG_tQ_t\|_{\mathrm{HS}}^2
&\le3s_t\|Q_tK_tQ_t\|_{\mathrm{HS}}^2
+\frac32\frac{(q_t-p_t)^2}{s_t}r_t^2\\
&\le384+\frac34D_t.
\end{aligned}
\tag{4.2}
$$

Indeed, (2.6) and $Q_tA_tQ_t\preceq4Q_t$ give the first contribution
$3\cdot8\cdot4^2=384$. For $\eta\le1/6$,

$$
\frac{(q-p)^2}{s}\le\frac12,
$$

and $r^2\le D$, giving the second contribution $3D/4$.

Combining (3.5), (4.1), and (4.2) gives

$$
\mathbb E\int_0^H S_tdt
\le384T+\frac34\mathbb E\int_0^H D_tdt
+2\mathfrak J_\chi^0(T).
\tag{4.3}
$$

Thus (G2) would produce

$$
\mathbb E\int_0^H S_tdt
\le(384+2C_\chi)T
+2C_r\mathbb E\int_0^H r_tdt
+\left(\frac34+2\gamma\right)
\mathbb E\int_0^H D_tdt.
\tag{4.4}
$$

The threshold is exactly

$$
\gamma<\frac18
\quad\Longleftrightarrow\quad
\frac34+2\gamma<1.
$$

Therefore the It\^o identity, the factor-two mixed block, the constant $384$, and the
$\gamma<1/8$ arithmetic are correct. The implication remains conditional on (2.6). The failure
is that (G2) itself is stronger than the source estimate and is false.

## Exact spectator refutation of (G2)

### Product and cut

Let $\gamma_1$ be the standard Gaussian law and let $\xi$ be the centered rate-one
one-sided-exponential law. For an integer $N\ge1$, set

$$
\mu_N=\gamma_1\otimes\xi^{\otimes N}
$$

and take the cylinder

$$
E=\{x_0\ge0\}\times\mathbb R^N.
\tag{5.1}
$$

This is an isotropic log-concave product and $\mu_N(E)=1/2$. Under stochastic localization the
posterior remains a coordinate product. Write $a_t^0=(1+t)^{-1}$ for the deterministic Gaussian
posterior variance and $\lambda_t^j$ for the $j$th exponential posterior variance. In the fixed
coordinate basis,

$$
A_t=\operatorname{diag}(a_t^0,\lambda_t^1,\ldots,\lambda_t^N),
$$

$$
B_t=\operatorname{diag}(r_t,0,\ldots,0),
\qquad
G_t=\operatorname{diag}(g_t^0,0,\ldots,0),
\tag{5.2}
$$

and hence each spectator block has

$$
R_t^j=\lambda_t^j,
\qquad
G_t^j=0,
\qquad
\Gamma_t^j=\Theta_t^j.
\tag{5.3}
$$

The Gaussian covariance has no martingale coefficient, and $a_t^0<3$, so the base block makes
zero contribution to (G1). All of (G1) is the sum of the $N$ spectator contributions. The mass
process $p_t$ and $\tau_\eta$ are functions only of the Gaussian base observation and are
independent of every spectator process.

Also, $B_t\preceq A_t$ and (5.2) give the dimension-free pathwise bounds

$$
0\le r_t\le a_t^0\le1,
\qquad
0\le D_t=2a_t^0r_t-r_t^2\le2.
\tag{5.4}
$$

Thus the right side of (G2) is at most $(C_\chi+C_r+2\gamma_+)T$, independently of $N$, where
$\gamma_+=\max\{\gamma,0\}$.

### One spectator: exact positive injection

For one exponential spectator, write

$$
d\lambda_t=\vartheta_t\,dW_t-\lambda_t^2dt.
\tag{5.5}
$$

Because $A$, $\Theta$, and $\Gamma$ commute in this scalar block, its integrand in (G1) is

$$
j_t=\left(\chi'(\lambda_t)+\frac{\lambda_t}{2}\chi''(\lambda_t)\right)
\vartheta_t^2.
\tag{5.6}
$$

Put $g(u)=u\chi(u)$. Then $g(1)=0$,
$g'(u)=\chi(u)+u\chi'(u)\ge0$, and
$g''(u)=2\chi'(u)+u\chi''(u)$. Scalar It\^o calculus gives, for every deterministic $h>0$,

$$
\begin{aligned}
f_\chi(h)
&:=\mathbb E\int_0^h j_tdt\\
&=\mathbb E g(\lambda_h)
+\mathbb E\int_0^h g'(\lambda_t)\lambda_t^2dt\\
&=\mathbb E[\lambda_h\chi(\lambda_h)]
+\mathbb E\int_0^h
\left(\chi(\lambda_t)\lambda_t^2
+\chi'(\lambda_t)\lambda_t^3\right)dt
\ge0.
\end{aligned}
\tag{5.7}
$$

This is the scalar form of (S1). It also verifies directly that no sign convention from (3.3)
is being reused circularly.

The published covariance-spike node `prop:covariance-spike`, applied in dimension one with the
Gaussian-channel variance $s=1/h$, gives

$$
\mathbb P\!\left(\lambda_h\ge\frac{c_{\rm sp}}h\right)
\ge\frac12e^{-1/h}.
\tag{5.8}
$$

The observation conversion is $c_h/h=X+h^{-1/2}G$. Choose $h$ with
$h\le c_{\rm sp}/4$. Since $\chi=1$ on $[4,\infty)$, (5.7)--(5.8) give the strict lower bound

$$
f_\chi(h)\ge4\,\mathbb P(\lambda_h\ge4)
\ge2e^{-1/h}>0.
\tag{5.9}
$$

No persistent spike event is used. The derivatives of $\chi$ are supported where
$3<\lambda<4$, and one-dimensional log-concave standardized third moments are bounded, so the
finite-horizon It\^o expectations can be justified directly by localization. Alternatively,
truncate, recenter, and rescale the exponential prior, prove (5.7) on the compact process, and
pass to the fixed-time limit; the strict event in (5.9) persists after an arbitrarily small
threshold slack.

### Independent tight stopping

For the Gaussian base,

$$
p_t=\Phi\!\left(\frac{c_t^0}{\sqrt{1+t}}\right),
\qquad
c_t^0=tX_0+W_t^0.
\tag{5.10}
$$

Let $z_\eta=\Phi^{-1}(1/2+\eta)>0$. If
$T\le z_\eta/2$, the event

$$
\{|X_0|\le1\}\cap
\left\{\sup_{0\le t\le T}|W_t^0|<z_\eta/2\right\}
$$

has positive probability and implies $\tau_\eta>T$. Hence

$$
w_\eta(T):=\mathbb P(\tau_\eta>T)>0.
\tag{5.11}
$$

Put $H=T\wedge\tau_\eta$. Conditional on the base-measurable value $H=h$, every spectator has
the unchanged deterministic-horizon expectation $f_\chi(h)$. Since $f_\chi(h)\ge0$ for every
$h$ and $H=T$ on $\{\tau_\eta>T\}$,

$$
\mathfrak J_\chi^0(T)
=N\mathbb E f_\chi(H)
\ge Nw_\eta(T)f_\chi(T).
\tag{5.12}
$$

Choose

$$
0<T\le\min\left\{T_0,\frac{c_{\rm sp}}4,
\frac{z_\eta}2\right\}.
$$

Equations (5.9) and (5.12) yield

$$
\mathfrak J_\chi^0(T)
\ge2Nw_\eta(T)e^{-1/T}.
\tag{5.13}
$$

The right side of (G2) is bounded independently of $N$ by (5.4). Taking

$$
N>
\frac{(C_\chi+C_r+2\gamma_+)T}
{2w_\eta(T)e^{-1/T}}
$$

contradicts (G2). The quantifier order is

$$
(\chi,C_\chi,C_r,\gamma,\eta,T_0)
\longrightarrow T
\longrightarrow N.
$$

This proves that no fixed legitimate cutoff admits the proposed universal raw-injection bound.

### Why this does not refute the source estimate

For a spectator block, $G=0$ identically. Equation (3.4) restricted to that block is precisely

$$
0=-\mathbb E[\lambda_H\chi(\lambda_H)]
-\mathbb E\int_0^H
\left(\chi(\lambda_t)\lambda_t^2
+\chi'(\lambda_t)\lambda_t^3\right)dt
+\mathfrak J_{\chi,\mathrm{spect}}^0(H).
$$

Thus the large positive contraction is cancelled exactly by terms discarded in (3.5). The
actual $S,r,D$ processes in (5.2) live in the single Gaussian base coordinate and do not grow
with $N$. The witness refutes the proposed sufficient estimate, not its intended conclusion.

## What the obvious spectator subtraction leaves

The obstruction is not repaired by silently deleting spectator coordinates. There is no
canonical spectator decomposition for a general cut. The invariant algebraic subtraction is
the cut-free spectral potential

$$
\Psi_\chi(A)=\operatorname{Tr}(A\chi(A)).
$$

Write $Z_t=\operatorname{Tr}(F_tB_t)$ and use (2.3)--(2.4). Subtracting the It\^o identity for
$\Psi_\chi(A_t)$ from (3.4) cancels every block with $B=0$ and gives, on a prefix,

$$
\begin{aligned}
\mathbb E\int_0^H s_t\operatorname{Tr}(F_tG_t^2)dt
&=\mathbb EZ_H
+\mathbb E\int_0^H
\left(2\operatorname{Tr}(A_tF_tB_t)
-r_t\operatorname{Tr}(F_tB_t)
\right)dt\\
&\quad+\mathbb E\int_0^H
\operatorname{Tr}(A_t^2\chi'(A_t)B_t)dt\\
&\quad-\frac12\mathbb E\int_0^H\sum_k
\operatorname{Tr}\!\left(
D^2\chi(A_t)[\Theta_{t,k},\Theta_{t,k}]B_t
\right)dt\\
&\quad-\mathbb E\int_0^H\sum_k
\operatorname{Tr}\!\left(
D\chi(A_t)[\Theta_{t,k}]\mathcal N_{t,k}
\right)dt.
\end{aligned}
\tag{6.1}
$$

This identity is tensor-stable under independent spectators, but its first deterministic term
already reaches the full scalar damping. If $Ae=\lambda e$, $B=ree^T$, $\lambda\ge4$, and
$0<r\le\lambda$, then $Fe=e$, $\chi'(\lambda)=0$, and

$$
2\operatorname{Tr}(AFB)-r\operatorname{Tr}(FB)
=(2\lambda-r)r
=2\operatorname{Tr}(AB)-r^2
=D.
\tag{6.2}
$$

Hence the immediate comparison has coefficient exactly one, not a strict fraction. This is the
first irreducible term after the necessary spectator cancellation. The terminal increment
$Z_H\ge0$ also has the wrong sign. A successful replacement needs a new signed cancellation
from the last two cut-dependent terms, a different cut-relative potential, or additional
trajectory structure. Merely applying the directional third-moment bound does not provide such
a sign.

For reference, the exact $D\chi$ cut term is

$$
\begin{aligned}
\sum_k\operatorname{Tr}
\left(D\chi(A)[\Theta_k]\mathcal N_k\right)
&=2s\sum_k\delta^TD\chi(A)[\Theta_k]Ke_k\\
&\quad-\alpha s\sum_k\delta_k
\delta^TD\chi(A)[\Theta_k]\delta.
\end{aligned}
\tag{6.3}
$$

Letwin's available estimate controls one whitened directional third-moment contraction. The
complete sums in (6.3), with the divided-difference multiplier $D\chi(A)$ between two tensor
indices, require a new orientation-sensitive contraction theorem. A global Hilbert--Schmidt
Cauchy--Schwarz estimate either restores a trace factor or spends covariance factors that are
already saturated in (6.2). The $D^2\chi$ term has the analogous complete Brownian-coordinate
sum. Thus the current third-moment literature does not repair the strict damping after the
spectator subtraction.

## Exact residue

- **Refuted gate formulation.** The universal raw estimate (G2) is false for every legitimate
  nondecreasing fixed cutoff. Independent exponential spectators make its left side grow
  linearly in dimension while leaving $S,r,D$ unchanged.
- **Technical gap.** The refutation is complete at proof-sketch level but has not gone through a
  standalone `prover` dossier and distinct cold review. It warrants no ledger status change yet.
- **Needs new idea.** Replace (G2) by a cut-relative or net-injection statement in which blocks
  with $B=G=0$ cancel identically, while retaining a strict scalar damping surplus.
- **Fenced.** The obvious invariant subtraction $\Psi_\chi(A)$ gives (6.1), and the deterministic
  $B$ drift saturates $D$ exactly in (6.2). Bounding it term by term cannot yield the required
  coefficient below one.
- **Needs new idea.** Control the signed combination of the last two terms of (6.1) with the
  saturated deterministic drift and terminal $Z_H$; a norm bound that discards the sign is not
  enough.
- **Technical/epistemic gap.** Even after a corrected high-block estimate, the present low-block
  implication uses the unreviewed preprint input (2.6).

## Fence-by-fence audit

### `rem:two-tail-slice-bounds`

No slice-wise absolute-scale source bound is asserted. The present product has zero spectator
source and detects instead that the proposed auxiliary potential charges covariance motion in
directions irrelevant to the cut. It neither contradicts nor bypasses the two-tail lower bound.
A corrected gate must both ignore spectators and still dominate the aligned two-tail source.

### `rem:projection-ceiling`

The refutation is an exact block-diagonal scalar It\^o calculation, not a projection-test
estimate. The conditional implication audit uses the full matrix input (2.6) and explicitly
retains its preprint status; it does not infer QCTS from radial or one-dimensional tests.

### `rem:relative-ceiling`

No universal bound on $\Xi_T$ or on relative covariance occupation is inserted. The witnesses
are products with dimension-free KLS. Their growing raw injection therefore refutes only an
overstrong auxiliary estimate, not KLS and not the tight-prefix source conclusion.

### Other catalogued fences

No crude covariance bootstrap is used (`rem:crude-insufficient`), no localized isoperimetric
profile is inserted (`rem:profile-circularity`), and no conclusion about a product incident-high gate is
drawn from a one-coordinate cut (`rem:single-coordinate-cuts`). The one-coordinate cylinder is used
only to separate the auxiliary injection from the actual source.

## Route verdict and proposed gate update

`conj:trace-upgrade` remains viable and open, but the staged raw-contraction gate should be withdrawn. Its
failure is structural: it charges independent covariance spectators that cancel only when the
terminal and favorable drift terms are retained. The next gate must be tensor-stable under
direct sums before any occupation estimate is attempted.

Proposed one-line replacement for the orchestrator:

> The raw prefix projector-motion estimate is refuted by Gaussian-halfspace cylinders with
> arbitrarily many exponential spectators: blocks with $B=G=0$ contribute positive
> $\operatorname{Tr}(A\chi(A))$ injection while the cut source is zero. Formulate a
> spectator-cancelling cut-relative or net-injection estimate and prove a strict damping surplus;
> the obvious subtraction of $\operatorname{Tr}(A\chi(A))$ leaves the deterministic term
> $2\operatorname{Tr}(A\chi(A)B)-r\operatorname{Tr}(\chi(A)B)$, which can equal the full $D$.

The gate text should also state $0\le\chi\le1$ and $\chi'\ge0$, since those hypotheses are
required for the advertised prefix implication.

## Proof-ready candidate statement

The following is exact enough for a standalone dossier.

> **Proposition (spectator obstruction to the raw soft-projector injection).** Fix any
> $C^2$ nondecreasing $\chi:\mathbb R\to[0,1]$ with $\chi=0$ on $(-\infty,3]$ and
> $\chi=1$ on $[4,\infty)$. For every $C_\chi,C_r\ge0$, every $\gamma\in\mathbb R$, every
> $T_0>0$, and every $\eta\in(0,1/2)$, there are an integer $N$, an isotropic log-concave
> product $\mu_N$ and a fixed balanced cylinder $E$ such that, for some $0<T\le T_0$, the
> quantity (G1) satisfies
> $$
> \mathfrak J_\chi^0(T)>
> C_\chi T+C_r\mathbb E\int_0^{T\wedge\tau_\eta}r_tdt
> +\gamma\mathbb E\int_0^{T\wedge\tau_\eta}D_tdt.
> $$
> One may take $\mu_N=\gamma_1\otimes\xi^{\otimes N}$ and
> $E=\{x_0\ge0\}\times\mathbb R^N$. The same witnesses have no spectator contribution to
> $S,r,$ or $D$ and therefore do not refute `ass:tight-prefix-carleson` or KLS.

Suggested candidate node, if the orchestrator wants the failed gate recorded formally:

```yaml
- id: prop:soft-projector-spectator-obstruction
  kind: proposition
  status: open
  route: eldan-localization
  statement: "Every legitimate fixed soft cutoff has a Gaussian-base/exponential-spectator product-cylinder family for which the raw prefix D2chi/Dchi injection grows linearly in the spectator dimension while S, r, and D remain base-local; hence the raw injection bound staged for conj:trace-upgrade is not tensor-stable."
  depends_on: [lem:matrix-riccati, prop:covariance-spike]
```

No `proved`, `refuted`, `solution`, `review`, `checked_by`, or cross-route edge is proposed.

## Numerical disposition

No `finum` run is requested. The witness and threshold are analytic, and a finite sampled path
would certify nothing. The exact product factorization and the published fixed-time spike event
already discriminate the gate.

```yaml
outcome: complete
artifacts:
  - research/explorations/2026-08-27-kls-route-prober-tight-prefix-soft-projector-w3p01.md
proposed_deltas:
  - stage prop:soft-projector-spectator-obstruction as an open candidate only if the orchestrator wants formal provenance for the failed auxiliary gate
  - replace the raw conj:trace-upgrade injection gate by the spectator-cancelling requirement quoted above; retain conj:trace-upgrade and ass:tight-prefix-carleson as open
  - add 0 <= chi <= 1 and chi' >= 0 to any retained soft-projector implication statement
next_role: prover
next_prompt: |
  Write one standalone dossier for the candidate `prop:soft-projector-spectator-obstruction`.
  Reconstruct the prefix soft-projector identity independently. Use the isotropic product
  gamma_1 tensor xi^N with the Gaussian halfspace cylinder, prove block factorization and the
  exact one-spectator identity (5.7), invoke the published dimension-one covariance-spike event
  with s=1/T, and condition on the independent Gaussian-base stopping time to obtain (5.13).
  Bound r <= 1 and D <= 2, choose N after T, and negate every proposed raw-injection constant.
  State explicitly that the construction refutes only the auxiliary raw D2chi/Dchi estimate,
  not ass:tight-prefix-carleson, conj:trace-upgrade, or KLS. Do not analyze or claim any relation to
  conj:stein-weighted or conj:product-alignment. Compile the dossier and hand it to a distinct cold
  proof-checker; do not edit the ledger, manuscript, route-control files, or this exploration.
```
