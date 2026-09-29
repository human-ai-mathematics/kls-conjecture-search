---
artifacts:
  - research/runs/2026-09-06T175558.606924Z-cmh-cone.jsonl
  - research/runs/2026-09-06T175611.501834Z-cmh-cone.jsonl
---
# Orchestrator: wave `w5` — the linear sector of Route C, exponential cones, and the wave-four resume queue

Date: 2026-09-06. Role: `orchestrator` (main session, sole ledger writer). Run id: `w5`.

## Task

Attack `conj:kls` through the existing routes, with the freedom to open a new one. The wave
chose the linear sector of Route C (gate zero, `conj:gate-zero`) because it is the cheapest
precise open statement on the frontier, and it closed the two review items the wave-four
interruption left behind.

## Mathematical content of the wave

**The linear sector is a third-moment statement plus a high-mode remainder.** Testing the CMH
quotient on a linear function gives the column energy $\E|\tau a|^2$ of the canonical Stein
kernel. Its projection onto the gap eigenspace $\{1,x_b\}$ has coefficients
$\E_\mu[\tau_{ia}x_b]=\tfrac12\E_\mu[X_iX_aX_b]$, so
$$\E|\tau a|^2=1+\tfrac14\|T_3(a)\|_{\mathrm{HS}}^2+\E|v_a|^2,$$
with $v_a$ orthogonal to constants and linear functions (`lem:linear-sector-third-moment`,
certified). Consequently gate zero at constant $c$ contains the directional third-moment bound
$\|T_3(a)\|_{\mathrm{HS}}\le2\sqrt{c-1}$ (`cor:gate-zero-third-moment`, certified). The
identity $\E_\nu\partial_{ijk}\varphi=\tfrac12T_{ijk}$ is Lemma 3.7 of the Chen–Klartag
preprint, and the summed form is their Theorem 1.2 chain; the directional statement with the
named remainder is what the repository adds.

**Sharp gate zero.** The natural sharp statement is $\E[H\Sigma^{-1}H]\preceq2\Sigma$, the
operator form of the Chen–Klartag trace bound (`conj:gate-zero-sharp`, open, refines
`conj:gate-zero`). By the corollary it implies $\kappa_n\le2$, sharper than Letwin's
$2\sqrt2$, which calibrates its difficulty (brief, trap 10). The literature scout found no
operator-form statement anywhere in the literature.

**Exponential cones: explicit moment maps and a new equality set.** For a centered convex body
$K\subset\R^{n-1}$ and $\beta\ge n$, the law $\propto x_1^{\beta-n}e^{-x_1}$ on the cone over
$K$ has moment potential $\exp(y_1+\lambda(y')/\beta)-\beta y_1+\log\Gamma(\beta)$, with
$\lambda$ the moment potential of $\mathrm{Unif}(\beta K)$, and Stein kernel
$x_1\begin{pmatrix}1&u^\top\\u&uu^\top+\beta\tau_K(u)\end{pmatrix}$
(`prop:cone-moment-map`, certified). Its first column is the position vector, a covariance
gradient with no solenoidal part; the axis gate value is exactly $1+n/\beta\le2$, equal to
$2$ iff $\beta=n$, and the third moment attains $\|T_3(e_1)\|_{\mathrm{HS}}^2=4n/\beta$ with
zero remainder (`prop:cone-linear-sector`, certified). For the cube base the whole gate matrix
is explicit and at most $2$ (`cor:cube-cone-gate-zero`, certified). The $\beta=n$ case is the
cone of Chen–Klartag's Lemma 4.2; the moment map and the general family are new.

**What the family does not do.** The exact `cmh-cone` battery (264 exact cone instances over
products of simplices and intervals up to $m=7$, all decided $\lambda_{\max}\le2$ by rational
$LDL^\top$; ball cones directional with margin) found no violation of the sharp form, and the
cube-cone CMH Galerkin quotients sit strictly below the exponential-product values at equal
degree. So the base perturbation the manuscript proposed as a CMH(4) stress test is
flat-to-downhill; any pressure on CMH(4) within this family lies in the radial factor.

## Certifications wired this wave

| node | status | dossier | review |
|---|---|---|---|
| `lem:fiber-root-degree-two` | proved | `solutions/lem-fiber-root-degree-two.tex` | `2026-09-06-lem-fiber-root-degree-two-proof-review.md` |
| `lem:cmh-linear-spectral-resolution` | proved (weak column equation; manuscript reworded, `prop:cmh-bochner` dropped from `depends_on`) | `solutions/lem-cmh-linear-spectral-resolution.tex` (repaired w5p03) | audit then `2026-09-06-lem-cmh-linear-spectral-resolution-proof-review.md` |
| `lem:linear-sector-third-moment`, `cor:gate-zero-third-moment` | proved | `solutions/lem-linear-sector-third-moment.tex` | `2026-09-06-lem-linear-sector-third-moment-proof-review.md` |
| `prop:cone-moment-map`, `prop:cone-linear-sector`, `cor:cube-cone-gate-zero` | proved | `solutions/prop-cone-moment-map.tex` (repaired w5p04) | audit then `2026-09-06-prop-cone-moment-map-proof-review.md` |

No author reviewed their own dossier; every review reconstructed the work from artifacts. Two
first reviews returned audits (statement-scope mismatch on the spectral resolution, resolved by
rewording the manuscript to the weak form the dossier proves; the definition of "moment
potential" in the cone dossier, resolved by restricting to essentially-continuous potentials as
in Cordero-Erausquin–Klartag), and the repaired dossiers passed second cold reviews.

`conj:kls` is untouched: every certified node is exact-case or structural, none carries an
`assumes`, and none is reported as progress on the target (P2).

## Ledger and manuscript deltas applied

Seven new nodes in modules 41 and 42; `status.tex` regenerated; brief edge case 7 (exponential
cones) and trap 10 (sharp linear sector versus the CMH constant); attribution sentences to
Chen–Klartag Lemmas 3.7 and 4.2 and Klartag's conical integration formula
(`Klartag2018IsotropicMahler` added to the bibliography); module 45 prose updated for the
certified fiber lemma; module 41 prose updated for the certified spectral resolution and the
definitions of $Q_{\rm lin}$, $(\mathrm{AB})_{\rho,\beta}$, $A$ and $Q$.

## Open items handed to the synthesizer

- Portfolio: `ap:fiber-simplex-dual` blocker `lem:fiber-root-degree-two` discharged;
  `ap:cmh-anisotropic-bootstrap` blocker `lem:cmh-linear-spectral-resolution` discharged, with
  the strong column equation ($\Tr Q\in L^2$) recorded as the residual; `ap:cmh-gate-zero`
  now has a first target (`conj:gate-zero-sharp`), an exact decision procedure, and a proved
  decomposition tool; `ap:cmh-solenoidal-perturbation` should be told the base direction is
  exhausted for polytopal bases up to $m=7$.
- Instance registry: the six wave-four proposals and the eight `w5n01` proposals.
- Live candidates: `cand:directional-h-minus-one-two`, `cand:letwin-rank-one-second-moment`
  (literature scout), `cand:cmh-exponential-galerkin-rate`,
  `cand:cone-transverse-equality-simplex` (numerics). None is promoted here.
- Non-blocking follow-ups: journal theorem numbering of the CEK uniqueness theorem; the
  `sync` items on module 15 wording (which is in fact correct, the cited preprint being the
  one with a v2) and on the cone integrability sentence, which the orchestrator justified in
  prose.

## Standing risk

The identity $\E_\nu\partial_{ijk}\varphi=\tfrac12T_{ijk}$ and the cone third moments are
in an unreviewed version-1 preprint; the repository's own proofs do not depend on it, so no
node imports it, but the attribution sentences would need revisiting if that preprint changed.
