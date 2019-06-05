#!/usr/bin/env python3

N = int(input())
A = sorted(map(int,input().split()))
L,R = map(int,input().split())

# O(N log N) approach here
# It's not hard to see that the result is either:
#    - one of the bounds L or R
# or - a middle value m between two consecutive values
#      of the sorted A, if m is in [L,R]

# Case of L
M, Dminmax = L, min(abs(L-a) for a in A)
# Middles
for i in range(N-1):
    m = (A[i]+A[i+1])//2
    if L<=m<=R and m-A[i]>Dminmax:
        M, Dminmax = m, m-A[i]
# Case of R
D = min(abs(R-a) for a in A)
if D>Dminmax:
    M, Dminmax = R, D
print(M)
