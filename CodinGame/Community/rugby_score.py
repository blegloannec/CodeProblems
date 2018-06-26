#!/usr/bin/env python3

# poor usual number combination problem, we do not bother doing the proper DP
# then climb back here to enumerate solutions (so we do not benefit from
# memoization, still it is way good enough considering the tiny input size)

P = [5,2,3]
S = [0,0,0]
def combin(n,i=0):
    if i==3:
        if n==0:
            yield S
    else:
        k = 0
        while k*P[i]<=n and (i!=1 or k<=S[0]):
            S[i] = k
            yield from combin(n-k*P[i],i+1)
            k += 1

n = int(input())
for C in combin(n):
    print(*C)
