#!/usr/bin/env python3

### max bipartite matching from tryalgo ###
def augment(u, bigraph, visit, match):
    for v in bigraph[u]:
        if not visit[v]:
            visit[v] = True
            if match[v] is None or augment(match[v], bigraph, visit, match):
                match[v] = u
                return True
    return False

def bip_match(bigraph, nU, nV):
    match = [None]*nV
    for u in range(nU):
        augment(u, bigraph, [False]*nV, match)
    return match
### ===== ###


def build_graph(Vmin):
    graph = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if Grid[i][j]>=Vmin:
                graph[i].append(j)
    return graph

def main():
    global N, Grid
    N = int(input())
    Grid = [list(map(int,input().split())) for _ in range(N)]
    Val = set()
    for L in Grid:
        Val |= set(L)
    Val = sorted(Val)
    l, r = 0, len(Val)-1
    while l<r:
        m = (l+r+1)//2
        graph = build_graph(Val[m])
        match = bip_match(graph,N,N)
        if None not in match:  # there exists a perfect matching
            l = m
        else:
            r = m-1
    print(Val[l])

main()
