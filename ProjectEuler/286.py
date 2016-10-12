#!/usr/bin/env python

# really easy one!

# DP to compute the proba for a given q
P = []
def dp(q,n=50,p=20):
    if P[n][p]>=0.:
        return P[n][p]
    P[n][p] = (n/q)*dp(q,n-1,p)+(1.-n/q)*dp(q,n-1,p-1)
    return P[n][p]

def prob(q):
    global P
    # init
    P = [[-1. for _ in xrange(21)] for _ in xrange(51)]
    P[0][0] = 1.
    for n in xrange(1,51):
        P[n][0] = (n/q)*P[n-1][0]
    for p in xrange(1,21):
        P[0][p] = 0.
    # dp
    return dp(q)

# dicho search of q for a given target proba x
def dicho(x):
    a,b = 51.,53.
    m0,m = 0.,1.
    while m0!=m:
        m0,m = m,(a+b)/2.
        if prob(m)>=x:
            a = m
        else:
            b = m
    print m

dicho(0.02)
