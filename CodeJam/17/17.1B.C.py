#!/usr/bin/env python3

from heapq import *

# Code *almost* identical to the one submitted during the contest.
# Got a WA on large testcase during contest due to a stupid floating
# point error: the maximal distance filtering was initially done in terms
# of time, i.e. AFTER dividing distances by speed, which causes critical
# floating point errors...

def dijkstra(graph, S, source=0, target=None):
    n = len(graph)
    black = [False] * n
    dist = [float('inf')] * n
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        dist_node, node = heappop(heap)
        if not black[node]:
            black[node] = True
            if node == target:
                break
            for (neighbor,weight) in graph[node]:
                dist_neighbor = dist_node + weight
                if dist_neighbor < dist[neighbor]:
                    dist[neighbor] = dist_neighbor
                    heappush(heap, (dist_neighbor, neighbor))
    return dist

def floyd_warshall(weight):
    V = range(len(weight))
    for k in V:
        for u in V:
            for v in V:
                weight[u][v] = min(weight[u][v], weight[u][k]+weight[k][v])

def main():
    T = int(input())
    for t in range(1,T+1):
        N,Q = map(int,input().split())
        E,S = [],[]
        for _ in range(N):
            Ei,Si = map(int,input().split())
            E.append(Ei)
            S.append(Si)
        G = [[] for _ in range(N)]
        for u in range(N):
            L = list(map(int,input().split()))
            for v in range(N):
                if L[v]>=0:
                    G[u].append((v,L[v]))
        D = []
        for u in range(N):
            Du = dijkstra(G,S,u)
            for v in range(N): # filtering
                if Du[v]>E[u]:
                    Du[v] = float('inf')
                else:
                    # ONLY NOW we can divide by the speed without
                    # getting critical floating point errors!
                    Du[v] /= S[u]
            D.append(Du)
        floyd_warshall(D)
        res = []
        for _ in range(Q):
            u,v = map(int,input().split())
            u -= 1
            v -= 1
            res.append(D[u][v])
        print('Case #%d: %s' % (t,' '.join(map(str,res))))

main()
