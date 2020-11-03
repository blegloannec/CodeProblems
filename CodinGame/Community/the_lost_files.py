#!/usr/bin/env python3

from collections import defaultdict

E = int(input())
G = defaultdict(list)
for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

C = F = 0
Seen = set()
for u0 in G:
    if u0 not in Seen:  # DFS from u0
        C += 1
        cv = ce = 0
        Seen.add(u0)
        S = [u0]
        while S:
            u = S.pop()
            cv += 1
            ce += len(G[u])
            for v in G[u]:
                if v not in Seen:
                    Seen.add(v)
                    S.append(v)
        # Euler's formula: v - e + f = 2
        F += 1 - cv + ce//2
print(C, F)
