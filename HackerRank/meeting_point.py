#!/usr/bin/env python3

# Given some 2D points, find the point that minimizes the sum of chess-king
# distances (uniform norm) to all the other points.
# This would be easy with Manhattan distance as we could deal with both
# coordinates separately.
# Fortunately, if we turn the axis by pi/4:
#   P = (x,y) |--> Q = (a,b) = (x+y,x-y)
# then we have 2*Dinf(P0,P1) = D1(Q0,Q1)
#     2*max(|x0-x1|,|y0-y1|) = abs(a0-a1) + abs(b0-b1)
# hence we can use the Manhattan approach through this coordinate change.

N = int(input())
P = [tuple(map(int,input().split())) for _ in range(N)]
A = sorted((x+y,i) for i,(x,y) in enumerate(P))
B = sorted((x-y,i) for i,(x,y) in enumerate(P))
SA = sum(A[i][0]-A[0][0] for i in range(1,N))
SB = sum(B[i][0]-B[0][0] for i in range(1,N))
M = [0]*N
M[A[0][1]] += SA
M[B[0][1]] += SB
for i in range(1,N):
    SA += (A[i][0]-A[i-1][0])*(i-(N-i))
    SB += (B[i][0]-B[i-1][0])*(i-(N-i))
    M[A[i][1]] += SA
    M[B[i][1]] += SB
print(min(M)//2)
