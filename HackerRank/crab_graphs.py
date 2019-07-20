#!/usr/bin/env python3

# intuitive yet really non-trivial reduction to a max-flow problem
# cf editorial https://www.hackerrank.com/challenges/crab-graphs/editorial
# for technical details of the proof

### ford-fulkerson from tryalgo 
def add_reverse_arcs(graph, capac=None):
    for u, _ in enumerate(graph):
        for v in graph[u]:
            if u not in graph[v]:
                if type(graph[v]) is list:
                    graph[v].append(u)
                    if capac:
                        capac[v][u] = 0
                else:
                    assert type(graph[v]) is dict
                    graph[v][u] = 0

def _augment(graph, capacity, flow, val, u, target, visit):
    visit[u] = True
    if u == target:
        return val
    for v in graph[u]:
        cuv = capacity[u][v]
        if not visit[v] and cuv > flow[u][v]:  # reachable arc
            res = min(val, cuv - flow[u][v])
            delta = _augment(graph, capacity, flow, res, v, target, visit)
            if delta > 0:
                flow[u][v] += delta            # augment flow
                flow[v][u] -= delta
                return delta
    return 0

def ford_fulkerson(graph, capacity, s, t):
    add_reverse_arcs(graph, capacity)
    n = len(graph)
    flow = [[0] * n for _ in range(n)]
    INF = float('inf')
    while _augment(graph, capacity, flow, INF, s, t, [False] * n) > 0:
        pass                         # work already done in _augment
    return (flow, sum(flow[s]))      # flow network, amount of flow
###

def main():
    C = int(input())
    for _ in range(C):
        N,T,M = map(int,input().split())
        N2 = 2*N+2
        Graph = [[] for _ in range(N2)]
        Capacity = [[None]*N2 for _ in range(N2)]
        s, t = 0, N2-1
        for u in range(1,N+1):
            ul, ur = 2*u-1, 2*u
            Graph[s].append(ul)
            Capacity[0][ul] = T
            Graph[ur].append(t)
            Capacity[ur][t] = 1
        for _ in range(M):
            u,v = map(int,input().split())
            ul, ur = 2*u-1, 2*u
            vl, vr = 2*v-1, 2*v
            Graph[ul].append(vr)
            Capacity[ul][vr] = 1
            Graph[vl].append(ur)
            Capacity[vl][ur] = 1
        print(ford_fulkerson(Graph, Capacity, s, t)[1])

main()
