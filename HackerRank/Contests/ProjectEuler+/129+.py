#!/usr/bin/env python

import sys
from collections import defaultdict
from fractions import gcd
import random
random.seed()

# we want a fast way to compute A(n)
# the basic idea is that if gcd(n,10) = 1 then
# by Euler, 10^phi(9n) = 1 mod 9n
# hence 9n | 10^phi(9n)-1 = 99..9 phi(9n) times
# hence n | (10^phi(9n)-1)/9 = 11...1 phi(9n) times = R(phi(9n))
# hence A(n) | phi(9n)
# so, let us decompose 9n using Pollard's rho, deduce the decomposition
# of phi(9n), enumerate the divisors of phi(9n) and test them to return
# the smallest that works
# see also: http://math.stackexchange.com/questions/472404/repunit-divisibility


## Miller-Rabin
def digits(n,b=10):
    c = []
    while n>0:
        c.append(n%b)
        n /= b
    return c

def witness(a,n,b):
    d = 1
    for i in xrange(len(b)-1,-1,-1):
        x = d
        d = (d*d)%n
        if d==1 and x!=1 and x!=n-1:
            return True
        if b[i]==1:
            d = (d*a)%n
    return d!=1

def det_miller_rabin_64(n):
    b = digits(n-1,2)
    for w in [2,3,5,7,11,13,17,19,23,29,31,37]:
        if n==w:
            return True
        if witness(w,n,b):
            return False
    return True

## Pollard's rho
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

def factorisation(n,D):
    while n>1:
        if det_miller_rabin_64(n):
            D[n] += 1
            return D
        f = pollard_rho(n)
        if f!=None:
            factorisation(f,D)
            n /= f
    return D

def full_factorisation(n):
    D = defaultdict(int)
    while n%2==0:
        D[2] += 1
        n /= 2
    return factorisation(n,D)


## Code specifique au pb
# decomp de phi(9n)
def eulerphi9(n):
    D = full_factorisation(n)
    D[3] += 2
    Dphi = defaultdict(int)
    for p in D:
        if D[p]>1:
            Dphi[p] += D[p]-1
        Dpm1 = full_factorisation(p-1)
        for q in Dpm1:
            Dphi[q] += Dpm1[q]
    return Dphi

# generateur des diviseurs
def divisors(F,i=0):
    if i==len(F):
        yield 1
    else:
        p,m = F[i]
        f = 1
        for _ in xrange(m+1):
            for d in divisors(F,i+1):
                yield f*d
            f *= p

def main():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        n = int(sys.stdin.readline())
        D = eulerphi9(n)
        F = [(p,D[p]) for p in D]
        for d in sorted(divisors(F)):
            if pow(10,d,9*n)==1:
                print d
                break

main()
