---
title: "Song–Zhang v2: constructing the block radius and closing inner refinement"
ledger-node:
  - thm:sz-v2-iterated-curvature
  - lem:sz-v2-operator-block-primitives
  - lem:sz-v2-normalized-hierarchy
  - lem:sz-v2-mesoscopic-powers
numbering:
  enumerator: "137.%s"
---

**Overview.** This dossier reconstructs the operator argument of Section 6
of [@SongZhang2026ConstantKLS]. A restricted inverse operator gives a
low-energy gradient. Normalization pays for its skew linear moment. Averaging
an orbit then reduces the startup losses to cubic order in the inverse
radius. A joint dyadic frame controls all subsequent losses. The resulting
comparison iterates a static coefficient radius; the additive conversion
from that radius to $C_P$ is used only once at the end.

**Dependencies.** We use [](#lem:sz-analytic-foundations),
[](#thm:sz-polynomial-variance), [](#thm:sz-curvature-comparison), the
fixed-depth profiles of [](#thm:sz-iterated-curvature), and the three new
foundations [](#lem:sz-v2-joint-frame), [](#lem:sz-v2-skew-credit),
[](#prop:sz-v2-static-coefficient-transfer). The latter have their full proofs
in the separate foundations dossier and require independent review. No BKL
result or consequence of KLS is used.

Fix a centered regular measure of covariance $\Sigma\preceq I$ and Hessian
$D^2W\succeq aI>0$. Use the analytic operator $H$,
$B=H^{-1}$ on centered functions, $P_+f=f-\mathbb Ef$,
$D=P_+\nabla H^{-1/2}$, $Lf=\mathbb E[Xf]$, and
$\mathcal T=P_+\nabla B=DB^{1/2}$. Operators act componentwise on finite
families and append ordered derivative slots. Put $P=C_P=\lambda^{-1}$.
All inverse powers, gradients and second derivatives below are justified
by the form-domain and Bochner results in [](#lem:sz-analytic-foundations).

## Restricted operator and normalized hierarchy

:::{prf:lemma} Restricted radius and extremizer
:label: lem:sol-sz-v2-restricted
For the restricted quotient
$$R=\sup_{\mathbb E\nabla f=0}
       \frac{\operatorname{Var}f}{\mathbb E|\nabla f|^2},$$
one has
$$\mathcal T^*\mathcal T=B-L^*L,\qquad
 \|\mathcal T\|^2=R,\qquad R\le P\le R+1.$$
There is a centered unit $f\in\operatorname{Dom}H$ with
$$\mathbb E\nabla f=0,\quad \mathbb E|\nabla f|^2=R^{-1},
 \quad Bf=Rf+q\cdot X,\quad q=Lf.$$
The centered unit gradient $U=\sqrt R\nabla f$ has energy
$\lambda\le\|H^{1/2}U\|^2\le R^{-1}$.
:::

:::{prf:proof}
Write $A=LH^{1/2}$, initially on the form domain. Its adjoint is
$A^*z=H^{1/2}(z\cdot X)$ and the Dirichlet identity gives $AA^*=I$.
Thus $A$ extends boundedly and $E=I-A^*A$ is an orthogonal projection.
The mean removed from $\nabla H^{-1/2}h$ is $Ah$, so $D^*D=E$.
The substitution $h=H^{1/2}f$ turns the restricted quotient into
$\|EBE\|$. Also $B^{1/2}EB^{1/2}=B-L^*L$. Equality of the norms of
$T^*T$ and $TT^*$ for $T=B^{1/2}E$ proves the radius identities.
In the splitting $\operatorname{ran}A^*\oplus\operatorname{ran}E$, the
first diagonal block of $B$ is $ABA^*=\Sigma\preceq I$ and the second
is at most $RI$. Positivity controls the mixed term, hence
$$\langle(x,y),B(x,y)\rangle
 \le(\|x\|+\sqrt R\|y\|)^2
 \le(1+R)(\|x\|^2+\|y\|^2).$$
This proves $P\le R+1$; the reverse $R\le P$ is immediate.
The compact positive operator $B-L^*L$ has a positive top eigenvalue:
$E$ has nonzero range since it removes only finitely many directions from
an infinite-dimensional centered space. Its unit top eigenvector satisfies
$Bf=Rf+(Lf)\cdot X$. Both terms other than $Rf$ are in
$\operatorname{Dom}H$, so $f$ is too. Taking gradient means gives
$Lf=R\mathbb E\nabla f+Lf$, and pairing its $H$-image with $f$ gives
$1=R\mathbb E|\nabla f|^2$.
For $h=Bf$, Bochner yields
$$1=R^2\mathbb E\|D^2f\|^2+
 \mathbb E[(R\nabla f+q)^TD^2W(R\nabla f+q)].$$
Dropping the last nonnegative term gives the upper energy bound for $U$;
the gap gives the lower bound.
:::

:::{prf:lemma} Normalized hierarchy and delayed energy
:label: lem:sol-sz-v2-hierarchy
Start with any centered unit form-domain family $F_0$ of energy $\nu$.
Set $u^j=DF_j$. If $u^j\ne0$, put
$$\beta_{j+1}=\frac{\|u^j\|^2}{\|B^{1/2}u^j\|^2},\qquad
 F_{j+1}=\sqrt{\beta_{j+1}}B^{1/2}u^j,\qquad
 \chi_j=\|H^{1/2}u^j\|^2-\beta_{j+1}\|u^j\|^2.$$
At a zero successor continue by zero, set $\beta=\lambda$, $\chi=0$.
With $v_j=\|F_j\|^2$, $e_j=\|H^{1/2}F_j\|^2$,
$p_j=\|LH^{1/2}F_j\|^2$, and partial sums
$P_N=\sum_{j<N}p_j$, $X_N=\sum_{j<N}\chi_j$, $V_N=\sum_{j<N}v_j$,
$$v_{j+1}=v_j-p_j,\quad e_{j+1}\le e_j-av_j-\chi_j,
 \quad p_j\le\min(v_j,e_j)\le\nu,$$
$$\lambda\le\beta_j\le e_{j-1}/v_j\quad(v_j>0),
 \qquad v_N=1-P_N,$$
$$aV_N+X_N\le\nu-\lambda+\lambda P_N,
 \qquad aV_N+X_N\le\nu-\sigma+\sigma P_{N+1},\quad\sigma=R^{-1}.$$
Every finite nonzero prefix lies in the required form domains.
:::

:::{prf:proof}
Cauchy–Schwarz in the spectral measure gives
$\|u\|^4\le\|B^{1/2}u\|^2\|H^{1/2}u\|^2$, proving the bounds on
$\beta$ and $\chi\ge0$. The squared $L^2$ norm of
$\nabla H^{-1/2}F_j$ is $v_j$ and its mean is $LH^{1/2}F_j$.
Centering proves the mass identity. Bochner bounds the derivative energy
of $u^j$ by $e_j-av_j$, and inverse normalization subtracts $\chi_j$.
Thus each successor is again in the form domain and all inequalities
hold inductively, including the zero convention. Since $L$ is a contraction,
$p_j\le e_j$. Telescoping, using $e_N\ge\lambda v_N$, gives the first
budget. For the second, write
$v_{N+1}=\|DF_N\|^2=\|\mathcal T H^{1/2}F_N\|^2\le Re_N$.
The telescoped inequality $aV_N+X_N\le\nu-e_N$ then gives the claim.
:::

The defect in inverse normalization also gives the identity
$$u^{j+1}=\beta_{j+1}^{-1/2}P_+\nabla u^j+P_+\nabla z^j,
 \qquad\|\nabla z^j\|^2=\chi_j/\beta_{j+1}. \tag{1}$$
Indeed take $z^j=B^{1/2}F_{j+1}-\beta_{j+1}^{-1/2}u^j$ and expand its
Dirichlet norm. The first term has symmetric newest derivative slots.
Thus a fresh adjacent swap has norm at most $2\sqrt{\chi_j/\lambda}$.
An older swap is acted on by $\sqrt\beta\mathcal T$, with its scalar
normalizer fixed to that of the original whole family, and never by an
uncontrolled differentiation.

For Appell testing put $Q_kh=\mathbb E[\mathcal A_kh]$. Its norm is
at most $k!c_k$. Integration by parts and the derivative rule for Appell
polynomials give
$Q_{k+1}/(k+1)=P_{k+1}Q_k\mathcal T$ and
$$P_k(\sqrt{\beta_j}Q_1u^{j-1})
 =\frac{\prod_{i=0}^{k-1}\sqrt{\beta_{j-i}}}{k!}Q_ku^{j-k}. \tag{2}$$
These hold on full output direct sums. The removed mean gradient contributes
zero since every positive-degree Appell polynomial is centered.

## The initial restart and a mesoscopic orbit

A coarse coefficient seed needed below follows without a new localization
argument. At the fixed depth $r_*$ of the static transfer, the certified
v1 profile bounds $C_P$ by $\Gamma^2\ell_{r_*}(a^{-1})^2$ for one universal
$\Gamma$. Repeated Poincaré inequalities on Appell derivatives give
$c_k\le C_P^{(k-1)/2}$: start with covariance normalization at degree one,
and use $K_k\le C_P k^2K_{k-1}$. Apply
[](#prop:sz-v2-static-coefficient-transfer). Since the fixed iterates of
$g$ satisfy $\ell_{r_*}(d)\le Cg(d)$, this proves
$$c_k\le[C_{\rm seed}\log(e+k)]^{k-1}\qquad(k\ge1). \tag{3}$$
The constant is uniform over all log-concave covariance contractions.
In particular choose a universal $\bar c_3\ge c_3$. Letwin gives $K_2\le8$.

:::{prf:lemma} Compensated gradient restart
:label: lem:sol-sz-v2-restart
For $R\ge16$ there is a centered unit starting family with energy $\nu$
and first three losses satisfying
$$\nu\le(R-K_2/(4R))^{-1},\quad
 \nu-\lambda\le2R^{-2},\quad P_3\le160\lambda^2.$$
More generally, for a centered unit genuine gradient $U$ of energy $e$,
inverse normalization, centering its gradient, then inverse normalization
again produces a unit family of energy at most
$$\big(e^{-1}-\|\operatorname{Sym}(LU)\|^2\big)^{-1} \tag{4}$$
whenever the denominator is positive.
:::

:::{prf:proof}
Normalize $U$ by $F_0=\sqrt\beta B^{1/2}U$,
$\beta=\|B^{1/2}U\|^{-2}$. Its first loss is
$p_0=\beta\|LU\|^2$. The skew-credit theorem gives
$1-p_0\ge\beta(e^{-1}-\|\operatorname{Sym}LU\|^2)$.
The next unit family $F_1/\sqrt{v_1}$ has energy at most
$\beta/(1-p_0)$, proving (4).
Use now the restricted gradient $U=\sqrt R\nabla f$ and $\sigma=R^{-1}$.
Quadratic testing of $Hf=R^{-1}(f-H(q\cdot X))$ gives
$2\operatorname{Sym}\mathbb E[X\otimes\nabla f]=R^{-1}Q_2f$:
the affine correction has zero pairing with the centered quadratic Appell
polynomial, since its gradient has zero mean. Hence
$\|\operatorname{Sym}LU\|^2\le K_2/(4R)$, proving the energy bound.
Also $\lambda\le\beta\le e\le\sigma$,
$\sigma-\lambda\le\sigma^2$, and $\sigma/\lambda\le17/16$.
Since $K_2/4\le2$,
$$\nu-\lambda\le\frac{\sigma}{1-2\sigma^2}
                    -\frac{\sigma}{1+\sigma}\le2\sigma^2.$$

We verify the three actual restart losses, rather than only their symmetric
parts. On three slots let $P=(I+s_{12})/2$, $S=(I+s_{23})/2$.
Then $\|T\|^2\le8(\|PT\|^2+\|(I-S)T\|^2)$: on the trivial and sign
representations $P+I-S=I$, and on the standard representation its eigenvalues
are $1\pm\sqrt3/2>1/8$. This also follows directly from the two-dimensional
reflection matrices. Let $\chi_{\rm pre}=e-\beta\le\sigma^2$.
For the original $p_1$, use (1) with the initial normalization and (2) at
degree two; the three-slot inequality gives
$$p_1\le2K_2\beta\beta_1+8(\beta_1/\beta)\chi_{\rm pre}.$$
For $j\ge2$ it gives
$$p_j\le2K_2\beta_j\beta_{j-1}v_{j-1}
                  +8(\beta_j/\beta_{j-1})\chi_{j-2}. \tag{5}$$
Through $j=3$, the crude loss bound $p_j\le\sigma$ implies
$v_j\ge1-j\sigma\ge13/16$, $\beta_j\le4\sigma/3$,
$\beta_j/\beta_{j-1}\le4/3$, and
$\beta_j\beta_{j-1}v_{j-1}\le4\sigma^2/3$.
The ratio estimate follows from decreasing energy and
$p_{j-1}\le e_{j-1}=\beta_{j-1}v_{j-1}$.
The first energy budget gives $\chi_0\le2\sigma^2$ and
$\chi_1\le3\sigma^2$. Equation (5) therefore gives respectively
$p_1\le32\sigma^2$, $p_2\le(128/3)\sigma^2$,
$p_3\le(160/3)\sigma^2$. Divide their sum by
$v_1\ge1-\sigma$ for the unit restart. Its first three losses are at most
$128\sigma^2/(1-\sigma)\le160\lambda^2$. All families used are nonzero
by the mass estimates.
:::

:::{prf:lemma} Mesoscopic powers
:label: lem:sol-sz-v2-mesoscopic
There are universal $R_0,C_*>0$ such that
$$R-C_*/R\le\|\mathcal T^m\|^{2/m}\le R
 \quad(1\le m\le\lfloor R\rfloor+2, R\ge R_0). \tag{6}$$
:::

:::{prf:proof}
First, if required normalizers satisfy $\beta_i\le3\sigma$ and
$\beta_i/\lambda\le6$, block recovery from the certified curvature dossier,
with one coordinate slot and three derivative slots, gives
$$p_j\le A_0\sigma^3+B_0(\chi_{j-2}+\chi_{j-3})\quad(j\ge3),
 \quad A_0=486\bar c_3^2,\ B_0=50000. \tag{7}$$
Indeed its recovery constants are $3$ and $4$. The degree-three coherent
term in (2) has squared norm at most $27\bar c_3^2\sigma^3$.
The two derivative swaps in (1), one propagated once by a map of norm at
most $\sqrt3$, give a symmetrization error at most
$6\sqrt{\beta_j/\lambda}(\sqrt{\chi_{j-2}}+\sqrt{3\chi_{j-3}})$.
Its square is at most $1296(\chi_{j-2}+\chi_{j-3})$.
Squaring the recovery inequality with weights $18,32$ proves (7).

Put $K=512+4A_0$, $M=\lfloor R\rfloor$, and $p_*=K\sigma^2$.
Increase $R_0$ so that $R_0\ge\max(16,4B_0,\sqrt{8K})$.
Use the compensated restart, whose energy obeys
$\nu\le\sigma+3\sigma^3$ and $P_3\le160\sigma^2$.
Before a first exit of $P_N$ above $p_*$, its required normalizers are at
most $\nu/(1-p_*)\le3\sigma$ with ratio to $\lambda$ at most six.
The possible exit successor still has mass at least $1-p_*-\nu>0$.
Sum (7) through $N\le M$, use the delayed budget at $N-2$, and obtain
$$P_N\le160\sigma^2+A_0N\sigma^3
                 +2B_0(3\sigma^3+\sigma P_N).
$$
Since $N\le\sigma^{-1}$ and $2B_0\sigma\le1/2$, this gives
$P_N\le(323+2A_0)\sigma^2<3K\sigma^2/4$. The first three prefixes
satisfy that bound directly, so no exit occurs.

Take the restricted extremizer $f$ and let
$W_k=\mathcal T^kf$, $a_k=\|W_k\|^2$, $b_k=\|LW_k\|^2$.
Then $a_0=1$, $a_1=R$, and $W_1/\sqrt R=U$.
The compensated normalized hierarchy is exactly
$F_j=s_j B^{1/2}W_{j+2}$ for positive scalars $s_j$; this follows
by substituting the definition of each successor. For
$\eta_k=a_k/\langle W_k,BW_k\rangle$ this gives
$$e_j/v_j=\eta_{j+2},\qquad
 b_{j+2}/a_{j+2}=p_j/(v_j\eta_{j+2}),\qquad\eta_k\ge\lambda.$$
Thus the prefix estimate implies
$\sum_{k=2}^{M+1}b_k/a_k\le K\sigma^2/[\lambda(1-p_*)]\le2K\sigma$.
The skew-credit argument already used in (4) gives
$a_2/a_1=\|\mathcal TU\|^2=\eta_1^{-1}-\|LU\|^2
\ge e_U^{-1}-K_2/(4R)\ge R-2\sigma$.
Bochner gives the form inequality $\mathcal T\mathcal T^*\preceq B$:
$\|H^{1/2}\mathcal Th\|\le\|h\|$ and duality prove it.
Consequently
$$a_{k+1}+b_k=\langle W_k,BW_k\rangle
 \ge\|\mathcal T^*W_k\|^2\ge a_k^2/a_{k-1}.$$
The ratios $a_k/a_{k-1}$ are therefore at least
$R-(2+2K)/R$ through $M+2$, using the finite, positive hierarchy above.
Multiply these ratios to obtain the lower bound in (6), with $C_*=2+2K$.
The upper bound follows from $\|\mathcal T\|^2=R$.
:::

## Averaged orbit and its static radius

:::{prf:lemma} Orbit defect identities
:label: lem:sol-sz-v2-raw-orbit
For $z>0$, $w_j=z^{-j/2}\mathcal T^jf$, $b_j=\|w_j\|^2$,
$l_j=\|Lw_j\|^2$, define $D_j=\|\nabla(B-zI)w_j\|^2$ for $j\ge1$.
Then
$$D_j\le z(b_{j+1}-2b_j+b_{j-1})+l_j, \tag{8}$$
$$w_{j+1}=\sqrt zP_+\nabla w_j+z^{-1/2}P_+\nabla(B-zI)w_j. \tag{9}$$
The fresh swap of the two newest derivative slots in $w_{j+1}$ has norm
at most $2\sqrt{D_j/z}$. Subsequent swaps propagate by $\mathcal T/\sqrt z$.
:::

:::{prf:proof}
Bochner gives $\|H^{1/2}w_j\|^2\le b_{j-1}/z$.
Also $\langle w_j,Bw_j\rangle=z b_{j+1}+l_j$ from
$\mathcal T^*\mathcal T=B-L^*L$. Expansion of the Dirichlet square
$D_j=\langle w_j,Bw_j\rangle-2z b_j+z^2\|H^{1/2}w_j\|^2$
proves (8). Identity (9) follows by adding and subtracting $zI$.
Each $w_j$, $j\ge1$, is a centered gradient in its newest slot;
subtracting a constant vector preserves this property. Its weak second
derivatives commute, so the first term in (9) is symmetric in the two
newest slots. The other term has norm at most $\sqrt{D_j/z}$, proving the
swap bound. All maps commute with permutations of older slots.
:::

:::{prf:lemma} Averaged startup
:label: lem:sol-sz-v2-averaged
For all sufficiently large universal $R$, set
$m=\lfloor R\rfloor$ and $z=\|\mathcal T^m\|^{2/m}$.
There are universal $C_S,C_7,C_0$ and a centered unit finite family with
energy $\nu$ and first seven losses satisfying
$$\nu\le\frac{z^{-1}}{1-C_Sz^{-3}},\quad
 S_7:=\sum_{j=0}^6p_j\le C_7z^{-3},\quad
 D_0:=\max(\nu-R^{-1},0)\le C_0z^{-3}. \tag{10}$$
Furthermore
$$\|\mathcal T^l\|\le C_{\rm blk}z^{l/2}\quad(l\ge0),
 \qquad C_{\rm blk}=(R/z)^{(m-1)/2}\le2. \tag{11}$$
:::

:::{prf:proof}
The map $\mathcal T=DB^{1/2}$ is compact and (6) makes
$\mathcal T^m\ne0$. Choose a unit top right singular vector $f$ of
$\mathcal T^m$ and use the orbit just defined. Then $b_0=b_m=1$,
$b_{j+1}\le(R/z)b_j$, and
$b_j\ge(z/R)^{m-j}$ for $0\le j\le m$.
Equation (6) gives $\log(R/z)\le2C_*/R^2$ beyond a fixed threshold.
Consequently
$$b_j\le2\ (0\le j\le m+9),\qquad b_j\ge1/2\ (0\le j\le m). \tag{12}$$
For $N=m+8$, summing (8) gives
$$\sum_{j=1}^ND_j\le\sum_{j=1}^Nl_j
 +z(b_{N+1}-b_N+1-b_1)\le\sum_{j=1}^Nl_j+2C_*.$$
The last bound uses $z(b_{N+1}-b_N)\le(R-z)b_N\le2C_*/R$ and
$z(1-b_1)\le z[1-(z/R)^{m-1}]\le C_*$ after a fixed enlargement.

We need full linear moments, not just symmetric moments. At degree two,
Appell testing gives $P_2Q_1w_2=Q_2w_1/(2\sqrt z)$.
The three-slot frame used in (5) and the fresh defect (9) yield
$$l_2\le(2K_2b_1+8D_1)/z.$$
For $j\ge3$, block recovery on one coordinate and three derivative slots
has constants $3,4$. The degree-three coherent term is
$P_3Q_1w_j=Q_3w_{j-2}/(3!z)$, while the symmetrization error is at most
$6z^{-1/2}(\sqrt{D_{j-1}}+\sqrt{R/z}\sqrt{D_{j-2}})$.
Since $R/z\le2$, squaring gives
$$l_j\le18\bar c_3^2z^{-2}b_{j-2}
                 +10^4z^{-1}(D_{j-1}+D_{j-2}). \tag{13}$$
Since $l_1\le b_1\le2$, (12),(13), and $N\le4z$ imply
$$\sum_{j=1}^Nl_j\le2+4K_2/z+36\bar c_3^2N/z^2
                         +(8+2\cdot10^4)z^{-1}\sum_{j=1}^ND_j.$$
Absorb the last term in the preceding defect-sum inequality by increasing
one universal radius threshold. It follows that
$$\sum_{j=1}^{m+8}D_j\le C_D,
 \qquad\sum_{j=2}^{m+8}l_j\le C_L/z \tag{14}$$
for universal constants.

Use the finite direct sum $Y=\bigoplus_{j=0}^{m-1}w_j$ and put
$S_k=\sum_{j=k}^{m+k-1}b_j$, $C_k=\sum_{j=k}^{m+k-1}l_j$.
The family $U=\mathcal TY/\sqrt{zS_0}$ has norm one because
$b_m=b_0$. It is centered and a genuine gradient in each output column;
Bochner gives $e_U\le z^{-1}$. Quadratic testing also gives
$\|\operatorname{Sym}Lw_j\|^2\le K_2b_{j-1}/(4z)$ for $j\ge1$.
Use this for $j=1,2$, and (14) for the remaining indices. Since
$S_0\ge m/2$ and $m$ is comparable to $z$, it follows that
$\|\operatorname{Sym}LU\|^2\le C_S z^{-2}$.

Start the hierarchy at $F_0=B^{1/2}Y/\|B^{1/2}Y\|$.
Its first successor, renormalized to unit mass, is the inverse
normalization of $U$. Apply (4); the unit restart at $F_2$ then has
energy at most $(z-C_Sz^{-2})^{-1}$, as claimed.
To verify its losses exactly, each $F_k$ is a positive scalar multiple
of $B^{1/2}\mathcal T^kY$, and
$$\|\mathcal T^kY\|^2=z^k S_k,\qquad
 \langle\mathcal T^kY,B\mathcal T^kY\rangle
                  =z^k(zS_{k+1}+C_k).$$
Consequently its loss fraction is
$$p_k/v_k=C_k/(zS_{k+1}+C_k). \tag{15}$$
For $2\le k\le8$, (14) gives $C_k\le C_L/z$, while the interval
in $S_{k+1}$ contains $k+1,\ldots,m$. Equation (12) gives
$S_{k+1}\ge m/4\ge z/8$ at $m\ge16$.
Thus these seven loss fractions are at most $8C_Lz^{-3}$. They are exactly
the first seven losses of the unit restart, whose masses are at most one;
take $C_7=56C_L$. Every family through $F_9$ is nonzero because its window
contains positive terms in the interior of (12).
Equation (6) gives $z^{-1}-R^{-1}=O(z^{-3})$, and the remaining energy
error is $O(z^{-4})$. This proves the bound on $D_0$.
Finally, for $l=qm+r$ with $0\le r<m$,
$\|\mathcal T^l\|\le R^{r/2}z^{qm/2}$, proving (11).
The estimate on $\log(R/z)$ already proves $C_{\rm blk}\le2$.
:::

:::{prf:lemma} Static radius controlling every degree
:label: lem:sol-sz-v2-static-radius
There is a universal $H_0\ge1$ and a parameter $Z(\mu)$ such that
$$c_d(\mu)\le Z(\mu)^{(d-1)/2}\ (d\ge1),\qquad
 C_P(\mu)\le Z(\mu)+2,\qquad
 Z(\mu)\le\max(H_0,C_P(\mu)). \tag{16}$$
Whenever $Z>H_0$, it is the $z$ of the averaged startup lemma.
:::

:::{prf:proof}
Choose a universal $R_*$ above the preceding thresholds with
$C_*/R_*\le1$, and such that for $R\ge R_*$,
$C_{\rm seed}^2\log(e+R)^2\le R/2\le z$. Put $H_0=R_*+1$.
For $R<R_*$ define $Z=H_0$; otherwise define $Z=\max(H_0,z)$.
Iteration of $Q_{k+1}/(k+1)=P_{k+1}Q_k\mathcal T$ across $m$
degrees, keeping older output slots and using contraction of every
symmetrization, gives
$$c_d\le\|\mathcal T^m\|c_{d-m}=z^{m/2}c_{d-m}
 \quad(d\ge m+1).$$
For $1\le d\le m$, the seed (3) bounds $c_d$ by $z^{(d-1)/2}$.
Repeated subtraction of $m$ proves this for every degree, including the
remainder degree one. If $R<R_*$, repeated Poincaré on Appell derivatives
gives $c_d\le C_P^{(d-1)/2}\le H_0^{(d-1)/2}$.
For large $R$, $C_P\le R+1\le z+2$ by (6), and $z\le R\le C_P$.
These statements and the small-$R$ case give (16).
Only finite-degree polynomial inequalities are used in future transfers;
no continuity of $Z$ or $m$ is asserted or needed.
:::

## Joint losses and finite comparison

:::{prf:lemma} Loss bound for the averaged startup
:label: lem:sol-sz-v2-joint-loss
For the averaged starting family, suppose a prefix's required normalizers
are at most $B_*$, and set $t=\max(1,B_*z)$. For dyadic $d\ge4$, define
$$\theta=324C_FC_{\rm blk}^2
       \sum_{k<d\text{ dyadic}}k^6(B_*t^3)^kc_k^2,$$
$$\Delta=S_7+2C_F\sum_{4\le k<d\text{ dyadic}}k^2B_*^kc_k^2,
 \qquad\tau_d=C_FdB_*^dc_d^2,\qquad C_F=10^4.$$
Then
$$P_N\le\Delta+N\tau_d+(\theta/\lambda)X_{\max(N-2,0)}. \tag{17}$$
:::

:::{prf:proof}
Apply the joint frame to $T_j=\sqrt{\beta_j}Q_1u^{j-1}$.
Equation (2) bounds its degree-$k$ coherent projection by
$B_*^{k/2}c_k$. A fresh derivative swap is bounded by
$2\sqrt{\chi/\lambda}$. After $h-1$ additional steps, (11) bounds
it by $2C_{\rm blk}t^{(h-1)/2}\sqrt{\chi/\lambda}$: the block
constant appears once for the entire propagation. These maps commute
with old slot permutations. Sorting the $3k$ derivative slots uses each
adjacent swap at most $3k$ times; telescoping products of isometries and
averaging gives
$$\|(I-S_k)P_kT_j\|
 \le6kC_{\rm blk}B_*^{k/2}c_k\lambda^{-1/2}
       \sum_{h=1}^{3k-1}t^{(h-1)/2}\sqrt{\chi_{j-k-h}}.$$
The inner convolution kernel has $\ell^1$ norm at most $3kt^{3k/2}$.
Weighted Cauchy–Schwarz, summation in $j$, and the frame weight $C_Fk^2$
produce the asserted coefficient $324C_FC_{\rm blk}^2k^6$.
Every defect index in a prefix $j<N$ is at most $N-3$, explaining the
delay in (17). At generation $j\ge7$, use the largest available dyadic
degree, capped at $d$; availability is $2k-1\le j$.
Each degree $k<d$ is used for $2k$ generations and contributes coherent
loss at most $C_FkB_*^kc_k^2$ per generation. The first seven losses
are kept separately. The terminal contribution is bounded by $N\tau_d$.
Shorter prefixes satisfy the same bound by nonnegativity. Every required
slot and defect index is present before invoking the frame.
:::

:::{prf:lemma} Delayed finite comparison
:label: lem:sol-sz-v2-delayed
Let a centered unit hierarchy start at energy $\nu\le1/4$ and write
$D_0=\max(\nu-\sigma,0)\le\sigma$. Fix $0<p\le1/8$ and
$B_*=\nu/(1-p)$. Suppose the bound
$$P_N\le\Delta+N\tau+(\theta/\lambda)X_{\max(N-2,0)},
 \qquad p_0+p_1\le\Delta$$
holds for every prefix whose required normalizers are at most $B_*$,
including its first exiting prefix. If
$$\theta\sigma/\lambda\le1/8,\qquad
 \Delta+\theta D_0/\lambda\le p/64,$$
then $a<12(\sigma+D_0/p)\tau$.
:::

:::{prf:proof}
For $N\ge3$, the delayed budget at $N-2$ gives
$X_{N-2}\le D_0+\sigma P_{N-1}\le D_0+\sigma P_N$.
For $N\le2$ the startup estimate suffices. Thus every justified prefix obeys
$$(1-\theta\sigma/\lambda)P_N\le\Delta+N\tau+\theta D_0/\lambda.$$
The first two successors exist since each loss is at most $\nu\le1/4$.
The delayed budget at one yields $a\le D_0+\sigma(p_0+p_1)
\le D_0+\sigma p$.
Suppose $a\ge12(\sigma+D_0/p)\tau$. Put
$m=\lceil(D_0+\sigma p)/a\rceil$ and $M=m+1$.
Then $M\le3(D_0+\sigma p)/a$ and $M\tau\le p/4$.
Before a first $N\le M$ with $P_N>p$, required normalizers use preceding
masses at least $1-p$, hence are at most $B_*$. The possible successor
has mass at least $1-p-\nu>0$. The preceding inequality gives
$P_N\le p/64+p/4+P_N/8$, hence $P_N\le cp$ with $c=17/56<1$.
There is no exit and this holds throughout the finite horizon.
At $m=M-1$, the delayed budget and surviving mass then give respectively
$$aV_m\le D_0+c\sigma p,\qquad
 aV_m\ge(1-cp)(D_0+\sigma p).$$
Subtract the upper bound from the lower. The difference is
$\sigma p(1-c-cp-cD_0/\sigma)\ge\sigma p(1-2c-cp)>0$,
a contradiction. No infinite hierarchy limit is used.
:::

## Closing the depth recurrence

:::{prf:theorem} Curvature profiles with a polynomial depth cost
:label: thm:sol-sz-v2-inner
There is a universal constant $C$ such that every centered regular
covariance contraction, in every dimension, satisfies
$$C_P(\mu)\le C(r+1)^{1/3}\ell_r(a^{-1})^2\qquad(r\ge1)$$
whenever $D^2W\succeq aI>0$. This proves
[](#thm:sz-v2-iterated-curvature).
:::

:::{prf:proof}
We first iterate the static radius $Z$ in (16). Let $r\ge r_*$ and
suppose its already established profile is
$Z\le\widetilde\Gamma_r^2\ell_r(a^{-1})^2$, where
$\widetilde\Gamma_r\ge G(r+1)^{1/6}$; $G$ will be one large universal
constant. Require $G^2>2H_0$. Static transfer then gives
$$c_k\le[Q\ell_r(k)]^{k-1},\qquad
 Q=(1+r^{-2})\widetilde\Gamma_r.$$
Together with (3), there are two simultaneous coefficient bounds, the
second independent of $r$. Put
$$s=r+1,\quad\delta=(32s)^{-1},\quad p=(4096s)^{-1},
 \quad b=(1-2p)^{-1},\quad q=e^{-\delta},$$
$$M_0=2^{44}(1+C_F),\qquad
 k_0=\lceil64\delta^{-1}\log(M_0/\delta)\rceil.$$
For a dyadic $d\ge4$, suppose for contradiction
$$Z>b^4e^\delta Q^2\ell_r(d)^2. \tag{18}$$
This exceeds the floor, so $Z=z$ is the actual block radius. Put $u=z^{-1}$.
Then $b^4uQ^2\ell_r(d)^2<q$, $u\le G^{-2}s^{-1/3}$,
and $u^3\le G^{-6}s^{-1}$.
The averaged startup gives (10); choose $G$ so that $C_Su^3\le p$ and
all universal radius thresholds hold. Prior to an exit of cumulative mass
$p$, the needed normalizers satisfy
$$B_*\le u/(1-p)^2\le bu,\qquad \max(1,B_*z)\le b.$$
Since $C_{\rm blk}\le2$, the preceding joint loss estimate is bounded by
$$\theta_d=1296C_F\sum_{k<d\text{ dyadic}}k^6(b^4u)^kc_k^2,$$
$$\Delta_d=C_7u^3+2C_F\sum_{4\le k<d\text{ dyadic}}k^2(bu)^kc_k^2,
 \qquad\tau_d=C_Fd(bu)^dc_d^2. \tag{19}$$

We check these sums uniformly in $r,d$. There is a universal $C_M$ such
that $k_0\le C_Ms^2$ for every $s\ge1$, since $\log s\le s$.
Therefore $s^{-1/6}\log(e+k_0)$ is bounded uniformly: bound it by
$\log(e+C_M)+2s^{-1/6}\log s$, and use
$\sup_{s\ge1}s^{-1/6}\log s=6/e$.
One fixed enlargement of $G$ thus ensures
$\widetilde\Gamma_r\ge2C_{\rm seed}\log(e+k_0)$.
For $k\le k_0$, the seed and (18) give
$$b^4u[C_{\rm seed}\log(e+k)]^2\le1/4,$$
$$ (b^4u)^kc_k^2\le b^4u\,4^{-(k-1)},$$
$$ (bu)^kc_k^2\le b^3u^3C_{\rm seed}^4\log(e+k)^4\,4^{-(k-3)}
 \quad(k\ge4).$$
The resulting integer series, with weights $k^6$ and $k^2$, converge.
They contribute respectively at most a universal constant times $u$ and
one times $u^3$.
For $k_0<k<d$, the iterated-logarithm coefficient bound and monotonicity
give
$$(b^4u)^kc_k^2\le b^4u q^{k-1},\qquad
 (bu)^kc_k^2\le q^k.$$
For $0<\delta\le1$, comparison with the integral of $(x+1)^je^{-\delta x/2}$
gives, with the generous fixed constants shown,
$$\sum_{k>k_0}k^6e^{-\delta k}
 \le2^{30}\delta^{-7}e^{-\delta k_0/2},\qquad
 \sum_{k>k_0}k^2e^{-\delta k}
 \le2^{10}\delta^{-3}e^{-\delta k_0/2}.$$
For example $k^je^{-\delta k/2}$ is integrated over $[k-1,k]$ after
replacing $k$ by $x+1$ and weakening the exponential by $e^{1/2}$;
expanding $(x+1)^j$ and integrating each monomial gives these bounds.
Also $e^{-\delta k_0/2}\le(\delta/M_0)^{32}$.
The chosen $M_0$ therefore makes the tail contributions at most $u$
and $p/512$, respectively. Replacing dyadic sums by integer sums only
increases them. We have universal constants $C_\theta,C_\Delta$ such that
$$\theta_d\le C_\theta u,\qquad
 \Delta_d\le C_\Delta u^3+p/512. \tag{20}$$

Because $C_P\le z+2$, we have $\lambda\ge1/(z+2)$.
Also $\sigma=R^{-1}\le u$ and $\sigma\ge u/2$ above a fixed threshold.
Choose $G$ once so large that, in addition to all previous requirements,
$$2C_\theta/G^2\le1/8,\qquad
 (C_\Delta+2C_\theta C_0)/G^6\le2^{-20},$$
$$C_S/G^6\le1/4096,\qquad
 G^{-2}+4096C_0G^{-6}\le1,\qquad G^4\ge2C_0.$$
All these are compatible lower bounds on a single universal constant.
They imply
$$\theta_d\sigma/\lambda\le1/8,\qquad
 \Delta_d+\theta_dD_0/\lambda\le p/64,\qquad
 \sigma+D_0/p\le1.$$
Indeed $\theta_dD_0/\lambda\le2C_\theta C_0u^3$ for $z\ge2$, and
$u+4096sC_0u^3\le G^{-2}+4096C_0G^{-6}$.
The same thresholds ensure $\nu\le1/4$ and $D_0\le\sigma$.
The delayed comparison consequently gives
$$a<12C_Fd(bu)^dc_d^2. \tag{21}$$

If $0<a\le1$, put $h=\log(e+a^{-1})$ and choose dyadic $d$ with
$$C_Ts^2h\le d<2C_Ts^2h$$
for a sufficiently large universal $C_T$.
It can be chosen so that $\log(12C_Fd/a)\le\delta d$ for all $s,h\ge1$:
the left side is at most $\log(24C_FC_T)+2\log s+2h$, while the right
is at least $(C_T/32)sh$. It suffices that
$C_T/32\ge\log(24C_FC_T)+4$ and $d\ge4$.
Writing $L_*=Q^2\ell_r(d)^2\ge1$, the assumed (18) and (21) imply
$$a<12C_FdL_*^{-1}(buL_*)^d
 \le12C_Fd e^{-\delta d}\le a,$$
a contradiction. Thus
$$Z\le b^4e^\delta(1+r^{-2})^2\widetilde\Gamma_r^2\ell_r(d)^2. \tag{22}$$
For $a\ge1$, Brascamp–Lieb gives $C_P\le1$; by (16), $Z\le H_0$,
so the large universal profile already covers this case.

The logarithmic elasticity estimate from the static-transfer proof gives
$$\ell_r(d)\le\zeta_r\ell_{r+1}(a^{-1}),\qquad
 \zeta_r=\exp(2^{-r}\log(2C_T(r+1)^2)).$$
Furthermore
$$\log(b^4e^\delta)\le16p+\delta
 =9/(256s)\le\tfrac13\log(1+1/s),$$
where $\log(1+1/s)\ge1/(2s)$ suffices.
Define
$$B_{r_*}=1,\quad
 B_{r+1}=B_r(1+r^{-2})^2\zeta_r^2,\qquad
 \widetilde\Gamma_r^2=G^2(r+1)^{1/3}B_r.$$
The product is bounded above and below by positive universal constants,
since its logarithm is at most a constant multiple of
$\sum r^{-2}+\sum2^{-r}(1+\log(r+1))<\infty$.
At the one fixed depth $r_*$, the v1 curvature theorem and (16) initialize
the $Z$ profile by one further enlargement of $G$.
Equation (22) now proves the next profile at each finite depth, with the
chosen amplitude, because the factor $b^4e^\delta$ is paid by
$((r+2)/(r+1))^{1/3}$. Every coefficient premise used at a given step has
therefore already been proved at its previous finite depth.
Cover the finitely many smaller depths by the certified v1 profiles and
increase one universal constant. Finally (16) and $\ell_r\ge1$ give
$C_P\le(\widetilde\Gamma_r^2+2)\ell_r(a^{-1})^2$.
The additive two is absorbed once here, after the radius induction.
This proves the asserted universal polynomial envelope in $r$.
:::

**Fences respected.** No `bounded_by` edge is proposed for this node.
The brief's small-degree initialization requirement is met by the static
transfer starting at degree two and the fixed seed (3). All large-radius
requirements are universal and are imposed before starting the depth
induction; their common constant is $G$. This profile is still curvature
dependent, and its dimension transfer still depends on dimension. No CMH,
occupation or trace antecedent is discharged. There is no infinite-depth
limit and no use of a KLS-equivalent coefficient assertion without its
explicit profile premise.
