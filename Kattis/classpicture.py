#!/usr/bin/env python3

import sys

# Held-Karp
def tsp(G, Memo, used, last):
    if used==0:
        return -1
    key = (used,last)
    if key not in Memo:
        Memo[key] = None
        for prev in G[last]:
            if (used>>prev)&1 and tsp(G, Memo, used^(1<<prev), prev) is not None:
                Memo[key] = prev
                break
    return Memo[key]

def main():
    while True:
        try:
            N = int(sys.stdin.readline())
        except:
            break
        Names = sorted(sys.stdin.readline().strip() for _ in range(N))
        G = [[True]*N for _ in range(N)]
        M = int(sys.stdin.readline())
        for _ in range(M):
            u,v = sys.stdin.readline().split()
            u = Names.index(u)
            v = Names.index(v)
            G[u][v] = G[v][u] = False
        G = [[v for v in range(N) if G[u][v]] for u in range(N)]
        full = (1<<N)-1
        Memo = {}
        u = 0
        while u<N and tsp(G, Memo, full^(1<<u), u) is None:
            u += 1
        if u==N:
            print('You all need therapy.')
        else:
            Path = []
            used = full
            while u>=0:
                Path.append(u)
                used ^= 1<<u
                u = tsp(G, Memo, used, u)
            print(' '.join(Names[i] for i  in Path))

main()
