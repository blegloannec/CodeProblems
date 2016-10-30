#!/usr/bin/env python

import sys

# Let a < b < c be a prime pythagorean triple
# (ie. a^2+b^2 = c^2 and gcd(a,b) = 1)
# a < b < c "good" triple <=> d = b-a | c
# d^2 = (b-a)^2 = b^2 - 2ab + a^2 = c^2 - 2ab
# d^2 | c^2 = d^2 + 2ab, hence d^2 | 2ab
# assume d>1 and let p be a prime factor of d
#   p^2 | 2ab, hence p | ab
#   ab = a(a+d) = a^2 + ad and p | d, so p | a^2, then p | a
#   ab = (b-d)b = b^2 + bd, then p | b
#   which contradicts the fact that a is coprime with b
# hence d = 1 and b = a+1

# a < b < c "good" triple <=> b-a = 1
# a^2 + (a+1)^2 = c^2
# 2a^2 + 2a + 1 = c^2
# multiply the equation by 2
# (2a+1)^2 + 1 = 2c^2
# let A = 2a+1
# A^2 - 2c^2 = -1, negative Pell equation (see pb 100)!

def compte(L):
    x0,y0 = 1,1
    x,y = x0,y0
    cpt = 0
    while True:
        x,y = x0*x + 2*y0*y, x0*y + y0*x
        if x*x-2*y*y==-1 and x%2==1:
            l = x+y
            if l>=L:
                break
            cpt += (L-1)/l
    return cpt

def main():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        print compte(int(sys.stdin.readline()))

main()
