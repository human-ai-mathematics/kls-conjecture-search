"""The ball base: the radial moment-map ODE, solved by quadrature (directional).

For ``K = B_R`` the moment potential of ``Unif(K)`` is radial, ``lambda(y) = Lambda(|y|)``,
and the moment-map condition ``(grad lambda)_# e^{-lambda} = Unif(K)`` reads, in radial
form,

    Lambda'(s)^m = nu(B_s) = |S^{m-1}| int_0^s t^{m-1} e^{-Lambda(t)} dt,   Lambda'(0) = 0,

because the map ``y -> Lambda'(|y|) y/|y|`` sends the sphere of radius ``s`` to the sphere
of radius ``r = Lambda'(s)`` and preserves enclosed mass.  Differentiating gives
``m Lambda'^{m-1} Lambda'' = |S^{m-1}| s^{m-1} e^{-Lambda}``.  The Hessian of a radial
potential is ``Lambda'' u^u^T + (Lambda'/s)(I - u^u^T)``, so the canonical Stein kernel of
``Unif(K)`` at the target radius ``r = Lambda'(s)`` is

    tau_B(u) = alpha(r) u^ u^T + beta_perp(r) (I - u^ u^T),
    alpha = Lambda''(s),   beta_perp = Lambda'(s)/s.

Normalisation is *not* imposed.  Integrating from ``Lambda(0) = 0`` produces the kernel of
the uniform law on the ball of radius ``R = Lambda'(infinity)``, which is a legitimate
centered convex base; the gate pencil is invariant under the rescaling that would carry it
to the unit ball, so no normalisation constant is chased.

The state vector integrates ``(Lambda, F = Lambda'^m)`` together with the seven radial
moments the gate matrix needs, using the exact identity ``F'(s) ds`` for the radial law of
``U``.  Everything in this module is **quadrature**: adaptive Runge-Kutta with a paired
tolerance-refinement check, hence `directional` evidence only, never `exact`.

Closed-form calibrations: ``m = 1`` must reproduce ``tau = (R^2 - r^2)/2`` with ``R = 2``
(the solution is ``Lambda' = 2 tanh s``), the Stein normalisation must give
``E[alpha] + (m-1) E[beta_perp] = E|U|^2 = m R^2/(m+2)``, and the ``m = 1`` transverse gate
value must equal the cube-cone closed form of cor:cube-cone-gate-zero at ``n = 2``.
"""
from __future__ import annotations

import math

import numpy as np
from scipy.integrate import solve_ivp

#: Radial moments accumulated along the ODE, in state order after (Lambda, F).
MOMENT_KEYS = ("r2", "r4", "alpha", "alpha2", "r2alpha", "beta_perp", "beta_perp2")


def _omega(m: int) -> float:
    """Volume of the unit ball of ``R^m``."""
    return math.pi ** (m / 2) / math.gamma(m / 2 + 1)


def _rhs(m: int):
    omega = _omega(m)
    surface = m * omega

    def rhs(s, y):
        lam, F = y[0], y[1]
        Fp = surface * s ** (m - 1) * math.exp(-lam)
        w = F ** (1.0 / m)
        alpha = Fp / (m * F ** ((m - 1) / m))
        beta_perp = w / s
        r2 = w * w
        return [w, Fp,
                r2 * Fp, r2 * r2 * Fp, alpha * Fp, alpha * alpha * Fp,
                r2 * alpha * Fp, beta_perp * Fp, beta_perp * beta_perp * Fp]

    return rhs


def _initial(m: int, s0: float):
    omega = _omega(m)
    c = omega ** (1.0 / m)
    lam = c * s0 * s0 / 2
    F = omega * s0 ** m * (1 - m * c * s0 * s0 / (2 * (m + 2)))
    mass = omega * s0 ** m
    tail = m * omega * s0 ** (m + 2) / (m + 2)
    return [lam, F,
            c * c * tail, c ** 4 * m * omega * s0 ** (m + 4) / (m + 4),
            c * mass, c * c * mass, c ** 3 * tail,
            c * mass, c * c * mass]


def radial_profile(m: int, s0: float = 1e-6, rtol: float = 1e-12, atol: float = 1e-14,
                   tail_tol: float = 1e-15, s_max_cap: float = 4096.0):
    """Solve the radial moment-map ODE for ``Unif(B_R)`` and return its radial moments."""
    if m < 1:
        raise ValueError("ball base needs m >= 1")
    rhs = _rhs(m)
    s_max = 20.0
    while True:
        sol = solve_ivp(rhs, (s0, s_max), _initial(m, s0), method="DOP853",
                        rtol=rtol, atol=atol, dense_output=True)
        if not sol.success:
            raise ArithmeticError(f"radial moment-map ODE failed for m={m}: {sol.message}")
        y = sol.y[:, -1]
        tail = rhs(s_max, y)[1] * s_max / y[1]
        if tail < tail_tol or s_max >= s_max_cap:
            break
        s_max *= 2
    lam, F = y[0], y[1]
    R = F ** (1.0 / m)
    moments = {key: y[2 + i] / F for i, key in enumerate(MOMENT_KEYS)}
    return {"m": m, "R": R, "mass": F, "s_max": s_max, "tail_estimate": tail,
            "lambda_at_s_max": lam, "solution": sol, "rtol": rtol, "atol": atol,
            **{f"E_{key}": moments[key] for key in MOMENT_KEYS}}


def stein_trace_residual(profile) -> float:
    """``E[alpha] + (m-1) E[beta_perp] - E|U|^2``: the Stein normalisation, relative."""
    m, R = profile["m"], profile["R"]
    got = profile["E_alpha"] + (m - 1) * profile["E_beta_perp"]
    want = m * R * R / (m + 2)
    return abs(got - want) / abs(want)


def one_dimensional_kernel_residual(profile, probes: int = 9) -> float:
    """``m = 1``: compare ``alpha(r)`` along the solution with ``(R^2 - r^2)/2``."""
    if profile["m"] != 1:
        raise ValueError("this calibration is one-dimensional")
    sol, R = profile["solution"], profile["R"]
    worst = 0.0
    for s in np.linspace(0.05, 3.0, probes):
        lam, F = sol.sol(s)[0], sol.sol(s)[1]
        r = F
        alpha = 2.0 * math.exp(-lam)                       # Lambda'' = |S^0| e^{-Lambda}
        want = (R * R - r * r) / 2
        worst = max(worst, abs(alpha - want) / abs(want))
    return worst


def gate_ratios(profile, beta: int):
    """Axis and transverse normalized gate values of the cone over ``B_R``.

    ``Sigma_U = sigma^2 I`` with ``sigma^2 = E|U|^2/m``; the base is symmetric so the
    axis and transverse sectors decouple and

        axis       = 1 + n/beta                                   (exact, prop:cone-linear-sector)
        transverse = [ (beta+1) sigma^2
                       + ( E[(r^2 + beta alpha)^2]
                           + (m-1) beta^2 E[beta_perp^2] ) / (m sigma^2) ]
                     / ( beta (beta+1) sigma^2 ).
    """
    m = profile["m"]
    n = m + 1
    sigma2 = profile["E_r2"] / m
    e_sq = (profile["E_r4"] + 2 * beta * profile["E_r2alpha"]
            + beta * beta * profile["E_alpha2"])
    numerator = ((beta + 1) * sigma2
                 + (e_sq + (m - 1) * beta * beta * profile["E_beta_perp2"])
                 / (m * sigma2))
    transverse = numerator / (beta * (beta + 1) * sigma2)
    return {"m": m, "n": n, "beta": beta, "R": profile["R"], "sigma_sq": sigma2,
            "axis": 1.0 + n / beta, "transverse": transverse,
            "lambda_max": max(1.0 + n / beta, transverse)}
