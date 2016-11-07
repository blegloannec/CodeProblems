#!/usr/bin/env python

import sys

# we simply want to count the number of iterations of the loop nest 
# an iteration is determined by 1 <= i1 < i2 < ... < ik <= n
# with i2-i1 >= 1, i3-i2 >= 2, i4-i3 >= 3, ...
# let us do a simple translation
# so let j1 = i1, j2 = i2 > j1, j3 = i3-1 > j2 with j2-j1 >= 1,
# j4 = i4-(1+2) >= i3 > j3 with j4-j3 >= 1,
# j5 = i5-(1+2+3) >= i4-2 > j4 with j5-j4 >= 1, etc
# so that an iteration is perfectly determined by
# 1 <= j1 < j2 < ... < jk <= n-(1+2+...+(k-2)) = n-(k-1)(k-2)/2
# the number of iterations is then binom(n-(k-1)(k-2)/2,k)

P = 10**9+7

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def inv_mod(a,n):
    _,u,_ = bezout(a,n)
    return u

def binom(n,p):
    if p>n:
        return 0
    res = 1
    while p>0:
        res = (((res*n)%P)*inv_mod(p,P))%P
        p -= 1
        n -= 1
    return res

def main():
    n,k = map(int,sys.stdin.readline().split())
    print binom(n-(k-1)*(k-2)/2,k)

main()
