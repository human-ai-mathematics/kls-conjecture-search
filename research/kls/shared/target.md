# The KLS target — route-agnostic

What every route is trying to prove, and the bridge that ties it to Parts I/II. This file
restates nothing formally: the canonical statements live in `modules/kls/*.tex` (linked by
`\label`) and the logical state lives in the central [`../ledger.yaml`](../ledger.yaml). Math in
LaTeX (`$…$`).

## The conjecture

Kannan–Lovász–Simonovits: there is a universal constant $c>0$ such that **every** isotropic
log-concave probability measure $\mu$ on $\mathbb R^n$ has Cheeger constant $h_\mu\ge c$,
equivalently up to universal constants a dimension-free Poincaré bound. With the Cheeger
normalization used in the manuscript, the direct implication is
$C_P(\mu)\le4h_\mu^{-2}$; the reverse comparison for log-concave measures also carries a
universal factor. Writing
$h^\star_n=\inf\{h_\mu:\mu\text{ isotropic log-concave on }\mathbb R^n\}$
(`eq:hstar-def`), the claim is
$$\inf_n h^\star_n > 0.$$

- **Best known.** Published: $h^\star_n\ge c\,(\log n)^{-1/2}$ (Klartag 2023). Conditional on
  Letwin's July 2026 version-1 preprint (arXiv:2607.24164), the claimed bound is
  $h^\star_n\ge c\,(\log n)^{-1/4}$. A route "wins" only by removing the last
  $\mathrm{polylog}$.
- **Fixed-cut localization posture.** The Eldan route works *by contradiction against a
  near-worst measure* $h_\mu\le(1+\varepsilon)\,h^\star_n$. Within that mechanism, a proposed
  universal-time covariance bound for **every** measure may already be KLS-sufficient; see
  [`lower-bounds.md`](lower-bounds.md) and `obs:relative-ceiling`. This warning does not constrain
  the separate moment-map/spectral and deterministic CMH routes, which target the spectral gap
  through different objects.

## The bridge to Part II (`ab/conj:a1-bis`)

KLS is the **"Tier-$\infty$" boundary** of Part I. The Part II target A1-bis
(`ab/conj:a1-bis`, in `../../ledger.yaml`) is the *structured-posterior* counterpart:
$$C_P(\pi)\ \le\ K\,\lambda_{\max}(\mathrm{Cov}_\pi)\qquad\text{for a useful class of GLM posteriors,}$$
with $K$ universal or mildly geometry-dependent. The **same** bound with a universal $K$ for
**every** isotropic log-concave measure *is* KLS (after isotropic normalization
$\lambda_{\max}(\mathrm{Cov})=1$). So:

- A1-bis is a finite-sum-structured, *checkable* shadow of KLS — numerics can estimate the
  realized $K=C_P^{\text{lower}}/\lambda_{\max}(\mathrm{Cov})$ across GLM instances (the
  `finum` linear-test lower bound, cross-program node `ab/lem:linear-test-lower`).
- The route-neutral terminal `conj:kls` carries `bridges: [ab/conj:a1-bis]` in the ledger;
  the conditional headline theorems are route-specific entry points toward that terminal rather
  than bridge endpoints or unconditional discharges.

This bridge is route-agnostic: it holds whatever proof route eventually establishes the bound.
