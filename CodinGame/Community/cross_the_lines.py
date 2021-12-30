#!/usr/bin/env python3

from collections import *
from math import atan2

# connected components
def dfs(G,u,seen,comp):
    seen.add(u)
    comp.append(u)
    for v in G[u]:
        if v not in seen:
            dfs(G,v,seen,comp)

def components(G):
    C = []
    seen = set()
    for u in G:
        if u not in seen:
            comp = []
            dfs(G,u,seen,comp)
            C.append({u:G[u] for u in comp})
    return C

# computes the faces of a planar embedding
def faces(G):
    GI = {}
    for u in G:
        # sorting edges by their angle around each vertex
        G[u].sort(key=(lambda v: atan2(v[1]-u[1],v[0]-u[0])))
        # edges -> index dict.
        GI[u] = {G[u][i]:i for i in range(len(G[u]))}
    seen = set()  # seen oriented edges
    faces = []
    for u in G:
        for v in G[u]:
            if (u,v) not in seen:
                a,b = u,v
                face = [a]
                seen.add((a,b))
                while b!=u:
                    face.append(b)
                    # we turn around b and follow the next edge
                    a,b = b,G[b][(GI[b][a]+1)%len(G[b])]
                    seen.add((a,b))
                faces.append(face)
    return faces

# builds the dual graph from faces
def dual(F):
    DE = defaultdict(list)
    for i in range(len(F)):
        for j in range(len(F[i])):
            e = (F[i][j],F[i][(j+1)%len(F[i])])
            DE[tuple(sorted(e))].append(i)
    D = [[] for _ in range(len(F))]
    i = 0  # edge index
    for e in DE:
        assert(len(DE[e])==2)
        u,v = DE[e]
        D[u].append((v,i))
        D[v].append((u,i))
        i += 1
    return D

# computing the shortest tour of all edges by a BFS
# in the augmented graph whose vertices are
# (current original vertex, already used edges mask)
def edges_tour_bfs(D):
    Dist = {}
    u0 = 0
    edges_count = sum(len(V) for V in D)//2
    full = (1<<edges_count)-1
    Dist[u0,0] = 0
    Q = deque([(u0,0)])
    while Q:
        u,used = Q.popleft()
        if u==u0 and used==full:
            break
        for v,e in D[u]:
            vused = used|(1<<e)
            if (v,vused) not in Dist:
                Dist[v,vused] = Dist[u,used]+1
                Q.append((v,vused))
    return Dist[u0,full]

def main():
    N = int(input())
    G = defaultdict(list)
    for _ in range(N):
        x1,y1,x2,y2 = map(int,input().split())
        G[x1,y1].append((x2,y2))
        G[x2,y2].append((x1,y1))
    res = sum(edges_tour_bfs(dual(faces(C))) for C in components(G))
    print(res)

main()
