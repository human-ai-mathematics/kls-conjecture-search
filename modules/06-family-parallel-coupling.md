---
numbering:
  enumerator: "6.%s"
---

(sec:family-coupling)=
# Family 6: parallel coupling of exponential tilts

KLS is now proved, by three different arguments compared in Chapter [](#sec:kls-synthesis); as presented in this manuscript, none of them uses the parallel coupling, the tool behind the thin-shell theorem. This chapter describes what the coupling controls on its own and what it does not give.

**Object followed.** The family of log-affine perturbations of $\mu$, its exponential tilts

```{math}
:label: eq:coupling-tilts
\mu_\theta(\dd x)=\frac{e^{\inner\theta x}\,\mu(\dd x)}{\int e^{\inner\theta y}\,\mu(\dd y)},
\qquad\theta\in\R^n,
```

followed jointly along stochastic localization: the localization processes started from $\mu$ and from its tilts are driven together, so that what one learns about $X$ can be compared across the whole family.

**What it buys.** Control of how the law reacts to a *linear* perturbation, uniformly in the direction of the perturbation. The tilts of [](#eq:coupling-tilts) are the log-affine factor of the measures stochastic localization produces, before its Gaussian factor $e^{-t\abs x^2/2}$ (Chapter [](#sec:family-sl)), and they are the priors of the nonlinear-filtering reading of localization ([](#rem:sl-filtering)): observing $X$ through Gaussian noise turns the prior $\mu$ into a random exponential tilt of its Gaussian-weighted version $e^{-t\abs x^2/2}\mu$. Coupling the processes started from neighboring tilts measures how sensitive the posterior is to the prior along this $n$-parameter family, and that sensitivity is what the radial question asks about. Differentiating at $\theta=0$,

```{math}
:label: eq:coupling-derivative
\frac{\dd}{\dd\theta}\Big|_{\theta=0}\E_{\mu_\theta}g=\Cov_\mu\bigl(g,X\bigr),
```

so, to first order, the tilts probe the correlation of a test function with *linear* functions, and nothing else. By [](#eq:bk-radial), the thin-shell problem reduces to the low spectral mass of exactly those linear functions.

**Sharpest result.** The thin-shell theorem: for every isotropic log-concave $X$ in $\R^n$, $\E(\abs X-\sqrt n)^2\le C$ with $C$ universal [@KlartagLehec2025ThinShell], a preprint (version 2). The coupling is combined there with Guan's covariance technique [@Guan2024], already used in the proof of the slicing conjecture (Section [](#subsec:kls-solved-neighbours)). Along the way the argument controls how many covariance eigenvalues of the localized measure are large, and for how long; these two consequences are recorded in this manuscript as [](#thm:kl-stopped-rank-tail) and [](#thm:kl-integrated-rank-covariance) (Chapter [](#sec:covariance-tech)). The sharp constant, $\Var(\abs X^2)\le8n$, is the later [](#thm:chen-klartag-thin-shell).

**What it does not reach alone.** A coupling for *functional* perturbations $(1+\eps f)\mu$, with a cost controlled by $\int\abs{\nabla f}^2\dd\mu$ rather than by $\abs\theta^2$. Applied to a first eigenfunction $f$, such a coupling would test the slowest mode directly instead of its correlation with the coordinates. The family [](#eq:coupling-tilts) is fixed before the test function is: it has $n$ parameters, and to first order, by [](#eq:coupling-derivative), it sees a test function only through its covariance with linear functions. That is exactly enough for $\abs x^2$, whose derivatives are linear ([](#rem:quadratics-special)), and it says nothing about a first eigenfunction whose gradient is not. The parallel coupling is thus one more instance of the difficulty of Section [](#subsec:kls-adaptive-residue): an estimate uniform over a fixed family, where a spectral argument needs one adapted to the extremal function. The rank estimates it produces count large covariance eigenvalues but do not orient them against a cut or an eigenfunction (the paragraph after [](#thm:kl-integrated-rank-covariance)).

**Where this family meets the alternative mechanisms.** Through its rank estimates only ([](#thm:kl-stopped-rank-tail), [](#thm:kl-integrated-rank-covariance)), which bear on the early-time covariance control of the fixed eigenfunction and of the fixed-cut archive but discharge none of their open estimates. Extending the coupling itself beyond linear tilts is the further direction of Section [](#subsec:atlas-coupling-beyond-tilts); none of the alternative mechanisms carries it, and this manuscript formulates no statement for it.

% Agent note: the coupling-beyond-tilts direction (subsec:atlas-coupling-beyond-tilts) has no ledger node and no approach in the portfolio. The two rank theorems
% are imported from version 2 of the preprint and live in `sec:covariance-tech`.
