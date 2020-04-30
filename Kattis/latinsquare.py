#!/usr/bin/env python3


### max bipartite matching ###
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


def latin(Grid):
    V = set(range(1,N+1))-set(Grid[0])
    for v in V:  # remaining N-K values to place
        # using bip. match. to find a valid set of positions for
        # all N values v at once
        graph = [[] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if Grid[i][j]==0:
                    graph[i].append(j)
        match = bip_match(graph, N, N)
        if any(u is None for u in match):
            return False
        for j,i in enumerate(match):
            Grid[i][j] = v
    return True

def main():
    global N, Grid
    N,K = map(int, input().split())
    Grid = [list(map(int, input().split())) for _ in range(N)]
    if latin(Grid):
        print('YES')
        print('\n'.join(' '.join(map(str,L)) for L in Grid))
    else:
        print('NO')

main()
