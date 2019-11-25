#!/usr/bin/env python3

from functools import lru_cache

LPar, RPar = '([{', ')]}'

@lru_cache(maxsize=None)
def count(l,r):
    #assert l<=r and (r-l)%2==0
    if l==r:
        return 1
    if S[l] in RPar:
        return 0
    rpar = None
    if S[l] in LPar:
        rpar = RPar[LPar.index(S[l])]
    res = 0
    for m in range(l+1,r,2):
        if S[m]=='?' or S[m]==rpar or (rpar is None and S[m] in RPar):
            res += (3 if S[l]==S[m]=='?' else 1) * count(l+1,m) * count(m+1,r)
    return res

def main():
    global S
    N = int(input())
    S = input()
    print(str(count(0,N))[-5:])  # /!\ leave the leading 0s if any!

main()
