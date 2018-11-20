#!/usr/bin/env python3

from math import sqrt,ceil

n = int(input())

## DP min-max O(n^2)
inf = float('inf')
P = [inf]*(n+1)
P[0] = P[1] = 0

def wc(n):
    if P[n]==inf:
        for i in range(2,n):
            P[n] = min(P[n],max(i,1+wc(n-i)))
    return P[n]

#print(wc(n))


## Closed formula
# A *strategy* is a sequence 0 < h0 < h1 < h2 < ... < h(k) = n
# of floors to test with the first egg until it breaks.
# If the first egg breaks at h(i), then we linearly test
# the interval ]h(i-1),h(i)[ with the second egg.
# The worst case complexity when we break at h(i) is
# exactly i+h(i)-h(i-1).
# Let x be the value of the optimal worst case (x is what we
# want to calculate) and let us build a strategy that realizes
# x as its worst case.
# We want i+h(i)-h(i-1) = x, i.e. h(i) = h(i-1)+x-i
# The first egg is dropped at h0 = x; then the second is
# dropped x-1 floors higher (-1 to take into account the h0 test),
# h(1) = 2x-1; the third one is dropped x-2 higher (-2 to take into
# account the h0 and h1 tests), h(2) = 3x-2; etc.
# n = h0-0 + h1-h0 + h2-h1 + ... = x + x-1 + x-2 + ... <= x(x+1)/2
# => The optimal x is the minimum x such that x(x+1)/2 >= n.

# x(x+1) >= 2n
# x^2 + x - 2n = 0
# -1+sqrt(1+8n) / 2

def formula(n):
    return int(ceil((-1+sqrt(1+8*n))/2))

print(formula(n))
