---
---
# Triage of the directional-quotient exploration: SC4, Dirichlet SC1, radial capacity, preferred-direction localization

Date: 2026-08-25

Status: triage and quarantine record. **Nothing in this note is promoted to the ledger.** Its
purpose is the one stated in `CLAUDE.md` for `research/explorations/`: so that the next agent
does not re-run a refuted approach, and does not mistake uncertified numerics for evidence.

## Source and relation to Route C

A consolidated summary supplied on 25 August 2026 covering a moment-map exploration organized
around *directional* Stein-kernel quotients. It is **not** about Route C as the repository defines
it, despite being described as such by its author. Route C
(`modules/kls/40-moment-map-cmh.tex`) is Haar compression plus the square-root commutator; the
companion normalization layer (`41`, `42`) is the Stein generator, the Hodge splitting, and gate
zero. This summary is a third body of work: directional quotients $\Gamma_u$, exact Dirichlet and
$\ell_1$-radial models, a radial capacity/Hardy programme, and a preferred-direction localization
proposal. It shares the moment map and the number $4$ with Route C and little else.

Only the parts that survive the repository's evidence gates were imported, and they were imported
into the **normalization layer**, not here. This note records the rest.

## Imported elsewhere (do not re-derive)

- The perturbation family used to expose the factor-4 boundary mechanism — a product moment
  potential $\psi_0(s,t)=\phi(s)+t^2/2$ perturbed by $\varepsilon a(s)b_R(t)$ with
  $a'(s)=g(\phi'(s))$, whose double limit realizes an arbitrary one-dimensional Poincaré quotient
  — is now the prescribed construction for task **M9**
  (`conj:cmh-second-variation`). Its delicate ingredient is that the **first covariance
  variation vanishes**, so whitening is $I+O(\varepsilon^2)$ and does not move the quadratic
  coefficients; that is what makes it an admissible isotropic witness rather than a broken
  normalization.
- The asymmetric-Laplace family $\rho_\beta\propto e^{-x}$ on $x\ge0$, $e^{\beta x}$ on $x<0$,
  with standardized $C_P=4\beta^2/(1+\beta^2)\to4$. Checked: $\beta=1$ gives $2$ for the symmetric
  Laplace and $\beta\to\infty$ gives $4$ for the one-sided exponential, consistent with
  `thm:cmh-1d`.
- The observation that the Dirichlet family is exactly computable. Superseded in a stronger form:
  this summary claimed the *directional* inequality $\mathbb E|(H-I)u|^2\le\Gamma_u$ for all
  $\alpha_i>0$; `thm:cmh-dirichlet` proves the full functional inequality $\mathrm{CMH}(4)$ for
  all $\alpha_i\ge1$ (the log-concave range). Use the theorem, not the directional claim.

## SC4 versus gate zero — a constant mismatch worth remembering

The summary's principal conjecture was
$$
\mathrm{SC4}:\qquad \mathbb E|(H-I)u|^2\le4\Gamma_u\quad\text{for every unit }u,
\qquad \Gamma_u=\mathbb E\operatorname{tr}(J_u^2),\ J_u=D_x(\tau u-u),
$$
and it was proposed as the bridge to a $C_P\lesssim\log^{1/3}n$, $h\gtrsim\log^{-1/6}n$
improvement via $\mathbb EH^2\preceq5I$.

Two problems, both recorded so the target is not adopted as stated:

1. **The step $\mathrm{SC4}\Rightarrow\mathbb EH^2\preceq5I$ requires $\sup_u\Gamma_u\le1$, which
   the summary never states or proves.** Both worked models happen to give $\Gamma_u=1$ exactly
   (product exponentials: $J_u=e_ie_i^\top$; uniform simplex: forced by
   $\mathbb EH^2=\frac{2(n+2)}{n+4}I$ together with the stated ratio $n/(n+4)$), and the Gaussian
   gives $0$, so a uniform bound is plausible and may follow from Letwin. But it is an unproved
   link, and it is the link the whole quantitative payoff hangs on.
2. **Even granting it, the constants do not meet.** The linear sector of $\mathrm{CMH}(4)$ is gate
   zero, $\mathbb EH^2\preceq4I$ in isotropic position. SC4 delivers $5I$. So **SC4 as stated is
   not sufficient for gate zero**, let alone for $\mathrm{CMH}(4)$.

Since gate zero is elementary to state, derives from a one-line test function, and is the binding
condition, the repository tracks `conj:gate-zero` and does **not** open an SC4 node. SC4 is
recorded here as a related-but-insufficient variant.

## Quarantined: uncertified numerics (hard constraint 2)

None of the following is admissible evidence in this repository, and none was imported. Each
needs a `finum` artifact with provenance, or a persisted exact witness, before it may be cited.
The summary itself concedes in its own falsification list that "low-order uncertified quadrature
produced at least one false violation", which is precisely the failure mode several of these
exhibit.

| claim | reported basis | why quarantined |
|---|---|---|
| weak nonproduct coupling raises the quotient, $\mathcal K_\delta=\mathcal K_0+0.026\delta^2$ | unstated numerics | no artifact; and the source states global log-concavity certification was never completed, so it is not yet a valid witness at all |
| mean-anchored Muckenhoupt control is false, exceeded by $0.362\%$ | one numerical example | a $0.36\%$ margin from uncertified quadrature is exactly the acknowledged failure mode; needs interval arithmetic |
| $\operatorname{Var}(a)\le v-J$ is false ($d=30$ example) | numeric potential | the explicit potential is not persisted, so the refutation is not checkable |
| $\ell_1$-radial quartic has positive minimum $0.03637$ at $d=80$ | numeric | same; the *structural* correction below is separable and does survive |
| radial capacity $b_*(p)\le\mathbb Ew$ "survived thousands of tests" | sampling/grid | volume of tests is not a verdict under R1; directional at best |
| Dirichlet tangent quotient $\to 3.89033$ at degree 9 | Galerkin | plausible but unpersisted; see the note below, which matters more |

## Exact material worth keeping (not promoted, but checkable)

These are exact algebra and could be promoted later if someone writes the dossiers. They are
recorded so the derivations are not lost with the summary.

- **The corrected $\ell_1$-radial criterion.** Pearson's inequality $\rho\ge\frac1d+\tau_3^2$ and
  completing the $\tau_3$-square replace the over-strong determinant condition
  $B_0\gamma\ge4q_0^2$ by the endpoint-aware
  $q_r,q_t\ge0$ and $B_0-\frac{4q_0^2}\gamma\ge-2\sqrt{q_rq_t}$. The earlier condition forced the
  mixed coefficient itself to be nonnegative and ignored the positive radial and tangent margins;
  the apparent obstruction it produced was therefore artificial. This correction is exact and
  independent of the quarantined numerics above.
- **Radial Stein-ODE identities.** With $(ap)'=(d-s)p$, $v=\operatorname{Var}S$, $M=d^2+v$,
  $T=\mathbb Ea^2$, $Q=\mathbb E[Sa]$, $J=\mathbb E[U''a^2]$, $k=d-1$: the pointwise bound
  $a(s)\le s$ (from $((s-a)p)'=s(1-U')p$ and $\mathbb E[SU']=d=\mathbb ES$), the energy identity
  $v-J=\mathbb E(a')^2+k\mathbb E(a/S)^2$, and the combined
  $v-J\ge\frac{(Q-dv)^2}T+\frac{kv^2}M$, which is stronger than applying Cauchy--Schwarz to the
  two terms separately.
- **Radial capacity, exact special cases.** For $k=0$ and $p\propto e^{-\lambda r}$ on $[A,B]$
  with $\ell=\lambda(B-A)$: $b_*=\lambda^{-2}\tanh^2(\ell/4)$ and
  $\mathbb Ew=\lambda^{-2}(1-\frac{\ell^2}{4\sinh^2(\ell/2)})$, so the conjecture reduces to
  $\ell\le4\sinh(\ell/4)$ with the one-sided exponential as the equality limit. Also
  $\frac{\operatorname{Var}R}2\le\mathbb Ew$ for general $k$, and the truncated-Gamma regime
  $a\ge75k^2$. The Jensen/harmonic-mean step $\mathbb Ew\le\frac{vM}{M+kv}$ is exact.

## Negative results recorded so they are not re-run

1. **Directional constants $1$ and $2$ fail.** The perturbative construction embeds an arbitrary
   one-dimensional Poincaré quotient into the directional moment-map quotient, so for every $K<4$
   there is a smooth isotropic strongly log-concave target with $c_u>K\Gamma_u$; the same holds
   with $\mathbb E|(H-I)u|^2$ in place of $c_u$. Consistent with `thm:cmh-1d`: the boundary
   mechanism is the one-dimensional exponential in both cases.
2. **No finite raw derivative comparison.** $G_u\le K\Gamma_u$ is false for **every** finite $K$,
   because $g'$ can be localized where the one-dimensional Stein kernel is arbitrarily large.
   This kills the whole class of "directional Korn" bridges, including the Feshbach route that was
   to consume them.
3. **Polarizing the Chen--Klartag trace argument does not work.** The cyclic identity gives only
   $\operatorname{tr}R\ge0$, not $R\succeq0$; a bad direction is paid for by surplus in the
   complementary direction, with directional ratio of order $M$ for
   $H=\operatorname{diag}(M,1)$. This is the same phenomenon as
   `prop:letwin-not-gate-zero` in the normalization layer, and the two should be read together:
   trace information does not polarize into directional information for free.
4. **The proposed log-concavity-preserving transport $z'(r)=r^2/(r^2+k\tau(r))$ is dead** —
   truncated Gamma laws show it does not preserve log-concavity.
5. **The Dirichlet tangent-mode approach to $4$ is not a nonproduct obstruction.** The Galerkin
   sequence climbing toward $2+2\cos\frac{2\pi}{2d+1}\to4$ **degenerates, through the Gamma
   representation, to independent exponential factors**. It therefore recovers the known
   one-dimensional boundary obstruction rather than producing a new one. This is the most useful
   negative item in the summary: without it, that numerical sequence reads as nonproduct evidence
   for the constant $4$, and it is not.

## Preferred-direction localization — routed, not opened

The summary proposes controlling
$\mathfrak a_t=\lVert A_t\rVert_{\mathrm{op}}\,\theta_t^\top A_t\theta_t$ instead of
$\lVert A_t\rVert_{\mathrm{op}}^2$, with the prospective estimate
$\mathbb E\mathfrak a_t^{1/3}\lesssim1$ at $t\asymp C_P(\mu)^{-1}$, on the grounds that large
exceptional covariance eigenvalues are harmless if the first eigenfunction avoids them.

This is a sharpening of the `conj:trace-upgrade` / `conj:stein-weighted` / `conj:product-alignment` cluster, and
**hard constraint 6 forbids opening it as a parallel effort**. It is recorded here and referred to
that cluster's owner. It is also close in spirit to `conj:mm-spectral-occupation` on the
`moment-map-spectral` route, which already follows a first eigenfunction; whoever takes it up
should compare the two before adding a node, not after.

Note also the summary's own observation that for product exponentials $T_k=2e_ke_k^\top$, so the
maximum-direction effect persists even though KLS tensorizes perfectly. That is a real constraint
on any proof requiring uniform operator-norm control, and it is consistent with
`rem:single-coordinate-cuts` without being implied by it.

## Net assessment

Roughly the perturbative obstruction, the Dirichlet computability, and the five negative results
were worth keeping; the quantitative programme built on them (SC4 as a target, the radial capacity
conjecture, the coupling-gain rigidity estimate) rests on numerics this repository cannot accept
and on at least one constant mismatch. The exact algebra listed above is separable from the
numerics and survives.
