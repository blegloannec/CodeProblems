#!/usr/bin/env python3

from itertools import combinations
from functools import reduce
from operator import mul

N,K = map(int,input().split())
P = list(map(int,input().split()))

# inclusion-exclusion in O(2^K)
cnt = 0
for k in range(1,K+1):
    for T in combinations(P,k):
        cnt += (2*(k%2)-1) * (N//reduce(mul,T))
print(cnt)
