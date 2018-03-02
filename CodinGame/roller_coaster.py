#!/usr/bin/env python3

l,c,n = map(int,input().split())
G = [int(input()) for _ in range(n)]

# pre-computation to deal with each ride in O(1)
M = [0]*n
I = [0]*n
j = m = 0
for i in range(n):
    if i>0:
        m -= G[i-1]
    if j==i:
        m = G[i]
        j = (i+1)%n
    while j!=i and m+G[j]<=l:
        m += G[j]
        j = (j+1)%n
    I[i] = j
    M[i] = m

# accelerated simulation
i = d = 0
for _ in range(c):
    d += M[i]
    i = I[i]
print(d)
