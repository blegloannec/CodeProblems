#!/usr/bin/env python3

from math import atan2, pi

K = int(input())
N = int(input())
I0 = int(input())
Pt = [tuple(map(int,input().split())) for _ in range(K)]

anorm = lambda a: a if a>=0 else pi+a
angle = lambda i: lambda j: anorm(-atan2(Pt[j][1]-Pt[i][1], Pt[j][0]-Pt[i][0]))
Around = [sorted((j for j in range(K) if j!=i), key=angle(i)) for i in range(K)]
NextPiv = [{Around[i][j]: Around[i][(j+1)%(K-1)] for j in range(K-1)} for i in range(K)]

curr = I0
prev = Around[curr][-1]
init = (curr,prev)

Piv = [curr]
prev, curr = curr, NextPiv[curr][prev]
while len(Piv)<=N and (curr,prev)!=init:
    Piv.append(curr)
    prev, curr = curr, NextPiv[curr][prev]

Cnt = [0]*K
q,r = divmod(N+1,len(Piv))
for idx,i in enumerate(Piv):
    Cnt[i] += q + (idx<r)
print(Piv[r-1])
for i in range(K):
    print(Cnt[i])
