#!/usr/bin/env python3

n = int(input())
S = list(map(int,input().split()))

L = {}
for i in range(n):
    if S[i]-1 in L:
        L[S[i]] = L[S[i]-1]+1
    elif S[i] not in L:
        L[S[i]] = 1
l,x = max((L[x],-x) for x in L)
x = -x
print(*range(x-l+1,x+1))
