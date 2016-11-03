#!/usr/bin/env python3

from collections import deque

n, a, b, k, m = [int(i) for i in input().split()]

def bfs(start,dest):
    dist = [-1 for _ in range(n+1)]
    dist[start] = 0
    Q = deque([start])
    while Q:
        u = Q.popleft()
        if u==dest:
            return dist[u]
        if u+a<=n and dist[u+a]<0:
            dist[u+a] = dist[u]+1
            Q.append(u+a)
        if u-b>0 and dist[u-b]<0:
            dist[u-b] = dist[u]+1
            Q.append(u-b)
    return 'IMPOSSIBLE'

print(bfs(k,m))
