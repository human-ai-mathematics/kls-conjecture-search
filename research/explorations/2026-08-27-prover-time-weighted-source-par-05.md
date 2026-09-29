---
---
# Prover: scale-weighted all-cut source budget

Date: 2026-08-27

Role: `prover`

Concurrency key: `solution:lem-time-weighted-source`

Ledger node: `lem:time-weighted-source`

Dossier: `solutions/lem-time-weighted-source.tex`

## Statement audited

The accepted ledger node and manuscript Lemma `lem:time-weighted-source` agree: for every
isotropic log-concave initial law, every fixed measurable cut $E$ with $0<\mu(E)<1$, and every
$T>0$,

$$
\mathbb E\int_0^T t^2(S_t+r_t^2)\,dt
\le T^2\mathbb E r_T\le T.
$$

The manuscript consequence restricts the nonnegative integrand to a balanced stopped window;
it does not replace $r_T$ by a stopped terminal value and does not remove the factor $t^2$.
The dossier states exactly that consequence, and in fact observes by positivity that it holds
for any stopping time.

The ledger gives this node no `bounded_by` edge. Its only `depends_on` entry is
`thm:scalar-riccati`, which is `proved`, agent-certified, and depends on the likewise certified
`lem:matrix-riccati`. The other analytic input is the standard posterior Brascamp--Lieb
covariance cap $A_t\preceq t^{-1}I$ for $t>0$, already part of the repository's localization
setup. There is no unresolved premise.

## Analytic proof

Covariance decomposition gives

$$
A_t=p_t\Sigma_t^E+q_t\Sigma_t^{E^c}+B_t,
\qquad B_t=s_t\delta_t\delta_t^T,
$$

so $0\preceq B_t\preceq A_t$. Since $B_t$ has rank at most one, its only possible nonzero
eigenvalue is $r_t=\operatorname{Tr}B_t$. Thus, for $t>0$,

$$
0\le r_t\le\lambda_{\max}(A_t)\le t^{-1}.
$$

The same cap yields

$$
s_t\delta_t^TA_t\delta_t=\operatorname{Tr}(A_tB_t)
\le t^{-1}\operatorname{Tr}B_t=t^{-1}r_t,
$$

and therefore

$$
D_t=2s_t\delta_t^TA_t\delta_t-r_t^2
\le\frac{2r_t}{t}-r_t^2.
$$

Multiplying the certified scalar Riccati identity
$dr_t=dM_t+(S_t-D_t)dt$ by $t^2$ gives

$$
d(t^2r_t)
=t^2dM_t+(2tr_t+t^2S_t-t^2D_t)dt
\ge t^2dM_t+t^2(S_t+r_t^2)dt.
$$

For $0<\varepsilon<T$, the dossier localizes the weighted martingale
$\int_\varepsilon^t u^2dM_u$ at increasing bounded levels. Writing
$\theta_k=T\wedge\rho_k$, expectation at the localized time gives

$$
\mathbb E\int_\varepsilon^{\theta_k}t^2(S_t+r_t^2)dt
\le \mathbb E[\theta_k^2r_{\theta_k}]-\varepsilon^2\mathbb E r_\varepsilon.
$$

The bound $0\le\theta_k^2r_{\theta_k}\le\theta_k\le T$ supplies domination of the terminal
term, while positivity supplies monotone convergence of the occupation term. Removing the
localizer therefore retains the sharper endpoint $T^2\mathbb E r_T$. Finally
$0\le\varepsilon^2\mathbb E r_\varepsilon\le\varepsilon$, so monotone convergence as
$\varepsilon\downarrow0$ handles the initial endpoint. The bound
$T^2\mathbb E r_T\le T$ follows pathwise from $r_T\le T^{-1}$.

The proof records the regularization passage explicitly. It first works with compact smooth
data and bounded stopping. On every strip $[\varepsilon,T]$, the certified regularization
convention gives convergence of posterior cut masses and first and second moments; Fatou applies
to the nonnegative occupation, while $0\le T^2r_T\le T$ gives terminal uniform integrability.
The constants are independent of the approximation, and then $\varepsilon\downarrow0$ handles
the endpoint. No compact-support or smoothness assumption remains.

## Fence audit

Although `lem:time-weighted-source` has no `bounded_by` metadata, every fence relevant to the
nearby operator-to-trace gate was checked.

- `obs:proj-ceiling`: the proof makes no projection-to-tensor inference; it uses the exact scalar
  Riccati identity and the full covariance cap.
- `obs:two-tail`: the conclusion permits source of scale $t^{-2}$ and retains the quadratic time
  weight. It asserts no slice-wise absolute-scale control.
- `obs:relative-ceiling`: no universal bound on $\Xi_T$ or relative-scale covariance occupation
  is assumed.
- `obs:crude-insufficient`, `obs:circularity`, and `obs:rank-one-refuted`: the proof uses neither
  the crude $\Xi_T$ estimate, a localized isoperimetric profile, nor a product-cut witness.

No implication or comparison is made among `q:upgrade`, `q:stein-weighted`, and `q:alignment`.
The dossier proves no Carleson estimate and no KLS conclusion.

## Hypotheses, gaps, and status

Hypotheses actually used:

1. $\mu$ is isotropic and log-concave on $\mathbb R^n$;
2. $E$ is fixed before localization and $0<\mu(E)<1$;
3. $T>0$;
4. the certified scalar Riccati identity;
5. covariance decomposition $B_t\preceq A_t$ and the rank-one identity
   $\lambda_{\max}(B_t)=r_t$;
6. the posterior Brascamp--Lieb cap $A_t\preceq t^{-1}I$ for $t>0$;
7. bounded localization, Fatou/monotone convergence, and terminal uniform integrability as
   displayed above.

No additional or unstated hypothesis was used. No unclosed analytic step was identified. The
result is unconditional, but the dossier remains an unchecked candidate with
`checked_by: none`; the author does not certify it.

## Build and ledger disposition

The standalone command

```bash
cd solutions && latexmk -pdf -outdir=../build lem-time-weighted-source.tex
```

returned exit code 0 and produced `build/lem-time-weighted-source.pdf`. The only remaining LaTeX
warnings are the expected standalone cross-manuscript references to
`lem:time-weighted-source` and `thm:scalar-riccati`; all dossier-internal references resolve.

There is no applicable ledger delta while `checked_by: none`. The deferred artifact candidate
is `solution: solutions/lem-time-weighted-source.tex`; it may be wired only atomically with a
real `checked_by` value and, for agent certification, a passing persisted review by a distinct
reviewer.

```yaml
outcome: complete
artifacts:
  - solutions/lem-time-weighted-source.tex
  - research/explorations/2026-08-27-prover-time-weighted-source-par-05.md
proposed_deltas:
  - none while checked_by is none; solutions/lem-time-weighted-source.tex is only a deferred artifact candidate
next_role: proof-checker
next_prompt: |
  Cold-audit `solutions/lem-time-weighted-source.tex` for ledger node
  `lem:time-weighted-source`, reconstructing the argument from repository artifacts without
  relying on the prover's conversation. Verify exact agreement with the accepted statement at
  `modules/kls/27-eldan-open-targets.tex` and the ledger, and verify the dependency closure
  through the already certified `thm:scalar-riccati` and `lem:matrix-riccati`. Check in detail:
  covariance decomposition and the rank-one identity; the posterior Brascamp--Lieb cap;
  `D_t <= 2r_t/t-r_t^2`; the weighted Ito inequality; bounded localization of
  `int_epsilon^t u^2 dM_u`; dominated convergence of the terminal term, monotone/Fatou passage
  for occupation, the endpoint `epsilon down to 0`, and the regularization passage. Confirm the
  stopped-window consequence is obtained only by positivity. Audit all relevant fences despite
  the node having no `bounded_by` edge, and confirm the dossier does not remove the quadratic
  weight or claim `q:upgrade`, `q:stein-weighted`, `q:alignment`, an all-cut Carleson estimate,
  or KLS. Recompile standalone. If and only if every step passes, write a persisted proof review
  naming `/root/prove_time_weighted_par_05` as author and yourself as distinct reviewer, then
  return the exact atomic ledger/manuscript certification proposal to the orchestrator. Do not
  edit the dossier, either ledger, or the manuscript.
```
