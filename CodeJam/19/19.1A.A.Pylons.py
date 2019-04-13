#!/usr/bin/env pypy2

# Looking for an hamiltonian path in a grid with specific move constraints
# (see also https://en.wikipedia.org/wiki/Ore%27s_theorem )
# There is no elegant trick here, a randomized backtracking was actually
# the expected approach.

import random
random.seed()

# randomized backtracking
def rand_search(u=-1, i=0):
    if i==S:
        return True
    if i==0:
        V = range(S)
    else:
        V = [v for v in G[u] if not Used[v]]
    random.shuffle(V)
    for v in V:
        Used[v] = True
        Path.append(v)
        if rand_search(v,i+1):
            return True
        Path.pop()
        Used[v] = False
    return False

def case():
    global S, G, Used, Path
    S = R*C
    G = [[] for _ in xrange(S)]
    for i in xrange(R):
        for j in xrange(C):
            for x in xrange(R):
                for y in xrange(C):
                    if i!=x and j!=y and i-j!=x-y and i+j!=x+y:
                        G[i*C+j].append(x*C+y)
    Used = [False]*S
    Path = []
    return rand_search()

if __name__=='__main__':
    T = int(raw_input())
    for t in xrange(1,T+1):
        R,C = map(int,raw_input().split())
        if not case():
            print 'Case #%d: IMPOSSIBLE' % t
        else:
            print 'Case #%d: POSSIBLE' % t
            for u in Path:
                x,y = divmod(u,C)
                print x+1, y+1
