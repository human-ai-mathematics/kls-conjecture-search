"""Exact sphere-moment algebraic countermodel used by the CMH regression."""
from __future__ import annotations

import math

import numpy as np


def countermodel_params(m: int):
    d = m / math.sqrt(2 * m - 1)
    return d, 1.0 - d / m


def etr_bhbh_closed(B: np.ndarray, m: int) -> float:
    """Closed-form ``E Tr(B H B H)`` from exact sphere moments."""
    d, c = countermodel_params(m)
    a = float(B[0, 0])
    r = np.asarray(B[0, 1:], float)
    D = np.asarray(B[1:, 1:], float)
    trD, trD2 = float(np.trace(D)), float(np.trace(D @ D))
    return (a * a
            + (2 * d / m) * a * trD
            + 2 * (c + 2 * d / m) * float(r @ r)
            + (c * c + 2 * c * d / m + 2 * d * d / (m * (m + 2))) * trD2
            + (d * d / (m * (m + 2))) * trD * trD)


def _hh_moment_tensor(m: int) -> np.ndarray:
    d, _ = countermodel_params(m)
    n = m + 1
    Im, In = np.eye(m), np.eye(n)
    tensor = np.einsum("ab,cd->abcd", In, In)
    tensor[0, 1:, 0, 1:] += d * Im / m
    tensor[0, 1:, 1:, 0] += d * Im / m
    tensor[1:, 0, 0, 1:] += d * Im / m
    tensor[1:, 0, 1:, 0] += d * Im / m
    d_ijkl = np.einsum("ij,kl->ijkl", Im, Im)
    d_ikjl = np.einsum("ik,jl->ijkl", Im, Im)
    d_iljk = np.einsum("il,jk->ijkl", Im, Im)
    tensor[1:, 1:, 1:, 1:] += (-(d ** 2 / m ** 2) * d_ijkl
                               + d ** 2 * (d_ijkl + d_ikjl + d_iljk) / (m * (m + 2)))
    return tensor


def etr_bhbh_tensor(B: np.ndarray, m: int) -> float:
    return float(np.einsum("ij,kl,jkli->", B, B, _hh_moment_tensor(m)))


def countermodel_sectors(m: int):
    """Normalized ``E Tr(BHBH)/Tr(B^2)`` in each ``O(m)``-invariant sector."""
    d, c = countermodel_params(m)
    vector = 1.0 + d / m
    traceless_direct = c * c + 2 * c * d / m + 2 * d * d / (m * (m + 2))
    traceless_closed = 1.0 + (m - 2) / ((2 * m - 1) * (m + 2))
    stuff = m * traceless_closed + m * d * d / (m + 2)
    quad_form = np.array([[1.0, -d], [-d, 2.0 * m - stuff]])
    worst = 0.0
    for a, t in ((1.0, 0.0), (0.0, 1.0), (1.0, 1.0), (d, 1.0),
                 (-2.0, 0.7), (3.0, -1.3)):
        B = np.zeros((m + 1, m + 1))
        B[0, 0] = a
        B[1:, 1:] = t * np.eye(m)
        deficit = 2.0 * float(np.trace(B @ B)) - etr_bhbh_closed(B, m)
        worst = max(worst, abs(deficit - (a - d * t) ** 2))
    return dict(m=m, d=d, c=c, one_plus_d=1.0 + d,
                vector_sector=vector, traceless_sector=traceless_direct,
                traceless_sector_closed_form=traceless_closed,
                traceless_formula_residual=abs(traceless_direct - traceless_closed),
                scalar_sector_max=2.0,
                scalar_perfect_square_residual=float(worst),
                scalar_discriminant=float(np.linalg.det(quad_form)),
                all_sectors_at_most_2=bool(vector <= 2.0 and traceless_direct <= 2.0),
                EH2_11=1.0 + d, EH2_11_exceeds_4=bool(1.0 + d > 4.0))


def countermodel_tensor_crosscheck(m: int) -> float:
    rng = np.random.default_rng(0)
    worst = 0.0
    for _ in range(4):
        B = rng.standard_normal((m + 1, m + 1))
        B = 0.5 * (B + B.T)
        worst = max(worst, abs(etr_bhbh_closed(B, m) - etr_bhbh_tensor(B, m)))
    return float(worst)
