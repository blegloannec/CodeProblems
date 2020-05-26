#!/usr/bin/env pypy

# For any fixed direction, you get a set of aligned points chains
# and the best tour you can do only depends on the sizes of these chains.
# Clearly, isolated points (singleton chains) can only be visited as
# first and last element.
# Even chains are trivial to visit (consider them as a bunch of disjoint
# pairs of successive points and link these pairs with wormholes to visit
# all the points and leave freely).
# Note that the 4th example gives a widget to visit and leave freely
# 2 chains of size 3:
#    1 -- 2 -- 3   by linking 2-5 and 6-4 and entering in 1, we visit
#    4 -- 5 -- 6   1,2,5,6,4,5,2,3 in order and leave freely
# Odd chains (of size >= 3 > 1) can be decomposed into an even chain +
# a chain of size 3. Hence if there are an even number of odd chains, then
# we can pair the 3-chains using the widget and visit everything.
# If there is an odd number of odd chains, then there is an odd number of
# non-isolated points. But then it is not possible to end with an isolated
# point while still visiting every vertex since this would require to
# have an even number of points in between: Wormholes form a perfect matching
# of all visited points in this case. Hence we cannot do better than
# considering the extra odd chain as an even chain + an isolated point.
# This gives us the answer in all possible cases.

import sys
from collections import Counter
input = sys.stdin.readline

def main():
    T = int(input())
    for t in xrange(1,T+1):
        N = int(input())
        P = [tuple(map(int, input().split())) for _ in range(N)]
        res = 1
        for i in xrange(N):
            xi,yi = P[i]
            for j in xrange(i+1,N):
                xj,yj = P[j]
                a = yj-yi
                b = xi-xj
                # lines ax + by = c
                C = Counter(a*x+b*y for x,y in P)
                isolated = sum(1 for c in C.values() if c==1)
                path = N - isolated
                path += min((2 if path%2==0 else 1), isolated)
                res = max(res, path)
        sys.stdout.write('Case #%d: %d\n' % (t,res))

main()
