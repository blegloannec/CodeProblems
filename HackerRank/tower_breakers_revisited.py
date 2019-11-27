#!/usr/bin/env python3

from functools import lru_cache

def mex(X):
    x = 0
    while x in X:
        x += 1
    return x

@lru_cache(maxsize=None)
def grundy(n):
    if n<=1:
        return 0
    X = set(grundy(d) for d in range(1,n) if n%d==0)
    return mex(X)

# we discover that the Grundy function is the number of prime factors counted
# with multiplicity (i.e. non necessarily distinct)

def sieve_nb_factors(N=10**6+1):
    F = [0]*N
    for p in range(2,N):
        if F[p]==0:
            q = p
            while q<N:
                for k in range(q,N,q):
                    F[k] += 1
                q *= p
    return F

def main():
    F = sieve_nb_factors()
    T = int(input())
    for _ in range(T):
        N = int(input())
        H = map(int,input().split())
        g = 0
        for h in H:
            g ^= F[h]
        print(2 if g==0 else 1)

main()
