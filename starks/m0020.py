#!/usr/bin/env python3
"""Independent checks of M-0020 (bt1_5d39cc28), own code, stdlib only.

(a) Bucket lemma |E(P,Q;A)| <= floor(b / max(1, A - c)): exhaustive over F_3 at n = 3 for every
    (f, g, P, Q) value vector and every A, plus random and adversarial (bucket-packed) cases over
    F_5, F_7, F_11, F_101. Only values of P and Q on the domain matter, so vectors suffice.
(b) Conditional transfer with the trivial cover (every pair of degree < k, E_sp empty) on small
    RS codes over F_7 and F_11: every bad z (by brute force over z and R) lies in the union of the
    E(P,Q;A); and the transfer's conclusion (outside the union every qualifying R has an exact
    pair) holds.
(c) Sharpness example over Q (exact Fractions): the n - A + 1 challenges z = -t_i are bad, and
    the total number of bad challenges of the line, by exhaustive enumeration of A-subsets.
(d) J_2 >= 8 K^3 on a grid (arithmetic only).
"""
import itertools, json, random
from fractions import Fraction


# ---------- (a) bucket lemma ----------
def E_size(f, g, P, Q, A, p):
    n = len(f)
    C = [i for i in range(n) if f[i] == P[i] and g[i] == Q[i]]
    c = len(C)
    b = sum(1 for i in range(n) if g[i] != Q[i])
    cnt = 0
    for z in range(p):
        S = [i for i in range(n) if (f[i] + z * g[i] - P[i] - z * Q[i]) % p == 0]
        if len(S) >= A and S != C:
            cnt += 1
    return cnt, b // max(1, A - c), b, c


def part_a():
    res = {"exhaustive_F3_n3_cases": 0, "violations": 0, "tight": 0}
    p, n = 3, 3
    vecs = list(itertools.product(range(p), repeat=n))
    for f in vecs:
        for g in vecs:
            for P in vecs:
                for Q in vecs:
                    for A in range(1, n + 1):
                        e, bound, _, _ = E_size(f, g, P, Q, A, p)
                        res["exhaustive_F3_n3_cases"] += 1
                        if e > bound:
                            res["violations"] += 1
                        elif e == bound and e > 0:
                            res["tight"] += 1
    rng = random.Random(1)
    rand_cases = rand_viol = 0
    for p in (5, 7, 11, 101):
        for _ in range(4000):
            n = rng.randrange(2, 10)
            P = [rng.randrange(p) for _ in range(n)]
            Q = [rng.randrange(p) for _ in range(n)]
            # adversarial: pick bucket values so many coordinates share one z_i
            zs = [rng.randrange(min(p, 3)) for _ in range(n)]
            f, g = [], []
            for i in range(n):
                mode = rng.randrange(4)
                if mode == 0:          # common agreement
                    f.append(P[i]); g.append(Q[i])
                elif mode == 1:        # g = Q, f != P: never agrees
                    g.append(Q[i]); f.append((P[i] + 1 + rng.randrange(p - 1)) % p)
                else:                  # g != Q with z_i = zs[i]
                    d = 1 + rng.randrange(p - 1)
                    g.append((Q[i] + d) % p)
                    f.append((P[i] - zs[i] * d) % p)
            for A in range(1, n + 1):
                e, bound, _, _ = E_size(f, g, P, Q, A, p)
                rand_cases += 1
                if e > bound:
                    rand_viol += 1
    res["random_adversarial_cases"] = rand_cases
    res["random_violations"] = rand_viol
    return res


# ---------- polynomial helpers over F_p ----------
def all_polys(k, p):
    return list(itertools.product(range(p), repeat=k))


def evals(coeffs, xs, p):
    return [sum(c * pow(x, j, p) for j, c in enumerate(coeffs)) % p for x in xs]


def interpolable_on(T, w, xs, k, p, table):
    """Is w restricted to T the restriction of a degree < k polynomial? (table: all codewords)"""
    key = tuple(w[i] for i in T)
    return key in table[tuple(T)]


def part_b():
    rng = random.Random(2)
    out = []
    for (p, n, k, A, lines) in ((7, 6, 2, 4, 150), (7, 6, 2, 3, 150), (11, 5, 2, 3, 30), (7, 7, 3, 5, 4)):
        xs = list(range(1, n + 1)) if n < p else list(range(n))
        polys = all_polys(k, p)
        code = [tuple(evals(c, xs, p)) for c in polys]
        restr = {}
        for r in range(0, n + 1):
            for T in itertools.combinations(range(n), r):
                restr[T] = {tuple(cw[i] for i in T) for cw in code}
        not_in_union = 0
        transfer_fail = 0
        total_bad = 0
        for _ in range(lines):
            # mix: random lines and lines near the code (more bad challenges)
            if rng.random() < 0.5:
                f = [rng.randrange(p) for _ in range(n)]
                g = [rng.randrange(p) for _ in range(n)]
            else:
                F0, G0 = rng.choice(code), rng.choice(code)
                f, g = list(F0), list(G0)
                for i in rng.sample(range(n), rng.randrange(1, n - k + 1)):
                    f[i] = rng.randrange(p)
                    g[i] = rng.randrange(p)
            union = set()
            for P in code:
                for Q in code:
                    Cset = [i for i in range(n) if f[i] == P[i] and g[i] == Q[i]]
                    for z in range(p):
                        S = [i for i in range(n) if (f[i] + z * g[i] - P[i] - z * Q[i]) % p == 0]
                        if len(S) >= A and S != Cset:
                            union.add(z)
            for z in range(p):
                w = [(f[i] + z * g[i]) % p for i in range(n)]
                bad = False
                for R in code:
                    T = tuple(i for i in range(n) if R[i] == w[i])
                    if len(T) >= A and not (interpolable_on(T, f, xs, k, p, restr)
                                            and interpolable_on(T, g, xs, k, p, restr)):
                        bad = True
                    if z not in union and len(T) >= A:
                        # transfer conclusion: R = P + zQ with (P, Q) exact on all of T
                        ok = any(all(P[i] == f[i] and Q[i] == g[i] for i in T)
                                 and all((P[i] + z * Q[i]) % p == R[i] for i in range(n))
                                 for P in code for Q in code)
                        if not ok:
                            transfer_fail += 1
                if bad:
                    total_bad += 1
                    if z not in union:
                        not_in_union += 1
        out.append({"p": p, "n": n, "k": k, "A": A, "lines": lines, "bad_total": total_bad,
                    "bad_not_in_union": not_in_union, "transfer_failures": transfer_fail})
    return out


# ---------- (c) sharpness over Q ----------
def q_interp_values(xs_all, idx, ys):
    xs = [xs_all[i] for i in idx]
    vals = []
    for x in xs_all:
        tot = Fraction(0)
        for i, xi in enumerate(xs):
            term = Fraction(ys[i])
            for j, xj in enumerate(xs):
                if j != i:
                    term *= Fraction(x - xj, xi - xj)
            tot += term
        vals.append(tot)
    return vals


def q_bad_challenges(xs, f, g, k, A):
    n = len(xs)
    bad = set()
    for S in itertools.combinations(range(n), A):
        base = list(S[:k])
        F = q_interp_values(xs, base, [f[i] for i in base])
        G = q_interp_values(xs, base, [g[i] for i in base])
        conds = [(f[i] - F[i], g[i] - G[i]) for i in S[k:]]
        cands, ok = None, True
        for a, b in conds:
            if b == 0:
                if a != 0:
                    ok = False
                    break
                continue
            z = -a / b
            if cands is None:
                cands = {z}
            elif z not in cands:
                ok = False
                break
        if not ok:
            continue
        if cands is None:
            cands = {-(f[i] - F[i]) / (g[i] - G[i]) for i in range(n) if g[i] != G[i]}
        for z in cands:
            T = [i for i in range(n) if f[i] + z * g[i] == F[i] + z * G[i]]
            if len(T) >= A and not all(f[i] == F[i] and g[i] == G[i] for i in T):
                bad.add(z)
    return bad


def part_c():
    out = []
    for n in (5, 6, 7, 8):
        for k in (2, 3):
            for A in range(k + 1, n + 1):
                xs = list(range(n))
                core = list(range(A - 1))
                f = [Fraction(0)] * n
                g = [Fraction(0)] * n
                t = {}
                for j, i in enumerate(range(A - 1, n)):
                    g[i] = Fraction(1)
                    f[i] = Fraction(j + 1)
                    t[i] = f[i]
                bad = q_bad_challenges(xs, f, g, k, A)
                claimed = {-t[i] for i in t}
                out.append({"n": n, "k": k, "A": A, "claimed": len(claimed),
                            "claimed_all_bad": claimed <= bad, "total_bad": len(bad)})
    return out


def part_d():
    worst = None
    for K in range(1, 60):
        tau = 2 * K
        for v in range(2, 8):
            for h in range(1, 6):
                for l in range(0, 5):
                    bcut = 1 + tau * (v - 1)
                    acut = l + tau * h
                    J2 = h * bcut ** 3 + 3 * v * acut * bcut ** 2
                    ratio = Fraction(J2, 8 * K ** 3)
                    if worst is None or ratio < worst:
                        worst = ratio
    return {"min_J2_over_8K3": float(worst), "holds": worst >= 1}


if __name__ == "__main__":
    print(json.dumps({"a": part_a(), "b": part_b(), "c": part_c(), "d": part_d()}, indent=1))
