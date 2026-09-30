---
verdict: pass
authors:
  - /root/kls_core_author
reviewer: /root/kls_bootstrap_author
fingerprints:
  solutions/kls-localization-riccati-core.md: 45d34f81bd2b04c5ec437bdee5b8dbba845d26206e918bc78f31d5c15ba9a60f
  lem:survival-implies-kls: fcc0ff284f00b4f7d903900409e37db884463ad15f1f7cbb2c48ecb254e4cc64
  lem:matrix-riccati: b529c0f736b4dce32a7843e81f8edb6569491781941e3b8aecdc1be0ddf7a023
  thm:scalar-riccati: 83fdb94d00721fdfab219b0a417b1ac815c170925d051a187929c3635241286d
  cor:per-direction: 41aeb34aa0f748e931a100d435bb6cbba97772f149ce25c2e089fc77974c1e43
  cor:tight-window-consumption: 7d0f9e5dce52482fc3b8f93155bb46e66596d3aac7d92a63f7e508bc25b59946
  lem:pathwise-BL: 5b8de97a90772764778ad79fc4a9f56642c732304f4792a95b6cc493c7a95d6a
  prop:stein-rep: 9099e7a4a738ecdfba0dfb17d987613878c496da02125eb85d2141fa3e86cfb3
  cor:away-from-zero: d15055503849fa299724c5cb1640fab8f4b60ebc491621b6ffb1d34480e0dd95
  lem:stein-vs-source: 6bd84bc399d194fcb26d5a831feb198bcda29c1beaa21a9d1ebe64320eca30b5
  solutions/kls-qcts-stein-boundary-core.md: 61ca993ab0b90b1a077993bd35fc62131f132b57c8c1ccbb67fe94d29ec0d417
  prop:qcts-equivalence: a2120cd5d1d4968432ea232d734c8f07c4542570f23684fd94a105e065fe246e
  def:qcts: 0f22746bfd781ed526102c33b699417cb07ef6d9df40f0fb4ce59158e6376b86
  lem:boundary-rep: ec5bb90e57459669bbd919a3edcac5720f3f22bda24693a1dbca6463219f6756
  prop:two-tail: 85de1f26b16a82f85696ec5a655749365c0f036976c11265cee235f780c44d7b
---

# KLS localization, Riccati, QCTS, Stein, and boundary core — independent R2 audit

## Certified scope

This report certifies exactly the following twelve ledger nodes.

1. `lem:survival-implies-kls`
2. `lem:matrix-riccati`
3. `thm:scalar-riccati`
4. `cor:per-direction`
5. `cor:tight-window-consumption`
6. `lem:pathwise-BL`
7. `cor:away-from-zero`
8. `prop:qcts-equivalence`
9. `prop:stein-rep`
10. `lem:stein-vs-source`
11. `lem:boundary-rep`
12. `prop:two-tail`

The dossier statements match the corresponding manuscript labels and current ledger statements.
The applicable obstruction metadata is also respected: `prop:qcts-equivalence` uses the full
family of matrix-adapted balanced cuts and therefore does not cross `obs:proj-ceiling`.

## Checks performed

### Localization and Riccati core

The review independently re-derived the conditional-moment identity
$C^E-pA=sK$, including the quadratic-covariation term $-Av\,dt$ in $dv$.  It then recomputed
every Itô correction in $B=vv^T/s$.  The terms linear in $q-p$ cancel and the three quadratic
terms have coefficients $1+1-2=0$, leaving

$$
 dB=dN+(sG^2-AB-BA+rB)dt,
 \qquad
 dR=d\widetilde N-(R^2+sG^2)dt.
$$

Taking traces gives $dr=dM+(S-D)dt$.  The Loewner inequality $B\preceq A$ gives
$2s\delta^TA\delta\ge2r^2$, hence $D\ge r^2$.  For `cor:per-direction`, the review checked
that expectations are first taken at bounded localizing stopping times, that the terminal
$R$ term is nonnegative, and that finite-horizon and then infinite-horizon occupation bounds
follow by Fatou/monotone convergence without an endpoint uniform-integrability assumption.

For `lem:survival-implies-kls`, the reviewed argument uses only the deterministic-time perimeter
supermartingale direction and the standard $c\sqrt T$ isoperimetric lower bound for a
$T$-uniformly log-concave posterior.  It does not optionally stop the perimeter process.

For `cor:tight-window-consumption`, all constants were recomputed.  On
$|p-1/2|\le\eta\le1/6$, $s\ge2/9$, while $s\le1/4$.  Gronwall gives
$\mathbb E r_{T\wedge\tau_\eta}\le C_*$, the centroid integral is at most
$(9/2)C_*T$, and the continuous-exit/Doob estimate is

$$
 \mathbb P(\tau_\eta\le T)\le\frac{9C_*T}{8\eta^2}.
$$

The nested initial window supplies the required displacement $\eta/2$; no factor is missing.

For `lem:pathwise-BL`, the quadratic test belongs to the posterior's Brascamp--Lieb form domain
for every $t>0$, by the Gaussian localization factor and form closure.  The exact color identity
and $\nabla f_M=2M(x-a)$ give
$s\|K\|_{\mathrm{HS}}^2\le4\lambda_{\max}(A)/t\le4/t^2$.
For `cor:away-from-zero`, $s\ge3/16$ and $|q-p|\le2\eta$ give the error
$(128/3)\eta^2r^2$; the displayed choice
$\eta_0=\min\{1/4,\sqrt3/16\}$ makes it at most $D/2$.

### QCTS and Stein core

The review checked the conditional covariance algebra in `prop:stein-rep` and the distinction
between the two normalizations:

$$
 \mathcal S_\nu(E)/s=s\|K\|_{\mathrm{HS}}^2,
 \qquad S=s\|G\|_{\mathrm{HS}}^2.
$$

They coincide only at balance.  Off balance, applying
$\|U+V\|^2\le2\|U\|^2+2\|V\|^2$, $s\ge3/16$, and $D\ge r^2$ in both directions gives exactly
the two $64\eta^2D$ errors in `lem:stein-vs-source`.

For the converse in `prop:qcts-equivalence`, full-dimensional isotropy makes the quadratic
law atomless for every nonzero symmetric $M$, so the median cut is deterministic and has
exact mass $1/2$; no randomized probability-space extension is hidden.  The median-sign identity
$\mathbb E[gY]=\mathbb E|Y-m|$ is exact.  The reviewer also checked the cited primary
Carbery--Wright theorem: Theorem 7 with moment parameters $q=2d$ and $r=d$ gives
$\|P\|_2^{1/d}\le2C\|P\|_1^{1/d}$ for a degree-$d$ polynomial under any log-concave law.
For $d\le2$ this is the required dimension-free $L^1$-to-$L^2$ upgrade.  Since the mean is the
best $L^2$ constant, the final variance comparison follows with the claimed universal change
of constant.

For `lem:boundary-rep`, the normal $n$ points into $E$, so the outward normal of $E$ on the
relative interface is $-n$, producing the printed minus sign.  The support-boundary contribution
has outward normal $n_K$ and vanishes by the Neumann condition.  Compatibility, uniqueness modulo
constants, smooth normal traces, and the fact that relative weighted perimeter counts the
interior interface were all checked before applying surface Cauchy--Schwarz.

For `prop:two-tail`, the review recomputed the exact Gaussian tail moments.  Both conditional
means vanish, the variance contrast is
$G=8a\varphi(a)\Lambda e_1e_1^T$, and
$\mathcal S/s=16a^2\varphi(a)^2\Lambda^2$.  Whitening plus Gaussian isoperimetry gives the exact
profile $I_{\nu_\Lambda}(1/2)=\varphi(0)\Lambda^{-1/2}$, attained by the long-axis halfspace.
Thus the absolute and relative excesses, the slice-wise contradiction, and the threshold
covariance power $5/2$ all have the asserted constants and directions.  This is an analytic
calculation; no sampled or floating numerical output is used as proof.

## Compilation

Both dossiers compile standalone with `latexmk -pdf -interaction=nonstopmode -halt-on-error`:

- `/tmp/kls-localization-riccati-core-review/kls-localization-riccati-core.pdf`
- `/tmp/kls-qcts-stein-boundary-core-review/kls-qcts-stein-boundary-core.pdf`

Both commands returned exit code 0.  The remaining undefined references are the expected
cross-manuscript labels in standalone subfiles.

## Explicit exclusions

This audit certifies only the twelve nodes enumerated above.  It does not certify the open
operator-to-trace upgrade, either Carleson assumption, the weighted geometric package, any
universal KLS conclusion without its displayed conditional input, or the imported Letwin
preprint.  The two-tail result is a static obstruction and weight calibration, not a dynamic
occupation estimate.
