#!/usr/bin/env python

import sys,random
from math import sqrt
from fractions import gcd
from collections import defaultdict
random.seed()

# On remarque que x,y > 0 donc x,y > n
# On peut reecrire X = x-n > 0 et Y = y-n > 0
# 1/(X+n) + 1/(Y+n) = 1/n
# <=> n(2n+X+Y) = (X+n)(Y+n)
# <=> n^2 = XY
# On a dont autant de solutions (X,Y) que de diviseurs de n^2
# carre <=> nb impair de diviseurs
# Comme on veut eliminer la symetrie X/Y, il faut faire attention
# a la solution (n,n)
# nb sol = ((nb div de n^2)-1)/2 + 1

# Pollard's rho
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

def digits(n,b=10):
    c = []
    while n>0:
        c.append(n%b)
        n /= b
    return c

# Miller-Rabin
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

def miller_rabin(n,s=20):
    for j in xrange(s):
        if witness(random.randint(1,n-1),n):
            return False
    return True

def nb_div_n2(n):
    D = defaultdict(int)
    while n%2==0:
        D[2] += 1
        n /= 2
    F = factorisation(n,D)
    nb = 1
    for p in F:
        nb *= (2*F[p]+1)
    return nb

def nb_sol(n):
    return 1+(nb_div_n2(n)-1)/2

def main():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        N = int(sys.stdin.readline())
        print nb_sol(N)

main()
