#!/usr/bin/env python

def dp():
    N,M,P = 250250,250,10**16
    NB = [[0 for _ in xrange(M)] for _ in xrange(N+1)]
    NB[0][0] = 1
    for n in xrange(N+1):
        x = pow(n,n,M)
        for s in xrange(M):
            # not using x
            NB[n][s] = (NB[n][s]+NB[n-1][s])%P
            # using x
            NB[n][(s+x)%M] = (NB[n][(s+x)%M]+NB[n-1][s])%P
    return NB[N][0]-1 # -1 to remove empty set

print dp()
