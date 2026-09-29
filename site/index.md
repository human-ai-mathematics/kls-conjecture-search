---
title: Do linear functions see the slowest mode of every convex body?
numbering: false
relies-on:
  conj:kls: {status: open, fingerprint: b34221c5440f365f12cb6529324aed7a62b355236e5a037761de51f02adeab69}
  thm:klartag-logn: {status: proved, fingerprint: 70dd5528111bc813bcfa6750d3afcfcdc31121dbf564fb0681db32265b576b60}
  thm:letwin-qcts: {status: open, fingerprint: 8e2ac0819f46db553fe83a6f3034436816565262316c2e6bde7d81baead1a082}
  thm:cmh-implies-affine-poincare: {status: proved, fingerprint: 96fd21faf9d64d72f98fb884b57bd648952eba813b3c71eba4c32088571bb433}
  thm:cmh-dirichlet: {status: proved, fingerprint: 0950144e400e4a077e8ae82686d149d0a736b6ec651e7c588e4e867146a8db94}
  prop:spectral-sufficiency: {status: proved, fingerprint: fd64938a59bc75857af5ea37fa1553ec3f448a47d6d24f506dbe4dff01507869}
  q:mm-spectral-occupation: {status: open, fingerprint: fd459923a0b85e2a9af9179faa1e1e80bbe2357831a49d986221586cfd268249}
  lem:conditional-fiber-form: {status: proved, fingerprint: f2110f8c5c36056fda52257a3ad145a50f7c460b5bdc6b9ec4146e907db3cec2}
  q:conditional-fiber-frame: {status: open, fingerprint: d73bceb7210a8fa4046d805a649bd44e5e86c16a33aab2f80d14080df3c30423}
  conj:gate-zero-sharp: {status: open, fingerprint: df72819e702a79d3f42c81937662a671d552303846f945cee9c4ada07cce2946}
  prop:weighted-spectator-obstruction: {status: proved, fingerprint: 43186945070f01440b94ed29e452f474290ea070a94c9874921fbc1b8e3329ab}
  q:weighted: {status: refuted, fingerprint: 60cd33f3e512ec8005eea236cdb2dfe8198f8248c0f2236fdfcf0febf02f95fb}
checked: 2026-09-29
---

% stamp: written by check.py --stamp; do not edit
*Last checked against the research record: 2026-09-29.*
% end stamp

A log-concave probability measure $\mu$ on $\mathbb R^n$ — the uniform measure on a convex
body, a Gaussian, any density $e^{-V}$ with $V$ convex — has a Poincaré constant
$C_{\mathrm P}(\mu)$, the best constant in $\operatorname{Var}_\mu f\le C\int|\nabla f|^2\,\mathrm d\mu$.
Linear functions show that it is at least the largest variance of $\mu$ in any direction.
The Kannan–Lovász–Simonovits conjecture (1995) says that, up to a universal constant, it is
at most that:

$$
C_{\mathrm P}(\mu)\;\le\;C\,\|\operatorname{Cov}(\mu)\|_{\mathrm{op}}
\qquad\text{for every log-concave }\mu\text{ in every dimension.}
$$

Equivalently, the cheapest way to cut a convex body into two large pieces is, up to a
universal factor, a hyperplane.

**Where things stand.** The conjecture is open. The best published bound replaces $C$ by
$C\log n$ (Klartag, 2023); a July 2026 preprint, not yet refereed, claims $C\sqrt{\log n}$.
This project has not proved or refuted the conjecture: it has proved a new inequality that
would imply it, together with the first non-product cases where that inequality holds,
reduced the conjecture to two open estimates, and refuted several natural intermediate
statements, none of which bears on the conjecture itself.

## What is proved here

- **A sufficient condition with no randomness in it.** A second-order inequality for the
  Hessian of the moment map implies the Poincaré inequality with the same constant, and it
  holds with constant $4$ on the line, on products and on every log-concave Dirichlet law
  (the simplex included). Constant $4$ in general would prove the conjecture.
- **Two reductions.** The conjecture follows from a source-against-damping estimate for a
  first eigenfunction followed along stochastic localization, and from a spectral gap for a
  resampling process along conditional lines. Both estimates are open.
- **Counterexamples that fence the search.** Estimates weighted by the global covariance
  fail on products of exponentials, because of independent coordinates the cut does not
  see; the natural resampling frame fails on the simplex.

## Open questions

The results page states each open estimate precisely, next to the theorem it would complete:
the eigenfunction estimate ([Theorem D](#site:thm-d)), the choice of a resampling frame
([Theorem E](#site:thm-e)), and the sharp operator bound on the moment-map Hessian
([Theorem C](#site:thm-c)), which would already give a sharp third-moment bound for all
isotropic log-concave measures. No problem has been written up yet as a self-contained card;
[Open problems](open.md) will list them as they are.

## Read further

- [The problem](problem.md): the conjecture, examples computed by hand, the history of the
  bounds, and the obstacle every method meets.
- [Results](results.md): what is proved here — theorems, conditional reductions and
  counterexamples — each with the idea of its proof.
- [Full proofs](proofs.md): the complete written proofs, each checked by a reviewer other
  than its author.
- [About](about.md): how to contribute, and how results are checked.
