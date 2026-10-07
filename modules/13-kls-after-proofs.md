---
numbering:
  enumerator: "13.%s"
---

% Prose only: this chapter holds no labelled statement (owner's decision, 2026-10-06).

(sec:kls-after-proofs)=
# KLS after its proofs

With the three proofs of Chapters [](#sec:bkl-proof), [](#sec:sz-v2-proof) and [](#sec:bk-proof), the statement [](#conj:kls) holds: there is a universal $C$ with $\CP(\mu)\le C$ for every isotropic log-concave probability measure $\mu$, in every dimension. This chapter collects what that statement gives, which constants the three proofs provide, and what is decided about the best constant. It proves nothing new; it is a guide to the theorem as a tool.

(subsec:after-equivalent-forms)=
## Equivalent forms, and the affine change of variables

The isotropic, affine, Cheeger and geometric forms of the theorem are stated in Section [](#subsec:kls-conjecture), with the two-sided comparison [](#eq:cheeger-two-sided) between the Poincaré and Cheeger constants; the geometric form is the one in which Kannan, Lovász and Simonovits asked the question [@KannanLovaszSimonovits1995]. One passage is worth writing out, because it produces a stronger inequality on the way. The affine form [](#eq:kls-affine) follows from the isotropic one by a change of variables. If $\mu$ is full-dimensional with covariance $\Sigma$, write $X=m+\Sigma^{1/2}Y$ with $Y$ isotropic and log-concave; for $f$ on $\R^n$ put $g(y)=f(m+\Sigma^{1/2}y)$. Then $\Var f(X)=\Var g(Y)\le C\,\E\abs{\nabla g(Y)}^2=C\,\E\abs{\Sigma^{1/2}\nabla f(X)}^2\le C\norm\Sigma_\op\E\abs{\nabla f(X)}^2$. A measure supported on a proper affine subspace is treated in that subspace. The middle term is the stronger, affine-invariant form $\Var_\mu f\le C\,\E_\mu\inner{\Sigma\nabla f}{\nabla f}$, whose best constant is the affine Poincaré constant $\CPaff(\mu)$ used in Chapter [](#sec:moment-map-cmh).

(subsec:after-consequences)=
## What follows from it

**Thin shell and slicing.** Applied to $f(x)=\abs x^2$ in isotropic position, the theorem gives $\Var\abs X^2\le4n\,\CP(\mu)\le4Cn$ ([](#eq:kls-implies-thin-shell)), the thin-shell bound; thin shell in turn implies a universal bound on the isotropic constant, the slicing problem [@EldanKlartag2011]. This is the chain [](#eq:kls-implication-chain). Both consequences were proved before KLS, by other means (Section [](#subsec:kls-solved-neighbours)): thin shell by Klartag and Lehec [@KlartagLehec2025ThinShell], with the sharp constant $8n$, attained by products of exponentials, in a preprint of Chen and Klartag [@ChenKlartag2026SharpThinShell]; slicing by Klartag and Lehec [@KlartagLehec2025Slicing], and again by Bizeul [@Bizeul2025SmallBallSlicing]. KLS now gives them a common source, with a constant $4C$ in the thin-shell bound that is not sharp.

**Concentration.** A Poincaré inequality with constant $\CP$ implies exponential concentration for Lipschitz functions: for $f$ $1$-Lipschitz, $\mu(\abs{f-\E_\mu f}\ge t)\le2e^{-ct/\sqrt{\CP}}$ with $c$ universal [@BobkovLedoux1997; @BakryGentilLedoux2014]. With KLS, every $1$-Lipschitz function of an isotropic log-concave vector deviates from its mean by more than $t$ with probability at most $2e^{-c't}$, with $c'$ independent of the dimension. For the Euclidean norm this is the thin-shell statement again, at the level of tails.

**Mixing of the random walks on convex bodies.** The algorithms that sample a convex body or estimate its volume run random walks — the ball walk, hit-and-run — whose mixing is controlled through conductance, and the conductance of these walks is bounded below in terms of the isoperimetric constant of the body. A dimension-free Cheeger constant in isotropic position therefore removes the corresponding factor from those mixing bounds. The arguments and their quantitative forms are surveyed in [@LeeVempala2024; @KLnotes].

(subsec:after-constants)=
## The constants the three proofs give

The constant each proof gives is recorded in the row *Constant obtained* of the table of Section [](#subsec:proofs-compared-table). For the question of the best constant, one fact matters: the BK bound is fully numerical, $\CP\le1+2\cdot10^{16}$ for every isotropic log-concave measure ([](#thm:bk-explicit-poincare)), with inverse Cheeger scale at most $\sqrt{\pi(1+2\cdot10^{16})}$ ([](#cor:bk-cheeger)), while the BKL and SZ v2 reconstructions give universal constants that are not evaluated.

(subsec:after-constant-question)=
## The question of the constant

Write $C_\star$ for the best universal constant: the supremum of $\CP(\mu)/\norm{\Cov\mu}_\op$ over all log-concave $\mu$ in all dimensions, equivalently the supremum of $\CP(\mu)$ over isotropic log-concave $\mu$. The three proofs give $C_\star<\infty$, and BK gives $C_\star\le1+2\cdot10^{16}$. Here is what is decided about its value, and where.

- **$C_\star\ge1$**, by the linear test: $\CP(\mu)\ge\norm{\Cov\mu}_\op$ for every $\mu$, with equality for the Gaussian.
- **$C_\star\ge4$**, by the exponential on the line: for the density $e^{-x}$ on $[0,\infty)$, the functions $e^{ax}$ with $a\to\tfrac12$ give $\CP\ge4\Var$ (Section [](#sec:kls-examples)).
- **On the line, $4$ is exact.** Every one-dimensional log-concave law has $\CP\le4\Var$ [@KannanLovaszSimonovits1995; @cattiaux2018poincare]; [](#thm:cmh-1d) contains this bound.
- **Products stay at $4$.** The Poincaré constant of a product is the largest of those of its factors, so every product of one-dimensional log-concave laws has $\CP\le4\norm{\Cov}_\op$, in every dimension.
- **Dirichlet laws stay at $4$.** Every log-concave Dirichlet law — in particular the uniform measure on a simplex — has $\CPaff\le4$, and so does every linear image, product and convolution of independent such laws ([](#cor:cmh-dirichlet-poincare)). Since $\inner{\Sigma\nabla f}{\nabla f}\le\norm\Sigma_\op\abs{\nabla f}^2$, each of these laws has $\CP\le4\norm{\Cov}_\op$.
- **What would give $4$ everywhere.** By [](#thm:cmh-implies-affine-poincare), $\CPaff(\mu)\le\CMH(\mu)$ with no loss. A universal bound $\CMH\le4$ over all isotropic log-concave measures would therefore give $\CP\le4\norm{\Cov}_\op$ for every log-concave measure, and with the exponential, $C_\star=4$.

So the ratio reaches $4$ on the exponential — as a supremum, since no square-integrable function attains its Poincaré constant — and does not exceed $4$ on the line, on products of one-dimensional log-concave laws, or on log-concave Dirichlet laws and their linear images, products and convolutions. Between $4$ and $1+2\cdot10^{16}$ this manuscript decides nothing: it neither proves $C_\star=4$ nor exhibits a log-concave measure with ratio above $4$, and none of the three proofs gives the upper bound $4$. The moment-Hessian inequality is the one mechanism here aimed at the value $4$; its cheapest necessary test, the linear test, has a sharp form with constant $2$, [](#conj:gate-zero-sharp), which none of the three proofs gives.

(subsec:after-what-next)=
## What comes next

The theorem leaves the mechanisms by which it might be proved otherwise, and the stronger statements they aim at. Chapter [](#sec:frontier-atlas) maps three of them by what each would add to the three proofs: the moment map, a deterministic proof with the constant $4$; the fixed eigenfunction, a localization mechanism that ignores covariance spikes; and conditional fibers, a mechanism resting only on one-dimensional inequalities.
