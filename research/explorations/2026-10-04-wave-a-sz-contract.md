---
candidates:
  - id: cand:sz-uniform-conditional-initialization
    statement: >-
      There exist universal G >= 1 and integer r0 >= 2 such that, for every
      integer r >= r0 and every Gamma >= G, if every centered regular
      log-concave covariance contraction with potential curvature at least aI
      satisfies CP <= Gamma^2 ell_r(a^{-1})^2 for every a > 0, then every
      centered log-concave covariance contraction mu satisfies
      c_d(mu) <= ((1+r^{-2}) Gamma)^d ell_r(d)^d/(d+1)^2 for every integer
      1 <= d < ceil(32 r^2). Regular means a smooth potential with positive
      lower and finite upper Hessian bounds; c_d is the symmetric Appell
      coefficient sqrt(K_d)/d! in full ordered-index Hilbert--Schmidt norm,
      and ell_r is the r-fold iterate of x -> log(e+x).
---

# Wave A: the complete Song–Zhang induction contract

## Question examined

Route `ap:sz-induction-contract`; nodes [](#thm:sz-iterated-curvature),
[](#thm:sz-curvature-comparison), [](#thm:sz-polynomial-variance),
[](#lem:sz-analytic-foundations), and
[](#prop:sz-exponential-coefficients-equivalence).
Started with **mine**, then moved to **construct** to specify a reusable
conditional replacement contract: the growing thresholds are payments for
specific estimates, not independent obstructions to every possible improvement.
This does not undertake `ap:sz-recovery-probe` or `ap:s-occupation`.

The frozen certified dossiers and their independent reviews dated 2026-10-03
are the local mathematical inputs. Source correspondence was checked against
[Song–Zhang v1, Sections 5.4 and 6.1–6.2](https://arxiv.org/html/2610.01447v1#S5.SS4):
comparison Theorem 5.1, coefficient Theorem 6.3/Lemma 6.4, and Proposition 6.1.
Equation numbers below refer explicitly to the local dossiers, whose proofs
contain the full arguments; source numbering is different.
No defect in either certified statement is proposed here.

## What we learned

### 1. Canonical statements and quantifier order

*Established by reading the certified interfaces.* The canonical comparison is:

> Let $0<\epsilon\le1$, let $\ell:\mathbb N\to[1,\infty)$ be nondecreasing,
> and let $R\ge2^{40}\epsilon^{-2}$. Let $\nu(dx)=e^{-W(x)}dx$ be a centered
> probability measure on $\mathbb R^n$ with $W\in C^\infty$,
> $aI\preceq D^2W\preceq bI$ for some $0<a\le b<\infty$, and
> $\operatorname{Cov}(\nu)\preceq I$. Using the Appell tensors of
> [](#thm:sz-polynomial-variance), define
> $K_k(\nu)=\sup_{T\text{ symmetric},\|T\|_{\mathrm{HS}}=1}
> \operatorname{Var}_\nu(P_k^\nu[T])$ and
> $c_k(\nu)=\sqrt{K_k(\nu)}/k!$.
> If $c_k(\nu)\le R^k\ell(k)^k/(k+1)^2$ for every integer $k\ge1$, then
> every dyadic integer $d\ge2$ satisfies
> $C_P(\nu)\le16(1+\epsilon)R^2\ell(d)^2
> \max\{1,a^{-1/(d+1)}\}$.

The canonical iterated statement is:

> Put $\ell_0(x)=x$ and $\ell_{r+1}(x)=\log(e+\ell_r(x))$ for $x\ge0$.
> There are a universal constant $C_0>0$ and universal constants
> $(\Gamma_r)_{r\ge1}$, with $\Gamma_r\le C_0 4^r$, such that the following
> holds simultaneously in every dimension. If $\nu(dx)=e^{-W(x)}dx$ is a
> centered probability measure, $W\in C^\infty$,
> $aI\preceq D^2W\preceq bI$ for some $0<a\le b<\infty$, and
> $\operatorname{Cov}(\nu)\preceq I$, then for every integer $r\ge1$,
> $C_P(\nu)\le\Gamma_r^2\ell_r(a^{-1})^2$.

Write $\mathcal H_r(\Gamma)$ for the latter regular-law inequality at depth
$r$, universally quantified over dimension, law, and its admissible $a,b$.
It must hold for all such laws **before** the degree induction starts.
The constants below are chosen first, then $r$, then $\Gamma$, then a law
and degree. No constant depends on the dimension, the Hessian upper bound,
or a particular localization posterior.

Appell normalization is $D^dP_d[T]=d!T$ and
$\mathbb E D^jP_d[T]=0$ for $0\le j<d$. The tensor norm is the sum over
all ordered indices, not over distinct monomials. For isotropic laws $c_1=1$;
for covariance contractions $c_1\le1$. Polynomial conclusions hold for all
centered log-concave covariance contractions, including affine-support
limits; the spectral comparison itself remains in the regular class.

### 2. Reusable finite-depth contract

*Established, reconstruction of the certified proof.* Fix a universal $c>0$
small enough for the estimate on $A(\eta)$ below. Choose one integer $r_0\ge2$
so that, for every $r\ge r_0$, with $\alpha_r=r^{-2}$,

$$
\eta_r=c\alpha_r^2\le\eta_0,\qquad
2^{-(r-1)}\log[2+2\log(1/\eta_r)]\le\alpha_r/8,\qquad
2^{-r}\log(2/\alpha_r)\le\alpha_r. \tag{C0}
$$

These requirements are compatible because exponential decay beats the
indicated polynomial and logarithmic factors. Fix $K\ge128\cdot33$.
For **each** depth $r\ge r_0$, the unchanged induction requires

$$
\boxed{\mathcal H_r(\Gamma_r),\quad
\Gamma_r\ge Kr^2,\quad R_r=(1+\alpha_r)\Gamma_r
\ge2^{40}\alpha_r^{-2}.} \tag{C1}
$$

The coefficient output is, simultaneously for every integer $d\ge1$ and
all log-concave covariance contractions,

$$
c_d\le R_r^d b_{r,d},\qquad
b_{r,0}=1,\quad b_{r,d}=\ell_r(d)^d/(d+1)^2\ (d\ge1). \tag{C2}
$$

The two distinct degree ranges are $1\le d<D_r=\lceil32r^2\rceil$,
initialized with $c_d\le32^dd!$, and $d\ge D_r$, handled by the hierarchy.
At a hierarchy degree $d$, let $Q=(d!)^2\|T\|_{\rm HS}^2$,
$w_s=R_r^{2s}b_{r,s}^2$, and use the posterior derivative quantities of
[](#lem:sol-sz-hierarchy). Their initial data are
$N_d(0)=Q$, $N_j(0)=0$ for $j<d$. Choose
$\tau=\eta_r/d^2$, $\delta=\eta_r\tau=\eta_r^2/d^2$.
The exact sufficient scalar closing condition in the iteration dossier (12) is

$$
e^{\eta_r}(1+\eta_r)A(\eta_r)
\frac{\ell_r(d^2/\eta_r^2)^2}{\ell_r(d)^2}
\frac{(d+1)^4}{d^4}\le(1+\alpha_r)^2, \tag{C3}
$$

where

$$
A(\eta)=2304\eta e^{2308\eta}
 +(e^{2\eta}+16\sqrt{2304\eta}\,e^{1154\eta})^2.
$$

The three logarithmic costs in (C3) are at most
$\alpha_r/2$, $\alpha_r/4$, and $\alpha_r/8$, respectively.
The last is exactly why this argument starts only at $D_r$.
For smaller degrees the proof uses
$32^dd!\le(128D_r)^d/(d+1)^2\le R_r^d b_{r,d}$;
$\Gamma_r\ge Kr^2$ pays this initialization, and is not used in (C3).

For comparison choose $\epsilon=\alpha_r$, set $h=\log(e+a^{-1})$, and
choose a dyadic degree $d$ with
$h/\alpha_r\le d<2h/\alpha_r$ (automatically $d\ge2$).
This is a **different** degree choice from $D_r$: the comparison is valid
at every dyadic $d\ge2$ because (C2) was already proved at all degrees.
Its curvature cost is at most $e^{\alpha_r}$; its iterated-log ratio costs
at most $e^{\alpha_r}$. Thus the output contract is

$$
\mathcal H_{r+1}\bigl(4e^{3/r^2}\Gamma_r\bigr). \tag{C4}
$$

Initialization in depth is independent of any final KLS bound:
$c_k\le32^kk!$ permits comparison with $\epsilon=1$, $R=2^{40}$,
$\ell(k)=k$, yielding $\widehat\Gamma_1=2^{48}$.
Coarse feedback has $R=2^{12}\Gamma$; comparison at $\epsilon=1$
yields $\widehat\Gamma_r=2^{48+30(r-1)}$ at every fixed depth.
Choose the starting constant so that

$$
\Gamma_{r_0}\ge\widehat\Gamma_{r_0},\qquad
4^{r-r_0}\Gamma_{r_0}\ge\max(Kr^2,2^{40}r^4)
\quad\text{for every }r\ge r_0. \tag{C5}
$$

The boundedness of a polynomial divided by $4^r$ makes this one finite
choice possible. It establishes the admissibility of (C1) before each
application, not just an eventual upper envelope.

### 3. Hypothesis usage and bottleneck map

*Established, proof mining.* Mechanism of [](#thm:sz-iterated-curvature):
regular curvature control extends to affine-normalized posteriors;
zero lower-derivative initial data make their short-time hierarchy nearly
lossless; the polynomial comparison adds one logarithm.
Its bottleneck is paying the small-degree initialization at the same radius
as the nearly lossless large-degree estimate.

Mechanism of [](#thm:sz-curvature-comparison):
iterate a centered inverse-gradient family from the first eigenfunction;
recover its polynomial tests while charging normalization defects;
absorb the cumulative centering loss before curvature exhausts energy.
Its bottleneck includes the *whole* lag kernel and the startup mass, not
only terminal tensor recovery.

| Hypothesis/payment | Exact use and failure when removed |
|---|---|
| Smooth potential, $0<aI\preceq D^2W\preceq bI$ | [](#lem:sz-analytic-foundations) supplies compact resolvent, attained first eigenfunction, Bochner, commuting weak Hessians, and spectral domains. Comparison does not operate directly on nonsmooth calibrations. |
| Centering and covariance $\preceq I$ | $Lh=\mathbb E[Xh]$ is a contraction; $p_j\le\lambda$. Whitening and affine contraction transfer polynomial coefficients in full tensor norm. |
| Universality of $\mathcal H_r(\Gamma)$ | Every whitened posterior, rather than just the starting law, needs it. |
| Continuity of $a\mapsto\Gamma^2\ell_r(a^{-1})^2$ | The affine-inflation lemma passes regular curvature control through Gaussian convolution. Its matrix weight is $A+\delta B^{-1}$, with no commuting-matrix assumption. |
| Compact support in the degree proof | Justifies localization integrability and the tower identity for fixed derivative products; removed by conditioning, centering, whitening and fixed-order moment convergence. No uniform-in-degree convergence rate is asserted. |
| $\ell\ge1$, monotone | Bounds lower-degree coefficients by the terminal profile and absorbs the final prefactor. |
| Whole-family normalization | $\beta=\|u\|_2^2/\|H^{-1/2}u\|_2^2$ is held fixed during permutations; normalizing components separately invalidates the propagated swap bound. |
| $D_r=\lceil32r^2\rceil$ | Pays $4\log(1+1/d)\le\alpha_r/8$ in (C3). |
| $\Gamma\ge Kr^2$ | Pays **only** the factorial initialization below $D_r$ in this sharp coefficient proof. |
| $L=\lceil64/\epsilon\rceil+2$, $p_*=\epsilon/[64(L+1)]$ | Makes the recovery-amplified defect base $J$ smaller than $C=16(1+\epsilon)$ while keeping normalizers $\beta_j\le\lambda/(1-p_*)$. |
| $k_0=\lceil2^{10}\epsilon^{-1}\log(2/\epsilon)\rceil$ | Splits the defect and startup series: factorial estimate below $k_0$, geometric profile tail above it. |
| $R\ge64k_0$ | Ensures $32k/R\le1/2$ in the factorial part. |
| $1664(4L^2/B)/R\le2^{-15}$ | Pays the low-degree lag-kernel contribution, comparison dossier (8); combined with the high-degree tail gives $2\lambda W_*^2\le1/8$. |
| $L/(CR^2)+(L+1)2^{36}/R^4\le p_*/32$ | Pays the first $L$ generations and the low-degree startup sum. The remaining geometric startup tail costs another $p_*/32$. |
| $\lambda\le p_*/2$ | Prevents a single centering jump from escaping past $p_*$; ensures nonzero successors through the possible exit. Derived from $\lambda\le1/(CR^2\ell(d)^2)$. |
| $R^2\ge64/(p_*C)$ | Absorbs the terminal factor $64/p_*$ into $(CR^2\ell(d)^2)^{d+1}$. |

Here $B=2\sqrt{L/(L-2)}$, $b=(1-p_*)^{-1}$,
$A=bB^2$, $J=B^4b^{L+1}$. The theorem's single
$R\ge2^{40}\epsilon^{-2}$ is a sufficient envelope for these separate
payments; it is not established to be their optimal envelope.
The all-degree coefficient inequality is an explicit **antecedent** of the
comparison. The certified factorial inequality and analytic foundations are
**dependencies**. Neither node has a `bounded_by` edge. The brief's
uniform-admissibility and equivalent-strength fences remain in force;
no CMH, occupation, or trace implication is inferred.

### 4. What the bounded-profile obstruction actually excludes

*Established here, not certified as new nodes.* The proposition tested is:
“There is a bounded sequence of profile radii satisfying the unchanged
contracts (C0)–(C3) and the small-loss comparison at arbitrarily large depth.”
Its exact negation is: for every finite $M$ and every sequence with
$\Gamma_r\le M$, there exists a depth $r$ at which (C1) fails.
Indeed $Kr^2>M$ eventually; independently
$(1+r^{-2})M<2^{40}r^4$ eventually.
This excludes every bounded-product replacement of (C4) **that retains
these admissibility premises**. It does not exclude every bounded-multiplier
improvement of the proof when those premises or their proofs are changed.
The portfolio's stronger unqualified wording should be narrowed accordingly.

There is also a structural obstruction in the displayed comparison
majorant, beyond the oversized constant $2^{40}$. Its lag kernel is

$$
w_s=\sum_{\substack{k<d\\k\text{ dyadic}}}
 t_k\mathbf1_{\{k+1\le s\le(L+1)k-1\}},\qquad
 t_k=\frac{4Lk}{B}J^{k/2}c_k\lambda^{(k-1)/2}.
$$

For an isotropic law $c_1=1$. Every terminal degree $d\ge2$ includes
$k=1$, hence

$$
W_*\ge(L-1)t_1=\frac{4L(L-1)}B\sqrt J,
\quad
2\lambda W_*^2\ge128L^2(L-1)^2\lambda. \tag{O1}
$$

Thus this particular absorption certificate $2\lambda W_*^2\le1/8$
requires $\lambda\le[1024L^2(L-1)^2]^{-1}$. Replacing only a tail estimate
cannot fix its degree-one contribution. Uniformly certifying that inequality
on the whole numerical small-gap interval
$0<\lambda\le1/(CR^2\ell(d)^2)$ forces
$CR^2\ell(d)^2\ge1024L^2(L-1)^2$. Likewise the displayed startup
majorant has $\delta_d\ge L\lambda$, so its target
$\delta_d\le p_*/16$ requires $\lambda\le p_*/(16L)$.
These are statements about the chosen majorants, **not** lower bounds on
actual centering loss or actual Poincaré constants. No law with a prescribed
small spectral gap is constructed or assumed. Exploiting the actual defects
rather than this positive kernel could evade (O1).

The exact large-degree closing condition (C3) also cannot simply be extended
to a fixed small degree: its left side is at least $(1+1/d)^4>1$ whereas
its right side tends to one. That is a failure of this sufficient scalar
condition, not a counterexample to the desired coefficient estimate.

### 5. A precise replacement specification

*Established as a conditional sufficiency calculation; the estimates
specified here are unproved.* A reusable repair of the same architecture
must provide both interfaces below, with constants chosen once.

1. **Uniform conditional startup.** Prove
   `cand:sz-uniform-conditional-initialization`. Combined with the already
   proved large-degree argument (C3), this yields (C2) at every degree for
   $\Gamma\ge G$, without $\Gamma\ge Kr^2$. This candidate is only the
   missing low-degree implication, not an asserted theorem.
2. **Uniform near-unit comparison on the used profiles.** For some universal
   $R_*$ and $B_*<\infty$, prove that, whenever the regular law satisfies
   (C2) at depth $r\ge r_0$ with $R\ge R_*$, every dyadic $d\ge2$ satisfies
   $C_P\le e^{B_*\alpha_r}R^2\ell_r(d)^2
   \max(1,a^{-1/(d+1)})$, with no growing threshold in $r$.
   This is a required interface specification, **not** a proposed proved
   comparison or evidence that it is true. It is deliberately restricted
   to the profiles used by the depth loop.

For a comparison proof retaining the stopped-energy contradiction, an exact
estimate to seek instead of the existing kernel bound is, on every justified
prefix through its possible exit,

$$
P_N\le s_{r,d}+N T_{r,d}\lambda^d+\theta\,X_N/\lambda,\qquad
\theta\le1/8,\quad s_{r,d}\le p_*/16. \tag{R1}
$$

It must additionally justify $p_j\le p_*/2$ through that exit, the successor
nonvanishing, and the normalizer hypotheses **without** requiring a growing
radius. Here $P_N,X_N$ and $v_N=1-P_N$ are the genuine spectral-family
quantities of the comparison dossier. If $\lambda\le1$ in the small-gap
regime, the same contradiction with $M=\lceil\lambda/a\rceil$ gives
$a\lambda^{-(d+1)}<32T_{r,d}/p_*$. Thus, to deliver the proposed comparison
with $C_r=e^{B_*\alpha_r}$, one needs precisely

$$
\frac{32T_{r,d}}{p_*}\le(C_r R^2\ell_r(d)^2)^{d+1}. \tag{R2}
$$

The current choices are $s_{r,d}=\delta_d$,
$T_{r,d}=2A^dc_d^2$, $\theta=2\lambda W_*^2$ and fail uniformity as
explained in (O1). Merely declaring (R1)–(R2) compatible supplies no estimate.
Changing the prefix cutoff or replacing the scalar normalizer bound is
allowed, but then the construction and exit argument must be reproved.
Keeping the old recovery bases $A\to4$, $J\to16$ while declaring
$C_r\to1$ also fails: the tail ratio $J/C_r$ no longer lies below one.

If both interfaces were proved, choose a starting
$\Gamma_{r_0}\ge\max(G,R_*,\widehat\Gamma_{r_0})$ and the same dyadic
choice as before. The resulting radius satisfies

$$
\Gamma_{r+1}\le
\exp[(B_*/2+5/2)\alpha_r]\Gamma_r.
$$

Indeed its four factors are $e^{B_*\alpha_r/2}$,
$1+\alpha_r$, the log-ratio $e^{\alpha_r}$, and the square-root curvature
cost $e^{\alpha_r/2}$. Their product is bounded over all depths.
This verifies the algebraic contract, not either replacement estimate.
There is no newly admitted KLS route.

A useful circularity test: an **unconditional** bounded initialization
radius for all $r$ and all $d<D_r$ already supplies uniform exponential
coefficients. For fixed $d$, let $r\to\infty$. The map $g(x)=\log(e+x)$
is a contraction on $[0,\infty)$ with derivative at most $1/e$ and unique
fixed point $\rho\in(1,2)$; hence $\ell_r(d)\to\rho$.
If $R_r\le M$, the initialization would give
$c_d\le(M\rho)^d/(d+1)^2$ for every $d$ and every law.
By [](#prop:sz-exponential-coefficients-equivalence) this is already
KLS-strength. Conversely uniform exponential coefficients can pay a fixed
polynomial denominator by a larger universal radius. The candidate above
therefore retains its curvature-profile antecedent: removing that antecedent
is not a cheap initialization repair.

*Observed:* no numerical observations were used; no run was needed.
*Intuition:* a useful improvement must change how the early degrees or
actual normalization defects are charged. The algebra does not identify
which such improvement is available.

## What resists

`cand:sz-uniform-conditional-initialization` is open. No estimate replaces
(R1) or proves the uniform comparison specification. The $k=1$ kernel
obstruction excludes retaining that majorant, not cancellations or refined
spectral information. The conditional low-degree statement is not certified
and cannot become a dependency. Regular approximation, all-law quantifiers,
and full tensor normalization remain compulsory in any replacement.

## Proposed next step

Close the audit objective of `ap:sz-induction-contract`: the complete
contract and its scoped bounded-profile decision have been delivered.
Do not present this closure as settling a mathematical target. Keep the
candidate available for a separately authorized construction assignment;
`ap:sz-recovery-probe` retains its own independent task and state.

The first test for that assignment is to derive the conditional low-degree
bound directly from $\mathcal H_r(\Gamma)$ with $\Gamma\ge G$, beginning
with the exact terminal-transfer expression in the iteration dossier (9)
for $2\le d<D_r$. Retain the actual adjacent-degree ratio and the top
Appell derivative, rather than replacing them by (C3). Decide whether the
factor $(d+1)^4/d^4$ can be eliminated or paid from degree-dependent slack
uniformly in $r$. A successful argument must initialize the *whole* moving
range, not only each fixed degree separately. Failure of that particular
bound is a local obstruction, not a refutation of the candidate.

Proposed portfolio delta: set `ap:sz-induction-contract.state: closed` and
replace its `next` with: “Before reopening as a construction objective,
prove or refute cand:sz-uniform-conditional-initialization, retaining its
universal curvature-profile antecedent and the whole range d<ceil(32 r^2);
then combine it with a uniform comparison satisfying (R1)–(R2) of the Wave A
contract. No bounded-product conclusion follows from a recovery multiplier
alone.” Narrow the objective's interpretation to unchanged-contract
incompatibility; do not claim impossibility for all bounded-multiplier
improvements. No ledger, manuscript, or bibliography delta is proposed.
