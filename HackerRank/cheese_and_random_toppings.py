#!/usr/bin/env python3

from functools import lru_cache

# "M is squarefree and its prime factors are less than 50"
def factor(n):
    if n&1==0:
        n >>= 1
        yield 2
    d = 3
    while d*d<=n:
        if n%d==0:
            n //= d
            yield d
        d += 2
    if n>1:
        yield n

@lru_cache(maxsize=None)
def binom(n,p):
    if p>n:
        return 0
    return 1 if p==0 else n*binom(n-1,p-1)//p

def binom_lucas(n,k,p):
    res = 1
    while n>0 or k>0:
        n,a = divmod(n,p)
        k,b = divmod(k,p)
        res = (res * binom(a,b)) % p
    return res

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a//b)*v)

def rev_chinois(a,p,b,q):
    _,u,v = bezout(p,q)
    return (b*u*p+a*v*q)%(p*q)

def main():
    T = int(input())
    for _ in range(T):
        N,R,M = map(int,input().split())
        res,m = 0,1
        for p in factor(M):
            resp = binom_lucas(N,R,p)
            res = rev_chinois(res,m,resp,p)
            m *= p
        print(res)

main()
