#!/usr/bin/env python

import sys
from math import sqrt

# x > y > z > 1
# let A = x+y, B = x+z, C = y+z, all squares
# A > B > C
# then x-y = B-C, x-z = A-C, y-z = A-B, all squares too
# 2x = A+B-C, 2y = A-B+C, 2z = -A+B+C, all even and positive
# B+C > A

# clearly, if x,y,z is a valid triplet, then so are the x*t^2,y*t^2,z*t^2

def is_sqr(n):
    s = int(sqrt(n))
    return s*s==n

def gen(N=1000):
    for c in xrange(1,N):
        C = c*c
        for b in xrange(c+1,N):
            B = b*b
            for a in xrange(b+1,int(sqrt(B+C))+1):
                A = a*a
                if (A+B-C)%2==0 and (A-B+C)%2==0 and (-A+B+C)%2==0 and is_sqr(B-C) and is_sqr(A-C) and is_sqr(A-B):
                    yield ((A+B-C)/2,(A-B+C)/2,(-A+B+C)/2)

def main_gen():
    for t in gen(10000):
        print t

T = [(434657, 420968, 150568),(733025, 488000, 418304),(3713858, 891458, 88642),
     (993250, 949986, 856350),(14438177, 1283048, 577448),(5320193, 1782032, 589568),
     (2843458, 2040642, 1761858),(2399057, 2288168, 1873432),(7640833, 4504392, 2465208)]

def main():
    N = int(sys.stdin.readline())
    M = 10**12
    cpt = 0
    for (x,y,z) in T:
        k = 1
        while k*k*x<=M:
            print k*k*x,k*k*y,k*k*z
            k += 1
            cpt += 1
            if cpt==N:
                return

# triples precomputation (for hardcoding):
#main_gen()

main()
