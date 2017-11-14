#!/usr/bin/env python

B = 10
N = 1<<B

def f(P):  # DP O(P * 2^B)
    C = [0]*N
    # init : nb ayant 1 chiffre
    for i in xrange(1,B):
        C[1<<i] = 1
    S = C[:]
    for k in xrange(2,P+1):
        C0 = [0]*N
        for s in xrange(N):
            for a in xrange(B):
                C0[s|(1<<a)] += C[s]
        C = C0
        # C[m] contient les nb ayant exactement k chiffres utilisant
        # exactement les chiffres indiques par le bitmask m
        for s in xrange(N):
            S[s] += C[s]
        # S la somme cumulee des C consecutifs (idem que C pour les
        # nb ayant <= k chiffres)
    res = 0
    for a in xrange(2,N):
        res += S[a]*(S[a]-1)/2
        for b in xrange(a+1,N):
            if a&b!=0:
                res += S[a]*S[b]
    return res

print(f(18) % 1000267129)
