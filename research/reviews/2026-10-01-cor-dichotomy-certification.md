---
verdict: pass
authors:
  - dichotomy researcher, gpt-6-astra, 2026-10-01
reviewer: reviewer, gpt-6-astra, 2026-10-01
fingerprints:
  solutions/cor-dichotomy.md: fd881c0ea0bdabadb45e8cb66e80a5f5f76381e44552bd71480dd6f102ce210b
  cor:dichotomy: 4455e1fe18ca1498290438a1e110c3a06773e8ab0e5bb12d49701b681e4d9ae0
  thm:bootstrap: c63a5b4f893d86e70e67812caeccaa0015e754febda8a6a832909f82b015492b
  cor:loglog: 993fe5733752c06b378ba37d27e4cfb44bd644aaf9810493cb1328bfd4bf7bc7
  cor:KI-discharged: 5ddd85d0e5ca16534f2e52aadb8a2a8b139979e5b19edb727c861d88a43243b7
  lem:half: 1d4daf2283e1a1022580a067533d1cc3aae4194fa319d223aa00e4112d031a2f
  lem:whitening: 3df7fc9dc6144b5c2ca23c0e9d21fc7a2132c0d494e03c75213cdc7ad7f72573
  thm:klartag-logn: 70dd5528111bc813bcfa6750d3afcfcdc31121dbf564fb0681db32265b576b60
  def:cheeger-excess: 11c7b2640e46c21535a33849034c875cbc82d1aef65481500b28589ab7a1fe1d
  ass:absolute-geometric-completion: d9d5e38e2ace44adf3adaee48e5df4cee1743fe663306bc9b4bcc47f54830ce1
---

# Independent certification of the residual dichotomy

## Findings

This is a fresh-context `certify` review reconstructed from repository artifacts. No conversation that authored or directed the dossier was supplied. The author identity comes from `research/explorations/2026-10-01-dichotomy-quantifier-repair.md`; its assertions are not used as proof evidence.

The theorem in `solutions/cor-dichotomy.md` agrees exactly with `cor:dichotomy` in `modules/20-eldan-open-targets.md`: the completion implies the existence of universal $a>0$ and $N\ge3$ with $\hstar_n\ge a/(1+\log\log n)$ for $n\ge N$, with the stated dependence and eventual factor-two consequence. The completion is an antecedent, not an established geometric result.

The dependency statements were checked in `modules/19-bootstrap.md` and `modules/30-covariance-technology.md`, against the relevant statements and arguments in `solutions/kls-bootstrap-interface.md` and the covariance-discharge section of `solutions/kls-product-covariance.md`. They supply exactly the balance identity, monotonicity, clean bootstrap, published $C_2=2$ window, and polylogarithmic supply consumed here. Their existing certifications are retained; this review does not replace them. All direct proof dependencies are proved or defined, and the full checker reports no lifted certification.

The sole direct imported result is the finite-dimensional positivity bound `thm:klartag-logn`. I checked Theorem 1.2 and definition (1.5) on page 3 of [Klartag's published article](https://arxiv.org/pdf/2303.14938), *Ars Inveniendi Analytica* (2023), Paper 4. Its upper bound for the reciprocal Cheeger constant gives the manuscript's lower bound for $\hstar_n$ for $n\ge2$. This is a published input, not an unchecked preprint. No new external result is imported through this dossier.

The proof steps check as follows.

1. Fixing the completion constants before the dimension is correct. $0<T_0<1/8$ gives $0<\eta=T_0^{1/3}<1/2$. The chosen positive $\eps$ is at most $1$, $\eps_g$, and $T_0^{1/3}$. Consequently the same near-worst law and the same stopping width meet both sets of hypotheses.
2. The published cutoff $c_0(\log n)^{-2}$ tends to zero. Thus one dimension threshold makes $t_1(n)\le T_0$ and $L_n=1+\log\log n\ge1$ simultaneously for every larger integer. The constant $C_L$ is independent of the measure and cut; all constants chosen in the argument have the asserted dependence.
3. Positivity of $\hstar_n$ and the finite Gaussian competitor justify a multiplicative near-minimizer of its infimum. This gives $h_\mu\le(1+\eps)\hstar_n\le2\hstar_n$. There is no assumption of an extremizing measure.
4. The certified balance identity makes $I_\mu(1/2)=h_\mu/2$ finite. The definition of the profile then supplies balanced cuts with $0\le e_j<\min(\delta_g,j^{-1})$. Each has finite lower outer Minkowski perimeter. The equality $e_j=\bar e_0(E_j)$ uses balance, not regularity or existence of a minimizing set.
5. The supply estimate applies separately to each fixed cut, with its own stopping time. Since $T_0^{4/3}\le1\le L_n$, its error is at most $2C_Lh_\mu L_n\le4C_L\hstar_nL_n$. Under the contradiction hypothesis this is at most $\kappa T_0$ by $a\le\kappa T_0/(4C_L)$. The completion therefore yields the same lower bound $c_g$ for every approximating perimeter.
6. Only scalar perimeter values are passed to a limit. They converge to $I_\mu(1/2)$, so $h_\mu\ge2c_g$. There is no interchange of a stochastic expectation with a cut limit. On the other hand $h_\mu\le2a/L_n\le c_g$ by $a\le c_g/2$, a strict contradiction since $c_g>0$.
7. The argument excludes even $\hstar_n\le a/L_n$ and hence gives the claimed weak lower bound. For $\log\log n\ge1$, $L_n\le2\log\log n$, which gives the stated asymptotic consequence.

The separate matched-time remark is correct as an implication with its additional premise. For every $n\ge2$, choose arbitrarily accurate positive near-worst tolerances below all four specified bounds. The generic constant $C_B$ cancels the $1/C_B$ in that premise at precisely the completion time. Applying the balanced-cut limit for each such law gives $h_{\mu_k}\ge2c_g$; the subsequent scalar limit $\eps_k\to0$ gives $\hstar_n\ge2c_g$. Monotonicity supplies dimension one. The remark correctly does not infer the matched-time premise from `conj:taming`, whose time is existential and depends on the requested error. Neither premise is discharged by this review.

Every hypothesis used is stated: isotropy, log-concavity, the dimension ranges, near-worstness, balance, finite initial excess within the fixed positive tolerance, the fixed completion constants, and the bootstrap time and width restrictions. The last remark additionally uses its explicitly quantified covariance estimate. No unstated hypothesis is required. `lem:whitening` is used directly only in that remark and indirectly through the bootstrap in the main proof; there is no problematic unused antecedent.

There are no registered `bounded_by` edges. The contextual profile-circularity, crude-input, and relative-scale warnings are respected: the argument uses the external worst-dimensional infimum and the polylogarithmic supply, and claims no all-measure covariance improvement. The two spectator obstructions concern stronger uniform propagation claims. The present proof retains the near-worst completion as an antecedent and asserts no uniform superlinear remainder.

## Corrections

None to the reviewed dossier or canonical statement.

## Validation

`uv --cache-dir /tmp/kls-uv-cache run scripts/check.py` completed with exit code 0 and no MyST errors. The actual `--fingerprint solutions/cor-dichotomy.md` command then completed with exit code 0; its output is reproduced above. The dossier was correctly reported as a draft before applying this review.

## Exclusions

This certifies only `cor:dichotomy`. It does not prove the absolute geometric completion, covariance taming, a matched-time estimate, KLS, or any other open node. Existing dependency proofs are consumed under their certifications rather than recertified here. The surrounding manuscript prose and abbreviated proof are outside this certification and may require the planned writer pass; they do not alter the exact canonical claim checked above. This is not a full manuscript/brief `sync` audit.

## Handoff

```yaml
files:
  - research/reviews/2026-10-01-cor-dichotomy-certification.md
deltas:
  - 'For cor:dichotomy in research/program/ledger.yaml, set status: proved and add proofs: [{artifact: solutions/cor-dichotomy.md, review: research/reviews/2026-10-01-cor-dichotomy-certification.md}]. Preserve depends_on: [thm:bootstrap, cor:loglog, cor:KI-discharged, lem:half, lem:whitening, thm:klartag-logn, def:cheeger-excess] and assumes: [ass:absolute-geometric-completion]. Leave the completion and conj:taming open; no route closure follows.'
```
