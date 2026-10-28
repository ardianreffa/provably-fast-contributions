#!/usr/bin/env python3
"""Independent check of the level-16 kernel-lift cap (bp1_09ba872d), own code, stdlib only.

Setting: BabyBear, mu_16 = <zeta>, an activation point s, a kernel point y1, pool = the other 14.
A 9-subset Z of the pool is a member of a partner word v if v is interpolable on Z by degree < 8.

Checks, for many (s, y1, v):
  1. direct interpolation on every one of the 2,002 nine-sets  ==  the claimed linear criterion
     sum_{y in Z} y L_U(y) v(y) = 0  (U = mu_16 minus Z)  ==  the e_j(C) hyperplane form;
  2. distinct interpolants P of members: pairwise |Z cap Z'| <= 7, and #P <= 182;
  3. D_s = #distinct residuals v(s) - P(s), D_y1 = #distinct P(y1); both <= #P.
Also the Johnson-bound chain A(12,4,3) <= 20, A(13,4,4) <= 65, A(14,4,5) <= 182 and 65*182+1.
"""
import itertools, random, sys, json

p = 2013265921
g0 = 31
zeta = pow(g0, (p - 1) // 16, p)
assert pow(zeta, 16, p) == 1 and pow(zeta, 8, p) != 1, "zeta must have order 16"
MU = [pow(zeta, i, p) for i in range(16)]


def inv(a):
    return pow(a, p - 2, p)


def lagrange_eval(xs, ys, t):
    """Value at t of the interpolant of degree < len(xs)."""
    tot = 0
    for i, xi in enumerate(xs):
        num, den = 1, 1
        for j, xj in enumerate(xs):
            if j != i:
                num = num * (t - xj) % p
                den = den * (xi - xj) % p
        tot = (tot + ys[i] * num * inv(den)) % p
    return tot


def member_direct(Z, v):
    """Is v interpolable on Z (9 points) by degree < 8? Interpolate on 8, test the 9th."""
    xs = [MU[i] for i in Z]
    ys = [v[i] for i in Z]
    return lagrange_eval(xs[:8], ys[:8], xs[8]) == ys[8]


def poly_key(Z, v):
    """Identify the interpolant P by its values on all of mu_16 (degree < 8 from 8 points of Z)."""
    xs = [MU[i] for i in Z[:8]]
    ys = [v[i] for i in Z[:8]]
    return tuple(lagrange_eval(xs, ys, MU[t]) for t in range(16))


def crit_LU(Z, v):
    U = [i for i in range(16) if i not in Z]
    tot = 0
    for i in Z:
        y = MU[i]
        L = 1
        for u in U:
            L = L * (y - MU[u]) % p
        tot = (tot + y * L % p * v[i]) % p
    return tot == 0


def crit_hyperplane(C, pool, s, y1, v):
    """sum over the pool of y (y - s)(y - y1) v(y) prod_{c in C}(y - c): affine-linear in e_j(C)."""
    tot = 0
    for i in pool:
        y = MU[i]
        t = y * (y - MU[s]) % p * (y - MU[y1]) % p * v[i] % p
        for c in C:
            t = t * (y - MU[c]) % p
        tot = (tot + t) % p
    return tot == 0


def analyse(s, y1, v, check_criteria=True):
    pool = [i for i in range(16) if i not in (s, y1)]
    members = []
    mism = 0
    for Z in itertools.combinations(pool, 9):
        d = member_direct(Z, v)
        if check_criteria:
            C = [i for i in pool if i not in Z]
            if not (d == crit_LU(Z, v) == crit_hyperplane(C, pool, s, y1, v)):
                mism += 1
        if d:
            members.append(Z)
    polys = {}
    for Z in members:
        polys.setdefault(poly_key(Z, v), []).append(Z)
    keys = list(polys)
    # pairwise intersection over all member pairs with different interpolants
    worst = 0
    for a in range(len(keys)):
        for b in range(a + 1, len(keys)):
            for Z1 in polys[keys[a]]:
                for Z2 in polys[keys[b]]:
                    worst = max(worst, len(set(Z1) & set(Z2)))
    Ds = len({(v[s] - P[s]) % p for P in keys})
    Dy1 = len({P[y1] for P in keys})
    return {"members": len(members), "distinct_P": len(keys), "D_s": Ds, "D_y1": Dy1,
            "max_meet_distinct_P": worst, "criterion_mismatches": mism}


def johnson():
    # A(12,4,3): each point lies in at most floor(11/2) triples pairwise meeting in <= 1 point
    a1243 = (12 * (11 // 2)) // 3
    a1344 = (13 * a1243) // 4
    a1445 = (14 * a1344) // 5
    return a1243, a1344, a1445, 65 * a1445 + 1


def main():
    out = {"johnson": johnson()}
    # Binomials y^8 - c y^15 at y1 = index 0, every s, every c in mu_16 (the posted family).
    best = None
    rows = []
    y1 = 0
    for s in range(1, 16):
        for ci in range(16):
            c = MU[ci]
            v = [(pow(MU[i], 8, p) - c * pow(MU[i], 15, p)) % p for i in range(16)]
            r = analyse(s, y1, v, check_criteria=(s in (1, 4)))
            r.update({"s": s, "c_index": ci})
            rows.append(r)
            if best is None or r["D_s"] > best["D_s"]:
                best = r
    out["binomial_best"] = best
    out["binomial_max_distinct_P"] = max(r["distinct_P"] for r in rows)
    out["binomial_max_meet"] = max(r["max_meet_distinct_P"] for r in rows)
    out["binomial_criterion_mismatches"] = sum(r["criterion_mismatches"] for r in rows)
    out["binomial_bound_violations"] = sum(1 for r in rows if max(r["D_s"], r["D_y1"], r["distinct_P"]) > 182)
    # Random partners and degenerate partners (support on few pool points), random (s, y1).
    rng = random.Random(20261028)
    rnd = []
    for trial in range(int(sys.argv[1]) if len(sys.argv) > 1 else 40):
        s, y1 = rng.sample(range(16), 2)
        kind = trial % 4
        if kind == 0:
            v = [rng.randrange(p) for _ in range(16)]
        elif kind == 1:   # degree < 8 plus a sparse perturbation: many members
            base = [rng.randrange(p) for _ in range(8)]
            v = [sum(base[j] * pow(MU[i], j, p) for j in range(8)) % p for i in range(16)]
            for i in rng.sample(range(16), 2):
                v[i] = (v[i] + rng.randrange(1, p)) % p
        elif kind == 2:   # random binomial y^a - c y^b
            a, b = rng.sample(range(16), 2)
            c = MU[rng.randrange(16)]
            v = [(pow(MU[i], a, p) - c * pow(MU[i], b, p)) % p for i in range(16)]
        else:             # random trinomial with mu_16 coefficients
            ex = rng.sample(range(16), 3)
            co = [MU[rng.randrange(16)] for _ in ex]
            v = [sum(cc * pow(MU[i], e, p) for cc, e in zip(co, ex)) % p for i in range(16)]
        r = analyse(s, y1, v)
        r.update({"kind": ["random", "deg<8+2 errors", "binomial", "trinomial"][kind]})
        rnd.append(r)
    out["random_trials"] = len(rnd)
    out["random_criterion_mismatches"] = sum(r["criterion_mismatches"] for r in rnd)
    out["random_max_meet"] = max(r["max_meet_distinct_P"] for r in rnd)
    out["random_max_distinct_P"] = max(r["distinct_P"] for r in rnd)
    out["random_max_members"] = max(r["members"] for r in rnd)
    out["random_bound_violations"] = sum(1 for r in rnd if max(r["D_s"], r["D_y1"], r["distinct_P"]) > 182)
    out["random_by_kind"] = {k: max((r["members"], r["distinct_P"], r["D_s"]) for r in rnd if r["kind"] == k)
                             for k in {r["kind"] for r in rnd}}
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
