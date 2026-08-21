"""finum CLI:  python -m finum selftest
              python -m finum run --target TARGET [--seed N] [--out PATH] [--heavy]"""
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
                    help="artifact path (default research/runs/<timestamp>-<target>.jsonl)")
    pr.add_argument("--heavy", action="store_true",
                    help="run expensive independent gates (currently kls-loc only)")

    args = p.parse_args(argv)

    if args.cmd == "selftest":
        from .selftest import selftest
        return selftest()

    if args.cmd == "run":
        from .run import run
        if args.heavy and args.target != "kls-loc":
            p.error("--heavy is currently supported only for --target kls-loc")
        cfg = {"heavy": True} if args.heavy else {}
        path = run(args.target, seed=args.seed, out=args.out, **cfg)
        print(f"wrote {path}")
        return 0

    return 2


if __name__ == "__main__":
    sys.exit(main())
