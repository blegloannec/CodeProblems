#!/usr/bin/env python3

from math import gcd

N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

# double area
A = sum(P[i-1][0]*P[i][1] - P[i][0]*P[i-1][1] for i in range(N))

# boundary points (NB: gcd() is ok with negative values)
B = sum(gcd(P[i-1][0]-P[i][0], P[i-1][1]-P[i][1]) for i in range(N))

# Pick's theorem
print((A+2-B)//2)
