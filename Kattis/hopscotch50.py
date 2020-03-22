#!/usr/bin/env python3

INF = float('inf')

def hop(i,j):
    if H[i][j] is None:
        if G[i][j]==K:
            d = 0
        else:
            d = INF
            for u,v in V[G[i][j]+1]:
                d = min(d, abs(i-u)+abs(j-v)+hop(u,v))
        H[i][j] = d
    return H[i][j]

def main():
    global N, K, G, V, H
    N,K = map(int,input().split())
    G = [list(map(int,input().split())) for _ in range(N)]
    V = [[] for _ in range(K+1)]
    for i in range(N):
        for j in range(N):
            V[G[i][j]].append((i,j))
    H = [[None]*N for _ in range(N)]
    for k in range(K,0,-1):
        for i,j in V[k]:
            hop(i,j)
    d = INF
    for i,j in V[1]:
        d = min(d, hop(i,j))
    print('-1' if d==INF else d)

main()
