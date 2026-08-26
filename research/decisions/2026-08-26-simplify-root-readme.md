# Simplify the root README

- **Date:** 2026-08-26
- **Type:** repository documentation
- **Scope:** `README.md`
- **Mathematical effect:** none

## Problem

The root README mixed stable repository orientation with a detailed research-status summary and a
long literal directory listing. The status prose duplicated the ledgers and could drift, while the
layout had recently contained a stale entry for the removed `LEAN_DESIGN.md` file.

## Decision

Keep the root README responsible for three tasks only:

1. describe the manuscript and its three parts;
2. provide the LaTeX build command; and
3. route readers to the manuscript, research, proof, numerical, and contribution-contract planes.

Derive the live research frontier with `research/check_ledger.py status` instead of narrating it
in mutable prose. Replace the literal directory tree with links to existing canonical entry
points.

## Validation

- Every relative link in `README.md` resolves.
- `python3 -B research/check_ledger.py`: 2 ledgers, 170 nodes, 632 labels, 0 errors.
- `python3 -B research/check_agents.py`: 13 roles, 0 errors.
- `python3 -B -m unittest discover -s research/tests -p 'test_*.py'`: 41 tests pass.
- `git diff --check` is clean.
