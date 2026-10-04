---
verdict: pass
authors:
  - kls_core_author, unknown, 2026-08-25
  - kls_bootstrap_author, unknown, 2026-08-25
  - kls_bootstrap_author, unknown, 2026-08-27
  - /root/aug25_grouped_repair, gpt-6-astra, 2026-10-04
reviewer: reviewer, gpt-6-astra, 2026-10-04
fingerprints:
  solutions/kls-localization-riccati-core.md: 78f7ddf53ac80fcaff2a9d431212a4139795cf4f01b50d1dd05924901a794813
  lem:matrix-riccati: b529c0f736b4dce32a7843e81f8edb6569491781941e3b8aecdc1be0ddf7a023
  thm:scalar-riccati: 83fdb94d00721fdfab219b0a417b1ac815c170925d051a187929c3635241286d
  cor:per-direction: 41aeb34aa0f748e931a100d435bb6cbba97772f149ce25c2e089fc77974c1e43
  cor:tight-window-consumption: 7d0f9e5dce52482fc3b8f93155bb46e66596d3aac7d92a63f7e508bc25b59946
  lem:survival-implies-kls: fcc0ff284f00b4f7d903900409e37db884463ad15f1f7cbb2c48ecb254e4cc64
  lem:pathwise-BL: 5b8de97a90772764778ad79fc4a9f56642c732304f4792a95b6cc493c7a95d6a
  prop:stein-rep: 809545792ca08860114a8276ff5b61febda2930cfd2b8b0f3a1a5ca1a0d00e6a
  cor:away-from-zero: d15055503849fa299724c5cb1640fab8f4b60ebc491621b6ffb1d34480e0dd95
  lem:stein-vs-source: 6bd84bc399d194fcb26d5a831feb198bcda29c1beaa21a9d1ebe64320eca30b5
  solutions/kls-bootstrap-interface.md: 8d97ee24296ac9c2b9f82b3597c0533b20d091097cf61b37e2daafb0be320d9c
  lem:half: 1d4daf2283e1a1022580a067533d1cc3aae4194fa319d223aa00e4112d031a2f
  lem:whitening: 3df7fc9dc6144b5c2ca23c0e9d21fc7a2132c0d494e03c75213cdc7ad7f72573
  thm:bootstrap: c63a5b4f893d86e70e67812caeccaa0015e754febda8a6a832909f82b015492b
  lem:perimeter-martingale: c0e1c3539694fe07c6ebe7c767bafeeadef66ac4778e02f7d217b6c9d3ad3daa
  lem:crude: 4596fedb12dae4093deded196b84f7f3f624d96f97cc69158a7eca583e997a6f
  cor:loglog: 993fe5733752c06b378ba37d27e4cfb44bd644aaf9810493cb1328bfd4bf7bc7
  ass:KI: 19c8922790211e205d6eda530efc90f61707e276482b5179d2254928e394f7c4
  cor:KI-discharged: 5ddd85d0e5ca16534f2e52aadb8a2a8b139979e5b19edb727c861d88a43243b7
  prop:ceiling: 0f7675a8caf88da1824c1bd76c2d2534a0d0ced9821774be7418b340413e1a20

---

# Fresh certification of the repaired Riccati and bootstrap dossiers

## Findings

**Pass for both dossiers and all twelve consumers below.** This full independent
examination was launched with paths and a repair mission, without the authoring
conversation. The prior revise report and repair checkpoint supplied the defect
inventory and authorship, not proof evidence. No earlier pass replaces checking.

| Dossier | Canonical node | Verdict |
|---|---|---|
| `solutions/kls-localization-riccati-core.md` | `lem:matrix-riccati` | pass |
| same | `thm:scalar-riccati` | pass |
| same | `cor:per-direction` | pass |
| same | `cor:tight-window-consumption` | pass |
| same | `lem:pathwise-BL` | pass |
| same | `cor:away-from-zero` | pass |
| `solutions/kls-bootstrap-interface.md` | `lem:half` | pass |
| same | `lem:whitening` | pass |
| same | `thm:bootstrap` | pass |
| same | `lem:crude` | pass |
| same | `cor:loglog` | pass |
| same | `prop:ceiling` | pass |

### Riccati algebra and original-posterior domains

Near zero, continuity of the localization parameter and the starting law's
exponential moment give a common integrable majorant for each polynomial
moment. On compact positive-time intervals, Gaussian damping and a bounded
localization parameter do the same. The normalizer is positive and continuous;
restricted moments have the same bounds. Posterior equivalence preserves both
positive color masses at finite times. Localizing moments, inverse masses and
quadratic variations therefore gives exhaustive stops. The indicator is a
bounded multiplier of polynomial tests; no cut derivative or perimeter
approximation is needed. The posterior martingale formula follows directly
from the normalized likelihood with $dc=dW+a\,dt$, whose drift cancels.

I checked $dv=sK\,dW-Av\,dt$, including the product-rule correction in $pa$.
For $B=vv^T/s$, both inverse-$s$ drift terms and the cross term
$-(q-p)(KB+BK)$ are correct. Substitution of $K=G+(q-p)B/s$ cancels the
linear terms and the quadratic coefficients $1+1-2$, without commuting
matrices. Subtraction from the covariance SDE uses $B^2=rB$ and yields
$-(R^2+sG^2)$. Taking traces gives $S-D$, and $B\preceq A$ gives $D\ge r^2$.
These imply the exact canonical matrix and scalar statements.

Stopping each deterministic quadratic form of $R$, taking expectations and
discarding its nonnegative terminal value proves the directional dissipation
bound. Fatou removes stops; monotone convergence extends the horizon. Both
canonical displayed assertions hold. The source-only Loewner bound is a
consequence of the stronger dissipation statement; the canonical informal
“Equivalently” does not assert reconstruction of the discarded term.

The repaired consumption proof first sums the directional bound in a fixed
orthonormal basis, giving $\mathbb E\int_0^T S\le n$ independently of the
Carleson premise. Monotone convergence for this finite source and Fatou for
the nonnegative terminal $r$ and accumulated $D$ give their joint bound
$1+n$. Thus $u(T)=\mathbb E r_{T\wedge\tau_\eta}$ is locally integrable
and all terms are finite before absorption. The Carleson premise is applied
only after auxiliary stops are removed, on its original deterministic prefixes.
The canonical signed constants can be replaced by their nonnegative parts,
matching the dossier without changing allowed dependence.

I checked the ensuing Gronwall bound, $r_0\le1$, $s\ge2/9$, initial
window displacement $\eta/2$, and probability maximal inequality giving
$9C_*T/(8\eta^2)$. This is the weak square-submartingale maximal inequality,
not the strong norm inequality with an extra factor four. Continuous exit
reaches the boundary under the strict-inequality definition. A sufficiently
small positive deterministic time therefore gives survival with probability
one half and minimum mass one third. The active canonical survival bridge
has exactly this interface and supplies the boundary conclusion. The obsolete
internal survival proof has been removed; no reduced-boundary identification
is used.

### Positive-time Brascamp–Lieb bounds

The normalized color has mean zero and squared norm one. Its pairing with the
centered quadratic is $\sqrt{s}\langle K,M\rangle$, whose gradient energy
is $4\operatorname{Tr}(MAM)$. Cauchy–Schwarz and the variance bound with
coefficient $1/t$ give $4\lambda_{max}(A)/t$ by Hilbert–Schmidt duality;
the covariance cap supplies $4/t^2$. Gaussian damping puts the polynomial
and gradient in the form domain, with cutoff convergence.

The exact variance normalization was checked against the actual published
rederivation [Nguyen, JFA 266 (2014), equation (1.9) and Section 4]
(https://arxiv.org/pdf/1302.4589). Its inverse-Hessian coefficient gives $1/t$.
For nonsmooth convex potentials or convex support, convex Moreau-envelope
smoothing followed by mollification preserves the separate quadratic term;
an affine lower bound supplies a common Gaussian majorant. The inequality
passes first for compact smooth tests and then by form closure to these
polynomials. The original 1976 article was not retrieved; this checked
published source supplies the exact variance result used.

I also checked $S\le2s\|K\|_{HS}^2+2(q-p)^2r^2/s$, the error coefficient
$(128/3)\eta^2D$, and $\eta_0=\min(1/4,\sqrt3/16)$. They give
$8/t^2+D/2$. Tonelli proves the interval assertion for $t_0>0$;
there is no zero-time assertion.

### Profile and bootstrap

The actual [Milman source, Corollaries 6.5 and 6.12]
(https://arxiv.org/pdf/0712.4092) provides symmetry and interior concavity
for nonsmooth absolutely continuous log-concave laws, including dimension one,
with the same lower exterior Minkowski convention. Interpolation from positive
epsilon and nonnegativity gives $I(p)/p\ge I(q)/q$ for $p<q\le1/2$;
no endpoint continuity is used. Symmetry gives $h=2I(1/2)$. The affine-hull
reduction preserves the profile: off-support portions of a competitor can
only enlarge its neighborhoods, and intrinsic competitors are available.
A Dirac law has no nontrivial-mass competitors, so both infima are infinite
and the balanced-set assertion is vacuous. No minimizer is assumed.

The whitening neighborhood inclusion and lower-limit scaling have the right
direction and factor $\|A^{1/2}\|_{op}^{-1}$. Positive likelihood preserves
nondegeneracy. Cylinder competitors in a Gaussian product prove dimensional
monotonicity without a tensorization assertion.

The perimeter input is used only at deterministic time. Its canonical Borel,
finite-initial-perimeter scope suffices for every measurable cut here: infinite
initial perimeter makes the upper bound trivial; otherwise the actual set's
closure has equal initial mass, since positive closure mass excess would force
infinite content. Closure leaves neighborhoods unchanged, and posterior
equivalence preserves mass equality. Thus the Borel input applies without
assuming perimeter continuity under approximation. All mass-martingale and
covariance calculations hold on the original posterior. The setup's
compact-smooth approximation sentence is unnecessary for these inequalities;
no general approximation theorem for rough-set perimeters is certified.

Both signs of $1-P-Y/2$ were checked. In the nonnegative case the ratio
$1/(1+\varepsilon)\le\hstar_n/h_\mu\le1$ gives the asserted coefficients;
in the negative case nonnegativity of the Cheeger term suffices. The bracket
bound $sr\le\lambda_{max}(A)/4$ yields the exit constant $1/(4\eta^2)$.
Tonelli integration gives exactly $1/16$, $1/8$, $1/4$. For $T<1/8$,
$\eta=T^{1/3}<1/2$ and $\varepsilon\le T^{1/3}$ give the clean estimate
with $C=2$. These match all canonical bootstrap quantifiers and constants.

The crude bound follows from the nonnegative trace with drift
$-\operatorname{Tr}(A^2)$, localization and Fatou, then the covariance cap
and splitting at $1/n$. It includes the stated endpoints. For loglog,
`ass:KI` supplies the small-time expectation bound and `cor:KI-discharged`
its proved discharge. Integration over the two intervals and substitution
into bootstrap give both conclusions. The input explicitly has $n\ge3$;
fixed low dimensions can be absorbed using the trace bound and enlarged
absolute constants. No logarithmic claim at $n=1$ is certified.

### Ceiling, hypotheses, relations, and validation

The all-measure ceiling implication has the exact canonical smallness
condition. Integrating $\lambda_{max}\le1+X$ gives $(1+\kappa)T_0$;
balanced exit costs displacement $1/6$, and the bracket factor $1/4$ leaves
coefficient nine. The canonical survival bridge then gives KLS. The final
canonical sentence is certified in its expressly delimited, certificate-specific
sense: making the clean upper bound small term by term asks for relative
covariance control, small $T^{1/3}$, and separate initial-excess control.
This is not necessity for actual excess, an all-measure requirement forced
by near-worst bootstrap, a converse, or a prohibition on proving that input.
The repaired dossier explicitly distinguishes these statements.

Hypotheses used are finite-dimensional isotropic log-concave initialization;
a nontrivial fixed cut for conditional moments; positive time for curvature;
deterministic directions; the nested window and prefix Carleson premise with
finite constants and $\alpha<1$; covariance nondegeneracy for whitening;
balanced mass, near-worstness and the epsilon/eta ranges for bootstrap;
$1/n\le T\le1$ for crude evaluation; the supplied covariance-window ranges
for loglog; and the uniform all-measure premise and smallness for ceiling.
Isotropy is unnecessary for the local Riccati algebra but supplies initial
budgets. No unstated hypothesis remains necessary. The Stein dependencies
are partly redundant because their needed algebra is rederived; their
canonical statements nevertheless supply the contrast and conversion used.

All required canonical dependency interfaces were checked. The new
`cor:per-direction` consumption edge and `thm:bootstrap` ceiling edge are
present. All dependencies are proved; these nodes have no open dependency,
open assumption edge, or proved bounding fence. The profile, crude-input and
relative-input methodological remarks are respected. No run artifact or new
preprint import supplies a proof step.

The full `UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py`, rerun in
the host environment after a sandbox Node-version mismatch, reports no MyST
or other structural error. Its only twelve failures are the expected stale
old certifications for exactly these consumers. The grouped fingerprint
command on both dossiers succeeded; its exact output is the front matter.
No proof or canonical statement changed during examination.

## Corrections

None required for the twelve claims. Replace their proof records as below and
preserve historical reports. The scope limitations above preclude stronger
ceiling or general perimeter-approximation interpretations.

## Exclusions

No recertification of the separate survival, perimeter, QCTS/Stein or
covariance-window dossiers and their full source proofs: only their proved
canonical interfaces were checked. Other consumers, surrounding manuscript
remarks, a ceiling converse, source trace upgrade and KLS itself are outside
scope. The third dossier from the prior grouped mission is not certified here.
No refutation or target-status transition is proposed.

## Handoff

Retain `status: proved` and all current relations for each of the twelve nodes.
Replace its complete `proofs` list by the applicable single record below.

```yaml
# Each of lem:matrix-riccati, thm:scalar-riccati, cor:per-direction,
# cor:tight-window-consumption, lem:pathwise-BL, cor:away-from-zero:
proofs:
  - artifact: solutions/kls-localization-riccati-core.md
    review: research/reviews/2026-10-04-aug25-repaired-review.md
```

```yaml
# Each of lem:half, lem:whitening, thm:bootstrap, lem:crude,
# cor:loglog, prop:ceiling:
proofs:
  - artifact: solutions/kls-bootstrap-interface.md
    review: research/reviews/2026-10-04-aug25-repaired-review.md
```

```yaml
files: [research/reviews/2026-10-04-aug25-repaired-review.md]
deltas:
  - Replace the twelve proof records exactly as specified above; retain their proved statuses and current relations.
```
