#!/usr/bin/env python3

# Approach for the Test Set 1, i.e. F = S = 1.
# Clearly swaps are actually *profitable* iff:
#       both cells have distinct values (i.e. <=> 2 flips)
#   and                 the opposite values in the target
#                       (otherwise 1 flip is strictly better)
# Moreover, profitable swaps can be considered distinct as, if a cell
# is swapped twice, then it takes back its original color, hence it
# is equivalent to 2 flips: 1 on each of the other two swapped cells
# (and, by the way, one of the swaps must violate the second property above).
# Then observe the grid as a bipartite graph where we only keep the
# edges corresponding to profitable swaps. Maximizing the number of
# distinct profitable swaps (to minimize the number of remaining flips)
# is exactly equivalent to finding a maximum bipartite matching.

def aug(u,G,M,seen):
    for v in G[u]:
        if not seen[v]:
            seen[v] = True
            if M[v]==None or aug(M[v],G,M,seen):
                M[v] = u
                return True
    return False

def bip_match(G,Us,Vs):
    M = [None]*Vs
    for u in range(Us):
        aug(u,G,M,[False]*Vs)
    return M

def main():
    T = int(input())
    for t in range(1, T+1):
        H,W,F,S = map(int, input().split())
        assert F==S==1
        P0 = [input() for _ in range(H)]
        P1 = [input() for _ in range(H)]
        cost = 0
        N = H*W
        idx = lambda i,j: i*W+j
        G = [[] for _ in range(N)]
        for i in range(H):
            for j in range(W):
                if P0[i][j]!=P1[i][j]:
                    cost += 1
                    u = idx(i,j)
                    if j+1<W and P0[i][j+1]!=P0[i][j] and P0[i][j+1]!=P1[i][j+1]:
                        v = idx(i,j+1)
                        if (i^j)&1: G[u].append(v)
                        else:       G[v].append(u)
                    if i+1<H and P0[i+1][j]!=P0[i][j] and P0[i+1][j]!=P1[i+1][j]:
                        v = idx(i+1,j)
                        if (i^j)&1: G[u].append(v)
                        else:       G[v].append(u)
        M = bip_match(G, N, N)
        cost -= N - M.count(None)
        print(f'Case #{t}: {cost}')

main()
