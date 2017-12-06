#!/usr/bin/env python3

I = list(map(int,input().split()))
N = len(I)

K = tuple(I)
S = {}
cpt = 0
while K not in S:
    S[K] = cpt
    i = I.index(max(I))
    q,r = divmod(I[i],N)
    I[i] = 0
    for j in range(N):
        I[(i+j+1)%N] += q + int(j<r)
    K = tuple(I)
    cpt += 1
print(cpt)       # Part 1
print(cpt-S[K])  # Part 2
