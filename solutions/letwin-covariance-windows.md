---
title: "Solution: third moments and covariance moment windows"
ledger-node:
  - prop:letwin-kappa
  - cor:letwin-window
  - cor:KI-letwin
  - thm:V2-window
numbering:
  enumerator: "107.%s"
---

*Part of the results of the literature written out here, Chapter [](#sec:covariance-tech); the reading order is on the [full proofs](#sec:proofs-literature) page.*

**Overview.** A quadratic-variance bound controls the directional third-moment
tensor by duality. Substitution into the published Klartag--Lehec fixed-time
moment theorem gives a covariance window of order $1/\log n$. Taking its
first and second moments yields the claimed interface consequences. The
independent published sup-over-time estimate supplies the shorter fallback
window without the quadratic input.

**Source matching.** We use [@KlartagLehec2022Polylog, Corollary 5.4], checked
in [arXiv:2203.15551v2](https://arxiv.org/html/2203.15551v2#S5), and
[@KLnotes, Theorem 61], checked in
[arXiv:2406.01324v2](https://arxiv.org/html/2406.01324v2#S7).
In the former source $\|\cdot\|_2$ is the Schatten two-norm, hence exactly
our Hilbert--Schmidt norm. Its parameter $\kappa_n$ is the one below.
Corollary 5.4 has a time constant independent of the moment exponent;
its moment constant depends on that exponent. The two citations concern,
respectively, fixed-time moments and a supremum-over-time tail. We do not
upgrade one into the other.

:::{prf:theorem} Directional third-moment bound
:label: thm:sol-letwin-kappa-bound
Conditional on [](#thm:letwin-qcts), for every dimension $n\ge1$,

$$
\kappa_n:=\sup_{\nu\text{ isotropic log-concave}}
\sup_{|\theta|=1}
\left\|\mathbb E_{X\sim\nu}[\langle X,\theta\rangle X\otimes X]
\right\|_{\mathrm{HS}}\le2\sqrt2.
$$

This proves [](#prop:letwin-kappa).
:::

:::{prf:proof}
Fix the law and direction, and put
$M=\mathbb E[\langle X,\theta\rangle X\otimes X]$.
It is a finite symmetric matrix. Centering and isotropy imply

$$
\mathbb E\langle X,\theta\rangle=0,\quad
\mathbb E\langle X,\theta\rangle^2=1,\quad
\|M\|_{\mathrm{HS}}^2
=\mathbb E[\langle X,\theta\rangle(X^TMX-\operatorname{Tr}M)].
$$

Cauchy--Schwarz and the quadratic-chaos antecedent give
$\|M\|_{\mathrm{HS}}^4\le\operatorname{Var}(X^TMX)
\le8\|M\|_{\mathrm{HS}}^2$.
If $M=0$ there is nothing to prove; otherwise divide by its squared norm.
Taking both suprema gives the result, with no dimensional factor.
:::

:::{prf:theorem} Fixed-time covariance moments
:label: thm:sol-letwin-moment-window
For each real $p\ge1$ there is $C_p<\infty$, depending only on $p$, and
there is a universal $c>0$, independent of $p$, such that for every isotropic
log-concave initial law on $\mathbb R^n$, $n\ge2$,

$$
\mathbb E\|A_t\|_{\mathrm{op}}^p\le C_p
\qquad(0\le t\le c/\log n).
$$

This is [](#cor:letwin-window); its proof uses [](#thm:letwin-qcts) as an
input theorem, not as an additional unstated conclusion of this dossier.
:::

:::{prf:proof}
The published Corollary 5.4 states that, for an absolute $C$,

$$
\mathbb E\|A_t\|_{\mathrm{op}}^p\le C_p
\quad\hbox{if }0<t\le(C\kappa_n^2\log n)^{-1}.
$$

Its proof combines Lemma 5.2's fixed-time tail with
$\|A_t\|_{\mathrm{op}}\le t^{-1}$, giving
$2^p+t^{-p}e^{-1/(Ct)}$. For every real $p\ge1$ the second term has
finite supremum: setting $y=1/t$, it is $y^pe^{-y/C}$, maximized at
$y=Cp$. Thus no integer restriction on $p$ or loss in the time window is
needed. The smooth positive initial-density convention of that paper
can be removed as follows.

Let $X\sim\mu$ and let $G,Z$ be independent standard Gaussians, independent
of $X$. For $\varepsilon>0$ put
$X_\varepsilon=(X+\varepsilon G)/\sqrt{1+\varepsilon^2}$.
Its law $\mu_\varepsilon$ is smooth, positive, isotropic and log-concave,
and converges weakly to $\mu$. For fixed $t>0$, write the tilted posterior
covariance as $A^\mu(t,b)$, with likelihood
$e^{b\cdot x-t|x|^2/2}$. The observation representation of localization
says that $A_t$ has the law of $A^\mu(t,tX+\sqrt t Z)$: this is the
Gaussian Bayes likelihood, equivalently the law of the tilt parameter in
the proof of Lemma 2.2 of the cited paper. Use the same representation
for $\mu_\varepsilon$ and $b_\varepsilon=tX_\varepsilon+\sqrt t Z$.

Almost surely $b_\varepsilon\to b=tX+\sqrt t Z$. For $b$ in a compact
set, each polynomial of degree at most two multiplied by
$e^{b\cdot x-t|x|^2/2}$ is bounded and continuous in $x$, with tails
tending uniformly to zero as $|x|\to\infty$. Weak convergence of the
initial laws and $b_\varepsilon\to b$ therefore give convergence of
their normalizing integrals and of their first two unnormalized moments.
The limiting normalizer is positive. Dividing and subtracting the squared
mean gives

$$
A^{\mu_\varepsilon}(t,b_\varepsilon)
\longrightarrow A^\mu(t,b)
\quad\hbox{almost surely}.
$$

Fatou transfers the uniform $p$-moment estimate to the arbitrary initial
law. At $t=0$, $A_0=I_n$, so the bound holds after enlarging $C_p$ to at
least one. This argument needs no convergence of entire stochastic paths.

Finally [](#prop:letwin-kappa), with its antecedent discharged by the input
[](#thm:letwin-qcts), gives $\kappa_n^2\le8$. Taking $c=1/(8C)$ therefore
places the asserted window inside the published window and proves the claim.
The proof of Lemma 5.2 uses $\beta=2\log n>0$ and is applicable for every
$n\ge2$; the stated dimensional restriction avoids interpreting $1/\log1$.
:::

:::{prf:theorem} First-moment interface consequence
:label: thm:sol-letwin-KI-window
Conditional on [](#thm:letwin-qcts), [](#ass:KI) holds with exponent
$C_2=1$ for $n\ge3$. For $t_1=c_0/\log n$ with universal $c_0>0$,
and $t_1\le T\le1$, the interface obeys

$$
\Xi_T\le C_1t_1+\log(T/t_1)\le C'(1+\log\log n).
$$

This proves [](#cor:KI-letwin), including its claimed use of the larger
cutoff in the polylogarithmic evaluation.
:::

:::{prf:proof}
Take $p=1$ in [](#cor:letwin-window). Choose its universal $c_0$ smaller
if necessary so that $c_0\le\log3$, making $t_1\le1$ for $n\ge3$.
This supplies exactly the constants in [](#ass:KI), with $C_2=1$.
For $0\le t\le t_1$, $X_t\le\|A_t\|_{\mathrm{op}}$ gives
$\mathbb EX_t\le C_1$. For $t>0$, the posterior is $t$-uniformly
log-concave; the Brascamp--Lieb covariance cap is $A_t\preceq t^{-1}I$.
Thus on $[t_1,T]$, $X_t\le t^{-1}$, and integration proves the first
displayed inequality. Since $T\le1$ and $n\ge3$, its right side is
at most $C_1+\log\log n+|\log c_0|$, which proves the second after
adjusting a universal constant. This repeats the interface integration
used in [](#cor:loglog); it claims no removal of the logarithmic loss and
does not change any near-worstness or geometric premises downstream.
:::

:::{prf:theorem} Second-moment interface and published fallback
:label: thm:sol-letwin-V2-window
Conditional on [](#thm:letwin-qcts), there exist universal $c_0,K_0>0$
such that for every isotropic log-concave initial law of dimension $n\ge2$,

$$
\mathbb EX_t^2\le K_0\qquad(0\le t\le c_0/\log n).
$$

The condition (V2) holds on this interval, and [](#cor:V2-implies) gives
the all-cut inequality there for each measure. Independently of Letwin's
input, (V2) holds on $[0,c_0/(\log n)^2]$ for every such measure; its
all-cut consequence is unconditional for products. These are all the
assertions of [](#thm:V2-window).
:::

:::{prf:proof}
For the first bound, take $p=2$ in [](#cor:letwin-window) and use
$X_t^2\le\|A_t\|_{\mathrm{op}}^2$. Integrating over any deterministic
subinterval $I$ gives $\int_I\mathbb EX_t^2\,dt\le K_0|I|$.
Apply [](#cor:V2-implies) to obtain the stated all-cut inequality. Its
product implication is unconditional, but this verification on the longer
window still uses the quadratic input.

For the independent fallback, use [](#thm:KL-window), the published
Theorem 61 in the notes cited above. At any $0<t\le1/(C(\log n)^2)$,
the event $\{\|A_t\|_{\mathrm{op}}\ge2\}$ is contained in its
sup-over-time event and has probability at most $e^{-1/(Ct)}$.
On the complement $X_t^2\le1$, and on the event the covariance cap
gives $X_t^2\le t^{-2}$. Therefore

$$
\mathbb EX_t^2\le1+t^{-2}e^{-1/(Ct)}
\le1+4C^2e^{-2}.
$$

The last bound follows by maximizing $y^2e^{-y/C}$ at $y=2C$.
At zero $X_0=0$. Choose $c_0$ no larger than both available window
constants and $K_0$ at least both available bounds. Integration again
gives (V2). The product branch of [](#cor:V2-implies) then yields its
unconditional all-cut consequence; the general branch retains its Letwin
antecedent. Both windows tend to zero with dimension, so neither statement
is [](#ass:all-cut-carleson), which requires a universal positive horizon.
:::

**Dependencies, hypotheses and fences.** The third-moment proposition is a
conditional implication with [](#thm:letwin-qcts) in `assumes`.
The unconditional moment-window corollary uses that theorem and the
third-moment proposition as proof dependencies. The two interface statements
retain the manuscript's Letwin antecedent. The second-moment statement
also uses [](#thm:KL-window) and [](#cor:V2-implies).
No target has an explicit `bounded_by` edge. The statements avoid dimension
one wherever $\log n$ is a denominator; the third-moment bound itself
includes dimension one. No posterior singularity arises from a full-dimensional
isotropic initial law at finite time, since its likelihood is positive.
The bounds are fixed-time moments, with $C_p$ allowed to depend on $p$;
there is no asserted dimension-free time window or moment of a time supremum.
