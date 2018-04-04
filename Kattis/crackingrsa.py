#!/usr/bin/env python3

from fractions import gcd

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a//b)*v)

def inv_mod(a,n):
    g,u,_ = bezout(a,n)
    assert(g==1)
    return u%n

def factor2(n):
    if n%2==0:
        return (2,n//2)
    d = 3
    while d*d<=n:
        if n%d==0:
            return (d,n//d)
        d += 2
    assert(False)

def main():
    T = int(input())
    for _ in range(T):
        n,e = map(int,input().split())
        p,q = factor2(n)
        phi = (p-1)*(q-1)
        d = inv_mod(e,phi)
        print(d)

main()
