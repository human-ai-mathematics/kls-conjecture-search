"""numerics: list targets, run fast checks, or emit a numerical research artifact."""
from __future__ import annotations

import argparse
import sys


def main(argv: list[str] | None = None) -> int:
    from .targets import REGISTRY

    p = argparse.ArgumentParser(prog="numerics", description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list", help="show targets and their available run profiles")

    pc = sub.add_parser("check", help="run fast target-owned calibration/regression checks")
    pc.add_argument("target", nargs="?", choices=sorted(REGISTRY))
    pc.add_argument("--seed", type=int, default=7)

    # Kept because CLAUDE.md and historical exploration logs use this spelling.
    sub.add_parser("selftest", help="compatibility alias for 'check'")

    pr = sub.add_parser("run", help="run a target's battery -> a research/runs artifact")
    pr.add_argument("target", nargs="?", choices=sorted(REGISTRY),
                    help="target id (required unless legacy --target is used)")
    pr.add_argument("--target", dest="legacy_target", choices=sorted(REGISTRY) + ["kls-loc"],
                    help=argparse.SUPPRESS)
    pr.add_argument("--profile", default="standard",
                    help="target-owned run profile (default: standard; see 'numerics list')")
    pr.add_argument("--seed", type=int, default=0)
    pr.add_argument("--out", default=None,
                    help="artifact path (default research/runs/<timestamp>-<target>.jsonl)")
    pr.add_argument("--heavy", action="store_true", help=argparse.SUPPRESS)

    args = p.parse_args(argv)

    if args.cmd == "list":
        for name, spec in REGISTRY.items():
            mode = "stochastic" if spec.stochastic else "deterministic"
            print(f"{name:14} {mode:13} profiles={','.join(spec.profiles)}  {spec.summary}")
        return 0

    if args.cmd in {"check", "selftest"}:
        from .selftest import selftest
        return selftest(target=getattr(args, "target", None), seed=getattr(args, "seed", 7))

    if args.cmd == "run":
        from .artifact import run, confine_to_runs
        if args.target and args.legacy_target:
            p.error("give the target once, either positionally or with legacy --target")
        target = args.target or args.legacy_target
        if target == "kls-loc":
            target = "loc-engine"
        if target is None:
            p.error("run requires a target; see 'numerics list'")
        profile = "full" if args.heavy else args.profile
        try:
            out = confine_to_runs(args.out) if args.out else None
            path = run(target, seed=args.seed, profile=profile, out=out)
        except ValueError as exc:
            p.error(str(exc))
        print(f"wrote {path}")
        return 0

    return 2


if __name__ == "__main__":
    sys.exit(main())
