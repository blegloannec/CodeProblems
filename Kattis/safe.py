#!/usr/bin/env python3

# BFS is definitely the intended way here
# (though algebraic approach might be interesting too...)

from collections import deque

N = 3
B = 4

# neighborhood precomp
Neigh = [[] for _ in range(N*N)]
for i in range(N):
    for j in range(N):
        u = N*i+j
        for vj in range(N):
            Neigh[u].append(N*i+vj)
        for vi in range(N):
            if vi!=i:
                Neigh[u].append(N*vi+j)

def bfs(U):
    F = tuple(0 for _ in range(N*N))
    D = {U:0}
    Q = deque([U])
    while Q:
        U = Q.popleft()
        if U==F:
            return D[F]
        for u in range(N*N):
            V = list(U)
            for v in Neigh[u]:
                V[v] = (V[v]+1)%B
            V = tuple(V)
            if V not in D:
                D[V] = D[U]+1
                Q.append(V)
    return -1

def main():
    I = []
    for _ in range(N):
        I += list(map(int,input().split()))
    I = tuple(I)
    print(bfs(I))

main()
