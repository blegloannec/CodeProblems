#!/usr/bin/env python

from math import sqrt
from fractions import gcd

# "mauvaise" factorisation
def decomp(n):
    F = []
    m = 0
    while n%2==0:
        n /= 2
        m += 1
    if m>0:
        F.append((2,m))
    i = 3
    s = int(sqrt(n))+1
    while n>1 and i<s:
        m = 0
        while n%i==0:
            n /= i
            m += 1
        if m>0:
            F.append((i,m))
        i += 2
    if n>1:
        F.append((n,1))
    return F

def eulerphi(n):
    res = 1
    for (p,m) in decomp(n):
        res *= (p-1)*p**(m-1)
    return res

# Th d'Euler : si a et n pee alors a^phi(n) = 1 mod n
# donc a^x = a^(x%phi(n)) mod n

def hypexpmod(a,k,m):
    if k==1:
        return a%m
    if m==1:
        # permet de s'arreter des que les phi(m) iteres
        # atteignent 1 (des 24 pour m=10**8, au lieu de 1855)
        return 0
    assert(gcd(a,m)==1)
    return pow(a,hypexpmod(a,k-1,eulerphi(m)),m)

print hypexpmod(1777,1855,10**8)
