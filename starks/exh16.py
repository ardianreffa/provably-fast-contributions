#!/usr/bin/env python3
"""Exhaustive bad-challenge count, from the definition, for the free-point line at n = 16 (h = 1).

k = 8, A = 10 on mu_16 in BabyBear. Every polynomial with >= A agreements is determined by an
A-subset S of its agreement set, so enumerating all C(16, 10) = 8,008 subsets finds every bad z.
Writes the bad challenges as a kit instance (witness = k points of the agreement set).
Usage: exh16.py s y1 c_index out.json [seed]
"""
import itertools, json, random, sys

p = 2013265921
zeta = pow(31, (p - 1) // 16, p)
MU = [pow(zeta, i, p) for i in range(16)]
n, k, A = 16, 8, 10


def inv(a):
    return pow(a, p - 2, p)


def interp_values(idx, ys):
    """Values on all of mu_16 of the interpolant of degree < len(idx) through (MU[idx], ys)."""
    xs = [MU[i] for i in idx]
    w = []
    for i, xi in enumerate(xs):
        den = 1
        for j, xj in enumerate(xs):
            if j != i:
                den = den * (xi - xj) % p
        w.append(ys[i] * inv(den) % p)
    out = []
    for t in range(n):
        x = MU[t]
        if t in idx:
            out.append(ys[idx.index(t)])
            continue
        tot = 0
        for i in range(len(xs)):
            num = 1
            for j in range(len(xs)):
                if j != i:
                    num = num * (x - xs[j]) % p
            tot = (tot + w[i] * num) % p
        out.append(tot)
    return out


def bad_challenges(f, g):
    bad = {}
    for S in itertools.combinations(range(n), A):
        base = list(S[:k])
        F = interp_values(base, [f[i] for i in base])
        G = interp_values(base, [g[i] for i in base])
        rest = S[k:]
        a = [(f[i] - F[i]) % p for i in rest]
        b = [(g[i] - G[i]) % p for i in rest]
        cands = None  # None = every z
        ok = True
        for aj, bj in zip(a, b):
            if bj == 0:
                if aj != 0:
                    ok = False
                    break
                continue
            z = (-aj) * inv(bj) % p
            if cands is None:
                cands = {z}
            elif z not in cands:
                ok = False
                break
        if not ok:
            continue
        if cands is None:
            # f and g both interpolable on S; only points off S where g != G can make z bad
            cands = {(-(f[i] - F[i])) * inv((g[i] - G[i]) % p) % p
                     for i in range(n) if (g[i] - G[i]) % p}
        for z in cands:
            T = [i for i in range(n) if (f[i] + z * g[i] - F[i] - z * G[i]) % p == 0]
            if len(T) < A:
                continue
            joint = all(f[i] == F[i] and g[i] == G[i] for i in T)
            if not joint:
                bad.setdefault(z, T[:k])
    return bad


def main():
    s, y1, ci = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    rng = random.Random(int(sys.argv[5]) if len(sys.argv) > 5 else 7)
    c = MU[ci]
    v = [(pow(MU[i], 8, p) - c * pow(MU[i], 15, p)) % p for i in range(n)]
    a1, b1, alpha, beta = (rng.randrange(1, p) for _ in range(4))
    f = [alpha * v[i] % p for i in range(n)]
    g = [beta * v[i] % p for i in range(n)]
    f[s] = (a1 + alpha * v[s]) % p
    g[s] = (b1 + beta * v[s]) % p
    f[y1] = rng.randrange(p)          # the free point x* (h = 1: the kernel fibre is x* alone)
    g[y1] = rng.randrange(p)
    bad = bad_challenges(f, g)
    inst = {"p": p, "k": k, "A": A, "domain": MU, "f": f, "g": g,
            "challenges": [{"z": z, "witness": w} for z, w in sorted(bad.items())]}
    json.dump(inst, open(sys.argv[4], "w"))
    print(json.dumps({"s": s, "y1": y1, "c_index": ci, "exhaustive_bad": len(bad),
                      "z0_present": (-alpha * inv(beta)) % p in bad}))


if __name__ == "__main__":
    main()
