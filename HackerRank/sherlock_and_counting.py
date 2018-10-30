#!/usr/bin/env python3

from math import *

# i*(n-i) <= nk
# i^2 - ni + nk >= 0
# D = n^2 - 4nk
# x0/1 = (n +/- sqrt(D)) / 2
# positive outside of [x0,x1]

def main():
    q = int(input())
    for _ in range(q):
        n,k = map(int,input().split())
        D = n*n-4*n*k
        res = n-1
        if D>0:
            d = sqrt(D)
            x0,x1 = (n-d)/2,(n+d)/2
            res = max(0,floor(x0)) + max(0,n-ceil(x1))
            # NB: both terms are actually equal as the equation/curve
            #     is symmetrical at n/2 in [0,n], or said otherwise
            #     is invariant by the substitution i <--> n-i,
            #     or again x0 = n-x1 (which is also obvious from the formula)
        print(res)

main()
