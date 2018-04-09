#!/usr/bin/env python3

from fractions import gcd

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
        a,n,b,m = map(int,input().split())
        x = rev_chinois(a,n,b,m)
        print(x,n*m)

main()
