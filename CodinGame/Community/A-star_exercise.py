#!/usr/bin/env python3

# https://en.wikipedia.org/wiki/A*_search_algorithm
# "If the heuristic h satisfies the additional condition h(x) <= d(x,y) + h(y)
# for every edge (x,y) of the graph (where d denotes the length of that edge),
# then h is called monotone, or consistent. In such a case, A* can be implemented
# more efficiently - roughly speaking, no node needs to be processed more than once
# (see closed set below) - and A* is equivalent to running Dijkstra's algorithm with
# the reduced cost d'(x,y) = d(x,y) + h(y) - h(x)."
# => this is what we do here

from heapq import *

INF = float('inf')

def Astar(Graph,H,s,t):
    N = len(Graph)
    G = [INF]*N
    F = [INF]*N
    #Pred = [None]*N
    seen = [False]*N
    G[s] = 0
    F[s] = G[s]+H[s]
    Q = [(F[s],s)]
    while Q:
        f,u = heappop(Q)
        if seen[u]:
            continue
        print(u,f)  # output trace
        if u==t:
            break
        seen[u] = True
        for v,c in Graph[u]:
            if not seen[v] and G[u]+c+H[v]<F[v]:
                G[v] = G[u]+c
                F[v] = G[v]+H[v]
                #Pred[v] = u
                heappush(Q,(F[v],v))
    # usual output, not required here
    #Path = []
    #u = t
    #while u!=None:
    #    Path.append(u)
    #    u = Pred[u]
    #return Path[::-1]

def main():
    N,M,s,t = map(int,input().split())
    H = list(map(int,input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        u,v,c = map(int,input().split())
        G[u].append((v,c))
        G[v].append((u,c))
    Astar(G,H,s,t)

main()
