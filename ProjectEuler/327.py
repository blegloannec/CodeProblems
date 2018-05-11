#!/usr/bin/env pypy

# cout du depot de K cartes en R
def G(C,R,K):
    res = 0
    if K>C-R:  # allers-retours necessaires
        P = C-2*R
        if P<=0:
            return float('inf')
        L = K-(C-R)
        K = C-R
        AR = (L+P-1)//P  # nb d'allers-retours
        res += L + AR*2*R
    res += K+R  # dernier aller simple
    return res

memo = {}
def M(C,R):
    if R+1<=C:
        return R+1
    if (C,R) not in memo:
        memo[C,R] = min(G(C,r,M(C,R-r)) for r in xrange(1,min(C//2,R)+1))
    return memo[C,R]

print sum(M(C,30) for C in xrange(3,41))
