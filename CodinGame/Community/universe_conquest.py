#!/usr/bin/env python3

# Minimum weight bipartite vertex cover
# TODO: NP-hard or not??
#   Consider the following:
#    http://tryalgo.org/en/matching/2016/08/05/konig/
#    https://en.wikipedia.org/wiki/K%C5%91nig%27s_theorem_(graph_theory)

def subset_weight(subset):
    w = i = 0
    while subset:
        if subset&1:
            w += Weight[i]
        i += 1
        subset >>= 1
    return w

MinWeight = float('inf')
def backtrack(used=0, weight=0, i=0):
    global MinWeight
    if weight<MinWeight:
        if i==P:
            MinWeight = weight
        elif used&(1<<i) or used&Neigh[i]==Neigh[i]:
            backtrack(used, weight, i+1)
        else:
            backtrack(used|(1<<i), weight+Weight[i], i+1)
            backtrack(used|Neigh[i], weight+subset_weight(Neigh[i]^(Neigh[i]&used)), i+1)

if __name__=='__main__':
    P,H = map(int,input().split())
    Subset, Weight = zip(*(input().split() for _ in range(P)))
    Weight = list(map(int,Weight))
    Neigh = [0]*P
    for _ in range(H):
        A,B = map(int,input().split())
        A -= 1
        B -= 1
        if Subset[A]!=Subset[B]:
            Neigh[A] |= 1<<B
            Neigh[B] |= 1<<A
    backtrack()
    print(MinWeight)
