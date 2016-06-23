#!/usr/bin/env python

from math import sqrt

# x > y > z > 1
# let A = x+y, B = x+z, C = y+z, all squares
# A > B > C
# then x-y = B-C, x-z = A-C, y-z = A-B, all squares too
# 2x = A+B-C, 2y = A-B+C, 2z = -A+B+C, all even and positive
# B+C > A

def is_sqr(n):
    s = int(sqrt(n))
    return s*s==n

def main():
    N = 1000
    vmin = 1<<31
    for c in xrange(1,N):
        C = c*c
        for b in xrange(c+1,N):
            B = b*b
            for a in xrange(b+1,int(sqrt(B+C))+1):
                A = a*a
                if (A+B-C)%2==0 and (A-B+C)%2==0 and (-A+B+C)%2==0 and is_sqr(B-C) and is_sqr(A-C) and is_sqr(A-B):
                    #print A+B-C,A-B+C,-A+B+C
                    vmin = min(vmin,(A+B+C)/2)
    print vmin

main()
