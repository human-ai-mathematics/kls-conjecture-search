---
---

# BKL analytic foundations and the full tilt criterion reconstruction

## Question examined

Mission: reconstruct the analytic and criterion parts of
arXiv:2610.05474v1, Sections 2--3, for the import of BKL into
the proof of [](#conj:kls), including an exact comparison with the
Appell coefficients already used here. Starting lens: **prove**.

Author identity: plan_import (researcher), unknown, 2026-10-06.
The model identifier was not recorded. This is a researcher's
reconstruction and handoff, not a review or certification.

Nodes engaged: [](#def:bkl-tilt-cumulants),
[](#lem:bkl-analytic-foundations),
[](#lem:bkl-tensor-symmetrization),
[](#thm:bkl-tilt-criterion),
[](#prop:bkl-tilt-appell-duality),
[](#lem:sz-analytic-foundations),
[](#thm:sz-polynomial-variance).
The source is [BKL v1](https://arxiv.org/html/2610.05474v1);
its criterion is reconstructed rather than replaced by the existing
[](#prop:sz-exponential-coefficients-equivalence).

## What we learned

*Established as written arguments, not certified.*
Two dossiers have been added:

- [Analytic and tensor foundations](../../solutions/bkl-analytic-foundations.md)
  contains the polynomial-growth inverse-operator argument, the
  eigenfunction growth argument, regular approximation with all
  polynomial moments, and the tensor incidence identity.
- [Tilt criterion and Appell duality](../../solutions/bkl-tilt-criterion.md)
  contains the entire normalized inverse-gradient construction,
  Bochner defects, approximate symmetrization, Taylor transfer,
  doubling estimate, finite dyadic contradiction and operator duality.

The analytic proof uses the already certified spectral/graph-core
construction and scalar stability of [](#lem:sz-analytic-foundations).
It separately establishes the stronger polynomial-growth properties
needed in the BKL regular class. For the eigenfunction a weighted
weak barrier for $f/(1+|x|^2)^m$ avoids assuming decay of its
Schrödinger transform at infinity. For approximation, conditioning
on growing balls precedes Gaussian convolution and a quadratic
potential perturbation; the compact intermediate support bounds
every posterior cumulant of fixed order and hence the required
potential derivatives. A diagonal choice preserves every polynomial
moment.

The criterion proof keeps its premise local to one regular measure
and uniform in degree and test. It uses a finite exit index and
a finite dyadic sum. It does not pass inverse operators or
eigenfunctions through an approximation limit.
The explicit doubling constant in the dossier is $C_0=2^{17}$;
the resulting universal Poincaré bound is
$C_P\le100C_0^2R^2$. These constants follow from the displayed
analytic inequalities; no numerical experiment is used.

The duality is stated for all full-dimensional log-concave laws.
Exponential integrability near zero justifies differentiation
against an arbitrary $L^2$ test. The adjoint of
$T\mapsto P_d^\mu[T]/d!$ is precisely
$f\mapsto\mathcal T_df$, proving equality of operator norms.
The polynomial variance estimate itself is not used; its Appell
normalization is the interface reused from the previous corpus.

## What resists

Independent mathematical review remains necessary. No author
verdict is supplied, no proof record has been created by this
researcher, and no mathematical status has been changed.
The new criterion is an implication; the cumulant estimate and
suspension that supply its premise belong to other dossiers.

No new bounded-by edge is proposed. The existing projection
warning is addressed by use of the full tensor space.
The relative-covariance ceiling, crude-bootstrap warning and
profile-circularity warning concern conclusions absent from
these dossiers. In particular no CMH, occupation or
trace-upgrade statement follows from this work alone.

## Proposed next step

Launch a fresh-context reviewer, with neither the authoring
conversation nor the author as reviewer, on the two dossiers and
the four corresponding canonical statements. The review should
specifically examine:

1. The weighted weak barrier, local derivative-growth induction
   and precise use of the certified spectral foundations.
2. The strengthened regular approximation with all moments.
3. The combinatorial coefficients in the tensor identity.
4. Zero successors, the finite exit index, tensor-slot ordering
   and the scope of each normalizer bound.
5. The defect multiplicities and telescoping of the dyadic sum.
6. Factorials, mean-zero Appell polynomials and equality of
   operator norms on the full symmetric tensor space.

The proposed statement dependencies are:

- analytic foundations: normalization and SZ analytic foundations;
- tensor symmetrization: normalization only;
- tilt criterion: normalization and both new foundation lemmas;
- duality: normalization and the existing Appell convention.

There are no requested route closures. The original equivalence
remains a separate comparison interface, not a substitute for
the criterion proof written here.
