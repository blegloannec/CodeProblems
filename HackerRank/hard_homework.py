#!/usr/bin/env python3

from math import sin,cos

# O(N) approach (iterating over z, or technically x+y)
def max_sin(N):
    res = float('-inf')
    min_cos0, min_cos1 = max_cos0, max_cos1 = 1., cos(1./2.)
    for n in range(2,N):
        # maximize sin x + sin y for x+y = n, z = N-n
        # sin x + sin y = 2 sin (x+y)/2 cos (x-y)/2
        #               = 2 sin n/2 cos (2x-n)/2
        # assuming y <= x    < n   (without loss of generality)
        #          n <= 2x   < 2n
        #          0 <= 2x-n < n
        # i.e. 2x-n goes along all integers between 0 and n-2 having
        # the same parity as n
        # hence we simply need to maintain the min/max over x values
        # of cos (2x-n)/2 with increasing n
        s0 = 2.*sin(n/2.)
        s = s0 * (max_cos0 if s0>0 else min_cos0) + sin(N-n)
        res = max(res, s)
        # updating min/max cos
        c = cos(n/2.)
        min_cos1, min_cos0 = min(min_cos0,c), min_cos1
        max_cos1, max_cos0 = max(max_cos0,c), max_cos1
    return res

if __name__=='__main__':
    N = int(input())
    print('{:.9f}'.format(round(max_sin(N),9)))
