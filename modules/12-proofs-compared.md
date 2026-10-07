---
numbering:
  enumerator: "12.%s"
---

(sec:kls-synthesis)=
# The proofs of KLS compared

This chapter compares the three proofs of [](#conj:kls): Bizeul–Klartag–Lehec (BKL), Chapter [](#sec:bkl-proof) [@BizeulKlartagLehec2026KLS]; Song–Zhang, second version (SZ v2), Chapters [](#sec:sz-v2-proof) and [](#sec:sz-v2-blocks) [@SongZhang2026ConstantKLS]; and Balasubramanian–Kasiviswanathan (BK), Chapter [](#sec:bk-proof) [@BalasubramanianKasiviswanathan2026KLS]. Their ideas are sketched in Section [](#sec:kls-conversions). All three control the exponential growth of Appell coefficients; they differ in the closing estimate, the spectral conversion and the constant obtained, and the table below is the reference for these differences.

(subsec:proofs-compared-table)=
## The three proofs side by side

| | Bizeul–Klartag–Lehec | Song–Zhang, second version | Balasubramanian–Kasiviswanathan |
|---|---|---|---|
| **Object estimated** | Cumulants of every order, then tilt averages of arbitrary test functions | The common Appell radius $\mathcal A(\mu)$ ([](#def:sz-v2-common-radius)) | Powers of compatible integration operators, then the coefficients $c_d$ |
| **Decisive estimate** | The factorial cumulant bound [](#thm:bkl-cumulant-bound), uniform in dimension | Summable multiplicative and additive costs at every refinement ([](#prop:sz-v2-summable-budgets)) | A common prefactor for all powers, $\|J^q\|^2\le2B^q$ ([](#cor:bk-integration-powers)) |
| **Closing mechanism** | Suspension encodes an arbitrary test function as one extra coordinate ([](#prop:bkl-suspension)) | Successively refined curvature profiles give bounded coefficient radii | Reverse transfer closes a direct degree induction, $c_d\le10^{8d}/(d+1)^4$ ([](#thm:bk-appell-bound)) |
| **Use of dimension uniformity** | The suspension lives in dimension $nN+1$, with $N\to\infty$ | A coefficient cap must hold for every localized law in the next refinement | Tensor rank and dimension must not weaken the Hodge estimate or the coefficient recurrence |
| **Localization** | Inverse-covariance noise and cumulants in a moving covariance metric | Gaussian localization transfers curvature profiles to coefficient caps | Inverse-covariance noise, covariance tensor bounds from Letwin, and moving Appell variance |
| **Spectral conversion** | The exponential tilt-average criterion [](#thm:bkl-tilt-criterion) | The single conversion $\CP\le2^{85}\mathcal A$ ([](#prop:sz-v2-common-radius)) | $\CP\le1+\|J\|^2$ and a limit in the number of polynomial observations ([](#thm:bk-explicit-poincare)) |
| **Constant obtained** | $\CP\le2CK$; universal $C,K$ are not evaluated here | $\CP\le2^{85}\mathcal A$; the universal bound on $\mathcal A$ is not evaluated here | $\CP\le1+2\cdot10^{16}$, fully numerical |
| **Reusable tools** | Cumulant dynamics, all-order cumulant estimates, suspension | Common-radius conversion, finite inverse-gradient chains, summable refinements | Compatible-tensor Hodge estimate, operator-power bound, reverse coefficient transfer |

(subsec:proofs-compared-shared)=
## Shared coefficients, distinct spectral reductions

The Appell coefficients $c_d(\mu)$ are the normalized sizes of the polynomials adapted to the moments of $\mu$ (Section [](#sec:sz-notation)). The convention is identical in all three arguments. An exponential bound $c_d\le A^d$, uniform in degree, dimension and measure, is equivalent to KLS ([](#prop:sz-exponential-coefficients-equivalence)). This identifies the common conclusion to seek; it does not establish it.

BKL use the spectral criterion isolated by the first version of Song–Zhang, in the exponential form they prove from their own analytic foundations. The norm of their tilt-average operator is exactly $c_d$ ([](#prop:bkl-tilt-appell-duality)). Their cumulant estimate and suspension therefore supply the premise of [](#thm:bkl-tilt-criterion). Song–Zhang v2 retains the polynomial–curvature apparatus of v1, but refines $\mathcal A$ and pays its spectral conversion only once, after all rounds. The earlier curvature transfer [](#thm:sz-curvature-transfer) serves its intermediate dimension-dependent bound, not this last conversion.

BK also obtains exponential coefficients, with a summable degree weight $(d+1)^{-4}$, but its final conversion follows from the compatible integration calculus. For one fixed regular measure of curvature $a>0$, let the observation degree $D$ tend to infinity in [](#cor:bk-integration-powers). The factor $a^{-1/(D+1)}$ tends to one, so $\CP\le1+2R_*^2$, with $R_*=10^8$. Approximation then removes regularity. Thus the common exponential criterion describes what all three achieve; it is not the identical last lemma in each proof.

(subsec:proofs-compared-differences)=
## What separates the arguments

**Cumulants, refinement, or a degree recurrence.** BKL estimate cumulants inductively and use suspension to reach general functions. Song–Zhang v2 instead improves a curvature profile repeatedly, controlling every round's admissibility and making the losses summable. BK closes an induction straight on $c_d$: lower degrees control integrations under curved laws, and localization transfers those integration bounds to degree $d$. For its large-degree step the integration length is $q=\lfloor d/2\rfloor$, while the observation degree is $D=\lfloor\sqrt d\rfloor$. Keeping one prefactor for the whole integration chain is essential; multiplying separate one-step bounds discards the gain.

**What localization transports.** BKL and BK both normalize the noise by the inverse covariance. BKL follows cumulants in a moving metric; BK controls covariance tensor products and the variance of a polynomial whose Appell normalization changes with the law. Song–Zhang uses Gaussian localization to convert curvature profiles to coefficient bounds. A shared noise normalization does not make the objects or estimates interchangeable.

**Where the constants are spent.** The v1 spectral comparison incurred a fixed cost at every round. Song–Zhang v2 makes the radius-refinement costs summable and spends the final conversion once. BKL avoids that refinement altogether. BK's finite observation bound supplies a factor independent of the number of integrations, allowing a direct recurrence with a numerical majorant. The resulting constant is explicit but far from the lower bound $4$ supplied by the exponential law (Chapter [](#sec:kls-after-proofs)).

(subsec:proofs-compared-bk)=
**Two different Hodge comparisons.** BK projects weighted divergence onto compatible symmetric tensor fields for the potential of the original measure. The matrix example in Chapter [](#sec:bk-proof) shows the harmonic-mean curvature left after this projection. The moment-Hessian comparison [](#cor:cmh-hodge-comparison) uses the canonical moment-map Hessian and a different energy. Neither statement identifies the other's hypotheses, so the BK estimate does not settle the moment-Hessian inequality.

(subsec:proofs-provenance)=
## Provenance and dependencies

The three arguments share earlier polynomial and localization ideas. BK's quadratic initialization explicitly uses Letwin's [](#thm:letwin-qcts), and its Appell convention agrees with [](#thm:sz-polynomial-variance). Distinct proofs here means distinct closing arguments, not independence from the earlier literature.

The reconstructed BKL argument uses no SZ v2 estimate or KLS conclusion as an input. The SZ v2 reconstruction uses no BKL cumulant or tilt bound, including their consequence [](#cor:bkl-uniform-conditional-initialization). The BK induction uses neither of those proofs' conclusions nor KLS itself. Reusing the BKL initialization to recover KLS would keep BKL's provenance; it would not supply another argument establishing exponential growth.

The versions and deposit times of BKL and SZ v2 are given in Chapter [](#sec:sz-v2-proof). The BK source is arXiv v1, read in an identical earlier PDF whose Git commit and hash [@BalasubramanianKasiviswanathan2026KLS] records. These bibliographic facts identify the texts reconstructed here without asserting priority.

What KLS itself gives, and the question of its best constant, follow in Chapter [](#sec:kls-after-proofs); what the alternative mechanisms would add to these proofs is in Chapter [](#sec:frontier-atlas).
