#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def find(x):
    if T[x] is None:
        return x
    T[x] = find(T[x])
    return T[x]

def union(x, y):
    x0 = find(x)
    y0 = find(y)
    if x0==y0:
        return False
    T[y0] = x0
    return True

def tree_path(u0, uf):
    Pred = [None]*N
    S = [u0]
    while S:
        u = S.pop()
        if u==uf:
            break
        for v in G[u]:
            if v!=Pred[u]:  # as G is a tree
                Pred[v] = u
                S.append(v)
    Path = [uf]
    while Path[-1]!=u0:
        Path.append(Pred[Path[-1]])
    #Path.reverse()  # useless
    return Path

def main():
    global N,T,G
    N,M = map(int, input().split())
    E = [tuple(map(int, input().split())) for _ in range(M)]
    u0 = 0; uf = N-1
    # Max. Span. Tree until u0 and uf are connected
    SE = sorted(E, key=(lambda abc: abc[2]))
    T = [None]*N
    G = [[] for _ in range(N)]
    while find(u0) != find(uf):
        a,b,_ = SE.pop()
        if union(a, b):
            G[a].append(b)
            G[b].append(a)
    # DFS in the tree
    Path = tree_path(u0, uf)
    # Output edges to cut
    PathV = set(Path)
    PathE = set((Path[i-1],Path[i]) for i in range(1,len(Path)))
    Cut = []
    for i,(a,b,_) in enumerate(E):
        if (a in PathV or b in PathV) and \
           ((a,b) not in PathE and (b,a) not in PathE):
            Cut.append(i)
    if Cut:
        print(*Cut)
    else:
        print('none')

main()
