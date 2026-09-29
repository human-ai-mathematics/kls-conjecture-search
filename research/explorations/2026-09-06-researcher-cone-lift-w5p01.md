---
---

# Researcher (prove lens): the exponential-cone dossier

Run `w5p01`, agent `/w5/researcher-cone-lift`, concurrency key
`solution:solutions/prop-cone-moment-map.tex`.

## What was attacked

The three open internal nodes of `subsec:cmh-cones` in
`modules/kls/42-cmh-exact-cases.tex`, taken verbatim: `prop:cone-moment-map` (the cone lift
of the moment potential and the explicit canonical Stein kernel), `prop:cone-linear-sector`
(the linear sector of $\bar\mu_{K,\beta}$: zero-flux divergence of the first Stein column,
the affine $H^{-1}$ supremum $\beta+n$, the axis gate value $1+n/\beta\le2$, and the
isotropic third-moment identity $\tau_Ze_1=e_1+\tfrac12T_3(e_1)Z$), and
`cor:cube-cone-gate-zero` (the full normalized gate matrix of the cube cone).

## What was produced

One standalone dossier, `solutions/prop-cone-moment-map.tex`, with header
`ledger-node : prop:cone-moment-map; prop:cone-linear-sector; cor:cube-cone-gate-zero`.
It compiles standalone (`latexmk` exit 0; every undefined reference is a cross-module
label). It proves exactly the three manuscript statements; nothing is proved less, and the
following is proved in addition and recorded as such: the Stein identity
$\E[\bar x_i f]=\E\langle\tau e_i,\nabla f\rangle$ for every $C^1$ function of polynomial
growth (the cone is not a compact target, so `thm:regular-moment-map-compact-target` does not
supply it), the memberships $\psi=\tfrac12x^\top\Sigma^{-1}x\in\operatorname{Dom}(\mathsf A_1)$
and $x_1\in\operatorname{Dom}(\mathsf A)$ with $\mathsf A x_1=\bar x_1$ under the no-flux core
$\mathbb R+C_c^\infty(\mathbb R^n)$, the affine covariance
$\tau_{T\#\eta}(Tx)=T\tau_\eta(x)T^\top$ of the canonical kernel, and the one-dimensional
kernel $\tau_1(t)=\tfrac12(1-t^2)$ of $\mathrm{Unif}[-1,1]$ derived from the Monge–Ampère
equation.

## Hypotheses used

- `thm:regular-moment-map-compact-target` (published), applied only to the uniform law on
  the base $K$ (and $\beta K$): smooth strictly convex potential, gradient diffeomorphism onto
  the interior, $\mathbb E\,\tau_K=\operatorname{Cov}(U)$.
- The uniqueness-up-to-translation part of the moment-measure theorem of
  Cordero-Erausquin–Klartag (`CorderoErausquinKlartag2015MomentMeasures`), used to identify
  four constructed potentials with the canonical one ($\varphi$, the rescaled base potential,
  the product potential of the cube, the affine transport). Without it every statement holds
  with "the moment potential" read as the explicit $\varphi$.
- Elementary Gamma moments; $\beta\ge n$ only for log-concavity and for the two
  inequalities; the barycenter condition on $K$ for centering and the odd-moment
  cancellations.

## Corrections to the orchestrator's derivation

One sign: the rescaled base potential is $\lambda_K(\beta y)-m\log\beta$ (so that
$\int e^{-\lambda}=1$), not $+m\log\beta$; irrelevant for the Hessian, corrected in the
dossier. Everything else verified line by line.

## Unclosed steps

None in the argument. Two items are flagged in the dossier's final remark for the
literature scout / reviewer rather than proved: (a) the exact theorem number in
Cordero-Erausquin–Klartag 2015 for the existence-and-uniqueness statement (content is the
"essentially unique" of `eq:moment-measure`); (b) the manuscript prose sentence that a
square-base cone is not an affine image of a product is neither used nor proved. A
convention is also recorded: the operator domains are the closures from the no-flux core
$\mathbb R+C_c^\infty(\mathbb R^n)$; under a Dirichlet-type core the quotient value is
unchanged but $x_1\in\operatorname{Dom}(\mathsf A)$ would need re-examination.

## Deferred ledger artifact

No ledger delta is applicable now. After independent review, the deferred record for each
of the three nodes is
`proofs[].artifact: solutions/prop-cone-moment-map.tex`, `mode: agent`, with the review
path supplied by the reviewer. `prop:cone-linear-sector` and `cor:cube-cone-gate-zero`
already list `prop:cone-moment-map` in `depends_on`; the dossier uses nothing else internal
except `thm:regular-moment-map-compact-target`, already listed on `prop:cone-moment-map`.

## Portfolio

`ap:cmh-gate-zero`: no state change proposed by this checkpoint alone (the dossier is a
draft until reviewed). The cone family supplies an exact equality set for
`conj:gate-zero-sharp` in the axis direction and a full verification on cube cones; it
proves no universal bound and does not move `conj:gate-zero`.
