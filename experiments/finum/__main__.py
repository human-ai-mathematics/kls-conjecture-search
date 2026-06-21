"""finum CLI:  python -m finum selftest
              python -m finum run --target {A1,A2,A3,A4,A5,kls} [--seed N] [--out PATH]"""
from __future__ import annotations

import argparse
import sys


def main(argv: list[str] | None = None) -> int:
    from .targets import REGISTRY

    p = argparse.ArgumentParser(prog="finum", description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("selftest", help="every target's calibration reproduces its closed form, or fail")

    pr = sub.add_parser("run", help="run a target's battery -> a research/runs artifact")
    pr.add_argument("--target", default="A1", choices=sorted(REGISTRY),
                    help="Part II target (A1-A5) or Part III route-gating (kls)")
    pr.add_argument("--seed", type=int, default=0)
    pr.add_argument("--out", default=None,
                    help="artifact path (default research/runs/<date>-<target>.jsonl)")

    args = p.parse_args(argv)

    if args.cmd == "selftest":
        from .selftest import selftest
        return selftest()

    if args.cmd == "run":
        from .run import run
        path = run(args.target, seed=args.seed, out=args.out)
        print(f"wrote {path}")
        return 0

    return 2


if __name__ == "__main__":
    sys.exit(main())
