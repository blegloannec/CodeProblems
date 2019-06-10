#!/usr/bin/env python3

# Greedy approach cutting in decreasing order of cost
# (here implemented in reverse, merging in increasing order)
# It's obvious that doing all the cuts along the same direction
# in decreasing order is optimal, let us prove it's also optimal
# when considering the two types of cuts all together.
# Let us consider an order of operations and an index i such that:
#  - cuts i and i+1 have different directions, say i is H and i+1 is V;
#  - Cost(i) < Cost(i+1).
# Then if we denote as Hi and Vi the numbers of H and V cuts before i,
# the contribution of cuts i and i+1 to the score is
#   A = Cost(i)*Vi + Cost(i+1)*(Hi+1)
# and swapping i and i+1 gives a contribution of
#   B = Cost(i+1)*Hi + Cost(i)*(Vi+1)
# As B-A = Cost(i)-Cost(i+1) < 0, the current order is not optimal.

MOD = 10**9+7

Q = int(input())
for _ in range(Q):
    Size = list(map(int,input().split()))
    Cost =  [(int(c),0) for c in input().split()]
    Cost += [(int(c),1) for c in input().split()]
    Cost.sort()
    res = 0
    for c,d in Cost:
        res += c * Size[d^1]
        res %= MOD
        Size[d] -= 1
    print(res)
