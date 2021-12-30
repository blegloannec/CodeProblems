#!/usr/bin/env python3

import sys

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


def main():
    N,K = map(int,sys.stdin.readline().split())
    Grid = [list(map(int,sys.stdin.readline().split())) for _ in range(K)]
    Avail = [set(Grid[i][j]-1 for i in range(K)) for j in range(N)]
    if any(len(S)<K for S in Avail) or any(len(set(L))<N for L in Grid):
        sys.stdout.write('no\n')
    else:
        Avail = [set(range(N))-S for S in Avail]
        for _ in range(N-K):
            # simply using bip. match. to compute a new line compatible
            # with what we currently have
            graph = [list(S) for S in Avail]
            match = bip_match(graph, N, N)
            new_line = [None]*N
            for v,u in enumerate(match):
                new_line[u] = v+1
                Avail[u].remove(v)
            Grid.append(new_line)
        sys.stdout.write('yes\n')
        sys.stdout.write('\n'.join(' '.join(map(str,L)) for L in Grid))
        sys.stdout.write('\n')

main()
