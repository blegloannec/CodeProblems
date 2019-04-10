#!/usr/bin/env pypy2

def dist2(i,j):
    return (A[i][0]-B[j][0])**2 + (A[i][1]-B[j][1])**2

def augment(u, bigraph, visit, match):
    for v in bigraph[u]:
        if not visit[v]:
            visit[v] = True
            if match[v] is None or augment(match[v], bigraph, visit, match):
                match[v] = u
                return True
    return False

def max_bipartite_matching(G):
    #N = len(G)
    #M = max(max(L) if L else -1 for L in G) + 1
    match = [None]*M
    for u in range(N):
        augment(u, G, [False]*M, match)
    return match

def solvable(E):
    G = [[] for _ in range(N)]
    for (_,i,j) in E:
        G[i].append(j)
    match = max_bipartite_matching(G)
    size = sum(int(u is not None) for u in match)
    return size>=K

if __name__=='__main__':
    N,M,K = map(int,raw_input().split())
    A = [tuple(map(int,raw_input().split())) for _ in xrange(N)]
    B = [tuple(map(int,raw_input().split())) for _ in xrange(M)]
    E = sorted((dist2(i,j),i,j) for i in range(N) for j in range(M))
    l,r = K,len(E)
    while l<r:
        m = (l+r)//2
        if solvable(E[:m]):
            r = m
        else:
            l = m+1
    print(E[l-1][0])
