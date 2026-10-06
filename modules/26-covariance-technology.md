---
numbering:
  enumerator: "26.%s"
---

(sec:covariance-tech)=
# Covariance technology: small-time operator-norm control

Both variants of the fixed cut, the all-cut and the near-Cheeger variant, meter the danger of localization through the same cut-free covariance functional. Recall from [](#eq:interface-def) the covariance excess $X_t=(\lmax(A_t)-1)_+$ and the interface functional $\Xi_T(\mu)=\int_0^T\E X_t\dd t$; its second-moment companion is

```{math}
:label: eq:Xi2-def
\Xi^{(2)}_T(\mu)=\int_0^T\E X_t^2\dd t .
```

The bootstrap of Section [](#sec:bootstrap) consumes $\Xi_T$ and the covariance reduction of Section [](#sec:product-stress) consumes $\Xi^{(2)}_T$; both rest on the small-time operator-norm control imported here. We isolate it as an assumption and discharge it against the cited covariance technology. The exponent $C_2=2$ comes from the published sup-time estimate below. The $C_2=1$ implication [](#cor:KI-letwin) uses the quadratic input [](#thm:letwin-qcts), pinned to the July 2026 version-1 preprint. This source attribution is separate from the verification displayed beside each statement.

:::{prf:assumption} Known small-time operator-norm control; matched to {[@KlartagLehec2022Polylog; @Letwin2026QuadraticKLS]}
:label: ass:KI
There are universal constants $c_0,C_1,C_2>0$ such that for every isotropic log-concave $\mu$ on $\R^n$, $n\ge3$,

$$
\E\,\norm{A_t}_\op\ \le\ C_1
\qquad\text{for all }0\le t\le t_1(n):=c_0(\log n)^{-C_2}.
$$
:::

This is the shape of the estimate underlying the Chen bootstrap as presented in Klartag's lectures. The older argument through the then-known Cheeger bound supplied $C_2=2$. Letwin's dimension-free quadratic Poincaré inequality ([](#thm:letwin-qcts)) instead bounds the third-moment parameter $\kappa_n$ universally; inserted into the precise Klartag–Lehec moment window, it gives $C_2=1$. The standard two-sided-exponential product example suggests that $1/\log n$ is the natural endpoint for covariance-only control: the largest time scale it can reach, since the top covariance eigenvalue of that product reaches order $\log n$ at times of order $1/\log n$.

:::{prf:theorem} Klartag–Lehec; the sup-over-time form is [@KLnotes, Thm. 61]
:label: thm:KL-window
There is a universal constant $C$ such that for every isotropic log-concave $\mu$ on $\R^n$ and every $t\le\dfrac1{C\log^2n}$,

$$
\Prob\bigl(\exists\,s\le t:\ \norm{A_s}_\op\ge2\bigr)\ \le\ \exp\Bigl(-\frac1{Ct}\Bigr).
$$
:::

:::{prf:theorem} Isoperimetric $\log n$ bound; [@Klartag2023Logarithmic]
:label: thm:klartag-logn
There is a universal constant $C$ such that every isotropic log-concave probability on $\R^n$, $n\ge2$, satisfies $\hstar_n\ge C^{-1}(\log n)^{-1/2}$; by Cheeger's inequality, every such law has $\CP\le C\log n$.
:::

This published bound makes the small-gap branch in Section [](#subsec:spectral-window-chain) empty. The separate argument for [](#thm:letwin-kls) sharpens the dimension dependence without using this bound; no covariance statement below by itself gives a universal time window.

The newer parallel-coupling preprint contains rank-sensitive information that is stronger than an operator-norm window but still cut-free. The integrated rank estimate below uses the stopped rank estimate; the subsequent third-moment and covariance-window arguments use separate inputs.

:::{prf:theorem} Stopped rank tails; [@KlartagLehec2025ThinShell]
:label: thm:kl-stopped-rank-tail
For the simplified stochastic localization of an isotropic compactly supported log-concave law, write $\lambda_1(t)\ge\cdots\ge\lambda_n(t)$ for the eigenvalues of $A_t$. There is a universal $C$ such that, for every stopping time $\sigma$ and $t>0$,

$$
\sum_{i=1}^n\Prob\bigl(\lambda_i(t\wedge\sigma)\ge3\bigr)
\le Cn\exp(-t^{-1/8}).
$$

Consequently, if $\sigma_k=\inf\{t:\lambda_k(t)\ge3\}$, then

$$
\Prob(\sigma_k\le t)\le C\frac nk\exp(-t^{-1/8}),
\qquad
\E\sigma_k^{-2}\le C\left(1+\log\frac nk\right)^{16}.
$$
:::

:::{prf:theorem} Integrated rank covariance; [@KlartagLehec2025ThinShell]
:label: thm:kl-integrated-rank-covariance
Under the same hypotheses,

$$
\E\sum_{i=1}^n
\exp\left(2\int_0^1\lambda_i(t)\dd t\right)\le Cn .
$$
:::

Both statements refer to the pinned version 2 of [@KlartagLehec2025ThinShell]; their badges carry the verification information for each import. They control how many covariance eigenvalues are large and how long each rank can remain large. They do not control the orientation of a cut tensor $K_t$, a posterior Hessian $H_t$, or an eigenfunction source relative to those eigenspaces. In particular, neither theorem by itself discharges [](#conj:trace-upgrade), [](#conj:mm-spectral-occupation), or the high-rank part of [](#conj:stein-weighted).

:::{prf:proposition} Letwin's third-moment bound
:label: prop:letwin-kappa
Define

$$
\kappa_n
=\sup_{\nu}\sup_{\theta\in S^{n-1}}
\norm{\E_{X\sim\nu}\bigl[\inner{X}{\theta}\,X\otimes X\bigr]}_{\HS},
$$

where the first supremum is over isotropic log-concave laws on $\R^n$. Conditional on the preprint input of [](#thm:letwin-qcts),

$$
\kappa_n\le2\sqrt2.
$$
:::

:::{prf:proof}
Fix $\nu,\theta$ and put $M=\E[\inner{X}{\theta}\,X\otimes X]$. Isotropy and centering give

$$
\norm M_{\HS}^2
=\E\!\left[\inner{X}{\theta}\bigl(X^TMX-\Tr M\bigr)\right].
$$

Cauchy–Schwarz and [](#thm:letwin-qcts) therefore imply $\norm M_{\HS}^4\le8\norm M_{\HS}^2$. The claim follows, including the case $M=0$.
:::

:::{prf:corollary} The quadratic-chaos covariance window
:label: cor:letwin-window
For every fixed $p\ge1$ there are universal constants $c,C_p>0$ such that, for every isotropic log-concave initial measure on $\R^n$, $n\ge2$, and

$$
0\le t\le \frac{c}{\log n},
\qquad
\E\norm{A_t}_{\op}^p\le C_p.
$$
:::

:::{prf:proof}
Klartag–Lehec [@KlartagLehec2022Polylog, Cor. 5.4] give the fixed-time moment bound on $t\le(C\kappa_n^2\log n)^{-1}$. Substituting [](#prop:letwin-kappa), using [](#thm:letwin-qcts), gives the stated window. The time constant is independent of $p$, while $C_p$ may depend on it. To remove the source's smooth-density convention, smooth and isotropically normalize the initial law. At each fixed positive time the Gaussian likelihood makes its tilted moments continuous under this approximation; coupling the Gaussian observations gives posterior covariance convergence, and Fatou transfers the moment bound. At $t=0$, $A_0=I$. This passage concerns fixed-time moments and makes no assertion about a time supremum.
:::

:::{prf:remark} Attribution and the 2026 window upgrade
:label: rem:kl-window-verified
[](#thm:KL-window) — *sup over time*, threshold $2$, clean window $t\le(C\log^2n)^{-1}$ with no thin-shell constant — is [@KLnotes, Thm. 61]. It should *not* be attributed to [@KlartagLehec2022Polylog, Lemma 5.2], which is the weaker *fixed-time* bound $\Prob(\norm{A_t}_\op\ge2)\le e^{-1/(Ct)}$ on the $\kappa_n$-dependent window $t\le(C\kappa_n^2\log n)^{-1}$. The second moment is moreover published in exactly the strength needed: [@KlartagLehec2022Polylog, Cor. 5.4] gives $\E\norm{A_t}_\op^p\le C_p$ for every $p\ge1$ on that window, so $\E X_t^2\le\E\norm{A_t}_\op^2\le C$ directly. [](#prop:letwin-kappa) now makes the latter window $c/\log n$, resolving the former intermediate-window question at the fixed-time moment level. These statement numbers have been verified against arXiv:2406.01324v2 (the version matching the published Bull. Amer. Math. Soc. **62** (2025), no. 4, article) for [@KLnotes], and against arXiv:2203.15551 for [@KlartagLehec2022Polylog].
:::

:::{prf:corollary} Discharge of [](#ass:KI)
:label: cor:KI-discharged
The published [](#thm:KL-window), together with the Brascamp–Lieb cap, discharges [](#ass:KI) with $C_2=2$.
:::

:::{prf:proof}
For $t\le c/\log^2n$, split according to $\norm{A_t}_\op<2$ and use [](#thm:KL-window) plus $\norm{A_t}_\op\le t^{-1}$ to obtain $\E\norm{A_t}_\op\le2+t^{-1}e^{-1/(Ct)}\le C_1$.
:::

:::{prf:corollary} Letwin-v1 sharpening of the covariance window
:label: cor:KI-letwin
Conditional on the preprint input of [](#thm:letwin-qcts), [](#ass:KI) holds with $C_2=1$: there is a universal constant $c_0>0$ such that for every isotropic log-concave $\mu$ on $\R^n$, $n\ge3$, and every $0\le t\le c_0(\log n)^{-1}$,

$$
\E\,\norm{A_t}_\op\ \le\ C_1 .
$$

Consequently, conditional on the same version-1 preprint input, the polylog evaluation of the interface functional ($\Xi_T\le C(1+\log\log n)$, [](#cor:loglog)) may use the larger cutoff $t_1(n)=c_0/\log n$. This improves the verified early-time window but does not remove the $\log\log n$ universal-time loss or any of the geometric inputs downstream.
:::

:::{prf:proof}
This is [](#cor:letwin-window) with $p=1$.
:::
