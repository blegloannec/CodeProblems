#!/usr/bin/env python3

from math import log

# x^(ay^b) mod m
# si pgcd(x,m) = 1, x^((ay^b) mod phi(m)) mod m

def factor(n):  # good enough here
    D = []
    m = 0
    while n&1==0:
        m += 1
        n >>= 1
    if m>0:
        D.append((2,m))
    d = 3
    while d*d<=n:
        m = 0
        while n%d==0:
            m += 1
            n //= d
        if m>0:
            D.append((d,m))
        d += 2
    if n>1:
        D.append((n,1))
    return D

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
        X,A,Y,B,M = map(int,input().split())
        if B==0:
            Y = B = 1
        if A==0 or Y==0:
            res = 1 % M
        else:
            DM = factor(M)
            res,mod = 0,1
            for p,e in DM:
                pe = p**e
                x = 0
                if X%p==0:
                    if log(A)+B*log(Y) < log(e):
                        x = pow(X, A*Y**B, pe)
                else:
                    phi = (p-1)*pe//p
                    x = pow(X, (A*pow(Y,B,phi))%phi, pe)
                res = rev_chinois(res,mod,x,pe)
                mod *= pe
        print(res)

main()
