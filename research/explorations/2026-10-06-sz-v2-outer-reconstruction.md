---
---

# Song–Zhang v2: actual finite blocks and summable outer profiles

## Question examined

Route `ap:sz-v2-reconstruction`, prove lens: reconstruct the analytic mechanism
of Section 9 of [@SongZhang2026ConstantKLS], rather than only the scalar
summability contract. The nodes engaged are
[](#lem:sz-v2-orbit-green-restart), [](#lem:sz-v2-block-extension),
[](#lem:sz-v2-block-propagation), [](#prop:sz-v2-finite-chain-blocks),
[](#lem:sz-v2-profile-refinement), [](#prop:sz-v2-small-loss),
[](#prop:sz-v2-summable-budgets), and [](#thm:sz-v2-kls).

## What was learned

**Arguments written; independent review controls their status.** The outer
reconstruction is now split into stable generic foundations (dossier 145),
finite-chain realization (148), near-unit depth and coefficient-return
arguments (140), retained geometric budgets (141), and the final finite
parameter choice followed by approximation (142). The root reports that
independent review has passed the generic foundations and finite-chain
realization. The final profile group is being submitted separately; this
checkpoint makes no certification decision about it.

The actual-radius energy budget cannot be obtained by substituting a block
radius into the generic operator-norm budget. Dossier 145 proves it from the
actual direct-sum orbit: the ratio of successive normalized energies is the
block radius times a nonincreasing window-mass ratio. The resulting matched
budget accompanies the same family that supplies the retained loss prefix.
This is a real extra analytic input to the scalar outer contract.

The dependence on the number of retained coefficient caps is removed by a
single sum over disjoint degree intervals. In each interval the corresponding
margin times the degree is bounded below by a constant times the square root
of that degree. One convergent polynomial-times-exponential series therefore
bounds all intervals together; summing a constant separately for every cap
would not suffice.

The near-unit profile refinement uses three distinct operations. Static
transfer extracts coefficients at an explicitly admissible depth and odd
order. The actual finite block family gives a terminal-degree contradiction
through its delayed joint-loss bound and matched energy budget. Finally the
terminal-depth distortions are multiplied only above a starting depth of order
the reciprocal loss budget. The extraction retains the exact selected order;
a fixed additive shift in the next unsmoothed height would not be a small loss.

The new node `lem:sz-v2-profile-refinement` is proposed separately from the
small-loss theorem: the summable-budget proof uses this stronger reusable
interface, not merely the latter theorem's conclusion. The optional earlier
caps enter through explicit maximum bounds on their floors. Their number
does not multiply any constant.

## What remains to audit

The profile dossiers require independent mathematical audit. In particular:

- Check the low/high height split in the coefficient return, including the
  initialization at the new starting depth and all odd-order constraints.
- Check the simultaneous constant choices in the near-unit depth step, and
  the logarithmic dependence of additive allowances on the bounded profile
  offset before fixing its geometric increments.
- Check that the static transfer is invoked with a uniform all-law premise,
  and that every first-exit estimate uses the actual family's matched budget.
- Check the final finite choice of the profile index and depth before weak
  approximation, and the extension from compact smooth tests to locally
  Lipschitz tests of finite energy.

No BKL result, coefficient consequence of BKL, or prior KLS conclusion is an
input to these arguments. No claim of priority follows from the older Wave A
scalar contract: the present reconstruction imports and reconstructs the new
analytic mechanism from the Song–Zhang revision.

## Proposed next step

Independently review dossiers 140–142 with the explicit refinement interface,
and repair any exact defect before recording new proof statuses. Keep the
already reviewed generic blocks stable. Once the final theorem passes, the
root can add the minimal canonical KLS composition without changing its source
provenance or erasing the independent BKL record.
