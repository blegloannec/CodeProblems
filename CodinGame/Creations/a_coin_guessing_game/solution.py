#!/usr/bin/env python3

# - Seeing the possibilities as a bipartite graph, the solution must to be
#   its unique perfect matching.
#   If this graph had no cycle (a forest), we could build the solution
#   by a greedy iterated leaf-cutting process.
#   The given criterion informally suggests us that a leaf-cutting
#   (deduction) process will always break the cycles so that we are in an
#   equivalent situation as the ideal one.
#    [NB (harder to see, stated here without a proof): This approach actually
#     always works provided that the graph has a unique perfect matching.
#     The given criterion is only there to help the solver convince himself that this
#     rather natural deduction process will work).]
# - Of course, a maximum bipartite matching approach is also possible and passes here.
# - Some efficient enough backtracking can also probably pass...
# Anyway, there is no need to know/understand that much to solve the puzzle.

def leaves_elim(Pairs):
    M = len(Pairs)
    Q = [i for i in range(M) if len(Pairs[i])==1]
    Sol = [None]*M
    while Q:
        u = Q.pop()
        if Pairs[u]:
            assert len(Pairs[u])==1
            v = Pairs[u].pop()
            Sol[u], Sol[v] = v, u
            while Pairs[v]:
                w = Pairs[v].pop()
                if w!=u:
                    Pairs[w].remove(v)
                    if len(Pairs[w])==1:
                        Q.append(w)
    return Sol

def main():
    N,T = map(int,input().split())
    M = 2*N
    Pairs = [set(range(1-i%2,M,2)) for i in range(M)]
    for _ in range(T):
        Conf = [int(c)-1 for c in input().split()]
        Even, Odd = [], []
        for c in Conf:
            (Even if c%2==0 else Odd).append(c)
        for e in Even:
            for o in Odd:
                Pairs[e].discard(o)
                Pairs[o].discard(e)
    Sol = leaves_elim(Pairs)
    assert None not in Sol
    print(*(Sol[i]+1 for i in range(0,M,2)))

main()
