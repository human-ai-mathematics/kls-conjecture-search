# The KLS target — route-agnostic

What every route is trying to prove, and the bridge that ties it to Parts I/II. This file
restates nothing formally: the canonical statements live in `modules/kls/*.tex` (linked by
`\label`) and the logical state lives in the route ledgers. Math in LaTeX (`$…$`).

## The conjecture

Kannan–Lovász–Simonovits: there is a universal constant $c>0$ such that **every** isotropic
log-concave probability measure $\mu$ on $\mathbb R^n$ has Cheeger constant $h_\mu\ge c$,
equivalently a dimension-free Poincaré bound $C_P(\mu)\le 1/c^2$. Writing
$h^\star_n=\inf\{h_\mu:\mu\text{ isotropic log-concave on }\mathbb R^n\}$
(`eq:hstar-def`), the claim is
$$\inf_n h^\star_n > 0.$$

- **Best known.** $h^\star_n\ge c\,(\log n)^{-1/2}$ (Klartag 2023; after Chen 2021,
  Klartag–Lehec 2022). A route "wins" only by removing the last $\mathrm{polylog}$.
- **Proof posture (shared).** All current work is *by contradiction against a near-worst
  measure* $h_\mu\le(1+\varepsilon)\,h^\star_n$. A route that needs a bound for **every**
  measure (not just near-worst) is doing something KLS-equivalent — see
  [`lower-bounds.md`](lower-bounds.md) and `obs:relative-ceiling`.

## The bridge to Part II (`ab/conj:a1-bis`)

KLS is the **"Tier-$\infty$" boundary** of Part I. The Part II target A1-bis
(`ab/conj:a1-bis`, in `../../ledger.yaml`) is the *structured-posterior* counterpart:
$$C_P(\pi)\ \le\ K\,\lambda_{\max}(\mathrm{Cov}_\pi)\qquad\text{for a useful class of GLM posteriors,}$$
with $K$ universal or mildly geometry-dependent. The **same** bound with a universal $K$ for
**every** isotropic log-concave measure *is* KLS (after isotropic normalization
$\lambda_{\max}(\mathrm{Cov})=1$). So:

- A1-bis is a finite-sum-structured, *checkable* shadow of KLS — numerics can estimate the
  realized $K=C_P^{\text{lower}}/\lambda_{\max}(\mathrm{Cov})$ across GLM instances (the
  `finum` linear-test lower bound, `lem:linear-test-lower`).
- The headline KLS implications `thm:intro-all-cut` and `thm:intro-weighted` carry
  `bridges: [ab/conj:a1-bis]` in the ledger; that single edge is the spine from Parts I/II to
  Part III.

This bridge is route-agnostic: it holds whatever proof route eventually establishes the bound.
