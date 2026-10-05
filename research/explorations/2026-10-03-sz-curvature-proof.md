---
---

# Reconstructing polynomial-to-curvature comparison

## Question examined

On `ap:polynomial-curvature-audit`, reconstruct Section 5 of
Song–Zhang arXiv:2610.01447v1 as the implication
`thm:sz-curvature-comparison`, using `lem:sz-analytic-foundations` and
`thm:sz-polynomial-variance`. The starting lens was **prove**, unchanged.
The proposed canonical statement is in the manuscript; the complete argument
is in `solutions/thm-sz-curvature-comparison.md`.

## What we learned

- *Established (argument written, awaiting independent review):* the normalized
  inverse-operator family has an exact defect identity. Its derivative error
  is paid by the energy drop, without commuting a spatial derivative with a
  spectral inverse.
- *Established (argument written, awaiting independent review):* the block
  recovery constant follows from the full singular spectrum of a subset
  incidence map. This works on the whole tensor space and all finite direct
  sums; no dimension-dependent irreducible-component estimate is hidden.
- *Established (argument written, awaiting independent review):* the swap of
  derivative slots $a,a+1$ in $u^J$ is created in $u^{J-a+1}$, has source
  $\chi_{J-a}$, and is propagated through exactly $a-1$ bounded maps. It is
  essential to retain the scalar normalizer for the original entire family.
- *Established (argument written, awaiting independent review):* the dyadic
  factorial ratios telescope to a single factorial. All overlapping defect
  intervals are absorbed by one positive lag kernel, so their number is not
  charged again. The low-degree universal polynomial estimate is necessary
  to make this kernel small uniformly in terminal degree.
- *Established (argument written, awaiting independent review):* the stopped
  prefix has nonzero successor families and the required normalizer bound
  before the local estimate is applied. The contradiction at the finite
  horizon closes the curvature comparison with its explicit threshold.

## What resists

The comparison is a conditional estimate for a specified polynomial profile;
it does not establish a depth-uniform profile by itself. Its admissibility
threshold $R\ge2^{40}\epsilon^{-2}$ remains part of the theorem, hence the
bounded-product improvement discussed previously cannot be inserted without
checking this condition. No implication to CMH, sharp gate zero, universal-time
occupation, or dimension-free KLS has been established. The two prerequisite
nodes and this reconstruction require independent review before any dependency
is treated as discharged.

## Proposed next step

Have a fresh reviewer certify `thm:sz-curvature-comparison` against its
canonical statement and the complete dossier, checking the subset-incidence
spectrum, polynomial testing with unbounded tests, slot order in the swap
propagation, dyadic terminal and defect coefficients, the exact geometric-series
bounds, and the first-exit normalizer argument. Review the two prerequisite
nodes independently. Then feed the comparison, with its threshold unchanged,
into the degree/depth induction behind `thm:sz-iterated-curvature`.
