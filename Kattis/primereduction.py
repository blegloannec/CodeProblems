#!/usr/bin/env python3

from functools import lru_cache

def sieve(N):
    P = [True]*N
    for p in range(2,N):
        if P[p]:
            for k in range(2*p,N,p):
                P[k] = False
    return [p for p in range(2,N) if P[p]]

P = sieve(31622)

@lru_cache(maxsize=None)
def step(N):
    n = N
    res = 0
    for p in P:
        if p*p>n:
            break
        while n%p==0:
            res += p
            n //= p
    if n==N: # prime
        return -1
    if n>1:
        res += n
    return res

def red(n):
    m = step(n)
    c = 1
    while m!=-1:
        n,m = m,step(m)
        c += 1
    return (n,c)

def main():
    while True:
        n = int(input())
        if n==4:
            break
        print(*red(n))

main()
