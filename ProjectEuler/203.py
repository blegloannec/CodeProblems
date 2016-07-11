#!/usr/bin/env python

from math import sqrt
import random
random.seed()
from collections import defaultdict
from fractions import gcd

def sqrfree(decomp):
    for p in decomp:
        if decomp[p]>1:
            return False
    return True

# Miller-Rabin
def digits(n,b=10):
    c = []
    while n>0:
        c.append(n%b)
        n /= b
    return c

def witness(a,n):
    b = digits(n-1,2)
    d = 1
    for i in xrange(len(b)-1,-1,-1):
        x = d
        d = (d*d)%n
        if d==1 and x!=1 and x!=n-1:
            return True
        if b[i]==1:
            d = (d*a)%n
    return d!=1

def miller_rabin(n,s=15):
    for j in xrange(s):
        if witness(random.randint(1,n-1),n):
            return False
    return True

# Pollard's rho (remove powers of 2 before)
def pollard_rho(n):
    l = set()
    c = random.randint(1,n-1)
    f = (lambda x: (x*x+c)%n)
    x = random.randint(0,n-1)
    y = x
    x = f(x)
    y = f(f(y))
    while x!=y:
        p = gcd(n,abs(x-y))
        if 1<p<n:
            return p
        x = f(x)
        y = f(f(y))
    return None

def factorisation(n, D):
    while n>1:
        if miller_rabin(n):
            D[n] += 1
            return D
        f = pollard_rho(n)
        if f!=None:
            factorisation(f,D)
            n /= f
    return D

# MAIN
def main():
    N = 51
    T = [[0 for _ in xrange(N)] for _ in xrange(2)]
    T[0][0] = T[1][0] = 1
    s = set([1])
    for i in xrange(1,N):
        for j in xrange(1,i+1):
            T[i%2][j] = T[(i-1)%2][j-1]+T[(i-1)%2][j]
            n = T[i%2][j]
            m = 0
            while n%2==0:
                n /= 2
                m += 1
            if m<2 and sqrfree(factorisation(n,defaultdict(int))):
                s.add(T[i%2][j])
    print sum(s)

main()
