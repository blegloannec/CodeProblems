#!/usr/bin/env python

from fractions import gcd

# we use Burnside's lemma to count modulo symmetries
# G a finite group acting on a finite set X
# fix(g) = {x in X / g.x = x}
# |X/G| = 1/|G| * sum( |fix(g)|, g in G )
# here X is the set of colorings of the pizzas (including rotations)
# G is the group of rotations
# X/G is the set of colorings modulo rotations
# fix(g) is the set of colorings that are periodic of "period" g
# for f(m,n), such g can only be a multiple of m, ie m <= a*m <= n*m
# in which case the actual minimal corresponding period is
# gcd(a*m,n*m) = m*gcd(a,n)

def binom(n,p):
    return 1 if p==0 else n*binom(n-1,p-1)/p

# m>=2, n>=1
def f(m,n):
    res = 0
    for a in xrange(1,n+1):
        # period a*m
        d = gcd(a,n)
        # actual minimal period d*m
        nb = 1
        # counting colorings of the minimal period
        for k in xrange(m-1):
            nb *= binom((m-k)*d,d)
        res += nb
    return res/(n*m)

def main():
    N = 10**15
    s = 0
    for m in xrange(2,100):
        for n in xrange(1,100):
            v = f(m,n)
            if v>N:
                break
            s += v
    print s

main()
