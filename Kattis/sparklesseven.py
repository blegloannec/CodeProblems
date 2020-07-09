#!/usr/bin/env python3

# ===== tryalgo's F-F ===== #
def _augment(graph, capacity, flow, val, u, target, visit):
    visit[u] = True
    if u == target:
        return val
    for v in graph[u]:
        cuv = capacity[u][v]
        if not visit[v] and cuv > flow[u][v]:
            res = min(val, cuv - flow[u][v])
            delta = _augment(graph, capacity, flow, res, v, target, visit)
            if delta > 0:
                flow[u][v] += delta
                flow[v][u] -= delta
                return delta
    return 0

def ford_fulkerson(graph, capacity, s, t):
    n = len(graph)
    flow = [[0] * n for _ in range(n)]
    INF = float('inf')
    while _augment(graph, capacity, flow, INF, s, t, [False] * n) > 0:
        pass
    return (flow, sum(flow[s]))
# ===== ===== #

S = 7
Name = ('Twilight Sparkle', 'Applejack', 'Rarity', 'Pinkie Pie', 'Fluttershy', 'Rainbow Dash', 'Spike')

def main():
    N = 2*S+2
    # 0 = source, 1..S = members, S+(1..S) = weaknesses, 2S+1 = sink
    # building capacities
    C = [[0]*N for _ in range(N)]
    for u in range(S):
        for v,c in enumerate(input().split()):
            if c=='1':
                C[1+u][1+S+v] = 1
    for v in range(S):
        C[1+S+v][N-1] = 1
    for u in range(S):
        C[0][1+u] = 1
    # building the graph
    G = [[] for _ in range(N)]
    for u in range(N):
        for v in range(u+1,N):
            if C[u][v]>0 or C[v][u]>0:
                G[u].append(v)
                G[v].append(u)
    # solution
    for k in range(1,S+1):
        # trying to solve the problem with k operations
        for u in range(S):
            C[0][1+u] = k
        F, flow = ford_fulkerson(G, C, 0, N-1)
        if flow==S:  # solution found
            O = [[] for _ in range(k)]
            for u in range(S):
                l = 0
                for v in range(S):
                    if F[1+u][1+S+v]>0:
                        O[l].append((u,v))
                        l += 1
            print(k)
            for o in O:
                print(len(o))
                for u,v in o:
                    print(Name[u], v+1)
            return
    print('IMPOSSIBLE')

main()
