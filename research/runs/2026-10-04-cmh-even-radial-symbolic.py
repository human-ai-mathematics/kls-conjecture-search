# /// script
# requires-python = ">=3.11"
# dependencies = ["sympy", "numpy", "scipy"]
# ///
"""Exact finite-degree boundary CMH variation for ap:c-solenoidal-perturbation.

    uv run research/runs/2026-10-04-cmh-even-radial-symbolic.py

This writes <same name>.jsonl beside itself: a
provenance line, then one record per result. Format: SPECIFICATION.md, Formats → Run.
Nothing it prints certifies anything.
"""
import json
import platform
import random
import subprocess
from importlib.metadata import version
from pathlib import Path

SEED = 0                    # fixed once the artifact is cited
PACKAGES: list[str] = ["sympy", "numpy", "scipy"]    # the dependencies above, by name, e.g. ["numpy", "mpmath"]
OUT = Path(__file__).with_suffix(".jsonl")


def provenance(**params) -> dict:
    """The seed, the parameters, the commit (dirty if uncommitted) and the versions."""
    def git(*args: str) -> str:
        return subprocess.run(["git", *args], capture_output=True, text=True,
                              cwd=OUT.parent).stdout.strip()
    return {"provenance": {"seed": SEED, **params,
                           "git_commit": git("rev-parse", "HEAD") or None,
                           "dirty": bool(git("status", "--porcelain")),
                           "python": platform.python_version(),
                           "versions": {name: version(name) for name in PACKAGES}}}


def run(rng: random.Random) -> list[dict]:
    """Exact matrices for ap:c-solenoidal-perturbation, numerical eigenspaces."""
    import sympy as sp
    import numpy as np
    from scipy.linalg import eigh
    b,s,t,q=sp.symbols("b s t q")
    def expect(expr):
        result=0
        for (i,j),coef in sp.Poly(sp.expand(expr),s,t).terms():
            if j%2==0:
                result+=coef*sp.rf(b,i)/sp.Integer(j+1)
        return sp.factor(result)
    records=[]
    for d in range(1,5):
        indices=[(k,j) for k in range(1,d+1) for j in range(k+1)]
        gs=[s**k*t**j for k,j in indices]
        us=[sp.Matrix([k*s**k*t**j,s**k*(k*t**(j+1)+b*sp.Rational(j,2)*(1-t*t)*t**(j-1))]) for k,j in indices]
        ls=[-k*s**k*t**j+s**(k-1)*(k*(k-1+b)*t**j+b*sp.Rational(j,2)*((j-1)*t**(j-2)-(j+1)*t**j)) for k,j in indices]
        N=sp.Matrix(len(gs),len(gs),lambda i,j:expect(us[i][0]*us[j][0]/b+3*us[i][1]*us[j][1]/(b*(b+1))))
        D=sp.Matrix(len(gs),len(gs),lambda i,j:expect(ls[i]*ls[j]))
        N0=N.subs(b,2);D0=D.subs(b,2)
        N1=N.diff(b).subs(b,2);D1=D.diff(b).subs(b,2)
        vals,vec=eigh(np.array(N0,float),np.array(D0,float))
        top=vals[-1]; mask=np.abs(vals-top)<1e-8; V=vec[:,mask]
        slopes,W=eigh(V.T@(np.array(N1,float)-top*np.array(D1,float))@V)
        polys=[]; exact_branches=[]
        root=[None,sp.Integer(2),sp.Integer(3),2+sp.sqrt(2),(5+sp.sqrt(5))/2][d]
        for parity in [0,1]:
            ix=[i for i,(_,j) in enumerate(indices) if j%2==parity]
            A=N0.extract(ix,ix)-q*D0.extract(ix,ix)
            polys.append(str(sp.factor(A.det())))
            null=A.subs(q,root).nullspace()
            assert len(null)==1
            v=null[0].applyfunc(sp.simplify)
            den=sp.simplify((v.T*D0.extract(ix,ix)*v)[0])
            numprime=sp.simplify((v.T*N1.extract(ix,ix)*v)[0]/den)
            denprime=sp.simplify((v.T*D1.extract(ix,ix)*v)[0]/den)
            slope=sp.simplify(numprime-root*denprime)
            exact_branches.append(dict(parity=parity,root=str(root),optimizer=str(sp.expand(sum(v[k]*gs[i] for k,i in enumerate(ix)))),beta_derivative=str(slope),Nprime_D0normalized=str(numprime),Dprime_D0normalized=str(denprime)))
        records.append(dict(degree=d,indices=indices,N0=str(N0),D0=str(D0),N1=str(N1),D1=str(D1),characteristic_even_odd=polys,exact_branches=exact_branches,top=float(top),multiplicity=int(mask.sum()),beta_slopes=slopes.tolist(),epsilon_second=2*float(slopes[-1]),optimizers=(V@W).tolist()))
    return records


if __name__ == "__main__":
    records = [provenance(degrees=[1,2,3,4],family="beta=2+epsilon^2"), *run(random.Random(SEED))]
    OUT.write_text("".join(json.dumps(record) + "\n" for record in records))
    print(OUT.read_text(), end="")
