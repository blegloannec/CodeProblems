#!/usr/bin/env python3

import sys

### max bipartite matching from tryalgo ###
def augment(u, bigraph, visit, match):
    for v in bigraph[u]:
        if not visit[v]:
            visit[v] = True
            if match[v] is None or augment(match[v], bigraph, visit, match):
                match[v] = u
                return True
    return False

def bip_match(bigraph, nU, nV):
    match = [None]*nV
    for u in range(nU):
        augment(u, bigraph, [False]*nV, match)
    return match
### ===== ###


def main():
    N = int(sys.stdin.readline())
    AB = []
    G = [[] for _ in range(N)]
    V = []
    Vnum = {}
    for u in range(N):
        a,b = map(int,sys.stdin.readline().split())
        AB.append((a,b))
        for v in (a+b, a-b, a*b):
            if v not in Vnum:
                Vnum[v] = len(V)
                V.append(v)
            G[u].append(Vnum[v])
    M = bip_match(G, N, len(V))
    Sol = [None]*N
    for v,u in enumerate(M):
        if u is not None:
            Sol[u] = V[v]
    if any(v is None for v in Sol):
        sys.stdout.write('impossible\n')
    else:
        for (a,b),c in zip(AB,Sol):
            op = next(op for d,op in ((a+b,'+'),(a-b,'-'),(a*b,'*')) if d==c)
            sys.stdout.write(f'{a} {op} {b} = {c}\n')

main()
