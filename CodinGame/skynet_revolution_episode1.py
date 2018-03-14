#!/usr/bin/env python3

# doing it the intended way

from collections import deque

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n,l,e = map(int,input().split())
G = [set() for _ in range(n)]
for _ in range(l):
    u,v = map(int,input().split())
    G[u].add(v)
    G[v].add(u)
E = [False]*n
for _ in range(e):
    E[int(input())] = True

def bfs_closest_exit(u0):
    P = [None]*n
    Q = deque([u0])
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if P[v]==None:
                P[v] = u
                if E[v]:
                    return (P[v],v)
                Q.append(v)

# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    u,v = bfs_closest_exit(si)
    G[u].remove(v)
    G[v].remove(u)
    print(u,v)
