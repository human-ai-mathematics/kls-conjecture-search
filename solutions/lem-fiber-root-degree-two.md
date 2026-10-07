---
title: 'The degree-two value for the root frame'
label: sec:sol-lem-fiber-root-degree-two
ledger-node: lem:fiber-root-degree-two
numbering:
  enumerator: D11.%s
---

*Part of the conditional-fiber mechanism, Chapter [](#sec:conditional-fiber-frame); the reading order is on the [full proofs](#sec:proofs-fibers) page.*

**Overview.** This dossier proves [](#lem:fiber-root-degree-two) as [](#thm:sol-fiber-root-degree-two): for every $m\ge3$, the root-frame pencil on the degree-two quotient $V_{m,2}$ of the uniform simplex has $\lmin(K,G)=(m+2)(m+3)/(5m^2)$, attained exactly on the radial quadratic. The proof splits $V_{m,2}$ into $S_m$-isotypic sectors, reduces the pencil on each to a small Gram matrix, and evaluates these exactly with Dirichlet moments. The corollary is conditional on the identification [](#eq:sol-frd2-root-identification) and lives inside the candidate degree-$k$ dual-certificate framework. It rules out degree-two dual refuters and says nothing about degrees $k\ge3$, non-polynomial tests or KLS.

1. Exact Dirichlet moments ([](#lem:sol-frd2-moments)) and the pair-fiber decomposition ([](#lem:sol-frd2-pair)). On each pair fiber, $\delta/s$ is uniform on $[-1,1]$, which gives the pair-energy formula [](#eq:sol-frd2-pair-energy); hence $K$ is finite and positive semidefinite on $V_{m,2}$.
2. Symmetry: [](#lem:sol-frd2-irreducibles) and [](#lem:sol-frd2-decomposition) show $V_{m,2}\cong\mathrm{triv}\oplus\mathrm{std}\otimes\R^2\oplus\mathrm X$, with explicit generators $f_0$, $(L,Q)$ and $F$.
3. [](#lem:sol-frd2-reduction) shows that invariant forms do not couple different sectors. Positivity on each sector therefore reduces to a Gram matrix of seed vectors.
4. Sector computations from steps 1–2: in the trivial sector the ratio is exactly $\lambda^*$ ([](#lem:sol-frd2-trivial)); the standard sector reduces to a $2\times2$ Gram matrix ([](#lem:sol-frd2-standard)); the two-row sector reduces to a scalar ([](#lem:sol-frd2-tworow)).
5. Assembly: $K-\lambda^*G$ vanishes on the trivial sector. It is positive definite on the standard sector ([](#eq:sol-frd2-std-psd)) and on $\mathrm X$. This proves [](#eq:sol-frd2-main) together with its equality case.
6. Corollary [](#cor:sol-frd2-no-degree-two-refuter), under its stated hypothesis: averaging a certificate over the root-frame atoms and applying the theorem gives $\eps\ge\lambda^*>\tfrac15$, and also gives $\Lambda_{m,2}\ge\lambda^*$.

**Scope.** This dossier proves an exact finite-dimensional spectral identity for the $A_{m-1}$ root-frame conditional-fiber form of Route F ([](#sec:conditional-fiber-frame)) restricted to polynomial test functions of degree at most two, for *every* $m\ge3$ simultaneously. The statement was suggested by exact rational computations at $m=3,\dots,15$ recorded in provenance-stamped run artifacts (see [](#rem:sol-frd2-artifacts)); no step of any proof below uses those computations. The main theorem is unconditional and self-contained. The corollary is stated *only* as a conditional, refutation-channel statement inside the candidate degree-$k$ dual-certificate framework for [](#conj:conditional-fiber-frame); it makes no claim about the all-frame gate itself, about degrees $k\ge3$, about non-polynomial tests, or about KLS.

**Setting.** Let $m\ge3$, let $\Delta_{m-1}=\{p\in\R_+^m:\sum_ip_i=1\}$, and let $P=(P_1,\dots,P_m)$ be uniform on $\Delta_{m-1}$, i.e. $P\sim\Dir(1,\dots,1)$; write $\mu$ for its law. Put $H_0=\one^\perp$, $d=m-1$, $R_m=\sqrt{m(m+1)}$, and

```{math}
:label: eq:sol-frd2-isotropic
X=R_m\Bigl(P-\frac1m\one\Bigr)\in H_0,
```

which is isotropic on $H_0$ (uniform-simplex root proposition of the certified dossier `solutions/conditional-fiber-frame-structure.md`; this normalization is not used before the corollary). The symmetric group $S_m$ acts on functions by permuting the coordinates of $p$, and $\mu$ is exchangeable, so $S_m$ acts by isometries of $L^2(\mu)$.

For $i<j$ let $\mathcal F_{ij}=\sigma\bigl((P_\ell)_{\ell\ne i,j}\bigr)$, let $s_{ij}=P_i+P_j$ (an $\mathcal F_{ij}$-measurable variable, since $s_{ij}=1-\sum_{\ell\ne i,j}P_\ell$), and write $\Var_{ij}$ and $\Cov_{ij}$ for conditional variance and covariance given $\mathcal F_{ij}$. Define, for $f,g\in L^2(\mu)$ with all the conditional quantities finite,

```{math}
:label: eq:sol-frd2-forms
K(f,g)
=\frac{12}{m^2(m+1)}\sum_{i<j}
\E\,\frac{\Cov_{ij}(f,g)}{s_{ij}^{\,2}},
\qquad
G(f,g)=\Cov(f,g).
```

The quadratic form $K(f,f)$ is exactly the root-frame conditional-fiber form $\mathcal D_{\rm root}(f)$ of [](#eq:conditional-root-form), as proved in the certified dossier above (its equation defining the root form); for the main theorem, [](#eq:sol-frd2-forms) is simply taken as the definition, so the theorem does not depend on that identification. Both $K$ and $G$ depend only on the $\mu$-equivalence classes of $f,g$, vanish when one argument is a.e. constant, and are $S_m$-invariant (exchangeability of $\mu$ and invariance of the family of pairs).

Let $W_{\rm poly}$ be the linear span of the monomials $p_i$ ($1\le i\le m$) and $p_ip_j$ ($1\le i\le j\le m$), i.e. all polynomials of degree at most $2$ with zero constant term, and define the *degree-two quotient*

```{math}
:label: eq:sol-frd2-V
V_{m,2}
=\bigl\{[f]:f\in W_{\rm poly}\bigr\}
\subset L^2(\mu)\big/\R\one,
```

where $[f]$ denotes the class of $f$ modulo additive constants. On $V_{m,2}$ the form $G=\Var$ is positive definite by construction, $K$ is positive semidefinite and finite ([](#lem:sol-frd2-pair)), and both are $S_m$-invariant. The generalized minimum eigenvalue of the pencil is

```{math}
:label: eq:sol-frd2-lmin
\lmin(K,G)\big|_{V_{m,2}}
=\min_{0\ne v\in V_{m,2}}\frac{K(v,v)}{G(v,v)}.
```

## Statements

:::{prf:theorem} degree-two root-frame pencil identity
:label: thm:sol-fiber-root-degree-two
For every $m\ge3$,

```{math}
:label: eq:sol-frd2-main
\lmin(K,G)\big|_{V_{m,2}}
=\frac{(m+2)(m+3)}{5m^2},
```

and the minimum is attained exactly on the one-dimensional line $\R\cdot\bigl[\textstyle\sum_i p_i^2\bigr] =\R\cdot\bigl[\abs{X}^2-(m-1)\bigr]$ spanned by the radial quadratic. In particular $\lmin(K,G)|_{V_{m,2}}>\tfrac15$ for every $m\ge3$, and $\lmin(K,G)|_{V_{m,2}}\to\tfrac15$ as $m\to\infty$.
:::

The corollary below lives inside the candidate degree-$k$ dual-certificate framework for the simplex falsification channel of [](#conj:conditional-fiber-frame) (the all-frame min–max $\Lambda_{m,k}$ and its exact dual certificates; an exploratory framework, not a statement of the manuscript). We restate the needed objects to be self-contained. Write $S(H_0)$ for the unit sphere of $H_0$. For $\theta\in S(H_0)$ and $f$ a polynomial, let

```{math}
:label: eq:sol-frd2-qtheta
\qJac_\theta[f]
=\int_{\theta^\perp}
\frac{\Var_{\mu_{\theta,z}}\bigl(f(z+T\theta)\bigr)}
{\Var_{\mu_{\theta,z}}(T)}
\dd\bar\mu_\theta(z)
```

be the single-direction normalized fiber energy of the certified structural dossier (with its null- and zero-variance-fiber conventions), a finite quantity for polynomial $f$ by the certified factor-$4$ bound. An *admissible frame* is an even Borel probability $\rho$ on $S(H_0)$ with $(m-1)\int\theta\theta^T\dd\rho=I_{H_0}$. A *degree-$2$ dual certificate with objective $\eps$* is a finite family $c_1,\dots,c_R\in V_{m,2}$, weights $w_1,\dots,w_R\ge0$, and a symmetric matrix $M$ on $H_0$ such that

```{math}
:label: eq:sol-frd2-certificate
\sum_{r=1}^R w_r\,G(c_r,c_r)=1,
\qquad
\sum_{r=1}^R w_r\,\qJac_\theta[c_r]\le\theta^TM\theta
\quad\text{for all }\theta\in S(H_0),
\qquad
\Tr M\le\eps.
```

By the weak-duality computation reproduced in the proof below, such a certificate forces every admissible frame $\rho$ (for which the averaged form is defined) to have degree-two pencil gap at most $\eps$; a sequence of such certificates with $\eps_m\to0$ at the fixed degree $k=2$ would therefore be the decisive fixed-degree refuter of the route on the simplex.

:::{prf:corollary} conditional: no degree-two dual refuter
:label: cor:sol-frd2-no-degree-two-refuter
Assume the identification, certified in `solutions/conditional-fiber-frame-structure.md` (nodes *lem:conditional-fiber-form* and *prop:conditional-fiber-root-obstruction*), of the pair-redistribution formula [](#eq:sol-frd2-forms) with the conditional-fiber form of the admissible $A_{m-1}$ root frame, i.e.

```{math}
:label: eq:sol-frd2-root-identification
K(f,f)=(m-1)\int_{S(H_0)}\qJac_\theta[f]\dd\rho_{\rm root}(\theta),
\qquad
\rho_{\rm root}=\frac1{m(m-1)}\sum_{i\ne j}\delta_{(e_i-e_j)/\sqrt2}.
```

Then for every $m\ge3$:

1. every degree-$2$ dual certificate [](#eq:sol-frd2-certificate) has

   $$
   \eps\;\ge\;\frac{(m+2)(m+3)}{5m^2}\;>\;\frac15;
   $$

2. consequently no sequence of degree-$2$ dual certificates with $\eps_m\to0$ exists, and within this framework any fixed-degree polynomial dual refutation of the conditional-fiber-frame route on the uniform simplex requires test degree $k\ge3$;

3. for every admissible frame $\rho$ whose averaged degree-two form $A_\rho(f,f)=(m-1)\int\qJac_\theta[f]\dd\rho(\theta)$ is defined on $V_{m,2}$, the all-frame degree-two min–max satisfies

   $$
   \Lambda_{m,2}
   :=\sup_{\rho\ \text{admissible}}
   \ \min_{0\ne v\in V_{m,2}}\frac{A_\rho(v,v)}{G(v,v)}
   \;\ge\;\frac{(m+2)(m+3)}{5m^2}\;>\;\frac15 .
   $$

This corollary asserts nothing about upper bounds on $\Lambda_{m,2}$, about $\Lambda_{m,k}$ for $k\ge3$, about non-polynomial test functions, about the truth value of [](#conj:conditional-fiber-frame), or about KLS.
:::

## Preliminaries: moments and pair fibers

:::{prf:lemma} Dirichlet monomial moments
:label: lem:sol-frd2-moments
For $a\in\mathbb N^m$ with $\abs a=\sum_ia_i$,

```{math}
:label: eq:sol-frd2-moment-formula
\E\prod_{i=1}^mP_i^{a_i}
=\frac{(m-1)!\,\prod_{i=1}^ma_i!}{(m-1+\abs a)!}.
```

In particular, with $D_r=m(m+1)\cdots(m+r-1)$ and distinct indices $i,j,k,l$:

```{math}
:label: eq:sol-frd2-moment-table
\begin{gathered}
\E P_i=\frac1m,\qquad
\E P_i^2=\frac2{D_2},\qquad
\E P_iP_j=\frac1{D_2},\\
\E P_i^3=\frac6{D_3},\qquad
\E P_i^2P_j=\frac2{D_3},\qquad
\E P_i^4=\frac{24}{D_4},\qquad
\E P_i^3P_j=\frac6{D_4},\\
\E P_i^2P_j^2=\frac4{D_4},\qquad
\E P_i^2P_jP_k=\frac2{D_4},\qquad
\E P_iP_jP_kP_l=\frac1{D_4}.
\end{gathered}
```
:::

:::{prf:proof}
Let $E_1,\dots,E_m$ be i.i.d. standard exponentials and $S=\sum_iE_i$. By the classical Gamma–Dirichlet factorization, $(E_1/S,\dots,E_m/S)\sim\Dir(1,\dots,1)$ and is independent of $S\sim\GammaLaw(m,1)$. Hence

$$
\prod_ia_i!
=\E\prod_iE_i^{a_i}
=\E\Bigl[S^{\abs a}\prod_iP_i^{a_i}\Bigr]
=\E S^{\abs a}\cdot\E\prod_iP_i^{a_i}
=\frac{(m-1+\abs a)!}{(m-1)!}\,\E\prod_iP_i^{a_i},
$$

using $\E S^{r}=\Gamma(m+r)/\Gamma(m)$. Rearranging gives [](#eq:sol-frd2-moment-formula); the table is immediate.
:::

The following consequences are used repeatedly ($i,j,a,b$ distinct):

```{math}
:label: eq:sol-frd2-small-moments
\E s_{ij}=\frac2m,\qquad
\E s_{ij}^2=\frac{2\cdot2+2\cdot1}{D_2}=\frac6{D_2},\qquad
\E(P_a-P_b)^2=\frac{2\cdot2-2\cdot1}{D_2}=\frac2{D_2}.
```

:::{prf:lemma} pair-fiber decomposition of degree-two energies
:label: lem:sol-frd2-pair
Fix $i<j$ and abbreviate $s=s_{ij}$, $\delta=P_i-P_j$. Then, conditionally on $\mathcal F_{ij}$ and on the event $\{s>0\}$ (whose complement is $\mu$-null), the ratio $\delta/s$ is uniform on $[-1,1]$ and independent of $\mathcal F_{ij}$; consequently

```{math}
:label: eq:sol-frd2-delta-moments
\Var_{ij}(\delta)=\frac{s^2}3,\qquad
\Var_{ij}(\delta^2)=\frac{4s^4}{45},\qquad
\Cov_{ij}(\delta,\delta^2)=0.
```

Every polynomial $f$ of degree at most $2$ can be written on the pair fiber, via the substitution $p_i=\tfrac{s+\delta}2$, $p_j=\tfrac{s-\delta}2$, uniquely as

```{math}
:label: eq:sol-frd2-abc
f=\alpha_f+\beta_f\,\delta+\gamma_f\,\delta^2,
```

where $\alpha_f,\beta_f,\gamma_f$ are polynomials in $s$ and $(p_\ell)_{\ell\ne i,j}$ (hence $\mathcal F_{ij}$-measurable), with $\deg\beta_f\le1$ and $\gamma_f$ constant. For two such polynomials $f,g$,

```{math}
:label: eq:sol-frd2-pair-energy
\E\,\frac{\Cov_{ij}(f,g)}{s^2}
=\frac13\,\E\bigl[\beta_f\beta_g\bigr]
+\frac4{45}\,\E\bigl[\gamma_f\gamma_g\,s^2\bigr],
```

a finite quantity. In particular $K$ is finite, symmetric, bilinear, positive semidefinite, and well defined on $V_{m,2}$.
:::

:::{prf:proof}
The law $\mu$ has constant density with respect to $(m-1)$-dimensional Hausdorff measure on $\Delta_{m-1}$. Conditioning on $(P_\ell)_{\ell\ne i,j}$ fixes $s=1-\sum_{\ell\ne i,j}P_\ell$ and leaves $(P_i,P_j)$ with a constant conditional density on the segment $\{(x,y):x,y\ge0,\ x+y=s\}$; parametrized by $P_i\in[0,s]$ this is the uniform law, so $\delta/s=2P_i/s-1$ is uniform on $[-1,1]$, with conditional law not depending on $\mathcal F_{ij}$. The event $\{s=0\}$ is the face $\{P_i=P_j=0\}$, which is $\mu$-null. With $V=\delta/s$ uniform on $[-1,1]$: $\E V=\E V^3=0$, $\E V^2=\tfrac13$, $\E V^4=\tfrac15$, whence $\Var(\delta\mid\mathcal F_{ij})=s^2/3$, $\Var(\delta^2\mid\mathcal F_{ij})=s^4(\tfrac15-\tfrac19)=\tfrac{4s^4}{45}$, and $\Cov(\delta,\delta^2\mid\mathcal F_{ij})=s^3\,\E V^3=0$, proving [](#eq:sol-frd2-delta-moments).

For [](#eq:sol-frd2-abc), substitute $p_i=\tfrac{s+\delta}2$, $p_j=\tfrac{s-\delta}2$ into each monomial of $f$:

```{math}
:label: eq:sol-frd2-substitution-table
\begin{gathered}
p_i=\tfrac s2+\tfrac\delta2,\qquad
p_j=\tfrac s2-\tfrac\delta2,\qquad
p_i^2=\tfrac{s^2}4+\tfrac s2\,\delta+\tfrac14\,\delta^2,\qquad
p_j^2=\tfrac{s^2}4-\tfrac s2\,\delta+\tfrac14\,\delta^2,\\
p_ip_j=\tfrac{s^2}4-\tfrac14\,\delta^2,\qquad
p_ip_\ell=\tfrac{p_\ell}2\,s+\tfrac{p_\ell}2\,\delta,\qquad
p_jp_\ell=\tfrac{p_\ell}2\,s-\tfrac{p_\ell}2\,\delta
\quad(\ell\ne i,j),
\end{gathered}
```

while monomials not involving $p_i,p_j$ contribute to $\alpha_f$ only. Collecting powers of $\delta$ gives [](#eq:sol-frd2-abc) with the stated degrees; uniqueness holds because $(1,\delta,\delta^2)$ are linearly independent functions of $\delta$ on any fiber with $s>0$. Since $\alpha_f$ is $\mathcal F_{ij}$-measurable, bilinearity of conditional covariance and [](#eq:sol-frd2-delta-moments) give

$$
\Cov_{ij}(f,g)
=\beta_f\beta_g\,\frac{s^2}3+\gamma_f\gamma_g\,\frac{4s^4}{45},
$$

the two cross terms carrying the vanishing factor $\Cov_{ij}(\delta,\delta^2)=0$. Dividing by $s^2$ on $\{s>0\}$ and taking expectations proves [](#eq:sol-frd2-pair-energy); the integrands are polynomials, hence bounded on the simplex, so the expectation is finite. Positive semidefiniteness of $K$ is clear from $\Var_{ij}\ge0$. Conditional covariances depend only on the a.e. classes of $f,g$ and vanish when one argument is a.e. constant, so $K$ descends to $V_{m,2}$.
:::

## Symmetry structure of the degree-two quotient

Throughout, “module” means a finite-dimensional real representation of $S_m$; all maps are $S_m$-equivariant unless stated otherwise. We use the following standard facts about a finite group $\Gamma$ acting on real vector spaces; each has a one-paragraph classical proof, recalled for self-containment.

- (Complete reducibility.) Averaging any inner product over $\Gamma$ produces an invariant inner product; the orthogonal complement of a submodule is a submodule; hence every module is a direct sum of irreducibles, every submodule has an invariant complement, and every quotient of a module is isomorphic to a submodule. Consequently, in a short exact sequence of modules the multiplicity of each irreducible is additive.

- (Schur.) A nonzero map between irreducibles is an isomorphism; the image of an irreducible submodule under any equivariant map is $0$ or isomorphic to it. The *$E$-isotypic component* $W_E(V)$ of a module $V$ is the sum of all submodules isomorphic to the irreducible $E$; equivariant maps send $E$-isotypic parts into $E$-isotypic parts, and $V$ is the direct sum of its isotypic components.

- (Orbit counting for permutation modules.) If $\Gamma$ acts on finite sets $S,T$, the space of equivariant linear maps $\R^S\to\R^T$ has dimension equal to the number of $\Gamma$-orbits on $T\times S$: an equivariant matrix is exactly a matrix constant on orbits.

- (Multiplicity via Hom.) If $E$ is irreducible with $\operatorname{End}_\Gamma(E)=\R\,\mathrm{id}$, then for every module $V$ the multiplicity of $E$ in $V$ equals $\dim\operatorname{Hom}_\Gamma(E,V)$, and $W_E(V)\cong E\otimes\R^{k}$ with $k$ that multiplicity. (Decompose $V$ into irreducibles by (F1); by (F2) and Schur, $\operatorname{Hom}_\Gamma(E,\cdot)$ of each summand is $\R$ for summands $\cong E$ and $0$ otherwise.) In particular the multiplicity of $E$ is monotone under submodules and quotients.

- (Invariant bilinear forms on an irreducible.) If $E$ is irreducible with $\operatorname{End}_\Gamma(E)=\R\,\mathrm{id}$, the space of invariant bilinear forms on $E$ is one-dimensional, spanned by any fixed invariant inner product $J_E$: a form corresponds to an equivariant map $E\to E^*\cong E$, i.e. to an element of $\operatorname{End}_\Gamma(E)=\R$.

:::{prf:lemma} the three irreducibles
:label: lem:sol-frd2-irreducibles
Let $M=\R^m$ with permuted coordinates and, for $m\ge3$, let $N=\R^{\binom{[m]}2}$ be the permutation module on unordered pairs $\{i,j\}$, with basis $(x_{ij})_{i<j}$. Then:

1. $M=\mathrm{triv}\oplus\mathrm{std}$, where $\mathrm{triv}=\R\one$ and $\mathrm{std}=\{a:\sum_ia_i=0\}$ is irreducible of dimension $m-1$ with $\operatorname{End}_{S_m}(\mathrm{std})=\R\,\mathrm{id}$, and $\mathrm{std}\not\cong\mathrm{triv}$.

2. For $m\ge4$, $N=\mathrm{triv}\oplus\mathrm{std}\oplus\mathrm X$ with each summand of multiplicity one, where $\mathrm X$ is irreducible of dimension $m(m-3)/2$, satisfies $\operatorname{End}_{S_m}(\mathrm X)=\R\,\mathrm{id}$, and $\mathrm X\not\cong\mathrm{triv},\mathrm{std}$. For $m=3$, $N=\mathrm{triv}\oplus\mathrm{std}$ and the summand $\mathrm X$ is absent.
:::

:::{prf:proof}
(1) $S_m$ has two orbits on $[m]^2$ (diagonal, off-diagonal), so $\dim\operatorname{End}(M)=2$ by (F3). Also $M^{S_m}=\R\one$ is one-dimensional, so $\mathrm{triv}$ has multiplicity one; let $C=\one^\perp$ be its invariant complement. Then $C^{S_m}=0$, so $\operatorname{Hom}(\mathrm{triv},C)=0$ and $2=\dim\operatorname{End}(M) =\dim\operatorname{End}(\mathrm{triv})+\dim\operatorname{End}(C) =1+\dim\operatorname{End}(C)$. A decomposable module has endomorphism algebra of dimension at least $2$ (the two projections), so $\operatorname{End}(C)=\R\,\mathrm{id}$ forces $C$ irreducible. Finally $C\not\cong\mathrm{triv}$ because $C^{S_m}=0$. Set $\mathrm{std}=C$.

(2) Let $m\ge4$. The orbits of $S_m$ on (ordered) pairs of $2$-subsets are classified by $\abs{A\cap B}\in\{2,1,0\}$, all realized, so $\dim\operatorname{End}(N)=3$. The orbits on $[m]\times\binom{[m]}2$ are classified by $i\in A$ versus $i\notin A$, so $\dim\operatorname{Hom}(M,N)=2$. As $N^{S_m}$ is one-dimensional (one orbit of $2$-subsets), $\mathrm{triv}$ has multiplicity one in $N$ and $\dim\operatorname{Hom}(\mathrm{std},N) =\dim\operatorname{Hom}(M,N)-\dim\operatorname{Hom}(\mathrm{triv},N)=2-1=1$, so by (F4) $\mathrm{std}$ has multiplicity exactly one. Decompose $N=\mathrm{triv}\oplus S'\oplus \mathrm X$ with $S'\cong\mathrm{std}$ and $\mathrm X$ the sum of the remaining irreducible summands, which contains no copy of $\mathrm{triv}$ or $\mathrm{std}$. Then cross-Homs between the three summands vanish and $3=\dim\operatorname{End}(N)=1+1+\dim\operatorname{End}(\mathrm X)$, so as in (1) $\mathrm X$ is irreducible with $\operatorname{End}(\mathrm X)=\R\,\mathrm{id}$, and $\mathrm X\not\cong\mathrm{triv},\mathrm{std}$ (otherwise those multiplicities would exceed one). Its dimension is $\binom m2-1-(m-1)=m(m-3)/2$. For $m=3$ there is no orbit with $\abs{A\cap B}=0$, so $\dim\operatorname{End}(N)=2$ and the same argument yields $N=\mathrm{triv}\oplus\mathrm{std}$ (dimensions: $3=1+2$).
:::

:::{prf:lemma} isotypic decomposition of $V_{m,2}$
:label: lem:sol-frd2-decomposition
For $m\ge3$, as $S_m$-modules,

```{math}
:label: eq:sol-frd2-isotypic
V_{m,2}\;\cong\;
\mathrm{triv}\ \oplus\ \mathrm{std}\otimes\R^2\ \oplus\ \mathrm X,
\qquad
\dim V_{m,2}=\frac{(m-1)(m+2)}2,
```

where the $\mathrm X$-summand is absent when $m=3$. Moreover:

1. the $\mathrm{triv}$-isotypic component is $W_{\rm triv}=\R\,[f_0]$ with $f_0=\sum_kp_k^2$, and $[f_0]\ne0$;

2. the classes $L=[p_1-p_2]$ and $Q=[p_1^2-p_2^2]$ are nonzero, linearly independent, and lie in the $\mathrm{std}$-isotypic component $W_{\rm std}$; they are the images of the common seed vector $v_0=e_1-e_2\in\mathrm{std}$ under the two equivariant maps $T_1:a\mapsto[\textstyle\sum_ia_ip_i]$ and $T_2:a\mapsto[\textstyle\sum_ia_ip_i^2]$, whose images span $W_{\rm std}$;

3. for $m\ge4$, the class $F=[(p_1-p_3)(p_2-p_4)]$ is nonzero and lies in the $\mathrm X$-isotypic component $W_{\mathrm X}$, which it generates.
:::

:::{prf:proof}
*Kernel of the quotient map.* Define the equivariant surjection $\Psi:W_{\rm poly}\to V_{m,2}$, $f\mapsto[f]$. We claim

```{math}
:label: eq:sol-frd2-kernel
\ker\Psi
=\Bigl\{\,b_0\textstyle\sum_ip_i
+\bigl(\textstyle\sum_ip_i-1\bigr)\textstyle\sum_ib_ip_i
\;:\;b_0\in\R,\ b\in\R^m\Bigr\}
\;\cong\;\mathrm{triv}\oplus M
\;\cong\;2\,\mathrm{triv}\oplus\mathrm{std}.
```

Indeed $f\in\ker\Psi$ means $f=c$ $\mu$-a.e. for some $c\in\R$. The support $\Delta_{m-1}$ has nonempty relative interior in the hyperplane $H=\{\sum_ip_i=1\}$, and a polynomial vanishing on a relatively open subset of an affine subspace vanishes on the whole subspace; hence $f-c$ vanishes on $H$. Choosing affine coordinates in which $t=\sum_ip_i-1$ is one coordinate and dividing by $t$ (polynomial division in $t$, degree bookkeeping: $\deg\le2$), we get $f=c+(\sum_ip_i-1)\ell$ with $\ell$ affine, say $\ell=b_0+\sum_ib_ip_i$. Since $f$ has zero constant term, $c=b_0$, which yields exactly the displayed set; conversely every element of that set is $\mu$-a.e. constant (equal to $b_0$). The parametrization $(b_0,b)\mapsto f$ is linear, injective (compare first the quadratic homogeneous part $(\sum_ip_i)(\sum_ib_ip_i)$, which vanishes only if $b=0$ since the polynomial ring is a domain; then $b_0\sum p_i=0$ forces $b_0=0$), and equivariant for the action fixing $b_0$ and permuting $b$. This proves [](#eq:sol-frd2-kernel).

*Multiplicities.* The monomial families $(p_i)$, $(p_i^2)$, $(p_ip_j)_{i<j}$ are linearly independent in the polynomial ring and are permuted by $S_m$ exactly as the bases of $M$, $M$, $N$; hence $W_{\rm poly}\cong M\oplus M\oplus N$, whose isotypic multiplicities are (by [](#lem:sol-frd2-irreducibles)): $\mathrm{triv}$: $3$, $\mathrm{std}$: $3$, $\mathrm X$: $1$ (for $m\ge4$; $\mathrm X$ absent at $m=3$). By (F1) applied to $0\to\ker\Psi\to W_{\rm poly}\to V_{m,2}\to0$ and [](#eq:sol-frd2-kernel), the multiplicities in $V_{m,2}$ are $\mathrm{triv}$: $3-2=1$, $\mathrm{std}$: $3-1=2$, $\mathrm X$: $1-0=1$, and no other irreducible occurs. This is [](#eq:sol-frd2-isotypic); the dimension is $1+2(m-1)+m(m-3)/2=(m-1)(m+2)/2$ (also valid at $m=3$).

*(1).* $[f_0]$ is $S_m$-fixed. It is nonzero: if $f_0\in\ker\Psi$, comparing quadratic homogeneous parts in [](#eq:sol-frd2-kernel) gives $\sum_ip_i^2=(\sum_ip_i)(\sum_ib_ip_i)$; the coefficient of $p_i^2$ forces $b_i=1$ for all $i$, but then the coefficient of $p_1p_2$ on the right is $2\ne0$, a contradiction. Since the $\mathrm{triv}$-multiplicity is one, $W_{\rm triv}=\R[f_0]$.

*(2).* $T_1,T_2$ are restrictions to $\mathrm{std}\subset M$ of the equivariant maps $a\mapsto[\sum a_ip_i]$, $a\mapsto[\sum a_ip_i^2]$, so their images lie in $W_{\rm std}$ by (F2), and $L=T_1v_0$, $Q=T_2v_0$. Linear independence of $L,Q$ in $V_{m,2}$: suppose $aL+bQ\in\ker\Psi$, i.e. $a(p_1-p_2)+b(p_1^2-p_2^2) =b_0\sum_ip_i+(\sum_ip_i-1)\sum_ib_ip_i$. Quadratic parts: $b(p_1^2-p_2^2)=(\sum_ip_i)(\sum_ib_ip_i)$; the $p_i^2$ coefficients give $b_1=b$, $b_2=-b$, $b_\ell=0$ ($\ell\ge3$), and then the $p_1p_3$ coefficient (using $m\ge3$) gives $0=b_1+b_3=b$, so $b=0$ and $b\equiv0$. The linear part then reads $a(p_1-p_2)=b_0\sum_ip_i$, forcing $a=b_0=-a$, i.e.\ $a=0$. In particular $L,Q\ne0$, so $T_1,T_2\ne0$ and, $\mathrm{std}$ being irreducible, $T_1(\mathrm{std})\cong T_2(\mathrm{std})\cong\mathrm{std}$. The two image submodules are distinct: if $T_1(\mathrm{std})=T_2(\mathrm{std})=:U$, then $T_1,T_2\in\operatorname{Hom}(\mathrm{std},U)$, a one-dimensional space by (F4)–(F5) (as $U\cong\mathrm{std}$), so $T_2=cT_1$ and $Q=cL$, contradicting independence. Distinct irreducible submodules intersect in $0$, so $T_1(\mathrm{std})\oplus T_2(\mathrm{std})\subseteq W_{\rm std}$ has dimension $2(m-1)=\dim W_{\rm std}$; hence the images span $W_{\rm std}$.

*(3).* Let $m\ge4$ and let $\psi:N\to V_{m,2}$ be the equivariant map $x_{ij}\mapsto[p_ip_j]$. Consider

$$
v=x_{12}-x_{23}-x_{14}+x_{34}\in N,
\qquad
\psi(v)=[p_1p_2-p_2p_3-p_1p_4+p_3p_4]=[(p_1-p_3)(p_2-p_4)]=F.
$$

We check $v\in W_{\mathrm X}(N)$. With the standard (invariant) inner product on $N$, the isotypic components of $N$ are mutually orthogonal. The $\mathrm{triv}$-component is spanned by $\sum_{i<j}x_{ij}$, and the $\mathrm{std}$-component lies in the image of the equivariant map $A:M\to N$, $e_k\mapsto u_k:=\sum_{\ell\ne k}x_{k\ell}$ (indeed $A(\mathrm{std})\ne0$ because $u_1-u_2$ has coefficient $1$ on $x_{13}$, and the $\mathrm{std}$-multiplicity of $N$ is one, so $W_{\rm std}(N)=A(\mathrm{std})$). Now $\langle v,\sum_{i<j}x_{ij}\rangle=1-1-1+1=0$ and, for every $k$, $\langle v,u_k\rangle=0$: for $k=1$ the pairs of $v$ containing $1$ are $x_{12}$ ($+$) and $x_{14}$ ($-$); for $k=2$: $x_{12}$ ($+$), $x_{23}$ ($-$); for $k=3$: $x_{23}$ ($-$), $x_{34}$ ($+$); for $k=4$: $x_{14}$ ($-$), $x_{34}$ ($+$); for $k\ge5$: none. Hence $v\perp W_{\rm triv}(N)\oplus W_{\rm std}(N)$, i.e.\ $v\in W_{\mathrm X}(N)$. By (F2), $F=\psi(v)\in W_{\mathrm X}(V_{m,2})$. Finally $F\ne0$: if $(p_1-p_3)(p_2-p_4)\in\ker\Psi$, comparing quadratic parts with [](#eq:sol-frd2-kernel) gives $(p_1-p_3)(p_2-p_4)=(\sum_ip_i)(\sum_ib_ip_i)$; the left side has no $p_i^2$ terms, so all $b_i=0$, but the left side has $p_1p_2$-coefficient $1$, a contradiction. Since $W_{\mathrm X}$ has multiplicity one and $\psi|_{W_{\mathrm X}(N)}$ is injective (its restriction to the irreducible $W_{\mathrm X}(N)$ is nonzero), $F$ generates $W_{\mathrm X}$ as a module.
:::

:::{prf:lemma} invariant pencil reduction
:label: lem:sol-frd2-reduction
Let $V$ be a module with invariant symmetric bilinear forms $B$ (arbitrary) and $G$ (positive definite), and let $V=\bigoplus_EW_E$ be its isotypic decomposition over pairwise non-isomorphic irreducibles $E$ with $\operatorname{End}(E)=\R\,\mathrm{id}$. Then:

1. $B(W_E,W_{E'})=0$ for $E\not\cong E'$; hence $B$ is positive semidefinite (resp. definite) on $V$ if and only if it is so on each $W_E$.

2. Suppose $W_E$ is spanned by the images of equivariant maps $T_1,\dots,T_k:E\to V$ that are linearly independent in $\operatorname{Hom}_{S_m}(E,V)$, and fix $0\ne v_0\in E$. Then the map $\Phi:E\otimes\R^k\to W_E$, $u\otimes\varepsilon_a\mapsto T_au$, is an isomorphism, and there is a symmetric $k\times k$ matrix $\widehat B$ with

   ```{math}
   :label: eq:sol-frd2-tensor-form
   B(T_au,T_bu')=\widehat B_{ab}\,J_E(u,u')
   \qquad(u,u'\in E,\ 1\le a,b\le k),
   ```

   where $J_E$ is a fixed invariant inner product on $E$. Consequently $B$ is positive semidefinite (resp. definite) on $W_E$ if and only if the $k\times k$ Gram matrix $\bigl(B(T_av_0,T_bv_0)\bigr)_{a,b}=J_E(v_0,v_0)\,\widehat B$ is positive semidefinite (resp. definite).
:::

:::{prf:proof}
(1) The invariant form $B$ and an invariant inner product on $W_{E'}$ induce an equivariant map $W_E\to W_{E'}^*\cong W_{E'}$. By (F2) and Schur, every equivariant map from an $E$-isotypic to an $E'$-isotypic module is zero when $E\not\cong E'$. Hence $B(W_E,W_{E'})=0$, and $B$ decomposes as the orthogonal (with respect to the decomposition) sum of its restrictions.

(2) $\Phi$ is equivariant and surjective (images span), and $\dim(E\otimes\R^k)=k\dim E=\dim W_E$ because the multiplicity of $E$ in $W_E$ equals $\dim\operatorname{Hom}(E,W_E)\ge k$ by linear independence, while surjectivity gives $\le k$; so $\Phi$ is an isomorphism. For fixed $a,b$, the bilinear form $(u,u')\mapsto B(T_au,T_bu')$ on $E$ is invariant, hence by (F5) equals $\widehat B_{ab}J_E(u,u')$ for a unique scalar $\widehat B_{ab}$; symmetry of $B$ and of $J_E$ gives $\widehat B_{ab}=\widehat B_{ba}$. Now for $f=\Phi\bigl(\sum_\alpha u^\alpha\otimes s_\alpha\bigr)$ with $(u^\alpha)_\alpha$ a $J_E$-orthonormal basis of $E$ and $s_\alpha\in\R^k$,

```{math}
:label: eq:sol-frd2-tensor-sum
B(f,f)
=\sum_{\alpha,\gamma}\sum_{a,b}
s_\alpha^a s_\gamma^b\,B(T_au^\alpha,T_bu^\gamma)
=\sum_{\alpha,\gamma}J_E(u^\alpha,u^\gamma)\,s_\alpha^T\widehat B\,s_\gamma
=\sum_\alpha s_\alpha^T\widehat B\,s_\alpha.
```

Since every element of $W_E$ is such an $f$ and the vectors $(s_\alpha)_\alpha$ are arbitrary, $B\ge0$ (resp. $>0$) on $W_E$ iff $\widehat B\succeq0$ (resp. $\succ0$), iff the Gram matrix $J_E(v_0,v_0)\widehat B$ is so ($J_E(v_0,v_0)>0$).
:::

## Sector computations

Throughout this subsection $E_{ij}(f,g)$ denotes the pair energy [](#eq:sol-frd2-pair-energy) and we tabulate the coefficients $(\beta,\gamma)$ of [](#lem:sol-frd2-pair) for each seed and each pair type; pairs not listed have $\beta=\gamma=0$. Recall [](#eq:sol-frd2-small-moments) and $D_2=m(m+1)$, $D_3=D_2(m+2)$, $D_4=D_3(m+3)$.

:::{prf:lemma} trivial sector
:label: lem:sol-frd2-trivial
With $f_0=\sum_kp_k^2$,

```{math}
:label: eq:sol-frd2-trivial
K(f_0,f_0)=\frac{4(m-1)}{5m^2(m+1)^2},
\qquad
G(f_0,f_0)=\frac{4(m-1)}{(m+1)^2(m+2)(m+3)},
\qquad
\frac{K(f_0,f_0)}{G(f_0,f_0)}=\frac{(m+2)(m+3)}{5m^2}.
```

Moreover $[f_0]=\tfrac1{m(m+1)}\,[\abs X^2-(m-1)]$ in $V_{m,2}$.
:::

:::{prf:proof}
For every pair $(i,j)$, by [](#eq:sol-frd2-substitution-table), $p_i^2+p_j^2=\tfrac{s^2}2+\tfrac{\delta^2}2$, so $(\beta,\gamma)=(0,\tfrac12)$ and, by [](#eq:sol-frd2-pair-energy) and [](#eq:sol-frd2-small-moments), $E_{ij}(f_0,f_0)=\tfrac4{45}\cdot\tfrac14\,\E s^2=\tfrac1{45}\cdot\tfrac6{D_2} =\tfrac2{15D_2}$. Summing over the $\binom m2$ pairs and inserting the prefactor of [](#eq:sol-frd2-forms),

$$
K(f_0,f_0)
=\frac{12}{m^2(m+1)}\cdot\frac{m(m-1)}2\cdot\frac2{15\,m(m+1)}
=\frac{4(m-1)}{5m^2(m+1)^2}.
$$

For the variance, [](#lem:sol-frd2-moments) gives $\E f_0=m\cdot\tfrac2{D_2}=\tfrac2{m+1}$ and $\E f_0^2=m\,\E P_1^4+m(m-1)\,\E P_1^2P_2^2 =\tfrac{24m+4m(m-1)}{D_4}=\tfrac{4m(m+5)}{D_4}$, so

$$
G(f_0,f_0)
=\frac{4(m+5)}{(m+1)(m+2)(m+3)}-\frac4{(m+1)^2}
=\frac{4\bigl[(m+5)(m+1)-(m+2)(m+3)\bigr]}{(m+1)^2(m+2)(m+3)}
=\frac{4(m-1)}{(m+1)^2(m+2)(m+3)},
$$

using $(m+5)(m+1)-(m+2)(m+3)=m-1$. The quotient is $(m+2)(m+3)/(5m^2)$. Finally $\abs X^2=m(m+1)\sum_i(p_i-\tfrac1m)^2=m(m+1)\bigl(f_0-\tfrac1m\bigr)$, so $[\abs X^2-(m-1)]=m(m+1)[f_0]$.
:::

:::{prf:lemma} standard sector Gram matrices
:label: lem:sol-frd2-standard
With $L=p_1-p_2$ and $Q=p_1^2-p_2^2$,

```{math}
:label: eq:sol-frd2-standard-gram
\begin{aligned}
K(L,L)&=\frac2{m(m+1)}, &
K(L,Q)&=\frac4{m^2(m+1)}, &
K(Q,Q)&=\frac{8(8m-1)}{5m^3(m+1)^2},\\
G(L,L)&=\frac2{m(m+1)}, &
G(L,Q)&=\frac8{m(m+1)(m+2)}, &
G(Q,Q)&=\frac{40}{m(m+1)(m+2)(m+3)}.
\end{aligned}
```
:::

:::{prf:proof}
*Energies.* The $(\beta,\gamma)$ tables from [](#eq:sol-frd2-substitution-table), with $j$ always denoting an index $\ge3$ distinct from $1,2$:

$$
\begin{array}{l|cc|cc}
\text{pair} & \beta_L & \gamma_L & \beta_Q & \gamma_Q\\\hline
(1,2) & 1 & 0 & s & 0\\
(1,j) & \tfrac12 & 0 & \tfrac s2 & \tfrac14\\
(2,j) & -\tfrac12 & 0 & -\tfrac s2 & -\tfrac14
\end{array}
$$

(For $(1,j)$: $L=\tfrac{s+\delta}2-p_2$ and $Q=\tfrac{s^2}4+\tfrac s2\delta+\tfrac{\delta^2}4-p_2^2$; for $(2,j)$, with $\delta=p_2-p_j$: $L=p_1-\tfrac{s+\delta}2$, $Q=p_1^2-\tfrac{s^2}4-\tfrac s2\delta-\tfrac{\delta^2}4$; for $(1,2)$: $L=\delta$, $Q=s\delta$.) By [](#eq:sol-frd2-pair-energy)–[](#eq:sol-frd2-small-moments):

$$
\begin{aligned}
E_{12}(L,L)&=\tfrac13, &
E_{1j}(L,L)=E_{2j}(L,L)&=\tfrac1{12},\\
E_{12}(L,Q)&=\tfrac13\E s=\tfrac2{3m}, &
E_{1j}(L,Q)=E_{2j}(L,Q)&=\tfrac13\cdot\tfrac{\E s}4=\tfrac1{6m},\\
E_{12}(Q,Q)&=\tfrac13\E s^2=\tfrac2{D_2}, &
E_{1j}(Q,Q)=E_{2j}(Q,Q)
&=\tfrac13\cdot\tfrac{\E s^2}4+\tfrac4{45}\cdot\tfrac{\E s^2}{16}
=\tfrac{16}{180}\,\E s^2=\tfrac8{15D_2}.
\end{aligned}
$$

There are $2(m-2)$ pairs of the types $(1,j),(2,j)$, so

$$
\begin{aligned}
\sum_{i<j}E_{ij}(L,L)&=\tfrac13+\tfrac{2(m-2)}{12}=\tfrac m6,\\
\sum_{i<j}E_{ij}(L,Q)&=\tfrac2{3m}+\tfrac{2(m-2)}{6m}=\tfrac{2+(m-2)}{3m}
=\tfrac13,\\
\sum_{i<j}E_{ij}(Q,Q)&=\tfrac2{D_2}+\tfrac{16(m-2)}{15D_2}
=\tfrac{2(8m-1)}{15D_2}.
\end{aligned}
$$

Multiplying by $12/(m^2(m+1))$ gives the three $K$-entries in [](#eq:sol-frd2-standard-gram).

*Variances.* By symmetry $\E L=\E Q=0$, so, by [](#lem:sol-frd2-moments),

$$
\begin{aligned}
G(L,L)&=\E(P_1-P_2)^2=\tfrac2{D_2},\\
G(L,Q)&=\E\bigl[(P_1-P_2)(P_1^2-P_2^2)\bigr]
=\E\bigl[P_1^3+P_2^3-P_1P_2(P_1+P_2)\bigr]
=\tfrac{12-4}{D_3}=\tfrac8{D_3},\\
G(Q,Q)&=\E(P_1^2-P_2^2)^2
=2\,\E P_1^4-2\,\E P_1^2P_2^2=\tfrac{48-8}{D_4}=\tfrac{40}{D_4}.
\end{aligned}
$$
:::

:::{prf:lemma} two-row sector, $m\ge4$
:label: lem:sol-frd2-tworow
With $F=(p_1-p_3)(p_2-p_4)$,

```{math}
:label: eq:sol-frd2-tworow
K(F,F)=\frac{8(5m-4)}{5m^3(m+1)^2},
\qquad
G(F,F)=\frac4{m(m+1)(m+2)(m+3)},
\qquad
\frac{K(F,F)}{G(F,F)}
=\frac{2(5m-4)(m+2)(m+3)}{5m^2(m+1)}.
```
:::

:::{prf:proof}
*Energy.* The $(\beta,\gamma)$ table, computed from [](#eq:sol-frd2-substitution-table) (here $j\ge5$; in each row $\delta=p_i-p_j$ for the listed pair $(i,j)$, $i<j$):

$$
\begin{array}{l|cc|l}
\text{pair} & \beta_F & \gamma_F & \text{derivation}\\\hline
(1,3) & p_2-p_4 & 0 & F=\delta\,(p_2-p_4)\\
(2,4) & p_1-p_3 & 0 & F=(p_1-p_3)\,\delta\\
(1,2) & \tfrac{p_3-p_4}2 & -\tfrac14 &
F=\bigl(\tfrac{s+\delta}2-p_3\bigr)\bigl(\tfrac{s-\delta}2-p_4\bigr)\\
(3,4) & \tfrac{p_1-p_2}2 & -\tfrac14 &
F=\bigl(p_1-\tfrac{s+\delta}2\bigr)\bigl(p_2-\tfrac{s-\delta}2\bigr)\\
(1,4) & \tfrac{p_2-p_3}2 & \tfrac14 &
F=\bigl(\tfrac{s+\delta}2-p_3\bigr)\bigl(p_2-\tfrac{s-\delta}2\bigr)\\
(2,3) & \tfrac{p_1-p_4}2 & \tfrac14 &
F=\bigl(p_1-\tfrac{s-\delta}2\bigr)\bigl(\tfrac{s+\delta}2-p_4\bigr)\\
(1,j) & \tfrac{p_2-p_4}2 & 0 & F=\bigl(\tfrac{s+\delta}2-p_3\bigr)(p_2-p_4)\\
(2,j) & \tfrac{p_1-p_3}2 & 0 & \\
(3,j) & -\tfrac{p_2-p_4}2 & 0 & \\
(4,j) & -\tfrac{p_1-p_3}2 & 0 &
\end{array}
$$

For instance, for the pair $(1,2)$: $F=\bigl[(\tfrac s2-p_3)+\tfrac\delta2\bigr] \bigl[(\tfrac s2-p_4)-\tfrac\delta2\bigr] =\alpha+\tfrac{p_3-p_4}2\,\delta-\tfrac14\,\delta^2$ with $\alpha$ $\mathcal F_{12}$-measurable; the rows $(3,4)$, $(1,4)$, $(2,3)$ are identical expansions. By [](#eq:sol-frd2-pair-energy)–[](#eq:sol-frd2-small-moments),

$$
\begin{aligned}
E_{13}(F,F)=E_{24}(F,F)
&=\tfrac13\,\E(P_2-P_4)^2=\tfrac2{3D_2},\\
E_{12}(F,F)=E_{34}(F,F)=E_{14}(F,F)=E_{23}(F,F)
&=\tfrac13\cdot\tfrac{\E(P_3-P_4)^2}4+\tfrac4{45}\cdot\tfrac{\E s^2}{16}
=\tfrac1{6D_2}+\tfrac1{30D_2}=\tfrac1{5D_2},\\
E_{ij}(F,F)\ \ (i\in\{1,2,3,4\},\ j\ge5)
&=\tfrac13\cdot\tfrac{\E(P_a-P_b)^2}4=\tfrac1{6D_2}
\qquad(4(m-4)\text{ pairs}).
\end{aligned}
$$

Hence

$$
\sum_{i<j}E_{ij}(F,F)
=\frac1{D_2}\Bigl[\frac43+\frac45+\frac{4(m-4)}6\Bigr]
=\frac1{D_2}\cdot\frac{20+12+10(m-4)}{15}
=\frac{2(5m-4)}{15\,D_2},
$$

and $K(F,F)=\tfrac{12}{m^2(m+1)}\cdot\tfrac{2(5m-4)}{15m(m+1)} =\tfrac{8(5m-4)}{5m^3(m+1)^2}$.

*Variance.* $\E F=\E P_1P_2-\E P_1P_4-\E P_2P_3+\E P_3P_4=0$, and expanding $F^2=(p_1^2-2p_1p_3+p_3^2)(p_2^2-2p_2p_4+p_4^2)$ termwise with [](#lem:sol-frd2-moments) (all four indices distinct),

$$
\E F^2
=\frac{4\cdot4-8\cdot2+4\cdot1}{D_4}
=\frac4{D_4},
$$

the three groups being: the four square–square products, each with $\E P_a^2P_b^2=4/D_4$, totalling $16/D_4$; the four products of a square with a $-2p_bp_c$ factor, each contributing $-2\,\E P_a^2P_bP_c=-4/D_4$, totalling $-16/D_4$; and the single product $(-2p_1p_3)(-2p_2p_4)$, contributing $4\,\E P_1P_2P_3P_4=4/D_4$. The quotient follows by $G(F,F)=\E F^2$ and $D_4=m(m+1)(m+2)(m+3)$.
:::

## Proof of [](#thm:sol-fiber-root-degree-two)

:::{prf:proof}
Write $\lambda^*=(m+2)(m+3)/(5m^2)$ and let $\Phi=K-\lambda^*G$, an $S_m$-invariant symmetric bilinear form on $V_{m,2}$ ([](#lem:sol-frd2-pair)). By [](#lem:sol-frd2-decomposition) and [](#lem:sol-frd2-reduction)(1),

$$
\Phi(f,f)=\Phi(f_{\rm triv},f_{\rm triv})
+\Phi(f_{\rm std},f_{\rm std})+\Phi(f_{\mathrm X},f_{\mathrm X})
$$

for the isotypic components of any $f\in V_{m,2}$ (the $\mathrm X$-term absent at $m=3$). We treat the three sectors.

*Trivial sector.* $W_{\rm triv}=\R[f_0]$ and, by [](#lem:sol-frd2-trivial), $K(f_0,f_0)=\lambda^*G(f_0,f_0)$, i.e. $\Phi\equiv0$ on $W_{\rm triv}$, with $G(f_0,f_0)>0$.

*Standard sector.* Apply [](#lem:sol-frd2-reduction)(2) with $E=\mathrm{std}$, $k=2$, the maps $T_1,T_2$ and seed $v_0=e_1-e_2$ of [](#lem:sol-frd2-decomposition)(2) (linearly independent in $\operatorname{Hom}$, since $c_1T_1+c_2T_2=0$ evaluated at $v_0$ gives $c_1L+c_2Q=0$, hence $c_1=c_2=0$). Positive definiteness of $\Phi$ on $W_{\rm std}$ is therefore equivalent to positive definiteness of the $2\times2$ Gram matrix of $(L,Q)$ under $\Phi$. Multiplying the entries of [](#eq:sol-frd2-standard-gram) by the common positive factor $m(m+1)/2$ yields the normalized matrices

$$
\widetilde K=
\begin{pmatrix}
1 & \tfrac2m\\
\tfrac2m & \tfrac{4(8m-1)}{5m^2(m+1)}
\end{pmatrix},
\qquad
\widetilde G=
\begin{pmatrix}
1 & \tfrac4{m+2}\\
\tfrac4{m+2} & \tfrac{20}{(m+2)(m+3)}
\end{pmatrix},
$$

and a direct computation gives

$$
\begin{aligned}
(\widetilde K-\lambda^*\widetilde G)_{11}
&=1-\frac{(m+2)(m+3)}{5m^2}
=\frac{4m^2-5m-6}{5m^2}=\frac{(4m+3)(m-2)}{5m^2},\\
(\widetilde K-\lambda^*\widetilde G)_{12}
&=\frac2m-\frac{4(m+3)}{5m^2}
=\frac{10m-4m-12}{5m^2}=\frac{6(m-2)}{5m^2},\\
(\widetilde K-\lambda^*\widetilde G)_{22}
&=\frac{4(8m-1)}{5m^2(m+1)}-\frac4{m^2}
=\frac{4(8m-1)-20(m+1)}{5m^2(m+1)}=\frac{12(m-2)}{5m^2(m+1)},
\end{aligned}
$$

that is,

```{math}
:label: eq:sol-frd2-std-psd
5m^2\,(\widetilde K-\lambda^*\widetilde G)
=(m-2)
\begin{pmatrix}
4m+3 & 6\\
6 & \tfrac{12}{m+1}
\end{pmatrix}.
```

For $m\ge3$ the factor $m-2$ is positive, the diagonal entries are positive, and the determinant of the bracketed matrix is $\tfrac{12(4m+3)}{m+1}-36=\tfrac{12(4m+3)-36(m+1)}{m+1}=\tfrac{12m}{m+1}>0$. Hence $\Phi$ is positive definite on $W_{\rm std}$: $\Phi(f_{\rm std},f_{\rm std})>0$ whenever $f_{\rm std}\ne0$.

*Two-row sector ($m\ge4$).* $W_{\mathrm X}$ has multiplicity one and is generated by $F$ ([](#lem:sol-frd2-decomposition)(3)), so [](#lem:sol-frd2-reduction)(2) with $k=1$ reduces positivity on $W_{\mathrm X}$ to the sign of the scalar $\Phi(F,F)$. By [](#lem:sol-frd2-tworow),

$$
\frac{K(F,F)}{G(F,F)}
=\frac{2(5m-4)}{m+1}\,\lambda^*
=\lambda^*+\frac{9(m-1)}{m+1}\,\lambda^*
>\lambda^*,
$$

since $2(5m-4)-(m+1)=9(m-1)>0$. Hence $\Phi(F,F)=G(F,F)\bigl(\tfrac{K(F,F)}{G(F,F)}-\lambda^*\bigr)>0$ and $\Phi$ is positive definite on $W_{\mathrm X}$.

*Assembly.* For every $f\in V_{m,2}$, $\Phi(f,f)\ge0$, i.e. $K(f,f)\ge\lambda^*G(f,f)$, with equality if and only if $f_{\rm std}=0$ and $f_{\mathrm X}=0$, i.e. $f\in W_{\rm triv}=\R[f_0]$. Since $K(f_0,f_0)=\lambda^*G(f_0,f_0)$ with $G(f_0,f_0)>0$, the minimum [](#eq:sol-frd2-lmin) equals $\lambda^*$ and is attained exactly on $\R[f_0]=\R[\abs X^2-(m-1)]$ ([](#lem:sol-frd2-trivial)). Finally $(m+2)(m+3)>m^2$ gives $\lambda^*>\tfrac15$ for all $m$, and $\lambda^*\to\tfrac15$.
:::

## Proof of [](#cor:sol-frd2-no-degree-two-refuter)

:::{prf:proof}
All statements are conditional on the identification [](#eq:sol-frd2-root-identification), certified in `solutions/conditional-fiber-frame-structure.md`: the root frame $\rho_{\rm root}$ is an admissible even frame, and for every $f$ in the maximal form domain (in particular for every polynomial) the root conditional-fiber form equals the pair-redistribution expression [](#eq:sol-frd2-forms).

*(1).* Let $(c_r,w_r,M,\eps)$ be a degree-$2$ dual certificate [](#eq:sol-frd2-certificate). Apply the direction bound in [](#eq:sol-frd2-certificate) at the $m(m-1)$ atoms of $\rho_{\rm root}$ and average:

$$
\sum_rw_r\,K(c_r,c_r)
=(m-1)\int\sum_rw_r\,\qJac_\theta[c_r]\dd\rho_{\rm root}(\theta)
\le(m-1)\int\theta^TM\theta\dd\rho_{\rm root}(\theta)
=\Tr\Bigl(M\,(m-1)\!\int\theta\theta^T\dd\rho_{\rm root}\Bigr)
=\Tr M\le\eps,
$$

using the frame identity $(m-1)\int\theta\theta^T\dd\rho_{\rm root}=I_{H_0}$ and $M$ symmetric on $H_0$. On the other hand, by [](#thm:sol-fiber-root-degree-two), $K(c_r,c_r)\ge\lambda^*G(c_r,c_r)$ for every $r$, so

$$
\eps\ \ge\ \sum_rw_r\,K(c_r,c_r)
\ \ge\ \lambda^*\sum_rw_r\,G(c_r,c_r)=\lambda^*
=\frac{(m+2)(m+3)}{5m^2}>\frac15 .
$$

*(2).* Immediate from (1): every degree-$2$ certificate objective exceeds $\tfrac15$ uniformly in $m\ge3$, so no sequence $\eps_m\to0$ exists at $k=2$. Within the candidate framework, in which a fixed-degree dual refuter is exactly such a certificate sequence, any polynomial dual refutation must therefore use degree $k\ge3$.

*(3).* For any admissible $\rho$ whose averaged form $A_\rho$ is defined on $V_{m,2}$, the supremum defining $\Lambda_{m,2}$ dominates the value at $\rho=\rho_{\rm root}$, and by [](#eq:sol-frd2-root-identification) and [](#thm:sol-fiber-root-degree-two) that value is $\lmin(K,G)|_{V_{m,2}}=\lambda^*$.
:::

## Remarks, non-claims, and audit

:::{prf:remark} agreement with the recorded exact rational artifacts
:label: rem:sol-frd2-artifacts
Two exact computations in rational arithmetic, kept in the project's run records, give the degree-two root-frame pencil minimum at $m=3,4,5$ as $2/3$, $21/40$, $56/125$ respectively, and record the radial quotient anchor $(m+2)(m+3)/(5m^2)$ exactly for every computed $m\le15$. These values agree with the closed form [](#eq:sol-frd2-main): $(5\cdot6)/45=2/3$, $(6\cdot7)/80=21/40$, $(7\cdot8)/125=56/125$. Per repository constraint, these artifacts are directional research evidence only; no step of the proofs above uses them, and this agreement certifies nothing.
:::

:::{prf:remark} unclosed steps
:label: rem:sol-frd2-unclosed
None. [](#thm:sol-fiber-root-degree-two) is unconditional; every step is finite-dimensional linear algebra, elementary representation theory of $S_m$ (proved from facts (F1)–(F5), themselves proved or classical with one-line arguments), and exact Dirichlet moments ([](#lem:sol-frd2-moments), whose proof invokes the classical Gamma–Dirichlet factorization: the normalized vector of i.i.d. standard exponentials is $\Dir(1,\dots,1)$ and independent of their sum). [](#cor:sol-frd2-no-degree-two-refuter) is conditional exactly on the hypothesis stated in its preamble, namely the certified identification [](#eq:sol-frd2-root-identification) (nodes *lem:conditional-fiber-form* and *prop:conditional-fiber-root-obstruction*, both `checked_by: agent` with a persisted review), together with the candidate status of the $\Lambda_{m,k}$/dual-certificate framework itself.
:::

:::{prf:remark} explicit non-claims
:label: rem:sol-frd2-nonclaims
This dossier does *not* claim: any upper bound on $\Lambda_{m,2}$ or on any all-frame quantity; anything about $\Lambda_{m,k}$ or root-frame pencils for $k\ge3$; anything about non-polynomial tests — indeed the certified vertex-cap obstruction ([](#prop:conditional-fiber-root-obstruction)) shows the *full $L^2$* root-frame gap is $O(m^{-2})$, so the degree-two floor [](#eq:sol-frd2-main) genuinely does not extend beyond the polynomial quotient; any optimality of the root orbit among admissible frames; any answer to [](#conj:conditional-fiber-frame); and nothing about KLS.
:::

**Obstructions respected.** The candidate node carries no `bounded_by` edge. Consistency checks against the neighboring certified and imported obstructions: (i) *prop:conditional-fiber-root-obstruction* (root-frame $L^2$ gap $O(m^{-2})$ via a vertex-cap indicator) is compatible with [](#eq:sol-frd2-main) because the cap indicator is not a polynomial of degree two; the two statements jointly prove that any test exhibiting the root-frame collapse must leave $V_{m,2}$, which is precisely the content of [](#cor:sol-frd2-no-degree-two-refuter)(2) for the dual channel. (ii) *prop:sasada-negative-exchange* (imported negative-rate exchange upper bound $48/[m(m+1)]$ for the $L^2$ gap) is compatible for the same reason. (iii) The six route-level obstruction nodes (*rem:two-tail-slice-bounds*, *rem:projection-ceiling*, *rem:crude-insufficient*, *rem:relative-ceiling*, *rem:profile-circularity*, *rem:single-coordinate-cuts*) fence Eldan-localization proof shapes; no stochastic localization, projection summation, bootstrap, isoperimetric localization, or rank-one inference occurs here. No numerical output justifies any step.
