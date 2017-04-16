#!/usr/bin/env python3

# as there is always a solution, the tree must have
# an even number of vertices
# the maximal decomposition is actually unique: simply remove
# all the edges that split the tree into 2 even subtrees
# those picks are obviously compatible
# it's maximal as an edge that split into 2 odd subtrees
# is obviously not a valid pick

# algo in O(N) by DFS
# even child subtree => remove the edge

def size(G,u=0,u0=None):
    s,e = 1,0
    for v in G[u]:
        if v!=u0:
            sv,ev = size(G,v,u)
            s += sv
            e += ev
            if sv%2==0: # remove the edge
                e += 1
    return s,e

def main():
    N,M = map(int,input().split())
    # It's a tree, so M = N-1, great input specifications!
    # Also, the problem statement mentions that the tree "is
    # rooted at node 1", which is completely irrelevant!
    # Moreover, the N <= 100 bound is way too low.
    G = [[] for _ in range(N)]
    for _ in range(M):
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    print(size(G)[1])

main()
