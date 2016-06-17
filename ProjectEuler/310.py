#!/usr/bin/env python

from math import sqrt

N = 100001
#N = 30

def mex(succ):
    i = 0
    while i in succ:
        i += 1
    return i

G = [-1 for _ in xrange(N)]
G[0] = 0
def grundy(n):
    if G[n]>=0:
        return G[n]
    succ = set()
    s = int(sqrt(n))
    for k in xrange(1,s+1):
        succ.add(grundy(n-k*k))
    g = mex(succ)
    G[n] = g
    return g

def main():
    # valeur max prise par la fonction de grundy : 74
    GMAX = 75
    invG = [[] for _ in xrange(GMAX)]
    for i in xrange(N):
        invG[grundy(i)].append(i)
    # Calcul des T[y][k] le nb de x<=y tels que
    # grundy(x)^grundy(y) = k
    # en O(N * GMAX^2)
    T = [[0 for _ in xrange(GMAX)] for _ in xrange(N)]
    for gx in xrange(GMAX):
        Vx = invG[gx]
        for gy in xrange(GMAX):
            gz = gx^gy
            if gz>=GMAX:
                continue
            # on exploite le fait que les invG[.] sont triees
            ix = 0
            for y in invG[gy]:
                while ix<len(Vx) and y>=Vx[ix]:
                    ix += 1
                T[y][gz] += ix
    # propagation des sommes
    for i in xrange(1,N):
        for k in xrange(GMAX):
            T[i][k] += T[i-1][k]
    # T[i][k] contient le nb de couples x<=y<=i tels que
    # grundy(x)^grundy(y) = k
    cpt = 0
    for z in xrange(N):
        cpt += T[z][grundy(z)]
    print cpt

main()
