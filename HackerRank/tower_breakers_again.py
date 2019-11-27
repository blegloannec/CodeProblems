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
    # XOR_{n/d} grundy(d) = grundy(d) if n/d odd else 0
    X = set(grundy(d) if (n//d)%2==1 else 0 for d in range(1,n) if n%d==0)
    return mex(X)

# we discover that the Grundy function is the number of odd prime factors
# counted with multiplicity (i.e. non necessarily distinct)
# + 1 for even numbers (~ factors 2 counted only once)

def sieve_grundy(N=10**5+1):
    G = [0]*N
    for k in range(2,N,2):
        G[k] = 1
    for p in range(3,N):
        if G[p]==0:
            q = p
            while q<N:
                for k in range(q,N,q):
                    G[k] += 1
                q *= p
    return G

def main():
    G = sieve_grundy()
    T = int(input())
    for _ in range(T):
        N = int(input())
        H = map(int,input().split())
        g = 0
        for h in H:
            g ^= G[h]
        print(2 if g==0 else 1)

main()
