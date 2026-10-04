---
---

# One-dimensional CMH identity without an operator inverse

## Question examined

Prove/repair `thm:cmh-1d` in the exact-case component of Route C after
`research/reviews/2026-10-04-cmh-aug25-grouped-exact-cases-revise.md`.
The canonical statement is: “For every centered one-dimensional law for which
the operators above are defined, $\CMH(\mu)=\CP(\mu)/\Var(\mu)$.
In particular every one-dimensional log-concave law satisfies $\mathrm{CMH}(4)$,
and the constant $4$ cannot be lowered.” The operator setup is the
nondegenerate interval law, finite nonzero variance, canonical zero-flux
Stein kernel, and natural closed no-flux forms of `def:cmh`.
The mission also covers the unrestricted one-dimensional specialization in
`thm:cmh-product`. No canonical statement changes.

## What we learned

*Established, awaiting independent review.* The replacement proof in
`solutions/thm-cmh-dirichlet.md` avoids every operator inverse. Compact flux
fields $u=\phi/\rho$ form a graph core for the no-flux adjoint $D_\mu^*$,
since the adjoint of their differential expression is the maximal scalar
derivative. Each such field is exactly attained by the bounded CMH test
$f_\phi(x)=\int_{x_0}^x\phi(t)/(\tau(t)\rho(t))\,dt$.
Thus a finite CMH bound implies coercivity of $D_\mu^*$ on its entire
domain and closed range onto centered $L^2$, yielding the Poincaré bound.
In particular infinite Poincaré constant forces infinite CMH constant.

*Established, awaiting independent review.* If Poincaré is finite, Riesz
representation provides an $L^2$ solution of $D_\mu^*w=\Aop f$ with
norm at most $\sqrt{\CP}\|\Aop f\|_2$. Comparing weak identities on
bounded primitives of compactly supported derivatives proves $w=\tau f'$.
This supplies the reverse inequality for every $f\in\Dom(\Aop)$ and
justifies its numerator without presupposing its finiteness. The proof neither
asserts $\operatorname{Ran}\Aop=L^2_0$ nor uses a spectral gap for $\Aop$.

*Established diagnostic from the review.* For $\rho=c(1+x^2)^{-3}$,
$\tau=(1+x^2)/4$ and $f=h=x$, the ordinary Poisson primitive is
$x/4+x^3/12$ up to a constant and is not in $L^2(\mu)$.
This invalidates the old inverse step, not the theorem. The new argument
never takes that inverse and covers this law in its infinite-constant branch.
For completeness its Poincaré constant is infinite: choose a nonzero smooth
bump $b$ supported in $(1,2)$ and test $b(x/R)$. Its second moment has
order $R^{-5}$, its squared mean has order $R^{-10}$, and its derivative
energy has order $R^{-7}$, by the change of variable $x=Rt$ and elementary
two-sided bounds on $(1+R^2t^2)^{-3}$ for $R\ge1$, $1\le t\le2$.
The variance-to-energy ratio therefore diverges. These are analytic estimates,
not computation.

## What resists

The repaired argument is uncertified. Its domain identifications must be
checked against the canonical phrase “for which the operators above are
defined”: the proof uses the maximal ordinary derivative, the natural weighted
no-flux form, and interior density regularity of that differential-operator
setup, but no additional tail or gap assumption. The compact flux core and
bounded primitive tests make the boundary convention explicit.
No additional defect from the grouped revise report is left intentionally open.
The mirrored manuscript proof still needs its responsible writer's replacement.

There are no `bounded_by` edges on `thm:cmh-1d` or `thm:cmh-product`;
`def:cmh` remains their normalization dependency, with no new `assumes`.
The proof makes no universal CMH, thin-shell, projection, or perturbative claim.
The other nine proofs, including exponential sharpness and the Gamma/Dirichlet
branch, have been preserved apart from an explicit extended-constant sentence
in the product proof.

## Proposed next step

A fresh independent reviewer should examine the complete repaired dossier,
starting with the frozen revise report and testing the compact-flux graph core,
operator-domain membership of $f_\phi$, the closed-range lower bound, the
Riesz upper bound, infinite constants, and the unrestricted product consequence.
Have the manuscript writer synchronize the mirrored proof after stabilization,
without changing the theorem statement. There is no proposed ledger transition
before independent certification.

Repair author identity: `cmh_1d_domain_repair, gpt-6-astra, 2026-10-04`.
Earlier author identities retained from the revise report:
`kls-cmh-normalization, unknown, 2026-08-25`;
`kls_ledger_audit, unknown, 2026-08-25`;
`repair_cmh_hodge_domain_w3, unknown, 2026-08-27`.
