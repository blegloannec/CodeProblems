#!/usr/bin/env python

# 20*9^2 = 1620 plus grande somme possible
# 40^2 <= 1620 <= 41^2

N,S,P = 20,1620,10**9

def dp():
    Som = [[0 for _ in xrange(S+1)] for _ in xrange(N+1)]
    Cpt = [[0 for _ in xrange(S+1)] for _ in xrange(N+1)]
    Cpt[0][0] = 1
    for n in xrange(1,N+1):
        for s in xrange(S+1):
            for c in xrange(10):
                if c*c>s:
                    break
                Som[n][s] = (Som[n][s] + Som[n-1][s-c*c] + c*pow(10,n-1,P)*Cpt[n-1][s-c*c])%P
                Cpt[n][s] += Cpt[n-1][s-c*c]
    print sum(Som[N][i*i] for i in xrange(1,41))%P

dp()
