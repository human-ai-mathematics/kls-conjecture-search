---
numbering:
  enumerator: "22.%s"
---

(sec:product-stress)=
# Product stress test of the all-cut Carleson estimate (Eldan–A)

This section executes [](#prog:product-test): it stress-tests the all-cut absorptive Carleson estimate ([](#ass:all-cut-carleson)) on product measures, where (i) localization preserves product structure, (ii) KLS is known ([](#prop:products)), and (iii) the operator norm of $A_t$ genuinely reaches $\log n$, so a proof cannot route through $\lmax$-control and a failure would force the geometric route.

Three core tools are pointed at the product model. First, the per-direction Carleson estimate ([](#cor:per-direction)) is a budget: $\E\int_0^\infty s_t\abs{G_t\theta}^2\dd t\le\theta^TR_0\theta\le1$ for every fixed direction. Second, the Stein identity $\calS_\nu(E)=s^2\norm K_\HS^2$ ([](#prop:stein-rep)) makes the quadratic-chaos machinery of Section [](#sec:qcts) directly applicable to the Riccati source. Third, the covariance technology of Section [](#sec:covariance-tech) supplies the cut-free comparison quantities. Notation is that of this report throughout: $\mu_t$ is Eldan stochastic localization [@Eldan2013ThinShell; @LeeVempala2024], $p_t,s_t,\delta_t,G_t,K_t,r_t,S_t,D_t,R_t$ are the two-color quantities, $\tau$ is the coarse balanced exit time, and $X_t=(\lmax(A_t)-1)_+$.

We also record the structural facts about products from [](#prop:products): if $\mu=\bigotimes_{i=1}^n\mu^{(i)}$ with isotropic one-dimensional log-concave factors, then $\mu_t$ is a product pathwise (the tilt factorizes), $A_t=\diag(A_t^{(1)},\dots,A_t^{(n)})$ with each $A^{(i)}$ a one-dimensional variance process of drift $-(A^{(i)})^2$, and $h_{\mu_t}\ge c\,\lmax(A_t)^{-1/2}$ pathwise, so that KLS for products is not in question; the question is whether the *program's estimate* holds there.

(sec:budgets)=
## Theorem A: coordinate budgets, and the refutation of the rank-one candidate

:::{prf:lemma} Block support
:label: lem:block
Let $\nu$ be a product probability measure on $\R^n$ with finite second moment, and let $E$ be measurable with respect to the coordinates in $J\subset\{1,\dots,n\}$. Assume $0<\nu(E)<1$. Then the two-color quantities of the pair $(\nu,E)$ satisfy: $\delta_i=0$ for $i\notin J$, and $G_{ij}=K_{ij}=0$ unless both $i,j\in J$.
:::

:::{prf:proof}
For $i\notin J$, the coordinate $x_i$ is independent of $\one_E$, jointly with each $x_j$. Hence $\E[x_i\mid E]=\E[x_i]$, giving $\delta_i=0$; for $j\in J$, $\Cov(x_i,x_j\mid E)=\E[x_i]\,\E[x_j\mid E]-\E[x_i]\,\E[x_j\mid E]=0$, using $\E[x_ix_j\one_E]=\E[x_i]\E[x_j\one_E]$; and for $j\notin J$, $j\ne i$, $\Cov(x_i,x_j\mid E)=0=\Cov(x_i,x_j)$, while for $j=i$ the conditional variance is unchanged. The same holds for $F=E^c$, so all entries of $G=\Sigma^E-\Sigma^F$ outside the $J\times J$ block vanish, and likewise for $K=G+(q-p)\delta\delta^T$.
:::

:::{prf:theorem} Coordinate-budget theorem
:label: thm:budget
Let $\mu=\bigotimes_i\mu^{(i)}$ be a product of isotropic one-dimensional log-concave measures, and let $E$ be measurable with respect to $k$ coordinates, with $p_0\in[2/5,3/5]$. Then:

(i) *(Total source budget)* $\displaystyle \E\int_0^\infty S_t\dd t\ \le\ \sum_{i\in J}(R_0)_{ii}\ \le\ k$;

(ii) *(Bounded information rate)* $\E\,r_{t\wedge\tau}\le1+k$ for all $t$;

(iii) *(Boundary bound)* there is a universal $c>0$ with

$$
\mu^+(E)\ \ge\ \frac{c}{\sqrt{1+k}}\;\min(p_0,q_0).
$$
:::

*Proof.* The pathwise product structure confines $G_t$ to the $J\times J$ block, so the source splits coordinatewise and the per-direction Carleson estimate ([](#cor:per-direction)) can be applied one direction at a time and summed. The calculation is carried out in Appendix [](#sec:appendix-route-e).

:::{prf:corollary} Refutation of the rank-one dynamic two-tail candidate
:label: cor:refutation
Let $\mu$ be a product as above and let $E$ be *any fixed* cut with $p_0\in[2/5,3/5]$ depending on one fixed coordinate $i$, chosen before localization. This includes a fixed two-tail cut in a coordinate whose variance subsequently inflates, but not a pathwise choice of $E$ or $i$. Then

$$
\E\int_0^\infty S_t\dd t\ \le\ 1
\qquad\text{and}\qquad
\mu^+(E)\ \ge\ c\,\min(p_0,q_0),
$$

with universal $c$. Consequently no such cut can witness a failure of the consumption chain of [](#ass:all-cut-carleson): the conclusion that the program derives from the Carleson estimate holds for these cuts unconditionally. Quantitatively, the source spends only a vanishing fraction of time at large height: for every *deterministic* level $L>0$,

$$
\E\,\bigl|\{t\ge0:\ S_t\ge\tfrac12L^2\}\bigr|
\ \le\ \frac2{L^2}\,\E\int_0^\infty S_t\dd t\ \le\ \frac2{L^2}.
$$

Thus a two-tail configuration of source height $S_t\asymp\Lambda^2$ ([](#prop:two-tail) with $\Lambda=A_t^{(i)}$), wherever along the path the coordinate variance $A_t^{(i)}$ inflates to order $\Lambda$, *is self-extinguishing*: a spike to height of order $\Lambda^2$ is paid at that rate from a per-coordinate budget of total size $1$, so the time spent above any fixed fraction of it is $O(\Lambda^{-2})$.
:::

:::{prf:proof}
Immediate from [](#thm:budget) with $k=1$; the occupation bound is Markov's inequality at the deterministic level, $\E\int_0^\infty\one_{\{S_t\ge L^2/2\}}\dd t\le\frac2{L^2}\E\int_0^\infty S_t\dd t$, together with the total source budget $\E\int_0^\infty S_t\dd t\le1$ from [](#thm:budget)(i).
:::

:::{prf:remark} What the refutation does and does not say
:label: rem:refutation-scope
[](#cor:refutation) verifies, for single-coordinate cuts, the *total stopped source bound* — which is what the Riccati–Gronwall consumption of [](#thm:carleson-implies-centroid) actually uses — not the literal interval form of [](#ass:all-cut-carleson); the distinction is immaterial for the program, since the consumption needs only $\E r_{t\wedge\tau}$ bounded, which (ii) provides directly. The corollary closes the specific attack proposed in the original formulation of the test when the cut and coordinate are fixed before localization. It does not justify selecting the coordinate or cut after observing the path. The per-direction estimate, which entered the program after that proposal, is exactly the tool that kills the fixed-coordinate version. The original “teeth” of the test — a proof of [](#ass:all-cut-carleson) cannot route through $\lmax(A_t)$ — is hereby complemented on the counterexample side: *a counterexample cannot route through a single inflated coordinate either*. Both the proof and the refutation are forced into genuinely high-dimensional, cut-specific territory; [](#thm:budget) localizes the entire remaining danger of the product model in cuts of unbounded coordinate complexity.
:::

(sec:covariance-reduction)=
## Theorem C: the covariance reduction and its general quadratic-chaos input

For cuts of unbounded complexity the block structure is unavailable. Product structure gives an elementary pathwise quadratic-chaos bound at every time. [](#thm:letwin-qcts) now gives the same intrinsic input for every log-concave posterior, conditional on its version-1 preprint status; the unwhitening loss remains exactly the cut-free covariance factor.

:::{prf:lemma} Quadratic chaos for non-isotropic products
:label: lem:product-qcts
Let $\nu=\bigotimes_i\nu^{(i)}$ be a product of centered one-dimensional log-concave measures with variances $\sigma_i^2$, $A=\diag(\sigma_i^2)$, $Y\sim\nu$. Then for every symmetric $M$,

```{math}
:label: eq:product-qcts
\Var\bigl(Y^TMY\bigr)\ \le\ C_*\,\norm{A^{1/2}MA^{1/2}}_\HS^2 ,
```

with $C_*$ universal.
:::

*Proof.* Expand the quadratic form and use independence and centering to kill every cross-covariance, leaving a diagonal and an off-diagonal sum. The calculation is carried out in Appendix [](#sec:appendix-route-e).

[](#lem:product-qcts) remains a preprint-independent proof of the input on product paths. For general log-concave posteriors it is replaced by [](#cor:qcts-source).

:::{prf:theorem} Pathwise covariance bound on the source
:label: thm:covariance-bound
Conditional on [](#thm:letwin-qcts), let $\mu$ be any isotropic log-concave initial measure and $E$ any measurable set. Then pathwise, on the coarse balanced window $\{p_t\in[1/3,2/3]\}$,

```{math}
:label: eq:S-le-X2
S_t\ \le\ C\bigl(1+X_t^2\bigr),
```

with $C$ universal. The same conclusion holds unconditionally when $\mu$ is a product of isotropic one-dimensional log-concave measures.
:::

:::{prf:proof}
Fix $t$ and write $\nu=\mu_t$, centered at $a_t$, with covariance $A=A_t$. Under the preprint input, [](#cor:qcts-source) gives $S_t\le17\lmax(A_t)^2$ on the coarse window. Since $\lmax(A_t)\le1+X_t$ and $(1+X_t)^2\le2(1+X_t^2)$, this proves the first assertion.

For a product path, the proof of [](#cor:qcts-source) goes through with [](#lem:product-qcts) in place of [](#thm:letwin-qcts), yielding the same conclusion with a different universal constant and without the preprint input.
:::

:::{prf:corollary} Covariance reduction of the all-cut estimate
:label: cor:V2-implies
Define the *second-moment interface condition* on a window $[0,T_0]$:

```{math}
:label: eq:V2
\tag{V2}
\int_I\E X_t^2\dd t\ \le\ K\,\abs I
\qquad\text{for every interval }I\subset[0,T_0].
```

Conditional on [](#thm:letwin-qcts), if (V2) holds for the localization of an isotropic log-concave measure $\mu$, then the all-cut estimate [](#eq:all-cut-carleson) holds for $\mu$ on $[0,T_0]$ with $C_0=C(1+K)$, $C_1=0$, and damping coefficient $\alpha=0$. For product measures the implication is unconditional. In that case it reduces the estimate to a statement about $n$ independent one-dimensional variance processes, with no reference to cuts.
:::

:::{prf:proof}
$\E\int_{I\cap[0,\tau]}S_t\dd t\le C\int_I(1+\E X_t^2)\dd t\le C(1+K)\abs I$ by [](#thm:covariance-bound), since the coarse window holds on $\{t<\tau\}$.
:::

:::{prf:remark}
This is the precise sense in which the product model isolates the covariance content of Eldan–A: a cut-free second-moment bound suffices. Note the consistency with the discipline warning of [](#eq:trivial-lambda): (V2) concerns the *excess* $X=(\lmax-1)_+$ in square, not $\E\int\lmax\le CT$ for all measures (which would already imply KLS and is not available); for products, (V2) is not circular — KLS for products is known independently — it is a concrete, decidable question about explicit one-dimensional SDEs. The next section decides it on the dimension-dependent early window and assesses it beyond.
:::

(sec:window)=
## Theorem D: the second-moment window and the sharpness regime

### The second-moment bound through the $1/\log n$ window

The required covariance input is the fixed-time operator-norm moment control of Section [](#sec:covariance-tech). The published sup-over-time estimate [](#thm:KL-window) supplies a preprint-independent $c/\log^2n$ fallback. Letwin's quadratic-chaos input and the Klartag–Lehec moment theorem together extend the fixed-time second-moment window to $c/\log n$.

:::{prf:theorem} Letwin-enhanced second-moment interface window
:label: thm:V2-window
Conditional on [](#thm:letwin-qcts), there are universal constants $c_0,K_0$ such that for every isotropic log-concave $\mu$ on $\R^n$ and every $t\le t_1(n):=c_0(\log n)^{-1}$,

$$
\E\,X_t^2\ \le\ K_0 ,
\qquad\text{hence \textup{(V2)} holds on }[0,t_1(n)]\text{ with }K=K_0 .
$$

Consequently, conditional on the preprint, [](#cor:V2-implies) gives the inequality [](#eq:all-cut-carleson), measure by measure, for every initial log-concave $\mu$ (including products) on this dimension-dependent window. For products the implication (V2)$\Rightarrow$[](#eq:all-cut-carleson) is preprint-independent, but the present $c/\log n$ verification of (V2) still uses the preprint. None of this establishes [](#ass:all-cut-carleson), whose time window must be universal in $n$. Without the preprint, [](#thm:KL-window) verifies (V2) for every measure on $[0,c_0(\log n)^{-2}]$; the all-cut conclusion then follows preprint-independently for products via the product case of [](#cor:V2-implies). For non-product measures that implication still uses [](#thm:letwin-qcts).
:::

*Proof.* On the short window the second-moment covariance bound is pointwise and integrates directly; the preprint-independent fallback instead splits on $\{\norm{A_t}_\op<2\}$ and pays the Brascamp–Lieb cap on the small complement. The calculation is carried out in Appendix [](#sec:appendix-route-e).

### The natural endpoint and the remaining universal-time gap

The formerly open fixed-time moment window between $c/\log^2n$ and $c/\log n$ is closed by the combination above, conditional on Letwin's version-1 preprint. This does not silently strengthen the distinct published *sup-over-time* statement of [](#thm:KL-window). The scale $1/\log n$ is also the natural endpoint for covariance-only control: the explicit product of centered one-sided exponentials has an eigenvalue that can reach order $\log n$ at times of order $1/\log n$ [@KLnotes, Remarks 62, 64 and Prop. 65]. Thus the live gap for $\Xi_T^{(2)}$ is no longer an intermediate polylogarithmic interval; it is the passage from the sharp dimension-dependent early window to a universal time, precisely where cut-aware temporal alignment must replace covariance-only control.

:::{prf:remark} Heuristic — Expected failure of (V2) on universal windows for exponential products
:label: heur:V2-fails
Let $\mu$ be the product of $n$ centered one-sided exponentials. Suppose, as the sharpness discussion of [@KLnotes, Remark 62] and [@KlartagChenNotes] indicates, that with probability bounded below some coordinate variance reaches the scale of the Brascamp–Lieb cap, $A_t^{(i)}\asymp1/t$, on a time window $[t_1,2t_1]$ with $t_1\asymp1/\log n$. Then on that window $\E X_t^2\gtrsim t^{-2}$, and

$$
\int_{t_1}^{2t_1}\E X_t^2\dd t\ \gtrsim\ \frac1{t_1}\ \asymp\ \log n .
$$

Hence on any *universal* window $[0,T_0]$, the condition (V2) is expected to fail for exponential products, with $\int_0^{T_0}\E X_t^2\dd t\gtrsim\log n$. We mark this as a heuristic: the cited statements establish inflation near the $1/\log n$ scale and describe the covariance estimate as “pretty much sharp”; the quantitative strength $\lmax\asymp1/t$ with non-negligible probability requires the sharpness example to be carried out in detail, which we have not done line by line.
:::

:::{prf:remark} Consequence of the heuristic, stated conditionally
:label: rem:covariance-route-dead
If [](#heur:V2-fails) is correct, then the covariance-only route of [](#cor:V2-implies) cannot prove [](#ass:all-cut-carleson) for products on a universal window — even though both the assumption's conclusion (KLS for products) and the per-cut estimates of [](#thm:budget) are true there. This is the precise product-model analogue of the crude-interface insufficiency of [](#rem:insufficiency): cut-free covariance information saturates at a logarithm. The stress test then returns the verdict the original proposal anticipated, in refined form: any proof of [](#ass:all-cut-carleson) for products must be *cut-aware*, and [](#thm:budget) exhibits the prototype mechanism — fixed per-coordinate budgets paid from the within-class variance $R_0$ — while [](#cor:refutation) shows that the dual counterexample mechanism must likewise be cut-aware and high-complexity. The residue is a single question.
:::

(sec:residual)=
## The residual: the adapted alignment problem

Combining [](#thm:budget) and [](#thm:covariance-bound), the anatomy of any counterexample to [](#ass:all-cut-carleson) within the product model is tightly constrained. To violate $\E\int_0^{T\wedge\tau}S_t\dd t\le MT$ for a given large $M$ and universal $T$, a fixed balanced cut $E$ must satisfy: (a) $E$ depends on at least $MT$ coordinates ([](#thm:budget)(i)); (b) at least of order $MT$ units of per-coordinate budget $\sum_i\E\int s\abs{Ge_i}^2$ — each coordinate contributing at most $1$ over *all* time — must be spent inside the common short window $[0,T]$; (c) the expenditure must be concentrated, by [](#thm:covariance-bound), at times when $X_t$ is large, i.e.\ aligned with the rare inflation excursions of the independent coordinate processes; and (d) throughout, the mass must remain balanced ($t<\tau$) and the source must not be matched by the damping $D_t$, which the Riccati identity subtracts for free. The cut is fixed before the Brownian path; the inflating coordinate indices and the conditional means $a_{t,i}$ around which a two-tail configuration would have to center are random. The decisive question is whether (b)–(d) are simultaneously achievable.

:::{prf:conjecture} Adapted alignment problem for products
:label: q:alignment
Let $\mu$ be a product of $n$ isotropic two-sided exponentials. There exist a universal $T_0$ and constants $C_0,C_1,\alpha<1$ such that for every $n$ and every balanced cut $E$, writing $P_t^H$ for the coordinate projection onto $H_t=\{i:A_t^{(i)}\ge2\}$ and $P_t^L=I-P_t^H$,

$$
\E\int_{I\cap[0,\tau]} S_t^H\dd t
\ \le\ C_0\abs I+C_1\E\int_{I\cap[0,\tau]}r_t\dd t
+\alpha\,\E\int_{I\cap[0,\tau]}D_t\dd t ,
\qquad I\subset[0,T_0] .
$$

Here

$$
S_t^H:=s_t\bigl(\norm{P_t^HG_tP_t^H}_\HS^2
+2\norm{P_t^LG_tP_t^H}_\HS^2\bigr)
=S_t-s_t\norm{P_t^LG_tP_t^L}_\HS^2
$$

counts every matrix entry incident to an inflated coordinate. This definition avoids an absorption loss: the simpler column mask counts each high–low entry only once, whereas the full source counts it twice. It also satisfies $S_t^H\le2s_t\sum_{i\in H_t}\abs{G_te_i}^2$. The negation says that a fixed cut can spend $\Omega(1)$-fractions of unboundedly many per-coordinate budgets inside the inflation excursions of those coordinates, within a common universal window, while staying balanced and underdamped. The displayed estimate, combined with [](#thm:V2-window) for the early $c/\log n$ window (conditional on the cited preprint) and a matching treatment of the non-inflated part at moderate times, would settle [](#prog:product-test) positively. Its failure — an explicit high-complexity cut achieving the alignment — would refute [](#ass:all-cut-carleson) and eliminate Eldan–A's all-cut hypothesis, leaving Eldan–B as the surviving localization sub-route rather than constraining unrelated approaches.
:::

:::{prf:remark} Designated test family
:label: rem:test-family
The first energy-shell candidate $\{\sum_i x_i^2\ge\theta\}$ is too radial: its source is already covered on the early covariance window and does not interrogate the dangerous adapted alignment. A sharper refutation-seeking family is the balanced tail union

$$
E_n=\{\max_i\abs{x_i}\ge a_n\}
=\Bigl\{\sum_i\one_{\{\abs{x_i}\ge a_n\}}\ge1\Bigr\},
\qquad \mu(E_n)=\frac12.
$$

It is permutation-symmetric but coordinate-selective, depends on all coordinates, and its complement is a product of one-dimensional truncated factors. Symmetry spreads the budget uniformly, while exchangeability lets a random inflating coordinate find the cut. A useful computation must measure the incident high-variance source $S_t^H$ in [](#q:alignment), together with $r_t$, $D_t$, balance survival, and interval sweeps past $c/\log n$. Such a computation is refutation-seeking model evidence only, not a proof of the all-cut estimate.
:::

(subsec:product-fences)=
## Fences this section establishes

:::{prf:conjecture} Single-coordinate product cuts self-extinguish
:label: obs:rank-one-refuted
For a product measure and a fixed balanced cut depending on one coordinate, $\E\int_0^\infty S_t\dd t\le1$ by [](#cor:refutation). Such a cut cannot sustain a covariance-inflation counterexample, so any surviving witness or proof must treat high-complexity cuts and occupation across many coordinates. The fence is methodological and is not itself certified.
:::
