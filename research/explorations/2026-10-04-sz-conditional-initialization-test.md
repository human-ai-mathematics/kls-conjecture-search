---
---

# Conditional initialization: the retained terminal term and its missing slack

## Question examined

Route `ap:sz-conditional-initialization`; canonical candidate
`cand:sz-uniform-conditional-initialization` in
[the Wave A contract](2026-10-04-wave-a-sz-contract.md). Starting lens: **prove**.
The attempted proof yields a sharper sufficient condition and an obstruction
only to closing that condition with saturated inductive coefficients. It
neither proves nor refutes the candidate. No recovery or occupation comparison
is undertaken.

The statement under examination, quoted verbatim from its canonical record, is:

> There exist universal G >= 1 and integer r0 >= 2 such that, for every
> integer r >= r0 and every Gamma >= G, if every centered regular
> log-concave covariance contraction with potential curvature at least aI
> satisfies CP <= Gamma^2 ell_r(a^{-1})^2 for every a > 0, then every
> centered log-concave covariance contraction mu satisfies
> c_d(mu) <= ((1+r^{-2}) Gamma)^d ell_r(d)^d/(d+1)^2 for every integer
> 1 <= d < ceil(32 r^2). Regular means a smooth potential with positive
> lower and finite upper Hessian bounds; c_d is the symmetric Appell
> coefficient sqrt(K_d)/d! in full ordered-index Hilbert--Schmidt norm,
> and ell_r is the r-fold iterate of x -> log(e+x).

Write its universal regular-law antecedent as $\mathcal H_r(\Gamma)$.
It is assumed throughout the terminal-transfer calculation, for all dimensions,
all such laws, and every admissible curvature lower bound. The choice of $G,r_0$
precedes $r,\Gamma$, and the latter precede the target law and degree.
The premise is not replaced by a bound for one target law or one posterior.

The mathematical inputs are [](#thm:sz-iterated-curvature), specifically its
certified dossier's equations (2), (5), (9), and (10), and the Appell and
localization constructions in [](#thm:sz-polynomial-variance). Their relevant
normalizations and statements, and [](#prop:sz-exponential-coefficients-equivalence),
were read. No source fact beyond these local proved arguments is needed.

## What we learned

### 1. An exact sufficient condition retaining the derivative energy

*Established, uncertified reduction.* Fix $r\ge2$, $\Gamma\ge1$, assume
$\mathcal H_r(\Gamma)$, and put

$$
\alpha=r^{-2},\qquad R=(1+\alpha)\Gamma,\qquad
b_0=1,\quad b_k=\frac{\ell_r(k)^k}{(k+1)^2}\quad(k\ge1).
$$

At a degree $d\ge2$, suppose the desired bounds $c_k\le R^kb_k$ have already
been proved **for every centered log-concave covariance contraction** at each
$1\le k<d$. This is the degree-induction hypothesis, not an additional
unconditional coefficient assertion.

First take a compactly supported isotropic initial law $\mu$ and
$f=P_d^\mu[T]$, with symmetric $T\ne0$. Use the covariance-adapted localization
and $N_j,L_j,G_1$ of the certified iteration proof. Set
$Q=(d!)^2\|T\|_{\mathrm{HS}}^2$ and $w=R^{2d-2}b_{d-1}^2$.
For $0<\eta<1$ choose

$$
\tau=\eta/d^2,\qquad \delta=\eta\tau=\eta^2/d^2,\qquad
X(t)=\frac{G_1(t)}{Qw},\qquad
\overline X=\frac{X(\tau)+(\eta/\tau)\int_0^\tau X(t)\,dt}{1+\eta}.
$$

Equation (9) of the iteration proof, with no derivative-energy majorization,
gives the desired degree-$d$ bound whenever

$$
e^{\eta/d^2}(1+\eta)
\frac{\ell_r(d^2/\eta^2)^2}{\ell_r(d)^2}
J_{r,d}\,\overline X\le(1+\alpha)^2,                    \tag{T}
$$

where the **exact** adjacent-degree factor is

$$
J_{r,d}=\left(\frac{d+1}{d}\right)^4
 \left(\frac{\ell_r(d-1)}{\ell_r(d)}\right)^{2d-2}.      \tag{J}
$$

Indeed $\ell_r(d)^2 b_{d-1}^2/b_d^2=J_{r,d}$, so (T) follows simply by
dividing the transferred variance bound by $QR^{2d}b_d^2$.
This is sufficient, not an equivalence with the desired variance bound.
The actual earlier-covariance/terminal-gradient correlation in equation (9)
is preserved in $G_1(t)$ and its integral.

### 2. What the top Appell component actually is

*Established, uncertified reduction.* Let $\nu_t$ be the centered whitened
posterior and define the vector-valued polynomial

$$
q_t(y)=A_t^{1/2}\nabla f(m_t+A_t^{1/2}y).
$$

All vector and derivative indices use the full ordered-index Euclidean norm.
Its exact Appell expansion is

$$
q_t-\mathbb E_{\nu_t}q_t=\sum_{k=1}^{d-1}q_{k,t},\qquad
q_{k,t}=\frac1{k!}P_k^{\nu_t}
       [\mathbb E_{\nu_t}D_y^kq_t].
$$

The formula is componentwise in the vector output. In the Hilbert space with
squared norm $\mathbb E_{\rm loc}\mathbb E_{\nu_t}|\cdot|^2$, put

$$
S(t)=\frac{\|q_{d-1,t}\|}{\sqrt{Qw}}.
$$

Then, exactly,

$$
X(t)=\frac{N_1(t)}{Qw}
 +\frac{\|q_{d-1,t}+\sum_{k=1}^{d-2}q_{k,t}\|^2}{Qw}.   \tag{A}
$$

In particular (A) retains possible cross terms; the summands have not been
asserted orthogonal. The certified hierarchy and convolution bound imply,
uniformly for $0\le t\le\tau$,

$$
\frac{N_1(t)}{Qw}\le n_\eta:=2304\eta e^{2308\eta},\qquad
\frac{\|\sum_{k=1}^{d-2}q_{k,t}\|}{\sqrt{Qw}}
 \le E_\eta:=16\sqrt{2304\eta}\,e^{1154\eta}.           \tag{B}
$$

For the second estimate, apply the lower-degree coefficient inequalities to
each $q_{k,t}$, use
$N_{1+k}(t)\le2304\eta e^{2308\eta}Q R^{2(d-1-k)}b_{d-1-k}^2$
for $k\le d-2$, and sum
$\sum_{k=1}^{d-2}b_kb_{d-1-k}/b_{d-1}\le16$.
For $d=2$ this sum is empty and its true bound is zero.
Consequently one available bound is

$$
\overline X\le n_\eta+
 \left(\sup_{0\le t\le\tau}S(t)+E_\eta\right)^2.       \tag{C}
$$

At time zero only the top component remains. Writing $T_i$ for the
$(d-1)$-tensor slice of $T$, Appell differentiation gives

$$
S(0)^2=X(0)=
\frac{\sum_i\operatorname{Var}_{\mu}P_{d-1}^{\mu}[T_i]}
 {((d-1)!)^2 R^{2d-2}b_{d-1}^2\|T\|_{\mathrm{HS}}^2}. \tag{D}
$$

Here $\sum_i\|T_i\|_{\mathrm{HS}}^2=\|T\|_{\mathrm{HS}}^2$ exactly; there is
no missing factor $d$ or $1/d$. Thus tensor slicing and the top derivative
normalization supply no automatic combinatorial saving.

For example, if a genuine strengthened degree-$(d-1)$ estimate
$c_{d-1}(\nu)\le sR^{d-1}b_{d-1}$ with $0\le s\le1$ is available uniformly
over all centered log-concave covariance contractions, then
$S(t)\le s e^{2\eta}$ by the top hierarchy bound
$N_d(t)\le Qe^{4\eta}$. In that case (T) follows from

$$
e^{\eta/d^2}(1+\eta)
\frac{\ell_r(d^2/\eta^2)^2}{\ell_r(d)^2}J_{r,d}
\left[n_\eta+(s e^{2\eta}+E_\eta)^2\right]
\le(1+\alpha)^2.                                      \tag{S}
$$

This identifies exactly where a posterior-uniform coefficient improvement
would enter. A bound on (D) for the starting law alone does not justify the
uniform-in-time substitution in (S). Alternatively one could estimate the
actual $\overline X$ directly and retain the cross terms in (A).

### 3. The exact adjacent ratio still fails with saturated coefficients

*Established, analytic obstruction to a sufficient estimate only.* The
logarithmic derivative estimate from the iteration proof yields

$$
0\le\log\frac{\ell_r(d)}{\ell_r(d-1)}
 \le2^{-r}\log\frac d{d-1}.
$$

Since $(d-1)\log(d/(d-1))\le1$,

$$
\log J_{r,d}\ge4\log(1+1/d)-2^{1-r}.                  \tag{E}
$$

Choose the moving degree $d=r$, which belongs to
$2\le d<\lceil32r^2\rceil$. For all sufficiently large integers $r$,

$$
4\log(1+1/r)-2^{1-r}>2\log(1+r^{-2}).                 \tag{F}
$$

For completeness, $\log(1+x)\ge x-x^2/2$ and
$\log(1+x)\le x$ show that the difference in (F) is at least
$4/r-4/r^2-2^{1-r}$, positive eventually.
When $s=1$, every other factor on the left of (S) is at least one:
$\eta<1$ implies $d^2/\eta^2\ge d$, and the bracket is at least one.
Hence **no choice of $0<\eta<1$ closes (S) along $d=r$ for large $r$**.
Keeping the precise $e^{\eta/d^2}$ instead of $e^\eta$ does not change this.
This obstruction survives the exact adjacent ratio; it is stronger than
merely observing the fixed-degree failure of the coarsened condition (C3).

Necessary for (S), but not asserted necessary for the candidate, is

$$
s\le\frac{1+\alpha}{\sqrt{J_{r,d}}}.                  \tag{N}
$$

Along $d=r$, (E) implies

$$
\log s\le-2/r+2/r^2+2^{-r}.
$$

Thus this majorant needs a relative coefficient saving of order $2/r$ at
that degree; depth slack of order $r^{-2}$ does not supply it.
The unchanged short-time choice $\eta=c r^{-4}$ has
$n_\eta=O(r^{-4})$ and $E_\eta=O(r^{-2})$, and the logarithmic profile
ratio is $o(r^{-2})$ by the certified estimate (13). Therefore it is the
adjacent-degree saving, not these error terms, that first resists on $d=r$.
All asymptotics here follow from the displayed analytic formulas; no
numerical run is used.

The obstruction treats the **majorant** $s=1$ as saturated. It constructs no
law saturating that majorant, and no law satisfying $\mathcal H_r(\Gamma)$
while violating the desired conclusion. In particular it gives no refutation
of `cand:sz-uniform-conditional-initialization`.

### 4. What is initialized without the missing estimate

*Established, elementary special cases.* Degree one has $c_1\le1$, so $G\ge4$
suffices. For degree two, [](#thm:letwin-qcts) gives
$K_2\le8$ and hence $c_2\le\sqrt2$. The same $G\ge4$ suffices, since
$R^2\ell_r(2)^2/9\ge16/9>\sqrt2$.
These assertions include covariance contractions by whitening on affine
support and tensor contraction. They require no curvature-profile premise.

More generally, for any **fixed** integer $m$, $G\ge128m$ initializes all
$d\le m$ using $c_d\le32^dd!$, $d!\le m^d$, and $(d+1)^2\le4^d$.
This changes $G$ with $m$ and does not initialize the moving range.

In particular that factorial estimate cannot supply the required strict
$s<1$ along $d=r$ at a fixed finite $\Gamma$. To see this without computation,
let $\rho\in(1,2)$ be the fixed point of $g(x)=\log(e+x)$.
Its derivative is at most $e^{-1}$, so
$|\ell_r(r-1)-\rho|\le e^{-r}|r-1-\rho|$; hence
$\ell_r(r-1)\le3$ eventually. With $m=r-1$ and $R\le2\Gamma$, the ratio
of the factorial upper bound to the target degree-$m$ bound is at least

$$
\frac{32^m m!}{R^m b_m}
 \ge(m+1)^2\left(\frac{16}{3\Gamma}\right)^m m!
 \longrightarrow\infty.
$$

For instance $m!\ge(m/2)^{\lfloor m/2\rfloor}$ proves the divergence.
Taking the minimum of this upper bound and the induction hypothesis
therefore returns $s=1$ eventually. This is a statement about available
bounds, not about actual coefficients or feasibility of the premise at a
fixed $\Gamma$ through arbitrarily large depths.

### 5. Regularity, dependency and fence check

*Established scope accounting.* The localization calculation starts with
compact isotropic laws. The universal regular-law premise extends to its
possibly nonsmooth strongly log-concave posteriors by the certified affine
profile-inflation lemma; its continuity requirement holds for
$\Gamma^2\ell_r(a^{-1})^2$. No Hessian upper bound is required uniformly
across these approximations. A successful coefficient induction would pass
to arbitrary centered covariance contractions by conditioning, centering,
whitening, fixed-degree moment convergence and affine-support restriction,
as in the certified proof. These operations do not turn fixed-degree
success into success over an unproved moving range.

The named Song--Zhang input nodes have no `bounded_by` edges. The brief's
uniform-admissibility fence is respected by retaining all $r,\Gamma,d$
quantifiers and identifying the failed scalar condition explicitly.
Its equivalent-strength fence is respected: no unconditional all-depth
coefficient radius is asserted, and the universal $\mathcal H_r(\Gamma)$
premise has not been removed. In any future conditional theorem it belongs
in the antecedent, not among discharged dependencies. No comparison
threshold, recovery multiplier, CMH antecedent or occupation bound is
claimed improved.

## What resists

`cand:sz-uniform-conditional-initialization` remains unresolved over the
entire moving range. Keeping exact adjacent logarithms and the constant top
derivative removes no normalization factor automatically. Bounds for the
actual top Appell component, its correlation with lower components, or its
time average could still beat the saturated estimate. No such
posterior-uniform saving has been established here. A separate draft dossier
is not proposed for this reduction-only outcome.

## Proposed next step

Keep `ap:sz-conditional-initialization` active. Replace its completed first
test by this precise one: under $\mathcal H_r(\Gamma)$ and the all-law
lower-degree induction hypothesis, estimate the actual averaged derivative
energy $\overline X$ in (T), beginning with the moving sequence $d=r$.
Determine whether the symmetric gradient family in (D), evolved through
its actual whitened posteriors, supplies the saving in (N), or whether cross
terms in (A) can supply the corresponding saving directly in (T). A bound
for one target law at time zero is insufficient. If a proposed estimate
fails, record an exact obstruction to that estimate and retain the
candidate unless its full implication has actually been contradicted.
Do not repeat optimization of $\eta$ with $s=1$: (E)--(F) already exclude
that certificate. The desired final proof still has to cover every
$1\le d<\lceil32r^2\rceil$ with constants chosen before $r$.
