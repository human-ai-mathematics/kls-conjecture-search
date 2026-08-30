# KLS route probe: the anisotropic bootstrap $(\mathrm{AB})_{\rho,\beta}$ and the spectral resolution of $\mathsf N,\mathsf D,\mathsf R$

Date: 2026-08-30

Role: `kls-route-prober`

Run id: `w4c01`

Concurrency key: `kls-gate:ass:cmh-recovery-envelope`

Target: the anisotropic source-retention inequality $(\mathrm{AB})_{\rho,\beta}$ inside the
proof-ready linear subgate of `ass:cmh-recovery-envelope`.

This probe continues `research/explorations/2026-08-27-kls-route-prober-cmh-linear-recovery-w3c01.md`
(cited below as **w3c01**). It works on one fixed regular isotropic compact-target moment map;
recovery-sequence quantifiers are exactly as in w3c01 and are not re-litigated. No numerics are
used. No node of the trace-upgrade cluster (`q:upgrade`, high-rank `q:stein-weighted`,
`q:alignment`) is opened; one comparison observation is quarantined in a "for the synthesizer"
note.

## Gate, verbatim

From `research/kls/gating.md`, node `ass:cmh-recovery-envelope`:

> Construct, for every centered log-concave law, at least one regular compact-target moment-map
> recovery sequence with a universal bound on $\liminf C_{\mathrm{CMH}}$. The unconditional affine
> Poincar\'e lower-semicontinuity lemma and the regular CMH endpoint then pass the bound to the
> limit. This is the preferred approximation gate; it does not demand control of every
> regularization choice. The current proof-ready linear subgate is anisotropic source retention:
> in isotropic source coordinates the exact matrices
> $\mathsf N=\int H^2$, $\mathsf D=\int H^{ab}(\partial_aH)(\partial_bH)$, and
> $\mathsf R=\tfrac12\int\{H,A+Q\}$ satisfy the candidate identities
> $\mathsf N=\mathsf D+\mathsf R$ and $\mathsf N-I\preceq\mathsf D$; a universal estimate
> $\mathsf R\succeq\rho\mathsf N-\beta I$ would give
> $Q_{\rm lin}\le(1+\beta)/\rho$. This reduction is parked pending proof certification. The
> scalar cyclic-square argument has no pointwise Loewner promotion, so any proof needs an
> integrated corrector or nonlocal coercivity, not matrix polarization alone.

## Standing objects and term-by-term decomposition

Fix one regular isotropic compact-target moment map: $\psi$ smooth strictly convex on
$\mathbb R^n$, source probability $\eta=e^{-\psi}\,dy$, target
$\nu=(\nabla\psi)_\#\eta$ with density $\propto e^{-V}$ on a compact convex body, centered and
isotropic ($\Sigma=I$, $\int H\,d\eta=I$ where $H=D^2\psi$). The Monge–Ampère equation is
$\log\det D^2\psi=V(\nabla\psi)-\psi+\mathrm{const}$. All integrations by parts use the
compact-target cutoff conventions certified in `thm:regular-moment-map-compact-target` and
reused in w3c01; on this class $H$ is bounded ($0\preceq H\preceq2R(K)^2I$, Klartag import), and
$u_b:=\partial_b\psi=b\cdot\nabla\psi$ is bounded with bounded gradient $Hb$.

Every term of the demanded object, and its current status:

- **The diffusion.** $\mathcal Lf=H^{ij}f_{ij}-(V_i\circ\nabla\psi)f_i$ with
  $(H^{ij})=H^{-1}$; certified as the source pullback of the Stein generator $L_\mu$ of
  `modules/kls/41-cmh-normalization.tex` (the dossier `solutions/thm-cmh-normalization.tex`
  fixes $L_\mu$; the pullback identity is re-derived below and is elementary). Its symmetric
  form is derived in this probe: $\mathcal Lf=e^{\psi}\partial_i\bigl(e^{-\psi}H^{ij}\partial_jf\bigr)$,
  Dirichlet form $\mathcal E(f)=\int H^{ij}f_if_j\,d\eta$, nonnegative operator
  $\mathsf A=-\mathcal L$.
- **The sources.** $A=H(D^2V\circ\nabla\psi)H\succeq0$ and
  $Q_{ij}=\operatorname{Tr}(H^{-1}\partial_iH\,H^{-1}\partial_jH)\succeq0$ (source derivatives),
  entering through the differentiated Monge–Ampère equation $\mathcal LH+H=A+Q$
  (w3c01 eq. (7); re-derived below as a consistency check).
- **The matrices.** $\mathsf N=\int H^2\,d\eta$, $\mathsf D=\int H^{ab}(\partial_aH)(\partial_bH)\,d\eta\succeq0$,
  $\mathsf R=\tfrac12\int\{H,A+Q\}\,d\eta$. Certified in probe (w3c01, ready for a prover):
  $\mathsf N=\mathsf D+\mathsf R$ (identity (9)) and $\mathsf N-I\preceq\mathsf D$
  (Brascamp–Lieb componentwise, inequality (10)). Not controlled anywhere: any
  $(\mathrm{AB})_{\rho,\beta}$: $\mathsf R\succeq\rho\mathsf N-\beta I$ with universal
  $\rho>0$, $\beta<\infty$.
- **The trace case.** $\operatorname{Tr}(HQ)\ge\operatorname{Tr}D_{\rm point}$ pointwise by the
  cyclic square, $\operatorname{Tr}(HA)\ge0$; hence
  $\operatorname{Tr}\mathsf R\ge\operatorname{Tr}\mathsf D=\operatorname{Tr}\mathsf N-\operatorname{Tr}\mathsf R$,
  the Chen–Klartag mechanism ($\rho=1/2$, $\beta=0$ at trace level), giving
  $\operatorname{Tr}\mathsf N\le2n$ self-containedly from (9)+(10)+cyclic.
- **Boundary/error terms.** All identities below are first proved on the smooth cutoff core;
  every discarded boundary term vanishes by the compact-target flux convention. No term is
  dropped by sign.
- **The fence inherited from w3c01.** The pointwise Loewner promotion of the cyclic square is
  refuted by the 2D jet (w3c01 eq. (13)); a proof must be integrated/nonlocal.

## What is established (prover-formalizable)

### P0. Symmetric form of the Stein diffusion in source coordinates

Since $\partial_iH^{ij}=-H^{ia}\psi_{iab}H^{bj}=-\operatorname{Tr}(H^{-1}\partial_bH)\,H^{bj}$ and the
once-differentiated Monge–Ampère equation reads

$$
 H^{ij}\psi_{ijk}=(V_i\circ\nabla\psi)H_{ik}-\psi_k,
 \tag{MA1}
$$

one computes
$e^{\psi}\partial_i(e^{-\psi}H^{ij}\partial_jf)
 =H^{ij}f_{ij}+(\partial_iH^{ij})f_j-\psi_iH^{ij}f_j
 =H^{ij}f_{ij}-(V_j\circ\nabla\psi)f_j=\mathcal Lf$.
So $\mathcal L$ is symmetric on $L^2(\eta)$ with carré du champ $H^{ij}f_if_j$, and it is the
pullback of the target Stein generator: for $f=g\circ\nabla\psi$ one has
$\nabla_yf=H\,(\nabla_xg\circ\nabla\psi)$, hence the CMH numerator field $H\nabla_xg$ is the
plain Euclidean source gradient $\nabla_yf$, and

$$
 \text{CMH reads: }\int|\nabla_yf|^2\,d\eta\le C\int(\mathcal Lf)^2\,d\eta .
$$

Differentiating (MA1) once more reproduces exactly $\mathcal LH+H=A+Q$; integrating it gives the
normalization

$$
 \int(A+Q)\,d\eta=\int H\,d\eta=I.
 \tag{P0.1}
$$

### P1. The columns of $H$ solve an exact eigen-equation

Set $u_a=\partial_a\psi$ (so $u_a=a\cdot x$ in target coordinates) and
$w^{(a)}=Ha=\nabla u_a$ (componentwise $w_i=H_{ai}$). Then:

1. **Eigenfunctions.** (MA1) is precisely $\mathcal Lu_a=-u_a$: each $u_a$ is an eigenfunction
   of $\mathsf A$ with eigenvalue $1$. (Target-side this is the certified linear-test identity
   $L_\mu(a\cdot x)=-a\cdot x$.) Moreover $\int u_a\,d\eta=0$ exactly, and, by one integration
   by parts and isotropy,
   $\langle u_b,u_c\rangle_{L^2(\eta)}=\int\psi_{bc}\,d\eta=\delta_{bc}$: the $u_b$ are an
   orthonormal system of centered eigenfunctions.
2. **Column equation.** The row $a$ of $\mathcal LH+H=A+Q$ says, componentwise,

   $$
    (1-\mathsf A)\,w_i=F_i,
    \qquad F:=(A+Q)a,\ F_i=(A+Q)_{ai}.
    \tag{P1.1}
   $$

3. **Compatibility.** $\langle F_i,u_b\rangle
   =\langle(1-\mathsf A)w_i,u_b\rangle=\langle w_i,(1-\mathsf A)u_b\rangle=0$: the source
   columns $(A+Q)a$ are $L^2(\eta)$-orthogonal to every $u_b$. Also $\int F_i\,d\eta=\delta_{ai}$
   by (P0.1).

### P2. Spectral gap one (Brascamp–Lieb)

For the log-concave $\eta=e^{-\psi}$, Brascamp–Lieb gives
$\operatorname{Var}_\eta(f)\le\int\langle H^{-1}\nabla f,\nabla f\rangle\,d\eta=\mathcal E(f)$.
Hence $\mathsf A\ge1$ on $\mathbb 1^\perp$: the Stein operator has spectral gap exactly $1$
(attained by the $u_b$). Set

$$
 U:=\operatorname{span}\{u_1,\dots,u_n\},\qquad
 V:=(\mathbb R\mathbb 1\oplus U)^\perp .
$$

$\mathsf A$ is self-adjoint and preserves $\mathbb R\mathbb 1$ and $U$, hence $V$; and
$\mathsf A-1\ge0$ on $V$. (If the eigenspace at $1$ is strictly larger than $U$, nothing below
changes: no inverse is taken.)

### P3. Spectral resolution of the bootstrap matrices (main structural result)

Decompose each column component along $\mathbb 1\oplus U\oplus V$:

$$
 H_{ai}=\delta_{ai}\cdot\mathbb 1+\sum_bM_{aib}\,u_b+v_i,
 \qquad
 M_{aib}:=\langle H_{ai},u_b\rangle=\int\psi_{aib}\,d\eta=\int\partial_bH_{ai}\,d\eta,
$$

with $M$ **totally symmetric** and $v_i=v_i^{(a)}\in V$. Then, for every unit $a$:

$$
 \boxed{
 \begin{aligned}
  a^T\mathsf Na&=1+\|M_a\|_{\rm HS}^2+\|v^{(a)}\|^2,\\
  a^T\mathsf Da&=\|M_a\|_{\rm HS}^2+\sum_i\langle v_i,\mathsf Av_i\rangle,\\
  a^T\mathsf Ra&=1-T_a,\qquad
  T_a:=\sum_i\langle v_i,(\mathsf A-1)v_i\rangle\ \ge0,
 \end{aligned}}
 \tag{P3.1}
$$

where $\|M_a\|_{\rm HS}^2=\sum_{i,b}M_{aib}^2$ and $\|v^{(a)}\|^2=\sum_i\|v_i\|_{L^2(\eta)}^2$.

*Proof sketch (complete for a prover).* First line: Pythagoras with orthonormal $u_b$ and
$\int H_{ai}\,d\eta=\delta_{ai}$. Second line: $a^T\mathsf Da=\sum_i\mathcal E(H_{ai})$ by
definition of $\mathsf D$ ($\mathcal E(H_{ai})=\int H^{bc}\partial_bH_{ai}\partial_cH_{ai}\,d\eta$,
summed over $i$); expand spectrally, with cross terms killed by invariance of $U,V$ and the
eigenvalue $1$ on $U$. Third line: subtract, using $\mathsf N=\mathsf D+\mathsf R$. Alternatively
directly: $a^T\mathsf Ra=\int\langle Ha,(A+Q)a\rangle\,d\eta$ (transpose symmetry under the
integral), then expand $Ha$ and use (P1.1) plus the P1.3 orthogonality:
$(\mathsf A-1)v_i=\delta_{ai}\mathbb 1-F_i$ and
$a^T\mathsf Ra=1+0-\sum_i\langle v_i,F_i\rangle=1-T_a$. $\square$

Immediate corollaries, each new or newly transparent:

- **(C1) $\mathsf R\preceq I$ always**, with $a^T\mathsf Ra=1$ iff the fluctuation
  $Ha-a-\sum_bM_{aib}u_b$ has all its spectral mass at level exactly $1$ (i.e. $T_a=0$). This
  recovers (10) and adds the rigidity statement. In particular the *only* way
  $(\mathrm{AB})_{\rho,\beta}$ can fail on a family with bounded $\mathsf N$ is
  $T_a>1+\beta-\rho\,a^T\mathsf Na$: high spectral mass of the columns above the
  Brascamp–Lieb gap.
- **(C2) Exact equivalence.** $(\mathrm{AB})_{\rho,\beta}$ holds at the map iff for every
  unit $a$

  $$
   T_a+\rho\bigl(\|M_a\|_{\rm HS}^2+\|v^{(a)}\|^2\bigr)\le1+\beta-\rho .
   \tag{P3.2}
  $$

  Since both summands are nonnegative, $(\mathrm{AB})_{\rho,\beta}$ is exactly the conjunction
  of the gate-type bound $\lambda_{\max}(\mathsf N)\le(1+\beta)/\rho$ **and** the high-mode
  excess bound $T_a\le1+\beta-\rho\,a^T\mathsf Na$. Neither implies the other. The gate's
  phrase "a universal estimate $\mathsf R\succeq\rho\mathsf N-\beta I$ would give
  $Q_{\rm lin}\le(1+\beta)/\rho$" is correct, but $(\mathrm{AB})$ is not a smaller target than
  its conclusion: it is the conclusion plus spectral-alignment control. Any proof strategy for
  $(\mathrm{AB})$ must therefore already contain a proof mechanism for bounded
  $\lambda_{\max}(\mathsf N)$.
- **(C3) Sharp candidate in spectral form.** $\mathsf R\succeq\mathsf D$ (w3c01 eq. (12)) is
  equivalent to
  $\|M_a\|_{\rm HS}^2+\sum_i\langle v_i,(2\mathsf A-1)v_i\rangle\le1$ for all unit $a$. Since
  $\mathsf A\ge1$ on $V$, it implies both
  $\|M_a\|_{\rm HS}^2\le1$, i.e.

  $$
   \sum_b\Theta_b^2\preceq I,\qquad \Theta_b:=\int\partial_bH\,d\eta=\mathbb E_\nu[x_bH],
   \tag{P3.3}
  $$

  and $\|v^{(a)}\|^2\le1$; total: $\lambda_{\max}(\mathsf N)\le2$, consistent with the gate's
  sharp constant.
- **(C4) Directional sufficiency.** In the derivation of $Q_{\rm lin}\le(1+\beta)/\rho$ only
  the top eigendirection $a_*$ of $\mathsf N$ is used: it suffices that (P3.2) hold at
  $a_*$ for each map of the chosen recovery sequence.
- **(C5) De-averaging reading.** Summing (P3.1) over an orthonormal basis $a=e_1,\dots,e_n$
  shows that the Chen–Klartag trace inequality is exactly the *averaged* form of (P3.2) with
  $(\rho,\beta)=(1/2,0)$:
  $\sum_aT_{e_a}+\tfrac12\sum_a(\|M_{e_a}\|^2+\|v^{(e_a)}\|^2)\le\tfrac n2$. The open content of
  $(\mathrm{AB})$ is the direction-wise de-averaging of this budget.

### P4. The pointwise deficit kernel, unifying the trace proof and the jet

At a point where $H$ has eigenframe $\{e_k\}$ and eigenvalues $\lambda_k$, write
$T_{ijk}=\psi_{ijk}$ (totally symmetric). Then

$$
 \Bigl(\tfrac12\{H,Q\}-D_{\rm point}\Bigr)_{k\ell}
 =\sum_{i,j}T_{ijk}T_{ij\ell}\,
  \frac{\lambda_k+\lambda_\ell-\lambda_i-\lambda_j}{2\lambda_i\lambda_j}.
 \tag{P4.1}
$$

*Checks.* Using symmetry, $D_{{\rm point},k\ell}=\sum_{ij}T_{ijk}T_{ij\ell}\tfrac{\lambda_i+\lambda_j}{2\lambda_i\lambda_j}$
and $(\tfrac12\{H,Q\})_{k\ell}=\tfrac{\lambda_k+\lambda_\ell}2\sum_{ij}\tfrac{T_{ijk}T_{ij\ell}}{\lambda_i\lambda_j}$.
The trace of (P4.1), after cyclic symmetrization, is
$\tfrac12\sum_{ijk}\tfrac{T_{ijk}^2}{\lambda_i}\tfrac{(\lambda_j-\lambda_k)^2}{\lambda_j\lambda_k}\ge0$
— the Chen–Klartag cyclic square. The w3c01 jet ($n=2$, $\lambda_1=\lambda<\mu=\lambda_2$,
$T_{112}=t$) gives $(1,1)$-entry $t^2(1/\mu-1/\lambda)<0$ — reproduced exactly.

So the demanded "contraction inequality on the symmetric 3-tensor" of attack direction 1 is,
in its sharp $\beta=0$, $A$-discarded form: **for the tensor field $T=D^3\psi$ of a moment map,**

$$
 \int\sum_{ij}T_{ijk}T_{ij\ell}c_kc_\ell\,
 \frac{\lambda_k+\lambda_\ell-\lambda_i-\lambda_j}{2\lambda_i\lambda_j}\,d\eta
 \;\ge\;-\frac12\int c^T\{H,A\}c\,d\eta
 \qquad\text{for all unit }c.
 \tag{P4.2}
$$

The kernel is antisymmetric under exchanging the output pair $(k,\ell)$ with the input pair
$(i,j)$ up to the $\lambda_i\lambda_j$ denominator; pointwise positivity fails exactly when the
tensor mass sits on triples whose output eigenvalues are smaller than the input ones ("energy
flowing down the spectrum of $H$"). No pointwise algebraic inequality on symmetric 3-tensors can
give (P4.2) — the jet *is* a symmetric 3-tensor — so the integral must exploit that $T=DH$ is a
derivative field coupled to the eigenvalue field of $H$. This makes precise the gate's
"integrated corrector or nonlocal coercivity" clause.

### P5. The $f(H)$-corrector hierarchy, and its calibration

For any smooth matrix function $f$ with the needed integrability,
$\int\mathcal Lf(H)\,d\eta=0$ gives the exact identity

$$
 \int Df(H)[A+Q]\,d\eta
 =\int Df(H)[H]\,d\eta-\int H^{ab}\,D^2f(H)[\partial_aH,\partial_bH]\,d\eta .
 \tag{P5.1}
$$

- $f(H)=H^2$ is exactly $\mathsf N=\mathsf D+\mathsf R$ (identity (9)).
- $f(H)=-H^{-1}$ collapses ($D^2$-term $=2H^{-1}QH^{-1}$-form after the frame computation) to
  the clean identity, **conditional on integrability of $H^{-1}$-moments**,

  $$
   \int(D^2V\circ\nabla\psi)\,d\eta
   =\int H^{-1}\,d\eta+\int H^{-1}QH^{-1}\,d\eta
   \succeq\int H^{-1}\,d\eta .
   \tag{P5.2}
  $$

  Calibration/caveat: for the 1D one-sided-exponential boundary law both sides are $+\infty$
  ($\mathbb E[1/Y]=\infty$), so (P5.2) is a statement of the regular interior of the class, not
  of its boundary. It is recorded because it demonstrates that the hierarchy (P5.1) *can*
  produce coercive matrix inequalities — just in the wrong Loewner corner ($H^{-1}$, not
  $H^2$).
- **Why the hierarchy alone cannot deliver $(\mathrm{AB})$.** In frame, every identity (P5.1)
  has second-order term $\sum_{a,m}\tfrac{T_{akm}T_{am\ell}}{\lambda_a}f^{[2]}(\lambda_k,\lambda_m,\lambda_\ell)$
  and first-order term $f^{[1]}(\lambda_k,\lambda_\ell)(A+Q-H)_{k\ell}$: all weights are divided
  differences, i.e. functions of eigenvalue tuples only. The obstruction (P4.1) is an
  eigenvalue-*ordering/alignment* failure at fixed tuple profile: at the jet, the negative
  direction and a compensating positive direction have the same eigenvalue data and differ only
  by which slot of $T$ carries the output. A single $f$-identity cannot separate them. This is
  an assessment with a precise formal core (the divided-difference form of (P5.1)), not a
  proved impossibility theorem for arbitrary combinations of (P5.1) across different $f$; the
  impossibility question is stated in the residue.

### P6. Unconditional dimension-dependent $(\mathrm{AB})$: $\mathsf R\succeq\mathsf N-nI$

From $\mathsf D\succeq0$ and the trace bootstrap
$\operatorname{Tr}\mathsf D\le\tfrac12\operatorname{Tr}\mathsf N\le n$:

$$
 \mathsf R=\mathsf N-\mathsf D
 \succeq\mathsf N-\operatorname{Tr}(\mathsf D)\,I
 \succeq\mathsf N-n\,I .
 \tag{P6.1}
$$

So $(\mathrm{AB})_{1,n}$ holds for every regular isotropic compact-target map, and the
bootstrap of w3c01 then gives $Q_{\rm lin}=\lambda_{\max}(\mathsf N)\le n+1$ (marginally better
than the trace bound $2n$; also directly: $\mathsf N\preceq(1+\operatorname{Tr}\mathsf D)I$).
Consequence for scope: **the entire content of the gate is the dimension-freeness of
$(\rho,\beta)$**; and any refuting family must, for each fixed $(\rho,\beta)$, produce
directions with $T_a+\rho\,a^T\mathsf Na>1+\beta$ while (P6.1) caps the possible growth at
linear in $n$.

### P7. The sharp candidate holds on all regular products of one-dimensional laws

For a product potential $\psi(y)=\sum_k\psi_k(y_k)$ of regular isotropic 1D factors, $H$, $Q$,
$A$, and hence $\mathsf N,\mathsf D,\mathsf R$ are diagonal, and per factor
$HQ=D_{\rm point}$ *pointwise* (one dimension), so

$$
 \mathsf R-\mathsf D=\operatorname{diag}_k\int V_k''(\psi_k')\,(\psi_k'')^3\,e^{-\psi_k}\,dy_k
 \succeq0 .
 \tag{P7.1}
$$

Thus $\mathsf R\succeq\mathsf D$, equivalently $\mathsf R\succeq\mathsf N/2$, holds with the
sharp constants on every finite product of regular 1D laws (and, by the certified recovery
calculus, on their invertible images). Any counterexample to $(\mathrm{AB})$ or to the sharp
candidate is therefore necessarily non-product with persistent eigenframe rotation, dimension
$\ge2$.

### Calibrations (exact, boundary laws used only as limits)

| law | $\mathsf N$ | $\mathsf D$ | $\mathsf R$ | $T_a$ | $\|M_a\|^2$ |
|---|---|---|---|---|---|
| Gaussian | $1$ | $0$ | $1$ | $0$ | $0$ |
| one-sided exponential (1D, boundary) | $2$ | $1$ | $1$ | $0$ | $1$ |
| symmetric Laplace (1D, boundary) | $5/4$ | $1/2$ | $3/4$ | $1/4$ | $0$ |
| product of exponentials (boundary) | $2I$ | $I$ | $I$ | $0$ | $1$ (all $a$) |

Notes. (i) The exponential saturates *both* $\mathsf R\preceq I$ and
$\mathsf R\succeq\mathsf D$ with **zero high-mode excess**: its column fluctuation
$H-1=Y-1=u$ lies entirely in the eigenvalue-1 eigenspace. The extremal configuration of the
whole linear gate is spectrally pure at the Brascamp–Lieb gap. (ii) For the Laplace, the
distributional curvature $V''=2\sqrt2\,\delta_0$ carries exactly the mass
$\int V''H^3\,d\nu=1/4$ that reconciles $\mathsf R=3/4$ with $\mathsf D=1/2$; smooth regular
approximants spread this atom. This is a concrete warning for any computation that discards
$A$ where $V$ is only piecewise smooth. (iii) $T_a>0$ generically: the excess channel is real,
not vacuous.

## The residue

Every remaining step toward $(\mathrm{AB})_{\rho,\beta}$ with universal constants, labelled:

1. **Needs new idea — the excess bound.** Prove $T_a\le1+\beta-\rho\,a^T\mathsf Na$ (equivalently
   $a^T\mathsf Ra\ge\rho\,a^T\mathsf Na-\beta$) for some universal $(\rho,\beta)$. By C2 this is
   the genuinely new half of $(\mathrm{AB})$ beyond the gate-type bound, and by C1 it is a
   spectral-localization statement: the columns of $H$ may not carry order-one $L^2$ mass at
   spectral levels of $\mathsf A$ bounded away from the Brascamp–Lieb gap, beyond the stated
   budget. No mechanism in the repository produces it; there is no uniform gap above $1$
   (product-exponential spectrum has one, but limits can fill it).
2. **Needs new idea — the third-moment ($U$-channel) bound.** Prove
   $\sum_b\Theta_b^2\preceq c\,I$ with universal $c$ for $\Theta_b=\int\partial_bH\,d\eta$
   (P3.3). This is *implied by* gate zero with constant $1+c$ and is strictly more concrete: a
   single deterministic totally symmetric 3-tensor built from third moments, no operator
   inverse, no test function. Letwin/Klartag directional bounds control only the
   fully-$a$-contracted slice $\sum_bM_{aab}^2\le2$; a generic symmetric 3-tensor admits no
   dimension-free promotion from contracted to full slice norms (an explicit
   $M=\sum_k\sigma_k\,e_1\odot e_k\odot e_k$-type tensor separates them by a factor $n$), so a
   proof must use the moment-map origin of $M$. This is the cheapest well-posed sub-target this
   probe can propose.
3. **Fenced — pointwise promotion and matrix algebra.** (P4.1) shows the pointwise deficit has
   an alignment-sensitive kernel; the w3c01 jet refutes pointwise Loewner promotion, and
   `prop:letwin-not-gate-zero` refutes matrix-moment algebra alone. P3 evades both by consuming
   differential structure (the eigen-equation (P1.1) exists only because $H$ is a Hessian tied
   to the measure by Monge–Ampère), but the *closing* estimate is still missing.
4. **Needs new idea (stated precisely) — corrector completeness.** Decide whether any finite
   combination of the identities (P5.1) over matrix functions $f$, integrated against admissible
   scalar weights, can dominate the alignment deficit (P4.2). The divided-difference calibration
   in P5 suggests no; a proof of impossibility would close attack direction 1 definitively and
   force genuinely nonlocal input (e.g. spectral information as in P3).
5. **Technical gap — second variation at the extremal corner.** At products of exponentials the
   configuration is $T_a=0$, $\|M_a\|^2=1$, and both sharp inequalities are tight. The
   admissible isotropy-preserving perturbation family already prescribed for
   `q:cmh-solenoidal-perturbation` (first covariance variation vanishing) can be re-used to
   compute the second variation of $a^T(\mathsf R-\mathsf D)a$ in the linear sector. A negative
   second variation would refute the sharp candidate (12) near the corner (not $(\mathrm{AB})$
   with slack constants); a nonnegative one would be corner rigidity. The machinery exists in
   the repository; the computation was not executed here and is the sharpest bounded next
   analytic step.
6. **Not found — refutation family.** A refutation of $(\mathrm{AB})$ for *every* universal
   pair requires $T_a+\rho\,a^T\mathsf Na$ unbounded for each fixed $\rho>0$, hence either
   $\lambda_{\max}(\mathsf N)\to\infty$ (which would refute gate zero for every constant — the
   major negative outcome scoped by the orchestrator) or $T_a\to\infty$, i.e.
   $\lambda_{\min}(\mathsf R)\to-\infty$. P7 excludes products and their invertible images;
   a near-Gaussian expansion gives $\mathsf R=I+O(\varepsilon)$, excluding perturbative
   witnesses (sketch level); (P6.1) caps growth at $O(n)$. No candidate family was found; the
   hunt should target non-product laws adjacent to the exponential corner with strong
   eigenframe rotation.

## Fence-by-fence evasion check

`ass:cmh-recovery-envelope` carries no ledger `bounded_by` edge; the full registry and the
route guardrails were checked.

- `obs:two-tail`: no localization cut, slice bound, or covariance weight appears; all
  statements are stationary identities at one fixed map.
- `obs:proj-ceiling`: the live quantities are full column energies $|Ha|^2$ and full slice
  norms $\|M_a\|_{\rm HS}$; scalar/projection bounds are used only where attributed (Letwin on
  $\sum_bM_{aab}^2$) and are explicitly flagged as insufficient for the full slice.
- `obs:crude-insufficient`: no stochastic covariance integral or bootstrap occurs.
- `obs:relative-ceiling`: no all-measure relative bound is inserted; (P6.1) is
  dimension-dependent and is presented as such.
- `obs:circularity`: no localized isoperimetric profile or evolving competitor family occurs;
  Brascamp–Lieb is a certified external input, not an assumed profile bound.
- `obs:rank-one-refuted`: products enter only through exact stationary block-diagonalization
  (P7), never through a product-cut occupation claim.
- CMH-specific guardrails: no pointwise Loewner promotion is asserted (P4 sharpens the jet
  into a kernel formula); no matrix-moment-only argument is used for any open claim
  (`prop:letwin-not-gate-zero` respected — P1–P3 consume the differentiated Monge–Ampère
  structure); no canonical kernel is transported through a noninvertible map; no continuity or
  semicontinuity of $Q_{\rm lin}$ or $C_{\rm CMH}$ is asserted; boundary laws (exponential,
  Laplace) are used only as calibration limits, never as members of the regular class.
- Trace-upgrade cluster: not opened. One comparison observation is quarantined below for the
  synthesizer; no equivalence or transfer is asserted or used.

## For the synthesizer (quarantined observation, not a conclusion)

C5 exhibits $(\mathrm{AB})$ as a direction-wise de-averaging of a trace identity, and C1/C2
show the missing quantity is spectral mass of a canonical field above a gap — structurally
reminiscent of the high-rank occupation quantities owned by the trace-upgrade cluster. Per
`CLAUDE.md` constraint 6 and `rem:trace-upgrade-unification`, this resemblance is handed to the
cluster owner for comparison only; nothing in this probe depends on it, and no implication in
either direction is claimed.

## Diagnostics for `finum` (directional; fixed refuting thresholds; do not duplicate w4c02)

These extend, not repeat, the running w4c02 battery ($\mathsf N,\mathsf D,\mathsf R$ on
Dirichlet/1D exactly, 2D MA directionally). All outputs are directional unless exact/rational.

1. **Dirichlet sharp-candidate check (exact).** On the Dirichlet family with all
   $\alpha_i\ge1$, compute $\lambda_{\min}(\mathsf R-\mathsf D)$ in exact rational arithmetic
   from the existing exact moment matrices. Refuting threshold: an exact value $<0$ at any
   admissible parameter refutes the sharp candidate $\mathsf R\succeq\mathsf D$ on a certified
   model class (it does not refute $(\mathrm{AB})$ with slack constants, and refutes nothing
   about KLS).
2. **Spectral-channel split at the top direction (2D MA solutions).** At the computed top
   eigendirection $a_*$ of $\mathsf N$, output the quadruple
   $(a_*^T\mathsf Na_*,\,a_*^T\mathsf Da_*,\,a_*^T\mathsf Ra_*,\,\|M_{a_*}\|_{\rm HS}^2)$ and
   the derived excess $T_{a_*}=1-a_*^T\mathsf Ra_*$. Fixed thresholds:
   $a_*^T(\mathsf R-\mathsf D)a_*<0$ is a directional lead against the sharp candidate;
   $a_*^T\mathsf Ra_*<0$ (i.e. $T_{a_*}>1$) is a directional lead against every $\beta=0$ form
   and the strongest possible directional signal for the excess channel;
   $T_{a_*}+\tfrac12a_*^T\mathsf Na_*>1$ is a directional lead against
   $(\mathrm{AB})_{1/2,0}$. Any lead remains a candidate until an exact witness passes the
   proof path.
3. **Third-moment channel (cheap, exact where moments are exact).** Compute
   $\lambda_{\max}\bigl(\sum_b\Theta_b^2\bigr)$, $\Theta_b=\mathbb E_\nu[x_bH]$, on the exact
   families. Refuting threshold: an exact value $>1$ on a certified model refutes the sharp
   candidate through C3 alone, without any operator computation.

## Route viability and proposed gate update

The linear subgate remains viable and unrefuted, but its shape changes. $(\mathrm{AB})$ is not
an undifferentiated matrix inequality to be attacked by polarization: it is *exactly* the
conjunction of a gate-zero-type bound and a new, previously invisible excess bound, and the
extremal configuration is spectrally rigid (all fluctuation at the Brascamp–Lieb gap). The
unconditional $(\mathrm{AB})_{1,n}$ shows only dimension-freeness is open. The productive
sub-targets, in increasing strength: the third-moment bound (P3.3); the excess bound
$T_a\le1$ (i.e. $\mathsf R\succeq0$); the corner second variation (residue 5).

Proposed one-line gate update for the orchestrator (route-control text only):

> Linear subgate, sharpened: in the certified-in-probe spectral resolution (columns
> $Ha=a+\sum_bM_{aib}u_b+v$ with $u_b=\partial_b\psi$ orthonormal Stein eigenfunctions at the
> Brascamp–Lieb gap $1$ and $(1-\mathsf A)(Ha)=(A+Q)a$), the estimate
> $(\mathrm{AB})_{\rho,\beta}$ is equivalent to
> $T_a+\rho(\|M_a\|^2+\|v\|^2)\le1+\beta-\rho$ with
> $T_a=\sum_i\langle v_i,(\mathsf A-1)v_i\rangle$; $\mathsf R\succeq\mathsf N-nI$ holds
> unconditionally, $\mathsf R\succeq\mathsf D$ holds on all regular products of 1D laws, and
> the open content is the dimension-free excess bound plus the third-moment slice bound
> $\sum_b(\int\partial_bH\,d\eta)^2\preceq cI$; matrix polarization, pointwise Loewner
> promotion, and single-$f(H)$ corrector identities are insufficient.

## Proposed ledger delta

One candidate structural node, `status: open`, non-certifying; it refines the parked
`lem:cmh-linear-bootstrap-reduction` of w3c01 and asserts no bound on $Q_{\rm lin}$.

```yaml
- id: lem:cmh-linear-spectral-resolution
  kind: lemma
  status: open
  route: moment-map-cmh
  file: modules/kls/41-cmh-normalization.tex
  statement: "For a regular isotropic compact-target moment map with source potential psi, Stein generator A_op = -L in source coordinates, and columns Ha = grad(partial_a psi): the u_b = partial_b psi are centered orthonormal eigenfunctions of A_op at its Brascamp-Lieb spectral gap 1; the columns satisfy (1-A_op)(Ha)=(A+Q)a with (A+Q)a orthogonal to every u_b and E[A+Q]=I; and with the induced decomposition Ha = a + sum_b M_aib u_b + v one has a^T N a = 1+|M_a|^2+|v|^2, a^T D a = |M_a|^2+<v,A_op v>, a^T R a = 1 - <v,(A_op-1)v>. Consequently R <= I with equality iff the column fluctuation is spectrally pure at the gap; (AB)_{rho,beta} is equivalent to <v,(A_op-1)v> + rho(|M_a|^2+|v|^2) <= 1+beta-rho for all unit a; R >= N - nI holds unconditionally; and R >= D holds for all regular finite products of one-dimensional laws."
  depends_on: [thm:regular-moment-map-compact-target, def:cmh, prop:cmh-bochner]
```

No `proved`, `refuted`, `solution`, `checked_by`, status change to `ass:cmh-recovery-envelope`,
or cross-route edge is proposed.

```yaml
outcome: blocked
artifacts:
  - research/explorations/2026-08-30-kls-route-prober-cmh-anisotropic-bootstrap-w4c01.md
proposed_deltas:
  - "Optionally stage open lem:cmh-linear-spectral-resolution as specified above; it refines and should be coupled with the parked lem:cmh-linear-bootstrap-reduction from w3c01."
  - "Apply the proposed one-line sharpening of the ass:cmh-recovery-envelope linear subgate: (AB) = gate-type bound AND high-mode excess bound; record R >= N - nI, the product-case R >= D, and the third-moment sub-target sum_b Theta_b^2 <= cI."
  - "Forward the three finum diagnostics (exact Dirichlet lambda_min(R-D); top-direction spectral split with fixed thresholds; exact lambda_max(sum_b Theta_b^2)) to the w4c02 owner as additions, not duplicates."
next_role: prover
next_prompt: |
  Write a standalone dossier for candidate `lem:cmh-linear-spectral-resolution`, on one regular
  isotropic compact-target moment map in source coordinates, following
  research/explorations/2026-08-30-kls-route-prober-cmh-anisotropic-bootstrap-w4c01.md
  sections P0-P3, P6, P7. Prove, in order: (1) the symmetric-form identity
  L f = e^{psi} div(e^{-psi} H^{-1} grad f) via the once-differentiated Monge-Ampere equation,
  and that L is the source pullback of the certified Stein generator with
  H grad_x g = grad_y (g o grad psi); (2) that u_b = partial_b psi are centered, orthonormal
  (isotropy), bounded eigenfunctions with A_op u_b = u_b, and that Brascamp-Lieb gives
  A_op >= 1 on the orthogonal complement of constants; (3) the column equation
  (1-A_op)(Ha) = (A+Q)a from the twice-differentiated Monge-Ampere equation, the normalization
  E[A+Q] = I, and the orthogonality of (A+Q)a to every u_b; (4) the three display identities
  (P3.1) for a^T N a, a^T D a, a^T R a, being careful that U is defined as span{u_b} (not the
  full eigenspace) and that no operator inverse is taken; (5) corollaries C1-C5, including the
  equivalence of (AB)_{rho,beta} with the channel inequality (P3.2) and the rigidity
  characterization of a^T R a = 1; (6) R >= N - n I from D >= 0 and the trace bootstrap
  Tr D <= n derived self-containedly from N = D + R, N - I <= D, and the pointwise cyclic
  square; (7) R >= D for regular finite products of one-dimensional laws by
  block-diagonalization and the one-dimensional pointwise identity HQ = D_point. Audit all
  domains and cutoff integrations against the compact-target conventions of
  thm:regular-moment-map-compact-target; state explicitly that the lemma proves neither
  (AB)_{rho,beta} with universal constants, nor any bound on Q_lin beyond n+1, nor anything
  about C_CMH, KLS, or the trace-upgrade cluster. Include the calibration table (Gaussian,
  one-sided exponential, symmetric Laplace, exponential products) as remarks, labelling the
  non-smooth laws as boundary calibrations outside the regular class, and include the
  distributional-curvature warning for the Laplace. Do not include the P4 kernel or the P5
  hierarchy in the certified statement; they may appear as non-certified remarks. Do not edit
  the ledger, manuscript, routes, gating, bibliography, or reviews.
```
