"""Channel 1(a): the one-dimensional anisotropic-bootstrap matrices, in exact rational form.

In one dimension the canonical moment-map Hessian in target coordinates is the Stein kernel
``tau``, so with the target standardized to variance one

    N = E[tau^2],   D = E[tau (tau')^2],   R = N - D.

Two independent exact identities are checked here, and they are what pins the index placement of
``D`` under the source/target change of variables ``partial_{y_a} H = H_{ab} partial_{x_b} H``:

1.  ``N = 2 D + E[H^3 V'']`` where ``V = -log rho`` is the *target* potential.  This is the
    one-dimensional specialization of the probe's ``N = D + R`` with
    ``R = int H (A + Q) d eta``, ``A = H^2 (V'' o grad psi)`` and ``Q = (partial_y H)^2/H^2``:
    the ``Q`` reservoir contributes exactly ``D`` and the ``A`` reservoir exactly ``E[H^3 V'']``.
2.  ``N - 1 <= D`` (Brascamp-Lieb), the scalar shadow of the probe's certified ``N - I <= D``.

Consequence, recorded because it is the cleanest exact statement this channel produces: for every
log-concave law on the line ``V'' >= 0``, hence ``R = D + E[H^3 V''] >= D``, i.e. ``R >= N/2``
holds on the line, with equality exactly on the log-affine densities (uniform, one-sided
exponential).  One dimension therefore *cannot* refute the sharp candidate; only genuinely
multi-dimensional instances can.  That is why this channel is a calibration anchor, not a test.
"""
from __future__ import annotations

from fractions import Fraction


def rising(a: Fraction, k: int) -> Fraction:
    out = Fraction(1)
    for j in range(k):
        out *= a + j
    return out


# ---------------------------------------------------------------------------------------
# tiny exact polynomial helper: dict {degree: Fraction}
# ---------------------------------------------------------------------------------------

def pmul(f, g):
    out: dict[int, Fraction] = {}
    for df, cf in f.items():
        for dg, cg in g.items():
            out[df + dg] = out.get(df + dg, Fraction(0)) + cf * cg
    return {d: c for d, c in out.items() if c}


def padd(f, g, scale: Fraction = Fraction(1)):
    out = dict(f)
    for d, c in g.items():
        out[d] = out.get(d, Fraction(0)) + scale * c
    return {d: c for d, c in out.items() if c}


def pscale(f, scale: Fraction):
    return {d: c * scale for d, c in f.items() if c * scale}


def pdiff(f):
    return {d - 1: c * d for d, c in f.items() if d}


def pexpect(f, moment) -> Fraction:
    return sum((c * moment(d) for d, c in f.items()), Fraction(0))


# ---------------------------------------------------------------------------------------
# exact families
# ---------------------------------------------------------------------------------------

def _assemble(tau, moment, variance: Fraction, a_reservoir_poly):
    """``(N, D, A)`` from a rational ``tau`` and the polynomial ``tau^3 V''``."""
    tau_prime = pdiff(tau)
    s4 = variance * variance
    n = pexpect(pmul(tau, tau), moment) / s4
    d = pexpect(pmul(tau, pmul(tau_prime, tau_prime)), moment) / s4
    a = pexpect(a_reservoir_poly, moment) / s4
    return n, d, a


def gaussian_instance():
    return {
        "name": "gaussian", "family": "gaussian",
        "parameters": {"mean": 0, "variance": 1},
        "tau": "tau = 1",
        "N": Fraction(1), "D": Fraction(0), "A_term": Fraction(1),
        "identity_note": "V'' = 1 and tau = 1, so N = 2D + E[tau^3 V''] reads 1 = 0 + 1.",
    }


def gamma_instance(shape: int):
    """``Gamma(a, 1)`` centred and standardized: ``tau_W(w) = w``, ``V''(w) = (a-1)/w^2``."""
    a = Fraction(shape)

    def moment(k: int) -> Fraction:
        return rising(a, k)

    tau = {1: Fraction(1)}
    a_poly = {1: a - 1}                       # tau^3 V'' = w^3 (a-1)/w^2 = (a-1) w
    n, d, at = _assemble(tau, moment, a, a_poly)
    return {
        "name": f"gamma-a{shape}", "family": "gamma",
        "parameters": {"shape": shape, "scale": 1, "centered_and_standardized": True},
        "tau": "tau_W(w) = w on the raw Gamma variable",
        "N": n, "D": d, "A_term": at,
        "identity_note": "V''(w) = (a-1)/w^2, so tau^3 V'' = (a-1) w is polynomial. "
                         "a = 1 is the centred one-sided exponential.",
    }


def beta_instance(a_par: int, b_par: int):
    """``Beta(a, b)`` centred and standardized: ``tau_W(w) = w(1-w)/A``, ``A = a+b``."""
    a, b = Fraction(a_par), Fraction(b_par)
    total = a + b

    def moment(k: int) -> Fraction:
        return rising(a, k) / rising(total, k)

    w = {1: Fraction(1)}
    omw = {0: Fraction(1), 1: Fraction(-1)}
    tau = pscale(pmul(w, omw), 1 / total)
    variance = a * b / (total * total * (total + 1))
    w3 = pmul(w, pmul(w, w))
    omw3 = pmul(omw, pmul(omw, omw))
    # tau^3 V'' = ((a-1) w (1-w)^3 + (b-1) w^3 (1-w)) / A^3
    a_poly = padd(pscale(pmul(w, omw3), a - 1), pscale(pmul(w3, omw), b - 1))
    a_poly = pscale(a_poly, 1 / total ** 3)
    n, d, at = _assemble(tau, moment, variance, a_poly)
    name = "uniform" if (a_par, b_par) == (1, 1) else f"beta-{a_par}-{b_par}"
    return {
        "name": name, "family": "beta",
        "parameters": {"alpha": a_par, "beta": b_par, "centered_and_standardized": True},
        "tau": "tau_W(w) = w(1-w)/(a+b)",
        "N": n, "D": d, "A_term": at,
        "identity_note": "V'' = (a-1)/w^2 + (b-1)/(1-w)^2; tau^3 V'' is polynomial. "
                         "Beta(1,1) is the uniform interval; Beta(a,b) is Dir(a,b) on Delta_1.",
    }


def laplace_instance():
    """Two-sided Laplace with variance one, ``b^2 = 1/2``, ``tau(x) = b(|x| + b)``.

    ``V'' = 2 delta_0 / b`` is a measure, so the ``A`` reservoir is evaluated analytically:
    ``E[tau^3 V''] = tau(0)^3 * 2 rho(0)/b = b^6 * 2 * (1/(2b)) / b = b^4 = 1/4``.
    """
    return {
        "name": "laplace", "family": "laplace",
        "parameters": {"location": 0, "scale": "1/sqrt(2)"},
        "tau": "tau(x) = b(|x| + b), b = 1/sqrt(2)",
        "N": Fraction(5, 4), "D": Fraction(1, 2), "A_term": Fraction(1, 4),
        "identity_note": "V'' carries an atom at 0; the A reservoir is evaluated analytically as "
                         "b^4 = 1/4. The identity N = 2D + A still holds exactly.",
    }


ONE_D_GAMMA_SHAPES = (1, 2, 5, 20)
ONE_D_BETA_PARAMETERS = ((1, 1), (1, 2), (1, 5), (1, 20), (2, 2), (2, 5), (3, 7))
RHO_BETAS = (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(1))


def one_d_instances(gamma_shapes=ONE_D_GAMMA_SHAPES, beta_parameters=ONE_D_BETA_PARAMETERS):
    rows = [gaussian_instance()]
    rows.extend(gamma_instance(a) for a in gamma_shapes)
    rows.extend(beta_instance(a, b) for a, b in beta_parameters)
    rows.append(laplace_instance())
    for row in rows:
        n, d, at = row["N"], row["D"], row["A_term"]
        row["R"] = n - d
        row["identity_residual"] = n - 2 * d - at
        row["sharp_margin"] = row["R"] - n / 2                    # R - N/2, must be >= 0
        row["brascamp_lieb_margin"] = d - (n - 1)                 # D - (N - I), must be >= 0
        row["rho_star"] = {str(beta): (row["R"] + beta) / n for beta in RHO_BETAS}
    return rows


def float_row(row: dict) -> dict:
    return {
        "instance": row["name"], "family": row["family"],
        "parameters": row["parameters"], "tau_formula": row["tau"],
        "N": float(row["N"]), "D": float(row["D"]), "R": float(row["R"]),
        "N_fraction": str(row["N"]), "D_fraction": str(row["D"]), "R_fraction": str(row["R"]),
        "A_reservoir_fraction": str(row["A_term"]),
        "identity_residual_fraction": str(row["identity_residual"]),
        "identity_holds_exactly": bool(row["identity_residual"] == 0),
        "sharp_margin": float(row["sharp_margin"]),
        "sharp_margin_fraction": str(row["sharp_margin"]),
        "sharp_candidate_holds": bool(row["sharp_margin"] >= 0),
        "brascamp_lieb_margin_fraction": str(row["brascamp_lieb_margin"]),
        "brascamp_lieb_holds": bool(row["brascamp_lieb_margin"] >= 0),
        "rho_star": {k: float(v) for k, v in row["rho_star"].items()},
        "rho_star_fraction": {k: str(v) for k, v in row["rho_star"].items()},
        "note": row["identity_note"],
    }


def gate_zero_r1_crosscheck() -> list[tuple[str, float, float]]:
    """``N`` here must equal ``R1`` of the certified ``cmh-gate-zero`` battery, law by law."""
    from ..cmh_gate_zero import one_d_laws

    by_name = {law["name"]: float(law["r1_exact_fraction"]) for law in one_d_laws()}
    rows = []
    for row in one_d_instances():
        name = row["name"]
        if name in by_name:
            rows.append((name, float(row["N"]), by_name[name]))
    rows.append(("exponential-centered", float(gamma_instance(1)["N"]),
                 by_name["exponential-centered"]))
    for b in (1, 2, 5, 20):
        rows.append((f"beta-1-{b}", float(beta_instance(1, b)["N"]), by_name[f"beta-1-{b}"]))
    return rows
