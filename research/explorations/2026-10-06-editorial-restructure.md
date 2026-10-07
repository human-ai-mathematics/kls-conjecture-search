---
---

# The manuscript restructured around the two proofs

<!-- Orchestrator checkpoint for a writer's pass in four steps. No node, statement or status changes. -->

## Question examined

How should the manuscript be organised so that it (1) explains the two proofs of
`conj:kls` pedagogically, (2) helps a reader understand KLS as a theorem, and (3)
presents alternative arguments? After the repositioning of the same day
(`2026-10-06-editorial-post-kls.md`) the overview still explained neither proof: its
section "Two conversions that reach every test function" presented Letwin and
Song–Zhang v1, two dimension-dependent bounds; the promised comparison of the proofs
did not exist; nothing treated KLS as a theorem (forms, consequences, constants); the
approaches were described about six times; and the fixed cut weighed eleven chapters
whose results are obstructions.

## What we learned

*Judgment (orchestrator, with the project owner's decisions of 2026-10-06).*

1. **Order of the proofs: v1 → BKL → v2.** BKL is the shorter route from the spectral
   criterion of v1 and the first deposited (19:30:34 UTC against 21:21:03 UTC on 4 October).
   The technical estimates of v2 (`sec:sz-v2-blocks`) form a chapter of their own.
2. **The synthesis is dissolved.** `sec:kls-synthesis` now heads the comparison of the two
   proofs (`modules/11-proofs-compared.md`), with one provenance box
   (`subsec:proofs-provenance`) gathering the caveats previously scattered in the proof
   chapters. Old targets 1, 2 and 4 and the tensorization constraint moved into the map of
   alternative mechanisms (`modules/13-alternative-mechanisms.md`, `sec:frontier-atlas`);
   target 3 into the fixed-cut archive (`subsec:effective-rank`); target 5 and the
   methodological section of the v2 chapter (`sec:sz-v2-methodological-comparison`) left
   the manuscript and are preserved verbatim below.
3. **KLS after its proofs** (`modules/12-kls-after-proofs.md`, `sec:kls-after-proofs`):
   prose only, no new statement. Equivalent forms, consequences, the constants of the two
   proofs (neither is evaluated: `C_P ≤ 2CK` for BKL, `C_P ≤ 2^{85}𝒜` for v2 with 𝒜
   bounded by unevaluated constants), and the question of the best constant.
4. **The overview explains both proofs.** "How KLS was proved" (anchor
   `sec:kls-conversions` kept) replaces "Two conversions…": Letwin shortened, the
   criterion of v1, one page each on BKL (`subsec:kls-bkl-idea`) and v2
   (`subsec:kls-sz-v2-idea`). The six-family table moved from the atlas to the overview
   (`subsec:kls-reading-map`).
5. **Alternative mechanisms and archive.** Three living mechanisms (moment map, fixed
   eigenfunction, conditional fibers), presented by what each would add to the two proofs;
   the fixed cut and its technical chapters form the final part "Archive: the fixed cut".
6. **Statement titles are deferred.** Remaining legacy titles ("Product-simplex cone gate",
   "… implies KLS", …) are listed in `TODO-EDITORIAL-POST-KLS.md` §9 for a separate pass
   through editorial notes. `prf:remark` titles are prose and were updated in this pass.

*Observed.* After each step `check.py --statements` is identical to the baseline (178
statements) and `check.py` reports 0 errors.

Module renumbering: BKL 09→08, SZ v2 08→09 (technical part → new 10), synthesis 21→11,
atlas 10→13, moment map 11–15→14–18, localization prelude 16→19, fixed eigenfunction
17→20, conditional fibers 18→21, fixed cut 19–20→27–28, fixed-cut technical 27–35→29–37;
new 12. Anchors dropped with no remaining reference: `subsec:synthesis-targets`,
`subsec:synthesis-assessment`, `sec:sz-v2-methodological-comparison`.

## What resists

- **Possible statement on the constant (proposal only).** Chapter 12 defines
  $C_\star=\sup\CP/\norm{\Cov}_\op$ over log-concave measures and records
  $C_\star\ge4$, equality on the line, on products and on log-concave Dirichlet laws, and
  that a universal $\CMH\le4$ would give $C_\star=4$. Whether "$C_\star=4$" deserves a
  conjecture node depends on its status in the literature, not checked here.
- Classical sources missing from `references.bib`, so Chapter 12 states these consequences
  only qualitatively or through surveys: Eldan–Klartag 2011 (thin shell ⇒ slicing),
  Gromov–Milman (concentration), Kannan–Lovász–Simonovits 1997 and Lovász–Vempala
  (mixing of the random walks).
- Route `ap:sz-conditional-initialization` still names the comparison with the
  `(d+1)^2` startup, which is now methodology only (text below).

## Proposed next step

A human reading of the welcome page, the overview, Chapters 11 and 12 and the two
composition proofs of `conj:kls` before the `pages` workflow is dispatched; then the
statement-title pass of `TODO-EDITORIAL-POST-KLS.md` §9.

## Appendix: text removed from the manuscript

Preserved verbatim for the methodological record (TODO §8).

`````markdown
# Methodological text removed from the manuscript (writer's pass, 2026-10-06)

## From modules/09-song-zhang-v2.md, section `sec:sz-v2-methodological-comparison` (verbatim)

(sec:sz-v2-methodological-comparison)=
## What the earlier obstruction analysis identified

Our analysis of the first version separated an algebraic requirement from the estimates
needed to realize it. Summable logarithmic losses would keep the total
cost bounded, but small-degree initialization and admissible starting
depths also required control. It identified the uniform exponential
coefficient assertion as equivalent to KLS in
[](#prop:sz-exponential-coefficients-equivalence). Neither observation
provided an estimate establishing that assertion.

BKL supply a cumulant and suspension mechanism for the coefficient end
point; the second version of Song–Zhang develops finite blocks, retained coefficient caps and depth
control. In the second version the iterated quantity is the common coefficient radius.
The fixed numerical factor converting that radius to $C_P$ is paid once,
after every refinement. Thus the second version does not require a near-unit replacement
of the first-version spectral comparison at every repetition.

The coefficient transfer also has a different normalization: its exponent
is $d-1$, whereas the earlier conditional-startup question used an exponent
$d$ and a denominator $(d+1)^2$. Identifying the two requires estimates
for those factors throughout the moving degree range. Neither a common
end point nor summable-loss arithmetic proves such an identification.
Likewise the earlier obstruction to a retained positive error majorant
concerns those particular estimates; the new joint-frame and orbit-window
estimates change what is controlled.

These comparisons explain which missing estimates matter without claiming
priority for either proof mechanism. Identifying a sufficient condition
and proving it are different achievements. The BKL initialization
consequence [](#cor:bkl-uniform-conditional-initialization) retains its
BKL provenance and is not an input to the separate argument of the second version.

## From modules/11-proofs-compared.md (old synthesis), Target 5 (verbatim)

**Target 5 — compare the repeated-refinement estimates with the earlier questions.**
The factor $16^r$ and growing admissibility thresholds of the first-version iteration
are limitations of those estimates, not unresolved requirements in the
literature after the second version. Chapter [](#sec:sz-v2-proof) explains the source's
replacement: polynomial depth cost, a common coefficient radius, repeated
height reduction, and finally a summable cost for the repetitions.

The finite-chain construction [](#prop:sz-v2-finite-chain-blocks) controls
centering losses, normalization and energy for one inverse-gradient
family, uniformly in the number of retained coefficient bounds. The
outer profiles, summable costs and final composition complete the
argument. BKL's coefficient theorem is not an input to it.

The older conditional-startup and near-unit-comparison questions retain
their exact normalization. The second version refines a common coefficient radius and
pays its fixed spectral conversion once, after all refinements. It does
not need a near-unit multiplier for the first-version comparison at each repetition.
Comparing the coefficient transfers must also account for their different
degree exponents and the older denominator $(d+1)^2$.

The earlier analysis correctly distinguished summable-loss arithmetic from
its missing estimates and identified the exponential coefficient end point
as KLS-strength in [](#prop:sz-exponential-coefficients-equivalence). It did
not supply either new proof mechanism. Section

## From modules/11-proofs-compared.md, 'Which target first' (verbatim)

claim of priority or a claim that the source satisfies every earlier
proposed interface literally.

(subsec:synthesis-assessment)=

## From modules/13 (old atlas), 'Research priorities' item 1 (verbatim)

1. **Compare the polynomial estimates.** The second version of Song–Zhang supplies a repeated-refinement proof distinct from BKL, described in [](#sec:sz-v2-proof). The common finite-block estimates, outer profiles, summable costs and final composition have been checked here. No BKL coefficient bound enters this argument. The remaining comparison concerns the exact older conditional-startup and near-unit-comparison formulations, which differ from the new common-radius construction. The exponential characterization [](#prop:sz-exponential-coefficients-equivalence) identifies the end point but does not prove the required estimates. Target 5 of Section [](#subsec:synthesis-targets) explains this comparison.
`````
