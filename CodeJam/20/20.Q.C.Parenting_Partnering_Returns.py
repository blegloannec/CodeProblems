#!/usr/bin/env python3

def bipartite(G):
    N = len(G)
    C = [None]*N
    for u0 in range(N):
        if C[u0] is None:
            C[u0] = 0
            Q = [u0]
            while Q:
                u = Q.pop()
                for v in G[u]:
                    if C[v] is None:
                        C[v] = 1-C[u]
                        Q.append(v)
                    elif C[v]==C[u]:
                        return None
    return C

def main():
    T = int(input())
    for t in range(1,T+1):
        N = int(input())
        A = [tuple(map(int,input().split())) for _ in range(N)]
        G = [[] for _ in range(N)]
        for i,(s1,e1) in enumerate(A):
            for j in range(i+1,N):
                s2,e2 = A[j]
                if max(s1,s2)<min(e1,e2):
                    G[i].append(j)
                    G[j].append(i)
        C = bipartite(G)
        res = ''.join('CJ'[c] for c in C) if C else 'IMPOSSIBLE'
        print('Case #{}: {}'.format(t,res))

main()
