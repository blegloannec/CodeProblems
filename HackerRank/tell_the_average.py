#!/usr/bin/env python3

# the value is the same for every permutation and is actually
# (L[0]+1)*(L[1]+1)*...*(L[n-1]+1) - 1
# (easy seen by induction)

P = 10**9+7

N = int(input())
L = list(map(int,input().split()))
res = 1
for x in L:
    res = (res*(x+1)) % P
res = (res-1)%P
print(res)
