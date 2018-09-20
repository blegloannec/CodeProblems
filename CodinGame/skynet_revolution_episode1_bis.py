#!/usr/bin/env python3

# alternative (less efficient) heuristic for the last achievement...

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

def bfs_access(u0):
    Dist = {u0:0}
    Q = deque([u0])
    a = d = 0
    while Q:
        u = Q.popleft()
        if E[u]:
            a += 1
            d += Dist[u]
        for v in G[u]:
            if v not in Dist:
                Dist[v] = Dist[u]+1
                Q.append(v)
    return a,d

def smallest_access(si):
    smin = float('inf'),0
    for u in range(n):
        for v in list(G[u]):
            if u<v:
                G[u].remove(v)
                G[v].remove(u)
                s = bfs_access(si)
                if s<smin:
                    smin = s
                    emin = (u,v)
                G[u].add(v)
                G[v].add(u)
    return emin

# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    u = v = None
    # immediate danger: the virus is next to an exit
    for w in G[si]:
        if E[w]:
            u,v = si,w
            break
    # otherwise, we use the heuristic
    if u is None:
        u,v = smallest_access(si)
    G[u].remove(v)
    G[v].remove(u)
    print(u,v)
