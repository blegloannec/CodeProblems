#!/usr/bin/env python3

# The order of the edges does not matter (it's easy to swap 2 consecutive
# edges without changing the area by symmetrizing the triangle formed
# by these two edges and the diagonal linking them).
# It's not hard to figure out that the answer is obtained by inscribing the
# polygon into a circle and to derive a formula for the optimal from there.
# However, to avoid to deal with the geometry, we use a ternary search on
# the diagonal here.

from math import sqrt

EPS = 1e-9

# https://en.wikipedia.org/wiki/Heron's_formula
def heron(a, b, c):
    s = (a+b+c)/2.
    return sqrt(s*(s-a)*(s-b)*(s-c))
    
def main():
    a,b,c,d = map(float, input().split())
    area = lambda diag: heron(a,b,diag) + heron(c,d,diag)
    l, r = max(abs(a-b),abs(c-d)), min(a+b,c+d)
    while r-l>EPS:
        m1 = (2.*l+r)/3.
        m2 = (l+2.*r)/3.
        a1 = area(m1)
        a2 = area(m2)
        if a1<a2:
            l = m1
        else:
            r = m2
    print(area(l))

main()
