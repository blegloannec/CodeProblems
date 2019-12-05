#!/usr/bin/env python3

from functools import lru_cache

@lru_cache(maxsize=None)
def binom(n,p):
    return 1 if p==0 else n*binom(n-1,p-1)//p

# integer weak compositions (weak: components can be 0)
# compo(s,n) = nb of ways to give a total rating s with n critics
def compo(n,p):
    return binom(n+p-1,p-1)

def count(R):
    N = len(R)
    S = sum(R)
    # counting ratings of sum < S
    res = sum(compo(s,N) for s in range(S))
    # counting ratings < R of sum exactly S
    sr = 0
    for i in range(N-1):
        n = N-(i+1)
        # ratings < R of sum S that coincide with R[:i]
        for r in range(R[i]):
            res += compo(S-(sr+r),n)
        sr += R[i]
    return res+1  # +1 for R itself

def main():
    while True:
        R = list(map(int,input().split()))
        if R[0]<=0:
            break
        print(count(R[1:]))

main()
