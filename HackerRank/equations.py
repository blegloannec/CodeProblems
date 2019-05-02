#!/usr/bin/env python3

# see also PE 108 & 110
# 1/x + 1/y = 1/n  (1)
# let X = x-n and Y = y-n
# (1) <=> 1/(X+n) + 1/(Y+n) = 1/n
#     <=> n(2n+X+Y) = (X+n)(Y+n)
#     <=> n^2 = XY
# hence the solutions are in bijection with the divisors of n^2
# for n = N! here

from collections import defaultdict

MOD = 1000007

def sieve_decomp_fact(N):
    N += 1
    P = [True]*N
    Decomp = defaultdict(int)
    for i in range(2,N):
        if P[i]:
            m = 1
            for k in range(2*i,N,i):
                P[k] = False
                l = k//i
                m += 1
                while l%i==0:
                    l //= i
                    m += 1
            Decomp[i] += m
    return Decomp

if __name__=='__main__':
    N = int(input())
    D = sieve_decomp_fact(N)
    res = 1
    for p in D:
        res = (res * (2*D[p]+1)) % MOD
    print(res)
