#!/usr/bin/env python3

# kinda poor greedy approach
# definitely not the shortest way to solve that pb, yet good enough

N = int(input())
X = list(map(int,input().split()))
l,r = 0,N-1
swap = 0
while l<r:
    while l<r and X[l]==1:
        l += 1
    while l<r and X[r]==0:
        r -= 1
    if l<r:
        X[l],X[r] = X[r],X[l]
        swap += 1
print(swap)
