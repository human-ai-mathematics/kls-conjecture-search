---
numbering:
  enumerator: "19.%s"
---

(sec:localization-prelude)=
# Prelude: what stochastic localization does, and what it costs

The fixed cut and the fixed eigenfunction share a language, and this section is that language, at the level of detail needed to follow either approach's argument and to see where it stops. It states no identity precisely and proves nothing. The exact process, the SDEs, the Itô calculations, the two-colour notation, the Riccati and Stein identities, the covariance estimates and the model geometries are in the shared technical foundations (Sections [](#sec:notation), [](#sec:riccati), [](#sec:covariance-tech) and [](#sec:models)) and, for the mass martingale and the Stein dictionary, among the fixed-cut chapters (Sections [](#sec:mass-martingale) and [](#sec:stein-dictionary)); each is linked below at the point where it is first needed. A reader willing to take the mechanism on trust can go directly from here to Section [](#sec:spectral-approach) or Section [](#sec:introduction).

(subsec:prelude-process)=
## The process, and why one would want it

The difficulty in KLS is that a log-concave measure can be badly conditioned in a way no single observable sees. Stochastic localization is a way of *improving* the measure continuously while keeping track of what the improvement costs.

One runs a measure-valued process $p_t$, started at $\mu$, in which the density is multiplied by a Gaussian factor driven by a Brownian motion: informally, at time $t$ the measure has been tilted by $e^{\inner{\theta_t}{x}-t|x|^2/2}$ with $\theta_t$ a martingale. Three things happen at once, and all three matter.

(1) **The measure becomes strongly log-concave.** The quadratic factor $e^{-t|x|^2/2}$ makes $p_t$ at least $t$-strongly log-concave, so by Brascamp–Lieb its Poincaré constant is at most $1/t$. Waiting is therefore *free progress*: at any time $t$, the localized measure is as good as a Gaussian of variance $1/t$. Formally this is [](#eq:BL-cap).

(2) **The measure is preserved on average.** $p_t$ is a martingale in the measure: $\E p_t=\mu$ for every $t$. Nothing is lost by running the process; the information is redistributed, not destroyed. This is what makes step (3) legitimate.

(3) **The covariance moves, and can move badly.** The conditional covariance $A_t=\Cov(p_t)$ obeys its own SDE, [](#eq:cov-sde), whose drift is not sign-definite. This is the only place a cost is incurred, and the whole of both approaches is about paying it.

(subsec:prelude-transfer)=
## Transferring an isoperimetric statement back

The reason (2) is worth having is that isoperimetry transfers. Fix a would-be bottleneck set $E$ and follow its mass $m_t=p_t(E)$. Because $p_t$ is a measure martingale, $m_t$ is a bounded martingale, so it converges; and its quadratic variation is exactly an integral of the correlation between $\one_E$ and the localization direction. Two readings of the same fact drive the two approaches.

*If the mass stays balanced for a while*, then at that time the localized measure is both $t$-strongly log-concave and still genuinely cut by $E$, and a strongly log-concave measure with a balanced cut has boundary. Integrating that back through the martingale gives a lower bound on $\mu^+(E)$, which is a Cheeger statement about $\mu$ itself. This is [](#lem:survival-implies-kls), and its stopped form, [](#thm:centroid-implies-kls), is the exact bridge the fixed-cut approach consumes.

*If the mass is identified too quickly* — $m_t$ rushing to $0$ or $1$ — then the quadratic variation was large, which means the cut was strongly correlated with the localization direction, which is information about the geometry rather than a failure. The fixed-cut approach is the attempt to show that the second case cannot happen for *every* balanced cut at once.

The fixed-eigenfunction approach changes one object and nothing else: it follows $M_t(f)=\E_{p_t}f$ for a fixed near-first eigenfunction $f$ instead of $m_t=\E_{p_t}\one_E$. The SDE is the same shape, with $\Cov_{p_t}(X,f)$ in place of the set correlation, and the payoff is that the tensor orientation of $f$ survives, where a set indicator has already discarded it.

(subsec:prelude-riccati)=
## Source against damping: how to read the Riccati equation

Everything technical in the two approaches is a contest between two terms, and it is worth naming them before meeting them. Along the process, the scalar quantity the argument actually tracks obeys an equation of the form

$$
\dd r_t=\dd M_t+(S_t-D_t)\dd t ,
$$

a martingale increment plus a drift split into exactly one positive *source* $S_t$ and one coercive *damping* $D_t$. This is [](#thm:scalar-riccati); the matrix identity behind it is [](#lem:matrix-riccati), and both are derived in Section [](#sec:riccati).

The source is where the argument can lose. It measures how strongly the localization direction is correlated with the object being followed, and Section [](#sec:stein-dictionary) gives it a Stein representation — [](#lem:stein-vs-source) converts between a Stein norm and the source on the tight window — which is what makes it estimable at all. The damping is coercive, $D_t\gtrsim r_t^2$, so a bounded source is *absorbed*: the process cannot run away. Every argument in either approach is, in the end, an attempt to absorb the source into the damping for long enough.

The gap between what can be absorbed and what can be estimated has a name, and it is the same gap in both approaches: control is available at *trace* scale and needed at *operator* scale. Section [](#sec:stein-dictionary) states that operator-to-trace gap explicitly, and [](#conj:trace-upgrade) in Section [](#sec:open) is the fixed cut's version of it.

(subsec:prelude-warning)=
## The warning that constrains both approaches

One thing must be carried into both approaches from Section [](#sec:kls-remaining), because it rules out the argument a reader is most likely to try to construct.

> *There is no uniform bound on $\norm{A_t}_\op$ along the path, even for measures that satisfy KLS.* [](#prop:covariance-spike) exhibits the counterexample, and it is a product of centered exponentials — a measure that is dimension-free by tensorization.

So an argument may not simply bound the covariance better. It must either follow an object that notices when a spike is harmless — the fixed cut follows one cut, the fixed eigenfunction one eigenfunction, and both retain structure that $\norm{A_t}_\op$ has thrown away — or leave the method entirely, which is what the moment-map and conditional-fiber approaches do. The covariance technology of Section [](#sec:covariance-tech) is correspondingly a *small-time* theory: it controls the covariance for a short while, not forever, and the two localization approaches are built to need only that.

Product measures are the standing stress test for exactly this reason, and Section [](#sec:models) collects them alongside the Gaussian model, where the covariance is deterministic, damping is active and the excess vanishes identically. The two models bracket the problem: whatever a proposal does, it must be right on both.

(subsec:prelude-onward)=
## Where to go from here

Section [](#sec:qcts) states the static input the fixed-cut approach consumes and the two-tail obstruction that limits what it can supply; it sits among the shared foundations but is worth reading before the fixed-cut chapters, because it is an obstruction, not a tool. Section [](#sec:spectral-approach) then opens the fixed-eigenfunction approach and Section [](#sec:introduction) the fixed-cut approach, each with a summary in the same format.
