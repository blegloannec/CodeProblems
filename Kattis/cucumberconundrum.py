#!/usr/bin/env python3

# https://en.wikipedia.org/wiki/Circle_packing_in_a_circle

from math import sqrt

# Diam[i] is the min diameter of a circle enclosing i unit circles
Diam = [0., 1., 2., 1.+2./sqrt(3.), 1.+sqrt(2.), 1.+sqrt(2.+2./sqrt(5.)), 3., 3.]

s, r, n, z = input().split()
s = float(s)
r = float(r)
n = int(n)
z = int(z)

d = s/r
a = 100.*(r/s)**2
while not (a*n<=z and d>=Diam[n]):
    n -= 1
print(n)
