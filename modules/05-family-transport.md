---
numbering:
  enumerator: "5.%s"
---

(sec:family-transport)=
# Family 5: transport maps and the entropic barrier

**Object followed.** A map pushing a reference measure — usually a Gaussian, or Wiener measure — onto $\mu$, together with the derivative of that map.

**What it buys.** A reformulation in which KLS becomes a regularity statement about a single transport map rather than a spectral statement about a diffusion. The reformulation is exact and appealing; the difficulty is that the three natural instances each fail in an instructive and different way.

(subsec:transport-caffarelli)=
## Caffarelli

If the target is uniformly more log-concave than a Gaussian, Caffarelli's contraction theorem makes the Brenier map from that Gaussian to $\mu$ $1$-Lipschitz. The Gaussian Poincaré inequality then transfers directly, with no loss.

This settles the strongly log-concave case, the same case already settled by Bakry–Émery for structured families. It cannot cover arbitrary log-concave measures, whose curvature may vanish identically — the uniform measure on a convex body being the extreme instance.

(subsec:transport-brownian)=
## Brownian (Föllmer) transport

The Brownian transport map sends Wiener measure to a target $\mu$ [@MikulincerShenfeld2021BrownianTransport]. A dimension-free estimate on its Malliavin derivative,

```{math}
:label: eq:brownian-derivative
\E\norm{\calD X_1}_\op^2\le C,
```

would give $\Var_\mu f\le C\Lip(f)^2$ for every Lipschitz $f$; Milman's equivalence between Lipschitz concentration and a spectral gap for log-concave measures [@Milman2009Isoperimetric] would then upgrade that to KLS.

:::{warning} No pathwise dimension-free Lipschitz map exists
:label: rem:no-lipschitz-transport
The corresponding *pathwise* statement is false, and cheaply so. A dimension-free Lipschitz map from a Gaussian to every log-concave $\mu$ would transfer the Gaussian logarithmic Sobolev inequality and Gaussian tail decay to $\mu$. Already the one-dimensional exponential law violates both. So [](#eq:brownian-derivative) must be read as an *averaged operator* estimate; the $\E$ and the order of the norm are not cosmetic.
:::

This is the reason the family has not yet produced an independent bound: current estimates on [](#eq:brownian-derivative) are polylogarithmic and largely inherit existing KLS-scale input rather than supplying it. The averaged operator derivative is the plausible target.

(subsec:transport-entropic)=
## The entropic barrier

For a convex body $K$ set

$$
\Lambda(\theta)=\log\int_Ke^{\inner\theta x}\dd x .
$$

Then

```{math}
:label: eq:entropic-hessian
\Hess\Lambda(\theta)=\Cov_{p_\theta}(X),
```

where $p_\theta\propto e^{\inner\theta x}\one_K$, and $D^3\Lambda(\theta)$ is the third-moment tensor of the same exponential tilt [@BubeckEldan2014EntropicBarrier]. The entropic barrier therefore packages exactly the covariance and third-moment geometry that stochastic localization manipulates — [](#eq:entropic-hessian) and [](#eq:sl-covariance-sde) are two descriptions of one object, one indexed by a tilt parameter and one by a time.

The gap is a matter of which contractions are controlled. Ordinary self-concordance controls *scalar* contractions of $D^3\Lambda$, of the form $D^3\Lambda[u,u,u]$. Localization needs *matrix* or Hilbert–Schmidt contractions — precisely the parameter $\kappa_n$ of [](#eq:kappa-def). Letwin's theorem now supplies the latter ([](#prop:letwin-kappa)), which closes this particular mismatch; that estimate alone does not supply the all-functions spectral step. The BKL argument adds all-order cumulants and suspension (Chapter [](#sec:bkl-proof)).

**The precise missing estimate.** The dimension-free averaged bound [](#eq:brownian-derivative) on the expected operator norm of the transport derivative.

**Why it stalls.** [](#rem:no-lipschitz-transport) rules out the pathwise approach, so any argument must work in expectation — and an expected operator norm is not accessible by the pathwise convexity techniques that make Caffarelli's theorem work. Available derivative bounds either lose the alignment between the derivative and the test function, or reuse KLS-scale input and so cannot improve it.

:::{prf:remark} Structured cases where KLS is known
:label: rem:known-cases
Before the general BKL theorem, several structured classes already admitted direct arguments. KLS holds for products by tensorization; for uniformly log-concave measures via Brascamp–Lieb/Bakry–Émery (Section [](#subsec:transport-caffarelli)); for $\ell_p$-balls; and for broad classes of generalized Orlicz balls [@KolesnikovMilman2016OrliczKLS]. For unconditional measures, Mikulincer and Zadik proved a dimension-free bound a few days before the general proofs, by a different route: a spectral analysis of a Dunkl–Langevin operator attached to a transform of the measure [@MikulincerZadik2026Unconditional]. The general BKL result [](#conj:kls), explained in Chapter [](#sec:bkl-proof), also covers every unconditional convex body. These earlier cases remain useful for understanding how additional structure can make the constant explicit.
:::

**Where this family meets the alternative mechanisms.** It enters none of them directly. The nearest open question is the coupling one of the next family, Chapter [](#sec:family-coupling), whose extension beyond linear tilts is described in Section [](#subsec:atlas-coupling-beyond-tilts); no labelled statement of this manuscript formulates it. Transport enters the alternative mechanisms only through the Brascamp–Lieb cap that stochastic localization uses.
% Agent note: the coupling-beyond-tilts direction (subsec:atlas-coupling-beyond-tilts) has no ledger node and no approach in the portfolio.
