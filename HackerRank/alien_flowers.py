#!/usr/bin/env python3

P = 10**9+7

def inv_mod(n):
    return pow(n,P-2,P)

def binom_mod(n,p):
    if not 0<=p<=n:
        return 0
    res = 1
    for i in range(p):
        res = (res * (n-i) * inv_mod(p-i)) % P
    return res

def multiset(n,p):
    return binom_mod(n+p-1,p)

def formula(RR,RB,BB,BR):
    res = 0
    if abs(RB-BR)==1:
        S = max(RB,BR)
        # transitions RB and BR split the chain in S bins for R & S bins for B
        res = (multiset(S,RR)*multiset(S,BB)) % P
    elif RB==BR:
        if RB==0:        # no transitions
            if RR==BB==0:
                res = 2  # 2 words of size 1, "R" and "B"
            elif min(RR,BB)==0:
                res = 1  # "RR..R" or "BB..B"
        else:
            # depending on the starting color, transitions split the chain in
            #    RB+1 bins for R & RB bins for B
            # or the symmetric
            res = (multiset(RB+1,RR)*multiset(RB,BB) + multiset(RB,RR)*multiset(RB+1,BB)) % P
    return res

RR,RB,BB,BR = map(int,input().split())
print(formula(RR,RB,BB,BR))
