---
verdict: pass
authors:
  - researcher_implications, gpt-6-astra, 2026-10-01
reviewer: reviewer_weighted, gpt-6-astra, 2026-10-01
fingerprints:
  solutions/thm-intro-weighted.md: 327d210e66b326aa12c9bae635999e6eec67a3871e41d3b07c92d8e62708c619
  thm:intro-weighted: c14292a91db7cfea2d1153bb9c3a2d0d457cb5fe7802432163dc4654ce5a2948
  lem:stein-vs-source: 6bd84bc399d194fcb26d5a831feb198bcda29c1beaa21a9d1ebe64320eca30b5
  cor:tight-window-consumption: 7d0f9e5dce52482fc3b8f93155bb46e66596d3aac7d92a63f7e508bc25b59946
  lem:half: 1d4daf2283e1a1022580a067533d1cc3aae4194fa319d223aa00e4112d031a2f
  ass:weighted-package: 814ad484d39e72ce4ede9dacf954dd637418c82ecf409d0271330c484d8aaab0
---

# Weighted implication — certify review

## Findings

**Pass.** This fresh-context review reconstructs the proof from the dossier, canonical statements, ledger, SPECIFICATION.md and program brief. The reviewer did not author or direct the proof and has no authoring conversation in context. The assignment supplies the author identity. The complete dossier was read; the verdict does not use the falsity of its antecedent.

The dossier theorem agrees with `thm:intro-weighted`: the explicit positive horizon and nonnegative finite constants are exactly those of the current `ass:weighted-package`. Universality is retained across every isotropic log-concave measure and every eligible cut. The ledger correctly puts the package in `assumes`, separately from the three proved dependencies.

The proof steps check as follows.

1. From $\beta\ge0$ and $2\beta+64\eta^2<1$ one obtains $64\eta^2<1$, hence $0<\eta<1/8<1/6$. The supplied window is admissible for both the Stein conversion and tight-window consumption. No new window is chosen. Also $T_1=\min(T_0,1)>0$.
2. On the stopped interval the certified conversion is $S\le2\mathcal S/s+64\eta^2D$. Here $s>0$. Integration of nonnegative quantities and clause (ii-w) give the displayed source inequality with $\alpha=2\beta+64\eta^2$ and coefficients $2C_0,2C_1,2C_2$. No cancellation of potentially infinite damping integrals is introduced by this dossier.
3. Since $C_2\ge0$, clause (i-w) can be multiplied by $2C_2$. It gives $2C_2^2(Te_0+T^{1+\gamma})\le4C_2^2T$ for $e_0\le1$, $\gamma>0$, and $0<T\le T_1$. Thus $C'_0=2C_0+4C_2^2$ and $C'_1=2C_1$ are finite nonnegative universal constants. The estimate holds for every prefix, as required by the consumer.
4. The canonical `cor:tight-window-consumption` supplies a positive boundary constant for each such pair, uniformly because $T_1,C'_0,C'_1,\alpha,\eta$ are universal. Its nested initial condition is automatic at half mass. The corollary's stochastic integration and approximation argument is a certified dependency, not a new assertion proved here.
5. For finite $I=I_\mu(1/2)$, the defining infimum admits finite-perimeter half-mass competitors with $I\le\mu^+(E_k)\le I+1/k$. Consequently $0\le e_0(E_k)\le1/k\le1$. The same $c_*$ applies to every $k$, so $I\ge c_*$. The infinite-profile alternative causes no failure of the asserted lower bound. The certified half-mass identity gives $h_\mu=2I\ge2c_*$, which is the geometric KLS formulation used by the repository.

All used hypotheses are explicit: isotropic log-concavity, finite perimeter, half mass, the initial excess restriction, the fixed positive window, the absorption margin, and the finite universal package constants. The larger initial mass class offered by the package is unused; half-mass cuts suffice. The superlinear remainder is stronger than needed for this consumption step, but is used only through its $O(T)$ bound. No numerical evidence or new external import enters the proof.

The canonical statements and uses of `lem:stein-vs-source`, `cor:tight-window-consumption`, and `lem:half` were checked. Their ledger records are proved and certified, with no open antecedent required for these applications. This review accepts their existing certification rather than recertifying their entire transitive proof ancestry. The conversion's algebra and the half-profile infimum reduction also check directly. There is no formal `bounded_by` edge on this theorem. The two-tail and spectator obstructions are respected because the weighted package remains an antecedent; neither its propagation nor its trace clause is established here.

### Build and version evidence

Immediately before recording these reports, the escalated command `UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py` completed with exit 1 and exactly one error: the old refuter review has a stale fingerprint for `ass:weighted-package`. It reported no MyST error and no other defect. The exact `--fingerprint solutions/thm-intro-weighted.md` command then exited zero; its output is copied above. File hashes of both dossiers and the canonical statement files were checked unchanged through the final fingerprint stage.

This is a mathematical pass, not a claim that the global check is already zero. The companion fresh refuter review must first replace the stale proof record; the orchestrator must obtain a clean full check before the subsequent new status transition.

## Corrections

None to this proof. No unverified step remains within the stated certification scope. The known stale certification is addressed by the companion report, without modifying the historical review.

## Exclusions

This certifies only `thm:intro-weighted` as an implication. It neither discharges `ass:weighted-package` nor proves KLS unconditionally. It does not certify any replacement package or reopen `ap:e-weighted-excess`. No manuscript, ledger, proof, or prior review is edited.

## Proposed certification and handoff

After replacing the refuter proof record as specified in the companion report and obtaining a zero-error full check, set `thm:intro-weighted` to `proved` with the following record and unchanged logical relations:

```yaml
status: proved
depends_on: [lem:stein-vs-source, cor:tight-window-consumption, lem:half]
assumes: [ass:weighted-package]
proofs:
  - artifact: solutions/thm-intro-weighted.md
    review: research/reviews/2026-10-01-weighted-implication-review.md
```

```yaml
files:
  - research/reviews/2026-10-01-weighted-implication-review.md
deltas:
  - "After the companion refuter record replacement and a clean full check, apply the displayed proof record and proved status to thm:intro-weighted; preserve its depends_on and assumes exactly. Run the full check again after the transition."
```
