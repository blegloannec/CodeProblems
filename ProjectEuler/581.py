#!/usr/bin/env python

from heapq import *

# stupid technique, no idea of the upper bound...
# just pick the answer when it seems to stop finding new numbers
# (~20s with pypy)

# NB (a posteriori): see also
# https://en.wikipedia.org/wiki/St%C3%B8rmer's_theorem

P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
L = len(P)

# not so clever way of generating 47-smooth
def smooth():
    H = [1]
    S = set([1])
    while H:
        X = heappop(H)
        S.remove(X)
        yield X
        for i in xrange(len(P)):
            if X*P[i] not in S:
                heappush(H,X*P[i])
                S.add(X*P[i])

S = 0
last = 1
for x in smooth():
    if x==last+1:
        S += last
        print last,S
    last = x
