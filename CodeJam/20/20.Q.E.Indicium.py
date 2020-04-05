#!/usr/bin/env pypy

# A few basic preliminary remarks:
#  - Any lines/columns permutation of a latin square is a latin square.
#    This allows in particular to reorder the diagonal arbitrarily.
#  - Any values permutation of a latin square is a latin square.
#    In particular the symmetry x <-> N+1-x acts on the trace t <-> N^2+N-t.
#  - If the diagonal contains N-1 times the value x then the last value has
#    to be x too, otherwise the column/line of this value could not contain x.
#    In particular, t = N+1 = (N-1)*1 + 2 is an impossible trace, as well
#    as its symmetric t = N^2-1.
#    For the same reason, the particular case of N = 3 & K = 5 = 1+1+3 = 1+2+2
#    is also impossible, as well as its symmetric K = 7.
#    These are the only impossible cases.
# The first two remarks would allow to build lots of latin squares from a
# basic circulant one. Yet the approach we use below is different:
#  - We use a line-by-line bipartite matching approach to complete a
#    latin square given its diagonal (whenever possible);
#  - For every possible case, we randomly generate diagonals of the required
#    sum until we find one that can be successfully completed.

import sys, random
random.seed()


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
    for u in xrange(nU):
        augment(u, bigraph, [False]*nV, match)
    return match
### ===== ###


# completing a Latin square (knowing the diagonal, here)
# line-by-line using bipartite matching
# (recycled from Kattis/superdoku.py)
def latin_diag(N, Diag):
    Diag = [d-1 for d in Diag]
    Grid = []
    Avail = [set(xrange(N)) for j in xrange(N)]
    for j,d in enumerate(Diag):
        Avail[j].remove(d)
    for i in xrange(N):
        graph = [[v for v in S if v!=Diag[i]] for S in Avail]
        graph[i] = [Diag[i]]
        match = bip_match(graph, N, N)
        if any(u is None for u in match):
            return None
        new_line = [None]*N
        for v,u in enumerate(match):
            new_line[u] = v+1
            Avail[u].discard(v)
        Grid.append(new_line)
    return Grid

# randomly generates a diagonal of sum K
def random_diag(N, K):
    Diag = [1]*N
    R = K-N
    while R>0:
        i = random.randint(0,N-1)
        if Diag[i]<N:
            v = random.randint(1, min(N-Diag[i], R))
            Diag[i] += v
            R -= v
    return Diag

def main():
    T = int(raw_input())
    for t in xrange(1,T+1):
        N,K = map(int,raw_input().split())
        if K==N+1 or K==N*N-1 or (N==3 and (K==5 or K==7)):
            # impossible cases
            print 'Case #%d: IMPOSSIBLE' % t
        else:
            # randomly generate a diagonal of sum K until the latin square
            # is completable (almost always takes <=5 tries, usually <=2)
            M = latin_diag(N, random_diag(N,K))
            while M is None:
                M = latin_diag(N, random_diag(N,K))
            print 'Case #%d: POSSIBLE' % t
            print '\n'.join(' '.join(map(str,L)) for L in M)

main()
