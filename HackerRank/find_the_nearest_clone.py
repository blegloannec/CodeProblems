#!/usr/bin/env python3

from collections import deque

# BFS to find the shortest path between any two distinct nodes from a subset
# of vertices.
# Each vertex is possibly visited twice:
#  - the first time is a classic shortest path from any initial vertex u0
#    of the subset;
#  - the second time is a shortest path **from an initial vertex v0 != u0**.
def subset_bfs(U0):
    Dist = [[-1]*2 for _ in range(N)]
    From = [[None]*2 for _ in range(N)]
    inU0 = [False]*N
    for u in U0:
        Dist[u][0] = 0
        From[u][0] = u
        inU0[u] = True
    Q = deque([(u,0) for u in U0])
    while Q:
        u,bis = Q.popleft()
        if inU0[u] and bis:
            return Dist[u][1]
        for v in G[u]:
            if Dist[v][0]==-1:  # first visit
                assert bis==0
                Dist[v][0] = Dist[u][bis]+1
                From[v][0] = From[u][bis]
                Q.append((v,0))
            elif Dist[v][1]==-1 and From[v][0]!=From[u][bis]:  # second visit
                Dist[v][1] = Dist[u][bis]+1
                From[v][1] = From[u][bis]
                Q.append((v,1))
    return -1

if __name__=='__main__':
    N,M = map(int,input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    Color = list(map(int,input().split()))
    col0 = int(input())
    U0 = [u for u in range(N) if Color[u]==col0]
    print(subset_bfs(U0))
